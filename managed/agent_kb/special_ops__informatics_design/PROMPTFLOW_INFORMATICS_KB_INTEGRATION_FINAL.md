---
status: active_promptflow
repo: leela-spec/apexai-os-meta
branch: main
target_agent: special_ops__informatics_design
target_root: managed/agent_kb/special_ops__informatics_design
scope: apex_new_base_delta_patch
mode: patch_new_base_files_only
write_target: mapped_physical_new_base_file
read_only_legacy_source: standard_kb_files
external_repo_access: forbidden
masterofarts_access: forbidden
---

# PROMPTFLOW — special_ops__informatics_design Apex New-Base Delta Patch FINAL

## 0. Repository lock

Use exactly this repository:

```text
leela-spec/apexai-os-meta
```

Use exactly this target root:

```text
managed/agent_kb/special_ops__informatics_design/
```

Do not search, open, read, infer from, or fall back to:

```text
leela-spec/MasterOfArts
OpenClaw external repo paths
any external source repository
any deprecated Apex promptflow copy that points outside apexai-os-meta
```

If the connector cannot open `leela-spec/apexai-os-meta` or this exact target root, stop with:

```text
blocked_connector_or_repo_mismatch
```

Do not attempt recovery by searching MasterOfArts.

## 1. Purpose

Patch the newly placed Informatics Design KB files with missing Apex AI OS compatibility logic.

The editable target is the mapped physical file inside:

```text
managed/agent_kb/special_ops__informatics_design/newversion/
managed/agent_kb/special_ops__informatics_design/newversions/
```

The standard KB files are read-only legacy sources only.

This flow does not promote new-base files into the standard KB root.
This flow does not copy standard KB files into `newversion/` or `newversions/`.
This flow does not modify standard KB files.

## 2. Target model

| Surface | Role | Writable? |
|---|---|---|
| `managed/agent_kb/special_ops__informatics_design/newversion/**` | candidate new-base files | yes, only if mapped by H1/content |
| `managed/agent_kb/special_ops__informatics_design/newversions/**` | candidate new-base files | yes, only if mapped by H1/content |
| `managed/agent_kb/special_ops__informatics_design/ESSENCE.md` | read-only legacy delta source | no |
| `managed/agent_kb/special_ops__informatics_design/BEST_PRACTICES.md` | read-only legacy delta source | no |
| `managed/agent_kb/special_ops__informatics_design/MISTAKES.md` | read-only legacy delta source | no |
| `managed/agent_kb/special_ops__informatics_design/TEMPLATES.md` | read-only legacy delta source | no |
| `managed/agent_kb/special_ops__informatics_design/LEARNING_QUEUE.md` | read-only legacy delta source | no |
| `managed/agent_kb/special_ops__informatics_design/appendices/**` | read-only legacy delta source | no, unless physically under `newversion/` or `newversions/` |

## 3. Prime directive

Preserve first. Patch second. Improve never.

The task is not to make the KB better. The task is to make the new-base files Apex-compatible without changing their design.

Do not clean, improve, simplify, summarize, normalize, deduplicate, reorder, relabel, isolate, localize, sanitize, or redesign the new base.

## 4. Required execution sequence

1. Read this promptflow from `leela-spec/apexai-os-meta` at this exact path.
2. List `managed/agent_kb/special_ops__informatics_design/newversion/` if present.
3. List `managed/agent_kb/special_ops__informatics_design/newversions/` if present.
4. Inspect the H1 of every Markdown file in both folders.
5. Build the identity map by H1/content, not by filename alone.
6. Read the matching standard KB file only as a legacy delta source.
7. Patch only the mapped physical new-base file when a valid Apex delta is missing.
8. Fetch back every patched new-base file from `main`.
9. Verify standard KB root files were not modified.

## 5. Identity map table

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

- Filename and H1 agree -> edit that physical new-base file if a patch is needed.
- Filename wrong but H1 clear and unique -> edit that physical new-base file according to H1 identity.
- H1 missing or duplicated -> skip.
- Promptflow/provenance artifact -> skip unless H1 clearly identifies a KB target.
- No mapped new-base file -> do not write anything for that target.

Known Informatics misfile hint, to verify not assume:

```text
ESSENCE.md <- newversions/LEARNING_QUEUE.md
BEST_PRACTICES.md <- newversions/ESSENCE.md
LEARNING_QUEUE.md <- newversions/MISTAKES.md
APPENDIX_KB_SOURCE_MANIFEST.md <- newversions/BEST_PRACTICES.md
APPENDIX_KB_INFORMATION_RANKING_LEDGER.md <- newversions/APPENDIX_KB_SOURCE_MANIFEST.md
APPENDIX_KB_CANDIDATE_LEDGER.md <- newversions/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md <- newversions/APPENDIX_KB_CANDIDATE_LEDGER.md
TEMPLATES.md unresolved
MISTAKES.md unresolved
```

## 6. Valid Apex delta

Patch old Apex logic only if it is all of the following:

1. present in the read-only standard Apex file,
2. absent from the mapped physical new-base file,
3. still valid for Apex AI OS,
4. necessary for Apex operation,
5. insertable without changing the new-base architecture.

Likely valid Informatics deltas:

- owner / validator / review metadata
- MetaOps validation boundary
- Apex-specific authority boundary
- accepted_in_kb_base vs runtime truth boundary
- release-pack / project inheritance assumptions
- no direct runtime/config mutation constraints

Reject:

- structure normalization
- schema improvements
- deduplication
- appendix rewrites
- generic informatics prose
- external repo as active target
- migration/process commentary
- source-lineage sanitization unless exactly obsolete or Apex-incompatible

## 7. Patch rule

Patch only this kind of path:

```text
managed/agent_kb/special_ops__informatics_design/newversion/**
managed/agent_kb/special_ops__informatics_design/newversions/**
```

Never patch this kind of path in this flow:

```text
managed/agent_kb/special_ops__informatics_design/ESSENCE.md
managed/agent_kb/special_ops__informatics_design/BEST_PRACTICES.md
managed/agent_kb/special_ops__informatics_design/MISTAKES.md
managed/agent_kb/special_ops__informatics_design/TEMPLATES.md
managed/agent_kb/special_ops__informatics_design/LEARNING_QUEUE.md
managed/agent_kb/special_ops__informatics_design/appendices/**
```

## 8. Final report required

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
fetch_back_status:
changed_file_set:
remaining_questions:
```

Do not claim success unless:

```text
standard_root_files_changed: []
all changed_file_set paths are under newversion/ or newversions/
all patched new-base files were fetched back from main
```
