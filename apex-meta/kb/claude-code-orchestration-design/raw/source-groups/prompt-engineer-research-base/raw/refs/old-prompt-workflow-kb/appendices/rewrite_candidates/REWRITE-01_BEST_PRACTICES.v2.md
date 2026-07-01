---
class: special_ops_prompts_workflows_best_practices
role: SPECIAL_OPS_PROMPTS_WORKFLOWS_ACCEPTED_PRACTICES
surface: agent_kb_scaffold
version: "2.0-candidate"
created_at: "2026-05-07"
last_validated_at: "2026-05-07"
context_mode: compact
target_model_min: gpt-4o
max_active_rules: 12
status: candidate_replacement
owner: special_ops__prompts_workflows
validator: meta_ops
source_file: BEST_PRACTICES.md
candidate_for: KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS
---

# BEST_PRACTICES

```yaml
critical_path:
  priority: critical
  rules:
    - id: BP-CP-01
      tier: critical
      rule: "Keep this scaffold as a compact YAML-first accepted-practices registry."
      prevents: "prose-dominant scaffold drift"
      evidence_refs: [KB_Audit_v2.md]
    - id: BP-CP-02
      tier: critical
      rule: "Preserve accepted practice semantics through stable IDs and evidence refs."
      prevents: "loss of validated prompt/workflow doctrine during rewrite"
      evidence_refs: [BEST_PRACTICES.md]
    - id: BP-CP-03
      tier: critical
      rule: "Do not promote candidate, appendix, or runtime-governance material into accepted practices without validation."
      prevents: "unreviewed governance or research smuggling"
      evidence_refs: [LEARNING_QUEUE.md]

file_contract:
  output_type: accepted_practices_scaffold
  active_policy_format: parse_valid_yaml
  max_active_practices: 12
  required_entry_fields: [id, tier, status, practice, context_conditions, prevents, evidence_refs, scores, owner, validator, review_due]
  validation: "yaml.safe_load frontmatter and all fenced YAML before promotion"

scope_boundary:
  allowed_content: [critical_path, file_contract, scope_boundary, practice_registry, appendix_pointers, validation_boundary]
  forbidden_content: [patch_plan, diff_hunks, search_replace_markers, long_evidence_prose, unvalidated_learning_queue_candidates, runtime_template_catalog_body]
```

## Active Practice Registry

