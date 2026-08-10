#!/usr/bin/env python3
"""Validate and normalize a bounded APEX OpenClaw execution request.

This is the authority boundary: OpenClaw only receives a request after this
program accepts it. The contract is closed-world and stdlib-only. Unknown
fields, tools, commands, paths, or Git operations fail closed.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path
from typing import NoReturn
from urllib.parse import urlsplit


SCHEMA_VERSION = "apex.execution-request/v1"
TOP_FIELDS = frozenset(
    {
        "schema_version",
        "execution_id",
        "idempotency_key",
        "origin",
        "instruction",
        "provider",
        "prompt_ref",
        "roots",
        "grants",
        "success_criteria",
        "stop_conditions",
        "result_path",
        "evidence_dir",
    }
)
ALLOWED_TOOLS = frozenset(
    {"browser", "read", "write", "edit", "apply_patch", "exec", "process", "session_status"}
)
ALLOWED_GIT_OPERATIONS = frozenset({"status", "diff", "add", "commit", "push"})
ROOT_MODES = frozenset({"read", "read_write"})
INLINE_TOKENS = frozenset(
    {"-c", "/c", "-command", "-encodedcommand", "--eval", "-e", "--execute"}
)
INTERPRETER_EXECUTABLES = frozenset(
    {"bash", "cmd", "cscript", "node", "powershell", "pwsh", "python", "python3", "sh", "wscript"}
)
REVIEWED_COMMAND_IDENTITIES = frozenset(
    {
        # Windows 11 2026-08-10: C:\Windows\System32\where.exe
        "f51fab8041e5023d7290b540a2106f051ef0bd2bc3443c9daf318628b560fa29",
    }
)
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$")
HASH_RE = re.compile(r"^[0-9a-fA-F]{64}$")
RESERVED_NAMES = frozenset(
    {"CON", "PRN", "AUX", "NUL"}
    | {f"COM{i}" for i in range(1, 10)}
    | {f"LPT{i}" for i in range(1, 10)}
)


class RequestError(Exception):
    def __init__(self, code: str, detail: str):
        super().__init__(detail)
        self.code = code
        self.detail = detail


def fail(code: str, detail: str) -> NoReturn:
    raise RequestError(code, detail)


def require_object(value: object, code: str, name: str) -> dict:
    if not isinstance(value, dict):
        fail(code, f"{name} must be an object")
    return value


def exact_fields(value: dict, allowed: set[str] | frozenset[str], code: str, name: str) -> None:
    unknown = sorted(set(value) - set(allowed))
    if unknown:
        fail(code, f"unknown {name} fields: {unknown}")


def require_text(value: object, code: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(code, f"{name} must be a non-empty string")
    return value


def safe_path(raw: object, code: str, name: str, *, must_exist: bool = False) -> Path:
    text = require_text(raw, code, name)
    if "\x00" in text or "*" in text or "?" in text:
        fail(code, f"{name} contains a prohibited character")
    if text.startswith(("\\\\", "//", "\\\\?\\", "\\\\.\\")):
        fail(code, f"{name} uses a UNC or device path")
    colon_positions = [index for index, char in enumerate(text) if char == ":"]
    if any(index != 1 for index in colon_positions):
        fail(code, f"{name} uses an alternate data stream")
    for component in re.split(r"[\\/]", text):
        if not component or component in {".", ".."}:
            continue
        if component != component.rstrip(" ."):
            fail(code, f"{name} has a trailing dot or space")
        if component.split(".", 1)[0].upper() in RESERVED_NAMES:
            fail(code, f"{name} contains a reserved Windows name")
        if re.fullmatch(r"[A-Za-z0-9_-]{1,6}~\d+", component):
            fail(code, f"{name} contains an 8.3 short name")
    candidate = Path(text)
    if not candidate.is_absolute():
        fail(code, f"{name} must be absolute")
    try:
        resolved = candidate.resolve(strict=must_exist)
    except OSError as exc:
        fail(code, f"{name} cannot be resolved: {exc}")
    return resolved


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_hash(raw: object, code: str, name: str) -> str:
    value = require_text(raw, code, name)
    if not HASH_RE.fullmatch(value):
        fail(code, f"{name} must be 64 hexadecimal characters")
    return value.lower()


def reject_reparse_chain(raw: object, code: str, name: str) -> None:
    path = Path(require_text(raw, code, name))
    for candidate in (path, *path.parents):
        try:
            attributes = os.lstat(candidate).st_file_attributes
        except AttributeError:
            return
        except FileNotFoundError:
            continue
        except OSError as exc:
            fail(code, f"{name} reparse inspection failed: {exc}")
        if attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
            fail(code, f"{name} traverses a reparse point: {candidate}")


def is_within(path: Path, root: Path) -> bool:
    try:
        return os.path.commonpath((os.path.normcase(path), os.path.normcase(root))) == os.path.normcase(root)
    except ValueError:
        return False


def containing_root(path: Path, roots: list[dict], *, writable: bool) -> dict | None:
    candidates = [root for root in roots if is_within(path, Path(root["path"]))]
    candidates.sort(key=lambda root: len(Path(root["path"]).parts), reverse=True)
    if not candidates:
        return None
    selected = candidates[0]
    if writable and selected["mode"] != "read_write":
        fail("WRITE_REQUIRES_READ_WRITE", f"write path is under a read-only root: {path}")
    return selected


def nonempty_text_list(value: object, code: str, name: str) -> list[str]:
    if not isinstance(value, list) or not value:
        fail(code, f"{name} must be a non-empty list")
    result = []
    for item in value:
        result.append(require_text(item, code, name))
    return result


def validate(raw: object) -> dict:
    request = require_object(raw, "REQUEST_TYPE", "request")
    exact_fields(request, TOP_FIELDS, "UNKNOWN_FIELD", "top-level")
    missing = sorted(TOP_FIELDS - set(request))
    if missing:
        fail("MISSING_FIELD", f"missing required fields: {missing}")
    if request["schema_version"] != SCHEMA_VERSION:
        fail("SCHEMA_VERSION", f"expected {SCHEMA_VERSION}")

    execution_id = require_text(request["execution_id"], "EXECUTION_ID", "execution_id")
    idempotency_key = require_text(request["idempotency_key"], "IDEMPOTENCY_KEY", "idempotency_key")
    if not ID_RE.fullmatch(execution_id):
        fail("EXECUTION_ID", "execution_id has invalid characters or length")
    if not ID_RE.fullmatch(idempotency_key):
        fail("IDEMPOTENCY_KEY", "idempotency_key has invalid characters or length")

    origin = require_object(request["origin"], "ORIGIN", "origin")
    exact_fields(origin, {"repo", "workflow", "step"}, "ORIGIN", "origin")
    if set(origin) != {"repo", "workflow", "step"}:
        fail("ORIGIN", "origin requires repo, workflow, and step")
    normalized_origin = {
        "repo": str(safe_path(origin["repo"], "ORIGIN", "origin.repo", must_exist=True)),
        "workflow": require_text(origin["workflow"], "ORIGIN", "origin.workflow"),
        "step": require_text(origin["step"], "ORIGIN", "origin.step"),
    }

    roots_raw = request["roots"]
    if not isinstance(roots_raw, list) or not roots_raw:
        fail("ROOTS", "roots must be a non-empty list")
    roots: list[dict] = []
    for index, root_raw in enumerate(roots_raw):
        root = require_object(root_raw, "ROOTS", f"roots[{index}]")
        exact_fields(root, {"path", "mode"}, "ROOTS", f"roots[{index}]")
        mode = root.get("mode")
        if mode not in ROOT_MODES:
            fail("ROOT_MODE", f"roots[{index}].mode must be read or read_write")
        reject_reparse_chain(root.get("path"), "ROOT_REPARSE", f"roots[{index}].path")
        root_path = safe_path(root.get("path"), "ROOT_PATH", f"roots[{index}].path", must_exist=True)
        roots.append({"path": str(root_path), "mode": mode})
    normalized_root_paths = [os.path.normcase(root["path"]) for root in roots]
    if len(normalized_root_paths) != len(set(normalized_root_paths)):
        fail("ROOTS", "duplicate roots are not permitted")

    prompt_ref = require_object(request["prompt_ref"], "PROMPT_REF", "prompt_ref")
    exact_fields(prompt_ref, {"path", "sha256"}, "PROMPT_REF", "prompt_ref")
    reject_reparse_chain(prompt_ref.get("path"), "PROMPT_REPARSE", "prompt_ref.path")
    prompt_path = safe_path(prompt_ref.get("path"), "PROMPT_REF", "prompt_ref.path", must_exist=True)
    if containing_root(prompt_path, roots, writable=False) is None:
        fail("PATH_OUTSIDE_ROOTS", f"prompt path is outside declared roots: {prompt_path}")
    expected_hash = require_text(prompt_ref.get("sha256"), "PROMPT_HASH", "prompt_ref.sha256")
    if not HASH_RE.fullmatch(expected_hash):
        fail("PROMPT_HASH", "prompt_ref.sha256 must be 64 hexadecimal characters")
    actual_hash = sha256_file(prompt_path)
    if actual_hash.lower() != expected_hash.lower():
        fail("PROMPT_HASH", "prompt bytes do not match prompt_ref.sha256")

    reject_reparse_chain(request["result_path"], "RESULT_REPARSE", "result_path")
    reject_reparse_chain(request["evidence_dir"], "EVIDENCE_REPARSE", "evidence_dir")
    result_path = safe_path(request["result_path"], "RESULT_PATH", "result_path")
    evidence_dir = safe_path(request["evidence_dir"], "EVIDENCE_PATH", "evidence_dir")
    for path in (result_path, evidence_dir):
        if containing_root(path, roots, writable=True) is None:
            fail("PATH_OUTSIDE_ROOTS", f"write path is outside declared roots: {path}")

    grants = require_object(request["grants"], "GRANTS", "grants")
    exact_fields(grants, {"tools", "scripts", "commands", "git"}, "GRANTS", "grants")
    if set(grants) != {"tools", "scripts", "commands", "git"}:
        fail("GRANTS", "grants requires tools, scripts, commands, and git")
    tools = grants["tools"]
    if not isinstance(tools, list) or any(not isinstance(tool, str) for tool in tools):
        fail("TOOLS", "grants.tools must be a string list")
    unknown_tools = sorted(set(tools) - ALLOWED_TOOLS)
    if unknown_tools:
        fail("UNKNOWN_TOOL", f"unknown tools: {unknown_tools}")
    if len(tools) != len(set(tools)):
        fail("TOOLS", "grants.tools contains duplicates")

    scripts_raw = grants["scripts"]
    if not isinstance(scripts_raw, list):
        fail("SCRIPTS", "grants.scripts must be a list")
    if scripts_raw and "exec" not in tools:
        fail("SCRIPTS", "script grants require the exec tool grant")
    scripts: list[dict] = []
    script_ids: set[str] = set()
    for index, script_raw in enumerate(scripts_raw):
        script = require_object(script_raw, "SCRIPTS", f"scripts[{index}]")
        script_fields = {"id", "executable", "executable_sha256", "path", "sha256", "argv"}
        exact_fields(script, script_fields, "SCRIPTS", f"scripts[{index}]")
        if set(script) != script_fields:
            fail("SCRIPTS", f"scripts[{index}] lacks required fields")
        script_id = require_text(script["id"], "SCRIPTS", f"scripts[{index}].id")
        if script_id in script_ids:
            fail("SCRIPTS", f"duplicate script id: {script_id}")
        script_ids.add(script_id)
        reject_reparse_chain(script["executable"], "EXECUTABLE_REPARSE", f"scripts[{index}].executable")
        reject_reparse_chain(script["path"], "SCRIPT_REPARSE", f"scripts[{index}].path")
        executable = safe_path(script["executable"], "EXECUTABLE", f"scripts[{index}].executable", must_exist=True)
        script_path = safe_path(script["path"], "SCRIPT_PATH", f"scripts[{index}].path", must_exist=True)
        script_root = containing_root(script_path, roots, writable=False)
        if script_root is None:
            fail("PATH_OUTSIDE_ROOTS", f"script is outside declared roots: {script_path}")
        if script_root["mode"] != "read":
            fail("SCRIPT_ROOT_MODE", f"script must be under a read-only root: {script_path}")
        executable_hash = require_hash(
            script["executable_sha256"], "EXECUTABLE_HASH", f"scripts[{index}].executable_sha256"
        )
        script_hash = require_hash(script["sha256"], "SCRIPT_HASH", f"scripts[{index}].sha256")
        if sha256_file(executable) != executable_hash:
            fail("EXECUTABLE_HASH", f"executable identity mismatch: {executable}")
        if sha256_file(script_path) != script_hash:
            fail("SCRIPT_HASH", f"script identity mismatch: {script_path}")
        argv = script["argv"]
        if not isinstance(argv, list) or any(not isinstance(arg, str) for arg in argv):
            fail("SCRIPT_ARGV", f"scripts[{index}].argv must be a string list")
        if any(arg.casefold() in INLINE_TOKENS for arg in argv):
            fail("INLINE_EXECUTION", f"scripts[{index}].argv contains inline execution")
        scripts.append(
            {
                "id": script_id,
                "executable": str(executable),
                "executable_sha256": executable_hash,
                "path": str(script_path),
                "sha256": script_hash,
                "argv": argv,
            }
        )

    commands_raw = grants["commands"]
    if not isinstance(commands_raw, list):
        fail("COMMANDS", "grants.commands must be a list")
    if commands_raw and "exec" not in tools:
        fail("COMMANDS", "command grants require the exec tool grant")
    commands: list[dict] = []
    command_ids: set[str] = set()
    for index, command_raw in enumerate(commands_raw):
        command = require_object(command_raw, "COMMANDS", f"commands[{index}]")
        command_fields = {"id", "executable", "executable_sha256", "argv"}
        exact_fields(command, command_fields, "COMMANDS", f"commands[{index}]")
        if set(command) != command_fields:
            fail("COMMANDS", f"commands[{index}] lacks required fields")
        command_id = require_text(command["id"], "COMMANDS", f"commands[{index}].id")
        if command_id in command_ids:
            fail("COMMANDS", f"duplicate command id: {command_id}")
        command_ids.add(command_id)
        reject_reparse_chain(command["executable"], "EXECUTABLE_REPARSE", f"commands[{index}].executable")
        executable = safe_path(command["executable"], "EXECUTABLE", f"commands[{index}].executable", must_exist=True)
        executable_hash = require_hash(
            command["executable_sha256"], "EXECUTABLE_HASH", f"commands[{index}].executable_sha256"
        )
        if sha256_file(executable) != executable_hash:
            fail("EXECUTABLE_HASH", f"executable identity mismatch: {executable}")
        argv = command["argv"]
        if not isinstance(argv, list) or any(not isinstance(arg, str) for arg in argv):
            fail("COMMAND_ARGV", f"commands[{index}].argv must be a string list")
        if executable.stem.casefold() in INTERPRETER_EXECUTABLES:
            fail("COMMAND_INTERPRETER", f"interpreter is prohibited as an exact command: {executable.name}")
        if executable_hash not in REVIEWED_COMMAND_IDENTITIES:
            fail("COMMAND_IDENTITY", f"command executable identity is not reviewed: {executable}")
        if any(arg.casefold() in INLINE_TOKENS for arg in argv):
            fail("INLINE_EXECUTION", f"commands[{index}].argv contains inline execution")
        commands.append(
            {"id": command_id, "executable": str(executable), "executable_sha256": executable_hash, "argv": argv}
        )

    git_raw = grants["git"]
    git_grant = require_object(git_raw, "GIT", "grants.git")
    git_fields = {"repo", "remote", "remote_url", "branch", "operations", "add_paths", "commit_message"}
    exact_fields(git_grant, git_fields, "GIT", "grants.git")
    if set(git_grant) != git_fields:
        fail("GIT", "grants.git lacks required fields")
    git_repo = safe_path(git_grant["repo"], "GIT_REPO", "grants.git.repo", must_exist=True)
    if git_grant["remote"] != "origin":
        fail("GIT_REMOTE", "only remote origin is permitted")
    remote_url = require_text(git_grant["remote_url"], "GIT_REMOTE", "grants.git.remote_url")
    if Path(remote_url).is_absolute():
        remote_url = str(safe_path(remote_url, "GIT_REMOTE", "grants.git.remote_url", must_exist=True))
    else:
        parsed_remote = urlsplit(remote_url)
        if (
            parsed_remote.scheme != "https"
            or parsed_remote.hostname != "github.com"
            or parsed_remote.username is not None
            or parsed_remote.password is not None
            or parsed_remote.query
            or parsed_remote.fragment
            or not parsed_remote.path.endswith(".git")
        ):
            fail("GIT_REMOTE", "remote_url must be a local absolute path or credential-free GitHub HTTPS URL")
    if git_grant["branch"] != "main":
        fail("GIT_BRANCH", "only branch main is permitted")
    operations = git_grant["operations"]
    if not isinstance(operations, list) or any(not isinstance(op, str) for op in operations):
        fail("GIT_OPERATION", "grants.git.operations must be a string list")
    if set(operations) - ALLOWED_GIT_OPERATIONS:
        fail("GIT_OPERATION", "grants.git.operations contains a prohibited operation")
    if len(operations) != len(set(operations)):
        fail("GIT_OPERATION", "grants.git.operations contains duplicates")
    git_root = containing_root(git_repo, roots, writable=False)
    if git_root is None:
        fail("PATH_OUTSIDE_ROOTS", f"Git repo is outside declared roots: {git_repo}")
    if set(operations) & {"add", "commit", "push"} and git_root["mode"] != "read_write":
        fail("WRITE_REQUIRES_READ_WRITE", "mutating Git operations require a read_write repo root")
    add_paths_raw = git_grant["add_paths"]
    if not isinstance(add_paths_raw, list):
        fail("GIT_ADD_PATH", "grants.git.add_paths must be a list")
    add_paths = []
    for index, raw_path in enumerate(add_paths_raw):
        add_path = safe_path(raw_path, "GIT_ADD_PATH", f"grants.git.add_paths[{index}]")
        if not is_within(add_path, git_repo):
            fail("GIT_ADD_PATH", f"Git add path escapes repo: {add_path}")
        add_paths.append(str(add_path))
    commit_message_raw = git_grant["commit_message"]
    if commit_message_raw is not None and (
        not isinstance(commit_message_raw, str) or not commit_message_raw.strip()
    ):
        fail("GIT_COMMIT_MESSAGE", "grants.git.commit_message must be null or non-empty text")
    if "commit" in operations and commit_message_raw is None:
        fail("GIT_COMMIT_MESSAGE", "commit operation requires an exact commit_message")

    success_criteria = nonempty_text_list(request["success_criteria"], "SUCCESS_CRITERIA", "success_criteria")
    stop_conditions = nonempty_text_list(request["stop_conditions"], "STOP_CONDITIONS", "stop_conditions")

    return {
        "schema_version": SCHEMA_VERSION,
        "execution_id": execution_id,
        "idempotency_key": idempotency_key,
        "origin": normalized_origin,
        "instruction": require_text(request["instruction"], "INSTRUCTION", "instruction"),
        "provider": require_text(request["provider"], "PROVIDER", "provider"),
        "prompt_ref": {"path": str(prompt_path), "sha256": actual_hash},
        "roots": roots,
        "grants": {
            "tools": tools,
            "scripts": scripts,
            "commands": commands,
            "git": {
                "repo": str(git_repo),
                "remote": "origin",
                "remote_url": remote_url,
                "branch": "main",
                "operations": operations,
                "add_paths": add_paths,
                "commit_message": commit_message_raw,
            },
        },
        "success_criteria": success_criteria,
        "stop_conditions": stop_conditions,
        "result_path": str(result_path),
        "evidence_dir": str(evidence_dir),
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(json.dumps({"valid": False, "code": "USAGE", "detail": "expected one request path"}))
        return 2
    try:
        request_path = safe_path(argv[1], "REQUEST_PATH", "request path", must_exist=True)
        raw = json.loads(request_path.read_text(encoding="utf-8-sig"))
        normalized = validate(raw)
    except RequestError as exc:
        print(json.dumps({"valid": False, "code": exc.code, "detail": exc.detail}, sort_keys=True))
        return 2
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "code": "REQUEST_READ", "detail": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps({"valid": True, "request": normalized}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
