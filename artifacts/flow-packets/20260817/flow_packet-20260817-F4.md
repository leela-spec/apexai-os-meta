```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: flow_packet
  gate: G2
  packet_id: flow-packet-20260817-F4
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: partial
  target_surface: none
  expected_action: "After G2 confirmation, operator selects the Investment branch and supplies the branch-specific input; then execute the bounded intake/contract work and return evidence."
  sources: [artifacts/next-day-plans/next_day_plan-20260817.md, apex-meta/epics/investment-intelligence-automation/001.md]
  uncertainties:
    - "The operator has not yet selected video discovery, alerts, or decision-feedback for Monday."
  authority: {state: candidate, basis_digest: null, verification_ref: null}
  operator_validation: not_requested
```

# F4 — Investment override

```yaml
flow_packet:
  packet_id: flow_packet_20260817_F4
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
    source_refs: [apex-meta/epics/investment-intelligence-automation/001.md]
    notes: "F4 overrides the default Residual slot because G1 confirmed Investment as a primary daily category."
  flow_identity:
    flow_id: F4
    flow_slot: F4
    project: Investment
    flow_role: investment_review_or_reactivation
    flow_status: planned
    default_flow: false
    override_reason: "G1-confirmed W34 primary-category override."
  flow_context_summary:
    operator_intent_summary: "Protect one Investment flow while preserving equal priority across video discovery, alerts, and decision-feedback branches."
    project_state_summary: "The three branch-entry tasks are blocked on operator-specific inputs; Monday therefore begins with branch choice and input acquisition."
    weekly_plan_alignment: operator_override
    source_context_refs: [artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md, apex-meta/epics/investment-intelligence-automation/001.md]
    constraints:
      - "Do not choose a branch on the operator's behalf."
      - "Do not fabricate topics, sources, alert conditions, or decision-process inputs."
      - "Do not convert discovered content into investment recommendations by default."
    assumptions: []
    unresolved_inputs:
      - "Branch choice: video discovery | alerts | decision feedback"
      - "Branch-specific operator inputs"
  workflow_process_labels: {workflow_stage: intake, process_stage: operator_input_acquisition, expected_output_type: clarified_input_contract, validation_source: inferred_from_context, fit_status: operator_review_recommended}
  flow_sprint_plan:
    sprint_policy: compressed_two_sprints
    sprint_count: 2
    recap_digest_required: true
    sprints:
      - {sprint_id: S1, sprint_role: first_work_sprint, sprint_goal: "Select one Investment branch and collect the exact operator-specific input required to clear its starting blocker.", expected_output_type: operator_input_record, prompt_sequence_ref: F4-S1, capture_focus: [decision_made, unresolved_question, source_context_used], completion_marker: not_started, validation_status: blocked_by_missing_operator_decision}
      - {sprint_id: S3, sprint_role: recap_digest_preparation_sprint, sprint_goal: "If sufficient input is supplied, draft the bounded branch-start contract and prepare evidence for FlowRecap; otherwise record the unresolved blocker exactly.", expected_output_type: clarified_input_contract, prompt_sequence_ref: F4-S3, capture_focus: [artifact_created, blocker_found, next_step_guess, unresolved_question], completion_marker: not_started, validation_status: operator_review_recommended}
  prompt_pack_ref: {flow_prompt_pack_path: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F4.md, prompt_pack_status: operator_review_recommended, prompt_pack_authority: precap-next-day}
  usage_tracking_refs: {status: missing_dependency}
  flow_execution_capture_preparation: {raw_flow_dump_template_ref: "# Raw Flow Dump Template", skipped_flow_marker_template_ref: "# Skipped Flow Marker Template", capture_status: prepared}
  FlowRecap_handoff_block: {source_flow_id: F4, expected_evidence: [branch_choice, operator_input_record, clarified_input_contract_or_exact_blocker], recap_status: pending_execution}
  operator_review_flags:
    - "G2 approval required before execution."
    - "Operator branch choice and branch-specific input are required during F4."
  validation_status: operator_review_recommended
```

## Raw Flow Dump Template
- Branch selected:
- Operator inputs supplied:
- Contract/output created:
- Remaining blocker:
- Suggested next step:

## Skipped Flow Marker Template
- flow_id: F4
- status: skipped
- reason:

## FlowRecap Handoff
Consume with normalized F4 evidence. A missing branch choice remains a blocker; do not infer one from the weekly plan.
