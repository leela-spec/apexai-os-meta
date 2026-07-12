# flow_packet-20260713-F1

```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: flow_packet
  gate: none
  packet_id: "flow_packet-20260713-F1"
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: skipped
  target_surface: none
  next_state: "F1 (Leela) is confirmed as a planned skip for Monday; its skipped_flow_marker becomes the G3 evidence, independently dispatchable to normalize/recap."
  prerequisites:
    - artifacts/next-day-plans/next_day_plan-20260713.md
  expected_action: operator files the skipped_flow_marker (or overrides and executes), then dispatches normalize for this flow independently
  sources:
    - artifacts/weekly-plans/weekly_plan_packet-20260712-2026-W29.md
  uncertainties:
    - "Leela maintenance-hold rating was inferred with low confidence in the weekly packet; operator has not confirmed no Leela push is needed."
  unresolved_risk: none
  stop_condition: "Halt skip handling if the operator names urgent Leela work for Monday — convert to an executed flow instead."
  authority:
    state: candidate
    basis_digest: null
    verification_ref: null
  operator_validation: not_requested
```

```yaml
flow_packet:
  packet_id: flow_packet_2026-07-13_F1
  artifact_name: flow_packet
  created_or_updated_at: "2026-07-12"
  execution_day: "2026-07-13"
  generation_mode: standard_mode
  review_status: operator_review_recommended

  flow_packet_metadata:
    package: precap-next-day
    source_skill: precap-next-day
    contract_version: "0.1"
    produced_during: PreCapNextDay
    primary_consumer: operator
    downstream_consumers:
      - FlowRecap
    source_refs:
      - artifacts/weekly-plans/weekly_plan_packet-20260712-2026-W29.md

  flow_identity:
    flow_id: F1
    flow_slot: F1
    project: Leela
    flow_role: app_product_or_system_work
    flow_status: skipped
    default_flow: true
    override_reason: "Weekly plan holds Leela at maintenance for 2026-W29; Monday is single-focus Apex."

  flow_context_summary:
    operator_intent_summary: "No Leela intent named for Monday; weekly plan role is maintenance with no planned pushes."
    project_state_summary: "No Leela project state available (bootstrap week; empty status file)."
    weekly_plan_alignment: aligned
    source_context_refs:
      - artifacts/weekly-plans/weekly_plan_packet-20260712-2026-W29.md
    constraints: []
    assumptions:
      - "Leela genuinely needs no push this week because the operator named none (weekly packet medium-risk assumption)."
    unresolved_inputs:
      - current_project_status_overview

  workflow_process_labels:
    workflow_stage: maintenance_hold
    process_stage: skip_capture
    expected_output_type: skipped_flow_marker
    validation_source: inferred_from_context
    fit_status: valid_with_warnings

  flow_sprint_plan:
    sprint_policy: skipped
    sprint_count: 0
    sprints: []
    recap_digest_required: false

  prompt_pack_ref:
    flow_prompt_pack_path: artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F1.md
    prompt_pack_status: not_needed_for_skipped_flow
    prompt_pack_authority: references/flow-prompt-pack-contract.md
    prompt_engineering_dependency_status: not_needed_for_skipped_flow

  usage_tracking_refs:
    planned_usage_budget_ref: not_applicable_skipped_flow
    usage_tracking_status: not_needed_for_skipped_flow
    expected_usage_capture_fields: []

  flow_execution_capture_preparation:
    capture_status: not_needed_for_skipped_flow
    capture_instructions:
      - "File the skipped_flow_marker below; add an operator note only if the skip reason changes."
    raw_flow_dump_template: see_raw_flow_dump_template_section
    skipped_flow_marker_template: see_skipped_flow_marker_template_section

  operator_review_flags:
    - planned_skip_confirm_maintenance_hold

  validation_status: valid_with_warnings
```

## raw-flow-dump-template

```yaml
raw_flow_dump_template:
  template_id: raw_flow_dump_template_2026-07-13_F1
  flow_id: F1
  execution_day: "2026-07-13"
  completion_marker: not_started   # only used if operator overrides the skip and works on Leela
  operator_raw_notes: ""
  prompt_results: []
  artifacts_created: []
  decisions_made: []
  blockers: []
  model_usage_notes: []
  next_step_guess: ""
  recap_request: run_FlowRecap
```

## skipped-flow-marker-template

```yaml
skipped_flow_marker_template:
  marker_id: skipped_flow_marker_2026-07-13_F1
  flow_id: F1
  execution_day: "2026-07-13"
  skip_status: planned_skip
  skip_reason: "Maintenance week for Leela per weekly_plan_packet-20260712-2026-W29; Monday is single-focus Apex orchestrator verification."
  carry_forward_policy: operator_decides_later
  next_review_point: weekly_review
```

## flowrecap-handoff-block

```yaml
FlowRecap_handoff_block:
  handoff_id: FlowRecap_handoff_2026-07-13_F1
  flow_packet_ref: artifacts/flow-packets/20260713/flow_packet-20260713-F1.md
  raw_flow_dump_expected: false
  skipped_flow_marker_allowed: true
  context_to_pass:
    - flow_identity
    - flow_context_summary
    - skipped_flow_marker_template
    - operator_review_flags
  required_operator_completion_marker: skipped
  FlowRecap_ready_status: skipped_marker_only
  boundary_note: "PreCapNextDay prepares this handoff but does not run FlowRecap or create FlowRecap output."
```
