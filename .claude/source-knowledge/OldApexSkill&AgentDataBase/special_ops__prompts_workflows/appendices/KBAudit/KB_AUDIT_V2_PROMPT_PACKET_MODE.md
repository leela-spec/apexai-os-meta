---
class: kb_audit_v2_prompt_packet_mode
role: SPECIAL_OPS_KB_AUDIT_V2_EXTERNAL_CHAT_PACKET_CONTROLLER
surface: repo_process_pipeline_addendum
version: "1.0"
created_at: "2026-05-07"
last_validated_at: "2026-05-07"
context_mode: compact
status: active_for_current_run
scope: special_ops__prompts_workflows_scaffold_update_prompt_packets
target_repo: leela-spec/MasterOfArts
target_branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows
patch_output_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/patches
parent_pipeline: KB_AUDIT_V2_UPDATE_PIPELINE.md
source_contracts:
  - AGENT_PIPELINE_CONTROLLER.md
  - AGENT_PATCH_CONTRACT.md
  - KB_Audit_v2.md
target_model_min: gpt-4o
validated_against_model: gpt-5.5
max_active_rules: 12
---

# KB_AUDIT_V2_PROMPT_PACKET_MODE

```yaml
MODE_LOCK:
  default_mode: controller_generates_external_chat_prompt_packet
  controller_chat_role: orchestrator_and_validator
  executor_chat_role: patch_author_and_fetch_back_validator
  applies_to:
    - ESSENCE.md
    - BEST_PRACTICES.md
    - MISTAKES.md
    - TEMPLATES.md
    - LEARNING_QUEUE.md
  supersedes_for_current_run:
    - direct_patch_creation_by_controller_chat
  does_not_supersede:
    - AGENT_PIPELINE_CONTROLLER.md
    - AGENT_PATCH_CONTRACT.md
    - KB_Audit_v2.md
```

---

## CRITICAL LOCKS

```yaml
CRITICAL_LOCKS:
  priority: critical
  rules:
    - id: PP-LOCK-01
      rule: "Controller chat outputs a portable execution prompt packet; it does not author the target patch directly unless the operator explicitly overrides prompt-packet mode."
      prevents: "orchestrator/executor role collapse"
      evidence_refs: [AGENT_PIPELINE_CONTROLLER, AGENT_PATCH_CONTRACT]
    - id: PP-LOCK-02
      rule: "Each prompt packet is one target file only and contains the exact repo path, target path, patch output path, source contracts, audit checks, halt rules, and required return summary schema."
      prevents: "scope drift; multi-file accidental execution"
      evidence_refs: [AGENT_PIPELINE_CONTROLLER]
    - id: PP-LOCK-03
      rule: "Executor chat must fetch the live target file before generating old_text and must treat its own fetched SHA as source of truth."
      prevents: "stale preimage copied from controller prompt"
      evidence_refs: [AGENT_PATCH_CONTRACT]
    - id: PP-LOCK-04
      rule: "Executor chat must write only one .patch.md file under patch_output_root and must fetch it back before returning summary."
      prevents: "unvalidated patch artifact; target mutation"
      evidence_refs: [AGENT_PIPELINE_CONTROLLER, AGENT_PATCH_CONTRACT]
    - id: PP-LOCK-05
      rule: "Controller chat resumes only from executor summary plus independent fetch-back validation of the patch file."
      prevents: "trusting executor prose completion"
      evidence_refs: [AGENT_PIPELINE_CONTROLLER]
```

---

## PROMPT PACKET REQUIRED SHAPE

```yaml
PROMPT_PACKET_REQUIRED_SHAPE:
  sections:
    - ROLE
    - TASK
    - HARD_SCOPE_LOCK
    - SOURCE_CONTRACTS_TO_USE
    - TARGET_FILE_PACKET
    - REQUIRED_EXECUTION_STATE_MACHINE
    - KB_AUDIT_CHECKS_TO_APPLY
    - WRITE_CLASS_DECISION
    - PATCH_CONTRACT
    - VALIDATION_GATE
    - HALT_CONDITIONS
    - FORBIDDEN_ACTIONS
    - REQUIRED_OUTPUT_TO_REPO
    - REQUIRED_SUMMARY_BACK_TO_CONTROLLER
  constraints:
    - "No direct target file mutation."
    - "No multiple target files."
    - "No old_text from prompt or memory."
    - "No continuing after HALT."
    - "No using support docs as controllers."
```

---

## EXECUTOR RETURN SUMMARY SCHEMA

```yaml
EXECUTOR_RETURN_SUMMARY_SCHEMA:
  required_yaml_block: EXECUTOR_PATCH_SUMMARY
  fields:
    task_id: ""
    target_file: ""
    target_file_sha: ""
    patch_file: ""
    patch_file_sha: ""
    write_class: "scaffold_update | full_body_replace | no_op"
    audit_flags: []
    operations_count: 0
    preimage_checks:
      - op_id: ""
        old_text_occurrences: 0
        old_text_copied_from_live_file: false
        result: "pass | fail"
    validation:
      patch_file_created: false
      patch_file_fetch_back: "pass | fail"
      frontmatter_present: "pass | fail"
      patch_plan_yaml_present: "pass | fail"
      preimage_check_yaml_present: "pass | fail"
      target_header_present: "pass | fail"
      delimiters_intact: "pass | fail | not_applicable"
      old_text_occurrences_all_equal_1: "pass | fail | not_applicable"
    halt:
      occurred: false
      halt_id: ""
      reason: ""
    next_recommended_controller_action: "validate_patch_and_continue | halt | ask_operator"
```

---

## CONTROLLER RESUME RULES

```yaml
CONTROLLER_RESUME_RULES:
  on_executor_summary_received:
    actions:
      - fetch_back_patch_file_from_repo
      - verify_patch_file_path_matches_summary
      - verify_patch_contract_sections
      - verify_validation_claims_against_patch_file
      - decide_continue_or_halt
  on_missing_or_invalid_summary:
    action: "HALT and request corrected executor summary."
  on_patch_fetch_failure:
    action: "HALT patch_validation_failed."
```
