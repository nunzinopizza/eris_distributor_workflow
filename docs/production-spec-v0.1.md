
# Distributor Cider Order-to-Payment Workflow

## Production Solution Documentation - Version 0.1

**Organization:** ERIS Brewery & Cider House
**Document status:** Build baseline - sufficient to begin solution construction; deferred items remain explicitly identified
**Prepared:** July 19, 2026 - 11:28 AM CT
**Source boundary:** Approved collaborative design decisions through July 19, 2026. Unresolved details are marked TBD or Build-Stage Decision; no unresolved item is presented as a completed fact.

---

## Layer 1 - One-Page Workflow Overview

| Field | Approved working definition |
| --- | --- |
| Workflow name | Distributor Cider Order-to-Payment Workflow |
| Purpose | Provide one controlled process for distributor orders from intake through PO, BOL, invoice, approval, email, pickup, payment, and closeout. |
| Triggers | Distributor PO or order email; ERIS-created Lakeshore suggested PO; Production-created BOL; copy/revise a prior order. |
| Desired result | The order is documented, approved where required, sent with the correct document versions, picked up, invoiced, settled, closed, and preserved in a final packet with a complete audit trail. |
| Business owner | To be assigned in the Access and Ownership tab. Design lead/user representative: Nunzino Pizza, Chief Strategy Officer. |
| Systems involved | Current process: Outlook and Excel/workbooks. Target solution: SharePoint, Canvas Power App, Dataverse, Power Automate, Outlook, and controlled Word-to-PDF templates. |
| Frequency | On demand and event-driven for orders, documents, approvals, email, pickup, and payment; scheduled daily reminders where defined. |
| In scope | Lakeshore Beverage Company, Grant Importing, and Skeff Distributing; Lakeshore Halsted and Arlington locations; PO, BOL, invoice, communications, approvals, confirmation, payment, and closeout. |
| Completion standard | Closed order, confirmed settlement, final PDF packet, linked source emails and attachments, retained document versions, and complete order event history. |

### One-sentence outcome

A distributor order is converted into controlled PO, BOL, invoice, communication, approval, pickup, payment, and closeout records, with the correct document versions sent and a complete audit trail retained.

*Section status: approved build baseline. July 19, 2026 - 11:28 AM CT*

---

## Layer 2 - Operating and Technical Documentation

### 1. Documentation model

This production package intentionally separates business actions from Power Automate mechanics. The operating sections explain what the business process must do. The technical register records how the solution will be implemented and clearly labels details that are still unresolved.

The package includes the three views required to preserve the current process while defining the automation:

- Current manual/workbook process
- Target automated process
- Exceptions that still require a person

*Section status: approved documentation structure. July 19, 2026 - 11:28 AM CT*

---

## 2. Current process, automated process, and human exceptions

| Phase | Current manual/workbook process | Target automated process | Human exception or review |
| --- | --- | --- | --- |
| Order intake | User reads an email or PO and enters information in a workbook. | The app captures or extracts the source information, presents it for review, and creates the order only after confirmation. | Ambiguous source documents, missing data, and unsupported attachments require review. |
| Order identification | Users rely on workbook references and filenames. | The system assigns a permanent Internal Order ID and controlled date/location-based document references. | No human override of the permanent Internal Order ID. |
| Product and pricing | Users select or type distributor items and prices in the workbook. | Distributor-specific products and effective-dated prices load from master data and are snapshotted on each order line. | New products, price overrides, and adjustments require authorized users and approvals where defined. |
| Suggested PO | The workbook creates a PO and the user drafts an email. | The system generates the suggested PO, email package, subject, summary block, recipients, and approval request. | The user/approver reviews the exact PDF, recipients, subject, body, and attachments. |
| Distributor response | Users monitor email manually and interpret replies. | Strong matches are linked to the order; reminders and escalation are automated. | Ambiguous matches and any confirmation differences require human resolution. |
| BOL | Production or another user creates and prints a BOL from the workbook. | The app creates the BOL, manages versions, and requires Confirm Printed after successful physical printing. | A revised BOL must be reprinted and reconfirmed. |
| Final PO and BOL send | Users manually revise the PO, attach both files, and send. | Finalizing the BOL updates final quantities, regenerates the PO, checks approval and print blockers, and prepares the combined email. | Final PO changes require approval; the BOL may still be printed while approval is pending. |
| Pickup | Pickup details are updated manually. | The workflow tracks Scheduled, Ready for Pickup, Picked Up, and Pickup Issue, preserving scheduled and actual values. | Differences between scheduled and actual pickup are reviewed and logged. |
| Invoice | The workbook creates the invoice and the user drafts a separate email. | The system uses confirmed BOL quantities and approved final PO prices, creates the PDF and email package, and sends immediately upon approval. | Invoice adjustments, price changes, recipients, body, and attachments require review in the combined approval package. |
| Payment | Users read remittance emails and update records manually. | A matched remittance creates a Payment Notice and extracts settlement details. | A user must confirm payment; mismatches remain Review Required. |
| Closeout | Users assemble and file documents manually. | The system prepares the final packet and moves the order to Ready for Closeout. | A user must review and press Close Order. |

