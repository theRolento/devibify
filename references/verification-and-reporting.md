# Verification and reporting

## Evidence types

- **Executed check:** a command or test ran and its exact result was observed.
- **Browser-observed:** behavior was exercised in a rendered browser, including visual, keyboard, and focus inspection.
- **Automated accessibility check:** an accessibility tool ran on the exercised states; it finds only some failures and never establishes conformance.
- **Source inspection:** code or configuration was read directly.
- **Inference:** a reasoned conclusion not directly executed or observed.
- **Not verified:** the environment or scope prevented validation; name the cause and the residual risk.

Record each method separately; one never substitutes for another.

## Command checks

Discover commands from repository scripts and guidance: formatting, lint, typecheck, unit, component, end-to-end, production build, and framework checks. Record exact commands and results.

## Browser checks

- Load the changed route and exercise the primary flow.
- Exercise every changed control and reachable state.
- Inspect 320px, an intermediate width, and a wide desktop width, plus the exact viewport of an authoritative design reference.
- Complete the main flow with a keyboard, and inspect focus visibility, placement, containment, and return.
- Inspect labels, error associations, contrast, and non-color state communication.
- Inspect zoom and reflow where layout changed, and reduced-motion behavior where motion changed.
- Inspect console errors and failed requests.
- Capture screenshots when they add evidence.

Prefer the repository's existing Playwright or equivalent setup, and run existing automated accessibility checks when available. A single verification run needs no new persistent dependency.

## Bounded claims

Write claims that name their evidence:

- passed the repository typecheck and build;
- exercised the primary flow at 320px, 768px, and 1440px;
- the existing automated accessibility test reported no violations; manual screen-reader testing not performed;
- matched the supplied design reference at the target viewport with the listed deviations.
