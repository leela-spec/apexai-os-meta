# Prompt Engineering Package Manifest

```yaml
package_manifest:
  package_name: prompt-engineering
  package_path: ".claude/skills/prompt-engineering/"
  manifest_role: lightweight_package_index
  primary_output: final_copy_paste_prompt
  file_purpose_map: package_file_index_purpose_fields

  package_file_index:
    - { path: ".claude/skills/prompt-engineering/SKILL.md", purpose: "Entrypoint for prompt generation, validation, provider adaptation, and package boundaries.", read_when: [skill_invocation, entrypoint_review, support_navigation] }
    - { path: ".claude/skills/prompt-engineering/references/prompt-packet-contract.md", purpose: "Owns prompt packet, prompt sequence, and copy-paste prompt contracts.", read_when: [building_prompt_packet, validating_prompt_sequence, checking_prompt_body] }
    - { path: ".claude/skills/prompt-engineering/references/prompt-task-taxonomy.md", purpose: "Owns task taxonomy and task-to-prompt-pattern mapping.", read_when: [classifying_prompt_task, selecting_prompt_pattern, resolving_task_ambiguity] }
    - { path: ".claude/skills/prompt-engineering/references/iteration-loop-patterns.md", purpose: "Owns standard iteration loops, stop conditions, and loop red flags.", read_when: [selecting_iteration_loop, building_follow_up_sequence, diagnosing_loop_failure] }
    - { path: ".claude/skills/prompt-engineering/references/provider-style-contract-chatgpt.md", purpose: "Owns ChatGPT provider-style guidance for reasoning, research, and agent-run prompts.", read_when: [adapting_for_ChatGPT, writing_research_prompt, writing_agent_run_prompt] }
    - { path: ".claude/skills/prompt-engineering/references/provider-style-contract-claude.md", purpose: "Owns Claude provider-style guidance for file generation, skill packages, and structured documents.", read_when: [adapting_for_Claude, writing_file_generation_prompt, writing_skill_package_prompt] }
    - { path: ".claude/skills/prompt-engineering/references/provider-style-contract-gemini.md", purpose: "Owns Gemini provider-style guidance for long-context digestion and comparative synthesis.", read_when: [adapting_for_Gemini, handling_long_context, comparing_documents] }
    - { path: ".claude/skills/prompt-engineering/references/provider-style-contract-openrouter-todo.md", purpose: "Owns the OpenRouter placeholder boundary without final model mapping.", read_when: [noting_OpenRouter_later, avoiding_final_model_map, marking_API_placeholder] }
    - { path: ".claude/skills/prompt-engineering/references/prompt-quality-validation.md", purpose: "Owns prompt quality checks, workflow alignment checks, and failed-output examples.", read_when: [validating_prompt_quality, checking_workflow_alignment, diagnosing_failed_prompt] }
    - { path: ".claude/skills/prompt-engineering/references/prompt-learning-feedback-contract.md", purpose: "Owns lightweight prompt learning feedback and cross-package learning handoffs.", read_when: [capturing_prompt_feedback, learning_from_failed_output, feeding_dependency_skills] }
    - { path: ".claude/skills/prompt-engineering/examples/starter-prompt-pack-example.md", purpose: "Provides one compact realistic prompt-pack example for calibration.", read_when: [operator_requests_example, calibrating_prompt_pack, testing_package_behavior] }
    - { path: ".claude/skills/prompt-engineering/package-manifest.md", purpose: "Indexes package files, dependencies, boundaries, and acceptance checks.", read_when: [inspecting_package_structure, validating_file_inventory, reviewing_acceptance_checks] }

  dependency_map:
    upstream_optional:
      - workflow-process-design
      - ai-routing-and-usage-tracking
    downstream_consumers:
      - precap-next-day
      - workflow-process-design
      - ai-routing-and-usage-tracking
    integration_unit: prompt_packet

  package_boundaries:
    must_do:
      - "Generate finalized copy-paste prompts."
      - "Validate prompt quality and workflow alignment."
      - "Provide provider-aware prompt adaptation guidance."
    must_not_do:
      - "Do not create daily plans."
      - "Do not execute project work."
      - "Do not run FlowRecap."
      - "Do not merge project status."
      - "Do not finalize OpenRouter model mapping."
      - "Do not require machine-readable capture blocks inside every prompt."

  acceptance_checks:
    required_files_indexed: true
    manifest_is_index_not_contract: true
    read_when_conditions_present: true
    no_validation_role_field: true
    no_schema_blocks_duplicated: true
    package_boundaries_are_imperative: true
    dependency_map_present: true
```
