# ERIS Distributor Workflow — Agent Instructions

## Project purpose

Build the ERIS Distributor Cider Order-to-Payment Workflow described in:

- `docs/production-spec-v0.1.md`
- `docs/open-decisions.md`
- `docs/acceptance-tests.md`
- `docs/traceability-matrix.md`

The production specification is the primary source of truth.

## Core rule

Do not invent business rules, statuses, permissions, data fields, approval behavior, or technical decisions.

Anything identified as TBD, deferred, unresolved, or a Build-Stage Decision must remain unresolved until it is explicitly decided and documented.

## Approved architecture

The target solution uses:

- SharePoint workflow home
- Canvas Power App
- Dataverse
- Power Automate
- Outlook
- SharePoint document libraries
- Controlled Word-to-PDF templates

Power Pages is not currently part of the approved design.

## Required workflow protections

The solution must never:

- Guess an ambiguous email, document, payment, or order match.
- Create free-form product lines.
- Send to an external recipient who is not an approved stored contact.
- Change the permanent Internal Order ID.
- Mark a BOL printed without user confirmation.
- Send a final PO/BOL package while blockers remain.
- Mark an invoice paid solely from a remittance email.
- Close an order without user review.
- Reopen a canceled order.
- Send a blocked document category.

## Order and document rules

- Use one optional order-level Notes field.
- Do not create order-line notes.
- Preserve source filenames as metadata.
- Preserve prior document versions.
- Use confirmed BOL quantities as the final quantity source.
- Use approved final PO prices for invoice creation.
- Keep PO, BOL, and invoice output to one portrait page with no more than 18 order lines.

## Development behavior

Before making a change:

1. State the proposed change.
2. Identify the files that will be created or modified.
3. Identify the requirement or acceptance criterion being implemented.
4. Call out any unresolved decision that blocks the work.

When making a change:

- Make the smallest practical change.
- Do not silently modify approved requirements.
- Do not delete documentation or tests without explicit approval.
- Keep implementation, documentation, tests, and traceability aligned.
- Add meaningful error handling and audit logging.
- Do not place credentials, secrets, connection strings, or production identifiers in the repository.

After making a change:

- Summarize what changed.
- List files changed.
- State what was tested.
- State what remains unresolved.
- Update the traceability matrix and acceptance tests when applicable.

## Repository approach

Application development has not begun.

Work in this order unless explicitly directed otherwise:

1. Correct and stabilize project documentation.
2. Resolve or record open decisions.
3. Define the Dataverse logical and physical data model.
4. Define security roles and ownership.
5. Define SharePoint document architecture.
6. Define Power Automate flow contracts.
7. Define Canvas Power App screens and actions.
8. Create solution components.
9. Implement tests and deployment controls.

Use small, descriptive Git commits.
