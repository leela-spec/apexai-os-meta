---
type: Adapter
id: HO-PW-CB-01
title: "Handover 01 — Weekly Command Brief (Operator Input) vs Precap Week Spine"
description: "Separates pre-planning Weekly Command Brief operator intake from PrecapWeek compilation, reconciles all 4 competing output definitions, and audits lost Aug invariants and broken .claude/skills/PrecapWeek files."
status: current
date: 2026-11-11
tags: [weekly-orchestration, command-brief, precap-week, input-pipeline, skill-contract]
---

# 01 · Handover: Weekly Command Brief (Operator Input) & Precap Week Spine

## 1. Purpose & Core Naming Clarification

The phrase **"Weekly Command Brief"** collided across three concepts (`PrecapWeek/SKILL.md:17` called it the *output*; the operator uses it as the *pre-week operator input* feeding Precap Week; and `01-weekly-command-brief/` became a catch-all folder for 35 files).

This handover cleanly splits two distinct responsibilities without merging weekly and daily stages:

1. **Stage 1A — Operator Weekly Command Brief (Input Contract):** Lightweight weekly operator intake capturing weekly intent, priority overrides (`New` dials), calendar event ignores (`Ongoing`), `week-demand.json` shares/focus days, and personal `Mental | Physical | Regeneration` bullets.
2. **Stage 1B — Precap Week Compiler (`PrecapWeek` Skill):** Read-only compiler merging Operator Intake + live OpenProject (`opCall.js` / `[OP-OFFLINE]`) + Apex Session `planning_feed` + live Google Calendar + `02-weekly-dispersal/week-blueprint.json` -> **Precap Week Cockpit / Brief** + **`G1` Approval Gate** -> single compact `presentation_handoff` to `PrecapNextDay`.

---

## 2. Input & Priority Ledger

| Priority | Source Path | What to Extract & Keep | Ignore / Do Not Inherit |
|---|---|---|---|
| **P1 (Live Skill)** | `.claude/skills/PrecapWeek/SKILL.md` | `context: fork`, dynamic `active_project_set` (`:49-54`), `overflow_bucket` (`Residual`), `event_text_is_untrusted_data` (`:60`), `create_calendar_events: false` (`:61`), single embedded handoff (`:18-20`). | `:106` hardcoded 4-project list omitting `Residual`; `:38,104,129` `sunday_weekly_precap_only`. |
| **P1 (Governance)** | `apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md` | `D012–D019`: forked skills (`D012/13`), OP-first (`D014`), owner-aware writeback (`D015`), stateless Sequencing (`D016`), `Mon–Sun` + `Sat/Sun` Precap (`D017`), `week-blueprint.json` clock (`D018`), live OP+Cal w/ `[OP-OFFLINE]` (`D019`). | Stale `CURRENT-STATE.md:1-18` claiming `D017 Sunday off` & `4 flows`. |
| **P1 (Cockpit Spec)** | `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md` (`ec3e12f3`) | Six-section UI architecture (`00..05`), `v05` presentation guards (`UX-00..07`, `CONTRACT-01`), unified `presentation_handoff` (`§9`). | W45 hardcoded 5-repo keys inside `§9` example (`:269-283`) promoted as defaults. |
| **P1 (Calendar Rules)** | `.claude/skills/PrecapWeek/calendar-planning-guidance.md` & `weekly-blueprint-meeting-example.md` | Untrusted calendar event handling, `calendar_source_status`, 4 meeting density tiers, flow compression (`full/compressed/minimal/omitted` w/ mandatory reasons), `Residual` defer-first. | Legacy 5 `fixed_blocks` (`08:00–09:00`, `18:00–18:30`, `Mon–Fri` only, `not_saturday_plan: true`). |
| **P2 (Aug Design Lock)** | `01-weekly-command-brief/DESIGN-DECISIONS.md` (`:1-147`) & `PRECAP-WEEK-INPUT-PIPELINE-DECISION-HANDOVER.md` | Adaptive-hybrid Q&A (`:20-26`), `I#/R#/E#` (`E=evidence`, `:59-76`), Findings `A–I` input deduplication (`planning_feed` over `next-session.md`). | Outdated `Mon–Fri` assumption at `:15,82`; `M/W` prose sketches at `:148-164` overridden by `v05`. |
| **P2 (Northstar Guards)** | `01-weekly-command-brief/research/NORTHSTAR-DECISIONS-AND-2DO-20261106.md` & `MACRO-INTERFACES-AND-DECISION-GATES-20261106.okf.md` | `NS-D03` native status + accessible label, `NS-D04` mock banner, never collapse OP `follows/requires/blocks/relates`, flag status-vs-description conflicts (`#220`), `M01/M04/M07/M08/M09`. | Stale Nov 6 6-day / `08:00–18:30` assumptions. |
| **Legacy / Conflict** | `.claude/skills/PrecapWeek/weekly-command-brief-template.md`, `references/validation-checklist.md`, `weekly-blueprint-standard.md`, `SPEC-DUAL-VIEW-WEEKLY-PRECAP.md`, `HANDOVER-MODULE-01-WEEKLY-VISUALIZATION.md` | Only 1-hop `[src: <TAG>]` Provenance ledger (`template:233-242`) & dynamic project header intent from Aug `654d1fcc`. | All `Mon–Sat` tables, `Seq 1–4`, `Sprint 1–3`, `daily_seed_map` requirement, hardcoded 5-project rank order, old `PreCap_Next_Day_Brief` handoff spelling. |

