---
type: Reference
id: MOA-SEQ-DISPERSAL-REGISTER
title: Weekly dispersal assumptions and decisions register
description: What the operator confirmed, what is inferred, what conflicts, and what still needs a ruling before the weekly dispersal system is authored.
status: working
as_of: 2026-11-09
tags: [sequencing, dispersal, weekly-orchestration, precap-week, epics, rhythm, path, algorithm]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Weekly dispersal — assumptions and decisions register

**The governed record is now [SPEC-WEEKLY-DISPERSAL.okf.md](SPEC-WEEKLY-DISPERSAL.okf.md)** — rules `WD-01`..`WD-48` and the full decision ledger. This file is the **working** record: operator inputs, assumptions, conflict evidence, and the applied amendment. Where the two differ, the specification governs.

Scope: the mechanism that decides which Mental, Physical, Craft and Regeneration content occupies which slot of which day, and how that reaches Precap Week Matrix 2. Related: [index.md](index.md) (bundle), [decisions.md](../decisions.md) open choice N05, and [PRECAP-INTEGRATION-ANALYSIS.md](PRECAP-INTEGRATION-ANALYSIS.md).

## 1. Build scope — a reduced slice, not the Sequencing system

The Sequencing system is **not** being built. Four parts are, and each one substitutes for a canonical Leela layer while borrowing its schema. Leela's runtime spine (`10_ENTITY_MODEL.md:80-108`) maps 1:1 onto the reduced build:

| Leela layer | Canonical role | Reduced build | Status |
|---|---|---|---|
| **Skill Tree** | navigate and select target | **Personal Epic database** (JSON): Epic > Block > Sub-Block > Chunk | BUILD |
| **Path** | weekly demand (`PathCycle` > `PathDemandLine`) | **`WeekDemand`** — operator-set weekly priority shares only | BUILD (substitute) |
| **Sequencing** | decide and execute (`ResolvedSequenceRecommendation` > `SequenceInstance` > `SlotRun`) | **Small slot-filling algorithm** | BUILD |
| **Rhythm** | time placement (`BookableSlot` > `PlacedEvent`) | **Precap Week** Matrix 2 | EXISTS |
| **Stats** | realized truth (`xp_ledger`, `v_stats_week`, `v_bp_week`) | — | EXCLUDED, later development |

Reassigned ownership, superseding the first-iteration mapping:

| Operator term | Owner in the reduced build | Mechanism | Authority |
|---|---|---|---|
| Focus days (Intention Mon/Wed/Fri) | **Precap Week** | Per-day assignment in Matrix 2 | OD-13 |
| Day shape (Morning Routine, Flow 1-4, evening block) | **Precap Week** | Matrix 2 slot inventory | OD-14 |
| Intention 40 / ACIM 20 / Surrender 20 / Breathing 20 | **`WeekDemand`** | Operator-set shares; no Path feature is built | OD-12, DD-02 |
| Interleaving, spaced repetition, chunking, testing | **The algorithm** | Quality multipliers on projected XP | OD-15 |
| Intention / Surrender / ACIM as individual Epics | **Personal Epic database** | `EPIC` rows in the skill tree | OD-05, OD-16 |
| Which practice fills a slot | **The algorithm** | `slot -> chunk` binding | OD-09 |
| "Constantly practiced throughout the week" | **The algorithm** | Emergent: repetition suppresses the spacing and interleaving multipliers | §1.1 |
| Balance Points | **The algorithm** | Week-level feasibility floor; the only point source branch `R` has | OD-21, X-01 |
| Regeneration content reaching the plan | **The BP floor** | `rest_adherence` cannot be satisfied without `R` | OD-22, X-06 |
| Up to 3 prioritised bullets per day per branch | **Precap Week** Matrix 2 | Per-day settings band | OD-10 |

### 1.1 What the algorithm solves for

**Objective: maximise projected XP within a Balance-Point floor on the week.** Because Stats is excluded there is no realized XP, so both quantities are *projected* — the Algorithm-calculated stage, never a Run fact.

Per occurrence:

`projected_xp = base_xp(chunk) x priority_factor(epic) x quality_multiplier(spacing, interleaving, chunking, testing)`

- `priority_factor` uses Leela's Path-priority XP curve: **0.75x at priority 1 to 1.50x at priority 10** (glossary ST-034).
- `quality_multiplier` carries the four principles. This is the mechanism that makes dispersal emerge rather than being hand-scheduled: binding the same Epic into adjacent slots collapses its own spacing and interleaving multipliers, so clustering is self-penalising under an XP objective.
- Operator shares are enforced as **quotas**, not as priorities — see DD-02.

