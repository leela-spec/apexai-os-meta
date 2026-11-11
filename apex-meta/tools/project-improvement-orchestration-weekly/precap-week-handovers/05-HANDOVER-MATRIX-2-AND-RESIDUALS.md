---
type: Adapter
id: HO-PW-M2-05
title: "Handover 05 — Section 03 Matrix 2 (Temporal Timetable + Personal Strip + GCal) & Section 04 Residuals"
description: "Governs the T1 Monday-Sunday fit-to-width Matrix 2 timetable, catches hardcoded HTML / Sunday-missing DATA.days / rowspan mobile / Google Calendar 90m bugs, and establishes a standalone contract for Section 04 Residuals."
status: current
date: 2026-11-11
tags: [weekly-orchestration, matrix-2, residuals, week-blueprint, google-calendar, t1-clock]
---

# 05 · Handover: Sections `03 · Matrix 2` & `04 · Residuals`

## 1. Purpose

Bind Section `03 · Matrix 2` strictly to [`02-weekly-dispersal/week-blueprint.json`](../02-weekly-dispersal/week-blueprint.json) + `slot-inventory.json`, fix concrete HTML/mobile/Calendar collisions (`DATA.days`, `rowspan`, `HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md`), integrate `DD-22` Option A `P/M/R` bands, and create the missing governing contract for Section `04 · Residual Information`.

---

## 2. Input & Priority Ledger

| Priority | Source Path | Role & Grounding | Ignore / Exclude |
|---|---|---|---|
| **P1 (Sole Clock)** | `02-weekly-dispersal/week-blueprint.json` | Canonical `Mon–Sun` clock (`08:00–24:00` weekday `960m`, `Day Outro 22:00–22:30`, `Mon–Wed Project Night 20:30–22:00`, `Thu–Fri Freizeit 20:30–22:00`, `18:30–19:30` evening physical outside `72×2m P`, `Sat–Sun 12:00–16:00` 2 Flows, `sun_off_retired: true`, `StatusMerge: Saturday_or_Sunday`). | Any hardcoded `09:00–18:00`, `21:00` shutdown, or `Sun OFF`. |
| **P1 (Slot Proof)** | `02-weekly-dispersal/build_slot_inventory.py` & `render_blueprint.py` | Enforces `120m` Flow invariant (`line 207`) across `240` `slot_occurrences` (`72 P + 72 M + 72 C + 24 R`). | Note: Epic-to-slot assignment unbuilt (`render_blueprint.py:70-71`). |
| **P1 (Matrix 2 Spec)** | `01-weekly-command-brief/HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md` (`v05 + T1`) & `SPEC-PRECAP-WEEK-ITERATIONS.okf.md:23,159-245` | One fit-to-width `Mon–Sun` timetable (`table-layout:fixed`), zero scrollbars, zero `#flowdetail/#daystrip/.displayrow`, `Mental\|Physical\|Regeneration` strip after `23:30–24:00`, `DD-22A` read-only `P/M/R` Chunks. | Contradictory Section `04` absence; stale sprint-3 checklist ambiguity. |
| **P1 (Calendar Rules)** | `.claude/skills/PrecapWeek/calendar-planning-guidance.md` & `D019` | Read-only live Google Calendar check, untrusted event text, collision compression & omission reasons, `create_calendar_events: false` in PrecapWeek. | `HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md` (`90m/60m/30m`, `18:00–18:30`, `PrecapWeek` writer claims). |
| **P2 (Open Deltas)** | `01-weekly-command-brief/research/OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md` & `ORCHESTRATOR-MATRIX-2-DESIGN-HANDOVER-20261106.okf.md` | `Q06` (no permanent project lanes), `Q08` (`PrecapNextDay` owns granular micro-checklists), `Q10` (`PrecapWeek` never mutates Calendar), `Q13`. | `Q09` stale `Sun OFF` default; `38h vs 35h` pre-`T1` math. |
| **Broken Impl** | `01-weekly-command-brief/precap-week-cockpit-W45-actual-data-v03.html:22-23,27,128-163` | Working `table-layout:fixed` CSS & `#focusstrip` skeleton. | Hardcoded `tbody`, 6-day `DATA.days` (missing Sunday!), mobile `rowspan` breakage. |

---

## 3. Forensic Diff — Latest vs Added (`Nov 9–11`) vs Bugs & Conflicts Found

