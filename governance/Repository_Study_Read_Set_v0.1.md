# Repository Study Read Set v0.1

## Purpose

This record captures a concrete execution defect discovered during repository study: the executor stated that the project repository had been studied completely while the actual read set was incomplete.

## Evidence

Repository: `LuckyBait/Foundation`
Branch: `main`

During the study, the executor read the canonical Foundation chain and then stated that the project structure had been studied. `governance/Governance_Backlog.md` had not yet been read at that point and was only opened later.

Therefore the statement that the repository context had been fully studied was not supported by the actual read set.

## Defect

**Repository Study Completion Error**

An executor must not declare a repository study complete merely because the canonical recovery route has been read. A recovery route and a full repository study are different operations.

## Required control

A repository study must produce a verifiable Read Set containing, at minimum:

- repository;
- branch or commit/ref;
- expected corpus or declared study scope;
- every file in that scope;
- file/blob SHA where available;
- read status for every file;
- failed or unread files;
- final completion status.

The executor may state `READ_COMPLETE` only when every file in the declared scope has a successful read status and no required file remains unread or failed.

## Context assessment rule

After a complete read set, material conclusions should be recorded with their repository source references. A content hash identifies the exact source state; it does not replace the substantive context record.

## Current status

**Observed / requires Governance consideration.**

This record does not modify Foundation v1.0. It records an execution defect discovered while operating the post-v1.0 system and is evidence for evaluating a future repository-study control.
