# Dataverse Design Standard

## ERIS Distributor Workflow

| Document Control | Value |
| --- | --- |
| Document ID | STD-001 |
| Version | 1.0 |
| Status | Project Standard |
| Last Updated | July 25, 2026 |
| Project | ERIS Distributor Workflow |
| Applies To | Dataverse solutions, tables, columns, relationships, choices, and related components |

## Purpose

This document defines the required Microsoft Dataverse configuration standards for every solution component created for the ERIS Distributor Workflow. No Dataverse component should be physically created until its configuration has been documented according to this standard.

## 1. Solution Configuration Standard

The following properties shall be approved before creating any Dataverse tables.

| Property | Required |
| --- | --- |
| Solution Display Name | Yes |
| Solution Unique Name | Yes |
| Publisher Display Name | Yes |
| Publisher Unique Name | Yes |
| Publisher Prefix | Yes |
| Option Value Prefix | Yes |
| Development Environment | Yes |
| Base Language | Yes |
| Base Currency | Yes |
| Environment Auditing | Yes |
| Audit Retention Policy | Yes |
| Deployment Strategy (Managed / Unmanaged) | Yes |

### Current Project Decision

**Approved Publisher Prefix:** `eris`

This prefix shall be used for all custom Dataverse components.

Examples: `eris_Product`, `eris_DistributorOrder`, `eris_OrderProductLine`, `eris_unit_price`

## 2. Table Design Standard

Every Dataverse table specification shall include the following properties.

### Identity

- Display Name
- Plural Display Name
- Description
- Schema Name
- Logical Name
- Entity Set Name

### Table Characteristics

- Table Type
- Record Ownership
- Primary ID
- Primary Name Column

### Features

- Attachments
- Activities
- Connections
- Email
- Access Teams
- Feedback
- Dataverse Search
- Offline Availability
- Queue Availability
- SharePoint Document Management

### Data Management

- Duplicate Detection
- Track Changes
- Auditing
- Long-Term Retention

### User Experience

- Quick Create
- Forms
- Views
- Commands

### Validation

- Alternate Keys
- Business Rules
- Status Strategy

### Governance

- Managed Properties

## 3. Column Design Standard

Every column specification shall include the following.

### Column Identity

- Display Name
- Schema Name Portion
- Full Schema Name
- Logical Name
- Description

### Data Definition

- Dataverse Data Type
- Format
- Behavior
- Requirement Level

### Data Source

- User Entered
- System Generated
- Snapshot
- Calculated

### Limits

- Default Value
- Maximum Length
- Minimum Value
- Maximum Value
- Precision

### Date Configuration

- User Local
- Date Only
- Time Zone Independent

### Choice Configuration

- Global or Local Choice
- Allowed Values
- Default Value

### Calculation

- Formula or Calculated Expression

### Application Configuration

- Searchable
- Sortable
- Dashboard Availability
- AI Form Fill
- App Visibility
- App Editability

### Security

- Column Security
- Auditing

### Business Validation

- Business Validation Rules
- Alternate Key Participation

### Column Governance

- Managed Properties

## 4. Requirement-Level Standard

Dataverse custom columns shall use only supported requirement levels.

| Requirement | Usage |
| --- | --- |
| Optional | Allowed |
| Business Recommended | Allowed |
| Business Required | Allowed |

SystemRequired applies only to Microsoft system columns.

Critical business rules shall additionally specify:

- Canvas App Validation
- Power Automate Validation
- Server-side Validation
- Business Rule Enforcement

## 5. Date and Time Standard

Every Date/Time column must explicitly document its behavior.

| Behavior | Purpose |
| --- | --- |
| User Local | Time-zone conversion |
| Date Only | Calendar dates |
| Time Zone Independent | Fixed timestamps |

No Date/Time column shall accept the Dataverse default without review.

## 6. Currency Standard

Currency columns shall document:

- Precision
- Minimum Value
- Maximum Value
- Currency Precision Method
- Transaction Currency Behavior

Formula versus Calculated Currency columns shall be selected only after implementation testing confirms the desired behavior.

## 7. Auditing Standard

Auditing decisions shall be documented separately for:

- Environment
- Table
- Column

Audit logging shall be enabled intentionally for operational, financial, and compliance data.

## 8. Physical Creation Rule

No Dataverse table shall be physically created until all required configuration defined by this standard has been approved.

## 9. Project Decisions

| Item | Status |
| --- | --- |
| Publisher Prefix | Approved |
| Prefix Value | `eris` |
| Relationships | Deferred until table approval |
| Table Creation | After logical model approval |
| Schema Names | Immutable after creation |
