---
type: Report
id: PRECAP-WEEK-BRIEF-2026-W46
title: "Weekly Command Brief — 2026-W46 (09–15 Nov 2026 (ISO W46))"
description: "OKF v0.2 executive weekly brief for 2026-W46 compiling Stage 1A intake, 6 Portfolio Areas, Mon-Sun blueprint clock, T2 dispersal totals, and PrecapNextDay handoff."
status: draft
date: 2026-11-12
tags: [weekly-orchestration, precap-week, command-brief, okf-v02]
---

# Weekly Command Brief — 2026-W46 (09–15 Nov 2026 (ISO W46))

> **Result state:** `READY_WITH_REVIEW` · **G1 gate:** `PROPOSED_FOR_G1`  
> **Direction:** Advance Leela Skill Tree crown §F.1-§F.5 (#234, 6/9 pass post QA-211) + repo-efficiency brief  
> **Next action:** `RECONFIRM_MIDWEEK_G1 (Schedule Thu Thomas GCal hold [CAL-GAP], clear dup 'Chris' event, lock Wed F4 + Thu Chris decisions, then hand off to PrecapNextDay)`  
> **Review needed:** 3 live flags: (1) [CAL-GAP] Thu Nov 12 Thomas planning (2Dos.md: AI Orchestration 3x3 / OpenMausBot / skill env) missing on GCal + duplicate 'Chris' event at 10:00; (2) [OP-OFFLINE] 127.0.0.1:8083 ECONNREFUSED on Wed Nov 11; (3) Mindful Bar Q-26/Q-27 & UK mark 'Mindful Bar' wait on operator.  
> **Interactive Cockpit (`v0.5`):** [precap-week-cockpit-2026-W46.html](../precap-week-cockpit-2026-W46.html)

## 00 · Portfolio Compass (`T1 / T2` Grounded)

| Metric | Value | Source Basis |
|---|---|---|
| **Net Craft Capacity (`T1`)** | `35.0h / 36.0h C` (`48.0h` gross) | `24` Flows (`72m` recap inside `12.0h` P/M/R) `[src: CLK]` |
| **Weekly Flows (`Mon–Sun`)** | `24` (`20` Wkd / `4` Wknd) | Weekday `08:00–24:00` + Weekend `12:00–16:00` `[src: CLK]` |
| **3x3 Craft Sprints (`C1–C3`)** | `72` sprints (`240` slots) | `3 × 30m` Craft per Flow + `DD-22A` bands `[src: DSP]` |
| **6 Portfolio Areas** | `6 Areas · 15 L1 · 5 L2` | Canonical `06-PORTFOLIO` standard `[src: OP]` |
| **G1 Readiness & Overrides** | `PROPOSED_FOR_G1` (`3` overrides) | OP: `OFFLINE_FALLBACK` · Cal: `ONLINE` `[src: INT]` |

## 01 · Operator Decisions (`New` & `Ongoing` · `G1`)

| ID | Bucket | Decision / Policy | Override Delta | Gate | Src |
|---|---|---|---|---|---|
| `D-W46-01` | New | Mid-week 6-Portfolio frontier | Initial Nov 8 W46 project… -> Mid-week Wed Nov 11 re-ba… | `PROPOSED_FOR_G1` | `[INT]` |
| `D-W46-02` | New | Leela weekly scope & QA-211 depth lock | All active Project #3/#9/… -> Pause Path UI; ship Crown… | `PROPOSED_FOR_G1` | `[INT]` |
| `D-W46-03` | New | Schedule Thu Nov 12 Thomas planning ([CAL-GAP]) | Hold Thu F3 (13:30-15:30) candidate… | `PROPOSED_FOR_G1` | `[INT]` |
| `D-W46-04` | New | Mindful Bar First-Test Micro & 5 Open Decisions | Lock cocoa bar positioning (MB-DEC-… | `PROPOSED_FOR_G1` | `[INT]` |
| `POL-01` | Ongoing | Standing ignore (cross-ref: §03) | Google Calendar busy bl… -> calendar_ignores: WC Me… | `CONFIRMED` | `[CLK]` |
| `POL-02` | Ongoing | Protected event (cross-ref: §03) | Alex & Chris (C. Sgarz · -60m Craft) | `CONFIRMED` | `[CLK]` |
| `POL-03` | Ongoing | Protected event (cross-ref: §03) | München Tanz (+ 18:15 commute buffe… | `CONFIRMED` | `[CLK]` |
| `POL-04` | Ongoing | OpenProject [OP-OFFLINE] + Non-Blocking GCal Item… | opCall.js doctor ECONNREFUSED; Nov… | `CONFIRMED` | `[OP]` |

## 02 · Matrix 1 Overview (`6 Portfolio Areas`)

| Rank | Portfolio Area | `L1` Priority Outcomes (`WP` Ref) | `L2` Nice | Cross-Repo Edges |
|---|---|---|---|---|
| 1 | **Leela** | ⚡ Skill Tree Crown Engine §F.1–§F.5 (`#234`); ⚡ SpatialViewNode & Durable Placement Contracts… | Repo-Efficiency Over-Engineering A… | — |
| 2 | **IPOS** | ⚡ ADR-003 Cleanup & RI-11 YouTube/RSS Intake Breadth (`#224 / #226`); RI-10 Fixture Acceptance… | 60-Indicator Registry Widening & A… | — |
| 3 | **Master of Arts** | ⚡ Flow Video Series Production; Website Stage 3 IA & First-Family Content Transformation (`#16… | Sequencing Dispersal Engine T1/T2… | 🔗 Cross-Repo: Feeds IPOS Ingestion |
| 4 | **Apex AI** | ⚡ Thu Thomas Planning & ki-basis / OpenMausBot Setup (`#139`); Module 02 PrecapNextDay & Daily… | KI-Basis Private vs Community Comp… | 🔗 Cross-Repo: Feeds Leela Skill Portability |
| 5 | **Mindful Bar** | ⚡ First-Test Micro Pass; ⚡ Thu 10:00 Chris Sync & 4-Track Decisions | Resolve Mindful Bar OpenProject Sk… | 🔗 Cross-Repo: Apex OP Skill Sync |
| 6 | **Residual** | Tonight Wed Project Night: Sexy Content, Dance & Studio Reset; Personal Errands: Ma, Bahn & Ba… | — | — |

## 03 · Matrix 2 Calendar Collisions & Personal Focus

| Date | Event | Window | Policy | Capacity Delta |
|---|---|---|---|---|
| `2026-11-11, 13` | WC Meister | `18:00–20:00` | `ignored_ongoing` | `0m` |
| `2026-11-12` | Alex & Chris | `10:00–11:00` | `protected` | `-60m` |
| `2026-11-12` | München Tanz commute buffer | `18:15–18:45` | `buffer` | `0m` |
| `2026-11-12` | München Tanz | `18:45–21:00` | `protected` | `0m` |

| Dimension | In-Flow Budget | Focus & Protocols |
|---|---|---|
| **Mental** | `216m` in-Flow | Daily Morning Intention coherence (Mon/Wed/Fri/Sun focus days · Tue Surrender · Thu Breathing); ACIM & S… |
| **Physical** | `144m` in-Flow + Course | Protect right knee recovery — Knee chunk pinned to `*_*_I3_P` slots (11/wk quota); Preserve 18:30-19:30… |
| **Regeneration** | `288m` (`0 XP`) | Protect 22:00-22:30 Day Outro boundary after Wed Project Night & Thu München Tanz; Rotate Audiobooks (11… |

## 04 · Residual Information & 1-Hop Provenance

| `WP` Ref | Deferred Item | Reason | Revisit Trigger |
|---|---|---|---|
| `OP-WP#204` | MoA ACIM Secular Credits Page | Moved out of Matrix 1 L2 to Longlist Deferred. | After OP-WP#163 / OP-WP#246 Website Stage 3 IA sign-off. |
| `[OP-UNRESOLVED]` | MoA Stripe Webhook Integration | Staged future billing wave (Kleinunternehmer §19 UStG manua… | After first signed Flow client contract & Obsidian PDF billing v… |
| `OP-WP#227` | IPOS Telegram Research Digest | Deferred Mission 2 summary behind OP-WP#232 per OP-REL#97. | After OP-WP#224, OP-WP#226 YouTube/RSS breadth & OP-WP#232 Unifi… |

| Tag | Source | Freshness |
|---|---|---|
| `[CLK]` | `../02-weekly-dispersal/week-blueprint.json` — Canonical Blueprint Clock (T1) | `CURRENT` |
| `[DSP]` | `../02-weekly-dispersal/week-allocation.json` — T2 Weekly Allocation & Dials | `CURRENT` |
| `[INT]` | `fixtures/w46-reference-intake.json` — Operator Intake (W46 Momentary) | `CURRENT` |
| `[GCAL]` | `gcalendar:readonly-2026-11-11` — Google Calendar Live Query (Nov 9-23) | `CURRENT` |
| `[OP]` | `../00-openproject-dependency-intake/EVIDENCE-20261106.okf.md` — OpenProject Intake Evidence [OP-OFFLINE] | `AGED` |

> **Telemetry & Ledger:** OpenProject uses `[OP-OFFLINE]` (`OFFLINE_FALLBACK`). Confidence: HIGH on live T1/T2 clock math, live GCal holds, and Wed 15:18 CET repo SHAs; MEDIUM on OpenProject sync ([OP-…. Assumptions: Wed/Fri WC Meister 18:00-20:00 stays ignored (Ongoing); Thu duplicate 'Chris' GCal event maps to Alex & Chris….

## 05 · Sequencing Orientation (`T2` Allocation)

| Metric | Allocation Value |
|---|---|
| **Projected Yield (`[src: DSP]`)** | `2,880m` TP (`2,808m` slots + `72m` recap) · `3,706.0` XP (`C 3,086.8`, `M 357.71`, `P 261.49`, `R 0.0`) · `BP 100.0` (`50/25/25`) |
| **Gaussian Focus Coupling** | `σ = 6.0h` centered on `19:00` (`w_max = 1.5x`, zero Fri→Sat bleed) |

## Downstream Handoff (`PrecapWeek -> PrecapNextDay`)

> Machine handoff packet: [`fixtures/w46-reference-handoff.json`](./w46-reference-handoff.json) (`PRECAP-WEEK-HANDOFF-v2.1`).

| Packet ID | Week | Target Consumer | Result State | G1 Status |
|---|---|---|---|---|
| `weekly-command-brief-20261111-2026-W46` | `2026-W46` | `PrecapNextDay` | `READY_WITH_REVIEW` | `PROPOSED_FOR_G1` |