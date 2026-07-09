---
okf_schema: apex.repair_pack_readme.v1
repair_pack_id: 001-package-validation-repair
status: planned
repo: leela-spec/apexai-os-meta
branch: main
base_commit_expected: 147dc36a24bef5fa1863aef77e9a5e842f73281e
repair_pack_folder: .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair
---

# Repair Pack 001 — Package Validation Repair

```okf
mission:
  target_skill_folder: ".claude/skills/deterministic-markdown-patcher2"
  planner_role: "semantic repair-pack planner only"
  mutator_role: "scripts/patch_executor.py and scripts/fixture_runner.py"
  target_files_mutated_by_this_chat: []

diagnosis:
  - id: fixture_template_missing_runtime_files
    evidence: "templates/fixture_spec.template.json invokes patch_intent.json and patch_policy.json, but fixture_runner.py only materializes files declared in files[]."
    target_file: ".claude/skills/deterministic-markdown-patcher2/templates/fixture_spec.template.json"
    repair_intent: "intents/001-fix-fixture-template-files.patch_intent.json"
    operation: "replace-once"
    expected_validation:
      - "validate-intent exits 0"
      - "apply-intent exits 0"
      - "repaired template contains file entries for patch_intent.json and patch_policy.json"

  - id: required_python_validation_command_rejected_by_executor
    evidence: "templates/patch_policy.template.json marks a Python validation command as required, while patch_executor.py rejects validation subprocesses that are not git, rg, or yq."
    target_file: ".claude/skills/deterministic-markdown-patcher2/templates/patch_policy.template.json"
    repair_intent: "intents/002-make-python-validation-optional.patch_intent.json"
    operation: "replace-once"
    expected_validation:
      - "validate-intent exits 0"
      - "apply-intent exits 0"
      - "repaired template contains required: false"
      - "repaired template no longer contains required: true"

intentionally_not_repaired:
  - "No direct edits to SKILL.md, schemas, executor, fixture runner, or reference docs were performed by this chat."
  - "No unified diffs were authored."
  - "No full-file target replacement was planned."
  - "No optional tools, hooks, CI, mdpatch, remark, comby, fuzzy matching, table editing, sed, awk, or perl were added."
  - "Policy field naming remains schema-compatible with the current package: patch_policy.json uses full_file_rewrite:false because references/patch-policy.schema.json and scripts/patch_executor.py currently require that field."

files_created:
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/README.okf.md"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/patch_policy.json"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/fixture_spec.json"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/codex_apply_handoff.okf.md"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/intents/001-fix-fixture-template-files.patch_intent.json"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/intents/002-make-python-validation-optional.patch_intent.json"

no_target_files_mutated_by_this_chat: true
```
