# Tables and data visualization

## Table semantics and structure

- Use a table for genuinely tabular relationships, never page layout.
- Add a meaningful caption when users need it.
- Identify row and column headers correctly.
- Use `scope` or equivalent associations for simple tables and explicit relationships for complex tables.
- Keep column ordering stable.
- Show units, time context, numeric alignment, and appropriate precision.

## Table behavior

- Expose sort state and keyboard operation.
- Make active filters visible.
- Communicate pagination and result counts.
- Keep selection and bulk-action state accurate.
- Represent loading, empty, error, partial, stale, and permission states.
- Keep sticky headers from obscuring focus.
- Make row actions discoverable and keyboard accessible.
- Use virtualization only when data size justifies it and semantics remain usable.
- Offer exports only when real product behavior supports them.

## Narrow widths

Choose and test one explicit strategy:

- horizontal scrolling with preserved headers and context;
- priority columns with a details view;
- progressive disclosure;
- a transformed list whose relationships remain understandable.

Preserve comparison. Converting every table row into a card is not an acceptable default when it destroys tabular relationships.

## Charts and metrics

- Use real data or clearly labelled fixture data.
- Show source or provenance, time range, freshness, and units.
- Use honest axes and scales.
- Explain missing and partial data.
- Tie each trend line and metric to a real task or decision.
- Avoid unsupported extrapolation.
- Distinguish series with labels, shapes, patterns, or direct annotation where color alone is insufficient.
- Make interactive charts keyboard accessible.
- Provide a textual summary or data table for essential information.
- Keep important values available outside tooltips.
- Explain truncation and aggregation that could change interpretation.
- Protect sensitive segments and small cohorts.

## Dashboard integrity

Verify that every KPI, chart, and filter supports a user decision, action, or monitoring responsibility. Remove unsupported widgets rather than filling them with invented data.
