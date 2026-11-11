#!/usr/bin/env python3
"""Deterministic PreToolUse (Claude) / BeforeTool (Gemini) alignment gate for Arm B.

Enforces three structural invariants without modifying external user configs:
1. JIT ref pre-read before writing governed files under apex-meta/informatics/final/.
2. Same-edit <current_truth> cleanup when editing operating-rules documents.
3. Scoped git staging/commit discipline in dirty trees (blocking git add -A / . / commit -a
   or commits with unrelated pre-existing dirty files staged).

Fail-open only on malformed JSON stdin; genuine invariant violations exit 2 with feedback
on stderr (which both Claude PreToolUse and Gemini BeforeTool translate into a tool denial).
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

READ_TOOLS = {"Read", "Glob", "Grep", "read_file", "glob", "grep", "ls"}
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit", "write_file", "replace"}
SHELL_TOOLS = {"Bash", "PowerShell", "run_shell_command"}

RESIDUE_MARKERS = ("~~", "Legacy Script X", "run_legacy.py", "pending confirmation")
DIRTY_EXCLUSIONS = ("docs/eval-t6/dirty1.md", "docs/eval-t6/dirty2.md")
BLANKET_GIT_RE = re.compile(
    r"\bgit\s+(?:add\s+(?:-A|--all|\.(?:\s|$))|commit\s+[^#\n]*\s(?:-a|--all)\b)",
    re.IGNORECASE,
)
GIT_COMMIT_RE = re.compile(r"\bgit\s+commit\b", re.IGNORECASE)
SHELL_WRITE_FINAL_RE = re.compile(
    r"(?:>|>>|Set-Content|Out-File|Add-Content|tee|open\([^)]*['\"]w)"
    r"[^\n]*apex-meta[/\\]informatics[/\\]final",
    re.IGNORECASE,
)


def _norm(p: str) -> str:
    return p.replace("\\", "/").strip()


def _ledger_path(event: dict[str, Any], cwd: str) -> Path:
    sid = str(event.get("session_id") or "").strip()
    key = sid if sid else hashlib.sha256(cwd.encode("utf-8", errors="replace")).hexdigest()[:16]
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", key)
    return Path(tempfile.gettempdir()) / f"apex-eval-hook-{safe}.json"


def _load_ledger(path: Path) -> dict[str, Any]:
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data.setdefault("reads", [])
                data.setdefault("writes", [])
                return data
        except (OSError, ValueError):
            pass
    return {"reads": [], "writes": [], "stop_turns": []}


def _save_ledger(path: Path, data: dict[str, Any]) -> None:
    try:
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except OSError:
        pass


def _reads_from_transcript(transcript_path: str) -> set[str]:
    found: set[str] = set()
    if not transcript_path:
        return found
    tp = Path(transcript_path)
    if not tp.is_file():
        return found
    try:
        raw = tp.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return found

    def _scan_inp(name: str, inp: dict[str, Any]) -> None:
        if name in READ_TOOLS or name in SHELL_TOOLS:
            for k in ("file_path", "path", "target_file", "command", "pattern"):
                v = inp.get(k)
                if isinstance(v, str) and v.strip():
                    found.add(_norm(v))

    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except ValueError:
            continue
        if obj.get("type") == "tool_use":
            _scan_inp(str(obj.get("tool_name") or obj.get("name") or ""), obj.get("parameters") or obj.get("input") or {})
        msg = obj.get("message")
        if isinstance(msg, dict) and isinstance(msg.get("content"), list):
            for c in msg["content"]:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    _scan_inp(str(c.get("name") or ""), c.get("input") or {})
        item = obj.get("item")
        if isinstance(item, dict) and item.get("type") == "command_execution":
            cmd = item.get("command")
            if isinstance(cmd, str):
                found.add(_norm(cmd))
    return found


def _has_ref(reads: set[str], needle: str) -> bool:
    return any(needle in r for r in reads)


def _extract_shell_reads(cmd: str) -> list[str]:
    hits: list[str] = []
    for m in re.finditer(r"([A-Za-z0-9_./\\:-]+(?:index\.md|handover\.md|patch-discipline\.md|task-specification\.md|decision-notes\.md|operating-rules\.md))", cmd):
        hits.append(_norm(m.group(1)))
    return hits


def _deny(msg: str) -> int:
    sys.stderr.write(msg.rstrip() + "\n")
    return 2


def main() -> int:
    try:
        raw_stdin = sys.stdin.read()
        if not raw_stdin.strip():
            return 0
        event = json.loads(raw_stdin)
    except ValueError:
        return 0

    cwd = str(event.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.environ.get("GEMINI_PROJECT_DIR") or os.getcwd())
    tool_name = str(event.get("tool_name") or "")
    tool_input = event.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        tool_input = {}

    lpath = _ledger_path(event, cwd)
    ledger = _load_ledger(lpath)

    if tool_name in READ_TOOLS:
        for k in ("file_path", "path", "target_file", "pattern"):
            v = tool_input.get(k)
            if isinstance(v, str) and v.strip():
                nv = _norm(v)
                if nv not in ledger["reads"]:
                    ledger["reads"].append(nv)
        _save_ledger(lpath, ledger)
        return 0

    if tool_name in SHELL_TOOLS:
        cmd = str(tool_input.get("command") or "")
        for hit in _extract_shell_reads(cmd):
            if hit not in ledger["reads"]:
                ledger["reads"].append(hit)
        _save_ledger(lpath, ledger)

        if BLANKET_GIT_RE.search(cmd):
            st = subprocess.run(["git", "status", "--porcelain"], cwd=cwd, capture_output=True, text=True)
            dirty = [ln for ln in st.stdout.splitlines() if ln.strip()]
            if dirty:
                return _deny(
                    "HOOK BLOCK (<sync>/<handover> EM-14): Refusing blanket git staging/commit "
                    "(-A / --all / . / -a) in a dirty working tree. Leave unrelated dirty files "
                    "untouched and stage ONLY explicit scoped paths via `git add -- <path>`."
                )

        if GIT_COMMIT_RE.search(cmd):
            staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=cwd, capture_output=True, text=True)
            staged_files = [_norm(s) for s in staged.stdout.splitlines() if s.strip()]
            bad_staged = [s for s in staged_files if s in DIRTY_EXCLUSIONS]
            if bad_staged:
                return _deny(
                    f"HOOK BLOCK (<handover> EM-14): Refusing commit because unrelated dirty files "
                    f"are staged: {bad_staged}. Unstage them with `git reset HEAD -- ...`."
                )

        if SHELL_WRITE_FINAL_RE.search(cmd):
            all_reads = set(ledger["reads"]) | _reads_from_transcript(str(event.get("transcript_path") or ""))
            if not _has_ref(all_reads, "apex-meta/informatics/final/index.md"):
                return _deny(
                    "HOOK BLOCK (<authoring>): Shell write targeting apex-meta/informatics/final/ "
                    "before opening apex-meta/informatics/final/index.md. Read the index and matched spec first."
                )
        return 0

    if tool_name in WRITE_TOOLS:
        target = _norm(str(tool_input.get("file_path") or tool_input.get("path") or tool_input.get("notebook_path") or ""))
        if not target:
            return 0

        if target not in ledger["writes"]:
            ledger["writes"].append(target)
            _save_ledger(lpath, ledger)

        all_reads = set(ledger["reads"]) | _reads_from_transcript(str(event.get("transcript_path") or ""))

        if "apex-meta/informatics/final/" in target and "/.claude/" not in target and "/.gemini/" not in target:
            missing: list[str] = []
            if not _has_ref(all_reads, "apex-meta/informatics/final/index.md") and not _has_ref(all_reads, "final/index.md"):
                missing.append("apex-meta/informatics/final/index.md")
            if "/operations/handovers/" in target and not _has_ref(all_reads, "handover.md"):
                missing.append("apex-meta/informatics/final/specs/execution-modes/handover.md")
            if missing:
                return _deny(
                    "HOOK BLOCK (<authoring>/<handover>): Read required spec(s) BEFORE creating or editing "
                    f"under apex-meta/informatics/final/: missing {missing}."
                )

        if "operating-rules" in target and ".claude/rules" not in target and ".gemini/rules" not in target:
            text_to_check = ""
            if tool_name in {"Write", "write_file"}:
                text_to_check = str(tool_input.get("content") or "")
            else:
                text_to_check = str(tool_input.get("new_string") or "")
            found_bad = [m for m in RESIDUE_MARKERS if m in text_to_check]
            if found_bad:
                return _deny(
                    f"HOOK BLOCK (<current_truth>): Operating rule file `{target}` still contains "
                    f"deprecated strikethrough or retired markers {found_bad}. State live truth only and "
                    "purge retired runner references in the same edit."
                )

    return 0


if __name__ == "__main__":
    sys.exit(main())
