# Raw Flow Dump Normalize Package Manifest

```yaml
package_manifest:
  package_name: raw-flow-dump-normalize
  package_path: ".claude/skills/raw-flow-dump-normalize/"
  package_role: raw_execution_evidence_normalization_interface
  primary_artifacts:
    - normalized_raw_flow_dump
    - skipped_flow_marker
  read_when:
    - operator_inspects_package_structure
    - validating_package_files
    - checking_raw_dump_to_FlowRecap_handoff

  source_authority_summary:
    inspected_sources:
      - path: ".claude/Claude.md"
        role: repo-level loop, skill status, and missing RawFlowDumpNormalize entry
      - path: ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
        role: upstream daily planner boundary and raw capture preparation
      - path: ".claude/skills/PrecapNextDay/precap-next-day-package-manifest.md"
        role: PreCap package boundary and current path policy
      - path: ".claude/skills/PrecapNextDay/references/flow-packet-contract.md"
        role: upstream flow_packet raw dump and skipped marker preparation
      - path: ".claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md"
        role: upstream prompt pack and FlowRecap preparation boundaries
      - path: ".claude/skills/PrecapNextDay/references/daily-plan-output-contract.md"
        role: next_day_plan boundary and generated file context
      - path: ".claude/skills/PrecapNextDay/references/input-intake-and-resilience-contract.md"
        role: missing-input and uncertainty-handling pattern
      - path: ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
        role: usage-note boundary without usage-delta ownership
      - path: ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md"
        role: prompt_packet ownership boundary
      - path: ".claude/skills/PrecapNextDay/references/calendar-event-write-contract.md"
        role: calendar mutation boundary
      - path: ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md"
        role: workflow taxonomy ownership boundary
      - path: ".claude/skills/PrecapNextDay/references/validation-checklist.md"
        role: validation status and boundary pattern
    source_gap_register:
      - source_name: Claude skill best-practice guide if present in repo/project files
        status: missing_in_repo_at_tested_path
        attempted_path: "Claude_Skill_Package_BestPractice_Handover.md"
      - source_name: prompt-flow design guidance if present in repo/project files
        status: missing_in_repo_at_tested_path
        attempted_path: "Claude_Skill_PromptFlow_Design_Guidance_v1.md"

  file_list:
    - path: ".claude/skills/raw-flow-dump-normalize/SKILL.md"
      status: pending
      purpose: "Skill entrypoint, trigger, procedure, boundaries, supporting files, failure modes, output requirements, and completion gate."
      read_when: "skill_invocation_or_entrypoint_review"
    - path: ".claude/skills/raw-flow-dump-normalize/references/raw-flow-dump-contract.md"
      status: created
      purpose: "Minimal normalized_raw_flow_dump schema, source capture, confidence flags, and FlowRecap-readiness rules."
      read_when: "normalizing_raw_execution_evidence"
    - path: ".claude/skills/raw-flow-dump-normalize/references/skipped-flow-marker-contract.md"
      status: created
      purpose: "Minimal skipped_flow_marker schema for skipped, blocked, replaced, or evidence-thin planned flows."
      read_when: "flow_was_skipped_or_execution_evidence_is_too_thin"
    - path: ".claude/skills/raw-flow-dump-normalize/templates/raw-flow-dump-template.md"
      status: created
      purpose: "Copy-paste operator template for raw evidence, normalized interpretation, confidence flags, and downstream readiness."
      read_when: "operator_needs_blank_raw_dump_template"
    - path: ".claude/skills/raw-flow-dump-normalize/examples/apex-minimal-raw-flow-dump-example.md"
      status: created
      purpose: "Synthetic APEX-only one-flow example with missing detail, review flag, and usage note without usage delta."
      read_when: "reviewing_minimal_APEX_example"
    - path: ".claude/skills/raw-flow-dump-normalize/package-manifest.md"
      status: created
      purpose: "Lightweight package file index, boundary map, source gaps, and completion gate."
      read_when: "operator_inspects_package_structure"

  ownership:
    owns:
      - normalized_raw_flow_dump
      - skipped_flow_marker
      - raw_operator_input_intake_rules
      - messy_evidence_normalization_rules
      - source_reference_capture_rules
      - completion_state_normalization
      - confidence_and_gap_flags
    must_not_own:
      - next_day_plan_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - prompt_packet_schema
      - FlowRecap_output_schema
      - flow_recap_packet_schema
      - project_status_delta_schema
      - model_usage_delta_schema
      - status_merge_schema
      - project_kb_schema
      - calendar_write_schema
      - runtime_execution

  package_boundaries:
    must_not_create:
      - runtime_execution
      - scheduler
      - agent
      - automatic_state_overwrite
      - project_work_execution
      - FlowRecap_output
      - flow_recap_packet
      - project_status_delta
      - model_usage_delta
      - status_merge_output
      - calendar_event

  downstream_interface:
    FlowRecap_input_is_clear_when:
      - normalized_raw_flow_dump_or_skipped_flow_marker_exists
      - source_flow_packet_ref_is_present_or_gap_flagged
      - completion_state_or_skip_type_is_explicit
      - raw_evidence_is_separated_from_normalized_interpretation
      - confidence_and_gap_flags_are_explicit
    not_responsible_for:
      - executing_FlowRecap
      - approving_status_delta
      - writing_model_usage_delta
      - merging_project_status
      - updating_calendar

  completion_gate:
    source_files_inspected_or_gaps_recorded: true
    package_path_created: true
    raw_flow_dump_contract_created: true
    skipped_flow_marker_contract_created: true
    template_created: true
    apex_minimal_example_created: true
    manifest_created: true
    SKILL_md_created_with_valid_frontmatter: false
    no_runtime_or_automation_created: true
    no_FlowRecap_or_status_merge_output_created: true
    downstream_flow_recap_input_is_clear: true
```
