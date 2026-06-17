---
class: kb_audit_v2_update_pipeline
role: SPECIAL_OPS_KB_AUDIT_V2_PATCH_RUN_CONTROLLER
surface: repo_process_pipeline
version: "1.0"
created_at: "2026-05-07"
last_validated_at: "2026-05-07"
context_mode: compact
status: active_for_current_run
scope: special_ops__prompts_workflows_kb_update
target_repo: leela-spec/MasterOfArts
target_branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows
appendix_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices
patch_output_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/patches
source_contracts:
  - AGENT_PIPELINE_CONTROLLER.md
  - AGENT_PATCH_CONTRACT.md
  - KB_Audit_v2.md
target_model_min: gpt-4o
validated_against_model: gpt-5.5
max_active_rules: 12
---

# KB_AUDIT_V2_UPDATE_PIPELINE

```yaml
RUN_PURPOSE:
  objective: >
    Audit and patch every in-scope Special Ops prompt/workflow KB scaffold and appendix
    file against KB_Audit_v2.md, using AGENT_PIPELINE_CONTROLLER.md as the execution
    state machine and AGENT_PATCH_CONTRACT.md as the patch artifact contract.
  non_objective: >
    Do not rewrite the repository directly during the audit loop. Produce validated
    .patch.md files only, except for this operator-requested pipeline file.
```

---

## CRITICAL LOCKS

```yaml
CRITICAL_LOCKS:
  priority: critical
  rules:
    - id: LOCK-01
      rule: "Use AGENT_PIPELINE_CONTROLLER.md as the only execution state machine."
      prevents: "process drift from unrelated repo procedures"
      evidence_refs: [AGENT_PIPELINE_CONTROLLER]
    - id: LOCK-02
      rule: "Use AGENT_PATCH_CONTRACT.md as the only patch format and validation contract."
      prevents: "freehand patch generation; unverifiable mutations"
      evidence_refs: [AGENT_PATCH_CONTRACT]
    - id: LOCK-03
      rule: "Use KB_Audit_v2.md as the only KB audit policy source for file-quality decisions."
      prevents: "mixed-source audit criteria; contradictory remediation rules"
      evidence_refs: [KB_Audit_v2]
    - id: LOCK-04
      rule: "Never generate old_text from memory; copy it verbatim from the live fetched file."
      prevents: "preimage mismatch; broken search_replace patches"
      evidence_refs: [AGENT_PATCH_CONTRACT]
    - id: LOCK-05
      rule: "Never process the next target until the current target patch is written, fetched back, and validated."
      prevents: "batch drift; hidden invalid patch accumulation"
      evidence_refs: [AGENT_PIPELINE_CONTROLLER]
    - id: LOCK-06
      rule: "Halt immediately on any controller or patch-contract HALT condition."
      prevents: "silent continuation after invalid state"
      evidence_refs: [AGENT_PIPELINE_CONTROLLER, AGENT_PATCH_CONTRACT]
```

---

## SCOPE LOCK

```yaml
SCOPE_LOCK:
  repo: leela-spec/MasterOfArts
  branch: main
  include_roots:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices
  include_file_types:
    - .md
  include_scaffold_files:
    - ESSENCE.md
    - BEST_PRACTICES.md
    - MISTAKES.md
    - TEMPLATES.md
    - LEARNING_QUEUE.md
  include_appendix_files: all_markdown_files_under_appendix_root
  exclude_rules:
    - "Ignore any path segment clearly indicating new research or newly integrated research material."
    - "If an excluded research path cannot be identified exactly, do not invent a path; continue with explicit target listing and let the operator reject the list at INIT."
  forbidden_scope:
    - "Files outside target_root."
    - "Global governance files unless explicitly added by the operator."
    - "Runtime config files unless explicitly added by the operator."
```

---

## AUDIT BASIS

