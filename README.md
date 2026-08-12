# Devibify

Devibify is a Codex skill for implementing, refactoring, and auditing web interfaces that need product-design judgment. It keeps work within scope, grounds decisions in product evidence, preserves coherent design systems, covers reachable states, and reports what verification supports.

Use it for UI work such as:

- auditing a product surface without changing files;
- fixing a focused interaction or accessibility defect;
- implementing a page, form, table, dashboard, or flow;
- refactoring shared UI without changing accepted behavior;
- translating an approved visual reference into code;
- replacing generic AI-generated structure with product-specific hierarchy.

Devibify does not target backend-only work, mechanical frontend edits, copy proofreading, or exact token substitutions that require no UX decision.

## Install

Install the whole repository at:

```text
$CODEX_HOME/skills/devibify
```

The default location is `~/.codex/skills/devibify`. Keep the repository structure intact. Codex starts with `SKILL.md` and loads supporting references when relevant; tests and eval data remain maintenance assets.

## Invoke

Call the skill by name when you want to force activation:

```text
Use $devibify to audit this checkout flow. Return findings only, cite the evidence for each finding, and do not change files.
```

The skill also allows implicit invocation for matching frontend work. Its description excludes backend work and mechanical edits.

## Operating modes

See the [mode definitions and selection rules](SKILL.md#select-the-mode) in `SKILL.md`.

## Repository layout

### Runtime surface

- `SKILL.md` contains activation boundaries, guardrails, modes, workflow gates, and reference routing.
- `agents/openai.yaml` contains Codex interface metadata and implicit-invocation policy.
- `references/` contains task-specific guidance loaded through the routing table.
- `scripts/scan-ui-smells.py` provides an optional, read-only source scanner. Its findings require human or agent review.

### Assurance harness

- `scripts/validate-devibify.py` checks package structure, metadata, links, encoding, eval schemas, and release counts.
- `tests/` covers the validator and every scanner rule with standard-library unit tests.
- `evals/` records trigger expectations, behavior cases, critical gates, and the scoring rubric.

The eval corpus specifies expected behavior. This repository has no runtime Codex evaluator, so it does not claim that a model has passed those cases. The validator checks eval structure and coverage. These maintenance files belong in the source repository even though Codex does not need them during a skill run.

Regular users do not need to run the assurance harness. It is included for maintainers, contributors, and anyone who wants to verify the repository.

## Validate

Run the repository checks from its root:

```bash
python scripts/validate-devibify.py .
python scripts/validate-devibify.py . --json
python -m unittest discover -s tests -p 'test_*.py'
python -m py_compile scripts/validate-devibify.py scripts/scan-ui-smells.py
```

Scan supported UI source files with:

```bash
python scripts/scan-ui-smells.py <path>
python scripts/scan-ui-smells.py <path> --json
python scripts/scan-ui-smells.py <path> --strict
```

The scanner reports findings without editing files. Default mode returns status 0 when it finds issues. Strict mode returns status 1 when it finds a high-confidence issue.

## History

See [CHANGELOG.md](CHANGELOG.md) for the v1 and v2 feature summaries.

## Attribution

Cyxzdev's [Uncodixfy](https://github.com/cyxzdev/Uncodixfy) inspired Devibify.

## License

See [LICENSE.md](LICENSE.md).
