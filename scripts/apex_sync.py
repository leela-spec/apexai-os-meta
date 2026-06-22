#!/usr/bin/env python3
"""Deterministic read-side synchronization reports for Apex task files.

Canonical path: scripts/apex_sync.py

This script is intentionally standard-library-only. It reads Apex Markdown task
files from apex-meta/epics/*/[0-9][0-9][0-9].md, computes read-side reports,
and writes only apex-meta/registry/index.md when the registry subcommand is
invoked with --dry-run false.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

STATUS_ENUM = {"open", "in-progress", "blocked", "done", "deferred"}
PRIORITY_VALUES = {"high": 3, "medium": 2, "low": 1}
NO_DUE_DATE_URGENCY = 999
TASK_GLOB = "apex-meta/epics/*/[0-9][0-9][0-9].md"
REGISTRY_RELATIVE_PATH = Path("apex-meta/registry/index.md")

REVIEW_MALFORMED_FRONTMATTER = "malformed_frontmatter"
REVIEW_MISSING_TASK_ID = "missing_task_id"
REVIEW_DUPLICATE_TASK_ID = "duplicate_task_id"
REVIEW_UNSUPPORTED_STATUS = "unsupported_status"
REVIEW_MISSING_DEPENDENCY_TARGET = "missing_dependency_target"
REVIEW_CIRCULAR_DEPENDENCY_RISK = "circular_dependency_risk"
REVIEW_BLOCKED_WITHOUT_REASON = "blocked_without_reason"
REVIEW_STALE_TASK_CANDIDATE = "stale_task_candidate"
REVIEW_REGISTRY_OUT_OF_DATE = "registry_out_of_date"
REVIEW_DRIFT_DETECTED = "drift_detected"
REVIEW_SCRIPT_FAILED = "script_failed"

REQUIRED_REVIEW_FLAGS = [
    REVIEW_MALFORMED_FRONTMATTER,
    REVIEW_MISSING_TASK_ID,
    REVIEW_DUPLICATE_TASK_ID,
    REVIEW_UNSUPPORTED_STATUS,
    REVIEW_MISSING_DEPENDENCY_TARGET,
    REVIEW_CIRCULAR_DEPENDENCY_RISK,
    REVIEW_BLOCKED_WITHOUT_REASON,
    REVIEW_STALE_TASK_CANDIDATE,
    REVIEW_REGISTRY_OUT_OF_DATE,
    REVIEW_DRIFT_DETECTED,
    REVIEW_SCRIPT_FAILED,
]


@dataclass(frozen=True)
class TaskRecord:
    id: int
    title: str
    status: str
    priority: str
    due_date: Optional[str]
    depends_on: Tuple[int, ...]
    blocked_by: Tuple[str, ...]
    updated_date: Optional[str]
    created_date: Optional[str]
    epic_slug: str
    task_path: str
    frontmatter: Dict[str, Any]
    body: str


@dataclass(frozen=True)
class TaskLoadResult:
    tasks: List[TaskRecord]
    review_flags: List[Dict[str, Any]]
    discovered_task_files: int


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--root",
        default=".",
        help="Repository root containing apex-meta/epics/. Default: current directory.",
    )
    common.add_argument(
        "--json",
        action="store_true",
        help="Write machine-readable JSON to stdout.",
    )
    common.add_argument(
        "--dry-run",
        nargs="?",
        const="true",
        default="true",
        choices=("true", "false"),
        help="Dry-run mode. Default: true. Use '--dry-run false' only with registry.",
    )

    parser = argparse.ArgumentParser(
        description="Compute Apex synchronization reports from Markdown task files."
    )
    subcommands = parser.add_subparsers(dest="subcommand", required=True)

    subcommands.add_parser("next", parents=[common], help="Compute next actionable tasks.")
    subcommands.add_parser("blockers", parents=[common], help="List blockers and blocked tasks.")
    subcommands.add_parser("registry", parents=[common], help="Rebuild or preview the registry index.")
    subcommands.add_parser("drift", parents=[common], help="Detect registry/source drift.")

    stall_parser = subcommands.add_parser("stall", parents=[common], help="Detect stale task candidates.")
    stall_parser.add_argument(
        "--stale-days",
        type=int,
        default=14,
        help="Days since updated/created timestamp before a non-done task is stale. Default: 14.",
    )
    stall_parser.add_argument(
        "--today",
        default=None,
        help="Override today's date for deterministic tests, formatted YYYY-MM-DD.",
    )

    score_parser = subcommands.add_parser(
        "score",
        parents=[common],
        help="Compute priority, urgency, unlock depth, and focus candidates.",
    )
    score_parser.add_argument(
        "--today",
        default=None,
        help="Override today's date for deterministic tests, formatted YYYY-MM-DD.",
    )

    return parser.parse_args(argv)


def parse_dry_run(value: str) -> bool:
    return value.lower() != "false"


def review_flag(flag_name: str, reason: str, **fields: Any) -> Dict[str, Any]:
    item: Dict[str, Any] = {"flag": flag_name, "reason": reason}
    for key, value in fields.items():
        if value is not None:
            item[key] = value
    return item


def read_task_files(root: Path) -> TaskLoadResult:
    tasks: List[TaskRecord] = []
    review_flags: List[Dict[str, Any]] = []
    task_files = sorted(root.glob(TASK_GLOB))

    for task_file in task_files:
        relative_path = safe_relative(task_file, root)
        try:
            text = task_file.read_text(encoding="utf-8")
        except OSError as exc:
            review_flags.append(
                review_flag(
                    REVIEW_MALFORMED_FRONTMATTER,
                    f"cannot read file: {exc}",
                    task_path=relative_path,
                )
            )
            continue

        frontmatter, body, parse_error = parse_markdown_task(text)
        if parse_error is not None:
            review_flags.append(
                review_flag(REVIEW_MALFORMED_FRONTMATTER, parse_error, task_path=relative_path)
            )
            continue

        record = build_task_record(root, task_file, frontmatter, body, review_flags)
        if record is not None:
            tasks.append(record)

    review_flags.extend(validate_duplicate_ids(tasks))
    review_flags.extend(validate_status_values(tasks))
    review_flags.extend(validate_dependency_targets(tasks))
    review_flags.extend(validate_circular_dependency_risk(tasks))
    review_flags.extend(validate_blocked_reason(tasks))

    return TaskLoadResult(
        tasks=tasks,
        review_flags=review_flags,
        discovered_task_files=len(task_files),
    )


def parse_markdown_task(text: str) -> Tuple[Dict[str, Any], str, Optional[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, "missing opening frontmatter fence"

    end_index: Optional[int] = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break
    if end_index is None:
        return {}, text, "missing closing frontmatter fence"

    frontmatter_lines = lines[1:end_index]
    body = "\n".join(lines[end_index + 1 :]).strip()
    try:
        frontmatter = parse_minimal_yaml(frontmatter_lines)
    except ValueError as exc:
        return {}, body, str(exc)
    return frontmatter, body, None


def parse_minimal_yaml(lines: Iterable[str]) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    current_key: Optional[str] = None

    for line_number, raw_line in enumerate(lines, start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith(" ") and current_key and raw_line.strip().startswith("- "):
            data.setdefault(current_key, [])
            if not isinstance(data[current_key], list):
                raise ValueError(
                    f"frontmatter line {line_number}: mixed scalar/list value for {current_key}"
                )
            data[current_key].append(parse_scalar(raw_line.strip()[2:].strip()))
            continue

        if raw_line.startswith("-") and current_key:
            data.setdefault(current_key, [])
            if not isinstance(data[current_key], list):
                raise ValueError(
                    f"frontmatter line {line_number}: mixed scalar/list value for {current_key}"
                )
            data[current_key].append(parse_scalar(raw_line[1:].strip()))
            continue

        if ":" not in raw_line:
            raise ValueError(f"frontmatter line {line_number}: expected key: value")

        key, value = raw_line.split(":", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"frontmatter line {line_number}: empty key")

        current_key = key
        value = value.strip()
        if value == "":
            data[key] = []
        else:
            data[key] = parse_scalar(value)

    return data


def parse_scalar(value: str) -> Any:
    value = strip_inline_comment(value).strip()
    if not value:
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    lower = value.lower()
    if lower in {"null", "none", "~"}:
        return None
    if lower == "true":
        return True
    if lower == "false":
        return False
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in split_inline_list(inner)]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def strip_inline_comment(value: str) -> str:
    in_single = False
    in_double = False
    for index, char in enumerate(value):
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        elif char == "#" and not in_single and not in_double:
            previous = value[index - 1] if index > 0 else " "
            if previous.isspace():
                return value[:index]
    return value


def split_inline_list(inner: str) -> List[str]:
    parts: List[str] = []
    current: List[str] = []
    in_single = False
    in_double = False
    for char in inner:
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        if char == "," and not in_single and not in_double:
            parts.append("".join(current))
            current = []
        else:
            current.append(char)
    parts.append("".join(current))
    return parts


def build_task_record(
    root: Path,
    task_file: Path,
    frontmatter: Dict[str, Any],
    body: str,
    review_flags: List[Dict[str, Any]],
) -> Optional[TaskRecord]:
    relative_path = safe_relative(task_file, root)
    raw_id = frontmatter.get("id")
    if raw_id in (None, ""):
        review_flags.append(
            review_flag(
                REVIEW_MISSING_TASK_ID,
                "frontmatter field id is missing",
                task_path=relative_path,
            )
        )
        return None

    try:
        task_id = int(raw_id)
    except (TypeError, ValueError):
        review_flags.append(
            review_flag(
                REVIEW_MISSING_TASK_ID,
                "frontmatter field id is not an integer",
                task_path=relative_path,
                raw_id=raw_id,
            )
        )
        return None

    status = str(frontmatter.get("status") or "open").strip()
    priority = str(frontmatter.get("priority") or "medium").lower().strip()
    if priority not in PRIORITY_VALUES:
        priority = "medium"

    due_date = coerce_optional_string(frontmatter.get("due_date"))
    updated_date = first_present_string(frontmatter, ("updated_date", "updated", "updated_at"))
    created_date = first_present_string(frontmatter, ("created_date", "created", "created_at"))

    return TaskRecord(
        id=task_id,
        title=str(frontmatter.get("title") or frontmatter.get("name") or fallback_title(body) or task_file.stem),
        status=status,
        priority=priority,
        due_date=due_date,
        depends_on=tuple(coerce_int_list(frontmatter.get("depends_on"))),
        blocked_by=tuple(coerce_string_list(frontmatter.get("blocked_by"))),
        updated_date=updated_date,
        created_date=created_date,
        epic_slug=task_file.parent.name,
        task_path=relative_path,
        frontmatter=frontmatter,
        body=body,
    )


def coerce_optional_string(value: Any) -> Optional[str]:
    if value in (None, ""):
        return None
    return str(value).strip() or None


def first_present_string(frontmatter: Dict[str, Any], keys: Sequence[str]) -> Optional[str]:
    for key in keys:
        value = coerce_optional_string(frontmatter.get(key))
        if value is not None:
            return value
    return None


def fallback_title(body: str) -> str:
    for line in body.splitlines():
        clean = line.strip()
        if clean.startswith("#"):
            return clean.lstrip("#").strip()
    return ""


def safe_relative(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def coerce_int_list(value: Any) -> List[int]:
    if value in (None, ""):
        return []
    raw_items = value if isinstance(value, list) else [value]
    result: List[int] = []
    for item in raw_items:
        try:
            result.append(int(item))
        except (TypeError, ValueError):
            continue
    return result


def coerce_string_list(value: Any) -> List[str]:
    if value in (None, ""):
        return []
    raw_items = value if isinstance(value, list) else [value]
    return [str(item).strip() for item in raw_items if str(item).strip()]


def validate_duplicate_ids(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    by_id: Dict[int, List[TaskRecord]] = {}
    for task in tasks:
        by_id.setdefault(task.id, []).append(task)

    flags: List[Dict[str, Any]] = []
    for task_id, matches in sorted(by_id.items()):
        if len(matches) <= 1:
            continue
        paths = [task.task_path for task in matches]
        for task in matches:
            flags.append(
                review_flag(
                    REVIEW_DUPLICATE_TASK_ID,
                    "task id appears in multiple task files",
                    id=task_id,
                    task_path=task.task_path,
                    duplicate_paths=paths,
                )
            )
    return flags


def validate_status_values(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    return [
        review_flag(
            REVIEW_UNSUPPORTED_STATUS,
            "status is not one of open, in-progress, blocked, done, deferred",
            id=task.id,
            status=task.status,
            task_path=task.task_path,
        )
        for task in tasks
        if task.status not in STATUS_ENUM
    ]


def validate_dependency_targets(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    ids = {task.id for task in tasks}
    flags: List[Dict[str, Any]] = []
    for task in tasks:
        missing = [dep for dep in task.depends_on if dep not in ids]
        if missing:
            flags.append(
                review_flag(
                    REVIEW_MISSING_DEPENDENCY_TARGET,
                    "depends_on references missing task id(s)",
                    id=task.id,
                    task_path=task.task_path,
                    missing_depends_on=missing,
                    depends_on=list(task.depends_on),
                )
            )
    return flags


def validate_circular_dependency_risk(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    by_id = {task.id: task for task in tasks}
    visiting: Set[int] = set()
    visited: Set[int] = set()
    cycles: List[List[int]] = []

    def visit(task_id: int, stack: List[int]) -> None:
        if task_id in visiting:
            cycle_start = stack.index(task_id) if task_id in stack else 0
            cycles.append(stack[cycle_start:] + [task_id])
            return
        if task_id in visited:
            return
        visiting.add(task_id)
        stack.append(task_id)
        task = by_id.get(task_id)
        if task is not None:
            for dep in task.depends_on:
                if dep in by_id:
                    visit(dep, stack)
        stack.pop()
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in sorted(by_id):
        visit(task_id, [])

    flags: List[Dict[str, Any]] = []
    seen: Set[Tuple[int, ...]] = set()
    for cycle in cycles:
        normalized = tuple(cycle)
        if normalized in seen:
            continue
        seen.add(normalized)
        flags.append(
            review_flag(
                REVIEW_CIRCULAR_DEPENDENCY_RISK,
                "cycle detected in depends_on graph",
                depends_on_cycle=cycle,
            )
        )
    return flags


def validate_blocked_reason(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    return [
        review_flag(
            REVIEW_BLOCKED_WITHOUT_REASON,
            "status is blocked but blocked_by is empty",
            id=task.id,
            task_path=task.task_path,
        )
        for task in tasks
        if task.status == "blocked" and not task.blocked_by
    ]


def flags_matching(review_flags: List[Dict[str, Any]], names: Set[str]) -> List[Dict[str, Any]]:
    return [item for item in review_flags if item.get("flag") in names]


def is_done(task: Optional[TaskRecord]) -> bool:
    return bool(task and task.status == "done")


def blocked_by_is_clear(task: TaskRecord, by_id: Dict[int, TaskRecord]) -> bool:
    if not task.blocked_by:
        return True
    numeric_blockers: List[int] = []
    for blocker in task.blocked_by:
        try:
            numeric_blockers.append(int(blocker))
        except ValueError:
            return False
    return all(is_done(by_id.get(blocker_id)) for blocker_id in numeric_blockers)


def dependency_state(task: TaskRecord, by_id: Dict[int, TaskRecord]) -> Tuple[bool, List[int], List[int]]:
    missing = [dep for dep in task.depends_on if dep not in by_id]
    unsatisfied = [dep for dep in task.depends_on if dep in by_id and by_id[dep].status != "done"]
    return not missing and not unsatisfied, missing, unsatisfied


def priority_score(task: TaskRecord) -> int:
    return PRIORITY_VALUES.get(task.priority, PRIORITY_VALUES["medium"])


def parse_date(value: Optional[str]) -> Optional[date]:
    if value is None:
        return None
    clean = str(value).strip()
    if not clean:
        return None
    try:
        if "T" in clean:
            return datetime.fromisoformat(clean.replace("Z", "+00:00")).date()
        return datetime.strptime(clean[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def parse_today(value: Optional[str]) -> date:
    parsed = parse_date(value)
    if value is not None and parsed is None:
        raise ValueError("--today must be formatted YYYY-MM-DD")
    return parsed or date.today()


def urgency_score(task: TaskRecord, today_value: date) -> int:
    parsed_due_date = parse_date(task.due_date)
    if parsed_due_date is None:
        return NO_DUE_DATE_URGENCY
    return (parsed_due_date - today_value).days


def task_timestamp(task: TaskRecord) -> Optional[date]:
    return parse_date(task.updated_date) or parse_date(task.created_date)


def compute_unlock_depths(tasks: List[TaskRecord]) -> Dict[int, int]:
    reverse_edges: Dict[int, Set[int]] = {task.id: set() for task in tasks}
    valid_ids = set(reverse_edges)
    for task in tasks:
        for dependency in task.depends_on:
            if dependency in valid_ids:
                reverse_edges.setdefault(dependency, set()).add(task.id)

    def downstream_count(task_id: int) -> int:
        seen: Set[int] = set()
        stack = list(reverse_edges.get(task_id, set()))
        while stack:
            item = stack.pop()
            if item in seen:
                continue
            seen.add(item)
            stack.extend(reverse_edges.get(item, set()))
        return len(seen)

    return {task.id: downstream_count(task.id) for task in tasks}


def task_summary(
    task: TaskRecord,
    *,
    today_value: Optional[date] = None,
    unlock_depth: Optional[int] = None,
    reason: Optional[str] = None,
) -> Dict[str, Any]:
    entry: Dict[str, Any] = {
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "priority": task.priority,
        "priority_score": priority_score(task),
        "due_date": task.due_date,
        "depends_on": list(task.depends_on),
        "blocked_by": list(task.blocked_by),
        "updated_date": task.updated_date,
        "created_date": task.created_date,
        "epic_slug": task.epic_slug,
        "task_path": task.task_path,
    }
    if today_value is not None:
        entry["urgency_score"] = urgency_score(task, today_value)
    if unlock_depth is not None:
        entry["unlock_depth"] = unlock_depth
    if reason is not None:
        entry["reason"] = reason
    return entry


def focus_sort_key(entry: Dict[str, Any]) -> Tuple[int, int, int, int]:
    return (
        -int(entry.get("priority_score", 0)),
        int(entry.get("urgency_score", NO_DUE_DATE_URGENCY)),
        -int(entry.get("unlock_depth", 0)),
        int(entry.get("id", 0)),
    )


def sort_focus_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(entries, key=focus_sort_key)


def base_report(
    report_name: str,
    *,
    generated_at: str,
    dry_run: bool,
    root: Path,
    script_exit_code: int,
    review_flags: Optional[List[Dict[str, Any]]] = None,
    **fields: Any,
) -> Dict[str, Any]:
    report: Dict[str, Any] = {
        "report_name": report_name,
        "generated_at": generated_at,
        "dry_run": dry_run,
        "root": str(root),
        "script_exit_code": script_exit_code,
        "review_flags": review_flags or [],
    }
    report.update(fields)
    return report


def dependency_validation_report(
    load: TaskLoadResult,
    *,
    generated_at: str,
    dry_run: bool,
    root: Path,
    script_exit_code: int = 0,
) -> Dict[str, Any]:
    selected = flags_matching(
        load.review_flags,
        {
            REVIEW_MISSING_DEPENDENCY_TARGET,
            REVIEW_CIRCULAR_DEPENDENCY_RISK,
            REVIEW_DUPLICATE_TASK_ID,
            REVIEW_MISSING_TASK_ID,
        },
    )
    return base_report(
        "dependency_validation_report",
        generated_at=generated_at,
        dry_run=dry_run,
        root=root,
        script_exit_code=script_exit_code,
        review_flags=selected,
        task_count=len(load.tasks),
        discovered_task_files=load.discovered_task_files,
    )


def command_next(root: Path, dry_run: bool, generated_at: str) -> Dict[str, Any]:
    today_value = date.today()
    load = read_task_files(root)
    by_id = {task.id: task for task in load.tasks}
    unlock_depths = compute_unlock_depths(load.tasks)
    candidates: List[Dict[str, Any]] = []

    for task in load.tasks:
        dependencies_satisfied, missing, unsatisfied = dependency_state(task, by_id)
        if task.status in {"open", "in-progress"} and dependencies_satisfied and blocked_by_is_clear(task, by_id):
            candidates.append(
                task_summary(
                    task,
                    today_value=today_value,
                    unlock_depth=unlock_depths.get(task.id, 0),
                    reason="status is open or in-progress, depends_on is satisfied, and blocked_by is clear",
                )
            )
        elif missing or unsatisfied:
            continue

    return {
        "next_action_report": base_report(
            "next_action_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            task_count=len(load.tasks),
            discovered_task_files=load.discovered_task_files,
            candidates=sort_focus_entries(candidates),
        ),
        "dependency_validation_report": dependency_validation_report(
            load,
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
        ),
        "script_exit_code": 0,
    }


def command_blockers(root: Path, dry_run: bool, generated_at: str) -> Dict[str, Any]:
    load = read_task_files(root)
    by_id = {task.id: task for task in load.tasks}
    blocked_tasks: List[Dict[str, Any]] = []
    missing_dependency_targets: List[Dict[str, Any]] = []

    for task in load.tasks:
        dependencies_satisfied, missing, unsatisfied = dependency_state(task, by_id)
        if task.status == "blocked" or task.blocked_by or unsatisfied:
            entry = task_summary(
                task,
                reason="task is blocked, has blocked_by, or has unsatisfied depends_on",
            )
            entry["unsatisfied_depends_on"] = unsatisfied
            blocked_tasks.append(entry)
        if missing:
            missing_dependency_targets.append(
                {
                    "id": task.id,
                    "title": task.title,
                    "task_path": task.task_path,
                    "depends_on": list(task.depends_on),
                    "missing_depends_on": missing,
                }
            )
        if dependencies_satisfied:
            continue

    return {
        "blocker_report": base_report(
            "blocker_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            blocked_tasks=blocked_tasks,
            missing_dependency_targets=missing_dependency_targets,
        ),
        "dependency_validation_report": dependency_validation_report(
            load,
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
        ),
        "script_exit_code": 0,
    }


def escape_table(value: Any) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def registry_lines(load: TaskLoadResult, generated_at: str) -> List[str]:
    lines = [
        "# Apex Work Registry",
        "",
        "```yaml",
        "registry_report:",
        f"  generated_at: {generated_at}",
        f"  source: {TASK_GLOB}",
        f"  task_count: {len(load.tasks)}",
        f"  discovered_task_files: {load.discovered_task_files}",
        f"  review_flags_count: {len(load.review_flags)}",
        "```",
        "",
        "| id | epic_slug | status | priority | due_date | depends_on | blocked_by | updated_date | created_date | title | task_path |",
        "|---:|---|---|---|---|---|---|---|---|---|---|",
    ]
    for task in sorted(load.tasks, key=lambda item: (item.epic_slug, item.id, item.task_path)):
        lines.append(
            "| {id} | {epic_slug} | {status} | {priority} | {due_date} | {depends_on} | "
            "{blocked_by} | {updated_date} | {created_date} | {title} | {task_path} |".format(
                id=task.id,
                epic_slug=escape_table(task.epic_slug),
                status=escape_table(task.status),
                priority=escape_table(task.priority),
                due_date=escape_table(task.due_date),
                depends_on=escape_table(",".join(str(dep) for dep in task.depends_on)),
                blocked_by=escape_table(",".join(task.blocked_by)),
                updated_date=escape_table(task.updated_date),
                created_date=escape_table(task.created_date),
                title=escape_table(task.title),
                task_path=escape_table(task.task_path),
            )
        )
    lines.append("")
    if load.review_flags:
        lines.extend(["## Review Flags", ""])
        for item in load.review_flags:
            lines.append(
                f"- `{item.get('flag')}`: {escape_table(item.get('reason'))} "
                f"({escape_table(item.get('task_path', item.get('id', 'global')))})"
            )
        lines.append("")
    return lines


def generate_registry_content(root: Path, generated_at: str) -> Tuple[str, TaskLoadResult]:
    load = read_task_files(root)
    return "\n".join(registry_lines(load, generated_at)), load


def command_registry(root: Path, dry_run: bool, generated_at: str) -> Dict[str, Any]:
    content, load = generate_registry_content(root, generated_at)
    registry_path = root / REGISTRY_RELATIVE_PATH
    wrote_registry = False

    if not dry_run:
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        registry_path.write_text(content, encoding="utf-8")
        wrote_registry = True

    return {
        "registry_report": base_report(
            "registry_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            target_path=str(REGISTRY_RELATIVE_PATH),
            allowed_write_path=str(REGISTRY_RELATIVE_PATH),
            wrote_registry=wrote_registry,
            task_count=len(load.tasks),
            discovered_task_files=load.discovered_task_files,
            registry_content=content,
        ),
        "script_exit_code": 0,
    }


def command_stall(
    root: Path,
    dry_run: bool,
    generated_at: str,
    stale_days: int,
    today_value: Optional[str],
) -> Dict[str, Any]:
    load = read_task_files(root)
    current_date = parse_today(today_value)
    stale_tasks: List[Dict[str, Any]] = []
    review_flags = list(load.review_flags)

    for task in load.tasks:
        if task.status in {"done", "deferred"}:
            continue
        timestamp = task_timestamp(task)
        if timestamp is None:
            continue
        age_days = (current_date - timestamp).days
        if age_days >= stale_days:
            entry = task_summary(
                task,
                reason="non-done task has not changed within stale-days threshold",
            )
            entry["stall_days"] = age_days
            stale_tasks.append(entry)
            review_flags.append(
                review_flag(
                    REVIEW_STALE_TASK_CANDIDATE,
                    f"no timestamp change for {age_days} days",
                    id=task.id,
                    task_path=task.task_path,
                    stall_days=age_days,
                )
            )

    return {
        "stall_report": base_report(
            "stall_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=review_flags,
            stale_days_threshold=stale_days,
            stale_tasks=stale_tasks,
        ),
        "script_exit_code": 0,
    }


def command_drift(root: Path, dry_run: bool, generated_at: str) -> Dict[str, Any]:
    content, load = generate_registry_content(root, generated_at)
    registry_path = root / REGISTRY_RELATIVE_PATH
    current_content: Optional[str] = None
    if registry_path.exists():
        current_content = registry_path.read_text(encoding="utf-8")
    drift_detected = current_content != content
    review_flags = list(load.review_flags)
    if drift_detected:
        review_flags.append(
            review_flag(
                REVIEW_DRIFT_DETECTED,
                "registry content does not match regenerated task index",
                task_path=str(REGISTRY_RELATIVE_PATH),
            )
        )
        review_flags.append(
            review_flag(
                REVIEW_REGISTRY_OUT_OF_DATE,
                "registry should be regenerated by running registry --dry-run false after review",
                task_path=str(REGISTRY_RELATIVE_PATH),
            )
        )

    return {
        "drift_report": base_report(
            "drift_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=review_flags,
            source=TASK_GLOB,
            registry_path=str(REGISTRY_RELATIVE_PATH),
            registry_exists=registry_path.exists(),
            drift_detected=drift_detected,
            task_count=len(load.tasks),
        ),
        "registry_report": base_report(
            "registry_report",
            generated_at=generated_at,
            dry_run=True,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            target_path=str(REGISTRY_RELATIVE_PATH),
            registry_content=content,
        ),
        "script_exit_code": 0,
    }


def command_score(root: Path, dry_run: bool, generated_at: str, today_value: Optional[str]) -> Dict[str, Any]:
    load = read_task_files(root)
    current_date = parse_today(today_value)
    unlock_depths = compute_unlock_depths(load.tasks)
    by_id = {task.id: task for task in load.tasks}
    scored_tasks: List[Dict[str, Any]] = []
    focus_candidates: List[Dict[str, Any]] = []

    for task in load.tasks:
        entry = task_summary(
            task,
            today_value=current_date,
            unlock_depth=unlock_depths.get(task.id, 0),
            reason="priority_score, urgency_score, and unlock_depth computed from frontmatter and depends_on graph",
        )
        scored_tasks.append(entry)
        dependencies_satisfied, _missing, _unsatisfied = dependency_state(task, by_id)
        if task.status in {"open", "in-progress"} and dependencies_satisfied and blocked_by_is_clear(task, by_id):
            focus_candidates.append(entry)

    return {
        "score_report": base_report(
            "score_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            tasks=sorted(scored_tasks, key=lambda item: int(item["id"])),
        ),
        "focus_candidate_report": base_report(
            "focus_candidate_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            candidates=sort_focus_entries(focus_candidates),
        ),
        "script_exit_code": 0,
    }


def render_human(report_bundle: Dict[str, Any]) -> str:
    lines: List[str] = []
    for key, value in report_bundle.items():
        if key == "script_exit_code":
            continue
        lines.append(f"# {key}")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(value, indent=2, sort_keys=True))
        lines.append("```")
        lines.append("")
    lines.append(f"script_exit_code: {report_bundle.get('script_exit_code', 0)}")
    return "\n".join(lines)


def emit(report_bundle: Dict[str, Any], json_mode: bool) -> int:
    exit_code = int(report_bundle.get("script_exit_code", 0))
    if json_mode:
        print(json.dumps(report_bundle, indent=2, sort_keys=True))
    else:
        print(render_human(report_bundle))
    return exit_code


def script_failure_report(root: Path, dry_run: bool, generated_at: str, exc: Exception) -> Dict[str, Any]:
    failure = review_flag(REVIEW_SCRIPT_FAILED, str(exc))
    return {
        "script_failure_report": base_report(
            "script_failure_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=1,
            review_flags=[failure],
            script_stderr=str(exc),
        ),
        "script_exit_code": 1,
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    dry_run = parse_dry_run(args.dry_run)
    generated_at = utc_now_iso()

    try:
        if args.subcommand == "next":
            report_bundle = command_next(root, dry_run, generated_at)
        elif args.subcommand == "blockers":
            report_bundle = command_blockers(root, dry_run, generated_at)
        elif args.subcommand == "registry":
            report_bundle = command_registry(root, dry_run, generated_at)
        elif args.subcommand == "stall":
            report_bundle = command_stall(root, dry_run, generated_at, args.stale_days, args.today)
        elif args.subcommand == "drift":
            report_bundle = command_drift(root, dry_run, generated_at)
        elif args.subcommand == "score":
            report_bundle = command_score(root, dry_run, generated_at, args.today)
        else:
            raise ValueError(f"unsupported subcommand: {args.subcommand}")
    except Exception as exc:
        report_bundle = script_failure_report(root, dry_run, generated_at, exc)

    return emit(report_bundle, args.json)


if __name__ == "__main__":
    sys.exit(main())