Per week, as a property of the whole assignment rather than of any single occurrence (`v_bp_week`, `10_ENTITY_MODEL.md:130`):

`projected_bp = branch_diversity(50) + work_break_alternation(25) + focus_day_alternation(25)`

Components per the operator's correction of 2026-11-09, superseding the glossary's generic wording:
- **`branch_diversity` (50)** — spread across `P / M / C / R`. **Never repository diversity**, which is what HANDOVER-05 proposed and which is rejected.
- **`work_break_alternation` (25)** — that each craft block is followed by its recap and each flow by its 12-minute break. Structural and per-flow verifiable, not a week-level estimate.
- **`focus_day_alternation` (25)** — that emphasis days alternate across **whichever** days carry emphasis (OD-07), not a hard-coded Monday/Wednesday pair. A week stacking all focus days consecutively fails this component even when all seven days are planned.

**BP is a feasibility floor, not a second term in the objective.** A candidate week must clear the floor; among the weeks that clear it, the highest projected XP wins. Nothing has to be tuned to trade one point type against the other, and goal work is never crowded out by balance work. See DD-01.

### 1.1.1 Why reinstating BP is the countermeasure X-06 needed

| Branch | Sources XP | Sources BP | Consequence for the algorithm |
|---|---|---|---|
| `P` Physical | yes | yes | ranked by XP, also feeds balance |
| `M` Mental | yes | yes | ranked by XP, also feeds balance |
| `C` Craft | yes | **never** (ST-010) | ranked by XP only |
| `R` Regeneration | **never** (ST-010) | yes | **reachable only through BP** |

`R` scores exactly zero XP by rule, so under an XP-only objective it was unschedulable (X-06). Under the floor it becomes mandatory instead: `work_break_alternation` cannot be satisfied without the `R` break closing each flow, and `branch_diversity` cannot be satisfied unless all four branches appear. BP's third component, `alternation`, additionally penalises same-branch adjacency — branch-level interleaving that a per-occurrence multiplier cannot express. The two point types are therefore orthogonal by construction: **XP decides what advances goals, BP decides how the week is spread.**

### 1.2 Schema to build upon (`10_ENTITY_MODEL.md:13-78`)

Already defined; the personal database mirrors it rather than inventing fields.

```
EPIC            { epic_id "EP_hex12", epic_slug, epic_name, version }
BLOCK           { block_id "BL_hex14", epic_id, level 1-4, label, parent_block_id, sort_order }
CHUNK           { chunk_id "CH_hex14", chunk_ref, chunk_name, branch P|M|C|R,
                  activity_types, media_type, lvl, description, process, intensity, tags }
NODE_PLACEMENT  { epic_id, node_key "N###", chunk_id, time_mode, min, avr, max,
                  block1..4_id, bundle_label, fusion_label, node_sort_order }
SET_MEMBER      { set_id "ST_hex", set_type "bundle|fusion", member_node_key }
EDGE            { from_node_key, to_node_key, edge_type "hard_successor|soft_successor" }
```

- A **Sub-Block is not a separate entity**: it is a `BLOCK` with a `parent_block_id`, at level 2-4.
- `chunk_id` is unique within an Epic; `CH_*` is the cross-feature content identity (`SSOT-D-047 §8`).
- A Chunk reaches an Epic through `NODE_PLACEMENT`, never by duplication (`2026-10-22 placement handover:35-37`).
- `NODE_PLACEMENT.min/avr/max` carry minutes, which is where slot durations come from.

## 2. Confirmed operator inputs

