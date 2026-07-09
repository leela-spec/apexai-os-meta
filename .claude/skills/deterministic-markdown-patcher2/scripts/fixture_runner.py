#!/usr/bin/env python3
"""Fixture runner for deterministic Markdown patcher specs."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


def now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def fail(message: str, details: Any = None) -> int:
    payload = {"status": "FAIL", "timestamp": now(), "message": message}
    if details is not None:
        payload["details"] = details
    emit(payload)
    return 1


def load_spec(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        spec = json.load(fh)
    if not isinstance(spec, dict) or spec.get("schema_version") != "fixture_spec.v1":
        raise ValueError("fixture spec schema_version must be fixture_spec.v1")
    for key in ("fixture_id", "files", "commands", "assertions"):
        if key not in spec:
            raise ValueError(f"fixture spec missing {key}")
    return spec


def safe_rel(path: str) -> Path:
    p = Path(path)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError(f"unsafe fixture path: {path}")
    return p


def create_files(root: Path, files: list[dict[str, Any]]) -> list[str]:
    written: list[str] = []
    for item in files:
        if not isinstance(item, dict) or not isinstance(item.get("path"), str) or not isinstance(item.get("content"), str):
            raise ValueError("file entries require path and content strings")
        path = root / safe_rel(item["path"])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["content"], encoding="utf-8", newline="")
        written.append(item["path"])
    return written


def seed_executor(root: Path) -> None:
    scripts = root / "scripts"
    scripts.mkdir(exist_ok=True)
    src = Path(__file__).resolve().parent / "patch_executor.py"
    if src.exists() and not (scripts / "patch_executor.py").exists():
        shutil.copy2(src, scripts / "patch_executor.py")


def run_commands(root: Path, commands: list[dict[str, Any]]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for command in commands:
        if not isinstance(command, dict):
            raise ValueError("command entries must be objects")
        argv = command.get("command")
        if not isinstance(argv, list) or not argv or not all(isinstance(v, str) and v for v in argv):
            raise ValueError("command must be a non-empty argv array")
        expected = command.get("expected_exit", 0)
        if not isinstance(expected, int):
            raise ValueError("expected_exit must be integer")
        proc = subprocess.run(argv, cwd=str(root), text=True, capture_output=True, timeout=command.get("timeout_seconds", 120), shell=False)
        result = {
            "name": command.get("name", argv[0]),
            "command": argv,
            "expected_exit": expected,
            "exit_code": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "passed": proc.returncode == expected,
        }
        results.append(result)
        if not result["passed"]:
            break
    return results


def check_assertions(root: Path, assertions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for assertion in assertions:
        if not isinstance(assertion, dict) or not isinstance(assertion.get("path"), str):
            raise ValueError("assertion entries require path")
        path = root / safe_rel(assertion["path"])
        text = path.read_text(encoding="utf-8")
        for phrase in assertion.get("must_contain", []):
            passed = isinstance(phrase, str) and phrase in text
            results.append({"path": assertion["path"], "type": "must_contain", "phrase": phrase, "passed": passed})
        for phrase in assertion.get("must_not_contain", []):
            passed = isinstance(phrase, str) and phrase not in text
            results.append({"path": assertion["path"], "type": "must_not_contain", "phrase": phrase, "passed": passed})
    return results


def run_spec(spec_path: Path) -> int:
    try:
        spec = load_spec(spec_path)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            files = create_files(root, spec["files"])
            seed_executor(root)
            command_results = run_commands(root, spec["commands"])
            commands_passed = all(r["passed"] for r in command_results)
            assertion_results = check_assertions(root, spec["assertions"]) if commands_passed else []
            assertions_passed = all(r["passed"] for r in assertion_results)
            status = "PASS" if commands_passed and assertions_passed else "FAIL"
            emit(
                {
                    "status": status,
                    "timestamp": now(),
                    "fixture_id": spec["fixture_id"],
                    "created_files": files,
                    "command_results": command_results,
                    "assertion_results": assertion_results,
                }
            )
            return 0 if status == "PASS" else 1
    except Exception as exc:
        return fail(str(exc))


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        spec = {
            "schema_version": "fixture_spec.v1",
            "fixture_id": "self_test",
            "files": [
                {"path": "docs/example.md", "content": "# Example\n\n## Current Behavior\n\nThis section describes the current behavior.\n"},
                {
                    "path": "patch_intent.json",
                    "content": json.dumps(
                        {
                            "schema_version": "patch_intent.v1",
                            "intents": [
                                {
                                    "intent_id": "replace_current_behavior",
                                    "operation": "replace-heading-section",
                                    "target": {"target_file_guess": "docs/example.md", "heading_path": ["Example", "Current Behavior"]},
                                    "replacement": {"content": "updated behavior"},
                                    "validation": {"expected_phrases": ["updated behavior"], "forbidden_phrases": ["current behavior"]},
                                    "safety": {"require_unique_match": True, "fail_on_ambiguity": True, "allow_full_file_rewrite": False, "max_files_touched": 1},
                                }
                            ],
                        }
                    ),
                },
                {
                    "path": "patch_policy.json",
                    "content": json.dumps(
                        {
                            "schema_version": "patch_policy.v1",
                            "path_allowlist": ["docs/example.md"],
                            "protected_paths": [],
                            "report_directory": "reports",
                            "allowed_operations": ["validate-intent", "replace-heading-section", "apply-intent"],
                            "validation_commands": [],
                            "full_file_rewrite": False,
                        }
                    ),
                },
            ],
            "commands": [
                {
                    "name": "validate",
                    "command": [sys.executable, "scripts/patch_executor.py", "validate-intent", "--intent", "patch_intent.json", "--policy", "patch_policy.json"],
                    "expected_exit": 0,
                },
                {
                    "name": "apply",
                    "command": [
                        sys.executable,
                        "scripts/patch_executor.py",
                        "apply-intent",
                        "--intent",
                        "patch_intent.json",
                        "--policy",
                        "patch_policy.json",
                        "--allow-write",
                    ],
                    "expected_exit": 0,
                },
            ],
            "assertions": [{"path": "docs/example.md", "must_contain": ["updated behavior"], "must_not_contain": ["current behavior"]}],
        }
        spec_path = root / "fixture.json"
        spec_path.write_text(json.dumps(spec), encoding="utf-8")
        return run_spec(spec_path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run deterministic patcher fixtures")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--spec")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.spec:
        return fail("--spec is required unless --self-test is used")
    return run_spec(Path(args.spec))


if __name__ == "__main__":
    sys.exit(main())
