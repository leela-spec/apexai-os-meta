---
type: Specification
id: SPEC-WEEKLY-DISPERSAL-v1.0
title: "Weekly Dispersal Specification — Flow Contract, Slot Inventory, Share Mechanism & Binding Notation"
description: "Canonical specification for the weekly dispersal slice: the 3x3 Flow contract, three day regimes, 240-occurrence slot inventory, Epic branch scope, and failure guards."
status: current
date: 2026-11-10
scope: [sequencing, dispersal, precap-week, slots, epics, xp, bp, quota, notation]
tags: [sequencing, dispersal, specification, weekly-orchestration, precap-week, slot-inventory, quota]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Weekly Dispersal Specification

**Sequencing** is a distribution system powered by interleaving, spaced repetition, chunking, and testing to achieve a valuable dispersion of practicing and pursuing goals, skills, and trainings.

This specification governs the Flow contract, day regimes, slot inventory, Epic branch set, and failure guards.

### Single-Owner Companions

- Calendar clock: `apexai-os-meta/.../02-weekly-dispersal/week-blueprint.json`.
- Algorithm & BP authority: [ALGORITHM.md](ALGORITHM.md).
- Entity schema & Personal Epic database: [EPICS-SCHEMA.md](EPICS-SCHEMA.md) and [epics.json](epics.json).
- Weekly operator dials (`DD-02`): [week-demand.json](week-demand.json).
- Active register & changelog: [ASSUMPTIONS-AND-DECISIONS-REGISTER.md](ASSUMPTIONS-AND-DECISIONS-REGISTER.md) and [log.md](log.md).
- Generated inventory, `T2` allocator & outputs: [slot-inventory.json](slot-inventory.json), [build_slot_inventory.py](build_slot_inventory.py), [allocate_week.py](allocate_week.py), and [week-allocation.json](week-allocation.json).

---

## 1. Core Architectural Invariants

- **WD-01 [P0 | I98/E96/R05] Reduced Slice Only**: Build only the personal Epic database, [week-demand.json](week-demand.json), slot-filling algorithm, and Precap Week surface. Reuse Leela's schemas without reimplementing the full Path or Stats modules.
- **WD-02 [P0 | I98/E95/R04] The Flow Is 3x3 At 120 Minutes**: Every Flow is three slots by three
  iterations of the branch triple `[P, M, C]`, closing on one `R` break, totalling exactly 120
  minutes. One standard everywhere — weekday, weekend, project night or not. Reject any Flow of
  another duration rather than shortening a slot to fit.
- **WD-03 [P0 | I97/E98/R05] Branch Point Sourcing Is Absolute**: Branch `R` never sources XP and
  branch `C` never sources BP (glossary `ST-010`). Never mint XP for `R` to make it schedulable;
  reachability for `R` comes from structural BP balance (`ALGORITHM.md`).
- **WD-04 [P0 | I96/E94/R06] XP Is Solved For, Never Redefined**: XP is a quantity — goal-progress
  leverage over TP, with leverage `= XP / TP` (`ST-008`). Because every slot has a determinate TP,
  compute `XP = leverage x TP` for craft and practice alike. A percentage display is a derived view
  (`XP_concentration`) of that one quantity, never a second metric wearing the same name.
- **WD-05 [P0 | I95/E92/R07] BP Measures Branches, Not Repositories**: Balance Points are
  `branch_diversity(50) + work_break_alternation(25) + focus_day_alternation(25)`. Repository
  diversity is not BP. Focus-day alternation reads whichever days carry emphasis; never hard-code a
  weekday pair.
- **WD-06 [P0 | I94/E93/R06] One Authoring Surface Per Assignment**: Exactly one surface authors a
  slot assignment. The algorithm binds; every other view reads. Reject any second editable surface
  over the same assignment — two authors with no merge authority diverge silently.
- **WD-07 [P0 | I93/E95/R05] Projected, Never Realized**: With Stats excluded there is no
  `xp_ledger` and no Run facts. Every figure this specification governs is the Algorithm-calculated
  projected stage. Never present a projected figure as realized.

---

## 2. The Flow Contract

### 2.1 Composition

- **WD-08 [P1 | I95/E95/R04] Slot Schema**: A Flow's slot sequence is `[P, M, C] x 3` then `R`.
  Per iteration: `P` 2 minutes, `M` 3 minutes, `C` 30 minutes. Per Flow: one `R` break of 12
  minutes. Grounded at `qmd #1a447e:47-57`.
