---
type: Specification
id: SPEC-WEEKLY-DISPERSAL-v1.0
title: "Weekly Dispersal Specification — Flow Contract, Slot Inventory, Share Mechanism & Binding Notation"
description: "Canonical specification for the weekly dispersal slice: the 3x3 Flow contract, the three day regimes, the 240-occurrence slot inventory, the XP/TP/BP point model, the share-and-quota mechanism shared by Mental and Physical, the slot binding notation, and the full decision ledger."
status: operator_review_pending
date: 2026-11-09
scope: [sequencing, dispersal, precap-week, slots, epics, xp, bp, quota, notation]
tags: [sequencing, dispersal, specification, weekly-orchestration, precap-week, slot-inventory, quota]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Weekly Dispersal Specification

This specification is the **canonical source of truth** for the weekly dispersal slice: the mechanism
that decides which Mental, Physical, Craft and Regeneration content occupies which slot of which day,
and how that reaches Precap Week Matrix 2. It supersedes the working register as the decision record.

Companion artifacts: [ASSUMPTIONS-AND-DECISIONS-REGISTER.md](ASSUMPTIONS-AND-DECISIONS-REGISTER.md)
(working assumptions and conflict evidence), [PRECAP-INTEGRATION-ANALYSIS.md](PRECAP-INTEGRATION-ANALYSIS.md)
(the collision with Precap Week v2.0 and Handovers 03-06), [slot-inventory.json](slot-inventory.json)
(the generated inventory), [build_slot_inventory.py](build_slot_inventory.py) (its generator).

---

## 1. Core Architectural Invariants

- **WD-01 [P0 | I98/E96/R05] Reduced Slice, Not The Sequencing System**: Build only the four reduced
  parts — personal Epic database, `WeekDemand` shares, slot-filling algorithm, and the Precap Week
  surface. Never build or imply the Leela Path, Sequencing or Stats features. Borrow their schemas;
  do not reimplement their scope.
- **WD-02 [P0 | I98/E95/R04] The Flow Is 3x3 At 120 Minutes**: Every Flow is three slots by three
  iterations of the branch triple `[P, M, C]`, closing on one `R` break, totalling exactly 120
  minutes. One standard everywhere — weekday, weekend, project night or not. Reject any Flow of
  another duration rather than shortening a slot to fit.
- **WD-03 [P0 | I97/E98/R05] Branch Point Sourcing Is Absolute**: Branch `R` never sources XP and
  branch `C` never sources BP (glossary `ST-010`). Never mint XP for `R` to make it schedulable;
  reachability for `R` comes from the BP floor alone.
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
  four Flows plus a project night), `weekday_plain` (Thursday, Friday — four Flows), `weekend`
  (Saturday, Sunday — two Flows). Both weekday regimes carry identical slot counts; the regimes
  differ only in the evening.
- **WD-13 [P2 | I85/E88/R07] Project Night Is Not A Flow**: The Monday-to-Wednesday project night
  runs `20:00-21:30` and is an evening block, not a Flow; it contributes no slot occurrences
  (`DD-33` closed).
- **WD-14 [P1 | I90/E90/R06] The Declared Weekday Cut**: The morning anchor runs 30 minutes
  (`08:00-08:30`) and everything after it moves 30 minutes earlier against the inherited geometry.
  Flows run `08:30-10:30 / 10:30-12:30 / 13:45-15:45 / 16:00-18:00`, the midday anchor
  `12:30-13:30`, the evening block `19:00-20:00`, shutdown `21:30-22:00`. `DD-32` closed.
- **WD-14a [P2 | I84/E92/R05] Flows 1 And 2 Are Adjacent**: No turnaround separates Flow 1 from
  Flow 2. Each Flow already closes on its own 12-minute `R` break, so adjacency removes the
  inter-Flow gap only and never the break.
- **WD-14b [P2 | I82/E90/R06] Weekend Flows Start At Noon**: The two weekend Flows run `12:00-14:00`
  and `14:00-16:00`, back-to-back with no pause between them.
- **WD-14c [P1 | I88/E94/R04] Day Geometry Is Overlap-Checked**: The generator sorts every placed
  element per regime and rejects any overlap. The operator shifts these times by voice, and the
  first such shift drove the midday anchor into Flow 2.

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
  `21:30-24:00` night window is rest, not schedule, and is **not** a slot source.
- **WD-20 [P2 | I86/E90/R06] Anchors Are Outside The Quota**: The morning (`08:00-09:00`) and midday
  anchors are practice surface but carry no quota-bearing slots. The daily shutdown is never
  bindable.

---

## 4. The Point Model

- **WD-21 [P1 | I94/E96/R04] TP Is Determinate**: `1 TP = 1 minute` (`ST-007`), counted once across
  serial and concurrent activity. Every slot's TP is read off the Flow contract — 2, 3, 30 or 12 —
  never estimated. This determinacy is what makes `WD-04` computable.
