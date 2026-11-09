---
type: Reference
id: MOA-SEQ-PRECAP-INTEGRATION
title: Integrating the dispersal slice with Precap Week v2.0 and Handovers 03-06
description: What the parallel Precap Week development changed, where it collides with the dispersal work, and the rulings needed before either side can be applied.
status: working
as_of: 2026-11-09
tags: [sequencing, dispersal, precap-week, integration, stats, xp, bp, matrix-2]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Precap Week integration analysis

Companion to [ASSUMPTIONS-AND-DECISIONS-REGISTER.md](ASSUMPTIONS-AND-DECISIONS-REGISTER.md). Decision IDs continue that register's sequence from DD-19.

## 0. Connectivity and what the parallel work actually is

- **Online: yes.** `git fetch origin` returns exit 0 against `https://github.com/leela-spec/apexai-os-meta.git`.
- **Remote has nothing Precap-related pending.** Local `main` is `behind 2`: `388b69eb` (CLI harness bake-off) and `95d4c799` (its QA correction). Both concern multi-CLI harness selection, not weekly orchestration.
- **The Precap development is already local**, in commit `8ff2eb89` "upgrade Precap Week spec to v2.0 and add Handovers 03-06" (2026-11-09, pushed). The four handovers and spec v2.0 are the parallel work.
- **None of the four is applied.** All carry `status: ready_for_operator_verification`. They are proposals in the same state my §7 amendment was in before approval.
- **One of them is partly applied already, which matters.** Spec v2.0 line 20 makes `XP/TP/BP` balance and the Testing-vs-Application ratio a **`[P0]` Core Architectural Invariant**, citing `HANDOVER-05`. So HANDOVER-05's metric definitions are already load-bearing in the spec, not merely proposed.

| Handover | Subject | Collides with dispersal? |
|---|---|---|
| 03 - G-I-P-S-O task spec, variable grammar, symbol set | How a task is specified and rendered in Matrix 1 | Yes - defines what may occupy a sprint |
| 04 - Operator Decision Brief redesign | Part 1 `Standard` / `New` / `Ongoing` dropdowns | Yes - holds the day geometry and the Special Days |
| 05 - Precap stats system | Header KPI chips, XP/TP/BP, coverage triple | **Yes, directly and seriously** |
| 06 - Cross-project dependency view | Whether to keep the Mermaid DAG | No - Matrix 1 visual only |

## 1. The point constructs - RESOLVED

The collision reported in the first pass is resolved: XP is solved for rather than renamed (§1.1), and BP has one definition on branches rather than two scopes (§1.2). Both resolutions come from the operator's corrections of 2026-11-09.

| Symbol | Leela / dispersal meaning (canon) | Precap meaning (HANDOVER-05) | Compatible? |
|---|---|---|---|
| **TP** | Time Points, `1 TP = 1 minute`, counted once across serial and concurrent activity (`ST-007`, `GLOSSARY:48`) | Planned focus minutes across F1-F4, rendered `○ 38.5h / 2,310 TP` | **Yes.** Identical construct. |
| **XP** | Experience Points: nonneg. estimate of **goal-progress leverage over TP**. Leverage is the ratio `XP / TP` (`ST-008`, `GLOSSARY:47`) | "Count/share of placed minutes advancing `L1 Priority Goals`", rendered `74% on L1 Goals` | **Reconciled** - §1.1. Keep canon's quantity; the percentage becomes a derived view. |
| **BP** | Balance Points, 50/25/25 over branches `P/M/C/R` | Weekly Balance Index 0-100: `repo diversity 50 + shutdown/lunch 25 + Mon/Wed alternation 25` | **Precap reading rejected** - §1.2. One BP, on branches, with work/break and focus-day alternation. |

### 1.1 The XP resolution - solve for XP, do not rename it

My first recommendation was to rename the Precap chip. **That was the wrong fix and is withdrawn.** The operator's objection is correct and it carries the solution: *TP is a set thing, so you can solve for XP.*

Here is the mechanism. Canon gives the identity directly (`ST-008`): leverage `= XP / TP`, therefore

`XP = leverage x TP`

Every slot in the day has a **determinate TP** — 2, 3, 30 or 12 minutes, fixed by the flow structure (§2). TP is not estimated, it is read off the schedule. So assigning each binding a leverage coefficient yields XP as an actual quantity, for the craft slot exactly as for the mental slot. Nothing has to be approximated and nothing has to be renamed.

