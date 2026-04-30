---
name: devibify
description: "Prevent vibe-coded, generic AI-looking frontend UI. Use when generating, reviewing, refactoring, or polishing HTML, CSS, React, Vue, Svelte/SvelteKit, dashboards, landing pages, product UI, components, forms, tables, or styling so the result has disciplined design systems, specific copy, working interactions, responsive behavior, loading states, accessibility, and production-ready verification."
---

# Devibify

Devibify turns frontend work into intentional product design instead of rushed vibe-coded output. Use it as a strict design and implementation workflow for UI that must feel calm, consistent, useful, and production-ready.

## Primary Operating Standard

Act as a senior product designer and frontend engineer who builds design systems for a living. Every UI choice must show:

- clarity over novelty
- consistency over variety
- usability over decoration
- accessibility over visual tricks
- production readiness over demo quality

The final result should feel shipped by a mature product team with a real design system. Nothing should feel improvised, placeholder-driven, over-animated, or designed only to make a screenshot look busy.

## Workflow

1. Inspect the existing project before designing.
   - Follow existing project patterns unless explicitly asked to change them.
   - Reuse components, tokens, utilities, and layout conventions before inventing new ones.
   - Keep changes minimal, targeted, and production-ready.
   - Do not introduce unnecessary dependencies, abstractions, or visual novelty.

2. Define or infer a UI contract for non-trivial work.
   - User goal: who the UI is for, the main task, and what must be obvious first.
   - Surface and scope: page, route, modal, drawer, form, table, card, nav, settings panel, or primitive.
   - Layout structure: regions, hierarchy, alignment, and information order.
   - Component inventory: existing pieces to reuse and new pieces that are justified.
   - State inventory: default, hover, focus, active, selected, disabled, loading, empty, error, success, skeleton.
   - Responsive behavior: small, medium, large, very narrow, and wide layouts where relevant.
   - Tokens: color, typography, spacing, sizing, radius, border, elevation, and motion.
   - Copy constraints: specific language, labels, button text, empty states, and prohibited placeholders.
   - Accessibility requirements: semantics, keyboard flows, focus, labels, errors, announcements.
   - Verification plan: interactions, breakpoints, screenshots, tests, and acceptance checks.

3. Establish a compact visual system before writing UI.
   - Use an existing system first.
   - If none exists, choose a strict 4pt or 8pt spacing scale and use it everywhere.
   - Define one type ramp with consistent sizes, weights, and line heights.
   - Pick a small palette and use color for hierarchy and state, not novelty.
   - Use one radius system, one border system, and one elevation system.
   - Keep motion subtle, purposeful, and compatible with reduced-motion preferences.

4. Implement complete behavior, not decorative UI.
   - Real actions must use real buttons.
   - Links must navigate somewhere valid.
   - Tabs must switch, accordions must open, modals must close, menus must be keyboard usable.
   - Async actions must show pending feedback and disable duplicate submission.
   - Data-backed areas need loading, empty, error, and recovery states when applicable.

5. Run the Devibify pass before presenting.
   - Remove red flags from the report below.
   - Standardize spacing, radii, shadows, alignment, and type where nearby UI drifts.
   - Replace generic copy with specific copy.
   - Remove fake proof, fake charts, dead controls, and placeholder links.
   - Verify responsive behavior, interactions, loading states, and accessibility basics.

## Vibe-Coded Website Report

Use this report as the main diagnostic lens. If five or more markers appear, assume the UI reads as vibe-coded and revise before shipping.

### Visual Red Flags

- Random purple gradients, purple glows, purple shadows, purple hover fills, or purple accents with no brand reason.
- Sparkle icons, sparkle emoji, or decorative emoji in hero text, buttons, cards, pricing, or footers.
- Hover effects on every card: aggressive lift, tilt, bounce, layout movement, or flashlight-like shadows.
- Emojis used as icons, headings, bullets, or status indicators.
- Fake testimonials: generic names, AI-looking avatars, no titles, no links, repeated wording, unverifiable quotes.
- Social icons that link to `#`, generic domains, 404s, or empty accounts.
- Massive icons paired with tiny text, inverting the hierarchy.
- Generic font usage with no rhythm: overly heavy headings, overly light body text, inconsistent line heights.
- Semi-transparent or blurred headers that lose contrast over scrolling content.
- Bad animation: unrelated Lottie files, wiggle effects, bounce overshoot, stutter, early scroll triggers.

### Structural Red Flags

- No loading states for async actions or data regions.
- Buttons stay unchanged while work is pending.
- Blank gaps appear while data loads.
- Components move around from page to page.
- Button sizes, padding, alignment, or container widths change randomly.
- Server actions or client interactions feel frozen with no feedback.
- Cards, grids, sticky elements, or margins drift out of alignment.
- Border radii are inconsistent across buttons, cards, inputs, avatars, and images.

