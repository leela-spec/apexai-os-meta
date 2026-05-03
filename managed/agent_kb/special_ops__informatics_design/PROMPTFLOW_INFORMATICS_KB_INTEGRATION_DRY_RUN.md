---
status: draft_promptflow
repo: leela-spec/apexai-os-meta
branch: main
target_agent: special_ops__informatics_design
target_root: managed/agent_kb/special_ops__informatics_design
scope: apex_new_base_integration
mode: preserve_new_base_patch_minimal_apex_delta
discovery_rule: check_newversion_and_newversions_before_blocking
---

# PROMPTFLOW — special_ops__informatics_design Apex New-Base Integration (DRY RUN)

## 0. Purpose

Integrate newly placed Apex AI OS KB files for `special_ops__informatics_design` into their standard KB paths.

This is a fidelity-preserving integration, not a cleanup, rewrite, redesign, normalization, localization, or rebuild.

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

Do not clean, improve, simplify, summarize, normalize, deduplicate, reorder, relabel, isolate, localize, sanitize, or redesign the new base.

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

Candidate new-base folders, both mandatory to check before declaring missing:

```text
managed/agent_kb/special_ops__informatics_design/newversion/
managed/agent_kb/special_ops__informatics_design/newversions/
```

If `newversion/` is absent or incomplete, check `newversions/` before reporting missing new base.

Do not modify anything in this promptflow. Dry-run only.

## 3. Non-negotiable discovery rule

Before any comparison or delta decision:

1. List files under `newversion/` if present.
2. List files under `newversions/` if present.
3. Inspect the H1 of every Markdown file in both folders.
4. Build the identity map from detected content identity, not from filename alone.
5. Do not mark a target missing until both candidate folders have been checked.

Known failure to prevent:

```text
Checking only newversion/ and concluding no new base exists, while the real folder is newversions/.
```

## 4. Valid Apex delta

Patch old Apex logic only if it is:

1. present in the old Apex file
2. absent from the mapped new base
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
- schema improvements
- deduplication
- appendix rewrites
- external repo as active target
- migration/process commentary
- source/provenance sanitization unless exactly obsolete or Apex-incompatible

## 5. Identity map (required, before any editing)

Produce the identity map before any file comparison:

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
- No new base found for target after checking both candidate folders -> do not overwrite with old Apex.
- Filename mismatch is only an identity-map problem, not permission to clean or redesign content.

Expected misfile pattern already observed for this agent:

| intended_target_file | likely physical source |
|---|---|
| `ESSENCE.md` | `newversions/LEARNING_QUEUE.md` |
| `BEST_PRACTICES.md` | `newversions/ESSENCE.md` |
| `LEARNING_QUEUE.md` | `newversions/MISTAKES.md` |
| `APPENDIX_KB_SOURCE_MANIFEST.md` | `newversions/BEST_PRACTICES.md` |
| `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` | `newversions/APPENDIX_KB_SOURCE_MANIFEST.md` |
| `APPENDIX_KB_CANDIDATE_LEDGER.md` | `newversions/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` |
| `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | `newversions/APPENDIX_KB_CANDIDATE_LEDGER.md` |
| `TEMPLATES.md` | unresolved; do not infer from promptflow body |
| `MISTAKES.md` | unresolved until H1 inspection finds it |

This table is a hint, not authority. Verify by H1/content identity during dry run.

## 6. File comparison

Produce:

| target_file | new_base_source | old_apex_file | comparison_result | repair_needed |
|---|---|---|---|---|

Do not compare by filename if the identity map mapped the target by H1.

## 7. Legacy delta decisions

Produce:

| old_file_element | keep / patch_into_new / reject | reason | exact_target_section |
|---|---|---|---|

Definitions:

- keep = already represented in new base; no patch
- patch_into_new = valid missing Apex delta
- reject = obsolete / duplicate / invalid / over-normalizing

## 8. Proposed minimal patch plan

Produce:

| target_file | patch_delta | target_section | risk | requires_approval |
|---|---|---|---|---|

All `patch_delta` entries must be Apex-compatibility deltas only.

## 9. Intentional overlap rule

Do not remove or relocate overlapping concepts.

Informatics Design may intentionally repeat schema, file-type, redundancy, and chunking doctrine across files.

Preserve internal redundancy and taxonomy.

## 10. Appendix rule

Appendices are database surfaces.

Do not:

- recreate
- sanitize
- collapse
- centralize
- summarize into Apex-local tables

Preserve:

- IDs
- row structures
- ranking logic
- candidate linkage
- evidence linkage
- source lineage
- cross-file pointers

Remove only:

- claims that an external repo is the active target/runtime
- obsolete migration process instructions
- instructions to operate outside Apex

Do not remove historical evidence references merely because they mention historical sources.

## 11. External source rule

Do not operate on external repos.

Do not preserve obsolete statements that external repos are active targets.

Do not remove evidence references, source IDs, or database lineage merely because they mention historical sources.

## 12. Validation is not authorization

If validation finds mismatch, ambiguity, missing files, or a broken mapping:

- report it
- do not repair it

Allowed repair in later approved patch phase: filename/H1 identity mapping only.
Forbidden repair: rewriting appendices into cleaner Apex-local tables.

## 13. Output — DRY RUN REPORT

Return exactly:

# Integration dry-run report

## New-base folder discovery

Report whether `newversion/` and `newversions/` exist, and which files were inspected.

## Identity map

| physical_new_base_path | detected_h1 | intended_target_file | confidence | action |
|---|---|---|---|---|

## File comparison

| target_file | new_base_source | old_apex_file | comparison_result | repair_needed |
|---|---|---|---|---|

## Legacy delta decisions

| old_file_element | keep / patch_into_new / reject | reason | exact_target_section |
|---|---|---|---|

## Proposed minimal patch plan

| target_file | patch_delta | target_section | risk | requires_approval |
|---|---|---|---|---|

## Skips / blockers

| target_file | reason | required_operator_action |
|---|---|---|

No file edits are allowed in this run.
