# Changelog

## v3

- Made the skill host-neutral for Claude Code and Codex, and added a Claude Code plugin marketplace entry.
- Reduced six modes to four (Audit, Fix, Build, Refactor), with the design reference as a modifier.
- Shortened `SKILL.md` to a five-step workflow without gates, moved conflict handling into it, and narrowed reference routing.
- Removed rules that belong to the host agent: Git restrictions, instruction priority, and the fixed completion-report template.
- Added `visual-direction.md` with replacements for generic AI patterns and fallback design defaults, and `examples.md` with worked dashboard, landing page, and form examples.
- Made the UI-smell scanner JSX/TSX-, Vue-, and Svelte-aware, fixed CRLF positions and token-file false positives, and dropped indented Sass support.
- Removed the maintainer harness: the package validator, unit tests, fixtures, and eval cases.

## v2

- Added six operating modes for audits, focused fixes, feature work, new designs, refactors, and reference-based implementation.
- Added stricter scope, product-evidence, interface-state, accessibility, responsive, and verification rules.
- Expanded task-specific guidance for forms, tables, charts, localization, performance, resilience, privacy, and deceptive design.
- Replaced rigid visual bans with checks based on product context and design intent.
- Added a validator, UI-smell scanner, tests, fixtures, and evaluation cases for maintaining the skill.

## v1

- Introduced Devibify as a Codex skill for avoiding generic, vibe-coded web interfaces.
- Added a product-design workflow, UI contract, design-system guidance, component requirements, and verification checklist.
- Added UI review guidance for visual, structural, content, accessibility, responsive, and technical problems.