*Section status: build baseline. July 19, 2026 - 11:28 AM CT*

## 3. Step-by-step operating workflow

| Step | Action | System / person | Input | Output | If something goes wrong |
| --- | --- | --- | --- | --- | --- |
| 1 | Receive or initiate order | Outlook / Power App / User | Distributor email, PO, BOL request, or prior order | Workflow entry selected | Do not create an order until the source and entry path are identified. |
| 2 | Review source and required fields | User | Distributor, PO number, Ship To, products, quantities, dates, contacts, attachments | Complete or saved intake draft | Missing or ambiguous information remains a draft and requires review. |
| 3 | Create order | Power App / Dataverse | Reviewed intake | Permanent Internal Order ID and initial status | The Internal Order ID cannot be changed or reused. |
| 4 | Load distributor master data | Power App / Dataverse | Distributor and location | Bill To, Ship To, contacts, logo, item descriptions, prices | Missing or inactive contacts must be replaced with another stored contact or a newly authorized record. |
| 5 | Add order lines | User / Power App | Approved distributor products and whole-unit quantities | Order line snapshots | No free-form products. Duplicate products must be combined or canceled. |
| 6 | Calculate pallet estimate | Power App | CAN, 1/2 BBL, and 1/4 BBL quantities | System pallet estimate | Non-pallet items contribute zero. User may record a final pallet count separately. |
| 7 | Generate or register PO | Power Automate / User | Order data or distributor-provided PO | Suggested PO PDF or filed source PO | Uploaded source filename is preserved as metadata; the active file uses the ERIS naming convention. |
| 8 | Prepare suggested PO package | Power Automate | PO PDF, recipient roles, email template, pickup/logistics summary | Approval-ready package | Only stored recipients and permitted PDFs may be included. |
| 9 | Review suggested PO approval | Approver | Exact PO version, recipients, subject, body, attachments | Approve, Reject, or Return for Changes | Reject and Return require comments. Reassignment is allowed to an eligible approver. |
| 10 | Send suggested PO | Power Automate / User | Approved package | Sent suggested PO email | Whether approval itself sends immediately or enables a separate send remains a build-stage decision. |
| 11 | Monitor distributor response | Outlook / Power Automate | Incoming email | Linked communication or match-review item | Strong matches link automatically; ambiguous matches are never guessed. |
| 12 | Apply follow-up schedule | Power Automate | Unanswered suggested PO | Reminder or human-intervention escalation | First reminder next business day, then daily; third unanswered follow-up stops automation and escalates. |
| 13 | Resolve confirmation | User | Distributor response and any differences | Confirmed order or Confirmation Issue / Review Required | Differences do not overwrite the order automatically. |
| 14 | Create or update BOL | Production / Power App | Distributor, Ship To, pickup date/time, products, quantities, shipping details | BOL PDF | The system checks for an existing order before creating a duplicate. |
| 15 | Print BOL | User | Current BOL version | Physical BOL | Printing alone does not update status. |
| 16 | Confirm BOL printed | User | Successful physical print | Confirmed Printed status with user, time, and version | Number of copies is not tracked. |
| 17 | Revise BOL when needed | User / Power Automate | Changed shipping information | Revised BOL with same number and filename | The BOL displays REVISED and revision number and returns to Reprint Required. |
| 18 | Finalize BOL | User / Power Automate | Confirmed BOL products and quantities | Finalized BOL and final quantities | Confirmed BOL quantities become the source of truth. |
| 19 | Regenerate final PO | Power Automate | Finalized BOL quantities and approved pricing | Updated PO using same number and filename | Prior suggested version remains in SharePoint version history. |
| 20 | Request final PO approval when changed | Power Automate / Approver | Difference between suggested and final PO | Approved final PO or pending blocker | BOL printing remains available, but combined sending is blocked. |
| 21 | Prepare final PO/BOL email | Power Automate | Final PO, supporting BOL, recipient roles, template | Preview/Send package | Subject lists both filenames separated by vertical bars. |
| 22 | Resolve send blockers | User | Final PO Approval Pending, BOL Not Confirmed Printed, missing contacts, document issues | Cleared blockers | Send remains visible but disabled; each blocker has a direct action link. |
| 23 | Send final PO and BOL | User / Power Automate | Cleared package | Email sent; both documents marked Sent | If the send fails, neither document is marked Sent and the package is preserved for retry. |
| 24 | Mark Ready for Pickup | Authorized user | Operational readiness | Ready for Pickup status | Status change is logged. |
| 25 | Mark Picked Up | Authorized user | Scheduled or corrected actual pickup date/time | Picked Up status and invoice generation trigger | Differences between scheduled and actual values are retained. |
| 26 | Generate invoice draft | Power Automate | Confirmed BOL quantities and approved final PO prices | Invoice PDF draft | The invoice does not refresh prices from the current master table. |
| 27 | Add invoice adjustments | Authorized user | Freight, credit memo, deposit adjustment, or Other | Adjustment lines and approval requirement | Other requires a description. All adjustments require approval. |
| 28 | Prepare invoice package | Power Automate | Invoice PDF, recipients, subject, complete email body, permitted attachments | Combined approval request | The approval screen must show the complete package. |
| 29 | Approve and send invoice | Approver / Power Automate | Exact invoice package | Immediate invoice email send and Sent status | The screen warns that Approve immediately sends the email. |
| 30 | Match remittance email | Outlook / Power Automate | Incoming remittance or payment notice | Payment Notice with extracted details | Ambiguous matches or discrepancies require review. |
| 31 | Confirm payment | User | Payment amount/date/reference and credit memo use | Confirmed settlement and Ready for Closeout | The system never marks Paid automatically. |
| 32 | Generate final packet | Power Automate | PO, material emails, BOL, invoice, remittance, workflow references | Final PDF packet | The user controls which material emails are included. |
| 33 | Close order | Authorized user | Reviewed final packet and confirmed settlement | Complete / Closed order | Completed orders are normally locked. Reopen permissions are defined separately. |
| 34 | Cancel order when required | Authorized user | Cancellation email or decision | Canceled order | Canceled orders cannot reopen; any revival creates a new linked order. |

