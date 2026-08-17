# Meso Guidance — Component-by-Component Integration Map

## Purpose

Translate the macro target into a concrete migration map for the current Weekly Orchestration repository.

This file defines **how the validated design is connected to the live system**. It does not finalize detailed wording/layout inside each output module; those decisions happen in the bounded module chats.

The architecture research in `01-ARCHITECTURE-RESEARCH-PROMPT.md` may simplify the physical `agent + skill` composition. Until that decision is accepted, this file uses current owners and focuses on authority, interfaces, stale-information removal, and runtime activation.

---

## 1. Global orchestration spine

### Current active owner

- `.claude/skills/weekly-orchestrator/SKILL.md`
- `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
- `.claude/skills/weekly-orchestrator/references/review-wiring.md`
- weekly stage-agent routing under `.claude/agents/`

### Current problem

The central loop is a real control plane, but it predates effective integration of the validated operator-facing layer. It currently makes shared packet envelopes and multiple gates central runtime concerns. Its stage returns are envelope/summary oriented rather than operator-artifact oriented.

### Required integration

The corrected Weekly Orchestrator must become the one canonical lifecycle authority and explicitly state:

1. ordered stages and their trigger conditions;
2. which stages are AI, deterministic, operator, or mixed;
3. accepted input references for each stage;
4. primary operator artifact, if any;
5. minimal downstream machine handoff, if any;
6. persistence rule;
7. real gate/review trigger;
8. state authority and mutation boundary;
9. degraded-mode behavior;
10. next consumer.

### Handoff-envelope review

Do not assume the current universal envelope survives unchanged.

For every field in `references/handoff-schema.md`, require:

`field -> named consumer -> concrete capability/failure prevented`.

If a field is inferable from file path/stage context, duplicated elsewhere, or only used to validate another generic envelope field, it is a simplification/archive candidate.

The operator-facing artifact must not begin with this envelope merely because a machine consumer needs a few fields.

### Gate review

Re-evaluate G1-G5 against the accepted policy:

- routine low-risk progression should not create avoidable stops;
- consequential, ambiguous, destructive, scope/priority-changing, or explicitly flagged changes remain gated;
- review agents should run only for demonstrated consequential cases, consistent with `review-wiring.md`.

A gate is retained only if it represents a real decision or safety boundary, not a stage-completion ceremony.

---

## 2. Project reality / planning input

### Design source

J1 Project State Success Card in:

- `step3-output-design-system/03-planning-artifact-designs.okf.yaml`

### Intended job

Answer: **What project reality is safe and useful to plan from now?**

It is planning context, not a second project database.

### Current stale-risk areas

- `ProjectStatus` can behave as a second transformation/state surface;
- PrecapWeek currently accepts `current_project_status_overview`, Session planning feed, Sync reports, detailed state files, project-priority signals, and ratings;
- the same project reality can therefore be represented in multiple layers before planning starts.

### Required integration direction

Module `08-project-status` must later determine whether the operator needs a durable ProjectStatus artifact at all.

For Module 00, establish only:

- confirmed durable state remains canonical;
- planning reads a concise, trustworthy projection/reference of that state;
- ProjectStatus, if retained, is derived/read-only;
- Sync outputs are deterministic helpers, not separate truth;
- numeric 1-100 priority/urgency values are not required globally unless a real retained consumer proves the need.

---

## 3. Weekly planning / J2 Weekly Command Brief

### Current owner

- `.claude/skills/PrecapWeek/SKILL.md`
- current worker: `.claude/agents/apex-precap-week.md` pending architecture-research verdict

### Validated design

- J2 in `03-planning-artifact-designs.okf.yaml`
- `.claude/skills/PrecapWeek/weekly-command-brief-template.md` was promoted in Step 5

### Current stale instructions

Current PrecapWeek still centers:

- `precap_week_output`;
- `first_precap_next_day_seed`;
- fixed planning project roster;
- `[priority/urgency/date]` values with 1-100 numeric fields;
- `weekly-plan-output-contract.md` as output schema authority;
- schema validation/operator-validation mechanics.

The active entrypoint does not make the promoted Weekly Command Brief template the normal primary operator artifact.

### Required integration

Module 01 must ultimately make the Weekly Command Brief the normal human-facing product of weekly planning.

Module 00 must prepare the interface by defining:

**Input:** confirmed current project context + operator weekly intent + relevant calendar/capacity constraints + recent execution signals when useful.

**AI job:** synthesize weekly direction, project targets, meaningful work, expected results, blockers/decisions, cross-project sequencing, optional day seeds.

**Operator job:** answer targeted planning questions and approve/edit the week.

**Primary output:** Weekly Command Brief.

**Downstream:** PrecapNextDay receives the approved weekly direction by reference/minimal seed; it must not require the weekly AI to duplicate the full brief into another machine schema.

### Stale retirement candidates to test

- numeric 1-100 rating requirement;
- fixed-project-roster machinery if canonical project state already defines active projects;
- `weekly-plan-output-contract.md` sections that merely duplicate the human brief;
- mandatory machine seed fields that PrecapNextDay can derive/read directly;
- agent envelope fields not consumed downstream.

Retain any machine-only data only after identifying the exact PrecapNextDay consumer.

---

## 4. Daily planning / J3 PreCap Next Day Brief

### Current owner

- `.claude/skills/PrecapNextDay/SKILL.md`
- current worker: `.claude/agents/apex-precap-next-day.md` pending architecture-research verdict

### Validated design

J3 defines the day-level overview. It keeps all three sprints visible for each full active flow, but complete execution details live in J4 Flow Execution Cards.

### Current stale instructions

Current PrecapNextDay makes these explicit schema authorities:

- `next_day_plan`;
- `flow_packet`;
- `flow_prompt_pack`;
- additional usage/workflow/calendar structures.

Its procedure requires one flow packet and one flow prompt pack per represented flow. Its completion gate requires prompt-pack references.

### Required integration

Module 02 must ultimately make the PreCap Next Day Brief the primary daily operator artifact.

Module 00 must establish:

**Input:** approved weekly direction + current confirmed state + recent execution/recap signals + real day constraints.

**AI job:** choose/shape the day, represented flows, short S1/S2/S3 intent, execution sequence and expected end-of-day state.

**Primary output:** PreCap Next Day Brief.

**Expansion:** direct references to J4 Flow Execution Cards.

**Machine handoff:** only data that the flow-card generator genuinely cannot derive from the brief/context references.

### Stale retirement candidates to test

- `flow_packet` as a separate persisted artifact if the Flow Execution Card can carry the required execution contract;
- full `flow_prompt_pack` contract;
- generated-file indexes that are derivable from paths;
- usage/workflow metadata with no current runtime consumer;
- generic degraded placeholders presented as readiness.

---

## 5. Flow preparation / J4 Flow Execution Card

### Current owner

Currently bundled into PrecapNextDay's flow-packet generation; detailed ownership may be adjusted by architecture research.

### Validated design

J4 is the **primary operator execution workspace** for one flow.

It owns:

- flow-relevant context;
- goals and expected outputs;
- three sprints;
- sprint tasks and inputs;
- dependencies;
- done conditions;
- stop/review conditions;
- direct prompt-file links;
- end-of-flow evidence expectation.

It explicitly does not own final prompt content, routing reasoning, FlowRecap interpretation, or durable state.

### Required integration

Module 03 must determine whether the existing `flow_packet` becomes:

**Preferred direction:** the Flow Execution Card itself, with only a tiny machine block/reference if a downstream consumer needs structured fields;

or

**Fallback:** a hidden/ephemeral machine artifact generated from the Flow Execution Card when a real consumer requires it.

Do not maintain two full persistent representations of the same flow unless the consumer audit proves necessity.

---

## 6. Prompt preparation / J5 Prompt Files

### Current owners

- PrecapNextDay currently creates/defines `flow_prompt_pack` structures;
- PromptEngineer owns final prompt construction;
- AIRouting owns routing recommendations where needed.

### Validated design

J5 explicitly replaces the rejected large repetitive operator-facing Flow Prompt Pack with:

- one simple file per actual prompt;
- direct relative links from the Flow Execution Card;
- optional tiny sprint-to-prompt mapping;
- actual prompt body;
- recommended surface;
- minimal degraded/missing flag when relevant.

### Required integration

Module 04 must make prompt readiness real:

1. PrecapNextDay/flow preparation determines what prompt is needed;
2. PromptEngineer creates the actual prompt body;
3. AIRouting contributes a recommendation only when routing is genuinely needed;
4. the prompt file is materialized;
5. the Flow Execution Card links to it;
6. the flow cannot be called fully ready when a required prompt body is missing.

### Stale retirement target

The operator-facing `flow_prompt_pack` should be retired unless architecture research identifies a real machine consumer requiring a compact mapping. If such a consumer exists, keep only that minimal mapping, not repeated flow/sprint context.

---

## 7. Execution evidence / J6 and J6a

### Intended role

Capture what actually happened without confusing plan with execution.

### Current owners

- operator execution / returned evidence;
- `apex-evidence-normalize` / raw-flow normalization path;
- skip-marker handling.

### Required integration direction

Module 05 must determine the minimum evidence contract required for reliable recap.

Module 00 should establish:

- raw evidence is not project truth;
- plan is never accepted as proof of execution;
- normalization is conditional on evidence shape/quality, not automatically valuable as a mandatory human-visible stage;
- skipped flow uses a minimal truthful marker;
- evidence lineage is retained where consequential.

If normalized evidence can be derived transiently for FlowRecap, do not persist a large extra artifact without a named future consumer.

---

## 8. FlowRecap / J7

### Current owner

- `.claude/skills/flow-recap/`
- worker `.claude/agents/apex-flow-recap.md` pending architecture-research verdict

### Intended role

Translate actual execution evidence into an operator-readable result and candidate implications. It does not silently mutate durable project state.

### Required integration direction

Module 06 should make the J7 result-card pattern the normal recap surface and remove duplicated schema-first operator presentation.

The recap should clearly distinguish:

- what actually happened;
- outputs/evidence;
- blockers/decisions;
- candidate project/task changes;
- what needs review;
- what can be handed onward automatically.

---

## 9. Status merge / J9 and durable state / J10

### Current owners

- status-merge stage/skill;
- apex-session for durable confirmed mutation.

### Required integration direction

Module 07 must test whether a daily `status_merge_packet` is the simplest useful transaction or whether candidate changes can be represented more directly.

The invariant is more important than the packet name:

```text
execution evidence
  -> interpreted candidate changes
  -> consequential review only where required
  -> confirmed mutation through the durable state authority
  -> mutation receipt / refreshed planning context
