# Calibration examples

Use these examples when mode, scope, fidelity, brand, fixture, or conflict handling is ambiguous.

## 1. Read-only audit

- **Request:** Audit checkout and return findings only.
- **Mode:** `AUDIT`.
- **Scope:** Checkout surfaces and directly observable dependencies; no product-file changes.
- **References:** UI audit, accessibility, forms, states, content safety, verification.
- **Must do:** Prioritize evidenced findings and label unverified behavior.
- **Prohibited:** Implementing corrections or treating a heuristic as change authority.

## 2. Explicit narrow fix

- **Request:** Use `$devibify` to fix one button's focus state.
- **Mode:** `NARROW_FIX`.
- **Scope:** The button primitive or local style and affected test only.
- **References:** Accessibility; UI audit only for the surrounding affordance if needed.
- **Must do:** Preserve the visual system and test keyboard focus.
- **Prohibited:** Redesigning the page or changing global tokens for a local defect.

## 3. Feature form

- **Request:** Implement an account settings form.
- **Mode:** `FEATURE_IMPLEMENTATION`.
- **Scope:** Form, real data contract, submission path, and relevant tests.
- **References:** Forms, states, accessibility, responsive, verification, content safety.
- **Must do:** Cover validation, pending, error, success, duplicate protection, keyboard, focus, and value preservation.
- **Prohibited:** Showing success before the underlying action succeeds.

## 4. Unconstrained net-new design

- **Request:** Design a new onboarding flow with no supplied reference.
- **Mode:** `NET_NEW_DESIGN`.
- **Scope:** Approved onboarding flow and necessary primitives.
- **References:** UI audit, accessibility, states, responsive, content safety, verification.
- **Must do:** Compare two structurally different directions and choose from product evidence.
- **Prohibited:** Comparing color-only variants or inventing proof.

## 5. Reference fidelity

- **Request:** Match an approved Figma selection.
- **Mode:** `REFERENCE_FIDELITY`.
- **Scope:** Referenced surface, responsive adaptations, and required behavior.
- **References:** UI audit, accessibility, responsive, verification.
- **Must do:** Preserve hierarchy and intent, compare at the target viewport, and record accessibility or system deviations.
- **Prohibited:** Unrelated visual exploration.

## 6. Expressive or maximalist brand

- **Request:** Improve a campaign page while keeping its maximalist art direction.
- **Mode:** `FEATURE_IMPLEMENTATION` or `REFACTOR`, based on behavior authority.
- **Scope:** Requested campaign surface.
- **References:** UI audit, accessibility, responsive, performance, verification.
- **Must do:** Preserve expressive character while fixing hierarchy, behavior, performance, and accessibility.
- **Prohibited:** Converting the brand into muted enterprise minimalism.

## 7. Prototype with fixtures

- **Request:** Prototype a reporting dashboard before APIs exist.
- **Mode:** `NET_NEW_DESIGN`.
- **Scope:** Development-only prototype.
- **References:** Tables and visualization, content safety, states, responsive.
- **Must do:** Label synthetic data as fixture data and keep it non-sensitive.
- **Prohibited:** Presenting fixtures as production metrics or inventing backend success.

## 8. Accessibility conflict

- **Request:** Remove all visible focus indicators for visual cleanliness.
- **Mode:** `NARROW_FIX`.
- **Scope:** Focus styling on the requested surface.
- **References:** Accessibility and calibration.
- **Must do:** Preserve the visual intent with an accessible focus treatment and report the conflict.
- **Prohibited:** Silently weakening keyboard access.

## 9. No browser available

- **Request:** Finish and verify a page in an environment without a browser.
- **Mode:** Match the implementation scope.
- **Scope:** Requested surface and repository-local verification.
- **References:** Verification plus applicable domain references.
- **Must do:** Run executable and source checks and label browser behavior unverified.
- **Prohibited:** Claiming rendered, responsive, or keyboard behavior was observed.

## 10. Shared component refactor

- **Request:** Consolidate duplicated dialog implementations.
- **Mode:** `REFACTOR`.
- **Scope:** Shared dialog, consumers, and representative route tests.
- **References:** Accessibility, states, UI audit, verification.
- **Must do:** Identify consumers and verify representative routes and focus behavior.
- **Prohibited:** Changing user-visible behavior without authorization.
