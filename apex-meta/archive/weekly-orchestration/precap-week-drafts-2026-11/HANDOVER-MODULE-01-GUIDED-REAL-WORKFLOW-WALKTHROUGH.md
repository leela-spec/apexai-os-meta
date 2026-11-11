# Module 01 Handover — Guided Real-Workflow Walkthrough and Co-Build

## Mission

Continue Module 01 (`Weekly_Command_Brief`) with the operator in a new chat by **walking through the real weekly workflow from the beginning**, step by step, using current repository evidence and realistic W34 data.

The operator does **not** want another abstract architecture review or a large batch of design questions. The operator needs to understand the system by experiencing what it would actually do on a Sunday PrecapWeek run, seeing the inputs, transformations, weekly artifact, boundary into PrecapNextDay, and calendar implications in concrete snapshots.

The purpose of the walkthrough is to let the operator co-design the correct production behavior from inside the real workflow.

Do **not** begin by editing production files.

Do **not** begin by asking the operator to choose between terms such as `planning_feed`, `ProjectStatus`, `daily_seed_map`, `flow grid`, `calendar_block_proposal`, or `PrecapNextDay` without first demonstrating what those concepts mean in practice.

The expected end state is:

1. the operator understands each major stage of the weekly planning flow;
2. the operator has made the remaining design decisions from concrete examples;
3. contradictions in the current production files are resolved conceptually;
4. only then, an exact **patch-only** implementation packet is produced for the existing files;
5. the repaired workflow is tested with realistic weekly scenarios.

---

# 1. Current situation

Module 01 has a valid core concept but is **not yet internally coherent**.

The useful design work should be preserved. The current commit must not be wholesale-reverted merely because some semantics drifted.

## 1.1 Validated core architecture

The following boundary is already authoritative and should not be reopened unless the operator explicitly changes it:

```text
Sunday / PrecapWeek
        |
        v
Weekly Command Brief
        |
        | embedded compact handoff
        v
PrecapNextDay
        |
        v
Flow-level / sprint-level daily execution planning
```

`PrecapWeek` owns the **Monday-Friday weekly architecture**.

It may determine:

- weekly strategic targets;
- intended outcomes/work by weekday;
- cross-day sequencing;
- deadline/dependency-aware placement;
- meeting/capacity-aware allocation;
- project/flow allocation by weekday;
- full / compressed / minimal / omitted weekly direction;
- deliberate deferrals;
- rationale for non-obvious placement.

`PrecapNextDay` owns operationalization:

- revalidate tomorrow's real conditions;
- select actual executable flows;
- define sprint-level structure;
- create execution cards/prompts;
- determine exact intra-day sequence;
- handle applicable calendar-write requests.

The Weekly Command Brief is authoritative weekly direction, not a frozen executable daily schedule.

Canonical design authority:

`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/DESIGN-DECISIONS.md`

---

## 1.2 Useful new visual concept

A Dual-Matrix Weekly Architecture was selected:

```text
Matrix 1 — Project Strategy
What should each project achieve this week?

            ↓ traceability

Matrix 2 — Week Allocation
Where should those movements happen Monday-Friday?
```

This basic two-layer idea should be treated as **provisionally retained**.

### Matrix 1 intended role

Human question:

> What meaningful progress should each active project achieve this week, and what will that unlock or produce?

Useful grain:

```text
Project
→ weekly strategic target
→ small number of traceable sub-targets
→ expected deliverable / leverage
```

Example shape:

```text
MasterOfArts
Weekly target: establish website-definition baseline
[M-T1] source + purpose baseline
[M-T2] information architecture
Expected output: reviewable website definition baseline
```

The exact data must be derived from live W34/current sources; do not fabricate project truth merely to fill the example.

### Matrix 2 intended role

Human question:

> Where is the week's intended work allocated across Monday-Friday, given real capacity, meetings, dependencies and deferrals?

The current production template uses:

```text
weekday columns
×
F1-F4 flow rows
```

This representation may be retained if it remains **weekly allocation**, not detailed daily execution.

