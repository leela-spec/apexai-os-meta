# META_DETECTIVE_WATCHDOG_QA_HYGIENE_PER_TARGET_DIFF_HANDOVER

Status: handover promptflow  
Owner: operator / next execution chat  
Target repo: `leela-spec/MasterOfArts`  
Target branch: `main`  
Purpose: create individual unified diff artifacts only  
Patching status: not part of this flow  
Runtime/config status: no runtime config edits  
Stop posture: stop on scope drift, missing target, failed validation, or any request to mutate target files directly

## 0. Why this handover exists

A previous recovery attempt created a single combined patch bundle. That is not the desired method.

The required method is stricter:

- one target file at a time
- one individual unified diff artifact per target file
- one mini-validation per diff artifact
- no patch application
- no whole-file replacement of target files
- no branch patching
- no silent target expansion
- no combined mega patch

This handover is the only intended instruction packet for the next chat.

## 1. Copy/paste prompt for the next chat

```text
You are executing a bounded GitHub repo handover for MasterOfArts.

Repository: leela-spec/MasterOfArts
Branch: main
Execution mode: create individual unified diff artifact files only.

Read and lock this handover first:
OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_PER_TARGET_DIFF_HANDOVER.md

Then read and lock the source execution plan:
OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md

Hard scope:
- Create unified diff artifacts only.
- Create each diff as its own separate file on main.
- Do not apply any diff.
- Do not patch, update, or replace the actual target files.
- Do not create or use a work branch.
- Do not create a PR.
- Do not edit openclaw.json.
- Do not create permanent agents.
- Do not create new KB roots.
- Do not move Hygiene Clean under Meta Detective.
- Do not create one combined patch bundle.
- Do not silently add extra targets.

Allowed writes:
Only write per-target .diff artifacts under:
OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/

Naming rule:
Use exactly one file per target and one iteration suffix:
01_new_working_file__iter01.diff
02_ESSENCE__iter01.diff
03_BEST_PRACTICES__iter01.diff
04_MISTAKES__iter01.diff
05_TEMPLATES__iter01.diff
06_LEARNING_QUEUE__iter01.diff
07_AGENT_KB_INDEX__iter01.diff
08_CROSS_REFERENCE_MANIFEST__iter01.diff
09_META_HEADS_KB_BASE_BUILD_INDEX__iter01.diff

If a diff artifact already exists, do not overwrite it silently. Create the next iteration suffix, for example __iter02.diff, and state why.

For each target, perform this micro-flow independently:
1. Read the source execution plan section for that phase.
2. Read the current target file from main, except for the new working file target where the target may not exist yet.
3. Lock the exact allowed change for that one target only.
4. Create a unified diff for only that target file.
5. Write the unified diff to its individual .diff artifact path on main.
6. Read back the written .diff artifact.
7. Validate the artifact:
   - starts with `diff --git`
   - contains exactly one `diff --git` block
   - touches exactly one target path
   - does not contain edits to any other target
   - does not apply the patch
   - does not mutate the target file
   - does not mention or edit openclaw.json
   - does not create a permanent agent or KB root
   - preserves Hygiene Clean as separate
   - uses only 1-100 EVD / IMP / RSK scoring where scores appear
8. Only after read-back validation passes, continue to the next target.

Final output required:
A compact validation report with one row per diff artifact:
- artifact path
- target path
- source phase
- validation: pass / hold
- reason if hold

Return `yes` only if all required diff artifacts are created and pass read-back validation. Otherwise return `hold` plus the first blocker.
```

## 2. Locked target list

The next chat must treat these as the only target files for diff generation.

| Order | Source phase | Target file | Diff artifact file |
|---:|---|---|---|
| 01 | Phase 1 | `OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_EXECUTION_PROMPTFLOW_COMPLIANCE_AUDITOR_WORKING.md` | `OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/01_new_working_file__iter01.diff` |
| 02 | Phase 2 | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/ESSENCE.md` | `OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/02_ESSENCE__iter01.diff` |
| 03 | Phase 3 | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/BEST_PRACTICES.md` | `OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/03_BEST_PRACTICES__iter01.diff` |
| 04 | Phase 4 | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/MISTAKES.md` | `OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/04_MISTAKES__iter01.diff` |
| 05 | Phase 5 | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/TEMPLATES.md` | `OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/05_TEMPLATES__iter01.diff` |
| 06 | Phase 6 | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/LEARNING_QUEUE.md` | `OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/06_LEARNING_QUEUE__iter01.diff` |
| 07 | Phase 7 | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/AGENT_KB_INDEX.md` | `OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/07_AGENT_KB_INDEX__iter01.diff` |
| 08 | Phase 7 | `OpenClaw/07_finalopenclawsystem/managed/knowledge/CROSS_REFERENCE_MANIFEST.md` | `OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/08_CROSS_REFERENCE_MANIFEST__iter01.diff` |
| 09 | Phase 7 | `agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md` | `OpenClaw/07_finalopenclawsystem/docs/working/diffs/meta_detective_watchdog_qa_hygiene/09_META_HEADS_KB_BASE_BUILD_INDEX__iter01.diff` |

