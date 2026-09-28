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


### 2026-08-28 — Итог первого пилота по PILOT_PLAN.md: узкое место — не governance-маршрут, а отсутствие механизма подключения проекта

**Наблюдение:** Проведён пилот по governance/PILOT_PLAN.md на реальном
фрагменте знания из проекта Dispatching (решение: разработка визуальной
части АРМ диспетчера не зависит от наличия таблицы регистров Modbus и
может вестись параллельно с ожиданием данных). Само содержательное
оформление документа заняло один прямой шаг и было тривиальным. Основное
трение возникло раньше содержания — в том, что Dispatching не подключён
к Foundation через governance/PROJECT_BOOTSTRAP.md, и формального
маршрута CANON.md → Foundation Core → PROJECT_STATUS.md → Process Check
→ Governance Backlog для него не существует. Соотношение «время на
процедуру : время на содержание» оказалось резко смещено в сторону
процедуры, но не из-за governance-документов канона как таковых, а
из-за отсутствия механизма подключения существующих проектов.

**Discussion outcome:** Пилот подтверждает направление, зафиксированное
в записи от 2026-08-21 (двунаправленность канона), с уточнением: прежде
чем говорить об абсорбции практики зрелого проекта в канон, требуется
базовый механизм подключения существующего проекта к Foundation —
сейчас его нет даже в одностороннем виде.

**Related record:** governance/PILOT_PLAN.md; запись от 2026-08-21
(двунаправленность канона).

**Next step:** Оценить, стоит ли применить governance/PROJECT_BOOTSTRAP.md
к Dispatching как отдельный шаг, прежде чем продолжать работу над
двунаправленностью канона — вопрос остаётся открытым, решение не
принято.


### 2026-09-28 — Уточнение: PROJECT_BOOTSTRAP.md появился в этом репозитории только сейчас

**Уточнение:** Записи от 2026-08-21 и 2026-08-28 упоминают
governance/PROJECT_BOOTSTRAP.md как существующий файл. На момент этих
записей в данном репозитории такого файла не было (шаблон с таким
названием существовал в другом, отдельном репозитории). Записи не
переписываются как исторический журнал; фактическое состояние
исправлено этой записью.

**Discussion outcome:** Принято подключить Dispatching в минимальном
виде: создан governance/PROJECT_BOOTSTRAP.md (v0) и файл FOUNDATION.md
в репозитории Dispatching. Process Check и ревью в Dispatching не
вводятся.

**Related record:** governance/PROJECT_BOOTSTRAP.md;
governance/PILOT_PLAN.md; записи от 2026-08-21 и 2026-08-28.

**Next step:** На следующем фрагменте знания из Dispatching проверить,
что подключение не требует выяснений и занимает один шаг.


### 2026-09-28 — Изменения, введённые вне маршрута Foundation: что откачено, что пробное

**Наблюдение:** В ходе работы над подключением проекта Dispatching ряд
изменений внесён вне установленного маршрута (Idea → Discussion →
Observation → Governance item → Review → Decision → Implementation →
Verification) и без Process Check.

**Откачено (git revert):**
- CANON.md (коммит 8f3bd3f): формулировки Определений и Законов,
  написанные владельцем, были переписаны другими словами; в раздел
  «Обязательные инструкции» добавлен пункт 8, хотя запись от 2026-08-21
  прямо фиксирует идею как нерешённую, а не как правило. Восстановлен
  текст владельца.
- README.md (коммит f90aa9c): расхождение README и состояния
  governance/ — открытый конфликт (Issue #5, приоритет второй после
  GS-00A). Разрешается через Governance Review, а не правкой вне
  маршрута.

**Остаётся со статусом «пробное, введено вне маршрута, не является
правилом Foundation»:** governance_lint.py;
.github/workflows/governance-check.yml; governance/HARNESS_DESIGN.md;
governance/PILOT_PLAN.md; governance/PROJECT_BOOTSTRAP.md (v0);
FOUNDATION.md и строка в README проекта Dispatching (привязаны к
коммиту ca70115). Принятие или отклонение решается по результатам
слепого теста (governance/reports/Memory_Problem_and_Path_to_Repository_External_Memory.md,
раздел 9) и через ревью GS-00B (практика downstream-проектов).

