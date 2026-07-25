# Dataverse Logical Data Model

## Distributor Cider Order-to-Payment Workflow — Version 0.1

**Status:** Working design  
**Controlling specification:** `docs/production-spec-v0.1.md`  
**Open-decision register:** `docs/open-decisions.md`

---

## 1. Purpose

Define the Dataverse records, relationships, ownership, lifecycle fields, and audit requirements needed to support the approved Distributor Cider Order-to-Payment Workflow.

This document does not resolve deferred business decisions or define the final physical Dataverse schema.

## 2. Modeling rules

- The permanent Internal Order ID cannot be changed or reused.
- Order lines use approved products; free-form products are not allowed.
- Each order line preserves product-description and price snapshots.
- Notes exist only at the order level and may be blank.
- Prior document versions and source evidence must remain recoverable.
- Ambiguous email, document, order, and payment matches require human review.
- Material actions, status changes, approvals, sends, and payment actions require audit history.
- Canceled orders cannot be reopened.

## 3. Core records

1. Distributor
2. Distributor Location
3. Distributor Contact
4. Contact Role Assignment
5. Product
6. Distributor Product Listing
7. Effective-Dated Price
8. Order
9. Order Line
10. Commercial Document
11. Commercial Document Version
12. Invoice Adjustment
13. Approval
14. Approval Submission Cycle
15. Email Communication
16. Email Communication Attachment
17. Confirmation Issue
18. Pickup Event
19. Credit Memo
20. Credit Memo Application
21. Payment Notice
22. Settlement
23. Supporting Document
24. Order Event History
25. Final Packet

## 4. Relationship model

The following relationships support the approved workflow. Cardinality describes the logical business relationship; the final Dataverse lookup, intersect-table, and cascade behavior will be documented in the physical data model.

| Parent record | Cardinality | Related record | Required relationship rule |
| --- | --- | --- | --- |
| Distributor | 1:N | Distributor Location | Each location belongs to exactly one distributor. A distributor may have one or more locations. |
| Distributor | 1:N | Distributor Contact | Each contact belongs to exactly one distributor. |
| Distributor Contact | 1:N | Contact Role Assignment | Each assignment belongs to exactly one contact. A contact may hold multiple roles. |
| Distributor Location | 0:N | Contact Role Assignment | A role assignment may be location-specific or distributor-wide. |
| Distributor | 1:N | Distributor Product Listing | Each listing belongs to exactly one distributor. |
| Product | 1:N | Distributor Product Listing | Each listing references exactly one approved ERIS product. |
| Distributor Product Listing | 1:N | Effective-Dated Price | Each price belongs to exactly one distributor product listing. |
| Distributor | 1:N | Order | Each permanent order belongs to exactly one distributor. |
| Distributor Location | 1:N | Order | Each permanent order uses exactly one selected Ship To location. |
| Order | 1:N | Order Line | Each order line belongs to exactly one order. |
| Product | 1:N | Order Line | Each order line references exactly one approved ERIS product. |
| Distributor Product Listing | 1:N | Order Line | Each order line references exactly one distributor product listing. |
| Order | 1:N | Commercial Document | Each commercial document belongs to exactly one order. |
| Commercial Document | 1:N | Commercial Document Version | Each document version belongs to exactly one commercial document. |
| Commercial Document | 1:N | Invoice Adjustment | Each invoice adjustment belongs to one invoice document; non-invoice documents cannot receive invoice adjustments. |
| Order | 1:N | Approval | Each approval belongs to exactly one order. |
| Approval | 1:N | Approval Submission Cycle | Each submission cycle belongs to exactly one approval. |
| Order | 1:N | Email Communication | Each linked communication belongs to exactly one order. |
| Email Communication | 1:N | Email Communication Attachment | Each attachment row belongs to exactly one communication. |
| Commercial Document Version | 0:N | Email Communication Attachment | An attachment may reference an exact commercial-document version. |
| Supporting Document | 0:N | Email Communication Attachment | An attachment may instead reference an order-linked supporting document. |
| Order | 1:N | Confirmation Issue | Each confirmation issue belongs to exactly one order. |
| Order | 1:N | Pickup Event | Each pickup event belongs to exactly one order. |
| Order | 1:N | Supporting Document | Each supporting document belongs to exactly one order. |
| Order | 1:N | Payment Notice | Each payment notice belongs to exactly one order. |
| Email Communication | 0:N | Payment Notice | A payment notice may reference one matched source communication. |
| Commercial Document | 1:N | Payment Notice | Each payment notice references the expected invoice document. |
| Order | 1:N | Settlement | Each settlement belongs to exactly one order. |
| Commercial Document | 1:N | Settlement | Each settlement references exactly one invoice document. |
| Payment Notice | 0:N | Settlement | A settlement may reference one reviewed payment notice; a notice may remain unconfirmed. |
| Credit Memo | 1:N | Credit Memo Application | Each application belongs to exactly one credit memo. |
| Settlement | 1:N | Credit Memo Application | Each application belongs to exactly one settlement. |
| Commercial Document | 1:N | Credit Memo Application | Each application references exactly one invoice document. |
| Order | 1:N | Order Event History | Each event-history entry belongs to exactly one order. |
| Order | 1:N | Final Packet | Each final-packet version belongs to exactly one order. |

### 4.1 Exact-version relationships

Approvals and outbound communications must identify the exact document and package versions reviewed or sent.

- `Commercial Document` stores the durable identity and current stage of a PO, BOL, or invoice.
- `Commercial Document Version` stores each generated or registered version.
- `Approval Submission Cycle` stores the immutable package presented during that submission.
- `Email Communication Attachment` identifies the exact commercial-document version or supporting document included in a communication.
- The parent `Approval` record may point to the current submission cycle for navigation, but the immutable approval evidence belongs to the submission cycle.

