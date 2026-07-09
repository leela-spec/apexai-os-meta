---
okf_schema: apex.codex_apply_handoff.v1
handoff_id: deterministic_markdown_patcher2_repair_pack_002
repo: leela-spec/apexai-os-meta
branch: main
repair_pack_folder: .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair
---

```bash
git checkout main
git pull --ff-only origin main

python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json
python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/fixture_spec.json
python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/001-fix-executor-local-diff-scope.patch_intent.json
python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/002-add-executor-rollback-on-post-validation-failure.patch_intent.json
python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/003-accept-fixture-runner-positional-spec.patch_intent.json
python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/004-align-allow-write-contract-or-handoff.patch_intent.json

python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py validate-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/001-fix-executor-local-diff-scope.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/reports
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py apply-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/001-fix-executor-local-diff-scope.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/reports --allow-write
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py validate-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/002-add-executor-rollback-on-post-validation-failure.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/reports
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py apply-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/002-add-executor-rollback-on-post-validation-failure.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/reports --allow-write
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py validate-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/003-accept-fixture-runner-positional-spec.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/reports
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py apply-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/003-accept-fixture-runner-positional-spec.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/reports --allow-write
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py validate-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/004-align-allow-write-contract-or-handoff.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/reports
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py apply-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/intents/004-align-allow-write-contract-or-handoff.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/reports --allow-write

python .claude/skills/deterministic-markdown-patcher2/scripts/fixture_runner.py .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/fixture_spec.json
python .claude/skills/deterministic-markdown-patcher2/scripts/fixture_runner.py --spec .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/fixture_spec.json
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py --self-test
python .claude/skills/deterministic-markdown-patcher2/scripts/fixture_runner.py --self-test

git diff -- .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py .claude/skills/deterministic-markdown-patcher2/scripts/fixture_runner.py .claude/skills/deterministic-markdown-patcher2/references/executor-contract.md
git status --short

git add .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py .claude/skills/deterministic-markdown-patcher2/scripts/fixture_runner.py .claude/skills/deterministic-markdown-patcher2/references/executor-contract.md
git commit -m "Apply executor dirty-tree scope repair pack"
git push origin main
```

```okf
constraints:
  - "Do not stash."
  - "Do not require a clean tree."
  - "Do not create a branch or PR."
  - "Do not commit .claude/skills/deterministic-markdown-patcher2/repair-packs/002-executor-dirty-tree-scope-repair/reports unless explicitly requested."
  - "Commit only changed target files if every validate-intent, apply-intent, fixture_runner, and self-test command passes."

final_report_format:
  status: "completed | failed"
  changed_files: []
  unexpected_changed_files: []
  failures_found: []
  repairs_made: []
  commit_sha: ""
```
