---
class: special_ops_prompts_workflows_mistakes
role: SPECIAL_OPS_PROMPTS_WORKFLOWS_ACCEPTED_FAILURE_PATTERNS
surface: agent_kb_scaffold
version: "2.0-candidate"
created_at: "2026-05-07"
last_validated_at: "2026-05-07"
context_mode: compact
target_model_min: gpt-4o
max_active_registry_entries: 13
max_active_rules: 4
max_active_checks: 6
status: candidate_replacement
owner: special_ops__prompts_workflows
validator: meta_ops
source_file: MISTAKES.md
candidate_for: KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS
---

# MISTAKES

```yaml
critical_path:
  priority: critical
  rules:
    - id: MK-CP-01
      tier: critical
      rule: "Keep this scaffold as a compact YAML-first accepted failure-pattern registry."
      prevents: "prose-dominant failure-pattern drift"
      evidence_refs: [KB_Audit_v2.md]
    - id: MK-CP-02
      tier: critical
      rule: "Preserve accepted mistake semantics through stable IDs and evidence refs."
      prevents: "loss of validated prompt/workflow failure doctrine during rewrite"
      evidence_refs: [MISTAKES.md]
    - id: MK-CP-03
      tier: critical
      rule: "Do not promote candidate, appendix, or runtime-governance material into accepted mistake patterns without validation."
      prevents: "unreviewed governance or research smuggling"
      evidence_refs: [LEARNING_QUEUE.md]
    - id: MK-CP-04
      tier: critical
      rule: "Separate registry-entry counts, critical-rule counts, and validation-check counts."
      prevents: "ambiguous active-count compliance claims"
      evidence_refs: [REWRITE-01_controller_validation]
file_contract:
  output_type: complete_markdown_replacement_candidate
  active_registry_path: failure_registry.patterns
  title: MISTAKES
  required_entry_fields: [id, tier, status, pattern, trigger_conditions, countermeasure, prevents, evidence_refs, scores, owner, validator, review_due]
  schema_enforced_outputs: true
scope_boundary:
  allowed: [accepted_failure_pattern_registry, compact_countermeasures, evidence_refs, validation_boundary]
  forbidden: [patch_plan, diff_hunks, search_replace_markers, runtime_governance_claims, appendix_body_promotion]
count_semantics:
  max_active_registry_entries:
    meaning: "Maximum accepted or candidate-integrated PW-MK entries in failure_registry.patterns."
    includes: [PW-MK_entries_only]
    excludes: [critical_path.rules, validation_boundary.machine_validation_checks, appendix_pointers]
  max_active_rules:
    meaning: "Maximum explicit critical path rules outside the registry."
    includes: [critical_path.rules]
    excludes: [failure_registry.patterns, validation_boundary.machine_validation_checks]
  max_active_checks:
    meaning: "Maximum validation checks in validation_boundary.machine_validation_checks."
    includes: [validation_boundary.machine_validation_checks]
    excludes: [failure_registry.patterns, critical_path.rules]
```

```yaml
registry_control:
  duplicate_or_overlap_policy:
    canonical_id_required: true
    semantic_overlap_action: map_to_existing_id_or_mark_pending_meta_ops_validation
    no_paraphrased_duplicate_rules: true
    duplicate_scan_keys: [pattern, trigger_conditions, countermeasure, prevents]
  active_policy_budget:
    format: yaml_first
    prose_budget_tokens: 100
    long_evidence_location: appendices
  target_model_policy:
    target_model_min: gpt-4o
    design_for_weakest_model_in_fleet: true
```

