# Traceability Matrix

## Use of this matrix

`docs/production-spec-v0.1.md` is the controlling business specification. This matrix assigns identifiers to requirement groups without changing or interpreting the business rules. A requirement is **confirmed** only when its cited section states it as approved or a build baseline. A **build-stage decision** is intentionally unresolved and must not be implemented as a rule until the controlling specification is updated.

| ID | Specification section | Requirement group | Classification | Planned delivery / evidence |
| --- | --- | --- | --- | --- |
| TR-001 | Layer 1 overview | Controlled distributor order-to-payment process, in-scope distributors/locations, named triggers, final packet, audit trail, and named target components. | Confirmed | Phase 1 foundation; end-to-end slice evidence. |
| TR-002 | §1 Documentation model | Keep operating requirements separate from automation mechanics and retain current, target, and human-exception views. | Confirmed | All phases; documentation review. |
| TR-003 | §2 Current/target process | Capture/review intake; controlled IDs/master data; controlled documents, approvals, pickup, invoice, payment, and closeout with stated human gates. | Confirmed | Phases 1–6; scenario tests. |
| TR-004 | §3 Steps 1–34 | Execute the ordered operating workflow from entry selection through cancellation, including each stated output and recovery path. | Confirmed | Phases 1–6; acceptance tests AT-01 through AT-28. |
| TR-005 | §4 Decision rules | Enforce the stated if/then controls for matching, contacts, products, pricing, pickups, BOL/PO, sending, invoice, payment, cancellation, credit memo, and blocked PDFs. | Confirmed except explicitly deferred behaviors | Phases 1–6; rule tests. |
| TR-006 | §5.1–§5.2 Exceptions and prohibitions | Require human review in the listed cases and never perform any prohibited automatic action. | Confirmed | Phases 1–6; negative tests. |
| TR-007 | §5.3–§5.4 Controls and recovery | Provide ID, sequence, duplicate, credit-memo, edit-lock, version-history, event-log, retry, draft-resume, amendment, and cancellation controls as stated. | Confirmed, with technical settings deferred | Phases 1–6; audit and recovery tests. |
| TR-008 | §6 Solution architecture | Use SharePoint home/library, Canvas Power App, Dataverse, Power Automate, Outlook, and controlled Word-to-PDF templates; exclude Power Pages. | Confirmed | Phase 1; architecture review. |
| TR-009 | §7 Core data model | Support every listed logical record and its stated minimum responsibility. | Confirmed logical model; physical design is build work | Phases 1–6; data-model review. |
| TR-010 | §8 Identifiers and naming | Generate permanent order IDs, controlled document references, location codes, date-based system-wide suffixes, and preserve source filename metadata. | Confirmed | Phases 1–2; naming tests. |
| TR-011 | §9 Master data and calculations | Use allowed product formats, whole units, distributor/effective-dated pricing snapshots, pallet calculation, and controlled contact roles. | Confirmed | Phases 1–2; calculation and validation tests. |
| TR-012 | §10 Entry points | Support reviewed distributor intake, ERIS-created Lakeshore suggested PO, production-created BOL, and selective copy/revise behavior. | Confirmed | Phase 2 onward; entry-point tests. |
| TR-013 | §11 Output standards | Create one-page portrait PO/BOL/invoice PDFs, support up to 18 lines, apply stated branding/version/note rules. | Confirmed | Phase 3; rendering tests. |
| TR-014 | §12 Suggested PO communication | Produce the stated suggested-PO content, summary, subject, approval package, and only the suggested PO attachment. | Confirmed except post-approval send behavior | Phase 3; package test. |
| TR-015 | §13 BOL and final PO communication | Control BOL print/reprint/finalization, PO regeneration/approval, combined-send blockers, attachment order, subject, and sent statuses. | Confirmed | Phase 4; workflow tests. |
| TR-016 | §14 Pickup, invoice, and invoice email | Track pickup, create invoice from BOL/approved pricing, control adjustments/terms, and approve/send the exact invoice package. | Confirmed except listed deferred details | Phase 5; invoice tests. |
| TR-017 | §15 Attachments and communications | Accept only categorized PDFs; apply send eligibility; preserve email/package evidence and Outlook Sent Items/history linkage. | Confirmed except message-category refinements | Phases 3–5; attachment/email tests. |
| TR-018 | §16 Approval framework | Record action-specific exact-package approvals, outcomes, comments, reassignment, resubmission, and reminders. | Confirmed except access and reminder details | Phases 3–5; approval tests. |
| TR-019 | §17 Confirmation, no response, cancellation, and revision | Match/link communications, require review for differences, use the stated follow-up schedule, and enforce cancellation/decline behavior. | Confirmed | Phase 4; matching and lifecycle tests. |
| TR-020 | §18 Payment and closeout | Create payment notices from strong matches, require user payment confirmation, control credit memo balances, generate/review packet, and close. | Confirmed | Phase 6; settlement and closeout tests. |
| TR-021 | §19 Flow inventory | Deliver business capabilities DCO-01 through DCO-14, subject to their stated human gates and current-status notes. | Confirmed inventory; working names may change | Phases 1–6; flow inventory review. |
| TR-022 | §20 Technical build register | Document locations, owners, triggers, variables, filters, timeout/retry settings, test date, and deployment state before production. | Confirmed requirement; many values are TBD | Phase 1 and production readiness; configuration record. |
| TR-023 | §21 Lifecycle metadata | Use the controlled working stages for orders, documents, credit memos, and approvals as metadata, not necessarily PDF content. | Confirmed | Phases 1–6; state-transition tests. |
| TR-024 | §22 Access and ownership | Define the listed privileges, owners, connection ownership, notifications, and escalation path. | Required but unassigned | Prerequisite before production; access matrix. |
| TR-025 | §23 Production readiness | Complete every checklist item before production release. | Confirmed release gate | Pre-production; readiness sign-off. |
| TR-026 | §24 Acceptance criteria | Demonstrate all listed acceptance standards for intake, documents, naming, approvals, BOL, sending, invoice, communications, payment, closeout, and auditability. | Confirmed | `docs/acceptance-tests.md`. |
| TR-027 | §25 Deferred build-stage decisions | Resolve, document, test, and control each listed decision before production; do not silently implement it. | Build-stage decision | `docs/open-decisions.md`. |
| TR-028 | §26 Document control | Preserve specification version, source boundary, and next controlled-update triggers. | Confirmed | Change-control review. |

## Coverage rules

- Every backlog item and acceptance test must cite one or more `TR-*` IDs and the corresponding specification section.
- A requirement marked as a build-stage decision is a dependency, not implementation authorization.
- A change to a confirmed requirement requires a controlled update to `docs/production-spec-v0.1.md` before it is released.