- OD-01: The practice is **ACIM** (A-C-I-M). The week table's "Asana" and the earlier spelling "ASIM" are both artifacts of the same practice. Canonical label is `ACIM`. No Asana or posture practice is implied.
- OD-02: The system is a dispersal puzzle built on **interleaving, spaced repetition, chunking and testing**.
- OD-03: Mental shares are **Intention 40 percent, ACIM 20, Surrender 20, Breathing 20**.
- OD-04: The week is **Monday to Sunday**. Precap Week v4 is to be changed for both Saturday and Sunday.
- OD-05: Each mental practice is an **individual Epic**: Intention, Surrender, ACIM, Breathing.
- OD-06: Current physical Epics are **Dancing**, **Martial Arts**, and **Knee**.
- OD-07: Operator-defined **focus days**: Intention Mon/Wed/Fri, Surrender Tue, Breathing Thu, ACIM Sun.
- OD-08: In the physical week pattern, **Kombo becomes Dancing**. Settled.
- OD-09: Conform to Sequencing: its Algorithm and its Epics. A standalone allocation mechanism is refused.
- OD-10: **Matrix 2 carries a per-day settings band** beneath each column with up to three prioritised bullets each for Mental, Physical, Special Projects and Regeneration.
- OD-11: ~~Balance Points are dropped; XP only.~~ **SUPERSEDED by OD-21.**
- OD-12: The Path feature is **not** built. Only the **priority setting** is — an operator decision per week.
- OD-13: Focus days are owned by **Precap Week**, not Rhythm.
- OD-14: The day shape is owned by **Precap Week**, not Rhythm.
- OD-15: Interleaving, spaced repetition, chunking and testing are **represented inside the algorithm**.
- OD-16: Intention, Surrender and ACIM as individual Epics belong in the **personal skill tree**.
- OD-17: **Stats is excluded** for now; later development.
- OD-18: The personal Epic database is expressed as **JSON**, in `Epic > Block > Sub-Block > Chunk` orientation, built on existing structure where it exists.
- OD-19: Deliverables live in **both** `MasterOfArts` and `apexai-os-meta`, kept in step by a **sync script** that updates each from the other.
- OD-20: Work order is **slots first, then the filling system**.
- OD-21: **Balance Points are reinstated**, superseding OD-11. BP is the countermeasure that makes Regeneration placeable and supplies the week-level dispersal pressure XP alone cannot generate.
- OD-22: **Regeneration must be included.** It is not optional content and may not be omitted from the week.
- OD-23: Sprint length is **30 minutes, fixed as the default** — refined by OD-29 to mean the **craft block** within a 36-minute sprint.
- OD-29: **A Flow is a `3x3` schedule**: three slots x three iterations — three mental blocks of 3 minutes, three physical of 2 minutes, three craft of 30 minutes, one minute of recap per craft sprint, plus a 12-minute break. Totals 120 minutes. Grounded at `qmd #1a447e:47-57`.
- OD-30: **BP components are branch diversity, work/break alternation, and focus-day alternation** — not repository diversity, and not a hard-coded Monday/Wednesday pair. Supersedes HANDOVER-05's reading.
- OD-31: **XP is solved for, not renamed.** TP is determinate per slot, so `XP = leverage x TP` applies to work and practice alike; a percentage display is a derived view of that quantity.
- OD-32: **Regeneration is included**, confirming OD-22 against the XP-only objection.
- OD-33: **Saturday and Sunday carry two flows each**, against four on Monday to Friday. Settles A-11 and fixes the quota denominator at 72 mental slots per week.
- OD-34: **Every flow is 120 minutes — one standard, no per-flow variation.** Supersedes the flexing craft block of the first reconciliation: the craft block is always 30 minutes. Consequence: the live Matrix 2 flows F2 (75 min) and F4 (105 min) are **non-conformant** and the weekday must be re-cut. See DD-32.
- OD-35: **Physical Epics are Martial Arts, Dance, S/BJJ, General and Knee.** Week-table mapping: Strikes and Kicks to Martial Arts; Dance and Moves to Dance; S/BJJ its own Epic; Running and Stretch to General; **EFX dropped**; Knee a separate Epic with no week-table entry.
- OD-36: **The 1-minute recap is owned by Craft**, confirming DD-29. It is the closing minute of the craft block, not a slot of its own, so the mental denominator stays 72.
- OD-37: **Weekend flows use the same 120-minute standard.** Confirms DD-30's shape; the clock times remain unset.
- OD-38: Produce **processes, wireframes and user stories** for the open decisions and ambiguities, not prose alone. Delivered as the published blueprint page.
- OD-39: **Three day regimes, not two.** Monday to Wednesday carry a **project night**; Thursday and Friday do not; the weekend is its own regime at two flows. Both weekday regimes run the same four flows, so slot counts are unaffected — the regimes differ only in the evening.
- OD-40: **Physical uses the same share mechanism as mental.** Supersedes A-06's pattern-driven reading. Shares are operator dials on both branches and are expected to change over time, so the register no longer treats a particular set of percentages as settled.
- OD-41: **Regeneration is an ordinary branch.** Its slots are the 24 in-flow breaks, carrying `R` content such as Yoga Nidra or reading. The 21:30-24:00 night window is **not a slot source**. Closes A-10, which was malformed.
- OD-42: **Wednesday doubles.** Dance and Martial Arts take the Wednesday project night *and* their share of the physical slots. Closes A-09.
- OD-43: **StatusMerge may be Saturday or Sunday.** Either is acceptable; propagate the change everywhere Saturday is hard-coded. Closes A-12.
- OD-44: The default weekday is **not verified**. The re-cut in DD-32 remains a proposal.
- OD-24: The **Knee Epic is branch `P`** — it is training for the knee, not recovery content.
- OD-25: Branch `R` carries substantial Chunk content, including **Yoga Nidra, audiobooks and socializing**. It is not a thin branch.
- OD-26: The week is planned **Monday to Sunday**. Saturday and Sunday are **not excluded** — they run under a **different regime, a different standard** from Monday to Friday.
- OD-27: **Focus-day specifications will be supplied later** by the operator (DD-03).
- OD-28: Precap Week amendments are to be **shown before they are applied**.

