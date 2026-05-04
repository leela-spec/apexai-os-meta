---
status: active_promptflow
repo: leela-spec/apexai-os-meta
branch: main
scope: five_special_ops_new_base_file_drift_research
mode: research_before_patch_no_file_edits
write_policy: report_only
created_for: ApexAI_OS autonomous KB migration and new-base integrity validation
---

# PROMPTFLOW - Special Ops New-Base File Drift Research

## 0. Purpose

Run a mandatory pre-patch research pass for the five Special Ops agent KB new-base folders before any Apex delta integration, promotion, harmonization, or unified-diff patching.

This promptflow exists because prior integration attempts showed two dangerous failure classes:

1. legacy repo/reference drift: old external repo, runtime, execution-root, or promptflow references can become false active instructions after migration into Apex;
2. body/filename drift: files inside `newversion/` or `newversions/` may have headings or bodies that appear to belong to another target file.

This is a research and reporting flow only. It does not patch files.

## 1. Hard repo lock

Required repo:

```text
leela-spec/apexai-os-meta
```

If the current repo is not exactly `leela-spec/apexai-os-meta`, stop with:

```text
blocked_repo_mismatch
```

Do not operate on external repos. Do not follow deprecated promptflow targets, old execution roots, or external runtime/write instructions.

## 2. Exact target agent folders

Run this flow for exactly these five folders:

```text
managed/agent_kb/special_ops__informatics_design/
managed/agent_kb/special_ops__prompts_workflows/
managed/agent_kb/special_ops__knowledge_bank/
managed/agent_kb/special_ops__ai_handling_routing/
managed/agent_kb/special_ops__hygiene_clean/
```

For each folder, inspect both possible new-base folders if present:

```text
managed/agent_kb/<AGENT_ID>/newversion/
managed/agent_kb/<AGENT_ID>/newversions/
```

Do not conclude that a new-base folder is missing until both have been checked.

## 3. Hard non-edit rule

This promptflow is research only.

Forbidden in this run:

```text
- modifying standard KB root files
- modifying files under newversion/
- modifying files under newversions/
- modifying appendices
- creating patches
- applying patches
- renaming files
- moving files
- deleting files
- promoting files into standard KB paths
- syncing standard files into newversion/newversions
```

Allowed output:

```text
- in-chat report, or
- a separate operator-requested report artifact, if explicitly requested
```

Default: return the report in chat.

## 4. Controlling principle

```text
The task is not to make the KB better.
The task is to determine whether the five new-base folders are safe to patch later.
```

A heading difference alone is not evidence of corruption. A repeated pattern where file bodies appear to be stored under the wrong filenames is evidence of possible compromise and must be researched before patching.

## 5. Legacy-reference drift research

### 5.1 Search target

For each of the five target folders, search every file under:

```text
managed/agent_kb/<AGENT_ID>/**
```

Search for legacy/external drift references, including:

```text
MasterOfArts
OpenClaw
07_finalopenclawsystem
external repo
old execution root
deprecated promptflow
Apex forbidden as target
non-Apex runtime
```

### 5.2 Classification

Produce this ledger:

```markdown
| agent_id | file | reference_text | reference_type | risk | useful_info | required_action |
|---|---|---|---|---|---|---|
```

Allowed `reference_type`:

```text
active_target_or_runtime_claim
old_execution_instruction
old_source_of_truth_claim
deprecated_promptflow_reference
historical_build_trace
source_lineage_note
ambiguous_drift_risk
```

Allowed `required_action`:

```text
rewrite_into_apex_native_language
remove_as_no_value
operator_decision_required
ignore_if_promptflow_only_and_not_part_of_final_kb_body
```

### 5.3 Final Apex autonomy rule

Final Apex KB files should have no legacy repo references. If useful information still depends on legacy wording, extract the useful information and rewrite it into Apex-native language in the later patch phase. If safe rewriting is not possible, flag it for operator handling.

Do not silently delete useful content merely because it contains a legacy reference.

## 6. Body/filename integrity research

### 6.1 Research objective

Determine whether unusual headings in `newversion/` or `newversions/` files are:

```text
1. legitimate internal headings/cross-references,
2. harmless redesign differences,
3. body/filename mismatches,
4. export/order-shift corruption,
5. non-KB artifacts accidentally placed in the new-base folder.
```