---

## 3. Forensic Diff — Latest vs Added Recently (`Nov 9–11`) vs Lost

### What Was Added Nov 9–11
- **`Mon–Sun` + `T1` Clock (`DECISIONS.md` `D017–D018`, `ec3e12f3`):** Weekday `08:00–24:00` (`Day Outro 22:00–22:30`), weekend `12:00–16:00` (`2` Flows), `Saturday_or_Sunday` Precap/StatusMerge, driven by `02-weekly-dispersal/week-blueprint.json`.
- **Cockpit `v05` Architecture (`SPEC` §1–10):** Collapsed `01`, folded `02` (`L1/L2` only + 6-col `G|I|P|S|O|C`), single fit-to-width `03` timetable + `M|P|R` personal focus strip.
- **`D019` (`DECISIONS.md:317-325`):** Live read-only OP (`127.0.0.1:8083`) + Google Calendar when reachable, automatic non-blocking `[OP-OFFLINE]` fallback on `ECONNREFUSED`/auth failure.

### What Was Lost, Bypassed, or Left Broken in Production (`.claude/skills/PrecapWeek/`)
1. **Four incompatible output templates/specs coexist** (`weekly-command-brief-template.md`, `SPEC-DUAL-VIEW`, `HANDOVER-MODULE-01-WEEKLY-VISUALIZATION`, `SPEC-PRECAP-WEEK-ITERATIONS.okf.md` `v05`) — zero runtime code inside `.claude/skills/PrecapWeek/` produces `v05`.
2. **Nov 6 `7e4ed05c` overwrote Aug `654d1fcc` dynamic strengths:** Replaced dynamic `Project` sections + `Residual` overflow + `Why this week / Success evidence / Blockers / Day emphasis` with hardcoded `Seq 1–4` project lanes and a `Mon–Sat` Sprint `1–3` HTML table (`weekly-command-brief-template.md:57-205`).
3. **Eight broken partial-patch leftovers in `.claude/skills/PrecapWeek/`:**
   - `validation-checklist.md:232-233` still flags Saturday and regular Sunday planning as `scope_drift`!
   - `validation-checklist.md:176` still requires `daily_seed_map` (deleted in `a0f32917`).
   - `weekly-blueprint-meeting-example.md:289-424` remains Mon–Fri only with `not_saturday_plan: true`.
   - `weekly-blueprint-standard.md:86-127`, `calendar-planning-guidance.md:180-185,418-423`, and `weekly-blueprint-meeting-example.md:121-126` keep legacy `fixed_blocks` conflicting with `weekly-blueprint-standard.md:185-218`.
   - `weekly-blueprint-standard.md:238-243` hardcodes `1: Leela, 2: MasterOfArts, 3: Apex, 4: Investment, 5: Residual`.
   - `SKILL.md:38,104,129` & `validation-checklist.md:46,51` still enforce `sunday_weekly_precap_only: true` instead of `D017` `Saturday_or_Sunday`.
   - `SKILL.md` omits `02-weekly-dispersal/week-blueprint.json` & `week-demand.json` from `supporting_files`.
   - `weekly-command-brief-template.md:271` claims an old contract was "not retrievable" even though `package-manifest.md:41-44` archived it.