## 3. Assumptions

Each assumption states what fails if it is wrong.

- A-01 **Flow composition — CLOSED, grounded in canon (`qmd #1a447e:47-57`, `#46ebe0:17-27,48-49`).** A Flow is `3 slots x 3 iterations` of the branch triple `[P, M, C]`, closing on `R`. With the operator's minutes: `3 x (P 2 + M 3 + C 30 + recap 1) + R 12 = 120 min`, which is exactly Flows 1 and 3 in the live Matrix 2. `30er` is the **craft block**; the `3`s are the mental and physical micro-blocks ahead of it. A sprint is 36 minutes, not 30. Practice overhead is fixed at 18 min + 12 min break per flow, so **the craft block absorbs each flow's remaining time** (30/15/30/25) and the practice slot count is invariant. See integration analysis §2-§3.
- A-08 **Morning anchor — CLOSED.** The mental quota's denominator is the **12 in-flow `M` slots per day**, not the `08:00-09:00` anchor. The anchor is additional practice surface outside the quota.
- A-11 **Weekend flow count — CLOSED by OD-33.** Two flows on each of Saturday and Sunday.
- A-09, A-10, A-12 **All CLOSED** by OD-42, OD-41 and OD-43. A-10 was withdrawn as malformed rather than answered: `R` is an ordinary branch and the bindable-versus-protected framing did not apply to it.
- A-13 **Project-night times — OPEN.** "from 8 to 2030" is read as **20:00-20:30**, a 30-minute block. If it means 18:00-20:30 the evening is a 150-minute block instead. Recorded as DD-33; does not affect slot counts, since the project night is not a flow.
- A-14 **Physical shares are derived, not declared.** The percentages in the inventory come from day frequency in the operator week table. They are a starting point only, and they give Knee zero. Recorded as DD-34.

## 3.1 Slot inventory — BUILT

[slot-inventory.json](slot-inventory.json), generated by [build_slot_inventory.py](build_slot_inventory.py). OD-20's first ordered step is complete.

Visual blueprint for the operator: <https://claude.ai/artifact/4QEZffC7rxdqwKxVC9hcax>

| | Weekday (x5) | Weekend (x2) | Week total |
|---|---|---|---|
| Flows per day, 120 min each | 4 | 2 | **24** |
| `M` mental slots, 3 min | 12 | 6 | **72** (216 min) |
| `P` physical slots, 2 min | 12 | 6 | **72** (144 min) |
| `C` craft blocks, 30 min | 12 | 6 | **72** (2,160 min) |
| `R` flow breaks, 12 min | 4 | 2 | **24** (288 min) |

240 slot occurrences carry stable ids of the form `SO_MON_F2_I1_M` — day, flow, iteration, branch. Verification: every one of the 24 flows satisfies `duration == 120` and `sum(slot minutes) + recap minutes == 120`, the craft block is 30 everywhere, and the 240 ids are unique. Total flow time is 2,880 min = 48.0 h per week. The generator raises on any flow duration other than 120 (OD-34), so a non-conformant day fails loudly rather than producing a ragged flow.

Three regimes (OD-39). Both weekday regimes run four flows, so they differ only in the evening:

| Regime | Days | Flows/day | Evening |
|---|---|---|---|
| `weekday_project` | Mon, Tue, Wed | 4 | Project night (A-13 for the times) |
| `weekday_plain` | Thu, Fri | 4 | open |
| `weekend` | Sat, Sun | 2 | open |

**Shares, one mechanism for both branches (OD-40).** `allocate_quota()` is shared code: largest remainder at the week, ties to the Epic with the least focus-day capacity. These are dials and will move, so the figures below are the current setting, not a finding.

| Mental | Share | Slots | | Physical | Share | Slots |
|---|---|---|---|---|---|---|
| Intention | 40% | 29 | | Martial Arts | 43% | 31 |
| ACIM | 20% | 15 | | Dance | 29% | 21 |
| Surrender | 20% | 14 | | S/BJJ | 14% | 10 |
| Breathing | 20% | 14 | | General | 14% | 10 |
| | | | | **Knee** | **0%** | **0** |

