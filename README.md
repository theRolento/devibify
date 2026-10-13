# Devibify

Devibify is an [Agent Skill](https://agentskills.io) for Claude Code and Codex that designs, builds, refactors, and audits web interfaces with product-design judgment. It replaces generic AI-generated structure with product-specific hierarchy, keeps work within scope, preserves coherent design systems, covers reachable states, and reports what verification supports.

Use it for UI work such as:

- auditing a product surface without changing files;
- fixing a focused interaction or accessibility defect;
- building a page, form, table, dashboard, or flow;
- refactoring shared UI without changing accepted behavior;
- implementing an approved screenshot or Figma design;
- turning a generic AI-looking page into one specific to the product.

Devibify does not target backend-only work, copy proofreading, or exact mechanical edits such as renames, token values, or asset conversions.

## Install

### Claude Code: plugin

```text
/plugin marketplace add theRolento/devibify
/plugin install devibify@devibify
```

Claude Code 2.1.275 or later also accepts the one-step form `/plugin install devibify --marketplace theRolento/devibify`. The plugin skill is invoked as `/devibify:devibify`.

### Claude Code: personal skill

```bash
git clone https://github.com/theRolento/devibify.git ~/.claude/skills/devibify
```

Invoke it as `/devibify`.

### Codex

```bash
git clone https://github.com/theRolento/devibify.git "${CODEX_HOME:-$HOME/.codex}/skills/devibify"
```

Invoke it as `$devibify`.

Either agent also activates the skill on its own for matching UI work. Keep the repository structure intact: the agent reads `SKILL.md` first and loads reference files only when a task needs them. Update a clone with `git pull`.

## Invoke

Name the skill to force activation:

```text
/devibify audit this checkout flow. Return findings only, cite the evidence for each finding, and do not change files.
```

In Codex, write `$devibify` in place of `/devibify`.

## How it works

Devibify picks one of four modes (Audit, Fix, Build, Refactor), grounds the work in a design thesis (primary user, primary task, product character), writes a proportional UI contract, and verifies with labelled evidence. See [`SKILL.md`](SKILL.md) for the workflow and [`references/visual-direction.md`](references/visual-direction.md) for the generic patterns it replaces.

## Repository layout

The repository root is the skill root, so a clone installs the skill directly for both agents.

- `SKILL.md`: modes, scope, workflow, conflict handling, and reference routing.
- `references/`: task-specific reference files loaded on demand.
- `scripts/scan-ui-smells.py`: an optional, read-only source scanner for HTML, JSX, TSX, Vue, Svelte, CSS, SCSS, and Less, which the agent runs during audits and builds. It needs Python 3 and never edits files; its findings are advisory.
- `agents/openai.yaml`: Codex interface metadata and implicit-invocation policy. Claude Code ignores it.
- `.claude-plugin/marketplace.json`: the Claude Code plugin marketplace entry.

## History

See [CHANGELOG.md](CHANGELOG.md).

## Attribution

Cyxzdev's [Uncodixfy](https://github.com/cyxzdev/Uncodixfy) inspired Devibify.

## License

See [LICENSE.md](LICENSE.md).
