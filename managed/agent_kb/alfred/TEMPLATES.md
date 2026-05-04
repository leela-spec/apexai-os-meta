# TEMPLATES

## Purpose

Accepted validated reusable Alfred templates.

This file is the canonical home for Alfred's reusable forms: intake frames, alignment frames, route briefs, handoff packets, escalation forms, and KB repair reports. It absorbs the reusable template-level material from `HANDOFF_SCHEMA.md` while preserving `ESSENCE.md` as authority, `BEST_PRACTICES.md` as operating method, and `MISTAKES.md` as anti-pattern control.

## Status

```yaml
agent_id: alfred
kb_root: managed/agent_kb/alfred/
canonical_file: TEMPLATES.md
file_status: canonical_templates_consolidated
absorbed_template_from:
  - managed/agent_kb/alfred/HANDOFF_SCHEMA.md
constrained_by:
  - managed/agent_kb/alfred/ESSENCE.md
  - managed/agent_kb/alfred/BEST_PRACTICES.md
  - managed/agent_kb/alfred/MISTAKES.md
  - managed/agent_kb/alfred/SOURCE_MANIFEST.md
  - managed/agent_kb/alfred/COVERAGE_AUDIT.md
source_posture: validated_core_only
validator: meta_ops
next_recommended_file: managed/agent_kb/alfred/LEARNING_QUEUE.md
review_due: 2026-07-25
```

## Template schema

```yaml
template_entry:
  id:
  status: accepted | deprecated
  use_when:
  template_body:
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: alfred
  validator: meta_ops
  review_due:
```

## Template posture

Templates are reusable forms, not governance or runtime law.

Use these templates to make Alfred outputs consistent and route-ready. Do not treat examples as permission to execute, self-validate, promote accepted truth, mutate config, or harden source-gap-dependent Leela mechanics.

When a template depends on detailed Leela product mechanics, mark those mechanics as source-gap-dependent unless a later source-extension pass directly validates them.

## Accepted templates

### ALFRED-TPL-001 — First-contact intake

Use when a new operator request arrives and Alfred must convert raw intent into an aligned task frame.

```md
## Alfred Intake

- **Goal:** [what the operator wants changed, decided, created, or understood]
- **Desired output:** [answer / file / patch / route brief / plan / review / recommendation]
- **Context:** [current situation, relevant prior state, live constraint]
- **Timing:** [deadline, day/week pressure, calendar boundary]
- **Capacity:** [energy, available time, cognitive load, emotional sensitivity]
- **Priority:** [why this matters now]
- **Evidence/source status:** [fully_read / partially_read / not_accessible / provisional / mixed]
- **Risk:** [what can go wrong if routed or executed incorrectly]
- **Open questions:** [only questions required for safe continuation]
- **Recommended owner:** [Alfred / meta_ops / meta_strategy / meta_detective / special_ops__prompts_workflows / special_ops__knowledge_bank / operator]
- **Next action:** [smallest useful step]
- **Stop condition:** [what blocks safe continuation]
```

Evidence: `S1`, `S2`, `S5`, `ESSENCE.md`, `BEST_PRACTICES.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-002 — Weekly alignment

Use when the operator needs to reconcile weekly demand, priorities, capacity, and sequencing at a high level.

```md
## Weekly Alignment

- **Path demand:** [targets, priority pressure, carry-over, must-win outcomes]
- **Rhythm supply:** [available windows, boundaries, recovery needs, fixed commitments]
- **Skill Tree / Epic scope:** [which life/work domain or Epic is in focus]
- **Chunk reality:** [what the smallest useful action units are]
- **Sequence mode:** [Spark / Session / Flow / no-run repair]
- **Tradeoff:** [what must be dropped, deferred, shrunk, or protected]
- **Recommendation:** [one clear week-shaping move]
- **Route:** [owner and handoff if Alfred should not continue locally]
- **Source posture:** [validated high-level framing / provisional product mechanics / source gap]
- **Review signal:** [Stats/Sid/feedback signal to inspect later, if available]
```

Evidence: `S3`, `S4`, `S5`, `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-003 — Day-start sequencing