The mental tie went to ACIM: its focus day is Sunday, a two-flow day with 6 mental slots against 12 on Tuesday and Thursday, so the weekend cut penalises ACIM alone. **Physical shares are derived from week-table day frequency and give Knee nothing** (A-14, DD-34) — either a declared share or the positional pin `*_*_I3_P -> Knee` fixes it, the latter without touching any share.
- A-02 **Branches — CONFIRMED.** Intention, Surrender, ACIM and Breathing are branch `M`. Dancing, Martial Arts and Knee are branch `P` (OD-24). Regeneration content (Yoga Nidra, audiobooks, socializing, OD-25) is branch `R` and needs at least one Epic of its own, which does not yet exist — see DD-17.
- A-03 **Quota basis.** The 40/20/20/20 split is read as a share of mental **slot occurrences**, not of minutes. Mental slots are uniform in length under A-01, so the two coincide; occurrences are the directly schedulable unit and need no duration estimates. See DD-02.
- A-04 **Focus days are hard per-day assignments.** With Rhythm dropped as owner (OD-13), focus days are authored directly into Matrix 2 rather than expressed as soft emphasis curves. Focus-day *strength* as a tunable is deferred (DD-03).
- A-05 **Cycle start.** One week per cycle, starting Monday.
- A-06 **Physical is pattern-driven, mental is quota-driven.** The operator considers the physical allocation already given by the week table (Mon Strikes, Tue Kicks, Wed Dance, Thu Moves, Fri Kicks, Sat EFX plus S/BJJ, Sun Running and Stretch; muscle focus Push/Pull, Running/Beine, Core on rotation). Physical therefore needs no percentage quota — the weekday pattern *is* the assignment. Only Mental is dispersed by quota plus algorithm. **If wrong, the physical Epics need shares like the mental ones.**
- A-07 **Projected, not realized XP.** With Stats excluded there is no `xp_ledger`, so the algorithm optimises the Algorithm-calculated projected stage only. No Run facts exist and none may be claimed.

## 4. Conflicts requiring a ruling

- X-01 **BP double definition — REOPENED by OD-21, now RULED.** With BP reinstated the two definitions collide again. **The locked glossary wins:** `branch balance 50 + rest adherence 25 + alternation 25`. Two grounds, neither a preference:
  - *Authority.* The glossary carries `authority_tier: 1` and `status: locked`. The Algorithm document sits in `quasi/`, unlocked and unratified.
  - *Mechanism.* The Algorithm document's components are `spacing 30 + testing 35 + interleaving 20 + application 15` — the same four principles the XP `quality_multiplier` already carries (§1.1). Adopting them would score one effect twice under two names, and would leave `branch_balance` and `rest_adherence` unmeasured, which are precisely the two things the reinstatement exists to measure. The glossary's components are orthogonal to XP; the Algorithm document's are a duplicate of it.
  The Algorithm document's definition is recorded as **superseded**.
- X-02 **Sunday — CLOSED by OD-07 and OD-04.** ACIM takes Sunday. Precap Week changes accordingly.
- X-04 **Thursday physical collision — CLOSED by OD-08.** Settled by the operator.
- X-05 **"Chunking" overloaded — CLOSED.** OD-02 means the principle dial, not the `Chunk` entity.
- X-03 **Week span is contradicted in three artifacts, not one — OPEN.** DD-06 was reported as verified; it is not. Evidence gathered this session:
  - `SPEC-PRECAP-WEEK-ITERATIONS.okf.md:24` — "Full-width **Monday–Saturday** hourly table"; `:200` repeats it; `:209-214` renders `<th>` columns Monday through Saturday; `:113` states "**Sunday OFF by default**".
  - `.claude/skills/PrecapWeek/references/validation-checklist.md:39-41` — `monday_to_friday_scope_only: true`, `saturday_excluded: true`, `sunday_regular_planning_excluded: true`.
  - `.claude/skills/PrecapWeek/SKILL.md:36-44` — scope `Monday_to_Friday_weekday_planning`; `Saturday_planning` and `Sunday_regular_day_planning` are listed as **forbidden**, not merely absent.
  Two of the three are hard prohibitions, so Monday-Sunday cannot be produced until they are amended. **Ruled by OD-26: all three are amended, Saturday and Sunday admitted under a distinct regime.** The three-artifact count was itself understated: the prohibition lived in **five** files, two of which name no weekday at all (§7.5). Status: **CLOSED — 22 edits applied across 5 files on 2026-11-09**, verified by table-column arithmetic, YAML parse and a token sweep. See §7.
