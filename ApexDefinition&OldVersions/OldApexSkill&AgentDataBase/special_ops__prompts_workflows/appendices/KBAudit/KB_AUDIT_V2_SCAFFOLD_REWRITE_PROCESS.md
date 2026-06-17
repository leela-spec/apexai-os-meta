---
class: kb_audit_v2_scaffold_rewrite_process
role: SPECIAL_OPS_KB_AUDIT_V2_FULL_SCAFFOLD_RETROFIT_CONTROLLER
surface: repo_process_pipeline
version: "1.0"
created_at: "2026-05-07"
last_validated_at: "2026-05-07"
context_mode: compact
status: active_for_restart
scope: special_ops__prompts_workflows_5_scaffold_full_kb_audit_v2_rewrite
target_repo: leela-spec/MasterOfArts
target_branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows
patch_output_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/patches
source_contracts:
  - AGENT_PIPELINE_CONTROLLER.md
  - AGENT_PATCH_CONTRACT.md
  - KB_Audit_v2.md
  - KB_AUDIT_V2_PROMPT_PACKET_MODE.md
target_model_min: gpt-4o
validated_against_model: gpt-5.5
max_active_rules: 12
supersedes_for_restart:
  - KB_AUDIT_V2_UPDATE_PIPELINE.md
  - KB_AUDIT_V2_PROMPT_PACKET_MODE.md
  - TASK-01_BEST_PRACTICES.patch.md
  - TASK-02_MISTAKES.patch.md
  - TASK-03_TEMPLATES.patch.md
  - TASK-04_LEARNING_QUEUE.patch.md
  - TASK-05_ESSENCE.patch.md
---

# KB_AUDIT_V2_SCAFFOLD_REWRITE_PROCESS

```yaml
RESTART_OBJECTIVE:
  objective: >
    Restart the Special Ops Prompts Workflows scaffold update as a full KB_Audit_v2
    compliance retrofit for the five scaffold files. The goal is not to add one compact
    concept per file. The goal is to rewrite or substantially patch each scaffold file
    so it is more token-efficient, machine-readable, drift-resistant, and structurally
    aligned with KB_Audit_v2.
  correction_from_failed_run: >
    The prior run incorrectly treated KB_Audit_v2 as a concept-integration source and
    produced small additive entries. That is insufficient. The restart must evaluate
    each scaffold file as an artifact that itself needs to satisfy the KB_Audit_v2
    design standard as far as its scaffold role allows.
```

---

## CRITICAL LOCKS

```yaml
CRITICAL_LOCKS:
  priority: critical
  rules:
    - id: RLOCK-01
      tier: critical
      rule: "Use KB_Audit_v2.md as the structural writing standard for the target files, not merely as a source of new entries."
      prevents: "small symbolic additions that fail to improve machine-readability or drift resistance"
      evidence_refs: [KB_Audit_v2]
    - id: RLOCK-02
      tier: critical
      rule: "Default to full_body_replace when a scaffold file's overall structure is prose-dominant, metadata-light, or not meaningfully KB_Audit_v2-compliant."
      prevents: "under-patching files that need structural retrofit"
      evidence_refs: [KB_Audit_v2, AGENT_PIPELINE_CONTROLLER]
    - id: RLOCK-03
      tier: critical
      rule: "Use scaffold_update only when the existing file already has a mostly compliant machine-readable structure and bounded repairs are sufficient."
      prevents: "choosing search_replace only because it is safer, when it cannot accomplish the requested rewrite"
      evidence_refs: [AGENT_PATCH_CONTRACT]
    - id: RLOCK-04
      tier: critical
      rule: "For each target file, produce a portable executor prompt packet; the controller does not directly author the patch unless the operator explicitly overrides prompt-packet mode."
      prevents: "controller/executor role collapse and recurrence of the prior process mismatch"
      evidence_refs: [KB_AUDIT_V2_PROMPT_PACKET_MODE]
    - id: RLOCK-05
      tier: critical
      rule: "The executor must fetch the live file, decide write_class, create exactly one patch file, fetch it back, and return a structured summary."
      prevents: "stale preimage, multi-file drift, and unvalidated completion"
      evidence_refs: [AGENT_PIPELINE_CONTROLLER, AGENT_PATCH_CONTRACT]
    - id: RLOCK-06
      tier: critical
      rule: "Do not preserve existing prose or entry shape merely because it exists; preserve only content that remains useful after conversion into compact YAML-first scaffold structure."
      prevents: "legacy structure bias and superficial compliance"
      evidence_refs: [KB_Audit_v2]
```

---

## TARGET SET