```yaml
failure_registry:
  role: accepted_failure_patterns_scaffold
  owner: special_ops__prompts_workflows
  validator: meta_ops
  max_active_registry_entries: 13
  entry_schema:
    required_fields: [id, tier, status, pattern, trigger_conditions, countermeasure, prevents, evidence_refs, scores, owner, validator, review_due]
    scores_schema:
      EVD: "1-5 evidence strength"
      IMP: "1-5 impact if fixed"
      RSK: "1-5 risk if unfixed"
  patterns:
    - id: PW-MK-001
      tier: critical
      status: accepted
      pattern: "Whole-document rewrite is used for a bounded defect, causing silent compression, omissions, or unrelated wording changes."
      trigger_conditions: [long_markdown_file, localized_defect_or_reference_break, weak_anchors_or_broad_cleanup_instruction, missing_preservation_invariant]
      countermeasure: "Use patch mode for stable local defects; otherwise use a complete final body or live-edit instruction with explicit preservation and read-back verification."
      prevents: "silent compression, omissions, and unrelated wording drift during bounded repair"
      evidence_refs:
        - "appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-001"
        - "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-003"
      scores: {EVD: 5, IMP: 5, RSK: 5}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-002
      tier: critical
      status: accepted
      pattern: "Source summaries, previous-chat claims, or candidate artifacts are treated as primary truth when raw source is available."
      trigger_conditions: [multiple_source_files_exist, summaries_are_easier_than_originals, prompt_says_use_these_files, authority_order_not_declared]
      countermeasure: "Declare source tiers before execution; use raw/current source as primary and mark derived, working, speculative, or stale material explicitly."
      prevents: "authority inversion between live source and derived artifacts"
      evidence_refs:
        - "appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-006"
        - "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-008"
      scores: {EVD: 5, IMP: 5, RSK: 4}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-003
      tier: required
      status: accepted
      pattern: "One prompt or promptflow blends research, architecture, editing, QA, packaging, and finalization into one opaque pass."
      trigger_conditions: [many_major_outputs_requested, target_not_one_bounded_artifact_or_closed_file_set, quality_gates_unsequenced, automatic_continuation]
      countermeasure: "Classify overload before execution; split into bounded passes or treat the promptflow as a closed execution unit with explicit file order and verification gates."
      prevents: "opaque multi-domain execution with unverified intermediate quality gates"
      evidence_refs:
        - "appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-002"
        - "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-004"
      scores: {EVD: 5, IMP: 5, RSK: 4}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-004
      tier: critical
      status: accepted
      pattern: "Output is approved because it is fluent, structured, or plausible, without evidence, read-back, diff, test, or checklist verification."
      trigger_conditions: [agent_says_done_after_generation, file_write_or_patch_not_fetched_back, instruction_parity_check_not_run, evidence_refs_not_recorded]
      countermeasure: "Require verification before trust using read-back, diff review, file-state check, checklist, source evidence, or test according to output type."
      prevents: "false completion and unverified candidate promotion"
      evidence_refs:
        - "appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-006"
        - "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-005"
        - "appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-08--false-completion-without-fetch-back"
      scores: {EVD: 5, IMP: 5, RSK: 5}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-005
      tier: required
      status: accepted
      pattern: "A reusable prompt, template, or workflow pattern is treated as hidden runtime governance."
      trigger_conditions: [template_lacks_authority_limits, promptflow_used_as_governance_approval, scaffold_content_copied_into_config_QA_promotion_or_orchestration_lanes]
      countermeasure: "Keep templates as construction aids; route governance, config, QA, and promotion questions to their owning surfaces or agents."
      prevents: "governance authority smuggling from reusable prompt artifacts"
      evidence_refs:
        - "appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-003"
        - "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-014"
      scores: {EVD: 4, IMP: 5, RSK: 4}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-006
      tier: required
      status: accepted
      pattern: "Out-of-mode improvements are silently applied during a bounded execution run."
      trigger_conditions: [adjacent_cleanup_or_architecture_improvement_noticed, closed_or_one_file_mode, improvement_feels_obviously_useful, no_capture_section_exists]
      countermeasure: "Capture high-value improvements in a bounded Improvement Opportunities Not Applied section; do not apply them until a future authorized mode."
      prevents: "scope creep and unauthorized mutation during bounded execution"
      evidence_refs:
        - "appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-008"
        - "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-011"
      scores: {EVD: 5, IMP: 4, RSK: 3}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-007
      tier: required
      status: accepted
      pattern: "A named promptflow artifact is treated as the whole task even when the operator intended execution of the broader flow."
      trigger_conditions: [operator_names_promptflow_appendix_or_artifact_path, named_artifact_exists_or_matches_prior_commit, user_asks_to_execute_not_inspect, intent_not_compared_to_contract_and_repo_state]
      countermeasure: "Run an intent-contract check before completion; create the missing bounded artifact or stop on a real blocker when intended scope exceeds named artifact status."
      prevents: "no-op completion when operator intent requires broader flow execution"
      evidence_refs:
        - "appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#user-intent-versus-executed-promptflow-gap-analysis"
        - "appendices/APPENDIX_KB_EXAMPLES.md#example-2-user-intent-versus-named-artifact-mismatch"
        - "appendices/PROMPTFLOW_PROMPTS_WORKFLOWS_BOUNDED_EXECUTION_GUARDRAILS.md#5-required-execution-contract"
      scores: {EVD: 5, IMP: 5, RSK: 4}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-008
      tier: required
      status: accepted
      pattern: "Completion is claimed from artifact existence instead of current completeness, intent fit, and validation against the requested phase."
      trigger_conditions: [prior_artifact_exists, previous_commit_contains_related_content, status_report_before_intended_deliverable_check, output_requires_decisions_options_recommendations_or_next_step_research]
      countermeasure: "Validate against active deliverable, exact target, content completeness, one-file or one-artifact constraint, and stop condition; create missing artifact or report exact gap."
      prevents: "artifact-existence completion claims that miss the requested decision layer"
      evidence_refs:
        - "appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#current-qa-status"
        - "appendices/APPENDIX_KB_EXAMPLES.md#regression-checklist"
      scores: {EVD: 5, IMP: 5, RSK: 4}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-009
      tier: required
      status: accepted
      pattern: "Execution state is reconstructed from chat history, prior messages, or implied continuity instead of an explicit current frame or state block."
      trigger_conditions: [continue_from_where_we_left_off, current_state_or_frame_missing_stale_or_contradictory, source_refs_or_target_file_inferred_from_prior_chat, executor_proceeds_despite_state_ambiguity]
      countermeasure: "Require an explicit current frame/state block and atomic task payload; emit HALT or CLARIFY if state is missing, stale, or contradictory."
      prevents: "execution from stale or implicit chat-history state"
      evidence_refs:
        - "appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-01--implicit-chat-history-state-reconstruction"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-02--stale-or-missing-state_block"
      scores: {EVD: 5, IMP: 5, RSK: 3}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-010
      tier: required
      status: accepted
      pattern: "A compound or underspecified task payload expands into multiple artifacts, directory scans, unauthorized targets, or scaffold edits."
      trigger_conditions: [scope_contains_AND_or_THEN, target_file_missing_broad_or_outside_allowed_root, input_refs_absent_directory_level_or_inferred, appendix_task_also_mutates_scaffold]
      countermeasure: "Split compound work into one atomic task per call; require exact target file, exact source refs, and target-root validation before execution."
      prevents: "multi-artifact expansion, unauthorized targets, and scaffold mutation from underspecified payloads"
      evidence_refs:
        - "appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-03--compound-task_payload-using-andthen"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-04--target-path-outside-target-root"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-05--directory-scan-without-explicit-input_refs"
      scores: {EVD: 5, IMP: 5, RSK: 4}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-011
      tier: critical
      status: accepted
      pattern: "Execution continues after a HALT, CLARIFY, patch-check failure, split-required condition, or failed closure validation."
      trigger_conditions: [unresolved_HALT_exists, ambiguity_should_produce_CLARIFY_but_executor_guesses, patch_preimage_or_dry_run_fails, split_required_output_replaced_with_summary, closure_claimed_despite_failed_or_missing_validation]
      countermeasure: "Treat control signals and validation failures as hard stops until payload, source refs, patch preimage, split plan, or validation evidence is corrected."
      prevents: "unsafe continuation after hard-stop or validation-failure signals"
      evidence_refs:
        - "appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md"
        - "appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-06--ambiguity-that-should-return-clarify"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-07--unsafe-continuation-after-halt-condition"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-09--patch-preimage-mismatch"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-10--skipped-dry-run-before-patch"
        - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-11--split-required-output-that-substitutes-summary"
      scores: {EVD: 5, IMP: 5, RSK: 4}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-MK-012
      tier: critical
      status: candidate_replacement_integrated
      pattern: "A KB scaffold is rewritten as prose-dominant Markdown without frontmatter, early critical path, parse-valid YAML registry, or explicit count semantics."
      trigger_conditions: [missing_yaml_frontmatter, critical_rules_buried_after_first_500_tokens, accepted_patterns_written_as_markdown_list_entries, count_semantics_ambiguous]
      countermeasure: "Use frontmatter plus early critical_path/file_contract/scope_boundary/count_semantics YAML and a parse-valid compact registry."
      prevents: "symbolic KB_Audit_v2 compliance and machine-unreadable scaffold drift"
      evidence_refs:
        - "KB_Audit_v2.md#ACTIVE-POLICY"
        - "KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS.md#3-KB_Audit_v2-structural-standard"
      scores: {EVD: 5, IMP: 5, RSK: 5}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"
      validation_note: "Promote to accepted only if operator/meta_ops approves this candidate replacement."

    - id: PW-MK-013
      tier: critical
      status: candidate_replacement_integrated
      pattern: "Validation is claimed from formatted output or executor summary instead of fetch-back, YAML parse, ID preservation, count consistency, and plausibility checks."
      trigger_conditions: [candidate_file_not_fetched_back, yaml_blocks_not_parsed, IDs_not_preserved_or_mapped, registry_rule_check_counts_confused, new_entries_marked_plain_accepted_without_validation]
      countermeasure: "Run fetch-back validation, parse frontmatter and YAML blocks, verify ID preservation, separate count domains, and guard new entries before promotion."
      prevents: "false completion and unverified candidate promotion"
      evidence_refs:
        - "KB_Audit_v2.md#AUDIT-CHECKLIST"
        - "KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS.md#7-Validation-gate"
      scores: {EVD: 5, IMP: 5, RSK: 5}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"
      validation_note: "Promote to accepted only if operator/meta_ops approves this candidate replacement."
```

