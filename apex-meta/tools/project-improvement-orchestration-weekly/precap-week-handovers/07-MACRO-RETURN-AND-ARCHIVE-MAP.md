---
type: Reference
id: HO-PW-MACRO-07
title: "Handover 07 — Macro Return, Modular Loop Re-Integration & Deterministic Archive Plan"
description: "Reconciles the six individual Precap Week module chats back into the preserved modular weekly lifecycle (Weekly Command Brief Intake -> Precap Week -> Recap Day -> Precap Day), specifies every inter-module contract, and lists all 35+ files in 01-weekly-command-brief/ by Keep/Merge/Archive disposition."
status: current
date: 2026-11-11
tags: [weekly-orchestration, macro-architecture, reconciliation, archive-plan, module-convergence]
---

# 07 · Macro Return & Archive Plan (`Step 3 After Module Chats`)

## 1. Purpose & Non-Collapse Boundary

After individual module chats close `01` through `06`, this Macro convergence specification re-connects every output back into the preserved **modular Weekly Orchestrator loop** (`weekly-orchestrator/SKILL.md`, `D012/D013`).

**Strict Modular Boundary (`<hold_position>`):** Never merge `Weekly Command Brief (Operator Input)`, `Precap Week`, `Recap Day / Flow Recap`, and `Precap Day` into one monolithic file or chat. Each stage owns **one primary job** and passes only a thin, structured handoff forward.

---

## 2. Preserved End-to-End 4-Stage Macro Loop

```text
[Stage 1A: Weekly Command Brief]  <-- Operator weekly intent, project pauses, GCal ignores, M/P/R focus, week-demand.json
        |
        v (Operator Weekly Input + Live OP opCall.js + Live Google Calendar + week-blueprint.json + Session planning_feed)
[Stage 1B: Precap Week (+ Dispersal T2)]
   - 00 Portfolio Compass (Stats: 5 KPIs grounded in slot-inventory & OP)
   - 01 Operator Decisions (New / Ongoing / Standard + Gate G1 PROPOSED->APPROVED)
   - 02 Matrix 1 (L1/L2, G|I|P|S|O|C, 🔗 Cross-Repo, Shortlist/Longlist -> selected_work_reference)
   - 03 Matrix 2 (Mon-Sun T1 08:00-24:00 & 12:00-16:00, DD-22A P/M/R Chunks, M|P|R Personal Strip)
   - 04 Residuals & Provenance ([OP-OFFLINE] flags, meeting compression, 1-hop [src], compact presentation_handoff)
   - 05 Sequencing Orientation (Q13 / dispersal summary / T2 allocation ledger)
        |
        v (Gate G1 Approved -> Single compact presentation_handoff YAML + week-allocation.json)
[Stage 4/5: Recap Day / Flow Recap + Status Merge]  <-- Flow Evidence -> flow-recap (parallel per flow) -> status-merge -> G5 -> OP / apex-session
        |
        v (Confirmed OP & Session state + closing-day actuals + capacity delta)
[Stage 2/3: Precap Day (PrecapNextDay)]  <-- Next Day Brief -> Flow Execution Cards -> Concrete Sprint Prompt Files -> Gated GCal writes (Q10)
```

---

## 3. Cross-Module Producer -> Consumer Interface Table

| Producer | Output Artifact / Field | Exact Consumer(s) | Invariant Protecting Against Drift |
|---|---|---|---|
| **Operator Command Brief (`01`)** | `operator_weekly_command_brief` YAML + `week-demand.json` | `03 Operator Decisions`, `05 Matrix 2` (`M\|P\|R`), `06 Sequencing` | Decisions enter `New`; background holds enter `Ongoing`; never overwrite `week-blueprint.json`. |
| **`02-weekly-dispersal/week-blueprint.json`** | `operating_window`, `regimes`, `weekday_anchors`, `status_merge_day` | `02 Stats`, `03 Standard Decisions`, `05 Matrix 2`, `06 build_slot_inventory.py`, `PrecapNextDay` | **Sole clock owner** (`08:00–24:00`, `Day Outro 22:00–22:30`, `Sat–Sun 12:00–16:00`). Never duplicated as prose truth elsewhere. |
| **Live Intake (`D019` + `D014`)** | Paginated OP (`opCall.js` / `[OP-OFFLINE]`), Google Cal (untrusted text), `planning_feed` | `04 Matrix 1`, `05 Matrix 2`, `03 Ongoing`, `02 Stats` | Missing external services never block planning (`[OP-OFFLINE]`); fake numeric WP IDs forbidden. |
| **Matrix 1 (`04`)** | `selected_work_reference[]` (`op_ref`, `title`, `tier`, `readiness`, `cross_repo_links`, `slot_hint`) | `05 Matrix 2` (`C` slots), `06 Sequencing` (`C` XP/TP), `PrecapNextDay` | Matrix 1 stays **zero-time / zero-sprint**; Matrix 2 links back by ref instead of cloning tasks. |
| **Sequencing `T2` (`06`)** | `week-allocation.json` (`240` `slot_id -> chunk_id`), projected `XP/TP/BP` | `05 Matrix 2` (`DD-22A` `P/M/R` strip), `02 Stats` (`S2`), Section `05` | `R` never mints `XP`; evening courses never enter `72×2m P`; `Matrix 2` never authors `C`. |
| **Precap Week Output (`01`)** | Cockpit (`00–05`) + single `presentation_handoff` YAML | **`PrecapNextDay` (`G2`)** | No duplicated `flow_packet` or separate machine seed; `PrecapWeek` never creates GCal events (`Q10`). |

---

## 4. Cleanup & Deterministic Archive Plan (`01-weekly-command-brief/` Audit of 35+ Items — EXECUTED `2026-11-11`)

