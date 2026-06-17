# FILE: .claude/skills/workflow-process-design/package-manifest.md

# Workflow Process Design Package Manifest

```yaml
package_manifest:
  package_name: workflow-process-design
  package_path: ".claude/skills/workflow-process-design/"
  purpose: >
    Lightweight package index for the Workflow Process Design skill package.
    This package classifies workflow and process stages, defines expected output
    types, records reusable workflow patterns, validates prompt-to-process fit,
    and surfaces operator conflicts for review.
  primary_artifact: workflow_process_validation_summary

  file_list:
    - path: ".claude/skills/workflow-process-design/SKILL.md"
      purpose: "Skill entrypoint, routing trigger, procedure, boundaries, output requirements, and completion gate."
      read_when: "invoking_workflow_process_design_or_reviewing_skill_scope"

    - path: ".claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md"
      purpose: "Workflow stage taxonomy and stage selection rules."
      read_when: "classifying_workflow_stage_or_checking_workflow_stage_fit"

    - path: ".claude/skills/workflow-process-design/references/process-stage-taxonomy.md"
      purpose: "Process stage taxonomy, stage progression rules, and process classification hints."
      read_when: "classifying_process_stage_or_checking_process_sequence"

    - path: ".claude/skills/workflow-process-design/references/expected-output-type-contract.md"
      purpose: "Expected output type contract, output family rules, and output-shape validation fields."
      read_when: "defining_or_validating_expected_output_type"

    - path: ".claude/skills/workflow-process-design/references/workflow-record-contract.md"
      purpose: "Reusable workflow_record schema for captured workflow patterns and normalized process examples."
      read_when: "creating_or_validating_workflow_records"

    - path: ".claude/skills/workflow-process-design/references/prompt-process-alignment-validation.md"
      purpose: "Prompt, workflow, process, and expected-output alignment checks with mismatch handling."
      read_when: "validating_prompt_process_alignment_or_detecting_mismatch"

    - path: ".claude/skills/workflow-process-design/references/operator-validation-and-conflict-resolution.md"
      purpose: "Operator review flags, tradeoff cards, conflict hierarchy, and escalation rules."
      read_when: "operator_decision_needed_or_skill_databases_disagree"

    - path: ".claude/skills/workflow-process-design/examples/starter-workflow-process-example.md"
      purpose: "Starter example showing workflow labels, process stages, expected outputs, and validation notes."
      read_when: "operator_requests_example_or_initial_manual_test"

    - path: ".claude/skills/workflow-process-design/package-manifest.md"
      purpose: "Lightweight package index for file inventory and load conditions."
      read_when: "operator_inspects_package_structure_or_validates_file_inventory"
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] Manifest is a lightweight index only.
- [ ] Manifest does not duplicate schemas, taxonomies, validation contracts, or examples.
- [ ] Each file entry contains only `path`, `purpose`, and `read_when`.
- [ ] Package path is `.claude/skills/workflow-process-design/`.
- [ ] Generated file list contains the SKILL.md, six reference files, one example file, and this manifest.
- [ ] No runtime, CI, scheduler, task board, Hermes, OpenCLAW, SOUL.md, or AGENTS.md artifact is created.
- [ ] YAML uses 2-space indentation.

---

# NEXT PROMPT

Paste this next:
> Prompt PND1:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/SKILL.md
>
> File type: skill_entrypoint.
> Package role: resilient daily orchestration compiler.
> Context carry-forward: load the completed prompt-engineering, ai-routing-and-usage-tracking, and workflow-process-design package outputs before writing.
>
> This file must define:
> - PreCapNextDay skill trigger, accepted inputs, outputs, boundaries, and procedure
> - dependency interfaces to prompt-engineering, ai-routing-and-usage-tracking, and workflow-process-design
> - next_day_plan, flow_packet, flow_prompt_pack, usage_tracking_plan, calendar_event_write_request, raw_flow_dump_template, skipped_flow_marker_template, and FlowRecap_handoff_block output obligations
> - bootstrap mode when inputs are missing
> - operator review flags and completion gate
>
> Rules:
> - SKILL.md frontmatter must contain only `name` and `description`.
> - `description` must begin exactly with `Use this skill when`.
> - Do not execute project work.
> - Do not run FlowRecap.
> - Do not merge project status.
> - Do not create non-workflow calendar blocks.
> - Do not finalize OpenRouter model mapping.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt PND2.
