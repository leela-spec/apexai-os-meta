# flow_packet-20260713-F3

```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: flow_packet
  gate: none
  packet_id: "flow_packet-20260713-F3"
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: complete
  target_surface: none
  next_state: "F3 (Apex) is executable as Monday's single-focus flow: fable-orchestrator full-loop verification plus simulation-record capture, with raw-dump capture prepared for FlowRecap."
  prerequisites:
    - artifacts/next-day-plans/next_day_plan-20260713.md
  expected_action: operator executes F3 sprints, fills the raw flow dump, then dispatches normalize + FlowRecap for this flow independently
  sources:
    - artifacts/weekly-plans/weekly_plan_packet-20260712-2026-W29.md
  uncertainties:
    - "Fable-orchestrator completion claims are unverified (no recap evidence exists yet) — verification may find open work."
    - "Prompt pack is degraded_generic_prompt_mode; prompts are generic scaffolds, not prompt-engineering packets."
  unresolved_risk: "If S1 verification fails hard, S2 simulation records may be blocked; capture the failure as evidence instead."
  stop_condition: "Halt flow if orchestrator components needed for verification are missing from the repo, or if operator overrides the day focus."
  authority:
    state: candidate
    basis_digest: null
    verification_ref: null
  operator_validation: not_requested
```

```yaml
flow_packet:
  packet_id: flow_packet_2026-07-13_F3
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
      - ai-routing-and-usage-tracking
      - status-merge_later
    source_refs:
      - artifacts/weekly-plans/weekly_plan_packet-20260712-2026-W29.md
    notes: "First cycle; independently dispatchable for parallel normalize/recap."

  flow_identity:
    flow_id: F3
    flow_slot: F3
    project: Apex
    flow_role: orchestration_system_buildout
    flow_status: planned
    default_flow: true

  flow_context_summary:
    operator_intent_summary: "Monday = fable-orchestrator full-loop verification + simulation records (per weekly packet Monday direction and dispatch intent)."
    project_state_summary: "state/apex-project-status.md is empty (bootstrap). Weekly intent claims fable-orchestrator is near closure; this flow produces the evidence to verify that claim. Closure completes Tuesday (target-log closure + regression-suite packet decision)."
    recap_carry_forward: []
    weekly_plan_alignment: aligned
    calendar_constraints_summary: "No calendar data; assumed-standard capacity, unverified."
    source_context_refs:
      - artifacts/weekly-plans/weekly_plan_packet-20260712-2026-W29.md
    constraints:
      - "Verify actual Monday availability before starting S1."
      - "Verification only — do not start Tuesday's target-log closure or regression-suite decision inside this flow."
    assumptions:
      - "Orchestrator components referenced by commit 26ed183e exist and are runnable/inspectable."
    unresolved_inputs:
      - current_project_status_overview
      - flow_recap_packets
      - calendar_events
    confidence_notes:
      - "Goal confidence high (direct operator intent); project-state confidence low (empty status file)."

  workflow_process_labels:
    workflow_stage: system_verification
    process_stage: execute_and_capture_evidence
    expected_output_type: verification_evidence_notes
    validation_source: inferred_from_context
    fit_status: operator_review_recommended
    mismatch_flags: []
    operator_review_note: "Labels inferred without workflow-process-design validation; confirm at review."

  flow_sprint_plan:
    sprint_policy: default_three_sprints
    sprint_count: 3
    recap_digest_required: true
    sprints:
      - sprint_id: S1
        sprint_role: first_work_sprint
        sprint_goal: "Run the fable-orchestrator full loop end-to-end (PreCapWeek → PreCapNextDay → execution capture → FlowRecap → status-merge dispatch path) in simulation and record pass/fail per stage handoff."
        expected_output_type: full_loop_verification_notes
        success_criteria:
          - "Each stage handoff attempted with an explicit pass/fail/blocked result."
          - "Envelope and gate behavior checked against handoff-schema.md."
        prompt_sequence_ref: flow_prompt_pack_2026-07-13_F3.S1
        capture_focus:
          - artifact_created
          - blocker_found
          - decision_made
          - source_context_used
        completion_marker: not_started
        validation_status: valid_with_warnings
      - sprint_id: S2
        sprint_role: second_work_or_deepening_sprint
        sprint_goal: "Capture simulation records: per-stage inputs/outputs, gate states, degraded-mode behavior, and any defects or gaps found in S1, filed as durable evidence for initiative closure."
        expected_output_type: simulation_records
        success_criteria:
          - "One record per simulated stage with evidence path references."
          - "Defect/gap list explicit (empty list is a valid result)."
        prompt_sequence_ref: flow_prompt_pack_2026-07-13_F3.S2
        capture_focus:
          - artifact_created
          - unresolved_question
          - decision_made
        completion_marker: not_started
        validation_status: valid_with_warnings
      - sprint_id: S3
        sprint_role: recap_digest_preparation_sprint
        sprint_goal: "Fill the raw flow dump: what was verified, records created, defects found, blockers, next-step guess toward Tuesday's target-log closure."
        expected_output_type: recap_digest_notes
        prompt_sequence_ref: flow_prompt_pack_2026-07-13_F3.S3
        capture_focus:
          - next_step_guess
          - model_usage
          - artifact_created
        completion_marker: not_started
        validation_status: valid

  prompt_pack_ref:
    flow_prompt_pack_path: artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F3.md
    prompt_pack_status: generic_degraded_mode
    prompt_pack_authority: references/flow-prompt-pack-contract.md
    prompt_engineering_dependency_status: missing_use_degraded_generic_prompt_mode
    note: "Kept minimal per dispatch (first cycle); review before execution."

  usage_tracking_refs:
    planned_usage_budget_ref: not_available_first_cycle
    usage_tracking_status: degraded_missing_usage_context
    expected_usage_capture_fields:
      - provider_used
      - surface_class_used
      - prompt_count
      - result_quality_signal
    note: "No AI surface inventory or usage summary supplied; no quota claims made. Capture actuals in the raw dump."

  flow_execution_capture_preparation:
    capture_status: prepared
    capture_instructions:
      - "Record each loop stage attempted and its pass/fail/blocked result."
      - "Record simulation-record file paths as they are created."
      - "Record defects, gaps, and any deviation from handoff-schema expectations."
      - "Record provider/surface actually used, if any AI was used."
      - "Record next-step guess for Tuesday (target-log closure readiness)."
    raw_flow_dump_template: see_raw_flow_dump_template_section
    skipped_flow_marker_template: see_skipped_flow_marker_template_section

  operator_review_flags:
    - workflow_labels_should_be_confirmed
    - prompt_pack_low_confidence
    - usage_planning_degraded

  validation_status: valid_with_warnings
```

