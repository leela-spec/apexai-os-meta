# Apex Alfred — Claude Skill Definition Best Practice Guide

## Overview

This guide defines how to translate the PreCap / FlowRecap / APSU orchestration loop into Claude-native skill files inside `.claude/skills/`. It covers format rules, wording principles, interconnection patterns, and complete minimum viable `SKILL.md` templates for every process in the system.

The system is a six-stage loop:

```
PreCapWeek → PreCapNextDay → OperatorExecutesPlannedFlow
→ FlowRecapSkill → AllProjectStatusPacketUpdate (APSU)
→ [next PreCapNextDay cycle]
```

Skills map to this loop as follows: **PreCapWeek**, **PreCapNextDay**, **FlowRecapSkill**, and **APSU** are full Claude skills. **PromptAndAIRoutingPlanning** and **ModelSubscriptionUsageTracking** are supporting skills called by PreCapNextDay and FlowRecapSkill respectively. **OperatorExecutesPlannedFlow** is a human action — it has no skill file, but its output contract (RawFlowDump) must be documented in `schemas/`.

---

## Part 1 — Best Practice Format Rules

### 1.1 The anatomy of a SKILL.md

Every skill file follows the Agent Skills open standard and Claude Code's own extension guidance. The canonical structure is:

```
.claude/skills/<skill-name>/
├── SKILL.md              ← mandatory: description, frontmatter, procedure
├── references/           ← supporting contracts, schemas, examples
│   ├── io-contract.md
│   └── examples/
│       └── minimal-example.yaml
└── evals/               ← for critical skills: should-trigger and should-not-trigger tests
    └── eval-cases.md
```

The `SKILL.md` file itself has three zones:

1. **YAML frontmatter** — machine-readable routing metadata
2. **Objective block** — one paragraph, plain language, what this skill does and does not do
3. **Procedure block** — numbered steps, one action per step, minimal prose

### 1.2 Frontmatter rules

```yaml
---
name: skill-name-in-kebab-case
description: >
  One to three sentences. Start with a trigger verb.
  Name the exact input this skill expects.
  Name the exact output it produces.
  Name what it must NOT do (boundary).
allowed-tools: Read Write Grep Glob Bash
disable-model-invocation: false
---
```

**Description wording rules (critical):**

- The description is Claude's **routing key** — it decides which skill to invoke.
- Start with a verb: *Converts*, *Validates*, *Merges*, *Generates*, *Digests*.
- Name the **exact artifact** consumed, not a category. Write `flow_packet plus raw_flow_dump`, not "execution data".
- Name the **exact artifact** produced. Write `flow_recap_packet with operator_validated_next_step`, not "a summary".
- Name the **boundary** in one clause: `Does not merge across multiple projects` or `Never triggers next planning automatically`.
- Keep it under 60 words. Longer descriptions cause routing confusion.

**allowed-tools discipline:**

- Only list tools the skill actually uses.
- `Read` and `Grep` are safe for all skills.
- `Write` is needed only for skills that produce files (FlowRecap, APSU, PreCapNextDay).
- `Bash` is needed only for validation scripts.
- `disable-model-invocation: true` for any skill that writes to infrastructure, scheduler configs, or secrets.

### 1.3 Objective block rules

- One paragraph, three to six sentences.
- Restate the trigger condition in plain language.
- Name the input sources explicitly.
- Name the output artifacts explicitly.
- State what the skill **does not do** — this prevents scope creep across sessions.
- Do **not** put procedure steps here.

### 1.4 Procedure block rules

- Numbered steps only. No bullet lists inside procedure.
- Each step = one verb + one artifact + one outcome. Example: `Read flow_packet from the path supplied in the task board entry.`
- Group steps into logical phases with a bold label: `**Phase 1 — Load and validate**`
- Maximum 15 steps before the skill should be split.
- Always end with a `**Completion gate**` step that names the exact artifact the skill must produce and the condition that marks it done.
- Never embed schema definitions in the procedure — reference them from `references/`.

### 1.5 Interconnection: how skills hand off to each other

In this system, skills are connected via **artifact contracts**, not direct calls. One skill writes an artifact to a canonical path. The next skill reads from that path. The task board (`state/tasks.json`) is the coordination layer — it tracks which artifact is available for which skill.

The handoff pattern in every step that produces an output:

```
→ Write [artifact_name] to [LOGICAL_SLOT]
→ Update task board entry: set status to [ready_for_next_skill]
→ Emit handoff_packet if crossing a profile boundary
```

Never hard-code absolute paths inside `SKILL.md`. Use logical slot names (`FLOW_RECAP_SLOT`, `STATUS_PACKET_SLOT`) and resolve them via `schemas/naming.md` or environment config.

### 1.6 Validation and operator gates

Every skill in this system has at least one **operator gate** — a point where Claude must pause and wait for explicit human approval before continuing. These must be written as a procedure step, not just mentioned in the objective.

Pattern:
```
Step N: Present [summary or proposed output] to the operator.
  → Do not proceed until the operator explicitly approves, edits, or rejects.
  → If rejected, return to Step [N-k] with the operator's correction noted.
```

Use `validation_needed: true` in the output artifact's YAML block when the next downstream skill must not run until the gate passes.

---

## Part 2 — Skill-by-Skill Templates

### SKILL 1 — `precap-week`

**Path:** `.claude/skills/precap-week/SKILL.md`
**Owner profile:** `meta_strategist`

```markdown
---
name: precap-week
description: >
  Generates a weekly_plan_packet from the current all_project_status_packet,
  operator weekly intent, project priorities, and calendar constraints.
  Produces a structured weekly plan covering Leela, MasterOfArts,
  ApexAI/Hermes, and Residual pressure, with a first PreCapNextDay seed.
  Does not generate daily flow packets or assign prompt routes.
allowed-tools: Read Write Grep
disable-model-invocation: false
---

## Objective

Converts operator weekly intent and current project state into one approved
weekly_plan_packet. The packet defines strategic direction for the week,
project-level priorities, day-by-day allocation hints, and the seed context
for the first PreCapNextDay run. This skill does not plan individual flows,
generate prompt packets, or schedule model usage. It produces strategic
framing only. The operator must approve before the packet is used by
PreCapNextDay.

## Procedure

**Phase 1 — Load inputs**

1. Read `state/status/all_project_status_packet.yaml` from STATUS_PACKET_SLOT.
2. Read operator weekly intent from the task board entry or supplied note.
3. Read calendar constraints if provided. Mark as `missing` if absent —
   do not fabricate constraints.
4. Read `state/plans/weekly/` for any prior weekly plan to understand
   carry-forward context.

**Phase 2 — Normalize and prioritize**

5. For each project (Leela, MasterOfArts, ApexAI/Hermes, Residual), extract:
   - current status summary
   - next executable chunk
   - blockers or dependencies
6. Rank projects by urgency and operator intent.
   → If operator intent conflicts with blocker state, surface the conflict
   explicitly. Do not silently resolve it.

**Phase 3 — Draft weekly plan packet**

7. Draft `weekly_plan_packet` using the schema at
   `schemas/weekly_plan_packet.schema.yaml`.
   Required fields: `week_id`, `weekly_priorities`, `project_allocations`,
   `day_by_day_direction`, `fixed_calendar_constraints`,
   `first_PreCapNextDay_trigger_context`.
8. Validate: every project must have an allocation or an explicit omission
   reason. If any required field is empty, mark it `PENDING` — do not invent.

**Phase 4 — Operator gate**

9. Present the draft weekly_plan_packet to the operator as a readable
   markdown summary.
   → State: proposed week_id, project priority ranking, day allocations,
   any conflicts found, any missing inputs.
   → Do not write the packet to disk until the operator approves.

10. On approval: write `weekly_plan_packet` to WEEKLY_PLAN_SLOT at
    `state/plans/weekly/precap-week-{week_id}.yaml`.
11. Update task board: set `precap-week` task to `completed`.
    Set `precap-next-day` task to `ready`.

**Completion gate**

12. Skill is complete when:
    - `weekly_plan_packet` exists at WEEKLY_PLAN_SLOT
    - all required fields are present and not `PENDING`
    - operator approval is recorded in the packet under `operator_validation`
```

**References folder:**
- `references/io-contract.md` → maps upstream (APSU output) to downstream (PreCapNextDay input)
- `references/examples/weekly_plan_packet_minimal.yaml`

---

### SKILL 2 — `precap-next-day`

**Path:** `.claude/skills/precap-next-day/SKILL.md`
**Owner profile:** `meta_operations`