---

## 1.3 Current contradictions that the walkthrough must resolve

### Contradiction A — sprint-depth leakage

The live production template currently places `S1`, `S2`, `S3` goals inside every F1-F4 weekday cell.

Potential normal week expansion:

```text
4 flows × 5 weekdays × 3 sprint goals = up to 60 sprint goals
```

But the locked design explicitly says sprint-level execution belongs to `PrecapNextDay`.

The operator must understand this by seeing one **realistic weekly cell** transformed into its possible next-day version before making a decision.

Do not ask merely:

> Should S1-S3 be removed?

Instead demonstrate:

```text
WEEKLY VERSION
Mon / F1
MasterOfArts · [M-T1]
Website-definition baseline

NEXT-DAY VERSION
Mon / F1
MasterOfArts · [M-T1]
S1 locate/audit source
S2 reconcile purpose/audience
S3 produce baseline artifact
Exact sequence / prompt / execution card
```

Then explain the cost/benefit of deciding the S1-S3 split on Sunday versus Monday.

---

### Contradiction B — metric policy

Earlier validated policy:

```text
Task or outcome (I94/R25/E9)
```

- `I` = Impact
- `R` = Risk
- `E` = Evidence strength
- scale 1-100
- inline only
- no required separate metric columns
- no synthetic master score
- do not let metrics override deadlines/dependencies/operator intent/capacity

Later visualization material introduced:

```text
(I#/E#/R#: Score)
```

plus a composite formula.

These policies conflict.

The walkthrough must show one concrete allocation where a synthetic score could produce a misleading result.

Example logic:

```text
Task A: very high impact, but blocked until Wednesday
Task B: lower impact, hard Monday deadline
```

Show why a composite score cannot replace temporal/dependency reasoning.

Then ask the operator whether to preserve the original I/R/E evidence notation, suppress metrics from the matrices, or use another explicit model.

Do not present the later composite score as already authoritative.

---

### Contradiction C — deleted Daily Seed Map still required elsewhere

The current production template removed the old `## Daily seed map` section.

However:

- `.claude/skills/PrecapWeek/SKILL.md` still instructs PrecapWeek to produce a directional daily seed map;
- `.claude/skills/PrecapWeek/references/validation-checklist.md` still requires `daily_seed_map`.

The walkthrough should make this understandable as a simple representation problem:

```text
OLD
Daily seed map
Mon: likely MoA + Leela
Tue: likely Apex...

NEW
Matrix 2 already contains the Monday-Friday allocation
```

Decision question after demonstration:

> Does Matrix 2 fully replace the old daily seed map, or is there unique information in the seed map that still needs a compact home?

Likely answer: Matrix 2 replaces it, but verify through the walkthrough rather than treating this as blindly accepted.

---

### Contradiction D — calendar authority

Live `PrecapWeek` contract:

```text
read calendar constraints: yes
create calendar events: no
calendar block proposals only
```

Locked design:

```text
PrecapWeek: week-level allocation
PrecapNextDay: next-day operationalization + relevant calendar writes
```

A later handover proposes automated Google Calendar creation for F1-F4 from both weekly and daily planning.

This may be useful future work, but it is not yet reconciled with the production boundary.

The walkthrough must demonstrate the difference:

```text
SUNDAY
Wed has ~2h usable capacity because meetings dominate the day.
Weekly decision: only one meaningful movement should be planned.

WEDNESDAY PRECAP
Actual calendar changed.
11:00 meeting cancelled.
Now 3.5h are available.
Daily system decides exact F1/F2 blocks and optionally writes them.
```

Then ask where calendar-writing authority should live.

Do not implement the Google Calendar writer during this walkthrough.

---

### Contradiction E — downstream handoff is too small relative to the locked design

Locked design expects the embedded handoff to preserve access to:

- week / weekly intent;
- result/review state;
- reference to the week-architecture section;
- next target day;
- intended role/outcomes for that day;
- capacity assumption;
- fixed constraints;
- carry-forward dependencies/review items;
- next consumer.

