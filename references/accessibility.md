# Accessibility

## Baseline

Default production web UI to WCAG 2.2 Level AA. Apply stricter repository, contractual, or jurisdictional requirements when present. Use native HTML before ARIA, and use ARIA only when native semantics are insufficient. Follow the WAI-ARIA Authoring Practices for custom widgets; ARIA semantics alone do not implement keyboard behavior.

Automated tools identify only some failures and do not establish conformance. Reserve claims such as "fully accessible" for evidence that actually supports them.

## Structure and semantics

- Set the document language and a meaningful page title.
- Use landmarks, logical headings, lists, and genuine table structures.
- Use native buttons for actions and links for navigation.
- Give controls and regions accessible names and descriptions.
- Use persistent form labels, field groups, fieldsets, and legends where applicable.
- Expose current, selected, checked, pressed, expanded, invalid, and busy states correctly.
- Provide a skip or bypass mechanism when repeated content warrants it.

## Keyboard

- Complete the primary flow with a keyboard and confirm there are no traps.
- Preserve a predictable tab order.
- Preserve native Enter and Space behavior.
- Implement required arrow-key behavior for composite widgets.
- Let Escape dismiss overlays when the interaction pattern calls for it.
- Keep positive `tabindex` out of the flow unless an exceptional documented pattern requires it.
- Replace click-only `div` or `span` controls with semantic controls.

## Focus

- Keep a visible focus indicator.
- Keep sticky headers, footers, banners, and overlays from obscuring focus.
- Place focus sensibly after route changes, dialog opening, validation failure, and destructive events.
- Contain focus inside modal dialogs and return it to the invoking control.
- Keep focus and selection visually distinct where both exist.
- Preserve focus through asynchronous rerenders.

## Perceivability

- Give meaningful images useful alternative text and decorative images empty alternatives.
- Provide captions, transcripts, or alternatives for media when required.
- Meet WCAG text contrast and non-text contrast thresholds.
- Communicate state with more than color.
- Name icon-only controls accessibly.
- Keep text over media readable in every reachable state.

## Reflow, zoom, and text adaptation

- Preserve content and function at 200 percent text resize.
- Reflow at the equivalent of 320 CSS pixels where applicable.
- Avoid general horizontal page scrolling; allow it for inherently two-dimensional content.
- Tolerate WCAG text-spacing overrides.
- Avoid fixed heights that clip enlarged, wrapped, or translated text.

## Targets and pointer behavior

- Meet the 24 by 24 CSS pixel target minimum or a valid spacing exception.
- Treat target size independently from visible glyph size.
- Expose hover-only content on focus or persistently.
- Make hover or focus content dismissible, hoverable, and persistent where required.
- Provide a non-drag alternative when required.
- Consider pointer cancellation and accidental activation.

## Motion and timing

- Honor `prefers-reduced-motion`.
- Preserve understandable state changes without motion.
- Avoid flashing content.
- Communicate timeouts and expiring sessions and provide recovery where possible.

## Status and errors

- Announce asynchronous status without disruptive focus changes when appropriate.
- Associate errors with fields and communicate them with text, not color alone.
- Give success, warning, and failure states meaningful text.
- Use live regions sparingly and deliberately.

## Accessible authentication

- Allow password managers and paste.
- Avoid memory tests or puzzles without alternatives.
- Use correct autocomplete tokens.
- Give reveal-password controls state-specific accessible names.

## Verification matrix

Record each applicable row separately; never substitute one method for another.

| Method | What it can evidence | Result |
|---|---|---|
| Source inspection | Semantics, attributes, relationships, likely behavior | |
| Automated accessibility scan | Tool-detectable violations in exercised states | |
| Keyboard inspection | Order, operation, traps, dismissal | |
| Focus inspection | Visibility, placement, containment, return | |
| Screen-reader inspection, if performed | Names, roles, states, announcements, reading order | |
| Zoom and reflow inspection | Text resizing, 320 CSS pixel reflow, clipping, overflow | |
| Not verified | Exact method and residual risk | |