```markdown
---
name: precap-next-day
description: >
  Converts a weekly_plan_packet plus all_project_status_packet into one
  executable next_day_plan containing four flow_packets (F1 Leela,
  F2 MasterOfArts, F3 ApexAI/Hermes, F4 Residual), prompt_packets per
  sprint, and FlowRecapSkill instruction blocks.
  Does not execute flows, modify project status, or trigger FlowRecapSkill.
allowed-tools: Read Write Grep Glob
disable-model-invocation: false
---

## Objective

Translates weekly strategic direction, current project state, recent
FlowRecaps, skipped markers, model usage constraints, and calendar
feasibility into one approved execution day plan. The plan is composed
of four fixed flows in a fixed sequence (F1 → F2 → F3 → F4). Each flow
contains three sprints (S1 work, S2 work, S3 recap/digest). Each sprint
contains prompt_packets with model routing, context instructions, and
output capture requirements. This skill does not execute work, update
project state, or automatically trigger downstream skills. All outputs
require operator approval before any flow is executed.

## Procedure

**Phase 1 — Load and validate inputs**

1. Read `weekly_plan_packet` from WEEKLY_PLAN_SLOT.
   → If missing: block and request. Do not fabricate.
2. Read `all_project_status_packet` from STATUS_PACKET_SLOT.
   → If missing: mark `status_source: none` and proceed with reduced
   context. Surface this clearly to operator in gate step.
3. Read latest FlowRecaps from FLOW_RECAP_SLOT (most recent per project).
   → If none: proceed. Mark `latest_recaps: none`.
4. Read skipped_flow_markers from SKIPPED_MARKER_SLOT. If none, note it.
5. Read model_usage_summary from MODEL_USAGE_SLOT. If missing, note it.
6. Read AI_surface_inventory from the registry file if available.
7. Read calendar_constraints from operator note or task board entry.

**Phase 2 — Define execution day**

8. Define `execution_day_id` using format `YYYY-MM-DD-{ordinal}`.
9. Review calendar constraints and mark any flow that is infeasible.
   → Do not silently skip a flow. Add `calendar_block: true` and reason.

**Phase 3 — Instantiate flow structure**

10. For each flow F1/F2/F3/F4, create a flow_packet stub with:
    - `flow_id`, `project_id`, `fixed_position`, `execution_day_id`
    - `flow_goal` (derived from weekly plan + status delta)
    - `why_this_flow_now` (one sentence, grounded in project state)
    - `expected_outputs` (concrete, not vague)
    - `completion_state_options`: completed / partial / skipped / blocked

**Phase 4 — Generate sprints and prompt packets**

11. For each flow, define three sprints S1/S2/S3.
    F4 (Residual) sprint mapping:
    → S1 = Leela residual, S2 = MasterOfArts residual,
      S3 = ApexAI/Hermes residual.
12. For each sprint, generate one or more prompt_packets using the schema
    at `schemas/prompt_packet.schema.yaml`.
    Required per packet: `prompt_packet_id`, `prompt_goal`,
    `suggested_AI_surface`, `suggested_model_or_mode`, `reasoning_depth`,
    `context_to_include`, `files_to_upload_or_reference`,
    `expected_prompt_output`, `fallback_route`, `usage_tracking_required`,
    `cost_class`, `output_capture_instruction`.
    → If model_usage_summary signals a scarce mode: apply fallback_route.

**Phase 5 — Embed FlowRecapSkill instruction blocks**

13. For each flow, embed one FlowRecapSkill_instruction block containing:
    - `original_flow_packet_reference`
    - `required_raw_dump_items`
    - `required_operator_validation_question`
    - `completion_state_options`

**Phase 6 — Operator gate**

14. Present the full next_day_plan to the operator:
    → Show: execution_day_id, four flow goals, key prompt routes,
    any missing inputs flagged, any calendar blocks.
    → Do not write flow packets to disk until the operator approves.

15. On approval:
    → Write `next_day_plan` to NEXT_DAY_PLAN_SLOT at
      `state/plans/daily/precap-next-day-{execution_day_id}.md`.
    → Write each flow_packet to FLOW_PACKET_SLOT at
      `state/packets/flows/{execution_day_id}-F{n}.yaml`.
    → Update task board: set `precap-next-day` to `completed`.
      Set each `flow-recap-{Fn}` task to `waiting_for_operator`.

**Completion gate**

16. Skill is complete when:
    - `next_day_plan` exists at NEXT_DAY_PLAN_SLOT
    - all four flow_packets exist at FLOW_PACKET_SLOT
    - all prompt_packets are embedded in their flow_packets
    - all FlowRecapSkill_instruction blocks are present
    - operator approval is recorded in the plan under `operator_gate`
```

