# Documentation Register

**Solution:** ERIS Distributor Cider Order-to-Payment Solution  
**Repository baseline:** 0.1  
**Last updated:** July 25, 2026 - 7:35 AM CT  

Documents are listed in dependency order. Continuous control documents remain active throughout the project.

| Dependency Order | ID | Document | Status | Requires | Markdown |
|---:|---|---|---|---|---|
| 1 | DOC-001 | Executive Workflow Overview | Needs Refinement | None | [DOC-001-executive-workflow-overview.md](docs/documentation/DOC-001-executive-workflow-overview.md) |
| 2 | DOC-002 | Business Requirements Specification | Needs Refinement | DOC-001 | [DOC-002-business-requirements-specification.md](docs/documentation/DOC-002-business-requirements-specification.md) |
| 3 | DOC-003 | Functional Requirements Specification | Draft | DOC-002, DOC-021 | [DOC-003-functional-requirements-specification.md](docs/documentation/DOC-003-functional-requirements-specification.md) |
| 4 | DOC-004 | Operating Workflow Manual | Draft | DOC-002, DOC-003 | [DOC-004-operating-workflow-manual.md](docs/documentation/DOC-004-operating-workflow-manual.md) |
| 5 | DOC-005 | Solution Architecture | Draft | DOC-002 | [DOC-005-solution-architecture.md](docs/documentation/DOC-005-solution-architecture.md) |
| 6 | DOC-006 | Dataverse Logical Data Model | Draft | DOC-002, DOC-005, DOC-021 | [DOC-006-dataverse-logical-data-model.md](docs/documentation/DOC-006-dataverse-logical-data-model.md) |
| 7 | DOC-007 | Physical Dataverse Design | Task to Complete | DOC-006, DOC-013 | [DOC-007-physical-dataverse-design.md](docs/documentation/DOC-007-physical-dataverse-design.md) |
| 8 | DOC-008 | SharePoint Architecture | Task to Complete | DOC-005, DOC-002, DOC-013 | [DOC-008-sharepoint-architecture.md](docs/documentation/DOC-008-sharepoint-architecture.md) |
| 9 | DOC-009 | Canvas App Functional Specification | Task to Complete | DOC-003, DOC-006, DOC-007, DOC-013 | [DOC-009-canvas-app-functional-specification.md](docs/documentation/DOC-009-canvas-app-functional-specification.md) |
| 10 | DOC-010 | Power Automate Design Specification | Task to Complete | DOC-003, DOC-005, DOC-006, DOC-007, DOC-008, DOC-009, DOC-013 | [DOC-010-power-automate-design-specification.md](docs/documentation/DOC-010-power-automate-design-specification.md) |
| 11 | DOC-011 | Email and Communication Specification | Draft | DOC-002, DOC-003, DOC-013, DOC-021 | [DOC-011-email-and-communication-specification.md](docs/documentation/DOC-011-email-and-communication-specification.md) |
| 12 | DOC-012 | Document Generation Specification | Draft | DOC-002, DOC-006, DOC-008, DOC-021 | [DOC-012-document-generation-specification.md](docs/documentation/DOC-012-document-generation-specification.md) |
| 13 | DOC-013 | Security and Permissions Specification | Task to Complete | DOC-002, DOC-005, DOC-006, DOC-021 | [DOC-013-security-and-permissions-specification.md](docs/documentation/DOC-013-security-and-permissions-specification.md) |
| 14 | DOC-014 | Exception Handling and Recovery Guide | Task to Complete | DOC-003, DOC-009, DOC-010, DOC-013 | [DOC-014-exception-handling-and-recovery-guide.md](docs/documentation/DOC-014-exception-handling-and-recovery-guide.md) |
| 15 | DOC-015 | Audit and Logging Specification | Task to Complete | DOC-006, DOC-007, DOC-008, DOC-010, DOC-013 | [DOC-015-audit-and-logging-specification.md](docs/documentation/DOC-015-audit-and-logging-specification.md) |
| 16 | DOC-016 | Deployment and Operations Guide | Task to Complete | DOC-005, DOC-007, DOC-008, DOC-009, DOC-010, DOC-013, DOC-014, DOC-015 | [DOC-016-deployment-and-operations-guide.md](docs/documentation/DOC-016-deployment-and-operations-guide.md) |
| 17 | DOC-017 | Administrator Guide | Task to Complete | DOC-007, DOC-008, DOC-009, DOC-010, DOC-013, DOC-014, DOC-015, DOC-016 | [DOC-017-administrator-guide.md](docs/documentation/DOC-017-administrator-guide.md) |
| 18 | DOC-018 | User Guide | Task to Complete | DOC-004, DOC-009, DOC-011, DOC-012, DOC-014, DOC-017 | [DOC-018-user-guide.md](docs/documentation/DOC-018-user-guide.md) |
| 19 | DOC-019 | Test Plan | Task to Complete | DOC-003, DOC-007, DOC-008, DOC-009, DOC-010, DOC-011, DOC-012, DOC-013, DOC-014, DOC-015 | [DOC-019-test-plan.md](docs/documentation/DOC-019-test-plan.md) |
| 20 | DOC-020 | Acceptance Test Scripts | Task to Complete | DOC-019, DOC-003, DOC-009, DOC-010, DOC-011, DOC-012, DOC-013, DOC-014 | [DOC-020-acceptance-test-scripts.md](docs/documentation/DOC-020-acceptance-test-scripts.md) |
| Continuous | DOC-021 | Decision Register | Draft | DOC-002 | [DOC-021-decision-register.md](docs/documentation/DOC-021-decision-register.md) |
| Continuous | DOC-022 | Repository Revision History | Draft | All documents | [DOC-022-repository-revision-history.md](docs/documentation/DOC-022-repository-revision-history.md) |

## NotSure Review Findings

- The earlier one-page overview conflicts with the controlling blueprint on BOL approval and invoice timing; DOC-001 is therefore marked Needs Refinement.
- The Version 0.1 blueprint is sufficient to begin development, but it is not Finalized because it contains explicit deferred decisions and lacks stable requirement IDs.
- Technical documents that depend on unfinished design are created as controlled placeholders rather than populated with guessed implementation details.
- No percentage-complete figures are used because the repository does not yet contain a measurable completion formula.
- Finalized status is reserved for documents with no known unresolved item inside their stated scope.

## Immediate Dependency-Order Work

1. Refine DOC-001 against DOC-002.
2. Add requirement IDs and resolve structural gaps in DOC-002.
3. Build DOC-003 and DOC-004 from the approved requirements.
4. Import and reconcile the active Dataverse logical-model work into DOC-006.
5. Complete architecture and security decisions before physical, app, and flow specifications.

Last updated: July 25, 2026 - 7:35 AM CT