---
type: Report
id: PRECAP-WEEK-BRIEF-2026-W46
title: "Weekly Command Brief — 2026-W46 (09–15 Nov 2026 (ISO W46))"
description: "OKF v0.2 executive weekly brief for 2026-W46 compiling Stage 1A intake, 6 Portfolio Areas, Mon-Sun blueprint clock, T2 dispersal totals, and PrecapNextDay handoff."
status: draft
date: 2026-11-11
tags: [weekly-orchestration, precap-week, command-brief, okf-v02]
---

# Weekly Command Brief — 2026-W46 (09–15 Nov 2026 (ISO W46))

> **Result state:** `READY_WITH_REVIEW` · **G1 gate:** `PROPOSED_FOR_G1`  
> **Direction:** Advance Leela Skill Tree crown §F.1-§F.5 (#234, 6/9 pass post QA-211) + repo-efficiency brief; ship IPOS YouTube/RSS breadth (#226) + RI-10 replay (#230-#233) post ADR-003 (#224); move Master of Arts 6 Flow video scripts (01..06) -> filming, Stage 3 Website IA (#246), and Flow PDF billing; prep Thu Thomas meeting ([CAL-GAP]), Module 02 PrecapNextDay & HANDOVER-12 (#139/#198/#222); run Mindful Bar Micro pass + Thu 10:00 Alex & Chris founder check (Q-26/Q-27, €3.50-€6.90 price test).  
> **Next action:** `RECONFIRM_MIDWEEK_G1 (Schedule Thu Thomas GCal hold [CAL-GAP], clear dup 'Chris' event, lock Wed F4 + Thu Chris decisions, then hand off to PrecapNextDay)`  
> **Review needed:** 3 live flags: (1) [CAL-GAP] Thu Nov 12 Thomas planning (2Dos.md: AI Orchestration 3x3 / OpenMausBot / skill env) missing on GCal + duplicate 'Chris' event at 10:00; (2) [OP-OFFLINE] 127.0.0.1:8083 ECONNREFUSED on Wed Nov 11; (3) Mindful Bar Q-26/Q-27 & UK mark 'Mindful Bar' wait on operator.  
> **Interactive Cockpit (`v0.5`):** [precap-week-cockpit-2026-W46.html](../precap-week-cockpit-2026-W46.html)

## 00 · Portfolio Compass (`T1 / T2` Grounded)

Capacity and sprint metrics derive directly from the weekly blueprint and allocation JSON.

| Metric | Value | Source Basis |
|---|---|---|
| **Net Craft Capacity (`T1`)** | `35.0h / 36.0h C` (`48.0h` gross) | `24` Flows (`72m` trailing recap inside `12.0h` P/M/R) `[src: CLK]` |
| **Weekly Flows (`Mon–Sun`)** | `24` (`20` Wkd / `4` Wknd) | Weekday `08:00–24:00` + Weekend `12:00–16:00` `[src: CLK]` |
| **3x3 Craft Sprints (`C1–C3`)** | `72` sprints (`240` slot_ids) | `3 × 30m` Craft per Flow + `DD-22A` P/M/R bands `[src: DSP]` |
| **6 Portfolio Areas** | `6 Areas · 15 L1 · 5 L2` | Canonical `06-PORTFOLIO` standard `[src: OP]` |
| **G1 Readiness & Overrides** | `PROPOSED_FOR_G1` (`3` overrides) | OP: `OFFLINE_FALLBACK` · Cal: `ONLINE` `[src: INT]` |

## 01 · Operator Decisions (`New` & `Ongoing` · `G1`)

Standard clock windows live solely in `02-weekly-dispersal/week-blueprint.json`.

- **`D-W46-01 · Mid-week 6-Portfolio frontier`** — `Leela Crown §F (#234) · IPOS RI-10/11 · MoA 6 scripts->filming · Apex Thomas & Mod02 · Mindful Bar Micro` (`G1: PROPOSED_FOR_G1`) *(Override: `Initial Nov 8 W46 projection (7 unscripted videos, Spec v0.2)` -> `Mid-week Wed Nov 11 re-baselining from live repo SHAs & 2Dos.md`)* `[src: INT]`
- **`D-W46-02 · Leela weekly scope & QA-211 depth lock`** — `Crown §F.1-§F.5 only (6/9 passing; Path UI paused)` (`G1: PROPOSED_FOR_G1`) *(Override: `All active Project #3/#9/#10/#11 work packages eligible` -> `Pause Path UI; ship Crown §F.1-§F.5 + spatial placement contracts`)* `[src: INT]`
- **`D-W46-03 · Schedule Thu Nov 12 Thomas planning ([CAL-GAP])`** — `Place Thu Thomas block on GCal (AI Orchestration 3x3, OpenMausBot, skill env)` (`G1: PROPOSED_FOR_G1`) `[src: INT]`
- **`D-W46-04 · Mindful Bar First-Test Micro & 5 Open Decisions`** — `20-60 friend tasting Micro pass + €3.50-€6.90 price test + Q-26/Q-27` (`G1: PROPOSED_FOR_G1`) `[src: INT]`
- **Ongoing:** `Standing ignore · Wed/Fri WC Meister (18:00-20:00)` — `Ignored ambient calendar hold` `[src: CLK]`
- **Ongoing:** `Protected event · Thu 12 Nov 10:00-11:00 (2 GCal entries)` — `Alex & Chris (C. Sgarz · -60m Craft)` `[src: CLK]`
- **Ongoing:** `Protected event · Thu 12 Nov 18:45-21:00` — `München Tanz (+ 18:15 commute buffer)` `[src: CLK]`
- **Ongoing:** `OpenProject [OP-OFFLINE] + Non-Blocking GCal Items` — `opCall.js doctor ECONNREFUSED; Nov 6-8 snapshots + W47 VPN cue` `[src: OP]`

## 02 · Matrix 1 Overview (`6 Portfolio Areas`)

Full `G|I|P|S|O|C` fields and `Tasks -> Subtasks` open interactively in the HTML Cockpit.

| Rank | Portfolio Area | `L1` Priority Outcomes (`WP` Ref) | `L2` Nice | Cross-Repo Edges |
|---|---|---|---|---|
| 1 | **Leela** | ⚡ Skill Tree Crown Engine §F.1–§F.5 (ST-G1 · 6/9 Pass) (`OP-WP#234`); ⚡ SpatialViewNode & Durable Placement Contracts (`OP-WP#159 / OP-WP#39 / OP-WP#48`) | Repo-Efficiency Over-Engineering Audit (Analysis-Only Brief) | — |
| 2 | **IPOS** | ⚡ ADR-003 Cleanup & RI-11 YouTube/RSS Intake Breadth (`OP-WP#224 (In progress) / OP-WP#226`); RI-10 Fixture Acceptance Replay & FRED/Cockpit Readiness (`OP-WP#230–#233`) | 60-Indicator Registry Widening & Activepieces Probation (#225) | — |
| 3 | **Master of Arts** | ⚡ Flow Video Series Production (01..06 Scripts -> Filming) (`[OP-UNRESOLVED]`); Website Stage 3 IA & First-Family Content Transformation (`OP-WP#163 / OP-WP#244–#249`); ⚡ The Art of Flow PDF Billing & Movement Client Compliance (`[OP-UNRESOLVED]`) | Sequencing Dispersal Engine T1/T2 Dirty Tree Cleanup | 🔗 Cross-Repo: Feeds IPOS Ingestion |
| 4 | **Apex AI** | ⚡ Thu Thomas Planning & ki-basis / OpenMausBot Setup (`OP-WP#139 ([CAL-GAP])`); Module 02 PrecapNextDay & Daily Loop Convergence (`OP-WP#198`); Layer-1 Contract Benchmark (HANDOVER-12) & 338-Test Audit (`OP-WP#222`) | KI-Basis Private vs Community Compose Environment Question | 🔗 Cross-Repo: Feeds Leela Skill Portability |
| 5 | **Mindful Bar** | ⚡ First-Test Micro Pass (20-60 Friends & Network Tasting) (`[OP-UNRESOLVED]`); ⚡ Thu 10:00 Chris Sync & 4-Track Decisions (Q-26/27, Price, UK Mark, QR) (`[OP-UNRESOLVED]`) | Resolve Mindful Bar OpenProject Skill Drift & OP Transfer | 🔗 Cross-Repo: Apex OP Skill Sync |
| 6 | **Residual** | Tonight Wed Project Night: Sexy Content, Dance & Studio Reset (`[OP-UNRESOLVED]`); Personal Errands: Ma, Bahn & BahnCard, Kilian (+ W47 Ghost VPN) (`[OP-UNRESOLVED]`); ACIM-Secular QA (Decads 24-37) & Lika-Community WSL Compose (`[OP-UNRESOLVED]`) | — | — |

## 03 · Matrix 2 Calendar Collisions & Personal Focus

The full `Mon–Sun` hourly timetable lives inside Section `03` of the HTML Cockpit.

| Date | Event | Window | Policy | Capacity Delta |
|---|---|---|---|---|
| `2026-11-11` | WC Meister | `18:00–20:00` | `ignored_ongoing` | `0m` |
| `2026-11-12` | Alex & Chris (+ dup 'Chris' GCal entry) | `10:00–11:00` | `protected` | `-60m` |
| `2026-11-12` | München Tanz commute buffer | `18:15–18:45` | `buffer` | `0m` |
| `2026-11-12` | München Tanz | `18:45–21:00` | `protected` | `0m` |
| `2026-11-13` | WC Meister | `18:00–20:00` | `ignored_ongoing` | `0m` |

- **Mental (`216m` in-Flow):** Daily Morning Intention coherence (Mon/Wed/Fri/Sun focus days · Tue Surrender · Thu Breathing); ACIM & Surrender presence across F1-F4 transitions & Thu meeting load
- **Physical (`144m` in-Flow + Evening Course):** Protect right knee recovery — Knee chunk pinned to `*_*_I3_P` slots (11/wk quota); Preserve 18:30-19:30 Evening Physical (Tonight Wed Dance · Fri Kicks · Thu replaced by München Tanz 18:45-21:00)
- **Regeneration (`288m` breaks · `0 XP`):** Protect 22:00-22:30 Day Outro boundary after Wed Project Night & Thu München Tanz; Rotate Audiobooks (11), Yoga Nidra (8) & Socializing (5) across 24 in-Flow R breaks (288m, XP = 0)

## 04 · Residual Information & 1-Hop Provenance

OpenProject status uses `[OP-OFFLINE]` (`OFFLINE_FALLBACK`); see Deferrals and 1-hop ledger below.

| `WP` Ref | Deferred Item | Reason | Revisit Trigger |
|---|---|---|---|
| `OP-WP#204` | MoA ACIM Secular Credits Page | Moved out of Matrix 1 L2 to Longlist Deferred. | After OP-WP#163 / OP-WP#246 Website Stage 3 IA sign-off. |
| `[OP-UNRESOLVED]` | MoA Stripe Webhook Integration | Staged future billing wave (Kleinunternehmer §19 UStG manual PDF pipeline prioritized first). | After first signed Flow client contract & Obsidian PDF billing verification. |
| `OP-WP#227` | IPOS Telegram Research Digest | Deferred Mission 2 summary behind OP-WP#232 per OP-REL#97. | After OP-WP#224, OP-WP#226 YouTube/RSS breadth & OP-WP#232 Unified Cockpit UX. |

| Tag | Source | Freshness |
|---|---|---|
| `[CLK]` | `../02-weekly-dispersal/week-blueprint.json` — Canonical Blueprint Clock (T1) | `CURRENT` |
| `[DSP]` | `../02-weekly-dispersal/week-allocation.json` — T2 Weekly Allocation & Dials | `CURRENT` |
| `[INT]` | `fixtures/w46-reference-intake.json` — Operator Intake (W46 Momentary) | `CURRENT` |
| `[GCAL]` | `gcalendar:readonly-2026-11-11` — Google Calendar Live Query (Nov 9-23) | `CURRENT` |
| `[GIT]` | `c585e805 / 4db6a00 / e0ec6ff / da2573c9 / ade47dc / 59ee64e` — Live 7-Repo SHAs, Handovers & 2Dos.md | `CURRENT` |
| `[OP]` | `../00-openproject-dependency-intake/EVIDENCE-20261106.okf.md` — OpenProject Intake Evidence [OP-OFFLINE] | `AGED` |
| `[CAR]` | `../../../informatics/final/operations/18-APEX-CARRIER-MAP.md` — Mindful Bar 6th Portfolio Carrier | `CURRENT` |

- **Confidence:** HIGH on live T1/T2 clock math, live GCal holds, and Wed 15:18 CET repo SHAs; MEDIUM on OpenProject sync ([OP-OFFLINE] 127.0.0.1:8083 ECONNREFUSED, Nov 6-8 snapshots active) and unscheduled Thu Thomas slot ([CAL-GAP]).
- **Assumptions:** Wed/Fri WC Meister 18:00-20:00 stays ignored (Ongoing); Thu duplicate 'Chris' GCal event maps to Alex & Chris (-60m once); Thu Thomas meeting places into Thu F3 unless operator picks another window.

## 05 · Sequencing Orientation (`T2` Allocation)

All `240` slot occurrences are bound dynamically by `allocate_week.py` (`DD-16`: zero BP floor).

- **Projected Yield (`[src: DSP]`):** `2,880m` TP (`2,808m` slots + `72m` recap) · `3,706.0` XP (`C 3,086.8`, `M 357.71`, `P 261.49`, `R 0.0`) · `BP 100.0` (`50/25/25`).
- **Gaussian Focus Coupling:** `σ = 6.0h` centered on `19:00` (`w_max = 1.5x`, zero Fri→Sat bleed).

## Compact Downstream Handoff (`PrecapWeek -> PrecapNextDay`)

```yaml
presentation_handoff:
  schema_version: "PRECAP-WEEK-HANDOFF-v2.1"
  artifact_type: "Weekly_Command_Brief"
  packet_id: "weekly-command-brief-20261111-2026-W46"
  produced_at: "2026-11-11T15:23:00+01:00"
  week: "2026-W46"
  date_range:
    start: "2026-11-09"
    end: "2026-11-15"
  timezone: "Europe/Berlin"
  clock_owner: "apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json"
  dispersal_owner: "apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-allocation.json"
  cockpit_html_ref: "apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/precap-week-cockpit-2026-W46.html"
  brief_okf_ref: "apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/fixtures/w46-reference-weekly-command-brief.okf.md"
  data_json_ref: "apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/fixtures/w46-reference-cockpit.json"
  result_state: "READY_WITH_REVIEW"
  operator_g1_status: "PROPOSED_FOR_G1"
  source_status:
    openproject: "OFFLINE_FALLBACK"
    google_calendar: "ONLINE"
  weekly_intent: "Advance Leela Skill Tree crown §F.1-§F.5 (#234, ST-G1; Path paused) & repo-efficiency brief (#39); expand IPOS YouTube/RSS intake breadth post-ADR-003 (#224/#226) + run RI-10 fixture replay (#230-#233); convert Master of Arts 6 Flow video scripts (01..06) to filming, advance Stage 3 Website IA (#246), and prep Movement/Flow PDF billing; align Thu Nov 12 Thomas planning (AI Orchestration 3x3, OpenMausBot, skill env — [CAL-GAP] to schedule) + Module 02 PrecapNextDay & HANDOVER-12 (#139/#198/#222); run Mindful Bar Micro pass + Thu 10:00 Alex & Chris founder check (Q-26/Q-27, €3.50-€6.90 price test, 20-60 friend tasting)."
  six_portfolio_areas:
    - portfolio_id: "leela"
      label: "Leela"
      priority_rank: 1
      priority_goals:
        - "Skill Tree Crown Engine §F.1-§F.5 (ST-G1 · 6/9 Pass)"
        - "SpatialViewNode & Durable Placement Contracts"
      selected_work_refs:
        - "leela-crown:OP-WP#234"
        - "leela-spatial:OP-WP#159/#39/#48"
    - portfolio_id: "ipos"
      label: "IPOS"
      priority_rank: 2
      priority_goals:
        - "ADR-003 Cleanup & RI-11 YouTube/RSS Intake Breadth"
        - "RI-10 Fixture Acceptance Replay & FRED/Cockpit Readiness"
      selected_work_refs:
        - "ipos-intake:OP-WP#224/#226"
        - "ipos-acceptance:OP-WP#230-#233"
    - portfolio_id: "master_of_arts"
      label: "Master of Arts"
      priority_rank: 3
      priority_goals:
        - "Flow Video Series Production (01..06 Scripts -> Filming)"
        - "Website Stage 3 IA & First-Family Content Transformation"
        - "The Art of Flow PDF Billing & Movement Client Compliance"
      selected_work_refs:
        - "moa-videos:[OP-UNRESOLVED]"
        - "moa-web:OP-WP#163/#244-#249"
        - "moa-billing:[OP-UNRESOLVED]"
    - portfolio_id: "apex_ai"
      label: "Apex AI"
      priority_rank: 4
      priority_goals:
        - "Thu Thomas Planning & ki-basis / OpenMausBot Setup"
        - "Module 02 PrecapNextDay & Daily Loop Convergence"
        - "Layer-1 Contract Benchmark (HANDOVER-12) & 338-Test Audit"
      selected_work_refs:
        - "apex-thomas:OP-WP#139"
        - "apex-nextday:OP-WP#198"
        - "apex-contract:OP-WP#222"
    - portfolio_id: "mindful_bar"
      label: "Mindful Bar"
      priority_rank: 5
      priority_goals:
        - "First-Test Micro Pass (20-60 Friends & Network Tasting)"
        - "Thu 10:00 Chris Sync & 4-Track Decisions (Q-26/27, Price, UK Mark, QR)"
      selected_work_refs:
        - "mb-micro:[OP-UNRESOLVED]"
        - "mb-chris:[OP-UNRESOLVED]"
    - portfolio_id: "residual"
      label: "Residual"
      priority_rank: 6
      priority_goals:
        - "Tonight Wed Project Night: Sexy Content, Dance & Studio Reset"
        - "Personal Errands: Ma, Bahn & BahnCard, Kilian (+ W47 Ghost VPN)"
        - "ACIM-Secular QA (Decads 24-37) & Lika-Community WSL Compose"
      selected_work_refs:
        - "res-tonight:[OP-UNRESOLVED]"
        - "res-errands:[OP-UNRESOLVED]"
        - "res-acim-lika:[OP-UNRESOLVED]"
  reconciled_calendar_events:
    - date: "2026-11-11"
      title: "WC Meister"
      start: "18:00"
      end: "20:00"
      policy: "ignored_ongoing"
      capacity_delta_min: 0
    - date: "2026-11-12"
      title: "Alex & Chris (+ dup 'Chris' GCal entry)"
      start: "10:00"
      end: "11:00"
      policy: "protected"
      capacity_delta_min: -60
    - date: "2026-11-12"
      title: "München Tanz commute buffer"
      start: "18:15"
      end: "18:45"
      policy: "buffer"
      capacity_delta_min: 0
    - date: "2026-11-12"
      title: "München Tanz"
      start: "18:45"
      end: "21:00"
      policy: "protected"
      capacity_delta_min: 0
    - date: "2026-11-13"
      title: "WC Meister"
      start: "18:00"
      end: "20:00"
      policy: "ignored_ongoing"
      capacity_delta_min: 0
  capacity_deformations_and_omissions:
    - day: "Thursday"
      flow: "F1"
      shape: "compressed"
      reason: "Alex & Chris 10:00-11:00 overlaps tail of F1 (-30m Craft; duplicate 'Chris' entry not double-counted)"
    - day: "Thursday"
      flow: "F2"
      shape: "compressed"
      reason: "Alex & Chris 10:00-11:00 overlaps start of F2 (-30m Craft)"
    - day: "Thursday"
      flow: "F3"
      shape: "full"
      reason: "[CAL-GAP] Provisional host candidate for unscheduled Thu Thomas planning (2Dos.md:37-46) until GCal invite placed"
    - day: "Thursday"
      flow: "F4"
      shape: "full"
      reason: "Tails against 18:15-18:45 München Tanz commute buffer; hard stop by 18:15"
  next_day_seed:
    target_date: "2026-11-12"
    intended_emphasis: "Thu 12 Nov: Alex & Chris 10:00-11:00 (Mindful Bar Q-26/27, €3.50-€6.90 price test, UK mark, Micro pass), schedule missing Thomas hold [CAL-GAP] (AI Orchestration 3x3 / OpenMausBot / skill env), Leela Crown §F.1-§F.5 (#234), IPOS RI-10/11 (#226/#233), MoA Stage 3 IA (#246), München Tanz 18:45-21:00 (18:15 buffer)."
  next_consumer: "PrecapNextDay"
```