`74% on L1 Goals` then stops being a rival definition and becomes a **derived view of one XP quantity**:

`XP_concentration = XP(bindings on L1 goals) / XP(all bindings)`

One definition, two presentations. The chip can keep displaying a percentage; what changes is that the percentage is computed from XP rather than from raw minutes. The drill-down now works, because the ratio decomposes into the quantities beneath it instead of terminating in a different construct.

**And this is what makes the two layers commensurable.** Both the work week and the practice week produce XP as a quantity over known TP, so they sum into one weekly total and one concentration ratio. Under my earlier "rename the chip" proposal they would have stayed permanently separate — which would have defeated the integration the operator asked for. See DD-19, now resolved.

The practical change to HANDOVER-05 is narrow: its XP chip must be specified as `XP / TP` over a declared leverage policy, not as "count/share of placed minutes". The displayed number may well stay near 74%.

### 1.2 BP - one definition, on branches, per the operator's correction

HANDOVER-05's repo-diversity reading is **rejected**. There is one BP, measured on branches, and it applies to the whole week because the flow structure itself is a branch interleave (§2):

| Weight | Component | What it measures | Why the flow makes it measurable |
|---|---|---|---|
| **50** | **Branch diversity** | spread across `P / M / C / R` — never repository diversity | each flow cycles `[P, M, C]` and closes on `R`, so every flow contributes to all four |
| **25** | **Work / break alternation** | that craft blocks are actually followed by their breaks | the `C -> recap -> R` structure is exactly this; a flow that drops its 12-minute break fails here |
| **25** | **Focus-day alternation** | that emphasis days alternate across **whichever** days carry emphasis | generalised from HANDOVER-05's hard-coded Mon/Wed to the operator's focus days (OD-07, OD-27) |

Three things follow.

**The two-scope BP problem disappears.** There are no longer a work BP and a practice BP to reconcile; repo diversity is simply not BP, and DD-25 is withdrawn. The work layer's repository spread, if it is worth a chip at all, is a separate statistic under its own name.

**Component 2 changes character.** "Rest adherence" as a week-level abstraction becomes a concrete structural check: did each craft block get its recap and did each flow get its break. That is verifiable per flow rather than estimated per week.

**Component 3 is no longer hard-coded.** HANDOVER-05 froze Monday and Wednesday because those are this week's special-project evenings. Under the correction, BP reads whatever focus days `WeekDemand` declares — Intention Mon/Wed/Fri, Surrender Tue, Breathing Thu, ACIM Sun (OD-07) — and scores their alternation. A week that stacks every focus day consecutively fails component 3 even if all seven days are planned.

The convergence point still stands and is worth keeping: the parallel work independently arrived at a **50/25/25** split, matching the locked glossary against the Algorithm document's rival `spacing/testing/interleaving/application`. Two lines of work, same weights. That corroborates the X-01 ruling even though the component contents needed correcting.

## 2. What a Flow actually is - CORRECTED

My first reading of this section was wrong and is replaced. A Flow is **not** a container of three project sprints with practice pushed out to the anchors. A Flow **is** the practice-and-craft interleave itself.

### 2.1 The canonical definition (`qmd #1a447e:47-57`, `#46ebe0:17-27,48-49`)

`3x3` means **3 slots x 3 iterations** — the Settings grid lists `Slots: 3x3` beside `Iterations: 1-5`, and the Animation worked example states it outright: "Slots = 3, Iterations = 3". The three slots are the branch triple; the terminal `R` closes the flow.

```yaml
branch:  [P, M, C,  P, M, C,  R]
label:   ["Outside Breathing", "Anti-Stress Breathing", "Deep Work",
          "Sitting Stretches", "Process > Product", "Deep Work", "Break"]
minutes: [2, 2, 30,  2, 2, 30,  12]
lp_role: [precap, main, main,  main, main, main, recap]
cycles:  3
```

With the operator's minutes (`M` 3 rather than the corpus example's 2, plus 1 minute of recap per craft sprint):

| Iteration | `P` physical | `M` mental | `C` craft | recap | subtotal |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 30 | 1 | 36 |
| 2 | 2 | 3 | 30 | 1 | 36 |
| 3 | 2 | 3 | 30 | 1 | 36 |
| close | `R` break 12 | | | | 12 |
| | | | | **total** | **120 min** |

**120 minutes is exactly Flow 1 and Flow 3** in the live Matrix 2 (`09:00-11:00`, `13:30-15:30`). The canonical flow and the Precap calendar agree at the 2-hour case without adjustment.

