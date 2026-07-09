---
okf_schema: apex.codex_apply_handoff.v1
handoff_id: deterministic_markdown_patcher2_repair_pack_001
repo: leela-spec/apexai-os-meta
branch: main
repair_pack_folder: .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair
---

```bash
git checkout main
git pull --ff-only origin main

python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/patch_policy.json
python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/fixture_spec.json
python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/intents/001-fix-fixture-template-files.patch_intent.json
python -m json.tool .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/intents/002-make-python-validation-optional.patch_intent.json

python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py validate-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/intents/001-fix-fixture-template-files.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/reports
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py apply-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/intents/001-fix-fixture-template-files.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/reports --allow-write
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py validate-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/intents/002-make-python-validation-optional.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/reports
python .claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py apply-intent --intent .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/intents/002-make-python-validation-optional.patch_intent.json --policy .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/patch_policy.json --repo . --report-dir .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/reports --allow-write

python .claude/skills/deterministic-markdown-patcher2/scripts/fixture_runner.py --spec .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair/fixture_spec.json

git diff -- .claude/skills/deterministic-markdown-patcher2/templates/fixture_spec.template.json .claude/skills/deterministic-markdown-patcher2/templates/patch_policy.template.json .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair
git status --short

git add .claude/skills/deterministic-markdown-patcher2/templates/fixture_spec.template.json .claude/skills/deterministic-markdown-patcher2/templates/patch_policy.template.json .claude/skills/deterministic-markdown-patcher2/repair-packs/001-package-validation-repair
git commit -m "Apply deterministic markdown patcher repair pack"
git push origin main
```

```okf
constraints:
  - "Repair only failed repair-pack files or target files touched by successful intents."
  - "Do not manually edit target files outside the executor flow."
  - "Do not commit or push unless every validate-intent, apply-intent, and fixture_runner command passes."

final_report_format:
  status: "completed | failed"
  commit_sha: ""
  successful_intents: []
  failed_commands: []
  target_files_mutated: []
```