## 3. Target-specific requirements

### 01 — New working mode file

Create only a diff artifact for the new file:

`OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_EXECUTION_PROMPTFLOW_COMPLIANCE_AUDITOR_WORKING.md`

The unified diff should use `/dev/null` as the source if the file does not exist on main.

Required content sections in the proposed file:

- Status block
- Purpose
- Activation triggers
- Owns / does not own
- Input shape
- Output shape
- Compliance gate checklist
- Handoff partners
- Failure modes
- Template snippet
- Candidate KB target
- Metric convention: 1-100 only

Forbidden in this diff:

- permanent agent creation
- new KB root creation
- runtime config mutation
- moving Hygiene Clean under Detective

### 02 — ESSENCE.md

Create only a diff artifact for:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/ESSENCE.md`

Required changes in the diff:

- mission language expands from adversarial validation only to cross-agent watchdog for truth, process compliance, contradiction, drift, and escalation
- add `Execution & Promptflow Compliance Auditor` to accepted internal mode map
- add explicit QA/Hygiene watchdog language
- keep Hygiene Clean separate
- add rule: artifact evidence beats self-report
- add rule: Detective may audit Hygiene/Ops/Strategy outputs when compliance affects truth, authority, execution safety, or drift

Forbidden:

- whole-file replacement style
- unrelated rewrite of existing doctrine
- new sub-agent language
- new KB root language

### 03 — BEST_PRACTICES.md

Create only a diff artifact for:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/BEST_PRACTICES.md`

Required accepted practices to add or minimally patch:

1. Use Execution & Promptflow Compliance Auditor for repo writes and patch/diff claims.
2. Require artifact evidence for compliance claims.
3. Treat QA/Hygiene watchdogging as core Detective capability.
4. Keep Hygiene Clean separate but auditable by Detective.
5. Activate Detective Compliance Gate on high-risk or method-constrained work.

Every score entry added or touched must use:

```yaml
score_scale: 1-100
```

Forbidden:

- changing unrelated accepted practices
- converting this into a prompt/workflow owner file
- moving Hygiene under Detective

### 04 — MISTAKES.md

Create only a diff artifact for:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/MISTAKES.md`

Required accepted mistake entries:

- `DET-MIS-PROCESS-COMPLIANCE-FALSE-POSITIVE`
- `DET-MIS-SCOPE-EXPANSION-AS-DILIGENCE`
- `DET-MIS-SELF-REPORTED-COMPLIANCE`
- `DET-MIS-PROMPTFLOW-TREATED-AS-DECORATION`

Every entry must use:

```yaml
score_scale: 1-100
```

Forbidden:

- altering unrelated mistake entries except minimal index/intro references if necessary
- introducing 1-5 score scale

### 05 — TEMPLATES.md

Create only a diff artifact for:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/TEMPLATES.md`

Required templates:

- Detective Compliance Gate
- Execution Method Truth Check
- Instruction Parity Audit
- Scope Containment Audit
- Artifact Evidence Checklist
- Self-Validation Blocker

Every scored template entry must use:

```yaml
score_scale: 1-100
```

Forbidden:

- replacing existing template suite
- making Detective into patch executor

### 06 — LEARNING_QUEUE.md

Create only a diff artifact for:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/LEARNING_QUEUE.md`

Required candidate entry:

```yaml
learning_entry:
  id: candidate_meta_detective_watchdog_qa_hygiene_pack_v0
  status: strong_candidate
  source_ref:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_ORIENTATION_WORKING.md
  summary: Candidate watchdog expansion for Meta Detective. Adds Execution & Promptflow Compliance Auditor and makes QA/Hygiene watchdogging core to Detective while keeping Hygiene Clean structurally separate.
  candidate_target: mixed_pack
  candidate_targets:
    - essence
    - best_practice
    - mistake
    - template
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md
  scores:
    score_scale: 1-100
    EVD: 94
    IMP: 97
    RSK: 32
  owner: meta_detective
  validator: special_ops__hygiene_clean
  overlap_check: Verify boundaries with meta_ops, hygiene_clean, knowledge_bank, prompts_workflows, informatics_design, and ai_handling_routing.
  review_due: 2026-07-25