```yaml
AUDIT_BASIS:
  active_checks:
    - id: KB-ACHK-01
      check: "All YAML blocks parse without errors."
      fail_signal: yaml_parse_errors_detected
    - id: KB-ACHK-02
      check: "All critical-tier rules appear within the first 500 tokens."
      fail_signal: critical_rules_late_or_absent
    - id: KB-ACHK-03
      check: "Total active rule count is below configured max_active_rules."
      fail_signal: active_rule_count_exceeds_limit
    - id: KB-ACHK-04
      check: "Machine-consumed outputs reference schema-enforced structures, not prose-only instructions."
      fail_signal: prose_only_machine_output_contract
    - id: KB-ACHK-05
      check: "No duplicate or semantically paraphrased rules exist."
      fail_signal: duplicate_or_paraphrased_rules
    - id: KB-ACHK-06
      check: "Every active rule has tier, prevents, and evidence_refs fields."
      fail_signal: rule_metadata_missing
    - id: KB-ACHK-07
      check: "Active policy section contains <=100 tokens of non-YAML prose."
      fail_signal: active_policy_prose_bloat
    - id: KB-ACHK-08
      check: "Frontmatter contains version, last_validated_at, target_model_min, max_active_rules, context_mode."
      fail_signal: frontmatter_required_fields_missing
```

---

## WRITE CLASS DECISION

```yaml
WRITE_CLASS_DECISION:
  scaffold_update:
    choose_when:
      - "The live file has recoverable unique anchors."
      - "The live file has parseable or locally repairable YAML/Markdown structure."
      - "The required update can be bounded to <=10 search_replace operations."
    required_mode: search_replace
    old_text_required: true
    expected_occurrences: 1
  full_body_replace:
    choose_when:
      - "The file is new."
      - "The file has zero useful structure and cannot support safe anchors."
      - "YAML structure is unparseable and the active policy is prose-dominant."
      - "KB-ACHK-01 fails and cannot be isolated to a bounded block."
      - "KB-ACHK-02 and KB-ACHK-07 fail together with no recoverable anchors."
    authorization: operator_authorized_file_by_file_decision
    required_mode: full_body_replace
  no_op:
    choose_when:
      - "The file already passes active checks or only needs no material update."
    required_output: "closure_report entry; no patch file"
```

---

## EXECUTION STATE MACHINE

```yaml
EXECUTION_STATE_MACHINE:
  INIT:
    actions:
      - fetch_repo_file_list
      - filter_target_files_by_scope_lock
      - exclude_clear_new_research_paths
      - present_final_target_file_list_to_operator
      - await_single_batch_confirmation
    on_confirm: LOOP_START
    on_deny: HALT_OPERATOR_DENIED

  LOOP_START:
    actions:
      - select_next_unprocessed_target_file
    on_files_remaining: FETCH_LIVE_TARGET
    on_all_done: CLOSE

  FETCH_LIVE_TARGET:
    actions:
      - fetch_live_file_from_github
      - record_file_path
      - record_file_sha
      - record_fetched_at
    on_pass: AUDIT_TARGET
    on_fail: HALT_STALE_OR_MISSING_FILE

  AUDIT_TARGET:
    actions:
      - run_KB_ACHK_01_through_KB_ACHK_08
      - classify_failures
      - decide_write_class
      - record_audit_flags
    on_pass: PATCH_PLAN
    on_fail: PATCH_PLAN

  PATCH_PLAN:
    actions:
      - produce_patch_plan_yaml
      - produce_preimage_check_yaml
      - produce_search_replace_blocks_or_full_body_replace_payload
      - enforce_one_patch_file_per_target_file
      - write_patch_md_to_patch_output_root
    on_pass: VALIDATE_PATCH_FILE
    on_fail: HALT_PATCH_GENERATION_FAILED

  VALIDATE_PATCH_FILE:
    actions:
      - fetch_back_written_patch_md_from_repo
      - validate_frontmatter_yaml_present
      - validate_patch_plan_yaml_present
      - validate_preimage_check_yaml_present
      - validate_target_header_present
      - validate_delimiters_intact_for_search_replace
      - validate_old_text_occurrences_equal_1_for_each_search_replace_op
      - validate_old_text_copied_from_live_file
      - validate_full_body_replace_has_complete_new_text_when_applicable
    on_pass: LOOP_START
    on_fail: HALT_PATCH_VALIDATION_FAILED

  CLOSE:
    actions:
      - emit_closure_report_yaml
      - list_processed_files
      - list_patch_files_created
      - list_write_classes
      - list_no_op_files
      - list_halts
      - state_next_operator_step
```

