# Performance and resilience

## Rendering and dependency discipline

- Preserve the repository's rendering strategy.
- Keep server-rendered content on the server unless client rendering serves a demonstrated need.
- Avoid unnecessary client-side JavaScript.
- Reuse existing dependencies and primitives.
- Add no UI, icon, animation, form, chart, or styling library when current tools are adequate.
- Keep local needs free of expensive abstractions.
- Inspect bundle or build output with existing tooling unless scope authorizes more.

## Media and layout stability

- Reserve image and media dimensions.
- Use responsive images when supported.
- Load a likely LCP image eagerly enough for the product context.
- Lazy-load noncritical media appropriately.
- Bound video and animation costs.
- Prevent layout shifts from late content, fonts, banners, and state changes.
- Prefer transform and opacity for motion over layout-inducing properties.
- Keep fixed layers from causing overlap or jank.

## Data and interaction performance

- Avoid accidental request waterfalls.
- Cancel or ignore stale requests.
- Deduplicate requests with repository patterns.
- Use transitions or deferred rendering only when supported and useful.
- Virtualize only genuinely large lists.
- Prevent rerender loops and unstable keys.
- Inspect long tasks and delayed interactions when tooling permits.
- Keep near-instant operations free of flashing skeletons.
- Keep progress truthful for long operations.

## Core Web Vitals

When field or lab measurement exists, use these current good targets:

- LCP at or below 2.5 seconds;
- INP at or below 200 milliseconds;
- CLS at or below 0.1;
- field data evaluated at the 75th percentile.

Local source inspection cannot establish field performance. Label measured values as measurement and source-level conclusions as inference.

## Resilience

Exercise applicable slow-network, failed-request, retry, cancellation, timeout, offline, stale-content, authentication-expiry, permission-change, back/forward, reload, deep-link, partial-success, conflict-resolution, and recovery behavior. Preserve data unless product or security requirements make disposal necessary.

## Runtime hygiene

When observable, inspect console errors, hydration warnings, failed network requests, unhandled promise rejections, layout shifts, broken images or fonts, repeated requests, and runaway animation or memory behavior.