### 2.2 This relocates the dispersal grid

The mental and physical slots are **inside every flow**, opening every craft sprint. They are not confined to the morning and evening anchors. Per flow: 3 `M` slots, 3 `P` slots, 3 `C` slots, 1 `R` break. Across four flows a day:

| Branch | Slots per day | Minutes each | Minutes per day |
|---|---|---|---|
| `M` Mental | **12** | 3 | 36 |
| `P` Physical | **12** | 2 | 24 |
| recap | 12 | 1 | 12 |
| `C` Craft | 12 | varies (§3) | 300 |
| `R` Break | 4 | 12 | 48 |

**That is the slot inventory.** Over a Monday-Sunday week: 84 mental slots and 84 physical slots. The anchors (`08:00-09:00` meditation, `21:30-24:00` regeneration) are additional practice surface on top of this, not the whole of it.

### 2.3 What the anchors still are

| Window | Span | Content | Owner |
|---|---|---|---|
| Morning anchor | `08:00-09:00` (60m) | "Morning Routine, **Meditation** & Setup" | **Practice** - branch `M` |
| Flow 1 | `09:00-11:00` (2h, 3 sprints) | Project work | OpenProject / G-I-P-S-O |
| Flow 2 | `11:15-12:30` (1.25h, 3 sprints) | Project work | OpenProject / G-I-P-S-O |
| Midday anchor | `12:30-13:30` (60m) | "Midday Reset, Healthy Lunch & Fresh Air Walk" | **Practice** - `R`, partly `P` |
| Flow 3 | `13:30-15:30` (2h, 3 sprints) | Project work | OpenProject / G-I-P-S-O |
| Flow 4 | `16:00-17:45` (1.75h, 3 sprints) | Project work | OpenProject / G-I-P-S-O |
| Evening | `18:45-21:00` | Special Project Day (Mon, Wed); external anchors e.g. Munich Dance Thu | **Practice** - branch `P` |
| Shutdown | `21:00-21:30` | Outro, evidence commit, workspace reset | Fixed |
| Night | `21:30-24:00` | "Evening Regeneration, Rest, Reading & Night Recovery" | **Practice** - branch `R` |

Three consequences:

1. **The craft slot is the OpenProject surface; the P/M/R slots are the practice surface.** HANDOVER-03 binds a task to a `G-I-P-S-O` spec with work-package identity (`op_id: "OP-WP#163"`). That applies to the **`C` slot only** — the 30-minute deep-work block. The `P`, `M` and `R` slots in the same flow carry practice Chunks and need no work package. One flow therefore holds both layers side by side, which is the whole point of the interleave.
2. **The branch `R` content from OD-25 has two homes.** The 12-minute in-flow break (the corpus example annotates it "Light snack & audiobook" — `#1a447e:57`) takes short `R` content; `21:30-24:00` "Regeneration, Rest, Reading" takes long-form Yoga Nidra. Audiobooks fit either.
3. **The physical Epics are already in Precap Week.** HANDOVER-04 sets the Wednesday Special Project Day to "Dance & Martial Arts" — two of the three physical Epics by name. The dispersal layer does not introduce them; it schedules within a theme Precap Week already declares.

## 3. The arithmetic reconciles - the craft block flexes, the practice slots do not

The apparent conflict in my first reading dissolves once the flow is modelled correctly. Each flow carries a **fixed practice overhead** of `3 x (2 + 3 + 1) = 18 min` plus a `12 min` break = 30 minutes. Whatever remains is craft:

| Flow | Span | Duration | Practice + break | Craft total | Craft per block |
|---|---|---|---|---|---|
| Flow 1 | `09:00-11:00` | 120 | 30 | 90 | **30** |
| Flow 2 | `11:15-12:30` | 75 | 30 | 45 | **15** |
| Flow 3 | `13:30-15:30` | 120 | 30 | 90 | **30** |
| Flow 4 | `16:00-17:45` | 105 | 30 | 75 | **25** |
| | | **420** | **120** | **300** | |

420 minutes of flow time = 300 craft + 72 practice + 48 break, exactly. **The live Precap flow boundaries and the canonical 3x3 flow are consistent with no adjustment to either.**

OD-23's 30 minutes is therefore the **standard craft block**, which Flows 1 and 3 realise exactly. It was never the whole sprint — the sprint is 36 minutes (`2 + 3 + 30 + 1`). This also retires the last of the `33er` / `30er` question: `30er` is the craft block; the `3`s are the mental and physical micro-blocks ahead of it.