Use when the operator needs a day-start recommendation that turns priorities and capacity into a next runnable unit.

```md
## Day-Start Sequence Frame

- **Today's anchor:** [main priority or life constraint]
- **Energy/capacity:** [low / medium / high + reason]
- **Time windows:** [available blocks and hard boundaries]
- **Recommended mode:** [Spark / Session / Flow]
- **Why this mode:** [Path demand + Rhythm supply + risk]
- **First Chunk:** [smallest concrete first action]
- **Fallback:** [smaller recovery-safe option]
- **Do not do:** [tempting but wrong action for today]
- **Source posture:** [validated high-level framing / provisional product mechanics / source gap]
- **Route if needed:** [meta_ops / meta_strategy / meta_detective / special_ops__prompts_workflows / special_ops__knowledge_bank]
```

Evidence: `S3`, `S4`, `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-004 — Rhythm repair

Use when the operator's day/week is overloaded, fragmented, blocked, or inconsistent with capacity.

```md
## Rhythm Repair

- **Breakage:** [overload / fragmentation / no recovery / wrong placement / unclear boundary]
- **Demand source:** [Path / Epic / external commitment / emotional pressure]
- **Supply reality:** [available time, energy, calendar, recovery need]
- **Repair move:** [shrink / defer / move / sequence / protect / route / stop]
- **Next runnable unit:** [Spark / Session / Flow / admin repair / rest]
- **Boundary:** [what Alfred must not override]
- **Source posture:** [validated high-level framing / provisional product mechanics / source gap]
- **Review cue:** [what to check in Stats or later reflection, if available]
```

Evidence: `S3`, `S4`, `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-005 — Compact route brief

Use when Alfred's recommendation requires another owner to act, and the handoff should remain operator-readable.

```md
## Alfred Route Brief

- **To:** `<target agent or operator>`
- **Type:** `<execution_orchestration | strategy_options | validation_challenge | workflow_design | knowledge_placement | operator_clarification | source_gap_review | escalation_recommendation>`
- **Objective:** <one bounded objective>
- **Expected output:** <desired output>
- **Constraints:** <hard limits / must-not-do items>
- **Evidence:** <source refs or audit pointer>
- **Risk posture:** EVD `<low | material | high | unknown | not_material>` / IMP `<low | material | high | unknown | not_material>` / RSK `<low | material | high | unknown | not_material>`
- **Validator:** `<validator or none>`
- **Next action:** <immediate next step>
- **Stop condition:** <pause/escalation trigger>
- **Open questions:** <none or list>
- **Source gaps:** <none or list>
```

Evidence: `S1`, `S2`, `S3`, `HANDOFF_SCHEMA.md`, `ESSENCE.md`, `BEST_PRACTICES.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-006 — Canonical handoff packet

Use when the handoff is material, multi-step, source-sensitive, high-risk, or needs downstream execution without context reconstruction.

```yaml
handoff_id: HND-alfred-YYYYMMDD-001
from_agent: alfred
to_agent: meta_ops | meta_strategy | meta_detective | special_ops__prompts_workflows | special_ops__knowledge_bank | operator
handoff_type: execution_orchestration | strategy_options | validation_challenge | workflow_design | knowledge_placement | operator_clarification | source_gap_review | escalation_recommendation
target_surface: <path-or-bounded-target-or-none>
task_objective: <one bounded objective>
desired_output: <expected output shape>
operator_context:
  priority: <operator priority or none>
  timing: <timing/capacity constraint or none>
  relevant_context: <compact context only>
constraints:
  must_do:
    - <required constraint>
  must_not_do:
    - <forbidden action or boundary>
  assumptions:
    - <explicit assumption or none>
evidence_basis:
  source_refs:
    - <source ID, file path, claim cluster, or audit pointer>
  confidence: high | medium | low | unknown
  source_status: fully_read | partially_read | not_accessible | provisional | mixed
