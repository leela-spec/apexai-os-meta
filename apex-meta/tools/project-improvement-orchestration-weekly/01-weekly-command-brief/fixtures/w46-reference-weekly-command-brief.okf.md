---
type: Report
id: PRECAP-WEEK-BRIEF-2026-W46
title: "Weekly Command Brief — 2026-W46 (09–15 Nov 2026 (ISO W46))"
description: "OKF v0.2 executive weekly brief for 2026-W46 compiling Stage 1A intake, 6 Portfolio Areas, Mon-Sun blueprint clock, T2 dispersal totals, and PrecapNextDay handoff."
status: current
date: 2026-11-11
tags: [weekly-orchestration, precap-week, command-brief, okf-v02]
---

# Weekly Command Brief — 2026-W46 (09–15 Nov 2026 (ISO W46))

> **Result state:** `READY_WITH_REVIEW` · **G1 gate:** `APPROVED`  
> **Direction:** Ship Master of Arts 7 videos, responsive site (#163), and automated PDF billing feeding IPOS; lock Leela Skill Tree spatial/placement contracts (#159/#48, Path paused); close IPOS intake audit/Docling seam/viz (#224-#226); land Apex AI HID hook (#139), orchestration convergence (#198), and Dark Factory gate (#222); advance Mindful Bar spec v0.2 & ERPNext pilot eval.  
> **Next action:** `APPROVE_WEEK (G1 validated; pass presentation_handoff to PrecapNextDay)`  
> **Review needed:** Verify [OP-OFFLINE] Nov 6 snapshot currency and confirm Thu 10:00-11:00 + 18:15 buffer capacity compression  
> **Interactive Cockpit (`v0.5`):** [precap-week-cockpit-W45-actual-data-v03.html](../precap-week-cockpit-W45-actual-data-v03.html)

## 00 · Portfolio Compass (`T1 / T2` Grounded)

Capacity and sprint metrics derive directly from the weekly blueprint and allocation JSON.

| Metric | Value | Source Basis |
|---|---|---|
| **Net Craft Capacity (`T1`)** | `35.0h / 36.0h C` (`48.0h` gross) | `24` Flows (`72m` trailing recap inside `12.0h` P/M/R) `[src: CLK]` |
| **Weekly Flows (`Mon–Sun`)** | `24` (`20` Wkd / `4` Wknd) | Weekday `08:00–24:00` + Weekend `12:00–16:00` `[src: CLK]` |
| **3x3 Craft Sprints (`C1–C3`)** | `72` sprints (`240` slot_ids) | `3 × 30m` Craft per Flow + `DD-22A` P/M/R bands `[src: DSP]` |
| **6 Portfolio Areas** | `6 Areas · 16 L1 · 1 L2` | Canonical `06-PORTFOLIO` standard `[src: OP]` |
| **G1 Readiness & Overrides** | `APPROVED` (`3` overrides) | OP: `OFFLINE_FALLBACK` · Cal: `ONLINE` `[src: INT]` |

## 01 · Operator Decisions (`New` & `Ongoing` · `G1`)

Standard clock windows live solely in `02-weekly-dispersal/week-blueprint.json`.

- **`D-W46-01 · 6-Portfolio Flow routing`** — `F1-F2 MoA · F3 IPOS · F4 Apex AI / Leela / Mindful Bar / Residual` (`G1: APPROVED`) *(Override: `Default priority rank order (calendar-planning-guidance.md)` -> `Explicit W46 Flow topic allocation across 6 portfolios`)* `[src: INT]`
- **`D-W46-02 · Leela weekly scope freeze`** — `Skill Tree only (Path & Sequencing UI paused)` (`G1: APPROVED`) *(Override: `All active Project #10 work packages eligible` -> `Pause Path & Sequencing UI; lock Skill Tree contracts only`)* `[src: INT]`
- **`D-W46-03 · Mon & Wed Project Night themes`** — `Mon/Wed Sexy Content & Studio; Tue Billing sprint (20:30-22:00)` (`G1: APPROVED`) `[src: INT]`
- **`D-W46-04 · Mindful Bar 6th portfolio stream`** — `Cacao Bar Spec v0.2 + ERPNext/Frappe evaluation` (`G1: APPROVED`) `[src: INT]`
- **Ongoing:** `Standing ignore · Wed/Fri WC Meister (18:00-20:00)` — `Ignored ambient calendar hold` `[src: CLK]`
- **Ongoing:** `Protected event · Thu 10:00-11:00` — `Alex & Chris (C. Sgarz)` `[src: CLK]`
- **Ongoing:** `Protected event · Thu 18:45-21:00` — `München Tanz (+ 18:15 commute buffer)` `[src: CLK]`
- **Ongoing:** `OpenProject intake provenance (D019)` — `[OP-OFFLINE] Verified Nov 6 Snapshot` `[src: OP]`

## 02 · Matrix 1 Overview (`6 Portfolio Areas`)

Full `G|I|P|S|O|C` fields and `Tasks -> Subtasks` open interactively in the HTML Cockpit.

| Rank | Portfolio Area | `L1` Priority Outcomes (`WP` Ref) | `L2` Nice | Cross-Repo Edges |
|---|---|---|---|---|
| 1 | **Leela** | ⚡ Canonical Chunk identity (`OP-WP#159 / OP-WP#39`); ⚡ Durable placement identity (`OP-WP#48`) | — | — |
| 2 | **IPOS** | ⚡ Full ingestion pipeline audit (ADR-003) (`OP-WP#224 / OP-WP#228`); External intake seam (Docling + Trafilatura) (`OP-WP#226`); Sovereign data visualization over time (`OP-WP#225`) | — | — |
| 3 | **Master of Arts** | Website content draft & responsive layout (`OP-WP#163`); 7 produced videos (`[OP-UNRESOLVED]`); ⚡ Automated PDF billing (`[OP-UNRESOLVED]`) | — | 🔗 Cross-Repo: Feeds IPOS Viz |
| 4 | **Apex AI** | ⚡ OpenMouse kernel HID polling hook (`OP-WP#139`); Mindful repository orchestration & Precap convergence (`OP-WP#198`); Dark Factory integration gate (`OP-WP#222`) | — | 🔗 Cross-Repo: Unblocks Leela Chunk ID |
| 5 | **Mindful Bar** | Cacao Bar functional product spec v0.2 & validation (`[OP-UNRESOLVED]`); ERPNext / Frappe food-ops architecture evaluation (`[OP-UNRESOLVED]`) | Mindful Bar packaging & sensory deck notes | — |
| 6 | **Residual** | Apartment & Studio Art (`[OP-UNRESOLVED]`); Sexy Content visuals (Mon/Wed Project Night) (`[OP-UNRESOLVED]`); Community & Travel logistics (`[OP-UNRESOLVED]`) | — | — |

## 03 · Matrix 2 Calendar Collisions & Personal Focus

The full `Mon–Sun` hourly timetable lives inside Section `03` of the HTML Cockpit.

| Date | Event | Window | Policy | Capacity Delta |
|---|---|---|---|---|
| `2026-11-11` | WC Meister | `18:00–20:00` | `ignored_ongoing` | `0m` |
| `2026-11-12` | Alex & Chris | `10:00–11:00` | `protected` | `-60m` |
| `2026-11-12` | München Tanz commute buffer | `18:15–18:45` | `buffer` | `0m` |
| `2026-11-12` | München Tanz | `18:45–21:00` | `protected` | `0m` |
| `2026-11-13` | WC Meister | `18:00–20:00` | `ignored_ongoing` | `0m` |

- **Mental (`216m` in-Flow):** Daily Morning Intention coherence (Mon/Wed/Fri/Sun focus days); ACIM & Surrender presence across F1-F4 transitions
- **Physical (`144m` in-Flow + Evening Course):** Protect right knee recovery — Knee chunk pinned to `*_*_I3_P` slots (11/wk quota); Preserve 18:30-19:30 Evening Physical Course (Mon-Wed, Fri; Thu via München Tanz)
- **Regeneration (`288m` breaks · `0 XP`):** Protect 22:00-22:30 Day Outro boundary; Rotate Yoga Nidra, Audiobooks & Socializing across 24 in-Flow R breaks (XP = 0)

## 04 · Residual Information & 1-Hop Provenance

OpenProject status uses `[OP-OFFLINE]` (`OFFLINE_FALLBACK`); see Deferrals and 1-hop ledger below.

| `WP` Ref | Deferred Item | Reason | Revisit Trigger |
|---|---|---|---|
| `OP-WP#204` | MoA ACIM Secular Credits Page | Moved out of Matrix 1 L2 to Longlist Deferred. | After OP-WP#163 responsive layout sign-off. |
| `[OP-UNRESOLVED]` | MoA Stripe Webhook Integration | Staged future billing wave. | After local PDF invoice engine unit-test verification. |
| `OP-WP#227` | IPOS Telegram Research Digest | Deferred Mission 2 summary. | After OP-WP#224 & OP-WP#226 Docling/Trafilatura seam pass. |

| Tag | Source | Freshness |
|---|---|---|
| `[CLK]` | `../02-weekly-dispersal/week-blueprint.json` — Canonical Blueprint Clock (T1) | `CURRENT` |
| `[DSP]` | `../02-weekly-dispersal/week-allocation.json` — T2 Weekly Allocation & Dials | `CURRENT` |
| `[INT]` | `fixtures/w46-reference-intake.json` — Operator Intake (W46 Reference) | `CURRENT` |
| `[OP]` | `../00-openproject-dependency-intake/EVIDENCE-20261106.okf.md` — OpenProject Intake Evidence [OP-OFFLINE] | `AGED` |
| `[CAR]` | `../../../informatics/final/operations/18-APEX-CARRIER-MAP.md` — Mindful Bar 6th Portfolio Carrier | `CURRENT` |

- **Confidence:** HIGH on clock & dispersal math (deterministic JSON); MEDIUM on live OpenProject state ([OP-OFFLINE] Nov 6 snapshot active).
- **Assumptions:** Fri->Sat evening physical Gaussian spillover disabled per T2 allocator; WC Meister stays ignored per Ongoing directive.

## 05 · Sequencing Orientation (`T2` Allocation)

All `240` slot occurrences are bound dynamically by `allocate_week.py` (`DD-16`: zero BP floor).

- **Projected Yield (`[src: DSP]`):** `2,880m` TP (`2,808m` slots + `72m` recap) · `3,706.0` XP (`C 3,086.8`, `M 357.71`, `P 261.49`, `R 0.0`) · `BP 100.0` (`50/25/25`).
- **Gaussian Focus Coupling:** `σ = 6.0h` centered on `19:00` (`w_max = 1.5x`, zero Fri→Sat bleed).

## Compact Downstream Handoff (`PrecapWeek -> PrecapNextDay`)

```yaml
presentation_handoff:
  schema_version: "PRECAP-WEEK-HANDOFF-v2.1"
  artifact_type: "Weekly_Command_Brief"
  packet_id: "weekly-command-brief-20261108-2026-W46"
  produced_at: "2026-11-11T00:00:00Z"
  week: "2026-W46"
  date_range:
    start: "2026-11-09"
    end: "2026-11-15"
  timezone: "Europe/Berlin"
  clock_owner: "apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json"
  dispersal_owner: "apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-allocation.json"
  cockpit_html_ref: "apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/precap-week-cockpit-W45-actual-data-v03.html"
  brief_okf_ref: "apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/fixtures/w46-reference-weekly-command-brief.okf.md"
  data_json_ref: "apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/fixtures/w46-reference-cockpit.json"
  result_state: "READY_WITH_REVIEW"
  operator_g1_status: "APPROVED"
  source_status:
    openproject: "OFFLINE_FALLBACK"
    google_calendar: "ONLINE"
  weekly_intent: "Ship Master of Arts 7 videos, responsive site draft (#163), and automated PDF billing; freeze Leela Skill Tree spatial contracts (#159/#48, Path paused); complete IPOS intake audit & time-series viz (#224-#226); advance Apex AI HID (#139) & Dark Factory (#222); integrate Mindful Bar spec v0.2 & ERPNext eval."
  six_portfolio_areas:
    - portfolio_id: "leela"
      label: "Leela"
      priority_rank: 1
      priority_goals:
        - "Canonical Chunk identity"
        - "Durable placement identity"
      selected_work_refs:
        - "leela-chunk:OP-WP#159/#39"
        - "leela-placement:OP-WP#48"
    - portfolio_id: "ipos"
      label: "IPOS"
      priority_rank: 2
      priority_goals:
        - "Full ingestion pipeline audit (ADR-003)"
        - "External intake seam (Docling + Trafilatura)"
        - "Sovereign data visualization over time"
      selected_work_refs:
        - "ipos-audit:OP-WP#224/#228"
        - "ipos-seam:OP-WP#226"
        - "ipos-viz:OP-WP#225"
    - portfolio_id: "master_of_arts"
      label: "Master of Arts"
      priority_rank: 3
      priority_goals:
        - "Website content draft & responsive layout"
        - "7 produced videos"
        - "Automated PDF billing"
      selected_work_refs:
        - "moa-web:OP-WP#163"
        - "moa-videos:[OP-UNRESOLVED]"
        - "moa-billing:[OP-UNRESOLVED]"
    - portfolio_id: "apex_ai"
      label: "Apex AI"
      priority_rank: 4
      priority_goals:
        - "OpenMouse kernel HID polling hook"
        - "Mindful repository orchestration & Precap convergence"
        - "Dark Factory integration gate"
      selected_work_refs:
        - "apex-hid:OP-WP#139"
        - "apex-repo:OP-WP#198"
        - "apex-dark:OP-WP#222"
    - portfolio_id: "mindful_bar"
      label: "Mindful Bar"
      priority_rank: 5
      priority_goals:
        - "Cacao Bar functional product spec v0.2 & validation"
        - "ERPNext / Frappe food-ops architecture evaluation"
      selected_work_refs:
        - "mb-spec:[OP-UNRESOLVED]"
        - "mb-erp:[OP-UNRESOLVED]"
    - portfolio_id: "residual"
      label: "Residual"
      priority_rank: 6
      priority_goals:
        - "Apartment & Studio Art"
        - "Sexy Content visuals (Mon/Wed Project Night)"
        - "Community & Travel logistics"
      selected_work_refs:
        - "res-art:[OP-UNRESOLVED]"
        - "res-visual:[OP-UNRESOLVED]"
        - "res-community:[OP-UNRESOLVED]"
  reconciled_calendar_events:
    - date: "2026-11-11"
      title: "WC Meister"
      start: "18:00"
      end: "20:00"
      policy: "ignored_ongoing"
      capacity_delta_min: 0
    - date: "2026-11-12"
      title: "Alex & Chris"
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
      reason: "Alex & Chris 10:00-11:00 overlaps tail of F1 (-30m Craft)"
    - day: "Thursday"
      flow: "F2"
      shape: "compressed"
      reason: "Alex & Chris 10:00-11:00 overlaps start of F2 (-30m Craft)"
    - day: "Thursday"
      flow: "F4"
      shape: "full"
      reason: "Tails against 18:15-18:45 München Tanz commute buffer; monitor overrun"
  next_day_seed:
    target_date: "2026-11-09"
    intended_emphasis: "Mon Foundations: F1-F2 Master of Arts videos/website (#163), F3 IPOS ADR-003 (#224), F4 Mindful Bar Spec v0.2 & Residual studio art, Project Night 20:30-22:00 Sexy Content & Studio."
  next_consumer: "PrecapNextDay"
```
