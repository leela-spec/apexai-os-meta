# APEX Step 3 Round 4 — Review Draft

```
review_state:
  repository: leela-spec/apexai-os-meta
  branch: main
  live_repository_inspected: true
  round_4_files_written: false
  skill_templates_modified: false
  examples_modified: false
  durable_state_mutated: false
  decision_requested_from_marco:
    - keep
    - change
    - reject
```

## 1. Repository-grounded findings

### Verified ownership

**FlowRecap owns** recap interpretation, evidence summaries, candidate project-status changes, an advisory usage candidate, one next-step proposal, unresolved questions, and operator-review flags. It explicitly does **not** own accepted project state, durable KB updates, the final usage log, status merge, the next PreCapNextDay context, runtime, or calendar operations.

The `flow_recap_packet` contract confirms that:

- status changes remain candidate-only;
- usage output remains a candidate rather than the final log;
- operator validation is required for status acceptance;
- downstream consumers include `status-merge`, `model-usage-log`, and secondarily `project-kb-manager` and later planning.

**ModelUsageLog owns** the final `model_usage_delta`, `usage_summary`, planned-vs-actual comparison, route reuse/avoid signal, and lightweight future-planning advice. It does not choose routes before execution, define quotas, establish pricing truth, mutate project status, or replace AIRouting or FlowRecap.

The permitted route signals are exactly:

```
allowed_route_signals:
  - reuse_route
  - avoid_route
  - use_only_for_high_value_tasks
  - insufficient_data
  - operator_review_needed
```

The detailed usage contract requires missing actual evidence to produce a low-confidence advisory record with `insufficient_data`; exact model, pricing, cost, product-limit, and quota claims require explicit evidence.

### Contract and path drift

Two live-source issues should be recorded but do not block Round 4:

- The root system uses mixed-case paths such as `PrecapNextDay`, `ProjectStatus`, and `AIRouting`, while lower-case package naming appears elsewhere. Step 3 must preserve—not silently normalize—those live paths.
- The ModelUsageLog contract records that the expected AIRouting `package-manifest.md` was absent and an alternate manifest path was inspected instead.

### Unauthorized FlowRecap material

The two commits are **candidate material only**, not operator-approved design.

|Classification|Finding|
|---|---|
|**Compatible candidate material**|Result-card-first presentation; immediate outcome, change, next action and review; visible candidate-state warning; evidence/confidence section; downstream handoff; compact machine block. These align with verified Step 3 principles.|
|**Duplicative**|The template embeds a relatively detailed usage-learning section that overlaps with J8 and `model-usage-log`; its machine block also repeats more recap detail than the minimum downstream payload requires.|
|**Misleading**|The example contains a checked approval box and `operator_validated` state despite being unauthorized synthetic material. Those marks cannot be interpreted as Marco’s approval.|
|**Outside verified authority**|The example claims actual Round 4 progress and proposes project-status updates based on the unauthorized template work. It therefore cannot establish completion, accepted state, or a real downstream status candidate.|
|**Useful pre/post-change comparison**|The rewrite improved human readability significantly over the earlier schema-first template, but it compressed or removed some explicit contract fields from the visible surface. Those fields may remain in the secondary machine handoff, but the template cannot decide that before Round 4 design approval.|

The template commit changed a 203-line schema-forward document into a result-card-first 148-line projection. That direction is compatible, but the embedded full J8-like section and broad handoff block need tighter ownership boundaries.

The example commit is useful as a stress test for partial evidence, but its checked approval and `operator_validated` values are misleading and have no decision authority.

---

# A. J7 — FlowRecap Result Card

## Primary question

> **What happened in this flow, what evidence supports it, what candidate changes follow, and what must Marco review before anything moves downstream?**

## First-screen result card

```
FlowRecap_Result_Card:
  result_state: <completed|partially_completed|blocked|skipped|abandoned|unknown>
  what_changed: "<1–3 evidence-grounded sentences>"
  next_action: "<one concrete operator action; not a next-day plan>"
  review_needed: "<highest-priority review item or none>"

  show_only_when_material:
    evidence_gap: "<short warning>"
    candidate_state_warning: "Proposed changes are not accepted state."
    confidence: <medium|low|unknown>
```

