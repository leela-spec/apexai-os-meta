---
promptflow_id: hygiene_clean_unified_diff_artifact_manufacturing
repo_boundary: single_repo_only
working_repo: leela-spec/MasterOfArts
target_repo: leela-spec/MasterOfArts
target_branch: main
target_agent: special_ops__hygiene_clean
target_kb_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
artifact_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/
status: active
mode: bounded_artifact_manufacturing
created_for: continuation of approved Hygiene Clean KB unified-diff artifact sequence
---

# Promptflow: Hygiene Clean Unified Diff Artifact Manufacturing

## 1. Purpose

Create one unified-diff artifact per approved Hygiene Clean KB target file.

This promptflow exists to prevent context loss and scope drift during the remaining diff iterations.

It governs artifact creation only: each output is a `.diff` file stored in the Hygiene Clean appendix folder. It does not apply the diff to the target scaffold file.

## 2. Hard scope boundary

- **Only repo:** `leela-spec/MasterOfArts`.
- **Only branch:** `main`.
- **Only target root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/`.
- **Only artifact root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/`.
- **Allowed write type:** create one `.diff` artifact file per iteration.
- **Forbidden:** direct patching of scaffold or appendix target files in this promptflow.
- **Forbidden:** source expansion outside the Hygiene Clean KB folder.
- **Forbidden:** broad governance, bootstrap, project-wide protocol, or architecture rereads.
- **Forbidden:** revisiting approval decisions.

## 3. Source authority

Use only these local repo sources:

1. `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/ChangesHygiene.md`
2. `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/ChangesHygiene2.md`
3. current target file content for the one file being diffed, if the file already exists
4. prior `.diff` artifacts in the same appendix folder, only to avoid duplicate numbering or duplicate work

No other source is authorized for this diff-manufacturing flow.

## 4. Approved changed-file set

The only target files approved for unified-diff artifacts are:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/ESSENCE.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/BEST_PRACTICES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/TEMPLATES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/LEARNING_QUEUE.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_SOURCE_MANIFEST.md
```

## 5. Required diff artifact sequence

| Step | Target file | Diff artifact path | Status |
|---:|---|---|---|
| 1 | `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` | `appendices/PATCH_001_APP_KB_QA_AND_NEXT_RESEARCH_PLAN.diff` | created |
| 2 | `ESSENCE.md` | `appendices/PATCH_002_ESSENCE.diff` | pending |
| 3 | `BEST_PRACTICES.md` | `appendices/PATCH_003_BEST_PRACTICES.diff` | pending |
| 4 | `TEMPLATES.md` | `appendices/PATCH_004_TEMPLATES.diff` | pending |
| 5 | `LEARNING_QUEUE.md` | `appendices/PATCH_005_LEARNING_QUEUE.diff` | pending |
| 6 | `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md` | `appendices/PATCH_006_APP_KB_CANDIDATE_LEDGER.diff` | pending |
| 7 | `appendices/APPENDIX_KB_SOURCE_MANIFEST.md` | `appendices/PATCH_007_APP_KB_SOURCE_MANIFEST.diff` | pending |

## 6. Per-iteration procedure

For each remaining step, execute exactly this sequence:

1. Read `ChangesHygiene.md`.
2. Read `ChangesHygiene2.md`.
3. Read only the one current target file for the active step.
4. Create exactly one unified diff for the active target file.
5. Write the unified diff directly to the corresponding `.diff` artifact path listed above.
6. Stop.

Do not produce any other repo file in that iteration.

## 7. Unified diff format requirements

Every `.diff` artifact must satisfy:

- starts with `diff --git a/... b/...`
- contains exactly one target file diff
- uses the approved target path exactly
- writes only under `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/`
- if the target file is new, uses `new file mode 100644`, `--- /dev/null`, and `+++ b/<target>`
- if the target file exists, uses `--- a/<target>` and `+++ b/<target>`
- contains no ellipses, placeholders, TODO patch text, or omitted hunks
- contains no changes to non-target files

## 8. Content control requirements

Every diff must implement only approved rows from the design table:

| Target file | Approved content scope |
|---|---|
| `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` | create permanent QA / next-research appendix from `HYG-UPD-001` |
| `ESSENCE.md` | status vocabulary, read-budget profiles, compact KB map, routing boundary summary; preserve role boundary, authority/verification doctrine, candidate/truth boundary |
| `BEST_PRACTICES.md` | preserve core practices; add Hygiene-to-Night routing practice; avoid redundancy and Markdown strictness doctrine |
| `TEMPLATES.md` | template chooser, severity crib, closure validity checklist, candidate realization trace schema, source-note row, config-impact audit trigger, cross-agent routing check, exact-preservation validation fields |
| `LEARNING_QUEUE.md` | preserve candidate-only semantics; normalize statuses; point realization trace to candidate ledger |
| `APPENDIX_KB_CANDIDATE_LEDGER.md` | add realization trace fields and status-after-build columns; mark existing candidates as realized, appendix-only, queue-only, or deferred |
| `APPENDIX_KB_SOURCE_MANIFEST.md` | add update-authority note, source-gap severity markers, Source Notes register, Conflict Watch register; do not create standalone source-notes appendix |

Deferred and rejected items must remain deferred or rejected. They must not be silently integrated.

## 9. Validation gate after each diff artifact

After writing each `.diff` artifact, validate it against these controls:

```yaml
validation_gate:
  artifact_exists: true
  artifact_path_under_appendices: true
  unified_diff_format: true
  exactly_one_target_file: true
  target_file_in_approved_changed_file_set: true
  target_path_under_hygiene_clean_kb_root: true
  content_maps_to_ChangesHygiene: true
  content_maps_to_ChangesHygiene2: true
  no_unapproved_targets: true
  no_deferred_item_integrated: true
  no_rejected_item_integrated: true
  no_broad_governance_or_project_scope: true
```

If any check fails, stop and report the failed check. Do not proceed to the next diff.

## 10. Final validation after all seven diff artifacts

After all seven `.diff` artifacts exist, perform a final control pass:

1. Confirm exactly seven patch artifact files exist with names `PATCH_001` through `PATCH_007`.
2. Confirm each artifact contains exactly one `diff --git` header.
3. Confirm the seven target files exactly match the approved changed-file set in `ChangesHygiene2.md`.
4. Confirm every approved `HYG-UPD-001` through `HYG-UPD-013` is represented in at least one diff artifact.
5. Confirm every approved `HC-CAND-001` through `HC-CAND-011` and `HC-CAND-013` through `HC-CAND-016` is represented or preserved according to the design table.
6. Confirm `HC-CAND-012` remains deferred or appendix-only.
7. Confirm `HYG-UPD-014` through `HYG-UPD-022` remain deferred.
8. Confirm `HYG-UPD-023` remains rejected.
9. Confirm no diff writes outside the Hygiene Clean KB root.
10. Emit a compact validation report as `appendices/PATCHSET_VALIDATION_REPORT.md` only after all seven diffs exist.

## 11. Stop rule

For the next iteration, produce only the next pending `.diff` artifact in the required sequence and then stop.

The next pending artifact after creation of this promptflow is:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_002_ESSENCE.diff
```
