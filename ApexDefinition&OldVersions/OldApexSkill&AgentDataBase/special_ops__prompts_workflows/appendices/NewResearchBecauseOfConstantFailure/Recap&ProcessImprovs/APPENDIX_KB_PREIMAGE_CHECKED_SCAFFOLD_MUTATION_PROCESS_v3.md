---
class: appendix
role: PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS
surface: agent_kb_appendix
quality: accepted
scope: agent
purpose: define the preimage-checked scaffold mutation process
status: active
version: 2.0
validated_against_model: gpt-5.5
context_mode: compact
created_at: 2026-05-07
owner: special_ops__prompts_workflows
validator: meta_ops
task_id: TASK-13
target_agent: special_ops__prompts_workflows
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
---

# APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS

---

## CRITICAL_PATH
```yaml
CRITICAL_PATH:
  priority: critical
  rules:
    - "NEVER apply to existing file without fetching live content first"
    - "NEVER write if old_text occurrences != 1 — HALT patch_check_fail"
    - "ALWAYS fetch-back and diff-audit after every write"
  note: "These three rules override all other instructions if context compresses."
```

---

## SCORING_SEMANTICS
```yaml
SCORING_SEMANTICS:
  risk_if_unfixed:
    scale: 1-100
    meaning: danger if this change is NOT made; higher = more urgent
  evidence_strength:
    scale: 1-100
    meaning: confidence level based on external validation
  impact_if_fixed:
    scale: 1-100
    meaning: practical reliability gain if change is applied
```

---

## 1. Core distinction
```yaml
mechanism_truth:
  github_storage: deterministic
  git_diff_computation: deterministic
  ai_replacement_content_construction: probabilistic
  primary_risk_surface: between_live_file_fetch_and_write_submission
  required_control_for_critical_scaffold: preimage_checked_patch_before_write
  consequence:
    full_file_content_can_be_submitted: true
    resulting_diff_can_still_be_localized: true
    localized_diff_does_not_prove_atomic_search_replace_was_used: true
    whole_file_blob_replacement_does_not_itself_mean_semantic_drift_occurred: true
```

---

## 2. Execution state machine
```yaml
EXECUTION_STATE_MACHINE:
  PREPARE:
    actions: [fetch_live_file, record_sha]
    on_pass: VALIDATE
  VALIDATE:
    actions: [preimage_check, occurrence_count]
    on_pass: APPLY
    on_fail: HALT
  APPLY:
    actions: [deterministic_replace, write_with_sha]
    on_pass: VERIFY
    on_fail: HALT
  VERIFY:
    actions: [fetch_back, diff_audit, verify_gate]
    on_pass: CLOSE
    on_fail: ALERT_OPERATOR
```

---

## 3. Mandatory hard stops (execute in order, do not skip)
```yaml
MANDATORY_STEPS:
  - step: 1
    priority: critical
    action: fetch_live_target_file
    on_fail: "HALT stale_file"

  - step: 2
    priority: critical
    action: copy_old_text_verbatim_from_fetched_file
    constraint: no_paraphrase_no_memory_reconstruction
    on_fail: "HALT invalid_old_text"

  - step: 3
    priority: critical
    action: count_old_text_occurrences_in_fetched_file
    expected_occurrences: 1
    on_zero: "HALT patch_check_fail"
    on_multiple: "HALT patch_check_fail"

  - step: 4
    priority: critical
    action: apply_deterministic_replacement_in_memory
    constraint: first_and_only_occurrence
    on_fail: "HALT apply_failed"

  - step: 5
    priority: critical
    action: write_result_to_repository_with_current_sha
    then: fetch_back_and_run_diff_audit
    on_sha_conflict: "re-fetch and restart from step 1"
    on_verify_fail: "HALT alert_operator_do_not_auto_retry"
```

```yaml
OPTIONAL_STEPS:
  - draft_patch_plan_before_applying
  - verify_anchor_unique_in_file
  - run_ast_or_syntax_check_before_write
  - run_verify_gate_after_write
  - emit_artifact_closure_block
  - update_frame_state_via_state_keeper
  - run_hygiene_check_on_changed_file_set
  - check_for_external_claim_promotion
  - confirm_no_unrelated_hunks_in_diff
  - record_live_file_sha_before_write
```

---

## 4. Active contract sets by task type
```yaml
ACTIVE_CONTRACT_SETS_BY_TASK_TYPE:
  appendix_create:
    required:
      - FRAME_BLOCK
      - TASK_PAYLOAD
      - ARTIFACT_CLOSURE
      - fetch_back
  scaffold_update:
    required:
      - FRAME_BLOCK
      - TASK_PAYLOAD
      - PATCH_PLAN
      - PREIMAGE_CHECK
      - DIFF_AUDIT
      - ARTIFACT_CLOSURE
  full_body_authorized:
    required:
      - FRAME_BLOCK
      - explicit_full_body_authorization
      - changed_file_set_review
      - fetch_back
      - DIFF_AUDIT
      - ARTIFACT_CLOSURE
```

