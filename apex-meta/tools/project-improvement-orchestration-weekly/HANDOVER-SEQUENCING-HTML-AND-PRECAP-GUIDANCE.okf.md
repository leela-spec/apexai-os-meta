---
type: Handover
id: HANDOVER-SEQUENCING-HTML-AND-PRECAP-GUIDANCE-v1.0
title: "Design Handover — HTML Cockpit Sequencing Logic & PrecapWeek / PrecapNextDay Guidance"
description: "4-Dimensional handover (backed by INDEX-SEQUENCING-ONLINE-AI.okf.md) to design PrecapWeek HTML weekly sequencing decisions (#s03/#s05), Project-Day/Gaussian blueprint allocation, and concrete Chunk hydration in PrecapNextDay."
status: draft
date: 2026-11-12
scope: [weekly-orchestration, sequencing, dispersal, precap-week, precap-next-day, html-cockpit]
tags: [weekly-orchestration, sequencing, handover, precap-week, precap-next-day, html-cockpit, okf-v02]
references: [INDEX-SEQUENCING-ONLINE-AI.okf.md, 01-weekly-command-brief/SPEC-SEQUENCING.okf.md, 01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md, 02-weekly-dispersal/SPEC-WEEKLY-DISPERSAL.okf.md, 02-weekly-dispersal/ALGORITHM.md, 02-weekly-dispersal/EPICS-SCHEMA.md, 02-next-day-brief/README.md]
---

# Design Handover — HTML Cockpit Sequencing Logic & PrecapWeek / PrecapNextDay Guidance

## Section 1 — Operator Model vs. Verified Code Gaps (`As-Is` vs `Target`)

The target **Sequencing Architecture** separates quiet foreground operator choices from the background timing engine:
1. **HTML Cockpit Foreground (`PrecapWeek` `#s03 / #s05`)**: Shows only the **operator-decided Epics & Chunks standard** and **concise Project-Day alignments**. Gaussian focus curves and Epic band slot targets run strictly in the background.
2. **Craft (`C`) Owned by Matrix 1 & Flows**: Actual project tasks (`C1..C3`) come directly from **Matrix 1** (`selected_work_reference[]`) and execute inside Flows, never from `epics.json` micro-chunks.
3. **Background Dispersal Engine (`02-weekly-dispersal/`)**: `epics.json` + `week-demand.json` + `allocate_week.py` apply the **Gaussian focus window (`P` and `M`)** and compute **Epic band slot targets** (`week-allocation.json`), feeding both `PrecapWeek` and `PrecapNextDay` (`PrecapDay`).

Four verified code gaps currently block this design:

