# UI audit

Apply these checks to the actual product context; product requirements and an established design system outrank generic defaults. A failed heuristic is evidence to investigate, not authorization to change code.

## Product fit and primary task

- Identify the primary user, task, and next action from evidence.
- Order information around the task, not a generic page type.
- Match density to task frequency and user expertise.
- Give each section and component one clear responsibility.
- Make dashboards support decisions or monitoring rather than component count.
- Make landing pages express real value, brand, and attributable proof.
- Start operational pages with the working surface rather than a marketing hero.

## Information architecture and composition

- Confirm navigation communicates current location and reachable destinations.
- Group by user task and relationship.
- Preserve comparison where it matters, especially in dense lists and tables.
- Keep one primary action hierarchy per view.
- Report regions that support no task, explanation, decision, or narrative.

## Existing-system reuse

- Reuse existing components and tokens before creating new ones.
- Put a new variant in a shared primitive only when repeated use is real.
- Keep a local fix local, without global style drift.
- Keep icon families, radii, shadows, field heights, and spacing coherent unless a product reason justifies variation.
- Justify each new dependency against existing primitives and the actual need.
- Identify the consumers and blast radius of every changed shared component.

## Visual quality

Apply `visual-direction.md`: the generic-default table, hierarchy, and the fallback defaults where no system exists. Check that semantic colors carry consistent meaning with adequate contrast, that glyph size and target size are separate decisions, and that fixed or floating elements never obscure content or focus.

## Specialized checks

Use the sibling reference files for their areas: `accessibility.md`, `interaction-states.md`, `forms-and-validation.md`, `responsive-and-internationalization.md`, `tables-and-data-visualization.md`, `performance-and-resilience.md`, and `content-evidence-ethics-and-safety.md`. Load only those the audited surface touches.

## Severity

- **Blocker:** the primary task cannot be completed, or a material security, privacy, legal, deceptive-design, or severe accessibility issue exists.
- **High:** a major flow, state, responsive, data-integrity, or accessibility failure exists.
- **Medium:** substantial friction, inconsistency, or maintenance risk exists.
- **Low:** a localized polish or minor consistency issue exists.
- **Opportunity:** an optional enhancement not required for correctness.

## Finding format

Order findings by severity. Record each one as:

```md
### [ID] [Severity] Title

- Category:
- Location:
- Observed evidence:
- User or product impact:
- Concrete correction:
- Scope status: requested, necessary dependency, or adjacent issue
- Verification status:
```