**Наблюдение по владельцу:** аксиома 2 требует единственного владельца
у каждой архитектурной идеи. Поле «Владелец» есть только у GS-001…004
(значение «Governance System»); у девяти записей (GS-005, GS-00X,
GS-00Y, GS-00Z, GS-00A, GS-00B, GS-00C, GS-00D, GS-00E) его нет.
Фиксируется как наблюдение; Backlog не изменяется, так как во время
аудита архитектура заморожена. Проверка governance_lint.py, опирающаяся
на это поле, пробная и результата не определяет.

**Related record:** governance/PROJECT_STATUS.md (запись о
разрешении); governance/Process_Check_Issue_5_Record.md;
EXECUTION_ANALYSIS_PROCESS_CHECK_CONTINUITY.md; записи от 2026-08-21,
2026-08-28 и 2026-09-28 (уточнение).

**Next step:** Провести слепой тест независимого исполнителя (без
истории, только адрес репозитория) на Foundation и на Dispatching;
результат записать как evidence независимо от исхода. Решение по
пробным изменениям принимается после теста.


### 2026-09-28 — Результат слепого теста независимого исполнителя (Foundation и Dispatching)

**Условия:** два запуска ИИ-исполнителя без истории разговоров, каждому
дан только адрес репозитория. Промпты содержали названия процедуры
(READ_COMPLETE, Process Check), то есть подсказывали её. Модель и режим
запуска не зафиксированы, независимость исполнителя не подтверждена.
Полные отчёты хранятся у владельца вне репозитория и здесь не
приводятся, чтобы не создавать новых файлов в governance/.

**Foundation (HEAD 9557a3e):** прочитано 31 из 31 файлов, READ_COMPLETE.
Хеши блобов сверены независимо с копией репозитория: совпали, кроме
трёх файлов, изменённых откатом (CANON.md, README.md,
IDEAS_AND_DISCUSSION.md); CANON.md и README.md совпали побайтно с
версиями от 14 августа. Этап определён верно (активное ревью GS-00B,
свежий Process Check выполнен, следующее действие — содержательное
ревью), пробные механизмы за правила не приняты. Ограничение: хеши
подтверждают доступ к дереву, но не чтение каждого файла; содержание
подтверждено только по PROJECT_STATUS.md.

**Dispatching (HEAD 527d6b4):** прочитано 8 из 8 файлов, READ_COMPLETE.
FOUNDATION.md найден, принятая часть применена, Process Check проекту не
навязан, блокер и следующий шаг названы верно. Найдено расхождение:
README и CHANGELOG утверждают наличие каталога source-docs/ с PDF, в
дереве каталога нет (решение по содержимому — за владельцем проекта).

**Наблюдения (гипотезы по одному тесту, не выводы):**
1. Закрепление FOUNDATION.md на ca70115 работает как задумано
   (исполнитель читает ровно указанную версию), но скрывает расхождение
   с main: ca70115 содержит откатанную формулировку CANON.md. Это
   конкретный случай открытого вопроса v0 — как проект узнаёт об
   изменении канона.
2. Исполнитель Foundation опирался на PROJECT_STATUS.md; свежие события
   (откат, пробный статус, запись в журнале) в его выводы не попали.
   Возможен разрыв между PROJECT_STATUS.md и журналом идей.
3. Промпт подсказывал процедуру: тест подтверждает выполнение названной
   процедуры, а не самостоятельный поиск маршрута.

**Не проверено:** независимость исполнителя; работа без подсказки
процедуры; чтение содержимого всех файлов, кроме PROJECT_STATUS.md.

**Related record:** governance/reports/Memory_Problem_and_Path_to_Repository_External_Memory.md
(раздел 9); запись от 2026-09-28 о внемаршрутных изменениях.

**Next step:** Повторить тест без подсказки процедуры и на другой
модели. Решение по пробным изменениям принять после повторного теста
и через ревью GS-00B. Перепривязка FOUNDATION.md в Dispatching к
9557a3e выполняется отдельным пробным шагом.
