#!/usr/bin/env python3
"""Repair pass for hermes-e2e-two-week-v1: prompt diversification,
W02-Wednesday deferral consistency, artifact deepening."""
import os, json, hashlib, glob, re
from collections import OrderedDict

ROOT = "/workspace/apex-meta/tools/project-improvement-orchestration-weekly/simulations/hermes-e2e-two-week-v1"
os.chdir(ROOT)
DAYS = ["monday","tuesday","wednesday","thursday","friday"]
FLOWS = {
    "F1": {"proj": "masterofarts/LHTL", "name": "LHTL Cognitive OS",
           "milestone": "4-Pillar Active Recall & Feynman Cognitive Framework"},
    "F2": {"proj": "masterofarts/SuperHeroKids", "name": "SuperHeroKids Mindfulness",
           "milestone": "2-Day Workshop Lesson Plans & Mindfulness Cards"},
    "F3": {"proj": "investment/IPOS", "name": "IPOS Macro Indicator Pipeline",
           "milestone": "38 Candidate Macro Indicators (FRED Integration)"},
    "F4": {"proj": "apexai-os-meta", "name": "Apex Portfolio Control Plane",
           "milestone": "Deterministic Rollup Sync & Fail-Closed Ledger"},
}
DAY_FOCUS = {
    "monday":     ("Foundation & Extraction", "establish the working baseline for the week's milestone"),
    "tuesday":    ("Expansion & Drafting", "widen coverage and draft the primary deliverable set"),
    "wednesday":  ("Integration & Cross-Checks", "integrate outputs and resolve cross-item inconsistencies"),
    "thursday":   ("Hardening & Recovery", "harden validated output and absorb any mid-week recovery work"),
    "friday":     ("Consolidation & Week-Close", "consolidate the week's deliverable and prepare close-out evidence"),
}
SPRINT_ROLE = {
    "S1": ("Analysis & Design", "decompose the target and fix the exact work product shape"),
    "S2": ("Authoring & Build", "produce the substantive deliverable for this sprint"),
    "S3": ("Verification & QA", "verify against acceptance criteria and emit execution logs"),
}
WEEK_TAG = {"W01": "baseline pass", "W02": "stress-adaptive pass"}

def prompt_path(wk, d, fl, s):
    return f"runs/{wk}/{d}/flows/{fl}/prompts/{s}.md"

def read(p): return open(p, encoding="utf-8").read()
def write(p, c):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(c)

# ---------------------------------------------------------------- parse old headers
def parse_header(txt):
    g = lambda k: (re.search(rf"\*\*{k}:\*\* `?([^`\n]+)`?", txt) or [None,""])[1].strip()
    return {"surface": g("Assigned Surface"), "score": g("AIRouting Score Requirement"),
            "cost": g("Simulation Credit Cost")}

# ---------------------------------------------------------------- scenario overlays
def overlays(wk, d, fl, s, hdr, txt):
    notes = []
    if wk == "W02":
        if hdr["surface"] == "subscription_frontier_reasoning":
            notes.append("> [SCARCITY ADVISORY · P1] `subscription_frontier_reasoning` is in scarce state "
                         "(≤22% remaining). AIRouting fallback: downgrade to `subscription_frontier_chat` "
                         "unless this prompt meets the ≥240 high-end reasoning threshold.")
        if fl == "F2" and d in ("tuesday","thursday"):
            notes.append("> [HARD DEADLINE · P3] SuperHeroKids workshop print deadline lands this week — "
                         "this sprint feeds a physical deliverable and may not slip past Friday.")
        if wk == "W02" and d == "monday" and fl == "F1" and s == "S2":
            notes.append("> [OVERRUN FLAG · P5] Prior plan under-estimated this prompt at 4 credits; "
                         "actual simulated consumption was 12 (token overrun ×~2). Ledger already records actuals.")
        if d == "wednesday" and fl == "F3":
            notes.append("> [OMITTED · P4] Meeting-heavy day: this flow is DEFERRED to Thursday under "
                         "compression. Prompt retained for traceability; no execution dispatched.")
    else:
        if d == "wednesday" and fl == "F3":
            notes.append("> [FAILURE DRILL] Upstream FRED API timeout is injected this sprint; exercise the "
                         "fail-closed fallback and record the degradation in evidence.")
    return notes

