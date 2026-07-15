---
name: devibify
description: "Use this skill when implementing, refactoring, or auditing web interfaces that require product-specific hierarchy, design-system coherence, complete interaction and data states, responsive and accessibility hardening, content integrity, or removal of generic AI-generated patterns. Do not use for backend-only work, purely mechanical frontend edits, copy-only proofreading, or isolated token changes that require no UX or product-design judgment."
---

# Devibify

Treat each web interface as a product system shaped by real users, content, workflows, and constraints. Produce a scoped audit or implementation that is product-specific, coherent, complete across reachable states, accessible, resilient, and supported by bounded evidence.

## Non-negotiable guardrails

- Keep `AUDIT` read-only. Create only a report artifact the user explicitly requests.
- Keep changes inside requested scope, necessary dependency scope, and introduced regression scope. Report adjacent pre-existing issues separately.
- Preserve existing user work. Run Git or repository-management commands only when the user explicitly requests them.
- Classify missing information instead of inventing product facts, proof, data, routes, permissions, APIs, persistence, or successful behavior.
- Preserve coherent existing systems, accepted product behavior, and explicit design references.
- Preserve justified brand expression. Prefer the least visual complexity needed to clarify hierarchy, behavior, state, and intended brand character; treat restraint as a tool rather than a universal style.
- Use native semantics before ARIA and implement keyboard behavior explicitly where native behavior is unavailable.
- Implement every state the changed surface can actually reach.
- Reuse current dependencies and primitives. Add a dependency only when the task or repository establishes a real need.
- Tie completion claims to evidence. Report unexecuted checks as exact gaps, never as verified.

## Select the mode

Choose one primary mode before broad inspection or modification. Name a secondary mode only when useful, and announce any later mode change.

| Mode | Use it for | Required behavior |
|---|---|---|
| `AUDIT` | Inspect and report | Keep product files unchanged. Prioritize findings by severity, location, evidence, impact, correction, scope, and verification status. |
| `NARROW_FIX` | Correct a defined component, state, or localized defect | Limit changes to the requested surface and necessary dependencies. Fix introduced regressions; report adjacent issues. |
| `FEATURE_IMPLEMENTATION` | Add or substantially change a page, flow, component family, or behavior | Define a UI contract, inspect reuse and data contracts, and cover all reachable states plus responsive, keyboard, focus, error, and verification behavior. |
| `NET_NEW_DESIGN` | Design without an established reference | Establish product, user, task, content, constraints, visual and interaction theses, and density. When requirements do not determine structure, compare two directions that differ in hierarchy, workflow, density, navigation, or content emphasis. |
| `REFACTOR` | Improve structure or design-system coherence | Preserve visible behavior and visual intent unless authorized otherwise. Identify shared blast radius and inspect representative consumers. |
| `REFERENCE_FIDELITY` | Implement against an approved screenshot, design, or specification | Let the reference control hierarchy and visual intent within repository and accessibility constraints. Reuse existing components, verify target and responsive viewports, and record deviations and unspecified behavior. |

Explicit `$devibify` invocation still applies to narrow work; keep the process proportional.

## Apply priority and scope

Apply instructions in this order:

1. Higher-level system, organization, and repository instructions, including applicable `AGENTS.md` files.
2. The user's explicit request, acceptance criteria, and approved product or design references.
3. Established product behavior, content sources, data contracts, and coherent design-system conventions.
4. Devibify defaults and heuristics.

Surface accessibility, security, privacy, legal, and deceptive-design risks even when a lower-priority request conflicts with them. Preserve intent through the safest compliant implementation and report any deviation; never silently weaken accessibility or violate an explicit requirement.

Use four scope categories:

1. **Requested:** The explicitly requested surface and outcome.
2. **Necessary dependency:** The minimum supporting code, shared component, token, test, or route required for a safe result.
3. **Introduced regression:** Every defect caused by the implementation; fix it.
4. **Adjacent pre-existing:** Unrelated defects found during inspection; report them and leave them unchanged unless they block the request.

