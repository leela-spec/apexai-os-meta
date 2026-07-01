---
class: special_ops_prompts_workflows_essence
role: SPECIAL_OPS_PROMPTS_WORKFLOWS_COMPACT_ACTIVATION_DOCTRINE
surface: agent_kb_scaffold
version: "2.0-candidate"
created_at: "2026-05-07"
last_validated_at: "2026-05-07"
context_mode: compact
target_model_min: gpt-4o
max_active_rules: 5
max_active_checks: 5
status: candidate_replacement
owner: special_ops__prompts_workflows
validator: meta_ops
source_file: ESSENCE.md
candidate_for: KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS
---

# ESSENCE

```yaml
activation_contract:
  priority: critical
  purpose: "Activate Special Ops Prompts Workflows doctrine for reusable prompts, workflows, promptflows, handoffs, and bounded execution patterns."
  target_model_min: gpt-4o
  max_active_rules: 5
  max_active_checks: 5
  count_semantics:
    max_active_rules: "Count activation_contract.rules only; exclude read_when, default_sequence.steps, appendix_pointers, and validation checks."
    max_active_checks: "Count validation_boundary.machine_validation_checks only; exclude activation rules, read_when, default_sequence.steps, and appendix_pointers."
  scope_boundary:
    owns: [reusable_prompt_structures, workflow_stage_patterns, bounded_execution_sequences, promptflow_skeletons, handoff_templates, source_authority_and_verification_wording, out_of_mode_improvement_capture_patterns]
    does_not_own: [orchestration_authority, model_config_routing_authority, KB_placement_authority, QA_severity_authority, promotion_approval_authority, config_mutation]
  rules:
    - {id: ESS-CP-01, tier: critical, status: accepted_from_source, rule: "Lock target, source authority, output contract, and stop condition before execution.", prevents: "scope drift and unbounded promptflow execution", evidence_refs: [ESSENCE.md]}
    - {id: ESS-CP-02, tier: critical, status: accepted_from_source, rule: "Use bounded, stage-gated execution with verification before trust.", prevents: "fluent false completion and skipped source or file-state validation", evidence_refs: [ESSENCE.md]}
    - {id: ESS-CP-03, tier: critical, status: accepted_from_source, rule: "Carry explicit state for high-risk promptflows instead of relying on conversational continuity.", prevents: "implicit stale-state reconstruction", evidence_refs: [ESSENCE.md]}
    - {id: ESS-CP-04, tier: critical, status: accepted_from_source, rule: "Capture out-of-mode improvements without applying them inside the current bounded run.", prevents: "scope smuggling and unreviewed adjacent edits", evidence_refs: [ESSENCE.md]}
    - {id: ESS-CP-05, tier: critical, status: candidate_replacement_integrated, rule: "Keep this ESSENCE file YAML-first, compact, and structurally aligned with KB_Audit_v2.", prevents: "prose-dominant activation drift and symbolic audit compliance", evidence_refs: [KB_Audit_v2.md, KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS.md], validation_note: "Promote as accepted only after operator or meta_ops approval."}
```

```yaml
compact_doctrine:
  status: accepted_from_source
  doctrine:
    target_first: "Name exact deliverable, scope, non-goals, source authority, output contract, and stop condition before execution."
    bounded_execution: "Default to one substantial deliverable or one closed promptflow file set per pass."
    stage_gates: "Run source lock and plausibility checks before scaffold or execution output."
    constant_frame_control: "Carry explicit state, atomic task payload, gate check, stop signal, and closure proof for high-risk promptflows."
    authority_before_action: "Treat source authority as a pre-step gate; current primary files outrank summaries and chat context."
    verify_before_trust: "Use read-back, diff, file-state check, checklist, evidence, or test before reporting completion."
    patch_write_mode_by_context: "Patch stable local defects; use full final body or live-edit instruction when diff transport is fragile."
    capture_do_not_smuggle: "Send out-of-mode improvements to a capture section or LEARNING_QUEUE.md, not the current bounded run."
    examples_are_regression_tests: "Use concrete examples to check behavior, not as decorative reference material."
    templates_are_not_governance: "Use templates to build prompts and workflows; do not grant runtime authority through templates."
  read_when:
    - prompt_must_create_file_patch_research_artifact_or_handoff
    - promptflow_needs_staged_source_lock_and_scaffold_generation
    - execution_prompt_needs_mode_path_scope_locks
    - new_chat_or_agent_needs_clean_handoff
    - drift_risk_from_broad_scope_fragile_diff_transport_source_ambiguity_or_automatic_continuation
```

```yaml
default_sequence:
  steps:
    - lock_target_and_source_authority
    - classify_overload_and_non_goals
    - choose_patch_full_body_live_edit_research_handoff_or_promptflow_mode
    - execute_one_bounded_deliverable_or_closed_file_set
    - verify_against_source_or_file_state
    - record_deferred_candidates_in_LEARNING_QUEUE
    - stop_or_handoff_explicitly
```

```yaml
appendix_pointers:
  source_manifest: appendices/APPENDIX_KB_SOURCE_MANIFEST.md
  execution_control_contracts: appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
  ranking_ledger: appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
  candidate_ledger: appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
  anti_drift_evidence: appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
  conflict_report: appendices/SOURCE_CONFLICT_REPORT.md
  examples: appendices/APPENDIX_KB_EXAMPLES.md
  source_notes: appendices/APPENDIX_KB_SOURCE_NOTES.md
  qa_and_next_research_plan: appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
```

```yaml
validation_boundary:
  status: candidate_replacement_boundary
  source_file_mutation: forbidden
  patch_or_diff_artifacts: forbidden
  registry_expansion: forbidden
  machine_validation_checks:
    - {id: ESS-V-01, tier: critical, check: "Candidate exists only under rewrite_candidates.", pass_condition: "candidate_path_matches_allowed_root", fail_action: halt}
    - {id: ESS-V-02, tier: critical, check: "Original ESSENCE.md remains unmodified.", pass_condition: "source_file_sha_unchanged", fail_action: halt}
    - {id: ESS-V-03, tier: critical, check: "Frontmatter contains required model, status, owner, validator, and count fields.", pass_condition: "required_frontmatter_fields_present", fail_action: halt_or_reprompt}
    - {id: ESS-V-04, tier: critical, check: "All YAML blocks parse.", pass_condition: "yaml_parse_errors == 0", fail_action: halt_or_reprompt}
    - {id: ESS-V-05, tier: required, check: "Rule and check counts stay separated and new KB_Audit_v2 doctrine remains approval-guarded.", pass_condition: "max_active_rules == 5 and max_active_checks == 5 and ESS-CP-05.status != accepted", fail_action: reprompt}
```

```yaml
source_status_metadata:
  original_status: accepted
  candidate_status: candidate_replacement
  owner: special_ops__prompts_workflows
  validator: meta_ops
  seed_source: managed/agents/special_ops__prompts_workflows.md
  source_manifest: appendices/APPENDIX_KB_SOURCE_MANIFEST.md
  review_due: "2026-07-27"
  evidence_refs: [ESSENCE.md, KB_Audit_v2.md, KB_AUDIT_V2_NEW_FILE_REWRITE_PROCESS.md]
```