The current template handoff does not clearly carry all of these.

The walkthrough must show:

1. the Weekly Command Brief;
2. the proposed tiny handoff;
3. what `PrecapNextDay` would know immediately;
4. what it would have to reopen from the Brief;
5. which fields are genuinely routing/orientation fields versus duplicate payload.

Goal: **reference plus minimal next-day orientation**, not a second weekly schema.

---

### Contradiction F — accepted cleanup not yet complete

The current template still contains the stale historical `source_gap` about an old weekly-plan output contract.

Accepted Module 01 repair policy already says:

- remove this stale `source_gap`;
- do not resurrect the old contract.

Treat this as a mechanical repair, not a new design debate.

---

# 2. Separate workstream: input-pipeline efficiency

There is also an active PrecapWeek input-pipeline audit.

Do **not** mix the input simplification changes into the first visualization-alignment patch.

The correct order is:

```text
A. understand + repair Weekly Command Brief contract
B. verify output / PrecapNextDay boundary
C. then simplify PrecapWeek's input pipeline
```

Input-pipeline handover:

`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/PRECAP-WEEK-INPUT-PIPELINE-DECISION-HANDOVER.md`

High-confidence hypotheses awaiting operator-understandable validation include:

- `planning_feed` + `next-session.md` duplication;
- ProjectStatus being too large/redundant as a default AI input;
- loading too much Sync data;
- direct recap evidence being double-processed;
- calendar normalization being more detailed than weekly planning requires;
- blueprint containing stale project-priority assumptions;
- validation checklist duplicating owning contracts;
- selective retrieval being preferable to another persisted input packet.

The new chat should eventually walk through these too, but **only after the output architecture is coherent**, unless the operator explicitly prefers to switch order.

---

# 3. Core interaction rule for the new chat

The walkthrough should behave like a guided system simulation.

For each stage:

```text
1. SHOW what the real system receives
2. EXPLAIN what decision the system is trying to make
3. SHOW the intermediate/resulting artifact
4. SHOW what information is intentionally NOT decided yet
5. SHOW the downstream consumer
6. SHOW cost / duplication / ambiguity where relevant
7. ASK one bounded operator question
8. RECORD the decision
9. ADVANCE to the next stage
```

Do not ask five unrelated questions at once.

Do not use internal architecture jargon as the primary explanation.

Do not make the operator infer behavior from schemas.

If the operator says something such as:

> I need to see what that would actually look like

respond with another concrete workflow snapshot before asking again.

---

# 4. Required walkthrough — start from the real beginning

## Stage 0 — Orient the operator

### Goal

Explain the whole weekly loop in under ~15 lines before entering details.

Use a simple diagram:

```text
CURRENT PROJECT TRUTH + RECENT EXECUTION
                |
                v
       SUNDAY PRECAPWEEK
                |
   +------------+------------+
   |                         |
weekly strategy          week allocation
(Matrix 1)               (Matrix 2)
   |                         |
   +------------+------------+
                |
                v
      WEEKLY COMMAND BRIEF
                |
       one operator approval
                |
                v
        PRECAPNEXTDAY
                |
        exact daily flows
                |
      prompts / execution
```

Then tell the operator:

> We will now run through this as though we were planning an actual week. Nothing is being changed yet. At each step you will see what the AI sees, what it decides, and where it stops.

Do not ask a decision yet.

---

## Stage 1 — What does Sunday PrecapWeek actually know?

### Goal

Make the input bundle understandable.

Read current live sources, especially:

- `.claude/skills/PrecapWeek/SKILL.md`
- latest confirmed Apex Session planning feed
- relevant Sync next/blocker reports
- current weekly operator intent / W34 portfolio context
- calendar constraints when available
- blueprint references

Use real current repository files. Do not reconstruct from memory if a source exists.

### Show two snapshots

#### Snapshot A — current broad model

Example structure only:

```text
Sunday AI may be pointed at:
- Session planning_feed
- Session next-session context
- Sync next candidates
- Sync blockers
- perhaps ProjectStatus portfolio overview
- recent recaps/skip markers
- operator weekly intent
- calendar constraints
- weekly blueprint
```