```

Forbidden:

- promoting the candidate directly to accepted canon beyond what the source plan requires
- removing candidate-only safeguards

### 07 — AGENT_KB_INDEX.md

Create only a diff artifact for:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/AGENT_KB_INDEX.md`

Required pointer additions only if not already present:

- `OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md`
- `OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_EXECUTION_PROMPTFLOW_COMPLIANCE_AUDITOR_WORKING.md`

Forbidden:

- changing KB root map except minimal meta_detective notes if required
- adding new KB root

### 08 — CROSS_REFERENCE_MANIFEST.md

Create only a diff artifact for:

`OpenClaw/07_finalopenclawsystem/managed/knowledge/CROSS_REFERENCE_MANIFEST.md`

Required pointer additions only if not already present:

- `OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md`
- `OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_EXECUTION_PROMPTFLOW_COMPLIANCE_AUDITOR_WORKING.md`

Forbidden:

- changing runtime references
- creating source authority where the working files are only working/candidate surfaces

### 09 — META_HEADS_KB_BASE_BUILD_INDEX.md

Create only a diff artifact for:

`agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md`

Required pointer additions only if not already present:

- `OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md`
- `OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_EXECUTION_PROMPTFLOW_COMPLIANCE_AUDITOR_WORKING.md`

Forbidden:

- changing meta_strategy section
- changing manual attachment sections except if strictly necessary to preserve numbering after a local insertion
- treating working files as accepted canon

## 4. Diff artifact validation checklist

Each individual `.diff` artifact must pass this checklist before moving to the next target.

```yaml
diff_artifact_validation:
  artifact_path:
  target_path:
  source_phase:
  read_current_target_from_main: pass | fail | not_applicable_new_file
  starts_with_diff_git: pass | fail
  exactly_one_diff_git_block: pass | fail
  exactly_one_target_path: pass | fail
  no_target_file_mutation: pass | fail
  no_patch_application: pass | fail
  no_openclaw_json_touch: pass | fail
  no_new_permanent_agent: pass | fail
  no_new_kb_root: pass | fail
  hygiene_clean_separate: pass | fail
  score_scale_1_100_only: pass | fail | not_applicable
  verdict: pass | hold
  blocker:
```

## 5. Stop conditions

Stop immediately and report `hold` if any of these occur:

- a required source plan file cannot be read
- a target file cannot be read, except the new working file target
- a diff cannot be isolated to one target file
- the process would require editing `openclaw.json`
- the process would require creating a new permanent agent
- the process would require creating a new KB root
- the process would move Hygiene Clean under Meta Detective
- the process would mutate any actual target file
- the process would apply a diff
- the process would overwrite an existing diff artifact without an iteration suffix
- a generated diff reintroduces 1-5 scoring
- a generated diff mixes multiple target files
- a generated diff silently adds targets not in this handover

## 6. Explicit non-goals

The next chat must not do any of the following:

- apply the generated diffs
- open a PR
- create an execution branch
- patch `ESSENCE.md` or any target file directly
- use whole-file replacements for managed KB targets
- delete the existing combined patch bundle unless the operator explicitly asks
- create cleanup commits unless explicitly requested
- perform broader architecture redesign
- expand beyond the plan phases

## 7. Recommended final report shape

```md
# Per-target unified diff artifact validation

| # | Artifact | Target | Phase | Validation | Notes |
|---:|---|---|---|---|---|
| 01 |  |  | Phase 1 | pass / hold |  |
| 02 |  |  | Phase 2 | pass / hold |  |
| 03 |  |  | Phase 3 | pass / hold |  |
| 04 |  |  | Phase 4 | pass / hold |  |
| 05 |  |  | Phase 5 | pass / hold |  |
| 06 |  |  | Phase 6 | pass / hold |  |
| 07 |  |  | Phase 7 | pass / hold |  |
| 08 |  |  | Phase 7 | pass / hold |  |
| 09 |  |  | Phase 7 | pass / hold |  |

Final verdict: yes / hold
First blocker if hold:
```

## 8. Final lock statement for next chat

Before writing any diff artifact, the next chat must explicitly state:

```text
Scope locked: I will create only individual per-target unified diff artifacts on main under docs/working/diffs/meta_detective_watchdog_qa_hygiene/. I will not apply diffs, patch target files, create a branch, create a PR, edit openclaw.json, create agents, create KB roots, or move Hygiene Clean under Meta Detective.
```