Modules `01–06` have landed in their canonical owners (`SPEC-PRECAP-WEEK-ITERATIONS.okf.md`, `.claude/skills/PrecapWeek/*`, `week-blueprint.json`, `MasterOfArts/Sequencing/dispersal/*`), and superseded drafts/research have been moved via `git mv` into `apex-meta/archive/weekly-orchestration/precap-week-drafts-2026-11/` and `apex-meta/archive/weekly-orchestration/precap-week-research-2026-11/`:

| Current Path (`01-weekly-command-brief/` & sibling) | Classification | Disposition Upon Module Closure |
|---|---|---|
| `SPEC-PRECAP-WEEK-ITERATIONS.okf.md` | **KEEP (Canonical Spec)** | Single Precap Week Cockpit UI & structure spec (version bump `v2.1`). |
| `02-weekly-dispersal/week-blueprint.json` + Dispersal bundle | **KEEP (Canonical Engine/Clock)** | Clock in `apexai-os-meta`; engine/demand mirrored from `MasterOfArts`. |
| `DESIGN-DECISIONS.md` | **THIN OR ARCHIVE (`CDL-03`)** | Merge surviving rules (`I/R/E`, Adaptive Hybrid) into `.claude/skills/PrecapWeek/`, retire duplicate `M/W` prose. |
| `HANDOVER-02`, `HANDOVER-03`, `HANDOVER-04`, `HANDOVER-05`, `HANDOVER-06`, `HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md` | **MERGE -> ARCHIVE** | Once settled rules land inside `SPEC` + `.claude/skills/PrecapWeek/` (and GCal moves to `PrecapNextDay`), archive individual draft handovers via `git mv`. |
| `HANDOVER-01`, `HANDOVER.md`, `HANDOVER-MATRIX-1-*`, `SPEC-DUAL-VIEW-WEEKLY-PRECAP.md`, `HANDOVER-MODULE-01-*`, `WEEK-VISUALIZATION-RESEARCH-HANDOVER.md`, `HANDOVER-MASTER-PRECAP-AND-DISPERSAL-ORCHESTRATOR.okf.md` | **ARCHIVE (`git mv`)** | Superseded Nov 6–11 scaffolding/handovers; move intact with `archive_metadata` once `01–06` land. |
| `precap-week-cockpit-W45-actual-data-v03.html`, `generate_northstar_html.py`, `WEEKLY_PRECAP_*`, `WEEKLY_COMMAND_BRIEF_2026_W45.md`, `calendar-export/*` | **RETIRE TO `examples/` OR `archive/`** | Keep ONE validated W45/W46 fixture in `.claude/skills/PrecapWeek/examples/`; archive stale drafts (`DRAFT_W45`, old `.ics`). |
| `research/*` (`northstar-*`, `prototypes/*`, `weekly-precap-reset-20261107/`, `Q13`, `MATRIX1-R1`, `CLIGEM.md`, `GPT.md`, `PRECAP-WEEK-INPUT-PIPELINE-*`, `MACRO-INTERFACES-*`) | **ARCHIVE (`git mv`)** | Move completed historical research bundles out of `01-weekly-command-brief/` into `apex-meta/archive/weekly-orchestration/precap-week-research-2026-11/`. |
| `MASTER-INFORMATION-FLOW-AND-DESIGN-CRITICAL-PATH-20261106.okf.md`, `CURRENT-STATE.md`, `DECISIONS.md` | **KEEP (Root Control)** | Keep at project root; patch `CURRENT-STATE.md:1-18` (remove stale `D017 Sunday off` banner) and keep `DECISIONS.md` thin-pointer clean. |

---

## 5. Master Verification Checklist Before Touching `Recap Day` / `Precap Day`

1. **OKF & Reference Check:** `python apex-meta/scripts/okf_validator.py --target ...` passes cleanly (`0` errors) across all governed bundles.
2. **Static Drift Sweep (`CDL-04`):** `rg -n "Sun OFF|Sunday OFF|21:00|Mon-Sat|Monday-Saturday|WP-BIZ-01|WP-APEX-01|daily_seed_map|Seq 1:" .claude/skills/PrecapWeek/ apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/` returns zero active contradictions (only explicit historical/archive files).
3. **Production Runtime Proof (`D011`):** Fresh forked `PrecapWeek` chat (no handover memory) takes a sample `Operator Weekly Command Brief`, calls live/fallback OP & Calendar + `week-blueprint.json` + `T2`, produces valid Cockpit + unified `presentation_handoff`, and `PrecapNextDay` (`Module 02`) accepts that handoff cleanly!
4. **Cross-Repo Parity (`DD-15`):** `MasterOfArts` -> `sync_dispersal.py` -> `apexai-os-meta` runs cleanly with zero unexpected diffs.

## 6. Fresh-Chat Starter Prompt (Run ONLY After Chats `01–06` Complete)

```text
Read apex-meta/tools/project-improvement-orchestration-weekly/precap-week-handovers/07-MACRO-RETURN-AND-ARCHIVE-MAP.md and 00-RULE-CANONICAL-DECISION-LOCK.md.
Modules 01–06 are now complete. Verify interface compatibility across Operator Command Brief -> PrecapWeek (Compass 00, Decisions 01, Matrix 1 02, Matrix 2 03, Residuals 04, Sequencing 05) -> PrecapNextDay, synchronize CURRENT-STATE.md & DECISIONS.md, execute the git mv archival of superseded files in 01-weekly-command-brief/ per ARCHIVE-POLICY.md, run the static rg drift sweep, and trigger one fresh D011 forked-skill smoke test.
```
