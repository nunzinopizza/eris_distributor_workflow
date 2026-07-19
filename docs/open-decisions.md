# Open Decisions

## Status convention

The entries below are not new business rules. They either reproduce a deferred decision from §25 of the controlling specification or record an ambiguity/dependency that must be resolved before the affected capability is released. No default is assumed.

| ID | Type | Specification reference | Decision, ambiguity, or dependency | Required outcome before release |
| --- | --- | --- | --- | --- |
| OD-01 | Deferred decision | §25; §16 | Approval reminder timing, cadence, and escalation. | Controlled timing and escalation rules. |
| OD-02 | Deferred decision | §25; §22 | Role/permission matrix, including Close Approval authority. | Approved access matrix and assigned roles. |
| OD-03 | Deferred decision | §25; §4 | Whether pickup-time-only changes reset PO approval. | Controlled approval-reset behavior. |
| OD-04 | Deferred decision | §25; §5.3 | Edit-lock timeout and administrative override behavior. | Timeout/override rules and audit evidence. |
| OD-05 | Deferred decision | §25; §10 | Whether a copied order opens immediately as an editable Draft. | Defined copy-entry state. |
| OD-06 | Deferred decision | §25; §3 step 10; §12 | Whether suggested-PO approval immediately sends or enables a separate send. | One controlled post-approval send path. |
| OD-07 | Deferred decision | §25 | Detailed revised-email workflow statuses. | Controlled statuses and transitions. |
| OD-08 | Deferred decision | §25; §15 | Message-specific allowed/blocked attachment-category rules. | Category matrix for each email type. |
| OD-09 | Deferred decision | §25; §14 | Whether both pickup date and invoice date appear when they differ. | Approved invoice presentation rule. |
| OD-10 | Deferred decision | §25; §8 | Whether the invoice footer displays Internal Order ID. | Approved template rule. |
| OD-11 | Deferred decision | §25; §14 | Whether post-approval invoice PDF/body changes reset approval. | Controlled approval-version rule. |
| OD-12 | Deferred decision | §25; §14 | Invoice send-failure behavior and approval validity after failure. | Failure/retry and approval-validity rule. |
| OD-13 | Deferred decision | §25; §5.3–§5.4 | Duplicate-send, processing-lock, retry, timeout, and detailed error controls. | Tested operational-control design. |
| OD-14 | Deferred decision | §25; §14 | Recognized holiday calendar for due dates. | Named controlled calendar and maintenance owner. |
| OD-15 | Deferred decision | §25; §20 | SharePoint site/library/folder, environment, and connection-owner configuration. | Recorded production configuration and owners. |
| OD-16 | Deferred decision | §25; §11; §18 | Final document-template refinements and final-packet summary layout. | Approved rendered templates. |
| OD-17 | Missing dependency | §20; §22; §23 | Business owner, technical owner, environment owner, primary/backup connection owners, error recipients, and support escalation are TBD. | Named owners and support path. |
| OD-18 | Missing dependency | §20; §23 | SharePoint library must provide version history, metadata, order linkage, and permitted-PDF controls; its location is TBD. | Provisioned and validated library. |
| OD-19 | Missing dependency | §20; §23 | Dataverse solution/environment and auditing configuration are TBD. | Provisioned solution with required auditing. |
| OD-20 | Missing dependency | §11; §23 | Controlled logos and Word-to-PDF templates are required but not supplied in the specification package. | Approved assets and 18-line rendering evidence. |
| OD-21 | Missing dependency | §9; §22; §23 | Distributor, location, contact, product, price, and logo master data must be built and validated. | Approved master-data load and owner. |
| OD-22 | Unclear requirement | §17; §4 | A “strong” inbound-email/remittance match is required, while exact matching filters/expressions are deferred. The measurable threshold is not defined. | Approved, testable matching criteria and review route. |
| OD-23 | Unclear requirement | §4; §17 | Follow-ups are “next business day” then “daily/calendar day”; holidays and the meaning of the third unanswered follow-up need operational test cases. | Approved schedule examples aligned to the holiday decision. |
| OD-24 | Unclear requirement | §3; §13; §21 | The exact allowable sequence of BOL Generated, Reprint Required, Finalized, and Confirmed Printed is not expressed as a transition table. | State-transition table without changing stated blockers. |
| OD-25 | Unclear requirement | §3; §17 | A canceled order cannot reopen, while a declined order may be revised under the same order or copied. These are not contradictory, but the system must distinguish “declined” from “canceled” visibly. | Defined lifecycle terminology and transitions. |

## Contradiction review

No direct contradiction was found among the approved requirements. The items labelled **Unclear requirement** identify places where more precision is needed for a build or test; they are not contradictions and do not authorize a default behavior.

## Resolution rule

Each open item requires an owner, decision, effective date, specification update, and a linked acceptance test before production release, consistent with §25 and §26.
