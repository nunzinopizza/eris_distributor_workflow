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

- Deferred items are listed in Section 38 of the Version 0.1 blueprint.
- Known open decisions include approval reminders, Close Approval authority, role matrix, pickup-time approval reset, edit-lock timeout, copy-order initial state, suggested-PO approval/send behavior, revised-email statuses, attachment-category rules, invoice date display, Internal Order ID footer, post-approval edits, invoice send failure, duplicate-send controls, error messages, holiday calendar, and visual refinements.

## 7. Needs Refinement

- Decision IDs must be reconciled with the project's existing open-decisions file.
- Owners, target dates, options, rationale, resolution, and affected artifacts are not complete.

## 8. Tasks to Complete

- [ ] Import the existing open-decisions register from the repository.
- [ ] Assign stable IDs and affected-document links.
- [ ] Add decision owner, required-by milestone, options, outcome, rationale, and approval evidence.
- [ ] Update dependent document statuses whenever a decision is resolved.

## 9. Deferred Decisions

See `DOC-021-decision-register.md`. Only decision entries supported by the controlling specification or repository records may be added.

## 10. References

- Distributor Cider Order-to-Payment Workflow, Version 0.1 Solution Blueprint.
- Distributor Cider Order-to-Payment Workflow one-page overview, prepared July 17, 2026.
- Existing project repository records and approved design branches, when imported.

Last updated: July 25, 2026 - 7:35 AM CT