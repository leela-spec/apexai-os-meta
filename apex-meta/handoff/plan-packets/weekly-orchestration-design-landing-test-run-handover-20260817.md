# Handover — Land the Intended Weekly Orchestration and Test It

## Purpose

This handover supersedes the review-only posture of `operator-facing-artifact-simplification-review-handoff-20260817.md` for the next session.

The next AI is **not** being asked to rediscover the architecture, produce another broad audit, or offer 2–3 abstract redesign options. Enough evidence has already been recovered to establish the intended operator experience. The job now is to **close the remaining behavioral details with the operator, instantiate the design as concrete example outputs, and run a W34 replay before changing production skills**.

The design must be judged by whether the operator can actually plan the week, plan the day, open a flow, execute its three sprints with prepared prompts, and return evidence with low friction.

---

## 1. Design already established — carry this forward as the default

Do not reopen these points unless the operator explicitly changes them.

### Weekly planning

- Weekly planning is an **operator + AI planning conversation**, not a machine report.
- Its purpose is to understand the coming week, decide what should happen across active projects, surface meaningful constraints/decisions, and create a readable plan the operator can approve.
- The intended operator artifact is the **Weekly Command Brief** pattern already recovered in the repository.

### Daily planning

- Daily planning translates the approved week plus current project reality into the next execution day.
- The operator should receive one readable **PreCap Next Day Brief** that shows the day's direction, represented flows, short S1/S2/S3 summaries, expected outputs, and any material review item.
- The daily brief is an overview. It must not duplicate the full execution detail of each flow.

### Flow execution

- Each represented full flow gets its **own operator-facing Flow Execution Card**.
- A full flow has **three sprints**.
- The Flow Execution Card is the operator's actual workspace and contains the context, tasks, inputs, expected outputs, done conditions, stop/review conditions, and direct prompt links needed to execute the flow.
- The operator is expected to open and use these flow files.

### Prompts

- The previously recovered design explicitly rejected large repetitive operator-facing Flow Prompt Packs.
- Prompts should be **real execution assets**, not metadata placeholders.
- Default: one simple prompt file per required sprint prompt, directly linked from the Flow Execution Card.
- A prompt file contains only the small amount of usage context needed plus the **full callable/copyable prompt body**.
- PromptEngineer / the prompt-generation capability must create the actual prompt. Do not silently fall back to a metadata-only `degraded_generic_prompt_mode` and call that ready.

### Human / machine boundary

- Human-facing files are primary.
- Machine metadata may exist only where a named consumer requires it.
- Machine payloads must not repeat the human artifact.
- Raw schema fields, orchestration envelopes, validation boilerplate, lifecycle enums, ratings, and internal IDs are not part of the normal operator surface unless they affect an operator decision.

### Project state

- Canonical project/task state is the durable truth.
- Do not create a second independent truth system.
- `ProjectStatus`, if retained, is a **derived human/read projection of confirmed canonical state**, not a second state database.
- The current `[priority/urgency/date]` 1–100 machinery is **not presumed necessary**. Retain it only if a real current consumer and concrete value are demonstrated.

### Sync

- Apex Sync is **not a required operator-facing stage of the v0 weekly workflow**.
- Existing deterministic Sync functions may be used internally where they cheaply provide useful blocker/dependency/next-task evidence.
- Sync must not create extra operator work, extra approval gates, or extra human-facing artifacts in the v0 test.
- Do not redesign or delete Sync during the first test. First determine whether the intended workflow works without depending on it as a visible orchestration stage.

### Safety to preserve

Preserve only the safety boundaries that have demonstrated value:

1. plan is not execution evidence;
2. candidate project-state changes are not confirmed state;
3. real blockers and dependencies remain visible;
4. evidence/source lineage remains available where consequential;
5. consequential, ambiguous, destructive, scope-changing, priority-changing, or explicitly operator-gated decisions require approval;
6. routine deterministic bookkeeping should not create an operator approval stop.

---

## 2. Repository evidence that anchors the design