---

## PATCH FILE NAMING

```yaml
PATCH_FILE_NAMING:
  output_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/patches
  filename_pattern: "TASK-XX_<targetfilename>.patch.md"
  one_patch_per_target_file: true
  line_endings: LF
  encoding: utf-8
  examples:
    - target: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
      patch: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/patches/TASK-01_BEST_PRACTICES.patch.md
    - target: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_EXAMPLE.md
      patch: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/patches/TASK-02_APPENDIX_EXAMPLE.patch.md
```

---

## PATCH FILE CONTRACT

```yaml
PATCH_FILE_CONTRACT:
  required_sections:
    - frontmatter_yaml
    - patch_plan_yaml
    - preimage_check_yaml
    - search_replace_blocks_or_full_body_replace_payload
  frontmatter_required_fields:
    - task_id
    - target_file
    - write_class
    - audit_flags
    - created_at
  search_replace_required_fields:
    - op_id
    - mode
    - old_text
    - new_text
    - expected_occurrences
    - why_authorized
  preimage_required_fields:
    - task_id
    - target_file
    - op_id
    - old_text_occurrences
    - old_text_copied_from_live_file
    - result
  delimiter_contract:
    search: "<<<<<<< SEARCH"
    separator: "======="
    replace: ">>>>>>> REPLACE"
```

---

## HALT CONDITIONS

```yaml
HALT_CONDITIONS:
  - id: H-01
    trigger: stale_or_missing_file
    action: "Report target path and stop the loop."
  - id: H-02
    trigger: patch_generation_failed
    action: "Report task_id, op_id, target path, and reason. Stop the loop."
  - id: H-03
    trigger: patch_validation_failed
    action: "Report failed validation check. Stop the loop."
  - id: H-04
    trigger: operator_denied_at_init
    action: "Output pending target list and stop."
  - id: H-05
    trigger: old_text_occurrence_count_not_equal_1
    action: "Report target path and op_id. Stop the loop."
  - id: H-06
    trigger: target_scope_ambiguity_after_file_list
    action: "Report ambiguous paths and ask operator to approve or remove them before loop start."
```

---

## FORBIDDEN ACTIONS

```yaml
FORBIDDEN_ACTIONS:
  - self_approval_of_batch_target_list
  - self_approval_of_patch_validation
  - generating_old_text_from_memory
  - paraphrasing_old_text
  - combining_multiple_target_files_in_one_patch_md
  - writing_patch_files_outside_patch_output_root
  - mutating_target_files_during_audit_loop
  - continuing_after_halt
  - importing unrelated process controllers as governing procedure
  - treating support docs as controllers
```

---

## PER FILE REPORT RECORD

```yaml
PER_FILE_REPORT_RECORD:
  task_id: ""
  target_file: ""
  file_sha: ""
  write_class: "scaffold_update | full_body_replace | no_op"
  audit_flags: []
  operations_count: 0
  patch_file: ""
  validation_result: "pass | fail | skipped"
  halt_id: ""
  notes: ""
```

---

## CLOSURE REPORT TEMPLATE

```yaml
CLOSURE_REPORT:
  pipeline_run_id: "KB-AUDIT-V2-SPECIAL-OPS-YYYYMMDD"
  date: "YYYY-MM-DD"
  repo: leela-spec/MasterOfArts
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows
  total_files_discovered: 0
  total_files_confirmed: 0
  total_files_processed: 0
  total_patches_created: 0
  total_no_op_files: 0
  total_halts: 0
  files_full_body_replace: []
  files_scaffold_update: []
  files_no_op: []
  patch_files_created: []
  halt_events:
    - file: ""
      halt_id: ""
      reason: ""
  next_step: "Operator reviews patch files, then runs or authorizes deterministic patch application."
```

---

## OPERATOR CHECKPOINTS

```yaml
OPERATOR_CHECKPOINTS:
  before_loop:
    required: true
    prompt: "Confirm final target file list and authorize per-file write_class decisions."
  during_loop:
    required: false
    rule: "Do not interrupt unless a HALT condition occurs."
  after_loop:
    required: true
    prompt: "Review closure report and authorize patch application separately."
```
