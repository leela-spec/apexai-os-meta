---
task_id: TASK-05
target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
write_class: scaffold_update
audit_flags: [KB-ACHK-04, KB-ACHK-06, KB-ACHK-07, KB-ACHK-08]
created_at: 2026-05-07
---

PATCH_PLAN:
  task_id: TASK-05
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
  target_file_sha: "21021bff7b921a0bba234e705c3a945b50f0806c"
  write_class: scaffold_update
  operations:
    - op_id: OP-01
      priority: critical
      mode: search_replace
      old_text: |
        - **Verify before trust:** use read-back, diff, file-state check, checklist, evidence, or test before reporting completion.
        - **Patch/write mode by context:** patch stable local defects; use full final body or live-edit instruction when diff transport is fragile.
      new_text: |
        - **Verify before trust:** use read-back, diff, file-state check, checklist, evidence, or test before reporting completion.
        - **KB audit discipline:** encode active KB rules, checks, and templates as compact parse-valid YAML with explicit metadata; keep evidence prose out of active policy; require schema-enforced machine outputs and fetch-back validation for patch artifacts.
        - **Patch/write mode by context:** patch stable local defects; use full final body or live-edit instruction when diff transport is fragile.
      expected_occurrences: 1
      why_authorized: "KB audit checks require essence-level compression of parse-valid active policy, rule metadata, schema-enforced machine outputs, and patch fetch-back validation."

PREIMAGE_CHECK:
  task_id: TASK-05
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
  op_id: OP-01
  old_text_occurrences: 1
  old_text_copied_from_live_file: true
  result: pass

## target: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md

<<<<<<< SEARCH
- **Verify before trust:** use read-back, diff, file-state check, checklist, evidence, or test before reporting completion.
- **Patch/write mode by context:** patch stable local defects; use full final body or live-edit instruction when diff transport is fragile.
=======
- **Verify before trust:** use read-back, diff, file-state check, checklist, evidence, or test before reporting completion.
- **KB audit discipline:** encode active KB rules, checks, and templates as compact parse-valid YAML with explicit metadata; keep evidence prose out of active policy; require schema-enforced machine outputs and fetch-back validation for patch artifacts.
- **Patch/write mode by context:** patch stable local defects; use full final body or live-edit instruction when diff transport is fragile.
>>>>>>> REPLACE
