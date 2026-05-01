# APPENDIX_PROCESS_HANDOVER_PRIORITY

## Purpose

Operational appendix for Alfred's process-handover priority model.

This appendix defines how Alfred and Apex prioritize process handovers such as Night -> Day, Session Export -> Night synthesis, Daily Command Board construction, and craft-flow allocation.

It replaces the rejected parallel `value / urgency / leverage / fit` orientation model with one unified priority-control family:

```yaml
EVD / IMP / RSK + URG
```

## Authority boundary

```yaml
file_status: subordinate_operational_appendix
canonical_owner: managed/agent_kb/alfred/BEST_PRACTICES.md
source_decision_lock: managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
process_contract_reference: managed/processes/AGENT_HANDOFF_CONTRACTS.md
truth_boundary:
  - this appendix explains accepted Alfred/Apex process-handover priority practice after promotion into the Alfred KB
  - it does not replace managed process contracts
  - it does not authorize silent mutation of SSOT, OpState, calendar, config, or canonical KB
```

Alfred remains the current-system personal assistant actor. Leela remains future productization, not this runtime.

## Agent handoff vs process handover

The word handoff can mean two different things. Keep them separate.

| Type | Meaning | Example | Metric model |
|---|---|---|---|
| Agent handoff | One first-wave agent gives bounded work to another agent. | Alfred -> MetaOps, MetaOps -> Meta Detective | `EVD / IMP / RSK` |
| Process handover | One operating phase passes continuity, priority, or state to another phase. | Session -> Night, Night -> Day, Daily Board -> craft flow | `EVD / IMP / RSK + URG` |

The extra `URG` field is allowed only because process handovers often require explicit time pressure and delay-penalty handling.

## Relationship to AGENT_HANDOFF_CONTRACTS.md

`managed/processes/AGENT_HANDOFF_CONTRACTS.md` remains the formal process contract for first-wave agent handoffs.

Rules:

- Do not replace `EVD / IMP / RSK` with another metric family.
- Do not convert `EVD / IMP / RSK` to a 0-3 scale.
- Do not reintroduce `value / urgency / leverage / fit` as canonical metric fields.
- Add `URG` only when time pressure materially affects priority.
- If an Alfred -> MetaOps craft-flow brief becomes a material first-wave handoff, preserve formal handoff packet requirements.

## Core metrics

```yaml
process_handover_priority_v1:
  EVD: 1-100
  IMP: 1-100
  RSK: 1-100
  URG: 1-100
```

| Metric | Definition | Practical question | Existing/new |
|---|---|---|---|
| `EVD` | Strength and traceability of evidence. | How well do we know this is true enough to use? | existing |
| `IMP` | Importance/downstream impact if accepted, done, or ignored. | How much does this matter? | existing; absorbs prior `value` |
| `RSK` | Risk of proceeding, delaying, mishandling, or mutating truth incorrectly. | What can go wrong? | existing |
| `URG` | Time pressure, delay penalty, deadline pressure, or blocked-window pressure. | Why now? | new process-handover extension |

## Scale

Use the existing 1-100 band logic.

| Score range | Meaning |
|---:|---|
| 1-20 | low |
| 21-40 | limited |
| 41-60 | material |
| 61-80 | strong/high |
| 81-100 | decisive/highest |

### URG calibration

| URG range | Use when |
|---:|---|
| 1-20 | no meaningful penalty if deferred |
| 21-40 | useful soon, safe to defer |
| 41-60 | should happen in the current planning window |
| 61-80 | delay creates material loss or blocks downstream work |
| 81-100 | deadline, expiring window, hard external constraint, or severe delay penalty |

## Replaced variable mapping

```yaml
superseded_vulf_mapping:
  value:
    replacement: IMP
    status: absorbed
  urgency:
    replacement: URG
    status: retained_as_time_metric_with_1_100_scale
  leverage:
    replacement: rationale.unlocks
    status: not_score
  fit:
    replacement:
      - readiness
      - constraints
      - hard_flags
    status: not_score
```

