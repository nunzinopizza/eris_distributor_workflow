# DOC-004 - Operating Workflow Manual

**Solution:** ERIS Distributor Cider Order-to-Payment Solution  
**Version:** 0.1  
**Status:** Draft  
**Dependency order:** 4  
**Owner:** To be assigned  
**Last updated:** July 25, 2026 - 7:35 AM CT  

## 1. Purpose

Document the current manual process, target automated process, human responsibilities, exceptions, restart points, and operational controls.

## 2. Scope

This document is limited to the subject identified by its title. It does not replace the Business Requirements Specification or any dependent technical specification.

## 3. Dependencies

**Requires:** DOC-002, DOC-003

**Provides input to:** DOC-017, DOC-018, DOC-019

## 4. Current Status

**Draft**

Status is assigned under `STATUS_DEFINITIONS.md`. No percentage-complete estimate is used.

## 5. Revision History

| Version | Date | Status | Description |
|---|---|---|---|
| 0.1 | July 25, 2026 | Draft | Initial controlled repository document created from verified project sources. |

## 6. Known Completed Sections

- The business process is defined from order intake through final packet and closeout.
- Four approved entry points are defined.
- Human approval, confirmation review, BOL print confirmation, payment confirmation, and order closeout remain explicit human actions.
- No-response and payment-discrepancy escalation paths are defined at a business-rule level.

## 7. Needs Refinement

- The current manual process has not been fully documented step by step.
- The target operating table with step, actor/system, input, output, and failure handling has not been completed.
- Restart and recovery procedures are not yet defined for each failure stage.
- Role names remain dependent on DOC-013.

## 8. Tasks to Complete

- [ ] Interview process owners and document the current manual process.
- [ ] Build the target step-by-step operating table.
- [ ] Add exception, restart, recovery, and escalation procedures.
- [ ] Add screen references after DOC-009 exists.

## 9. Deferred Decisions

See `DOC-021-decision-register.md`. Only decision entries supported by the controlling specification or repository records may be added.

## 10. References

- Distributor Cider Order-to-Payment Workflow, Version 0.1 Solution Blueprint.
- Distributor Cider Order-to-Payment Workflow one-page overview, prepared July 17, 2026.
- Existing project repository records and approved design branches, when imported.

Last updated: July 25, 2026 - 7:35 AM CT