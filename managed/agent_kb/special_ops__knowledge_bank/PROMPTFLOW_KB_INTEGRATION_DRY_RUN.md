---
status: draft_promptflow
repo: leela-spec/apexai-os-meta
branch: main
target_agent: special_ops__knowledge_bank
target_root: managed/agent_kb/special_ops__knowledge_bank
scope: apex_new_base_integration
mode: preserve_new_base_patch_minimal_apex_delta
---

# PROMPTFLOW — special_ops__knowledge_bank Apex New-Base Integration (DRY RUN)

## 0. Purpose

Integrate newly placed Apex AI OS KB files for `special_ops__knowledge_bank` into their standard KB paths.

This is a fidelity-preserving integration, not a cleanup, rewrite, redesign, normalization, or rebuild.

The newly placed KB files are the canonical base. Existing Apex KB files are legacy-value sources only.

## 1. Prime directive

Preserve first. Patch second. Improve never.

The task is not to make the KB better; the task is to make the new KB base Apex-compatible without changing its design.

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

Allowed new-base folder:

```text
managed/agent_kb/special_ops__knowledge_bank/newversion/
```

Dry-run only. No file edits.

## 3. Valid Apex delta

Patch old Apex logic only if it is:

1. present in the old Apex file
2. absent from the new base
3. still valid for Apex AI OS
4. necessary for Apex operation
5. insertable without changing the new base architecture

Allowed Apex deltas include:

- candidate-to-promotion path
- project-to-meta learning flow
- meta-to-project release-pack assumptions
- source-note / promotion-trace boundaries
- owner / validator / review metadata

Reject:

- database simplification
- appendix restructuring
- deduplication
- schema normalization
- external repo as active target

## 4. Identity map

| physical_new_base_path | detected_h1 | intended_target_file | confidence | action |
|---|---|---|---|---|

## 5. File comparison

| target_file | new_base_source | old_apex_file | comparison_result | repair_needed |
|---|---|---|---|---|

## 6. Legacy delta decisions

| old_file_element | keep / patch_into_new / reject | reason | exact_target_section |
|---|---|---|---|

## 7. Proposed minimal patch plan

| target_file | patch_delta | target_section | risk | requires_approval |
|---|---|---|---|---|

## 8. Appendix rule

Appendices are database surfaces. Preserve IDs, row structures, ranking logic, and linkage.

## 9. Output — DRY RUN REPORT

Return:

# Integration dry-run report

## Identity map
## File comparison
## Legacy delta decisions
## Proposed minimal patch plan
## Skips / blockers

No file edits are allowed in this run.