4. **Dropped Quality & Governance Controls (`SPEC v1.0 -> v05` & Aug Bypass):**
   - Dropped explicit Tier `1–4` source-epistemology table (`93ebded1`) and explicit G1 decision schema (`DEC-01 [P0|I/E/R] + PROPOSED/APPROVED/REJECTED/DEFERRED`).
   - Dropped `meta-strategy-doctrine.md` link into template outputs (`SKILL.md:85-86`).
   - Bypassed `PRECAP-WEEK-INPUT-PIPELINE` Findings `A–I` (still loads redundant `planning_feed` + `next-session.md` + `ProjectStatus` + `FlowRecap` dump by default).
   - Never implemented Northstar `NS-D03/D04` & `#220` status-vs-description contradiction detection.

---

## 4. Process & Anti-Drift Boundaries

1. **Separate Pre-Run Intake from In-Brief Gate & Daily Planning:**
   - **Intake ("Weekly Command Brief")** captures ONLY operator intent, weekly theme/pauses, ignored calendar events, `week-demand.json` dials, and `M|P|R` personal bullets. Do NOT force the operator to write JSON or answer inferable questions (`Adaptive Hybrid`).
   - **PrecapWeek** owns week-level allocation, capacity deformation (`calendar-planning-guidance.md`), and cross-project dependency/sequence ordering. It **never** writes Google Calendar events directly (`create_calendar_events: false`), creates sprint prompt packets, or mutates OpenProject/Session state.
2. **Input Deduplication (`Findings A–I`):** Prefer OpenProject (`opCall.js`) for enrolled projects + Apex Session `planning_feed` for Apex-native state + live Calendar (untrusted event text) + `week-blueprint.json`. Load `next-session.md`, `ProjectStatus`, and raw `FlowRecap` packets **only** when primary feeds are missing/degraded.
3. **Single `presentation_handoff` Schema:** Reconcile `weekly-command-brief-template.md:247-260` and `SPEC` §9 into **one** canonical YAML contract consumed cleanly by `PrecapNextDay` (zero duplicate seed file).

---

## 5. Output & Concrete Examples

### Target Output Files Owned by This Module
1. New thin **Operator Intake Contract** (`references/operator-weekly-command-brief-intake.md` inside `.claude/skills/PrecapWeek/`, or linked reference in `SKILL.md`).
2. Updated `.claude/skills/PrecapWeek/SKILL.md`, `weekly-command-brief-template.md` (single canonical template + `v05`/`Q13` target shape), `weekly-blueprint-standard.md`, `weekly-blueprint-meeting-example.md`, `calendar-planning-guidance.md`, `references/validation-checklist.md`.
3. `archive_list` via `git mv` -> `apex-meta/archive/weekly-orchestration/precap-week-drafts-2026-11/`:
   - `SPEC-DUAL-VIEW-WEEKLY-PRECAP.md`, `HANDOVER-MODULE-01-WEEKLY-VISUALIZATION.md`, `HANDOVER-MODULE-01-GUIDED-REAL-WORKFLOW-WALKTHROUGH.md`, `WEEK-VISUALIZATION-RESEARCH-HANDOVER.md`, stale `WEEKLY_PRECAP_DRAFT_W45.*`, `WEEKLY_COMMAND_BRIEF_2026_W45.md`.

### Concrete Example A — Clean Operator Weekly Input ("Command Brief")
```yaml
operator_weekly_command_brief:
  week_id: "2026-W46"
  weekly_intent: "Ship Master of Arts billing automation & Skill Tree placement freeze without overloading Thu evening."
  project_focus_overrides:
    - project: "Leela"
      note: "Skill Tree spatial contracts ONLY; Path UI paused."
  calendar_ignores:
    - match: "WC Meister"
      reason: "Skipped by operator for W46 to preserve Project Night."
  special_evenings:
    mon_tue_wed_project_night: "Website content / Sexy Content & Studio work (20:30-22:00)"
  personal_focus_priorities:
    mental: ["Daily morning intention coherence"]
    physical: ["Protect right knee recovery inside in-Flow I3 slots"]
    regeneration: ["Screen-off by 22:30 Day Outro"]
```