### 6.2 Files to inspect

For each agent, inspect every Markdown file under both new-base folders, especially:

```text
ESSENCE.md
BEST_PRACTICES.md
MISTAKES.md
TEMPLATES.md
LEARNING_QUEUE.md
appendices/*.md
PROMPTFLOW*.md
SOURCE*.md
```

Also read the standard KB files only as reference points:

```text
managed/agent_kb/<AGENT_ID>/ESSENCE.md
managed/agent_kb/<AGENT_ID>/BEST_PRACTICES.md
managed/agent_kb/<AGENT_ID>/MISTAKES.md
managed/agent_kb/<AGENT_ID>/TEMPLATES.md
managed/agent_kb/<AGENT_ID>/LEARNING_QUEUE.md
managed/agent_kb/<AGENT_ID>/appendices/*.md
```

These standard files are read-only in this flow.

## 7. Required research steps

### Step 1 - Folder inventory

For each of the five agents, produce:

```markdown
| agent_id | folder | file_path | file_exists | size_chars | first_nonempty_line | detected_h1 | file_type_guess |
|---|---|---|---:|---:|---|---|---|
```

Purpose:

```text
- detect missing files
- detect accidental promptflow files
- detect empty files
- detect shifted appendices
- detect duplicate or near-duplicate bodies
```

### Step 2 - Filename expectation map

Use this expectation map for every agent:

```markdown
| expected_target_file | expected_role | expected_content_signals |
|---|---|---|
| ESSENCE.md | compact activation / role boundary | doctrine, scope, activation, file map, priorities |
| BEST_PRACTICES.md | operational practice rules | BP IDs, practices, rules, operating pattern |
| MISTAKES.md | failure patterns | mistakes, anti-patterns, recovery, failure modes |
| TEMPLATES.md | reusable schemas/templates | template blocks, row schemas, examples |
| LEARNING_QUEUE.md | candidate/future research backlog | candidate, deferred, research, promotion required |
| APPENDIX_KB_SOURCE_MANIFEST.md | provenance/source database | source_path, source_role, coverage, gap |
| APPENDIX_KB_INFORMATION_RANKING_LEDGER.md | ranking database | rank, info_unit, target_file, score |
| APPENDIX_KB_CANDIDATE_LEDGER.md | candidate database | candidate_id, status, promotion, evidence |
| APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md | failure/evidence database | drift, evidence, postmortem, countermeasure |
```

### Step 3 - Body-role classification

For each physical file in the new-base folders, classify the body role:

```markdown
| agent_id | physical_path | filename_expected_role | detected_h1 | body_role_guess | confidence | evidence_lines | mismatch_type |
|---|---|---|---|---|---|---|---|
```

Allowed `body_role_guess`:

```text
essence_body
best_practices_body
mistakes_body
templates_body
learning_queue_body
source_manifest_appendix
information_ranking_appendix
candidate_ledger_appendix
anti_drift_evidence_appendix
promptflow_artifact
source_conflict_report
qa_or_research_appendix
unknown
```

Allowed `mismatch_type`:

```text
none
heading_only_difference
cross_reference_heading
body_filename_mismatch
appendix_shift
promptflow_in_new_base
duplicate_body
missing_body
ambiguous
```

### Step 4 - Determine whether unusual H1 is legitimate

A heading is probably legitimate if:

```text
- filename role and body role match;
- H1 is a redesigned title or subsection, not a file identity label;
- file contains expected sections for its filename;
- cross-reference is explicit and not pretending to be the file identity;
- no duplicate body appears elsewhere.
```

A heading is suspicious if:

```text
- H1 exactly names another canonical target file;
- body sections match another file's expected role;
- several files form a shifted sequence;
- a promptflow appears where a KB scaffold should be;
- the intended body appears elsewhere under another filename.
```

## 8. Compromise detection scoring

Use this scoring matrix:

```markdown
| suspicion_signal | score |
|---|---:|
| H1 names another canonical target file | +3 |
| body role matches another target file | +4 |
| expected body appears elsewhere | +5 |
| several files form sequential shift | +5 |
| promptflow file appears in scaffold slot | +4 |
| appendix body appears in scaffold slot | +4 |
| filename and body role agree | -5 |
| only stylistic H1 difference | -3 |
| explicit cross-reference wording | -2 |
| body has expected role sections | -4 |
```

