# Interaction states

## Reachability principle

Implement and test the states the changed surface can actually reach. Derive reachability from user actions, data contracts, permissions, network behavior, and repository patterns. Do not manufacture every possible state for every component.

## State taxonomy

### Interaction states

Account for applicable default, hover, focus, active, selected, checked, mixed, pressed, expanded, collapsed, disabled, read-only, invalid, and warning states.

### Data and asynchronous states

Account for applicable idle, pending, optimistic, initial loading, background refreshing, partial data, success, empty, no matching results, stale, offline, timeout, rate limited, permission denied, authentication expired, server conflict, cancelled, retrying, partial success, undo available, autosaving, saved, unsaved changes, upload progress, download preparation, failure, and recovery states.

## State behavior

- Show immediate, accurate pending feedback for asynchronous actions.
- Guard duplicate submission while preserving legitimate retry.
- Keep layout stable while loading.
- Use a skeleton only when the final structure is known and latency makes it useful.
- Keep skeletons and decorative charts from impersonating real data.
- Preserve user input on recoverable errors.
- Make errors specific and actionable.
- Offer retry or an alternative when recovery is possible.
- Roll back or reconcile optimistic updates after rejection or conflict.
- Show freshness when users may act on stale data.
- Resolve server conflicts without silently overwriting newer data.
- Represent permission denial and authentication expiry explicitly rather than as empty data.
- Show progress, cancellation, and retry for long uploads when supported.
- Protect unsaved changes from lossy navigation.
- Match confirmation, undo, and recovery to the consequence and reversibility of destructive actions.
- Announce status when users would otherwise miss the change.

## History and persistence

Inspect reload, back and forward navigation, deep links, query and filter persistence, and URL-backed modal or drawer history where the product supports them. Restore scroll and focus when appropriate. Preserve unsaved input unless security or product rules require disposal, and communicate that boundary.

## State matrix

| Region or control | Trigger | Reachable states | Visible feedback | Recovery | Keyboard and focus | Announcement | Persistence or history | Evidence |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
