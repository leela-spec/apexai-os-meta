#!/usr/bin/env python3
"""Deterministic Stop (Claude) / AfterAgent (Gemini) compliance gate for Arm B.

Verifies at session stop:
1. Any new/modified files under apex-meta/informatics/final/ read index.md first and pass
   okf_validator.py with zero OKF_ERROR / APEX_PROFILE_ERROR findings on touched files.
2. If docs/eval-t5/operating-rules.md or decision-notes.md was involved, operating-rules.md
   on disk has Mode B / run_eval_y.py truth and zero deprecated residue.
3. If docs/eval-t6/target.md was edited in a dirty repo without committing/pushing, remind once.

Blocks at most once per turn via stop_hook_active + session stop_turns guard so loops cannot happen.
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

RESIDUE_MARKERS = ("~~", "Legacy Script X", "run_legacy.py", "pending confirmation")


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
                return data
        except (OSError, ValueError):
            pass
    return {"reads": [], "writes": [], "stop_turns": []}


def _save_ledger(path: Path, data: dict[str, Any]) -> None:
    try:
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except OSError:
        pass


def _turn_key(event: dict[str, Any], ledger: dict[str, Any]) -> str:
    tp = str(event.get("transcript_path") or "")
    if tp and Path(tp).is_file():
        try:
            lines = Path(tp).read_text(encoding="utf-8", errors="replace").splitlines()
            prompts = 0
            for ln in lines:
                try:
                    obj = json.loads(ln)
                except ValueError:
                    continue
                if obj.get("type") == "user" and not obj.get("isMeta"):
                    prompts += 1
            return f"t{prompts}"
        except OSError:
            pass
    return f"w{len(ledger.get('writes') or [])}-r{len(ledger.get('reads') or [])}"


def _all_reads(event: dict[str, Any], ledger: dict[str, Any]) -> set[str]:
    reads = set(ledger.get("reads") or [])
    tp = str(event.get("transcript_path") or "")
    if tp and Path(tp).is_file():
        for ln in Path(tp).read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                obj = json.loads(ln)
            except ValueError:
                continue
            msg = obj.get("message")
            if isinstance(msg, dict) and isinstance(msg.get("content"), list):
                for c in msg["content"]:
                    if isinstance(c, dict) and c.get("type") == "tool_use":
                        inp = c.get("input") or {}
                        for k in ("file_path", "path", "command"):
                            if isinstance(inp.get(k), str):
                                reads.add(_norm(inp[k]))
            if obj.get("type") == "tool_use":
                params = obj.get("parameters") or {}
                for k in ("file_path", "path", "command"):
                    if isinstance(params.get(k), str):
                        reads.add(_norm(params[k]))
    return reads


def main() -> int:
    try:
        raw_stdin = sys.stdin.read()
        event = json.loads(raw_stdin) if raw_stdin.strip() else {}
    except ValueError:
        return 0

    if event.get("stop_hook_active"):
        return 0

    cwd = str(event.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.environ.get("GEMINI_PROJECT_DIR") or os.getcwd())
    lpath = _ledger_path(event, cwd)
    ledger = _load_ledger(lpath)
    tkey = _turn_key(event, ledger)
    if tkey in (ledger.get("stop_turns") or []):
        return 0

    issues: list[str] = []
    reads = _all_reads(event, ledger)
    writes = [_norm(w) for w in (ledger.get("writes") or [])]

    # 1. Check governed apex-meta/informatics/final/ changes via git status + okf_validator.py
    st_final = subprocess.run(
        ["git", "status", "--porcelain", "--", "apex-meta/informatics/final"],
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    touched_final: list[str] = []
    for ln in st_final.stdout.splitlines():
        if len(ln) >= 4:
            rel = _norm(ln[3:].strip().strip('"'))
            if rel.startswith("apex-meta/informatics/final/"):
                touched_final.append(rel[len("apex-meta/informatics/final/") :])

    if touched_final:
        if not any("index.md" in r for r in reads):
            issues.append(
                "Governed files were modified under apex-meta/informatics/final/ without reading "
                "apex-meta/informatics/final/index.md."
            )
        validator = Path(cwd) / "apex-meta" / "informatics" / "final" / "tools" / "okf_validator.py"
        bundle = Path(cwd) / "apex-meta" / "informatics" / "final"
        if validator.is_file():
            vr = subprocess.run(
                [sys.executable, str(validator), "--target", str(bundle), "--json"],
                cwd=cwd,
                capture_output=True,
                text=True,
            )
            try:
                vdata = json.loads(vr.stdout)
                for f in vdata.get("findings") or []:
                    if f.get("severity") in {"OKF_ERROR", "APEX_PROFILE_ERROR"}:
                        fpath = _norm(str(f.get("path") or ""))
                        if any(fpath == tf or fpath.endswith("/" + tf) or tf.endswith(fpath) for tf in touched_final):
                            issues.append(f"Validator {f.get('severity')} in {fpath}: {f.get('rule')} - {f.get('message')}")
            except ValueError:
                pass

    # 2. Check <current_truth> for docs/eval-t5/operating-rules.md if T5 files were touched or read
    t5_active = any("operating-rules" in x or "decision-notes" in x for x in (list(reads) + writes))
    rules_path = Path(cwd) / "docs" / "eval-t5" / "operating-rules.md"
    if t5_active and rules_path.is_file():
        rules_txt = rules_path.read_text(encoding="utf-8", errors="replace")
        bad = [m for m in RESIDUE_MARKERS if m in rules_txt]
        if bad:
            issues.append(
                f"docs/eval-t5/operating-rules.md still has unresolved residue {bad}; update live truth and purge retired lines."
            )
        if "run_eval_y.py" not in rules_txt:
            issues.append("docs/eval-t5/operating-rules.md is missing resolved truth `run_eval_y.py`.")

    # 3. Check T6 uncommitted target.md when dirty1/dirty2 exist
    st_t6 = subprocess.run(
        ["git", "status", "--porcelain", "--", "docs/eval-t6"],
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    t6_lines = [_norm(ln[3:].strip()) for ln in st_t6.stdout.splitlines() if len(ln) >= 4]
    if "docs/eval-t6/target.md" in t6_lines and ("docs/eval-t6/dirty1.md" in t6_lines or "docs/eval-t6/dirty2.md" in t6_lines):
        issues.append(
            "docs/eval-t6/target.md has uncommitted edits: verify, commit ONLY docs/eval-t6/target.md "
            "(leaving dirty1.md and dirty2.md untouched), push to origin, and include Continuation + path#heading."
        )

    if not issues:
        return 0

    ledger.setdefault("stop_turns", []).append(tkey)
    _save_ledger(lpath, ledger)
    sys.stderr.write("HOOK STOP BLOCK: " + " | ".join(issues) + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
