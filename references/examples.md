# Examples

Each example contrasts a generic first draft with a product-specific result built from the same request.

## Operations dashboard

Request: "Build a dashboard for our support team."

**Generic draft:** four KPI cards (tickets, response time, satisfaction, agents online) with sparkline decorations, a line chart of tickets per day, a "Recent activity" feed with stock avatars, and a gradient header greeting the user by name.

**Product-specific result:**

- Thesis: support agents start each shift deciding which conversations to answer first; the product character is calm, dense, and fast.
- The working surface comes first: a queue table sorted by breach risk, with columns for customer, wait time, SLA remaining, priority, and assignee.
- Filters for "Mine", "Unassigned", and "Breaching soon" sit above the table and stay visible.
- One metric remains, "3 conversations breach SLA within 15 minutes", placed above the queue because it changes what the agent does next.
- Reachable states: empty queue ("No open conversations"), permission-limited view, stale data with a refresh time, and a failed load with retry.
- At 320px the table keeps customer, SLA remaining, and an open action; the other columns move into a details view.

## Landing page

Request: "Make a landing page for our scheduling product."

**Generic draft:** a centered hero, "Supercharge your scheduling", over a purple gradient; three feature cards with icons; "Trusted by 10,000+ teams" above a row of placeholder logos; a testimonial carousel; and a pricing grid with a highlighted middle tier.

**Product-specific result:**

- Thesis: clinic managers lose hours to phone rescheduling; the product character is dependable and plain-spoken.
- The headline names the audience and the outcome: "Patients reschedule themselves. Your front desk stops playing phone tag."
- The product appears as a real booking screen, with an annotated example of the rescheduling flow instead of feature cards.
- Proof comes only from sources in the repository; with none available, the section is left out and the page closes on the call to action.
- One primary action, "Book a 20-minute demo", repeats at the end; secondary links go to pricing and documentation.

## Account settings form

Request: "Implement the notification settings form."

**Generic draft:** a grid of toggle cards with icons, a floating "Save" button, a success toast shown on click, and errors shown only as red borders.

**Product-specific result:**

- Thesis: users want fewer, more relevant emails without fear of missing billing or security notices; the product character is trustworthy and quiet.
- A single column groups notifications by what they protect: security, billing, product updates. Mandatory security notices appear as read-only rows with a stated reason.
- Each row reads as a sentence, such as "Email me when an invoice is issued", with a native checkbox and a visible label.
- One "Save changes" button follows the form; it shows pending feedback, blocks double submission, and confirms only after the server succeeds.
- A server error appears in a summary at the top that receives focus and links to the affected rows, with the entered choices preserved.
- Navigating away with unsaved changes asks for confirmation.
