---
status: active_promptflow
repo: leela-spec/apexai-os-meta
branch: main
target_agent: special_ops__knowledge_bank
target_root: managed/agent_kb/special_ops__knowledge_bank
scope: apex_new_base_integration
mode: preserve_new_base_patch_minimal_apex_delta
discovery_rule: check_newversion_and_newversions_before_blocking
---

# PROMPTFLOW — special_ops__knowledge_bank Apex New-Base Integration FINAL

## 0. Purpose

Integrate newly placed Apex AI OS KB files for `special_ops__knowledge_bank` into their standard KB paths.

This is a fidelity-preserving integration, not a cleanup, rewrite, redesign, normalization, localization, or rebuild.

The newly placed KB files are the canonical base. Existing Apex KB files are legacy-value sources only.

## 1. Prime directive

Preserve first. Patch second. Improve never.

The task is not to make the KB better; the task is to make the new KB base Apex-compatible without changing its design.

The new base wins on structure, wording, headings, file roles, intentional overlap, cross-references, appendices, IDs, database tables, evidence links, ranking links, and candidate links.

Do not clean, improve, simplify, summarize, normalize, deduplicate, reorder, relabel, isolate, localize, sanitize, or redesign the new base.

## 2. Hard scope

Work only inside:

```text
managed/agent_kb/special_ops__knowledge_bank/
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
managed/agent_kb/special_ops__knowledge_bank/newversion/
managed/agent_kb/special_ops__knowledge_bank/newversions/
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

## 3. Non-negotiable discovery rule

Before any comparison, delta decision, or patch:

1. List files under `newversion/` if present.
2. List files under `newversions/` if present.
3. Inspect the H1 of every Markdown file in both folders.
4. Build the identity map from detected content identity, not filename alone.
5. Do not mark a target missing until both candidate folders have been checked.

## 4. Identity map gate

Produce internally before editing:

| physical_new_base_path | detected_h1 | intended_target_file | confidence | action |
|---|---|---|---|---|

Allowed confidence:

```text
path_match
heading_match_clear
ambiguous
missing
non_kb_artifact
```

Rules:

- Filename and H1 agree -> use as target base.
- Filename wrong but H1 clear and unique -> use H1 to map target.
- H1 missing -> skip and report.
- H1 duplicated -> skip and report.
- Promptflow/provenance artifact -> skip unless H1 clearly identifies a KB target.
- No new base found after checking both folders -> do not overwrite with old Apex.
- Filename mismatch is only an identity-map problem, not permission to clean or redesign content.

## 5. Valid Apex delta

Patch old Apex logic only if it is:

1. present in the old Apex file
2. absent from the mapped new base
3. still valid for Apex AI OS
4. necessary for Apex operation
5. insertable without changing the new base architecture

Likely valid Knowledge Bank deltas:

- candidate-to-promotion path
- project-to-meta learning flow
- meta-to-project release-pack assumptions
- source-note / promotion-trace boundaries
- owner / validator / review metadata
- accepted_in_kb_base vs runtime truth boundary

Reject:

- database simplification
- appendix restructuring
- deduplication
- schema normalization
- external repo as active target
- migration/process commentary
- source/provenance sanitization unless exactly obsolete or Apex-incompatible

## 6. Knowledge Bank-specific warning

Knowledge Bank appendices are database surfaces.

Do not recreate, sanitize, summarize, centralize, or normalize them during integration.

Preserve:

- IDs
- row structures
- ranking logic
- source lineage
- candidate linkage
- evidence linkage
- appendix-to-scaffold routing
- cross-file pointers

## 7. Intentional overlap rule

Repeated concepts across scaffold files and appendices are presumed intentional retrieval architecture.

Do not remove, relocate, compress, or isolate overlap unless the new base directly contradicts itself.

## 8. External source rule

Do not operate on external repos.

Do not preserve obsolete statements that external repos are active targets or runtime homes.

Do not remove evidence references, source IDs, or database lineage merely because they mention historical sources.

## 9. Patch phase

After the identity map gate:

1. Use mapped new base as body.
2. Apply only valid Apex deltas from the old Apex file.
3. Preserve headings, order, overlap, IDs, tables, appendices, and cross-references.
4. Do not edit unrelated wording.
5. Replace the standard file with the mapped new base plus approved Apex delta.
6. Fetch back each edited file from `main`.
7. Check edited files for forbidden active external-target claims.

Patch order:

```text
BEST_PRACTICES.md
MISTAKES.md
TEMPLATES.md
LEARNING_QUEUE.md
appendices/APPENDIX_KB_SOURCE_MANIFEST.md
appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
ESSENCE.md
```

Patch `ESSENCE.md` last.

## 10. Stop / skip conditions

Skip the affected target and report if:

```text
new base missing after both folders checked
H1 missing or duplicated
identity ambiguous
old Apex logic conflicts with new base
patch would touch non-Knowledge-Bank files
patch would mutate runtime config or governance authority
```

Do not repair ambiguous content.

## 11. Final validation table

Return:

| file | new_base_preserved | apex_delta_added | overlap_preserved | appendix_structure_preserved | forbidden_external_target_refs_removed | fetch_back | status |
|---|---|---|---|---|---|---|---|

Allowed status:

```text
patched
no_change_needed
skipped_ambiguous
skipped_missing_new_base
blocked_conflict
```

## 12. Final response

Return:

```text
repo:
branch:
target_root:
identity_map:
files_patched:
files_unchanged:
files_skipped:
apex_logic_added:
legacy_logic_rejected:
intentional_overlap_preserved:
appendix_structure_preserved:
external_target_refs_removed:
fetch_back_status:
remaining_questions:
```

Do not claim completion unless every patched file was fetched back from `main`.