```yaml
practice_registry:
  registry_class: accepted_practices
  owner: special_ops__prompts_workflows
  validator: meta_ops
  active_practice_count: 12
  duplicate_or_overlap_controls:
    id_uniqueness_required: true
    semantic_overlap_action: "merge_into_existing_id_or_route_to_LEARNING_QUEUE"
    parallel_rule_forbidden_without_validator: true
    evidence_ref_required_for_each_entry: true
    prevents_required_for_each_entry: true
  practices:
    - id: PW-BP-001
      tier: critical
      status: accepted
      practice: "Use full final bodies or live-edit instructions when Markdown diff transport is fragile; use patch mode only for small bounded defects with stable anchors."
      context_conditions: [large_markdown_rewrite, new_file_creation, non_line_stable_connector_output, CRLF_or_hidden_character_risk, malformed_unified_diff_with_bounded_intent, small_bounded_defect_with_reliable_anchors]
      prevents: "diff transport corruption and unsafe patch-mode use on unstable bodies"
      evidence_refs: [appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-001, appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-001, appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-003]
      scores: {EVD: 5, IMP: 5, RSK: 5}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-002
      tier: critical
      status: accepted
      practice: "Freeze objective, target, source authority, non-goals, output contract, and stop condition before serious prompt/workflow execution."
      context_conditions: [file_producing_prompt, research_producing_prompt, patch_producing_prompt, handoff_producing_prompt, multi_source_or_long_context_task]
      prevents: "scope drift, output-contract drift, and unstated success criteria"
      evidence_refs: [appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-001, appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-002, appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-a--scope-lock]
      scores: {EVD: 5, IMP: 5, RSK: 2}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-003
      tier: required
      status: accepted
      practice: "Use bounded, stage-gated, artifact-centered execution instead of broad autonomy or giant multi-phase prompts."
      context_conditions: [subscription_chat_execution, low_context_agent_handoff, documentation_or_architecture_work, workflow_blends_research_writing_QA_packaging_finalization]
      prevents: "multi-phase autonomy drift and summary substitution for artifacts"
      evidence_refs: [appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-003, appendices/APPENDIX_KB_CANDIDATE_LEDGER.md#pw-cand-003, appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-006]
      scores: {EVD: 5, IMP: 5, RSK: 3}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-004
      tier: critical
      status: accepted
      practice: "Make source authority a pre-step gate and verification a post-step gate; do not trust output because it looks fluent."
      context_conditions: [source_hierarchy_matters, reusable_or_committed_outputs, multiple_summaries_and_originals_exist, conflicting_primary_sources]
      prevents: "fluent but unverified output and authority inversion"
      evidence_refs: [appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-006, appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-b--source-authority-preflight, appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-d--verification-gate]
      scores: {EVD: 5, IMP: 5, RSK: 3}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-005
      tier: required
      status: accepted
      practice: "Detect out-of-mode improvements, but capture them explicitly instead of applying them silently."
      context_conditions: [closed_execution_mode, adjacent_improvement_detected_by_agent, high_confidence_out_of_scope_improvement]
      prevents: "silent scope expansion and unreviewed adjacent edits"
      evidence_refs: [appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-008, appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-e--out-of-mode-capture]
      scores: {EVD: 5, IMP: 4, RSK: 3}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-006
      tier: required
      status: accepted
      practice: "Use clean handoffs across chats, agents, or execution lanes: settled state, source priority, non-redo list, exact next job, risks, and success condition."
      context_conditions: [new_chat_continuation, codex_handoff, multi_stage_research_to_patch_workflow, saturated_or_overloaded_prior_thread]
      prevents: "handoff state loss and redundant rework"
      evidence_refs: [appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-010, appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-f--handoff-reset]
      scores: {EVD: 4, IMP: 5, RSK: 2}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-007
      tier: required
      status: accepted
      practice: "Record durable QA, gap, and next-research results in a repo appendix when a KB build or improvement pass changes what future agents should rely on."
      context_conditions: [KB_build_or_improvement_pass, future_scaffold_promotion_candidates_identified, verification_or_gap_analysis_would_remain_chat_only, multiple_appendices_or_scaffolds_may_be_affected]
      prevents: "loss of reusable QA findings and chat-only institutional memory"
      evidence_refs: [appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#purpose, appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#current-qa-status, appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#next-patch-candidates]
      scores: {EVD: 5, IMP: 5, RSK: 3}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-008
      tier: recommended
      status: accepted
      practice: "Treat prompt and workflow examples as behavioral regression tests for this lane; check target, source, mode, validation, and stop discipline."
      context_conditions: [prompt_or_promptflow_behavior_taught_reused_or_validated, prior_scope_drift_noop_fragile_diff_or_out_of_mode_failure, template_needs_before_after_evidence]
      prevents: "example drift and untested promptflow regressions"
      evidence_refs: [appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#f5-scaffold-promotion-matrix, appendices/APPENDIX_KB_EXAMPLES.md#purpose, appendices/APPENDIX_KB_EXAMPLES.md#regression-checklist]
      scores: {EVD: 5, IMP: 5, RSK: 3}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-009
      tier: critical
      status: accepted
      practice: "Carry execution state as an explicit frame or state block; never rely on chat-history reconstruction for current task state."
      context_conditions: [high_risk_promptflow_execution, multi_chat_or_operator_mediated_task_sequence, repo_writing_or_scaffold_update_workflow, stale_missing_or_contradictory_prior_context_possible]
      prevents: "implicit state reconstruction and stale-context continuation"
      evidence_refs: [appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md, appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-01--implicit-chat-history-state-reconstruction, appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-02--stale-or-missing-state_block]
      scores: {EVD: 5, IMP: 5, RSK: 3}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-010
      tier: critical
      status: accepted
      practice: "Execute high-risk tasks through an atomic task packet: one task, one target, explicit input refs, repeated scope, and a gate check before write or synthesis."
      context_conditions: [appendix_creation, scaffold_update, patch_or_file_write_task, handoff_to_chat_executor_or_operator, constrained_source_authority_or_target_root]
      prevents: "compound task bleed, wrong-target writes, and pre-gate synthesis"
      evidence_refs: [appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md, appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md, appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-03--compound-task_payload-using-andthen, appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-05--directory-scan-without-explicit-input_refs]
      scores: {EVD: 5, IMP: 5, RSK: 3}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-011
      tier: critical
      status: accepted
      practice: "Treat HALT, CLARIFY, patch-check failure, split-required conditions, and unverified external claims as routing controls, not prose warnings."
      context_conditions: [ambiguity_after_gate_check, patch_dry_run_or_preimage_failure, split_required_output, external_claim_affects_doctrine, closure_lacks_fetch_back_or_claim_status_proof]
      prevents: "unsafe continuation after halt signals and warning-only routing"
      evidence_refs: [appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md, appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md, appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md, appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-07--unsafe-continuation-after-halt-condition, appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-11--split-required-output-that-substitutes-summary, appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-13--external-modelplatform-claim-promoted-as-accepted-doctrine]
      scores: {EVD: 5, IMP: 5, RSK: 4}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"

    - id: PW-BP-012
      tier: critical
      status: accepted
      practice: "Maintain KB_Audit_v2 scaffold discipline: frontmatter, early critical path, YAML-first active policy, rule metadata, duplicate controls, and validation boundary."
      context_conditions: [agent_kb_scaffold_loaded_as_context, scaffold_rewrite_or_promotion, machine_consumed_policy_or_registry, prompt_workflow_doctrine_update]
      prevents: "noncompliant scaffold drift, prose-only contracts, duplicate rules, and symbolic audit integration"
      evidence_refs: [KB_Audit_v2.md, KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS.md#3-kb_audit_v2-structural-standard]
      scores: {EVD: 5, IMP: 5, RSK: 5}
      owner: special_ops__prompts_workflows
      validator: meta_ops
      review_due: "2026-07-27"
```

