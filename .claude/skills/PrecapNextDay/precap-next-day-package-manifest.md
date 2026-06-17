# FILE: .claude/skills/PrecapNextDay/precap-next-day-package-manifest.md

# PreCap Next Day Package Manifest

```yaml
package_manifest:
  package_name: precap-next-day
  package_path_actual: ".claude/skills/PrecapNextDay/"
  package_path_canonical_target: ".claude/skills/precap-next-day/"
  package_role: resilient_daily_orchestration_compiler
  primary_artifact: next_day_plan
  read_when:
    - operator_inspects_package_structure
    - validating_package_files

  file_list:
    - path: ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
      purpose: "Current skill entrypoint file in repo; later normalization to SKILL.md is pending."
      read_when: "skill_invocation_or_entrypoint_review"
    - path: ".claude/skills/PrecapNextDay/references/input-intake-and-resilience-contract.md"
      purpose: "Input availability, degraded modes, bootstrap behavior, and missing-context handling."
      read_when: "validating_input_resilience_or_missing_inputs"
    - path: ".claude/skills/PrecapNextDay/references/daily-plan-output-contract.md"
      purpose: "next_day_plan structure, fixed flow layout, review status, and generated-file index."
      read_when: "creating_or_validating_next_day_plan"
    - path: ".claude/skills/PrecapNextDay/references/flow-packet-contract.md"
      purpose: "Per-flow packet structure, sprint plan, raw-dump preparation, and FlowRecap handoff."
      read_when: "creating_flow_packets_or_recap_handoffs"
    - path: ".claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md"
      purpose: "Per-flow prompt pack structure and prompt execution packet bridge."
      read_when: "creating_flow_prompt_packs_or_prompt_execution_packets"
    - path: ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md"
      purpose: "Interface for consuming prompt-engineering outputs without owning prompt doctrine."
      read_when: "provider_prompting_or_prompt_quality_dependency_needed"
    - path: ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
      purpose: "Interface for consuming routing, quota, usage-budget, and usage-tag outputs."
      read_when: "planning_AI_usage_or_applying_usage_tracking"
    - path: ".claude/skills/PrecapNextDay/references/calendar-event-write-contract.md"
      purpose: "Workflow-block calendar write requests, approval gate, and write boundaries."
      read_when: "calendar_workflow_blocks_are_requested_or_available"
    - path: ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md"
      purpose: "Interface for consuming workflow/process validation without owning taxonomies."
      read_when: "validating_prompt_flow_or_sprint_process_fit"
    - path: ".claude/skills/PrecapNextDay/references/validation-checklist.md"
      purpose: "Package-level output validation checks and drift-prevention gates."
      read_when: "final_validation_or_operator_review_needed"
    - path: ".claude/skills/PrecapNextDay/references/operator-output-format-design.md"
      purpose: "Template derivation workflow, dashboard conventions, APEX-only example policy, and roundtrip test method."
      read_when: "creating_or_reviewing_operator_output_templates"

    - path: ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md"
      purpose: "Main operator dashboard template for next_day_plan outputs."
      read_when: "creating_next_day_plan_dashboard"
    - path: ".claude/skills/PrecapNextDay/templates/flow-packet-template.md"
      purpose: "Blank per-flow packet template."
      read_when: "creating_flow_packet_output"
    - path: ".claude/skills/PrecapNextDay/templates/flow-prompt-pack-template.md"
      purpose: "Blank per-flow prompt pack template with prompt placeholders and refs."
      read_when: "creating_flow_prompt_pack_output"
    - path: ".claude/skills/PrecapNextDay/templates/capture-and-handoff-template.md"
      purpose: "Capture and FlowRecap handoff preparation template."
      read_when: "preparing_capture_or_handoff"
    - path: ".claude/skills/PrecapNextDay/templates/calendar-event-write-request-template.md"
      purpose: "Reviewable calendar workflow-block request template."
      read_when: "preparing_calendar_write_request_review"
    - path: ".claude/skills/PrecapNextDay/templates/usage-tracking-summary-template.md"
      purpose: "Lightweight usage tracking summary and capture preparation template."
      read_when: "preparing_usage_tracking_summary"

    - path: ".claude/skills/PrecapNextDay/examples/apex-only-template-example/next-day-plan.md"
      purpose: "Filled APEX-only next_day_plan example."
      read_when: "reviewing_APEX_only_example"
    - path: ".claude/skills/PrecapNextDay/examples/apex-only-template-example/flows/"
      purpose: "Filled APEX-only F1-F4 flow packet examples."
      read_when: "reviewing_flow_packet_examples"
    - path: ".claude/skills/PrecapNextDay/examples/apex-only-template-example/prompts/"
      purpose: "Filled APEX-only F1-F4 flow prompt pack examples."
      read_when: "reviewing_prompt_pack_examples"
    - path: ".claude/skills/PrecapNextDay/examples/apex-only-template-example/capture/raw-flow-dump-template.md"
      purpose: "Prepared raw-flow capture fixture for future execution capture."
      read_when: "reviewing_capture_fixture"
    - path: ".claude/skills/PrecapNextDay/examples/apex-only-template-example/calendar/calendar-event-write-request.md"
      purpose: "Review-only calendar write request example with no actual calendar mutation."
      read_when: "reviewing_calendar_request_example"
    - path: ".claude/skills/PrecapNextDay/examples/apex-only-template-example/usage/usage-tracking-summary.md"
      purpose: "Degraded usage tracking summary example."
      read_when: "reviewing_usage_tracking_example"
    - path: ".claude/skills/PrecapNextDay/examples/apex-only-template-example/handoff/FlowRecap-handoff.md"
      purpose: "Prepared FlowRecap handoff example; FlowRecap not run."
      read_when: "reviewing_FlowRecap_handoff_example"
    - path: ".claude/skills/PrecapNextDay/examples/apex-only-template-example/handoff/template-layer-final-audit-summary.md"
      purpose: "Draft audit summary and open decision list for critique."
      read_when: "reviewing_template_layer_audit"

  package_boundaries:
    must_not_create:
      - project_execution
      - FlowRecap_output
      - project_status_merge
      - non_workflow_calendar_blocks
      - final_OpenRouter_model_map
      - API_frontier_model_default_daily_engine
```

Note: this manifest reflects the repo's current CamelCase package path. A later package-normalization pass can move files to the canonical lowercase path and rename the entrypoint to `SKILL.md`.