Keep an audit from becoming implementation. Keep a local defect from causing an unauthorized redesign, global token change, component-library replacement, route or endpoint creation, or product-copy and navigation change. Keep unconventional but intentional brand expression intact.

## Classify information

- **Observed:** Support it directly with the user request, repository, runtime, data contract, approved design, or authoritative source.
- **Inferred:** Derive a bounded conclusion from observed evidence; state the evidence and uncertainty when it affects architecture, content, behavior, or scope.
- **Unknown:** Leave unestablished information unknown.
- **Fixture:** Label synthetic development or test data clearly and keep it non-sensitive.

Use the smallest reversible assumption for a low-risk local decision. State an assumption before it affects architecture, content, permissions, navigation, or business behavior. Omit unsupported proof. Continue safely around noncritical unknowns; ask when an unknown would force a risky or irreversible choice.

## Identify non-trivial work

Treat work as non-trivial when any of these conditions applies:

- introduce or substantially change a page, route, flow, or reusable component;
- affect more than one interaction or data state;
- involve asynchronous, data-backed, permission-dependent, or destructive behavior;
- change navigation or information architecture;
- require a responsive transformation;
- change form validation, focus management, or error recovery;
- introduce a visual primitive, token, or dependency;
- affect multiple routes or products through a shared component;
- involve a custom widget or complex accessibility pattern;
- translate a visual reference into code;
- materially affect performance, privacy, security, consent, billing, or data integrity.

Treat a copy correction, exact token substitution, mechanical rename, or isolated non-behavioral style fix as narrow unless evidence shows broader impact.

## Run the workflow

### 1. Establish authority

Read applicable `AGENTS.md` and repository guidance. Identify the requested outcome, primary mode, requested and prohibited scope, change authority, and whether a visual reference is authoritative, inspirational, or absent. Avoid broad modification until these are explicit.

**Gate:** Name the mode, outcome, requested scope, prohibited scope, and change authority.

### 2. Inspect relevant product evidence

Inspect only relevant routes, neighboring screens, shared components and consumers, tokens and theme, content and localization sources, data types and contracts, loaders and actions, permissions, scripts and tests, browser tooling, accessibility patterns, and supplied references.

Identify the primary user and task, content and data sources of truth, constraints, reuse targets, shared blast radius, verification capabilities, and material unknowns.

**Gate:** Support product context with observed evidence or classify each material gap as unknown.

### 3. Define a proportional UI contract

For non-trivial work, record:

- mode, primary user, task, and surface purpose;
- requested scope, dependency scope, and out-of-scope boundaries;
- source of truth and information hierarchy;
- primary and secondary actions;
- layout regions, component inventory, and reuse plan;
- reachable interaction and data states;
- responsive transformations;
- keyboard and focus behavior;
- content and localization constraints;
- visual-system constraints and density: compact, balanced, paced, or immersive;
- observed facts, inferences, unknowns, and fixtures;
- verification plan.

For a narrow fix, reduce this to a concise scope and behavior note.

**Gate:** Give every visible region and control a purpose, every reachable state an intended outcome, and every material claim a possible evidence path or explicit verification bound.

### 4. Load applicable references

Read only what applies. Use the routing table below; do not load the whole reference directory for a narrow task.

### 5. Choose the product direction

Preserve coherent existing patterns. Build hierarchy with composition, layout, typography, spacing, and contrast before decoration. Use visual devices only for brand, structure, affordance, status, or narrative. Treat high-frequency AI patterns as hypotheses, not defaults. Compare two structural directions only for unconstrained net-new work.

**Gate:** Tie every new structural or visual choice to the established system or a product-specific rationale.

### 6. Implement behavior and content

Reuse components, tokens, icons, and dependencies. Use semantic controls. Implement reachable states, immediate accurate asynchronous feedback, duplicate-submission guards, recoverable error behavior, and input preservation. Make empty states truthful and actionable only when users can change the condition. Keep links real, controls functional, authorization and data contracts intact, and fixtures labelled. Add metadata only when page scope and framework support require it.

