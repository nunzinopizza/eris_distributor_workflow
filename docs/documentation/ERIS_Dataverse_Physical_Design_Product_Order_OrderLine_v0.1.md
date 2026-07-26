# ERIS Dataverse Physical Design — Product, Distributor Order, and Order Product Line

**Document ID:** DOC-007-PHYS-001  
**Version:** 0.1  
**Status:** Draft for physical-design approval  
**Prepared:** July 26, 2026  
**Publisher customization prefix:** `eris`  
**Scope:** Physical Dataverse specifications for the already-approved Product, Order, and Order Line designs. This document does not redesign business fields.

---

## 1. Governing rules

1. All custom Dataverse components use the approved `eris` publisher prefix.
2. Display names, schema names, logical names, Dataverse data types, behavior, requirement levels, source, validation, security, and auditing are documented separately.
3. Schema names are immutable after creation.
4. Microsoft system columns are not renamed.
5. Open business decisions remain unresolved and are not silently converted into defaults.
6. Relationships are documented here only where required by the already-approved fields. Cascade behavior remains subject to relationship approval.
7. The next dependency-driven table after these three is **Distributor Product Listing**, because Order Product Line requires that lookup.

---

# 2. Product table

## 2.1 Table specification

| Property | Physical specification |
|---|---|
| Display Name | Product |
| Plural Display Name | Products |
| Description | Controlled ERIS sellable product or package used in distributor order entry. |
| Schema Name | `eris_Product` |
| Logical Name | `eris_product` |
| Entity Set Name | `eris_products` |
| Table Type | Standard custom table |
| Record Ownership | Organization-owned |
| Primary ID | `eris_productid` |
| Primary Name Column | Internal Product Name — `eris_internal_product_name` |
| Attachments | No |
| Activities | No |
| Connections | No |
| Email | No |
| Access Teams | No |
| Feedback | No |
| Dataverse Search | Yes |
| Offline Availability | No — not approved |
| Queue Availability | No |
| SharePoint Document Management | No |
| Duplicate Detection | Yes |
| Track Changes | Yes |
| Auditing | Yes |
| Long-Term Retention | Not yet approved |
| Quick Create | Administrator-only, if enabled |
| Main Form | Product Administration |
| Primary Views | Active Products; Inactive Products; All Products |
| Alternate Keys | Internal SKU |
| Status Strategy | Microsoft Active/Inactive state plus approved `is_active` business column |
| Managed Properties | Customization restricted in managed deployment; exact locks to be set before export |

## 2.2 Product columns

### Internal SKU

| Property | Specification |
|---|---|
| Display Name | Internal SKU |
| Schema Name Portion | `internal_sku` |
| Full Schema Name | `eris_internal_sku` |
| Logical Name | `eris_internal_sku` |
| Description | Internal, system-controlled sequential ERIS product identifier. |
| Dataverse Data Type | Single Line of Text |
| Format | Text |
| Behavior | Simple |
| Requirement Level | Business Required |
| Data Source | System Generated |
| Default Value | None |
| Maximum Length | 30 |
| Searchable | Yes |
| Sortable | Yes |
| Dashboard Availability | Yes |
| AI Form Fill | No |
| App Visibility | Visible to administrators; hidden from ordinary product selection |
| App Editability | Read-only |
| Column Security | No |
| Auditing | Yes |
| Business Validation Rules | Must be unique; cannot be changed or reused after assignment. |
| Alternate Key Participation | Yes — sole column in Product Internal SKU alternate key |
| Enforcement | Server-side generation required; Canvas App must not create or edit the value. |
| Managed Properties | Cannot be deleted or have type changed after production deployment |

### Internal Product Name

| Property | Specification |
|---|---|
| Display Name | Internal Product Name |
| Schema Name Portion | `internal_product_name` |
| Full Schema Name | `eris_internal_product_name` |
| Logical Name | `eris_internal_product_name` |
| Description | Controlled ERIS product name. |
| Dataverse Data Type | Single Line of Text |
| Format | Text |
| Behavior | Simple |
| Requirement Level | Business Required |
| Data Source | User Entered |
| Default Value | None |
| Maximum Length | 200 |
| Searchable | Yes |
| Sortable | Yes |
| Dashboard Availability | Yes |
| AI Form Fill | No |
| App Visibility | Yes |
| App Editability | Administrator-only |
| Column Security | No |
| Auditing | Yes |
| Business Validation Rules | Free-form products cannot be created during order entry; product maintenance is restricted to authorized administrators. |
| Alternate Key Participation | No |
| Managed Properties | Cannot be deleted or have type changed after production deployment |

### Packaging Type

