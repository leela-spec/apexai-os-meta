# Phase 2 Value Contract Patch Pack Manifest

## Repository and Branch
- **Repository:** leela-spec/apexai-os-meta
- **Branch:** main

## Source Plan
- Primary plan file read: `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/Apex KB Phase 2 Minimal Value Contract - MacroMeso Change Plan.md`
- Repair file read: `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/Apex KB Phase 2 Repair.txt` (not found during this run)

## Target Files
- `.claude/skills/apex-kb/templates/wiki-page-templates.md`
- `.claude/skills/apex-kb/templates/ingest-analysis-template.md`
- `.claude/skills/apex-kb/references/kb-contract.md`
- `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`
- `.claude/skills/apex-kb/references/acceptance-tests.md`
- `.claude/skills/apex-kb/SKILL.md`
- `.claude/skills/apex-kb/references/lifecycle-state-machine.md`
- `.claude/skills/apex-kb/references/knowledge-promotion-rules.md`
- `.claude/skills/apex-kb/templates/kb-schema-template.md`

## Patch Files
- `001-wiki-page-templates.patch` modifies wiki page templates to introduce sections: Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims (modified), Routes Here, and Uncertainty / Raw Source Triggers across summary, concept, and entity page templates.
- `002-ingest-analysis-template.patch` renames the contradictions/open questions section in the ingest analysis template to Uncertainty / Raw Source Triggers and updates YAML accordingly.
- `003-kb-contract.patch` extends the KB contract with a new page value contract for Phase 2 compiled pages, detailing required sections and guidelines; ensures no fixed source cap and optional source cluster map; prohibits rigid schemas and page-level score metrics.
- `004-ingest-query-lint-audit-rules.patch` updates ingest/query/lint/audit rules to integrate the new value contract: exposes uncertainties in the contradiction rule, updates phase 1 and phase 2 descriptions, and mandates the Phase 2 page value contract.
- `005-acceptance-tests.patch` updates the sample compiled page in acceptance tests to include the new contract sections (Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, Uncertainty / Raw Source Triggers).
- `006-skill.patch` updates the apex-kb skill description, procedure, failure behavior, and completion gate to reflect the new Phase 2 page value contract and unify contradictions into uncertainties.
- `007-lifecycle-state-machine.patch` updates the lifecycle state machine’s S6_phase2_ready goal to specify the Phase 2 page value contract and updates the maintenance state to mention uncertainties instead of contradictions.
- `008-knowledge-promotion-rules.patch` adjusts the knowledge promotion rules to note that reviewed candidates are checked for contradictions or uncertainties.
- `009-kb-schema-template.patch` updates the KB schema template taxonomy to replace `contradictions` and `open_questions` with `uncertainty_raw_source_triggers` and updates operator review policy to `uncertainty_handling`.

## Patch-to-Target Map

| Patch File | Target File | Purpose |
|-----------|-------------|---------|
| 001-wiki-page-templates.patch | `.claude/skills/apex-kb/templates/wiki-page-templates.md` | Introduce Phase 2 value contract sections (Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, Uncertainty / Raw Source Triggers) for summary, concept, and entity page templates. |
| 002-ingest-analysis-template.patch | `.claude/skills/apex-kb/templates/ingest-analysis-template.md` | Rename contradictions/open questions section to Uncertainty / Raw Source Triggers in Phase 1 ingest analysis template. |
| 003-kb-contract.patch | `.claude/skills/apex-kb/references/kb-contract.md` | Add a page value contract for Phase 2 compiled pages; specify mandatory sections; forbid fixed source caps and score metrics; emphasise adaptive ranking and macro/meso/micro synthesis. |
| 004-ingest-query-lint-audit-rules.patch | `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md` | Update contradiction rule to include uncertainties; modify phase 1 and phase 2 descriptions to require the new value contract; ensure uncertainties and low-confidence claims remain visible. |
| 005-acceptance-tests.patch | `.claude/skills/apex-kb/references/acceptance-tests.md` | Provide a sample compiled page with the new contract sections in smoke tests. |
| 006-skill.patch | `.claude/skills/apex-kb/SKILL.md` | Update skill description, procedure step 7, failure behavior, and completion gate to align with the new page value contract and unify contradictions into uncertainties. |
| 007-lifecycle-state-machine.patch | `.claude/skills/apex-kb/references/lifecycle-state-machine.md` | Update state S6_phase2_ready goal and maintenance state to reference the Phase 2 page value contract and uncertainties. |
| 008-knowledge-promotion-rules.patch | `.claude/skills/apex-kb/references/knowledge-promotion-rules.md` | Clarify that reviewed candidates are checked for contradictions or uncertainties. |
| 009-kb-schema-template.patch | `.claude/skills/apex-kb/templates/kb-schema-template.md` | Update KB taxonomy to include `uncertainty_raw_source_triggers` and change the operator review policy from contradiction_handling to uncertainty_handling. |