```yaml
validation_boundary:
  promotion_rule: "This candidate may replace MISTAKES.md only after operator/meta_ops validation."
  new_entry_status_rule: "candidate_replacement_integrated entries are not plain accepted until replacement approval."
  machine_validation_checks:
    - id: MK-VG-01
      tier: critical
      check: "Frontmatter contains target_model_min, max_active_registry_entries, max_active_rules, max_active_checks, context_mode, owner, and validator."
      pass_condition: "required_frontmatter_fields_present == true"
      fail_action: halt
      prevents: "metadata-free scaffold loading"
      evidence_refs: [KB_Audit_v2.md]
    - id: MK-VG-02
      tier: critical
      check: "Every YAML block parses with yaml.safe_load_all."
      pass_condition: "yaml_parse_errors == 0"
      fail_action: halt
      prevents: "malformed machine-consumed policy blocks"
      evidence_refs: [KB_Audit_v2.md]
    - id: MK-VG-03
      tier: critical
      check: "critical_path.rules appears within the first 500 tokens."
      pass_condition: "critical_path_token_position <= 500"
      fail_action: halt
      prevents: "mid-document critical-rule burial"
      evidence_refs: [KB_Audit_v2.md]
    - id: MK-VG-04
      tier: required
      check: "failure_registry.patterns contains PW-MK-001 through PW-MK-011 or explicit mappings."
      pass_condition: "missing_original_ids == []"
      fail_action: revise
      prevents: "loss of validated accepted mistake semantics"
      evidence_refs: [MISTAKES.md]
    - id: MK-VG-05
      tier: required
      check: "Registry count, critical-rule count, and validation-check count each stay within their own frontmatter limits."
      pass_condition: "registry_entries <= max_active_registry_entries AND critical_rules <= max_active_rules AND validation_checks <= max_active_checks"
      fail_action: revise
      prevents: "ambiguous active-count compliance"
      evidence_refs: [REWRITE-01_controller_validation]
    - id: MK-VG-06
      tier: required
      check: "New integrated entries use guarded status, not plain accepted."
      pass_condition: "new_entries_plain_accepted == 0"
      fail_action: revise
      prevents: "unvalidated failure-pattern promotion"
      evidence_refs: [KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS.md]
```

```yaml
appendix_pointers:
  evidence_refs_only: true
  active_scaffold_excludes_appendix_bodies: true
  refs:
    - "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md"
    - "appendices/SOURCE_CONFLICT_REPORT.md"
    - "appendices/APPENDIX_KB_CANDIDATE_LEDGER.md"
    - "appendices/APPENDIX_KB_EXAMPLES.md"
    - "appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md"
    - "appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md"
    - "appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md"
    - "appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md"
    - "appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md"
    - "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md"
    - "appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md"
    - "appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md"
```