evd_band: low | material | high | unknown | not_material
imp_band: low | material | high | unknown | not_material
rsk_band: low | material | high | unknown | not_material
validator: <agent-or-none>
next_action: <immediate next action>
stop_condition: <condition requiring pause/escalation/return>
open_questions:
  - <question or none>
source_gaps:
  - <gap or none>
return_expected:
  owner: alfred | meta_ops | operator | other
  expected_return: <what should come back>
```

Evidence: `HANDOFF_SCHEMA.md`, `ROUTING_CONTRACT.md`, `BEST_PRACTICES.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-007 — Escalation / route decision

Use when Alfred detects that normal first-contact coaching is insufficient and the task must route to a governed specialist lane.

```md
## Escalation / Route Decision

- **Reason for escalation:** [execution / strategy / validation / KB / prompt-workflow / AI-routing / hygiene / source gap / operator clarification]
- **Why Alfred should not continue alone:** [boundary, evidence, risk, authority, or source-status reason]
- **Target owner:** [agent id or operator]
- **Expected result:** [specific return artifact]
- **Evidence:** [source, current context, audit pointer, or operator statement]
- **EVD band:** [low / material / high / unknown / not_material]
- **IMP band:** [low / material / high / unknown / not_material]
- **RSK band:** [low / material / high / unknown / not_material]
- **Validator:** [agent id or none]
- **Open questions:** [questions that affect safe continuation]
- **Stop condition:** [what blocks safe continuation]
```

Evidence: `S1`, `S2`, `A2`, `ESSENCE.md`, `BEST_PRACTICES.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-008 — Validation challenge request

Use when Alfred needs a separate validator because evidence, authority, contradiction, impact, or risk makes self-validation unsafe.

```yaml
handoff_id: HND-alfred-YYYYMMDD-detective-001
from_agent: alfred
to_agent: meta_detective
handoff_type: validation_challenge
target_surface: <artifact-or-decision-under-review>
task_objective: Review the claim, artifact, route, or decision for contradiction, authority drift, weak evidence, or unsafe continuation.
desired_output: Validation verdict, contradiction list, drift-risk notes, and required correction path.
constraints:
  must_do:
    - Check evidence sufficiency and authority boundary.
    - Identify stop/hold/escalation needs.
  must_not_do:
    - Do not silently rewrite the artifact under review.
evidence_basis:
  source_refs:
    - <claim cluster, file path, audit pointer, or operator statement>
  confidence: high | medium | low | unknown
  source_status: fully_read | partially_read | not_accessible | provisional | mixed
evd_band: low | material | high | unknown | not_material
imp_band: low | material | high | unknown | not_material
rsk_band: low | material | high | unknown | not_material
validator: none
next_action: Return validation verdict and correction path.
stop_condition: Stop if truth mutation, config mutation, or authority ambiguity is detected.
open_questions:
  - <review questions or none>
source_gaps:
  - <source gaps or none>
return_expected:
  owner: alfred | meta_ops
  expected_return: validation verdict and required action
```

Evidence: `HANDOFF_SCHEMA.md`, `MISTAKES.md`, `BEST_PRACTICES.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-009 — Knowledge placement / source-gap review

Use when material needs durable placement, source mapping, candidate/canon separation, or source-gap handling.