For each, explain in plain language:

```text
What is it?
Who produced it?
Is it confirmed truth, projection, or raw evidence?
What weekly decision can it change?
How large/duplicative is it?
```

#### Snapshot B — tentative lean model

Do not call this approved.

```text
Sunday AI sees by default:
- confirmed planning feed
- operator weekly intent
- actionable next candidates
- relevant blockers/dependencies only when needed
- weekly calendar constraints
- compact weekly planning grammar

Everything deeper remains available by reference.
```

### Operator question

Do **not** ask the full input-pipeline architecture here.

Ask only:

> Does this distinction make sense: the Sunday AI should begin from a small authoritative working set, but still be able to open deeper evidence when a weekly choice requires it?

If the answer is uncertain, show one concrete ProjectStatus-vs-planning-feed example before continuing.

This stage is orientation only; final input-pipeline decisions can be deferred until later.

---

## Stage 2 — Capture weekly intent like a real Sunday conversation

### Goal

Demonstrate the adaptive-hybrid interaction model.

Use the actual active project state and current operator context.

Show what can already be inferred from evidence versus what is operator-owned.

Example form:

```text
ALREADY KNOWN
- these projects are active
- these tasks are dependency-ready
- these blockers are confirmed
- Wednesday has a fixed capacity constraint

NOT SAFE TO INFER
- which strategic outcome matters most this week
- whether a personal/social allocation is intentionally protected
- whether one active project should deliberately receive no work
```

Then simulate the shortest useful Sunday questions.

Good:

```text
1. What would make this week feel meaningfully successful?
2. Any project that must move or must not consume capacity?
3. Any fixed commitment/capacity fact not visible in the calendar/state?
```

Bad:

```text
Fill these 17 fields:
weekly_intent:
minimum_success:
priority_override:
dating_allocation:
...
```

### Operator interaction

Actually let the operator answer the simulated weekly-intent questions if they want to.

If they prefer not to use current real-life intent for the design exercise, use a clearly labelled W34 fixture derived from repository evidence.

Do not silently turn design simulation answers into canonical project state.

---

## Stage 3 — Build Matrix 1 live

### Goal

Show how raw project truth becomes weekly strategy.

Use 3-5 representative active projects first rather than immediately rendering a huge portfolio.

For each project show:

```text
SOURCE STATE
What exists / what is actionable / blockers

WEEKLY INTERPRETATION
What meaningful result could happen this week?

MATRIX 1 ROW
Project | Weekly Target | Sub-targets | Deliverable / leverage
```

### Required questions during construction

Walk through at least these examples:

1. an obvious actionable project;
2. a project with a dependency/blocker;
3. a project intentionally deferred or capacity-only;
4. if available, a project where operator intent beats deterministic rank.

### Metric demonstration

Show inline I/R/E only where it clarifies a real judgment.

Example:

```text
Reconcile Home runtime against current contract (I92/R38/E88)
```

Then show why this does **not** mathematically determine weekday placement.

### Operator question

Ask whether Matrix 1 contains the right strategic grain:

> Is this enough to understand what each project should achieve and why, without turning the weekly brief into the execution plan?

If not, let the operator add/remove fields by looking at the actual rows.

Do not debate abstract field names before showing the rows.

---

## Stage 4 — Build Matrix 2 live from the same project movements

### Goal

Make the weekly allocation visible.

Start with a single Monday-Tuesday fragment before showing all five weekdays.

For example:

```text
| Flow | MON — 6h usable | TUE — 4h usable |
|------|-----------------|-----------------|
| F1   | MoA · [M-T1] Website baseline | Leela · [L-T1] Home verification |
| F2   | Leela · [L-T1] Home verification | Apex · [A-T1] KB baseline |
| F3   | Apex · [A-T1] KB baseline | MoA · [M-T2] IA |
| F4   | Investment input / optional | Deferred — meeting load |
```

Use live/current semantics rather than inventing arbitrary project facts.

### Explain each encoding