The final physical lookup, snapshot, and storage implementation will be documented in the physical data model.

### 4.2 Communication attachments

An Email Communication may contain multiple attachments. A commercial-document version or supporting document may appear in more than one communication. `Email Communication Attachment` resolves those relationships and preserves the attachment filename, sequence, exact version, approval-package inclusion, and actual-send outcome.

Each attachment row must reference exactly one of the following:

- one Commercial Document Version; or
- one Supporting Document.

It must not reference both or neither.

### 4.3 Relationship controls

- Deleting a parent record must not erase audit history, sent communications, approvals, payment evidence, attachments, or prior document versions.
- Completed and canceled orders must remain available for reporting and audit.
- A canceled order cannot be reactivated; a revived business transaction requires a new linked order.
- Snapshot values on an Order Line must remain unchanged when later master data changes.
- Location-specific contact assignments take precedence only through explicitly documented recipient-selection rules.
- Draft intake data may be incomplete before permanent order creation; the permanent Order requires one distributor and one Ship To location.
- A Payment Notice may exist without a Settlement.
- A Settlement must reference one invoice document.
- An Email Communication Attachment must preserve the exact file identity used for approval and sending.

## 5. Record definitions

The fields below are logical business fields. Dataverse column names, data types, lengths, alternate keys, ownership models, and required-level settings will be defined in the physical data model.

### 5.1 Distributor

**Purpose:** Stores the controlled identity, billing information, branding, and status of each distributor.

| Logical field | Business meaning |
| --- | --- |
| Distributor | Official distributor entity name. |
| Distributor Code | Controlled short code used in document references and filenames. |
| Bill-To Information | Controlled billing name and address used on commercial documents. |
| Branding Asset | Approved distributor logo or reference to the controlled logo file. |
| Status | Active or inactive. |

**Rules**

- Orders may use only an active distributor.
- Distributor codes must be unique.
- Branding must come from a controlled asset.
- Deactivating a distributor must not change prior orders or documents.

### 5.2 Distributor Location

**Purpose:** Stores approved Ship To locations associated with a distributor.

| Logical field | Business meaning |
| --- | --- |
| Distributor | Parent distributor. |
| Location Name | Recognizable business name for the location. |
| Location Code | Controlled code used in document references and filenames. |
| Ship-To Information | Controlled Ship To name and address. |
| Status | Active or inactive. |

**Rules**

- Each location belongs to one distributor.
- Location codes must be unique within the applicable naming scope.
- Orders may use only an active location.
- Historical orders retain the location information used when the order was created.
- Approved working location codes include H for Lakeshore Halsted, A for Lakeshore Arlington, G for Grant, and S for Skeff.

### 5.3 Distributor Contact

**Purpose:** Stores approved external contacts that may be used for workflow communications.

| Logical field | Business meaning |
| --- | --- |
| Distributor | Parent distributor. |
| Location | Optional location scope; blank means distributor-wide. |
| Contact Name | Contact's name. |
| Title | Contact's business title or function. |
| Email Address | Approved external email address. |
| Phone Number | Contact phone number. |
| Status | Active or inactive. |
| Last Verified | Date the contact information was last confirmed. |
| Notes | Administrative contact notes. |

**Rules**

- External recipients must be stored contacts.
- An inactive contact cannot be selected for a new outbound package.
- A contact may be distributor-wide or location-specific.
- Prior communications retain the recipient information actually used.

### 5.4 Contact Role Assignment

**Purpose:** Identifies how an approved contact may participate in distributor communications.

| Logical field | Business meaning |
| --- | --- |
| Distributor Contact | Approved contact receiving the assignment. |
| Distributor | Distributor scope of the assignment. |
| Location | Optional location-specific scope. |
| Contact Role | PO, Logistics/BOL, Invoice/AP, Confirmation, Remittance/Payment, or Escalation. |
| Recipient Type | To or CC. |
| Primary | Identifies the primary contact for the role and scope. |

**Rules**

- A contact may hold more than one role.
- One primary contact is allowed for each role and applicable scope.
- Recipient selection must use stored role assignments.
- The precedence between location-specific and distributor-wide assignments must be documented before implementation.

### 5.5 Product

**Purpose:** Stores each controlled ERIS sellable product or package.

| Logical field | Business meaning |
| --- | --- |
| Internal SKU | Controlled sequential ERIS product identifier. |
| Internal Product Name | ERIS product name. |
| Package Format | Approved package or item format. |
| Status | Active or inactive. |

**Approved package formats**

- `1/2 BBL`
- `6/4/12 CAN`
- `24/16 CAN`
- `1/4 BBL`
- `KEG DEPOSIT`
- `TAP HANDLE`
- `TAP HANDLE-F`
- `TIN TACKERS`

**Rules**

- Each distinct sellable package is a separate product.
- Free-form products are not allowed.
- Inactive products remain available on historical order records but cannot be selected for a new order.
- The internal SKU is retained but hidden from ordinary product selection.

### 5.6 Distributor Product Listing

**Purpose:** Connects an ERIS product to the item identity used by a specific distributor.

| Logical field | Business meaning |
| --- | --- |
| Distributor | Distributor using the listing. |
| Product | Approved ERIS product. |
| Distributor Item Number | Distributor-specific item identifier. |
| Distributor Description | Distributor-specific product description. |

**Rules**

- Order entry presents distributor-specific item numbers and descriptions.
- Only listed products may be selected for that distributor.
- The same distributor and product combination must not be duplicated.
- Order lines preserve the item number and description used when the order was created.

### 5.7 Effective-Dated Price

**Purpose:** Stores controlled distributor-specific pricing periods.