**The consequence that matters for dispersal:** the practice slot count is **invariant at 12 `M` + 12 `P` per day** regardless of how long each flow is, because only the craft block absorbs the difference. The quota denominator is stable, which is what makes a quota workable at all.

*Grounding note:* the per-flow craft figures of 15 and 25 minutes are derived arithmetic, not quoted from an artifact. What is quoted is the 18-minute practice overhead, the 12-minute break and the 30-minute standard craft block. The derivation assumes the practice overhead is constant across flows — see DD-20.

## 4. My Monday-Sunday amendment left stale text in the handovers

The amendment (register §7) did not reach the handover documents, because they were not in scope and are unapplied. Two carry the removed prohibition forward and would reintroduce it on ratification:

| Site | Text | Needed |
|---|---|---|
| `HANDOVER-04:66` | Daily Time Geometry: `08:00–24:00 Window · 21:00 Shutdown · Sun OFF` | drop `Sun OFF`, add the weekend regime |
| `HANDOVER-05:53` | header chip sub-line `Across 24 Flows · 6d (Mon-Sat)`, twice in the same row (`Mon-Sat Focus Allocation`) | `7d (Mon-Sun)`; flow count follows the weekend slot ruling (DD-18) |
| `HANDOVER-05:60` | "At Saturday `StatusMerge`" | Saturday is now a planned day under the weekend regime; confirm StatusMerge stays Saturday or moves to Sunday |

## 5. Decisions

### 5.1 Closed by the operator's corrections of 2026-11-09

| # | Decision | Ruling |
|---|---|---|
| **DD-19** | What the Precap "XP" chip is | **Solve for XP, do not rename it.** TP is determinate per slot, so `XP = leverage x TP` yields a real quantity everywhere, and `74% on L1` becomes `XP_concentration`, a derived view of it. One definition, two presentations; the two layers become summable. My rename proposal is withdrawn (§1.1). |
| **DD-20** | Sprint duration against the flow boundaries | **No conflict exists.** A sprint is 36 min (`P 2 + M 3 + C 30 + recap 1`); 30 min is the standard **craft block**. Practice overhead is fixed at 18 min/flow plus a 12 min break, and the craft block absorbs each flow's remaining time (30/15/30/25). 420 min of flow time reconciles exactly (§3). |
| **DD-21** | Whether practice binds inside the flows | **Yes - that is what a Flow is.** The `3x3` is 3 slots x 3 iterations of `[P, M, C]` closing on `R`. Practice is not confined to the anchors; it opens every craft sprint. My anchors-only recommendation is withdrawn (§2). |
| **DD-25** | Which BP the header chip shows | **Withdrawn - there is only one BP.** Measured on branch diversity 50, work/break alternation 25, focus-day alternation 25. Repo diversity is not BP (§1.2). |
| **DD-27** | Mental quota rounding | **Largest remainder at the week**, day counts float. At the 72-slot denominator (OD-33): Intention 29, ACIM 15, Surrender 14, Breathing 14. Per-day rounding would force 4.8 into an integer seven times over; a carried fraction needs the cross-week state DD-09 ruled out. Applied in the built inventory. |
| **DD-29** | Which branch owns the 1-minute craft recap | **Craft** (OD-36). It is the closing minute of the craft block, carrying `lp_role: recap`, not a slot of its own. The mental denominator therefore stays 72 rather than doubling to 144. |
| **DD-30** | Weekend flow shape | **The same 120-minute standard** (OD-37). Two flows per weekend day. Clock times still unset, so each is marked `span_status: assumed_pending_DD-30` in the inventory; the slot counts do not depend on them. |
| **DD-31** | Week table to physical Epics | **Five Epics** (OD-35): Strikes and Kicks to **Martial Arts**; Dance and Moves to **Dance**; **S/BJJ** its own; Running and Stretch to **General**; **Knee** separate; **EFX dropped**. Knee has no week-table entry, so it needs its own days or it draws nothing. |

### 5.2 Still open

