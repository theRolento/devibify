# UI Audit

Use this audit to review an existing interface or to run the final pass on a non-trivial implementation. Apply each relevant check to the actual product context; product requirements and an established design system outrank generic defaults.

## Product fit and composition

- Make the primary task and next action obvious before secondary information.
- Match information density to the job: compact for operational tools, more paced for explanatory pages.
- Keep navigation, containers, alignment, and component placement stable across related screens.
- Use cards only to group related content. Prefer sections, lists, or tables when they express the structure more clearly.
- Use dashboards to support decisions and actions. Add metrics, charts, side rails, and filters only when real data and user needs justify them.
- Let landing-page composition follow the actual value proposition and proof available.

Replace generic compositions with product-shaped ones:

- Replace an internal-tool hero with a useful title, context, and actions.
- Replace an automatic KPI-card grid with the decisions, trends, or queues the user needs.
- Replace floating sidebars and decorative rails with stable navigation and purposeful secondary content.
- Replace centered walls of text and dead luxury space with readable measures and useful hierarchy.
- Replace nested card stacks with fewer, clearer regions.

## Visual system

- Use the project's existing tokens before adding values.
- Keep spacing on one established 4px or 8px rhythm, with exceptions justified by alignment or content.
- Maintain a compact type hierarchy with readable body weight, line height, and line length.
- Use a small semantic palette with sufficient contrast for text, controls, focus, and disabled states.
- Keep related buttons, inputs, cards, panels, and dialogs on the same radius, border, and elevation logic.
- Prefer spacing, borders, and tonal contrast to heavy shadows.
- Keep icons subordinate to their labels, normally 16–20px in product UI, with a consistent family and stroke.
- Use motion to explain cause, response, or state change; keep it subtle and compatible with reduced-motion preferences.

Replace decoration without product meaning:

- Replace arbitrary gradients, neon, glow haze, bokeh, glass effects, and conic flourishes with the product palette and clear hierarchy.
- Replace decorative sparkles and emoji with useful copy or a consistent icon when one is needed.
- Replace ubiquitous pills, oversized radii, and colored shadows with restrained component geometry.
- Replace lift, tilt, bounce, wiggle, parallax, and layout-shifting hovers with stable color, border, or opacity feedback.
- Replace generic dark-SaaS styling with a direction grounded in the product and brand.

## Components and states

- Buttons expose primary, secondary, destructive, disabled, focus, and pending behavior where applicable; comparable actions share height and padding.
- Forms use persistent labels, useful descriptions, visible focus, field-associated errors, and guarded submission.
- Navigation exposes a clear current location and uses badges only for real, useful counts or state.
- Tables and dense lists prioritize scanability, disciplined columns, meaningful sorting or filtering, and graceful narrow-width behavior.
- Tabs switch content, accordions open, menus support keyboard use, and dialogs close, manage focus, and return focus appropriately.
- Loading states preserve the eventual layout. Empty states explain the condition and offer a relevant action. Errors are visible, specific, and recoverable.
- Status badges communicate real status; repeated decorative chips become plain text or a clearer grouping.

## Content integrity

- State what the product does, who it serves, and what changes for the user with concrete nouns and verbs.
- Replace abstract promises such as “launch faster” or “create without limits” with the actual workflow or outcome.
- Use labels and button text that describe the action; keep microcopy calm and brief.
- Use attributable testimonials, logos, metrics, charts, avatars, activity, and social proof. Omit them when evidence is unavailable.
- Use real links and destinations. Keep scaffolding visibly identified during development and remove it from the finished surface.
- Keep footer, copyright, legal text, and contact details accurate.

## Responsive behavior and accessibility

- Preserve hierarchy and access to primary actions across narrow, intermediate, and wide layouts.
- Reflow dense regions intentionally; avoid accidental horizontal page scroll, clipped text, awkward full-width buttons, and unreadable columns.
- Let headings, labels, controls, and translated or long content wrap without overlap.
- Use native semantics first. Give controls accessible names and make the main flow keyboard-completable.
- Keep focus visible, associate labels and errors with inputs, announce asynchronous results when needed, and maintain readable contrast.
- Make touch targets usable and keep hover-only information available through focus or persistent content.

## Page completeness

- Provide a meaningful title, meta description, favicon, and social metadata when the framework and project support them.
- Verify every visible link, button, tab, menu, dialog, form, toggle, and disclosure.
- Verify pending, loading, empty, error, disabled, selected, and success states that the changed surface can reach.
- Remove placeholder text, images, avatars, test labels, dead `#` destinations, and inert controls from the finished surface.
- Confirm that no decorative element impersonates data, proof, navigation, or functionality.

## Audit result

For a review-only request, report findings by impact, cite the affected element or file, and give a concrete correction. Distinguish observed failures from suggestions and from items that could not be verified. For implementation work, fix in-scope failures before presenting the result and disclose any remaining constraints.
