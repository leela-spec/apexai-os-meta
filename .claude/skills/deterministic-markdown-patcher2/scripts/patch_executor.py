#!/usr/bin/env python3
"""Deterministic Markdown patch executor.

Standard-library-only CLI for validating semantic patch intents, resolving live
targets, applying one bounded mutation, and reporting JSON proof or failure.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


REPORTS = {
    "success": "patch_success.json",
    "failure": "patch_failure.json",
    "ambiguity": "ambiguity_report.json",
    "validation": "validation_report.json",
}
OPS = {
    "inspect",
    "locate",
    "extract-span",
    "replace-once",
    "replace-heading-section",
    "frontmatter-set",
    "diff",
    "apply-intent",
    "validate-intent",
}
MUTATION_OPS = {"replace-once", "replace-heading-section", "frontmatter-set"}
FORBIDDEN_INTENT_KEYS = {
    "old_text",
    "required_old_text",
    "line_number",
    "line_start",
    "line_end",
    "line_range",
    "hunk",
    "diff_hunks",
    "unified_diff",
}


class PatchError(Exception):
    def __init__(
        self,
        message: str,
        *,
        code: int = 1,
        mode: str = "failure",
        field: str = "",
        candidates: list[dict[str, Any]] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.mode = mode
        self.field = field
        self.candidates = candidates or []


def now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def load_json(path: Path, label: str) -> Any:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        raise PatchError(
            f"{label} JSON parse failed: {exc}",
            code=2,
            mode="validation failed",
            field=label,
        )
    except OSError as exc:
        raise PatchError(
            f"{label} could not be read: {exc}",
            code=2,
            mode="validation failed",
            field=label,
        )


def repo_root(args: argparse.Namespace) -> Path:
    return Path(args.repo or ".").resolve()


def normalize_rel(path: str) -> str:
    rel = path.replace("\\", "/").strip()
    while rel.startswith("./"):
        rel = rel[2:]
    if not rel or rel.startswith("../") or rel == ".." or Path(rel).is_absolute():
        raise PatchError(
            "target path outside allowlist",
            code=2,
            mode="target path outside allowlist",
            field="target.target_file_guess",
        )
    return rel


def path_matches(pattern: str, rel: str) -> bool:
    pat = normalize_rel(pattern)
    variants = {pat}
    if "/**/" in pat:
        variants.add(pat.replace("/**/", "/"))
    if pat.endswith("/**"):
        variants.add(pat[:-3])
    return any(
        rel == item
        or rel.startswith(item.rstrip("/") + "/")
        or fnmatch.fnmatch(rel, item)
        for item in variants
    )


def require_path_allowed(policy: dict[str, Any], rel: str) -> None:
    allow = policy.get("path_allowlist", [])
    protected = policy.get("protected_paths", [])
    if not any(path_matches(p, rel) for p in allow):
        raise PatchError(
            "target path outside allowlist",
            code=2,
            mode="target path outside allowlist",
            field="path_allowlist",
        )
    if any(path_matches(p, rel) for p in protected):
        raise PatchError(
            "target path outside allowlist",
            code=2,
            mode="target path outside allowlist",
            field="protected_paths",
        )


def safe_target(repo: Path, policy: dict[str, Any], target: dict[str, Any]) -> tuple[str, Path]:
    rel = normalize_rel(require_str(target, "target_file_guess", "target"))
    require_path_allowed(policy, rel)
    path = (repo / rel).resolve()
    try:
        path.relative_to(repo)
    except ValueError:
        raise PatchError(
            "target path outside allowlist",
            code=2,
            mode="target path outside allowlist",
            field="target.target_file_guess",
        )
    return rel, path


def require_str(obj: dict[str, Any], key: str, label: str, *, min_len: int = 1) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or len(value) < min_len:
        raise PatchError(f"validation failed: {label}.{key}", code=2, mode="validation failed", field=f"{label}.{key}")
    return value


def require_bool_const(obj: dict[str, Any], key: str, value: bool, label: str) -> None:
    if obj.get(key) is not value:
        raise PatchError(f"validation failed: {label}.{key}", code=2, mode="validation failed", field=f"{label}.{key}")


def check_keys(obj: dict[str, Any], allowed: set[str], label: str) -> None:
    extra = sorted(set(obj) - allowed)
    if extra:
        raise PatchError(
            f"validation failed: unexpected keys in {label}: {extra}",
            code=2,
            mode="validation failed",
            field=label,
        )


def validate_policy(policy: Any) -> dict[str, Any]:
    if not isinstance(policy, dict):
        raise PatchError("validation failed: policy must be object", code=2, mode="validation failed", field="policy")
    check_keys(
        policy,
        {
            "schema_version",
            "path_allowlist",
            "protected_paths",
            "report_directory",
            "allowed_operations",
            "validation_commands",
            "full_file_rewrite",
        },
        "policy",
    )
    if policy.get("schema_version") != "patch_policy.v1":
        raise PatchError("validation failed: policy schema_version", code=2, mode="validation failed", field="schema_version")
    for key in ("path_allowlist", "allowed_operations"):
        if not isinstance(policy.get(key), list) or not policy[key] or not all(isinstance(v, str) and v for v in policy[key]):
            raise PatchError(f"validation failed: policy.{key}", code=2, mode="validation failed", field=key)
    if not isinstance(policy.get("report_directory"), str) or not policy["report_directory"]:
        raise PatchError("validation failed: report_directory", code=2, mode="validation failed", field="report_directory")
    if not isinstance(policy.get("protected_paths", []), list):
        raise PatchError("validation failed: protected_paths", code=2, mode="validation failed", field="protected_paths")
    if policy.get("full_file_rewrite") is not False:
        raise PatchError("validation failed: full_file_rewrite", code=2, mode="validation failed", field="full_file_rewrite")
    for command in policy.get("validation_commands", []):
        if not isinstance(command, dict):
            raise PatchError("validation failed: validation_commands", code=2, mode="validation failed", field="validation_commands")
        check_keys(command, {"name", "command", "timeout_seconds", "required"}, "validation_command")
        if not isinstance(command.get("command"), list) or not command["command"] or not all(isinstance(v, str) and v for v in command["command"]):
            raise PatchError("validation failed: validation command argv", code=2, mode="validation failed", field="validation_commands.command")
        timeout = command.get("timeout_seconds")
        if not isinstance(timeout, int) or timeout < 1 or timeout > 3600:
            raise PatchError("validation failed: validation command timeout", code=2, mode="validation failed", field="validation_commands.timeout_seconds")
    unknown_ops = sorted(set(policy["allowed_operations"]) - OPS)
    if unknown_ops:
        raise PatchError(f"validation failed: unknown allowed operations {unknown_ops}", code=2, mode="validation failed", field="allowed_operations")
    return policy


def validate_intent_doc(intent_doc: Any) -> list[dict[str, Any]]:
    if not isinstance(intent_doc, dict):
        raise PatchError("validation failed: intent must be object", code=2, mode="validation failed", field="intent")
    check_keys(intent_doc, {"schema_version", "intents"}, "intent")
    if intent_doc.get("schema_version") != "patch_intent.v1":
        raise PatchError("validation failed: intent schema_version", code=2, mode="validation failed", field="schema_version")
    intents = intent_doc.get("intents")
    if not isinstance(intents, list) or not intents:
        raise PatchError("validation failed: intents", code=2, mode="validation failed", field="intents")
    seen: set[str] = set()
    for item in intents:
        validate_one_intent(item, seen)
    return intents


def validate_one_intent(item: Any, seen: set[str]) -> None:
    if not isinstance(item, dict):
        raise PatchError("validation failed: intent entry", code=2, mode="validation failed", field="intents[]")
    forbidden = sorted(set(item) & FORBIDDEN_INTENT_KEYS)
    if forbidden:
        raise PatchError(f"validation failed: forbidden executable keys {forbidden}", code=2, mode="validation failed", field="intents[].forbidden")
    check_keys(item, {"intent_id", "operation", "target", "hints", "replacement", "frontmatter", "validation", "safety", "notes"}, "intent")
    intent_id = require_str(item, "intent_id", "intent", min_len=3)
    if not re.match(r"^[a-z0-9][a-z0-9_-]{2,80}$", intent_id):
        raise PatchError("validation failed: intent_id", code=2, mode="validation failed", field="intent_id")
    if intent_id in seen:
        raise PatchError("validation failed: duplicate intent_id", code=2, mode="validation failed", field="intent_id")
    seen.add(intent_id)
    op = require_str(item, "operation", "intent")
    if op not in OPS:
        raise PatchError("validation failed: operation", code=2, mode="validation failed", field="operation")
    target = item.get("target")
    if not isinstance(target, dict):
        raise PatchError("validation failed: target", code=2, mode="validation failed", field="target")
    check_keys(target, {"target_file_guess", "heading_path", "frontmatter_required"}, "target")
    require_str(target, "target_file_guess", "target")
    if "heading_path" in target and (
        not isinstance(target["heading_path"], list)
        or len(target["heading_path"]) > 12
        or not all(isinstance(v, str) and v for v in target["heading_path"])
    ):
        raise PatchError("validation failed: heading_path", code=2, mode="validation failed", field="target.heading_path")
    if "hints" in item:
        validate_hints(item["hints"])
    if "replacement" in item:
        validate_replacement(item["replacement"])
    if "frontmatter" in item:
        validate_frontmatter(item["frontmatter"])
    if "validation" in item:
        validate_assertions(item["validation"])
    safety = item.get("safety")
    if not isinstance(safety, dict):
        raise PatchError("validation failed: safety", code=2, mode="validation failed", field="safety")
    check_keys(safety, {"require_unique_match", "fail_on_ambiguity", "allow_full_file_rewrite", "max_files_touched"}, "safety")
    require_bool_const(safety, "require_unique_match", True, "safety")
    require_bool_const(safety, "fail_on_ambiguity", True, "safety")
    if safety.get("allow_full_file_rewrite", False) is not False:
        raise PatchError("validation failed: allow_full_file_rewrite", code=2, mode="validation failed", field="safety.allow_full_file_rewrite")
    max_files = safety.get("max_files_touched", 1)
    if not isinstance(max_files, int) or max_files < 1 or max_files > 50:
        raise PatchError("validation failed: max_files_touched", code=2, mode="validation failed", field="safety.max_files_touched")
    if op in {"replace-once", "replace-heading-section"} and "replacement" not in item:
        raise PatchError("validation failed: missing replacement content", code=2, mode="validation failed", field="replacement")
    if op == "frontmatter-set" and "frontmatter" not in item:
        raise PatchError("validation failed: missing frontmatter", code=2, mode="validation failed", field="frontmatter")


def validate_hints(hints: Any) -> None:
    if not isinstance(hints, dict):
        raise PatchError("validation failed: hints", code=2, mode="validation failed", field="hints")
    check_keys(hints, {"nearby_phrases", "symbol_or_section_names", "frontmatter_keys"}, "hints")
    for key, maximum in (("nearby_phrases", 10), ("symbol_or_section_names", 10), ("frontmatter_keys", 20)):
        if key in hints and (
            not isinstance(hints[key], list)
            or len(hints[key]) > maximum
            or not all(isinstance(v, str) and v for v in hints[key])
        ):
            raise PatchError(f"validation failed: hints.{key}", code=2, mode="validation failed", field=f"hints.{key}")


def validate_replacement(rep: Any) -> None:
    if not isinstance(rep, dict):
        raise PatchError("validation failed: replacement", code=2, mode="validation failed", field="replacement")
    check_keys(rep, {"content", "content_role", "preserve_surrounding_formatting"}, "replacement")
    require_str(rep, "content", "replacement")
    if rep.get("content_role", "span_replacement") not in {"section_body", "span_replacement", "generated_block", "config_value"}:
        raise PatchError("validation failed: replacement.content_role", code=2, mode="validation failed", field="replacement.content_role")


def validate_frontmatter(fm: Any) -> None:
    if not isinstance(fm, dict):
        raise PatchError("validation failed: frontmatter", code=2, mode="validation failed", field="frontmatter")
    check_keys(fm, {"set", "create_if_missing"}, "frontmatter")
    if not isinstance(fm.get("set"), dict) or not fm["set"]:
        raise PatchError("validation failed: frontmatter.set", code=2, mode="validation failed", field="frontmatter.set")
    if fm.get("create_if_missing", False) is not False:
        raise PatchError(
            "frontmatter missing when operation requires it",
            code=2,
            mode="frontmatter missing when operation requires it",
            field="frontmatter.create_if_missing",
        )


def validate_assertions(validation: Any) -> None:
    if not isinstance(validation, dict):
        raise PatchError("validation failed: validation", code=2, mode="validation failed", field="validation")
    check_keys(validation, {"expected_phrases", "forbidden_phrases", "commands"}, "validation")
    for key in ("expected_phrases", "forbidden_phrases", "commands"):
        if key in validation and (not isinstance(validation[key], list) or not all(isinstance(v, str) and v for v in validation[key])):
            raise PatchError(f"validation failed: validation.{key}", code=2, mode="validation failed", field=f"validation.{key}")


def select_intent(intents: list[dict[str, Any]], args: argparse.Namespace, command: str) -> dict[str, Any]:
    if args.intent_id:
        matches = [i for i in intents if i["intent_id"] == args.intent_id]
        if len(matches) != 1:
            raise PatchError("zero target matches", code=3, mode="zero target matches", field="intent_id")
        return matches[0]
    if command == "validate-intent":
        return intents[0]
    if len(intents) != 1:
        raise PatchError("multiple target matches", code=3, mode="multiple target matches", field="intents")
    return intents[0]


def read_text(path: Path) -> tuple[str, str]:
    data = path.read_bytes()
    newline = "crlf" if b"\r\n" in data else "lf"
    return data.decode("utf-8"), newline


def write_text_preserve(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="")


def frontmatter_bounds(text: str) -> tuple[int, int] | None:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None
    first_end = 5 if text.startswith("---\r\n") else 4
    m = re.search(r"(?m)^---\s*$", text[first_end:])
    if not m:
        return None
    return first_end, first_end + m.start()


def scan_headings(text: str) -> list[dict[str, Any]]:
    headings: list[dict[str, Any]] = []
    stack: list[str] = []
    for match in re.finditer(r"(?m)^(#{1,6})[ \t]+(.+?)\s*#*\s*$", text):
        level = len(match.group(1))
        title = match.group(2).strip()
        stack = stack[: level - 1]
        stack.append(title)
        headings.append(
            {
                "level": level,
                "title": title,
                "path": stack.copy(),
                "start": match.start(),
                "body_start": match.end(),
            }
        )
    for idx, heading in enumerate(headings):
        end = len(text)
        for nxt in headings[idx + 1 :]:
            if nxt["level"] <= heading["level"]:
                end = nxt["start"]
                break
        heading["end"] = end
    return headings


def heading_summary(headings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [{"level": h["level"], "title": h["title"], "path": h["path"]} for h in headings]


def resolve_heading(text: str, heading_path: Any) -> dict[str, Any]:
    if not isinstance(heading_path, list) or not heading_path:
        raise PatchError(
            "duplicate/ambiguous heading path",
            code=3,
            mode="duplicate/ambiguous heading path",
            field="target.heading_path",
        )
    matches = [h for h in scan_headings(text) if h["path"] == heading_path]
    if len(matches) == 0:
        raise PatchError("zero target matches", code=3, mode="zero target matches", field="target.heading_path")
    if len(matches) > 1:
        raise PatchError(
            "duplicate/ambiguous heading path",
            code=3,
            mode="duplicate/ambiguous heading path",
            field="target.heading_path",
            candidates=heading_summary(matches),
        )
    return matches[0]


def resolve_phrase(text: str, hints: dict[str, Any]) -> dict[str, Any]:
    candidates: list[dict[str, Any]] = []
    for phrase in hints.get("nearby_phrases", []) + hints.get("symbol_or_section_names", []):
        start = 0
        while True:
            idx = text.find(phrase, start)
            if idx < 0:
                break
            candidates.append({"phrase": phrase, "start": idx, "end": idx + len(phrase), "preview": text[idx : idx + min(len(phrase), 120)]})
            start = idx + max(1, len(phrase))
    if not candidates:
        raise PatchError("zero target matches", code=3, mode="zero target matches", candidates=[])
    unique = {(c["start"], c["end"], c["phrase"]): c for c in candidates}
    candidates = list(unique.values())
    if len(candidates) > 1:
        raise PatchError("multiple target matches", code=3, mode="multiple target matches", candidates=candidates)
    return candidates[0]


def inspect_file(repo: Path, policy: dict[str, Any], intent: dict[str, Any]) -> dict[str, Any]:
    rel, path = safe_target(repo, policy, intent["target"])
    if not path.exists():
        raise PatchError("zero target matches", code=3, mode="zero target matches", field=rel)
    text, newline = read_text(path)
    headings = scan_headings(text)
    return {
        "path": rel,
        "size": path.stat().st_size,
        "newline_style": newline,
        "has_frontmatter": frontmatter_bounds(text) is not None,
        "headings": heading_summary(headings),
    }


def locate_target(repo: Path, policy: dict[str, Any], intent: dict[str, Any]) -> dict[str, Any]:
    rel, path = safe_target(repo, policy, intent["target"])
    if not path.exists():
        raise PatchError("zero target matches", code=3, mode="zero target matches", field=rel)
    text, _ = read_text(path)
    op = intent["operation"]
    if op == "replace-heading-section":
        h = resolve_heading(text, intent["target"].get("heading_path"))
        return {"path": rel, "kind": "heading_section", "heading_path": h["path"], "start": h["body_start"], "end": h["end"]}
    if op == "frontmatter-set":
        bounds = frontmatter_bounds(text)
        if bounds is None:
            raise PatchError(
                "frontmatter missing when operation requires it",
                code=3,
                mode="frontmatter missing when operation requires it",
                field=rel,
            )
        return {"path": rel, "kind": "frontmatter", "start": bounds[0], "end": bounds[1]}
    candidate = resolve_phrase(text, intent.get("hints", {}))
    return {"path": rel, "kind": "phrase", **candidate}


def extract_span(repo: Path, policy: dict[str, Any], intent: dict[str, Any]) -> dict[str, Any]:
    rel, path = safe_target(repo, policy, intent["target"])
    text, _ = read_text(path)
    located = locate_target(repo, policy, intent)
    return {**located, "text": text[located["start"] : located["end"]]}


def ensure_write_allowed(args: argparse.Namespace) -> None:
    if not args.allow_write:
        raise PatchError("validation failed: --allow-write required for mutation", code=2, mode="validation failed", field="allow_write")


def replace_once(repo: Path, policy: dict[str, Any], intent: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    ensure_write_allowed(args)
    rel, path = safe_target(repo, policy, intent["target"])
    text, _ = read_text(path)
    located = locate_target(repo, policy, intent)
    replacement = intent["replacement"]["content"]
    new_text = text[: located["start"]] + replacement + text[located["end"] :]
    write_text_preserve(path, new_text)
    return {"changed_paths": [rel], "resolved_target": located}


def replace_heading_section(repo: Path, policy: dict[str, Any], intent: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    ensure_write_allowed(args)
    rel, path = safe_target(repo, policy, intent["target"])
    text, _ = read_text(path)
    h = resolve_heading(text, intent["target"].get("heading_path"))
    replacement = intent["replacement"]["content"]
    if replacement and not replacement.startswith(("\n", "\r\n")):
        replacement = "\n\n" + replacement
    if replacement and not replacement.endswith(("\n", "\r\n")):
        replacement += "\n"
    new_text = text[: h["body_start"]] + replacement + text[h["end"] :]
    write_text_preserve(path, new_text)
    return {"changed_paths": [rel], "resolved_target": {"path": rel, "kind": "heading_section", "heading_path": h["path"], "start": h["body_start"], "end": h["end"]}}


def yaml_scalar(value: Any, indent: int = 0) -> str:
    pad = " " * indent
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        if value == "" or any(ch in value for ch in "\n:#[]{}") or value.strip() != value:
            return json.dumps(value)
        return value
    if isinstance(value, list):
        if not value:
            return "[]"
        return "\n" + "\n".join(pad + "- " + yaml_scalar(v, indent + 2).lstrip() for v in value)
    if isinstance(value, dict):
        if not value:
            return "{}"
        lines = []
        for key, sub in value.items():
            if not isinstance(key, str) or not key:
                raise PatchError("validation failed: frontmatter key", code=2, mode="validation failed", field="frontmatter.set")
            rendered = yaml_scalar(sub, indent + 2)
            if rendered.startswith("\n"):
                lines.append(f"{pad}{key}:{rendered}")
            else:
                lines.append(f"{pad}{key}: {rendered}")
        return "\n" + "\n".join(lines)
    raise PatchError("validation failed: unsupported frontmatter value", code=2, mode="validation failed", field="frontmatter.set")


def parse_simple_yaml(block: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#") or line.startswith((" ", "\t", "-")):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def frontmatter_set(repo: Path, policy: dict[str, Any], intent: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    ensure_write_allowed(args)
    rel, path = safe_target(repo, policy, intent["target"])
    text, _ = read_text(path)
    bounds = frontmatter_bounds(text)
    if bounds is None:
        raise PatchError(
            "frontmatter missing when operation requires it",
            code=3,
            mode="frontmatter missing when operation requires it",
            field=rel,
        )
    start, end = bounds
    existing = parse_simple_yaml(text[start:end])
    for key, value in intent["frontmatter"]["set"].items():
        existing[key] = yaml_scalar(value)
    block = "\n".join(f"{key}: {value}" for key, value in existing.items()) + "\n"
    new_text = text[:start] + block + text[end:]
    write_text_preserve(path, new_text)
    return {"changed_paths": [rel], "resolved_target": {"path": rel, "kind": "frontmatter", "start": start, "end": end}}


def run_subprocess(argv: list[str], cwd: Path, timeout: int = 60) -> dict[str, Any]:
    if not argv or argv[0] not in {"git", "rg", "yq"}:
        raise PatchError("validation failed: subprocess restricted to git, rg, yq", code=2, mode="validation failed", field="subprocess")
    proc = subprocess.run(argv, cwd=str(cwd), text=True, capture_output=True, timeout=timeout, shell=False)
    return {"command": argv, "exit_code": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}


def is_git_repo(repo: Path) -> bool:
    try:
        result = run_subprocess(["git", "rev-parse", "--is-inside-work-tree"], repo)
        return result["exit_code"] == 0 and result["stdout"].strip() == "true"
    except Exception:
        return False


def git_diff(repo: Path, paths: list[str] | None = None) -> dict[str, Any]:
    argv = ["git", "diff", "--"]
    if paths:
        argv += paths
    return run_subprocess(argv, repo)


def changed_paths(repo: Path) -> list[str]:
    result = run_subprocess(["git", "diff", "--name-only"], repo)
    if result["exit_code"] != 0:
        return []
    return [line.strip().replace("\\", "/") for line in result["stdout"].splitlines() if line.strip()]


def verify_diff_scope(repo: Path, policy: dict[str, Any], allowed: list[str]) -> None:
    if not is_git_repo(repo):
        return
    allowed_set = set(allowed)
    bad = []
    for path in changed_paths(repo):
        if path not in allowed_set:
            bad.append(path)
            continue
        try:
            require_path_allowed(policy, path)
        except PatchError:
            bad.append(path)
    if bad:
        raise PatchError(
            "diff touches unallowed path",
            code=5,
            mode="diff touches unallowed path",
            field="git diff",
            candidates=[{"path": p} for p in bad],
        )


def run_validation(repo: Path, policy: dict[str, Any], intent: dict[str, Any], allowed: list[str]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    rel, path = safe_target(repo, policy, intent["target"])
    text = path.read_text(encoding="utf-8")
    for phrase in intent.get("validation", {}).get("expected_phrases", []):
        ok = phrase in text
        results.append({"type": "expected_phrase", "phrase": phrase, "passed": ok})
        if not ok:
            raise PatchError("validation failed", code=4, mode="validation failed", field="validation.expected_phrases")
    for phrase in intent.get("validation", {}).get("forbidden_phrases", []):
        ok = phrase not in text
        results.append({"type": "forbidden_phrase", "phrase": phrase, "passed": ok})
        if not ok:
            raise PatchError("validation failed", code=4, mode="validation failed", field="validation.forbidden_phrases")
    for command in policy.get("validation_commands", []):
        if command["command"][0] not in {"git", "rg", "yq"}:
            result = {
                "type": "command",
                "name": command.get("name", command["command"][0]),
                "command": command["command"],
                "exit_code": 2,
                "stdout": "",
                "stderr": "validation command rejected: subprocess is restricted to git, rg, yq",
                "passed": False,
            }
            results.append(result)
            if command.get("required", True):
                raise PatchError("validation failed", code=4, mode="validation failed", field="validation_commands", candidates=[result])
            continue
        proc = subprocess.run(command["command"], cwd=str(repo), text=True, capture_output=True, timeout=command["timeout_seconds"], shell=False)
        result = {
            "type": "command",
            "name": command.get("name", command["command"][0]),
            "command": command["command"],
            "exit_code": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "passed": proc.returncode == 0,
        }
        results.append(result)
        if command.get("required", True) and proc.returncode != 0:
            raise PatchError("validation failed", code=4, mode="validation failed", field="validation_commands", candidates=[result])
    verify_diff_scope(repo, policy, allowed or [rel])
    return results


def report_dir(args: argparse.Namespace, policy: dict[str, Any] | None = None) -> Path | None:
    value = args.report_dir or (policy or {}).get("report_directory")
    if not value:
        return None
    path = Path(value)
    if not path.is_absolute():
        path = repo_root(args) / path
    return path


def write_report(args: argparse.Namespace, policy: dict[str, Any] | None, kind: str, payload: dict[str, Any]) -> None:
    directory = report_dir(args, policy)
    if directory is None:
        return
    directory.mkdir(parents=True, exist_ok=True)
    (directory / REPORTS[kind]).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_inputs(args: argparse.Namespace) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    if not args.intent or not args.policy:
        raise PatchError("validation failed: --intent and --policy are required", code=2, mode="validation failed", field="arguments")
    intent_doc = load_json(Path(args.intent), "intent")
    policy_doc = load_json(Path(args.policy), "policy")
    policy = validate_policy(policy_doc)
    intents = validate_intent_doc(intent_doc)
    for item in intents:
        if item["operation"] not in policy["allowed_operations"]:
            raise PatchError("validation failed: operation not allowed", code=2, mode="validation failed", field="allowed_operations")
        rel = normalize_rel(item["target"]["target_file_guess"])
        require_path_allowed(policy, rel)
    return intent_doc, intents, policy


def success(command: str, payload: dict[str, Any], args: argparse.Namespace, policy: dict[str, Any] | None = None) -> int:
    out = {"status": "PASS", "command": command, "timestamp": now(), **payload}
    if command == "validate-intent":
        write_report(args, policy, "validation", out)
    elif command in {"apply-intent", "replace-once", "replace-heading-section", "frontmatter-set"}:
        write_report(args, policy, "success", out)
    emit(out)
    return 0


def failure(command: str, err: PatchError, args: argparse.Namespace, policy: dict[str, Any] | None = None) -> int:
    out = {
        "status": "FAIL",
        "command": command,
        "timestamp": now(),
        "failure_mode": err.mode,
        "message": str(err),
        "governing_field": err.field,
        "candidates": err.candidates,
        "rollback_status": "not_applicable",
    }
    kind = "ambiguity" if err.mode in {"zero target matches", "multiple target matches", "duplicate/ambiguous heading path"} else "failure"
    if err.mode == "validation failed":
        kind = "validation"
    write_report(args, policy, kind, out)
    emit(out)
    return err.code


def apply_intent(repo: Path, policy: dict[str, Any], intent: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    op = intent["operation"]
    if op not in MUTATION_OPS:
        raise PatchError("validation failed: apply-intent requires a mutation operation", code=2, mode="validation failed", field="operation")
    rel, path = safe_target(repo, policy, intent["target"])
    before = path.read_text(encoding="utf-8") if path.exists() else None
    try:
        if op == "replace-once":
            result = replace_once(repo, policy, intent, args)
        elif op == "replace-heading-section":
            result = replace_heading_section(repo, policy, intent, args)
        else:
            result = frontmatter_set(repo, policy, intent, args)
        validations = run_validation(repo, policy, intent, result["changed_paths"])
        diff = git_diff(repo, result["changed_paths"]) if is_git_repo(repo) else {"stdout": "", "exit_code": 0}
        return {**result, "validation_results": validations, "git_diff": diff.get("stdout", "")}
    except PatchError as exc:
        if before is not None and exc.code in {4, 5}:
            path.write_text(before, encoding="utf-8", newline="")
        raise


def command_main(command: str, args: argparse.Namespace) -> int:
    policy: dict[str, Any] | None = None
    try:
        repo = repo_root(args)
        _, intents, policy = load_inputs(args)
        intent = select_intent(intents, args, command)
        if command == "validate-intent":
            return success(command, {"intent_count": len(intents), "validated_intents": [i["intent_id"] for i in intents]}, args, policy)
        if command == "inspect":
            return success(command, {"inspection": inspect_file(repo, policy, intent)}, args, policy)
        if command == "locate":
            return success(command, {"resolved_target": locate_target(repo, policy, intent)}, args, policy)
        if command == "extract-span":
            return success(command, {"span": extract_span(repo, policy, intent)}, args, policy)
        if command == "replace-once":
            return success(command, replace_once(repo, policy, intent, args), args, policy)
        if command == "replace-heading-section":
            return success(command, replace_heading_section(repo, policy, intent, args), args, policy)
        if command == "frontmatter-set":
            return success(command, frontmatter_set(repo, policy, intent, args), args, policy)
        if command == "diff":
            rel, _ = safe_target(repo, policy, intent["target"])
            diff = git_diff(repo, [rel]) if is_git_repo(repo) else {"stdout": "", "exit_code": 0}
            return success(command, {"path": rel, "diff": diff.get("stdout", "")}, args, policy)
        if command == "apply-intent":
            return success(command, apply_intent(repo, policy, intent, args), args, policy)
        raise PatchError("validation failed: unknown command", code=2, mode="validation failed", field="command")
    except PatchError as exc:
        return failure(command, exc, args, policy)
    except Exception as exc:  # Fail closed for unexpected ambiguity or IO problems.
        return failure(command, PatchError(f"validation failed: {exc}", code=2, mode="validation failed"), args, policy)


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        doc = root / "doc.md"
        doc.write_text("# Title\n\n## Target\n\nold phrase\n", encoding="utf-8")
        intent = {
            "schema_version": "patch_intent.v1",
            "intents": [
                {
                    "intent_id": "replace_target_section",
                    "operation": "replace-heading-section",
                    "target": {"target_file_guess": "doc.md", "heading_path": ["Title", "Target"]},
                    "replacement": {"content": "new phrase"},
                    "validation": {"expected_phrases": ["new phrase"], "forbidden_phrases": ["old phrase"]},
                    "safety": {"require_unique_match": True, "fail_on_ambiguity": True, "allow_full_file_rewrite": False, "max_files_touched": 1},
                }
            ],
        }
        policy = {
            "schema_version": "patch_policy.v1",
            "path_allowlist": ["doc.md"],
            "protected_paths": [],
            "report_directory": "reports",
            "allowed_operations": ["validate-intent", "replace-heading-section", "apply-intent", "inspect", "locate", "extract-span", "diff"],
            "validation_commands": [],
            "full_file_rewrite": False,
        }
        (root / "intent.json").write_text(json.dumps(intent), encoding="utf-8")
        (root / "policy.json").write_text(json.dumps(policy), encoding="utf-8")
        args = argparse.Namespace(
            intent=str(root / "intent.json"),
            policy=str(root / "policy.json"),
            repo=str(root),
            report_dir=None,
            intent_id=None,
            allow_write=True,
        )
        code = command_main("validate-intent", args)
        if code:
            return code
        code = command_main("apply-intent", args)
        if code:
            return code
        if "new phrase" not in doc.read_text(encoding="utf-8"):
            emit({"status": "FAIL", "command": "--self-test", "message": "mutation assertion failed"})
            return 1
    emit({"status": "PASS", "command": "--self-test", "timestamp": now()})
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Deterministic Markdown patch executor")
    parser.add_argument("--self-test", action="store_true")
    sub = parser.add_subparsers(dest="command")
    for command in sorted(OPS):
        p = sub.add_parser(command)
        p.add_argument("--intent")
        p.add_argument("--policy")
        p.add_argument("--repo", default=".")
        p.add_argument("--report-dir")
        p.add_argument("--intent-id")
        p.add_argument("--allow-write", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.command:
        emit({"status": "FAIL", "command": None, "message": "command required"})
        return 2
    return command_main(args.command, args)


if __name__ == "__main__":
    sys.exit(main())
