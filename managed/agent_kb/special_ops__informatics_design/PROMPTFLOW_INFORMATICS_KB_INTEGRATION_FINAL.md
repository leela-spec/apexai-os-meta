---
status: active_promptflow
repo: leela-spec/apexai-os-meta
branch: main
target_agent: special_ops__informatics_design
target_root: managed/agent_kb/special_ops__informatics_design
scope: apex_new_base_integration
mode: execute_actual_file_integration_not_prior_run_summary
discovery_rule: check_newversion_and_newversions_before_blocking
anti_failure_rule: no_false_positive_completion
---

# PROMPTFLOW — special_ops__informatics_design Apex New-Base Integration FINAL

## 0. Purpose

Execute the actual Informatics Design integration into the Apex AI OS repo.

This promptflow must integrate the newly placed Informatics Design KB files into their standard paths while preserving the new base and patching only required Apex AI OS compatibility deltas.

This is an execution flow. It is not a report-only flow and not a restatement of an earlier base build.

## 1. Absolute anti-failure rule

Do not claim execution from memory, previous chat summaries, previous base-build results, or retrieved execution snippets.

A valid execution requires all of the following in this run:

1. Read this promptflow file.
2. Inspect the actual target root.
3. Inspect `newversion/` and `newversions/` if present.
4. Build a content/H1 identity map.
5. Compare mapped new bases against current Apex standard files.
6. Decide per target whether an Apex delta must be patched.
7. Patch files when valid deltas exist.
8. Fetch back every patched file from `main`.
9. Return changed-file set, unchanged-file set, skipped-file set, and verification status.

If no files are patched, the final report must still show the identity map, comparison result, and per-file no-change justification.

## 2. Prime directive

Preserve first. Patch second. Improve never.

The task is not to make the KB better; the task is to make the new KB base Apex-compatible without changing its design.

The newly placed KB files are the canonical base. Existing Apex KB files are legacy-value sources only.

The new base wins on structure, wording, headings, file roles, intentional overlap, cross-references, appendices, IDs, database tables, evidence links, ranking links, candidate links, and source lineage.

Do not clean, improve, simplify, summarize, normalize, deduplicate, reorder, relabel, isolate, localize, sanitize, or redesign the new base.

## 3. Hard scope

Work only inside:

```text
managed/agent_kb/special_ops__informatics_design/
```

Allowed target files:

```text
ESSENCE.md
BEST_PRACTICES.md
MISTAKES.md
TEMPLATES.md
LEARNING_QUEUE.md
appendices/APPENDIX_KB_SOURCE_MANIFEST.md
appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
```

Candidate new-base folders, both mandatory to check before declaring missing:

```text
managed/agent_kb/special_ops__informatics_design/newversion/
managed/agent_kb/special_ops__informatics_design/newversions/
```

Do not modify:

```text
openclaw.json
runtime config
provider/model config
shared governance files
other agent KB folders
managed/agents/**
```

Do not read or operate on external repos as active targets. Historical source references may remain as evidence lineage.

## 4. Mandatory execution ledger

Before editing, create an internal execution ledger:

```text
|step|required_action|evidence_required|status|
|---|---|---|---|
|1|read promptflow|current promptflow path + SHA/content seen|pending|
|2|inspect target root|list of current standard files found|pending|
|3|inspect new-base folders|newversion/newversions existence + file list|pending|
|4|map identities|H1/content identity map|pending|
|5|compare files|per-target comparison table|pending|
|6|decide deltas|keep/patch/reject table|pending|
|7|patch if needed|commit SHA per patched file or no-change justification|pending|
|8|fetch back|fetch-back status per patched file|pending|
|9|final report|changed/unchanged/skipped/blocked summary|pending|
```

The final response must include enough information to prove this ledger was completed. Do not output the word `completed` unless steps 1-9 have evidence.

## 5. Non-negotiable discovery rule

Before any comparison, delta decision, or patch:

1. List files under `newversion/` if present.
2. List files under `newversions/` if present.
3. Inspect the H1 of every Markdown file in both folders.
4. Build the identity map from detected content identity, not filename alone.
5. Do not mark a target missing until both candidate folders have been checked.

Known failure to prevent: checking only `newversion/` and concluding no new base exists while the real folder is `newversions/`.

If both folders are absent or empty, stop with `blocked_missing_new_base` and report actual inspected paths. Do not use old Apex files as replacements.

## 6. Identity map gate

Produce before editing:

```text
| physical_new_base_path | detected_h1 | intended_target_file | confidence | action |
|---|---|---|---|---|
```

Allowed confidence: `path_match`, `heading_match_clear`, `ambiguous`, `missing`, `non_kb_artifact`.

Rules:

- Filename and H1 agree -> use as target base.
- Filename wrong but H1 clear and unique -> use H1 to map target.
- H1 missing -> skip and report.
- H1 duplicated -> skip and report.
- Promptflow/provenance artifact -> skip unless H1 clearly identifies a KB target.
- No new base found after checking both folders -> do not overwrite with old Apex.
- Filename mismatch is only an identity-map problem, not permission to clean or redesign content.

Known likely misfile pattern for this agent, to verify by H1/content identity:

```text
ESSENCE.md <- newversions/LEARNING_QUEUE.md
BEST_PRACTICES.md <- newversions/ESSENCE.md
LEARNING_QUEUE.md <- newversions/MISTAKES.md
APPENDIX_KB_SOURCE_MANIFEST.md <- newversions/BEST_PRACTICES.md
APPENDIX_KB_INFORMATION_RANKING_LEDGER.md <- newversions/APPENDIX_KB_SOURCE_MANIFEST.md
APPENDIX_KB_CANDIDATE_LEDGER.md <- newversions/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md <- newversions/APPENDIX_KB_CANDIDATE_LEDGER.md
TEMPLATES.md unresolved; do not infer from promptflow body
MISTAKES.md unresolved until H1 inspection finds it
```

This hint is not authority.

## 7. File comparison table

For each allowed target file, produce before editing:

```text
| target_file | mapped_new_base_source | old_apex_file | comparison_result | apex_delta_needed | action |
|---|---|---|---|---|---|
```

Allowed action: `patch_new_base_with_apex_delta`, `promote_new_base_no_delta`, `skip_missing_new_base`, `skip_ambiguous_identity`, `skip_conflict`.

## 8. Legacy delta decision table

For every old-only element considered, produce:

```text
| old_file_element | decision | reason | exact_target_section |
|---|---|---|---|
```

Allowed decision: `keep_already_represented`, `patch_into_new`, `reject_obsolete`, `reject_duplicate`, `reject_generic`, `reject_external_active_target`, `reject_over_normalizing`.

## 9. Valid Apex delta

Patch old Apex logic only if it is all of the following:

1. present in the old Apex file,
2. absent from the mapped new base,
3. still valid for Apex AI OS,
4. necessary for Apex operation,
5. insertable without changing the new base architecture.

Likely valid Informatics Design deltas:

- owner / validator / review metadata
- MetaOps validation boundary
- Apex-specific agent authority boundaries
- accepted_in_kb_base vs runtime truth boundary
- release-pack / project inheritance assumptions
- no direct runtime/config mutation constraints

Reject generic informatics prose, structure normalization, schema improvements, deduplication, appendix rewrites, external repo as active target, migration/process commentary, source/provenance sanitization unless exactly obsolete or Apex-incompatible, and future-research ideas unless already present as old Apex logic and required for Apex operation.

## 10. Future-research / cross-system delta handling

Do not silently add broad future-research improvements merely because they were discussed elsewhere.

Items such as QA trace, source notes, examples, sidecars, attach packs, promotion trace, status vocabulary, read-budget profiles, and cross-agent harmonization may be patched only if they meet the valid Apex delta test in Section 9.

If important but not valid for direct patching, report under `remaining_questions / deferred_candidates`.

## 11. Informatics-specific warning

Do not improve information architecture while integrating it.

This agent's own content may contain schema, file-type, redundancy, and chunking doctrine. Preserve its internal redundancy and taxonomy.

Appendices are database surfaces. Preserve IDs, row structures, ranking logic, candidate linkage, evidence linkage, source lineage, and cross-file pointers.

Repeated concepts across scaffold files and appendices are presumed intentional retrieval architecture.

## 12. External source rule

Do not operate on external repos.

Do not preserve obsolete statements that external repos are active targets or runtime homes.

Do not remove evidence references, source IDs, or database lineage merely because they mention historical sources.

## 13. Patch phase

After Sections 5-8 are complete:

1. Use mapped new base as body.
2. Apply only valid Apex deltas from the old Apex file.
3. Preserve headings, order, overlap, IDs, tables, appendices, source lineage, and cross-references.
4. Do not edit unrelated wording.
5. Replace the standard file with the mapped new base plus valid Apex delta.
6. Fetch back each edited file from `main`.
7. Check edited files for forbidden active external-target claims.

Patch `ESSENCE.md` last.

## 14. Stop / skip conditions

Skip the affected target and report if new base is missing after both folders checked, H1 missing or duplicated, identity ambiguous, old Apex logic conflicts with new base, patch would touch non-Informatics files, or patch would mutate runtime config/governance authority.

Stop the entire run if the target root is not `managed/agent_kb/special_ops__informatics_design/` or repo is not `leela-spec/apexai-os-meta`.

## 15. Final validation table

Return:

```text
| file | mapped_new_base | new_base_preserved | apex_delta_added | forbidden_external_target_refs_removed | fetch_back | status |
|---|---|---|---|---|---|---|
```

Allowed status: `patched`, `promoted_no_delta`, `no_change_needed`, `skipped_ambiguous`, `skipped_missing_new_base`, `blocked_conflict`.

## 16. Final response

Return:

```text
repo:
branch:
target_root:
promptflow_read:
new_base_folders_inspected:
identity_map:
comparison_table:
files_patched:
files_promoted_no_delta:
files_unchanged:
files_skipped:
apex_logic_added:
legacy_logic_rejected:
deferred_candidates:
external_target_refs_removed:
fetch_back_status:
changed_file_set:
remaining_questions:
```

Do not claim completion unless every patched file was fetched back from `main` and every unpatched target has an explicit comparison-table justification.