*Section status: build baseline. July 19, 2026 - 11:28 AM CT*

## 4. Decision rules in plain if/then language

- If a source email or document is incomplete, then save an intake draft and require human completion before Create Order.
- If the system cannot confidently match an email, PO, BOL, remittance, or order, then place it in review and do not guess.
- If a required contact is missing or inactive, then an authorized user must select another stored contact or create an approved contact record.
- If a recipient is not stored in the contact system, then it cannot be used as an external recipient.
- If the same product is selected twice, then offer to combine quantities or cancel the duplicate selection.
- If a product is not on the approved list, then it cannot be entered as a free-form line.
- If a price changes after it was snapshotted, then use a price override or adjustment and require the defined approval.
- If the pickup date changes, then require approval. A pickup-time-only change is logged; approval-reset behavior is deferred to build.
- If Ship To changes, then update the location code and regenerate affected PO, BOL, and invoice references while preserving the Internal Order ID.
- If a BOL changes after printing, then generate a revised version, mark Reprint Required, and require Confirm Printed again.
- If final BOL products or quantities differ from the approved suggested PO, then require final PO approval before combined sending.
- If final PO approval is pending, then keep the BOL printable but display a Final PO Approval Pending banner in the app.
- If the BOL is not Confirmed Printed, then disable the final PO/BOL Send button.
- If any Preview/Send blocker exists, then keep Send visible but disabled and provide a direct action to resolve the blocker.
- If a combined PO/BOL send succeeds, then mark both documents Sent using the exact attachment versions recorded in the send log.
- If a combined PO/BOL send fails, then mark neither document Sent and preserve the package for retry.
- If the order is marked Picked Up, then automatically generate the invoice draft from confirmed BOL quantities and approved final PO prices.
- If an invoice adjustment is added, then require approval and show it as a separate invoice line.
- If the approver selects Approve on the invoice package, then send the exact package immediately.
- If the approver selects Reject or Return for Changes, then require a comment.
- If an approval is returned or rejected but not closed, then allow revision and resubmission in the same approval log.
- If an approval is reassigned, then limit the new assignee to eligible approvers and log the reassignment; a reason is optional.
- If a distributor does not respond, then send the first follow-up next business day and later follow-ups daily; after the third unanswered follow-up, stop automation and require human intervention.
- If a confirmation contains differences, then create Confirmation Issue / Review Required and do not overwrite the order automatically.
- If a cancellation is recorded, then move the order to Canceled immediately and do not reopen it.
- If a credit memo is applied, then reduce its available balance and prevent use beyond the remaining amount.
- If remittance data do not match the invoice or expected settlement, then create Payment Discrepancy / Review Required.
- If a remittance email matches strongly, then create a Payment Notice but do not mark the invoice Paid until a user presses Confirm Payment.
- If payment is confirmed, then prepare the final packet and move the order to Ready for Closeout; a user must still press Close Order.
- If a PDF category is blocked from sending, then it cannot be attached and the block cannot be overridden.

*Section status: approved rules plus explicitly deferred build behavior. July 19, 2026 - 11:28 AM CT*

## 5. Exceptions and controls

### 5.1 Human review is required for

- Ambiguous email, order, PO, BOL, confirmation, or remittance matches.
- Incomplete order intake and missing required data.
- New distributor contacts and products created by authorized users.
- Suggested PO package approval.
- Final PO changes caused by finalized BOL values.
- Pickup-date changes, price overrides, and invoice adjustments.
- Confirmation differences and distributor exceptions.
- BOL print confirmation and any required reprint confirmation.
- Invoice PDF and email package approval.
- Payment confirmation and settlement discrepancies.
- Final packet review and Close Order.

### 5.2 The system must never do these automatically

- Guess an ambiguous record or email match.
- Use a free-form external recipient.
- Add a free-form product line.
- Overwrite confirmed order data from an email difference without review.
- Mark a BOL Printed without user confirmation.
- Send a final PO/BOL package while a blocker exists.
- Mark an invoice Paid solely because a remittance email was received.
- Close an order without user review.
- Reopen a canceled order.
- Send a blocked document category.
- Allow ordinary users to edit controlled banking information.

