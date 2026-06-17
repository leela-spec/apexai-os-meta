---
class: kb_audit_v2_new_file_rewrite_process
role: SPECIAL_OPS_KB_AUDIT_V2_NEW_FILE_RETROFIT_CONTROLLER
surface: repo_process_pipeline
version: '1.0'
created_at: '2026-05-07'
last_validated_at: '2026-05-07'
context_mode: compact
status: active_for_restart
target_repo: leela-spec/MasterOfArts
target_branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows
candidate_output_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/rewrite_candidates
source_contracts:
  - AGENT_PIPELINE_CONTROLLER.md
  - KB_Audit_v2.md
target_model_min: gpt-4o
validated_against_model: gpt-5.5
max_active_rules: 12
supersedes_for_restart:
  - KB_AUDIT_V2_UPDATE_PIPELINE.md
  - KB_AUDIT_V2_PROMPT_PACKET_MODE.md
  - KB_AUDIT_V2_SCAFFOLD_REWRITE_PROCESS.md
  - patches/TASK-01_BEST_PRACTICES.patch.md
  - patches/TASK-02_MISTAKES.patch.md
  - patches/TASK-03_TEMPLATES.patch.md
  - patches/TASK-04_LEARNING_QUEUE.patch.md
  - patches/TASK-05_ESSENCE.patch.md
---

# KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS

```yaml
process_purpose:
  objective: >
    Restart the Special Ops Prompts Workflows scaffold retrofit using new complete
    replacement candidate files only. Do not create patch files. Do not mutate the
    original scaffold files. Each executor run writes one new candidate Markdown file
    that represents the proposed KB_Audit_v2-compliant replacement for one scaffold.
  correction_from_failed_runs:
    - prior_symbolic_patch_run_added_one_small_concept_per_file
    - prior_full_body_patch_run_kept_patch_transport_complexity_for_large_rewrites
    - patch_artifacts_became_the_work_instead_of_the_replacement_file
    - JSON_escape_and_large_patch_payload_handling_created avoidable execution risk
  desired_result: >
    Five readable replacement candidate files that can be inspected, compared, and
    applied later by the operator or a deterministic file replacement step.
```

---

## 1. Non-negotiable locks

```yaml
critical_locks:
  priority: critical
  rules:
    - id: NFL-01
      tier: critical
      rule: Use KB_Audit_v2.md as the structural writing standard for each scaffold file.
      prevents: symbolic concept integration without real machine-readability improvement
      evidence_refs: [KB_Audit_v2.md]
    - id: NFL-02
      tier: critical
      rule: Create complete new candidate files only; do not create .patch.md or .diff artifacts in this restart.
      prevents: patch transport complexity, escaped-payload failures, and patch-plan myopia
      evidence_refs: [operator_restart_instruction]
    - id: NFL-03
      tier: critical
      rule: Never mutate the original scaffold target during candidate generation.
      prevents: unreviewed scaffold replacement
      evidence_refs: [AGENT_PIPELINE_CONTROLLER.md]
    - id: NFL-04
      tier: critical
      rule: One executor prompt equals one target scaffold and one candidate output file.
      prevents: multi-file drift and cross-file contamination
      evidence_refs: [AGENT_PIPELINE_CONTROLLER.md]
    - id: NFL-05
      tier: critical
      rule: The controller emits a portable executor prompt; the executor writes the candidate file and returns a structured summary; the controller independently fetches back and validates.
      prevents: controller/executor role collapse and prose-only completion claims
      evidence_refs: [AGENT_PIPELINE_CONTROLLER.md]
    - id: NFL-06
      tier: critical
      rule: Candidate files must be complete replacement bodies, not partial snippets, not patch plans, and not commentary about possible changes.
      prevents: incomplete replacement artifacts
      evidence_refs: [KB_Audit_v2.md]
```

---

## 2. Target set