| Logical field | Business meaning |
| --- | --- |
| Distributor Product Listing | Product and distributor combination being priced. |
| Price | Approved unit price. |
| Effective Start Date | First date the price may be used. |
| Effective End Date | Optional last date the price may be used. |
| Status | Controlled price-record status. |

**Rules**

- Prices are distributor-specific and effective-dated.
- Only one applicable approved price should be selected for an order line.
- The selected price is copied to the order line as a snapshot.
- Later price changes do not alter existing order-line snapshots.
- A later difference requires an approved price override or invoice adjustment.
- Overlapping active price periods must be prevented or routed for correction.


### 5.8 Order

**Purpose:** Serves as the permanent parent record for one distributor order-to-payment transaction.

| Logical field | Business meaning |
| --- | --- |
| Internal Order ID | Permanent sequential system identifier, such as `ORD-000184`. |
| Distributor | Distributor responsible for the order. |
| Distributor Location | Selected Ship To location. |
| Workflow Entry Point | Distributor PO/order email, ERIS-created suggested PO, Production-created BOL, or copied prior order. |
| Related Prior Order | Optional link to the prior order when an order is copied, revised into a new transaction, or revived after cancellation. |
| Distributor Official PO Number | Distributor-assigned PO number when supplied. |
| PO Date | Date used for the purchase-order transaction and applicable document reference. |
| Scheduled Pickup Date | Current approved scheduled pickup date. |
| Scheduled Pickup Time | Current scheduled pickup time. |
| Logistics Responsibility | Logistics by ERIS or logistics arranged by distributor. |
| Current Order Status | Current controlled lifecycle stage. |
| System Pallet Estimate | System-calculated pallet estimate. |
| Final Pallet Count | Optional user-confirmed whole-number pallet count. |
| Order Notes | One optional order-level notes field; blank is permitted. |
| Created By | User or process that created the order. |
| Created Date and Time | Date and time the permanent order record was created. |

**Rules**

- The Internal Order ID is permanent, sequential, unique, and cannot be changed or reused.
- The order must reference one approved distributor and one approved Ship To location.
- An intake draft may exist before the permanent order is created.
- The permanent order is created only after the source and required information have been reviewed.
- The source entry point must be retained.
- Copying an order creates a new Internal Order ID and may retain a link to the prior order.
- A copied order does not inherit document numbers, approvals, communications, adjustments, payments, documents, pickup status, or historical dates.
- The exact starting state of a copied order remains unresolved under OD-05.
- If Ship To changes, the Internal Order ID remains unchanged, while affected document references are regenerated according to the approved naming rules.
- Pickup-date changes require approval.
- Pickup-time-only approval-reset behavior remains unresolved under OD-03.
- The system pallet estimate and user-confirmed final pallet count are retained separately.
- Order Notes are optional, shared at the order level, and may be blank.
- Order-line notes are not permitted.
- A canceled order cannot reopen. Any later revival creates a new linked order.
- Declined and canceled orders must remain visibly distinct; detailed transitions remain unresolved under OD-25.
- Completed and canceled orders remain available for audit and reporting.

### 5.9 Order Line

**Purpose:** Stores one approved distributor product and its order-specific quantity, description, and price snapshots.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Line Sequence | Controlled display and document-printing order. |
| Product | Approved ERIS product. |
| Distributor Product Listing | Distributor-specific product identity used for the line. |
| Quantity | Current whole-unit order quantity. |
| Quantity Source | Business source of the current quantity, such as reviewed intake or confirmed BOL. |
| Distributor Item Number Snapshot | Distributor item number retained as it existed when selected. |
| Distributor Description Snapshot | Distributor description retained as it existed when selected. |
| Unit Price Snapshot | Approved unit price retained for the order. |
| Price Source | Effective-dated price or approved override that supplied the snapshot. |
| Extended Amount | Quantity multiplied by the approved unit price snapshot. |

**Rules**

- Every line belongs to one order.
- Every line must reference an approved Product and Distributor Product Listing.
- Free-form products are not allowed.
- Quantities are whole units.
- Identical products cannot appear on duplicate active lines within the same order.
- If the same product is selected twice, the user must combine the quantities or cancel the duplicate selection.
- Distributor item number, description, and unit price are snapshotted on the order line.
- Later master-data changes do not alter existing snapshots.
- The approved final PO price becomes the invoice price.
- Later price differences require an approved price override or a separate invoice adjustment.
- Finalized BOL products and quantities become the current source of truth.
- A final BOL difference must not erase the approved suggested-PO evidence or prior document versions.
- Deposits, handles, and tin tackers contribute zero to the pallet estimate.
- CAN, 1/2 BBL, and 1/4 BBL quantities contribute according to the approved pallet calculation.
- An order supports no more than 18 document-output lines.
- Order-line notes are not permitted.

### 5.10 Commercial Document

**Purpose:** Stores the durable identity and current workflow state of each PO, BOL, and invoice associated with an order.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Document Type | PO, BOL, or Invoice. |
| Document Reference | Controlled business reference printed on or associated with the document. |
| Active Filename | Current controlled ERIS filename. |
| Source Filename | Original filename when the document originated outside ERIS. |
| Current Document Stage | Current controlled PO, BOL, or invoice stage. |
| Current Version | Reference to the active Commercial Document Version. |
| Current File Link | Convenience link to the current visible file in SharePoint. |
| Created Date and Time | Date and time the durable document identity was created. |
| Created By | User or automated process that created the durable document identity. |

**Data integrity and lifecycle constraints**

- Commercial documents are limited to PO, BOL, and invoice records.
- Each commercial document belongs to one order.
- Document references and filenames follow the approved controlled naming rules.
- The distributor official PO number is stored and printed where required but is not placed in the ERIS filename.
- The current version reference must identify exactly one Commercial Document Version belonging to the same Commercial Document.
- Prior versions must remain recoverable.
- A revised BOL keeps the same document number and filename.
- Whether PO, BOL, and invoice require separate physical Dataverse tables or one shared table with type-specific fields remains a physical-model decision.

