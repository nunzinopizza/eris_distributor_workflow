# DOC-008 - SharePoint Architecture

**Solution:** ERIS Distributor Cider Order-to-Payment Solution  
**Version:** 0.1  
**Status:** Task to Complete  
**Dependency order:** 8  
**Owner:** To be assigned  
**Last updated:** July 25, 2026 - 7:35 AM CT  

## 1. Purpose

Define document libraries, metadata, versioning, retention, permissions, naming, packet storage, and document-link behavior.

## 2. Scope

This document is limited to the subject identified by its title. It does not replace the Business Requirements Specification or any dependent technical specification.

## 3. Dependencies

**Requires:** DOC-005, DOC-002, DOC-013

**Provides input to:** DOC-010, DOC-012, DOC-015, DOC-016

## 4. Current Status

**Task to Complete**

Status is assigned under `STATUS_DEFINITIONS.md`. No percentage-complete estimate is used.

## 5. Revision History

| Version | Date | Status | Description |
|---|---|---|---|
| 0.1 | July 25, 2026 | Task to Complete | Initial controlled repository document created from verified project sources. |

## 6. Known Completed Sections

- DOC-002 requires SharePoint to store PDFs, source documents, packet files, and prior document versions.
- Current visible PDFs are replaced while prior versions remain in SharePoint version history.
- Uploaded source filenames are preserved as metadata.

## 7. Needs Refinement

- Library names, content types, metadata columns, folder strategy, retention, and permission inheritance are not defined.

## 8. Tasks to Complete

- [ ] Define libraries and content types.
- [ ] Define metadata and indexing.
- [ ] Define versioning, retention, and recycle/recovery settings.
- [ ] Define permissions and integration with Dataverse records.
- [ ] Define final packet storage and immutable-closeout behavior.

## 9. Deferred Decisions

See `DOC-021-decision-register.md`. Only decision entries supported by the controlling specification or repository records may be added.

## 10. References

- Distributor Cider Order-to-Payment Workflow, Version 0.1 Solution Blueprint.
- Distributor Cider Order-to-Payment Workflow one-page overview, prepared July 17, 2026.
- Existing project repository records and approved design branches, when imported.

Last updated: July 25, 2026 - 7:35 AM CT