- **WD-09 [P1 | I92/E94/R05] `3x3` Means Slots By Iterations**: Three slot roles cycled three times,
  not three sprints of three units. Grounded at `qmd #46ebe0:17-27,48-49`, where the Settings grid
  lists `Slots: 3x3` beside `Iterations: 1-5` and the worked example states `Slots = 3,
  Iterations = 3`.
- **WD-10 [P1 | I90/E92/R06] The Recap Minute Belongs To Craft**: The one-minute recap per craft
  sprint is the trailing minute of the craft block carrying `lp_role: recap`, never a slot of its
  own. Treating it as a Mental slot doubles the mental denominator from 72 to 144 and invalidates
  every quota figure.
- **WD-11 [P2 | I88/E90/R06] Fixed Overhead**: Practice overhead per Flow is
  `3 x (2 + 3 + 1) + 12 = 30` minutes, leaving 90 minutes of craft across three 30-minute blocks.
  The arithmetic is `3 x (2 + 3 + 30 + 1) + 12 = 120`.

### 2.2 Regimes

- **WD-12 [P1 | I92/E88/R07] Three Day Regimes**: `weekday_project` (Monday, Tuesday, Wednesday —
  four Flows plus a project night), `weekday_plain` (Thursday, Friday — four Flows plus evening Freizeit), `weekend`
  (Saturday, Sunday — two Flows). Both weekday regimes carry identical slot counts; the regimes
  differ only in the `20:30-22:00` evening block (`Project Night` Mon-Wed vs `Freizeit` Thu-Fri).
- **WD-13 [P2 | I85/E88/R07] Project Night Is Not A Flow**: The Monday-to-Wednesday project night
  runs `20:30-22:00` (90 min) and is an evening block, not a Flow; it contributes no slot occurrences
  (`DD-33` closed). On Thursday and Friday, `20:30-22:00` is `Freizeit` (90 min, `DD-37` closed).
- **WD-14 [P1 | I92/E94/R04] Single Canonical Clock Owner (`week-blueprint.json`)**: Read all start/end timestamps from `apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json` (`08:00-24:00` weekday, `12:00-16:00` weekend). Never duplicate clock tables here (`DD-32`, `DD-39`).
- **WD-14d [P2 | I86/E92/R05] The Weekday Has No Turnarounds**: Every element abuts its neighbour across the full 960-minute `08:00-24:00` span. Each Flow already closes on its own 12-minute `R` break, so the break between Flows is inside them.
- **WD-14a [P2 | I84/E92/R05] Flows 1 And 2 Are Adjacent**: No turnaround separates Flow 1 from
  Flow 2. Each Flow already closes on its own 12-minute `R` break, so adjacency removes the
  inter-Flow gap only and never the break.
- **WD-14b [P2 | I82/E90/R06] Weekend Flows Start At Noon**: The two weekend Flows run `12:00-14:00`
  and `14:00-16:00`, back-to-back with no pause between them. Both Saturday and Sunday run the weekend regime.
- **WD-14c [P1 | I88/E94/R04] Day Geometry Is Overlap-Checked**: The generator sorts every placed
  element per regime from `week-blueprint.json`, rejects any overlap, and verifies the 960-minute `08:00-24:00` weekday span.

---

## 3. The Slot Inventory

- **WD-15 [P1 | I94/E96/R04] Week Totals**: 24 Flows, 240 slot occurrences, 2,880 minutes. Per week:
  72 `M` (216 min), 72 `P` (144 min), 72 `C` (2,160 min), 24 `R` (288 min).
- **WD-16 [P1 | I90/E95/R05] Stable Slot Addresses**: Every occurrence carries the identifier
  `SO_<DAY>_<FLOW>_I<n>_<BRANCH>`, for example `SO_MON_F2_I1_M`. Addresses are stable across
  regenerations and are the binding target.
- **WD-17 [P1 | I92/E94/R05] Generated, Never Hand-Authored**: The inventory is generated from the
  Flow contract, so the contract and the inventory cannot drift. The generator rejects any Flow
  duration other than 120 minutes and any craft residual not divisible by the iteration count.
- **WD-18 [P2 | I88/E92/R06] Conformance Checks**: Each of the 24 Flows satisfies
  `sum(slot minutes) + recap minutes == 120`; the craft block equals 30 everywhere; the 240
  identifiers are unique.
- **WD-19 [P1 | I91/E90/R06] Regeneration Slots Are The In-Flow Breaks**: `R` is an ordinary branch.
  Its 24 slots are the in-flow breaks, carrying `R` content such as Yoga Nidra or reading. The
  `22:30-24:00` night window (`Freizeit` + `Sleep Routine`) is rest, not schedule, and is **not** a slot source.
