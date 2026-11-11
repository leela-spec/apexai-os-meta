#!/usr/bin/env python3
"""Run stage 1 cells as headless Claude Code sessions.

Each cell is a fresh git clone of an arm repository. The arm AGENTS.md is appended to the system prompt, which
mimics project instructions that are loaded automatically. Restricted mode ignores the user's global CLAUDE.md,
settings, hooks and skills. Bash is limited to cp, sha256sum and cmp.

Usage:
    python run_stage1.py smoke            # arms x tasks T6, T7, T8, rep 0 (pipeline check, not analysed)
    python run_stage1.py full             # arms x all tasks x reps in tasks.json, shuffled with the fixed seed
Cells with an existing non-empty output file are skipped, so a run can be resumed.
"""
from __future__ import annotations

import json
import os
import random
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE / "tasks.json").read_text(encoding="utf-8"))
FIXTURE = HERE / "fixtures" / "Packaging Ideas.md"
RUNS = HERE / "runs"
CELLS = HERE / "cells"
LOCK = threading.Lock()
CLAUDE = shutil.which("claude") or "claude"
REAL = [Path(r"C:\GitDev\mindful-bar"), Path(r"C:\GitDev\apexai-os-meta")]


def snapshot_real() -> dict:
    out = {}
    for repo in REAL:
        porcelain = subprocess.run(["git", "status", "--porcelain", "-uall"], cwd=repo, capture_output=True, text=True).stdout
        diff = subprocess.run(["git", "diff"], cwd=repo, capture_output=True, text=True).stdout
        import hashlib
        out[str(repo)] = {"porcelain_sha256": hashlib.sha256(porcelain.encode()).hexdigest(),
                          "diff_sha256": hashlib.sha256(diff.encode()).hexdigest(), "entries": len(porcelain.splitlines())}
    return out


def log(msg: str) -> None:
    with LOCK:
        with open(HERE / "progress.log", "a", encoding="utf-8") as f:
            f.write(time.strftime("%H:%M:%S ") + msg + "\n")


def run_cell(job: tuple[str, dict, int]) -> None:
    arm, task, rep = job
    name = f"{arm}-{task['id']}-r{rep}"
    out = RUNS / f"{name}.jsonl"
    if out.exists() and out.stat().st_size > 0:
        return
    parent = CELLS / name
    if parent.exists():
        shutil.rmtree(parent, onerror=lambda f, p, e: (os.chmod(p, 0o700), f(p)))
    parent.mkdir(parents=True)
    cell = parent / "mindful-bar"
    subprocess.run(["git", "clone", "-q", "-c", "core.autocrlf=false", str(HERE / f"arm{arm}"), str(cell)], check=True, capture_output=True)
    prompt = task["prompt"].replace("{FIXTURE}", str(FIXTURE))
    cmd = [CLAUDE, "-p", prompt, "--model", CFG["model"], "--restricted",
           "--tools", "Read,Grep,Glob,Write,Edit,Bash",
           "--allowedTools", "Bash(cp *),Bash(sha256sum *),Bash(cmp *)",
           "--append-system-prompt-file", "AGENTS.md",
           "--permission-mode", "acceptEdits", "--strict-mcp-config",
           "--output-format", "stream-json", "--verbose", "--no-session-persistence", "--disable-slash-commands",
           "--max-budget-usd", str(CFG["budget_usd_per_run"]), "--add-dir", str(FIXTURE.parent)]
    t0 = time.time()
    status = "ok"
    try:
        with open(out, "w", encoding="utf-8") as fo, open(RUNS / f"{name}.err", "w", encoding="utf-8") as fe:
            p = subprocess.run(cmd, cwd=cell, stdin=subprocess.DEVNULL, stdout=fo, stderr=fe, timeout=CFG["timeout_s"])
            if p.returncode != 0:
                status = f"exit{p.returncode}"
    except subprocess.TimeoutExpired:
        status = "timeout"
    log(f"{name} {status} {time.time() - t0:.0f}s")


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    RUNS.mkdir(exist_ok=True)
    CELLS.mkdir(exist_ok=True)
    tasks = {t["id"]: t for t in CFG["tasks"]}
    if mode == "smoke":
        jobs = [(a, tasks[t], 0) for a in CFG["arms"] for t in ("T6-edit", "T7-ingest", "T8-lookup")]
    elif mode == "full":
        jobs = [(a, t, r) for a in CFG["arms"] for t in CFG["tasks"] for r in CFG["reps"]]
        random.Random(CFG["seed"]).shuffle(jobs)
    else:
        print(__doc__)
        return 2
    before = snapshot_real()
    (HERE / f"safety-before-{mode}.json").write_text(json.dumps(before, indent=2), encoding="utf-8")
    log(f"START {mode} {len(jobs)} jobs")
    with ThreadPoolExecutor(max_workers=CFG["parallel"]) as ex:
        list(ex.map(run_cell, jobs))
    after = snapshot_real()
    (HERE / f"safety-after-{mode}.json").write_text(json.dumps(after, indent=2), encoding="utf-8")
    log(f"DONE {mode} real repos unchanged={before == after}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