This first screen describes the **flow result**, not whether validation machinery or completion gates passed. That follows the locked result-card rule.

## Essential sections

### 1. Planned versus actual

```
planned_vs_actual:
  planned:
    - "<goal or expected output>"
  actual:
    - "<evidence-supported outcome>"
  variance:
    - "<scope change, omission, extra work, or none>"
```

Keep this compact. The Flow Execution Card remains the detailed plan authority.

### 2. Outcome and artifacts

```
outcome:
  completed:
    - "<item>"
  incomplete_or_out_of_scope:
    - "<item>"

artifacts:
  created_or_changed:
    - label: "<artifact>"
      change: <created|updated|reviewed|proposed|no_output|unknown>
      ref: "<evidence ref>"
```

### 3. Decisions, blockers and open questions

Separate them visibly:

```
decisions:
  - summary: "<decision>"
    state: <made|proposed|deferred|needs_operator_validation>
    evidence_ref: "<ref>"

blockers_or_failures:
  - "<evidence-grounded blocker or none>"

unresolved_questions:
  - "<question or none>"
```

The contract already distinguishes outputs, decisions, blockers and unresolved questions; Step 3 should only determine how they are presented.

### 4. Candidate project-status delta

```
candidate_status_change:
  state: candidate
  proposal: "<one concise proposed change or no_state_change>"
  target: "<project/task/workstream/artifact/decision/blocker>"
  evidence_refs:
    - "<ref>"
  confidence: <high|medium|low|unknown>
  proposed_route: <status-merge|project-kb-manager|ProjectStatus_review|no_action|operator_decision_needed>
```

**Visible rule:** no wording such as “project status updated.” Use “candidate,” “proposed,” or “no change proposed.”

**Operator actions:**

- approve for downstream review;
- edit candidate;
- reject candidate;
- defer pending evidence;
- request more evidence.

Approval here authorizes a downstream review handoff; it does **not** itself write durable state.

### 5. Advisory usage evidence reference

J7 should contain only:

```
usage_candidate_summary:
  evidence_found: <yes|partial|no|unknown>
  observed_surface_or_model: "<value only when evidenced>"
  usage_purpose: "<short label>"
  candidate_ref: "<model_usage_delta_candidate ref>"
  confidence: <high|medium|low|unknown>
  handoff: <send_to_model-usage-log|no_meaningful_signal|operator_review_needed>
```

Do **not** calculate the route-learning conclusion here. J7 reports what usage evidence emerged; J8 interprets that evidence.

### 6. Evidence and confidence

```
evidence:
  status: <sufficient|partial|conflicting|missing_minimum_evidence>
  main_refs:
    - "<source — what it supports>"
  gaps_or_conflicts:
    - "<gap or none>"
  confidence: <high|medium|low|unknown>
```

Full source inventories remain collapsed or referenced unless they materially affect the decision.

### 7. Downstream handoffs

```
downstream:
  status_candidate:
    target: <status-merge|project-kb-manager|none>
    state: candidate
  usage_candidate:
    target: <model-usage-log|none>
    state: advisory_candidate
  next_step:
    owner: "<operator or named downstream owner>"
    proposal: "<one action>"
    not_a_next_day_plan: true
```

## Compact machine handoff

Reference the existing contract rather than reproduce it:

```
flow_recap_result_handoff:
  flow_recap_packet_ref: "<ref>"
  flow_result: "<state>"
  evidence_status: "<state>"
  candidate_project_status_delta_ref: "<ref or no_state_change>"
  model_usage_delta_candidate_ref: "<ref or none>"
  next_step_proposal_ref: "<ref>"
  operator_review_flags:
    - "<flag>"
  confidence: "<level>"
```

## Degraded behavior

|Condition|J7 behavior|
|---|---|
|Partial evidence|Produce a partial/low-confidence recap; identify unsupported conclusions.|
|Conflicting evidence|Preserve the conflict; do not choose a convenient interpretation silently.|
|Missing minimum evidence|Return `blocked` or `unknown` with one exact evidence request.|
|No supported status change|Emit `no_state_change`; do not invent progress.|
|No usage evidence|Set usage candidate to absent/unknown and allow J8 to produce `insufficient_data`.|
|Skipped flow|Show reason and handling; do not fabricate completed work.|