**Gate:** Give every visible control a real purpose and behavior, or mark it explicitly as development-only nonfunctional scaffolding.

### 7. Audit the changed surface

Apply relevant audit categories and specialized references. Fix in-scope failures and introduced regressions. Report adjacent pre-existing failures. Record categories that could not be verified. Treat heuristics as contextual checks rather than blanket change mandates.

**Gate:** Account for every category relevant to the changed surface, including those left unverified.

### 8. Verify with evidence

Discover and run relevant repository commands. When browser capability exists, exercise the primary flow, changed controls, reachable states, keyboard and focus, and representative very narrow, intermediate, and wide conditions. Inspect console and network failures and run existing accessibility checks when available.

Classify claims as executed automated check, browser-observed, visual inspection, keyboard and focus inspection, automated accessibility check, source inspection, inference, or not verified.

**Gate:** Attach evidence to every material completion claim or list it as unverified with cause and residual risk.

### 9. Report proportionally

Report the mode, requested and out-of-scope surfaces, changed files or audit locations, key product decisions, information classifications and fixtures, exact verification results, accessibility and responsive checks, gaps, residual risks, and adjacent issues left unchanged.

**Gate:** Let the report distinguish what was changed, observed, executed, inferred, and not verified without unsupported completion language.

## Route references

| Reference | Load when |
|---|---|
| [`references/ui-audit.md`](references/ui-audit.md) | Any audit, non-trivial page or flow change, or final product-quality pass |
| [`references/accessibility.md`](references/accessibility.md) | Any interactive UI, accessibility request, custom widget, form, navigation, dialog, page-level change, or audit |
| [`references/interaction-states.md`](references/interaction-states.md) | Any asynchronous, data-backed, permission-dependent, editable, upload, destructive, or multi-state control |
| [`references/forms-and-validation.md`](references/forms-and-validation.md) | Any form, search input with validation, checkout, authentication, account, upload, or data-entry flow |
| [`references/responsive-and-internationalization.md`](references/responsive-and-internationalization.md) | Any layout, typography, navigation, page, localized content, long text, mobile behavior, or right-to-left concern |
| [`references/tables-and-data-visualization.md`](references/tables-and-data-visualization.md) | Any table, dense list, chart, KPI, report, dashboard, analytics, comparison, or data export surface |
| [`references/performance-and-resilience.md`](references/performance-and-resilience.md) | Any page-level work, media, animation, large list, client rendering, data fetching, slow network, offline, or performance-sensitive flow |
| [`references/content-evidence-ethics-and-safety.md`](references/content-evidence-ethics-and-safety.md) | Marketing, proof, metrics, social content, consent, billing, subscriptions, privacy, permissions, destructive actions, user-generated content, or AI-generated output |
| [`references/verification-and-reporting.md`](references/verification-and-reporting.md) | Any audit or non-trivial implementation before final reporting |
| [`references/calibration-examples.md`](references/calibration-examples.md) | Mode, scope, fidelity, brand, fixture, or conflict handling is ambiguous |

For audits or non-trivial changes in supported file types, optionally run [`scripts/scan-ui-smells.py`](scripts/scan-ui-smells.py). Treat every result as an advisory prompt requiring context, not an automatic fix.

## Completion standard

Use the structured templates in `references/verification-and-reporting.md` for audits and non-trivial implementations. Keep tiny-fix reports concise but preserve the evidence boundary.

Stop short of broad claims such as fully accessible, production-ready, pixel-perfect, responsive across all devices, performance optimized, no regressions, secure, or compliant unless the evidence covers that full claim. State bounded results, exact gaps, and residual risks.

## Failure conditions

Treat the run as incomplete when any applicable condition remains:

- the primary mode or change authority is ambiguous;
- audit mode modified product files;
- scope expanded without authorization;
- a material unknown became a product fact;
- a reachable state or visible control lacks defined behavior;
- established authorization, accessibility, content integrity, or design-system constraints were silently weakened;
- a relevant failed check remains unexplained;
- a material completion claim lacks evidence or an explicit unverified label.