Read these before the first substantive answer. They are design evidence, not invitations to restart research.

- `apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml`
- `apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml`
- `apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml`
- `apex-meta/operator-output-design/step3-output-design-system/05-prompt-file-and-index-design.okf.yaml`
- `apex-meta/operator-output-design/step4-operator-template-system/templates/J02-weekly-command-brief.md`
- `apex-meta/operator-output-design/step4-operator-template-system/templates/J03-precap-next-day-brief.md`
- `apex-meta/operator-output-design/step4-operator-template-system/templates/J04-flow-execution-card.md`
- `apex-meta/operator-output-design/step4-operator-template-system/templates/J05-prompt-files-and-index.md`
- `apex-meta/operator-output-design/step4-operator-template-system/examples/master-of-arts-example-fragments.md`

Also inspect the current W34 outputs only as the **bad/current comparison case**:

- `artifacts/weekly-plans/project-status-overview-20260816.md`
- `artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md`
- `artifacts/next-day-plans/next_day_plan-20260817.md`
- `artifacts/flow-packets/20260817/flow_packet-20260817-F1.md`
- `artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F1.md`

Do not make the current W34 schemas the design authority.

---

## 3. How the new chat must start

The first phase is a **short iterative Q&A to close unresolved behavior**, not a new architecture workshop.

### Round 1 — Weekly planning semantics

Ask only the questions needed to determine:

- what the AI should automatically bring into the weekly conversation;
- what the operator actually decides at week level;
- how much weekday distribution is useful versus premature;
- what approval of a week means: committed direction versus flexible candidate plan;
- what weekly constraints/questions are important enough to interrupt the operator for.

After the answers, return a short concrete interpretation of the weekly interaction and a miniature example. Let the operator correct it.

### Round 2 — Daily + flow execution semantics

Ask only the questions needed to determine:

- what makes a flow `ready`;
- what belongs in the daily overview versus the Flow Execution Card;
- how the three sprints normally function;
- how flexible flow/sprint order should be;
- what happens when capacity supports fewer than the default flows.

After the answers, show one concrete example of a day flowing into one three-sprint Flow Execution Card. Let the operator correct it.

### Round 3 — Prompt callability + recap/gating only if still unresolved

Resolve only what is still necessary to run the test:

- whether a sprint normally needs one prompt or a short prompt sequence;
- how the operator wants to open/call prompts;
- which prompt-generation/routing capability should materialize them;
- the minimum evidence the operator returns after a flow;
- which kinds of resulting changes should auto-record versus require review.

Do not add more rounds unless a real ambiguity blocks the test.

---

## 4. Land a v0 design immediately after Q&A

After the Q&A, synthesize **one v0 design**. Do not present multiple architecture options unless the operator explicitly asks.

The v0 should be the simplest architecture consistent with the confirmed workflow:

```text
CANONICAL PROJECT STATE
        ↓
WEEKLY Q&A
        ↓
WEEKLY COMMAND BRIEF
        ↓
DAY Q&A / DAILY COMPILATION
        ↓
PRECAP NEXT DAY BRIEF
        ↓
FLOW EXECUTION CARDS
        ↓
REAL SPRINT PROMPT FILES
        ↓
OPERATOR EXECUTION
        ↓
MINIMAL EVIDENCE CAPTURE
        ↓
RECAP / CANDIDATE STATE CHANGES
        ↓
ONLY NECESSARY APPROVAL
        ↓
CANONICAL STATE UPDATE
```

Internal deterministic helpers may assist this flow, but they do not get their own operator-facing stage merely because they exist.

Before any production change, explain the v0 in plain language and show exactly what files the operator would normally touch.

Expected normal operator files:

1. one Weekly Command Brief for the week;
2. one Next Day Brief per planned day;
3. one Flow Execution Card per represented flow;
4. the real prompt files linked from those cards;
5. a concise recap/change review only when something material happened.

Anything beyond this must justify itself as hidden infrastructure or be excluded from v0.

