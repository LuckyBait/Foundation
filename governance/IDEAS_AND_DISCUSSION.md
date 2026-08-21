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


### 2026-08-21 — Двунаправленность канона: зрелые проекты должны мочь обогащать Foundation, а не только принимать его

**Идея:** Сейчас Foundation работает в одном направлении: канон → проект
(`PROJECT_BOOTSTRAP.md` описывает только подключение нового проекта к существующему
канону). Нет механизма для обратного направления: если уже существующий,
зрелый проект (например, Dispatching) выработал практику лучше, чем то, что
предписывает текущий Foundation, это никак не возвращается в канон. Суть
Foundation — сохранять и передавать контекст между любыми проектами независимо от
их зрелости — если зрелый проект выработал более правильное решение самого
механизма, канон должен это заметить и вобрать.

**Discussion outcome:** Принято как направление для дальнейшего обсуждения. Не формализовано как
Governance-правило — чтобы не создавать новый слой процесса до того, как механизм
проверен на практике.

**Boundary:** Абсорбция не должна требовать отдельного Governance Review для каждого
подключаемого проекта — это создаст тот же перекос в бюрократию, который уже
отмечен как проблема проекта. Найденная практика становится кандидатом в Governance
Backlog с пометкой «источник: практика проекта X» — по тому же принципу, что и GS-004
(«governance рождается из практики»), только источником практики может быть любой
подключённый проект, а не только сессия работы над самим Foundation.

**Related record:** `governance/PILOT_PLAN.md` — первая практическая проверка этого
направления на проекте Dispatching.

**Next step:** При проведении пилота по Dispatching оценить не только трение маршрута,
но и есть ли в практиках проекта решения, которые стоит вернуть в канон.
