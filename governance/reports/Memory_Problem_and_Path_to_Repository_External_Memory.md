# Memory Problem and Path to Repository External Memory

**Status:** Evidence / working record

**Purpose:** Preserve the reasoning that led to the decision to treat the repository as the durable external memory of the project rather than relying on an executor's chat context or personal memory.

## 1. Problem observed

During development of Foundation, important architectural ideas, algorithms, deferred decisions, observations, and process rules were repeatedly developed in conversation but were not always recorded in the repository at the moment they appeared.

As the conversational context grew, the executor could lose earlier context, reconstruct it incompletely, or repeat work that had already been done. A new chat could therefore appear to understand the project while lacking important decisions and ideas from earlier work.

The problem is therefore larger than ordinary chat-memory loss:

- conversational context grows quickly;
- important ideas can remain only in conversation;
- a new chat may not contain that history;
- another executor may have its own memory that conflicts with the current repository state;
- an executor can mistakenly infer that it understands the project without having read the complete relevant repository corpus.

## 2. Key conclusion

The executor's memory must not be the project's source of truth.

The durable project context must be recoverable from the repository.

The working model is:

```text
executor memory / chat context
        = temporary working context

repository
        = durable project memory + source of truth
```

Not remembering is acceptable. Failing to recover context from the authoritative source is acceptable only when the source is unavailable and the executor explicitly stops. Pretending to remember, infer, or understand without checking the source is not acceptable.

## 3. Why a hash alone is insufficient

A single hash can prove that bytes or a particular artifact state are identical, but it cannot prove that an executor reached the same semantic understanding of the system.

Therefore a useful continuity mechanism must preserve both:

1. the durable artifacts from which context can be recovered;
2. the evidence and records showing how the executor established that context.

This led to the Repository Study / Read Set approach rather than attempting to encode understanding into a single conversational hash.

## 4. Process that emerged

Before making an architectural or project-level decision, an executor should be able to establish:

```text
Repository identity
        ↓
current branch / HEAD
        ↓
recursive repository tree
        ↓
declared study scope
        ↓
Read Set: every file in scope + blob SHA + read status
        ↓
READ_COMPLETE
        ↓
Process Check
        ↓
context-grounded conclusion / allowed next action
```

If the authoritative source is unavailable, the executor must stop rather than reconstructing the missing repository from memory.

If repository identity is ambiguous, the executor must stop and resolve identity before studying the contents.

## 5. Important distinction: ideas must also become durable context

The system is not only about preserving finalized implementation.

When an idea, observation, algorithm, deferred decision, or potentially important conclusion appears during work, it must receive a durable repository record even if it is intentionally postponed.

Otherwise the same idea may be rediscovered repeatedly in later chats, while the conversational context continues to grow and eventually disappears.

This is why Governance Backlog / Ideas & Discussion and evidence records are important: they preserve useful context before it becomes an implementation commitment.

## 6. Evidence from execution

The following experiments were used to test the principle:

### Repository Study completeness

A concrete defect was discovered where an executor had claimed repository context was studied before the full declared corpus had actually been read. This was recorded in `governance/Repository_Study_Read_Set_v0.1.md` and entered into the Governance Backlog as GS-00A.

The Read Set mechanism was then tested independently in a fresh chat against `LuckyBait/Foundation`. The executor produced a 15-file scope, individual blob SHAs, read statuses, and `READ_COMPLETE` against the current `main` tree.

### Memory versus source of truth

An executor with historical memory of a different Foundation repository correctly raised a repository-identity conflict rather than silently assuming that its remembered repository was the current source. After clarification, it treated the explicitly identified repository as the target.

This demonstrated an important rule: memory may be a signal or warning, but it is not authoritative over the current repository.

### Missing source

In a clean environment where no repository, `.git` tree, or usable external source was available, the executor stopped and requested an accessible source rather than inventing branch, HEAD, or repository contents.

### Process Check behavior

A request to implement deferred `GS-00X Knowledge Runtime` was tested. The repository-grounded executor stopped instead of immediately designing and implementing it, because the current Governance state did not authorize that work and there was also a documented state inconsistency requiring resolution before acting.

## 7. Current interpretation

These tests do **not** yet constitute proof of a fully independent external-executor validation. Some tests used the same ChatGPT executor in a new chat, while another used Claude with its own possible historical context and environment constraints.

Therefore the correct claim is narrower:

> The repository-based continuity mechanisms have been exercised successfully in multiple fresh-chat / constrained-environment scenarios, but a fully blind test with a genuinely independent executor remains a future validation step.

## 8. Architectural implication

Foundation v1.0 remains the stable canonical baseline and is not changed by this record.

The observation concerns the execution and governance layer: the project needs a durable mechanism by which any future executor can reconstruct the relevant context from repository state without depending on the memory of a particular chat, model, or person.

The intended result is not preservation of every word of every conversation. It is preservation of the **useful, decision-relevant, architecture-relevant and process-relevant information required to continue the project correctly**.

## 9. Next validation

The next proposed experiment is a true blind external-executor test:

- no prior project conversation;
- no prior executor memory of the repository;
- no hidden GitHub project context;
- repository URL/source supplied as the only project source;
- executor must establish repository identity;
- executor must produce a complete Read Set;
- only after `READ_COMPLETE` may it perform Process Check and propose the next action.

The result of that test should be recorded as evidence, whether it passes or fails.
