---
class: appendix
role: PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS
surface: agent_kb_appendix
quality: proposed
scope: agent
purpose: define the preimage-checked scaffold mutation process and the GitHub full-file replacement versus localized diff distinction
status: created
created_at: 2026-05-07
owner: special_ops__prompts_workflows
validator: meta_ops
task_id: TASK-13
target_agent: special_ops__prompts_workflows
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
source_refs:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FRAME_PROCESS_CLOSE_REPORT.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/LEARNING_QUEUE.md
---

# APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS

## 1. Purpose

This appendix defines the safer scaffold-mutation process discovered after TASK-00 through TASK-12 of the constant-frame-controlled KB integration.

It records the operational distinction between deterministic Git/GitHub storage behavior and probabilistic AI construction of replacement content. It also defines a preimage-checked scaffold mutation workflow for future critical updates to accepted KB scaffold files.

This appendix is evidence and process guidance only. It does not mutate `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, or `LEARNING_QUEUE.md`.

## 2. Core distinction: deterministic GitHub storage versus probabilistic AI construction

The central distinction is:

| Layer | Actor | Determinism | Failure surface |
|---|---|---|---|
| Fetch current file | GitHub contents API or equivalent connector | Deterministic for a specific ref and path | Wrong path/ref, stale branch, auth failure |
| Decide target modification | AI executor or human operator | Probabilistic / judgment-based | Drift, omission, hallucinated anchors, broad rewrite |
| Construct replacement content or patch | AI executor or deterministic patch tool | Mixed | AI may reconstruct unrelated content incorrectly; tool may apply exactly what it is given |
| Store updated content | GitHub/Git object database | Deterministic | Stores exactly submitted bytes as a new object |
| Compute commit diff | Git | Deterministic | Diff view can be misinterpreted but computation is deterministic |
| Interpret whether change is safe | AI verifier, Meta Detective, operator | Mixed | False validation, missed unrelated hunk, self-approval |

GitHub full-file replacement is not the dangerous probabilistic step. GitHub deterministically stores the complete content submitted to it. The risk is upstream: the AI may construct that complete submitted content incorrectly.

Accepted process rule:

```yaml
mechanism_truth:
  github_storage: deterministic
  git_diff_computation: deterministic
  ai_replacement_content_construction: probabilistic
  primary_risk_surface: between_live_file_fetch_and_write_submission
  required_control_for_critical_scaffold: preimage_checked_patch_before_write
```

## 3. Git object model: blob, tree, commit, SHA, diff

Git stores repository history through content-addressed objects.

| Object | Meaning | Process relevance |
|---|---|---|
| Blob | Exact file content bytes. | A file update creates a new blob when content changes. |
| Tree | Directory snapshot mapping names to blobs and subtrees. | A commit points to a tree representing the repo state. |
| Commit | Snapshot metadata: tree, parent commit(s), author/committer, message. | Audit unit for one task result. |
| SHA | Cryptographic object identifier derived from object content. | Verifies exact object identity; if content changes, SHA changes. |
| Diff | Deterministic comparison between old and new content. | Shows semantic change hunks but not necessarily the write mechanism. |

A GitHub contents update for an existing file generally requires the current blob SHA. The write replaces the file content at the path with submitted complete content and records a new commit. Git then computes a diff between the old blob and the new blob.

Important consequence:

```yaml
git_object_consequence:
  full_file_content_can_be_submitted: true
  resulting_diff_can_still_be_localized: true
  localized_diff_does_not_prove_atomic_search_replace_was_used: true
  whole_file_blob_replacement_does_not_itself_mean_semantic_drift_occurred: true
```

## 4. Mechanical write versus semantic diff

Mechanical write and semantic diff are separate concepts.

### 4.1 Mechanical write

Mechanical write is how the repository receives and stores new content.

For GitHub contents-style writes:

```text
old file blob -> submitted complete replacement content -> new file blob -> new commit
```

This is deterministic once the submitted content is fixed. It does not prove that a bounded patch operation happened before submission.

### 4.2 Semantic diff

Semantic diff is Git's comparison between old and new file content.

A complete replacement submission can produce a small diff:

```text
old file:
A
B
C

new submitted file:
A
B changed
C

Git diff:
- B
+ B changed
```

The localized diff proves that the old and new blobs differ only in localized places. It does not prove that an exact `SEARCH/REPLACE` operation or `git apply` patch was used.

### 4.3 Required wording discipline

```yaml
allowed_claims:
  - GitHub stored a new blob for the submitted file content.
  - Git diff showed localized semantic changes.
  - The changed-file set contained only the authorized target file when commit evidence shows that.