---

## 5. PATCH_PLAN contract (merged PATCH_PLAN + SEARCH_REPLACE_BLOCK)
```yaml
PATCH_PLAN:
  task_id: TASK-XX
  priority: critical
  target_file: exact/repo/relative/path.md
  task_scope: one atomic scope sentence
  target_root: "<path>"
  write_class: scaffold_update | appendix_update | file_update | full_body_replace
  source_evidence:
    - exact source file path
  operations:
    - op_id: OP-01
      priority: critical | required | recommended
      mode: search_replace | append_after_anchor | append_before_anchor | full_body_replace
      anchor: exact unique anchor copied from live file
      old_text: |
        exact verbatim text copied from live fetched file
      old_text_constraints:
        on_zero_matches: "HALT patch_check_fail"
        on_multiple_matches: "HALT patch_check_fail"
        on_paraphrased_or_reconstructed: "HALT invalid_old_text"
      new_text: |
        intended replacement or insertion text
      expected_occurrences: 1
      why_authorized: task instruction plus source evidence ref
      forbidden_side_effects:
        - unrelated_cleanup
        - silent_rewrite
        - external_claim_promotion
        - scaffold_mutation_outside_task
```

```yaml
PATCH_PLAN_EXAMPLE:
  task_id: TASK-14
  target_file: appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
  task_scope: Add preimage-check guardrail to patch transport appendix.
  write_class: appendix_update
  source_evidence:
    - appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md
  operations:
    - op_id: OP-01
      priority: required
      mode: append_after_anchor
      anchor: "## Transport protocol selection"
      old_text: |
        ## Transport protocol selection
      new_text: |
        ## Transport protocol selection
        - "For critical scaffold: require preimage_checked_patch unless full_body_replace is explicitly authorized."
      expected_occurrences: 1
      why_authorized: TASK-14 instruction plus this appendix as source evidence
```

---

## 6. PREIMAGE_CHECK contract
```yaml
PREIMAGE_CHECK:
  task_id: TASK-XX
  target_file: exact/repo/relative/path.md
  live_file_sha:
    value: blob_sha_from_fetch_file
    on_changed_before_write: "HALT stale_file"
  operation_id: OP-01
  old_text_occurrences:
    value: 0 | 1 | multiple
    on_zero: "HALT patch_check_fail"
    on_multiple: "HALT patch_check_fail"
  expected_occurrences: 1
  anchor_unique:
    value: true | false
    on_false: "HALT patch_check_fail"
  old_text_copied_from_live_file:
    value: true | false
    on_false: "HALT invalid_old_text"
  line_endings_preserved: true | false
  result: pass | halt
```

---

## 7. VERIFY_GATE contract (merged META_DETECTIVE + HYGIENE_CLEAN)
```yaml
VERIFY_GATE:
  task_id: TASK-XX
  priority: required
  source_authority_checked:
    value: true | false
    on_false: revise
  executor_not_self_approving:
    value: true | false
    on_false: "HALT self_approval_forbidden"
  changed_file_set_correct:
    value: true | false
    on_false: "HALT wrong_file_changed"
  no_unrelated_hunks:
    value: true | false
    on_false: revise
  no_external_claim_promotion:
    value: true | false
    on_false: "HALT external_claim_unverified"
  structural_integrity:
    value: pass | fail
    on_fail: "HALT structural_drift"
  result: pass | revise | halt | escalate
```

---

## 8. DIFF_AUDIT contract
```yaml
DIFF_AUDIT:
  task_id: TASK-XX
  priority: required
  commit_sha_after: commit_sha
  target_file: exact/repo/relative/path.md
  changed_files:
    - exact/repo/relative/path.md
  allowed_hunks:
    - OP-01
  unrelated_hunks_present:
    value: false
    on_true: "HALT unrelated_drift_detected"
  existing_entries_preserved: true
  external_claims_not_promoted: true
  semantic_diff_matches_patch_plan: true
  result: pass | halt
  interpretation_rule: >
    A localized Git diff proves old and new blobs differ locally.
    It does not prove preimage-checked mutation occurred unless
    PATCH_PLAN + PREIMAGE_CHECK + DIFF_AUDIT are all present.
```

---

## 9. ARTIFACT_CLOSURE contract
```yaml
ARTIFACT_CLOSURE:
  task_id: TASK-XX
  priority: required
  write_mode: search_replace_preimage_checked | full_body_create | full_body_authorized
  target_file: exact/repo/relative/path.md
  live_file_sha_before: sha
  commit_sha_after: sha
  fetch_back:
    value: pass | fail
    on_fail: "HALT alert_operator"
  diff_audit: pass | halt
  verify_gate: pass | revise | halt | escalate
  next_task: TASK-XX | none
```