```yaml
TARGET_SET:
  scope: five_scaffold_files_only
  target_files:
    - task_id: RESTART-01
      file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
      expected_write_class: full_body_replace_or_large_scaffold_update
    - task_id: RESTART-02
      file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
      expected_write_class: full_body_replace_or_large_scaffold_update
    - task_id: RESTART-03
      file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
      expected_write_class: full_body_replace_or_large_scaffold_update
    - task_id: RESTART-04
      file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/LEARNING_QUEUE.md
      expected_write_class: full_body_replace_or_large_scaffold_update
    - task_id: RESTART-05
      file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
      expected_write_class: full_body_replace_or_large_scaffold_update
  excluded:
    - appendices/*
    - NewResearchBecauseOfConstantFailure/*
    - existing TASK-01_to_TASK-05 patch files except as superseded history
```

---

## REQUIRED STRUCTURAL STANDARD

```yaml
REQUIRED_STRUCTURAL_STANDARD:
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
  first_500_tokens:
    required_content:
      - critical_path_or_critical_rules_yaml
      - file_purpose_yaml
      - scope_or_boundary_yaml
  active_policy:
    format: parse_valid_yaml_first
    prose_budget_tokens: 100
    requirements:
      - critical_or_required_rules_have_tier
      - rule_like_entries_have_prevents
      - rule_like_entries_have_evidence_refs
      - machine_consumed_templates_have_schema_or_contract_fields
      - entries_are_not_duplicated_as prose
  evidence_and_detail:
    rule: "Keep long evidence, examples, research notes, and explanations in appendices or evidence_refs; do not bloat scaffold active policy."
  output_contracts:
    rule: "Any machine-consumed output template must include explicit schema/fields/validation, not only prose instructions."
  density:
    rule: "Prefer compact YAML entries and stable IDs over narrative paragraphs."
```

---

## FILE-SPECIFIC RETROFIT INTENT

```yaml
FILE_SPECIFIC_RETROFIT_INTENT:
  BEST_PRACTICES.md:
    target_role: accepted_practices_scaffold
    required_change: >
      Convert accepted practice content into a frontmatter + critical path + parse-valid YAML
      practice registry. Preserve useful existing practice IDs, but rewrite entries into a more
      machine-readable form with tier/prevents/evidence_refs where applicable.
    not_enough: "Adding PW-BP-012 only."

  MISTAKES.md:
    target_role: accepted_failure_patterns_scaffold
    required_change: >
      Convert accepted mistake patterns into a frontmatter + critical path + parse-valid YAML
      mistake registry with trigger, countermeasure, prevents, evidence_refs, and scoring fields.
      Add KB_Audit_v2 failure modes as part of the registry, not merely as a loose appended item.
    not_enough: "Adding PW-MK-012 only."

  TEMPLATES.md:
    target_role: reusable_templates_scaffold
    required_change: >
      Convert templates into a frontmatter + critical path + parse-valid YAML template registry.
      Ensure templates intended for machine use declare input fields, output fields, validation gates,
      halt conditions, and schema/contract requirements.
    not_enough: "Adding PW-TPL-011 only."

  LEARNING_QUEUE.md:
    target_role: candidate_only_learning_scaffold
    required_change: >
      Convert candidate entries into a frontmatter + critical path + parse-valid YAML queue registry
      with candidate status, promotion boundary, overlap check, validation owner, evidence_refs,
      and explicit non-promotion guardrails.
    not_enough: "Adding PW-LQ-012 only."

  ESSENCE.md:
    target_role: compact_activation_doctrine
    required_change: >
      Add frontmatter and a compact YAML-first activation block that names boundaries, default
      sequence, critical doctrine, and KB audit discipline while preserving ESSENCE as the shortest
      scaffold file. Use minimal prose after YAML.
    not_enough: "Adding one doctrine bullet only."
```

---

## WRITE CLASS DECISION

```yaml
WRITE_CLASS_DECISION:
  full_body_replace:
    prefer_when:
      - "File lacks YAML frontmatter required by KB_Audit_v2."
      - "Most active content is Markdown bullets/prose instead of parse-valid YAML."
      - "Retrofitting requires changing many entries or section order."
      - "A bounded search_replace patch would leave the file structurally non-compliant."
    required_patch_contract:
      - write_class: full_body_replace
      - old_text: omit
      - new_text: complete_file_content
      - search_replace_block: omit
      - diff_audit_still_required: true
  scaffold_update:
    allow_when:
      - "The file already has compliant frontmatter and YAML-first active policy."
      - "Only a small bounded repair is needed."
      - "old_text from live file occurs exactly once."
    required_patch_contract:
      - write_class: scaffold_update
      - mode: search_replace
      - old_text_verbatim_from_live_file: true
      - expected_occurrences: 1
  no_op:
    allow_when:
      - "File already satisfies KB_Audit_v2 materially."
    required_report: "Explain why no patch is necessary; likely rare for this restart."
```