**Related workflow requirements**

- Finalizing the BOL makes its confirmed products and quantities the source of truth.
- Finalizing the BOL regenerates the final PO using the same PO number and filename.
- If the final PO differs from the approved suggested PO, final PO approval is required.
- The combined final PO/BOL package cannot be sent until all approved blockers are cleared.
- The invoice is generated from confirmed BOL quantities and approved final PO prices.

### 5.11 Commercial Document Version

**Purpose:** Preserves each exact generated or registered version of a commercial document.

| Logical field | Business meaning |
| --- | --- |
| Commercial Document | Parent durable document identity. |
| Version Identifier | Permanent identifier for the exact generated or uploaded version. |
| Revision Number | Controlled revision number where revisions are supported. |
| File Link | Link to the exact file version or retained file evidence. |
| Is Current Version | Indicates whether this is the active version for the parent document. |
| Generated or Registered Date and Time | Date and time the version was generated or registered. |
| Generated or Registered By | User or automated process that created or registered the version. |
| Template Version | Controlled template version used to generate the PDF, when applicable. |
| Revision Marking | Indicates whether the version displays `REVISED` and the revision number. |
| Confirmed Printed | Indicates whether this exact BOL version was physically printed and confirmed. |
| Confirmed Printed By | User who confirmed successful physical printing. |
| Confirmed Printed Date and Time | Date and time physical printing was confirmed. |
| Sent Date and Time | Date and time this exact version was successfully sent, when applicable. |
| Superseded Date and Time | Date and time the version ceased to be current. |

**Data integrity and lifecycle constraints**

- Every version belongs to one Commercial Document.
- Version Identifier is permanent and unique.
- Only one version may be current for a Commercial Document.
- Approvals and outbound communications must reference the exact version reviewed or sent.
- Replacing the current visible PDF must not remove prior version evidence.
- Source filenames remain on the durable Commercial Document when the source originated outside ERIS.
- Revising a previously printed BOL creates a new version and returns the document to Reprint Required.
- Printing alone does not set Confirmed Printed.
- Confirmed Printed records the user, time, and exact version.
- A failed combined send marks neither document version as Sent.
- SharePoint version history may support file retention, but the logical model still requires a durable exact-version identifier.

### 5.12 Invoice Adjustment

**Purpose:** Stores a separately presented change applied to an invoice.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Invoice Document | Invoice receiving the adjustment. |
| Adjustment Type | Freight, Credit Memo, Deposit Adjustment, or Other. |
| Description | Explanation of the adjustment; required for Other. |
| Amount | Positive or negative adjustment amount. |
| Approval | Approval record governing the adjustment. |
| Adjustment Status | Current review or approval state. |
| Created By | User who entered the adjustment. |
| Created Date and Time | Date and time the adjustment was entered. |

**Rules**

- Multiple adjustments may be associated with one invoice.
- Approved adjustment types are Freight, Credit Memo, Deposit Adjustment, and Other.
- Other requires a description.
- Every invoice adjustment requires approval.
- Adjustments appear as separate invoice lines.
- An adjustment does not overwrite the original order-line price snapshot.
- Adjustment and settlement records must preserve separate audit evidence.
- Implementation must prevent one credit value from reducing the amount due both as an invoice adjustment and again as a settlement application.
- The relationship between an Invoice Adjustment of type Credit Memo and a Credit Memo Application remains unresolved and must not permit the same credit value to be counted twice.

### 5.13 Approval

**Purpose:** Stores the continuing approval case associated with an order action, document, email package, or proposed change.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Approval Type | Suggested PO package, final PO change, price override, pickup-date change, invoice adjustment, invoice package, or another approved type. |
| Approval Status | Current controlled approval stage. |
| Requester | User who requested approval. |
| Current Approver | Eligible user currently responsible for the decision. |
| Current Submission Cycle | Optional navigation reference to the latest Approval Submission Cycle. |
| Requested Date and Time | Date and time approval was first requested. |
| Closed Date and Time | Date and time the approval history was permanently closed. |
| Closed By | Authorized user who closed the approval. |

**Data integrity and lifecycle constraints**

- Approvals are action-specific.
- The Approval record represents the continuing approval case; immutable package evidence belongs to Approval Submission Cycle.
- Response options are Approve, Reject, and Return for Changes.
- Reject and Return for Changes require comments.
- Approve does not require a comment.
- One approval decision is required for each submitted cycle.
- Returned and rejected-but-open approvals may be revised and resubmitted within the same approval history.
- Close Approval permanently ends the approval request.
- Who may approve, reassign, or close an approval remains subject to OD-02.
- Reminder timing and escalation remain subject to OD-01.
- Suggested-PO post-approval send behavior remains subject to OD-06.
- Post-approval invoice-change behavior remains subject to OD-11.
- Approval validity after invoice send failure remains subject to OD-12.

### 5.14 Approval Submission Cycle

**Purpose:** Preserves each submission, return, revision, reassignment, and decision within one approval history.

