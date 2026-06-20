
# FILE: apex-meta/scripts/apex_sync.py

```python
#!/usr/bin/env python3
"""Deterministic read-side synchronization checks for Apex task files.

This script is standard-library-only. It reads Apex Markdown task files from
apex-meta/epics/*/[0-9][0-9][0-9].md, computes reports, and writes only
apex-meta/registry/index.md when the registry subcommand is invoked with
--dry-run false.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

STATUS_ENUM = {"open", "in-progress", "blocked", "done", "deferred"}
PRIORITY_VALUES = {"high": 3, "medium": 2, "low": 1}
NO_DUE_DATE_SCORE = 999
TASK_GLOB = "apex-meta/epics/*/[0-9][0-9][0-9].md"
REGISTRY_RELATIVE_PATH = Path("apex-meta/registry/index.md")

REVIEW_MALFORMED_FRONTMATTER = "malformed_frontmatter"
REVIEW_MISSING_TASK_ID = "missing_task_id"
REVIEW_UNSUPPORTED_STATUS = "unsupported_status"
REVIEW_MISSING_DEPENDENCY_TARGET = "missing_dependency_target"
REVIEW_CIRCULAR_DEPENDENCY_RISK = "circular_dependency_risk"
REVIEW_BLOCKED_WITHOUT_REASON = "blocked_without_reason"
REVIEW_STALE_TASK_CANDIDATE = "stale_task_candidate"
REVIEW_REGISTRY_OUT_OF_DATE = "registry_out_of_date"
REVIEW_DRIFT_DETECTED = "drift_detected"
REVIEW_SCRIPT_FAILED = "script_failed"


@dataclass(frozen=True)
class TaskRecord:
    id: int
    title: str
    status: str
    priority: str
    due_date: Optional[str]
    depends_on: Tuple[int, ...]
    blocked_by: Tuple[str, ...]
    epic_slug: str
    task_path: str
    frontmatter: Dict[str, Any]
    body: str


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute Apex synchronization reports from Markdown task files."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root containing apex-meta/epics/. Default: current directory.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Write machine-readable JSON to stdout.",
    )
    parser.add_argument(
        "--dry-run",
        nargs="?",
        const="true",
        default="true",
        choices=("true", "false"),
        help="Dry-run mode. Default: true. Use '--dry-run false' only for registry writes.",
    )

    subcommands = parser.add_subparsers(dest="subcommand", required=True)
    subcommands.add_parser("next", help="Compute actionable next task candidates.")
    subcommands.add_parser("blockers", help="List blocked tasks and missing dependency targets.")
    subcommands.add_parser("registry", help="Rebuild or print the compact registry index.")

    stall_parser = subcommands.add_parser("stall", help="Detect stale task candidates.")
    stall_parser.add_argument(
        "--stale-days",
        type=int,
        default=14,
        help="Minimum days since last task timestamp before flagging a non-done task. Default: 14.",
    )
    stall_parser.add_argument(
        "--today",
        default=None,
        help="Override today's date for deterministic tests, formatted YYYY-MM-DD.",
    )

    drift_parser = subcommands.add_parser("drift", help="Detect registry/source mismatch.")
    drift_parser.add_argument(
        "--registry-path",
        default=str(REGISTRY_RELATIVE_PATH),
        help="Registry path relative to root. Default: apex-meta/registry/index.md.",
    )

    score_parser = subcommands.add_parser(
        "score",
        help="Compute priority, urgency, unlock, and focus scores.",
    )
    score_parser.add_argument(
        "--today",
        default=None,
        help="Override today's date for deterministic tests, formatted YYYY-MM-DD.",
    )

    return parser.parse_args(argv)


def parse_dry_run(value: str) -> bool:
    return value.lower() != "false"


def read_task_files(root: Path) -> Tuple[List[TaskRecord], List[Dict[str, Any]]]:
    tasks: List[TaskRecord] = []
    review_flags: List[Dict[str, Any]] = []
    for task_file in sorted(root.glob(TASK_GLOB)):
        try:
            text = task_file.read_text(encoding="utf-8")
        except OSError as exc:
            review_flags.append(
                flag(REVIEW_MALFORMED_FRONTMATTER, task_file, f"cannot read file: {exc}")
            )
            continue

        frontmatter, body, parse_error = parse_markdown_task(text)
        if parse_error:
            review_flags.append(flag(REVIEW_MALFORMED_FRONTMATTER, task_file, parse_error))
            continue

        record = build_task_record(root, task_file, frontmatter, body, review_flags)
        if record is not None:
            tasks.append(record)

    review_flags.extend(validate_duplicate_ids(tasks))
    review_flags.extend(validate_dependency_targets(tasks))
    review_flags.extend(validate_status_values(tasks))
    review_flags.extend(validate_blocked_reason(tasks))
    review_flags.extend(validate_circular_dependency_risk(tasks))
    return tasks, review_flags


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


def parse_minimal_yaml(lines: List[str]) -> Dict[str, Any]:
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
        if ":" not in raw_line:
            raise ValueError(f"frontmatter line {line_number}: expected key: value")
        key, value = raw_line.split(":", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"frontmatter line {line_number}: empty key")
        value = value.strip()
        current_key = key
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
    raw_id = frontmatter.get("id")
    if raw_id is None:
        review_flags.append(
            flag(REVIEW_MISSING_TASK_ID, task_file, "frontmatter field id is missing")
        )
        return None
    try:
        task_id = int(raw_id)
    except (TypeError, ValueError):
        review_flags.append(
            flag(REVIEW_MISSING_TASK_ID, task_file, "frontmatter field id is not an integer")
        )
        return None

    relative_path = safe_relative(task_file, root)
    epic_slug = task_file.parent.name
    title = str(frontmatter.get("title") or fallback_title(body) or task_file.stem)
    status = str(frontmatter.get("status") or "open")
    priority = str(frontmatter.get("priority") or "medium").lower()
    if priority not in PRIORITY_VALUES:
        priority = "medium"
    due_date_value = frontmatter.get("due_date")
    due_date = None if due_date_value in (None, "") else str(due_date_value)
    depends_on = tuple(coerce_int_list(frontmatter.get("depends_on")))
    blocked_by = tuple(coerce_string_list(frontmatter.get("blocked_by")))

    return TaskRecord(
        id=task_id,
        title=title,
        status=status,
        priority=priority,
        due_date=due_date,
        depends_on=depends_on,
        blocked_by=blocked_by,
        epic_slug=epic_slug,
        task_path=relative_path,
        frontmatter=frontmatter,
        body=body,
    )


def fallback_title(body: str) -> str:
    for line in body.splitlines():
        clean = line.strip()
        if clean.startswith("#"):
            return clean.lstrip("#").strip()
    return ""


def safe_relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def coerce_int_list(value: Any) -> List[int]:
    if value is None or value == "":
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
    if value is None or value == "":
        return []
    raw_items = value if isinstance(value, list) else [value]
    return [str(item).strip() for item in raw_items if str(item).strip()]


def flag(name: str, task_path: Path | str, reason: str) -> Dict[str, Any]:
    return {
        "review_flags": [name],
        "task_path": str(task_path).replace("\\", "/"),
        "reason": reason,
    }


def validate_duplicate_ids(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    seen: Dict[int, TaskRecord] = {}
    flags: List[Dict[str, Any]] = []
    for task in tasks:
        if task.id in seen:
            flags.append(
                {
                    "review_flags": [REVIEW_MISSING_TASK_ID],
                    "id": task.id,
                    "task_path": task.task_path,
                    "reason": f"duplicate id also appears in {seen[task.id].task_path}",
                }
            )
        else:
            seen[task.id] = task
    return flags


def validate_dependency_targets(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    ids = {task.id for task in tasks}
    flags: List[Dict[str, Any]] = []
    for task in tasks:
        missing = [dep for dep in task.depends_on if dep not in ids]
        if missing:
            flags.append(
                {
                    "review_flags": [REVIEW_MISSING_DEPENDENCY_TARGET],
                    "id": task.id,
                    "task_path": task.task_path,
                    "depends_on": list(task.depends_on),
                    "reason": f"missing depends_on target(s): {missing}",
                }
            )
    return flags


def validate_status_values(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    flags: List[Dict[str, Any]] = []
    for task in tasks:
        if task.status not in STATUS_ENUM:
            flags.append(
                {
                    "review_flags": [REVIEW_UNSUPPORTED_STATUS],
                    "id": task.id,
                    "status": task.status,
                    "task_path": task.task_path,
                    "reason": "status is not one of open, in-progress, blocked, done, deferred",
                }
            )
    return flags


def validate_blocked_reason(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    flags: List[Dict[str, Any]] = []
    for task in tasks:
        if task.status == "blocked" and not task.blocked_by:
            flags.append(
                {
                    "review_flags": [REVIEW_BLOCKED_WITHOUT_REASON],
                    "id": task.id,
                    "task_path": task.task_path,
                    "reason": "status is blocked but blocked_by is empty",
                }
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
        placeholder = TaskRecord(0, "", "", "", None, (), (), "", "", {}, "")
        for dep in by_id.get(task_id, placeholder).depends_on:
            if dep in by_id:
                visit(dep, stack)
        stack.pop()
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in sorted(by_id):
        visit(task_id, [])

    flags: List[Dict[str, Any]] = []
    seen_cycles: Set[Tuple[int, ...]] = set()
    for cycle in cycles:
        normalized = tuple(cycle)
        if normalized in seen_cycles:
            continue
        seen_cycles.add(normalized)
        flags.append(
            {
                "review_flags": [REVIEW_CIRCULAR_DEPENDENCY_RISK],
                "depends_on": list(cycle),
                "reason": "cycle detected in depends_on graph",
            }
        )
    return flags


def dependency_validation_report(
    tasks: List[TaskRecord],
    review_flags: List[Dict[str, Any]],
) -> Dict[str, Any]:
    selected = [
        item
        for item in review_flags
        if any(
            value in item.get("review_flags", [])
            for value in (
                REVIEW_MISSING_DEPENDENCY_TARGET,
                REVIEW_CIRCULAR_DEPENDENCY_RISK,
            )
        )
    ]
    return {
        "dependency_validation_report": {
            "task_count": len(tasks),
            "review_flags": selected,
        }
    }


def is_done(task: Optional[TaskRecord]) -> bool:
    return bool(task and task.status == "done")


def blocked_by_is_clear(task: TaskRecord, by_id: Dict[int, TaskRecord]) -> bool:
    if not task.blocked_by:
        return True
    parsed_ids: List[int] = []
    for value in task.blocked_by:
        try:
            parsed_ids.append(int(value))
        except ValueError:
            return False
    return all(is_done(by_id.get(blocker_id)) for blocker_id in parsed_ids)


def dependency_state(
    task: TaskRecord,
    by_id: Dict[int, TaskRecord],
) -> Tuple[bool, List[int], List[int]]:
    missing = [dep for dep in task.depends_on if dep not in by_id]
    unsatisfied = [
        dep for dep in task.depends_on if dep in by_id and by_id[dep].status != "done"
    ]
    return not missing and not unsatisfied, missing, unsatisfied


def actionable_tasks(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    by_id = {task.id: task for task in tasks}
    unlock_depths = compute_unlock_depths(tasks)
    entries: List[Dict[str, Any]] = []
    for task in tasks:
        dependencies_satisfied, missing, unsatisfied = dependency_state(task, by_id)
        blocked_clear = blocked_by_is_clear(task, by_id)
        actionable = (
            task.status in {"open", "in-progress"}
            and dependencies_satisfied
            and blocked_clear
        )
        if actionable:
            entries.append(
                task_summary(
                    task,
                    priority_score=priority_score(task),
                    urgency_score=urgency_score(task, date.today()),
                    unlock_depth=unlock_depths.get(task.id, 0),
                    reason=(
                        "status is open or in-progress, depends_on is satisfied, "
                        "and blocked_by is clear"
                    ),
                )
            )
        elif missing or unsatisfied:
            continue
    return sort_focus_entries(entries)


def task_summary(
    task: TaskRecord,
    priority_score: Optional[int] = None,
    urgency_score: Optional[int] = None,
    unlock_depth: Optional[int] = None,
    reason: Optional[str] = None,
) -> Dict[str, Any]:
    entry: Dict[str, Any] = {
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "priority": task.priority,
        "due_date": task.due_date,
        "depends_on": list(task.depends_on),
        "blocked_by": list(task.blocked_by),
        "epic_slug": task.epic_slug,
        "task_path": task.task_path,
    }
    if priority_score is not None:
        entry["priority_score"] = priority_score
    if urgency_score is not None:
        entry["urgency_score"] = urgency_score
    if unlock_depth is not None:
        entry["unlock_depth"] = unlock_depth
    if reason is not None:
        entry["reason"] = reason
    return entry


def sort_focus_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(
        entries,
        key=lambda item: (
            -int(item.get("priority_score", 0)),
            int(item.get("urgency_score", NO_DUE_DATE_SCORE)),
            -int(item.get("unlock_depth", 0)),
            int(item.get("id", 0)),
        ),
    )


def command_next(root: Path, dry_run: bool) -> Dict[str, Any]:
    tasks, review_flags = read_task_files(root)
    candidates = actionable_tasks(tasks)
    report = {
        "next_action_report": {
            "dry_run": dry_run,
            "task_count": len(tasks),
            "candidates": candidates,
            "review_flags": review_flags,
        },
        **dependency_validation_report(tasks, review_flags),
        "script_exit_code": 0,
    }
    return report


def command_blockers(root: Path, dry_run: bool) -> Dict[str, Any]:
    tasks, review_flags = read_task_files(root)
    by_id = {task.id: task for task in tasks}
    blocked_entries: List[Dict[str, Any]] = []
    missing_dependency_entries: List[Dict[str, Any]] = []
    for task in tasks:
        dependencies_satisfied, missing, unsatisfied = dependency_state(task, by_id)
        if task.status == "blocked" or task.blocked_by or unsatisfied:
            entry = task_summary(
                task,
                reason="task is blocked, has blocked_by, or has unsatisfied depends_on",
            )
            entry["unsatisfied_depends_on"] = unsatisfied
            blocked_entries.append(entry)
        if missing:
            missing_dependency_entries.append(
                {
                    "id": task.id,
                    "task_path": task.task_path,
                    "depends_on": list(task.depends_on),
                    "missing_depends_on": missing,
                }
            )
        if dependencies_satisfied:
            continue
    return {
        "blocker_report": {
            "dry_run": dry_run,
            "blocked_tasks": blocked_entries,
            "missing_dependency_targets": missing_dependency_entries,
            "review_flags": review_flags,
        },
        **dependency_validation_report(tasks, review_flags),
        "script_exit_code": 0,
    }


def registry_lines(tasks: List[TaskRecord], review_flags: List[Dict[str, Any]]) -> List[str]:
    lines = [
        "# Apex Work Registry",
        "",
        "```yaml",
        "registry_report:",
        f"  source: {TASK_GLOB}",
        f"  task_count: {len(tasks)}",
        f"  review_flags_count: {len(review_flags)}",
        "```",
        "",
        "| id | epic_slug | status | priority | due_date | depends_on | blocked_by | title | task_path |",
        "|---:|---|---|---|---|---|---|---|---|",
    ]
    for task in sorted(tasks, key=lambda item: (item.epic_slug, item.id)):
        lines.append(
            "| {id} | {epic_slug} | {status} | {priority} | {due_date} | "
            "{depends_on} | {blocked_by} | {title} | {task_path} |".format(
                id=task.id,
                epic_slug=escape_table(task.epic_slug),
                status=escape_table(task.status),
                priority=escape_table(task.priority),
                due_date=escape_table(task.due_date or ""),
                depends_on=escape_table(",".join(str(dep) for dep in task.depends_on)),
                blocked_by=escape_table(",".join(task.blocked_by)),
                title=escape_table(task.title),
                task_path=escape_table(task.task_path),
            )
        )
    lines.append("")
    if review_flags:
        lines.extend(["## Review Flags", ""])
        for item in review_flags:
            lines.append(f"- {item}")
        lines.append("")
    return lines