- **WD-22 [P1 | I93/E92/R06] Objective Function**: Maximise projected XP subject to the BP floor.
  Per occurrence,
  `projected_xp = base_xp(chunk) x priority_factor(epic) x quality_multiplier(spacing, interleaving, chunking, testing)`,
  with `priority_factor` on Leela's Path-priority curve, `0.75x` at priority 1 to `1.50x` at
  priority 10 (`ST-034`).
- **WD-23 [P1 | I92/E90/R06] Dispersal Is Emergent, Not Scheduled**: The four scientific principles
  live in `quality_multiplier`. Binding one Epic into adjacent slots collapses its own spacing and
  interleaving multipliers, so clustering is self-penalising. Never hand-schedule dispersal that the
  objective already produces.
- **WD-24 [P1 | I91/E88/R07] BP Is A Floor, Not A Term**: A candidate week must clear the BP floor;
  among those that clear it, highest projected XP wins. Never weight BP against XP in one sum — a
  weighting either starves `R` or crowds out goal work, and needs a coefficient nobody can ground.
- **WD-25 [P2 | I88/E90/R07] Per-Component Floor**: The floor sets minima on each BP component
  separately. A single total lets a week buy past the floor on branch diversity while skipping rest
  entirely, which is the failure the floor exists to prevent. Values pending (`DD-16`).
- **WD-26 [P2 | I85/E94/R05] Glossary BP Supersedes The Algorithm Document**: Where the historical
  Algorithm document defines BP as `spacing 30 + testing 35 + interleaving 20 + application 15`,
  reject it. Those four components duplicate the XP `quality_multiplier` and leave branch diversity
  and rest unmeasured. The locked glossary (`authority_tier: 1`) governs.

---

## 5. The Share Mechanism

- **WD-27 [P1 | I93/E90/R06] One Mechanism For Both Branches**: Mental and Physical use identical
  share-and-quota code. Declare a share per Epic; the week's slots of that branch divide by largest
  remainder; ties resolve deterministically. Never special-case one branch as pattern-driven.
- **WD-28 [P1 | I90/E92/R05] Quota Is Occurrences, Not Minutes**: Shares bind slot occurrences. A
  share expressed as a priority weight drifts whenever the quality multipliers move, so the declared
  figure would not be the obtained figure.
- **WD-29 [P2 | I88/E90/R06] Rounding At The Week**: Round by largest remainder once per week and
  let per-day counts float. Per-day rounding compounds the error across seven days; carrying a
  fraction forward requires the cross-week state excluded by `DD-09`.
- **WD-30 [P2 | I86/E88/R07] Deterministic Tie-Break**: Ties go to the Epic with the least
  focus-day capacity — the one the weekend reduction penalises most is compensated first. Moving a
  focus day therefore moves the allocation with it, which a lexical or arbitrary tie-break would not.
- **WD-31 [P2 | I90/E75/R12] Shares Are Dials**: Share values are operator settings expected to
  change. No share figure in this specification is a finding, and no downstream artifact may treat a
  particular percentage as fixed.
- **WD-32 [P1 | I88/E94/R06] A Zero Share Is Schedulable Silence**: An Epic with a zero share draws
  no slots and the algorithm will never place it. Detect and surface this rather than letting an
  Epic vanish. Currently applies to **Knee**, which has no entry in the operator week table.

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

## 7. Decision Ledger

### 7.1 Closed

| # | Decision | Ruling |
|---|---|---|
| DD-01 | BP authority | Reinstated as a week-level feasibility floor on the locked glossary definition |
| DD-02 | Share expression | Quota of slot occurrences, not a priority weight |
| DD-03 | Focus-day strength | Not built this iteration; operator supplies focus-day specifications later |
| DD-04 | Knee branch | `P` Physical — knee training, settled on operator grounds |
| DD-05 | Sunday | ACIM on Sunday |
| DD-06 | Monday-Sunday span | All artifacts amended; Saturday and Sunday under a distinct regime |
| DD-07 | Thursday physical collision | Settled by the operator |
| DD-08 | Execution model | Build the algorithm, not a hand-written example week |
| DD-09 | Cross-week memory | Out of scope; stateless. Spaced repetition operates within the week |
| DD-10 | Physical allocation basis | Superseded by DD-34: physical uses the share mechanism |
| DD-11 | Special Projects source | OpenProject work packages |
| DD-12 | Deliverable home | Both repositories, one-way sync |
| DD-13 | Regeneration filling | By the algorithm via the BP floor; no nominal XP for `R` |
| DD-14 | Priority artifact name | `WeekDemand` (`week-demand.json`) |
| DD-15 | Sync direction | One source of truth, one-way copy |
| DD-19 | The Precap "XP" chip | Solve for XP; the percentage is a derived view (`WD-04`) |
| DD-20 | Sprint duration | No conflict: a sprint is 36 min, 30 is the craft block |
| DD-21 | Where practice binds | Inside the Flows — that is what a Flow is |
| DD-25 | Which BP the chip shows | Withdrawn; there is only one BP |
| DD-27 | Quota rounding | Largest remainder at the week |
| DD-29 | Recap branch | Craft (`WD-10`) |
| DD-30 | Weekend Flow shape | The same 120-minute standard; `12:00-14:00` and `14:00-16:00`, adjacent |
| DD-22 | The per-day band | **Option A.** A read-only readout rendered into Precap Week Matrix 2. Craft is omitted — it is authored in the work-package surface (`WD-06`) |
| DD-32 | Weekday re-cut | Declared: 30-minute morning anchor, everything after it 30 minutes earlier, Flows 1 and 2 adjacent (`WD-14`) |
| DD-33 | Project-night times | `20:00-21:30` |
| DD-34 | Physical shares | Knee raised to 15%; the remaining 85% keeps the week-table proportions `3:2:1:1` |
| DD-31 | Week table to Epics | Five physical Epics; EFX dropped |
| A-09 | Wednesday Special Project Day | Doubles: project night and slot share both |
| A-10 | Night window | Withdrawn as malformed; `R` is an ordinary branch (`WD-19`) |
| A-11 | Weekend Flow count | Two |
| A-12 | StatusMerge day | Saturday or Sunday; propagate everywhere Saturday is hard-coded |

