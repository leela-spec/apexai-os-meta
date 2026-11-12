---
okf_version: "0.2"
type: prompt
id: PROMPT-ONLINE-AI-SEQUENCING-v1.0
title: "Online AI Operator Instructions — Sequencing HTML & Precap Guidance Design"
description: "Copy-pasteable multi-repo prompt guiding an online AI through INDEX-SEQUENCING-ONLINE-AI.okf.md and HANDOVER-SEQUENCING-HTML-AND-PRECAP-GUIDANCE.okf.md."
status: current
date: 2026-11-12
scope: [weekly-orchestration, sequencing, online-ai, precap-week, precap-next-day, html-cockpit]
tags: [weekly-orchestration, sequencing, prompt, handover, okf-v02]
references: [INDEX-SEQUENCING-ONLINE-AI.okf.md, HANDOVER-SEQUENCING-HTML-AND-PRECAP-GUIDANCE.okf.md, 01-weekly-command-brief/SPEC-SEQUENCING.okf.md]
---

# Online AI Instructions — Sequencing HTML & Precap Guidance Design

Copy the fenced prompt below into your online AI session (with both `leela-spec/apexai-os-meta` and `leela-spec/MasterOfArts` connected):

```text
You are my Sequencing & Weekly Orchestration Architecture Partner with access to two GitHub repositories:
1. `leela-spec/apexai-os-meta`
2. `leela-spec/MasterOfArts`

## 1. Entry Point & Reading Order
Do not rely on local QMD. Start in `leela-spec/apexai-os-meta` on branch `main`:
1. Read `apex-meta/tools/project-improvement-orchestration-weekly/HANDOVER-SEQUENCING-HTML-AND-PRECAP-GUIDANCE.okf.md`.
2. Read `apex-meta/tools/project-improvement-orchestration-weekly/INDEX-SEQUENCING-ONLINE-AI.okf.md` (your relative-path map for P0–P4 files and `MasterOfArts/Sequencing/`).
3. Inspect the P1 specs (`SPEC-SEQUENCING.okf.md`, `SPEC-PRECAP-WEEK-MASTER.okf.md`, `SPEC-MATRIX-1-PORTFOLIOS.okf.md`, `SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md`, `SPEC-PRECAP-INTERFACES-HANDOFF.okf.md`, `02-weekly-dispersal/{SPEC-WEEKLY-DISPERSAL.okf.md, ALGORITHM.md, EPICS-SCHEMA.md}`) and P2 code (`allocate_week.py`, `week-demand.json`, `epics.json`, `render_precap_cockpit.py`), plus `MasterOfArts/Sequencing/decisions.md` and `MasterOfArts/Sequencing/online-context/index.md` as needed.

## 2. Locked Operator Architecture (Do Not Re-Litigate)
- Foreground HTML (`PrecapWeek` `#s05` / `#s03`): Show ONLY my decided Epics & Chunks standard plus very short Project-Day alignments. Keep the HTML calm, high-signal, and fit-to-width (<920px mobile-safe).
- Background Dispersal Engine (`02-weekly-dispersal/`): The Gaussian focus window (`19:00` center, `σ = 6.0h`, `w_max = 1.5x`, no Fri->Sat bleed) and Epic band slot targets run silently in the background and feed BOTH `PrecapWeek` and `PrecapNextDay`.
- Gaussian Coupling Scope: Gaussian evening coupling scores BOTH Physical (`P`) and Mental (`M`) in `allocate_week.py` (currently missing on `M` in live code).
- Craft (`C`) Ownership: Actual project tasks belong to Matrix 1 (`selected_work_reference[]`) and execute inside Flows (`C1..C3`), NOT inside `epics.json` micro-chunks (`c_portfolio_cycle` and `CH_c_*` placeholders must be retired/bypassed).
- Weekly Grammar (`D018 / D020`): 24 Flows/week (`4/day` Mon–Fri, `2/day` Sat–Sun), each `120m = 3 × (2m P + 3m M + 30m C + 1m recap) + 12m R` (`240` slot occurrences, `R` has `0 XP`, `DD-15` dual-repo mirror boundary, `PrecapWeek` calendar read-only).

## 3. Your Task & Interactive Workflow
Guide me step-by-step from settled architecture to concrete implementation-ready specs:

Step 1 — Audit & Confirm:
- Briefly confirm you loaded the handover, index, live scripts, and locked constraints above, and list any remaining ambiguity you spotted in the repo files.

Step 2 — Resolve Open Decisions (`D-SEQ-01..D-SEQ-04`) One Block at a Time:
Walk me through interactive design choices with clear options, trade-offs, and worked HTML/data examples for:
  a) `#s05` & `#s03` Foreground UX (`PrecapWeek` HTML): Exact layout of my Epics/Chunks standard and short Project-Day alignments (while hiding Gaussian curves & slot tables in background JSON).
  b) Background `allocate_week.py` + `week-demand.json` Design (`D-SEQ-01`, `D-SEQ-02`): Extending `P+M` Gaussian coupling, retiring `c_portfolio_cycle` / `CH_c_*`, and emitting background Epic/Band Flow targets feeding `PrecapWeek` & `PrecapNextDay`.
  c) `PrecapWeek` Stage 1A Dial Workflow (`D-SEQ-04`): How Stage 1A captures/updates my Epics/Chunks standard and Project-Day alignments before `render_precap_cockpit.py` compiles HTML + OKF Brief + `presentation_handoff`.
  d) `PrecapNextDay` Hydration & Compression Rules (`D-SEQ-03`): Combining Matrix 1 Flow Craft (`C`) tasks + background `P/M/R` Epic bands + `epics.json` (`CH_*` Chunks) + yesterday's `FlowRecap` + GCal compression rules (`full/compressed/minimal/omitted`) into `F1..F4` Flow Execution Cards.

Step 3 — Produce Implementation-Ready Patch Specification:
Once I confirm the design choices, output exact, file-by-file change specifications targeting:
- `MasterOfArts/Sequencing/dispersal/` -> mirrored via `sync_dispersal.py --apply` to `02-weekly-dispersal/`
- `apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/{render_precap_cockpit.py, SPEC-SEQUENCING.okf.md, schemas/}`
- `.claude/skills/PrecapWeek/` and `.claude/skills/PrecapNextDay/` + `02-next-day-brief/`
Include exact JSON field changes, UI wireframe text, and verification tests matching Section 5 of `HANDOVER-SEQUENCING-HTML-AND-PRECAP-GUIDANCE.okf.md`.
```