```yaml
handoff_id: HND-alfred-YYYYMMDD-kb-001
from_agent: alfred
to_agent: special_ops__knowledge_bank
handoff_type: knowledge_placement | source_gap_review
target_surface: managed/agent_kb/<agent-or-domain>/<candidate-file>.md | managed/knowledge/<file>.md | none
task_objective: Determine durable knowledge placement, source status, and candidate/canon boundary.
desired_output: KB placement recommendation, source-map note, and promotion-routing recommendation if needed.
constraints:
  must_do:
    - Preserve source status.
    - Separate candidate knowledge from accepted doctrine.
    - Identify whether material belongs in ESSENCE, BEST_PRACTICES, MISTAKES, TEMPLATES, LEARNING_QUEUE, source/audit control, or managed process/governance.
  must_not_do:
    - Do not approve promotion directly.
    - Do not treat learning queues as runtime truth.
    - Do not treat support files as a second scaffold.
evidence_basis:
  source_refs:
    - managed/agent_kb/alfred/SOURCE_MANIFEST.md
    - managed/agent_kb/alfred/COVERAGE_AUDIT.md
  confidence: high | medium | low | unknown
  source_status: fully_read | partially_read | not_accessible | provisional | mixed
evd_band: low | material | high | unknown | not_material
imp_band: low | material | high | unknown | not_material
rsk_band: low | material | high | unknown | not_material
validator: special_ops__informatics_design if structure validation is required; otherwise meta_ops
next_action: Return placement and source-boundary recommendation.
stop_condition: Stop if source material is being silently canonized.
open_questions:
  - <placement or source question>
source_gaps:
  - <source gaps or none>
return_expected:
  owner: alfred | meta_ops
  expected_return: KB placement recommendation and boundary note
```

Evidence: `HANDOFF_SCHEMA.md`, `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md`, `MISTAKES.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-010 — One-file KB repair report

Use after a single-file KB patch or repair iteration.

```md
## KB Patch Report

- **Target file:** `managed/agent_kb/alfred/<file>.md`
- **Operation:** [created / updated / redirected / deleted / verified unchanged]
- **Canonical class:** [ESSENCE / BEST_PRACTICES / MISTAKES / TEMPLATES / LEARNING_QUEUE / source-audit-control / appendix]
- **Reason:** [why the patch was needed]
- **Source basis:** [ESSENCE / BEST_PRACTICES / MISTAKES / TEMPLATES / SOURCE_MANIFEST / COVERAGE_AUDIT / other]
- **Commit SHA:** `<sha>`
- **Fetched blob SHA:** `<sha>`
- **Verification result:** [passed / failed]
- **Remaining risk:** [none / source gap / duplicate doctrine / appendix drift / needs redirect]
- **Next recommended file:** `<path or none>`
```

Evidence: `WORKFLOW_PLAYBOOK.md`, `BEST_PRACTICES.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-011 — Project Packet v1

Use when a work item needs compact project-facing context before MetaOps, Strategy, Detective, or KB routing.

```yaml
project_packet_v1:
  packet_id: PP-YYYYMMDD-001
  title: <short title>
  lane: leela | master_of_arts | wildcard | none
  current_state: draft | candidate | needs_validation | blocked | operator_review_required | accepted
  objective: <bounded objective>
  desired_output: <artifact or decision needed>
  context_summary: <compact context>
  metrics:
    EVD: <1-100>
    IMP: <1-100>
    RSK: <1-100>
    URG: <1-100 or null if not a process handover>
  controls:
    readiness: ready | partial | missing_input | blocked | operator_decision_needed
    hard_flags: []
    priority_class: P0 | P1 | P2 | P3
  rationale:
    impact_reason: <why it matters>
    urgency_reason: <why timing matters or none>
    unlocks: []
    risk_note: <risk>
    next_action: <smallest next action>
  stop_condition: <pause/escalation trigger>
```

Evidence: `APPENDIX_PROCESS_HANDOVER_PRIORITY.md`, `AGENT_HANDOFF_CONTRACTS.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-012 — Daily Command Board v1

Use when Alfred needs to present today's bounded command surface.

```md
## Daily Command Board

| Class | Item | Lane | Readiness | EVD | IMP | RSK | URG | Hard flags | Next action |
|---|---|---|---|---:|---:|---:|---:|---|---|
| P1 | <item> | <lane> | <readiness> | <1-100> | <1-100> | <1-100> | <1-100> | <flags> | <action> |

### Board controls

- **P0:** operator-confirmed or true stop-the-line only.
- **P1 cap:** maximum four normal-day craft-flow items.
- **Lock status:** draft | operator_locked | needs_revision.
- **Mutation rule:** after lock, add proposed deltas only.
```

Evidence: `APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-013 — MetaOps Craft Flow Handoff v1

