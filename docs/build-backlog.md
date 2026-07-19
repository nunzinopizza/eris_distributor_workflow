# Build Backlog

## Planning boundary

This is a delivery sequence, not an implementation authorization. It contains only work implied by the controlling specification. Build-stage decisions listed in `docs/open-decisions.md` must be resolved before the dependent item is released.

## Recommended first vertical slice

The smallest complete vertical slice is: **manually reviewed distributor order intake → permanent order ID → distributor/location/contact and product/price selection → order-line price snapshots and pallet estimate → suggested PO PDF preview → exact-package suggested-PO approval → audit history**.

It is complete because it proves the controlled record, master data, document creation, human approval, and traceability pattern. It deliberately excludes automated inbox extraction, sending behavior (OD-06), BOL, pickup, invoice, payment, and closeout.

| Phase | Small implementation items | Traceability | Dependencies / decisions | Done evidence |
| --- | --- | --- | --- | --- |
| 0. Resolve release prerequisites | Assign owners; provision solution/environment; select SharePoint library; define access matrix; load approved master data; obtain template/logo assets. | TR-008, TR-022, TR-024, TR-025 | OD-02, OD-15, OD-17–OD-21 | Approved configuration and access records. |
| 1. Foundation | Create logical data records for orders, lines, master data, documents, approvals, and immutable event history; configure naming/sequence and controlled lifecycle metadata. | TR-007–TR-011, TR-023 | OD-02, OD-04, OD-15, OD-19, OD-21 | Create/edit/audit and naming tests pass. |
| 2. First vertical slice | Implement reviewed manual intake; enforce required fields, stored contacts, approved products, whole quantities, duplicate-line control, price snapshots, pallet estimate; create suggested PO and approval preview. | TR-003–TR-005, TR-011–TR-014, TR-018 | OD-06, OD-16, OD-20–OD-21 | AT-01 through AT-08 pass; no external send is required. |
| 3. Suggested-PO communication | Complete exact approval outcomes, resubmission/reassignment logging, permitted-PDF selection, sender/recipient/package evidence, and the resolved suggested-PO send behavior. | TR-006, TR-014, TR-017–TR-018 | OD-01, OD-02, OD-06, OD-08, OD-13 | Suggested-PO package and negative-control tests pass. |
| 4. BOL, confirmation, and final PO | Add BOL entry/generation, print confirmation/reprint, BOL finalization, PO regeneration/difference approval, final PO/BOL blockers/send, inbound matching/review, and follow-ups. | TR-015, TR-019, TR-021, TR-023 | OD-01, OD-03, OD-07, OD-13, OD-22–OD-24 | BOL, confirmation, send-blocker, and retry tests pass. |
| 5. Pickup and invoice | Add pickup states/actual values, invoice draft generation, adjustments, due-date behavior, complete invoice approval and immediate send. | TR-016–TR-018, TR-021, TR-023 | OD-08–OD-14 | Pickup/invoice/approval tests pass. |
| 6. Payment and closeout | Add remittance match/review, payment notices, credit-memo balance control, user-confirmed payment, packet generation, close and cancellation controls. | TR-020–TR-021, TR-023 | OD-08, OD-13, OD-16, OD-22 | Settlement, packet, closeout, and cancellation tests pass. |
| 7. Production hardening | Implement resolved retry/timeout/duplicate-send/edit-lock rules; complete security, document-layout, integration, UAT, readiness evidence, and controlled release record. | TR-007, TR-022, TR-024–TR-028 | All open decisions | §23 checklist and applicable acceptance tests pass. |

## Sequencing rules

- No phase releases a capability that depends on an unresolved open decision.
- Every implementation item must link to a `TR-*` requirement and at least one objective acceptance test.
- Production release remains blocked until all §23 readiness items, §25 decisions, and relevant test evidence are complete.
