# UI audit

## Audit application and scope

Apply these checks to the actual product context. Product requirements and an established design system outrank generic defaults. Fix only failures in requested or necessary dependency scope and regressions introduced by the change. Report adjacent pre-existing failures separately. A failed heuristic is evidence to investigate, not automatic authorization to change code.

For specialized checks, load the applicable sibling reference named in `SKILL.md`. Do not convert a read-only audit into implementation.

## Product fit and primary task

- Identify the primary user, task, and next action from evidence.
- Order information around the task, not a generic page type.
- Match density to task frequency and user expertise.
- Keep navigation, containers, and patterns stable across related screens.
- Give each section and component one clear responsibility.
- Make dashboards support decisions or monitoring rather than component count.
- Make landing pages express real value, brand, and attributable proof.
- Start operational pages with the working surface rather than a marketing hero.
- Use hierarchy and useful content instead of decorative whitespace.

## Information architecture and composition

- Confirm navigation communicates current location and reachable destinations.
- Group by user task and relationship; avoid card boundaries as the primary hierarchy system.
- Preserve comparison where it matters, especially in dense lists and tables.
- Keep primary actions accessible without competing action hierarchies.
- Remove or report regions that do not support a task, explanation, decision, or narrative.

## Existing-system reuse and dependency discipline

- Reuse existing components and tokens before creating new ones.
- Put a new variant in a shared primitive only when repeated use is real.
- Prevent a local fix from causing global style drift.
- Keep icon families, radii, shadows, field heights, and spacing systems coherent unless a product reason justifies variation.
- Justify each new dependency against existing primitives and the actual need.
- Identify the consumers and blast radius of every changed shared component.

## Visual hierarchy and visual-system coherence

- Use the established spacing scale. When none exists, define a small coherent scale normally based on a 4px unit.
- Document optical or content-driven exceptions instead of introducing random values.
- Keep type hierarchy, measure, line height, and weight readable.
- Give semantic colors clear meaning and adequate contrast.
- Treat glyph size and interactive target size as separate decisions.
- Keep borders, elevation, radius, and motion consistent.
- Make motion communicate cause, response, hierarchy, or brand.
- Keep fixed and floating elements from obscuring content or focus.

Prefer the least visual complexity needed to make hierarchy, behavior, state, and intended brand character clear. Restraint is a tool, not a mandate to suppress expression.

## Brand specificity and anti-homogenization

Investigate these high-frequency defaults when they lack product rationale:

- automatic KPI rows, stock dashboards, and admin templates;
- card mosaics, nested cards, pill soup, and decorative badges;
- arbitrary gradients, glow, glass, blur, or generic dark SaaS styling;
- unsupported logos, avatars, testimonials, charts, metrics, or activity;
- decorative sidebars, floating rails, and overbuilt heroes;
- repeated identical section compositions and generic placeholder claims;
- surface-only variants that leave information architecture unchanged;
- an unrequested redesign of an established product surface.

Unusual, maximalist, or expressive styles pass when they are intentional, coherent, usable, and product-specific.

## Specialized audit checks

- For controls, reachable states, forms, and data displays, use `interaction-states.md`, `forms-and-validation.md`, and `tables-and-data-visualization.md` as applicable.
- For product language, claims, fixtures, consent, billing, privacy, and safety, use `content-evidence-ethics-and-safety.md`.
- For viewport behavior, localization, semantics, keyboard access, focus, labels, and non-color cues, use `responsive-and-internationalization.md` and `accessibility.md`.
- For runtime, metadata, rendering, dependency, media, and resilience checks, use `performance-and-resilience.md`; classify completion evidence with `verification-and-reporting.md`.

## Audit severity and output

- **Blocker:** The primary task cannot be completed, or a material security, privacy, legal, deceptive-design, or severe accessibility issue exists.
- **High:** A major flow, state, responsive, data-integrity, or accessibility failure exists.
- **Medium:** Substantial friction, inconsistency, or maintenance risk exists.
- **Low:** Localized polish or minor consistency issue exists.
- **Opportunity:** An optional enhancement is not required for correctness.

Record every finding with:

- ID;
- severity;
- category;
- location;
- observed evidence;
- user or product impact;
- concrete correction;
- scope status;
- verification status.
