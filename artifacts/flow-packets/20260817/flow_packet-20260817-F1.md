```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: flow_packet
  gate: G2
  packet_id: flow-packet-20260817-F1
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: complete
  target_surface: none
  expected_action: "After G2 confirmation, execute F1 and return a raw flow dump or skip marker."
  sources:
    - artifacts/next-day-plans/next_day_plan-20260817.md
    - apex-meta/epics/leela-core-interaction-development/001.md
  authority: {state: candidate, basis_digest: null, verification_ref: null}
  operator_validation: not_requested
```

# F1 — Leela

```yaml
flow_packet:
  packet_id: flow_packet_20260817_F1
  artifact_name: flow_packet
  created_or_updated_at: "2026-08-17"
  execution_day: "2026-08-17"
  generation_mode: standard_mode
  review_status: operator_review_recommended
  flow_packet_metadata:
    package: precap-next-day
    source_skill: precap-next-day
    contract_version: "0.1"
    produced_during: PreCapNextDay
    primary_consumer: operator
    downstream_consumers: [FlowRecap, prompt-engineering, ai-routing-and-usage-tracking, workflow-process-design, status-merge_later]
    source_refs: [apex-meta/epics/leela-core-interaction-development/001.md]
  flow_identity:
    flow_id: F1
    flow_slot: F1
    project: Leela
    flow_role: app_product_or_system_work
    flow_status: planned
    default_flow: true
  flow_context_summary:
    operator_intent_summary: "Advance Leela as an equal primary W34 category."
    project_state_summary: "Task leela-core-interaction-development:001 is dependency-clear and high priority."
    weekly_plan_alignment: aligned
    source_context_refs: [artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md, apex-meta/epics/leela-core-interaction-development/001.md]
    constraints: ["Use supported local/simulator evidence; do not assume runtime behavior."]
    assumptions: []
    unresolved_inputs: ["Exact execution environment availability is not yet verified."]
  workflow_process_labels:
    workflow_stage: verification
    process_stage: evidence_collection_and_gap_classification
    expected_output_type: conformance_report
    validation_source: inferred_from_context
    fit_status: operator_review_recommended
  flow_sprint_plan:
    sprint_policy: default_three_sprints
    sprint_count: 3
    recap_digest_required: true
    sprints:
      - {sprint_id: S1, sprint_role: first_work_sprint, sprint_goal: "Run and inspect SCR_Home_Today against the screen contract.", expected_output_type: runtime_observations, prompt_sequence_ref: F1-S1, capture_focus: [artifact_created, blocker_found, source_context_used, unresolved_question], completion_marker: not_started, validation_status: operator_review_recommended}
      - {sprint_id: S2, sprint_role: second_work_or_deepening_sprint, sprint_goal: "Classify observed gaps as keep/repair/mock-prototype debt/obsolete/deferred.", expected_output_type: gap_classification, prompt_sequence_ref: F1-S2, capture_focus: [decision_made, blocker_found, artifact_created], completion_marker: not_started, validation_status: operator_review_recommended}
      - {sprint_id: S3, sprint_role: recap_digest_preparation_sprint, sprint_goal: "Prepare evidence-backed conformance report and raw execution notes for FlowRecap.", expected_output_type: conformance_report, prompt_sequence_ref: F1-S3, capture_focus: [artifact_created, next_step_guess, unresolved_question], completion_marker: not_started, validation_status: operator_review_recommended}
  prompt_pack_ref:
    flow_prompt_pack_path: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F1.md
    prompt_pack_status: operator_review_recommended
    prompt_pack_authority: precap-next-day
  usage_tracking_refs: {status: missing_dependency}
  flow_execution_capture_preparation:
    raw_flow_dump_template_ref: "# Raw Flow Dump Template"
    skipped_flow_marker_template_ref: "# Skipped Flow Marker Template"
    capture_status: prepared
  FlowRecap_handoff_block:
    source_flow_id: F1
    expected_evidence: [runtime_observations, gap_classification, conformance_report]
    recap_status: pending_execution
  operator_review_flags: ["G2 approval required before execution."]
  validation_status: operator_review_recommended
```

## Raw Flow Dump Template
- Actual actions performed:
- Artifacts/evidence created:
- Decisions made:
- Blockers/gaps:
- Deviations from plan:
- Suggested next step:

## Skipped Flow Marker Template
- flow_id: F1
- status: skipped
- reason:

## FlowRecap Handoff
Consume this packet together with the normalized F1 raw flow dump or skip marker. Do not infer project-state changes from the plan alone.