- X-06 **XP-only makes Regeneration unschedulable — CLOSED by OD-21.** Branch `R` **never sources XP** (glossary ST-010), so under an XP-only objective `R` scored zero and would never be placed. Reinstating BP restores the only point source `R` has, and the `rest_adherence` component makes `R` mandatory rather than merely eligible (§1.1.1). The two consequences recorded earlier are both discharged: Knee is branch `P` on the operator's own grounds (OD-24, it is knee *training*), not as a workaround; and the Regeneration bullet row is now algorithm-reachable, so no fixed-binding fallback is needed (DD-13 reversed).

## 5. Open decisions

### 5.1 Closed

| # | Decision | Ruling |
|---|---|---|
| DD-01 | BP authority | **Reinstated as a week-level feasibility floor**, computed on the locked glossary definition (OD-21, X-01). XP stays the objective; BP is the constraint. |
| DD-02 | How `WeekDemand` expresses 40/20/20/20 | **Quota of slot occurrences.** 40 percent of the available mental slots must bind Intention; the algorithm maximises XP in choosing *which* ones. A priority weight was rejected: the realised share drifts whenever the quality multipliers move, so the number set would not be the number obtained. |
| DD-03 | Focus-day strength | **Not built in this iteration.** Focus days are fixed per-day assignments; operator will supply focus-day specifications later (OD-27). |
| DD-04 | Knee Epic branch | **`P` Physical** — knee *training* (OD-24). Settled on the operator's own grounds, no longer contingent on X-06. |
| DD-05 | Sunday | **ACIM on Sunday** (OD-07). |
| DD-06 | Which artifacts absorb Monday-Sunday | **All three**, in one amendment, with Saturday and Sunday under a distinct regime rather than as ordinary weekdays (OD-26). Change set drafted, not applied (OD-28, §7). |
| DD-07 | Thursday physical collision | **Settled by the operator** (OD-08). |
| DD-08 | Execution model | **Build the small algorithm.** The earlier wording asked whether to hand-write one week as a conformant example or build a resolver; the operator chose to build. |
| DD-09 | Cross-week memory of what ran | **Out of scope. Stateless for now.** Spaced repetition operates within the week only; a last-run ledger is future development alongside Stats (OD-17). |
| DD-10 | Physical shares and focus days | **Already given by the week table.** Physical is pattern-driven, not quota-driven (A-06). |
| DD-11 | Special Projects source | **OpenProject work packages.** |
| DD-12 | Home for the deliverables | **Both repositories, synced by script** (OD-19). |
| DD-13 | How Regeneration slots are filled | **By the algorithm, via the BP floor** — reversed from the earlier fixed-binding recommendation, which existed only because XP-only left `R` at zero. No nominal XP is minted for `R`; ST-010 holds (X-06). |
| DD-14 | Naming of the priority artifact | **`WeekDemand`** (`week-demand.json`). The runtime spine already labels this layer "Path (weekly demand)" with line item `PathDemandLine`, so the noun is inherited, not invented, and cannot be mistaken for the Path feature that is not being built. |
| DD-15 | Sync-script direction | **One source of truth in `MasterOfArts`, one-way copy to `apexai-os-meta`.** A bidirectional mirror of one file across two Git repositories produces conflicts with no merge authority. |

### 5.2 Open

All fifteen first-generation decisions are now closed. Three new ones arise from the BP reinstatement and the Monday-Sunday ruling.

| # | Decision | Options | Recommendation |
|---|---|---|---|
| DD-16 | The numeric BP floor a week must clear | a fixed threshold on the 100-point total / per-component minima on `branch_balance`, `rest_adherence`, `alternation` / all three components mandatory at full value | **Per-component minima.** A single total lets a week buy its way past the floor with branch balance alone while skipping rest entirely, which is the failure the reinstatement exists to prevent. Exact values depend on the slot count per day, so they are proposed with the slot inventory, not before it. |
| DD-17 | Which Epic owns branch `R` content (OD-25) | one `Regeneration` Epic with Blocks for Yoga Nidra / audiobooks / socializing / one Epic per activity, as with Mental | **One `Regeneration` Epic with Blocks.** The Mental practices are separate Epics because each carries its own weekly share (OD-03); `R` content has no per-activity share, so splitting it buys nothing and multiplies placement rows. |
| DD-18 | Saturday and Sunday regime content | weekend days carry a reduced slot count under the same algorithm / weekend days are operator-authored only, algorithm excluded / full parity with weekdays | **Reduced slot count, same algorithm.** OD-26 makes the weekend a different standard, not a different mechanism; a second mechanism would need its own conformance surface. Awaiting the focus-day specifications (OD-27) for the actual counts. |

