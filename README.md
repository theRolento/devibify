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

Place this repository folder in the Codex skills directory:

```text
$CODEX_HOME/skills/devibify
```

With the default Codex home directory, the path is:

```text
~/.codex/skills/devibify
```

Keep `SKILL.md` at the top of the installed `devibify` folder.

The repository file `agents/openai.yaml` stores skill interface metadata inside the skill folder.

This repository contains the runtime skill and its maintenance harness. Codex follows the routing in `SKILL.md`; tests and eval data do not enter a skill run unless a task opens or executes them.

## Invoke

Call the skill by name when you want to force activation:

```text
Use $devibify to audit this checkout flow. Return findings only, cite the evidence for each finding, and do not change files.
```

The skill also allows implicit invocation for matching frontend work. Its description excludes backend work and mechanical edits.

## Operating modes

Devibify selects one primary mode before broad inspection or modification:

| Mode | Purpose |
|---|---|
| `AUDIT` | Inspect and report without modifying product files |
| `NARROW_FIX` | Correct one defined surface or defect |
| `FEATURE_IMPLEMENTATION` | Add or change a page, flow, component family, or behavior |
| `NET_NEW_DESIGN` | Design a new interface without an established reference |
| `REFACTOR` | Improve structure while preserving accepted behavior and visual intent |
| `REFERENCE_FIDELITY` | Implement against an approved screenshot, design, or specification |

Each mode uses the same scope, evidence, and verification rules with effort proportional to the task.

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

The eval corpus specifies expected behavior. This repository has no runtime Codex evaluator, so it does not claim that a model has passed those cases. The validator checks eval structure and coverage.

## Validate

Run the repository checks from its root:

```bash
python scripts/validate-devibify.py .
python scripts/validate-devibify.py . --json
python -m unittest discover -s tests -p 'test_*.py'
python -m py_compile scripts/validate-devibify.py scripts/scan-ui-smells.py
python -m json.tool evals/trigger-cases.json >/dev/null
python -m json.tool evals/behavior-cases.json >/dev/null
```

Scan supported UI source files with:

```bash
python scripts/scan-ui-smells.py <path>
python scripts/scan-ui-smells.py <path> --json
python scripts/scan-ui-smells.py <path> --strict
```

The scanner reports findings without editing files. Default mode returns status 0 when it finds issues. Strict mode returns status 1 when it finds a high-confidence issue.

## Attribution

Cyxzdev's [Uncodixfy](https://github.com/cyxzdev/Uncodixfy) inspired Devibify.

## License

See [LICENSE.md](LICENSE.md).
