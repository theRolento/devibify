# Verification and reporting

## Evidence types

- **Executed automated check:** A command or test was run and its exact result was observed.
- **Browser-observed:** Behavior was directly exercised in a rendered browser.
- **Visual inspection:** Layout or fidelity was directly inspected.
- **Keyboard and focus inspection:** Interaction was exercised without a pointer.
- **Automated accessibility check:** An accessibility tool was run.
- **Source inspection:** Code or configuration was directly inspected.
- **Inference:** A reasoned conclusion was not directly executed or observed.
- **Not verified:** Environment or scope prevented validation.

## Command checks

Discover commands from repository scripts and guidance. Use applicable formatting, lint, typecheck, unit, component, end-to-end, production build, framework, and skill validation commands. Record exact commands and results. Do not invent command names.

## Browser checks

When browser capability exists:

- load the changed route and exercise the primary flow;
- exercise every changed control and reachable state;
- inspect a very narrow or mobile, intermediate, and desktop width;
- inspect the exact target viewport in fidelity mode;
- inspect keyboard flow and focus;
- inspect console and failed requests when possible;
- capture screenshots only when they add useful evidence.

Prefer an existing Playwright or equivalent setup. Add no persistent dependency for a single verification run without authorization.

## Accessibility verification

- Complete the main flow manually with a keyboard.
- Inspect focus visibility, placement, containment, and return.
- Inspect labels and error associations.
- Review contrast and non-color state communication.
- Inspect reflow or zoom where relevant.
- Inspect reduced-motion behavior when motion changed.
- Run existing automated accessibility checks when available.
- Keep automation-only results separate from conformance claims.

## Completion report template

```md
## Result

- Mode:
- Requested outcome:
- In-scope surface:
- Out-of-scope findings:

## Changed files or audit locations

- ...

## Product and design decisions

- ...

## Facts, assumptions, unknowns, and fixtures

- Observed:
- Inferred:
- Unknown:
- Fixtures:

## Verification

| Check | Evidence type | Result | Details |
|---|---|---|---|
| ... | ... | ... | ... |

## Accessibility and responsive checks

- ...

## Not verified and residual risk

- ...

## Adjacent issues not changed

- ...
```

## Audit finding template

```md
### [ID] [Severity] Title

- Category:
- Location:
- Observed evidence:
- User or product impact:
- Concrete correction:
- Scope status:
- Verification status:
```

## Claim boundaries

Reserve claims such as "fully accessible," "production-ready," "pixel-perfect," "responsive across all devices," "performance optimized," "no regressions," "all controls work," "secure," and "compliant" for evidence that supports their full scope.

Prefer bounded claims such as:

- passed the repository typecheck and build;
- exercised the primary flow at 320px, 768px, and 1440px;
- the existing automated accessibility test reported no violations, with manual screen-reader testing not performed;
- matched the supplied reference at the target viewport with the listed deviations.
