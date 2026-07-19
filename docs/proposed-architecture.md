# Proposed Architecture

## Scope and status

This document records the approved architecture direction in §6 and the logical build baseline in §7 of `docs/production-spec-v0.1.md`. It does not select unresolved configuration values or add business rules.

## Confirmed component responsibilities

| Component | Confirmed responsibility | Specification reference |
| --- | --- | --- |
| SharePoint workflow home | Navigation, document-library access, Canvas-app links, and operational landing content. | §6; TR-008 |
| Canvas Power App | Intake, order detail/editing, actions, approvals, blockers, payment confirmation, and closeout. | §6; TR-008 |
| Dataverse | Structured system of record for orders, lines, statuses, contacts, products, prices, approvals, communications, payments, and history. | §6–§7; TR-008–TR-009 |
| SharePoint document library | PDFs, source/supporting files, final packets, metadata, and version history. | §6; §15; TR-008, TR-017 |
| Power Automate | Document creation, approvals, email preparation/sending, reminders, matching, status changes, payment notices, and packet generation. | §6; §19; TR-008, TR-021 |
| Outlook | Source/confirmation/remittance intake; outbound delivery from individual user mailbox; Sent Items retention. | §6; §15; TR-008, TR-017 |
| Controlled Word-to-PDF templates | Stable one-page PO, BOL, and invoice layouts with the stated fonts, branding, fields, and 18-line limit. | §6; §11; TR-008, TR-013 |

Power Pages is excluded from the current design (§6).

## Logical information flow

```text
Reviewed entry source
        │
        ▼
Canvas Power App ───────────────► Dataverse system of record ───► Order Event History
        │                                  │
        │                                  ├──► Power Automate: documents, approvals, messages, reminders
        │                                  │                 │
        ▼                                  │                 ├──► Outlook (inbound/outbound, Sent Items)
Controlled user actions                    │                 └──► SharePoint document library (versions/metadata)
        │                                  │
        └──────────────────────────────────┴──► Payment confirmation → final packet → user close action
```

The diagram is a component-boundary view, not a flow design or a substitute for the DCO-01 through DCO-14 inventory in §19.

## Logical records required

The implementation must support the §7 record set: Distributor, Distributor Location, Distributor Contact, Contact Role Assignment, Product, Distributor Product Listing, Effective-Dated Price, Order, Order Line, PO/BOL/Invoice, Invoice Adjustment, Approval/Submission Cycle, Email Communication, Confirmation Issue, Pickup Event, Credit Memo, Payment Notice/Settlement, Supporting Document, Order Event History, and Final Packet.

## Explicitly unresolved architecture/configuration items

- SharePoint site, library, folder, metadata configuration, and send-category implementation (§20; OD-15, OD-18).
- Power Platform environment, Dataverse solution, and required auditing configuration (§20; OD-19).
- Primary/backup connector owners, error recipients, business/technical owners, and support escalation (§20, §22; OD-17).
- Exact email filters/matching expressions, retry/timeout settings, duplicate-send controls, and edit-lock behavior (§20, §25; OD-04, OD-13, OD-22).
- Controlled template/logo assets and final visual/packet refinements (§11, §25; OD-16, OD-20).

## Architectural guardrails

- The app and flows must preserve the human gates and automatic-action prohibitions in §4–§5.
- Dataverse holds structured workflow records; SharePoint retains document files and version history.
- Exact document/email versions must remain traceable through approval and send history (§15–§16).
- No component configuration is production-ready until the §23 readiness checklist and all applicable open decisions are completed.
