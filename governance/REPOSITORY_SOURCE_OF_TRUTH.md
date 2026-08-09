# Repository Source of Truth

## Status

Post-v1.0 Governance rule / operational record.

## Purpose

Preserve project state outside the memory of any single AI session, model, tool, or executor.

## Source of truth

The GitHub repository `LuckyBait/Foundation` is the canonical external storage location for the project's current documented state.

`main` is the canonical current branch. A commit on `main` is the versioned state of the repository at that point in time.

Foundation v1.0 Official Release is the historical baseline. It must not be silently rewritten by post-v1.0 Governance changes.

## Context recovery protocol

When an executor starts or resumes work, the executor should recover context from the repository in this order:

1. `CANON.md`
2. Foundation Core documents referenced by `CANON.md`
3. current Project State, when present
4. `governance/Governance_Backlog.md`
5. latest Release Review and decision records
6. only then continue with new work

The exact files and order may evolve through Governance decisions; the current `CANON.md` remains authoritative for the active reading route.

## Conversation history

Conversation history is auxiliary context, not the source of truth.

A conversation may be archived for historical reconstruction, but a significant decision, observation, status change, or architectural fact is not considered durable project state until it is represented by the appropriate repository artifact.

The repository therefore preserves **state**, while conversation archives preserve **history**.

## Access failure rule

If an executor cannot access the current repository state, it must explicitly report that limitation and must not silently substitute memory, an obsolete local copy, or an assumed project state.

## Change discipline

Changes to this rule are post-v1.0 Governance changes. They must be recorded, reviewed, and verified through the project's existing Governance process before becoming canonical.

**Principle:** the project should preserve the state of the work, not merely the history of the conversation.