forbidden_claims_without_evidence:
  - A true in-place search/replace engine was used.
  - A standalone patch file was created.
  - The file was not mechanically rewritten as a new blob.
  - Preimage matching occurred before write.
```

## 5. Why the previous whole-file update worked

TASK-07 through TASK-11 did not visibly drift because several controls overlapped:

| Control | Effect |
|---|---|
| Single target file per task | Reduced blast radius. |
| Target root lock | Prevented cross-lane or cross-repo mutation. |
| Appendices before scaffold | Kept deep content out of scaffold files. |
| Existing-entry preservation instructions | Reduced pressure to reconstruct or rewrite old doctrine. |
| Clear anchors and ID sequence | New entries could be appended after stable existing IDs. |
| Compact scaffold rule | Prevented appendix-depth schema dumps. |
| External-claim quarantine | Kept model/platform/runtime claims out of accepted doctrine. |
| Fetch-back and commit-diff review | Detected whether the final stored content drifted. |

This was successful because the AI-generated complete replacement content was close to the live file and the resulting Git diffs showed only localized additions or narrow authorized edits.

However, the non-drift result was validated after the write. It was not guaranteed by a pre-write exact preimage check.

## 6. When whole-file update breaks

Full-file update becomes unsafe when the AI must reconstruct or preserve large amounts of existing content without a deterministic preimage constraint.

| Break condition | Failure mode |
|---|---|
| Long file near context limits | AI omits sections or compresses old content. |
| Many similar anchors | AI inserts at wrong location or changes wrong block. |
| Broad instruction such as “clean up” or “harmonize” | Unrelated content gets rewritten. |
| No exact old_text copied from live file | Patch intent floats free of actual preimage. |
| No occurrence count | Duplicate anchors allow unintended replacement. |
| No pre-write dry run | Write happens before mismatch is detected. |
| No changed-file set review | Other files or unexpected paths can change unnoticed. |
| No commit diff inspection | Semantic drift can be accepted by self-report. |
| Operator accepts closure without evidence | False validation becomes process truth. |
| External/runtime claims appear in generated content | Unverified doctrine contamination. |

Rule:

```yaml
whole_file_update_risk_rule:
  if_existing_file_has_accepted_doctrine: prefer_preimage_checked_patch
  if_file_is_long_or_anchor_ambiguous: require_patch_plan_or_halt
  if_full_body_is_not_explicitly_authorized: full_body_replacement_forbidden
```

## 7. Required preimage-checked scaffold mutation process

Critical scaffold mutation must use a preimage-checked process unless full-body replacement is explicitly authorized.

```yaml
preimage_checked_scaffold_mutation_process:
  applies_to:
    - ESSENCE.md
    - BEST_PRACTICES.md
    - MISTAKES.md
    - TEMPLATES.md
    - LEARNING_QUEUE.md
    - other accepted doctrine surfaces
  default_mode: search_replace_preimage_checked
  steps:
    - fetch_live_target_file
    - record_live_file_sha
    - draft_patch_plan
    - copy_old_text_from_live_file
    - define_new_text
    - verify_old_text_occurs_exactly_once
    - verify_anchor_unique
    - halt_on_zero_or_multiple_matches
    - apply_deterministic_replacement
    - submit_resulting_complete_content_to_repository_if_tool_requires_full_content
    - fetch_back_written_file
    - inspect_commit_diff
    - verify_no_unrelated_hunks
    - run_meta_detective_compliance_gate
    - run_hygiene_clean_structural_check
    - emit_artifact_closure
```

The repository API may still store the result as a complete new blob. The safety improvement is that the submitted content is produced by a deterministic exact-match replacement process rather than by unconstrained full-file reconstruction.

## 8. PATCH_PLAN contract

```yaml
PATCH_PLAN:
  task_id: TASK-XX
  target_file: exact/repo/relative/path.md
  task_scope: one atomic scope sentence
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
  write_class: scaffold_update | appendix_update | file_update
  source_evidence:
    - exact source file path
  operations:
    - op_id: OP-01
      mode: search_replace | append_after_anchor | append_before_anchor | full_body_replace
      anchor: exact unique anchor copied from live file
      old_text: |
        exact text copied from live fetched file
      new_text: |
        intended replacement or insertion text
      expected_occurrences: 1
      why_authorized: task instruction plus source evidence
      forbidden_side_effects:
        - unrelated cleanup
        - silent rewrite
        - external claim promotion
        - scaffold mutation outside task
  validation_required:
    - preimage_check
    - diff_audit
    - fetch_back
    - meta_detective_compliance_gate
    - hygiene_clean_structural_check