```text
Day header
→ how much usable capacity / fixed load matters

Flow row
→ weekly allocation bucket, if retained

Project + sub-target tag
→ traceability back to Matrix 1

Short outcome phrase
→ what movement should happen

Deferred / omitted
→ explicit capacity decision
```

### Crucial boundary demonstration

Take one cell and show two versions.

#### Version A — weekly allocation

```text
MON / F1
MoA · [M-T1]
Website-definition baseline
```

#### Version B — Sunday pre-building Monday execution

```text
MON / F1
MoA · [M-T1]
S1 locate source
S2 reconcile audience
S3 synthesize IA baseline
90 min
09:00 → 10:30
prompt: ...
```

Explain:

```text
A answers: what should Monday advance?
B answers: exactly how Monday will execute it.
```

Then ask:

> How much of Version B do you actually want decided on Sunday, given that PrecapNextDay re-checks Monday's real conditions?

This is the correct place to resolve the S1/S2/S3 question.

Do not pre-decide the answer for the operator, but recommend preserving a meaningful weekly/day boundary unless they explicitly want Sunday to prebuild daily execution.

---

## Stage 5 — Simulate PrecapNextDay using Monday from Matrix 2

### Goal

Make the downstream boundary tangible.

Take the Monday allocation just created and pretend it is now Sunday evening / Monday planning time.

Show what PrecapNextDay receives:

```text
FROM WEEKLY BRIEF
- week intent
- Monday role/outcomes
- intended projects/sub-targets
- capacity assumption
- fixed constraints
- carry-forward dependencies/review items
```

Then introduce one change in reality:

```text
Example:
A Monday meeting was added.
Usable focus capacity falls from ~6h to ~4h.
```

Show what PrecapNextDay is allowed to change:

```text
- reduce F3
- defer F4
- compress one movement
- decide exact sprint structure
- establish actual execution sequence
```

Show what it should preserve unless new evidence justifies changing it:

```text
- weekly strategic target
- major project intent
- dependencies
- explicit operator priority
```

### Operator question

Ask:

> Does this feel like the correct division of responsibility, or do you want Sunday planning to lock more/less of Monday before PrecapNextDay runs?

Use the actual before/after example to refine the boundary.

---

## Stage 6 — Calendar integration demonstration

### Goal

Separate three distinct things that are currently easy to conflate:

```text
1. reading fixed calendar constraints
2. planning work around them
3. writing new APEX focus events
```

Show one concrete day.

Example structure:

```text
REAL CALENDAR
10:00–12:00 fixed meeting
14:00–15:30 fixed meeting

WEEKLY INTERPRETATION
Wednesday = compressed
~1 meaningful project movement

DAILY OPERATIONALIZATION
09:00–10:00 focused work
12:30–13:30 focused work
(or whatever current conditions support)

OPTIONAL CALENDAR WRITE
Create APEX focus event only after daily plan is finalized
```

Do not hard-code anchor times unless sourced from authoritative operator settings/current calendar rules.

### Operator question

Ask:

> Should PrecapWeek only express weekly capacity/allocation, while PrecapNextDay owns exact discretionary focus blocks and calendar writes?

If the operator wants Sunday calendar-writing, demonstrate the stale-plan failure case first:

```text
Sunday writes Wednesday 09:00–10:30.
Tuesday a new external meeting appears.
Now both the weekly plan and calendar event are stale.
```

Only then record the preference.

---

## Stage 7 — Show the complete Weekly Command Brief as the operator would see it

### Goal

After resolving the preceding boundaries, render one realistic full Brief.

Required order:

```text
1. compact control header
2. weekly direction / success
3. Matrix 1 — project strategy
4. Matrix 2 — weekly allocation
5. project detail sections only where they add information beyond Matrix 1
6. cross-project sequence / deferrals
7. review flags only when material
8. compact provenance
9. compact downstream handoff
```

### Anti-duplication test

For every section ask:

> Is this adding information or simply restating something already visible above?

Examples:

- Matrix 1 weekly target should not be reworded three times downstream.
- Project detail should expand success evidence/dependency/output, not repeat the Matrix 1 sentence.
- Matrix 2 should show placement, not repeat full project descriptions.
- handoff should reference the matrices, not copy them into YAML.

### First-10-second test

Ask the operator to answer from the rendered Brief:

```text
What is the week's overall direction?
What are the 2-4 most important project movements?
What does Monday look like?
Where is the week constrained?
What was intentionally deferred?
What, if anything, needs my decision?
```

If those are not obvious, iterate the artifact before discussing implementation.

---

## Stage 8 — Build the embedded PrecapNextDay handoff

### Goal

Demonstrate minimal routing versus duplication.

Show a candidate like:

```yaml
presentation_handoff:
  artifact_type: Weekly_Command_Brief
  artifact_ref: <path>
  week: 2026-WXX
  result_state: approved
  weekly_intent: <short intent>
  week_architecture_ref: "#weekly-architecture"

  next_target_day: Monday
  intended_day_role: <role>
  intended_outcomes:
    - <short refs / tags>
  capacity_assumption: <compact>
  fixed_constraints:
    - <material constraint>
  carry_forward:
    - <dependency/review item if any>

  next_consumer: PrecapNextDay
```

Then compare with two bad extremes.

### Too small

```yaml
artifact_ref: brief.md
next_consumer: PrecapNextDay
```

Problem: does not orient the downstream planning run.

### Too large

Full Matrix 1 + Matrix 2 copied into YAML.

Problem: duplicate representation, drift risk, context cost.

### Operator question

Ask whether the compact middle version contains enough orientation.

Adjust based on the actual PrecapNextDay consumption test.

---

## Stage 9 — Reveal current production-file contradictions

Only after the operator understands the desired workflow, show the actual files and mismatches.

Use a table:

| File | Current behavior | Desired behavior from walkthrough | Required action |
|---|---|---|---|
| `DESIGN-DECISIONS.md` | both unresolved and resolved visualization claims; conflicting metric specs | one coherent locked policy | patch |
| `weekly-command-brief-template.md` | Dual Matrix + S1-S3; stale source_gap | operator-approved matrix grain | patch |
| `PrecapWeek/SKILL.md` | still requests daily seed map | matrix-based week architecture | patch |
| `validation-checklist.md` | still requires daily_seed_map | validates current Brief structure | patch |
| visualization handover | may contain composite-score / calendar-write assumptions | align with operator decisions | patch |
| calendar handover | currently framed as active implementation handover | mark future/downstream authority if appropriate | patch or park |

Do not modify them yet.

Explain that these are **integration inconsistencies**, not evidence that the whole architecture must be redesigned.

---

# 5. Decision recording format

At the end of each stage, record only decisions actually made.

Use:

```okf
walkthrough_decision:
  id: W01
  topic: <short topic>
  evidence_seen:
    - <concrete snapshot/example>
  operator_decision: <decision>
  implication:
    - <what changes>
  files_likely_affected:
    - <paths>
  implementation_status: pending_patch
```

Do not silently promote a recommendation into an operator decision.

Maintain a running compact decision ledger visible in the chat after every 2-3 decisions.

---

# 6. Decision topics that must eventually close

The walkthrough should naturally resolve these; do not dump them all upfront.

## Output / weekly-vs-daily

```text
W01 — Matrix 1 strategic grain
W02 — Matrix 2 representation and F1-F4 semantics
W03 — S1/S2/S3 Sunday-vs-next-day ownership
W04 — full/compressed/minimal/omitted representation
W05 — day header capacity/meeting information
W06 — old Daily Seed Map replacement
```

## Metrics

```text
W07 — whether I/R/E is displayed, internal, or selective
W08 — preserve I/R/E order and no-composite policy vs explicitly change it
```

## Calendar

```text
W09 — weekly calendar constraint representation
W10 — exact discretionary block ownership
W11 — Google Calendar write ownership/timing
```

## Brief anatomy

```text
W12 — Matrix 1 vs project-detail duplication boundary
W13 — review flag visibility
W14 — provenance grain
W15 — downstream handoff fields
```