| Logical field | Business meaning |
| --- | --- |
| Approval | Parent approval request. |
| Submission Sequence | Controlled sequence number for the submission cycle. |
| Submitted By | User or process submitting the cycle. |
| Submitted Date and Time | Date and time the cycle was submitted. |
| Approver | Eligible approver assigned to the cycle. |
| Decision | Approve, Reject, or Return for Changes. |
| Decision Comments | Comments entered with the decision. |
| Decision Date and Time | Date and time the decision was recorded. |
| Package Snapshot Identifier | Permanent identifier for the immutable package presented. |
| Related Document Version | Exact Commercial Document Version presented, when applicable. |
| To Recipients Snapshot | Exact To recipients presented for approval. |
| CC Recipients Snapshot | Exact CC recipients presented for approval. |
| Subject Snapshot | Exact subject presented for approval. |
| Body Snapshot | Exact body presented for approval. |
| Attachment Manifest Snapshot | Exact ordered attachment list and version identifiers presented for approval. |
| Reassigned From | Previous approver, when reassigned. |
| Reassigned To | New eligible approver. |
| Reassignment Reason | Optional explanation for reassignment. |
| Reassigned By | Requester or current approver who performed the reassignment. |
| Reassignment Date and Time | Date and time of reassignment. |

**Rules**

- Submission cycles remain within one parent Approval record until Close Approval.
- Every submission cycle preserves the exact document version, recipients, subject, body, attachment order, and attachment versions reviewed.
- Reassignment is limited to eligible approvers.
- A reassignment reason is optional.
- Reassignment details are always logged.
- A new submission cycle must not erase earlier decisions, comments, versions, or assignments.
- The physical storage method for the immutable package remains a physical-model decision, but the logical ownership of that evidence remains on the submission cycle.

### 5.15 Email Communication

**Purpose:** Stores inbound and outbound order communications and the exact communication content used by the workflow.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Direction | Inbound or outbound. |
| Mailbox Message ID | Outlook identifier for the retained message. |
| Sender | Actual sender used or received. |
| To Recipients | Exact To recipients. |
| CC Recipients | Exact CC recipients. |
| Subject | Final email subject. |
| Body | Final complete email body. |
| Communication Type | Suggested PO, final PO/BOL, invoice, confirmation, follow-up, cancellation, remittance, or another controlled type. |
| Template Reference | Controlled template used, when applicable. |
| Sent or Received Date and Time | Actual communication timestamp. |
| Match Status | Strong match, ambiguous/review required, linked manually, unlinked, or another controlled matching state. |
| Material for Final Packet | User-controlled inclusion flag for material correspondence. |
| Send Status | Prepared, sent, failed, or another controlled technical state. |
| Failure Details | Recorded send or processing failure information. |

**Rules**

- Outbound recipients must be approved stored contacts.
- The exact sender, recipients, subject, body, attachment manifest, document versions, and timestamp must be retained.
- Sent messages must appear in Outlook Sent Items.
- Strong inbound matches may link automatically.
- Ambiguous matches are never guessed and must enter review.
- A user may unlink an irrelevant communication, and the action must be logged.
- Confirmation differences do not overwrite order data automatically.
- A failed send must preserve the communication and its Email Communication Attachment rows for controlled retry.
- Detailed revised-email statuses remain subject to OD-07.
- Exact matching thresholds remain subject to OD-22.
- Duplicate-send and processing controls remain subject to OD-13.

### 5.16 Email Communication Attachment

**Purpose:** Links an email communication to the exact commercial-document version or supporting document included in the prepared or sent package.

| Logical field | Business meaning |
| --- | --- |
| Email Communication | Parent communication. |
| Commercial Document Version | Exact commercial-document version attached, when applicable. |
| Supporting Document | Supporting document attached, when applicable. |
| Attachment Filename Snapshot | Exact filename presented or sent. |
| Attachment Sequence | Controlled attachment order within the package. |
| Included in Approved Package | Indicates that the attachment was part of the approved package. |
| Included in Actual Send | Indicates that the attachment was included in the successfully sent message. |
| Attachment Status | Prepared, approved, sent, failed, removed before submission, or another controlled state. |
| Added By | User or process that added the attachment. |
| Added Date and Time | Date and time the attachment was added. |
| Failure Details | Technical failure information specific to the attachment, when applicable. |

**Data integrity and lifecycle constraints**

- Every attachment belongs to one Email Communication.
- Each attachment references exactly one Commercial Document Version or one Supporting Document.
- An attachment must not reference both source types.
- The attachment filename and sequence are retained as snapshots.
- Approval evidence and send evidence must preserve the exact attachment version.
- A failed send must not set Included in Actual Send.
- Message-specific attachment-category rules remain subject to OD-08.
- Duplicate-send and processing controls remain subject to OD-13.

### 5.17 Confirmation Issue

**Purpose:** Stores each detected difference between distributor communication and the current order.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Source Communication | Email or source evidence containing the difference. |
| Field or Subject | Order field, product, quantity, date, price, or other value in question. |
| Source Value | Value received from the distributor or source document. |
| Current Order Value | Current controlled order value. |
| Issue Status | Review required, resolved, or another controlled review stage. |
| Resolution | Approved explanation or selected outcome. |
| Resolved By | Authorized user resolving the difference. |
| Resolved Date and Time | Date and time the issue was resolved. |

**Rules**

- Each difference is retained separately.
- Differences do not overwrite the order automatically.
- An order cannot be marked confirmed until all required confirmation issues are resolved.
- Resolution actions and resulting order changes must be recorded in Order Event History.
- The source communication remains linked and recoverable.

### 5.18 Pickup Event

**Purpose:** Preserves scheduled, actual, revised, readiness, completion, and issue-related pickup activity.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Pickup Status | Scheduled, Ready for Pickup, Picked Up, or Pickup Issue. |
| Scheduled Pickup Date | Scheduled pickup date applicable to the event. |
| Scheduled Pickup Time | Scheduled pickup time applicable to the event. |
| Actual Pickup Date | Actual pickup date recorded at pickup. |
| Actual Pickup Time | Actual pickup time recorded at pickup. |
| Issue Details | Explanation of a pickup issue or discrepancy. |
| Recorded By | User recording the event. |
| Recorded Date and Time | Date and time the event was recorded. |

