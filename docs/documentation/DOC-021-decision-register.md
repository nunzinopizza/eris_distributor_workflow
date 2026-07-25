# DOC-021 - Decision Register

**Solution:** ERIS Distributor Cider Order-to-Payment Solution  
**Version:** 0.1  
**Status:** Draft  
**Dependency order:** Continuous  
**Owner:** To be assigned  
**Last updated:** July 25, 2026 - 7:35 AM CT  

## 1. Purpose

Maintain the controlled record of deferred decisions, ambiguities, dependencies, resolutions, rationale, owners, dates, and affected documents.

## 2. Scope

This document is limited to the subject identified by its title. It does not replace the Business Requirements Specification or any dependent technical specification.

## 3. Dependencies

**Requires:** DOC-002

**Provides input to:** All documents

## 4. Current Status

**Draft**

Status is assigned under `STATUS_DEFINITIONS.md`. No percentage-complete estimate is used.

## 5. Revision History

| Version | Date | Status | Description |
|---|---|---|---|
| 0.1 | July 25, 2026 | Draft | Initial controlled repository document created from verified project sources. |

## 6. Known Completed Sections

- Deferred build-stage decisions are listed in §25 of the controlling production specification.
- `../open-decisions.md` is the substantive project decision register and contains stable `OD-*` identifiers.
- Known open decisions include approval reminders, Close Approval authority, role matrix, pickup-time approval reset, edit-lock timeout, copy-order initial state, suggested-PO approval/send behavior, revised-email statuses, attachment-category rules, invoice date display, Internal Order ID footer, post-approval edits, invoice send failure, duplicate-send controls, error messages, holiday calendar, and visual refinements.
- OD-26 records the unresolved conflict between the overall Order status values in the production specification and logical model without selecting a mapping or default.

## 7. Needs Refinement

- Owners, target dates, options, rationale, resolution, and affected artifacts are not complete.

## 8. Tasks to Complete

- [x] Identify the substantive open-decisions register and its stable IDs.
- [ ] Keep this control record aligned with `../open-decisions.md`.
- [ ] Add decision owner, required-by milestone, options, outcome, rationale, and approval evidence.
- [ ] Update dependent document statuses whenever a decision is resolved.

## 9. Deferred Decisions

See the substantive project register at `../open-decisions.md`. Only decision entries supported by the controlling specification or repository records may be added.

## 10. References

- Distributor Cider Order-to-Payment Workflow, Version 0.1 Solution Blueprint.
- Distributor Cider Order-to-Payment Workflow one-page overview, prepared July 17, 2026.
- Existing project repository records and approved design branches, when imported.

Last updated: July 25, 2026 - 7:35 AM CT
