# Repository Source of Truth

## Purpose

This record defines how project state is preserved and transferred between AI sessions, models, tools, and agents.

## Canonical source

The GitHub repository is the canonical external source of project state.

**Foundation v1.0 Official Release** is the baseline/foundation reference. It is preserved as an official repository artifact and must not be silently rewritten as if later Governance changes were part of the original v1.0 release.

The current project state is represented by the current repository artifacts, including the active Governance records and Release Review records.

## Context recovery rule

At the start of work, the executor must prefer current repository artifacts over conversational memory.

Minimum recovery sequence:

1. Read `CANON.md`.
2. Read the Foundation Core in the order defined by `CANON.md`.
3. Read current Project State / status records when present.
4. Read `governance/Governance_Backlog.md` when present.
5. Read the latest applicable Release Review and decision records.
6. Only then continue the task.

## Conversation history

Conversation history is auxiliary context, not the source of truth.

A conversation may explain why a decision was discussed, but a decision is not considered part of durable project state until it is recorded in the appropriate repository artifact.

Full conversation archives may be retained separately when useful, but they must not be required for normal project-state recovery.

## Durable-state rule

Any significant architectural decision, Observation, status change, Process Check rule, or accepted project-state change discovered during a chat must be transferred to the appropriate repository record before the work is considered durably recorded.

## Anti-drift rule

The executor must not infer current project state from remembered conversation details when a repository artifact exists that can establish the current state.

If repository state and remembered context conflict, repository state is the starting source of truth and the discrepancy must be surfaced rather than silently reconciled.

## Scope

This document is a post-v1.0 Governance artifact. It does not retroactively modify the Foundation v1.0 Official Release.