### 7.2 Open

| # | Decision | Recommendation |
|---|---|---|
| DD-16 | BP floor values | Per-component minima; values follow the slot inventory |
| DD-17 | Which Epic owns `R` content | One `Regeneration` Epic with Blocks, not one per activity |
| DD-18 | Weekend regime content | Reduced slot count under the same algorithm — settled at two Flows |
| DD-23 | "Path and Sequencing paused" | Qualify: the Leela feature is paused, the dispersal slice is active |
| DD-24 | Stale weekend text in Handovers 04, 05 | Fix now, before ratification reintroduces `Sun OFF` |
| DD-26 | Dependency-view choice | No recommendation; its own DoD requires an unrun OpenProject edge count |
| DD-28 | HANDOVER-05 XP chip amendment | Amend now; the definition is already a `[P0]` spec invariant |
| DD-35 | "Optimized to 5-minute iterations" | Not applied. Two readings: (a) declared shares round to 5-percentage-point steps, giving `35/25/10/15/15`; (b) the `P`+`M` pair is the 5-minute iteration unit and allocations must fill whole pairs. Reading (b) is already true of the Flow — 2 + 3 = 5 — which makes (a) the likelier ask |
| DD-36 | Evening block content | `19:00-20:00` is declared but unnamed. Not yet a slot source |
| DD-37 | Thursday and Friday evening | Those days have `18:00-19:00` and `20:00-21:30` unallocated, since only Monday to Wednesday carry a project night |

---

## 8. Entity Model Conformance

- **WD-37 [P1 | I92/E96/R04] Mirror The Canonical Schema**: The personal Epic database mirrors
  `EPIC / BLOCK / CHUNK / NODE_PLACEMENT / SET_MEMBER / EDGE` (`10_ENTITY_MODEL.md:13-78`). Never
  invent fields alongside it.
- **WD-38 [P1 | I90/E95/R05] A Sub-Block Is Not An Entity**: A Sub-Block is a `BLOCK` carrying a
  `parent_block_id` at level 2-4.
- **WD-39 [P1 | I93/E96/R04] Chunk Identity Is Canonical**: One canonical `CH_*` owns intrinsic
  content. A Chunk reaches an Epic through `NODE_PLACEMENT`, never by duplication; a placement never
  becomes a second Chunk.
- **WD-40 [P2 | I86/E92/R06] Epic Set**: Four Mental Epics (Intention, ACIM, Surrender, Breathing),
  five Physical (Martial Arts, Dance, S/BJJ, General, Knee), and one Regeneration Epic pending
  `DD-17`. Craft Epics are OpenProject work packages, not personal Epics.

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
  refused. *Prevents:* contradicting `ST-010` to work around a scheduling gap that the BP floor
  already closes.
- **WD-46 [P1 | I88/E90/R07] Mark Derived Figures As Derived**: Any share, span or count this
  specification inferred rather than received carries that status in the artifact. *Prevents:* an
  inference hardening into a requirement — the failure that produced `DD-33` and `DD-34`.
- **WD-47 [P2 | I86/E94/R05] Search Rule Names, Not Only Values**: When inventorying a rule across a
  corpus, search the rule identifiers as well as their values. *Prevents:* the incomplete inventory
  that missed `monday_to_friday_only` and `weekday_scope` because neither names a weekday.
- **WD-48 [P1 | I92/E95/R04] Never Report Proposed As Applied**: A drafted amendment is reported as
  drafted until an executor returns an exact-match result. *Prevents:* a change set presented as
  landed while the artifacts still carry the old rule.
