# Calibration examples

Use these examples when mode, scope, fidelity, brand, fixture, or conflict handling is ambiguous.

| Request | Mode and scope | Required handling |
|---|---|---|
| Audit checkout; return findings only | `AUDIT`; checkout and observable dependencies | Prioritize evidenced findings, label gaps, and leave product files unchanged. |
| Fix one button's focus state | `NARROW_FIX`; button primitive or local style and affected test | Preserve the visual system and verify keyboard focus. Do not redesign the page or change global tokens for a local defect. |
| Implement an account settings form | `FEATURE_IMPLEMENTATION`; form, data contract, submission path, and tests | Cover validation, pending, error, success, duplicate protection, keyboard, focus, and value preservation. Show success only after the action succeeds. |
| Design onboarding without a reference | `NET_NEW_DESIGN`; approved flow and necessary primitives | Compare two structural directions using product evidence. Do not compare color-only variants or invent proof. |
| Match an approved Figma selection | `REFERENCE_FIDELITY`; referenced surface, responsive adaptations, and behavior | Preserve hierarchy and intent, compare at the target viewport, and record accessibility or system deviations. |
| Improve a maximalist campaign page | `FEATURE_IMPLEMENTATION` or `REFACTOR`; requested campaign surface | Preserve the expressive brand while fixing evidenced hierarchy, behavior, performance, and accessibility failures. |
| Prototype a dashboard before APIs exist | `NET_NEW_DESIGN`; development-only prototype | Label non-sensitive synthetic data as fixtures. Do not present fixtures as production metrics or invent backend success. |
| Remove visible focus indicators | `NARROW_FIX`; requested focus styling | Keep an accessible focus treatment and report the conflict. |
| Verify a page without a browser | Mode and scope follow the implementation request | Run repository-local executable and source checks. Mark rendering, responsive behavior, keyboard behavior, and focus as unverified. |
| Consolidate duplicated dialogs | `REFACTOR`; shared dialog, consumers, and representative route tests | Identify consumers and verify representative routes and focus behavior. Preserve user-visible behavior. |
