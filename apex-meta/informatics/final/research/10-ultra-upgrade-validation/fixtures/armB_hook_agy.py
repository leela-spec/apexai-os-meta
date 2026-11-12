#!/usr/bin/env python3
"""Deterministic Antigravity (.agents/hooks.json) PreToolUse / Stop gate for Arm B-AGY.

Translates Antigravity camelCase hook JSON (stdin/stdout) cleanly:
- PreToolUse: reads {"toolCall": {"name", "args"}, "transcriptPath", "workspacePaths", "conversationId"}
  and returns {"decision": "allow"} or {"decision": "deny", "reason": "..."}.
- Stop: reads {"terminationReason", "transcriptPath", "workspacePaths", "conversationId", "executionNum"}
  and returns {} (allow stop) or {"decision": "continue", "reason": "..."} (block once per turn).
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

READ_TOOLS = {
    "read_file", "view_file", "view_file_outline", "view_code_item",
    "find_by_name", "grep_search", "list_dir",
}
WRITE_TOOLS = {
    "write_file", "write_to_file", "replace_file_content",
    "multi_replace_file_content", "sed_file",
}
SHELL_TOOLS = {"run_command"}

RESIDUE_T5 = ("~~", "Legacy Script X", "run_legacy.py", "pending confirmation")
RESIDUE_T7 = ("~~", "legacy-v1", "script_old.py", "pending confirmation")
DIRTY_EXCLUSIONS = (
    "docs/eval-t6/dirty1.md", "docs/eval-t6/dirty2.md",
    "docs/eval-t7/dirty1.md", "docs/eval-t7/dirty2.md",
)

BLANKET_GIT_RE = re.compile(
    r"\bgit\s+(?:"
    r"add\s+(?:--\s+)?(?:-A|--all|-u|--update|\.(?=\s|;|&|\||$))"
    r"|commit\b[^#;&|\n]*?\s(?:-(?!-)[A-Za-z]*a[A-Za-z]*(?=\s|$|[\"'])|--all\b)"
    r")",
    re.IGNORECASE,
)
GIT_COMMIT_RE = re.compile(r"\bgit\s+commit\b", re.IGNORECASE)
SHELL_CLAUSE_SPLIT_RE = re.compile(r"\r?\n|&&|\|\||;|\|")
BENIGN_REDIR_RE = re.compile(r"(?:^|\s)[12]?>&\s*[12](?=\s|$)|(?:^|\s)[12]?>>?\s*(?:/dev/null|\$null)\b", re.IGNORECASE)
SHELL_READ_VERB_RE = re.compile(
    r"(?:\b(?:cat|head|tail|sed|awk|more|less|rg|grep|Get-Content|gc|Select-String|sls|type)\b|open\(|read_text\()",
    re.IGNORECASE,
)
SHELL_READ_PATH_RE = re.compile(r"(?:^|[\s\"'=(])([A-Za-z0-9_./\\:-]*(?:\.md|\.py|\.json|\.txt))")


def _norm(val: Any) -> str:
    s = str(val or "").strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ('"', "'"):
        s = s[1:-1]
    return s.replace("\\", "/").strip()


def _repo_root(event: dict[str, Any]) -> str:
    wpaths = event.get("workspacePaths") or []
    if isinstance(wpaths, list) and wpaths:
        return _norm(wpaths[0])
    # Fallback: script sits in <repo>/.agents/armB_hook_agy.py
    return _norm(Path(__file__).resolve().parent.parent)


def _ledger_path(event: dict[str, Any], cwd: str) -> Path:
    cid = str(event.get("conversationId") or "").strip()
    key = cid if cid else hashlib.sha256(cwd.encode("utf-8", errors="replace")).hexdigest()[:16]
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", key)
    return Path(tempfile.gettempdir()) / f"apex-eval-agy-hook-{safe}.json"


def _load_ledger(path: Path) -> dict[str, Any]:
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data.setdefault("reads", [])
                data.setdefault("writes", [])
                data.setdefault("stop_turns", [])
                return data
        except (OSError, ValueError):
            pass
    return {"reads": [], "writes": [], "stop_turns": []}


def _save_ledger(path: Path, data: dict[str, Any]) -> None:
    try:
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except OSError:
        pass


def _append_git_telemetry(cwd: str, event_name: str, tool_name: str, decision: str, detail: str = "") -> None:
    git_dir = Path(cwd) / ".git"
    if not git_dir.is_dir():
        return
    try:
        tpath = git_dir / "hook-telemetry.jsonl"
        with tpath.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({"hook": event_name, "tool": tool_name, "decision": decision, "detail": detail}) + "\n")
    except OSError:
        pass


def _extract_shell_reads(cmd: str) -> list[str]:
    hits: list[str] = []
    for raw_clause in SHELL_CLAUSE_SPLIT_RE.split(_norm(cmd)):
        cleaned = BENIGN_REDIR_RE.sub(" ", raw_clause)
        if not SHELL_READ_VERB_RE.search(cleaned):
            continue
        for m in SHELL_READ_PATH_RE.finditer(cleaned):
            hits.append(m.group(1))
    return hits


def _shell_writes_final(cmd: str) -> bool:
    for raw_clause in SHELL_CLAUSE_SPLIT_RE.split(_norm(cmd)):
        cleaned = BENIGN_REDIR_RE.sub(" ", raw_clause)
        if "apex-meta/informatics/final" not in cleaned:
            continue
        if re.search(
            r"(?:>>?(?!&)|Set-Content\s+(?:-Path\s+)?|Out-File\s+(?:-FilePath\s+)?|Add-Content\s+(?:-Path\s+)?|\btee\s+(?:-a\s+)?)\s*['\"]?[^\s;|&\"']*apex-meta/informatics/final",
            cleaned,
            re.IGNORECASE,
        ):
            return True
        if re.search(
            r"\b(?:cp|mv|Copy-Item|Move-Item)\s+[^;|&]*\s+['\"]?[^\s;|&\"']*apex-meta/informatics/final",
            cleaned,
            re.IGNORECASE,
        ):
            return True
        if re.search(
            r"(?:open\([^)]*apex-meta/informatics/final[^)]*,\s*['\"][wa]|Path\([^)]*apex-meta/informatics/final[^)]*\)\.write_)",
            cleaned,
            re.IGNORECASE,
        ):
            return True
    return False


def _scan_transcript(transcript_path: str) -> tuple[set[str], int]:
    reads: set[str] = set()
    user_turns = 0
    if not transcript_path:
        return reads, user_turns
    tp = Path(transcript_path)
    full_tp = tp.with_name("transcript_full.jsonl")
    if full_tp.is_file():
        tp = full_tp
    if not tp.is_file():
        return reads, user_turns
    try:
        raw = tp.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return reads, user_turns

    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except ValueError:
            continue
        if obj.get("type") == "USER_INPUT":
            user_turns += 1
        for tc in obj.get("tool_calls") or []:
            if not isinstance(tc, dict):
                continue
            name = str(tc.get("name") or "")
            args = tc.get("args") or {}
            if not isinstance(args, dict):
                continue
            if name in READ_TOOLS:
                for k in ("Path", "AbsolutePath", "File", "TargetFile", "DirectoryPath", "SearchDirectory", "SearchPath", "path", "file_path"):
                    v = args.get(k)
                    if isinstance(v, str) and v.strip():
                        reads.add(_norm(v))
            elif name in SHELL_TOOLS:
                cmd = args.get("CommandLine") or args.get("command") or ""
                if isinstance(cmd, str):
                    for hit in _extract_shell_reads(cmd):
                        reads.add(hit)
    return reads, user_turns


def _has_ref(reads: set[str], needle: str) -> bool:
    return any(needle in r for r in reads)


def _extract_write_text(tool_name: str, args: dict[str, Any]) -> str:
    chunks: list[str] = []
    for k in ("Content", "CodeContent", "ReplacementContent", "content", "new_string"):
        v = args.get(k)
        if isinstance(v, str):
            chunks.append(v)
    rc = args.get("ReplacementChunks")
    if isinstance(rc, list):
        for item in rc:
            if isinstance(item, dict) and isinstance(item.get("ReplacementContent"), str):
                chunks.append(item["ReplacementContent"])
    return "\n".join(chunks)


def _handle_pretool(event: dict[str, Any], cwd: str) -> int:
    tc = event.get("toolCall") or {}
    tool_name = str(tc.get("name") or "")
    args = tc.get("args") or {}
    if not isinstance(args, dict):
        args = {}

    lpath = _ledger_path(event, cwd)
    ledger = _load_ledger(lpath)

    if tool_name in READ_TOOLS:
        for k in ("Path", "AbsolutePath", "File", "TargetFile", "DirectoryPath", "SearchDirectory", "SearchPath", "path", "file_path"):
            v = args.get(k)
            if isinstance(v, str) and v.strip():
                nv = _norm(v)
                if nv not in ledger["reads"]:
                    ledger["reads"].append(nv)
        _save_ledger(lpath, ledger)
        _append_git_telemetry(cwd, "PreToolUse", tool_name, "allow")
        print(json.dumps({"decision": "allow"}))
        return 0

    if tool_name in SHELL_TOOLS:
        cmd = _norm(args.get("CommandLine") or args.get("command") or "")
        for hit in _extract_shell_reads(cmd):
            if hit not in ledger["reads"]:
                ledger["reads"].append(hit)
        _save_ledger(lpath, ledger)

        cmd_unquoted = re.sub(r'"[^"]*"|\'[^\']*\'', ' "" ', cmd)
        if BLANKET_GIT_RE.search(cmd_unquoted):
            st = subprocess.run(["git", "status", "--porcelain"], cwd=cwd, capture_output=True, text=True)
            dirty = [ln for ln in st.stdout.splitlines() if ln.strip()]
            if dirty:
                _append_git_telemetry(cwd, "PreToolUse", tool_name, "deny", "blanket_git")
                print(json.dumps({
                    "decision": "deny",
                    "reason": (
                        "HOOK BLOCK (<sync>/<handover> EM-14): Refusing blanket git staging/commit "
                        "(-A / --all / -u / . / -a) in a dirty tree. Stage ONLY explicit scoped paths via `git add -- <path>`."
                    ),
                }))
                return 0

        if GIT_COMMIT_RE.search(cmd_unquoted):
            staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=cwd, capture_output=True, text=True)
            staged_files = [_norm(s) for s in staged.stdout.splitlines() if s.strip()]
            bad_staged = [s for s in staged_files if any(s.endswith(excl) for excl in DIRTY_EXCLUSIONS)]
            if bad_staged:
                _append_git_telemetry(cwd, "PreToolUse", tool_name, "deny", "dirty_staged")
                print(json.dumps({
                    "decision": "deny",
                    "reason": (
                        f"HOOK BLOCK (<handover> EM-14): Refusing commit because unrelated dirty files "
                        f"are staged: {bad_staged}. Unstage them with `git reset HEAD -- ...`."
                    ),
                }))
                return 0

        if _shell_writes_final(cmd):
            t_reads, _ = _scan_transcript(str(event.get("transcriptPath") or ""))
            all_reads = set(ledger["reads"]) | t_reads
            if not _has_ref(all_reads, "apex-meta/informatics/final/index.md") and not _has_ref(all_reads, "final/index.md"):
                _append_git_telemetry(cwd, "PreToolUse", tool_name, "deny", "shell_write_final_no_index")
                print(json.dumps({
                    "decision": "deny",
                    "reason": (
                        "HOOK BLOCK (<authoring>): Shell write targeting apex-meta/informatics/final/ "
                        "before opening apex-meta/informatics/final/index.md. Read the index and matched spec first."
                    ),
                }))
                return 0

        _append_git_telemetry(cwd, "PreToolUse", tool_name, "allow")
        print(json.dumps({"decision": "allow"}))
        return 0

    if tool_name in WRITE_TOOLS:
        target = ""
        for k in ("Path", "TargetFile", "AbsolutePath", "File", "file_path", "path"):
            v = args.get(k)
            if isinstance(v, str) and v.strip():
                target = _norm(v)
                break
        if not target:
            print(json.dumps({"decision": "allow"}))
            return 0

        if target not in ledger["writes"]:
            ledger["writes"].append(target)
            _save_ledger(lpath, ledger)

        t_reads, _ = _scan_transcript(str(event.get("transcriptPath") or ""))
        all_reads = set(ledger["reads"]) | t_reads

        if "apex-meta/informatics/final/" in target and "/.agents/" not in target:
            missing: list[str] = []
            if not _has_ref(all_reads, "apex-meta/informatics/final/index.md") and not _has_ref(all_reads, "final/index.md"):
                missing.append("apex-meta/informatics/final/index.md")
            if "/operations/handovers/" in target and not _has_ref(all_reads, "handover.md"):
                missing.append("apex-meta/informatics/final/specs/execution-modes/handover.md")
            if missing:
                _append_git_telemetry(cwd, "PreToolUse", tool_name, "deny", f"missing_{missing}")
                print(json.dumps({
                    "decision": "deny",
                    "reason": (
                        "HOOK BLOCK (<authoring>/<handover>): Read required spec(s) BEFORE creating or editing "
                        f"under apex-meta/informatics/final/: missing {missing}."
                    ),
                }))
                return 0

        if "operating-rules" in target and "/.agents/" not in target:
            text_to_check = _extract_write_text(tool_name, args)
            markers = RESIDUE_T7 if "eval-t7" in target else RESIDUE_T5
            found_bad = [m for m in markers if m in text_to_check]
            if found_bad:
                _append_git_telemetry(cwd, "PreToolUse", tool_name, "deny", "residue")
                print(json.dumps({
                    "decision": "deny",
                    "reason": (
                        f"HOOK BLOCK (<current_truth>): Operating rule file `{target}` still contains "
                        f"deprecated strikethrough or retired markers {found_bad}. State live truth only and "
                        "purge retired runner references in the same edit."
                    ),
                }))
                return 0

        _append_git_telemetry(cwd, "PreToolUse", tool_name, "allow")
        print(json.dumps({"decision": "allow"}))
        return 0

    print(json.dumps({"decision": "allow"}))
    return 0


def _handle_stop(event: dict[str, Any], cwd: str) -> int:
    if str(event.get("terminationReason") or "NO_TOOL_CALL") != "NO_TOOL_CALL":
        print(json.dumps({}))
        return 0

    lpath = _ledger_path(event, cwd)
    ledger = _load_ledger(lpath)
    t_reads, user_turns = _scan_transcript(str(event.get("transcriptPath") or ""))
    reads = set(ledger.get("reads") or []) | t_reads
    writes = [_norm(w) for w in (ledger.get("writes") or [])]

    tkey = f"turn-{user_turns}" if user_turns > 0 else f"exec-{event.get('executionNum', 1)}"
    if tkey in (ledger.get("stop_turns") or []):
        print(json.dumps({}))
        return 0

    issues: list[str] = []

    # 1. Governed apex-meta/informatics/final/ changes + okf_validator.py check
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
        if not any(r.endswith("final/index.md") or r == "index.md" for r in reads):
            issues.append(
                "Governed files modified under apex-meta/informatics/final/ without reading apex-meta/informatics/final/index.md."
            )
        validator = Path(cwd) / "apex-meta" / "informatics" / "final" / "tools" / "okf_validator.py"
        bundle = Path(cwd) / "apex-meta" / "informatics" / "final"
        if validator.is_file():
            vr = subprocess.run(
                [sys.executable, "-B", str(validator), "--target", str(bundle), "--json"],
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

    # 2. T5 living truth guard
    t5_active = any("eval-t5" in x or "decision-notes" in x for x in (list(reads) + writes))
    t5_rules = Path(cwd) / "docs" / "eval-t5" / "operating-rules.md"
    if t5_active and t5_rules.is_file():
        rtxt = t5_rules.read_text(encoding="utf-8", errors="replace")
        bad = [m for m in RESIDUE_T5 if m in rtxt]
        if bad:
            issues.append(f"docs/eval-t5/operating-rules.md still has deprecated residue {bad}.")
        if "run_eval_y.py" not in rtxt:
            issues.append("docs/eval-t5/operating-rules.md is missing resolved truth `run_eval_y.py`.")

    # 3. T6 dirty close-out guard
    st_t6 = subprocess.run(["git", "status", "--porcelain", "--", "docs/eval-t6"], cwd=cwd, capture_output=True, text=True)
    t6_lines = [_norm(ln[3:].strip()) for ln in st_t6.stdout.splitlines() if len(ln) >= 4]
    if "docs/eval-t6/target.md" in t6_lines and ("docs/eval-t6/dirty1.md" in t6_lines or "docs/eval-t6/dirty2.md" in t6_lines):
        issues.append(
            "docs/eval-t6/target.md has uncommitted edits: verify, commit ONLY docs/eval-t6/target.md "
            "(leaving dirty1.md and dirty2.md untouched), push to origin, and include 6-field Continuation citing prior-reasoning.md#choice."
        )

    # 4. T7 living truth + dirty close-out guard (triggered only if decision.md or operating-rules.md was modified/approved in Turn 4)
    last_inp = str(event.get("lastUserInput") or "")
    t7_closeout = "eval-t7" in last_inp and ("commit" in last_inp.lower() or "update" in last_inp.lower())
    if t7_closeout:
        t7_rules = Path(cwd) / "docs" / "eval-t7" / "operating-rules.md"
        if t7_rules.is_file():
            t7_txt = t7_rules.read_text(encoding="utf-8", errors="replace")
            bad7 = [m for m in RESIDUE_T7 if m in t7_txt]
            if bad7:
                issues.append(f"docs/eval-t7/operating-rules.md still has deprecated residue {bad7}.")
            if "run_policy_v2.py" not in t7_txt or "enforce-v2" not in t7_txt:
                issues.append("docs/eval-t7/operating-rules.md must contain live truth `enforce-v2` and `run_policy_v2.py`.")
        st_t7 = subprocess.run(["git", "status", "--porcelain", "--", "docs/eval-t7"], cwd=cwd, capture_output=True, text=True)
        t7_lines = [_norm(ln[3:].strip()) for ln in st_t7.stdout.splitlines() if len(ln) >= 4]
        if "docs/eval-t7/operating-rules.md" in t7_lines and ("docs/eval-t7/dirty1.md" in t7_lines or "docs/eval-t7/dirty2.md" in t7_lines):
            issues.append(
                "docs/eval-t7/operating-rules.md has uncommitted edits: commit ONLY docs/eval-t7/operating-rules.md "
                "(leaving dirty1.md and dirty2.md untouched), push to origin, and include 6-field Continuation citing docs/eval-t7/prior-reasoning.md#choice."
            )

    # 5. Unpushed commit check when explicit closeout task asks to push
    if ("eval-t6" in last_inp or t7_closeout) and "push" in last_inp.lower():
        h_local = subprocess.run(["git", "rev-parse", "HEAD"], cwd=cwd, capture_output=True, text=True)
        h_rem = subprocess.run(["git", "rev-parse", "refs/remotes/origin/main"], cwd=cwd, capture_output=True, text=True)
        if h_local.returncode == 0 and h_rem.returncode == 0 and h_local.stdout.strip() != h_rem.stdout.strip():
            issues.append(
                "Local commit on main is not pushed to origin yet; push the scoped commit and end with the 6-field Continuation citing prior reasoning."
            )

    if not issues:
        _append_git_telemetry(cwd, "Stop", "Stop", "allow")
        print(json.dumps({}))
        return 0

    ledger.setdefault("stop_turns", []).append(tkey)
    _save_ledger(lpath, ledger)
    _append_git_telemetry(cwd, "Stop", "Stop", "continue", f"{len(issues)}_issues")
    print(json.dumps({
        "decision": "continue",
        "reason": "HOOK STOP BLOCK: " + " | ".join(issues),
    }))
    return 0


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "pretool"
    try:
        raw_stdin = sys.stdin.read()
        event = json.loads(raw_stdin) if raw_stdin.strip() else {}
    except ValueError:
        print(json.dumps({"decision": "allow"} if mode == "pretool" else {}))
        return 0

    cwd = _repo_root(event)
    if mode == "stop":
        return _handle_stop(event, cwd)
    return _handle_pretool(event, cwd)


if __name__ == "__main__":
    sys.exit(main())