### 5.3 Duplicate and version controls

- Permanent sequential Internal Order ID for every created order.
- System-wide daily two-digit document suffix to prevent same-day reference collisions.
- Existing-order matching before a BOL-started order is created.
- No duplicate identical product lines within an order.
- Credit memo available-balance control to prevent double use.
- Single-user edit lock while other users remain read-only.
- Current visible document replaced while older versions remain in SharePoint version history.
- Send-processing and duplicate-click controls are deferred to implementation but must be included before production.

### 5.4 Failure recording and restart rules

- Failures are written to Order Event History and the applicable email, approval, document, or payment record.
- A failed combined PO/BOL send preserves the approved package and returns it for retry without marking either document Sent.
- An incomplete intake remains a saved draft and can be resumed.
- A returned or rejected-but-open approval is revised and resubmitted inside the same approval history.
- Completed orders may be amended only by a role that will be defined in the access matrix; all reopen/amend/reclose actions must be logged.
- Canceled orders cannot be restarted. A new linked order is required.
- Error notification recipients, retry timing, and timeout settings are build-stage decisions and must be documented before production.

*Section status: core controls approved; technical error handling partly deferred. July 19, 2026 - 11:28 AM CT*

## 6. Solution architecture

| Component | Production responsibility |
| --- | --- |
| SharePoint workflow home | Navigation, document-library access, links to the Canvas app, and operational landing content. |
| Canvas Power App | Order intake, order detail, editing, action buttons, approvals, blockers, payment confirmation, and closeout. |
| Dataverse | Preferred structured system of record for orders, lines, statuses, contacts, products, prices, approvals, communications, payments, and history. |
| SharePoint document library | PDFs, source documents, supporting files, final packets, metadata, and version history. |
| Power Automate | Document creation, approvals, email preparation and sending, reminders, matching, status changes, payment notices, and packet generation. |
| Outlook | Inbound source and confirmation/remittance email; outbound delivery from the individual user mailbox; Sent Items retention. |
| Controlled Word-to-PDF templates | Stable one-page portrait PO, BOL, and invoice layouts with fixed fonts, branding, fields, and up to 18 lines. |

Power Pages is not part of the current design. The internal solution is based on a SharePoint home and Canvas Power App.

*Section status: approved architecture direction. July 19, 2026 - 11:28 AM CT*

## 7. Core data model

| Record | Minimum responsibility |
| --- | --- |
| Distributor | Entity name, codes, bill-to information, branding, status. |
| Distributor Location | Ship To, location code, address, location-specific contacts. |
| Distributor Contact | Name, title, email, phone, location scope, active/inactive, last verified, notes. |
| Contact Role Assignment | PO, logistics/BOL, invoice/AP, confirmation, remittance/payment, escalation; To/CC and primary status. |
| Product | Internal SKU, internal name, package format, active/inactive. |
| Distributor Product Listing | Distributor-specific item number and description. |
| Effective-Dated Price | Distributor product price, effective dates, status. |
| Order | Internal Order ID, distributor, location, dates, statuses, logistics responsibility, notes. |
| Order Line | Product, quantity, item/description snapshot, price snapshot, source. |
| PO / BOL / Invoice | Document references, filename, stage, version, current file, links. |
| Invoice Adjustment | Type, description, amount, approval, invoice link. |
| Approval / Submission Cycle | Action, document/email version, requester, approver, decision, comments, reassignment, close status. |
| Email Communication | Direction, mailbox message ID, recipients, subject, body, attachments, match status, material-for-packet flag. |
| Confirmation Issue | Field difference, source value, order value, resolution, resolver. |
| Pickup Event | Scheduled and actual date/time, status, issue details. |
| Credit Memo | Memo number, original amount, available balance, application history, status. |
| Payment Notice / Settlement | Amount, date, reference, credit memo use, discrepancy, confirmation. |
| Supporting Document | PDF category, source filename, active filename, send eligibility, packet inclusion. |
| Order Event History | Immutable log of actions, users, timestamps, values, versions, and statuses. |
| Final Packet | Generated packet file, contents, version, closeout link. |

*Section status: logical build baseline. July 19, 2026 - 11:28 AM CT*

## 8. Identifiers and file naming

| Item | Example | Rule |
| --- | --- | --- |
| Internal Order ID | ORD-000184 | Permanent sequential identifier; printed quietly where later approved and always retained in metadata. |
| Lakeshore PO | LSB_PO_ERIS-H260719-01.pdf | PO date, location code, and system-wide daily suffix. |
| Grant PO | GRT_PO_ERIS-G260719-01.pdf | Same rule using Grant code. |
| Skeff PO | SKF_PO_ERIS-S260719-01.pdf | Same rule using Skeff code. |
| Lakeshore BOL | BOL-LSB-H260719-01.pdf | Pickup-date reference. |
| Grant BOL | BOL-GRT-G260719-01.pdf | Pickup-date reference. |
| Skeff BOL | BOL-SKF-S260719-01.pdf | Pickup-date reference. |
| Lakeshore invoice | ERIS Invoice LSB-H260719-01.pdf | Pickup-date reference; visible invoice number is ERIS-H260719-01. |
| Grant invoice | ERIS Invoice GRT-G260719-01.pdf | Pickup-date reference. |
| Skeff invoice | ERIS Invoice SKF-S260719-01.pdf | Pickup-date reference. |