def escape_table(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def generate_registry_content(
    root: Path,
) -> Tuple[str, List[TaskRecord], List[Dict[str, Any]]]:
    tasks, review_flags = read_task_files(root)
    return "\n".join(registry_lines(tasks, review_flags)), tasks, review_flags


def command_registry(root: Path, dry_run: bool) -> Dict[str, Any]:
    content, tasks, review_flags = generate_registry_content(root)
    registry_path = root / REGISTRY_RELATIVE_PATH
    wrote = False
    if not dry_run:
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        registry_path.write_text(content, encoding="utf-8")
        wrote = True
    return {
        "registry_report": {
            "dry_run": dry_run,
            "task_count": len(tasks),
            "target_path": str(REGISTRY_RELATIVE_PATH),
            "wrote_registry": wrote,
            "registry_content": content,
            "review_flags": review_flags,
        },
        "script_exit_code": 0,
    }


def parse_today(value: Optional[str]) -> date:
    if value is None:
        return date.today()
    return datetime.strptime(value, "%Y-%m-%d").date()


def extract_task_timestamp(task: TaskRecord) -> Optional[date]:
    for key in ("updated", "updated_at", "created", "created_at"):
        value = task.frontmatter.get(key)
        if value in (None, ""):
            continue
        parsed = parse_date(str(value))
        if parsed is not None:
            return parsed
    return None


def parse_date(value: str) -> Optional[date]:
    clean = value.strip()
    if not clean:
        return None
    try:
        if "T" in clean:
            return datetime.fromisoformat(clean.replace("Z", "+00:00")).date()
        return datetime.strptime(clean[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def command_stall(
    root: Path,
    dry_run: bool,
    stale_days: int,
    today_value: Optional[str],
) -> Dict[str, Any]:
    tasks, review_flags = read_task_files(root)
    current_date = parse_today(today_value)
    stale_entries: List[Dict[str, Any]] = []
    for task in tasks:
        if task.status in {"done", "deferred"}:
            continue
        timestamp = extract_task_timestamp(task)
        if timestamp is None:
            continue
        age = (current_date - timestamp).days
        if age >= stale_days:
            entry = task_summary(
                task,
                reason="non-done task has not changed within stale-days threshold",
            )
            entry["stall_days"] = age
            stale_entries.append(entry)
            review_flags.append(
                {
                    "review_flags": [REVIEW_STALE_TASK_CANDIDATE],
                    "id": task.id,
                    "task_path": task.task_path,
                    "reason": f"no timestamp change for {age} days",
                }
            )
    return {
        "stall_report": {
            "dry_run": dry_run,
            "stale_days_threshold": stale_days,
            "stale_tasks": stale_entries,
            "review_flags": review_flags,
        },
        "script_exit_code": 0,
    }


def command_drift(root: Path, dry_run: bool, registry_path_value: str) -> Dict[str, Any]:
    content, tasks, review_flags = generate_registry_content(root)
    registry_path = root / registry_path_value
    current_content: Optional[str] = None
    if registry_path.exists():
        current_content = registry_path.read_text(encoding="utf-8")
    drift_detected = current_content != content
    if drift_detected:
        review_flags.append(
            {
                "review_flags": [REVIEW_DRIFT_DETECTED, REVIEW_REGISTRY_OUT_OF_DATE],
                "task_path": registry_path_value,
                "reason": "registry content does not match regenerated task index",
            }
        )
    return {
        "drift_report": {
            "dry_run": dry_run,
            "source": TASK_GLOB,
            "task_count": len(tasks),
            "registry_path": registry_path_value,
            "drift_detected": drift_detected,
            "review_flags": review_flags,
        },
        "registry_report": {
            "dry_run": True,
            "target_path": registry_path_value,
            "registry_content": content,
        },
        "script_exit_code": 0,
    }


def priority_score(task: TaskRecord) -> int:
    return PRIORITY_VALUES.get(task.priority, PRIORITY_VALUES["medium"])


def urgency_score(task: TaskRecord, today_value: date) -> int:
    if not task.due_date:
        return NO_DUE_DATE_SCORE
    parsed = parse_date(task.due_date)
    if parsed is None:
        return NO_DUE_DATE_SCORE
    return (parsed - today_value).days


def compute_unlock_depths(tasks: List[TaskRecord]) -> Dict[int, int]:
    reverse: Dict[int, Set[int]] = {task.id: set() for task in tasks}
    valid_ids = set(reverse)
    for task in tasks:
        for dep in task.depends_on:
            if dep in valid_ids:
                reverse.setdefault(dep, set()).add(task.id)

    def downstream_count(task_id: int) -> int:
        seen: Set[int] = set()
        stack = list(reverse.get(task_id, set()))
        while stack:
            item = stack.pop()
            if item in seen:
                continue
            seen.add(item)
            stack.extend(reverse.get(item, set()))
        return len(seen)

    return {task.id: downstream_count(task.id) for task in tasks}


def command_score(
    root: Path,
    dry_run: bool,
    today_value: Optional[str],
) -> Dict[str, Any]:
    tasks, review_flags = read_task_files(root)
    current_date = parse_today(today_value)
    unlock_depths = compute_unlock_depths(tasks)
    by_id = {task.id: task for task in tasks}
    scored_tasks: List[Dict[str, Any]] = []
    focus_candidates: List[Dict[str, Any]] = []
    for task in tasks:
        entry = task_summary(
            task,
            priority_score=priority_score(task),
            urgency_score=urgency_score(task, current_date),
            unlock_depth=unlock_depths.get(task.id, 0),
            reason=(
                "priority_score, urgency_score, and unlock_depth computed "
                "from frontmatter and depends_on graph"
            ),
        )
        scored_tasks.append(entry)
        dependencies_satisfied, _missing, _unsatisfied = dependency_state(task, by_id)
        if (
            task.status in {"open", "in-progress"}
            and dependencies_satisfied
            and blocked_by_is_clear(task, by_id)
        ):
            focus_candidates.append(entry)
    return {
        "score_report": {
            "dry_run": dry_run,
            "tasks": sorted(scored_tasks, key=lambda item: int(item["id"])),
            "review_flags": review_flags,
        },
        "focus_candidate_report": {
            "dry_run": dry_run,
            "candidates": sort_focus_entries(focus_candidates),
        },
        "script_exit_code": 0,
    }


def render_human(report: Dict[str, Any]) -> str:
    lines: List[str] = []
    for key, value in report.items():
        if key == "script_exit_code":
            continue
        lines.append(f"# {key}")
        lines.append("")
        lines.append(json.dumps(value, indent=2, sort_keys=True))
        lines.append("")
    lines.append(f"script_exit_code: {report.get('script_exit_code', 0)}")
    return "\n".join(lines)


def emit(report: Dict[str, Any], json_mode: bool) -> int:
    exit_code = int(report.get("script_exit_code", 0))
    if json_mode:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_human(report))
    return exit_code


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    dry_run = parse_dry_run(args.dry_run)
    try:
        if args.subcommand == "next":
            report = command_next(root, dry_run)
        elif args.subcommand == "blockers":
            report = command_blockers(root, dry_run)
        elif args.subcommand == "registry":
            report = command_registry(root, dry_run)
        elif args.subcommand == "stall":
            report = command_stall(root, dry_run, args.stale_days, args.today)
        elif args.subcommand == "drift":
            report = command_drift(root, dry_run, args.registry_path)
        elif args.subcommand == "score":
            report = command_score(root, dry_run, args.today)
        else:
            report = {"script_exit_code": 1, "review_flags": [REVIEW_SCRIPT_FAILED]}
    except Exception as exc:
        report = {
            "script_exit_code": 1,
            "review_flags": [REVIEW_SCRIPT_FAILED],
            "script_stderr": str(exc),
        }
    return emit(report, args.json)


if __name__ == "__main__":
    sys.exit(main())