### Locked State (`ec3e12f3`)
- **Single Surface Only (`HANDOVER-02:14-16`):** Exactly one fit-to-width **Monday–Sunday** hourly table. `#flowdetail`, `#daystrip`, duplicate saved-sprint table, and `.displayrow` removed permanently.
- **`3×3` Flow Anatomy (`HANDOVER-02:36,38`):** `24` weekly `120m` Flows (`3 × (P 2m + M 3m + C 30m + recap 1m) + R 12m`), carrying Craft work (`C`) + read-only `P/M/R` practice Chunks (`DD-22` Option A).
- **Personal-Focus Strip (`HANDOVER-02:17,124-129`):** Directly below `23:30–24:00 Sleep Routine`, 3 equal columns (**`Mental` | `Physical` | `Regeneration`**) holding `1–3` operator priorities (never projects/WPs/Flows) or `not yet specified`.

### Seven Critical Bugs, Losses & Contradictions Found
1. **`v03.html` Hardcoding + Missing Sunday in `DATA.days` + Mobile `rowspan` Trap:**
   - `#s03` (`v03.html:140-158`) does NOT read `week-blueprint.json` or `slot-inventory.json`; it hardcodes HTML rows (`T1` labels manually pasted).
   - `DATA.days` (`v03.html:27`) still has **6 entries (`Mon–Sat`, NO `Sun`!)** and stale `Sat` `09:00–13:00` strings overwritten downstream.
   - `rowspan="2"/"3"/"8"` (`v03.html:142-150`) combined with `@media(max-width:920px)` `display:block` (`:12`) leaves `12:00–12:30` & `14:00–15:30` empty on Mon–Fri mobile and traps `Sat–Sun 16:00–24:00` inside `16:00–16:30`!
2. **`DD-22` Option A `P/M/R` Band Unimplemented:** `HANDOVER-02:38` requires rendering read-only in-Flow `P/M/R` practice Chunks, yet `v03.html:133-138` prints ONLY `C1/C2/C3` Craft items (`weekend` literally says `3x(P2+M3+C30+1)+12R`).
3. **`HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md` Violates `T1`, `Q06`, and `Q10`:**
   - Uses dead anchors `08:00–09:00` & `18:00–18:30` (`:12`), puts `F1–F4` inside `09:00–18:00`, defines **`90m` Standard / `60m` Compressed / `30m` Minimal Flows** (`build_slot_inventory.py:207` requires strict `duration_min == 120`!), ignores weekends, hardcodes `+02:00` CEST (`W46` is `+01:00` CET!), bans mixed-project Flows (`Q06`), and claims `PrecapWeek` writes events (`Q10` assigns gated writes solely to `PrecapNextDay`).
4. **Meeting Collision Subtraction Undefined vs `120m` Invariant:** `v03.html:27,143` dumps `Thu 10:00–11:00 Alex & Chris` across `F1`/`F2` as an unsubtracted `.cellnote`, and `Thu 18:45–21:00 München Tanz` collides across `18:30–19:30 Evening Physical` + `Project/Freizeit` without transition travel buffer or capacity recalculation.
5. **`Q06` (`Sequence vs Flow`) & `Q08` (`Sprint Depth`) Conflicts:** `v03.html:129` hardcodes `flowOwners` (`F1: MoA`, etc.) and `HANDOVER-02:28` pushes 3 microtasks inside weekly cells, conflicting with `OPERATOR-DECISION-DELTA Q06:56,65` (no fixed permanent project lanes) and `Q08:36,94-95` (`PrecapWeek` assigns day/Flow direction; `PrecapNextDay` authors 3 tactical sprints).
6. **Zero Contract for Section `04 · Residual Information`:** Section `04` exists only inside `v03.html:23` (`2×2` `.notebox`: Clock reconciliation, `EM-13` completeness, Deferrals & gaps, Downstream handoff) with zero standalone `HANDOVER-*` spec!
7. **`Weekly Command Brief` Spec Alignment:** Matrix 2 must emit explicit `capacity_deformations_and_omissions` (`calendar-planning-guidance.md`) inside Section `04` and `presentation_handoff` (`Q11`).

---

## 4. Process & Anti-Drift Boundaries

- **Generator-First Matrix 2 (`render_blueprint.py` / Cockpit Builder):** Matrix 2 DOM MUST be generated from `week-blueprint.json` (`regimes`, `operating_window`, `weekday_anchors`), `slot-inventory.json`, reconciled Google Calendar blocks, `T2` `P/M/R` assignments, and Matrix 1 `selected_work_reference` — zero manual `tbody` typing.
- **Responsive Mobile Integrity:** Render a dedicated stacked Mon–Sun card list `<920px` (or CSS Grid) instead of flexing `<tr rowspan="8">` tables.
- **Strict Section `04` Purity:** Never copy Matrix 1 cards or Matrix 2 schedules into `04`; keep it strictly for conflicts, `[OP-OFFLINE]` / Calendar gaps, deferrals, review flags, and the `presentation_handoff` block (`SPEC §7`).