Location codes are H for Lakeshore Halsted, A for Lakeshore Arlington, G for Grant, and S for Skeff. The two-digit suffix is assigned system-wide by date and does not change if the location changes later. The distributor official PO number is stored and printed but not placed in the ERIS filename. Source filenames are retained as metadata.

*Section status: approved. July 19, 2026 - 11:28 AM CT*

## 9. Master data and calculations

### 9.1 Product formats

- `1/2 BBL`
- `6/4/12 CAN`
- `24/16 CAN`
- `1/4 BBL`
- `KEG DEPOSIT`
- `TAP HANDLE`
- `TAP HANDLE-F`
- `TIN TACKERS`

Each distinct sellable package is a separate product. The normal selector shows distributor-specific item numbers and descriptions. The internal sequential SKU is retained but hidden from ordinary selection. Quantities are whole units. No free-form miscellaneous products or duplicate identical lines are allowed.

### 9.2 Pricing

Prices are distributor-specific and effective-dated. The order line saves a price snapshot. The approved final PO price becomes the invoice price. Later differences require an approved override or separate invoice adjustment.

### 9.3 Pallet estimate

- CAN: 80 cases per pallet
- 1/2 BBL: 8 units per pallet
- 1/4 BBL: 14 units per pallet
- Deposits, handles, and tin tackers: zero pallet contribution
- Combine all pallet-bearing fractions and round upward to a whole pallet
- Preserve both the system estimate and user-confirmed final pallet count

### 9.4 Contact roles

PO, logistics/BOL, invoice/AP, confirmation, remittance/payment, and escalation. One primary contact per role; a contact may hold multiple roles and may be distributor-wide or location-specific. External recipients must be stored contacts.

*Section status: approved. July 19, 2026 - 11:28 AM CT*

## 10. Workflow entry points

1. **Distributor PO or order email:** review source fields and attachments before Create Order assigns the Internal Order ID.
2. **ERIS-created Lakeshore suggested PO:** generate the PO immediately but require package approval before sending.
3. **Production-created BOL:** enter shipping data without pricing, match an existing order when possible, and create/link the PO and draft invoice as required.
4. **Copy or revise a prior order:** selectively reuse distributor, Ship To, products, quantities, notes, and contacts while refreshing current descriptions, prices, addresses, contacts, and pallet estimates. Never copy dates, document numbers, approvals, emails, adjustments, payments, documents, or pickup status.

*Section status: approved. July 19, 2026 - 11:28 AM CT*

## 11. Document output standards

- PO, BOL, and invoice use standard 8.5 x 11 portrait orientation.
- Every document must remain exactly one page with fixed readable fonts and spacing.
- Maximum supported order lines: 18. This workflow is not expected to exceed that limit.
- All three documents use a coordinated header/footer system and prominent document type/reference in the upper-right corner.
- ERIS BOL and invoice use the ERIS logo.
- A PO created on behalf of a distributor uses the distributor logo in the main header and a small ERIS logo in the footer.
- The PO does not state on its face that ERIS prepared it; the email provides that context.
- Current visible files are replaced by new versions while SharePoint version history retains prior PDFs.
- Order Notes are optional, order-level, shared across documents, editable, and automatically versioned without approval.

*Section status: approved. July 19, 2026 - 11:28 AM CT*

## 12. Suggested PO communication

The initial email attaches only the suggested PO and states that it is an ERIS-suggested order subject to distributor approval and inventory availability. It states that the BOL will be attached with the final PO after the BOL is finalized.

The summary block includes pickup date, pickup time, delivery location, Estimated Pallets, and one explicit logistics line: **Logistics by ERIS** or **Logistics arranged by distributor**.

Suggested PO subject: `ERIS Brewery & Cider House | [PO Filename.pdf]`

The suggested PO approval package includes the PO PDF, recipients, subject, full email body, and attachment list. The exact post-approval send behavior remains a build-stage decision.

*Section status: approved except one deferred send-control detail. July 19, 2026 - 11:28 AM CT*

## 13. BOL and final PO communication

The BOL may be generated and printed without approval. After successful printing, the user must press Confirm Printed. A revision keeps the same number and filename, displays REVISED and the revision number, replaces the current file, preserves prior versions, and returns the BOL to Reprint Required.

Finalizing the BOL makes its confirmed products and quantities the source of truth. The system automatically regenerates the PO using the same number and filename. If values differ from the approved suggested PO, final PO approval is required. The BOL may still be printed, but sending is blocked and the app shows Final PO Approval Pending.

Final PO/BOL subject: `ERIS Brewery & Cider House | [PO Filename.pdf] | [BOL Filename.pdf]`