**Rules**

- Scheduled and actual values are retained separately.
- Scheduled values may be used as defaults for actual pickup values.
- Differences between scheduled and actual pickup are retained and logged.
- Pickup-date changes require approval.
- Pickup-time-only approval-reset behavior remains subject to OD-03.
- Marking Picked Up triggers invoice-draft generation.
- A Pickup Issue remains visible until resolved through an approved operational action.

### 5.19 Credit Memo

**Purpose:** Stores the controlled value and remaining availability of a distributor credit memo.

| Logical field | Business meaning |
| --- | --- |
| Distributor | Distributor associated with the credit memo. |
| Credit Memo Number | Distributor or ERIS credit memo reference. |
| Original Amount | Original approved credit value. |
| Available Balance | Remaining unapplied value. |
| Credit Memo Status | Available, Partially Used, or Fully Used. |
| Source Document | Supporting credit memo PDF or evidence. |
| Created Date and Time | Date and time the record was created. |
| Created By | User or process creating the record. |

**Rules**

- The original amount remains unchanged.
- Available Balance is reduced only through recorded Credit Memo Applications.
- A credit memo cannot be applied beyond its available balance.
- Credit memo use must not be recorded twice.
- Status is derived from original amount, available balance, and application history.
- Source evidence remains linked and recoverable.

### 5.20 Credit Memo Application

**Purpose:** Stores each application of credit memo value to an invoice settlement.

| Logical field | Business meaning |
| --- | --- |
| Credit Memo | Credit memo being applied. |
| Settlement | Settlement receiving the credit. |
| Invoice Document | Invoice receiving the credit. |
| Amount Applied | Credit value applied in this transaction. |
| Applied Date and Time | Date and time the application was confirmed. |
| Applied By | Authorized user confirming the application. |

**Rules**

- Each application reduces the Credit Memo Available Balance.
- The applied amount must be greater than zero.
- The applied amount cannot exceed the available balance.
- Reversal or correction behavior must preserve the original application and audit history.
- One settlement may include multiple credit memo applications.
- One credit memo may be applied across multiple settlements until fully used.

### 5.21 Payment Notice

**Purpose:** Stores extracted remittance or payment information received for review.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Source Communication | Matched remittance or payment email. |
| Invoice Document | Expected invoice associated with the notice. |
| Payment Amount | Amount extracted from the notice. |
| Payment Date | Payment or remittance date extracted from the notice. |
| Payment Reference | Check, ACH, remittance, or other reference. |
| Credit Memo Information | Credit memo references identified in the notice. |
| Match Status | Strong match or review required. |
| Discrepancy Details | Difference between the notice and expected settlement. |
| Review Status | Current human-review state. |
| Created Date and Time | Date and time the notice was created. |

**Rules**

- A strongly matched remittance may create a Payment Notice automatically.
- A Payment Notice does not mark the invoice Paid.
- Ambiguous matches require human review.
- Mismatches create Payment Discrepancy / Review Required.
- Extracted values remain reviewable before payment confirmation.
- Exact extraction and match criteria remain subject to OD-22.

### 5.22 Settlement

**Purpose:** Stores the user-confirmed settlement of an invoice through payment, credit memos, or both.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Invoice Document | Invoice being settled. |
| Payment Notice | Source notice reviewed for the settlement. |
| Cash Payment Amount | Confirmed cash or electronic payment amount. |
| Payment Date | Confirmed settlement date. |
| Payment Reference | Confirmed payment reference. |
| Credit Memo Total | Total confirmed credit memo value applied. |
| Total Settlement Amount | Confirmed payment plus applied credit memos. |
| Discrepancy Status | Indicates whether unresolved differences remain. |
| Confirmed By | User pressing Confirm Payment. |
| Confirmed Date and Time | Date and time payment was confirmed. |

**Rules**

- The system never confirms payment solely because a remittance email was received.
- A user must review the settlement and press Confirm Payment.
- One settlement may combine payment and multiple credit memos.
- Payment discrepancies remain Review Required until resolved.
- Confirming settlement moves the order toward Ready for Closeout.
- Settlement confirmation must be recorded in Order Event History.
- Reversal or amendment behavior must preserve the original confirmation and audit record.

### 5.23 Supporting Document

**Purpose:** Stores source documents and additional order-linked PDFs that are not the controlled current PO, BOL, or invoice.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Document Category | Controlled PDF category. |
| Other Description | Required description when category is Other. |
| Source Filename | Original uploaded filename. |
| Active Filename | Controlled active filename where one is assigned. |
| File Link | SharePoint file location. |
| Can Be Sent | Indicates whether the category may be attached externally. |
| Blocked From Sending | Indicates that sending is prohibited. |
| Material for Final Packet | User-selected packet inclusion flag. |
| Uploaded By | User or process uploading the PDF. |
| Uploaded Date and Time | Date and time the file was registered. |

**Approved categories**

- Distributor PO
- Supporting Order Document
- Credit Memo
- Remittance / Payment Evidence
- Distributor Correspondence
- Approval or Exception Support
- Other

**Rules**

- Only PDFs may be uploaded through this workflow.
- Other requires a description.
- Blocked categories cannot be overridden.
- Email attachment pickers show only order-linked permitted PDFs.
- Source filenames are preserved as metadata.
- Message-specific attachment rules remain subject to OD-08.
- Supporting documents remain linked after order completion or cancellation.

### 5.24 Order Event History

**Purpose:** Provides the immutable activity record needed to reconstruct material order activity.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Event Type | Controlled category of action or system event. |
| Event Description | Human-readable description of what occurred. |
| Performed By | User, connection, or automated process responsible. |
| Event Date and Time | Date and time the event occurred. |
| Related Record Type | Approval, document, email, payment, pickup, line, or other related record type. |
| Related Record | Identifier or link to the affected record. |
| Prior Value | Prior material value or status, where applicable. |
| New Value | New material value or status, where applicable. |
| Document or Package Version | Exact version involved, where applicable. |
| Failure Details | Technical or business failure information, where applicable. |

