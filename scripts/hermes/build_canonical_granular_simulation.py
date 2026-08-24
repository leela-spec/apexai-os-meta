#!/usr/bin/env python3
"""
Canonical Granular Weekly Orchestration Full-Detail Simulation.
Generates every single required file adhering field-for-field to the official PrecapNextDay templates:
- PreCap Next Day Brief
- 4 Individual Flow Execution Cards (F1, F2, F3, F4)
- Prompt Files Index + 12 Individual Single-Prompt Files (S1, S2, S3 for F1..F4)
- 12 Individual Raw Execution Dumps (L3)
- 4 Individual Flow Recaps (F1..F4) + Status Merge Candidate + Status Merge Audit (L4)
- Apex Session Mutation + Sync Recompute (L5)
Across Week 1 and Week 2!
"""

import os
import sys
import yaml
import json
import hashlib
import datetime

SIM_ROOT = "/root/workspaces/apexai-os-meta/apex-meta/orchestration/simulation"

def sha256_file(filepath):
    if not os.path.exists(filepath):
        return None
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def generate_canonical_day(week_num, day_str, day_idx):
    w_dir = f"{SIM_ROOT}/week-0{week_num}"
    l2_dir = f"{w_dir}/l2-daily-planning/day-{day_str}"
    cards_dir = f"{l2_dir}/flow-cards"
    prompts_dir = f"{l2_dir}/prompts"
    l3_dir = f"{w_dir}/l3-flow-execution/day-{day_str}/raw-evidence"
    l4_dir = f"{w_dir}/l4-recap-merge/day-{day_str}"
    l5_dir = f"{w_dir}/l5-session-sync/day-{day_str}"

    os.makedirs(cards_dir, exist_ok=True)
    os.makedirs(prompts_dir, exist_ok=True)
    os.makedirs(l3_dir, exist_ok=True)
    os.makedirs(l4_dir, exist_ok=True)
    os.makedirs(l5_dir, exist_ok=True)

    print(f"\n>>> [WEEK {week_num}] BUILDING CANONICAL GRANULAR ARTIFACTS: DAY {day_idx} ({day_str.upper()}) <<<")

    # 1. PRECAP NEXT DAY BRIEF
    brief_content = f"""# PreCap Next-Day Brief — Day {day_idx} ({day_str.upper()})

```yaml
brief_type: precap_next_day_brief
producer: PrecapNextDay
simulation: APEX-E2E-SIM-2W-CANONICAL
week: {week_num}
day: {day_str}
upstream_inputs:
  - l0-init/projectstatus-snapshot.yaml
  - l1-weekly-brief/weekly-command-brief.md
gate: G2-{day_str.capitalize()}
```

## 1. Strategy & Focus for Day {day_idx}
Execute deep multi-lane production across MasterOfArts (LHTL & SuperHeroKids), Investment (IPOS 60-indicator coverage), and Apex Control Plane synchronization.

| Priority | Flow Lane | Target Project | Primary Sprint Deliverable | Success Signal |
|:---:|---|---|---|---|
| 🥇 | **F1** | `MasterOfArts/LHTL` | 4-Pillar Active Recall & Feynman Extraction Engine | Story closed with AC evidence |
| 🥈 | **F2** | `MasterOfArts/SuperHeroKids` | 2-Day Workshop Lesson Plans & Parent Guidebook | Complete curriculum packaged |
| 🥉 | **F3** | `Investment` | IPOS 60-Indicator Expansion & Pandera Schemas | 100% QA Test Pass |
| 4️⃣ | **F4** | `apexai-os-meta` | Level-by-Level State Ledger Tracking & Session Mutation | Checksums verified on disk |

FreeT Allocation: AM 09:00–12:00 -> F1 & F4 · PM 14:00–17:00 -> F2, F3, F4.
"""
    with open(f"{l2_dir}/precap-next-day-brief-day{day_idx}.md", "w", encoding="utf-8") as f:
        f.write(brief_content)

    # 2. FOUR INDIVIDUAL FLOW EXECUTION CARDS
    flows = [
        ("F1", "MasterOfArts / LHTL Cognitive OS", "MasterOfArts/LHTL", "Extract 4-Pillar Active Recall and Feynman Extraction Engine"),
        ("F2", "MasterOfArts / SuperHeroKids & Meditation", "MasterOfArts/SuperHeroKids", "Package 2-Day Workshop Curricula & Parent Handbook"),
        ("F3", "Investment / IPOS Macro Indicator Expansion", "Investment", "Ingest 38 candidate indicators from registry_120.yaml to reach 60 indicators"),
        ("F4", "Apex Control / Portfolio State Synchronization", "apexai-os-meta", "Enforce fail-closed state mutations and dependency recomputation")
    ]

    for f_id, f_title, f_repo, f_goal in flows:
        card_content = f"""# Flow Execution Card — {f_title}

> **Readiness:** READY  
> **Outcome target:** {f_goal}  
> **Next action:** EXECUTE_NEXT_SPRINT  
> **Review needed:** NONE  

## Start or resume here
**Current sprint:** S1  
**Current status:** READY  
**Exact next operator step:** Open prompt file `flow_prompt-{f_id.lower()}-s1.md` and dispatch to worker.  

## Operator controls
- [ ] Execute S1 prompt pack.
- [ ] Review intermediate output in `{f_repo}`.
- [ ] Advance to S2 and S3.

## Flow identity and context
**Flow ID:** `{f_id}`  
**Project:** `{f_repo}`  
**Why today:** Scheduled milestone execution in Weekly Command Brief.  
**Goals:** {f_goal}  

### S1 — Scoping & Foundation
**Sprint status:** READY  
- Task: Review baseline context and extract core structural models.
- Prompt File: `prompts/flow_prompt-{f_id.lower()}-s1.md`

### S2 — Deep Formulation & Implementation
**Sprint status:** READY  
- Task: Author complete production text, code schemas, and verification tests.
- Prompt File: `prompts/flow_prompt-{f_id.lower()}-s2.md`

### S3 — Verification & Packaging
**Sprint status:** READY  
- Task: Audit output quality, check edge cases, and package deliverables for flow-recap.
- Prompt File: `prompts/flow_prompt-{f_id.lower()}-s3.md`
"""
        with open(f"{cards_dir}/flow-execution-card-{f_id.lower()}.md", "w", encoding="utf-8") as f:
            f.write(card_content)

    # 3. PROMPT FILES INDEX & 12 INDIVIDUAL PROMPT FILES
    index_rows = []
    for f_id, f_title, f_repo, f_goal in flows:
        for s_idx in [1, 2, 3]:
            prompt_name = f"flow_prompt-{f_id.lower()}-s{s_idx}.md"
            index_rows.append(f"| `{f_id}-S{s_idx}` | [{f_title} — Sprint {s_idx}]({prompt_name}) | Hermes Worker | Execute Sprint {s_idx} for {f_id} | READY |")

            # Single prompt file content
            prompt_body = f"""# Prompt: {f_title} — Sprint {s_idx}

**Recommended surface:** Hermes Agent / Claude Sonnet  
**Use when:** Executing Sprint {s_idx} of Flow `{f_id}` in `{f_repo}`.  
**Expected return artifact:** Raw execution log and target workspace file.  

## Prompt
You are the Lead Specialist working in `/root/workspaces/{f_repo}`.
Execute Sprint {s_idx} of Flow `{f_id}`:
1. Target Goal: {f_goal} (Sprint {s_idx} Milestone).
2. Adhere strictly to repository coding/writing standards with zero fact bleed.
3. Output the complete, unedited production deliverable and raw execution log.
"""
            with open(f"{prompts_dir}/{prompt_name}", "w", encoding="utf-8") as f:
                f.write(prompt_body)

    prompt_index_content = f"""# Prompt Files and Index — Day {day_idx} ({day_str.upper()})

> **Prompt access state:** READY  
> **Outcome:** All 12 individual sprint prompt files generated and verified.  
> **Next action:** OPEN_NEXT_PROMPT  

## Prompt index

| Sprint | Prompt file | Recommended surface | Use when | Status |
|---|---|---|---|---|
""" + "\n".join(index_rows) + "\n"

    with open(f"{l2_dir}/prompt-files-and-index.md", "w", encoding="utf-8") as f:
        f.write(prompt_index_content)

    with open(f"{l2_dir}/g2-checkpoint-day{day_idx}.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"gate": "G2", "status": "APPROVED", "day": day_str, "prompt_count": 12, "flow_cards_count": 4}, f)

    print(f"  ✓ Generated PreCap Brief, 4 Flow Cards, Prompt Index, and 12 Single-Prompt Files (Gate G2 APPROVED).")

    # 4. LEVEL L3: 12 INDIVIDUAL RAW EXECUTION DUMPS
    for f_id, f_title, f_repo, f_goal in flows:
        for s_idx in [1, 2, 3]:
            dump_file = f"{l3_dir}/raw-dump-{f_id.lower()}-s{s_idx}.log"
            with open(dump_file, "w", encoding="utf-8") as f:
                f.write(f"RAW EXECUTION LOG — FLOW {f_id} SPRINT {s_idx}\nTimestamp: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\nTarget: {f_repo}\nStatus: COMPLETE\nArtifact verified on disk.")
    
    with open(f"{l3_dir}/g3-checkpoint-day{day_idx}.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"gate": "G3", "status": "EVIDENCE_HARVESTED", "dump_count": 12}, f)
    print(f"  ✓ Harvested 12 individual raw execution dumps (Gate G3 APPROVED).")

    # 5. LEVEL L4: 4 FLOW RECAPS + STATUS MERGE CANDIDATE + AUDIT
    for f_id, f_title, f_repo, f_goal in flows:
        recap_content = f"""# Flow Recap — {f_id} ({f_title})

## Sprint Deliberations
- **S1 (Scoping):** 100% complete. Raw dump `raw-dump-{f_id.lower()}-s1.log`.
- **S2 (Implementation):** 100% complete. Target files authored in `{f_repo}`.
- **S3 (Verification):** 100% complete. Zero fact bleed confirmed.

## Candidate State Delta
- Status: ADVANCED
- Deliverables: Verified on disk.
"""
        with open(f"{l4_dir}/flow-recap-{f_id.lower()}.md", "w", encoding="utf-8") as f:
            f.write(recap_content)

    status_merge_candidate = {
        "candidate_id": f"SMC-W{week_num}-D{day_idx}",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "reconciled_flows": ["F1", "F2", "F3", "F4"],
        "conflicts_detected": 0,
        "verdict": "MERGE_READY"
    }
    with open(f"{l4_dir}/status-merge-candidate.yaml", "w", encoding="utf-8") as f:
        yaml.dump(status_merge_candidate, f, sort_keys=False)

    with open(f"{l4_dir}/status-merge-audit.md", "w", encoding="utf-8") as f:
        f.write(f"# Status Merge Audit — Day {day_idx}\n\nAll 4 flow recaps reconciled with zero collisions. Gates G4 & G5: APPROVED.")

    with open(f"{l4_dir}/g4-g5-checkpoint-day{day_idx}.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"gate_G4": "APPROVED", "gate_G5": "APPROVED"}, f)
    print(f"  ✓ Generated 4 Flow Recaps, Status Merge Candidate, and Audit (Gates G4/G5 APPROVED).")

    # 6. LEVEL L5: CANONICAL SESSION MUTATION & SYNC RECOMPUTE
    session_mut = {
        "mutation_id": f"MUT-CANONICAL-W{week_num}-D{day_idx}",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "applied_deltas": [
            {"flow": "F1", "project": "MasterOfArts/LHTL", "status": "ADVANCED"},
            {"flow": "F2", "project": "MasterOfArts/SuperHeroKids", "status": "ADVANCED"},
            {"flow": "F3", "project": "Investment", "status": "ADVANCED"},
            {"flow": "F4", "project": "apexai-os-meta", "status": "SYNCED"}
        ]
    }
    with open(f"{l5_dir}/apex-session-mutation.json", "w", encoding="utf-8") as f:
        json.dump(session_mut, f, indent=2)

    sync_recompute = {
        "recompute_id": f"SYNC-W{week_num}-D{day_idx}",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "projectstatus_updated": True,
        "zero_fact_bleed_verified": True
    }
    with open(f"{l5_dir}/apex-sync-recompute.yaml", "w", encoding="utf-8") as f:
        yaml.dump(sync_recompute, f, sort_keys=False)

    print(f"  ✓ Level L5 Apex Session Mutation & Sync Recompute COMPLETE.")

def run_all_canonical():
    print("=======================================================================")
    print(">>> GENERATING FULL CANONICAL GRANULAR FILE TREE (WEEK 1 & WEEK 2) <<<")
    print("=======================================================================")
    days = ["mon", "tue", "wed", "thu", "fri"]

    # Week 1 Days 1..5
    for idx, day in enumerate(days, 1):
        generate_canonical_day(week_num=1, day_str=day, day_idx=idx)

    # Week 2 Days 1..5
    for idx, day in enumerate(days, 1):
        generate_canonical_day(week_num=2, day_str=day, day_idx=idx)

    print("\n=======================================================================")
    print(">>> CANONICAL GRANULAR SIMULATION TREE GENERATION 100% COMPLETE <<<")
    print("=======================================================================")

if __name__ == "__main__":
    run_all_canonical()
