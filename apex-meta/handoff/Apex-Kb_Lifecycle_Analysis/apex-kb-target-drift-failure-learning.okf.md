# Apex KB Target Drift Failure Learning

```okf
okf_document:
  id: apex_kb_target_drift_failure_learning_2026_07_06
  title: "Apex KB Target Drift Failure Learning"
  artifact_type: machine_readable_failure_learning
  created_at: "2026-07-06"
  target_folder: "apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/"
  intended_consumers:
    - future_chatgpt_apex_kb_sessions
    - apex_kb_index_builders
    - codex_prompt_orchestrators
    - apex_kb_process_maintainers
  token_policy:
    format: compact_okf_first
    redundancy_rule: do_not_repeat_existing_chat_drift_learning_unless_the_rule_is_narrower_or_stricter
    max_reader_action: apply_gates_before_reading_more_files
    purpose: prevent_guidance_bloat_that_confuses_future_llms

failure_event:
  name: handoff_folder_index_target_drift
  severity: critical
  date_detected: "2026-07-06"
  user_goal: >
    Create an Apex KB-style handoff folder index that helps future runs improve the
    Apex KB lifecycle process, including lifecycle learnings, failure modes,
    deterministic/LLM boundaries, Codex execution standards, high-impact tool
    inclusion, exclusions, and process upgrade direction.
  wrong_output_class: folder_inventory_router_disguised_as_lifecycle_index
  immediate_bad_result:
    - NARM/domain handoff files were read and ranked as high-priority read-first files.
    - Off-target domain continuation files polluted the Apex KB lifecycle index.
    - The same bad classification was duplicated across Markdown, OKF, and JSON outputs.
    - Machine-readable artifacts made the wrong routing more durable instead of stricter.
  correct_output_class: apex_kb_lifecycle_failure_and_upgrade_index

root_cause:
  primary: scope_priority_inversion
  explanation: >
    The assistant over-obeyed the instruction to read the folder and under-obeyed the
    actual mission: index only what improves the Apex KB lifecycle process. Folder
    membership was treated as evidence of relevance. That is false.
  contributing_causes:
    - id: folder_scope_overrode_task_scope
      description: >
        The assistant treated "read files in the folder" as "rank all folder files"
        instead of separating source-access from source-authority.
    - id: weak_relevance_gate
      description: >
        Files were tiered by apparent usefulness, but no hard gate asked whether a file
        directly improved Apex KB lifecycle design, execution, validation, retrieval,
        source custody, or process learning.
    - id: self_contradiction_not_blocked
      description: >
        The generated index said NARM files were not generic Apex KB authority, while
        also ranking them as read-first. The contradiction should have stopped the write.
    - id: machine_outputs_not_strict_enough
      description: >
        The OKF and JSON repeated prose judgments instead of enforcing stricter routing.
    - id: artifact_count_sprawl
      description: >
        Three generated files duplicated file lists, priorities, topics, and routes,
        increasing token waste and preserving the error in multiple places.
    - id: apex_kb_blueprint_not_applied
      description: >
        Apex KB principles were known but not operationalized: source custody was
        mistaken for semantic authority, deterministic inventory was mistaken for
        lifecycle synthesis, and a routing layer was mistaken for a final index.

hard_distinctions:
  source_access_vs_source_authority:
    rule: >
      Reading a file proves access only. It does not prove the file belongs in the
      primary answer or read-first set.
  folder_inventory_vs_task_index:
    rule: >
      A folder index may list every file, but a task-specific Apex KB lifecycle index
      must rank only files that serve the stated lifecycle target.
  domain_handoff_vs_process_handoff:
    rule: >
      Domain continuation files can be valid artifacts and still be excluded from the
      Apex KB lifecycle core.
  human_readable_vs_machine_readable:
    rule: >
      Machine-readable artifacts must be stricter and smaller than prose. They should
      encode clean decisions, not duplicate weak analysis.

mandatory_prewrite_gates:
  - id: mission_restated_as_filter
    question: "What exact decision or future action is this artifact supposed to improve?"
    required_answer_for_this_case: "Apex KB lifecycle improvement and failure prevention."
    fail_if: "The answer is only folder navigation, source inventory, or domain project continuation."
  - id: file_relevance_binary_gate
    question: "Does this file directly improve the target lifecycle process?"
    allowed_yes_reasons:
      - lifecycle_state_lock
      - deterministic_vs_llm_boundary
      - source_custody_or_manifest_integrity
      - codex_execution_standard
      - phase0_phase1_phase2_boundary
      - retrieval_query_lint_audit_process
      - high_impact_tool_inclusion_or_exclusion
      - documented_failure_pattern_or_repair
    fail_if: "The file is only domain content, a project-specific source list, or a session log unrelated to Apex KB lifecycle."
  - id: read_first_purity_gate
    question: "Are all read-first files directly relevant to the declared target?"
    pass_condition: "100 percent yes."
    fail_action: "Demote off-target files to appendix/domain_context/excluded_from_core before writing."
  - id: contradiction_gate
    question: "Does any prose statement contradict the machine-readable ranking?"
    fail_example: "Saying a file is not generic authority while ranking it read-first for generic lifecycle work."
    fail_action: "Do not write. Repair ranking first."
  - id: redundancy_gate
    question: "Does each generated file provide unique value?"
    pass_condition: "No repeated file list plus repeated topic map plus repeated priorities across multiple artifacts."
    fail_action: "Collapse to one human index plus one compact machine routing map, or one file only."
  - id: artifact_minimality_gate
    question: "Can the next LLM act correctly with fewer files or fewer repeated fields?"
    default_answer: "Yes, unless proven otherwise."
    fail_action: "Remove the extra artifact or convert it to metadata-only."

corrected_classification_policy:
  scope_classes:
    apex_kb_lifecycle_core:
      include_when:
        - file defines Apex KB lifecycle state or next patch target
        - file documents process drift, execution failure, or guardrail repair
        - file defines deterministic/semantic ownership, source custody, retrieval, lint, audit, or Codex execution standards
      eligible_for_read_first: true
    apex_kb_supporting_evidence:
      include_when:
        - file supports a lifecycle claim but is not the current authority
      eligible_for_read_first: conditional
    domain_project_context:
      include_when:
        - file concerns a specific KB domain such as NARM, Lika taxes, or another subject KB
        - file does not generalize to Apex KB lifecycle mechanics
      eligible_for_read_first: false
      placement: appendix_or_domain_route_only
    stale_or_contaminating:
      include_when:
        - file contains wrong execution assumptions, superseded branch policy, or task-specific false starts
      eligible_for_read_first: false
      placement: contamination_warning_only

corrected_output_design:
  preferred_file_count: 1_or_2
  if_one_file:
    path_pattern: "apex-kb-lifecycle-handoff-index.md"
    contents:
      - compact_machine_header
      - target_scope
      - read_first_lifecycle_files_only
      - excluded_domain_files
      - failure_modes
      - high_impact_tool_routes
      - next_run_rules
  if_two_files:
    human_index:
      purpose: detailed lifecycle synthesis
      must_not_duplicate: raw_file_ledger_fields
    machine_routing_map:
      purpose: compact routing decisions only
      must_not_duplicate: prose_explanations_or_long_key_claims
  discouraged:
    - markdown_index_plus_okf_plus_json_with_same_rankings
    - machine_files_that_repeat_prose
    - read_first_lists_with_domain_context_files

specific_repair_for_failed_handoff_index:
  demote_from_read_first:
    - narm-index-prep-handover.md
    - next-session.md
    - task_plan.md
    - findings.md
    - progress.md
  keep_as_domain_appendix:
    - narm-index-prep-handover.md
    - next-session.md
    - task_plan.md
    - findings.md
    - progress.md
  true_read_first_core:
    - apex-kb-chat-drift-learning.okf.md
    - apex-kb-v2-planning-handover.md
    - apex-kb-v2-source-payload-manifest-handover.md
    - Apex-KB_UpdatePlan.md
    - Apex KB Lifecycle Execution Audit.md
    - codex-old-agent-kb-execution-process-audit.md
  note: >
    The true core may live partly in project resources rather than the moved folder.
    If the task is Apex KB lifecycle improvement, expand beyond the folder after the
    initial folder-access check.

failure_prevention_algorithm:
  steps:
    - step: 1
      name: restate_mission_as_filter
      output: internal_only
    - step: 2
      name: inventory_sources
      output: file_list_with_scope_class
    - step: 3
      name: apply_binary_relevance_gate
      output: eligible_core_files_only
    - step: 4
      name: assign_read_first_only_to_core_files
      output: read_first_clean
    - step: 5
      name: place_off_target_files_in_appendix
      output: domain_context_or_excluded
    - step: 6
      name: run_contradiction_gate
      output: pass_or_repair
    - step: 7
      name: run_redundancy_gate
      output: minimal_file_plan
    - step: 8
      name: write_artifact
      output: one_or_two_nonredundant_files

llm_runtime_instruction:
  before_any_apex_kb_index_or_handoff:
    - "Do not let the file container define the target."
    - "Use the user's mission as the primary filter."
    - "Do not rank a file read-first unless it directly advances that mission."
    - "Treat off-target but valid files as appendix routes, not core authority."
    - "Machine-readable outputs must be smaller and stricter than prose."
    - "If a contradiction is visible before writing, stop and repair; do not persist it."

non_reopen_rules:
  - "Do not relitigate whether the prior output was wrong; this file records that it was wrong."
  - "Do not respond by adding more broad guardrail prose; enforce the binary gates above."
  - "Do not solve target drift by reading everything. Solve it by stricter relevance classification."
  - "Do not preserve bad rankings for completeness. Completeness belongs in inventory, not read-first."
  - "Do not create multiple machine files unless each has a non-overlapping consumer and field set."

success_criteria:
  - "Future Apex KB lifecycle indexes have zero domain-only files in read-first."
  - "Every read-first file has an explicit direct lifecycle relevance reason."
  - "Off-target files are still findable but cannot steer the process."
  - "Generated artifacts are not redundant across Markdown/OKF/JSON."
  - "The LLM can reconstruct the intended next action without rereading unrelated domain handoffs."
```
