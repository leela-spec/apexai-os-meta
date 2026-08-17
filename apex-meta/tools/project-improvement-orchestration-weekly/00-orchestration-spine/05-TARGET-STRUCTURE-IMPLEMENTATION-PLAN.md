# Detailed realization plan — target Weekly Runtime

**Target is locked:** one main-session `weekly-orchestrator`, six stage Skills executed with isolated `context: fork`, two retained blind reviewer agents, `apex-session` as durable mutation authority, `apex-sync` as deterministic read-side authority, and PromptEngineer/AIRouting/model-usage-log only on demand. I am treating the architecture research as the accepted target, not reopening the A–E comparison.

The repository control files still say architecture research is the next action and O001 is unresolved, so the first execution step is to **record the decision and immediately move into integration**—not perform more architecture research.

---

## 0. Scope lock

```okf
implementation_scope:
  objective: >
    Replace the current weekly-orchestrator -> stage-agent -> stage-skill
    runtime with the accepted skill-owned selectively-forked topology,
    then wire the validated operator-output design into the actual
    production entrypoints.

  must_achieve:
    - one canonical lifecycle authority
    - six wrapper agents removed from active production
    - six owning stage skills directly executable in isolated fork contexts
    - two reviewer agents retained
    - operator-output templates required by active runtime
    - stale schema-first authority removed or archived
    - minimal machine handoffs
    - fresh-context repeatability

  explicitly_not_this_work:
    - redesign Apex generally
    - redesign apex-plan
    - redesign apex-sync algorithms
    - replace apex-session architecture
    - introduce SDK infrastructure
    - introduce agent teams
    - introduce hooks/MCP/plugins
    - invent new universal schemas
    - perfect every operator artifact during Module 00
    - change unrelated project-management state

  anti_drift_rule: >
    Every change must directly move an active Weekly Orchestration
    runtime path from the current topology toward the accepted target.
```

This matches the existing Macro/Micro guidance: correct the production runtime at its authority sources, avoid a new control plane, and leave detailed artifact refinement to Modules 01–08.

---

# Phase 1 — Record the architecture decision

### 1.1 Resolve O001

Update:

`apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md`

Add a locked architecture decision:

```okf
O001_resolution:
  status: accepted

  composition:
    main_session:
      - weekly-orchestrator

    forked_stage_skills:
      - PrecapWeek
      - PrecapNextDay
      - raw-flow-dump-normalize_when_needed
      - flow-recap_per_flow
      - status-merge_per_batch
      - ProjectStatus_when_requested

    retained_custom_agents:
      - apex-review-validity
      - apex-review-alignment

    direct_backbone:
      - apex-session
      - apex-sync

    on_demand_dependencies:
      - PromptEngineer
      - AIRouting
      - model-usage-log

  removed_from_active_runtime:
    - apex-precap-week
    - apex-precap-next-day
    - apex-evidence-normalize
    - apex-flow-recap
    - apex-status-merge
    - apex-project-status
```

### 1.2 Advance project state

Update `CURRENT-STATE.md` from:

> architecture research is next

to approximately:

```okf
project_phase: Module_00_architecture_integration
accepted_topology: skill_owned_selectively_forked
active_step: central_runtime_and_stage_interface_migration
next_action: implement_global_spine
```

### Gate

No architectural question remains open before implementation.

---

# Phase 2 — Fix cold-start production discovery

The research identified `.claude/Claude.md` as a fresh-context portability risk. The current project activation file also contains the Weekly Orchestrator/backbone routing rules that need to survive the topology change.

### 2.1 Rename

```text
.claude/Claude.md
        ↓
.claude/CLAUDE.md
```

### 2.2 Keep this file deliberately small

It should own only:

- distinction between Weekly Orchestrator and Multi-Agent Orchestration;
    
- explicit activation rules;
    
- `weekly-orchestrator` as Weekly production entrypoint;
    
- `apex-plan`, `apex-sync`, `apex-session` as shared capabilities;
    
- global canonical-state boundaries;
    
- refs-not-copies / progressive loading principle.
    

It must **not** reproduce:

- Weekly lifecycle sequence;
    
- stage contracts;
    
- gate details;
    
- output templates;
    
- Skill-specific procedures.
    

Those belong downstream.

### 2.3 Verify

Fresh Claude Code startup must recognize the project instruction file before any Weekly work.

**Pass:** one project activation source; no case-dependent duplicate remains.