---

## 10. Full-body replacement rules
```yaml
full_body_replacement:
  allowed:
    new_file_creation: true
    explicit_full_body_task_authorization: true
    generated_file_where_whole_content_is_artifact: true
    very_small_file_manually_verifiable: conditional
    emergency_recovery_with_operator_confirmation: conditional
  forbidden_by_default:
    existing_scaffold_with_accepted_doctrine: true
    long_file_or_many_accepted_entries: true
    unclear_or_repeated_anchors: true
    broad_cleanup_or_harmonize_instruction: true
    missing_verifier: true
    missing_preimage_check: true
    external_or_runtime_claim_insertion: true
  even_when_allowed:
    git_diff_and_fetch_back_remain_mandatory: true
  model_change_policy:
    revalidate_on_model_change: true
    reason: model_outputs_are_non_deterministic_pin_and_retest_on_upgrade
```

---

## 11. Break conditions for full-file update
```yaml
whole_file_update_risk_rule:
  if_existing_file_has_accepted_doctrine: prefer_preimage_checked_patch
  if_file_is_long_or_anchor_ambiguous: require_patch_plan_or_halt
  if_full_body_not_explicitly_authorized: full_body_replacement_forbidden
  break_conditions:
    long_file_near_context_limits: ai_omits_sections
    many_similar_anchors: wrong_location_replaced
    broad_instruction: unrelated_content_rewritten
    no_exact_old_text: patch_intent_floats_free
    no_occurrence_count: duplicate_anchor_allows_unintended_replacement
    no_pre_write_dry_run: write_before_mismatch_detected
    no_changed_file_set_review: other_files_changed_unnoticed
    no_commit_diff_inspection: semantic_drift_accepted
    operator_accepts_closure_without_evidence: false_validation
```

---

## 12. Allowed/forbidden promotion claims
```yaml
promotion_rules:
  allowed_claims:
    - GitHub stored a new blob for the submitted file content
    - Git diff showed localized semantic changes
    - Changed file set contained only the authorized target file
  forbidden_without_evidence:
    - A true in-place search/replace engine was used
    - A standalone patch file was created
    - The file was not mechanically rewritten as a new blob
    - Preimage matching occurred before write
```

---

## 13. Next tasks
```yaml
NEXT_TASKS:
  - id: TASK-14
    target: appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
    scope: Add explicit mechanical GitHub write vs semantic diff and preimage-check guardrail.

  - id: TASK-15
    target: appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
    scope: Add PATCH_PLAN, PREIMAGE_CHECK, and DIFF_AUDIT as required contracts for file_update and scaffold_update.

  - id: TASK-16
    target: TEMPLATES.md
    scope: Add compact preimage-checked patch-plan template pointer only.

  - id: TASK-17
    target: MISTAKES.md
    scope: Add failure pattern for mistaking localized Git diff for pre-write bounded mutation proof.

  - id: TASK-18
    target: BEST_PRACTICES.md
    scope: Add compact best practice requiring preimage-checked patching for accepted scaffold mutation unless full-body replacement is explicitly authorized.

  - id: TASK-19
    target: LEARNING_QUEUE.md
    scope: Add candidate-only item for executable tooling tests and owner validation.
```

---

## 14. Task-13 closure scope record
```yaml
task_scope_record:
  task_id: TASK-13
  task_type: appendix_create
  version: "2.0"
  scope: >
    Define the preimage-checked scaffold mutation process and the GitHub
    full-file replacement vs localized diff distinction. Optimized for
    machine readability and token efficiency. All YAML blocks parse-valid.
  scaffold_mutation: none
  external_claim_promotion: none
  changes_from_v1:
    - CRITICAL_PATH block added at document top
    - SCORING_SEMANTICS block added for consistent metric definition
    - "15-step process collapsed to 5 mandatory hard stops + optional guidance"
    - PATCH_PLAN and SEARCH_REPLACE_BLOCK merged into single PATCH_PLAN contract
    - META_DETECTIVE_COMPLIANCE_GATE and HYGIENE_CLEAN merged into VERIFY_GATE
    - All inline on_fail fields use object shape for YAML validity
    - "8-phase operator flow replaced with 4-state EXECUTION_STATE_MACHINE"
    - Section 3 Git object model removed
    - Section 4.3 wording discipline lists removed
    - Section 2 prose table removed, mechanism_truth YAML retained
    - priority field added to all contracts and steps
    - Example block added to PATCH_PLAN
    - "context_mode: compact, version: 2.0, validated_against_model: gpt-5.5 in frontmatter"
    - Section 17 future map table replaced with compact NEXT_TASKS YAML list
    - ACTIVE_CONTRACT_SETS_BY_TASK_TYPE added for task-scoped contract loading
    - model_change_policy added with revalidate_on_model_change flag
```