The final PO is the primary attachment and the BOL is a supporting document. BOL Confirmed Printed and final PO approval are required blockers. Successful sending marks both documents Sent. The final PO itself does not display a FINAL label.

*Section status: approved. July 19, 2026 - 11:28 AM CT*

## 14. Pickup, invoice, and invoice email

Pickup statuses are Scheduled, Ready for Pickup, Picked Up, and Pickup Issue. The scheduled date/time becomes the default actual date/time and may be corrected when Picked Up is recorded; differences remain logged.

Marking Picked Up automatically creates the invoice draft. Confirmed BOL quantities and approved final PO prices are used. The invoice displays the distributor official PO number and related BOL number. The invoice is always sent separately from the PO/BOL email.

Invoice-only adjustments are Freight, Credit Memo, Deposit Adjustment, and Other. Other requires a description. Multiple adjustments are allowed and all require approval.

Invoice terms are Net 15 calendar days. Weekend due dates move backward to Friday; a recognized holiday then moves the date forward to the next business day. Late-payment interest is not calculated, tracked, printed, or automatically emailed.

Invoice subject: `ERIS Brewery & Cider House | [Invoice Filename.pdf]`

Every invoice email includes complete ACH instructions from controlled ERIS configuration, Net 15 terms, and a security reminder that ERIS will not change banking instructions by email and will confirm any change by phone. The older Penny/AI disclosure is not part of the default template.

The invoice PDF, recipients, subject, full email body, and attachments are approved in one request. The approval screen warns that Approve immediately sends the exact email package.

*Section status: approved; some post-approval error behavior deferred. July 19, 2026 - 11:28 AM CT*

## 15. Attachment and communication controls

Only PDFs may be uploaded. Every PDF receives one category: Distributor PO; Supporting Order Document; Credit Memo; Remittance / Payment Evidence; Distributor Correspondence; Approval or Exception Support; or Other with a required description.

The system maintains Can Be Sent and Blocked From Sending lists. Blocked categories cannot be overridden. Email pickers show only order-linked, permitted PDFs. The system retains the original template, final subject/body, recipients, attachments, document versions, sender, and send timestamp. Sent messages appear in Outlook Sent Items and the order history.

*Section status: approved; message-specific category refinements deferred. July 19, 2026 - 11:28 AM CT*

## 16. Approval framework

Approvals are action-specific and tied to the exact document, email, or proposed change. Current types include suggested PO package, final PO changes, price override, pickup-date change, invoice adjustment, and combined invoice package.

- Response options: Approve, Reject, Return for Changes
- One approval decision is required
- Reject and Return for Changes require comments
- Approve does not require a comment
- Requester and current approver may reassign to an eligible approver
- Reassignment reason is optional; all reassignment details are logged
- Return for Changes and rejected-but-open requests are revised and resubmitted within the same approval history
- Close Approval permanently ends the request; who may close is an access decision
- Automated reminders are required; timing and escalation remain build-stage decisions

*Section status: approved with access/reminder details deferred. July 19, 2026 - 11:28 AM CT*

## 17. Confirmation, no-response, cancellation, and revision

Incoming confirmations are matched using sender/contact, distributor PO number, ERIS references, Internal Order ID, subject, dates, pickup details, products, and quantities. Strong matches link automatically; ambiguous matches require review. A user may unlink an irrelevant email, and that action is logged.

Any difference creates Confirmation Issue / Review Required and does not overwrite the order. After all issues are resolved, an authorized user presses Mark Confirmed.

No-response schedule: first follow-up next business day, then every calendar day. The third unanswered follow-up moves the order to No Response - Human Intervention Required and stops automated reminders. Human outcomes are Confirmed, Distributor Declined, Pickup Rescheduled, or Cancel Order.

A cancellation email is sufficient evidence. A canceled order cannot be reopened. A declined order may be revised under the same order or copied into a new linked order, as selected by the user.

*Section status: approved. July 19, 2026 - 11:28 AM CT*

## 18. Payment and closeout

A strongly matched remittance email creates a Payment Notice and extracts amount, date, reference, credit memos, and discrepancies. The system never marks Paid automatically. A user must review and press Confirm Payment. Mismatches create Payment Discrepancy / Review Required.

Credit memos are separate records with Available, Partially Used, and Fully Used statuses. The record tracks original amount, invoice use, remaining balance, and prevents double use. One settlement may combine payment and multiple credit memos.

After payment confirmation, the system prepares the final packet and sets Ready for Closeout. The user reviews the packet and presses Close Order.

The final packet includes the PO, user-marked material order correspondence, BOL, invoice, payment/remittance correspondence, and a summary page with Internal Order ID and links/references to approvals and workflow history.

*Section status: approved. July 19, 2026 - 11:28 AM CT*

## 19. Power Automate flow inventory