| Property | Specification |
|---|---|
| Display Name | Packaging Type |
| Schema Name Portion | `packaging_type` |
| Full Schema Name | `eris_packaging_type` |
| Logical Name | `eris_packaging_type` |
| Description | Approved package or item format assigned through the Packaging Type table. |
| Dataverse Data Type | Lookup |
| Related Table | Packaging Type — physical specification pending |
| Behavior | Simple |
| Requirement Level | Business Required |
| Data Source | User Entered from controlled lookup |
| Searchable | Yes |
| Sortable | Yes |
| Dashboard Availability | Yes |
| AI Form Fill | No |
| App Visibility | Yes |
| App Editability | Administrator-only |
| Column Security | No |
| Auditing | Yes |
| Business Validation Rules | Must reference an approved active Packaging Type. |
| Alternate Key Participation | No |
| Relationship Delete Behavior | Restrict deletion while referenced |
| Managed Properties | Cannot be deleted or have type changed after production deployment |

### Is Active

| Property | Specification |
|---|---|
| Display Name | Is Active |
| Schema Name Portion | `is_active` |
| Full Schema Name | `eris_is_active` |
| Logical Name | `eris_is_active` |
| Description | Controls whether the product appears in normal order-entry selections. |
| Dataverse Data Type | Yes/No |
| Format | Yes/No |
| Behavior | Simple |
| Requirement Level | Business Required |
| Data Source | User Entered |
| Default Value | Yes |
| Allowed Values | Yes; No |
| Searchable | Yes |
| Sortable | Yes |
| Dashboard Availability | Yes |
| AI Form Fill | No |
| App Visibility | Yes |
| App Editability | Administrator-only |
| Column Security | No |
| Auditing | Yes |
| Business Validation Rules | `No` hides the product from normal order-entry selection but preserves it for historical records and administrator review/reactivation. |
| Alternate Key Participation | No |
| Managed Properties | Cannot be deleted or have type changed after production deployment |

---

# 3. Distributor Order table

## 3.1 Table specification

| Property | Physical specification |
|---|---|
| Display Name | Distributor Order |
| Plural Display Name | Distributor Orders |
| Description | Permanent parent record for one distributor order-to-payment transaction. |
| Schema Name | `eris_DistributorOrder` |
| Logical Name | `eris_distributororder` |
| Entity Set Name | `eris_distributororders` |
| Table Type | Standard custom table |
| Record Ownership | User or Team-owned |
| Primary ID | `eris_distributororderid` |
| Primary Name Column | Internal Order ID — `eris_internal_order_id` |
| Attachments | No |
| Activities | Yes |
| Connections | No |
| Email | No |
| Access Teams | Yes |
| Feedback | No |
| Dataverse Search | Yes |
| Offline Availability | No — not approved |
| Queue Availability | No |
| SharePoint Document Management | Yes, through related commercial-document records and controlled library integration |
| Duplicate Detection | Yes |
| Track Changes | Yes |
| Auditing | Yes |
| Long-Term Retention | Not yet approved |
| Quick Create | No |
| Main Form | Distributor Order |
| Primary Views | Active Orders; My Pending Work; Awaiting Confirmation; Awaiting Pickup; Awaiting Payment; Completed Orders; Canceled Orders |
| Alternate Keys | Internal Order ID |
| Status Strategy | Microsoft state/status plus Current Order Status business choice |
| Managed Properties | Customization restricted in managed deployment; exact locks to be set before export |

## 3.2 Distributor Order columns

