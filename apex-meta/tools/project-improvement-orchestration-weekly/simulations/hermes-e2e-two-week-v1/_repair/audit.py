#!/usr/bin/env python3
"""Final acceptance audit: manifest completeness, prompt uniqueness,
deferral consistency, traceability, quota invariants, review protocol."""
import os, json, glob, hashlib, sys

ROOT = "/workspace/apex-meta/tools/project-improvement-orchestration-weekly/simulations/hermes-e2e-two-week-v1"
os.chdir(ROOT)
fails, warns = [], []
def check(cond, msg):
    (fails if not cond else warns.__class__()).append(msg) if not cond else None
    if not cond: print("FAIL:", msg)

DAYS = ["monday","tuesday","wednesday","thursday","friday"]
# 1. manifest completeness
n = len(glob.glob("runs/*/*/flows/F*/prompts/S*.md"))
check(n==120, f"prompt count {n}!=120")
# 2. uniqueness
hashes = {}
for p in glob.glob("runs/*/*/flows/F*/prompts/S*.md"):
    h = hashlib.md5(open(p,'rb').read()).hexdigest()
    check(h not in hashes, f"duplicate body {p} == {hashes.get(h)}")
    hashes[h]=p
print(f"OK: 120 prompts, {len(hashes)} distinct bodies")
# 3. W02-Wednesday consistency
ul = [json.loads(l) for l in open("runs/W02/wednesday/usage-ledger.jsonl")]
f3 = [r for r in ul if r["flow"]=="F3"]
check(all(r.get("net_consumed")==0 for r in f3), "W02-Wed F3 net consumption nonzero")
recap = open("runs/W02/wednesday/flows/F3/flow-recap.md").read()
check("DEFERRED" in recap, "W02-Wed F3 recap missing DEFERRED")
receipt = open("runs/W02/wednesday/day-receipt.yaml").read()
check("flows_deferred: [F3]" in receipt and "flows_executed: 3" in receipt, "day receipt inconsistent")
brief = open("runs/W02/wednesday/precap-next-day-brief.md").read()
check("P4" in brief and "omitted" in brief.lower(), "Wednesday brief lacks compression notice")
card = open("runs/W02/wednesday/flows/F3/flow-execution-card.md").read()
check("DEFERRED" in card, "W02-Wed F3 card not marked deferred")
pi = open("runs/W02/wednesday/prompt-index.md").read()
check("OMITTED" in pi, "W02-Wed prompt index lacks OMITTED marks")
print("OK: W02-Wednesday deferral chain consistent")
# 4. quota: no negative balances anywhere; W02 starts from W01 Friday close
for f in glob.glob("runs/*/*/usage-ledger.jsonl"):
    for line in open(f):
        r=json.loads(line)
        check(r["remaining_credits"]>=0, f"negative balance in {f}")
w2start = open("runs/W02/inputs/quota-ledger-start.yaml").read()
w1close = open("runs/W01/friday/usage-summary.yaml").read()
import re
def ledger(t):
    a = dict(re.findall(r"^\s+(\w+): (\d+)$", t, re.M))
    b = dict(re.findall(r"^(\w+): (\d+)$", t, re.M))
    a.update(b)
    return {k: v for k, v in a.items() if k not in ("day", "credits_consumed_today", "net_consumed_today", "reserved_and_released")}
check(ledger(w2start)==ledger(w1close), "W02 start != W01 Friday close ledger")
print("OK: quota continuity W01->W02")
# 5. gates G1-G5 present per week/day
for wk in ["W01","W02"]:
    g=open(f"runs/{wk}/sunday/gate-G1.yaml").read(); check("APPROVED" in g, f"{wk} G1")
    for d in DAYS:
        sm=open(f"runs/{wk}/{d}/status-merge.md").read(); check("G5-APPROVED" in sm, f"{wk} {d} G5")
        rl=sum(1 for _ in open(f"runs/{wk}/{d}/routing-ledger.jsonl")); check(rl==12, f"{wk} {d} routing {rl}")
        uo=open(f"runs/{wk}/{d}/usage-summary.yaml").read(); check("remaining_quota_ledger" in uo, f"{wk} {d} usage summary")
print("OK: G1-G5 exercised across both weeks")
# 6. reviews: rubric completeness + distinct verdicts
for wk in ["W01","W02"]:
    revs=glob.glob(f"runs/{wk}/saturday-review/reviewer-*.okf.md")
    check(len(revs)==4, f"{wk} reviewer count")
    for r in revs:
        t=open(r).read()
        check(t.count("/5 |")==13 or t.count("/5 |")+t.count("/5.0")>0, f"{wk} {os.path.basename(r)} rubric")
        check("first_10_second_comprehension" in t and "provenance_clarity" in t, f"{wk} {r} missing dims")
        check("simulated_reviewer_verdict" in t, f"{wk} {r} missing simulation marker")
    fa=open(f"runs/{wk}/saturday-review/fresh-agent-challenge.okf.md").read()
    check(fa.count("CORRECT")>=8 and "PASS" in fa, f"{wk} fresh-agent challenge")
    syn=open(f"runs/{wk}/saturday-review/review-synthesis.okf.md").read()
    check("Disagreement" in syn, f"{wk} synthesis disagreement matrix")
print("OK: review protocol complete")
# 7. traceability spot: rollup repos -> brief flows -> cards
roll=json.load(open("runs/W01/inputs/portfolio-rollup.json"))
check(set(roll["repositories"].keys())=={"apex","masterofarts","acim","investment"}, "rollup repos")
prov=open("runs/W02/inputs/portfolio-rollup-provenance.yaml").read()
for o in ["real_board_snapshot","apex_portfolio_decision","synthetic_simulation_overlay"]:
    check(o in prov, f"W02 provenance origin missing: {o}")
snap=json.load(open("runs/W02/inputs/source-board-snapshots/acim.json"))
check(snap.get("freshness")=="stale_18h", f"P6 stale snapshot freshness={snap.get('freshness')}")
print("OK: provenance + P6 stale snapshot")
print("\n=== AUDIT:", "PASS" if not fails else f"{len(fails)} FAILURES", "===")
sys.exit(1 if fails else 0)
