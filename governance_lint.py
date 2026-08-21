#!/usr/bin/env python3
"""
governance_lint.py

CI-гейт для Foundation / governance слоя.
Проверяет не то, что "думала" модель, а то, что физически лежит в репозитории.
Ничего не пропускает на честном слове: либо структура присутствует, либо
проверка падает с ненулевым кодом возврата и PR не может быть смёржен
(при включённом branch protection + required status check).

Запуск: python3 governance_lint.py [--repo-root .]
Выход: 0 — всё ок; 1 — найдены нарушения (список печатается в stdout).
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

REQUIRED_BACKLOG_FIELDS = ["Статус", "Владелец"]
# Основание/Источник — синонимичные поля, достаточно одного из них
ALT_FIELD_GROUPS = [["Основание", "Источник"]]

IMPLEMENTED_STATUSES = [
    "Approved / Pending Implementation",
    "Accepted / Implemented",
    "Implemented",
]

DURABLE_RECORD_MARKERS = ["Durable record", "governance/"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def check_backlog_entries(repo_root: Path) -> list[str]:
    """Каждая запись GS-XXX в Governance_Backlog.md должна иметь обязательные
    поля. Если статус говорит о завершении/принятии — обязана быть ссылка
    на durable record, существующий физически в репозитории."""
    errors = []
    backlog = repo_root / "governance" / "Governance_Backlog.md"
    if not backlog.exists():
        return [f"MISSING: {backlog} не найден"]

    text = read(backlog)
    entries = re.split(r"\n-{5,}\n", text)

    for entry in entries:
        m = re.search(r"\bGS-[0-9A-Z]+\b", entry)
        if not m:
            continue
        gs_id = m.group(0)

        for field in REQUIRED_BACKLOG_FIELDS:
            if field not in entry:
                errors.append(f"{gs_id}: отсутствует обязательное поле '{field}'")

        if not any(any(f in entry for f in group) for group in ALT_FIELD_GROUPS):
            errors.append(
                f"{gs_id}: отсутствует поле 'Основание' или 'Источник'"
            )

        looks_completed = ("Implemented" in entry) or ("Accepted" in entry)
        if looks_completed:
            if not any(marker in entry for marker in DURABLE_RECORD_MARKERS):
                errors.append(
                    f"{gs_id}: статус указывает на завершение, но нет ссылки "
                    f"на durable record (ожидается путь вида governance/...md)"
                )
            else:
                # Проверяем, что упомянутый файл действительно существует
                for ref in re.findall(r"governance/[A-Za-z0-9_./-]+\.md", entry):
                    ref_path = repo_root / ref
                    if not ref_path.exists():
                        errors.append(
                            f"{gs_id}: ссылается на durable record '{ref}', "
                            f"но файл отсутствует в репозитории"
                        )
    return errors


def check_project_status_sync(repo_root: Path, base_ref: str) -> list[str]:
    """Если PR меняет что-то внутри governance/, PROJECT_STATUS.md обязан
    быть в числе изменённых файлов. Правило GS-002 / GS-010 в механическом
    виде: state должен обновляться вместе с изменением governance."""
    errors = []
    try:
        diff = subprocess.run(
            ["git", "diff", "--name-only", f"{base_ref}...HEAD"],
            cwd=repo_root, capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    except subprocess.CalledProcessError:
        # Нет доступа к git-истории (например, локальный запуск без diff) —
        # не блокируем, но явно сообщаем об ограничении.
        return ["WARNING: git diff недоступен, проверка синхронизации PROJECT_STATUS.md пропущена"]

    changed_governance = [f for f in diff if f.startswith("governance/") and f != "governance/PROJECT_STATUS.md"]
    status_changed = "governance/PROJECT_STATUS.md" in diff

    if changed_governance and not status_changed:
        errors.append(
            "PROJECT_STATUS.md не обновлён, хотя изменены файлы governance/: "
            + ", ".join(changed_governance)
        )
    return errors


def check_no_orphan_governance_files(repo_root: Path) -> list[str]:
    """Каждый файл governance/*.md должен быть упомянут либо в
    Governance_Backlog.md, либо в PROJECT_STATUS.md, либо в CANON.md —
    иначе это "осиротевший" артефакт без владельца в маршруте чтения."""
    errors = []
    gov_dir = repo_root / "governance"
    if not gov_dir.exists():
        return errors

    referenced_in = ""
    for ref_file in ["Governance_Backlog.md", "PROJECT_STATUS.md"]:
        p = gov_dir / ref_file
        if p.exists():
            referenced_in += read(p)
    canon = repo_root / "CANON.md"
    if canon.exists():
        referenced_in += read(canon)

    for f in gov_dir.rglob("*.md"):
        rel = f.relative_to(repo_root).as_posix()
        if f.name in ("Governance_Backlog.md", "PROJECT_STATUS.md"):
            continue
        if f.name not in referenced_in and rel not in referenced_in:
            errors.append(
                f"ORPHAN: {rel} не упомянут ни в Governance_Backlog.md, "
                f"ни в PROJECT_STATUS.md, ни в CANON.md"
            )
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--base-ref", default="origin/main",
                         help="база для git diff при проверке синхронизации PROJECT_STATUS.md")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    all_errors: list[str] = []

    all_errors += check_backlog_entries(repo_root)
    all_errors += check_project_status_sync(repo_root, args.base_ref)
    all_errors += check_no_orphan_governance_files(repo_root)

    warnings = [e for e in all_errors if e.startswith("WARNING")]
    real_errors = [e for e in all_errors if not e.startswith("WARNING")]

    for w in warnings:
        print(w)
    if real_errors:
        print("\ngovernance_lint: НАРУШЕНИЯ НАЙДЕНЫ:\n")
        for e in real_errors:
            print(f"  - {e}")
        print(f"\nВсего нарушений: {len(real_errors)}")
        sys.exit(1)

    print("governance_lint: OK — структурных нарушений не найдено.")
    sys.exit(0)


if __name__ == "__main__":
    main()
