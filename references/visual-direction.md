# Visual direction

The product's existing design system, tokens, and components come first. The fallback defaults below apply only where no system exists or a surface is genuinely new; say when you used them.

## Replace generic defaults

Each left-hand pattern is a high-frequency AI default. Treat it as a hypothesis to justify from product evidence; without that evidence, use the right-hand alternative.

| Generic default | Product-specific alternative |
|---|---|
| Hero with a gradient blob, a "Supercharge your workflow" headline, and three feature cards | Lead with the product's real output or working surface, and a headline naming who it serves and what changes for them |
| A row of four KPI cards above every dashboard | Start with the question the user comes to answer, such as the queue to work or the anomaly to inspect; place each metric beside what it describes, only where it drives a decision |
| Card mosaics, nested cards, every section in a rounded box | Group with alignment, spacing, and dividers; reserve containers for independent objects users select, move, or open |
| Pill and badge soup | Status as text with one restrained color or icon; badges only for state that changes what the user does next |
| Gradients, glow, glass, blur, generic dark SaaS styling | Flat surfaces with one brand accent; depth only where layers stack, such as menus, popovers, and dialogs |
| Decorative sidebars and floating rails | Navigation sized to the destinations: a top bar for a handful, a sidebar for many sections or deep applications |
| The same heading, subtitle, and three-column block repeated down the page | Composition chosen by content: a comparison is a table, a process is a sequence, one strong claim is one large statement with its proof |
| "Trusted by thousands", "lightning fast", stock avatars and testimonials | Concrete, attributable facts, or nothing |
| An icon or emoji beside every heading | Icons where they speed recognition (actions, file types, status), from one family |
| Everything centered | Left-aligned text for reading and scanning; centering reserved for short display moments |
| One large radius and a shadow on every element | One or two radii and a few elevation levels, each tied to a meaning |
| Two "directions" that differ only in color | Directions that differ in hierarchy, density, workflow, or navigation |
| An unrequested redesign of an established surface | The existing system, improved where evidence shows a failure |

Unusual, maximalist, or expressive styles pass when they are intentional, coherent, usable, and specific to the product.

## Hierarchy

- Give each view one focal point, and make the primary action the only element styled as primary.
- Build hierarchy with position, size, weight, and contrast before color.
- Group by proximity: space inside a group is clearly smaller than space between groups.
- Match density to use: compact for frequent expert work (tables, consoles, queues), balanced for settings and forms, paced for marketing and onboarding, immersive for media and storytelling.
- Keep containers, navigation, and patterns stable across related screens.

## Fallback defaults

Use these only without an established system:

- **Spacing:** a 4px base scale (4, 8, 12, 16, 24, 32, 48, 64). Document an optical exception instead of inventing a value.
- **Type:** one UI family (the system stack or one brand face), optionally a second for display; five or six sizes (for example 12, 14, 16, 20, 24, 32); 16px body text, 14px in dense tools; line height 1.4–1.6 for body and 1.1–1.3 for headings; a reading measure of 45–75 characters; two or three weights.
- **Color:** tokens named by role (surface, text, muted text, border, accent, focus), not by hue. Neutrals carry most surfaces and text, one accent marks primary actions and focus, and success, warning, danger, and info appear only for state. Meet WCAG contrast for text and non-text elements.
- **Shape and depth:** one or two radii; elevation levels only for stacked layers.
- **Motion:** 100–250ms, easing out on entry, used to show cause and effect, with a `prefers-reduced-motion` alternative.

## By surface

- **Operational and dashboard:** the working surface first, with no marketing hero; dense but scannable; tables for comparison; active filters visible; actions next to the content they act on.
- **Marketing and landing:** one clear value claim for a named audience; the product shown, not described; attributable proof; one primary call to action, repeated rather than competing with others.
- **Forms and settings:** a single column with labels above fields, grouped by the user's mental model, with explicit save behavior.
- **Content and documentation:** a readable measure, a strong heading hierarchy, and navigation that shows the current location.
