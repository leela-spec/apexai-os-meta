---
okf_schema: apex.repair_pack_readme.v1
repair_pack_id: 002-executor-dirty-tree-scope-repair
status: planned
repo: leela-spec/apexai-os-meta
branch: main
base_commit_expected: 45d0a6d0d72bcd7fa3fa1d111824e6f9958d89e0
repair_pack_folder: .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair
previous_repair_pack: .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair
---

# Repair Pack 002 — Executor Dirty-Tree Scope Repair

```okf
mission:
  target_skill_folder: ".claude/skills/deterministic-markdown-patcher2"
  planner_role: "semantic repair-pack planner only"
  mutator_role: "scripts/patch_executor.py and scripts/fixture_runner.py"
  target_files_mutated_by_this_chat: []
  dirty_tree_policy: "Dirty trees are not an operator error. The executor must validate its own mutation boundary, not the global worktree."

codex_failures_repaired:
  - id: global_dirty_tree_diff_scope
    finding: "patch_executor.py inspected global git diff state, so unrelated dirty files could fail a valid intent."
    required_behavior: "Compare current diff against an execution-local baseline and validate only newly changed executor paths plus declared allowed changed paths."
  - id: post_mutation_failure_left_target_changed
    finding: "A post-mutation failure could leave executor-mutated target content behind."
    required_behavior: "Restore executor-mutated paths to their pre-run content before writing the failure report."
  - id: multi_intent_sequential_false_failure
    finding: "A later intent could treat a previous successful intent's unstaged target diff as an unallowed outstanding diff."
    required_behavior: "Each apply-intent captures its own baseline so prior successful diffs do not break later intents."
  - id: fixture_runner_cli_mismatch
    finding: "Prior handoff used positional fixture_spec.json while fixture_runner.py accepted only --spec."
    required_behavior: "fixture_runner.py accepts both positional spec path and --spec."
  - id: allow_write_cli_contract_mismatch
    finding: "apply-intent requires --allow-write but the executor contract did not state that clearly in the invocation contract."
    required_behavior: "Document --allow-write for mutation commands and keep handoff commands aligned."
  - id: report_artifact_noise
    finding: "Runtime report files were produced during execution and removed before commit."
    required_behavior: "Reports are explicit runtime artifacts under report_dir and are not committed unless intentionally staged."

repair_intents:
  - id: fix_executor_local_diff_scope
    file: ".claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py"
    operation: "replace-once"
    reason: "Replace the contiguous changed_paths / verify_diff_scope / run_validation helper block."
    expected_behavior: "Unrelated pre-existing dirty files and prior successful intent diffs do not cause false diff-scope failures."
  - id: add_executor_post_validation_rollback
    file: ".claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py"
    operation: "replace-once"
    reason: "Replace the contiguous failure / apply_intent block and add restore_executor_mutated_paths."
    expected_behavior: "Any post-mutation PatchError or unexpected exception restores executor-mutated target paths before failure reporting."
  - id: accept_fixture_runner_positional_spec
    file: ".claude/skills/deterministic-markdown-patcher2/scripts/fixture_runner.py"
    operation: "replace-once"
    reason: "Replace main() parser contract only."
    expected_behavior: "Both fixture_runner.py fixture_spec.json and fixture_runner.py --spec fixture_spec.json work."
  - id: align_executor_contract_allow_write_dirty_reports
    file: ".claude/skills/deterministic-markdown-patcher2/references/executor-contract.md"
    operation: "replace-heading-section"
    reason: "Align CLI contract with --allow-write, dirty-tree non-error policy, and report artifact policy."
    expected_behavior: "Documentation no longer implies clean-tree or omits --allow-write for mutation."

intentionally_not_repaired:
  - "No hooks were added."
  - "No check_tools.py, CI, branch workflow, PR workflow, or stashing workflow was added."
  - "No clean-tree requirement was added."
  - "No mdpatch, remark, comby, fuzzy matching, table editing, sed, awk, perl, or patch fuzz was added."
  - "No old deterministic-markdown-patcher package files were inspected or copied."
  - "No direct edits to patch_executor.py, fixture_runner.py, references, templates, or unrelated repo files were performed by this browser chat."

files_created:
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/README.okf.md"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/fixture_spec.json"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/codex_apply_handoff.okf.md"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/001-fix-executor-local-diff-scope.patch_intent.json"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/002-add-executor-rollback-on-post-validation-failure.patch_intent.json"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/003-accept-fixture-runner-positional-spec.patch_intent.json"
  - ".claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/004-align-allow-write-contract-or-handoff.patch_intent.json"

no_target_files_mutated_by_this_chat: true
```