**References folder:**
- `references/io-contract.md` → full input list with sources and fallback rules
- `references/prompt-routing-guide.md` → model routing logic and cost classes
- `references/examples/flow_packet_minimal.yaml`
- `references/examples/prompt_packet_minimal.yaml`

---

### SKILL 3 — `flow-recap`

**Path:** `.claude/skills/flow-recap/SKILL.md`
**Owner profile:** `meta_operations`

This is the most critical skill in the system. It is the atomic execution-memory unit.

```markdown
---
name: flow-recap
description: >
  Converts one planned flow_packet plus one raw_flow_dump into a structured
  flow_recap_packet containing planned_vs_actual, sprint summary, artifact
  index, prompt result summary, project_status_delta, model_usage_delta,
  blockers, and an operator_validated_next_step.
  Does not merge across flows, update the all_project_status_packet,
  or trigger APSU.
allowed-tools: Read Write Grep Glob
disable-model-invocation: false
---

## Objective

Digests the evidence from one completed, partial, or blocked operator flow
into a structured, operator-validated recap packet. The packet is the atomic
memory unit that downstream skills (APSU, ModelSubscriptionUsageTracking,
and the next PreCapNextDay) rely on. A FlowRecap for F4 (Residual) must
produce split project_status_deltas — one per sprint project
(Leela from F4-S1, MasterOfArts from F4-S2, ApexAI/Hermes from F4-S3).
This skill does not merge recaps, update canonical project state, or
automatically create next-day planning context. It produces one
flow_recap_packet that is not considered complete until the operator has
explicitly validated the next_step_proposal and status_delta.

## Procedure

**Phase 1 — Load inputs**

1. Read `flow_packet` from FLOW_PACKET_SLOT for this flow_id.
   → If missing: block immediately. A recap without a planned packet is invalid.
2. Read `raw_flow_dump` from the path in the task board entry or from
   RAW_DUMP_SLOT for this flow_id.
   → If missing: check for a skipped_flow_marker at SKIPPED_MARKER_SLOT.
   → If skipped marker exists: produce a `skipped_flow_recap_stub` and close.
   → If neither exists: block and request operator input.
3. Read `prompt_packets` embedded in the flow_packet.
4. Read `existing_project_status_packet` from STATUS_PACKET_SLOT (optional).
5. Read `previous_flow_recap` for this project from FLOW_RECAP_SLOT (optional).
6. Read `usage_tracking_file` from MODEL_USAGE_SLOT (optional).

**Phase 2 — Validate**

7. Confirm that `flow_id` in raw_flow_dump matches `flow_id` in flow_packet.
   → Mismatch: block. Do not reconcile silently.
8. Confirm `execution_day_id` matches.
9. Confirm `completion_state` is one of:
   completed / partial / skipped / blocked / aborted / moved.
   → If absent: ask operator to classify before proceeding.

**Phase 3 — Compare planned vs actual**

10. For each sprint (S1/S2/S3), extract:
    - planned_output from flow_packet
    - actual_output from raw_flow_dump
    - delta classification: delivered / partial / missed / blocked

**Phase 4 — Build output sections**

11. Build `sprint_level_summary` for S1, S2, S3.
12. Build `artifact_index` from files, outputs, and artifacts mentioned
    in raw_flow_dump. Use format: `{artifact_type} | {name_or_path} | {status}`.
13. Build `prompt_result_summary` for each prompt_packet:
    - `prompt_packet_id`, `intended_goal`, `actual_output_quality`,
    `model_surface_used`, `route_value`, `recommendation`.
14. Build `model_usage_delta`:
    - `planned_route`, `actual_route`, `tokens_estimated`,
    `surface_used`, `should_repeat_route`, `routing_note`.
15. Build `project_status_delta`:
    - For F1/F2/F3: one primary project delta.
    - For F4 (Residual): three split deltas — F4_S1 → Leela,
      F4_S2 → MasterOfArts, F4_S3 → ApexAI/Hermes.
    Each delta: `project_id`, `status_change_summary`,
    `next_executable_chunk`, `blockers`, `artifact_references`.
16. Build `reusable_learning`: patterns, anti-patterns, routing discoveries.
17. Draft `next_step_proposal`: one concrete executable chunk per project
    affected, with a suggested flow assignment.
18. Build `context_for_future_PreCapNextDay`: seed for the next planning cycle.

**Phase 5 — Operator gate**

19. Present to operator:
    → Show: completion_state, planned_vs_actual delta, next_step_proposal,
    status_delta summary per project, any blockers.
    → Operator must explicitly: approve / edit / reject next_step_proposal.
    → Operator must confirm or correct project_status_delta.
    → Do not write the recap packet until the operator responds.

20. Record operator response as `operator_validated_next_step`.
    Set `validation_needed: false` once confirmed.

**Phase 6 — Write and update**

21. Write `flow_recap_packet` to FLOW_RECAP_SLOT at
    `state/recaps/flow/{execution_day_id}/{flow_id}-recap.md`.
22. Write `model_usage_delta` section reference to MODEL_USAGE_SLOT.
23. Update task board: set `flow-recap-{flow_id}` to `completed`.
    Set `apsu` task status: if all flows for the day are recapped, set
    `apsu` to `ready`. Otherwise leave as `waiting`.

**Completion gate**

24. Skill is complete when:
    - `flow_recap_packet` exists at FLOW_RECAP_SLOT for this flow_id
    - `operator_validated_next_step` is present and not empty
    - `validation_needed` is `false`
    - F4 recaps have three separate project_status_deltas
```

