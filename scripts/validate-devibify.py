#!/usr/bin/env python3
"""Validate the Devibify source package without modifying it."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


REQUIRED_REFERENCES = [
    "references/ui-audit.md",
    "references/accessibility.md",
    "references/interaction-states.md",
    "references/forms-and-validation.md",
    "references/responsive-and-internationalization.md",
    "references/tables-and-data-visualization.md",
    "references/performance-and-resilience.md",
    "references/content-evidence-ethics-and-safety.md",
    "references/verification-and-reporting.md",
    "references/calibration-examples.md",
]
REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    *REQUIRED_REFERENCES,
    "scripts/validate-devibify.py",
    "scripts/scan-ui-smells.py",
    "evals/trigger-cases.json",
    "evals/behavior-cases.json",
    "evals/behavior-rubric.md",
    "tests/test_validate_devibify.py",
    "tests/test_scan_ui_smells.py",
]
REQUIRED_DIRECTORIES = [
    "tests/fixtures/smell-clean",
    "tests/fixtures/smell-problems",
]
MODES = {
    "AUDIT",
    "NARROW_FIX",
    "FEATURE_IMPLEMENTATION",
    "NET_NEW_DESIGN",
    "REFACTOR",
    "REFERENCE_FIDELITY",
}
SKIP_DIRECTORIES = {".git", "__pycache__", ".pytest_cache"}
LOCAL_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
TOKEN_RE = re.compile(r"\w+|[^\w\s]", re.UNICODE)


@dataclass(order=True)
class Issue:
    path: str
    line: int
    rule_id: str
    message: str


class Validator:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.errors: list[Issue] = []
        self.warnings: list[Issue] = []
        self.summary: dict[str, Any] = {
            "root": str(root),
            "files_checked": 0,
            "skill_lines": 0,
            "estimated_skill_tokens": 0,
            "trigger_positive": 0,
            "trigger_negative": 0,
            "behavior_cases": 0,
        }

    def error(self, path: str, line: int, rule_id: str, message: str) -> None:
        self.errors.append(Issue(path, line, rule_id, message))

    def warn(self, path: str, line: int, rule_id: str, message: str) -> None:
        self.warnings.append(Issue(path, line, rule_id, message))

    def run(self) -> None:
        self._validate_structure()
        texts = self._validate_text_files()
        self._validate_skill(texts.get("SKILL.md"))
        self._validate_openai(texts.get("agents/openai.yaml"))
        self._validate_references(texts)
        self._validate_evals(texts)

    def _validate_structure(self) -> None:
        if self.root.name != "devibify":
            self.error(
                ".",
                1,
                "structure.skill-directory-name",
                f"skill directory basename must be 'devibify', found {self.root.name!r}",
            )
        for relative in REQUIRED_FILES:
            if not (self.root / relative).is_file():
                self.error(relative, 1, "structure.required-file", "required file is missing")
        for relative in REQUIRED_DIRECTORIES:
            if not (self.root / relative).is_dir():
                self.error(relative, 1, "structure.required-directory", "required directory is missing")

        duplicates: list[str] = []
        for path in self.root.rglob("SKILL.md"):
            if any(part in SKIP_DIRECTORIES for part in path.relative_to(self.root).parts):
                continue
            duplicates.append(path.relative_to(self.root).as_posix())
        if duplicates != ["SKILL.md"]:
            self.error(
                "SKILL.md",
                1,
                "structure.duplicate-skill",
                f"expected exactly one root SKILL.md, found {sorted(duplicates)}",
            )

    def _source_paths(self) -> Iterable[Path]:
        suffixes = {".md", ".yaml", ".yml", ".json", ".py", ".html", ".css"}
        for path in self.root.rglob("*"):
            if not path.is_file():
                continue
            relative = path.relative_to(self.root)
            if any(part in SKIP_DIRECTORIES for part in relative.parts):
                continue
            if path.suffix.lower() in suffixes:
                yield path

    def _validate_text_files(self) -> dict[str, str]:
        texts: dict[str, str] = {}
        for path in self._source_paths():
            relative = path.relative_to(self.root).as_posix()
            try:
                raw = path.read_bytes()
                text = raw.decode("utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                self.error(relative, 1, "text.utf8", f"file is not readable UTF-8: {exc}")
                continue
            self.summary["files_checked"] += 1
            texts[relative] = text
            if raw and not raw.endswith(b"\n"):
                self.warn(relative, text.count("\n") + 1, "text.final-newline", "file does not end with a newline")
            if path.suffix.lower() == ".md" and re.search(r"\]\([^)]*\\[^)]*\)", text):
                self.error(relative, 1, "text.path-separator", "Markdown resource paths must use '/' separators")
        return texts

    def _parse_frontmatter(self, text: str, path: str) -> tuple[dict[str, str], str] | None:
        lines = text.splitlines()
        if not lines or lines[0] != "---":
            self.error(path, 1, "skill.frontmatter-start", "frontmatter must start on the first line")
            return None
        try:
            closing = lines.index("---", 1)
        except ValueError:
            self.error(path, 1, "skill.frontmatter-end", "frontmatter closing delimiter is missing")
            return None
        fields: dict[str, str] = {}
        for number, line in enumerate(lines[1:closing], start=2):
            match = re.fullmatch(r"([A-Za-z0-9_-]+):\s*(.*)", line)
            if not match:
                self.error(path, number, "skill.frontmatter-syntax", "frontmatter must use simple key/value fields")
                continue
            key, raw_value = match.groups()
            if key in fields:
                self.error(path, number, "skill.frontmatter-duplicate", f"duplicate frontmatter key {key!r}")
            try:
                value = json.loads(raw_value) if raw_value.startswith(('"', "'")) else raw_value
            except json.JSONDecodeError:
                self.error(path, number, "skill.frontmatter-value", f"invalid quoted value for {key!r}")
                value = ""
            fields[key] = value
        return fields, "\n".join(lines[closing + 1 :]).strip()

    def _validate_skill(self, text: str | None) -> None:
        if text is None:
            return
        self.summary["skill_lines"] = len(text.splitlines())
        self.summary["estimated_skill_tokens"] = len(TOKEN_RE.findall(text))
        parsed = self._parse_frontmatter(text, "SKILL.md")
        if parsed is None:
            return
        fields, body = parsed
        if set(fields) != {"name", "description"}:
            self.error(
                "SKILL.md",
                2,
                "skill.frontmatter-keys",
                f"frontmatter must contain only name and description, found {sorted(fields)}",
            )
        name = fields.get("name", "")
        if name != "devibify":
            self.error("SKILL.md", 2, "skill.name", "name must be 'devibify'")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            self.error("SKILL.md", 2, "skill.name-format", "name does not satisfy Agent Skills naming rules")
        description = fields.get("description", "")
        if not isinstance(description, str) or not description.strip():
            self.error("SKILL.md", 3, "skill.description", "description must be nonempty")
            description = ""
        if len(description) > 1024:
            self.error("SKILL.md", 3, "skill.description-length", "description exceeds 1,024 characters")
        lower_description = description.lower()
        if not any(term in lower_description for term in ("web interface", "frontend", "ui")):
            self.error("SKILL.md", 3, "skill.description-positive", "description lacks a positive UI trigger")
        if not any(term in lower_description for term in ("do not use", "backend-only", "purely mechanical")):
            self.error("SKILL.md", 3, "skill.description-negative", "description lacks a negative boundary")
        if not body:
            self.error("SKILL.md", 5, "skill.body", "skill body must be nonempty")
        if self.summary["skill_lines"] >= 500:
            self.error("SKILL.md", 1, "skill.line-limit", "SKILL.md must stay below 500 lines")
        if self.summary["estimated_skill_tokens"] >= 5000:
            self.warn("SKILL.md", 1, "skill.token-budget", "estimated instruction size is at or above 5,000 tokens")
        if re.search(r"\b(?:TODO|FIXME|TBD)\b|placeholder scaffold", body, re.IGNORECASE):
            self.error("SKILL.md", 1, "skill.placeholder", "unfinished placeholder language remains")
        stripped = text.strip()
        if stripped.startswith("```") and stripped.endswith("```"):
            self.error("SKILL.md", 1, "skill.fenced-wrapper", "the complete skill is wrapped in a code fence")

        self._validate_links("SKILL.md", text, require_root_direct=True)

    def _parse_openai_yaml(self, text: str) -> dict[str, Any] | None:
        result: dict[str, Any] = {}
        section: str | None = None
        for number, raw_line in enumerate(text.splitlines(), start=1):
            if not raw_line.strip():
                continue
            top = re.fullmatch(r"([A-Za-z_][\w-]*):", raw_line)
            if top:
                section = top.group(1)
                result[section] = {}
                continue
            item = re.fullmatch(r"  ([A-Za-z_][\w-]*):\s*(.+)", raw_line)
            if not item or section is None:
                self.error("agents/openai.yaml", number, "openai.syntax", "unexpected YAML structure")
                continue
            key, raw_value = item.groups()
            if raw_value in {"true", "false"}:
                value: Any = raw_value == "true"
            elif raw_value.startswith('"') and raw_value.endswith('"'):
                try:
                    value = json.loads(raw_value)
                except json.JSONDecodeError:
                    self.error("agents/openai.yaml", number, "openai.quoted-string", "invalid quoted string")
                    value = ""
            else:
                self.error("agents/openai.yaml", number, "openai.quoted-string", "string values must be double quoted")
                value = raw_value
            result[section][key] = value
        return result

    def _validate_openai(self, text: str | None) -> None:
        if text is None:
            return
        data = self._parse_openai_yaml(text)
        if data is None:
            return
        interface = data.get("interface", {})
        policy = data.get("policy", {})
        for key in ("display_name", "short_description", "default_prompt"):
            if not isinstance(interface.get(key), str) or not interface[key]:
                self.error("agents/openai.yaml", 1, f"openai.{key}", f"interface.{key} must exist")
        short = interface.get("short_description", "")
        if isinstance(short, str) and not 25 <= len(short) <= 64:
            self.error("agents/openai.yaml", 1, "openai.short-description-length", "short_description must be 25 to 64 characters")
        prompt = interface.get("default_prompt", "")
        if isinstance(prompt, str) and "$devibify" not in prompt:
            self.error("agents/openai.yaml", 1, "openai.default-prompt", "default_prompt must include $devibify")
        if not isinstance(policy.get("allow_implicit_invocation"), bool):
            self.error("agents/openai.yaml", 1, "openai.implicit-invocation", "allow_implicit_invocation must be a boolean")
        allowed_top = {"interface", "policy"}
        if set(data) - allowed_top or set(interface) - {"display_name", "short_description", "default_prompt"} or set(policy) - {"allow_implicit_invocation"}:
            self.error("agents/openai.yaml", 1, "openai.unsupported-field", "unsupported metadata or dependency field is present")
        for key, value in interface.items():
            if "icon" in key and isinstance(value, str) and not (self.root / value).is_file():
                self.error("agents/openai.yaml", 1, "openai.missing-icon", f"icon asset does not exist: {value}")

    def _validate_links(self, relative: str, text: str, require_root_direct: bool = False) -> None:
        source = self.root / relative
        for match in LOCAL_LINK_RE.finditer(text):
            target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
            target = target.split("#", 1)[0]
            if not target or re.match(r"(?:https?://|mailto:|tel:)", target):
                continue
            line = text.count("\n", 0, match.start()) + 1
            if require_root_direct and (target.startswith(("./", "../", "/")) or not target.startswith(("references/", "scripts/", "evals/", "agents/"))):
                self.error(relative, line, "links.root-direct", f"skill resource link must be direct from the skill root: {target}")
            resolved = (source.parent / target).resolve()
            try:
                resolved.relative_to(self.root.resolve())
            except ValueError:
                self.error(relative, line, "links.outside-root", f"local link leaves the skill root: {target}")
                continue
            if not resolved.exists():
                self.error(relative, line, "links.broken", f"linked resource does not exist: {target}")

    def _sections(self, text: str) -> list[str]:
        chunks = re.split(r"(?m)^#{1,6}\s+", text)
        return [re.sub(r"\s+", " ", chunk).strip().lower() for chunk in chunks[1:] if len(chunk.strip()) >= 240]

    def _validate_references(self, texts: dict[str, str]) -> None:
        seen_sections: dict[str, str] = {}
        for relative in REQUIRED_REFERENCES:
            text = texts.get(relative)
            if text is None:
                continue
            if not re.search(r"(?m)^#\s+\S", text):
                self.error(relative, 1, "references.heading", "reference must have a top-level heading")
            if re.search(r"\b(?:TODO|FIXME|TBD)\b|lorem ipsum|placeholder scaffold", text, re.IGNORECASE):
                self.error(relative, 1, "references.placeholder", "unfinished placeholder language remains")
            self._validate_links(relative, text)
            for match in LOCAL_LINK_RE.finditer(text):
                target = match.group(1).split("#", 1)[0]
                if target.endswith(".md") and target:
                    self.error(relative, text.count("\n", 0, match.start()) + 1, "references.chain-depth", "references must not require another Markdown reference hop")
            for section in self._sections(text):
                if section in seen_sections:
                    self.error(relative, 1, "references.duplicate-section", f"large section duplicates content in {seen_sections[section]}")
                else:
                    seen_sections[section] = relative

    def _load_json(self, relative: str, text: str | None) -> Any | None:
        if text is None:
            return None
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            self.error(relative, exc.lineno, "evals.valid-json", exc.msg)
            return None

    def _check_unique_ids(self, relative: str, items: list[Any]) -> None:
        seen: set[str] = set()
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                self.error(relative, index + 1, "evals.object", "every case must be an object")
                continue
            case_id = item.get("id")
            if not isinstance(case_id, str) or not case_id:
                self.error(relative, index + 1, "evals.id", "every case must have a nonempty string id")
            elif case_id in seen:
                self.error(relative, index + 1, "evals.duplicate-id", f"duplicate eval id: {case_id}")
            else:
                seen.add(case_id)

    def _validate_evals(self, texts: dict[str, str]) -> None:
        trigger_path = "evals/trigger-cases.json"
        triggers = self._load_json(trigger_path, texts.get(trigger_path))
        if isinstance(triggers, list):
            self._check_unique_ids(trigger_path, triggers)
            positives = 0
            negatives = 0
            explicit = False
            for index, case in enumerate(triggers):
                if not isinstance(case, dict):
                    continue
                missing = {"id", "query", "should_trigger"} - set(case)
                if missing:
                    self.error(trigger_path, index + 1, "evals.trigger-schema", f"missing fields: {sorted(missing)}")
                if not isinstance(case.get("should_trigger"), bool):
                    self.error(trigger_path, index + 1, "evals.trigger-boolean", "should_trigger must be a boolean")
                elif case["should_trigger"]:
                    positives += 1
                else:
                    negatives += 1
                if "$devibify" in str(case.get("query", "")) and case.get("should_trigger") is True:
                    explicit = True
            self.summary["trigger_positive"] = positives
            self.summary["trigger_negative"] = negatives
            if positives < 15 or negatives < 15:
                self.error(trigger_path, 1, "evals.trigger-count", "at least 15 positive and 15 negative trigger cases are required for release")
            if not explicit:
                self.error(trigger_path, 1, "evals.explicit-trigger", "an explicit $devibify positive case is required")
        elif triggers is not None:
            self.error(trigger_path, 1, "evals.trigger-array", "trigger cases must be a JSON array")

        behavior_path = "evals/behavior-cases.json"
        behaviors = self._load_json(behavior_path, texts.get(behavior_path))
        if isinstance(behaviors, list):
            self._check_unique_ids(behavior_path, behaviors)
            covered: set[str] = set()
            for index, case in enumerate(behaviors):
                if not isinstance(case, dict):
                    continue
                missing = {"id", "prompt", "expected_mode", "must", "must_not"} - set(case)
                if missing:
                    self.error(behavior_path, index + 1, "evals.behavior-schema", f"missing fields: {sorted(missing)}")
                mode = case.get("expected_mode")
                if mode in MODES:
                    covered.add(mode)
                else:
                    self.error(behavior_path, index + 1, "evals.behavior-mode", f"unknown expected mode: {mode!r}")
                if not isinstance(case.get("must"), list) or not isinstance(case.get("must_not"), list):
                    self.error(behavior_path, index + 1, "evals.behavior-lists", "must and must_not must be arrays")
            self.summary["behavior_cases"] = len(behaviors)
            if len(behaviors) < 20:
                self.error(behavior_path, 1, "evals.behavior-count", "at least 20 behavior cases are required for release")
            if covered != MODES:
                self.error(behavior_path, 1, "evals.mode-coverage", f"behavior cases do not cover modes: {sorted(MODES - covered)}")
        elif behaviors is not None:
            self.error(behavior_path, 1, "evals.behavior-array", "behavior cases must be a JSON array")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the Devibify source package.")
    parser.add_argument("skill_directory", nargs="?", help="skill directory; defaults to the script's parent directory")
    parser.add_argument("--json", action="store_true", dest="json_output", help="emit machine-readable JSON")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    default_root = Path(__file__).resolve().parent.parent
    root = Path(args.skill_directory).expanduser() if args.skill_directory else default_root
    try:
        root = root.resolve(strict=True)
    except OSError as exc:
        print(f"ERROR {root}:1 [cli.unreadable-target] {exc}", file=sys.stderr)
        return 2
    if not root.is_dir() or not os.access(root, os.R_OK):
        print(f"ERROR {root}:1 [cli.unreadable-target] target must be a readable directory", file=sys.stderr)
        return 2

    validator = Validator(root)
    validator.run()
    validator.errors.sort()
    validator.warnings.sort()
    if args.json_output:
        payload = {
            "ok": not validator.errors,
            "errors": [asdict(issue) for issue in validator.errors],
            "warnings": [asdict(issue) for issue in validator.warnings],
            "summary": validator.summary,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        for issue in validator.errors:
            print(f"ERROR {issue.path}:{issue.line} [{issue.rule_id}] {issue.message}")
        for issue in validator.warnings:
            print(f"WARN  {issue.path}:{issue.line} [{issue.rule_id}] {issue.message}")
        if not validator.errors:
            print(
                "PASS  "
                f"{validator.summary['files_checked']} files checked; "
                f"SKILL.md {validator.summary['skill_lines']} lines, "
                f"~{validator.summary['estimated_skill_tokens']} tokens; "
                f"{validator.summary['trigger_positive']} positive and "
                f"{validator.summary['trigger_negative']} negative triggers; "
                f"{validator.summary['behavior_cases']} behavior cases"
            )
    return 1 if validator.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