Use when a Daily Command Board item becomes bounded MetaOps execution coordination.

```yaml
metaops_craft_flow_handoff_v1:
  handoff_id: HND-alfred-metaops-YYYYMMDD-001
  from_agent: alfred
  to_agent: meta_ops
  handoff_type: execution_orchestration
  board_item_ref: <Daily Command Board item id>
  lane: leela | master_of_arts | wildcard | none
  priority_class: P1 | P2 | P3
  objective: <bounded execution objective>
  expected_output: <return artifact>
  constraints:
    must_do: []
    must_not_do:
      - Do not exceed the bounded objective.
      - Do not mutate canonical files without a patch plan and approval path.
  metrics:
    EVD: <1-100>
    IMP: <1-100>
    RSK: <1-100>
    URG: <1-100>
  readiness: ready | partial | missing_input | blocked | operator_decision_needed
  hard_flags: []
  next_action: <immediate next step>
  stop_condition: <pause/escalation trigger>
  return_expected: <what MetaOps should return>
```

Evidence: `APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`, `AGENT_HANDOFF_CONTRACTS.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-014 — Operator-required Session Export correction

Use when a Session Export contains an operator-required correction and the correction must not directly mutate OpState.

```md
## Session Export Correction

- **Session export ref:** `<path or id>`
- **Correction source:** operator | verifier | trace audit
- **Correction:** <what was wrong>
- **Corrected trace statement:** <replacement trace statement>
- **OpState impact:** none | candidate_delta_required
- **Delta candidate ref:** `<id or none>`
- **Hard flags:** []
- **Stop condition:** Do not mutate OpState until delta is accepted.
```

Evidence: `APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-015 — OpState Delta Candidate v1

Use when trace or tracking suggests a live operating-state update.

```yaml
opstate_delta_candidate_v1:
  delta_id: OPD-YYYYMMDD-001
  source_trace: <Session Export, board item, or tracking record>
  proposed_change: <state change>
  reason: <why this may need to change>
  current_state_claim: <current known state>
  target_state_claim: <proposed state>
  evidence:
    EVD: <1-100>
    source_status: fully_read | partially_read | provisional | mixed | unknown
  impact:
    IMP: <1-100>
  risk:
    RSK: <1-100>
    hard_flags: []
  readiness: ready | partial | missing_input | blocked | operator_decision_needed
  validator: meta_ops | meta_detective | operator
  acceptance_needed: true
  stop_condition: Do not apply until accepted.
```

Evidence: `APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-016 — Tracking Record v1

Use for minimal Alfred v1 process tracking.

```yaml
tracking_record_v1:
  record_id: TRK-YYYYMMDD-001
  source: daily_board | session_export | handoff_return | operator_note
  item_ref: <id or path>
  action_taken: <what happened>
  result: done | partial | skipped | blocked | deferred
  friction_note: <short note or none>
  follow_up_candidate: <none or candidate id>
  exclusions:
    mood_energy_tracking: excluded_in_v1
    bp_xp_tracking: excluded_in_v1
```

Evidence: `APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-017 — Pattern Candidate v1

Use when repeated observations may become a future stable pattern.

```yaml
pattern_candidate_v1:
  pattern_id: PAT-YYYYMMDD-001
  observation: <what repeated or appears useful>
  occurrences:
    count: <integer>
    refs: []
  suspected_value: <why it may matter>
  constraints: []
  evidence:
    EVD: <1-100>
    IMP: <1-100>
    RSK: <1-100>
  status: candidate | strong_candidate | needs_validation | rejected | promoted
  promotion_threshold_note: <what evidence is still needed>
  stop_condition: Do not promote after one occurrence.
```

Evidence: `APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-018 — Weekly Preview v1

Use when daily board and rhythm evidence should become a lightweight week-facing preview without full operationalization.

```md
## Weekly Preview