The contract explicitly permits low-confidence or blocked recap output instead of invented evidence.

## J7 acceptance checks

```
J7_acceptance:
  result_card_first: true
  flow_result_not_completion_gate_result: true
  planned_vs_actual_visible: true
  outputs_decisions_blockers_and_questions_separated: true
  candidate_status_change_visibly_not_accepted: true
  status_acceptance_owner_preserved: true
  usage_output_is_candidate_reference_only: true
  next_step_is_not_next_day_plan: true
  evidence_and_interpretation_separated: true
  missing_evidence_degrades_confidence: true
  compact_machine_handoff_secondary: true
  no_schema_redefinition: true
```

---

# B. J8 — Usage Learning Card

## Primary question

> **What route was planned, what was actually used, how useful was it, and what lightweight reuse or avoidance signal should future planning receive?**

## First-screen result card

```
Usage_Learning_Card:
  result: <meaningful_learning|insufficient_data|operator_review_needed>
  planned_vs_actual: "<one concise comparison>"
  learning_signal: <reuse_route|avoid_route|use_only_for_high_value_tasks|insufficient_data|operator_review_needed>
  future_routing_hint: "<one short advisory hint or none>"
  operator_action: "<accept|correct|ignore|review evidence|no action>"
```

Conditional:

```
show_when_material:
  confidence: <medium|low|unknown>
  scarcity_or_cost_note: "<only with explicit source>"
  evidence_warning: "<short warning>"
```

## Essential sections

### 1. Planned and actual use

```
usage_comparison:
  planned:
    surface_or_model: "<planned value or unknown>"
    planned_usage_ref: "<ref or none>"

  actual:
    surface_or_model: "<evidenced value or unknown>"
    evidence_status: <explicit_operator_supplied|inferred_from_transcript|inferred_from_artifact_metadata|partial|missing|unknown>
    evidence_refs:
      - "<ref>"

  purpose: "<planning|deep_research|code_agent_run|review_or_audit|prompt_generation|recap_or_summary|unknown>"
```

### 2. Comparison result

Use the existing contract values:

```
comparison:
  value: <matched_plan|cheaper_or_lighter_than_planned|heavier_or_scarcer_than_planned|different_route_used|planned_but_not_executed|executed_without_plan|insufficient_data>
  explanation: "<one sentence>"
```

### 3. Outcome-quality signal

Keep this qualitative and evidence-bound:

```
outcome_quality:
  signal: <useful|mixed|poor|unknown>
  evidence: "<short evidence-grounded note>"
```

It should not become a broad model benchmark.

### 4. Reuse or avoidance signal

Exactly one current allowed value:

```
route_signal:
  value: <reuse_route|avoid_route|use_only_for_high_value_tasks|insufficient_data|operator_review_needed>
  rationale: "<short explanation>"
```

### 5. Future routing hint

```
future_routing_hint:
  advice: "<short advisory hint or none>"
  applies_to: "<similar task type or context>"
  changes_routing_automatically: false
```

This is advisory context for AIRouting or planning—not a routing decision.

### 6. Cost, quota or scarcity note

Only show when sourced:

```
resource_note:
  statement: "<supported note>"
  source_ref: "<explicit source>"
  verification_status: <verified|operator_supplied|stale|unknown>
```

No exact cost, token, quota or current-product-limit claim without explicit evidence.

## Operator actions

```
operator_actions:
  - accept_usage_learning
  - correct_actual_surface_or_model
  - change_learning_signal
  - ignore_for_future_routing
  - request_evidence_review
  - no_action
```

## Lightweight and no-learning behavior

J8 may be absent when no downstream learning is useful.

The smallest valid visible result is:

```
usage_learning:
  result: insufficient_data
  reason: "No reliable actual-usage evidence was captured."
  future_routing_hint: none
  operator_action: no_action
  confidence: low
```

The contract explicitly requires `insufficient_data` with low confidence when actual usage evidence is missing.

## Downstream handoff