### Content Red Flags

- Footer or copyright text is wrong, unfinished, or oddly phrased.
- Hero copy uses filler such as "build your dreams", "launch faster", "create without limits", or "where ideas become reality".
- The hero contains every trick at once: sparkle, emoji, gradient, two buttons, animated card, microcopy, background image, shadow, and decorative animation.
- Buzzword stacking replaces a clear value proposition.
- Testimonials, metrics, and logos are invented to fill space.

### Technical Red Flags

- Missing page title, meta description, favicon, or social metadata where the framework supports them.
- Bad mobile behavior: overflowing text, awkward card stacks, too-wide buttons, collapsed layouts, or horizontal scroll.
- Non-functional controls: dead carousels, inert tabs, accordions that do not open, modals that cannot close, dark mode toggles that do nothing.
- Placeholder text, placeholder images, placeholder avatars, `lorem ipsum`, test labels, or dead href values left in final output.

## Design System Rules

### Spacing

- Default to an 8pt spacing system unless the existing project clearly uses 4pt.
- Use the chosen scale for margins, padding, gaps, sections, toolbar heights, and component internals.
- Do not use arbitrary one-off values unless needed to match an existing system or solve a real layout constraint.

### Typography

- Use one heading family and one body family, or the existing project fonts.
- Define display, page title, section heading, body, label, caption, and button text behavior.
- Keep body text readable, never overly bold or overly light.
- Avoid generic type choices as a shortcut to polish. If using common fonts such as Inter, Poppins, Montserrat, Roboto, Arial, or system stacks, the rhythm must be deliberate.
- Keep line length, line height, and spacing between text blocks consistent.

### Color

- Reuse existing project colors first.
- If no palette exists, choose a small calm palette and stick to it.
- Avoid neon, random gradients, colored glow shadows, and purple gradients unless the brand clearly calls for them.
- Use accent color to clarify state or hierarchy, not to decorate emptiness.
- Maintain strong contrast for text, controls, disabled states, and focus rings.

### Radius, Borders, And Elevation

- Use one radius scale across the UI.
- Buttons, inputs, cards, panels, and dialogs should feel related.
- Keep cards at 8px radius or less unless the existing design system requires otherwise.
- Avoid pill overload and 20px to 32px radii as a default.
- Prefer borders, spacing, and typography before adding shadows.
- Use one subtle elevation style if elevation is needed. Avoid dramatic, colored, or glow-like shadows.

### Motion

- Use motion only when it clarifies cause, response, or state change.
- Prefer opacity, color, or small state changes over transforms.
- Avoid bounce, wiggle, tilt, dramatic lift, parallax, and scroll-triggered decoration.
- Hover states must never shift layout, break alignment, or create visual wobble.
- Respect `prefers-reduced-motion`.

## Normal UI Defaults

- Sidebars: 240px to 260px fixed width, solid background, simple border-right, no floating shell.
- Headers: plain hierarchy, no eyebrow labels, no gradient text, no decorative microcopy.
- Sections: standard padding, clear structure, no hero treatment inside internal tools unless there is a product reason.
- Navigation: simple links, clear active state, subtle hover, no transform movement.
- Buttons: solid fill or simple border, stable size, clear loading and disabled states, no gradient pills.
- Cards and panels: grouping only, subtle border, consistent internal spacing, no card-inside-card layouts.
- Forms: visible labels, useful help text, clear errors, simple focus states.
- Inputs: stable borders, visible focus ring, no animated underline gimmicks.
- Modals: straightforward overlay, clear title, close behavior, focus handling.
- Dropdowns: simple list, selected state, keyboard-safe behavior.
- Tables and lists: scanability first, left-aligned text, disciplined columns, badge use only when it adds information.
- Tabs: simple underline or border indicator, no sliding pill animation.
- Badges: small, limited, state-driven, no repeated decorative chips.
- Icons: 16px to 20px in most product UI, consistent stroke, never dominating nearby text.
- Toolbars: compact, predictable, icon buttons where symbols are familiar, text buttons only for clear commands.
- Footers: accurate text, real links, no filler metadata.

## Hard Bans

Do not ship these unless the user explicitly requests them and the product context justifies them:

- Random purple gradients, neon effects, glow haze, bokeh, glassmorphism, or conic flourishes.
- Sparkles or emojis as decorative UI.
- Fake testimonials, fake logos, fake charts, fake metrics, fake activity streams, or filler widgets.
- KPI-card grids as the automatic dashboard starting point.
- Floating detached sidebars, decorative right rails, or usage panels with no user need.
- Hero sections inside dashboards or operational tools.
- Eyebrow labels, uppercase micro-headings, and "premium" copy that says little.
- Generic dark SaaS composition as a default reflex.
- Overpadded layouts, dead luxury space, or centered walls of text.
- Multiple unrelated border radii, shadow systems, font moods, or alignment systems.
- Decorative badges and chips on every row or status.
- Clickable `div` or `span` elements for actions.
- Dead controls, placeholder hrefs, placeholder content, or non-functional toggles.

## Component Requirements

Buttons:

- Include primary, secondary, destructive, disabled, focus, and loading behavior when relevant.
- Keep comparable actions the same height and padding.
- Disable or guard repeat submission while pending.

Inputs:

- Use labels, errors tied to fields, visible focus states, and accessible descriptions when useful.
- Avoid placeholder-only labeling.

Cards and panels:

- Use for grouping related content, not for decorating every block.
- Keep internal spacing and heading/action placement consistent.

Navigation:

- Use predictable placement, clear active state, and meaningful labels.
- Avoid nav badges unless counts or states are real and useful.

Tables and dense lists:

- Prioritize alignment, row height, sorting/filtering affordances when relevant, and graceful overflow behavior.
- Do not hide important data behind decorative cards if a table is clearer.

Dialogs and overlays:

- Provide title, purpose, close action, keyboard dismissal where appropriate, focus return, and clear primary/secondary actions.

Loading, empty, and error states:

- Use skeletons for larger data regions where they preserve layout.
- Use button-level pending indicators for async actions.
- Give empty states a useful next action.
- Errors should be clear, recoverable, and visible.

## Copy Standards

- State what the product does, who it serves, and why it matters.
- Prefer concrete nouns and verbs over abstract optimism.
- Replace "launch faster" with the specific thing that becomes faster.
- Replace "build your dreams" with the actual workflow or outcome.
- Omit testimonials when real, attributable proof is unavailable.
- Keep microcopy calm, useful, and short.
- Ensure footer, legal, and copyright text is correct.

## Technical Completeness

For page-level work, include or preserve:

- meaningful page title
- meta description when the framework supports it
- social metadata and OG image when the project supports them
- favicon when relevant
- responsive behavior across small, medium, and large viewports
- working links, buttons, tabs, accordions, modals, menus, and forms
- no `#` links unless explicitly requested for scaffolding
- no placeholder data in the final UI
- semantic HTML and accessible controls

## Project Command Guidance

- Check project files before choosing commands.
- In Node, web, or SvelteKit projects, inspect `package.json` and use existing scripts such as `npm run lint`, `npm run format`, `npm run check`, `npm run test`, and `npm run build` when available.
- If no relevant script exists, use the local tool directly where appropriate, such as `npx eslint .` or `npx prettier --check .`.
- Do not invent new scripts unless explicitly asked.
- In Flutter or Dart UI projects, use the native toolchain. If FVM is configured, prefer `fvm flutter ...` and `fvm dart ...`.
- For Svelte or SvelteKit framework-specific changes, consult the official Svelte LLM docs before making framework-specific edits when required by repo instructions.

## Verification

UI work is complete only after relevant verification.

Check responsive behavior at:

- small mobile
- medium tablet or narrow laptop
- desktop
- very narrow or wide layouts when the surface is sensitive

Verify:

- no clipped, overlapping, or horizontally scrolling content unless intentional
- headings, labels, and buttons wrap cleanly
- primary actions remain visible and usable
- hover, focus, active, selected, disabled, loading, empty, error, and success states where relevant
- links navigate correctly and controls function
- keyboard users can complete the main flow
- focus is visible
- inputs have labels
- errors are associated with fields
- contrast is readable
- reduced motion is respected
- no placeholder text, dead social links, or inert UI remains

Use executable verification when the repo supports it: lint, typecheck, tests, builds, Playwright screenshots, Storybook checks, or component tests. If verification cannot be completed, state exactly what was not run, why, and what risk remains.

## Final Review Checklist

- The layout follows a grid and consistent container widths.
- Spacing follows a 4pt or 8pt rhythm.
- Typography has a stable hierarchy and readable line heights.
- Colors are disciplined and justified by brand, hierarchy, or state.
- Radii, borders, and shadows are consistent.
- Motion is subtle and tied to user intent.
- Icons are proportional and functional.
- Copy is specific, grounded, and free of filler.
- Loading, empty, error, disabled, and success states are handled.
- All visible interactive elements work.
- Mobile and desktop layouts are both polished.
- Technical metadata and page basics are present when relevant.
- The UI contains none of the report's major vibe-coded tells.