### Implication

- A high-value item is simply high `IMP`.
- A time-sensitive item has material or high `URG`.
- A leverage-heavy item lists concrete unlocks in `rationale.unlocks`.
- A poor-fit item is represented by `readiness`, hard flags, and constraints.

Do not store V/U/L/F as canonical fields.

## Controls

Controls are not scores. They gate routing and explain why a scored item can or cannot be placed.

```yaml
controls:
  readiness: ready|partial|missing_input|blocked|operator_decision_needed
  lane: leela|master_of_arts|wildcard|none
  hard_flags: []
  priority_class: P0|P1|P2|P3
```

### Readiness

| Value | Meaning | Default handling |
|---|---|---|
| `ready` | enough context and inputs exist to act | eligible for normal planning |
| `partial` | workable with caveats or assumptions | eligible with visible caveat |
| `missing_input` | needed input is absent | clarify or discover before execution |
| `blocked` | cannot proceed until blocker is removed | unblock or defer |
| `operator_decision_needed` | operator choice is required | route to operator decision |

### Lane

`lane` is a placement guardrail, not importance.

| Lane | Default interpretation |
|---|---|
| `leela` | normally eligible for CF1 or CF2 |
| `master_of_arts` | normally eligible for CF3 |
| `wildcard` | normally eligible for CF4 |
| `none` | no standing lane protection |

## Hard flags

Hard flags are evaluated before normal P-class assignment.

```yaml
hard_flags:
  - hard_deadline
  - blocked
  - missing_input
  - operator_decision_needed
  - hygiene_hold
  - calendar_conflict
  - no_actionable_next_step
```

| Flag | Default route |
|---|---|
| `hard_deadline` | evaluate as P0 candidate if `URG` is high |
| `blocked` | route to unblock or defer |
| `missing_input` | route to input request or discovery |
| `operator_decision_needed` | route to operator decision |
| `hygiene_hold` | route to hygiene resolution |
| `calendar_conflict` | route to rhythm repair |
| `no_actionable_next_step` | route to MetaOps or Night for clarification |

## P0-P3 classification

P-classes are classification results, not weighted score totals.

```yaml
priority_class_rules_v1:
  P0:
    meaning: must_handle_or_repair_before_normal_allocation
    rule_any:
      - hard_deadline and URG >= 81
      - hygiene_hold blocks safe work
      - operator_decision_needed blocks downstream work
      - calendar_conflict blocks the day plan
    handling:
      - surface_before_normal_allocation
      - no_auto_assign_to_flow
      - operator_confirmation_or_repair_required

  P1:
    meaning: should_receive_craft_flow_today
    rule_all:
      - IMP >= 61
      - readiness in [ready, partial]
      - no_blocking_hard_flag
    rule_any:
      - URG >= 41
      - rationale.unlocks is not empty
      - lane is protected and weekly/default commitment applies
    cap: max_4_per_day

  P2:
    meaning: valid_default_lane_or_backlog_work
    rule_all:
      - IMP >= 41
      - readiness in [ready, partial]
      - no_blocking_hard_flag

  P3:
    meaning: defer_backlog_clarify_or_unblock
    rule_any:
      - readiness in [missing_input, blocked]
      - no_actionable_next_step
      - EVD <= 40 and IMP >= 41
      - stale_without_delta
```

## P1 max-four-craft-flow rule

```yaml
p1_capacity_rule:
  max_assigned_per_day: 4
  overflow_destination: deferred_or_not_today
  overflow_requires:
    - reason
    - recommended_revisit
    - displaced_by
```

Alfred may recommend at most four P1 craft-flow assignments for a normal day because the working day contains four craft flows.

## P0 no-auto-assign rule

```yaml
p0_handling_v1:
  auto_assign_to_flow: false
  display_surface: risks_and_repairs
  requires_operator_confirmation: true
```

P0 means normal allocation is unsafe or insufficient. P0 does not automatically mean "put this in CF1."