```yaml
target_set:
  scope: five_scaffold_files_only
  original_targets:
    - id: REWRITE-01
      source_file: BEST_PRACTICES.md
      candidate_file: rewrite_candidates/REWRITE-01_BEST_PRACTICES.v2.md
      target_role: accepted_practices_scaffold
    - id: REWRITE-02
      source_file: MISTAKES.md
      candidate_file: rewrite_candidates/REWRITE-02_MISTAKES.v2.md
      target_role: accepted_failure_patterns_scaffold
    - id: REWRITE-03
      source_file: TEMPLATES.md
      candidate_file: rewrite_candidates/REWRITE-03_TEMPLATES.v2.md
      target_role: reusable_templates_scaffold
    - id: REWRITE-04
      source_file: LEARNING_QUEUE.md
      candidate_file: rewrite_candidates/REWRITE-04_LEARNING_QUEUE.v2.md
      target_role: candidate_learning_queue_scaffold
    - id: REWRITE-05
      source_file: ESSENCE.md
      candidate_file: rewrite_candidates/REWRITE-05_ESSENCE.v2.md
      target_role: compact_activation_doctrine
  excluded:
    - appendices/*
    - NewResearchBecauseOfConstantFailure/*
    - patches/*
    - any original scaffold mutation
```

---

## 3. KB_Audit_v2 structural standard

```yaml
required_structural_standard:
  frontmatter:
    required: true
    required_fields:
      - class
      - role
      - surface
      - version
      - last_validated_at
      - context_mode
      - target_model_min
      - max_active_rules
      - status
      - owner
      - validator
  early_active_policy:
    required_within_first_500_tokens:
      - critical_rules_or_critical_path_yaml
      - file_contract_yaml
      - scope_boundary_yaml
  active_policy:
    format: parse_valid_yaml_first
    prose_budget_tokens: 100
    requirements:
      - stable_ids
      - tier_for_rule_like_entries
      - prevents_for_rule_like_entries
      - evidence_refs_for_rule_like_entries
      - schema_contracts_for_machine_consumed_outputs
      - duplicate_or_overlap_controls
      - explicit validation_or_promotion_boundary
  evidence_policy:
    rule: Keep long evidence, examples, and explanations in appendices; active scaffold carries refs and compact rules only.
  density_policy:
    rule: Prefer compact YAML registries and concise strings over Markdown prose lists.
```

---

## 4. File-specific rewrite objectives

```yaml
file_specific_rewrite_objectives:
  BEST_PRACTICES.md:
    must_become: frontmatter_plus_critical_path_plus_yaml_practice_registry
    preserve: PW-BP-001_through_PW-BP-011_semantics
    add_or_integrate: KB_Audit_v2_scaffold_discipline_as_structural_rule
    not_enough: one_new_best_practice_entry
  MISTAKES.md:
    must_become: frontmatter_plus_critical_path_plus_yaml_failure_registry
    preserve: PW-MK-001_through_PW-MK-011_semantics
    add_or_integrate: YAML_prose_metadata_frontmatter_duplicate_and_validation_failure_modes
    not_enough: one_new_mistake_entry
  TEMPLATES.md:
    must_become: frontmatter_plus_critical_path_plus_yaml_template_registry
    preserve: PW-TPL-001_through_PW-TPL-010_semantics
    add_or_integrate: schema_backed_KB_Audit_v2_template_contracts
    not_enough: one_new_template_entry
  LEARNING_QUEUE.md:
    must_become: frontmatter_plus_critical_path_plus_yaml_candidate_registry
    preserve: PW-LQ-001_through_PW-LQ-011_semantics
    add_or_integrate: non_promotion_guardrails_and_audit_gate_candidates
    not_enough: one_new_learning_entry
  ESSENCE.md:
    must_become: shortest_frontmatter_plus_yaml_activation_doctrine
    preserve: core_boundary_sequence_and_doctrine_semantics
    add_or_integrate: KB_Audit_v2_discipline_as_activation_rule
    not_enough: one_new_bullet
```

---

## 5. Established operator flow

```yaml
operator_flow:
  controller_chat:
    role: orchestrator_and_validator
    per_target_actions:
      - fetch_live_original_target
      - inspect_current_deficiencies_against_KB_Audit_v2
      - generate_one_portable_executor_prompt
      - include exact source_file and candidate_file paths
      - include required structural standard and file-specific rewrite objective
      - wait_for_executor_summary
      - fetch_back_candidate_file
      - validate candidate file shape and plausibility
      - continue_or_halt
  executor_chat:
    role: candidate_file_author
    per_target_actions:
      - fetch_live_original_target
      - read KB_Audit_v2 and this process file
      - create exactly one complete candidate replacement file
      - fetch back candidate file
      - validate YAML/frontmatter/registry/plausibility
      - return EXECUTOR_CANDIDATE_SUMMARY
  operator:
    role: human_reviewer
    actions:
      - copy controller prompt into executor chat
      - paste executor summary back to controller
      - review closure report
      - separately authorize final application of candidates to originals
```

