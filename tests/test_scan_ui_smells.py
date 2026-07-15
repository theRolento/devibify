from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "scan-ui-smells.py"
CLEAN = ROOT / "tests" / "fixtures" / "smell-clean"
PROBLEMS = ROOT / "tests" / "fixtures" / "smell-problems"


def load_scanner_module():
    spec = importlib.util.spec_from_file_location("scan_ui_smells", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SCANNER = load_scanner_module()


def digest_tree(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in root.rglob("*")
        if path.is_file()
    }


class ScannerTests(unittest.TestCase):
    expected_rules = {
        "dead-href",
        "prevent-zoom",
        "img-missing-alt",
        "iframe-missing-title",
        "target-blank-no-rel",
        "duplicate-id",
        "positive-tabindex",
        "outline-removed",
        "clickable-noninteractive",
        "role-button-incomplete",
        "button-type-omitted",
        "visible-placeholder-copy",
        "layout-shifting-hover",
        "excessive-hardcoded-color",
    }
    high_rules = {
        "dead-href",
        "prevent-zoom",
        "img-missing-alt",
        "iframe-missing-title",
        "target-blank-no-rel",
        "duplicate-id",
        "positive-tabindex",
    }

    def test_every_rule_has_a_positive_fixture(self) -> None:
        findings, _ = SCANNER.scan(PROBLEMS, 5)
        self.assertEqual(self.expected_rules, {item.rule_id for item in findings})

    def test_high_confidence_rules_have_clean_negatives(self) -> None:
        findings, _ = SCANNER.scan(CLEAN, 5)
        self.assertFalse(self.high_rules & {item.rule_id for item in findings})

    def test_excluded_directories_are_ignored(self) -> None:
        findings, files_scanned = SCANNER.scan(PROBLEMS, 5)
        self.assertEqual(2, files_scanned)
        self.assertFalse(any("node_modules" in item.path for item in findings))

    def test_text_and_json_output_are_valid(self) -> None:
        text_result = subprocess.run([sys.executable, str(SCRIPT), str(PROBLEMS)], check=False, capture_output=True, text=True)
        self.assertEqual(0, text_result.returncode)
        self.assertIn("[HIGH dead-href]", text_result.stdout)
        self.assertIn("SCAN  ", text_result.stdout)

        json_result = subprocess.run([sys.executable, str(SCRIPT), str(PROBLEMS), "--json"], check=False, capture_output=True, text=True)
        self.assertEqual(0, json_result.returncode)
        payload = json.loads(json_result.stdout)
        self.assertEqual(len(self.expected_rules), payload["summary"]["findings"])

    def test_default_and_strict_exit_codes(self) -> None:
        default = subprocess.run([sys.executable, str(SCRIPT), str(PROBLEMS)], check=False, capture_output=True, text=True)
        strict = subprocess.run([sys.executable, str(SCRIPT), str(PROBLEMS), "--strict"], check=False, capture_output=True, text=True)
        missing = subprocess.run([sys.executable, str(SCRIPT), str(PROBLEMS / "missing")], check=False, capture_output=True, text=True)
        self.assertEqual(0, default.returncode)
        self.assertEqual(1, strict.returncode)
        self.assertEqual(2, missing.returncode)

    def test_scan_does_not_modify_files(self) -> None:
        before = digest_tree(PROBLEMS)
        SCANNER.scan(PROBLEMS, 5)
        self.assertEqual(before, digest_tree(PROBLEMS))

    def test_line_numbers_are_stable(self) -> None:
        findings, _ = SCANNER.scan(PROBLEMS, 5)
        dead = next(item for item in findings if item.rule_id == "dead-href")
        duplicate = next(item for item in findings if item.rule_id == "duplicate-id")
        self.assertEqual(9, dead.line)
        self.assertEqual(14, duplicate.line)

    def test_binary_and_minified_files_are_skipped(self) -> None:
        with tempfile.TemporaryDirectory(prefix=".scanner-test-", dir=ROOT) as directory:
            root = Path(directory)
            (root / "binary.html").write_bytes(b"<html>\x00</html>")
            (root / "bundle.min.css").write_text("a{color:#000}" * 1000, encoding="utf-8")
            (root / "one-line.css").write_text("a{color:#000}" * 1000, encoding="utf-8")
            findings, files_scanned = SCANNER.scan(root, 5)
            self.assertEqual([], findings)
            self.assertEqual(0, files_scanned)


if __name__ == "__main__":
    unittest.main()
