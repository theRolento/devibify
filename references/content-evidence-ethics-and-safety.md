# Content, evidence, ethics, and safety

## Product copy

- Use concrete nouns and verbs from the product domain.
- Make labels state the action and consequence.
- Prefer utility copy in operational products.
- Describe actual product value instead of abstract promises.
- Keep microcopy calm and brief.
- Keep prompts, design commentary, and implementation notes out of the UI.
- Remove repeated generic benefit claims.
- Verify legal, footer, contact, copyright, and metadata content when present.

## Evidence and proof

- Trace testimonials, logos, reviews, metrics, charts, avatars, and activity to an attributable source.
- Omit proof when evidence is unavailable.
- Label fixtures as synthetic or demo data.
- Keep decorative UI from impersonating measurement.
- Keep fabricated customer counts and urgency out of the interface.
- Keep code fixtures from being presented as production metrics.

## Ethical UX

Reject fabricated urgency or scarcity, confirmshaming, hidden fees or recurring charges, obscured cancellation, preselected invasive consent, asymmetric accept/reject prominence, disguised advertising, sneaked items or subscriptions, misleading labels, ambiguous destructive consequences, unjustified forced accounts, misleading privacy settings, and false success.

Show costs, recurring commitments, consequences, cancellation paths, and data-sharing choices before commitment. Make refusal and reversal proportional to acceptance.

## Privacy

- Minimize collected and displayed data.
- Keep production personal data out of fixtures.
- Keep secrets, tokens, credentials, and private identifiers out of UI, logs, source, screenshots, and URLs.
- Use appropriate masking and reveal behavior.
- Make privacy choices reflect real product behavior.
- Collect only fields the product needs.
- Preserve repository consent and retention patterns.
- Keep authorization-protected data out of client bundles.

## Security-adjacent UI behavior

- Treat hidden controls as presentation, never authorization.
- Preserve server-side permission checks and role boundaries.
- Use only established roles and permissions.
- Follow repository sanitization patterns for user-generated rich content.
- Identify external links and use the repository's safe-link behavior.
- Make dangerous actions and consequences explicit.
- Prefer undo or recovery when practical.
- Keep sensitive input out of logs.
- Replace raw internal errors and stack traces with safe, useful messages.
- Report that a visual review is not a security audit.

## AI-mediated interfaces

When the product presents AI-generated output:

- distinguish generated content from authoritative product data;
- show pending, partial, failed, and cancelled generation states;
- represent certainty and external actions truthfully;
- preserve review, edit, retry, and undo where appropriate;
- show sources or provenance when the product supports them;
- make destructive tool actions explicit;
- protect prompts and generated content under repository policy.
