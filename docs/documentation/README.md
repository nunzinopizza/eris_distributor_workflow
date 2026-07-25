# ERIS Distributor Documentation Repository

This package bootstraps a controlled documentation repository for the ERIS Distributor Cider Order-to-Payment Solution.

## What is included

- A dependency-ordered document register.
- Twenty-two controlled Markdown documents.
- Matching PDF snapshots.
- Standard status definitions.
- A reusable document template.
- A PowerShell installation script for the existing local Git repository.
- A PDF build script.

## Status discipline

Only these statuses are used:

- Task to Complete
- Draft
- Needs Refinement
- Finalized

No percentage-complete estimates are used.

## Install into the current local repository

From PowerShell, unzip this package and run:

```powershell
.\install-documentation.ps1 -RepositoryPath "C:\Dev\eris_distributor_workflow"
```

The script creates a branch named `docs/documentation-repository`, copies the documentation into the repository, stages it, and creates a local commit. It does not push because the project previously had no valid `origin` remote.

## First review sequence

1. `DOCUMENT_REGISTER.md`
2. `docs/documentation/DOC-001-executive-workflow-overview.md`
3. `docs/documentation/DOC-002-business-requirements-specification.md`
4. `docs/documentation/DOC-021-decision-register.md`
5. `docs/documentation/DOC-006-dataverse-logical-data-model.md`

Generated: July 25, 2026 - 7:35 AM CT
