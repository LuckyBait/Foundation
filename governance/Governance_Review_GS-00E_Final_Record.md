# Governance Review — GS-00E

## GS-00E — Governance Review Candidate Selection / Tie-Break Rule

**Статус решения:** ACCEPTED

## Основание

GS-00D установил обязательность объективной очередности Governance Reviews, но сознательно не определил конкретный алгоритм выбора.

Dependency Map подтвердил несколько допустимых Governance candidates, но не установил порядок между независимыми кандидатами. В частности, между GS-00A и GS-00B отсутствует подтверждённая зависимость, которая позволяла бы выбрать один из них исключительно на основании dependency evidence.

## Решение

Governance Review принимает GS-00E.

Governance System должен иметь детерминированное правило выбора следующего Governance Review, когда после проверки зависимостей остаётся более одного одновременно допустимого кандидата.

При этом правило не должно превращаться в субъективную priority-модель исполнителя.

## Утверждённый selection protocol

Очередность определяется последовательно:

**A → B → C → D → E**

где:

**A — Process admissibility**  
Проверяется текущий Process Check: соответствует ли кандидат текущему этапу, его цели и допустимому действию.

**B — Blocking dependencies**  
Кандидаты с невыполненными подтверждёнными обязательными зависимостями исключаются.

**C — Evidence-backed necessity**  
Если остаётся несколько кандидатов, преимущество получает кандидат, необходимость которого непосредственно подтверждена текущим durable evidence и который закрывает конкретный обнаруженный governance/process gap.

**D — Explicit governance dependency / downstream impact**  
Если после A–C остаётся несколько кандидатов, выбирается кандидат, решение которого создаёт подтверждённую предпосылку для других допустимых Governance items.

**E — Deterministic tie-break**  
Если после A–D кандидаты полностью равноправны, используется детерминированный tie-break по стабильному идентификатору Governance item в лексикографическом порядке. Это технический способ устранения ничьей, а не смысловой приоритет.

## Ограничения

Selection protocol НЕ разрешает:

- выбирать item по субъективному мнению исполнителя;
- выбирать «самый короткий» путь;
- использовать порядок появления идеи в чате как приоритет;
- считать меньший GS-ID содержательно более важным;
- создавать dependency только для того, чтобы искусственно поднять item в очереди;
- обходить Process Check;
- изменять Foundation v1.0.

## Durable selection record

Причина выбора каждого следующего Governance Review должна быть зафиксирована durable repository record с указанием применённых критериев A–E.

Минимальный формат:

```text
Candidate set:
Process stage:
A — admissibility:
B — dependencies:
C — evidence-backed necessity:
D — downstream impact:
E — deterministic tie-break (если применён):
Selected Review:
Reason:
```

## Пример

Если одновременно допустимы GS-00A и GS-00B:

```text
A: оба допустимы
B: у обоих нет невыполненных blocking dependencies
C: если GS-00A имеет непосредственное evidence о дефекте Repository Study,
   а GS-00B является более общей downstream observation,
   выбирается GS-00A
```

Если A–D дают полностью равный результат:

```text
GS-00A
GS-00B
   ↓
A–D равны
   ↓
E
   ↓
GS-00A выбран как детерминированный tie-break
```

Такой выбор не означает, что GS-00A важнее GS-00B.

## Итог

GS-00E закрывает обнаруженный пробел между dependency ordering и фактическим выбором следующего Governance Review.

Dependency Map остаётся evidence map и не превращается в priority-модель.

Foundation v1.0 остаётся неизменяемым baseline.

**End of Record.**