- **WD-20 [P2 | I86/E90/R06] Anchors Are Outside The Quota**: The weekday anchors in `week-blueprint.json` — `Morning Anchor` (`08:00-08:30`), `Midday Anchor` (`12:30-13:30`), `Afternoon Buffer` (`15:30-16:00`), `Physical Course` (`18:30-19:30`), `Evening Meal & Transition` (`19:30-20:30`), `Project Night / Freizeit` (`20:30-22:00`), `Day Outro` (`22:00-22:30`), and `Night Window` (`22:30-24:00`) — are practice/life surface and carry no quota-bearing slots. `Day Outro` (`22:00-22:30`) is never bindable.

---

## 4. The Point Model

Single owner for equations, BP authority (`DD-01`, `DD-16`), and Gaussian coupling: [ALGORITHM.md](ALGORITHM.md).

- **WD-21 [P1 | I94/E96/R04] TP Is Determinate**: Read `TP` (`1 TP = 1 minute`) directly from the Flow contract (`2`, `3`, `30`, or `12`).
- **WD-22 [P1 | I93/E92/R06] Algorithm Point Model**: Maximise projected `XP` (`leverage × TP`) with BP owned by the Algorithm (`50/25/25`) and no numeric BP cutoff floor (`DD-16`). See [ALGORITHM.md](ALGORITHM.md).
- **WD-26 [P2 | I85/E94/R05] Reject Historical Algorithm BP Definition**: Reject the older `spacing/testing/interleaving/application` BP formula. The locked `branch_diversity / work_break_alternation / focus_day_alternation` definition governs.

---

## 5. The Share Mechanism

Single owner for weekly shares, focus days, and evening physical activity mapping: [week-demand.json](week-demand.json). Quota rounding rules live in [ALGORITHM.md](ALGORITHM.md).

- **WD-27 [P1 | I93/E90/R06] One Mechanism For Both Branches**: Mental (`72` slots) and Physical (`72` in-Flow slots) use identical largest-remainder quota code over slot occurrences.
- **WD-30 [P2 | I86/E88/R07] Deterministic Tie-Break**: Break rounding ties by lowest focus-day capacity from [week-demand.json](week-demand.json).
- **WD-31 [P2 | I90/E75/R12] Shares Are Operator Dials**: Read weekly shares and focus days from [week-demand.json](week-demand.json) (`DD-02`, `DD-03`). Treat percentage numbers there as mutable dials snapped to `5%` steps (`DD-35`).
- **WD-32 [P1 | I88/E94/R06] Surface Zero-Share Epics**: Report any active Epic with zero allocated slots instead of dropping it silently.
- **WD-32b [P1 | I92/E96/R03] Evening Physical Courses Stay Outside In-Flow `P` Quota**: Exclude `18:30-19:30` evening physical courses (`60m`) from the `72 × 2m` in-Flow `P` denominator (`DD-39`, `DD-40`). Couple them via Gaussian proximity weighting in [ALGORITHM.md](ALGORITHM.md).

---

## 6. The Binding Notation

- **WD-33 [P1 | I90/E85/R07] Address Grammar**: A binding rule names a set of slot addresses and an
  Epic: `<day-set> <flow>_<iteration>_<branch> -> <Epic>`, where `*` matches any component and `+`
  joins days. Example: `*_*_I3_P -> Knee` binds the last physical slot of every Flow.
- **WD-34 [P1 | I88/E82/R08] Pins Are Constraints, The Rest Is Solved**: A rule pins its matched
  slots; the algorithm fills everything unpinned against the shares, spacing and interleaving. Pin as
  little as the intent requires.
- **WD-35 [P2 | I86/E78/R10] Prefer Positional Pins To Whole-Day Pins**: A positional pin repeats
  across the week and is maximally spaced by construction. A whole-day pin claims every slot of that
  day and leaves spacing nothing to work with inside it.
- **WD-36 [P2 | I84/E88/R08] Visualise The Effect, Not The Syntax**: Present every rule beside the
  slots it lights up, with the count it claims and the count left to the solver. Rendering the
  grammar as boxes teaches the syntax and hides the meaning.
- **WD-36a [P1 | I88/E90/R06] The Per-Day Band Renders Into Matrix 2**: The resolved day reaches the
  operator as a read-only band inside Precap Week Matrix 2, not as a separate surface. It shows the
  `P`, `M` and `R` bindings only; craft is omitted because the work package is authored in
  OpenProject and repeating it here would create a second authoring surface (`WD-06`). `DD-22`
  option A.