**Rules**

- Order Event History is append-only and immutable to ordinary users.
- Material changes, status changes, approvals, sends, printing confirmations, payment actions, reopen actions, and failures are logged.
- Failures must be logged even if notification delivery also fails.
- History must preserve the user or automated identity and timestamp.
- Historical entries must not be deleted when a related record is revised, superseded, completed, or canceled.
- The audit history must support reconstruction of the order from intake through closeout.

### 5.25 Final Packet

**Purpose:** Stores each generated closeout packet and its included-content manifest.

| Logical field | Business meaning |
| --- | --- |
| Order | Parent order. |
| Packet Version | Controlled generated-packet version. |
| Packet File Link | Link to the generated PDF packet. |
| Contents Manifest | Documents and communications included in the packet. |
| Generated By | User or automated process generating the packet. |
| Generated Date and Time | Date and time the packet was generated. |
| Reviewed By | User reviewing the packet before closeout. |
| Reviewed Date and Time | Date and time review was completed. |
| Closeout Reference | Link or reference to the final Close Order action. |

**Rules**

- The packet includes the PO, BOL, invoice, payment/remittance correspondence, and user-marked material order communications.
- The packet includes a summary page with the Internal Order ID and approval/workflow-history references.
- The user controls which material communications are included.
- Payment confirmation prepares the packet and moves the order to Ready for Closeout.
- A user must review the packet before pressing Close Order.
- Regenerated packet versions remain recoverable.
- Final visual layout remains subject to OD-16.

## 6. Lifecycle and status fields

The controlled values below reproduce the working lifecycle metadata from the production specification. They do not define every permitted transition. Exact transition tables remain required where identified as open decisions.

### 6.1 Order status

- Draft
- Suggested PO Approval Pending
- Suggested PO Sent
- Distributor Confirmation Pending
- Distributor Confirmed
- Distributor Declined
- Confirmation Issue / Review Required
- Scheduled
- Ready for Pickup
- Picked Up
- Pickup Issue
- Payment Discrepancy / Review Required
- Ready for Closeout
- Complete
- Canceled
- No Response - Human Intervention Required

**Known controls**

- Incomplete intake remains a draft.
- The listed values are controlled working statuses, not a complete transition table.
- The permanent order is created only after reviewed intake.
- Confirmation differences move the order into review rather than overwriting values.
- Ready for Pickup and Picked Up are recorded by authorized users.
- Marking Picked Up triggers invoice-draft generation.
- Payment discrepancies remain visible until resolved.
- Confirmed settlement prepares the order for closeout.
- Close Order is a separate user action.
- Canceled orders cannot reopen.
- Declined and canceled outcomes must remain visibly distinct.
- Exact declined-versus-canceled transitions remain subject to OD-25.

### 6.2 PO stage

- Suggested
- Final Approval Pending
- Approved for Sending
- Sent
- Superseded, when applicable

**Known controls**

- Suggested PO sending requires the approved package control.
- Final BOL differences may move the PO to Final Approval Pending.
- The combined PO/BOL send remains blocked while final PO approval is pending.
- Prior suggested and final versions remain recoverable.

### 6.3 BOL stage

- Generated
- Reprint Required
- Finalized
- Confirmed Printed
- Sent as Supporting Document
- Superseded

**Known controls**

- Printing alone does not create Confirmed Printed status.
- A revision after printing creates Reprint Required.
- Confirmed Printed is tied to the current BOL version.
- The final PO/BOL send requires Confirmed Printed.
- The exact permitted transition sequence remains subject to OD-24.

### 6.4 Invoice stage

- Draft
- Ready for Review
- Approval Pending
- Approved for Sending
- Sent
- Paid / Settled

**Known controls**

- Picked Up creates the invoice draft.
- Invoice adjustments require approval.
- The approval package contains the exact PDF, recipients, subject, body, and attachments.
- Approve immediately sends the exact package.
- A remittance email alone does not create Paid / Settled status.
- Confirm Payment is required.

### 6.5 Credit memo status

- Available
- Partially Used
- Fully Used

**Known controls**

- Status reflects application history and remaining balance.
- Use beyond the available balance is prohibited.

### 6.6 Approval status

- Pending
- Returned for Changes
- Rejected but Open
- Approved
- Closed

**Known controls**

- Returned and rejected-but-open approvals may be revised and resubmitted.
- Closed approval histories cannot be resubmitted.
- Who may Close Approval remains subject to OD-02.

## 7. Ownership, security, edit control, and auditing

### 7.1 Ownership

Final record ownership has not been assigned.

The physical design must document:

- Business owner
- Technical owner
- Power Platform environment owner
- Primary connection owners
- Backup connection owners
- Error-notification recipients
- Support escalation path
- Ownership model for each Dataverse table

These items remain subject to OD-17.

### 7.2 Access requirements

The access matrix must define who may:

- Create and edit orders.
- Create or deactivate distributors, locations, contacts, products, and prices.
- Create or change contact-role assignments.
- Override pricing.
- Add invoice adjustments.
- Approve each approval type.
- Reassign approvals.
- Close approvals.
- Confirm BOL printing.
- Finalize a BOL.
- Send PO, BOL, and invoice packages.
- Mark Ready for Pickup or Picked Up.
- Confirm payment.
- Apply credit memos.
- Close an order.
- Amend or reopen a completed order.
- Administer templates, logos, document categories, and banking configuration.

Role assignments remain subject to OD-02.

### 7.3 Required restrictions