```

### 8.1 PATCH_PLAN pass condition

A patch plan passes only when every operation has exact source authority, an exact target anchor, exact old text for existing-content replacement, and an expected occurrence count.

If a plan cannot identify exact old text or a unique anchor, it must return `HALT` or `CLARIFY`.

## 9. SEARCH_REPLACE_BLOCK contract

```yaml
SEARCH_REPLACE_BLOCK:
  target_file: exact/repo/relative/path.md
  live_file_sha_before: blob_sha_from_fetch_file
  old_text: |
    verbatim text copied from live file
  new_text: |
    replacement text
  expected_occurrences: 1
  preimage_source: fetched_live_file_sha
  line_ending_policy: preserve_existing
  whitespace_policy: exact_match_required
  on_zero_matches: HALT_patch_check_fail
  on_multiple_matches: HALT_patch_check_fail
  on_match_once: allow_apply
```

### 9.1 Search/replace scope boundary

A `SEARCH_REPLACE_BLOCK` is not a prose description. It is an executable or mechanically checkable operation. If `old_text` is reconstructed from memory or paraphrased, the block is invalid.

## 10. PREIMAGE_CHECK contract

```yaml
PREIMAGE_CHECK:
  task_id: TASK-XX
  target_file: exact/repo/relative/path.md
  live_file_sha: blob_sha_from_fetch_file
  operation_id: OP-01
  old_text_occurrences: 0 | 1 | multiple
  expected_occurrences: 1
  anchor_unique: true | false
  line_endings_preserved: true | false
  old_text_copied_from_live_file: true | false
  result: pass | halt
  halt_reason_if_any: no_match | multiple_matches | stale_file | ambiguous_anchor | line_ending_mismatch
```

### 10.1 PREIMAGE_CHECK hard stop

```yaml
preimage_hard_stop:
  if_old_text_occurrences_zero: HALT_patch_check_fail
  if_old_text_occurrences_multiple: HALT_patch_check_fail
  if_anchor_unique_false: HALT_patch_check_fail
  if_live_file_sha_changed_before_write: HALT_stale_file
```

## 11. DIFF_AUDIT contract

```yaml
DIFF_AUDIT:
  task_id: TASK-XX
  commit_sha_after: commit_sha
  target_file: exact/repo/relative/path.md
  changed_files:
    - exact/repo/relative/path.md
  allowed_hunks:
    - OP-01
    - OP-02
  unrelated_hunks_present: false
  existing_entries_preserved: true
  scaffold_files_untouched_except_target: true
  external_claims_not_promoted: true
  semantic_diff_matches_patch_plan: true
  result: pass | halt
```

### 11.1 Diff-audit interpretation rule

A localized Git diff means the old and new blobs differ locally. It is not proof of preimage-checked mutation unless the `PATCH_PLAN`, `SEARCH_REPLACE_BLOCK`, and `PREIMAGE_CHECK` are also present.

## 12. Meta Detective compliance gate

Meta Detective is the verifier, not the executor.

```yaml
META_DETECTIVE_COMPLIANCE_GATE:
  task_id: TASK-XX
  source_authority_checked: true | false
  candidate_vs_canon_checked: true | false
  boundary_drift_checked: true | false
  executor_not_self_approving: true | false
  evidence_before_approval: true | false
  no_external_claim_promotion: true | false
  changed_file_set_checked: true | false
  verdict: pass | revise | hold | needs_input | escalate
```

### 12.1 Meta Detective stop condition

If the executor claims a write mode that is not supported by evidence, Meta Detective must return `revise` or `hold`, not `pass`.

## 13. Hygiene Clean structural check

Hygiene Clean verifies file-structure and repository-health consequences.

```yaml
HYGIENE_CLEAN_STRUCTURAL_CHECK:
  task_id: TASK-XX
  pointer_integrity: pass | fail
  stale_state: pass | fail
  changed_file_set: pass | fail
  closure_safety: pass | fail
  structural_drift: pass | fail
  duplicate_id_check: pass | fail
  anchor_integrity: pass | fail
  result: pass | fail