---

# Phase 3 — Rewrite the central Weekly Orchestrator as the sole lifecycle authority

This is the core topology change.

The current `weekly-orchestrator/SKILL.md` explicitly requires all stage content work to run through named custom agents and hardcodes those agents into `stage_routing`.

## 3.1 Replace the routing model

Target:

```okf
stage_routing:
  precap_week:
    owner: PrecapWeek
    execution: context_fork

  precap_next_day:
    owner: PrecapNextDay
    execution: context_fork

  operator_execution:
    owner: operator_or_external_execution_surface
    execution: external

  evidence_normalize:
    owner: raw-flow-dump-normalize
    execution: conditional_context_fork

  flow_recap:
    owner: flow-recap
    execution: context_fork_per_flow
    parallelizable: true

  status_merge:
    owner: status-merge
    execution: context_fork_per_batch

  project_status:
    owner: ProjectStatus
    execution: optional_context_fork

  review:
    execution: custom_subagents
    agents:
      - apex-review-validity
      - apex-review-alignment

  durable_mutation:
    owner: apex-session

  deterministic_read_side:
    owner: apex-sync
```

## 3.2 Central orchestrator owns only lifecycle logic

Retain here:

- current loop position;
    
- ordered stage sequence;
    
- stage trigger;
    
- exact upstream refs passed to a stage;
    
- operator constraints;
    
- stage execution mode;
    
- persistence classification;
    
- operator authority/gates;
    
- review trigger;
    
- downstream consumer;
    
- degraded continuation;
    
- state mutation routing.
    

Remove from here:

- stage-specific output schemas;
    
- weekly planning doctrine;
    
- day-planning doctrine;
    
- prompt doctrine;
    
- recap interpretation;
    
- status merge semantics;
    
- project-status ranking semantics.
    

## 3.3 Replace agent dispatch with explicit Skill-input dispatch

Current pattern:

```text
parent
 -> named custom agent
 -> agent body
 -> preloaded Skill
 -> stage
```

Target:

```text
parent
 -> owning Skill with context: fork
 -> explicit refs + operator constraints
 -> stage
```

Every fork receives explicitly:

```okf
stage_invocation:
  run_date: required
  week_id: planning_stages_only
  input_refs: [...]
  operator_constraints: [...]
  requested_output_path_or_family: ...
```

No stage may depend on the parent chat's hidden design context.

## 3.4 Preserve the reviewers

Do **not** fold these into Skills:

```text
apex-review-validity
apex-review-alignment
```

They remain independent, blind, read-only Subagents.

## Phase 3 acceptance

The central runtime can explain the entire loop without mentioning any of the six removed wrapper agents.

---

# Phase 4 — Convert the six owning Skills into self-contained fork workers

Do this **before deleting the wrapper agents** so the replacement execution path exists first.

---

## 4A — PrecapWeek

Current entrypoint still makes `precap_week_output`, fixed projects, numeric ratings and `first_precap_next_day_seed` central runtime requirements.

### Change

`.claude/skills/PrecapWeek/SKILL.md`

Add isolated execution semantics:

```okf
execution:
  context: fork
  parent_context_assumed: false
```

Make the Skill self-contained from explicit refs.

### Module-00-level contract change

```okf
PrecapWeek:
  primary_operator_output: Weekly_Command_Brief

  inputs:
    - confirmed_current_project_context
    - operator_weekly_intent
    - real_calendar_or_capacity_constraints_when_available
    - relevant_recent_execution_signals

  AI_job:
    - weekly_synthesis
    - project_targets
    - planned_work
    - dependencies
    - blockers
    - decisions
    - cross_project_sequence

  downstream:
    consumer: PrecapNextDay
    transfer: reference_plus_minimal_seed
```

### Remove as global requirements

- fixed five-project roster;
    
- mandatory 1–100 priority/urgency ratings;
    
- schema compatibility ratings;
    
- requirement to duplicate the complete weekly result into a machine seed.
    

### Activate

`weekly-command-brief-template.md` becomes an **active required runtime reference**, not merely a promoted file.

### Do not do yet

Do not perfect the detailed Weekly Command Brief language/layout. That remains Module 01.

---

## 4B — PrecapNextDay

Current entrypoint makes `next_day_plan`, `flow_packet` and `flow_prompt_pack` separate schema authorities and requires flow-prompt-pack references for completion.

