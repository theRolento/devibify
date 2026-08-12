# Forms and validation

Treat a form as a recovery-oriented workflow, not a collection of styled fields.

## Labels and instructions

- Use persistent visible labels rather than placeholder-only fields.
- Communicate required and optional status consistently.
- Put helpful descriptions before users need them.
- Group related fields with fieldsets and legends.
- Choose the correct input type, name, autocomplete, and input mode.
- Use locale-aware formats and examples.
- Keep units, prefixes, and suffixes outside editable values when practical.

## Validation timing

- Give users a reasonable chance to complete a field before showing errors.
- Validate on submit and, when useful, after blur or meaningful interaction.
- Keep validation from fighting active typing.
- Keep client and server messages consistent.
- Explain incompleteness directly; a disabled submit button alone is insufficient.

## Error recovery

- State what is wrong and how to fix it.
- Place field-level errors near their fields and associate them programmatically.
- Preserve entered values.
- Use an error summary for page-level or multi-field errors when it improves recovery.
- Move focus to that summary after failed submission when appropriate and link summary items to fields.
- Keep summary and field wording consistent.
- Add an error state to the page title when the application pattern supports it.
- Distinguish validation, authorization, network, conflict, and system errors.
- Replace generic errors with specific information whenever the system provides it safely.

## Submission

- Show pending feedback and prevent duplicate submission.
- Preserve values after server rejection.
- Represent partial success explicitly.
- Show success only after the server or underlying action succeeds.
- Use backend idempotency guarantees when documented; do not invent them.
- State destructive or financial consequences before commitment.

## Authentication recovery

- Let masking support correction.
- Preserve as much work as safely possible across session expiry.

Use `accessibility.md` for password-manager, paste, autocomplete, and reveal-control requirements. Use `content-evidence-ethics-and-safety.md` for sensitive-data handling.

## Multi-step forms

When applicable, communicate progress and current step, preserve values through back navigation, provide review and confirmation, support save-and-resume only when real, keep step boundaries clear, validate at the appropriate stage, and state final submission consequences.

## File uploads

When applicable:

- state accepted type and size;
- expose progress, cancel, and retry;
- show virus scanning or processing state if the product exposes it;
- distinguish errors for individual files in multi-file uploads;
- expose accessible file names and remove controls;
- show completion only after upload and required processing finish.