| Working flow name | Trigger | Business action | Human gate | Current status |
| --- | --- | --- | --- | --- |
| DCO-01 Order Intake | Manual Power App action or reviewed Outlook source | Create intake draft, validate required fields, create Internal Order ID. | User confirms source and required information. | Design complete; build not started. |
| DCO-02 Suggested PO Generation | Order status/action | Create distributor-branded PO PDF and suggested PO email package. | Suggested PO package approval. | Design complete; immediate-send behavior still deferred. |
| DCO-03 Approval Orchestration | Approval request created or resubmitted | Assign approver, present package, record decisions, comments, reassignment, reminders. | Approve / Reject / Return for Changes / Close Approval. | Reminder cadence, escalation, and Close Approval permissions deferred. |
| DCO-04 Inbound Email Matching | New Outlook email | Match and link order, confirmation, PO, or remittance communications. | Ambiguous matches require user review. | Exact filters and expressions deferred. |
| DCO-05 Distributor Follow-Up | Scheduled check of unresolved sent communication | Send next-business-day and daily reminders; escalate after third unanswered follow-up. | Human intervention after escalation. | Design complete; exact schedule implementation pending. |
| DCO-06 BOL Generation and Print Control | BOL action or Production entry point | Match/create order, generate PDF, manage revisions, track Confirm Printed. | User confirms physical print. | Design complete. |
| DCO-07 Final PO Regeneration | BOL finalized | Use BOL quantities, regenerate PO, compare to approved suggested PO. | Approval required when final PO differs. | Design complete. |
| DCO-08 Final PO/BOL Send | All blockers cleared and user presses Send | Send combined package and mark both documents Sent. | User previews and confirms; blockers must be resolved. | Error/duplicate-click controls deferred. |
| DCO-09 Pickup and Invoice Trigger | Mark Picked Up | Record actual pickup and generate invoice draft. | User confirms actual pickup values. | Design complete. |
| DCO-10 Invoice Package Approval and Send | Invoice draft ready | Create complete invoice package; Approve sends immediately. | Approver reviews complete package. | Send-failure behavior deferred. |
| DCO-11 Remittance Processing | New matched remittance email | Create Payment Notice and extract settlement details. | User confirms payment or resolves discrepancy. | Exact extraction rules deferred. |
| DCO-12 Closeout Packet | Payment confirmed | Assemble packet and set Ready for Closeout. | User reviews and presses Close Order. | Design complete; exact packet template pending. |
| DCO-13 Revision and Version Control | Saved revision or material field change | Regenerate affected documents, reset flags, preserve version history. | User reviews changes and consequences before save. | Some approval-reset rules deferred. |
| DCO-14 Cancellation | Authorized Cancel Order action | Record evidence, set Canceled, block reopening. | Authorized user initiates. | Design complete. |

*Section status: production build inventory; names are working names. July 19, 2026 - 11:28 AM CT*

## 20. Technical build register

| Technical item | Current documented value |
| --- | --- |
| Flow names | Working names DCO-01 through DCO-14 in this document; final environment naming may be adjusted during build. |
| Trigger configuration | Manual Power App actions, Outlook new-email events, Dataverse status changes, scheduled reminders, and approval responses. |
| Connection owners | TBD before production. Primary and backup ownership must be documented for Outlook, Dataverse, SharePoint, and template connectors. |
| SharePoint site/library locations | TBD before build. Version history, metadata, order linkage, and permitted PDF categories are required. |
| Power App environment and Dataverse solution | TBD before build. Components should be deployed inside a managed solution for production. |
| Filter expressions | Logical rules are documented; exact Power Automate expressions and mailbox filters remain build items. |
| Core variables | InternalOrderID, DistributorCode, LocationCode, PODate, PickupDate, DailySequence, DocumentVersion, document stages, ApprovalID, SystemPalletEstimate, FinalPalletCount. |
| File naming | Controlled conventions in this document; source filename preserved as metadata. |
| Timeout/retry settings | Deferred to implementation. Must be documented and tested before production. |
| Error notification recipients | TBD in Access and Ownership. Failures must be logged even when notification delivery fails. |
| Last tested date | Not yet built or tested. A test register must be added during implementation. |
| Deployment status | Version 0.1 build baseline; not yet production deployed. |

*Section status: known values and explicit TBDs. July 19, 2026 - 11:28 AM CT*

## 21. Lifecycle metadata

| Record | Controlled working stages |
| --- | --- |
| Order | Draft; Leadership Approval; Sent to Supplier; Supplier Confirmed; Confirmation Issue / Review Required; Scheduled; Ready for Pickup; Picked Up; Pickup Issue; Payment Discrepancy / Review Required; Ready for Closeout; Complete; Canceled; No Response - Human Intervention Required. |
| PO | Suggested; Final Approval Pending; Approved for Sending; Sent; Superseded when applicable. |
| BOL | Generated; Reprint Required; Finalized; Confirmed Printed; Sent as Supporting Document; Superseded. |
| Invoice | Draft; Ready for Review; Approval Pending; Approved for Sending; Sent; Paid / Settled. |
| Credit memo | Available; Partially Used; Fully Used. |
| Approval | Pending; Returned for Changes; Rejected but Open; Approved; Closed. |

These stages are workflow and document-library metadata. They do not need to appear on the generated PDFs unless explicitly approved later.