---

## 6. Candidate file contract

```yaml
candidate_file_contract:
  output_type: complete_markdown_replacement_candidate
  allowed_write_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/rewrite_candidates
  filename_pattern: REWRITE-XX_ORIGINAL_BASENAME.v2.md
  forbidden_content:
    - patch_plan_only
    - diff_hunks
    - search_replace_markers
    - commentary_without_complete_replacement_body
  required_content:
    - YAML_frontmatter
    - title_matching_original_scaffold
    - parse_valid_yaml_active_policy
    - compact_registry_or_activation_block
    - appendix_pointers_or_evidence_refs
    - promotion_or_validation_boundary
```

---

## 7. Validation gate

```yaml
validation_gate:
  required_after_executor_fetch_back: true
  checks:
    - id: VG-01
      check: candidate_file_exists_under_rewrite_candidates
      fail_action: halt
    - id: VG-02
      check: no_original_scaffold_file_was_modified
      fail_action: halt
    - id: VG-03
      check: candidate_has_required_frontmatter
      fail_action: halt_or_reprompt
    - id: VG-04
      check: all_yaml_blocks_parse
      fail_action: halt_or_reprompt
    - id: VG-05
      check: active_policy_is_yaml_first_and_within_role_appropriate_prose_budget
      fail_action: reprompt
    - id: VG-06
      check: useful_existing_ids_are_preserved_or_explicitly_mapped
      fail_action: reprompt
    - id: VG-07
      check: KB_Audit_v2_is_structurally_integrated_not_symbolically_appended
      fail_action: reprompt
    - id: VG-08
      check: machine_consumed_templates_or_contracts_have_schema_fields_and_validation
      fail_action: reprompt
```

---

## 8. Plausibility gate

```yaml
plausibility_gate:
  purpose: distinguish_real_rewrite_from_superficial_update
  checks:
    - id: PG-01
      check: The candidate materially changes the scaffold structure toward KB_Audit_v2 compliance.
      fail_signal: unchanged_markdown_list_with_one_added_item
    - id: PG-02
      check: The candidate improves token efficiency and machine readability rather than increasing prose burden.
      fail_signal: long_explanatory_sections_or_duplicate_policy
    - id: PG-03
      check: The candidate makes drift-prevention controls explicit as fields, not prose advice.
      fail_signal: warnings_without_machine_routing_fields
    - id: PG-04
      check: The candidate preserves useful existing semantics in normalized registry form.
      fail_signal: lost_existing_doctrine_or_unmapped_ids
    - id: PG-05
      check: The candidate remains role-appropriate for its scaffold class.
      fail_signal: appendix_or_governance_content_smuggled_into_scaffold
```

---

## 9. Executor summary schema

```yaml
executor_candidate_summary_schema:
  required_block: EXECUTOR_CANDIDATE_SUMMARY
  fields:
    task_id: ''
    source_file: ''
    source_file_sha: ''
    candidate_file: ''
    candidate_file_sha: ''
    write_type: new_candidate_file
    original_file_mutated: false
    structural_changes:
      frontmatter_added: false
      yaml_first_active_policy: false
      critical_path_in_first_500_tokens: false
      rule_metadata_added: false
      schema_contracts_added: false
      prose_reduced_or_moved_to_refs: false
      duplicate_or_overlap_controls_added: false
    content_preservation:
      existing_ids_preserved_or_mapped: []
      existing_ids_removed: []
      removal_reason: ''
    validation:
      candidate_file_created: false
      candidate_fetch_back: pass_or_fail
      frontmatter_parse: pass_or_fail
      yaml_blocks_parse: pass_or_fail
      validation_gate: pass_or_fail
      plausibility_gate_self_check: pass_or_fail
    halt:
      occurred: false
      halt_id: ''
      reason: ''
    next_recommended_controller_action: validate_candidate_and_continue_or_halt
```

---

## 10. Closure standard

```yaml
closure_standard:
  close_only_when:
    - all_five_candidate_files_exist
    - all_five_candidate_files_fetch_back
    - all_five_pass_validation_gate
    - all_five_pass_plausibility_gate
    - superseded_patch_set_is_marked_non_final
  final_application_is_separate: true
  next_step_after_close: Operator reviews candidates and separately authorizes replacing original scaffold files.
```