## Input pipeline — after output alignment

```text
I01 — planning_feed vs next-session default
I02 — ProjectStatus default vs fallback/on-demand
I03 — Sync report loading strategy
I04 — recap evidence default vs on-demand
I05 — calendar input shape
I06 — blueprint scope
I07 — validation deduplication
I08 — ephemeral working set vs another packet
```

---

# 7. Source-reading discipline

The new chat must manage context deliberately.

## Read first

Read only:

1. this handover;
2. `DESIGN-DECISIONS.md`;
3. live `.claude/skills/PrecapWeek/SKILL.md`;
4. live `weekly-command-brief-template.md`.

This is enough to orient the first stages.

## Read when entering input walkthrough

Then read:

- latest Session planning feed;
- relevant W34/current Sync next-action report;
- blocker report only as needed;
- current operator/W34 weekly artifact if needed;
- `PRECAP-WEEK-INPUT-PIPELINE-DECISION-HANDOVER.md`.

Do not load the full ProjectStatus/score/blocker universe by default merely because it exists.

## Read when entering calendar stage

Only then read:

- `calendar-planning-guidance.md`;
- `weekly-blueprint-standard.md`;
- meeting-heavy blueprint reference;
- current calendar constraints if available.

## Read when entering validation/implementation stage

Only then read:

- `references/validation-checklist.md`;
- Module 01 HANDOVER/README files;
- visualization/calendar handovers that require alignment.

Core context rule:

> Read the smallest source set that can answer the current stage. Dereference deeper evidence when a concrete decision requires it.

---

# 8. Patch-only implementation rule

This project now has a critical mutation policy:

> Existing production files must only be changed through surgical patches/diffs against known current content. Do not reconstruct or replace an entire existing file for a localized change.

Therefore, after the walkthrough closes the design:

## Allowed direct writes

- genuinely new files;
- new research/decision handovers;
- new patch files.

## Existing files

Generate exact unified diffs only.

Likely patch targets:

```text
.claude/skills/PrecapWeek/SKILL.md
.claude/skills/PrecapWeek/weekly-command-brief-template.md
.claude/skills/PrecapWeek/references/validation-checklist.md
apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/DESIGN-DECISIONS.md
apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-MODULE-01-WEEKLY-VISUALIZATION.md
apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md
```

Do not assume every listed file needs modification. Patch only the files whose current text conflicts with the operator-approved walkthrough result.

## Application workflow

The implementation packet should instruct the local/CLI AI to use:

```powershell
git apply --check <patch>
git apply <patch>
git diff --check
git diff -- <target files>
```

Then:

- verify only expected hunks changed;
- verify unrelated content stayed untouched;
- run targeted tests/validation;
- commit and push only after the diff is correct.

If `git apply --check` fails, stop and regenerate the patch against current `main`. Do not manually reconstruct fuzzy hunks.

---

# 9. Required implementation sequence after walkthrough approval

## Phase A — freeze the repaired design

Create a compact decision record from W01-W15.

Verify there are no internal contradictions such as:

```text
"sprint planning belongs downstream"
AND
"PrecapWeek must output 60 sprint goals"
```

or:

```text
"no composite score"
AND
"calculate composite score"
```

---

## Phase B — generate one visualization-alignment patch set

Patch only the existing files required to make:

```text
DESIGN-DECISIONS
SKILL
TEMPLATE
VALIDATOR
HANDOVERS
```

agree on the same workflow.

Do **not** include the broader input-pipeline simplification unless a tiny change is mechanically required for consistency.

---

## Phase C — regression tests

Run three weekly scenarios.

### Test 1 — Normal week

Should demonstrate:

- several active projects;
- understandable Matrix 1;
- balanced Matrix 2;
- clear Monday direction;
- no sprint-level overproduction if that boundary was retained.

### Test 2 — Meeting-heavy week

Should demonstrate:

```text
normal day → full
constrained day → compressed
heavily constrained day → minimal / omitted
```

