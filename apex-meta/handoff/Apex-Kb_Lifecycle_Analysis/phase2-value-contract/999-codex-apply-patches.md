# Phase 2 Value Contract Patch Pack - Codex Apply Instructions

Follow these exact steps to apply the patch pack:

1. **Check out the correct repository and branch.** Clone or open the repository `leela-spec/apexai-os-meta` and work directly on the `main` branch. Do **not** create a new branch or open a pull request.

2. **Synchronize with origin.** From the repository root run:

   ```
   git checkout main
   git pull --ff-only origin main
   ```

3. **Apply the patch files in order.** Each patch must be checked and applied in ascending numeric order. From the repository root run:

   ```
   git apply --check apex-meta/patches/phase2-value-contract/001-wiki-page-templates.patch
   git apply apex-meta/patches/phase2-value-contract/001-wiki-page-templates.patch

   git apply --check apex-meta/patches/phase2-value-contract/002-ingest-analysis-template.patch
   git apply apex-meta/patches/phase2-value-contract/002-ingest-analysis-template.patch

   git apply --check apex-meta/patches/phase2-value-contract/003-kb-contract.patch
   git apply apex-meta/patches/phase2-value-contract/003-kb-contract.patch

   git apply --check apex-meta/patches/phase2-value-contract/004-ingest-query-lint-audit-rules.patch
   git apply apex-meta/patches/phase2-value-contract/004-ingest-query-lint-audit-rules.patch

   git apply --check apex-meta/patches/phase2-value-contract/005-acceptance-tests.patch
   git apply apex-meta/patches/phase2-value-contract/005-acceptance-tests.patch

   git apply --check apex-meta/patches/phase2-value-contract/006-skill.patch
   git apply apex-meta/patches/phase2-value-contract/006-skill.patch

   git apply --check apex-meta/patches/phase2-value-contract/007-lifecycle-state-machine.patch
   git apply apex-meta/patches/phase2-value-contract/007-lifecycle-state-machine.patch

   git apply --check apex-meta/patches/phase2-value-contract/008-knowledge-promotion-rules.patch
   git apply apex-meta/patches/phase2-value-contract/008-knowledge-promotion-rules.patch

   git apply --check apex-meta/patches/phase2-value-contract/009-kb-schema-template.patch
   git apply apex-meta/patches/phase2-value-contract/009-kb-schema-template.patch
   ```

4. **Validate the result.** After applying all patches run:

   ```
   grep -R "Adaptive Ranked Source Set" -n .claude/skills/apex-kb/
   grep -R "Macro / Meso / Micro" -n .claude/skills/apex-kb/
   grep -R "Routes Here" -n .claude/skills/apex-kb/
   grep -R "Uncertainty / Raw Source Triggers" -n .claude/skills/apex-kb/
   grep -R "page_value_score" -n .claude/skills/apex-kb/ && exit 1 || true
   grep -R "source_cluster_map" -n .claude/skills/apex-kb/ && exit 1 || true
   git diff --name-only
   ```

   The first four greps should find multiple occurrences of the required section headings. The next two greps must return no matches, confirming that neither `page_value_score` nor `source_cluster_map` appear in the codebase. The `git diff --name-only` output should list only the nine target files.

5. **Commit and push the changes.** Once validation passes, commit the updated target files and push directly to `main`:

   ```
   git commit -am "Apply Phase 2 value contract patches"
   git push origin main
   ```

These instructions ensure the Phase 2 value contract patches are applied cleanly to the `main` branch without introducing any extraneous changes.
