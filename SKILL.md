---
name: devibify
description: "Devibify frontend UI through disciplined product design and verification. Use for implementation, refactoring, or review of web interfaces—including components, forms, tables, dashboards, and landing pages—when the work needs coherent design-system choices, specific copy, complete interaction and data states, responsive behavior, accessibility, or removal of generic AI-looking patterns."
---

# Devibify

Treat the interface as a product system shaped by its users, content, and workflows. Make it specific, coherent, complete, and verifiable.

## Workflow

### 1. Inspect the product before designing

- Read repository guidance, relevant routes, neighboring screens, shared components, tokens, and project scripts.
- Identify the user, their primary task, the real content or data, and the product constraints.
- Reuse established patterns that support the task; note inconsistencies that the requested scope can safely correct.

Proceed when you can name the primary task, content source, reuse targets, required behavior, and available verification path.

### 2. Define the UI contract

For non-trivial work, establish:

- the page purpose, information hierarchy, and primary action
- the layout regions and component inventory
- the interaction and data states that can occur
- the narrow, medium, and wide layout transformations
- the typography, spacing, color, radius, border, elevation, and motion constraints
- the copy, semantics, keyboard flow, focus behavior, and error communication

Keep the contract proportional for a small change. Proceed when every visible region and control has a purpose, every asynchronous or data-backed area has an outcome for each reachable state, and the layout has defined behavior at narrow and wide widths.

### 3. Establish the smallest coherent visual system

- Preserve the existing system when it is coherent.
- When no system exists, define one spacing scale, one type ramp, a small semantic palette, and restrained rules for radius, borders, elevation, and motion.
- Build hierarchy with layout, spacing, typography, and contrast first. Reserve color, motion, and elevation for meaning and state.
- Derive new components from shared primitives and tokens instead of one-off values.

Proceed when every new visual choice belongs to the existing system or the compact system defined for the work.

### 4. Implement product behavior

- Use semantic controls and elements for their intended behavior.
- Give links valid destinations and controls complete interactions, including keyboard operation and visible focus.
- Represent applicable default, hover, focus, active, selected, disabled, pending, loading, empty, error, and success states.
- Show immediate pending feedback for asynchronous actions and guard against duplicate submission.
- Preserve layout while data loads, make errors recoverable, and give empty states a useful next action.
- Include page metadata and other framework-supported page basics for page-level work.

Proceed when every visible control works and every reachable interaction or data state has an intentional result.

### 5. Run the devibify audit

For a UI review or a non-trivial page or screen change, read [`references/ui-audit.md`](references/ui-audit.md) in full. For a narrow component change, read the sections that match the component and its surrounding surface. Apply every relevant check; fix each failure or identify the project or user constraint that requires it.

The audit is complete only when composition, visual system, content integrity, component behavior, responsive behavior, accessibility, and technical completeness have all been considered.

### 6. Verify with evidence

- Run the repository's relevant formatting, lint, typecheck, test, and build commands.
- Exercise the main flow and all changed controls in a browser when the environment supports it.
- Check representative narrow mobile, intermediate, and desktop widths; add very narrow or wide cases when the layout is sensitive.
- Check keyboard completion, focus visibility, labels and error associations, readable contrast, reduced motion, and intentional overflow.
- Inspect the changed surface for placeholders, invented proof, dead links, inert controls, and state-dependent layout shifts.

Finish only when the requested behavior is evidenced by executable checks or direct inspection. If a check cannot run, report the exact gap, cause, and remaining risk.

## Decision standard

Prefer the quietest design that makes the product's hierarchy and state obvious. Add a visual device only when it communicates structure, affordance, status, or brand character that simpler means cannot express. The result should feel native to this product, not interchangeable with a stock SaaS template.