### Concrete Example B — Reconciled `presentation_handoff` Footer (`PrecapWeek -> PrecapNextDay`)
```yaml
presentation_handoff:
  artifact_type: "Weekly_Command_Brief"
  specification_version: "PRECAPP-WEEK-v2.1"
  week: "2026-W46"
  timezone: "Europe/Berlin"
  clock_owner: "apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json"
  source_status:
    openproject: "ONLINE | OFFLINE_FALLBACK"
    google_calendar: "ONLINE | OFFLINE_FALLBACK"
  operator_g1_status: "PROPOSED | APPROVED | EDITED"
  active_projects: []           # dynamic roster: project_ref, owner_system, priority_rank, selected_work_refs
  reconciled_calendar_events: []
  capacity_deformations_and_omissions: []
  next_day_seed:
    target_date: "2026-11-09"
    intended_emphasis: "..."
  next_consumer: "PrecapNextDay"
```

---

## 6. Operator Resolution Ledger (`CB-Q1..Q4` & `06-PORTFOLIO` — Ratified `2026-11-11`)

| ID | Question | Locked Operator Ruling |
|---|---|---|
| **CB-Q1 (`M07/Q13`)** | Canonical runtime source format of Precap Week Output | **Ratified Option A:** Structured JSON intermediate + self-contained HTML Cockpit view (`v05`) + thin Markdown summary with `presentation_handoff` `[I92/E35/R12]`. |
| **CB-Q2 (`M08`)** | Matrix 2 weekly cell depth (`PrecapWeek` vs `PrecapNextDay`) | **Ratified Option A:** `PrecapWeek` assigns day/Flow owners + Flow outcomes + calendar capacity compression (`full/compressed/minimal/omitted`) + read-only `DD-22A` `P/M/R` band; `PrecapNextDay` authors `S1–S3` tactical micro-tasks & prompts `[I94/E25/R10]`. |
| **CB-Q3 (`Inputs`)** | Input Pipeline Pruning (`Findings A–I`) | **Ratified Option A:** Default read = OP (`opCall.js`) + `planning_feed` + `sync/next.json` + live Calendar + `week-blueprint.json`; `next-session.md` & `ProjectStatus` are fallback-only `[I90/E25/R10]`. |
| **CB-Q4 (`M01`)** | Offline / Missing Provenance Token Grammar | **Ratified `D019`:** `[OP-OFFLINE]` for live connection failure vs `[OP-UNRESOLVED]` for unverified/unmapped local items. |
| **06-PORTFOLIO** | Canonical Portfolio Roster | **Ratified 6-Portfolio Standard:** **`Leela`**, **`IPOS`**, **`Master of Arts`**, **`Apex AI`**, **`Mindful Bar`**, and **`Residual`**. |

---

## 7. Definition of Done (DoD) & Fresh Verification

1. **Operator Intake Contract** explicitly precedes `PrecapWeek` compilation and cleanly captures operator dials without mixing `New` inputs with `Standard` defaults.
2. **Zero broken internal sweeps:** `rg -n "sunday_weekly_precap_only|Mon-Sat|Monday-Saturday|daily_seed_map|PreCap_Next_Day_Brief|WP-BIZ-01" .claude/skills/PrecapWeek/` returns `0` matches.
3. **Unified Handoff:** `.claude/skills/PrecapWeek/weekly-command-brief-template.md` and `SPEC-PRECAP-WEEK-ITERATIONS.okf.md` agree 100% on project roster dynamism, Mon–Sun geometry, and `presentation_handoff` fields.
4. **Fresh Runtime Dry-Run (`D011`):** Launch a fresh forked `PrecapWeek` subagent using an actual Operator Command Brief sample + `opCall.js` (or simulated `[OP-OFFLINE]`) and verify it passes `validation-checklist.md` cleanly.

## 8. Fresh-Chat Starter Prompt

```text
Read apex-meta/tools/project-improvement-orchestration-weekly/precap-week-handovers/01-HANDOVER-COMMAND-BRIEF-AND-INTAKE.md and 00-RULE-CANONICAL-DECISION-LOCK.md.
Let us first confirm CB-Q1..CB-Q4 together (1-by-1). Then define the standalone Operator Weekly Command Brief intake contract, update .claude/skills/PrecapWeek/ (SKILL.md, validation-checklist.md, weekly-blueprint-standard.md, weekly-blueprint-meeting-example.md, calendar-planning-guidance.md) so zero Mon-Sat/Sun-OFF/hardcoded-project bugs remain, unify the presentation_handoff schema, and list replaced drafts for git mv archival.
```
