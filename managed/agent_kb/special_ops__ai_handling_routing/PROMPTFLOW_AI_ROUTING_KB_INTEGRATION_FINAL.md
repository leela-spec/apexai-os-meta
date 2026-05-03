---
status: active_promptflow
repo: leela-spec/apexai-os-meta
branch: main
target_agent: special_ops__ai_handling_routing
target_root: managed/agent_kb/special_ops__ai_handling_routing
scope: apex_new_base_delta_patch
mode: patch_new_base_files_only
write_target: mapped_physical_new_base_file
read_only_legacy_source: standard_kb_files
discovery_rule: check_newversion_and_newversions_before_blocking
anti_failure_rule: no_false_positive_completion
---

# PROMPTFLOW — special_ops__ai_handling_routing Apex New-Base Delta Patch FINAL

## 0. Purpose

Patch the newly placed AI Handling/Routing KB files with missing Apex AI OS compatibility logic.

The editable target is the mapped physical file inside `newversion/` or `newversions/`.

The standard KB files are read-only legacy sources used only to extract missing Apex deltas.

This promptflow does not promote new-base files into the standard KB root.
This promptflow does not sync standard KB files back into `newversion/` or `newversions/`.
This promptflow does not rewrite, clean, normalize, or redesign the new base.

## 1. Absolute anti-failure rule

Do not claim execution from memory, previous chat summaries, previous base-build results, or retrieved execution snippets.

A valid execution requires all of the following in this run:

1. Read this promptflow file.
2. Inspect the actual target root.
3. Inspect `newversion/` and `newversions/` if present.
4. Build a content/H1 identity map for the new-base files.
5. Compare mapped new-base files against current standard Apex KB files as read-only legacy sources.
6. Decide per target whether an Apex delta must be patched into the mapped physical new-base file.
7. Patch only mapped physical new-base files when valid deltas exist.
8. Fetch back every patched new-base file from `main`.
9. Verify standard KB root files were not modified.
10. Return changed-file set, unchanged-file set, skipped-file set, and verification status.

If no files are patched, the final report must still show the identity map, comparison result, and per-file no-change justification.

## 2. Prime directive

Preserve first. Patch second. Improve never.

The task is not to make the KB better; the task is to make the new KB base Apex-compatible without changing its design.

The newly placed KB files are the canonical base. Existing standard Apex KB files are legacy-value sources only.

The new base wins on structure, wording, headings, file roles, intentional overlap, cross-references, appendices, IDs, database tables, evidence links, ranking links, routing cards, candidate links, and source lineage.

Do not clean, improve, simplify, summarize, normalize, deduplicate, reorder, relabel, isolate, localize, sanitize, or redesign the new base.

## 3. Hard scope

Work only inside:

```text
managed/agent_kb/special_ops__ai_handling_routing/
```