```
usage_learning_handoff:
  model_usage_delta_ref: "<ref>"
  usage_summary_eligible: <true|false>
  route_signal: "<allowed value>"
  future_consumer:
    - AIRouting_review_context
    - PreCapNextDay_usage_context
  automatic_route_change: false
```

A `usage_summary` rollup remains optional and should be created only when multiple deltas or a planning-period summary are useful.

## Compact machine handoff

```
usage_learning_card_handoff:
  source_flow_recap_ref: "<ref>"
  model_usage_delta_ref: "<ref>"
  comparison: "<allowed comparison>"
  route_signal: "<allowed signal>"
  confidence: "<level>"
  future_routing_hint: "<hint or none>"
  operator_review_needed: <true|false>
```

## J8 acceptance checks

```
J8_acceptance:
  result_card_first: true
  planned_and_actual_usage_visible: true
  actual_usage_grounded_in_evidence_or_marked_unknown: true
  exactly_one_allowed_route_signal_used: true
  outcome_quality_is_qualitative_and_evidence_bound: true
  missing_evidence_supports_insufficient_data: true
  no_meaningful_learning_case_supported: true
  exact_cost_token_or_quota_claims_require_source: true
  future_routing_hint_is_advisory: true
  AIRouting_is_not_replaced: true
  FlowRecap_is_not_repeated: true
  project_status_is_not_mutated: true
  compact_machine_handoff_secondary: true
```

---

# C. Cross-artifact relationship

## J6 → J7

```
J6_to_J7:
  provides:
    - flow_id
    - completion_state
    - planned_work
    - actual_work
    - outputs
    - decisions
    - blockers
    - unresolved_questions
    - evidence_refs
    - readiness
    - optional_usage_evidence_refs

  J7_adds:
    - recap_interpretation
    - candidate_project_status_delta
    - model_usage_delta_candidate
    - next_step_proposal
    - operator_review_flags
```

J6 answers **what evidence exists**; J7 answers **what that evidence means**. That boundary is already locked in Round 3.

## J7 → J8

```
J7_to_J8:
  required:
    - source_flow_recap_ref
    - model_usage_delta_candidate_ref_or_inline_candidate
    - actual_usage_evidence
    - usage_purpose
    - confidence

  when_available:
    - planned_usage_ref
    - observed_surface_or_model
    - prompt_ref
    - routing_ref
    - sourced_scarcity_note

  J8_interprets:
    - planned_vs_actual_comparison
    - one_allowed_route_signal
    - outcome_quality_signal
    - future_routing_hint
```

**Non-duplication rule:** J7 exposes evidence and candidate capture; J8 owns the learning conclusion.

## J7 → J9

```
J7_to_J9:
  provides:
    - candidate_project_status_delta
    - evidence_refs
    - confidence
    - conflicts
    - operator_review_flags

  J9_owns:
    - candidate_change_review
    - conflict_resolution_presentation
    - approval_rejection_or_deferral
    - merge_proposal

  J7_does_not:
    - accept_the_change
    - mutate_project_state
    - produce_updated_all_project_status
```

## J8 → J12 / PreCapNextDay

```
J8_downstream:
  to_J12_AIRouting:
    provides:
      - route_signal
      - similar_task_context
      - outcome_quality
      - confidence
      - evidence_ref
    does_not:
      - override_routing
      - change_inventory_or_quota_maps

  to_PreCapNextDay:
    provides:
      - compact_usage_learning_ref
      - reusable_or_avoid_signal
      - high_value_only_signal
      - sourced_scarcity_note_when_available
    does_not:
      - create_the_next_day_plan
      - select_the_route
      - require_usage_bureaucracy_for_minor_interactions
```

---

# Recommended Round 4 decision

```
recommendation:
  J7: keep_with_boundary_tightening
  J8: keep
  cross_artifact_relationship: keep

  key_corrections_to_unauthorized_candidate:
    - remove_full_J8_interpretation_from_J7
    - keep_only_usage_evidence_and_candidate_reference_in_J7
    - remove_checked_approval_boxes_from_examples
    - never_label_unauthorized_examples_operator_validated
    - reduce_machine_handoff_to_downstream_minimum
    - preserve_full_contract_fields_by_reference_not_visual_duplication
```

**No repository files were created or changed.** Round 4 remains at the operator review gate.