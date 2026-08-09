# Process Check

## Status

Post-v1.0 operational execution rule.

## Purpose

Process Check is an execution-time control. It is intended to constrain the **next action of the executor before generating an architectural answer**, rather than reviewing an already-generated answer after the fact.

It does not replace Foundation, Governance, Project State, or Release Review. It controls how the executor moves between them.

## Mandatory rule

Before every project-related architectural response, the executor must perform the following short check using only the current repository state available from `main`:

1. What is the current stage?
2. What is the goal of that stage?
3. Does the proposed response belong to that goal?
4. If not, classify it as:
   - Governance Backlog / idea or discussion;
   - a later stage;
   - reject / out of scope.
5. Only then generate the response.

## Boundary rule

If a proposed action falls outside the current stage, the executor must not continue developing it as if it belonged to the current task.

Instead:

- record or route the idea to `governance/IDEAS_AND_DISCUSSION.md` when it is still forming;
- promote it to `governance/Governance_Backlog.md` when it is a sufficiently mature Governance proposal;
- identify the later stage when the matter belongs there;
- reject it when it is out of scope.

Then return to the current stage.

## Repository-only context rule

Process Check must use repository artifacts as its authoritative context. The executor must not use chat memory, an assumed previous state, or an obsolete local copy as a substitute for missing repository evidence.

The minimum recovery route is:

`CANON.md → Foundation Core → PROJECT_STATUS.md → Process Check → Governance Backlog → Ideas/Discussion → latest Release Review / Decision Records`

If a required repository source is unavailable, the executor must report the limitation and must not silently reconstruct the missing state from memory.

## Source-of-truth boundary

Process Check is an operational rule. It does not itself create Foundation principles or approve Governance decisions.

The rule may route work into Governance, but Governance decisions still require the normal review and decision process.

## Practical example

If the current stage is `ER-2` and its goal is terminology audit, a proposal to design a new architectural entity registry is outside the current goal. Process Check therefore routes the proposal to the appropriate Governance/Ideas record and returns execution to `ER-2`.

## Origin

This rule was developed and tested during Release Review v1.0. The review demonstrated that constraining the **next step before generation** is more effective than relying only on post-generation validation.

The initial rule was intentionally kept as a working execution practice. After the repository/context preservation work, it is now recorded here so that the execution rule survives changes of model, session, tool, or executor.

## Verification status

The rule is now recorded in the repository. It must be exercised against the repository-only context before the next integrity audit is considered valid.
