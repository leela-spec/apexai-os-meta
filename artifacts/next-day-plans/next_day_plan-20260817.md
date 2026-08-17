```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: next_day_plan
  gate: G2
  packet_id: next-day-plan-20260817
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: partial
  target_surface: none
  next_state: "If the operator confirms G2, the represented Monday flows may be executed and returned as raw flow evidence."
  prerequisites:
    - artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md
    - artifacts/weekly-plans/project-status-overview-20260816.md
    - apex-meta/handoff/planning-feed-20260816-w34.md
    - apex-meta/handoff/sync-reports/20260816-w34/next.json
    - apex-meta/handoff/sync-reports/20260816-w34/blockers.json
  expected_action: "Operator confirms or revises G2; after confirmation, execute approved flows and return raw dumps or skip markers."
  sources:
    - artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md
    - apex-meta/handoff/sync-reports/20260816-w34/next.json
    - apex-meta/epics/leela-core-interaction-development/001.md
    - apex-meta/epics/masterofarts-website-definition/001.md
    - apex-meta/epics/apex-kb-evolution/001.md
    - apex-meta/epics/investment-intelligence-automation/001.md
  uncertainties:
    - "Monday calendar constraints were not supplied and no calendar was queried."
    - "Dating has no reserved Monday allocation."
    - "Investment requires operator-specific input before a branch contract can be completed."
    - "PromptEngineer, AI routing, and workflow-process dependencies were not invoked; prompt packs use degraded generic placeholders."
  unresolved_risk: "The four-flow plan is not time-feasible until actual Monday availability is checked; flow order and count remain operator-selectable."
  stop_condition: "Stop at G2. Do not execute project work, normalize evidence, run FlowRecap, status merge, Session mutation, or calendar writes before G2 confirmation."
  authority:
    state: candidate
    basis_digest: null
    verification_ref: null
  operator_validation: not_requested
```

# PreCap Next Day — Monday 2026-08-17

