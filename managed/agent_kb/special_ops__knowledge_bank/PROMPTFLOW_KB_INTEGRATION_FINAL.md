---
status: active_promptflow
repo: leela-spec/apexai-os-meta
branch: main
target_agent: special_ops__knowledge_bank
target_root: managed/agent_kb/special_ops__knowledge_bank
scope: apex_new_base_delta_patch
mode: patch_new_base_files_only
write_target: mapped_physical_new_base_file
read_only_legacy_source: standard_kb_files
discovery_rule: check_newversion_and_newversions_before_blocking
anti_failure_rule: no_false_positive_completion
---

# PROMPTFLOW — special_ops__knowledge_bank Apex New-Base Delta Patch FINAL

## 0. Purpose

Patch the newly placed Knowledge Bank KB files with missing Apex AI OS compatibility logic.

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

The new base wins on structure, wording, headings, file roles, intentional overlap, cross-references, appendices, IDs, database tables, evidence links, ranking links, candidate links, and source lineage.

Do not clean, improve, simplify, summarize, normalize, deduplicate, reorder, relabel, isolate, localize, sanitize, or redesign the new base.

## 3. Hard scope

Work only inside:

```text
managed/agent_kb/special_ops__knowledge_bank/
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
```

Editable new-base folders, both mandatory to check before declaring missing:

```text
managed/agent_kb/special_ops__knowledge_bank/newversion/
managed/agent_kb/special_ops__knowledge_bank/newversions/
```

Only mapped physical files inside these new-base folders may be edited.

Do not modify:

```text
managed/agent_kb/special_ops__knowledge_bank/ESSENCE.md
managed/agent_kb/special_ops__knowledge_bank/BEST_PRACTICES.md
managed/agent_kb/special_ops__knowledge_bank/MISTAKES.md
managed/agent_kb/special_ops__knowledge_bank/TEMPLATES.md
managed/agent_kb/special_ops__knowledge_bank/LEARNING_QUEUE.md
managed/agent_kb/special_ops__knowledge_bank/appendices/**
openclaw.json
runtime config
provider/model config
shared governance files
other agent KB folders
managed/agents/**
```

Exception: files under `newversion/` or `newversions/` are editable if mapped by identity.

Do not read or operate on external repos as active targets. Historical source references may remain as evidence lineage.

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

The final response must include enough information to prove this ledger was completed. Do not output the word `completed` unless steps 1-10 have evidence.

## 5. Non-negotiable discovery rule

Before any comparison, delta decision, or patch:

1. List files under `newversion/` if present.
2. List files under `newversions/` if present.
3. Inspect the H1 of every Markdown file in both folders.
4. Build the identity map from detected content identity, not filename alone.
5. Do not mark a target missing until both candidate folders have been checked.

If both folders are absent or empty, stop with `blocked_missing_new_base` and report actual inspected paths. Do not use old Apex files as replacements.

## 6. Identity map gate

Produce before editing:

```text
| physical_new_base_path | detected_h1 | intended_target_file | confidence | action |
|---|---|---|---|---|
```

Allowed confidence:

```text
path_match
heading_match_clear
ambiguous
missing
non_kb_artifact
```

Rules:

- Filename and H1 agree -> use that physical new-base file as edit target.
- Filename wrong but H1 clear and unique -> use H1 to map that physical new-base file to the intended target identity.
- H1 missing -> skip and report.
- H1 duplicated -> skip and report.
- Promptflow/provenance artifact -> skip unless H1 clearly identifies a KB target.
- No new base found after checking both folders -> do not overwrite with old Apex.
- Filename mismatch is only an identity-map problem, not permission to clean or redesign content.

## 7. File comparison table

For each read-only legacy target identity, produce before editing:

```text
| target_file_identity | mapped_physical_new_base_path | read_only_old_apex_file | comparison_result | apex_delta_needed | action |
|---|---|---|---|---|---|
```

Allowed `action`:

```text
patch_mapped_new_base_with_apex_delta
leave_mapped_new_base_no_delta
skip_missing_new_base
skip_ambiguous_identity
skip_conflict
```

## 8. Legacy delta decision table

For every old-only element considered, produce:

```text
| old_file_element | decision | reason | exact_new_base_target_section |
|---|---|---|---|
```

Allowed `decision`:

```text
keep_already_represented
patch_into_new_base
reject_obsolete
reject_duplicate
reject_generic
reject_external_active_target
reject_over_normalizing
```

## 9. Valid Apex delta

Patch old Apex logic only if it is all of the following:

1. present in the read-only old Apex file,
2. absent from the mapped physical new-base file,
3. still valid for Apex AI OS,
4. necessary for Apex operation,
5. insertable without changing the new base architecture.

Likely valid Knowledge Bank deltas:

- candidate-to-promotion path
- project-to-meta learning flow
- meta-to-project release-pack assumptions
- source-note / promotion-trace boundaries
- owner / validator / review metadata
- accepted_in_kb_base vs runtime truth boundary
- MetaOps / Special Ops orchestration boundary
- no direct runtime/config mutation constraints

Reject database simplification, appendix restructuring, deduplication, schema normalization, generic KB prose, external repo as active target, migration/process commentary, source/provenance sanitization unless exactly obsolete or Apex-incompatible, and future-research ideas unless already present as old Apex logic and required for Apex operation.

## 10. Future-research / cross-system delta handling

Do not silently add broad future-research improvements merely because they were discussed elsewhere.

Items such as QA trace, source notes, examples, sidecars, attach packs, promotion trace, status vocabulary, read-budget profiles, and cross-agent harmonization may be patched only if they meet the valid Apex delta test in Section 9.

If important but not valid for direct patching, report under `remaining_questions / deferred_candidates`.

## 11. Knowledge Bank-specific warning

Knowledge Bank appendices are database surfaces.

Do not recreate, sanitize, summarize, centralize, or normalize them during integration.

Preserve IDs, row structures, ranking logic, source lineage, candidate linkage, evidence linkage, appendix-to-scaffold routing, and cross-file pointers.

Repeated concepts across scaffold files and appendices are presumed intentional retrieval architecture.

## 12. External source rule

Do not operate on external repos.

Do not preserve obsolete statements that external repos are active targets or runtime homes.

Do not remove evidence references, source IDs, or database lineage merely because they mention historical sources.

## 13. Patch phase

After Sections 5-8 are complete:

1. Use mapped physical new-base file as the edit target.
2. Apply only valid Apex deltas from the read-only old Apex file.
3. Preserve headings, order, overlap, IDs, tables, appendices, source lineage, and cross-references.
4. Do not edit unrelated wording.
5. Update only the mapped physical new-base file.
6. Fetch back each edited physical new-base file from `main`.
7. Confirm standard KB root files were not modified.
8. Check edited new-base files for forbidden active external-target claims.

Do not promote to standard paths.
Do not copy standard files into `newversion/` or `newversions/`.
Do not update `ESSENCE.md` or any standard root file in this promptflow.

## 14. Stop / skip conditions

Skip the affected target and report if:

```text
new base missing after both folders checked
H1 missing or duplicated
identity ambiguous
old Apex logic conflicts with new base
patch would touch standard KB root files
patch would touch non-Knowledge-Bank files
patch would mutate runtime config or governance authority
```

Stop the entire run if the target root is not `managed/agent_kb/special_ops__knowledge_bank/` or repo is not `leela-spec/apexai-os-meta`.

## 15. Final validation table

Return:

```text
| target_file_identity | mapped_physical_new_base_path | new_base_preserved | apex_delta_added | standard_root_unchanged | forbidden_external_target_refs_removed | fetch_back | status |
|---|---|---|---|---|---|---|---|
```

Allowed status:

```text
patched_new_base
new_base_no_delta_needed
skipped_ambiguous
skipped_missing_new_base
blocked_conflict
```

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