---

## PROMPT PACKET LOOP

```yaml
PROMPT_PACKET_LOOP:
  controller_actions_per_file:
    - fetch_live_target_file
    - summarize current structural deficiencies
    - generate portable executor prompt packet
    - include exact target, output path, source contracts, structural standard, write-class decision logic, required summary schema
  executor_actions_per_file:
    - fetch_live_target_file
    - audit against KB_Audit_v2
    - choose write_class with reason
    - create exactly one patch file
    - fetch back patch file
    - validate contract
    - return EXECUTOR_PATCH_SUMMARY
  controller_resume_actions:
    - fetch_back_patch_file
    - verify summary against patch artifact
    - inspect plausibility against full retrofit objective, not just delimiter validity
    - continue_or_halt
```

---

## PLAUSIBILITY GATE

```yaml
PLAUSIBILITY_GATE:
  required_after_patch_validation: true
  checks:
    - id: PG-01
      check: "Patch materially changes file structure toward KB_Audit_v2 compliance, not just adding one concept."
      fail_action: halt_or_reprompt
    - id: PG-02
      check: "Patch adds or preserves required frontmatter unless file role explicitly forbids it."
      fail_action: halt_or_reprompt
    - id: PG-03
      check: "Active scaffold content is YAML-first and more machine-readable after patch."
      fail_action: halt_or_reprompt
    - id: PG-04
      check: "Existing useful content is compressed, normalized, or mapped into the new schema rather than blindly discarded."
      fail_action: revise
    - id: PG-05
      check: "Patch does not simply append a KB_Audit_v2 item while leaving legacy structure unchanged."
      fail_action: halt_or_reprompt
```

---

## HALT CONDITIONS

```yaml
HALT_CONDITIONS:
  - id: RH-01
    trigger: "executor produces small additive patch that fails plausibility gate"
    action: "HALT and regenerate stricter prompt packet."
  - id: RH-02
    trigger: "executor modifies target file directly instead of patch file"
    action: "HALT."
  - id: RH-03
    trigger: "executor creates multiple target patches in one task"
    action: "HALT."
  - id: RH-04
    trigger: "patch file missing required contract sections"
    action: "HALT or request format repair before plausibility review."
  - id: RH-05
    trigger: "full_body_replace lacks complete replacement body"
    action: "HALT."
```

---

## FORBIDDEN ACTIONS

```yaml
FORBIDDEN_ACTIONS:
  - treating KB_Audit_v2 as a source for one appended rule only
  - preserving old scaffold shape when it blocks machine readability
  - applying TASK-01_to_TASK-05 as final without full retrofit review
  - bypassing prompt-packet mode
  - processing appendices during this restart
  - modifying target files directly
  - skipping plausibility gate
  - closing from delimiter/preimage validation alone when structural retrofit was required
```

---

## EXECUTOR SUMMARY SCHEMA

```yaml
EXECUTOR_PATCH_SUMMARY_SCHEMA:
  required_block: EXECUTOR_PATCH_SUMMARY
  required_fields:
    task_id: ""
    target_file: ""
    target_file_sha: ""
    patch_file: ""
    patch_file_sha: ""
    write_class: "full_body_replace | scaffold_update | no_op"
    audit_flags: []
    structural_changes:
      frontmatter_added_or_rewritten: false
      yaml_first_active_policy: false
      rule_metadata_added: false
      schema_contracts_added: false
      prose_reduced_or_moved: false
      duplicate_or_overlap_controls_added: false
    content_preservation:
      existing_ids_preserved_or_mapped: []
      existing_ids_removed: []
      removal_reason: ""
    validation:
      patch_file_created: false
      patch_file_fetch_back: "pass | fail"
      patch_contract_sections: "pass | fail"
      write_class_contract: "pass | fail"
      plausibility_gate_self_check: "pass | fail"
    halt:
      occurred: false
      halt_id: ""
      reason: ""
    next_recommended_controller_action: "validate_patch_and_continue | halt | ask_operator"
```

---

## CLOSURE STANDARD

```yaml
CLOSURE_STANDARD:
  close_only_when:
    - "All five scaffold files have validated patch artifacts."
    - "All five pass plausibility gate."
    - "Any superseded small patches are explicitly marked as superseded in closure."
    - "Closure report distinguishes patch-format validation from structural-compliance plausibility."
  next_step_after_close: "Operator applies only the restarted full-retrofit patch set, not the superseded minimal patch set."
```