1. **HTML Foreground Clutter (`render_precap_cockpit.py` `#s05`)**: [`_render_sequencing_html()`](01-weekly-command-brief/render_precap_cockpit.py#L735-L793) currently surfaces background math (`TP/XP/BP`, $\sigma = 6.0\text{h}$) instead of cleanly displaying the operator's decided Epics/Chunks standard and concise Project-Day alignments.
2. **Gaussian Missing on Mental (`M`) (`allocate_week.py`)**: [`allocate_week.py`](02-weekly-dispersal/allocate_week.py#L187-L338) runs `gaussian_evening_weight()` (`19:00`, $\sigma=6.0\text{h}$) only on **`P`**, leaving **`M`** on a flat `1.15x` `focus_days` bump. Operator confirmed Gaussian coupling must score **`M` too**.
3. **Craft (`C`) Misplaced in `epics.json` & `allocate_week.py`**: [`allocate_week.py`](02-weekly-dispersal/allocate_week.py#L268-L358) cycles a hardcoded 9-item list (`c_portfolio_cycle`) bound to 1 generic placeholder chunk per Portfolio in [`epics.json`](02-weekly-dispersal/epics.json#L427-L470) instead of letting Matrix 1 own `C` Flow tasks while dispersal governs `P/M/R`.
4. **Disconnected `PrecapWeek` & `PrecapNextDay` Guidance**: `.claude/skills/PrecapWeek/SKILL.md` lacks the background-to-foreground Epics/Chunks dial step, and `.claude/skills/PrecapNextDay/SKILL.md` + `02-next-day-brief/README.md` do not yet pull background slot bands (`week-allocation.json`), Matrix 1 `C` tasks, or compressed Flow rules.

---

## Section 2 — Input & Priority Ledger (`EM-09 §5.1`)

Read sources in strict priority order before proposing UX or runtime edits:

| Priority | Source / Owner | Required Extract | Explicitly Exclude / Ignore |
|:---:|---|---|---|
| **P0** | [`INDEX-SEQUENCING-ONLINE-AI.okf.md`](INDEX-SEQUENCING-ONLINE-AI.okf.md) | Complete relative-path map across `apexai-os-meta` + `MasterOfArts`, settled `D014–D021` digest | Assuming an online AI can run local QMD commands |
| **P1** | [`01-weekly-command-brief/SPEC-SEQUENCING.okf.md`](01-weekly-command-brief/SPEC-SEQUENCING.okf.md) & [`01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md`](01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md) | Section `05` contract, `2,880m / 240` slot accounting (`§3.1`), `D1–D3` calm clarity rules | Archived `SPEC-PRECAP-WEEK-ITERATIONS.okf.md` |
| **P1** | [`02-weekly-dispersal/SPEC-WEEKLY-DISPERSAL.okf.md`](02-weekly-dispersal/SPEC-WEEKLY-DISPERSAL.okf.md), [`ALGORITHM.md`](02-weekly-dispersal/ALGORITHM.md), [`EPICS-SCHEMA.md`](02-weekly-dispersal/EPICS-SCHEMA.md) | `WD-01..48`, `XP/TP/BP` rules, `DD-15` mirror boundary, `epics.json` schema | Duplicating solver formulas in foreground HTML |
| **P1** | [`02-weekly-dispersal/week-demand.json`](02-weekly-dispersal/week-demand.json), [`allocate_week.py`](02-weekly-dispersal/allocate_week.py), [`week-allocation.json`](02-weekly-dispersal/week-allocation.json) | Background slot/band generation, `M/P` Gaussian coupling gaps, `R` rotation | Putting `C` project tasks into `epics.json` |
| **P2** | [`01-weekly-command-brief/render_precap_cockpit.py`](01-weekly-command-brief/render_precap_cockpit.py) & [`schemas/presentation-handoff.schema.json`](01-weekly-command-brief/schemas/presentation-handoff.schema.json) | `#s03` Matrix 2 cells (`L488-684`), `#s05` (`L735-793`), `PRECAP-WEEK-HANDOFF-v2.1` | Verbose Gaussian math or solver band dumps in HTML |
| **P2** | [`.claude/skills/PrecapWeek/SKILL.md`](../../../.claude/skills/PrecapWeek/SKILL.md), [`.claude/skills/PrecapNextDay/SKILL.md`](../../../.claude/skills/PrecapNextDay/SKILL.md), [`02-next-day-brief/README.md`](02-next-day-brief/README.md) | Live runtime procedures, `F1..F4` Flow Cards, Matrix 1 -> Flow `C` execution | Aug `Mon–Sat` / `Seq 1–4` legacy patterns |
| **P3** | `MasterOfArts/Sequencing/` (`decisions.md`, `dispersal/`), [`SEQUENCING-SKILL-CAPABILITY-BACKLOG-20261106.okf.md`](../../archive/weekly-orchestration/precap-week-research-2026-11/research/SEQUENCING-SKILL-CAPABILITY-BACKLOG-20261106.okf.md) | Upstream `MasterOfArts` Sequencing rationale (`N05`, `Q13` Option A visuals) | Retired `Seq 1–4` HTML tables as live rules |

### Design Decisions & Locked Operator Rulings
- **Locked (`2026-11-12` · HTML Foreground vs. Background Split):** `#s05` / `#s03` HTML shows **only** the operator-decided **Epics & Chunks standard** plus **very short Project-Day alignments**. Gaussian focus curves and Epic band slot targets remain **background mechanics** feeding both `PrecapWeek` and `PrecapNextDay`.
- **Locked (`2026-11-12` · Craft = Flows / Matrix 1):** Craft (`C`) is always executed via **Flows** from **Matrix 1** (`selected_work_reference[]`), never via `epics.json` micro-chunks.
- **Locked (`2026-11-12` · Gaussian Coupling on `M` Too):** Evening Gaussian coupling (`19:00`, $\sigma = 6.0\text{h}$, $w_{\max} = 1.5\times$, no Fri→Sat bleed) applies to **both Physical (`P`) and Mental (`M`)** inside the background engine.
- **`D-SEQ-01` (`PrecapNextDay` Chunk Selection Timing):** Keep concrete `P/M/R` `CH_*` Chunk selection in `PrecapNextDay` (reading `epics.json` + background bands + `FlowRecap`), while `#s05` HTML renders only the operator's approved weekly Epics/Chunks standard.
- **`D-SEQ-02` (Retire `C` Micro-Placeholders in `allocate_week.py`):** Stop hardcoding `c_portfolio_cycle` against 1 generic chunk per Portfolio in `epics.json`; map Flow Craft ownership directly from Matrix 1 `selected_work_reference[]` + short Project-Day rules.
- **`D-SEQ-03` (Compressed Flow Degradation Policy):** Define precedence when calendar collisions cut a `120m` Flow (`-30m` or `-60m`): trim Matrix 1 `C` sprints first while preserving `P` (`Knee`), `M`, and closing `R` (`12m`), vs. proportional trim.
- **`D-SEQ-04` (Operator Demand Override in `PrecapWeek`):** Allow Stage 1A Q&A to emit a week-scoped Epics/Chunks standard & dial delta before compiling `week-allocation.json`, vs. editing `week-demand.json` upstream.

---

## Section 3 — Process & Design Workstreams (`EM-09 §5.1`)

Execute in three ordered phases under a pre-action `<align>` check:

1. **Track A — HTML Cockpit Sequencing View (`render_precap_cockpit.py`)**:
   - Read background outputs (`week-demand.json`, `week-allocation.json`, `epics.json`) inside `compute_dispersal_stats()` and `build_runtime_payload()` without exposing solver math in the UI.
   - Simplify `#s05` (`_render_sequencing_html()`) and `#s03` (`_wk_flow_cell()`) per locked foreground rules:
     - **Decided Epics & Chunks Standard (`#s05`)**: Display only the operator-locked weekly Epics/Chunks standard (`P/M/R` shares, pins, active Chunk sets).
     - **Short Project-Day Alignments (`#s05` & `#s03`)**: Render compact day-to-focus labels (`focus_days` / Project Days) without sprawling slot tables.
     - **Background Coupling Only**: Keep the `M/P` Gaussian focus window (`19:00`, $\sigma = 6.0\text{h}$) and Epic band slot targets in the background data layer feeding `PrecapWeek` and `PrecapNextDay`.
2. **Track B — Later `PrecapWeek` & Background Solver Guidance**:
   - Update `.claude/skills/PrecapWeek/SKILL.md` and `references/operator-weekly-command-brief-intake.md` with a concise **Sequencing Standard & Project-Day Step**: confirm the operator's `P/M/R` Epics/Chunks standard and short Project-Day alignments, route all Craft (`C`) work through **Matrix 1 -> Flows** (`D-SEQ-02`), run background `allocate_week.py` (with Gaussian coupling enabled on **both `P` and `M`**), then compile HTML + OKF Brief + `presentation_handoff`.
   - Keep `wXX-reference-weekly-command-brief.okf.md` under `100` lines by summarizing only deltas, Project-Day choices, and approved weekly standard (`§05`).
3. **Track C — Later `PrecapNextDay` (`PrecapDay`) Hydration (`02-next-day-brief/` & `.claude/skills/PrecapNextDay/`)**:
   - Wire `PrecapNextDay` intake to read both **Matrix 1 Flow Craft (`C`) tasks** (`selected_work_reference[]`) and background **Sequencing targets** (`presentation_handoff.dispersal_owner` -> `week-allocation.json` + `epics.json`).
   - Author daily Sequencing guidance covering: (a) hydrating `F1..F4` Flow Cards (`S1..S3`) with Matrix 1 Craft (`C1..C3`) sprints plus concrete `P/M/R` **`CH_*` Chunks** from `epics.json` + yesterday's `FlowRecap`, (b) preserving `*_*_I3_P` Knee pins, (c) applying `D-SEQ-03` Flow compression under GCal collisions, and (d) emitting `alloc_id` / `chunk_id` hooks for `FlowRecap` -> `StatusMerge`.

### Anti-Drift & Single-Owner Boundaries
- **Solver Authority (`DD-15`)**: Changes to `allocate_week.py`, `week-demand.json`, `epics.json`, or `SPEC-WEEKLY-DISPERSAL.okf.md` / `ALGORITHM.md` land upstream in `MasterOfArts/Sequencing/dispersal/` and mirror via `sync_dispersal.py --apply` (unless consolidated under a ratified repo decision).
- **Foreground vs. Background Wall**: Foreground HTML owns decided Epics/Chunks standard + short Project-Day labels; background `02-weekly-dispersal/` owns Gaussian curves + Epic band slot targets; Matrix 1 owns Craft (`C`) Flow tasks.
- **Calendar Safety**: `PrecapWeek` remains strictly read-only on Google Calendar; only `PrecapNextDay` proposes/writes `[FLOW]` blocks after explicit operator approval.

---

## Section 4 — Target Outputs & Worked Examples

### Target Files to Update Across Tracks
- **HTML & Compiler (`Track A`)**: [`01-weekly-command-brief/render_precap_cockpit.py`](01-weekly-command-brief/render_precap_cockpit.py), [`01-weekly-command-brief/SPEC-SEQUENCING.okf.md`](01-weekly-command-brief/SPEC-SEQUENCING.okf.md), [`01-weekly-command-brief/precap-week-cockpit-2026-W46.html`](01-weekly-command-brief/precap-week-cockpit-2026-W46.html) (recompiled).
- **Weekly Skill Guidance (`Track B`)**: [`.claude/skills/PrecapWeek/SKILL.md`](../../../.claude/skills/PrecapWeek/SKILL.md), [`.claude/skills/PrecapWeek/references/operator-weekly-command-brief-intake.md`](../../../.claude/skills/PrecapWeek/references/operator-weekly-command-brief-intake.md).
- **Daily Skill & Module 02 Guidance (`Track C`)**: [`02-next-day-brief/README.md`](02-next-day-brief/README.md), [`.claude/skills/PrecapNextDay/SKILL.md`](../../../.claude/skills/PrecapNextDay/SKILL.md), [`.claude/skills/PrecapNextDay/references/input-intake-and-resilience-contract.md`](../../../.claude/skills/PrecapNextDay/references/input-intake-and-resilience-contract.md), [`.claude/skills/PrecapNextDay/templates/flow-execution-card-template.md`](../../../.claude/skills/PrecapNextDay/templates/flow-execution-card-template.md).
- **Background Solver (`DD-15`)**: `C:/GitDev/MasterOfArts/Sequencing/dispersal/{week-demand.json, allocate_week.py, epics.json}` -> synced to `02-weekly-dispersal/`.

### Worked Example A — `PrecapWeek` Foreground HTML (`#s05` + `#s03`, Quiet Standard & Short Project Days)
```text
#s05 Decided Epics & Chunks Standard (Foreground):
  P Standard: Martial Arts (35%), Dance (25%), General (15%), Knee (15% *_*_I3_P), S/BJJ (10%)
  M Standard: Intention (40%), ACIM (20%), Surrender (20%), Breathing (20%) · R: Audiobooks/Nidra/Social (0 XP)
  Project Days (Short): Mon–Wed Project Night · Thu/Fri Freizeit · M Focus [Mon/Wed/Fri=Intention, Tue=Surrender, Thu=Breathing, Sun=ACIM]
  (Background Engine Only: P+M 19:00 Gaussian window + 240 Epic band slot targets feed Matrix 2 & PrecapNextDay)

#s03 Matrix 2 Cell (Thu · F2 · 10:30–12:30 · Compressed -30m):
  Craft (from Matrix 1): IPOS RI-11 + Apex Mod-02 (2 C sprints · C3 deferred)
  DD-22A Band (from Background): P [Martial Arts, Dance, Knee] · M [Breathing, Intention] · R [Audiobooks]
```

### Worked Example B — `PrecapNextDay` Flow Card Hydration (Matrix 1 `C` + Background Band + `epics.json`)
```text
Flow F2 (2026-11-12 Thu, 11:00–12:30 post Alex&Chris collision):
  Sources: Matrix 1 Craft Flows (`selected_work_reference[]`) + background `week-allocation.json` (`SO_THU_F2_*`) + `epics.json`
  Hydrated Flow Card:
    I1: P `CH_p_ma_strikes_2m` + M `CH_m_breathing_3m` + C1 [Matrix 1] IPOS RI-11 Replay (`30m`)
    I2: P `CH_p_dance_moves_2m` + M `CH_m_intention_3m` + C2 [Matrix 1] Apex Mod-02 Contract (`30m`)
    I3: P `CH_p_knee_iso_2m` (*_*_I3_P Pin) · C3 omitted per D-SEQ-03 -> Close R `CH_r_audiobooks_12m`
```

---

## Section 5 — Definition of Done & Verification Contract (`WP-25`)

The executing chat may claim completion only after all checks pass against live files:

1. **OKF & Schema Gates**: `python apex-meta/scripts/okf_validator.py --target apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief` exits `0`, and `render_precap_cockpit.py --validate-only` passes `Schema + T1/T2` checks.
2. **UI & Responsive Regression Gate**: Playwright inspection on desktop (`1440px`) and mobile (`<920px`) confirms `0` console errors, `scrollWidth <= clientWidth`, intact `#s00..#s05`, clean Epics/Chunks standard + short Project-Day labels in `#s05`, and zero solver/Gaussian clutter.
3. **Generality & Background Solver Check (`W47` Test)**: Running `allocate_week.py` confirms Gaussian weighting scores **both `P` and `M`** without Fri→Sat bleed, while `render_precap_cockpit.py` compiles a synthetic W47 payload cleanly with zero W46 leakage.
4. **Mirror & Boundary Check (`DD-15`)**: `sync_dispersal.py --check` verifies upstream alignment if solver files changed; Craft tasks trace strictly to Matrix 1 rather than `epics.json`.
5. **Failure-Mode Guards (`WP-25`)**:
   - **No Hardcoded Weekly Strings**: HTML and `PrecapNextDay` templates must read dynamically from Matrix 1 + `week-allocation.json` / `epics.json`, failing visibly (`[SEQ-MISSING]`) if absent.
   - **No Cross-Week/Weekend Bleed**: Background Gaussian coupling (`P` and `M`) must stop strictly before Saturday (`SEQ-D1`).
   - **Zero `R` XP Minting**: Any UI badge or daily card showing `XP > 0` for `Regeneration` breaks validation (`WD-03`).
   - **Unapproved G1 Blocker**: Daily `PrecapNextDay` cards fed by a `PROPOSED_FOR_G1` handoff must carry an explicit draft/review banner unless G1 is `APPROVED`.
