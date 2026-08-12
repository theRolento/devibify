from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate-devibify.py"


def load_validator_module():
    spec = importlib.util.spec_from_file_location("validate_devibify", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator_module()


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix=".validator-test-", dir=ROOT)
        self.base = Path(self.temp.name)
        self.skill = self.base / "devibify"
        self.skill.mkdir()
        shutil.copy2(ROOT / "SKILL.md", self.skill / "SKILL.md")
        for directory in ("agents", "references", "scripts", "evals", "tests"):
            shutil.copytree(
                ROOT / directory,
                self.skill / directory,
                ignore=shutil.ignore_patterns("__pycache__", ".validator-test-*", ".scanner-test-*"),
            )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def validate(self, root: Path | None = None):
        validator = VALIDATOR.Validator(root or self.skill)
        validator.run()
        return validator

    def rewrite_skill(self, transform) -> None:
        path = self.skill / "SKILL.md"
        path.write_text(transform(path.read_text(encoding="utf-8")), encoding="utf-8")

    def assert_rule(self, validator, rule_id: str) -> None:
        self.assertIn(rule_id, {issue.rule_id for issue in validator.errors})

    def test_valid_skill_passes(self) -> None:
        self.assertEqual([], self.validate().errors)

    def test_invalid_name_fails(self) -> None:
        self.rewrite_skill(lambda text: text.replace("name: devibify", "name: Devibify"))
        self.assert_rule(self.validate(), "skill.name")

    def test_directory_name_mismatch_fails(self) -> None:
        mismatch = self.base / "wrong-name"
        self.skill.rename(mismatch)
        self.assert_rule(self.validate(mismatch), "structure.skill-directory-name")

    def test_missing_description_fails(self) -> None:
        self.rewrite_skill(lambda text: "\n".join(line for line in text.splitlines() if not line.startswith("description:")) + "\n")
        self.assert_rule(self.validate(), "skill.description")

    def test_description_over_limit_fails(self) -> None:
        def transform(text: str) -> str:
            lines = text.splitlines()
            lines[2] = "description: \"" + ("interface " * 130) + "Do not use for backend-only work.\""
            return "\n".join(lines) + "\n"

        self.rewrite_skill(transform)
        self.assert_rule(self.validate(), "skill.description-length")

    def test_extra_frontmatter_key_fails(self) -> None:
        self.rewrite_skill(lambda text: text.replace("description:", "license: MIT\ndescription:", 1))
        self.assert_rule(self.validate(), "skill.frontmatter-keys")

    def test_missing_reference_fails(self) -> None:
        (self.skill / "references" / "accessibility.md").unlink()
        self.assert_rule(self.validate(), "structure.required-file")

    def test_broken_default_prompt_fails(self) -> None:
        path = self.skill / "agents" / "openai.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace("$devibify", "the skill"), encoding="utf-8")
        self.assert_rule(self.validate(), "openai.default-prompt")

    def test_short_description_outside_range_fails(self) -> None:
        path = self.skill / "agents" / "openai.yaml"
        text = path.read_text(encoding="utf-8")
        text = re.sub(r'(?m)^  short_description: ".*"$', '  short_description: "Too short"', text)
        path.write_text(text, encoding="utf-8")
        self.assert_rule(self.validate(), "openai.short-description-length")

    def test_invalid_eval_json_fails(self) -> None:
        (self.skill / "evals" / "trigger-cases.json").write_text("[invalid]\n", encoding="utf-8")
        self.assert_rule(self.validate(), "evals.valid-json")

    def test_duplicate_eval_id_fails(self) -> None:
        path = self.skill / "evals" / "trigger-cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        cases[1]["id"] = cases[0]["id"]
        path.write_text(json.dumps(cases) + "\n", encoding="utf-8")
        self.assert_rule(self.validate(), "evals.duplicate-id")

    def test_missing_newline_warns(self) -> None:
        path = self.skill / "references" / "accessibility.md"
        path.write_bytes(path.read_bytes().rstrip(b"\n"))
        validator = self.validate()
        self.assertIn("text.final-newline", {issue.rule_id for issue in validator.warnings})

    def test_json_output_and_exit_codes(self) -> None:
        valid = subprocess.run([sys.executable, str(SCRIPT), str(self.skill), "--json"], check=False, capture_output=True, text=True)
        self.assertEqual(0, valid.returncode)
        self.assertTrue(json.loads(valid.stdout)["ok"])

        self.rewrite_skill(lambda text: text.replace("name: devibify", "name: invalid_name"))
        invalid = subprocess.run([sys.executable, str(SCRIPT), str(self.skill), "--json"], check=False, capture_output=True, text=True)
        self.assertEqual(1, invalid.returncode)
        self.assertFalse(json.loads(invalid.stdout)["ok"])

        missing = subprocess.run([sys.executable, str(SCRIPT), str(self.base / "missing")], check=False, capture_output=True, text=True)
        self.assertEqual(2, missing.returncode)


if __name__ == "__main__":
    unittest.main()