**References folder:**
- `references/io-contract.md`
- `references/f4-residual-split-rule.md` → explains the three-way delta split
- `references/examples/flow_recap_packet_minimal.md`
- `references/examples/skipped_flow_recap_stub.yaml`
- `evals/should-trigger.md` → trigger cases: "flow done, raw dump ready"
- `evals/should-not-trigger.md` → wrong cases: "weekly planning", "status merge"

---

### SKILL 4 — `all-project-status-update` (APSU)

**Path:** `.claude/skills/all-project-status-update/SKILL.md`
**Owner profile:** `meta_operations`

```markdown
---
name: all-project-status-update
description: >
  Merges all unconsumed flow_recap_packets and skipped_flow_markers since
  the last APSU run into an updated all_project_status_packet and
  next_PreCapNextDay_input_context.
  Runs once daily or on operator demand.
  Does not trigger PreCapNextDay automatically and does not consume already
  registered recaps.
allowed-tools: Read Write Grep Glob
disable-model-invocation: false
---

## Objective

Maintains the canonical cross-project state of the system by merging
new FlowRecap evidence into the running all_project_status_packet. APSU
is the only process that writes to STATUS_PACKET_SLOT. It is the single
source of truth for what has been completed, what is blocked, and what
the next executable chunks are across Leela, MasterOfArts, and
ApexAI/Hermes. APSU does not plan flows, generate prompt packets, run
automatically, or create cron jobs. In v0.1, PreCapNextDay is always
triggered manually by the operator after APSU completes.

## Procedure

**Phase 1 — Load inputs**

1. Read `previous_all_project_status_packet` from STATUS_PACKET_SLOT.
   → If this is the first run: initialize an empty status packet.
2. Read `consumed_flow_recap_registry` from REGISTRY_SLOT.
   → Lists all flow_recap_ids already merged. Never merge a recap twice.
3. Read all `flow_recap_packets` from FLOW_RECAP_SLOT whose `flow_recap_id`
   is NOT in the consumed registry.
4. Read `skipped_flow_markers` from SKIPPED_MARKER_SLOT not yet registered.
5. Read `model_usage_summary` from MODEL_USAGE_SLOT (optional).
6. Read `operator_merge_notes` from task board or supplied note (optional).

**Phase 2 — Validate recaps**

7. For each unconsumed flow_recap_packet, check:
   - `operator_validated_next_step` is present and not empty
   - `validation_needed` is `false`
   → If validation_needed is still `true`: skip this recap. Log it as
   `blocked_from_merge`. Do not merge unvalidated recaps.
8. For each skipped_flow_marker, confirm it has: `flow_id`, `project_id`,
   `reason`, `recovery_note`.

**Phase 3 — Merge by project**

9. **Merge Leela:** Combine F1 project_status_delta + F4_S1 delta from
   any F4 recaps. Resolve conflicts: if two deltas contradict each other,
   flag as `conflict` and surface for operator review. Do not silently pick one.
10. **Merge MasterOfArts:** Combine F2 delta + F4_S2 delta. Same conflict rule.
11. **Merge ApexAI/Hermes:** Combine F3 delta + F4_S3 delta. Same conflict rule.
12. **Merge blockers:** For each project, add new blockers, mark resolved blockers
    as `resolved`, and carry unresolved blockers forward.
13. **Merge artifact index:** Append new artifact references to each project.
14. **Merge usage notes:** If model_usage_summary available, attach routing
    summary per project.

**Phase 4 — Detect high-impact changes**

15. Flag any project_status_change that:
    - reverses a previously completed milestone
    - removes a dependency previously marked resolved
    - changes a project's priority ranking
    → High-impact changes require operator review before the packet is written.

**Phase 5 — Generate next planning context**

16. For each project, define `next_executable_chunk` from validated next steps
    in the recaps.
17. Build `next_PreCapNextDay_input_context` with fields:
    `execution_day_target`, `project_next_chunks`, `project_blockers`,
    `skipped_flow_markers_to_consider`, `prompt_routes_to_reuse_or_avoid`,
    `high_impact_changes_requiring_operator_review`.

**Phase 6 — Operator gate (conditional)**

18. If any `conflict` or `high_impact_change` was flagged in Phase 3–4:
    → Present these items to the operator before writing.
    → Operator must resolve or explicitly defer each flagged item.
    → Do not write until resolved or deferred.
19. If no conflicts or high-impact changes: proceed directly to Phase 7.

**Phase 7 — Write outputs**

20. Write `updated_all_project_status_packet` to STATUS_PACKET_SLOT at
    `state/status/all_project_status_packet.yaml`.
21. Write `next_PreCapNextDay_input_context` to
    `state/plans/daily/next-precap-context-{date}.yaml`.
22. Update `consumed_flow_recap_registry` at REGISTRY_SLOT with the
    flow_recap_ids merged in this run.
23. Update task board: set `apsu` task to `completed`.
    Set `precap-next-day` task to `ready_for_operator_trigger`.

**Completion gate**

24. Skill is complete when:
    - `updated_all_project_status_packet` exists at STATUS_PACKET_SLOT
    - `next_PreCapNextDay_input_context` is written
    - `consumed_flow_recap_registry` is updated
    - all conflicts are resolved or deferred with operator sign-off
    - task board reflects completion
```

