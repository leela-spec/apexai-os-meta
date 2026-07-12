# next_day_plan-20260713

```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: next_day_plan
  gate: G2
  packet_id: "next_day_plan-20260713-mon-fable-closure"
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: complete
  target_surface: none
  next_state: "Monday 2026-07-13 is planned as a single-focus Apex day: F3 runs fable-orchestrator full-loop verification and captures simulation records; F1, F2, F4 carry planned-skip markers ready for G3 evidence capture."
  prerequisites:
    - artifacts/weekly-plans/weekly_plan_packet-20260712-2026-W29.md
  expected_action: operator confirms G2, then executes flows and returns raw dumps
  sources:
    - artifacts/weekly-plans/weekly_plan_packet-20260712-2026-W29.md
    - state/apex-project-status.md
  uncertainties:
    - "state/apex-project-status.md is empty — project-state confidence is low; plan rests on the G1 weekly packet and dispatch intent only."
    - "No calendar data — Monday capacity assumed standard and unverified."
    - "Prompt packs are degraded_generic_prompt_mode (minimal, first cycle); no prompt-engineering prompt_packets were generated."
    - "Upstream weekly packet is operator_validation: not_requested (autonomous run); gates batch-present at run end."
  unresolved_risk: "Full-loop verification may surface orchestrator defects that consume the whole day; simulation-record capture (S2) is the first candidate to compress if so."
  stop_condition: "Operator must halt if the weekly packet is rejected at batch G1 review, if Monday capacity materially differs from assumed-standard, or if fable-orchestrator components required for verification are missing."
  authority:
    state: candidate
    basis_digest: null
    verification_ref: null
  operator_validation: not_requested
```

