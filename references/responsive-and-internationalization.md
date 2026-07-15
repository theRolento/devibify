# Responsive behavior and internationalization

## Responsive principles

- Choose breakpoints from content pressure rather than device names.
- Define intentional narrow, intermediate, and wide behavior.
- Inspect very narrow reflow at 320 CSS pixels where applicable.
- Prevent accidental horizontal page scroll; preserve intentional overflow for tables, code, timelines, maps, and other two-dimensional content.
- Keep primary actions accessible.
- Let headings, labels, controls, badges, and errors wrap without clipping.
- Avoid fixed-height text containers that fail under wrapping.
- Keep sticky surfaces from obscuring focused content.
- Preserve usable touch targets.
- Check that mobile keyboards do not hide active fields or submission controls when testable.
- Respect safe-area insets where fixed UI meets viewport edges.
- Consider landscape and short-height viewports for full-screen surfaces.
- Keep reduced-motion and low-power behavior functional.

## Stress content

Test applicable layouts with long headings, long button labels, long names, unbroken identifiers and URLs, zero/one/many items, long errors, substantially expanded translated strings, variable row heights, and large localized numbers.

## Zoom and text

Use source or browser inspection to check 200 percent text size, zoom and reflow at the WCAG-equivalent narrow viewport, user text-spacing overrides, and browser minimum font settings where practical.

## Internationalization

- Preserve the repository's localization framework.
- Keep translated messages whole; avoid concatenating fragments.
- Use pluralization and message-formatting utilities.
- Format dates, times, numbers, percentages, and currencies with locale-aware APIs.
- Display the time zone when ambiguity affects meaning.
- Avoid hardcoded month, day, decimal, and currency formats.
- Set `lang` and `dir` correctly.
- Prefer logical properties such as inline-start and inline-end.
- Inspect right-to-left layout when the product supports it.
- Mirror directional controls only when their semantics require it.
- Keep logos, media, charts, and nondirectional symbols in their intended orientation.
- Isolate bidirectional user content safely.
- Tolerate substantial text expansion.
- Preserve accessible names after translation.
- Keep localizable text out of images when localization is expected.

## Responsive evidence

Name the viewport widths, zoom levels, text conditions, directions, or content stresses actually inspected. A bare claim that the UI is "responsive" is not evidence.