**References folder:**
- `references/io-contract.md`
- `references/conflict-resolution-rules.md`
- `references/examples/apsu_minimal_output.yaml`
- `evals/should-trigger.md` → "daily merge after flows recapped"
- `evals/should-not-trigger.md` → "mid-flow", "before FlowRecaps complete"

---

### SKILL 5 — `prompt-and-ai-routing-planning`

**Path:** `.claude/skills/prompt-and-ai-routing-planning/SKILL.md`
**Owner profile:** `meta_operations`
**Called by:** `precap-next-day` (during Phase 4)

```markdown
---
name: prompt-and-ai-routing-planning
description: >
  Generates structured prompt_packets for one or more sprint slots by
  selecting the optimal AI surface, model, reasoning depth, and fallback
  route based on sprint goal, cost class, and current model_usage_summary.
  Does not execute prompts or evaluate prompt results.
allowed-tools: Read Grep
disable-model-invocation: false
---

## Objective

Translates sprint goals and available model/surface inventory into
executable prompt_packets. Each packet is a complete AI execution
instruction set: what to ask, where to ask it, at what reasoning depth,
with what context, and how to capture the output. This skill is called
as part of PreCapNextDay and is not run independently. It reads the
AI_surface_inventory and model_usage_summary to apply routing constraints
before assigning routes.

## Procedure

**Phase 1 — Load routing inputs**

1. Read `AI_surface_inventory` from the registry file.
   → If missing: note it. Use only well-known surfaces.
2. Read `model_usage_summary` from MODEL_USAGE_SLOT.
   → Identify any scarce modes or over-budget surfaces.

**Phase 2 — Generate prompt_packet per sprint slot**

3. For each sprint slot provided:
   a. Read `sprint_goal` and `expected_outputs`.
   b. Classify task type: research / synthesis / code / creative / review.
   c. Assign `suggested_AI_surface` and `suggested_model_or_mode`
      based on task type and inventory.
   d. Assign `reasoning_depth`: standard / extended / deep_research.
   e. Define `cost_class`: low / medium / high / scarce.
   f. Define `fallback_route` for each scarce or high-cost assignment.
   g. Fill all required fields per `schemas/prompt_packet.schema.yaml`.

**Phase 3 — Return packets**

4. Return prompt_packet list to the calling skill (precap-next-day).
   Do not write to disk directly — PreCapNextDay owns the write step.

**Completion gate**

5. Skill is complete when every sprint slot has a fully populated
   prompt_packet with no required field left empty or marked `PENDING`.
```