## 6. Not verified in this session

- OpenProject was not queried. The live calendar was not read.
- Monday-Sunday is **applied** (§7), but no Precap Week brief has been *generated* under the amended rules. The amendment is verified structurally — column arithmetic, YAML parse, token sweep — not by producing a week.
- The physical pattern was read off the operator's week table, not from a committed artifact (A-06).
- No Chunk-level content exists yet for any of the Epics; only Epic identities and the `R` content hints of OD-25 are known.
- The BP floor values (DD-16) are undetermined; they depend on the slot inventory, which is next.

## 7. Monday-Sunday amendment — APPLIED 2026-11-09

Approved by the operator and written. **The change set grew from 14 edits across 3 files to 22 edits across 5 files**, because the drafted inventory was incomplete — see §7.5. The amendment admits Saturday and Sunday and names a **weekend regime** distinct from the weekday regime; it does not invent the weekend regime's content, which is DD-18.

Verification run after writing:
- Calendar table: 9 header cells; all 17 rows sum to exactly 9 columns under `colspan`/`rowspan` accounting.
- YAML: 31 fenced blocks across the four skill files parse clean under `yaml.safe_load`.
- Prohibition sweep: no `monday_to_friday`, `Saturday_planning`, `Sunday_regular_day_planning`, `saturday_excluded`, `Sunday OFF` or `weekday_scope` token remains in the PrecapWeek skill or the spec.

### 7.1 `apex-meta/.../01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md`

| # | Line | From | To |
|---|---|---|---|
| A1 | 24 | "Full-width **Monday–Saturday** hourly table ... (unchanged and validated)." | "Full-width **Monday–Sunday** hourly table ... **Monday–Friday run the weekday regime; Saturday and Sunday run the weekend regime** - same mechanism, reduced slot count, distinct standing content." |
| A2 | 67 | "progress will be achieved by **Saturday** close" | "by **Sunday** close" |
| A3 | 75 | "milestones to celebrate upon **Saturday** review" | "upon **Sunday** review" |
| A4 | 113 | "`21:00` Daily Shutdown, **Sunday OFF by default**." | "`21:00` Daily Shutdown. **Sunday is planned** under the weekend regime; it is no longer OFF by default." |
| A5 | 200 | "table spanning **Monday through Saturday**" | "table spanning **Monday through Sunday**" |
| A6 | 206, 210-215 | `min-width:1150px`; six day columns at `width:13.6%`; last `<th>` is Saturday | `min-width:1300px`; seven day columns at `width:11.7%`; a **Sunday `<th>`** appended after Saturday |
| A7 | 16 sites in `<tbody>` | every `colspan` sized for 8 total columns | each `colspan` incremented by one for 9 total columns: `7 -> 8` (x4), `6 -> 7` (x11), `5 -> 6` (x1) |

A6 arithmetic: `12% + 6% + 6 x 13.6% = 99.6%` becomes `12% + 6% + 7 x 11.7% = 99.9%`.

**A7 was not in the drafted set.** The table body carries no per-day cells — every row spans the days with `colspan` placeholders. Adding a seventh day column without incrementing all sixteen would have produced a malformed table in which the body is one column narrower than the header, so A7 is a material enabler of A6 rather than separate work.

### 7.2 `.claude/skills/PrecapWeek/references/validation-checklist.md`

| # | Line | From | To |
|---|---|---|---|
| B1 | 26-32 | `allowed_days:` Monday..Friday | append `- Saturday`, `- Sunday` |
| B2 | 33-35 | `excluded_days: [Saturday, Sunday_regular_day_planning]` | `excluded_days: []` plus a new `weekend_regime_days: [Saturday, Sunday]` |
| B3 | 36-37 | `allowed_sunday_exception: [Sunday_weekly_precap_session]` | retained verbatim - the Sunday precap session remains an anchor, now inside scope rather than an exception |
| B4 | 39-41 | `monday_to_friday_scope_only: true` / `saturday_excluded: true` / `sunday_regular_planning_excluded: true` | `monday_to_sunday_scope: true` / `saturday_weekend_regime_applied: true` / `sunday_weekend_regime_applied: true` |
| B6 | 292 | `trigger: request_extends_beyond_monday_to_friday_or_sunday_weekly_precap_exception` | `trigger: request_extends_beyond_monday_to_sunday_planning_scope` |
| B5 | 44-45 | `forbidden_scope_items:` includes `Saturday_planning`, `Sunday_regular_day_planning` | both entries **deleted**; the remaining five prohibitions are untouched - they concern prompt packets, execution and calendar writes, not week span |