# ---------------------------------------------------------------- 1. regenerate 120 prompts
hashes = {}
for wk in ["W01","W02"]:
    for d in DAYS:
        for fl in ["F1","F2","F3","F4"]:
            for s in ["S1","S2","S3"]:
                p = prompt_path(wk,d,fl,s)
                old = read(p); hdr = parse_header(old)
                F = FLOWS[fl]
                dtxt = DAY_FOCUS[d]; srole = SPRINT_ROLE[s]
                notes = overlays(wk,d,fl,s,hdr,old)
                body = f"""# Sprint Prompt: {F['proj']} — {s}
**Target File:** `{F['proj']}`
**Assigned Surface:** `{hdr['surface']}`
**AIRouting Score Requirement:** {hdr['score']}
**Simulation Credit Cost:** {hdr['cost']}
**Week / Day / Flow:** {wk} · {d} · {fl} ({WEEK_TAG[wk]})

## Objective
{F['milestone']} — {dtxt[0]} phase, sprint {s} ({srole[0]}): {dtxt[1]}.

## Sprint Scope ({srole[0]})
- Work product: {srole[1]}.
- Day emphasis: {dtxt[0]} — {dtxt[1]}.
- Milestone contribution: advance "{F['milestone']}" toward the {d} sub-target declared in the Weekly Command Brief.

## Instructions
1. Operate strictly within `/root/workspaces/{F['proj']}`.
2. Produce production-grade content adhering to domain standards with zero cross-repo fact bleed.
3. Emit structured artifacts and return deterministic execution logs.
4. Record actual credit consumption against surface `{hdr['surface']}` in the model-usage log.
"""
                if notes:
                    body += "\n## Scenario Overlays\n" + "\n".join(notes) + "\n"
                h = hashlib.md5(body.encode()).hexdigest()
                assert h not in hashes, f"duplicate prompt body at {p}"
                hashes[h] = p
                write(p, body)
print(f"[1] regenerated {len(hashes)} unique prompts")

# ---------------------------------------------------------------- 2. W02-Wednesday deferral consistency
wd = "runs/W02/wednesday"
# usage ledger: relabel F3 as reservation released
lines = [json.loads(l) for l in read(f"{wd}/usage-ledger.jsonl").splitlines() if l.strip()]
for r in lines:
    if r["flow"] == "F3":
        r["entry_type"] = "reservation_released"
        r["net_consumed"] = 0
        r["note"] = "P4 meeting compression: capacity reserved at planning, released before dispatch; deferred to Thursday."
    else:
        r["entry_type"] = "executed"
        r["setdefault"] = None
        r.pop("setdefault")
write(f"{wd}/usage-ledger.jsonl", "\n".join(json.dumps(r) for r in lines) + "\n")

gross = sum(r["credits_consumed"] for r in lines)
net = sum(r.get("net_consumed", r["credits_consumed"]) for r in lines)
released = gross - net
summary = read(f"{wd}/usage-summary.yaml")
summary += f"""
net_consumed_today: {net}
reserved_and_released: {released}
deferral_note: >
  F3 deferred under P4 meeting-heavy compression. Gross reservations (57) include
  18 released credits for F3; net execution consumption was {net}. Remaining-quota
  figures reflect reservations held through day close and released before Thursday.
"""
write(f"{wd}/usage-summary.yaml", summary)

write(f"{wd}/day-receipt.yaml", """receipt_id: RECEIPT-W02-WEDNESDAY
day: wednesday
prompts_materialized: 12
flows_planned: 4
flows_executed: 3
flows_deferred: [F3]
deferred_reason: P4_meeting_heavy_compression
gate_G5: APPROVED
signed_at: '2026-08-24T23:05:30.515691+00:00'
""")

sm = read(f"{wd}/status-merge.md")
sm = sm.replace("state_transitions:", "deferral_note: F3 capacity (18 cr) reserved then released; flow re-dispatches Thursday.\nstate_transitions:")
write(f"{wd}/status-merge.md", sm)

pi = read(f"{wd}/prompt-index.md")
for fl in ["F1","F2","F3"]:
    pass
pi = pi.replace("| VALIDATED |", "| VALIDATED |")
# mark F3 rows
pi = re.sub(r"(\| `F3-S\d` \|[^|]+\|[^|]+\|[^|]+\|[^|]+\|) VALIDATED \|",
            r" OMITTED (P4 compression) |", pi)
write(f"{wd}/prompt-index.md", pi)

# F3 card readiness
card_p = f"{wd}/flows/F3/flow-execution-card.md"
card = read(card_p)
card = card.replace("**Readiness:** READY", "**Readiness:** DEFERRED (P4 meeting-heavy compression)")
card = card.replace("- [x] S1:", "- [ ] S1:").replace("- [x] S2:", "- [ ] S2:").replace("- [x] S3:", "- [ ] S3:")
card = card.replace("-> Validated.", "-> Deferred to Thursday (no dispatch).")
write(card_p, card)

ev_p = f"{wd}/flows/F3/evidence.md"
write(ev_p, read(ev_p).rstrip() + "\n- DEFERRAL: no dispatch occurred; 18 reserved credits released per P4 compression.\n")

print("[2] W02-Wednesday deferral reconciled")
