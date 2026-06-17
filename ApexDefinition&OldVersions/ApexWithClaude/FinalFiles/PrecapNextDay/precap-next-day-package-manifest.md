# FILE: .claude/skills/precap-next-day/package-manifest.md

# PreCap Next Day Package Manifest

```yaml
package_manifest:
  package_name: precap-next-day
  package_path: ".claude/skills/precap-next-day/"
  package_role: resilient_daily_orchestration_compiler
  primary_artifact: next_day_plan
  read_when:
    - operator_inspects_package_structure
    - validating_package_files

  file_list:
    - path: ".claude/skills/precap-next-day/SKILL.md"
      purpose: "Skill entrypoint, trigger conditions, procedure, boundaries, and supporting-file map."
      read_when: "skill_invocation_or_entrypoint_review"
    - path: ".claude/skills/precap-next-day/references/input-intake-and-resilience-contract.md"
      purpose: "Input availability, degraded modes, bootstrap behavior, and missing-context handling."
      read_when: "validating_input_resilience_or_missing_inputs"
    - path: ".claude/skills/precap-next-day/references/daily-plan-output-contract.md"
      purpose: "next_day_plan structure, fixed flow layout, review status, and generated-file index."
      read_when: "creating_or_validating_next_day_plan"
    - path: ".claude/skills/precap-next-day/references/flow-packet-contract.md"
      purpose: "Per-flow packet structure, sprint plan, raw-dump preparation, and FlowRecap handoff."
      read_when: "creating_flow_packets_or_recap_handoffs"
    - path: ".claude/skills/precap-next-day/references/flow-prompt-pack-contract.md"
      purpose: "Per-flow prompt pack structure and prompt execution packet bridge."
      read_when: "creating_flow_prompt_packs_or_prompt_execution_packets"
    - path: ".claude/skills/precap-next-day/references/prompt-engineering-dependency-contract.md"
      purpose: "Interface for consuming prompt-engineering outputs without owning prompt doctrine."
      read_when: "provider_prompting_or_prompt_quality_dependency_needed"
    - path: ".claude/skills/precap-next-day/references/usage-tracking-dependency-contract.md"
      purpose: "Interface for consuming routing, quota, usage-budget, and usage-tag outputs."
      read_when: "planning_AI_usage_or_applying_usage_tracking"
    - path: ".claude/skills/precap-next-day/references/calendar-event-write-contract.md"
      purpose: "Workflow-block calendar write requests, approval gate, and write boundaries."
      read_when: "calendar_workflow_blocks_are_requested_or_available"
    - path: ".claude/skills/precap-next-day/references/workflow-process-validation-contract.md"
      purpose: "Interface for consuming workflow/process validation without owning taxonomies."
      read_when: "validating_prompt_flow_or_sprint_process_fit"
    - path: ".claude/skills/precap-next-day/references/validation-checklist.md"
      purpose: "Package-level output validation checks and drift-prevention gates."
      read_when: "final_validation_or_operator_review_needed"
    - path: ".claude/skills/precap-next-day/package-manifest.md"
      purpose: "Lightweight package index for file navigation and package inspection."
      read_when: "operator_inspects_package_structure"

  package_boundaries:
    must_not_create:
      - project_execution
      - FlowRecap_output
      - project_status_merge
      - non_workflow_calendar_blocks
      - final_OpenRouter_model_map
      - API_frontier_model_default_daily_engine
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] Manifest is a lightweight index, not a duplicate contract file.
- [ ] Every file entry uses only `path`, `purpose`, and `read_when`.
- [ ] No schemas, tests, validation roles, source names, citations, or old decision traces are embedded.
- [ ] Package boundaries prevent execution, FlowRecap, status merge, non-workflow calendar blocks, and final OpenRouter mapping.

---

# NEXT PROMPT

No next prompt. The `precap-next-day` package sequence is complete.
