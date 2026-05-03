---
status: draft_promptflow
repo: leela-spec/apexai-os-meta
branch: main
target_agent: special_ops__informatics_design
target_root: managed/agent_kb/special_ops__informatics_design
scope: apex_new_base_integration
mode: preserve_new_base_patch_minimal_apex_delta
---

# PROMPTFLOW — special_ops__informatics_design Apex New-Base Integration (DRY RUN)

## 0. Purpose

Integrate newly placed Apex AI OS KB files for `special_ops__informatics_design` into their standard KB paths.

This is a fidelity-preserving integration, not a cleanup, rewrite, redesign, normalization, or rebuild.

The newly placed KB files are the canonical base. Existing Apex KB files are legacy-value sources only.

## 1. Prime directive

Preserve first. Patch second. Improve never.

The task is not to make the KB better; the task is to make the new KB base Apex-compatible without changing its design.

The new base wins on:

- structure
- wording
- headings
- file roles
- intentional overlap
- cross-references
- appendices
- IDs
- database tables
- evidence/ranking/candidate links

Do not clean, improve, simplify, summarize, normalize, deduplicate, reorder, relabel, isolate, localize, or redesign the new base.

## 2. Hard scope

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

Allowed new-base folder:

```text
managed/agent_kb/special_ops__informatics_design/newversion/
```

Do not modify anything in this promptflow. Dry-run only.

## 3. Valid Apex delta

Patch old Apex logic only if it is:

1. present in the old Apex file
2. absent from the new base
3. still valid for Apex AI OS
4. necessary for Apex operation
5. insertable without changing the new base architecture

Allowed Apex deltas include:

- owner / validator / review metadata
- MetaOps validation boundary
- Apex-specific agent authority boundaries
- accepted_in_kb_base vs runtime truth
- release-pack / project inheritance assumptions
- no direct runtime/config mutation constraints
- QA severity, closure, escalation, validation rules

Reject:

- generic informatics prose
- structure normalization
- schema “improvements”
- deduplication
- appendix rewrites
- external repo as active target
- migration/process commentary

## 4. Identity map (required, before any editing)

Produce:

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

- Prefer filename match
- If filename wrong but H1 is clear → map by H1
- If H1 missing or duplicated → skip
- If no new base exists → do not overwrite
- Filename mismatch is NOT permission to fix content

## 5. File comparison

Produce:

| target_file | new_base_source | old_apex_file | comparison_result | repair_needed |
|---|---|---|---|---|

## 6. Legacy delta decisions

Produce:

| old_file_element | keep / patch_into_new / reject | reason | exact_target_section |
|---|---|---|---|

Definitions:

- keep = already represented in new base
- patch_into_new = valid missing Apex delta
- reject = obsolete / duplicate / invalid

## 7. Proposed minimal patch plan

Produce:

| target_file | patch_delta | target_section | risk | requires_approval |
|---|---|---|---|---|

## 8. Intentional overlap rule

Do not remove or relocate overlapping concepts.

Informatics design may intentionally repeat schema logic across files.

Preserve redundancy and taxonomy.

## 9. Appendix rule

Appendices are database surfaces.

Do not:

- recreate
- sanitize
- collapse
- centralize

Preserve:

- IDs
- row structures
- ranking logic
- candidate linkage
- evidence linkage
- cross-file pointers

Remove only:

- external repo as active runtime target
- obsolete migration instructions

## 10. External source rule

Do not operate on external repos.

Do not remove evidence lineage because it references historical sources.

## 11. Validation is not authorization

If issues are found:

- report them
- do not repair them

## 12. Output — DRY RUN REPORT

Return exactly:

# Integration dry-run report

## Identity map

## File comparison

## Legacy delta decisions

## Proposed minimal patch plan

## Skips / blockers

No file edits are allowed in this run.