| # | Decision | Options | Recommendation |
|---|---|---|---|
| **DD-22** | What the OD-10 three-bullet per-day band actually is | (a) **a read-only display of what the flows and anchors already hold** / (b) its own allocation surface the operator edits directly | **(a).** Two editable surfaces for one assignment diverge with no merge rule — the same failure as the bidirectional sync rejected in DD-15. The band shows the top three bindings per branch per day; it does not author them. |
| **DD-23** | The "Leela Path & Sequencing paused" status in spec `:22`, `:110` and HANDOVER-05 DoD 2 | (a) **qualify: the Leela *feature* is paused, the personal dispersal slice is active** / (b) mark Sequencing unpaused / (c) leave as is | **(a).** Both are true, and the distinction is exactly the reduced-slice framing of register §1. Leaving it makes the stats layer report `Paused (no denominator)` for a layer now producing output. |
| **DD-24** | Whether to fix the stale weekend text in Handovers 04 and 05 now (§4) | (a) **now** / (b) when those handovers are ratified | **(a).** They carry the same prohibition class just removed from five files. Ratifying them later would silently reintroduce `Sun OFF`. |
| **DD-26** | HANDOVER-06's dependency-view choice | Option A drop / Option B inline cross-repo pills / Option C collapsible strip | **No recommendation — not a sequencing matter and its own DoD is unmet.** Option B is the online recommendation, but DoD 1 requires a live count of cross-project `blocks`/`precedes` edges in OpenProject, which has not been run. If that count is zero, Option A is free. |
| **DD-32** | The weekday re-cut that four 120-minute flows require (new, from OD-34) | the live calendar runs F2 at 75 min and F4 at 105 min, which OD-34 forbids. (a) **re-cut to `09:00-11:00 / 11:15-13:15 / 14:15-16:15 / 16:30-18:30`, moving the midday anchor to 13:15-14:15** / (b) keep three flows a day / (c) shorten the anchors instead | **(a), drawn in the blueprint page §2 for confirmation.** It is the only arrangement that fits four 120-minute flows plus both 60-minute anchors inside `08:00-18:30`, and it moves one anchor rather than cutting any. Marked `span_status` per flow in the inventory. |
| **DD-28** | Whether HANDOVER-05's XP chip is amended now or on ratification (new, follows DD-19) | (a) amend now, since spec v2.0 `:20` already made `XP/TP/BP` a `[P0]` invariant citing it / (b) amend when the handover is ratified | **(a).** The wrong definition is already load-bearing in a `[P0]` invariant, not merely proposed. |

## 6. Ambiguities

**A-08 is closed** by the corrected flow model. The mental quota's denominator is the **12 in-flow `M` slots per day**, not the morning anchor. The `08:00-09:00` "Morning Routine, Meditation & Setup" hour is additional practice surface sitting outside the quota; whether it is also quota-bearing is DD-22's display question, not a quota question. The slot inventory is no longer blocked.

Four remain:

- **A-09 Wednesday Special Project Day.** "Dance & Martial Arts" names two physical Epics. Unclear whether that evening *is* the week's binding for those Epics, or separate project work that happens to share the names. Matters because the 12 in-flow `P` slots already cover physical practice — if Wednesday evening is additional, Dancing and Martial Arts are over-served relative to Knee.
- **A-10 The night window versus the in-flow break.** Branch `R` now has two surfaces: the 12-minute in-flow break (annotated "Light snack & audiobook" in the corpus) and `21:30-24:00` "Regeneration, Rest, Reading". Unclear whether the night window is plannable content the algorithm binds, or deliberately unplanned rest that BP measures but never schedules. The work/break alternation component reads differently under each.
- ~~**A-11 Weekend flow count.**~~ **CLOSED by OD-33: two flows each.** The week is 72 mental and 72 physical slots. Quota allocated in register §3.1; the slot inventory is built.
- **A-12 StatusMerge day.** HANDOVER-05 places `StatusMerge` on Saturday, which was the last planned day. Saturday is now mid-weekend; the natural boundary may be Sunday.

## 7. Open and not verified

- All four handovers remain `ready_for_operator_verification`. **Nothing in this document has been applied to any artifact.**
- The two remote commits were fetched and read by subject line only; neither touches weekly orchestration.
- HANDOVER-05 DoD 3 (`Target vs Placed` exposing unplaced L1 goals) depends on OpenProject data that was not queried in this session.
- HANDOVER-06 DoD 1 (live cross-project edge count) has not been run; DD-26 waits on it.
- Spec v2.0 carries `status: operator_review_pending` in its own frontmatter and now also contains the applied Monday-Sunday amendment. Whether that mixed state is acceptable, or the spec should be versioned to v2.1 on amendment, is unasked and unanswered.
- The practice-side BP floor values (DD-16) remain undetermined and now also depend on A-11.