Read-only legacy source files:

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
appendices/APPENDIX_KB_QUALITY_IMPROVEMENT_ANALYSIS.md
```

Editable new-base folders, both mandatory to check before declaring missing:

```text
managed/agent_kb/special_ops__ai_handling_routing/newversion/
managed/agent_kb/special_ops__ai_handling_routing/newversions/
```

Only mapped physical files inside these new-base folders may be edited.

Do not modify standard KB root files, standard appendices, `openclaw.json`, runtime config, provider/model config, shared governance files, other agent KB folders, or `managed/agents/**`.

Exception: files under `newversion/` or `newversions/` are editable if mapped by identity.

## 4. Mandatory execution ledger

Before editing, create an internal execution ledger:

```text
|step|required_action|evidence_required|status|
|---|---|---|---|
|1|read promptflow|current promptflow path + SHA/content seen|pending|
|2|inspect target root|list of read-only standard files found|pending|
|3|inspect new-base folders|newversion/newversions existence + file list|pending|
|4|map identities|H1/content identity map for new-base files|pending|
|5|compare files|per-target comparison table using standard file as read-only legacy source|pending|
|6|decide deltas|keep/patch/reject table|pending|
|7|patch if needed|commit SHA per patched physical new-base file or no-change justification|pending|
|8|fetch back|fetch-back status per patched physical new-base file|pending|
|9|standard-root unchanged check|standard KB files unchanged or explicitly not touched|pending|
|10|final report|changed/unchanged/skipped/blocked summary|pending|
```

Do not output the word `completed` unless steps 1-10 have evidence.

## 5. Non-negotiable discovery rule

Before any comparison, delta decision, or patch:

1. List files under `newversion/` if present.
2. List files under `newversions/` if present.
3. Inspect the H1 of every Markdown file in both folders.
4. Build the identity map from detected content identity, not filename alone.
5. Do not mark a target missing until both candidate folders have been checked.

## 6. Identity map gate

Produce before editing:

```text
| physical_new_base_path | detected_h1 | intended_target_file | confidence | action |
|---|---|---|---|---|
```

Allowed confidence: `path_match`, `heading_match_clear`, `ambiguous`, `missing`, `non_kb_artifact`.

Rules:

- Filename and H1 agree -> use that physical new-base file as edit target.
- Filename wrong but H1 clear and unique -> use H1 to map that physical new-base file to the intended target identity.
- H1 missing or duplicated -> skip and report.
- Promptflow/provenance artifact -> skip unless H1 clearly identifies a KB target.
- No new base found after checking both folders -> do not overwrite with old Apex.
- Filename mismatch is only an identity-map problem, not permission to clean or redesign content.

## 7. File comparison table

For each read-only legacy target identity, produce before editing:

```text
| target_file_identity | mapped_physical_new_base_path | read_only_old_apex_file | comparison_result | apex_delta_needed | action |
|---|---|---|---|---|---|
```

Allowed action: `patch_mapped_new_base_with_apex_delta`, `leave_mapped_new_base_no_delta`, `skip_missing_new_base`, `skip_ambiguous_identity`, `skip_conflict`.

## 8. Legacy delta decision table

For every old-only element considered, produce:

```text
| old_file_element | decision | reason | exact_new_base_target_section |
|---|---|---|---|
```

Allowed decision: `keep_already_represented`, `patch_into_new_base`, `reject_obsolete`, `reject_duplicate`, `reject_generic`, `reject_external_active_target`, `reject_over_normalizing`.

## 9. Valid Apex delta

Patch old Apex logic only if it is all of the following:

1. present in the read-only old Apex file,
2. absent from the mapped physical new-base file,
3. still valid for Apex AI OS,
4. necessary for Apex operation,
5. insertable without changing the new base architecture.

Likely valid AI Handling/Routing deltas:

- no provider/model config mutation
- config-impact review packet requirement
- MetaOps activation/routing boundary
- freshness/currentness review requirement
- human/operator approval for high-risk routing changes
- advisory-only routing boundary
- owner / validator / review metadata
- accepted_in_kb_base vs runtime truth boundary
- handoff/routing boundaries into validation, promotion, escalation, or Knowledge Bank lanes

Reject provider/model recommendation updates unless the new base already contains them, runtime config edits, config authority claims, generic routing prose, deduplication, appendix rewrites, external repo as active target, migration/process commentary, source/provenance sanitization unless exactly obsolete or Apex-incompatible, and future-research ideas unless already present as old Apex logic and required for Apex operation.

## 10. Agent-specific warning

Do not turn advisory routing guidance into runtime/provider config authority.

Do not update provider/model recommendations unless the new base already does.

Do not mutate runtime config.

Routing advice remains advisory unless promoted by the proper Apex authority path.

Appendices and quality analyses are database/evidence surfaces. Preserve IDs, row structures, ranking logic, candidate linkage, evidence linkage, source lineage, and cross-file pointers.

Repeated concepts across scaffold files and appendices are presumed intentional retrieval architecture.

## 11. Patch phase

After Sections 5-8 are complete:

1. Use mapped physical new-base file as the edit target.
2. Apply only valid Apex deltas from the read-only old Apex file.
3. Preserve headings, order, overlap, routing cards, IDs, tables, appendices, source lineage, and cross-references.
4. Do not edit unrelated wording.
5. Update only the mapped physical new-base file.
6. Fetch back each edited physical new-base file from `main`.
7. Confirm standard KB root files were not modified.
8. Check edited new-base files for forbidden active external-target claims and config-authority claims.

Do not promote to standard paths.
Do not copy standard files into `newversion/` or `newversions/`.
Do not update `ESSENCE.md` or any standard root file in this promptflow.

## 12. Stop / skip conditions

Skip the affected target and report if new base is missing after both folders checked, H1 missing or duplicated, identity ambiguous, old Apex logic conflicts with new base, patch would touch standard KB root files, patch would touch non-AI-Handling/Routing files, or patch would mutate runtime config/governance authority.

Stop the entire run if target root or repo is wrong.

## 13. Final validation table

Return:

```text
| target_file_identity | mapped_physical_new_base_path | new_base_preserved | apex_delta_added | standard_root_unchanged | forbidden_external_target_refs_removed | fetch_back | status |
|---|---|---|---|---|---|---|---|
```

Allowed status: `patched_new_base`, `new_base_no_delta_needed`, `skipped_ambiguous`, `skipped_missing_new_base`, `blocked_conflict`.

## 14. Final response

Return:

```text
repo:
branch:
target_root:
promptflow_read:
new_base_folders_inspected:
identity_map:
comparison_table:
new_base_files_patched:
new_base_files_unchanged:
standard_root_files_changed: must_be_empty
files_skipped:
apex_logic_added:
legacy_logic_rejected:
deferred_candidates:
external_target_refs_removed:
fetch_back_status:
changed_file_set:
remaining_questions:
```

Do not claim completion unless every patched physical new-base file was fetched back from `main`, every unpatched target has an explicit comparison-table justification, and `standard_root_files_changed` is empty.