---

## 5. Output & Concrete Examples

### Canonical Targets to Update
1. `01-weekly-command-brief/HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md` (add Section `04` Contract or sibling spec, enforce `week-blueprint.json` dynamic rendering, resolve `Q06/Q08` cell granularity, document mobile non-`rowspan` strategy).
2. `01-weekly-command-brief/research/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md` (either align to `T1` `120m` + `Europe/Berlin` auto-DST + `PrecapNextDay`-only writes + move/update to `Module 02`, OR deprecate per `CDL-05` if superseded).
3. `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md` (`§6` & `§7`).
4. Data-driven Matrix 2 (`#s03`) + Residuals (`#s04`) renderer reading `week-blueprint.json` + `slot-inventory.json`.

### Concrete Example — Compressed Collision Rule + Non-`rowspan` Cell Model
```json
{
  "day": "Thursday",
  "blocks": [
    {
      "time": "08:30-10:30",
      "blueprint_slot": "F1",
      "external_collision": "10:00-10:30 overlap w/ Alex & Chris (10:00-11:00)",
      "deformed_mode": "compressed_3x20C_or_moved",
      "net_craft_min": 60,
      "craft_owner_ref": "selected_work_ref:moa-website",
      "pmr_band_readonly": ["P: Martial Arts (gauss w=0.4)", "M: Breathing", "R: Audiobooks"]
    }
  ]
}
```

---

## 6. Operator Resolution Ledger (`M2-Q1..Q4` — Ratified `2026-11-11`)

1. **`Q08` Weekly Cell Depth:** **Ratified Option A:** Show Flow Owner (`selected_work_reference` link across the 6 Portfolio Areas) + Flow Target + clickable `C1/C2/C3` macro labels + read-only `DD-22A` `P/M/R` strip in `PrecapWeek`, leaving tactical `S1–S3` sub-steps and prompt packets to `PrecapNextDay`.
2. **Meeting Deformation vs `120m` Blueprint Guard (`build_slot_inventory.py:207`):** **Ratified:** Keep `24` nominal `120m` slots in `slot-inventory.json` for `slot_id` stability while applying a calendar capacity overlay (`full / compressed / minimal / omitted`).
3. **Transition Travel Windows (`Calendar`):** **Ratified:** Recurring offsite events (`München Tanz 18:45–21:00`) include an explicit commute/prep buffer (`18:15–18:45`).
4. **Google Calendar Writer Ownership (`Q10`):** **Ratified:** Updated `HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md` (`T1` `120m` flows, auto CET/CEST, gated writes) and moved under `02-next-day-brief/` (`PrecapNextDay`-only writer; `PrecapWeek` never writes calendar events).

---

## 7. Definition of Done (DoD)

1. `v03.html` / Cockpit Section `03` dynamically reads `week-blueprint.json` + `slot-inventory.json`, renders all `7` days (`Mon–Sun`, `DATA.days` has Sunday!), zero `rowspan` collapse bugs `<920px`, and `document.documentElement.scrollWidth <= window.innerWidth`.
2. `DD-22` Option A `P/M/R` read-only Chunk band renders cleanly inside Flow cells (grounded in `T2` output or explicit `T2_PENDING` state without touching `C`).
3. Personal-focus strip (`Mental | Physical | Regeneration`) sits strictly below `23:30–24:00 Sleep Routine` and renders `not yet specified` when unsupplied.
4. Section `04 · Residual Information` has a formal written contract inside `HANDOVER-02` (or `SPEC §7`) covering `[OP-OFFLINE]` flags, meeting collision deltas, deferrals, and `presentation_handoff`.
5. `HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md` has zero stale `90m` / `18:00–18:30` / `+02:00` / `PrecapWeek-writer` instructions.

## 8. Fresh-Chat Starter Prompt

```text
Read apex-meta/tools/project-improvement-orchestration-weekly/precap-week-handovers/05-HANDOVER-MATRIX-2-AND-RESIDUALS.md and 00-RULE-CANONICAL-DECISION-LOCK.md.
Let us resolve the Q08 weekly cell depth, meeting overlay vs 120m slot_id stability, commute buffers, and Google Calendar handover ownership. Then replace the hardcoded #s03 HTML with a week-blueprint.json + slot-inventory.json driven builder (fixing Sunday missing in DATA.days and the mobile rowspan bug), wire DD-22A P/M/R bands, codify Section 04 Residuals, and patch HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md.
```
