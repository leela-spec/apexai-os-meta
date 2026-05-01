# APPENDIX_PATTERN_LEARNING_AND_RHYTHM

## Purpose

Operational appendix for Alfred's candidate pattern learning and Rhythm planning reference.

This appendix defines how Alfred captures repeated planning, craft-flow, handoff, blocker, and operator-correction signals without prematurely turning them into canonical truth.

It also defines the light v1 Rhythm posture for Daily Command Board support.

## Authority boundary

```yaml
file_status: subordinate_operational_appendix
canonical_owner: managed/agent_kb/alfred/BEST_PRACTICES.md
candidate_owner: managed/agent_kb/alfred/LEARNING_QUEUE.md
source_decision_lock: managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
related_appendices:
  - managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md
  - managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md
  - managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md
```

Pattern learning is candidate-first. A pattern candidate is not canonical doctrine, runtime law, accepted KB truth, or OpState mutation.

## Pattern learning boundary

```yaml
pattern_learning_boundary:
  candidate_is_not_canonical: true
  working_pattern_library_is_not_accepted_truth: true
  source_tracking_records_are_evidence_not_doctrine: true
  operator_approval_required_for_canonical_change: true
  kb_ops_placement_required_for_promotion: true
```

Alfred may notice, describe, and route pattern candidates. Alfred may not silently canonize them.

## Pattern candidate creation

Create a candidate only after repeated evidence.

```yaml
pattern_detection_v1:
  create_candidate_if:
    repeated_success_count: ">=2"
    repeated_failure_same_root_cause: ">=2"
    repeated_operator_correction_same_field: ">=2"
    highly_efficient_workflow_seen: ">=2"
```

Candidate examples:

- same Daily Command Board correction appears twice
- same MetaOps handoff structure works twice
- same blocker appears twice with same root cause
- same physical/mental chunk rotation improves two craft flows
- same session outro field is repeatedly corrected

## Pattern Candidate v1

```yaml
pattern_candidate_v1:
  candidate_id:
  created_at:
  created_by: Alfred|Night|MetaOps|Operator
  candidate_type: planning|craft_flow|handoff|blocker|operator_override|tracking|rhythm
  summary:
  evidence_count:
  source_records: []
  repeated_signal:
  proposed_use:
  risk_if_wrong:
  status: candidate
  operator_review_needed: true|false
  target_future_surface:
```

## Pattern promotion

Promotion requires stronger evidence and governance.

```yaml
pattern_promotion_v1:
  normal_requirements:
    - successful_uses >= 3
    - evidence_across >= 2_sessions_or_periods
    - operator_approved: true
    - kb_ops_placed: true
  emergency_manual_promotion:
    allowed: true
    requires_label: manual_operator_override
```

Promotion target depends on content type:

| Candidate type | Likely target |
|---|---|
| identity/boundary doctrine | `ESSENCE.md` only after validation |
| operating method | `BEST_PRACTICES.md` |
| failure mode | `MISTAKES.md` |
| reusable form | `TEMPLATES.md` |
| unresolved/future improvement | `LEARNING_QUEUE.md` |
| source/audit note | `SOURCE_MANIFEST.md` or `COVERAGE_AUDIT.md` |

## Rejected candidate archive

Rejected candidates should not disappear silently.

```yaml
rejected_pattern_archive:
  candidate_id:
  rejected_at:
  rejection_reason:
  source_tracking_records: []
  resurface_only_if_new_evidence_count: ">=2"
```

## Operator override learning

```yaml
operator_override_learning:
  single_override: log_as_planning_correction
  repeated_same_override_count_2: create_pattern_candidate
  canonical_change: requires_operator_validation_and_kb_ops
```

A single override does not change doctrine. Repeated same-field overrides become candidates.

## Rhythm in Daily Command Board

Rhythm is represented lightly in v1 through a separate `rhythm_profile`, not by expanding every execution card.

```yaml
rhythm_profile_decision:
  include_in_v1_board: true
  structure: separate_rhythm_profile_with_by_flow_candidates
  reason: preserve_craft_flow_essence_without_bloating_execution_cards
```

The `rhythm_profile` supports:

- physical chunk candidates by flow
- mental chunk candidates by flow
- final break/reset
- afterwork regeneration plan
- branch balance notes when needed
- calendar conflict / rhythm repair signals

## Afterwork regeneration

```yaml
afterwork_regen:
  planned_by_Alfred: true
  replaces_work_flow: false
  tracking_required: false
  optional_note: true
```

Afterwork regeneration does not normally replace one of the four work craft flows. It is planned after the work day unless calendar reality or operator override requires a deviation.

## Weekly planning