- **WD-36b [P0 | I94/E90/R05] Every Operator View Is Generated From The Inventory**: Human-facing
  renderings of the week are produced from `slot-inventory.json`, never hand-authored. A
  hand-built page is a drawing of a week, not a reading of one, and drifts from the contract the
  moment a time changes.

---

## 7. Decision Routing (Single-Owner Links)

- **Closed Dispersal Decisions (`DD-01`..`DD-40`, `SEQ-D1`..`SEQ-D4`, `OD-*`, `A-*`, `X-*`):** Archived in [log.md](log.md).
- **Active Register & Runtime Verification Scope:** Tracked in [ASSUMPTIONS-AND-DECISIONS-REGISTER.md](ASSUMPTIONS-AND-DECISIONS-REGISTER.md).
- **Orchestration-Wide Architecture Decisions (`D001`..`D019`):** Governed by `apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md`.

---

## 8. Entity Model Conformance

- **WD-37 [P1 | I92/E96/R04] Mirror The Canonical Schema**: The personal Epic database ([epics.json](epics.json)) mirrors
  `EPIC / BLOCK / CHUNK / NODE_PLACEMENT / SET_MEMBER / EDGE` ([EPICS-SCHEMA.md](EPICS-SCHEMA.md), `10_ENTITY_MODEL.md:13-78`). Never
  invent fields alongside it.
- **WD-38 [P1 | I90/E95/R05] A Sub-Block Is Not An Entity**: A Sub-Block is a `BLOCK` carrying a
  `parent_block_id` at level 2-4.
- **WD-39 [P1 | I93/E96/R04] Chunk Identity Is Canonical**: One canonical `CH_*` owns intrinsic
  content. A Chunk reaches an Epic through `NODE_PLACEMENT`, never by duplication; a placement never
  becomes a second Chunk.
- **WD-40 [P2 | I86/E92/R06] All-Branch Epic Set (6-Portfolio Craft Standard)**: The Epic database covers **all four branches**:
  Mental (`Intention`, `ACIM`, `Surrender`, `Breathing`), Physical (`Martial Arts`, `Dance`, `S/BJJ`,
  `General`, `Knee`), Regeneration (`Regeneration` Epic with `Yoga Nidra`, `Audiobooks`, and
  `Socializing` Blocks; `DD-17` closed), and Craft / Projects across the **6 Portfolio Areas** (`Leela`, `IPOS`,
  `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`) bound to OpenProject work packages (`DD-11`).

---

## 9. Failure Guards

Each guard names the silent failure it prevents.

- **WD-41 [P0 | I96/E94/R05] Reject A Non-Conformant Flow**: A Flow of any duration but 120 minutes
  fails loudly at generation. *Prevents:* a ragged Flow whose slot count silently differs from the
  quota denominator.
- **WD-42 [P0 | I95/E92/R06] Reject A Renamed Point Construct**: Any artifact using XP, TP or BP for
  a quantity other than its `ST-007`/`ST-008`/`WD-05` definition is non-conformant. *Prevents:* a
  header figure and an algorithm figure sharing a name while being different types, which reads as a
  data bug at the first drill-down.
- **WD-43 [P1 | I92/E90/R06] Surface A Zero-Share Epic**: An Epic allocated zero slots is reported,
  never silently dropped. *Prevents:* Knee disappearing from the plan because the source table never
  mentioned it.
- **WD-44 [P1 | I90/E88/R07] Refuse A Second Authoring Surface**: Any proposal that lets two
  surfaces author one assignment is refused. *Prevents:* the band reading "Intention x2" while the
  slots hold five, with nothing to reconcile them.
- **WD-45 [P1 | I90/E92/R06] Never Mint XP For `R`**: A nominal XP value for Regeneration is
  refused. *Prevents:* contradicting `ST-010` to work around a scheduling gap that structural BP
  balance already closes.
- **WD-46 [P1 | I88/E90/R07] Mark Derived Figures As Derived**: Any share, span or count this
  specification inferred rather than received carries that status in the artifact. *Prevents:* an
  inference hardening into a requirement — the failure that produced `DD-33` and `DD-34`.
- **WD-47 [P2 | I86/E94/R05] Search Rule Names, Not Only Values**: When inventorying a rule across a
  corpus, search the rule identifiers as well as their values. *Prevents:* the incomplete inventory
  that missed `monday_to_friday_only` and `weekday_scope` because neither names a weekday.
- **WD-48 [P1 | I92/E95/R04] Never Report Proposed As Applied**: A drafted amendment is reported as
  drafted until an executor returns an exact-match result. *Prevents:* a change set presented as
  landed while the artifacts still carry the old rule.