```yaml
next_day_plan:
  plan_id: next_day_plan_2026_07_13_mon_fable_closure
  artifact_name: next_day_plan
  created_or_updated_at: "2026-07-12"
  execution_day: "2026-07-13"
  generation_mode: standard_mode
  review_status: operator_review_recommended

  daily_plan_metadata:
    plan_title: "PreCap Next Day Plan — Monday 2026-07-13 (2026-W29)"
    plan_role: resilient_daily_orchestration_plan
    operator_intent_status: supplied
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
      - operator_day_intent
      - weekly_plan_packet
      - manual_operator_notes
    missing_inputs:
      - current_project_status_overview
      - flow_recap_packets
      - calendar_events
      - fixed_calendar_constraints
      - AI_surface_inventory
      - model_usage_summary
    assumptions:
      - "Monday has standard work capacity (weekly packet assumption, unverified — no calendar data)."
      - "Fable-orchestrator components claimed complete in the weekly intent exist and are verifiable."
      - "Single-focus day: weekly packet Monday direction names only Apex; F1/F2/F4 planned skips are correct."
    degraded_mode_reasons:
      - "state/apex-project-status.md is empty (bootstrap state); no confirmed prior project truth."
      - "First cycle — no flow_recap_packets or skip markers to carry forward."
      - "Prompt-engineering prompt_packets not generated; prompt packs run in degraded_generic_prompt_mode."
      - "No AI surface inventory or usage summary; usage tracking hooks are generic."
    day_constraints:
      - "Verify actual Monday availability before starting F3 S1 (weekly packet starting constraint)."
    planning_conflicts: []

  daily_flow_overview:
    flow_count: 4
    residual_policy: omitted_with_reason
    omitted_flows: []
    compressed_flows: []
    flows:
      - flow_id: F1
        project: Leela
        flow_role: app_product_or_system_work
        flow_status: planned
        sprint_count: 0
        primary_goal: "Planned skip — maintenance week per weekly plan; no Leela push on Monday."
        expected_outputs:
          - skipped_flow_marker
        workflow_process_labels:
          workflow_stage: maintenance_hold
          process_stage: skip_capture
          expected_output_type: skipped_flow_marker
          validation_status: valid_with_warnings
        file_refs:
          flow_packet_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F1.md"
          flow_prompt_pack_ref: "artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F1.md"
          raw_flow_dump_template_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F1.md#raw-flow-dump-template"
          skipped_flow_marker_template_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F1.md#skipped-flow-marker-template"
          FlowRecap_handoff_block_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F1.md#flowrecap-handoff-block"
        review_flags:
          - planned_skip_confirm_maintenance_hold
        note: "flow_status planned refers to the skip being planned; flow packet carries flow_status: skipped (planned_skip)."
      - flow_id: F2
        project: MasterOfArts
        flow_role: coaching_business_website_offer_content_work
        flow_status: planned
        sprint_count: 0
        primary_goal: "Planned skip — maintenance week per weekly plan; no MasterOfArts push on Monday."
        expected_outputs:
          - skipped_flow_marker
        workflow_process_labels:
          workflow_stage: maintenance_hold
          process_stage: skip_capture
          expected_output_type: skipped_flow_marker
          validation_status: valid_with_warnings
        file_refs:
          flow_packet_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F2.md"
          flow_prompt_pack_ref: "artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F2.md"
          raw_flow_dump_template_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F2.md#raw-flow-dump-template"
          skipped_flow_marker_template_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F2.md#skipped-flow-marker-template"
          FlowRecap_handoff_block_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F2.md#flowrecap-handoff-block"
        review_flags:
          - planned_skip_confirm_maintenance_hold
        note: "flow_status planned refers to the skip being planned; flow packet carries flow_status: skipped (planned_skip)."
      - flow_id: F3
        project: Apex
        flow_role: orchestration_system_buildout
        flow_status: planned
        sprint_count: 3
        primary_goal: "Run fable-orchestrator full-loop verification and capture simulation records as durable evidence toward initiative closure."
        expected_outputs:
          - full_loop_verification_notes
          - simulation_records
          - defect_or_gap_list
          - recap_digest_notes
        workflow_process_labels:
          workflow_stage: system_verification
          process_stage: execute_and_capture_evidence
          expected_output_type: verification_evidence_notes
          validation_status: operator_review_recommended
        file_refs:
          flow_packet_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F3.md"
          flow_prompt_pack_ref: "artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F3.md"
          raw_flow_dump_template_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F3.md#raw-flow-dump-template"
          skipped_flow_marker_template_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F3.md#skipped-flow-marker-template"
          FlowRecap_handoff_block_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F3.md#flowrecap-handoff-block"
        review_flags:
          - prompt_pack_low_confidence
          - workflow_process_alignment_warning
      - flow_id: F4
        project: Residual
        flow_role: overflow_recovery_lagging_threads_cross_project_cleanup
        flow_status: planned
        sprint_count: 0
        primary_goal: "Planned skip — weekly plan defers Residual on Monday to protect single-focus orchestrator verification; overflow absorbs Friday."
        expected_outputs:
          - skipped_flow_marker
        workflow_process_labels:
          workflow_stage: deferred_overflow
          process_stage: skip_capture
          expected_output_type: skipped_flow_marker
          validation_status: valid_with_warnings
        file_refs:
          flow_packet_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F4.md"
          flow_prompt_pack_ref: "artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F4.md"
          raw_flow_dump_template_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F4.md#raw-flow-dump-template"
          skipped_flow_marker_template_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F4.md#skipped-flow-marker-template"
          FlowRecap_handoff_block_ref: "artifacts/flow-packets/20260713/flow_packet-20260713-F4.md#flowrecap-handoff-block"
        review_flags:
          - planned_skip_confirm_deferral
        note: "flow_status planned refers to the skip being planned; flow packet carries flow_status: skipped (planned_skip)."

  generated_file_index:
    day_plan_ref: "artifacts/next-day-plans/next_day_plan-20260713.md"
    generated_file_count: 9
    generated_or_defined_files:
      - artifact_name: next_day_plan
        artifact_role: day_level_plan
        logical_path: "artifacts/next-day-plans/next_day_plan-20260713.md"
        production_status: created
        validation_status: valid_with_warnings
      - artifact_name: flow_packet
        artifact_role: F1_skipped_flow_container
        logical_path: "artifacts/flow-packets/20260713/flow_packet-20260713-F1.md"
        production_status: created
        validation_status: valid_with_warnings
      - artifact_name: flow_packet
        artifact_role: F2_skipped_flow_container
        logical_path: "artifacts/flow-packets/20260713/flow_packet-20260713-F2.md"
        production_status: created
        validation_status: valid_with_warnings
      - artifact_name: flow_packet
        artifact_role: F3_primary_work_container
        logical_path: "artifacts/flow-packets/20260713/flow_packet-20260713-F3.md"
        production_status: created
        validation_status: operator_review_recommended
      - artifact_name: flow_packet
        artifact_role: F4_skipped_flow_container
        logical_path: "artifacts/flow-packets/20260713/flow_packet-20260713-F4.md"
        production_status: created
        validation_status: valid_with_warnings
      - artifact_name: flow_prompt_pack
        artifact_role: F1_skip_stub_pack
        logical_path: "artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F1.md"
        production_status: created
        validation_status: valid_with_warnings
      - artifact_name: flow_prompt_pack
        artifact_role: F2_skip_stub_pack
        logical_path: "artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F2.md"
        production_status: created
        validation_status: valid_with_warnings
      - artifact_name: flow_prompt_pack
        artifact_role: F3_primary_prompt_pack_degraded_generic
        logical_path: "artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F3.md"
        production_status: created
        validation_status: low_confidence_auto_generated
      - artifact_name: flow_prompt_pack
        artifact_role: F4_skip_stub_pack
        logical_path: "artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F4.md"
        production_status: created
        validation_status: valid_with_warnings
    files_requiring_operator_action:
      - artifact_name: next_day_plan
        action_needed: approve
        reason: "G2 confirmation (batch-presented at run end per autonomous override); calendar capacity unverified."
      - artifact_name: flow_packet
        action_needed: execute_flow
        reason: "F3 is the day's single execution target; return the raw flow dump after execution."
      - artifact_name: flow_prompt_pack
        action_needed: edit
        reason: "F3 pack is degraded_generic_prompt_mode; review prompts before execution."
      - artifact_name: skipped_flow_marker_template
        action_needed: skip_flow_with_marker
        reason: "Confirm F1/F2/F4 planned skips by filing their markers (or override and execute)."

  usage_tracking_summary:
    usage_plan_status: missing_dependency
    routing_recommendation_status: missing_dependency
    scarce_surface_use_policy: unknown_quota_operator_review
    usage_tracking_tags_present: true

  workflow_block_summary:
    calendar_mode: calendar_unavailable
    workflow_blocks_defined: false
    write_requests_present: false
    operator_acceptance_required: false
    write_policy_note: "No calendar write requests issued — no calendar context available; no basis for block proposals. Nothing was written to any calendar."

  FlowRecap_preparation_summary:
    raw_flow_dump_templates_present: true
    skipped_flow_marker_templates_present: true
    FlowRecap_handoff_blocks_present: true
    recap_capture_scope:
      - what_was_done
      - outputs_created
      - decisions_made
      - blockers
      - skipped_or_partial_work
      - prompt_results
      - usage_delta
      - next_step_guess
      - operator_validation_notes

  day_level_operator_review_flags:
    flags:
      - missing_project_status_context
      - missing_calendar_context
      - missing_AI_surface_inventory
      - missing_model_usage_summary
      - prompt_pack_low_confidence
      - compressed_flow_requires_approval
    review_required: true
    review_reason: "First-cycle plan built on the G1 weekly packet and dispatch intent only: empty project status, no calendar, degraded prompt/usage dependencies, and three planned skips need operator confirmation."

  day_level_completion_gate:
    next_day_plan_present: true
    each_active_flow_has_flow_packet_ref: true
    each_active_flow_has_prompt_pack_ref: true
    raw_flow_dump_capture_prepared: true
    skipped_flow_marker_capture_prepared: true
    FlowRecap_handoff_prepared: true
    operator_review_flags_present: true
    no_project_work_executed: true
    no_FlowRecap_run: true
    no_status_merge_run: true

  validation_status: valid_with_warnings
```