---

### SKILL 6 — `model-subscription-usage-tracking`

**Path:** `.claude/skills/model-subscription-usage-tracking/SKILL.md`
**Owner profile:** `meta_operations`
**Called by:** `flow-recap` (writes delta), `precap-next-day` (reads summary)

```markdown
---
name: model-subscription-usage-tracking
description: >
  Updates the running model_usage_log with one model_usage_delta from a
  completed FlowRecap, and generates a routing_recommendation_packet for
  the next PreCapNextDay.
  Does not plan flows or evaluate project state.
allowed-tools: Read Write Grep
disable-model-invocation: false
---

## Objective

Maintains a lightweight but accurate record of planned versus actual
AI surface and model usage across all flows. The primary consumers are
PreCapNextDay (for routing constraints) and APSU (for optional usage
summary). The skill should not block the core loop — all fields that
cannot be determined are marked `unknown` rather than `PENDING`. In v0.1,
the daily usage summary is optional and can be omitted if data is thin.

## Procedure

**Phase 1 — Load**

1. Read `model_usage_delta` from the flow_recap_packet for this flow_id.
2. Read `previous_model_usage_summary` from MODEL_USAGE_SLOT.
3. Read `available_AI_surface_inventory` from registry.

**Phase 2 — Append delta**

4. Append the usage delta to the log at MODEL_USAGE_SLOT.
   Include: `flow_id`, `sprint_id`, `prompt_packet_id`, `planned_route`,
   `actual_route`, `surface_used`, `tokens_estimated`, `output_quality`,
   `should_repeat_route`, `routing_note`.
   → Use `unknown` for any field not captured in the raw_flow_dump.

**Phase 3 — Generate routing recommendation**

5. If three or more entries exist for a given route:
   → Compute `route_reuse_signal`: repeat / avoid / neutral.
   → Flag any surface that has exceeded estimated capacity.
6. Build `routing_recommendation_packet`:
   `routes_to_prefer`, `routes_to_avoid`, `scarce_mode_warning`,
   `daily_summary_available: true/false`.

**Phase 4 — Write**

7. Write updated log to MODEL_USAGE_SLOT.
8. Write `routing_recommendation_packet` to a file consumable by
   PreCapNextDay at `state/metrics/subscriptions/routing-recs-{date}.yaml`.

**Completion gate**

9. Skill is complete when:
   - delta is appended to log without overwriting prior entries
   - routing_recommendation_packet is written
```

---

## Part 3 — Interconnection Map

The table below maps every artifact that crosses a skill boundary and names the exact logical slot each skill reads from and writes to.