## Appendix Pointers

```yaml
appendix_pointers:
  source_manifest: appendices/APPENDIX_KB_SOURCE_MANIFEST.md
  ranking_ledger: appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
  candidate_ledger: appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
  anti_drift_evidence: appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
  source_conflicts: appendices/SOURCE_CONFLICT_REPORT.md
  examples: appendices/APPENDIX_KB_EXAMPLES.md
  source_notes: appendices/APPENDIX_KB_SOURCE_NOTES.md
  qa_and_next_research_plan: appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
  constant_failure_integration_process: appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
  execution_control_contracts: appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
  constant_failure_source_notes: appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
  patch_transport_protocols: appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
  regression_examples: appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md
  runtime_template_catalog: appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md
  external_claim_verification: appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md
```

## Validation Boundary

```yaml
validation_boundary:
  promotion_flow:
    - route_new_or_revised_practice_to: LEARNING_QUEUE.md
    - require_evidence_refs: true
    - require_meta_ops_review: true
    - require_fetch_back_validation: true
    - require_yaml_parse_validation: true
  machine_validation_checks:
    - id: BP-VG-01
      tier: critical
      check: "Frontmatter includes version, last_validated_at, target_model_min, max_active_rules, and context_mode."
      pass_condition: "required_frontmatter_fields_present == true"
      fail_action: halt
    - id: BP-VG-02
      tier: critical
      check: "All fenced YAML blocks parse."
      pass_condition: "yaml_parse_errors == 0"
      fail_action: halt
    - id: BP-VG-03
      tier: required
      check: "Every practice entry has all required registry fields."
      pass_condition: "entries_missing_required_fields == 0"
      fail_action: revise
    - id: BP-VG-04
      tier: required
      check: "Accepted practice IDs are unique and active_practice_count does not exceed max_active_rules."
      pass_condition: "duplicate_ids == 0 AND active_practice_count <= max_active_rules"
      fail_action: revise
    - id: BP-VG-05
      tier: required
      check: "No practice duplicates or paraphrases another practice without explicit mapping."
      pass_condition: "semantic_overlap_unmapped == 0"
      fail_action: revise
```
