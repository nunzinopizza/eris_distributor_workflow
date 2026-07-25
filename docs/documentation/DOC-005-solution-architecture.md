# DOC-005 - Solution Architecture

**Solution:** ERIS Distributor Cider Order-to-Payment Solution  
**Version:** 0.1  
**Status:** Draft  
**Dependency order:** 5  
**Owner:** To be assigned  
**Last updated:** July 25, 2026 - 7:35 AM CT  

## 1. Purpose

Define the solution components, system boundaries, integrations, ownership, and deployment topology.

## 2. Scope

This document is limited to the subject identified by its title. It does not replace the Business Requirements Specification or any dependent technical specification.

## 3. Dependencies

**Requires:** DOC-002

**Provides input to:** DOC-006, DOC-008, DOC-009, DOC-010, DOC-013, DOC-016

## 4. Current Status

**Draft**

Status is assigned under `STATUS_DEFINITIONS.md`. No percentage-complete estimate is used.

## 5. Revision History

| Version | Date | Status | Description |
|---|---|---|---|
| 0.1 | July 25, 2026 | Draft | Initial controlled repository document created from verified project sources. |

## 6. Known Completed Sections

- The proposed architecture uses a SharePoint workflow home page, Canvas Power App, Dataverse, SharePoint document library, Power Automate, and Outlook.
- Power Pages is excluded from the current design.
- Outlook sends from the individual user's mailbox using a centrally managed ERIS signature template.

## 7. Needs Refinement

- Environment topology, connection references, service accounts, data-loss-prevention policy, and ownership model are not documented.
- Integration boundaries and failure ownership require definition.
- Architecture diagrams have not been created.

## 8. Tasks to Complete

- [ ] Create logical and deployment architecture diagrams.
- [ ] Define Development, Test, and Production environments.
- [ ] Define connector ownership, connection references, and service-account policy.
- [ ] Document security, retention, monitoring, and support boundaries.

## 9. Deferred Decisions

See `DOC-021-decision-register.md`. Only decision entries supported by the controlling specification or repository records may be added.

## 10. References

- Distributor Cider Order-to-Payment Workflow, Version 0.1 Solution Blueprint.
- Distributor Cider Order-to-Payment Workflow one-page overview, prepared July 17, 2026.
- Existing project repository records and approved design branches, when imported.

Last updated: July 25, 2026 - 7:35 AM CT