### Target contract

```okf
PrecapNextDay:
  execution:
    context: fork

  primary_operator_output:
    - PreCap_Next_Day_Brief

  expanded_outputs:
    - Flow_Execution_Card_per_full_flow
    - actual_prompt_files

  dependencies:
    PromptEngineer:
      load: only_when_prompt_required
    AIRouting:
      load: only_when_route_recommendation_required

  must_not:
    - treat_placeholder_prompt_as_ready
    - require_large_flow_prompt_pack
    - duplicate_full_flow_context
```

### Remove as mandatory

- separate full `flow_packet`;
    
- operator-facing `flow_prompt_pack`;
    
- generated file indexes that are trivially derivable;
    
- generic workflow/usage metadata with no consumer;
    
- degraded placeholder prompt packs being accepted as execution-ready.
    

### Activate

- `precap-next-day-brief-template.md`
    
- `flow-execution-card-template.md`
    
- `prompt-files-and-index-template.md`
    

Detailed behavior remains Modules 02–04.

---

## 4C — Evidence normalization

Target:

```okf
raw_flow_normalization:
  execution: context_fork_per_flow
  invocation: conditional

  if_input_already_conforms:
    action: bypass

  if_input_is_messy_or_partial:
    action: normalize

  output:
    purpose: FlowRecap_input
    persistence: only_if_future_consumer_requires
```

Remove the assumption that evidence normalization is a mandatory stage every time.

---

## 4D — FlowRecap

Target:

```okf
flow_recap:
  execution: context_fork_per_flow
  parallel_across_independent_flows: true

  primary_job:
    - interpret_actual_evidence
    - record_actual_results
    - identify_blockers
    - identify_decisions
    - propose_candidate_state_changes

  model_usage_log:
    invocation: only_when_actual_usage_evidence_exists

  mutation_authority: none
```

Eliminate automatic preloading of `model-usage-log`.

---

## 4E — StatusMerge

Target:

```okf
status_merge:
  execution: context_fork_per_batch

  owns:
    - combine_candidate_changes
    - expose_conflicts
    - produce_operator_decision_surface

  must_not_own:
    - durable_mutation
    - canonical_state
    - lifecycle_gate

  gate_owner: weekly-orchestrator
  mutation_consumer: apex-session
```

---

## 4F — ProjectStatus

Target:

```okf
ProjectStatus:
  execution: context_fork_when_requested
  lifecycle_required: false

  role:
    - readable_projection_of_confirmed_state

  sources:
    - confirmed_state
    - deterministic_Sync_signals_when_useful

  must_not:
    - become_second_state_authority
    - invent_priority_truth
    - be_required_after_every_mutation
```

---

# Phase 5 — Switch production routing

Once all six Skills can run directly as isolated workers:

### 5.1 Change `weekly-orchestrator/SKILL.md`

Point routing to the Skills.

### 5.2 Remove all production references to

```text
apex-precap-week
apex-precap-next-day
apex-evidence-normalize
apex-flow-recap
apex-status-merge
apex-project-status
```

Search:

- `.claude/skills/`
    
- `.claude/CLAUDE.md`
    
- manifests;
    
- active validation fixtures;
    
- current orchestration references.
    

Historical W34 artifacts are excluded from this cleanup: they should remain historical evidence.

### 5.3 Smoke-test routing before archival

Verify that the central orchestrator selects the direct Skill path.

**Do not archive the old agents before this check passes.**

---

# Phase 6 — Simplify the cross-stage handoff

The current central orchestrator requires a common handoff envelope for every stage. The existing Meso/Micro guidance already requires every field to justify itself through a named consumer.

## 6.1 Audit `handoff-schema.md`

For every field classify:

```okf
field_disposition:
  - KEEP_REQUIRED
  - KEEP_CONDITIONAL
  - DERIVE
  - MOVE_TO_STAGE_OWNER
  - ARCHIVE_REMOVE
```

### Retention test

```text
field
 -> exact consumer
 -> exact decision/capability
 -> concrete failure prevented
```

If that chain cannot be demonstrated, the field is removed or derived.

## 6.2 Machine handoff target

Prefer something like:

```okf
machine_handoff:
  artifact_ref: ...
  stage: ...
  state: candidate|confirmed
  expected_action: ...
  blockers_or_review_flags: [...]
```

Only if each retained field actually has a consumer.

Do **not** create another large replacement schema.

