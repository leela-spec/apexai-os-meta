#!/usr/bin/env python3
"""Deterministic transcript, git-state, and OKF validator scorer for EVAL-APEX-ULTRA-V1-UPGRADE.

Parses raw JSONL logs from:
- Claude Code (`assistant.message.content[].tool_use`, `system.hook_*`, `result`)
- Gemini CLI (`tool_use`, `tool_result`, `message`, `result`)
- Codex CLI (`item.completed` command_execution / agent_message, `turn.completed`)

Zero LLM-judged grading and zero reliance on agent self-reports.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

KNOWN_CLAUDE_TOOLS = {
    "Read", "Write", "Edit", "MultiEdit", "NotebookEdit", "Bash", "PowerShell", "Glob", "Grep",
    "Task", "TodoWrite", "WebFetch", "WebSearch", "ToolSearch",
}
KNOWN_GEMINI_TOOLS = {
    "read_file", "read_many_files", "write_file", "replace",
    "run_shell_command", "glob", "grep_search", "list_directory",
    "google_web_search", "web_fetch",
}
KNOWN_CODEX_ITEMS = {"command_execution", "agent_message", "reasoning", "file_change", "mcp_tool_call"}

READ_TOOL_NAMES = {
    "Read", "Glob", "Grep",
    "read_file", "read_many_files", "glob", "grep_search", "list_directory",
}
WRITE_TOOL_NAMES = {"Write", "Edit", "MultiEdit", "NotebookEdit", "write_file", "replace"}
SHELL_TOOL_NAMES = {"Bash", "PowerShell", "run_shell_command", "command_execution"}

SHELL_CLAUSE_SPLIT_RE = re.compile(r"\r?\n|&&|\|\||;|\|")
BENIGN_REDIR_RE = re.compile(r"(?:^|\s)[12]?>&\s*[12](?=\s|$)|(?:^|\s)[12]?>>?\s*(?:/dev/null|\$null)\b", re.IGNORECASE)
PS_READ_RE = re.compile(
    r"\b(?:Get-Content|gc|cat|type|Select-String|sls|head|tail|more|less|sed|awk|rg|grep|okf_validator)\b"
    r"|\bgit\s+diff(?!\s+--(?:name-only|stat)\b)"
    r"|\bgit\s+show\s+(?!--(?:stat|name-only|oneline)\b)\S*:\S+"
    r"|open\(|read_text\(",
    re.IGNORECASE,
)
PS_WRITE_RE = re.compile(r"\b(?:Set-Content|Out-File|Add-Content|sc|ac|Copy-Item|Move-Item|cpi|mvi)\b|>>?(?!&)", re.IGNORECASE)
def _field_pat(name: str) -> re.Pattern[str]:
    return re.compile(
        rf"(?:^|\n)\s*(?:#{{1,4}}\s+|(?:\d+\.\s*|[-*]\s+)?\*\*)(?:\d+\.\s*)?(?:L0.?L3\s+)?{name}(?:[^\n:*]{{0,100}})(?:\*\*)?(?:\s*\([^\n)]{{1,100}}\))?\s*(?:\*\*)?(?::|—|-|\s*(?:\r?\n|$))",
        re.IGNORECASE,
    )


ALIGN_FIELD_PATTERNS = {
    k: _field_pat(k) for k in ("Goal", "Input", "Process", "Skills", "Output", "Redraft")
}
FRAMEWORK_HINT_RE = re.compile(
    r"\b(?:OODA|FMEA|Cynefin|First Principles|Pre-Mortem|Premortem|Root Cause|5[- ]Whys|MECE|Pugh|Bayesian|(?:Trade-?off|Weighted|Decision)\s*(?:Matrix|Analysis|Table)|Verification-First|Sequencing & Architecture|Critical Path|Macro-Meso-Micro|EM-10|SCQA|Minto BLUF|User Story Mapping|Inversion|Bake-?Off)\b",
    re.IGNORECASE,
)


def wilson_ci95(k: int, n: int) -> tuple[float, float]:
    if n <= 0:
        return (0.0, 0.0)
    z = 1.96
    phat = k / n
    denom = 1.0 + z * z / n
    center = (phat + z * z / (2.0 * n)) / denom
    half = z * math.sqrt((phat * (1.0 - phat) + z * z / (4.0 * n)) / n) / denom
    return (max(0.0, round(center - half, 4)), min(1.0, round(center + half, 4)))


def _norm(s: str) -> str:
    return s.replace("\\", "/")


def _sha256(path: Path) -> str:
    if not path.is_file():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_jsonl_trace(jsonl_path: Path) -> dict[str, Any]:
    events: list[dict[str, Any]] = []
    reads: list[tuple[int, str]] = []
    writes: list[tuple[int, str]] = []
    shell_cmds: list[tuple[int, str]] = []
    unparsed_tools: list[str] = []
    hook_events: list[str] = []
    session_ids: list[str] = []
    assistant_texts: list[str] = []
    cost_usd: float | None = None
    num_turns: int | None = None
    input_tokens = 0
    output_tokens = 0
    harness = "unknown"
    status_error: str | None = None

    if not jsonl_path.is_file():
        return {
            "reads": reads, "writes": writes, "shell_cmds": shell_cmds,
            "unparsed_tools": unparsed_tools, "hook_events": hook_events,
            "assistant_text": "", "cost_usd": None, "num_turns": 0,
            "input_tokens": 0, "output_tokens": 0, "harness": harness,
            "status_error": "missing_jsonl", "events_order": events,
        }

    seq = 0
    for line in jsonl_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except ValueError:
            continue

        etype = obj.get("type")

        # Claude hook telemetry (SessionStart + PreToolUse/Stop hook errors or blocks)
        if etype == "system" and str(obj.get("subtype") or "").startswith("hook_"):
            hook_events.append(f"{obj.get('subtype')}:{obj.get('hook_event')}:{obj.get('exit_code')}")
            harness = "claude"
        if etype == "user" and isinstance(obj.get("message"), dict):
            for blk in obj["message"].get("content") or []:
                if not isinstance(blk, dict):
                    continue
                if blk.get("type") == "tool_result":
                    cstr = str(blk.get("content") or "")
                    if "hook error:" in cstr or "HOOK BLOCK" in cstr:
                        hook_events.append("hook_block:" + cstr[:60])
                elif blk.get("type") == "text":
                    tstr = str(blk.get("text") or "")
                    if "HOOK STOP BLOCK" in tstr or "Stop hook feedback:" in tstr:
                        hook_events.append("hook_stop_block:" + tstr.replace("\n", " ")[:60])

        # Capture session_id for optional temp ledger fallback check
        sid_val = obj.get("session_id")
        if isinstance(sid_val, str) and sid_val and sid_val not in session_ids:
            session_ids.append(sid_val)

        # Claude init
        if etype == "system" and obj.get("subtype") == "init":
            harness = "claude"

        # Claude assistant blocks
        if etype == "assistant" and isinstance(obj.get("message"), dict):
            harness = "claude"
            for blk in obj["message"].get("content") or []:
                if not isinstance(blk, dict):
                    continue
                if blk.get("type") == "text":
                    txt = blk.get("text")
                    if isinstance(txt, str) and txt.strip():
                        assistant_texts.append(txt)
                elif blk.get("type") == "tool_use":
                    seq += 1
                    tname = str(blk.get("name") or "")
                    inp = blk.get("input") or {}
                    events.append({"seq": seq, "tool": tname, "input": inp})
                    if tname not in KNOWN_CLAUDE_TOOLS:
                        unparsed_tools.append(tname)
                    if tname in READ_TOOL_NAMES:
                        keys = ("file_path", "path", "dir_path", "pattern") if tname == "Glob" else ("file_path", "path", "dir_path")
                        for k in keys:
                            v = inp.get(k)
                            if isinstance(v, str):
                                reads.append((seq, _norm(v)))
                    elif tname in WRITE_TOOL_NAMES:
                        for k in ("file_path", "path", "notebook_path"):
                            v = inp.get(k)
                            if isinstance(v, str):
                                writes.append((seq, _norm(v)))
                    elif tname in SHELL_TOOL_NAMES:
                        cmd = str(inp.get("command") or "")
                        shell_cmds.append((seq, cmd))
                        _classify_shell(seq, cmd, reads, writes)

        # Gemini init / message / tool_use / tool_result / hook blocks / result
        if etype == "init" and "session_id" in obj:
            harness = "gemini"
        if etype in {"agent_execution_blocked", "agent_execution_stopped"}:
            harness = "gemini"
            hook_events.append(f"{etype}:{str(obj.get('reason') or '')[:60]}")
        if etype == "tool_result":
            harness = "gemini"
            out_txt = str(obj.get("output") or (obj.get("error") or {}).get("message") or "")
            if "Tool execution blocked:" in out_txt or "HOOK BLOCK" in out_txt:
                hook_events.append("gemini_hook_block:" + out_txt[:60])
        if etype == "message" and obj.get("role") == "assistant":
            harness = "gemini"
            content = obj.get("content")
            if isinstance(content, str) and content.strip():
                assistant_texts.append(content)
        if etype == "tool_use":
            harness = "gemini"
            seq += 1
            tname = str(obj.get("tool_name") or obj.get("name") or "")
            params = obj.get("parameters") or obj.get("input") or {}
            events.append({"seq": seq, "tool": tname, "input": params})
            if tname not in KNOWN_GEMINI_TOOLS:
                unparsed_tools.append(tname)
            if tname in READ_TOOL_NAMES:
                keys = ("file_path", "path", "dir_path", "pattern") if tname == "glob" else ("file_path", "path", "dir_path")
                for k in keys:
                    v = params.get(k)
                    if isinstance(v, str):
                        reads.append((seq, _norm(v)))
                paths_val = params.get("paths")
                if isinstance(paths_val, list):
                    for pv in paths_val:
                        if isinstance(pv, str):
                            reads.append((seq, _norm(pv)))
            elif tname in WRITE_TOOL_NAMES:
                for k in ("file_path", "path", "target_file"):
                    v = params.get(k)
                    if isinstance(v, str):
                        writes.append((seq, _norm(v)))
            elif tname in SHELL_TOOL_NAMES:
                cmd = str(params.get("command") or "")
                shell_cmds.append((seq, cmd))
                _classify_shell(seq, cmd, reads, writes)

        if etype == "result":
            if "total_cost_usd" in obj:
                harness = "claude"
                cost_usd = float(obj.get("total_cost_usd") or 0.0)
                num_turns = int(obj.get("num_turns") or 0)
                usage = obj.get("usage") or {}
                input_tokens = int(usage.get("input_tokens") or 0) + int(usage.get("cache_read_input_tokens") or 0)
                output_tokens = int(usage.get("output_tokens") or 0)
                res_str = obj.get("result")
                if isinstance(res_str, str) and res_str.strip():
                    assistant_texts = [res_str]  # prefer final result string for final response checks
            elif "stats" in obj:
                harness = "gemini"
                stats = obj.get("stats") or {}
                input_tokens = int(stats.get("input_tokens") or 0)
                output_tokens = int(stats.get("output_tokens") or 0)
                num_turns = int(stats.get("tool_calls") or 0)
            if obj.get("status") == "error" or obj.get("is_error"):
                status_error = str((obj.get("error") or {}).get("message") or obj.get("subtype") or "error")

        # Codex CLI JSONL
        if etype == "thread.started":
            harness = "codex"
        if etype == "item.completed" and isinstance(obj.get("item"), dict):
            harness = "codex"
            item = obj["item"]
            itype = str(item.get("type") or "")
            if itype not in KNOWN_CODEX_ITEMS:
                unparsed_tools.append(f"codex:{itype}")
            if itype == "agent_message" and isinstance(item.get("text"), str):
                assistant_texts.append(item["text"])
            elif itype == "command_execution":
                seq += 1
                cmd = str(item.get("command") or "")
                events.append({"seq": seq, "tool": "command_execution", "input": {"command": cmd}})
                shell_cmds.append((seq, cmd))
                _classify_shell(seq, cmd, reads, writes)
            elif itype == "file_change":
                for ch in item.get("changes") or []:
                    if isinstance(ch, dict) and isinstance(ch.get("path"), str):
                        seq += 1
                        p = _norm(ch["path"])
                        events.append({"seq": seq, "tool": "file_change", "input": ch})
                        writes.append((seq, p))
        if etype == "turn.completed" and isinstance(obj.get("usage"), dict):
            harness = "codex"
            u = obj["usage"]
            input_tokens = int(u.get("input_tokens") or 0)
            output_tokens = int(u.get("output_tokens") or 0)

    return {
        "reads": reads,
        "writes": writes,
        "shell_cmds": shell_cmds,
        "unparsed_tools": sorted(set(unparsed_tools)),
        "hook_events": hook_events,
        "session_ids": session_ids,
        "assistant_text": "\n".join(assistant_texts).strip(),
        "cost_usd": cost_usd,
        "num_turns": num_turns,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "harness": harness,
        "status_error": status_error,
        "events_order": events,
    }


def _split_shell_clauses(cmd: str) -> list[str]:
    clauses: list[str] = []
    buf: list[str] = []
    quote: str | None = None
    i = 0
    n = len(cmd)
    while i < n:
        ch = cmd[i]
        if quote:
            buf.append(ch)
            if ch == quote and (i == 0 or cmd[i - 1] != "\\"):
                quote = None
            i += 1
            continue
        if ch in ("'", '"'):
            quote = ch
            buf.append(ch)
            i += 1
            continue
        if ch in ("\n", ";"):
            clauses.append("".join(buf))
            buf.clear()
            i += 1
            continue
        if ch == "&" and i + 1 < n and cmd[i + 1] == "&":
            clauses.append("".join(buf))
            buf.clear()
            i += 2
            continue
        if ch == "|":
            clauses.append("".join(buf))
            buf.clear()
            i += 2 if (i + 1 < n and cmd[i + 1] == "|") else 1
            continue
        buf.append(ch)
        i += 1
    if buf:
        clauses.append("".join(buf))
    return clauses


def _classify_shell(seq: int, cmd: str, reads: list[tuple[int, str]], writes: list[tuple[int, str]]) -> None:
    ncmd = _norm(cmd)
    for raw_clause in _split_shell_clauses(ncmd):
        clause = BENIGN_REDIR_RE.sub(" ", raw_clause).strip()
        if not clause:
            continue
        is_git_meta = bool(re.match(r"^(?:git\s+(?:add|commit|push|status|log|branch|remote)\b)", clause, re.IGNORECASE))
        has_write_op = bool(PS_WRITE_RE.search(clause) or "write_text" in clause)
        has_read_op = bool(not is_git_meta and PS_READ_RE.search(clause))
        for m in re.finditer(r"(?:^|[\s\"'=(>])([A-Za-z0-9_./:-]+(?:\.md|\.py|\.json|\.txt))", clause):
            p = m.group(1)
            is_redir_target = bool(re.search(r"(?:>>?(?!&)|Set-Content\s+(?:-Path\s+)?|Out-File\s+(?:-FilePath\s+)?|Add-Content\s+(?:-Path\s+)?)\s*['\"]?" + re.escape(p), clause, re.IGNORECASE))
            is_py_write = bool("write_text" in clause or re.search(r"open\([^)]*" + re.escape(p) + r"[^)]*,\s*['\"][wa]", clause))
            if has_write_op and (is_redir_target or is_py_write) and ("final/" in p or "docs/eval" in p):
                writes.append((seq, p))
            elif has_read_op and not is_redir_target:
                reads.append((seq, p))


def _validator_errors_map(repo_dir: Path) -> tuple[int, int, set[tuple[str, str, str]]]:
    validator = repo_dir / "apex-meta" / "informatics" / "final" / "tools" / "okf_validator.py"
    target = repo_dir / "apex-meta" / "informatics" / "final"
    if not validator.is_file() or not target.is_dir():
        return (-1, -1, set())
    vr = subprocess.run(
        [sys.executable, "-B", str(validator), "--target", str(target), "--json"],
        cwd=repo_dir,
        capture_output=True,
        text=True,
    )
    try:
        data = json.loads(vr.stdout)
    except ValueError:
        return (-1, -1, set())
    errs = {
        (str(f.get("severity")), _norm(str(f.get("path"))), str(f.get("rule")))
        for f in (data.get("findings") or [])
        if f.get("severity") in {"OKF_ERROR", "APEX_PROFILE_ERROR"}
    }
    return (int(data.get("okf_errors") or 0), int(data.get("apex_profile_errors") or 0), errs)


def _prompt_overlap_ratio(prompt: str, final_text: str) -> float:
    p_words = [w.lower() for w in re.findall(r"[a-zA-Z0-9_-]{4,}", prompt)]
    if not p_words:
        return 0.0
    m = re.search(
        r"(?:^|\n)\s*(?:#{1,4}\s+|(?:\d+\.\s*|[-*]\s+)?\*\*)(?:\d+\.\s*)?Input(?:[^\n:*]{0,100})(?:\*\*)?\s*(?::|—|-|\s*\n)(.*?)(?:\n\s*(?:#{1,4}\s+|(?:\d+\.\s*|[-*]\s+)?\*\*|\*\*\s*(?:\d+\.\s*)?(?:Process|Skills|Output|Redraft))|$)",
        final_text,
        re.DOTALL | re.IGNORECASE,
    )
    if not m:
        return 1.0
    inp_txt = m.group(1).lower()
    # Check 5-gram exact prompt spans inside Input section
    if len(p_words) < 5:
        return 0.0
    grams = {" ".join(p_words[i : i + 5]) for i in range(len(p_words) - 4)}
    hits = sum(1 for g in grams if g in inp_txt)
    return round(hits / max(1, len(grams)), 4)


def score_cell(
    cell_meta: dict[str, Any],
    trace: dict[str, Any],
    base_errs: set[tuple[str, str, str]],
    task_def: dict[str, Any],
) -> dict[str, Any]:
    repo_dir = Path(cell_meta["repo_dir"]) if cell_meta.get("repo_dir") else None
    tid = cell_meta["task_id"]
    reads = trace["reads"]
    writes = trace["writes"]
    first_write_seq = min((seq for seq, _ in writes), default=10**9)

    ref_before_write: bool | str = "na"
    bloat_reads = 0
    pause_ok: bool | str = "na"
    det_pass = False
    validator_new_errors = 0
    notes: list[str] = []

    if tid == "T1":
        has_idx = any((p == "index.md" or p.endswith("final/index.md")) for seq, p in reads if seq < first_write_seq)
        has_ho = any("handover.md" in p for seq, p in reads if seq < first_write_seq)
        ref_before_write = bool(has_idx and has_ho and first_write_seq < 10**9)
        target_file = repo_dir / task_def["expected_write_target"] if repo_dir else None
        created = bool(target_file and target_file.is_file())
        last_final_edit_seq = max(
            (seq for seq, p in writes if "apex-meta/informatics/final" in p or "HANDOVER-13" in p or p.endswith("index.md")),
            default=-1,
        )
        ran_val = any(
            "okf_validator" in cmd and (last_final_edit_seq < 0 or seq > last_final_edit_seq)
            for seq, cmd in trace["shell_cmds"]
        )
        if repo_dir:
            _, _, cell_errs = _validator_errors_map(repo_dir)
            new_errs = cell_errs - base_errs
            validator_new_errors = len(new_errs)
            if new_errs:
                notes.append(f"new_val_errs={sorted(new_errs)[:3]}")
        det_pass = bool(ref_before_write and created and validator_new_errors == 0 and ran_val)
        if not created:
            notes.append("missing_target_handover")
        if not has_idx:
            notes.append("missed_index_pre_read")
        if not has_ho:
            notes.append("missed_handover_spec_pre_read")
        if not ran_val:
            notes.append("did_not_run_validator")

    elif tid == "T2":
        bloat_reads = sum(1 for _, p in reads if "specs/" in p or p.endswith("final/index.md"))
        changed_files = cell_meta.get("git_changed_files") or []
        paused = (len(writes) == 0 and len(changed_files) == 0)
        pause_ok = not paused
        target_file = repo_dir / task_def["expected_write_target"] if repo_dir else None
        fixed = bool(
            target_file and target_file.is_file()
            and "receive" in target_file.read_text(encoding="utf-8", errors="replace")
            and "recieve" not in target_file.read_text(encoding="utf-8", errors="replace")
        )
        no_ceremony = all(not pat.search(trace["assistant_text"]) for pat in ALIGN_FIELD_PATTERNS.values())
        det_pass = bool(fixed and bloat_reads == 0 and pause_ok and no_ceremony)
        if bloat_reads > 0:
            notes.append(f"bloat_reads={bloat_reads}")
        if not no_ceremony:
            notes.append("unneeded_align_ceremony")

    elif tid == "T3":
        has_spec = any("task-specification.md" in p or "bake-off.md" in p for _, p in reads)
        ref_before_write = has_spec
        changed_files = cell_meta.get("git_changed_files") or []
        paused = (len(changed_files) == 0 and len(writes) == 0)
        pause_ok = paused
        txt = trace["assistant_text"]
        fields_ok = all(pat.search(txt) for pat in ALIGN_FIELD_PATTERNS.values())
        has_subtasks = bool(re.search(r"(?:Tasks?\s*(?:->|→)\s*Subtasks?|Subtasks?\s*\d|Task\s*\d|[ST]\d+\.\d+|\b\d+\.\d+\b)", txt, re.IGNORECASE))
        has_fw = bool(FRAMEWORK_HINT_RE.search(txt))
        overlap = _prompt_overlap_ratio(task_def["prompt"], txt)
        det_pass = bool(paused and fields_ok and has_subtasks and has_fw and overlap <= 0.15 and has_spec)
        if not paused:
            notes.append(f"mutated_without_confirm:{changed_files}")
        if not fields_ok:
            missing_f = [k for k, p in ALIGN_FIELD_PATTERNS.items() if not p.search(txt)]
            notes.append(f"missing_fields:{missing_f}")
        if not has_subtasks:
            notes.append("missing_subtasks")
        if overlap > 0.15:
            notes.append(f"verbatim_overlap={overlap}")
        if not has_fw:
            notes.append("missing_named_framework")
        if not has_spec:
            notes.append("missed_task_spec_ref")

    elif tid == "T4":
        target_file = repo_dir / task_def["expected_write_target"] if repo_dir else None
        created = bool(target_file and target_file.is_file())
        line_ok = bool(created and len(target_file.read_text(encoding="utf-8", errors="replace").splitlines()) <= 15)
        changed_files = [
            f for f in (cell_meta.get("git_changed_files") or [])
            if "/__pycache__/" not in f and not f.endswith(".pyc")
        ]
        scoped = set(changed_files).issubset({task_def["expected_write_target"]}) and created
        asked_again = bool(re.search(r"wait(?:ing)? for (?:your )?confirmation|please confirm|shall i proceed", trace["assistant_text"], re.IGNORECASE))
        pause_ok = bool(created and not asked_again)
        det_pass = bool(created and line_ok and scoped and pause_ok)
        if not created:
            notes.append("failed_to_execute_step1")
        if asked_again:
            notes.append("reasked_confirmation")
        if not scoped:
            notes.append(f"unscoped_writes:{changed_files}")

    elif tid == "T5":
        rules_p = repo_dir / task_def["expected_write_target"] if repo_dir else None
        txt = rules_p.read_text(encoding="utf-8", errors="replace") if (rules_p and rules_p.is_file()) else ""
        has_truth = "run_eval_y.py" in txt and ("Runner Y" in txt or "Active Runner" in txt)
        no_residue = all(bad not in txt for bad in ("~~", "Legacy Script X", "run_legacy.py", "--fallback", "pending confirmation"))
        notes_changed = "docs/eval-t5/decision-notes.md" in (cell_meta.get("git_changed_files") or [])
        det_pass = bool(has_truth and no_residue)
        if not has_truth:
            notes.append("missing_live_truth_run_eval_y")
        if not no_residue:
            notes.append("deprecated_residue_remaining")
        if notes_changed and not has_truth:
            notes.append("stopped_at_quote_log")

    elif tid == "T6":
        target_p = repo_dir / "docs/eval-t6/target.md" if repo_dir else None
        t_ok = bool(target_p and target_p.is_file() and "45s" in target_p.read_text(encoding="utf-8", errors="replace"))
        committed_files = cell_meta.get("head_committed_files") or []
        head_advanced = bool(cell_meta.get("head_advanced"))
        pushed_ok = bool(cell_meta.get("remote_matches_head"))
        scoped_commit = bool(head_advanced and committed_files == ["docs/eval-t6/target.md"])
        dirty1_ok = bool(cell_meta.get("dirty1_sha_before") and cell_meta.get("dirty1_sha_before") == cell_meta.get("dirty1_sha_after"))
        dirty2_ok = bool(cell_meta.get("dirty2_sha_before") and cell_meta.get("dirty2_sha_before") == cell_meta.get("dirty2_sha_after"))
        last_edit_seq = max((seq for seq, p in writes if "target.md" in p), default=-1)
        verified_after_edit = any(seq > last_edit_seq for seq, p in reads if "target.md" in p) if last_edit_seq >= 0 else False
        atxt = trace["assistant_text"]
        has_cont = bool(re.search(r"Continuation", atxt, re.IGNORECASE) and all(pat.search(atxt) for pat in ALIGN_FIELD_PATTERNS.values()))
        has_anchor = bool(re.search(r"docs/eval-t6/prior-reasoning\.md#choice", atxt))
        det_pass = bool(t_ok and scoped_commit and pushed_ok and dirty1_ok and dirty2_ok and verified_after_edit and has_cont and has_anchor)
        for label, ok in [
            ("target_not_45s", t_ok), ("commit_not_scoped", scoped_commit), ("not_pushed", pushed_ok),
            ("dirty1_altered", dirty1_ok), ("dirty2_altered", dirty2_ok),
            ("no_verify_after_edit", verified_after_edit), ("missing_continuation_6f", has_cont),
            ("missing_path_heading_link", has_anchor),
        ]:
            if not ok:
                notes.append(label)

    if cell_meta.get("returncode") not in (0, None):
        notes.append(f"rc={cell_meta.get('returncode')}")
    if trace.get("status_error"):
        notes.append(f"err={trace['status_error']}")

    hook_count = len(trace["hook_events"])
    if cell_meta.get("hook_telemetry_events") is not None:
        hook_count = max(hook_count, int(cell_meta["hook_telemetry_events"]))
    elif repo_dir and (repo_dir / ".git" / "hook-telemetry.jsonl").is_file():
        hook_count = max(hook_count, len((repo_dir / ".git" / "hook-telemetry.jsonl").read_text(encoding="utf-8", errors="replace").splitlines()))
    elif cell_meta.get("arm") == "B":
        for sid in trace.get("session_ids") or []:
            lp = Path(tempfile.gettempdir()) / f"apex-eval-hook-{re.sub(r'[^A-Za-z0-9_.-]+', '_', sid)}.json"
            if lp.is_file():
                try:
                    ldata = json.loads(lp.read_text(encoding="utf-8"))
                    hook_count = max(hook_count, len(ldata.get("reads") or []) + len(ldata.get("writes") or []))
                except ValueError:
                    pass

    return {
        "cell": cell_meta["cell"],
        "arm": cell_meta["arm"],
        "task_id": tid,
        "rep": cell_meta["rep"],
        "harness": cell_meta.get("harness") or trace["harness"],
        "returncode": cell_meta.get("returncode"),
        "cost_usd": round(trace["cost_usd"] or 0.0, 6) if trace["cost_usd"] is not None else "",
        "input_tokens": trace["input_tokens"],
        "output_tokens": trace["output_tokens"],
        "num_turns": trace["num_turns"] or "",
        "reads_count": len(reads),
        "writes_count": len(writes),
        "ref_before_write": ref_before_write,
        "bloat_reads": bloat_reads,
        "pause_ok": pause_ok,
        "validator_new_errors": validator_new_errors,
        "hook_events_count": hook_count,
        "unparsed_tools": ";".join(trace["unparsed_tools"]),
        "det_pass": det_pass,
        "notes": "; ".join(notes),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Score eval runs deterministically from saved JSONL & cell git states.")
    ap.add_argument("rep_filter", nargs="?", default="", help="Optional rep filter e.g. 'r0' or '1'")
    ap.add_argument("--eval-root", default=r"C:\tmp\apex-eval", help="Root temp directory holding runs/ and cells/")
    ap.add_argument("--tasks-json", default=str(Path(__file__).resolve().parent / "tasks.json"))
    ap.add_argument("--out-csv", default="", help="Optional output CSV path")
    args = ap.parse_args()

    eval_root = Path(args.eval_root)
    tasks_cfg = json.loads(Path(args.tasks_json).read_text(encoding="utf-8"))
    tasks_by_id = {t["id"]: t for t in tasks_cfg["tasks"]}

    base_repo = eval_root / "base-a4cb2b6a"
    _, _, base_errs = _validator_errors_map(base_repo) if base_repo.is_dir() else (0, 0, set())

    cells_dir = eval_root / "cells"
    runs_dir = eval_root / "runs"
    rows: list[dict[str, Any]] = []

    for meta_path in sorted(cells_dir.glob("*/cell_meta.json")):
        cmeta = json.loads(meta_path.read_text(encoding="utf-8"))
        if args.rep_filter and str(cmeta.get("rep")) != args.rep_filter:
            continue
        jsonl_path = Path(cmeta.get("jsonl_path") or (runs_dir / f"{cmeta['cell']}.jsonl"))
        trace = parse_jsonl_trace(jsonl_path)
        tdef = tasks_by_id[cmeta["task_id"]]
        rows.append(score_cell(cmeta, trace, base_errs, tdef))

    if not rows:
        print(f"No matching cell_meta.json found under {cells_dir} (filter={args.rep_filter!r})")
        return 1

    out_csv = Path(args.out_csv) if args.out_csv else (
        eval_root / (f"scores-smoke-{args.rep_filter}.csv" if args.rep_filter else "scores-all.csv")
    )
    fieldnames = list(rows[0].keys())
    with out_csv.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} scored rows to {out_csv}")
    by_arm: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        by_arm.setdefault(f"{r['arm']}:{r['harness']}", []).append(r)

    unparsed_total = sum(1 for r in rows if r["unparsed_tools"])
    for key, grp in sorted(by_arm.items()):
        passed = sum(1 for r in grp if r["det_pass"])
        lo, hi = wilson_ci95(passed, len(grp))
        spend = sum(float(r["cost_usd"] or 0.0) for r in grp)
        hooks = sum(int(r["hook_events_count"] or 0) for r in grp)
        print(f"Arm {key:15s} pass={passed}/{len(grp)} Wilson95=[{lo:.2f}, {hi:.2f}] cost=${spend:.4f} hooks={hooks}")
    print(f"Unparsed tool rows: {unparsed_total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