### 7.3 `.claude/skills/PrecapWeek/SKILL.md`

| # | Line | From | To |
|---|---|---|---|
| C1 | 36 | `included: - Monday_to_Friday_weekday_planning` | `- Monday_to_Sunday_planning` plus `- weekend_regime_application` |
| C2 | 43-44 | `excluded:` includes `Saturday_planning`, `Sunday_regular_day_planning` | both entries **deleted** |
| C3 | 105 | "limit active weekday planning to Monday through Friday (with Saturday reserved for buffer/review), include the Sunday weekly PreCap session" | "plan Monday through Sunday, applying the weekday regime Monday-Friday and the weekend regime Saturday-Sunday, and include the Sunday weekly PreCap session" |
| C4 | 129 | `monday_to_friday_scope_preserved: true` in `completion_gate` | `monday_to_sunday_scope_preserved: true` |

### 7.3b `.claude/skills/PrecapWeek/weekly-blueprint-standard.md` — not in the drafted set

| # | Line | From | To |
|---|---|---|---|
| D1 | 10 | `owns: - weekday_scope` | `- week_scope` |
| D2 | 13-15 | goal "Define the standard **Monday through Friday weekday** blueprint" | "Monday through **Sunday** blueprint ... Monday through Friday run the weekday regime; Saturday and Sunday run the weekend regime" |
| D3 | 27-45 | `weekday_scope:` block - `included_days` Mon..Fri, `excluded_days` Saturday + Sunday, `scope_rules.monday_to_friday_only: true`, `saturday_planning_excluded: true`, `sunday_regular_planning_excluded: true`, `no_weekend_recovery_or_life_planning_in_this_file: true` | `week_scope:` block - `included_days` Mon..Sun, `excluded_days: []`, explicit `weekday_regime_days` and `weekend_regime_days`, `monday_to_sunday_only: true`, the two `*_weekend_regime_applied: true` checks, `weekend_regime_content_defined_elsewhere: true` |
| D4 | 259 | `1: confirm_weekday_scope` | `1: confirm_week_scope` |

### 7.3c `.claude/skills/PrecapWeek/weekly-blueprint-meeting-example.md` — not in the drafted set

| # | Line | From | To |
|---|---|---|---|
| E1 | 12-13 | goal "adapts standard **weekday** planning" | "adapts standard **Monday through Sunday** planning" |
| E2 | 42-53 | `weekday_scope:` - `included` Mon..Fri, `excluded` Saturday + `Sunday_regular_day_planning` | `week_scope:` - `included` Mon..Sun, `excluded: []`, explicit `weekday_regime_days` and `weekend_regime_days` |

### 7.4 What the amendment deliberately does not do

- It does not define what the weekend regime *contains* - slot count, standing content, flow structure. That is DD-18 and needs the focus-day specifications (OD-27).
- It does not touch the five unrelated prohibitions in B5 and C2. Those block prompt-packet generation, project execution, status merging and calendar writes, and are independent of week span.
- It does not alter the `08:00-24:00` window or the `21:00` Daily Shutdown on any day.

### 7.5 Why the drafted inventory was incomplete

The X-03 evidence was gathered with a `Saturday|Sunday` search, which found three artifacts. That search cannot see a prohibition written without either day name, and two whole files were written that way:

- `weekly-blueprint-standard.md` held `monday_to_friday_only: true`, `saturday_planning_excluded: true` and `no_weekend_recovery_or_life_planning_in_this_file: true` under a `weekday_scope:` key.
- `weekly-blueprint-meeting-example.md` held a second `weekday_scope:` block of the same shape.
- `SKILL.md:129` held `monday_to_friday_scope_preserved: true` in its `completion_gate`.
- `validation-checklist.md:292` keyed its scope-drift trigger to `beyond_monday_to_friday`.

Had only the drafted 14 been applied, `completion_gate.monday_to_friday_scope_preserved` would have failed every Monday-Sunday brief, and the two blueprints would have reasserted the weekday-only scope the amendment removes. **The lesson for later inventories: search the rule names as well as the values.** A token sweep on `monday_to_friday`, `weekday_scope`, `saturday_excluded`, `Saturday_planning`, `Sunday_regular_day_planning` and `Sunday OFF` is what closed it; that sweep now returns clean.
