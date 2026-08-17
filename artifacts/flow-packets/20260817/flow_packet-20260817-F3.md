```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: flow_packet
  gate: G2
  packet_id: flow-packet-20260817-F3
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: complete
  target_surface: none
  expected_action: "After G2 confirmation, execute F3 and return a raw flow dump or skip marker."
  sources: [artifacts/next-day-plans/next_day_plan-20260817.md, apex-meta/epics/apex-kb-evolution/001.md]
  authority: {state: candidate, basis_digest: null, verification_ref: null}
  operator_validation: not_requested
```

# F3 — Apex

```yaml
flow_packet:
  packet_id: flow_packet_20260817_F3
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
    source_refs: [apex-meta/epics/apex-kb-evolution/001.md]
  flow_identity: {flow_id: F3, flow_slot: F3, project: Apex, flow_role: orchestration_system_buildout, flow_status: planned, default_flow: true}
  flow_context_summary:
    operator_intent_summary: "Advance Apex as an equal primary W34 category."
    project_state_summary: "Task apex-kb-evolution:001 is dependency-clear and high priority."
    weekly_plan_alignment: aligned
    source_context_refs: [artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md, apex-meta/epics/apex-kb-evolution/001.md]
    constraints: ["Use current main as truth; July handovers may be historical evidence only."]
    assumptions: []
    unresolved_inputs: []
  workflow_process_labels: {workflow_stage: audit, process_stage: current_state_rebaseline, expected_output_type: implementation_baseline, validation_source: inferred_from_context, fit_status: operator_review_recommended}
  flow_sprint_plan:
    sprint_policy: default_three_sprints
    sprint_count: 3
    recap_digest_required: true
    sprints:
      - {sprint_id: S1, sprint_role: first_work_sprint, sprint_goal: "Inventory current ApexKB CLI surface, installed skill contract, lifecycle states/gates, and KB roots from current main.", expected_output_type: implementation_inventory, prompt_sequence_ref: F3-S1, capture_focus: [source_context_used, artifact_created, blocker_found], completion_marker: not_started, validation_status: operator_review_recommended}
      - {sprint_id: S2, sprint_role: second_work_or_deepening_sprint, sprint_goal: "Verify retrieval architecture and semantic-acceptance behavior; classify previously listed residual risks as present/fixed/superseded.", expected_output_type: verification_matrix, prompt_sequence_ref: F3-S2, capture_focus: [decision_made, source_context_used, unresolved_question], completion_marker: not_started, validation_status: operator_review_recommended}
      - {sprint_id: S3, sprint_role: recap_digest_preparation_sprint, sprint_goal: "Assemble the current-state ApexKB baseline with representative completed KBs and unresolved risks.", expected_output_type: implementation_baseline, prompt_sequence_ref: F3-S3, capture_focus: [artifact_created, next_step_guess, unresolved_question], completion_marker: not_started, validation_status: operator_review_recommended}
  prompt_pack_ref: {flow_prompt_pack_path: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F3.md, prompt_pack_status: operator_review_recommended, prompt_pack_authority: precap-next-day}
  usage_tracking_refs: {status: missing_dependency}
  flow_execution_capture_preparation: {raw_flow_dump_template_ref: "# Raw Flow Dump Template", skipped_flow_marker_template_ref: "# Skipped Flow Marker Template", capture_status: prepared}
  FlowRecap_handoff_block: {source_flow_id: F3, expected_evidence: [implementation_inventory, verification_matrix, implementation_baseline], recap_status: pending_execution}
  operator_review_flags: ["G2 approval required before execution."]
  validation_status: operator_review_recommended
```

## Raw Flow Dump Template
- Current-main sources inspected:
- Verified behavior:
- Residual-risk disposition:
- Baseline artifact/result:
- Suggested next step:

## Skipped Flow Marker Template
- flow_id: F3
- status: skipped
- reason:

## FlowRecap Handoff
Consume with normalized F3 evidence; distinguish verified current-main facts from historical handover claims.