## Low-evidence / low-readiness rule

```yaml
low_evidence_or_low_readiness_handoff_rule:
  if EVD <= 40 and readiness in [missing_input, blocked]:
    route: discovery_or_clarification_handoff
  elif EVD <= 40:
    route: execution_handoff_with_evidence_warning
  elif readiness == partial:
    route: execution_handoff_with_assumption_warning
  else:
    route: normal_execution_handoff
```

## Examples

### Night -> Day Leela P1

```yaml
handover_item: leela_feature_spec_update
metrics:
  EVD: 75
  IMP: 85
  RSK: 35
  URG: 55
controls:
  readiness: ready
  lane: leela
  hard_flags: []
  priority_class: P1
rationale:
  impact_reason: Moves a core Leela spec/build surface forward.
  urgency_reason: Should be placed in the current daily planning window.
  unlocks:
    - downstream Nowa/Nova prompt preparation
route: CF1_or_CF2
```

### Urgent Master of Arts P0 candidate

```yaml
handover_item: master_of_arts_deadline_repair
metrics:
  EVD: 70
  IMP: 80
  RSK: 60
  URG: 90
controls:
  readiness: partial
  lane: master_of_arts
  hard_flags: [hard_deadline]
  priority_class: P0
rationale:
  urgency_reason: Deadline pressure creates severe delay penalty.
route: risks_and_repairs_then_operator_confirmed_override
```

### Blocked P3

```yaml
handover_item: unclear_project_task
metrics:
  EVD: 30
  IMP: 65
  RSK: 55
  URG: 25
controls:
  readiness: missing_input
  lane: wildcard
  hard_flags: [missing_input, no_actionable_next_step]
  priority_class: P3
route: discovery_or_input_request
```

### Calendar conflict P0/rhythm repair

```yaml
handover_item: overloaded_daily_board
metrics:
  EVD: 85
  IMP: 70
  RSK: 75
  URG: 82
controls:
  readiness: blocked
  lane: none
  hard_flags: [calendar_conflict]
  priority_class: P0
route: rhythm_repair_before_assignment
```

## Anti-patterns

- Reintroducing `value / urgency / leverage / fit` as canonical fields.
- Treating `URG` as a general replacement for all priority reasoning.
- Weighted total scoring as if precise.
- Hidden evidence weakness.
- Treating `lane` as importance.
- Treating `readiness` as a numeric score.
- Assigning more than four P1 craft-flow items.
- Auto-assigning P0 to a craft flow.
- Letting process handover metrics mutate OpState directly.
- Letting Daily Command Board changes after operator lock silently overwrite the board.

## Source basis

- `managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`
- `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md`
- `managed/processes/AGENT_HANDOFF_CONTRACTS.md`
- `managed/rituals/NIGHT_PLANNING_PROTOCOL.md`
- `managed/rituals/SESSION_EXPORT_PROTOCOL.md`
- uploaded source index and product-flow materials, including Alfred, Sequencing, Rhythm, Daily Flows, and Craft Flows inputs

## Future improvements

- Calibrate `URG` and P-class thresholds from real daily board outcomes.
- Define low-risk OpState auto-apply classes after v1 trace discipline is stable.
- Add full Weekly Rhythm Plan v1.1 after enough daily boards and tracking records exist.
- Explore whether future Algorithm can infer priority classes from tracking evidence without hiding the evidence basis.
- Reconsider mood/energy/BP-XP only after daily tracking proves useful and the operator explicitly promotes it.

## Simplification check

| Question | Verdict |
|---|---|
| What could be removed? | Detailed threshold examples could be moved to templates later if the appendix becomes too long. |
| What is necessary? | The `EVD / IMP / RSK + URG` lock, replaced-variable mapping, readiness/lane/hard-flag controls, P-class rules, and anti-patterns. |
| What is over-engineered? | Nothing material yet; the model avoids a second metric family and keeps `URG` bounded to process handovers. |
