#!/usr/bin/env python3
"""Deterministic scoring of stage 1 cells. No model judges anything here.

Usage:
    python score_stage1.py [suffix-filter]      e.g. python score_stage1.py r      scores *-r1,2,3 (default)
                                                     python score_stage1.py r0     scores the smoke cells (rep 0)
Writes scores.csv and prints per-arm summaries with Wilson 95% intervals.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE / "tasks.json").read_text(encoding="utf-8"))
TASKS = {t["id"]: t for t in CFG["tasks"]}
RUNS, CELLS = HERE / "runs", HERE / "cells"
FIXTURE = HERE / "fixtures" / "Packaging Ideas.md"
FIXTURE_SHA = hashlib.sha256(FIXTURE.read_bytes()).hexdigest()

GOV = {
    "writing-profile": "writing-profile.md", "file-architecture": "file-architecture.md",
    "patch-discipline": "patch-discipline.md", "handover": "execution-modes/handover.md",
    "bake-off": "bake-off.md", "qa-matrix": "qa-decision-matrix.md", "task-spec": "task-specification.md",
    "design02": "02-INFORMATION-ARCHITECTURE.md", "design03": "03-FILING-AND-IDENTITY.md",
    "blueprint": "authoring-blueprint.md",
}
IER = re.compile(r"I\s?\d{1,3}\s?/\s?E\s?\d{1,3}\s?/\s?R\s?\d{1,3}")
LINK = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")


def norm(p: str) -> str:
    return p.replace("\\", "/")


def wilson(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    z, p = 1.96, k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def parse_run(path: Path) -> dict:
    calls, results, final, cost, turns = [], {}, "", None, None
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = o.get("type")
        if t == "assistant":
            for b in o.get("message", {}).get("content", []) or []:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    calls.append({"id": b.get("id"), "name": b.get("name"), "input": b.get("input", {})})
        elif t == "user":
            c = o.get("message", {}).get("content", [])
            if isinstance(c, list):
                for b in c:
                    if isinstance(b, dict) and b.get("type") == "tool_result":
                        cont = b.get("content")
                        if isinstance(cont, list):
                            cont = " ".join(x.get("text", "") for x in cont if isinstance(x, dict))
                        results[b.get("tool_use_id")] = str(cont)
        elif t == "result":
            final, cost, turns = str(o.get("result", "")), o.get("total_cost_usd"), o.get("num_turns")
    return {"calls": calls, "results": results, "final": final, "cost": cost, "turns": turns}


def git(cell: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=cell, capture_output=True, text=True).stdout


def changed_files(cell: Path) -> tuple[list[str], list[str]]:
    new, mod = [], []
    for line in git(cell, "status", "--porcelain", "-uall").splitlines():
        code, p = line[:2], line[3:].strip().strip('"')
        (new if "?" in code or "A" in code else mod).append(p)
    return new, mod


def frontmatter_ok(text: str) -> bool:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return False
    keys = set()
    for ln in lines[1:]:
        if ln.strip() == "---":
            return {"type", "id", "title", "description", "tags", "status"} <= keys
        if not ln.strip() or ln.strip().startswith("#"):
            continue
        if ":" not in ln or ln.lstrip().startswith("- "):
            return False
        keys.add(ln.split(":", 1)[0].strip())
    return False


def links_ok(cell: Path, rel: str) -> bool:
    f = cell / rel
    for m in LINK.finditer(f.read_text(encoding="utf-8", errors="ignore")):
        t = m.group(1)
        if t.startswith(("http", "mailto")):
            continue
        if not (f.parent / t).resolve().exists():
            return False
    return True


def validator_findings(cell: Path) -> set[tuple]:
    r = subprocess.run([sys.executable, str(cell / "systems" / "apex" / "tools" / "okf_validator.py"), "--target", str(cell), "--json"],
                       capture_output=True, text=True)
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        return set()
    return {(f["rule"], f["path"], f["message"]) for f in data.get("findings", []) if f["severity"].endswith("ERROR")}


_BASE: dict[str, set] = {}


def baseline(arm: str) -> set:
    if arm not in _BASE:
        _BASE[arm] = validator_findings(HERE / f"arm{arm}")
    return _BASE[arm]


def score(name: str) -> dict:
    arm, rest = name.split("-", 1)
    task_id, rep = rest.rsplit("-", 1)
    task = TASKS[task_id]
    run = parse_run(RUNS / f"{name}.jsonl")
    cell = CELLS / name / "mindful-bar"
    calls = run["calls"]
    prev_text, reads, first_write = "", {}, None
    for i, c in enumerate(calls):
        inp = c["input"]
        if c["name"] in ("Write", "Edit") or (c["name"] == "Bash" and str(inp.get("command", "")).startswith("cp ")):
            first_write = i if first_write is None else first_write
        if c["name"] == "Read":
            p = norm(str(inp.get("file_path", "")))
            for k, frag in GOV.items():
                if p.endswith(frag) and k not in reads:
                    reads[k] = (i, frag.split("/")[-1] in prev_text or frag in prev_text)
        prev_text += " " + run["results"].get(c["id"], "")
    new, mod = changed_files(cell)
    new_md = [p for p in new if p.endswith(".md")]
    texts = {p: (cell / p).read_text(encoding="utf-8", errors="ignore") for p in new_md + [m for m in mod if m.endswith(".md")]}
    new_text = "\n".join(texts[p] for p in new_md).lower()
    v_new = len(validator_findings(cell) - baseline(arm))
    fm = all(frontmatter_ok(texts[p]) for p in new_md) if new_md else False
    lk = all(links_ok(cell, p) for p in texts) if texts else True
    gate_name, gate_ok = task["gate"], None

    def before(keys):
        idx = [reads[k][0] for k in keys if k in reads]
        return bool(idx) and (first_write is None or min(idx) < first_write)

    if gate_name == "authoring":
        gate_ok = before(["file-architecture"])
    elif gate_name == "handover":
        gate_ok = before(["handover"])
    elif gate_name == "trade_off":
        gate_ok = before(["bake-off", "qa-matrix"])
    elif gate_name == "editing":
        gate_ok = before(["patch-discipline"])
    placement_ok = det = None
    final = run["final"]
    if task_id == "T1-brand":
        placement_ok = any(p.startswith("brand-and-sales/identity/") for p in new_md)
        names = all(n in new_text for n in ["kakao moment", "pause bar", "cacao calm", "slow square", "mindful bar"])
        det = placement_ok and fm and lk and v_new == 0 and names
    elif task_id == "T2-allergen":
        placement_ok = any(p.startswith("compliance/") for p in new_md)
        det = placement_ok and fm and lk and v_new == 0 and "tree nut" in new_text and "soy lecithin" in new_text
    elif task_id == "T3-interview":
        placement_ok = any(p.startswith("customers/research/") for p in new_md)
        det = placement_ok and fm and lk and v_new == 0 and "consent" in new_text and "15:00" in new_text
    elif task_id == "T4-handover":
        ho = [p for p in new_md if re.search(r"^type:\s*Handover\s*$", texts[p], re.M)]
        words = bool(ho) and all(w in texts[ho[0]].lower() for w in ("input", "process", "output", "definition of done"))
        placement_ok = any(p.startswith("projects/") for p in new_md)
        det = bool(ho) and words and fm and lk and v_new == 0
    elif task_id == "T5-tradeoff":
        det = len(IER.findall(final)) >= 2 and "recommend" in final.lower()
    elif task_id == "T6-edit":
        stat = git(cell, "diff", "--numstat").split()
        diff = git(cell, "diff", "-U0")
        added = [l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++")]
        removed = [l[1:] for l in diff.splitlines() if l.startswith("-") and not l.startswith("---")]
        det = (mod == ["company/charter-and-strategy/working-context.md"] and not new and len(added) == 1 and len(removed) == 1
               and "afternoon pause" in added[0] and added[0] == removed[0].replace("afternoon break", "afternoon pause"))
    elif task_id == "T7-ingest":
        copies = [p for p in new if p.startswith("knowledge/original-source-documents/") and
                  hashlib.sha256((cell / p).read_bytes()).hexdigest() == FIXTURE_SHA]
        ledger = [p for p in new_md if p.startswith("knowledge/source-coverage/")]
        rec = "systems/migration/external-source-records.md" in mod and FIXTURE_SHA in texts.get("systems/migration/external-source-records.md", "")
        placement_ok = any(p.startswith("products/") and "sleeve" in texts[p].lower() for p in list(texts))
        det = bool(copies) and bool(ledger) and rec and placement_ok and all(frontmatter_ok(texts[p]) for p in ledger)
    elif task_id == "T8-lookup":
        det = "G8" in final and not new and not mod
    spec_reads = sorted(reads)
    return {"cell": name, "arm": arm, "task": task_id, "rep": rep, "gate": gate_name, "gate_ok": gate_ok, "placement_ok": placement_ok,
            "det_pass": det, "validator_new_errors": v_new, "files_new": len(new), "files_changed": len(mod),
            "spec_reads": "+".join(spec_reads), "design02_surfaced": reads.get("design02", (None, None))[1],
            "tool_calls": len(calls), "turns": run["turns"], "cost_usd": run["cost"], "final_chars": len(final),
            "ran": bool(calls) or bool(final)}


def main() -> int:
    flt = sys.argv[1] if len(sys.argv) > 1 else "r"
    names = sorted(p.stem for p in RUNS.glob("*.jsonl") if re.search(rf"-{flt}\d*$", p.stem) and (flt != "r" or not p.stem.endswith("-r0")))
    rows = [score(n) for n in names]
    out = HERE / ("scores.csv" if flt == "r" else f"scores-{flt}.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        if rows:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
    print(f"{len(rows)} cells scored -> {out.name}")
    by_arm = defaultdict(list)
    for r in rows:
        by_arm[r["arm"]].append(r)
    for arm, rs in sorted(by_arm.items()):
        def rate(key, filt=lambda r: True):
            sel = [r for r in rs if r[key] is not None and filt(r)]
            k = sum(1 for r in sel if r[key])
            lo, hi = wilson(k, len(sel))
            return f"{k}/{len(sel)} [{lo:.2f}-{hi:.2f}]"
        print(f"ARM {arm}: n={len(rs)} det_pass {rate('det_pass')} | placement {rate('placement_ok')} | gate_ok {rate('gate_ok')}"
              f" | mean calls {sum(r['tool_calls'] for r in rs)/len(rs):.1f} | cost ${sum((r['cost_usd'] or 0) for r in rs):.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