---

## 5. Create golden examples from the actual W34 case

Do **not** modify production skills yet.

Use the already available W34 portfolio context and Monday plan as test input and create a side-by-side v0 replay under a clearly isolated test location, for example:

`apex-meta/test-runs/weekly-orchestration-v0-w34/`

Create:

- `weekly-command-brief.md`
- `next-day-brief-20260817.md`
- `flows/F1-flow-execution-card.md`
- `flows/F2-flow-execution-card.md`
- `flows/F3-flow-execution-card.md`
- `flows/F4-flow-execution-card.md` when appropriate
- actual prompt files under `prompts/`, named by flow and sprint

The prompt files must contain actual prompt bodies suitable for execution. If a prompt-generation dependency cannot produce a real prompt, the corresponding flow is **not ready**; surface the missing dependency rather than creating a fake ready artifact.

Use the recovered templates as starting patterns, but simplify them further when fields do not help this concrete run. The templates are not sacred schemas.

---

## 6. Test the v0 before rewiring anything

The operator should review the W34 replay as if it were tomorrow's actual workflow.

Test these questions:

### Weekly

- Can the operator understand the week's intended outcomes quickly?
- Does it support actual week-level planning rather than repeat project state?
- Are the only questions shown the ones that require operator judgment?

### Daily

- Can the operator understand what tomorrow is for and why these flows were chosen?
- Is the daily brief an overview rather than a duplicate of the flow cards?

### Flow

- Can the operator open one Flow Execution Card and execute all three sprints without opening machine contracts?
- Are task, inputs, outputs, done conditions, blockers and prompt links sufficient?

### Prompts

- Are the prompts real, directly usable, correctly scoped, and already prepared?
- Is prompt metadata minimal?

### System

- Did we preserve real blockers/dependencies and plan/evidence separation?
- Did any missing machine field actually prevent execution?
- Did ProjectStatus or Sync add value to this concrete run? If yes, identify the exact value. If no, do not force them into the operator workflow.

The test passes when the operator says the artifacts are genuinely usable for a real day, not merely cleaner than before.

---

## 7. Only after the replay passes: minimally wire production

After the operator approves the golden examples, then inspect the live skill/agent path and make the smallest changes needed so production generates the approved outputs.

Likely changes to evaluate:

- make the Weekly Command Brief the normal PrecapWeek operator output;
- make the PreCap Next Day Brief the normal daily operator output;
- make Flow Execution Cards the actual per-flow operator files;
- replace large operator-facing Flow Prompt Packs with real per-prompt files and a tiny mapping only where needed;
- invoke PromptEngineer/materialization before a flow is marked ready;
- stop ProjectStatus from behaving like separate project truth;
- keep Sync hidden/read-only/on-demand unless a demonstrated function requires automatic use;
- reduce gates to consequential decisions rather than routine writes.

Do not perform unrelated cleanup or architecture migration during this step.

---

## Anti-drift rules for the next AI

1. **Do not restart first-principles architecture research.** The human-facing design has already been found and operator-validated.
2. **Do not preserve a component because it exists.** Preserve it only because the concrete v0 needs it.
3. **Do not add a new schema to simplify an old schema.**
4. **Do not make the operator validate internal orchestration machinery.**
5. **Do not call placeholder prompts 'ready'.**
6. **Do not turn Q&A into an endless requirements exercise.** Ask only what blocks a concrete test.
7. **Use examples as the specification.** Once the operator approves the W34 replay files, those examples become the acceptance target for production wiring.
8. **Test before migrate.** A usable side-by-side replay is required before changing production skills.

---

## First response required from the next AI

Do not give an architecture plan.

1. State in a few lines the v0 workflow you believe is already established.
2. State the few behavioral details that remain unresolved.
3. Start **Round 1 — Weekly planning semantics** with at most 4 questions.

The purpose of the first exchange is to close enough uncertainty to produce the actual Weekly Command Brief example, not to discuss the entire orchestration system again.
