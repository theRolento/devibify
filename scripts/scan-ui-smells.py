"""Report conservative UI smell findings without modifying source files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Iterator


HTML_SUFFIXES = {".html", ".htm"}
COMPONENT_SUFFIXES = {".jsx", ".tsx", ".vue", ".svelte"}
JSX_SUFFIXES = {".jsx", ".tsx"}
CSS_SUFFIXES = {".css", ".scss", ".less"}
SUPPORTED_SUFFIXES = HTML_SUFFIXES | COMPONENT_SUFFIXES | CSS_SUFFIXES
EXCLUDED_DIRECTORIES = {".git", "node_modules", "dist", "build", ".next", ".nuxt", "coverage", "vendor", "__snapshots__"}
GENERATED_MARKERS = {"generated", "gen", "autogen"}
MAX_TAG_LENGTH = 4000

TAG_START_RE = re.compile(r"(?<![\w$)\].])<(?P<name>[A-Za-z][\w:.-]*)")
CLOSING_TAG_RE = re.compile(r"</[A-Za-z][\w:.-]*\s*>")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
BLOCK_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)
LINE_COMMENT_RE = re.compile(r"(?m)(?:^|(?<=\s))//.*$")
SCRIPT_BLOCK_RE = re.compile(r"<script\b[^>]*>(.*?)</script\s*>", re.IGNORECASE | re.DOTALL)
STYLE_BLOCK_RE = re.compile(r"<style\b[^>]*>(.*?)</style\s*>", re.IGNORECASE | re.DOTALL)
OUTLINE_RE = re.compile(r"outline\s*:\s*(?:none|0(?:px|rem|em)?)(?:\s*!important)?\s*(?:;|})", re.IGNORECASE)
HOVER_BLOCK_RE = re.compile(r"(?P<selector>[^{}\n]*:hover[^{}\n]*)\{(?P<body>[^{}]*)\}", re.IGNORECASE)
LAYOUT_PROPERTY_RE = re.compile(r"(?:^|;)\s*(?:width|height|margin(?:-[\w-]+)?|padding(?:-[\w-]+)?|top|right|bottom|left)\s*:", re.IGNORECASE)
DECLARATION_RE = re.compile(r"(?<![\w$@-])(?P<property>[A-Za-z][\w-]*)\s*:(?P<value>[^;{}]+)")
COLOR_RE = re.compile(r"(?<![\w-])(?:#[0-9a-fA-F]{3,8}\b|(?:rgb|hsl)a?\([^)]*\))")
PLACEHOLDER_COPY_RE = re.compile(r"(?i:lorem\s+ipsum)|\bTODO\b|\bFIXME\b")
INERT_HREF_RE = re.compile(r"javascript\s*:\s*(?:void\s*\(\s*0\s*\)\s*)?;?", re.IGNORECASE)
CLICK_HANDLERS = ("onclick", "@click", "v-on:click", "on:click")
KEY_HANDLER_PREFIXES = ("onkey", "@key", "v-on:key", "on:key")
SPREAD = "{...}"


@dataclass(order=True)
class Finding:
    path: str
    line: int
    column: int
    rule_id: str
    confidence: str
    category: str
    message: str
    suggested_inspection: str


@dataclass
class Tag:
    name: str
    start: int
    end: int
    attrs: dict[str, str | None]
    self_closing: bool


def position(text: str, offset: int) -> tuple[int, int]:
    line = text.count("\n", 0, offset) + 1
    previous = text.rfind("\n", 0, offset)
    return line, offset - previous


def mask(text: str, pattern: re.Pattern[str], group: int = 0) -> str:
    """Blank matched spans while preserving offsets and line breaks."""

    def blank(match: re.Match[str]) -> str:
        whole = match.group(0)
        start, end = match.start(group) - match.start(), match.end(group) - match.start()
        return whole[:start] + re.sub(r"[^\r\n]", " ", whole[start:end]) + whole[end:]

    return pattern.sub(blank, text)


def read_balanced(text: str, index: int) -> int:
    """Return the index just past the brace block that starts at index."""
    depth = 0
    quote = ""
    while index < len(text):
        char = text[index]
        if quote:
            if char == "\\":
                index += 1
            elif char == quote:
                quote = ""
        elif char in "\"'`":
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index + 1
        index += 1
    return len(text)


def parse_attrs(source: str) -> dict[str, str | None]:
    """Parse attributes; values are raw strings, None when valueless."""
    attrs: dict[str, str | None] = {}
    index = 0
    while index < len(source):
        char = source[index]
        if char.isspace() or char == "/":
            index += 1
            continue
        if char == "{":
            end = read_balanced(source, index)
            if source[index + 1 : end].lstrip().startswith("..."):
                attrs[SPREAD] = None
            index = end
            continue
        match = re.match(r"[^\s=/>{\"']+", source[index:])
        if not match:
            index += 1
            continue
        name = match.group(0).lower()
        index += match.end()
        while index < len(source) and source[index].isspace():
            index += 1
        if index >= len(source) or source[index] != "=":
            attrs.setdefault(name, None)
            continue
        index += 1
        while index < len(source) and source[index].isspace():
            index += 1
        if index < len(source) and source[index] in "\"'":
            quote = source[index]
            end = source.find(quote, index + 1)
            end = len(source) if end == -1 else end
            value = source[index + 1 : end]
            index = end + 1
        elif index < len(source) and source[index] == "{":
            end = read_balanced(source, index)
            value = source[index:end]
            index = end
        else:
            match = re.match(r"[^\s>]*", source[index:])
            value = match.group(0) if match else ""
            index += len(value)
        attrs.setdefault(name, value)
    return attrs


def literal(value: str | None) -> str | None:
    """Return a statically known attribute value, or None for dynamic values."""
    if value is None:
        return None
    if not value.startswith("{"):
        return None if re.search(r"[{}]|\$\{", value) else value
    inner = value[1:-1].strip()
    string = re.fullmatch(r"\"([^\"]*)\"|'([^']*)'|`([^`$]*)`", inner)
    if string:
        return next(group for group in string.groups() if group is not None)
    if re.fullmatch(r"[+-]?\d+", inner):
        return inner
    return None


def iter_tags(text: str) -> Iterator[Tag]:
    for match in TAG_START_RE.finditer(text):
        index = match.end()
        quote = ""
        limit = min(len(text), index + MAX_TAG_LENGTH)
        while index < limit:
            char = text[index]
            if quote:
                if char == quote:
                    quote = ""
            elif char in "\"'":
                quote = char
            elif char == "{":
                index = read_balanced(text, index)
                continue
            elif char == "<":
                break
            elif char == ">":
                source = text[match.end() : index]
                self_closing = source.rstrip().endswith("/")
                yield Tag(match.group("name"), match.start(), index + 1, parse_attrs(source), self_closing)
                break
            index += 1


def is_native(name: str, suffix: str) -> bool:
    return suffix in HTML_SUFFIXES or name[0].islower()


def finding(path: str, text: str, offset: int, rule_id: str, confidence: str, category: str, message: str, inspection: str) -> Finding:
    line, column = position(text, offset)
    return Finding(path, line, column, rule_id, confidence, category, message, inspection)


def markup_view(text: str, suffix: str) -> str:
    view = mask(text, HTML_COMMENT_RE)
    if suffix in JSX_SUFFIXES:
        view = mask(view, BLOCK_COMMENT_RE)
        view = mask(view, LINE_COMMENT_RE)
    else:
        view = mask(view, SCRIPT_BLOCK_RE, 1)
    return mask(view, STYLE_BLOCK_RE, 1)


def scan_markup(path: str, text: str, suffix: str) -> list[Finding]:
    findings: list[Finding] = []
    view = markup_view(text, suffix)
    all_tags = list(iter_tags(view))
    tags = [tag for tag in all_tags if is_native(tag.name, suffix)]
    ids: set[str] = set()
    duplicate_confidence = "high" if suffix in HTML_SUFFIXES else "medium"

    for tag in tags:
        name = tag.name.lower()
        attrs = tag.attrs
        spread = SPREAD in attrs
        offset = tag.start

        if name == "a":
            href = literal(attrs.get("href"))
            if href is not None and (href.strip() in {"", "#"} or INERT_HREF_RE.fullmatch(href.strip())):
                findings.append(finding(path, text, offset, "dead-href", "high", "functionality", "Link has an empty or inert literal destination.", "Confirm the destination and use a real link, or use a button for an action."))
            target = (literal(attrs.get("target")) or "").lower()
            rel_known = "rel" not in attrs or literal(attrs["rel"]) is not None
            rel = set((literal(attrs.get("rel")) or "").lower().split())
            if target == "_blank" and rel_known and not {"noopener", "noreferrer"} & rel and not spread:
                findings.append(finding(path, text, offset, "target-blank-no-rel", "low", "security-adjacent", "Literal target=_blank link has no noopener or noreferrer token.", "Modern browsers imply noopener; check the repository link policy, legacy browser support, and whether noreferrer is wanted."))

        if name == "meta" and (literal(attrs.get("name")) or "").lower() == "viewport":
            content = literal(attrs.get("content")) or ""
            if re.search(r"user-scalable\s*=\s*no", content, re.IGNORECASE) or re.search(r"maximum-scale\s*=\s*(?:0(?:\.0*)?|1(?:\.0*)?)(?:\s*[,;]|\s*$)", content, re.IGNORECASE):
                findings.append(finding(path, text, offset, "prevent-zoom", "high", "accessibility", "Viewport metadata disables or severely caps user zoom.", "Allow user scaling and verify zoom and reflow behavior."))

        if name == "img" and "alt" not in attrs and not spread:
            findings.append(finding(path, text, offset, "img-missing-alt", "high", "accessibility", "Literal image has no alt attribute.", "Provide meaningful alternative text or alt=\"\" for a decorative image."))
        if name == "iframe" and "title" not in attrs and not spread:
            findings.append(finding(path, text, offset, "iframe-missing-title", "high", "accessibility", "Literal iframe has no title attribute.", "Provide a concise title that identifies the embedded content."))

        element_id = literal(attrs.get("id"))
        if element_id:
            if element_id in ids:
                findings.append(finding(path, text, offset, "duplicate-id", duplicate_confidence, "semantics", f"Literal id {element_id!r} is duplicated in this file.", "Make literal IDs unique and verify label, description, and fragment references."))
            ids.add(element_id)

        tabindex = literal(attrs.get("tabindex"))
        if tabindex is not None and re.fullmatch(r"\+?[1-9]\d*", tabindex.strip()):
            findings.append(finding(path, text, offset, "positive-tabindex", "high", "accessibility", "Positive tabindex creates a manual tab order.", "Use document order and tabindex=0 only where a custom interaction requires it."))

        keys = [key.split(".", 1)[0].split("|", 1)[0] for key in attrs]
        click_handler = any(key in CLICK_HANDLERS for key in keys)
        keyboard_handler = any(key.startswith(KEY_HANDLER_PREFIXES) for key in keys)
        role = (literal(attrs.get("role")) or "").lower()
        if name in {"div", "span"} and click_handler and "role" not in attrs and not keyboard_handler and "tabindex" not in attrs and not spread:
            findings.append(finding(path, text, offset, "clickable-noninteractive", "medium", "accessibility", f"Clickable {name} has no obvious semantics, keyboard handler, or tab focus.", "Inspect the interaction and prefer a native button or link."))
        if role == "button" and not keyboard_handler and not spread:
            findings.append(finding(path, text, offset, "role-button-incomplete", "medium", "accessibility", "role=button has no obvious keyboard handler.", "Inspect Enter and Space behavior, focusability, and disabled state; prefer a native button."))
        if name == "button" and "type" not in attrs and not spread:
            findings.append(finding(path, text, offset, "button-type-omitted", "medium", "forms", "Literal button omits its type.", "Inspect form context and set button, submit, or reset explicitly."))

    findings.extend(scan_text_nodes(path, text, view, all_tags))
    return findings


def scan_text_nodes(path: str, text: str, view: str, tags: list[Tag]) -> list[Finding]:
    """Flag placeholder copy in text that sits inside an element."""
    boundaries = [(tag.start, tag.end, "void" if tag.self_closing else "open") for tag in tags]
    boundaries += [(match.start(), match.end(), "close") for match in CLOSING_TAG_RE.finditer(view)]
    boundaries.sort()
    findings: list[Finding] = []
    for (_, end, kind), (next_start, _, next_kind) in zip(boundaries, boundaries[1:]):
        if kind != "open" and next_kind != "close":
            continue
        segment = view[end:next_start]
        segment = re.sub(r"\{[^{}]*\}", lambda match: " " * len(match.group(0)), segment)
        match = PLACEHOLDER_COPY_RE.search(segment)
        if match:
            findings.append(finding(path, text, end + match.start(), "visible-placeholder-copy", "medium", "content", "Visible markup appears to contain placeholder copy.", "Confirm the rendered text and replace development copy with sourced product content."))
    return findings


def scan_css(path: str, text: str, color_threshold: int, start: int = 0, end: int | None = None, line_comments: bool = False) -> list[Finding]:
    """Scan text[start:end] as CSS, reporting positions in the whole text."""
    end = len(text) if end is None else end
    view = text[:start] + mask(text[start:end], BLOCK_COMMENT_RE) + text[end:]
    if line_comments:
        view = view[:start] + mask(view[start:end], LINE_COMMENT_RE) + view[end:]
    findings: list[Finding] = []
    for match in OUTLINE_RE.finditer(view, start, end):
        findings.append(finding(path, text, match.start(), "outline-removed", "medium", "accessibility", "CSS removes an outline.", "Confirm an equally visible focus indicator exists in every state."))

    for match in HOVER_BLOCK_RE.finditer(view, start, end):
        if LAYOUT_PROPERTY_RE.search(match.group("body")):
            findings.append(finding(path, text, match.start("selector") + len(match.group("selector")) - len(match.group("selector").lstrip()), "layout-shifting-hover", "low", "motion", "Hover rule changes dimensions or layout position.", "Inspect for layout shift and prefer stable visual feedback when movement has no product purpose."))

    colors: list[int] = []
    for declaration in DECLARATION_RE.finditer(view, start, end):
        colors.extend(color.start() for color in COLOR_RE.finditer(view, declaration.start("value"), declaration.end("value")))
    if len(colors) > color_threshold:
        findings.append(finding(path, text, colors[color_threshold], "excessive-hardcoded-color", "low", "visual-system", f"File contains {len(colors)} literal color values outside token definitions, above the threshold of {color_threshold}.", "Inspect whether repeated colors should use existing semantic tokens."))
    return findings


def is_excluded(path: Path, root: Path) -> bool:
    relative_parts = path.relative_to(root).parts if path != root else ()
    if any(part in EXCLUDED_DIRECTORIES for part in relative_parts):
        return True
    lower_name = path.name.lower()
    stem_parts = set(re.split(r"[._-]", path.stem.lower()))
    return lower_name.endswith(".min.css") or bool(stem_parts & GENERATED_MARKERS)


def candidate_files(target: Path) -> Iterable[Path]:
    if target.is_file():
        if target.suffix.lower() in SUPPORTED_SUFFIXES:
            yield target
        return
    for path in sorted(target.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES and not is_excluded(path, target):
            yield path


def read_source(path: Path) -> str | None:
    try:
        raw = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in raw[:8192]:
        return None
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return None
    if len(text) > 5000 and text.count("\n") <= 1:
        return None
    first_lines = "\n".join(text.splitlines()[:5]).lower()
    if "generated file" in first_lines or "do not edit" in first_lines:
        return None
    return text


def scan(target: Path, color_threshold: int) -> tuple[list[Finding], int]:
    findings: list[Finding] = []
    files_scanned = 0
    base = target if target.is_dir() else target.parent
    for path in candidate_files(target):
        text = read_source(path)
        if text is None:
            continue
        files_scanned += 1
        relative = path.relative_to(base).as_posix()
        suffix = path.suffix.lower()
        if suffix in CSS_SUFFIXES:
            findings.extend(scan_css(relative, text, color_threshold, line_comments=suffix != ".css"))
            continue
        findings.extend(scan_markup(relative, text, suffix))
        for style in STYLE_BLOCK_RE.finditer(mask(text, HTML_COMMENT_RE)):
            findings.extend(scan_css(relative, text, color_threshold, style.start(1), style.end(1), line_comments="lang=" in style.group(0)[:80]))
    findings.sort()
    return findings, files_scanned


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Report advisory UI smell findings.")
    parser.add_argument("path", help="file or directory to scan")
    parser.add_argument("--json", action="store_true", dest="json_output", help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true", help="return 1 when high-confidence findings exist")
    parser.add_argument("--color-threshold", type=int, default=5, help="literal color count that prompts token review (default: 5)")
    args = parser.parse_args()
    if args.color_threshold < 1:
        parser.error("--color-threshold must be at least 1")
    return args


def main() -> int:
    args = parse_args()
    target = Path(args.path).expanduser()
    try:
        target = target.resolve(strict=True)
    except OSError as exc:
        print(f"ERROR {target}: {exc}", file=sys.stderr)
        return 2
    if not target.is_file() and not target.is_dir():
        print(f"ERROR {target}: input must be a file or directory", file=sys.stderr)
        return 2
    if target.is_file() and target.suffix.lower() not in SUPPORTED_SUFFIXES:
        print(f"ERROR {target}: unsupported file type", file=sys.stderr)
        return 2

    findings, files_scanned = scan(target, args.color_threshold)
    high_count = sum(item.confidence == "high" for item in findings)
    if args.json_output:
        print(json.dumps({"findings": [asdict(item) for item in findings], "summary": {"files_scanned": files_scanned, "findings": len(findings), "high_confidence": high_count}}, indent=2, sort_keys=True))
    else:
        for item in findings:
            print(f"{item.path}:{item.line}:{item.column} [{item.confidence.upper()} {item.rule_id}] {item.message} Inspect: {item.suggested_inspection}")
        print(f"SCAN  {files_scanned} files; {len(findings)} advisory findings; {high_count} high confidence")
    return 1 if args.strict and high_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