| Display Name | Full Schema Name / Logical Name | Dataverse Type | Behavior | Requirement | Source | Key configuration and approved validation |
|---|---|---|---|---|---|---|
| Internal Order ID | `eris_internal_order_id` | Single Line of Text, max 30 | Simple | Business Required | System Generated | Permanent sequential identifier; unique; immutable; alternate key; ordinary users cannot edit. |
| Distributor | `eris_distributor` | Lookup to Distributor | Simple | Business Required | User Selected | Must reference one approved active distributor when the permanent order is created. Delete behavior: Restrict. |
| Distributor Location | `eris_distributor_location` | Lookup to Distributor Location | Simple | Business Required | User Selected | Must belong to the selected Distributor and represent the selected Ship To location. Delete behavior: Restrict. |
| Workflow Entry Point | `eris_workflow_entry_point` | Choice | Simple | Business Required | User/System | Approved values: Distributor PO or order email; ERIS-created suggested PO; Production-created BOL; Copied prior order. No default established. |
| Related Prior Order | `eris_related_prior_order` | Self-referential Lookup | Simple | Optional | System/User | Used only when copying, revising into a new transaction, or reviving after cancellation. Must not permit cascade deletion. |
| Distributor PO Number | `eris_distributor_po_number` | Single Line of Text, max 100 | Simple | Business Required | User/Snapshot | Distributor-assigned PO number. Searchable, sortable, audited. |
| ERIS PO Reference | `eris_eris_po_ref` | Single Line of Text, max 50 | Simple | Business Required | System Generated | Controlled ERIS PO reference. Read-only after generation; searchable, sortable, audited. |
| PO Date | `eris_po_date` | Date and Time | Date Only | Business Required | User/System | Calendar date used for the PO transaction and document reference. |
| Scheduled Pickup Date | `eris_scheduled_pickup_date` | Date and Time | Date Only | Business Required | User Entered | Pickup-date changes require approval and audit logging. |
| Scheduled Pickup Time | `eris_scheduled_pickup_time` | Date and Time | Time Zone Independent | Business Required | User Entered | Exact scheduled pickup time is required. Approval-reset behavior for time-only changes remains governed by the open decision register. |
| Actual Pickup Date and Time | `eris_actual_pickup_datetime` | Date and Time | User Local | Optional until pickup; required by pickup action | User Confirmed | Single approved actual-pickup timestamp. Must not be populated before pickup confirmation. |
| Logistics Responsibility | `eris_logistics_responsibility` | Choice | Simple | Business Required | User Entered | Approved values: ERIS; Distributor. No other value established. |
| Current Order Status | `eris_current_order_status` | Choice | Simple | Business Required | System Controlled | Uses the approved lifecycle values. Detailed transition enforcement remains governed by the state-transition specification and open decisions. |
| System Pallet Estimate | `eris_system_pallet_estimate` | Decimal Number | Calculated/Formula pending implementation test | Business Required | Calculated | Read-only estimate calculated from order lines. Precision: 2. Pallet formula remains based on approved packaging rules. |
| Final Pallet Count | `eris_final_pallet_count` | Whole Number | Simple | Optional | User Confirmed | Minimum 0. Separate from system estimate. |
| Order Notes | `eris_order_notes` | Multiple Lines of Text | Plain Text | Optional | User Entered | One shared order-level notes field only; may be blank, edited, or cleared; changes audited. |
| Created By | Microsoft `createdby` | Lookup | System | SystemRequired | System Generated | Native Dataverse system column. |
| Created On | Microsoft `createdon` | Date and Time | User Local | SystemRequired | System Generated | Native Dataverse system column. |

### Distributor Order column controls

- All custom operational columns are searchable where Dataverse supports searching.
- Internal IDs, PO references, distributor, location, dates, status, and pickup values are sortable and available to views and dashboards.
- AI Form Fill is disabled for identifiers, lookups, status, dates, pickup values, pallet values, and notes unless separately approved.
- Column security is not enabled at this stage; table/role security will control access until the security matrix establishes a need.
- Auditing is enabled for all listed custom columns.
- A canceled order cannot be reopened. A later revival requires a new linked Distributor Order.
- A copied order receives a new Internal Order ID and does not inherit document numbers, approvals, communications, adjustments, payments, documents, pickup status, or historical dates.

---

# 4. Order Product Line table

## 4.1 Table specification

| Property | Physical specification |
|---|---|
| Display Name | Order Product Line |
| Plural Display Name | Order Product Lines |
| Description | One approved distributor product and its order-specific quantity, identity, and price snapshots. |
| Schema Name | `eris_OrderProductLine` |
| Logical Name | `eris_orderproductline` |
| Entity Set Name | `eris_orderproductlines` |
| Table Type | Standard custom table |
| Record Ownership | Organization-owned |
| Primary ID | `eris_orderproductlineid` |
| Primary Name Column | Line Name — `eris_line_name` |
| Attachments | No |
| Activities | No |
| Connections | No |
| Email | No |
| Access Teams | No |
| Feedback | No |
| Dataverse Search | Yes |
| Offline Availability | No — not approved |
| Queue Availability | No |
| SharePoint Document Management | No |
| Duplicate Detection | Yes |
| Track Changes | Yes |
| Auditing | Yes |
| Long-Term Retention | Not yet approved |
| Quick Create | No |
| Main Form | Order Product Line |
| Primary Views | Active Order Lines; Lines by Order; Lines by Product |
| Alternate Keys | Order + Product, subject to active-line duplicate enforcement design |
| Status Strategy | Microsoft Active/Inactive state; line deletion should be restricted after document evidence exists |
| Managed Properties | Customization restricted in managed deployment; exact locks to be set before export |

## 4.2 Order Product Line columns

