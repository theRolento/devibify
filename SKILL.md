---
name: devibify
description: "Design, build, refactor, or audit browser-visible web UI so it reads as product-specific instead of generic AI output, with coherent design systems, complete states, accessibility, responsive behavior, and evidence-backed verification. Use for any web page, component, flow, dashboard, form, or landing page whose visible experience changes or is reviewed. Do not use for backend-only work, copy proofreading, or exact mechanical edits such as renames, token values, or asset conversions."
---

# Devibify

Treat each interface as a product system shaped by real users, content, workflows, and constraints. Ground every visible choice in a **design thesis**: the primary user, their primary task, and the product character the interface serves. Generic AI defaults are the failure this skill prevents; [`references/visual-direction.md`](references/visual-direction.md) names them and their replacements.

## Pick the mode

| Mode | Use it for | Boundary |
|---|---|---|
| Audit | Inspect and report | Product files stay unchanged. Write only a report the user asks for. |
| Fix | A defined component, state, or localized defect | Change the requested surface and its necessary dependencies. |
| Build | A new or substantially changed page, flow, component family, or behavior | Cover every reachable state, responsive behavior, keyboard, and focus. |
| Refactor | Structure or design-system coherence | Keep visible behavior and visual intent unless the user authorizes a change. Inspect consumers of every shared component you touch. |

Name the mode when you start and announce any change. Scale the process to the mode: a Fix gets a one-sentence thesis and a scope note; a Build gets the full UI contract.

**Design reference.** Classify any screenshot, Figma frame, or specification as authoritative, inspirational, or absent. An authoritative design reference controls hierarchy and visual intent within accessibility and repository constraints: reuse existing components to match it, verify at its viewport plus narrow and wide widths, and record deviations and every state it leaves unspecified (errors, empty, loading, mobile). Derive unspecified states from repository patterns.

## Scope

- **Requested:** the surface and outcome the user asked for.
- **Necessary dependency:** the minimum shared code, token, test, or route a safe result needs.
- **Introduced regression:** anything your change breaks. Fix it.
- **Adjacent issue:** a pre-existing defect you notice. Report it and leave it unchanged unless it blocks the request.

A local defect gets a local fix: the redesign, global token change, component-library swap, new route or endpoint, and copy or navigation change each need the user's request. Intentional brand expression, including unconventional or maximalist styles, stays.

## Workflow

### 1. Gather evidence

Inspect the relevant routes, neighboring screens, shared components and their consumers, tokens and theme, content and localization sources, data contracts, permissions, and existing tests and browser tooling. Label each material fact as observed, inferred (with its evidence), or unknown. Take the smallest reversible assumption for a low-risk local decision and state it; ask when an unknown would force a risky or irreversible choice about architecture, content, permissions, navigation, or business behavior.

### 2. Write the UI contract

For a Build or Refactor, record:

- the design thesis and its evidence;
- the information hierarchy and the source of truth for each piece of content;
- primary and secondary actions;
- layout regions and the components reused for them;
- reachable states and the intended outcome of each;
- narrow, intermediate, and wide behavior;
- keyboard and focus behavior;
- density: compact, balanced, paced, or immersive;
- the verification plan.

For a Fix, write one sentence of thesis and scope. For an Audit, the thesis frames which findings matter.

### 3. Choose the direction

Keep coherent existing patterns. Build hierarchy with layout, type, spacing, and contrast before decoration, and give every visual device a reason: brand, structure, affordance, status, or narrative.

For a Build with no design reference and no evidence of product character, ask one focused question about that character before choosing a visual direction. When requirements leave the structure open, describe two directions in a few lines each that differ in hierarchy, workflow, density, or navigation, pick one with its rationale, and proceed; the user can redirect.

### 4. Implement

Reuse existing components, tokens, icons, and dependencies. Use native semantics before ARIA, and implement keyboard behavior wherever native behavior is unavailable. Give every control a real behavior and every link a real destination. Give asynchronous actions immediate pending feedback, a duplicate-submission guard, recoverable errors that keep the user's input, and a success state shown only after the action succeeds. Keep empty states truthful, with an action only when the user can change the condition. Show only attributable proof such as logos, testimonials, and metrics; while real data is unavailable, use **synthetic data** labelled as such.

### 5. Verify and report

Run the repository's relevant checks. When a browser is available, exercise the primary flow, every changed control and reachable state, keyboard and focus, and widths of 320px, an intermediate size, and a wide desktop; inspect console and network failures. Attach to every completion claim its evidence type: executed check, browser-observed, source inspection, inference, or not verified with the cause. Claims such as "fully accessible", "pixel-perfect", "production-ready", or "responsive on all devices" need evidence covering the whole claim; otherwise state the bounded result.

The report states the mode, what changed or was audited, the key design decisions, each verification with its evidence type, what remains unverified with its residual risk, and adjacent issues left unchanged. Audit findings use the format in [`references/ui-audit.md`](references/ui-audit.md).

## Conflicts

Host instructions (system, `AGENTS.md`, `CLAUDE.md`) and the user's explicit request outrank these defaults. When a request would weaken accessibility, security, privacy, or honesty, keep its intent through the safest compliant version and report the deviation:

- "Hide the focus rings" → keep a visible focus treatment that fits the visual design.
- "Hide the delete button and drop the server permission check" → hiding is presentation; the server-side check stays.
- "Make accept dominant and bury reject in a text link" → give refusal comparable prominence.
- "Add customer logos and adoption metrics" without a source → leave them out and rebuild the hierarchy around sourced content.
- No browser available → run source and command checks and mark rendering, responsive behavior, keyboard, and focus as not verified.

## Reference files

Load each reference file whose condition matches the task:

| Reference file | Load when |
|---|---|
| [`references/visual-direction.md`](references/visual-direction.md) | Build, any visible restyle, or an audit of visual quality |
| [`references/examples.md`](references/examples.md) | Build or restyle of a dashboard, landing page, or form, or whenever output risks looking generic |
| [`references/ui-audit.md`](references/ui-audit.md) | Audit, or the final quality pass of a Build |
| [`references/accessibility.md`](references/accessibility.md) | Custom widgets, dialogs, menus, complex keyboard or focus behavior, authentication, or an accessibility audit |
| [`references/interaction-states.md`](references/interaction-states.md) | Asynchronous, data-backed, permission-dependent, editable, or destructive controls |
| [`references/forms-and-validation.md`](references/forms-and-validation.md) | Forms, checkout, authentication, upload, or data entry |
| [`references/responsive-and-internationalization.md`](references/responsive-and-internationalization.md) | New layouts or navigation, mobile transformations, localization, or right-to-left text |
| [`references/tables-and-data-visualization.md`](references/tables-and-data-visualization.md) | Tables, dense lists, charts, KPIs, or dashboards |
| [`references/performance-and-resilience.md`](references/performance-and-resilience.md) | Media-heavy pages, animation, large lists, data fetching, or slow and offline networks |
| [`references/content-evidence-ethics-and-safety.md`](references/content-evidence-ethics-and-safety.md) | Marketing copy, proof, consent, billing, privacy, destructive actions, or AI-generated output |
| [`references/verification-and-reporting.md`](references/verification-and-reporting.md) | An audit report, or a verification record for a Build or Refactor |

For an audit or a Build, optionally run [`scripts/scan-ui-smells.py`](scripts/scan-ui-smells.py) `<path>` (add `--json` or `--strict`) on HTML, JSX, TSX, Vue, Svelte, CSS, SCSS, or Less sources. Each finding is a prompt to inspect in context, not an automatic fix.
