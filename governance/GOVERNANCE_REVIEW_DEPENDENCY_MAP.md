# Governance Review Dependency Map

## Статус

**Status:** Active Evidence Map  
**Purpose:** зафиксировать только подтверждённые зависимости между существующими Governance items и не допускать субъективного выбора следующего Governance Review.

Foundation v1.0 не изменяется.

## 1. Правило использования

Эта карта не является самостоятельной priority-моделью и не создаёт новых зависимостей.

В неё заносятся только зависимости, которые уже подтверждены существующими Governance records, backlog entries или завершёнными решениями.

Если зависимость не подтверждена evidence, она должна иметь статус `UNCONFIRMED` и не может использоваться как основание для блокировки или выбора следующего Review.

## 2. Confirmed dependencies

| Governance item | Dependency | Evidence basis | Status |
|---|---|---|---|
| GS-00X | завершение Release Review v1.0 | Governance Backlog: GS-00X explicitly deferred until after Release Review | CONFIRMED |
| GS-005 | завершение Release Review | Governance Backlog: GS-005 explicitly deferred until after Release Review | CONFIRMED |
| GS-00C | Repository Architecture Review closure | Repository Architecture Review Final Record; GS-00C records the closure criterion and durable final record | SATISFIED |
| GS-00D | наличие dependency evidence перед определением следующего Review | Governance Review GS-00D Final Record | SATISFIED |

## 3. Current state

Следующие Governance items уже имеют подтверждённую зависимость от завершённого Release Review:

- GS-00X
- GS-005

GS-00C завершён.

GS-00D завершён и установил необходимость использовать dependency evidence вместо субъективного выбора.

GS-00A и GS-00B требуют отдельного Governance Review, однако текущая карта не устанавливает между ними порядок, поскольку достаточного evidence для такого порядка пока нет.

## 4. Dependency graph

```text
Release Review v1.0
├──> GS-00X (deferred until Release Review completion)
└──> GS-005 (deferred until Release Review completion)

Repository Architecture Review
└──> GS-00C
      └──> closure criterion + durable final record

GS-00D
└──> dependency evidence
      └──> Governance Review Dependency Map

GS-00A ──> Governance Review (order not yet established)
GS-00B ──> Governance Review (order not yet established)
```

## 5. What this map does NOT establish

Эта карта не утверждает:

- что GS-00A должен рассматриваться раньше GS-00B;
- что GS-00X должен рассматриваться раньше других observations;
- что наличие меньшего идентификатора означает более высокий приоритет;
- что порядок появления в чате определяет порядок Review;
- что исполнитель может самостоятельно выбрать наиболее короткий маршрут.

## 6. Next determination

Следующий Process Check должен использовать эту карту и определить, достаточно ли текущего evidence для выбора следующего допустимого Governance Review.

Если зависимости между несколькими кандидатами остаются неразрешёнными, нельзя превращать предположение в dependency.

В таком случае отсутствие необходимого evidence регистрируется как отдельное Governance observation.

## 7. Source of truth

Primary source:

`governance/GOVERNANCE_REVIEW_DEPENDENCY_MAP.md`

Supporting sources:

- `governance/Governance_Backlog.md`
- `governance/Governance_Review_GS-00D_Final_Record.md`
- `governance/Repository_Architecture_Review_Final_Record.md`
- `governance/PROCESS_CHECK.md`

**End of Record.**