Classification:

```markdown
| score | classification | action |
|---:|---|---|
| <= 0 | likely_legitimate | Continue normally in later patchflow. |
| 1-4 | needs_review | Continue only if target file is not patch-critical; otherwise flag. |
| 5-8 | likely_mismatch | Later patchflow must map by body role if clear; do not patch by filename. |
| 9+ | probable_compromised_new_base | Stop later patch phase and require operator decision or reconstruction. |
```

Folder-level severe threshold:

```text
If 3 or more canonical target files show likely mismatch, classify the folder as probable_compromised_new_base.
```

## 9. Required output: New-Base Body/Filename Integrity Report

For each of the five agents, output:

```markdown
# New-Base Body/Filename Integrity Report - <AGENT_ID>

## Agent
- agent_id:
- target_root:
- folders_checked:
  - newversion/
  - newversions/

## A. Folder inventory
| folder | file_path | file_exists | detected_h1 | file_type_guess | notes |
|---|---|---:|---|---|---|

## B. Body-role classification
| physical_path | filename_expected_role | detected_h1 | body_role_guess | confidence | mismatch_type |
|---|---|---|---|---|---|

## C. Suspicion scoring
| physical_path | score | classification | evidence | recommended_action |
|---|---:|---|---|---|

## D. Target mapping proposal
| intended_target_file | selected_physical_source | mapping_basis | confidence | safe_to_patch |
|---|---|---|---|---|

## E. Missing / duplicate / artifact findings
| finding | severity | affected_files | operator_action_needed |
|---|---|---|---|

## F. Decision
One of:
- proceed_patch_by_filename
- proceed_patch_by_mapped_body_role
- proceed_partial_skip_ambiguous
- stop_new_base_compromised
```

## 10. Cross-agent summary report

After all five agents are inspected, produce:

```markdown
# Five-Agent New-Base Drift Research Summary

## A. Agent status matrix
| agent_id | newversion_found | newversions_found | legacy_refs_found | likely_mismatch_count | severe_findings | decision |
|---|---:|---:|---:|---:|---|---|

## B. Legacy reference drift ledger
| agent_id | file | reference_text | reference_type | risk | useful_info | required_action |
|---|---|---|---|---|---|---|

## C. Cross-agent compromise pattern
| pattern | affected_agents | evidence | severity | recommendation |
|---|---|---|---|---|

## D. Operator decisions required before patching
| decision_id | agent_id | issue | options | recommendation |
|---|---|---|---|---|

## E. Patch-readiness conclusion
One of:
- all_agents_ready_for_apex_delta_patch
- some_agents_ready_some_blocked
- all_agents_blocked_pending_new_base_reconstruction
```

## 11. Stop conditions for later patchflow

The later Apex delta patchflow must not run for an agent if this research flow finds:

```text
- multiple target bodies appear under wrong filenames with high confidence
- same intended target body appears in multiple files
- required target body cannot be found anywhere
- promptflow/provenance artifact occupies a scaffold target slot
- appendix bodies are shifted into scaffold files and scaffold bodies are missing
- no reliable mapping from intended target file to physical source exists
- three or more canonical target files show likely mismatch
```

## 12. Continue conditions for later patchflow

The later Apex delta patchflow may continue for an agent only if:

```text
- all expected target bodies are found, or missing files are explicitly reported and excluded;
- each intended target has exactly one selected physical source;
- ambiguous files are skipped and not patched;
- mapping table is explicit;
- later unified diffs target selected physical source paths only;
- standard root files remain read-only.
```

## 13. Final response requirements

Do not claim the five agents are patch-ready unless the report includes:

```text
- folder inventory for all five agents
- body-role classification for all discovered new-base files
- legacy-reference drift ledger
- suspicion scoring
- target mapping proposal
- per-agent decision
- cross-agent patch-readiness conclusion
```

Do not claim a folder is compromised without evidence from the scoring matrix.
Do not claim unusual headings are harmless without body-role evidence.
Do not patch files in this promptflow.