```

Do not let StatusMerge become a second state authority.

Routine, evidence-backed bookkeeping should not be forced through an operator ceremony if the accepted gate policy permits automatic application.

---

## 10. ProjectStatus / J11

### Current owner

- `.claude/skills/ProjectStatus/`
- `.claude/agents/apex-project-status.md` pending architecture-research verdict

### Intended role from validated design

Readable projection of **confirmed** portfolio/project reality.

### Required integration direction

Module 08 must answer whether this needs to be:

- persisted operator artifact;
- derived on demand;
- part of a project-state success view;
- or removed as a separate stage.

It must never become independent canonical truth.

Numeric ranking/rating machinery survives only if a retained consumer demonstrably needs it.

---

## 11. AIRouting / J12 and usage metadata

### Current risk

Current daily planning includes usage/routing dependency interfaces, which can expand into a large amount of planning metadata even when the operator only needs a usable prompt and recommended surface.

### Integration rule

AIRouting remains a specialist dependency, not a mandatory operator document.

Keep only:

- recommended execution surface when useful;
- routing reference if another component actually needs it;
- explicit unresolved routing issue when execution would be affected.

Do not reproduce routing doctrine, quotas, usage schemas, or model-selection reasoning in the day brief/flow card/prompt file by default.

---

## 12. Stale-information migration protocol

For every file modified by Modules 00-08, use this sequence.

### Step 1 — Classify authority

Mark the file as one of:

- `ACTIVE_CANONICAL`
- `ACTIVE_SUPPORTING`
- `COMPATIBILITY_ONLY`
- `SUPERSEDED_ARCHIVE`

Do not leave the status implicit when two generations of design exist nearby.

### Step 2 — Trace consumers

Before removing a field/file, search the active repo for exact references and semantic consumers.

### Step 3 — Migrate value

If a stale file contains a real invariant, move that invariant to the correct active owner before archiving the stale file.

### Step 4 — Archive

Move the superseded source out of active skill/agent paths according to `ARCHIVE-POLICY.md`, preserving:

- original path;
- archival date;
- reason;
- replacement authority;
- relevant commit/reference.

### Step 5 — Remove active references

Search again. No active entrypoint may still instruct a fresh runtime to load the archived contract as authority.

### Step 6 — Verify fresh loading

Start a fresh runtime/test context and invoke the real stage. If it reconstructs stale behavior, locate the remaining active instruction source rather than compensating in the test prompt.

---

## 13. Module handoff contract

After Module 00 stabilizes the global spine, each module chat receives only:

1. global lifecycle/interface relevant to that module;
2. validated design source for its output;
3. current owning skill/agent/contracts/templates;
4. known stale/conflicting instructions;
5. exact upstream input and downstream consumer;
6. archive policy;
7. fresh-test acceptance rule.

The module chat then:

```text
Q&A with operator
 -> finalize detailed module behavior
 -> update production files
 -> archive superseded module authority
 -> return implementation evidence to Master
```

The Master independently checks cross-system compatibility before the fresh runtime test.

---

## Meso completion condition

This integration map is satisfied when every retained production component has:

- one clear owner;
- one primary job;
- explicit upstream/downstream interface;
- justified AI/deterministic/operator role;
- justified persistence;
- only necessary gates;
- human-facing behavior wired through the active entrypoint where applicable;
- no conflicting stale authority remaining in active paths.

The next file, `04-MICRO-INTEGRATION-SEQUENCE.md`, defines the ordered implementation/check sequence the Master should execute without pre-deciding the detailed design inside Modules 01-08.