*Section status: working controlled values. July 19, 2026 - 11:28 AM CT*

## 22. Access and ownership requirements

The access tab must define who may create and edit orders; create products and contacts; change or override pricing; add adjustments; approve each action type; reassign or close approvals; confirm BOL printing; send documents; confirm payments; reopen completed orders; and administer templates, contacts, logos, and banking configuration.

The technical register must also name the business owner, technical owner, Power Platform environment owner, primary and backup connection owners, error-notification recipients, and support escalation path.

*Section status: required, not yet assigned. July 19, 2026 - 11:28 AM CT*

## 23. Production readiness checklist

- [ ] Assign the business owner, technical owner, connection owners, and backup owners.
- [ ] Finalize the role and permission matrix, including Close Approval and completed-order amendment rights.
- [ ] Create the Dataverse solution and tables with auditing enabled where required.
- [ ] Create the SharePoint library, metadata, versioning, and send-category controls.
- [ ] Build and validate all distributor, location, contact, product, price, and logo master data.
- [ ] Build controlled one-page portrait PO, BOL, and invoice templates and test all 18 product lines.
- [ ] Configure Outlook connections and confirm sent messages appear in the user mailbox and order history.
- [ ] Implement approval packages with exact document/email version locking and reassignment logging.
- [ ] Implement BOL Confirm Printed, reprint, and final PO approval blockers.
- [ ] Implement invoice approval warning and immediate-send behavior.
- [ ] Implement email matching, ambiguous-review queues, follow-ups, and human-intervention escalation.
- [ ] Implement Payment Notice extraction, discrepancy handling, Confirm Payment, and credit memo balance controls.
- [ ] Implement final packet generation and Close Order.
- [ ] Define and test retry, timeout, duplicate-send, edit-lock expiration, and failure notification controls.
- [ ] Complete unit, integration, security, document-layout, email-delivery, and user-acceptance testing.
- [ ] Record the last-tested date, test owner, results, defects, and production release approval.

*Section status: required before production release. July 19, 2026 - 11:28 AM CT*

## 24. Acceptance criteria

| Area | Acceptance standard |
| --- | --- |
| Order intake | All four entry points create or link the correct order without duplicate records and preserve source evidence. |
| Documents | PO, BOL, and invoice remain one-page portrait documents with fixed readable formatting and up to 18 lines. |
| Naming/versioning | References and filenames match the controlled rules; prior versions remain recoverable. |
| Approval | Exact document/email versions are reviewed; comments, returns, rejects, approvals, reassignments, and close actions are logged. |
| BOL control | A printed BOL is not considered confirmed until the user presses Confirm Printed; revisions require reprint. |
| Final PO/BOL send | Send is disabled until all blockers clear; successful delivery marks both documents Sent. |
| Invoice | Picked Up creates the draft from BOL quantities and approved final PO prices; invoice approval sends the exact package immediately. |
| Communications | Sent and received communications are linked, searchable, and retained; ambiguous matches are reviewed. |
| Payment | Remittance creates a notice, but only Confirm Payment changes settlement status; discrepancies remain visible. |
| Closeout | The final packet is generated, reviewed, and linked before Close Order. |
| Auditability | Material changes, statuses, users, timestamps, approvals, sends, versions, and payment actions are reconstructable from history. |

*Section status: initial UAT baseline. July 19, 2026 - 11:28 AM CT*

## 25. Deferred build-stage decisions

- Exact approval reminder timing, cadence, and escalation.
- Role and permission matrix, including who may Close Approval.
- Whether pickup-time-only changes reset PO approval.
- Edit-lock timeout and administrative override behavior.
- Whether a copied order opens immediately as an editable Draft.
- Whether approving a suggested PO package immediately sends it or enables a separate send action.
- Detailed revised-email workflow statuses.
- Message-specific allowed/blocked attachment-category rules.
- Whether both pickup date and invoice date appear when they differ.
- Whether the invoice footer displays the Internal Order ID.
- Whether post-approval changes to the invoice PDF or email body automatically reset approval.
- Invoice send-failure behavior and approval validity after failure.
- Duplicate-send, processing-lock, retry, timeout, and detailed error controls.
- Recognized holiday calendar used for invoice due dates.
- Exact SharePoint site, library, folder, environment, and connection-owner configuration.
- Final visual refinements to document templates and final packet summary page.

No deferred item should be silently implemented as a business rule. Each must be resolved, documented, tested, and added to the controlled specification before production release.

*Section status: open decision register. July 19, 2026 - 11:28 AM CT*

## 26. Document control

| Field | Value |
| --- | --- |
| Document | Distributor Cider Order-to-Payment Workflow - Production Solution Documentation |
| Version | 0.1 |
| Status | Build baseline |
| Prepared for | ERIS Brewery & Cider House |
| Prepared | July 19, 2026 - 11:28 AM CT |
| Source | Approved collaborative design decisions through July 19, 2026 |
| Next controlled update | After data model, access matrix, technical locations, error controls, and template prototypes are resolved |

**End of document - July 19, 2026 - 11:28 AM CT**