```yaml
next_day_plan:
  plan_id: next_day_plan_2026_08_17_w34_monday
  artifact_name: next_day_plan
  created_or_updated_at: "2026-08-17"
  execution_day: "2026-08-17"
  generation_mode: standard_mode
  review_status: operator_review_recommended

  daily_plan_metadata:
    plan_title: "PreCap Next Day Plan — 2026-08-17"
    plan_role: resilient_daily_orchestration_plan
    operator_intent_status: inferred_from_context
    source_context_status: partial
    input_resilience_mode: degraded_context_mode
    fixed_flow_policy:
      default_flows_required: true
      compression_allowed: true
      omission_allowed: true
      omission_requires_reason: true
    sprint_policy:
      default_sprints_per_flow: 3
      compressed_sprints_allowed: true
      recap_digest_sprint_expected: true

  daily_plan_context_summary:
    used_inputs:
      - weekly_plan_packet
      - precap_week_output
      - current_project_status_overview
      - detailed_project_state_files
    missing_inputs:
      - fixed_calendar_constraints
      - calendar_events
      - operator_day_intent
      - model_usage_summary
      - AI_surface_inventory
    assumptions:
      - "Use the G1-approved eight-hour/four-flow baseline only as a planning envelope, not a promise of available time."
      - "Use the first dependency-clear task aligned with the approved weekly direction for Leela, MasterOfArts, and Apex."
      - "Override default F4 Residual with Investment because G1 confirms Investment as a primary daily category."
    degraded_mode_reasons:
      - "Calendar context is unavailable."
      - "Prompt/routing/workflow dependencies are not materialized for this G2 candidate."
    day_constraints:
      - "No fixed flow times may be asserted until actual Monday availability is checked."
      - "Each flow may be compressed or skipped if real capacity is lower than the weekly baseline."
      - "Investment execution begins by collecting operator-specific inputs rather than fabricating them."
    planning_conflicts: []

  daily_flow_overview:
    flow_count: 4
    flows:
      - flow_id: F1
        project: Leela
        flow_role: app_product_or_system_work
        flow_status: planned
        sprint_count: 3
        primary_goal: "Verify SCR_Home_Today runtime against the current Home screen contract and produce an evidence-backed conformance report."
        expected_outputs:
          - "Home runtime conformance observations"
          - "Gap classification: keep/repair/mock-prototype debt/obsolete/deferred"
        workflow_process_labels:
          workflow_stage: verification
          process_stage: evidence_collection_and_gap_classification
          expected_output_type: conformance_report
          validation_status: operator_review_recommended
        file_refs:
          flow_packet_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F1.md
          flow_prompt_pack_ref: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F1.md
          raw_flow_dump_template_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F1.md#raw-flow-dump-template
          skipped_flow_marker_template_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F1.md#skipped-flow-marker-template
          FlowRecap_handoff_block_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F1.md#flowrecap-handoff
        review_flags: []
      - flow_id: F2
        project: MasterOfArts
        flow_role: coaching_business_website_offer_content_work
        flow_status: planned
        sprint_count: 3
        primary_goal: "Locate the current website-definition sources, identify conflicting variants, and designate the continuation baseline without inventing prior decisions."
        expected_outputs:
          - "Website-definition source inventory"
          - "Explicit continuation baseline and source paths"
        workflow_process_labels:
          workflow_stage: discovery
          process_stage: source_reconciliation
          expected_output_type: baseline_record
          validation_status: operator_review_recommended
        file_refs:
          flow_packet_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F2.md
          flow_prompt_pack_ref: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F2.md
          raw_flow_dump_template_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F2.md#raw-flow-dump-template
          skipped_flow_marker_template_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F2.md#skipped-flow-marker-template
          FlowRecap_handoff_block_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F2.md#flowrecap-handoff
        review_flags: []
      - flow_id: F3
        project: Apex
        flow_role: orchestration_system_buildout
        flow_status: planned
        sprint_count: 3
        primary_goal: "Re-baseline the current ApexKB implementation and contract from current main, including lifecycle, retrieval architecture, semantic acceptance, residual risks, and representative KB roots."
        expected_outputs:
          - "Current-state ApexKB baseline"
          - "Residual-risk disposition"
        workflow_process_labels:
          workflow_stage: audit
          process_stage: current_state_rebaseline
          expected_output_type: implementation_baseline
          validation_status: operator_review_recommended
        file_refs:
          flow_packet_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F3.md
          flow_prompt_pack_ref: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F3.md
          raw_flow_dump_template_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F3.md#raw-flow-dump-template
          skipped_flow_marker_template_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F3.md#skipped-flow-marker-template
          FlowRecap_handoff_block_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F3.md#flowrecap-handoff
        review_flags: []
      - flow_id: F4
        project: Investment
        flow_role: investment_review_or_reactivation
        flow_status: planned
        sprint_count: 2
        primary_goal: "Choose one of the three equal Investment branches for Monday and collect the operator-specific input required to clear that branch's starting blocker; if video discovery is chosen, define its search topics/sources/time window/relevance rules."
        expected_outputs:
          - "Selected Investment branch"
          - "Operator-supplied branch inputs"
          - "A self-contained starting contract if enough input is supplied"
        workflow_process_labels:
          workflow_stage: intake
          process_stage: operator_input_acquisition
          expected_output_type: clarified_input_contract
          validation_status: operator_review_recommended
        file_refs:
          flow_packet_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F4.md
          flow_prompt_pack_ref: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F4.md
          raw_flow_dump_template_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F4.md#raw-flow-dump-template
          skipped_flow_marker_template_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F4.md#skipped-flow-marker-template
          FlowRecap_handoff_block_ref: artifacts/flow-packets/20260817/flow_packet-20260817-F4.md#flowrecap-handoff
        review_flags:
          - "Operator must choose the Investment branch and provide its required inputs during execution."
    omitted_flows: []
    compressed_flows: [F4]
    residual_policy: omitted_with_reason

  generated_file_index:
    day_plan_ref: artifacts/next-day-plans/next_day_plan-20260817.md
    generated_file_count: 9
    generated_or_defined_files:
      - {artifact_name: next_day_plan, artifact_role: day_plan, logical_path: artifacts/next-day-plans/next_day_plan-20260817.md, production_status: created}
      - {artifact_name: flow_packet, artifact_role: F1, logical_path: artifacts/flow-packets/20260817/flow_packet-20260817-F1.md, production_status: created}
      - {artifact_name: flow_prompt_pack, artifact_role: F1, logical_path: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F1.md, production_status: created}
      - {artifact_name: flow_packet, artifact_role: F2, logical_path: artifacts/flow-packets/20260817/flow_packet-20260817-F2.md, production_status: created}
      - {artifact_name: flow_prompt_pack, artifact_role: F2, logical_path: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F2.md, production_status: created}
      - {artifact_name: flow_packet, artifact_role: F3, logical_path: artifacts/flow-packets/20260817/flow_packet-20260817-F3.md, production_status: created}
      - {artifact_name: flow_prompt_pack, artifact_role: F3, logical_path: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F3.md, production_status: created}
      - {artifact_name: flow_packet, artifact_role: F4, logical_path: artifacts/flow-packets/20260817/flow_packet-20260817-F4.md, production_status: created}
      - {artifact_name: flow_prompt_pack, artifact_role: F4, logical_path: artifacts/flow-packets/20260817/prompt-packs/flow_prompt_pack-20260817-F4.md, production_status: created}
    files_requiring_operator_action:
      - {artifact_name: next_day_plan, action_needed: approve, reason: "G2 approval required before execution."}
      - {artifact_name: F4_Investment, action_needed: supply_missing_input, reason: "Branch choice and branch-specific operator input are required."}

  usage_tracking_summary:
    usage_plan_status: missing_dependency
    routing_recommendation_status: missing_dependency
    scarce_surface_use_policy: unknown_quota_operator_review
    usage_tracking_tags_present: false

  FlowRecap_preparation_summary:
    status: prepared
    notes:
      - "Each flow packet contains raw-flow-dump and skipped-flow-marker preparation plus a FlowRecap handoff block."
      - "FlowRecap must not run until actual execution evidence or a skip marker exists."

  day_level_operator_review_flags:
    status: operator_review_recommended
    flags:
      - "Confirm Monday plan and feasible flow count/order."
      - "Calendar availability remains unverified."
      - "Confirm F4 Investment override and select the branch during execution."
      - "Prompt packs use degraded generic prompt placeholders until prompt-engineering/routing dependencies are materialized."

  day_level_completion_gate:
    next_day_plan_exists: true
    fixed_flows_represented: true
    represented_flows_have_packet_refs: true
    represented_flows_have_prompt_pack_refs: true
    FlowRecap_handoff_prepared: true
    calendar_writes_completed: false
    project_execution_completed: false
    operator_G2_confirmation_required: true

  validation_status: operator_review_recommended
```

## G2 Approval Question

Approve this Monday 2026-08-17 plan for execution, or name the exact revision required. Approval authorizes only the represented flows; it does not authorize calendar writes, FlowRecap conclusions, status merge, or canonical Session mutation.