- **Week anchor:** <main orientation>
- **Known hard constraints:** <calendar/operator constraints>
- **Likely P1 candidates:** <small list>
- **Rhythm considerations:** <soft capacity/placement notes>
- **Deferred candidates:** <P2/P3 or future work>
- **Evidence basis:** <tracking/session/board refs>
- **Open questions:** <blocking questions>
- **Boundary:** This is a preview, not a full Weekly Rhythm Plan.
```

Evidence: `APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md`, `APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

### ALFRED-TPL-019 — Monthly Direction Map placeholder

Use only as a non-operational placeholder until future work defines the monthly planning model.

```md
## Monthly Direction Map Placeholder

- **Directional theme:** <theme>
- **Likely lanes:** leela | master_of_arts | wildcard | mixed
- **Known constraints:** <constraints>
- **Candidate focus areas:** <short list>
- **Evidence gaps:** <what is not yet known>
- **Do not operationalize yet:** monthly planning remains future work until daily/weekly evidence is stable.
```

Evidence: `APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md`, `LEARNING_QUEUE.md`. Owner: `alfred`. Validator: `meta_ops`. Review due: `2026-07-25`.

## Controlled handoff types

Use these values for `handoff_type`:

| `handoff_type` | Use when | Typical target |
|---|---|---|
| `execution_orchestration` | Multi-step execution or specialist activation is needed. | `meta_ops` |
| `strategy_options` | Options, scenarios, timing, leverage, or recommendation packet is needed. | `meta_strategy` |
| `validation_challenge` | Evidence, authority, contradiction, drift, or risk needs adversarial review. | `meta_detective` |
| `workflow_design` | Repeatable prompt, process, checklist, or handoff pattern is needed. | `special_ops__prompts_workflows` |
| `knowledge_placement` | Durable KB placement, source mapping, or candidate/canon separation is needed. | `special_ops__knowledge_bank` |
| `operator_clarification` | The work cannot safely route until the operator clarifies constraints or intent. | Alfred/operator loop |
| `source_gap_review` | Source gaps or unread material block doctrine or execution quality. | `special_ops__knowledge_bank`, optionally `meta_detective` |
| `escalation_recommendation` | Stop, hold, degraded mode, or higher-level review may be needed. | `meta_ops` or `meta_detective` |

## Handoff quality checklist

A material handoff is acceptable only if it answers:

1. Who is receiving it?
2. What exactly should they produce?
3. What target surface or bounded artifact is affected?
4. What constraints and must-not-do rules apply?
5. What evidence supports the request?
6. What source gaps or provisional claims remain?
7. What EVD/IMP/RSK posture applies when material?
8. Who validates, if validation is needed?
9. What is the next action?
10. What condition stops or escalates the work?
11. What should be returned, and to whom?

## Invalid template use

| Invalid pattern | Why invalid | Correction |
|---|---|---|
| Missing target owner | Downstream work cannot proceed legibly. | Name a verified `to_agent`, operator loop, or route through `meta_ops`. |
| No stop condition | Receiver may continue unsafely under uncertainty. | Add explicit stop, hold, escalation, or return condition. |
| Unread source treated as read | Creates source-gap hardening. | Mark `not_accessible`, `provisional`, or route to source-gap review. |
| Alfred self-validates high-risk work | Collapses intake and validation roles. | Route to `meta_detective` or named validator. |
| Strategy routed as execution | Produces premature implementation. | Route to `meta_strategy` first. |
| Knowledge placement treated as promotion | Confuses candidate/canon boundary. | Route to `special_ops__knowledge_bank`; promotion remains separate. |
| Template treated as governance | Turns reusable wording into authority. | Keep as template unless separately promoted or routed to managed processes/governance. |
| Support file treated as template authority | Creates appendix-as-authority drift. | Resolve reusable forms to this file. |

## Consolidation rule

If a reusable form appears in a support file, move the stable version here. If a support file contains method rather than form, move it to `BEST_PRACTICES.md`. If it contains a failure pattern, move it to `MISTAKES.md`. If it contains provenance or audit status, leave it in source/audit control and reference it only when source posture matters.