The artifact must explain deferral without creating a micro-calendar.

### Test 3 — dependency/deadline week

Create or use a fixture where:

```text
high-impact work is blocked
lower-impact work has a hard near deadline
```

The resulting week must show that I/R/E metrics do not override temporal/dependency reality.

---

## Phase D — downstream consumption test

Give a fresh `PrecapNextDay` context only:

- the generated Weekly Command Brief;
- next-day live calendar/capacity;
- any new evidence.

Test whether it can produce a coherent next-day plan **without needing a second duplicated weekly machine artifact**.

If it cannot, identify the smallest missing handoff field.

Do not respond by copying the entire Brief into YAML.

---

## Phase E — operator acceptance

Show the operator:

1. actual repaired Weekly Command Brief;
2. normal + constrained examples;
3. one PrecapNextDay consumption example;
4. concise PASS/FAIL table;
5. only unresolved material choices.

The operator should be able to say:

> Yes, this is what I want the Sunday workflow to feel like.

Only then treat Module 01 output architecture as closed.

---

# 10. Then resume the input-pipeline simplification

After output architecture closes, continue the dedicated input-pipeline walkthrough from:

`research/PRECAP-WEEK-INPUT-PIPELINE-DECISION-HANDOVER.md`

The input exercise must use the same concrete style.

For each candidate input show:

```text
CURRENT AI VIEW
actual excerpt / approximate input size / overlap

LEAN AI VIEW
what remains

LOSS TEST
what weekly decision becomes impossible?

DRIFT TEST
can this duplicate disagree with higher-authority truth?
```

The likely target remains **authority-first selective retrieval**, not another persisted mega-packet.

Do not assume this target is approved until the operator sees the examples and confirms it.

---

# 11. Interaction style requirements

The operator prefers dense, precise explanations but cannot evaluate an architecture they cannot see behaving.

Therefore:

- use diagrams frequently;
- use before/after snapshots;
- use small real tables;
- use one realistic example repeatedly across stages so continuity is visible;
- distinguish `WEEKLY` from `NEXT DAY` visually;
- call out duplication explicitly;
- show the actual cost of over-detail, e.g. `4 flows × 5 days × 3 sprint goals = 60 sprint goals`;
- show what data disappears when a simplification is proposed;
- show what is still retrievable on demand;
- keep jargon secondary to behavior;
- do not hide uncertainties behind schemas;
- do not create new agents/skills/packet types as the default response to complexity;
- do not mutate production files during the walkthrough.

When a decision is hard, the next action is usually:

> show a better example

not:

> ask the same abstract question again.

---

# 12. Recommended opening message for the new chat

Start approximately like this:

> We will design this by running through the weekly workflow exactly as you would experience it on a Sunday. I will first show what PrecapWeek knows, then we will build the project strategy view, then the Monday-Friday allocation, then we will hand Monday into PrecapNextDay and watch what changes. At each boundary I will show what extra detail would cost and ask only one concrete decision. Nothing in production will be changed until the workflow itself makes sense end-to-end.

Then render Stage 0 and proceed directly into Stage 1.

Do not start with a ten-question Q&A.

---

# 13. Success condition

This handover succeeds when the next chat has helped the operator understand and approve an end-to-end experience resembling:

```text
CONFIRMED PROJECT TRUTH
        +
WEEKLY INTENT
        +
REAL CAPACITY
        |
        v
PRECAPWEEK
        |
        +--> Matrix 1: strategic project movements
        |
        +--> Matrix 2: Monday-Friday allocation
        |
        +--> material dependencies / deferrals / review flags
        |
        v
ONE WEEKLY COMMAND BRIEF
        |
        v
ONE OPERATOR APPROVAL
        |
        v
PRECAPNEXTDAY
        |
        +--> revalidate tomorrow
        +--> exact flows
        +--> sprint structure
        +--> prompts/execution
        +--> optional calendar write
```

with no unnecessary duplicate packet, no stale competing contract, no accidental Sunday micro-planning of the entire week, and no hidden loss of strategically useful context.