| Display Name | Full Schema Name / Logical Name | Dataverse Type | Behavior | Requirement | Source | Key configuration and approved validation |
|---|---|---|---|---|---|---|
| Line Name | `eris_line_name` | Single Line of Text, max 200 | Simple | Business Required | System Generated | Technical primary-name value derived from order identity and line sequence; not a new business field; read-only in the app. |
| Distributor Order | `eris_distributor_order` | Lookup to Distributor Order | Simple | Business Required | User/System | Every line belongs to exactly one order. Delete behavior must preserve historical evidence; cascade deletion not approved. |
| Line Sequence | `eris_line_sequence` | Whole Number | Simple | Business Required | System/User Controlled | Minimum 1; maximum 18 for document output; controls display and printing order. |
| Product | `eris_product` | Lookup to Product | Simple | Business Required | User Selected | Must reference an approved active Product for new lines. Historical lines retain inactive products. |
| Distributor Product Listing | `eris_distributor_product_listing` | Lookup to Distributor Product Listing | Simple | Business Required | User Selected from controlled listing | Must belong to the order’s Distributor and reference the same Product selected on the line. |
| Quantity | `eris_quantity` | Whole Number | Simple | Business Required | User Entered / Confirmed | Minimum 1; whole units only. |
| Quantity Source | `eris_quantity_source` | Choice | Simple | Business Required | System/User | Stores the approved source of the current quantity, including reviewed intake or confirmed BOL. Final allowed-value register must mirror the approved source-state specification. |
| Distributor Item Number Snapshot | `eris_distributor_item_number_snapshot` | Single Line of Text, max 100 | Simple | Business Required | Snapshot | Copied from Distributor Product Listing when selected; later listing changes do not overwrite it. |
| Distributor Description Snapshot | `eris_distributor_description_snapshot` | Single Line of Text, max 500 | Simple | Business Required | Snapshot | Copied from Distributor Product Listing when selected; later listing changes do not overwrite it. |
| Unit Price Snapshot | `eris_unit_price_snapshot` | Currency | Simple | Business Required | Snapshot | Precision 2; minimum $0.00; transaction-currency behavior follows the order currency. Later price changes do not overwrite it. |
| Price Source | `eris_price_source` | Lookup/controlled reference — exact target pending existing price-override physical design | Simple | Business Required | System | Identifies the effective-dated price or approved override that supplied the snapshot. No free text. |
| Extended Amount | `eris_extended_amount` | Currency | Formula or Calculated Currency pending implementation test | Business Required | Calculated | Quantity × Unit Price Snapshot; precision 2; read-only. |

### Order Product Line column controls

- Order-line notes are prohibited; no notes column is created.
- Identical products cannot appear on duplicate active lines within the same order.
- When the same product is selected twice, the Canvas App must require quantity combination or cancellation of the duplicate selection.
- Distributor item number, description, and unit price remain snapshots.
- Later Product, Distributor Product Listing, or Effective-Dated Price changes must not update existing snapshots.
- Finalized BOL products and quantities become the current source of truth without erasing prior PO or document-version evidence.
- Deposits, handles, and tin tackers contribute zero to the pallet estimate.
- CAN, 1/2 BBL, and 1/4 BBL quantities contribute under the approved pallet calculation.
- No order may produce more than 18 document-output lines.
- Auditing is enabled for every custom column in this table.
- AI Form Fill is disabled for all columns unless separately approved.

---

# 5. Dependency decision: next physical table

The next table should be **Distributor Product Listing**.

## Basis

1. Order Product Line has a Business Required lookup to Distributor Product Listing.
2. The listing supplies the distributor-specific item number and description that are copied into Order Product Line snapshots.
3. The listing also forms the parent dependency for Effective-Dated Price.
4. Completing Distributor Product Listing next allows the Order Product Line lookup, duplicate rule, snapshot source, and price-chain relationship to be physically finalized without redesigning Product, Distributor Order, or Order Product Line.

## Required next-table scope

The Distributor Product Listing physical design should capture only the already-approved fields:

- Distributor
- Product
- Distributor Item Number
- Distributor Description

It must also document the approved uniqueness rule preventing duplicate Distributor + Product combinations.

---

# 6. Items deliberately not resolved in this conversion

These are not field redesigns and remain outside this document until their controlling decisions are approved:

- Exact numerical values for global Choice options and option-value prefix.
- Final lifecycle transition matrix for Current Order Status.
- Exact time-only pickup-change approval-reset behavior.
- Exact server-side sequential numbering implementation for Internal SKU and Internal Order ID.
- Exact formula-versus-calculated implementation for currency and pallet calculations, pending Dataverse implementation testing.
- Final security-role and ownership matrix.
- Final relationship cascade settings beyond the approved requirement to preserve historical and audit evidence.
- Long-term retention configuration.
- Final managed-property locks.