```

### 13.1 Hygiene Clean routing

Hygiene Clean does not promote doctrine. It checks structural safety, stale pointers, duplicate IDs, changed-file set, and closure evidence.

## 14. Allowed full-body replacement cases

Full-body replacement is allowed only when explicitly authorized or lower-risk than patching.

| Case | Allowed? | Required controls |
|---|---:|---|
| New file creation | Yes | Target path absent or create authority explicit; fetch-back after write. |
| Explicit full-body replacement task | Yes | Task payload says full-body replacement and source authority supersedes old content. |
| Generated file where whole content is the artifact | Yes | Generated-output contract and validation. |
| Very small file where full content can be manually verified | Conditional | Human or Meta Detective review of entire file. |
| Emergency recovery | Conditional | Operator confirmation, diff review, and rollback plan. |

Even when full-body replacement is allowed, Git diff and fetch-back validation remain mandatory.

## 15. Forbidden full-body replacement cases

Full-body replacement is forbidden by default for critical doctrine surfaces unless explicitly authorized.

| Case | Reason |
|---|---|
| Existing scaffold file with accepted doctrine | Existing content must not be reconstructed probabilistically. |
| Long file or many accepted entries | Omission and normalization risk is high. |
| Unclear anchor | AI may insert or replace the wrong section. |
| Multiple similar anchors | Exact replacement target is ambiguous. |
| Broad cleanup instruction | Encourages unrelated edits. |
| Missing verifier | Self-approval is unsafe. |
| Missing preimage check | Non-drift is only post-hoc, not pre-write guaranteed. |
| External/runtime claim insertion | Risks unverified doctrine contamination. |

## 16. Operator execution flow

```yaml
operator_execution_flow:
  phase_1_prepare:
    - open execution chat with one atomic task packet
    - include target file and exact source refs
    - state whether task is create_file, scaffold_update, or appendix_update
  phase_2_gate:
    - executor returns or internally verifies GATE_CHECK
    - if ambiguous, executor returns CLARIFY
    - if unsafe, executor returns HALT
  phase_3_read:
    - fetch live target file if it exists
    - record blob SHA for existing files
    - fetch source evidence
  phase_4_patch_plan:
    - create PATCH_PLAN
    - include each operation and why it is authorized
    - for existing content, copy old_text from live file
  phase_5_preimage:
    - count old_text occurrences
    - verify anchor uniqueness
    - halt on zero, multiple, or stale SHA
  phase_6_apply:
    - apply deterministic replacement or authorized full-body creation
    - if GitHub API requires complete content, submit tool-generated complete result, not AI-reconstructed freehand content
  phase_7_verify:
    - fetch back written file
    - inspect commit diff
    - run DIFF_AUDIT
    - run Meta Detective compliance gate
    - run Hygiene Clean structural check
  phase_8_close:
    - emit ARTIFACT_CLOSURE with write mode, preimage result, diff audit, and next task
```

## 17. Future integration map

This appendix is the evidence layer for later updates. It does not authorize immediate scaffold mutation.

| Future task | Target | Update type | Required content | Boundary |
|---|---|---|---|---|
| TASK-14 | `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | appendix_update | Add explicit mechanical GitHub write versus semantic diff and preimage-check guardrail. | Do not update scaffold. |
| TASK-15 | `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` | appendix_update | Add `PATCH_PLAN`, `PREIMAGE_CHECK`, and `DIFF_AUDIT` as required contracts for `file_update` and `scaffold_update`. | Preserve existing execution contracts. |
| TASK-16 | `TEMPLATES.md` | scaffold_update | Add compact preimage-checked patch-plan template pointer. | No appendix-depth schema dump. |
| TASK-17 | `MISTAKES.md` | scaffold_update | Add failure pattern for mistaking localized Git diff for pre-write bounded mutation proof. | Preserve existing mistake entries. |
| TASK-18 | `BEST_PRACTICES.md` | scaffold_update | Add compact best practice requiring preimage-checked patching for accepted scaffold mutation unless full-body replacement is explicitly authorized. | No runtime/platform claims. |
| TASK-19 | `LEARNING_QUEUE.md` | learning_queue_update | Add candidate-only item for executable tooling tests and owner validation if unresolved. | Candidate-only. |

## 18. TASK-13 closure scope record

```yaml
task_scope_record:
  task_id: TASK-13
  task_type: appendix_create
  scope: Create an appendix defining the preimage-checked scaffold mutation process and the GitHub full-file replacement versus localized diff distinction.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md
  output_format: markdown_file
  scaffold_mutation: none
  external_claim_promotion: none
  search_replace_used_in_TASK_07_to_TASK_11_claimed: false
```
