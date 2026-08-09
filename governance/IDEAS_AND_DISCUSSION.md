# Ideas and Discussion

## Status

Post-v1.0 Governance working record.

## Purpose

Preserve the project's idea and discussion stage in the repository so that developing thoughts do not depend on the memory of a single AI session, model, tool, or chat.

This file is a **working record**, not a canonical specification.

## Lifecycle

Ideas may move through the following stages:

`Idea → Discussion → Observation → Governance item → Review → Decision → Implementation → Verification`

An item may also be rejected, deferred, superseded, or archived. Those outcomes should remain visible when they are relevant to understanding the project's evolution.

## Source-of-truth boundary

- This record is authoritative for the fact that an idea or discussion was recorded and for its recorded discussion state.
- It does **not** make an idea a Foundation rule.
- It does **not** make an idea an approved Governance decision.
- Canonical rules and current project state must remain in their designated repository artifacts.

## Recording rule

A significant idea, observation, concern, alternative, or proposed change discovered during project work should be recorded here or in the appropriate Governance artifact rather than relying solely on conversation history.

When an idea becomes sufficiently mature, it should be promoted to the appropriate Governance item or decision record. The original discussion record should remain available as history.

## Relationship to conversation history

Conversation history may provide additional context, but it is not required to reconstruct the recorded project discussion. The repository preserves the durable discussion state; chat remains an auxiliary interface and historical context.

## Current entries

### 2026-08-07 — Repository as external project memory

**Idea:** Use the GitHub repository as persistent external memory for project state and for the development stage of ideas, so continuity does not depend on AI memory or a particular chat session.

**Discussion outcome:** Accepted as a direction for implementation.

**Boundary:** The repository should preserve both evolving discussion and canonical state, while clearly separating their authority. Ideas and discussions must not silently become Foundation or approved Governance rules.

**Related record:** `governance/REPOSITORY_SOURCE_OF_TRUTH.md`

**Next step:** Establish the repository structure and Process Check route so an executor can recover both current state and relevant unresolved discussion from `main`.