| Artifact | Produced by | Written to (slot) | Consumed by | Notes |
|---|---|---|---|---|
| `weekly_plan_packet` | precap-week | WEEKLY_PLAN_SLOT | precap-next-day | Operator approval required before write |
| `next_day_plan` | precap-next-day | NEXT_DAY_PLAN_SLOT | Operator (human) | Operator approval required before write |
| `flow_packet` (×4) | precap-next-day | FLOW_PACKET_SLOT | Operator + flow-recap | One file per flow per day |
| `prompt_packet` | prompt-and-ai-routing-planning | Embedded in flow_packet | Operator + flow-recap + model-usage | Written by precap-next-day, not by routing skill |
| `raw_flow_dump` | Operator (human) | RAW_DUMP_SLOT | flow-recap | Not a skill — human writes messy markdown |
| `skipped_flow_marker` | Operator or flow-recap | SKIPPED_MARKER_SLOT | flow-recap (stub) + apsu | Produced instead of a raw_flow_dump |
| `flow_recap_packet` | flow-recap | FLOW_RECAP_SLOT | apsu + model-usage-tracking | Must include `operator_validated_next_step` |
| `model_usage_delta` | flow-recap (section) | Embedded in flow_recap | model-subscription-usage-tracking | Lightweight — `unknown` is valid |
| `project_status_delta` | flow-recap | Embedded in flow_recap | apsu | F4 must produce 3 split deltas |
| `all_project_status_packet` | apsu | STATUS_PACKET_SLOT | precap-next-day + precap-week | Only APSU writes to this slot |
| `next_PreCapNextDay_input_context` | apsu | NEXT_DAY_CONTEXT_SLOT | precap-next-day | Seed for next planning cycle |
| `consumed_flow_recap_registry` | apsu | REGISTRY_SLOT | apsu (next run) | Prevents duplicate merges |
| `routing_recommendation_packet` | model-subscription-usage-tracking | MODEL_RECS_SLOT | precap-next-day | Optional; used for prompt routing |

### Operator gates in the chain

```
PreCapWeek output       → G1: operator approves weekly_plan_packet
PreCapNextDay output    → G2: operator approves next_day_plan + flow_packets
After each flow         → G3: operator marks flow done/partial/skipped/blocked
FlowRecap output        → G4: operator validates next_step_proposal + status_delta
APSU output             → G5: operator reviews only conflicts and high-impact changes
```

No skill writes a canonical artifact until its upstream operator gate is confirmed. This rule must be embedded as the second-to-last procedure step in every skill that has an operator gate.

---

## Part 4 — Common Mistakes and How to Avoid Them

| Mistake | What happens | Correct pattern |
|---|---|---|
| Description uses vague input names ("execution data", "recent context") | Claude activates the wrong skill or fails to activate the right one | Name the exact artifact: `flow_packet plus raw_flow_dump` |
| Procedure embeds schema field lists inline | SKILL.md grows over 500 lines, Claude starts ignoring sections | Move schema refs to `references/io-contract.md` |
| APSU triggered after every flow | Duplicate merges, stale registry, wasted compute | Enforce `cadence: once_daily or manual` in APSU procedure |
| Operator gate step omitted | Claude writes canonical artifacts without approval | Every skill with a write step must have a gate step immediately before it |
| F4 recap produces one project_status_delta | Leela, MasterOfArts, Hermes lose tracking for residual work | F4 recap procedure must explicitly produce three split deltas |
| Absolute paths in SKILL.md | Skills break when deployed in different environments | Use logical slot names; resolve paths via `schemas/naming.md` |
| `disable-model-invocation` set to `true` on planning skills | Planning skills cannot call Claude for reasoning | Only set this on skills that write to infra, schedulers, or secrets |
| FlowRecap runs before operator marks completion state | Classification is guessed rather than confirmed | Step 9 in flow-recap procedure explicitly blocks until completion_state is confirmed |

---

## Part 5 — Recommended File Creation Order for These Skills

Based on the artifact dependency chain, create skill files in this order to ensure each skill can be tested with real inputs immediately after creation:

1. **`schemas/`** — all schemas first: `flow_packet`, `prompt_packet`, `flow_recap_packet`, `project_status_delta`, `all_project_status_packet`, `weekly_plan_packet`, `skipped_flow_marker`, `naming.md`
2. **`.claude/skills/prompt-and-ai-routing-planning/SKILL.md`** — no upstream skill dependency; can be tested with a stub sprint goal
3. **`.claude/skills/precap-week/SKILL.md`** — depends only on schemas and STATUS_PACKET_SLOT
4. **`.claude/skills/precap-next-day/SKILL.md`** — depends on precap-week output and routing planning skill
5. **`.claude/skills/flow-recap/SKILL.md`** — depends on flow_packet output from precap-next-day
6. **`.claude/skills/model-subscription-usage-tracking/SKILL.md`** — depends on flow-recap output
7. **`.claude/skills/all-project-status-update/SKILL.md`** — depends on flow-recap output and registry
8. **`evals/`** — add should-trigger / should-not-trigger cases for flow-recap and apsu first; these are the highest-risk skills