## 6.3 Human artifacts no longer begin with machine envelopes

The operator sees:

```text
Result Card
→ action/decision
→ supporting context
→ optional provenance
→ tiny machine handoff
```

This is the validated design already accepted by the project.

---

# Phase 7 — Normalize authority and persistence

Create one authoritative runtime map inside the Weekly Orchestrator contract, not a new independent registry.

```okf
authority:
  lifecycle: weekly-orchestrator
  weekly_planning: PrecapWeek
  daily_planning: PrecapNextDay
  prompt_content: PromptEngineer
  AI_routing: AIRouting
  evidence_normalization: raw-flow-dump-normalize
  recap: flow-recap
  candidate_merge: status-merge
  durable_mutation: apex-session
  deterministic_computation: apex-sync
  project_projection: ProjectStatus
  review_validity: apex-review-validity
  review_alignment: apex-review-alignment
```

## Persistence defaults

|Output|Target|
|---|---|
|Weekly Command Brief|durable operator artifact|
|Next Day Brief|durable operator artifact|
|Flow Execution Card|durable execution artifact|
|actual prompt file|durable execution artifact|
|normalization intermediate|ephemeral by default|
|FlowRecap result|durable result/evidence artifact|
|StatusMerge decision surface|durable when needed for mutation/audit|
|ProjectStatus|on-demand/derived unless Module 08 proves persistence value|
|Sync report|deterministic report under existing Sync contract|
|Session mutation|canonical durable state|

---

# Phase 8 — Retire the six wrapper agents

Only after direct routing passes.

Archive:

```text
.claude/agents/apex-precap-week.md
.claude/agents/apex-precap-next-day.md
.claude/agents/apex-evidence-normalize.md
.claude/agents/apex-flow-recap.md
.claude/agents/apex-status-merge.md
.claude/agents/apex-project-status.md
```

Preferred archive family:

```text
apex-meta/archive/weekly-orchestration/
  topology-pre-forked-skills-2026-08/
```

The repository's archive policy explicitly requires superseded production authority to leave active runtime paths while preserving provenance and replacement information.

Each archived file records:

```okf
archive_metadata:
  original_path: ...
  archived_date: 2026-08-17
  reason: replaced_by_direct_forked_skill_execution
  replacement: ...
  architecture_decision_ref: ...
```

Do not edit historical generated artifacts merely because their `produced_by` field names an old agent.

---

# Phase 9 — Clean role/doctrine loading

Review only the doctrines touched by the topology change.

### `meta-ops-doctrine`

Move unique lifecycle rules into `weekly-orchestrator` if they are genuinely global.

Then remove duplicate lifecycle authority from the doctrine.

### `meta-strategy-doctrine`

Move or associate relevant weekly-planning doctrine with `PrecapWeek`.

### `meta-detective-doctrine`

Keep as reviewer support.

### `hygiene-clean` / `informatics-design`

Do not load in normal Weekly execution.

Keep as QA/improvement references only.

### `alfred-doctrine`

Keep only genuinely operator-interaction-specific behavior that is not already central runtime law.

**Goal:** a routine weekly run should not preload architecture-improvement doctrine.

---

# Phase 10 — Static topology verification

Before detailed module work, run a strict active-path audit.

## Required zero-reference checks

No active runtime reference to:

```text
apex-precap-week
apex-precap-next-day
apex-evidence-normalize
apex-flow-recap
apex-status-merge
apex-project-status
```

Exceptions:

- archive;
    
- historical artifacts;
    
- architecture history.
    

## Required positive checks

Verify:

```okf
static_acceptance:
  weekly_orchestrator_is_single_lifecycle_owner: true

  direct_forked_skills_present:
    - PrecapWeek
    - PrecapNextDay
    - raw-flow-dump-normalize
    - flow-recap
    - status-merge
    - ProjectStatus

  retained_agents_exact:
    - apex-review-validity
    - apex-review-alignment

  durable_mutation_owner:
    - apex-session

  deterministic_read_side_owner:
    - apex-sync

  PromptEngineer_is_on_demand: true
  AIRouting_is_on_demand: true
  model_usage_log_is_on_demand: true
```

---

# Phase 11 — Module 00 integration test

This test proves the **architecture**, not detailed J2–J11 presentation quality.

Use a completely fresh Claude Code session under the existing `TEST-PROTOCOL.md`, which explicitly forbids supplying the design-chat rationale to the test runtime.