- Ordinary users cannot change the permanent Internal Order ID.
- Ordinary users cannot edit controlled banking information.
- External recipients must be stored approved contacts.
- Free-form product entry is prohibited.
- Blocked attachment categories cannot be overridden.
- Canceled orders cannot be reopened.
- Ordinary users cannot alter immutable Order Event History.
- Completed orders are normally locked.
- Completed-order amendment rights remain an access decision.
- Historical evidence must not be removed through parent-record deletion.

### 7.4 Edit control

The solution requires a single-user edit lock while other users remain read-only.

The following remain unresolved under OD-04:

- Lock timeout
- Lock renewal
- Administrative override
- Abandoned-session handling
- Required audit evidence for overrides

### 7.5 Auditing

Auditing must support reconstruction of:

- Order creation and entry point
- Master-data values selected
- Order-line snapshots
- Status changes
- Pickup changes
- Approval submissions and decisions
- Reassignments
- Document generation and versions
- BOL printing confirmation
- Email preparation and sending
- Inbound communication matching
- Confirmation issue resolution
- Payment notice creation
- Payment confirmation
- Credit memo use
- Packet generation
- Closeout
- Failures, retries, and administrative actions

The physical data model must identify which Dataverse tables and columns use native auditing in addition to Order Event History.

## 8. Logical keys, uniqueness, and preservation controls

### 8.1 Required uniqueness

- Internal Order ID is unique and permanent.
- Distributor Code is unique.
- Product Internal SKU is unique.
- A distributor and product combination cannot have duplicate active Distributor Product Listings.
- Duplicate identical active products are not permitted within one order.
- Effective-dated price periods must not overlap for the same Distributor Product Listing.
- Controlled document references and filenames must comply with the approved system-wide date sequence.

### 8.2 Snapshot preservation

The following order-specific values must remain unchanged when master data later changes:

- Distributor identity used
- Ship To information used
- Distributor item number
- Distributor product description
- Unit price
- Approved override source
- Exact email recipients
- Exact email subject and body
- Exact document and attachment versions
- Scheduled and actual pickup values
- Payment and credit memo confirmation values

Corrections must create controlled changes and audit evidence rather than silently rewriting history.

### 8.3 Delete behavior

Physical delete behavior must prevent loss of:

- Orders
- Order lines used on documents
- Approvals and submission cycles
- Sent and received communications
- Document references and version evidence
- Payment notices and settlements
- Credit memo applications
- Order Event History
- Final packets

Deactivation, completion, cancellation, supersession, or another controlled status should be used where permanent evidence must be retained.

## 9. Open modeling questions

The following open decisions affect or may affect the physical model:

| Open decision | Modeling effect |
| --- | --- |
| OD-02 | Security roles, ownership, approval authority, and Close Approval permissions. |
| OD-03 | Approval-reset fields and events for pickup-time-only changes. |
| OD-04 | Edit-lock table or fields, timeout, override, and audit behavior. |
| OD-05 | Starting state and copied-data handling for copied orders. |
| OD-07 | Revised-email communication statuses. |
| OD-08 | Attachment-category eligibility by communication type. |
| OD-11 | Approval invalidation when an approved invoice package changes. |
| OD-12 | Invoice approval and retry behavior after send failure. |
| OD-13 | Processing locks, idempotency, duplicate-send protection, retries, and timeouts. |
| OD-22 | Fields and thresholds required for measurable inbound-email matching. |
| OD-24 | Exact BOL status-transition table. |
| OD-25 | Declined-order and canceled-order lifecycle distinctions. |
| Unnumbered clarification | Distinction between an invoice Credit Memo adjustment and a Credit Memo Application, including duplicate-credit prevention. |

No unresolved item receives a default behavior in this logical model.

## 10. Physical data-model handoff

The physical Dataverse model must next define:

- Final table names and publisher prefix
- Column names
- Data types and lengths
- Required and optional columns
- Choice columns and controlled values
- Lookup behavior
- Alternate keys
- Ownership type
- Auditing configuration
- Cascade and delete behavior
- File and SharePoint integration
- Calculated and rollup fields
- Currency handling
- Date and time behavior
- Exact-version references
- Commercial-document current-version implementation
- Email Communication Attachment implementation
- Processing and edit-lock fields
- Environment variables
- Configuration tables
- Security roles and teams
- Master-data import requirements

Physical design must preserve the approved logical rules and must not resolve an open business decision without a controlled specification update.

## 11. Logical-model completion checks

- [x] Every core record in the production specification is represented, including Commercial Document Version and Email Communication Attachment.
- [x] Distributor, location, contact, product, and pricing master data are represented.
- [x] Order and Order Line snapshots are represented.
- [x] One optional order-level Notes field is represented.
- [x] Order-line notes are prohibited.
- [x] PO, BOL, invoice, durable document identity, and exact revision evidence are represented.
- [x] Exact approval submission packages and email attachment versions are represented.
- [x] Confirmation review is represented without automatic overwriting.
- [x] Scheduled and actual pickup values are retained.
- [x] Payment Notice and user-confirmed Settlement are separated.
- [x] Credit memo balance and application history are represented.
- [x] Supporting-document categories and send restrictions are represented.
- [x] Immutable Order Event History is represented.
- [x] Final Packet generation and review are represented.
- [x] Controlled lifecycle values are listed.
- [x] Logical relationships, cardinalities, and required optionality are identified.
- [x] Open decisions remain unresolved and identified.
- [ ] Credit Memo adjustment versus Credit Memo Application boundary approved.
- [ ] Physical Dataverse schema completed.
- [ ] Security and ownership matrix approved.
- [ ] State-transition tables approved.
- [ ] Acceptance tests linked to physical components.

**End of logical data model - Version 0.1**