## raw-flow-dump-template

```yaml
raw_flow_dump_template:
  template_id: raw_flow_dump_template_2026-07-13_F3
  flow_id: F3
  execution_day: "2026-07-13"
  completion_marker: not_started   # operator sets: done | partial | skipped | blocked
  operator_raw_notes: ""           # operator fills after work
  prompt_results: []               # operator fills after prompt execution
  artifacts_created: []            # operator fills: simulation record paths, verification notes
  decisions_made: []               # operator fills
  blockers: []                     # operator fills
  model_usage_notes: []            # operator fills when known
  next_step_guess: ""              # operator fills: readiness for Tuesday closure work
  recap_request: run_FlowRecap
```

## skipped-flow-marker-template

```yaml
skipped_flow_marker_template:
  marker_id: skipped_flow_marker_2026-07-13_F3
  flow_id: F3
  execution_day: "2026-07-13"
  skip_status: same_day_skip       # only if operator abandons the planned flow
  skip_reason: ""                  # operator fills
  carry_forward_policy: carry_forward_to_next_PreCapNextDay
  next_review_point: next_PreCapNextDay
```

## flowrecap-handoff-block

```yaml
FlowRecap_handoff_block:
  handoff_id: FlowRecap_handoff_2026-07-13_F3
  flow_packet_ref: artifacts/flow-packets/20260713/flow_packet-20260713-F3.md
  raw_flow_dump_expected: true
  skipped_flow_marker_allowed: true
  context_to_pass:
    - flow_identity
    - flow_context_summary
    - workflow_process_labels
    - flow_sprint_plan
    - prompt_pack_ref
    - usage_tracking_refs
    - raw_flow_dump_template
    - operator_review_flags
  required_operator_completion_marker: done
  FlowRecap_ready_status: ready_after_operator_execution
  boundary_note: "PreCapNextDay prepares this handoff but does not run FlowRecap or create FlowRecap output."
```