## Test A — cold start

Fresh session:

```text
run weekly-orchestrator
```

Verify:

- project instructions load;
    
- one production entrypoint is identified;
    
- no wrapper agent is selected;
    
- correct current loop position is found.
    

## Test B — PrecapWeek dispatch

Verify:

```text
weekly-orchestrator
 -> PrecapWeek fork
```

not:

```text
weekly-orchestrator
 -> apex-precap-week
 -> PrecapWeek
```

## Test C — PrecapNextDay dispatch

Same check.

## Test D — conditional evidence

Conforming evidence:

```text
normalizer NOT invoked
```

Messy evidence:

```text
raw-flow-dump-normalize fork invoked
```

## Test E — flow parallelism

Two independent recaps can run as separate isolated Skill workers.

## Test F — optional dependencies

With no usage evidence:

```text
model-usage-log NOT loaded
```

With no routing need:

```text
AIRouting NOT loaded
```

## Test G — reviewer isolation

Nonconsequential change:

```text
review agents do not run
```

Consequential trigger:

```text
validity + alignment agents run blind and independently
```

## Test H — authority

Attempt a durable change from `status-merge`.

Expected:

```text
rejected as direct mutation
→ routed to apex-session
```

---

# Phase 12 — Module 00 closure

Only after the topology test passes:

### Update

- `CURRENT-STATE.md`
    
- `DECISIONS.md`
    
- Module 00 README if necessary
    
- architecture references that still describe wrapper agents as active
    

### Module 00 completion state

```okf
module_00:
  topology: accepted_and_active
  central_runtime: corrected
  wrapper_agents_active: 0
  reviewer_agents_active: 2
  forked_stage_skills_active: 6
  stale_global_authority: none_known
  fresh_architecture_test: pass
  next_module: 01_weekly_command_brief
```

This is the exact completion condition the current Micro guidance is aiming at, now resolved against the architecture research rather than leaving the runtime primitive undecided.

---

# Phase 13 — Complete the human-runtime migration module by module

**Do not attempt all artifact-detail rewrites inside Module 00.**

The detailed sequence remains:

|Order|Module|Required production result|
|--:|---|---|
|01|Weekly Command Brief|`PrecapWeek` produces validated J2 human-first output|
|02|Next Day Brief|`PrecapNextDay` produces validated J3|
|03|Flow Execution Card|one actual J4 execution workspace per full flow|
|04|Sprint Prompts|real prompt files; direct links; no giant prompt pack|
|05|Execution Evidence|minimum truthful J6/J6a evidence contract|
|06|FlowRecap|J7 result card + candidate changes|
|07|Status Merge|minimal J9 decision/mutation handoff|
|08|Project Status|retain, derive-on-demand, or remove based on demonstrated consumer|

For **each** module:

```text
bounded module handover
    ↓
operator Q&A only where necessary
    ↓
edit owning active contract/template
    ↓
remove conflicting stale authority
    ↓
Master inspects actual repo diff/interfaces
    ↓
Master PASS
    ↓
fresh W34 runtime test
    ↓
operator result review
    ↓
close module
```

The validated design already defines the intended human-first relationships, so these modules should integrate/refine them rather than rediscover the output architecture.

---

# Critical dependency chain

```text
Architecture research                   DONE
        ↓
Record accepted topology
        ↓
Fix CLAUDE discovery
        ↓
Rewrite Weekly Orchestrator
        ↓
Make six Skills fork-capable/self-contained
        ↓
Switch central routing
        ↓
Simplify cross-stage handoff
        ↓
Normalize authority/persistence
        ↓
Archive six wrapper agents
        ↓
Static topology verification
        ↓
Fresh Module-00 architecture test
        ↓
MODULE 00 DONE
        ↓
01 Weekly Brief
        ↓
02 Next Day Brief
        ↓
03 Flow Card
        ↓
04 Prompt Files
        ↓
05 Evidence
        ↓
06 Recap
        ↓
07 Status Merge
        ↓
08 ProjectStatus
        ↓
Full fresh W34 lifecycle regression
```

## The main control rule

**Do not delete agents first, do not rewrite all output modules first, and do not run another architecture study.**

The shortest safe path is:

> **record decision → establish forked Skill replacements → switch the central control plane → retire duplicate authority → verify architecture → then integrate the operator modules one by one.**

That gets to the researched target without creating another intermediate architecture.