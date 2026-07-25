# DOC-001 - Executive Workflow Overview

**Solution:** ERIS Distributor Cider Order-to-Payment Solution  
**Version:** 0.1  
**Status:** Needs Refinement  
**Dependency order:** 1  
**Owner:** To be assigned  
**Last updated:** July 25, 2026 - 7:35 AM CT  

## 1. Purpose

Provide a concise business-level explanation of what the workflow accomplishes, who it serves, its approved starting points, and the result of successful completion.

## 2. Scope

This document is limited to the subject identified by its title. It does not replace the Business Requirements Specification or any dependent technical specification.

## 3. Dependencies

**Requires:** None

**Provides input to:** DOC-002, DOC-004, DOC-005

## 4. Current Status

**Needs Refinement**

Status is assigned under `STATUS_DEFINITIONS.md`. No percentage-complete estimate is used.

## 5. Revision History

| Version | Date | Status | Description |
|---|---|---|---|
| 0.1 | July 25, 2026 | Needs Refinement | Initial controlled repository document created from verified project sources. |

## 6. Known Completed Sections

- The workflow manages distributor cider orders from initial order activity through document creation, approvals, communications, payment tracking, and closeout.
- The workflow supports Lakeshore Beverage Company, Grant Importing, and Skeff Distributing.
- Authorized users may begin from a distributor order/PO, an ERIS-created Lakeshore suggested PO, a Production-created BOL, or a copied/revised prior order.
- The result is a connected record of documents, approvals, communications, issues, payment, and final closeout.

## 7. Needs Refinement

- The July 17 overview says a Production-created BOL requires approval and then triggers creation of a PO and invoice. The controlling Version 0.1 blueprint says a BOL may be generated and printed without approval, and the invoice draft is generated when the order is marked Picked Up.
- The overview must distinguish the suggested PO, final PO/BOL send, and separate invoice approval/send stages.
- The overview should identify the three supported distributors and Lakeshore's two delivery locations.

## 8. Tasks to Complete

- [ ] Rewrite the one-page overview so it matches the controlling Version 0.1 blueprint.
- [ ] Review the revised overview against DOC-002 before marking Finalized.
- [ ] Regenerate the approved one-page PDF.

## 9. Deferred Decisions

See `DOC-021-decision-register.md`. Only decision entries supported by the controlling specification or repository records may be added.

## 10. References

- Distributor Cider Order-to-Payment Workflow, Version 0.1 Solution Blueprint.
- Distributor Cider Order-to-Payment Workflow one-page overview, prepared July 17, 2026.
- Existing project repository records and approved design branches, when imported.

Last updated: July 25, 2026 - 7:35 AM CT