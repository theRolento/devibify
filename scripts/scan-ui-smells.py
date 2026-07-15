#!/usr/bin/env python3
"""Report conservative UI smell findings without modifying source files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SUPPORTED_SUFFIXES = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".css", ".scss", ".sass", ".less"}
EXCLUDED_DIRECTORIES = {".git", "node_modules", "dist", "build", ".next", ".nuxt", "coverage", "vendor", "__snapshots__"}
GENERATED_MARKERS = {"generated", "gen", "autogen"}
TAG_RE = re.compile(r"<(?P<name>[A-Za-z][\w:-]*)\b(?P<attrs>[^<>]*?)\s*/?>", re.DOTALL)
STYLE_BLOCK_RE = re.compile(r"<style\b[^>]*>(.*?)</style\s*>", re.IGNORECASE | re.DOTALL)
COLOR_RE = re.compile(r"(?<![\w-])(?:#[0-9a-fA-F]{3,8}\b|(?:rgb|hsl)a?\([^)]*\))")


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


def position(text: str, offset: int) -> tuple[int, int]:
    line = text.count("\n", 0, offset) + 1
    previous = text.rfind("\n", 0, offset)
    return line, offset - previous


def attr_value(attrs: str, name: str) -> str | None:
    match = re.search(
        rf"(?<![\w:-]){re.escape(name)}\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|{{?\s*([^\s>}}]+)\s*}}?)",
        attrs,
        re.IGNORECASE,
    )
    if not match:
        return None
    return next((group for group in match.groups() if group is not None), "")


def has_attr(attrs: str, name: str) -> bool:
    return re.search(rf"(?<![\w:-]){re.escape(name)}(?:\s*=|\s|$)", attrs, re.IGNORECASE) is not None


def finding(path: str, text: str, offset: int, rule_id: str, confidence: str, category: str, message: str, inspection: str) -> Finding:
    line, column = position(text, offset)
    return Finding(path, line, column, rule_id, confidence, category, message, inspection)


def scan_markup(path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    ids: dict[str, int] = {}
    for match in TAG_RE.finditer(text):
        name = match.group("name").lower()
        attrs = match.group("attrs")
        offset = match.start()

        if name == "a":
            href = attr_value(attrs, "href")
            if href is not None and (href.strip() in {"", "#"} or re.fullmatch(r"javascript\s*:\s*void\s*\(\s*0\s*\)\s*;?", href, re.IGNORECASE)):
                findings.append(finding(path, text, offset, "dead-href", "high", "functionality", "Link has an empty or inert literal destination.", "Confirm the destination and use a real link, or use a button for an action."))
            target = attr_value(attrs, "target")
            if target and target.lower() == "_blank":
                rel = (attr_value(attrs, "rel") or "").lower().split()
                if not ({"noopener", "noreferrer"} & set(rel)):
                    findings.append(finding(path, text, offset, "target-blank-no-rel", "high", "security-adjacent", "Literal target=_blank link has no safe rel token.", "Add noopener or noreferrer according to repository link policy."))

        if name == "meta" and (attr_value(attrs, "name") or "").lower() == "viewport":
            content = attr_value(attrs, "content") or ""
            if re.search(r"user-scalable\s*=\s*no", content, re.IGNORECASE) or re.search(r"maximum-scale\s*=\s*(?:0(?:\.0*)?|1(?:\.0*)?)(?:\s*[,;]|\s*$)", content, re.IGNORECASE):
                findings.append(finding(path, text, offset, "prevent-zoom", "high", "accessibility", "Viewport metadata disables or severely caps user zoom.", "Allow user scaling and verify zoom and reflow behavior."))

        if name == "img" and not has_attr(attrs, "alt"):
            findings.append(finding(path, text, offset, "img-missing-alt", "high", "accessibility", "Literal image has no alt attribute.", "Provide meaningful alternative text or alt=\"\" for a decorative image."))
        if name == "iframe" and not has_attr(attrs, "title"):
            findings.append(finding(path, text, offset, "iframe-missing-title", "high", "accessibility", "Literal iframe has no title attribute.", "Provide a concise title that identifies the embedded content."))

        element_id = attr_value(attrs, "id")
        if element_id and not any(token in element_id for token in ("{", "}", "$")):
            if element_id in ids:
                findings.append(finding(path, text, offset, "duplicate-id", "high", "semantics", f"Literal id {element_id!r} is duplicated in this file.", "Make literal IDs unique and verify label, description, and fragment references."))
            else:
                ids[element_id] = offset

        tabindex = attr_value(attrs, "tabindex")
        if tabindex is None:
            tabindex = attr_value(attrs, "tabIndex")
        if tabindex is not None and re.fullmatch(r"\+?[1-9]\d*", tabindex.strip()):
            findings.append(finding(path, text, offset, "positive-tabindex", "high", "accessibility", "Positive tabindex creates a manual tab order.", "Use document order and tabindex=0 only where a custom interaction requires it."))

        click_handler = any(has_attr(attrs, event) for event in ("onclick", "onClick", "@click", "v-on:click"))
        keyboard_handler = re.search(r"(?:onkey(?:down|up|press)|@key(?:down|up)|v-on:key(?:down|up))", attrs, re.IGNORECASE) is not None
        role = (attr_value(attrs, "role") or "").lower()
        if name in {"div", "span"} and click_handler and not role and not keyboard_handler and tabindex is None:
            findings.append(finding(path, text, offset, "clickable-noninteractive", "medium", "accessibility", f"Clickable {name} has no obvious semantics, keyboard handler, or tab focus.", "Inspect the interaction and prefer a native button or link."))
        if role == "button" and not keyboard_handler:
            findings.append(finding(path, text, offset, "role-button-incomplete", "medium", "accessibility", "role=button has no obvious keyboard handler.", "Inspect Enter and Space behavior, focusability, and disabled state; prefer a native button."))
        if name == "button" and not has_attr(attrs, "type"):
            findings.append(finding(path, text, offset, "button-type-omitted", "medium", "forms", "Literal button omits its type.", "Inspect form context and set button, submit, or reset explicitly."))

    visible_copy = re.compile(r">[^<]*(?:lorem\s+ipsum|\bTODO\b|\bFIXME\b)[^<]*<", re.IGNORECASE)
    for match in visible_copy.finditer(text):
        findings.append(finding(path, text, match.start(), "visible-placeholder-copy", "medium", "content", "Visible markup appears to contain placeholder copy.", "Confirm the rendered text and replace development copy with sourced product content."))
    return findings


def scan_css(path: str, text: str, color_threshold: int) -> list[Finding]:
    findings: list[Finding] = []
    for match in re.finditer(r"outline\s*:\s*(?:none|0(?:px|rem|em)?)(?:\s*!important)?\s*(?:;|})", text, re.IGNORECASE):
        findings.append(finding(path, text, match.start(), "outline-removed", "medium", "accessibility", "CSS removes an outline.", "Confirm an equally visible focus indicator exists in every state."))

    hover_block = re.compile(r"(?P<selector>[^{}\n]*:hover[^{}\n]*)\{(?P<body>[^{}]*)\}", re.IGNORECASE | re.DOTALL)
    for match in hover_block.finditer(text):
        body = match.group("body")
        if re.search(r"(?:^|;)\s*(?:width|height|margin(?:-[\w-]+)?|padding(?:-[\w-]+)?|top|right|bottom|left)\s*:", body, re.IGNORECASE):
            findings.append(finding(path, text, match.start("selector"), "layout-shifting-hover", "low", "motion", "Hover rule changes dimensions or layout position.", "Inspect for layout shift and prefer stable visual feedback when movement has no product purpose."))

    colors = list(COLOR_RE.finditer(text))
    if len(colors) > color_threshold:
        findings.append(finding(path, text, colors[color_threshold].start(), "excessive-hardcoded-color", "low", "visual-system", f"File contains {len(colors)} literal color values, above the threshold of {color_threshold}.", "Inspect whether repeated colors should use existing semantic tokens."))
    return findings


def is_excluded(path: Path, root: Path) -> bool:
    relative_parts = path.relative_to(root).parts if path != root else ()
    if any(part in EXCLUDED_DIRECTORIES for part in relative_parts):
        return True
    lower_name = path.name.lower()
    stem_parts = set(re.split(r"[._-]", path.stem.lower()))
    if lower_name.endswith((".min.js", ".min.css")) or stem_parts & GENERATED_MARKERS:
        return True
    return False


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
        relative = path.relative_to(base).as_posix() if path != target else path.name
        suffix = path.suffix.lower()
        if suffix not in {".css", ".scss", ".sass", ".less"}:
            findings.extend(scan_markup(relative, text))
            for style_match in STYLE_BLOCK_RE.finditer(text):
                style_findings = scan_css(relative, style_match.group(1), color_threshold)
                body_start = style_match.start(1)
                for item in style_findings:
                    absolute_offset = body_start + sum(len(line) + 1 for line in style_match.group(1).splitlines()[: item.line - 1]) + item.column - 1
                    item.line, item.column = position(text, absolute_offset)
                findings.extend(style_findings)
        else:
            findings.extend(scan_css(relative, text, color_threshold))
    findings.sort()
    return findings, files_scanned


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Report advisory UI smell findings.")
    parser.add_argument("path", help="file or directory to scan")
    parser.add_argument("--json", action="store_true", dest="json_output", help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true", help="return 1 when high-confidence findings exist")
    parser.add_argument("--color-threshold", type=int, default=5, help="literal color count that prompts token review (default: 5)")
    args = parser.parse_args(argv)
    if args.color_threshold < 1:
        parser.error("--color-threshold must be at least 1")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
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