```yaml
weekly_rhythm_plan:
  v1: light_preview_only
  v1_1: full_weekly_rhythm_plan
  reason: collect_daily_tracking_records_before_full_weekly_automation
```

V1 weekly preview may show:

- known hard deadlines
- likely high-urgency days
- obvious calendar conflicts
- broad lane commitments
- carry-over risks from Daily Command Boards

V1 must not overbuild a full weekly automation system before daily tracking evidence exists.

## Monthly planning

```yaml
monthly_direction_map:
  status: later
  allowed_now:
    - major_themes
    - known_hard_deadlines
    - risk_periods
  prohibited_now:
    - daily_flow_assignment
    - detailed_task_scheduling
```

Monthly planning is directional only in v1.

## Relationship to skill-tree / chunk system

Alfred may lightly capture chunk, epic, skill-tree, and workflow candidates from lived use.

Rules:

- Do not over-design taxonomy before usage creates evidence.
- Physical chunks are not project-linked by default.
- Chunk candidates can be recorded as learning candidates.
- Canonical Leela product data remains future productization, not current runtime.
- Alfred's candidate capture may later inform Leela product design.

## Examples

### Repeated successful MetaOps handoff

```yaml
pattern_candidate_v1:
  candidate_type: handoff
  summary: MetaOps produces better sprint plans when Alfred includes expected outputs, stop condition, and session_export_expectation.
  evidence_count: 2
  proposed_use: Add to MetaOps craft-flow handoff practice.
  status: candidate
```

### Repeated operator board correction

```yaml
pattern_candidate_v1:
  candidate_type: operator_override
  summary: Operator repeatedly moves Master of Arts admin out of CF3 when urgent Leela build work exists.
  evidence_count: 2
  proposed_use: Candidate lane override heuristic; do not promote until validated.
  status: candidate
```

### Recurring blocker

```yaml
pattern_candidate_v1:
  candidate_type: blocker
  summary: Missing current file map repeatedly blocks first craft flow execution.
  evidence_count: 2
  proposed_use: Add preflight file-map check to relevant board generation or MetaOps handoff template.
  status: candidate
```

### Physical/mental chunk rotation

```yaml
pattern_candidate_v1:
  candidate_type: rhythm
  summary: Physical activation plus cognitive framing before deep work improves craft-flow completion.
  evidence_count: 2
  proposed_use: Preserve physical/mental candidates in rhythm_profile by flow.
  status: candidate
```

## Anti-patterns

- Promoting a pattern after one occurrence.
- Deleting rejected candidates without trace.
- Treating working pattern library as canonical truth.
- Treating tracking records as accepted doctrine.
- Full weekly automation too early.
- Detailed monthly task schedule in v1.
- Replacing work craft flows with regeneration by default.
- Over-designing Skill Tree / Chunk taxonomy before usage evidence exists.
- Letting Alfred silently mutate canonical KB from repeated observations.

## Source basis

- `managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`
- `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md`
- `managed/agent_kb/alfred/LEARNING_QUEUE.md`
- `managed/knowledge/AGENT_KB_LANES.md`
- `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md`
- uploaded Rhythm, Sequencing, Daily Flows, Craft Flows, and Chunk/Epic materials

## Future improvements register

| Item | Current status | Why not v1 | Promotion condition |
|---|---|---|---|
| Full Weekly Rhythm Plan v1.1 | future | needs daily tracking evidence | repeated stable Daily Board usage and operator approval |
| Monthly Direction Map operationalization | future | v1 lacks evidence for detailed monthly scheduling | validated weekly flow and clear operator need |
| Low-risk OpState auto-apply classes | future | operator approval required in v1 | trace quality proven and operator explicitly approves classes |
| Pattern library storage structure | future | avoid premature taxonomy | enough pattern candidates exist to justify structure |
| Candidate detection automation | future | avoid false positives | repeated manual candidate process proves stable |
| Daily Command Board visualization | future | schema first, UI later | board schema and operator edit behavior stabilize |
| Future Algorithm from tracking evidence | future | not enough evidence | tracking records show stable predictive signals |
| BP/XP relation | future | Alfred tracking v1 excludes authoritative BP/XP | product-side Algorithm/Stats integration is validated |
| Mood/energy reconsideration | future | excluded from Alfred v1 | operator explicitly promotes after low-friction tracking works |

## Simplification check

| Question | Verdict |
|---|---|
| What could be removed? | Detailed future register can move to `LEARNING_QUEUE.md` after canonical patching. |
| What is necessary? | Candidate boundary, creation/promotion thresholds, rejected archive, Rhythm v1/v1.1 split, anti-patterns. |
| What is over-engineered? | Nothing material; thresholds are simple and prevent premature canonization. |