## Validation Commands
For each patch, the following commands were executed (in repository root):

```
# Example for patch 001
git checkout -- <target-file>
git status --porcelain -- <target-file>
# after modifying <target-file>
git diff --no-ext-diff -- <target-file> > <patch-file>
test -s <patch-file>
grep '^diff --git ' <patch-file>
git checkout -- <target-file>
git apply --check <patch-file>
git apply <patch-file>
git diff --name-only
git checkout -- <target-file>
git add <patch-file>
git commit -m "Add Phase 2 value contract patch 00X"
```

After all patches were created, cumulative validation was performed:

```
for p in apex-meta/patches/phase2-value-contract/*.patch; do git apply --check "$p"; done
for p in apex-meta/patches/phase2-value-contract/*.patch; do git apply "$p"; done
grep -R "Adaptive Ranked Source Set" -n .claude/skills/apex-kb/
grep -R "Macro / Meso / Micro" -n .claude/skills/apex-kb/
grep -R "Routes Here" -n .claude/skills/apex-kb/
grep -R "Uncertainty / Raw Source Triggers" -n .claude/skills/apex-kb/
grep -R "page_value_score" -n .claude/skills/apex-kb/ # should produce no matches
grep -R "source_cluster_map" -n .claude/skills/apex-kb/ # should produce no matches
git diff --name-only # should list only the nine target files
git checkout -- .claude/skills/apex-kb/
```

The grep checks reported the presence of the required section headings across the patched files and confirmed that `page_value_score` and `source_cluster_map` were absent. The `git diff --name-only` command after applying patches showed modifications to only the nine target files.

## Forbidden Files and Folders
No modifications were made to any forbidden files or directories. The following paths remained untouched:
- `.claude/skills/apex-kb2/`
- `apex-meta/kb/*/wiki/`
- `apex-meta/kb/*/ingest-analysis/`
- `apex-meta/scripts/`
- `derived/`
- `outputs/`
- `raw/`
- `sources/`

## Target File Reversion
After creating each patch, the modified target file was reverted to its original state using `git checkout -- <target-file>` before validating and committing the patch. The final commit history therefore contains only the `.patch` files; the actual target files under `.claude/skills/apex-kb/` remain unchanged in the repository.

## Patch Commit SHAs
| Patch | Commit SHA |
|------|------------|
| 001 | 4a5f33b |
| 002 | 6c60c06 |
| 003 | d9d74fd |
| 004 | 9eba5d9 |
| 005 | 692c2e9 |
| 006 | 5306d44 |
| 007 | 0956b0b |
| 008 | 3bcdc9e |
| 009 | a555c4c |

## Cumulative Checks
- **each_patch_git_apply_check:** PASS
- **cumulative_patch_check:** PASS (all patches apply cleanly on top of each other)
- **cumulative_grep_validation:** PASS (required headings present; forbidden strings absent)
- **target_files_modified_by_patch_pack_commits:** false (target files reverted after patch creation)
- **forbidden_files_touched:** false (no forbidden paths modified)

This manifest documents the creation and validation of the Phase 2 value contract patch pack. The patch files are ready for application on a clean checkout of `leela-spec/apexai-os-meta` on the `main` branch.
