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
11. Invoice Adjustment
12. Approval
13. Approval Submission Cycle
14. Email Communication
15. Confirmation Issue
16. Pickup Event
17. Credit Memo
18. Credit Memo Application
19. Payment Notice
20. Settlement
21. Supporting Document
22. Order Event History
23. Final Packet

## 4. Relationship model

The following relationships support the approved workflow. Cardinality describes the logical business relationship; the final Dataverse lookup and intersect-table design will be documented in the physical data model.

| Parent record | Relationship | Related record | Purpose |
| --- | --- | --- | --- |
| Distributor | One-to-many | Distributor Location | A distributor may have one or more shipping or operating locations. |
| Distributor | One-to-many | Distributor Contact | Contacts may apply across the distributor or be limited to a location. |
| Distributor | One-to-many | Contact Role Assignment | Defines approved recipient and operational roles for the distributor. |
| Distributor | One-to-many | Distributor Product Listing | Stores the products approved for sale to that distributor. |
| Distributor | One-to-many | Order | Every order belongs to one distributor. |
| Distributor Location | One-to-many | Order | Each order uses one selected Ship To location. |
| Distributor Location | Zero-to-many | Contact Role Assignment | A role assignment may be location-specific or distributor-wide. |
| Distributor Contact | One-to-many | Contact Role Assignment | A contact may hold multiple approved roles. |
| Product | One-to-many | Distributor Product Listing | One ERIS product may have distributor-specific item information. |
| Distributor Product Listing | One-to-many | Effective-Dated Price | A distributor product may have multiple controlled price periods. |
| Order | One-to-many | Order Line | An order contains controlled product and quantity lines. |
| Product | One-to-many | Order Line | Every order line references an approved ERIS product. |
| Distributor Product Listing | One-to-many | Order Line | The order line retains the distributor item identity used at order creation. |
| Order | One-to-many | Commercial Document | An order may have PO, BOL, invoice, and revised document records. |
| Commercial Document | One-to-many | Invoice Adjustment | Invoice documents may contain separately recorded adjustments. |
| Order | One-to-many | Approval | Approval requests are retained with the affected order. |
| Approval | One-to-many | Approval Submission Cycle | Returns, revisions, resubmissions, reassignments, and decisions remain in one approval history. |
| Order | One-to-many | Email Communication | Inbound and outbound communications are linked to the order. |
| Order | One-to-many | Confirmation Issue | Each detected difference is recorded and resolved separately. |
| Order | One-to-many | Pickup Event | Scheduled, actual, revised, and issue-related pickup activity is retained. |
| Order | One-to-many | Supporting Document | Source documents and permitted supporting PDFs remain linked to the order. |
| Order | One-to-many | Payment Notice | Matched remittance or payment communications create reviewable notices. |
| Order | One-to-many | Settlement | Confirmed payment and credit-memo settlement activity remains linked to the order. |
| Credit Memo | One-to-many | Credit Memo Application | Each use of a credit memo reduces its available balance. |
| Settlement | One-to-many | Credit Memo Application | A settlement may use one or more credit memos. |
| Order | One-to-many | Order Event History | Material activity is preserved as immutable audit history. |
| Order | One-to-many | Final Packet | Regenerated packet versions remain linked to the order. |

### 4.1 Exact-version relationships

Approvals and outbound communications must identify the exact document and email-package versions reviewed or sent. The physical method—direct lookup, immutable version identifier, snapshot record, or intersect record—will be decided in the physical data model.

### 4.2 Communication attachments

An Email Communication may contain multiple Supporting Documents, and a Supporting Document may appear in more than one communication. This is logically a many-to-many relationship. The physical Dataverse implementation remains a design-stage decision.

### 4.3 Relationship controls

- Deleting a parent record must not erase audit history, sent communications, approvals, payment evidence, or prior document versions.
- Completed and canceled orders must remain available for reporting and audit.
- A canceled order cannot be reactivated; a revived business transaction requires a new linked order.
- Snapshot values on an Order Line must remain unchanged when later master data changes.
- Location-specific contact assignments take precedence only through explicitly documented recipient-selection rules.

To be developed from the approved core data model.

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
| Contact Name | Contact’s name. |
| Title | Contact’s business title or function. |
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

To be developed one record at a time.

## 6. Lifecycle and status fields

To be aligned with the controlled lifecycle metadata in the production specification.

## 7. Ownership, security, and auditing

Role assignments remain subject to OD-02 and OD-17.

## 8. Open modeling questions

- OD-05: copied-order starting state
- OD-24: exact BOL transition sequence
- OD-25: declined versus canceled lifecycle behavior

No unresolved item is assigned a default in this document.
