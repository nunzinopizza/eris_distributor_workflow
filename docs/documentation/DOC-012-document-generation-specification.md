# DOC-012 - Document Generation Specification

**Solution:** ERIS Distributor Cider Order-to-Payment Solution  
**Version:** 0.1  
**Status:** Draft  
**Dependency order:** 12  
**Owner:** To be assigned  
**Last updated:** July 25, 2026 - 7:35 AM CT  

## 1. Purpose

Define PO, BOL, invoice, and final-packet fields, layout, branding, numbering, filenames, revision marks, generation rules, and source-of-truth inputs.

## 2. Scope

This document is limited to the subject identified by its title. It does not replace the Business Requirements Specification or any dependent technical specification.

## 3. Dependencies

**Requires:** DOC-002, DOC-006, DOC-008, DOC-021

**Provides input to:** DOC-010, DOC-016, DOC-019

## 4. Current Status

**Draft**

Status is assigned under `STATUS_DEFINITIONS.md`. No percentage-complete estimate is used.

## 5. Revision History

| Version | Date | Status | Description |
|---|---|---|---|
| 0.1 | July 25, 2026 | Draft | Initial controlled repository document created from verified project sources. |

## 6. Known Completed Sections

- Document naming conventions, location codes, daily suffix, one-page limit, product-line limit, branding rules, and lifecycle metadata are defined.
- Suggested and final PO share the same number and filename.
- Revised BOLs retain number and filename and display REVISED with revision number.
- The final packet contents and summary-page requirements are defined.

## 7. Needs Refinement

- Visual templates and precise field mapping are not finalized.
- Invoice date/pickup date display and Internal Order ID footer remain deferred.
- Recognized holiday calendar and exact due-date implementation require definition.

## 8. Tasks to Complete

- [ ] Create field-mapping tables for each document.
- [ ] Create and approve visual templates.
- [ ] Define pagination and one-page validation controls.
- [ ] Define generation, replacement, versioning, revision, and packet assembly procedures.
- [ ] Resolve document-display decisions in DOC-021.

## 9. Deferred Decisions

See `DOC-021-decision-register.md`. Only decision entries supported by the controlling specification or repository records may be added.

## 10. References

- Distributor Cider Order-to-Payment Workflow, Version 0.1 Solution Blueprint.
- Distributor Cider Order-to-Payment Workflow one-page overview, prepared July 17, 2026.
- Existing project repository records and approved design branches, when imported.

Last updated: July 25, 2026 - 7:35 AM CT