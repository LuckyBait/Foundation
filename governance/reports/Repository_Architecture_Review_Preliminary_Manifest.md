# Repository Architecture Review — Preliminary Manifest

Status: Preliminary / evidence record
Date: 2026-08-07
Source: Foundation.zip and its embedded Git repository
Embedded HEAD: c0a4518acbbf3c2585c88aed723d6730a36de (working archive reports c0a4518ac5caaba868f3c258aed723d6730a36de; verify exact SHA before release)

## Purpose

Record the observed repository/filesystem structure before any consolidation or Foundation amendment.

## Observed tracked structure

### Root

- CANON.md
- README.md
- КОНСТИТУЦИЯ_СИСТЕМЫ_ЗНАНИЙ.md
- MANIFEST.md
- UNIVERSAL_COLLABORATION_METHODOLOGY.md
- DOCUMENTATION_LIFECYCLE.md
- governance/

### governance/

- CANON.md
- README.md
- КОНСТИТУЦИЯ_СИСТЕМЫ_ЗНАНИЙ.md
- MANIFEST.md
- UNIVERSAL_COLLABORATION_METHODOLOGY.md
- DOCUMENTATION_LIFECYCLE.md
- REVIEW_REPORT_STANDARD.md
- reports/GS-00X_Knowledge_Runtime_Review_Report.md
- reports/ (Release Review report is not present at this level in the embedded HEAD)
- governance/

### governance/governance/

- README.md
- Governance_Backlog.md
- PROJECT_STATUS.md
- REVIEW_REPORT_STANDARD.md
- VERSIONING.md
- reports/GS-00X_Knowledge_Runtime_Review_Report.md
- reports/Release_Review_v1_0_Repeat_Audit_Review_Report.md

## Structural observations

1. The repository contains a duplicated Foundation document set under `governance/`.
2. The repository contains a nested `governance/governance/` subsystem.
3. Several files are byte-identical across root and governance layers (DOCUMENTATION_LIFECYCLE.md, MANIFEST.md, UNIVERSAL_COLLABORATION_METHODOLOGY.md, REVIEW_REPORT_STANDARD.md, and GS-00X review report). Identity must be treated as evidence, not as a decision to delete.
4. README.md, CANON.md, and governance README files are not byte-identical; their roles must be resolved before consolidation.
5. The embedded Git repository is internally consistent in the archive: `HEAD` and `origin/main` point to the same commit. The repository tree therefore represents an actual committed state, not merely an uncommitted working directory.
6. The archive also contains `.git` internals. These are source-control metadata and are not project content to be copied into the repository as ordinary files.

## Audit consequence

This preliminary manifest does not declare which copy is canonical and does not authorize deletion or relocation. The next task is to establish the intended filesystem model and ownership of each layer, then compare that model with the actual GitHub `main` tree.

## No Foundation amendment

No Foundation v1.0 amendment is approved by this record. Consolidation decisions remain pending Repository Architecture Review.
