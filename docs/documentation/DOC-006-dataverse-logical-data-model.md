# DOC-006 - Dataverse Logical Data Model

**Solution:** ERIS Distributor Cider Order-to-Payment Solution  
**Version:** 0.1  
**Status:** Needs Refinement\
**Dependency order:** 6  
**Owner:** To be assigned  
**Last updated:** July 25, 2026 - 7:35 AM CT  

## 1. Purpose

Define business entities, relationships, keys, ownership, lifecycle, and source-of-truth responsibilities without committing prematurely to physical column implementation.

## 2. Scope

This document is limited to the subject identified by its title. It does not replace the Business Requirements Specification or any dependent technical specification.

## 3. Dependencies

**Requires:** DOC-002, DOC-005, DOC-021

**Provides input to:** DOC-007, DOC-009, DOC-010, DOC-013, DOC-015

## 4. Current Status

**Needs Refinement**

Status is assigned under `STATUS_DEFINITIONS.md`. No percentage-complete estimate is used.

## 5. Revision History

| Version | Date | Status | Description |
|---|---|---|---|
| 0.1 | July 25, 2026 | Draft | Initial controlled repository document created from verified project sources. |
| 0.2 | July 25, 2026 | Needs Refinement | Aligned this control record with the substantive logical model and recorded the unresolved Order-status conflict. |

## 6. Known Completed Sections

- The core record list is defined in DOC-002, including Distributor, Location, Contact, Product, Order, Order Line, PO, BOL, Invoice, Approval, Communication, Confirmation Issue, Pickup Event, Credit Memo, Payment Notice, Settlement Transaction, Event History, and Final Packet.
- Permanent Internal Order ID and document-specific reference behavior are defined.
- Product-price snapshots and source-of-truth relationships are defined.
- Audit expectations require user, timestamp, record, document version, and action.
- The substantive logical model is present at `../dataverse-logical-model-v0.1.md` and defines records, relationships, lifecycle fields, ownership requirements, preservation controls, and the physical-design handoff.

## 7. Needs Refinement

- The overall Order status values in the logical model do not match the controlling production specification; OD-26 preserves this as an unresolved cross-document conflict.
- Cardinalities, optionality, ownership, alternate keys, and choice ownership require formal review.
- Approval submission cycles, document versions, email attachments, settlement allocation, and event history need relationship validation.

## 8. Tasks to Complete

- [x] Locate and register the substantive logical model in this repository.
- [ ] Resolve OD-26 through an approved decision before changing lifecycle values or mappings.
- [ ] Reconcile the substantive logical model against the Version 0.1 core-record list.
- [ ] Define cardinalities, business keys, ownership, and lifecycle for every entity.
- [ ] Perform normalization and auditability review before the model advances beyond Needs Refinement.

## 9. Deferred Decisions

See `DOC-021-decision-register.md`. Only decision entries supported by the controlling specification or repository records may be added.

## 10. References

- Distributor Cider Order-to-Payment Workflow, Version 0.1 Solution Blueprint.
- Distributor Cider Order-to-Payment Workflow one-page overview, prepared July 17, 2026.
- Existing project repository records and approved design branches, when imported.

Last updated: July 25, 2026 - 7:35 AM CT
