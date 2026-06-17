# 10. Improved future process

## Gold-standard workflow

```
PATCH_PLAN:  task_id: TASK-XX  target_file: <exact repo-relative path>  task_scope: <one atomic scope sentence>  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/  source_evidence:    - <exact source file>  operations:    - op_id: OP-01      mode: search_replace | append_after_anchor | append_before_anchor | full_body_replace      anchor: <exact unique anchor>      old_text: |        <exact text copied from live fetched file>      new_text: |        <replacement text>      expected_occurrences: 1      why_authorized: <task instruction + source evidence>  forbidden:    - unrelated cleanup    - silent rewrite    - unverified claim promotion    - scaffold mutation outside task
```

## `SEARCH_REPLACE_BLOCK`

```
SEARCH_REPLACE_BLOCK:  target_file: <path>  old_text: <verbatim live-file text>  new_text: <replacement>  expected_occurrences: 1  preimage_source: fetched_live_file_sha  on_zero_matches: HALT_patch_check_fail  on_multiple_matches: HALT_patch_check_fail
```

## `PREIMAGE_CHECK`

```
PREIMAGE_CHECK:  live_file_sha: <sha from fetch_file>  old_text_occurrences: 1  anchor_unique: true  line_endings_preserved: true  result: pass | halt
```

## `DIFF_AUDIT`

```
DIFF_AUDIT:  changed_files:    - <target_file only>  allowed_hunks:    - OP-01    - OP-02  unrelated_hunks_present: false  existing_entries_preserved: true  external_claims_not_promoted: true
```

## `META_DETECTIVE_COMPLIANCE_GATE`

```
META_DETECTIVE_COMPLIANCE_GATE:  source_authority_checked: true  candidate_vs_canon_checked: true  boundary_drift_checked: true  executor_not_self_approving: true  verdict: pass | revise | hold | needs_input | escalate
```

## `HYGIENE_CLEAN_STRUCTURAL_CHECK`

```
HYGIENE_CLEAN_STRUCTURAL_CHECK:  pointer_integrity: pass | fail  stale_state: pass | fail  changed_file_set: pass | fail  closure_safety: pass | fail  structural_drift: pass | fail
```

## `ARTIFACT_CLOSURE`

```
ARTIFACT_CLOSURE:  task_id: TASK-XX  write_mode: search_replace_preimage_checked  target_file: <path>  live_file_sha_before:  commit_sha_after:  fetch_back: pass  diff_audit: pass  meta_detective_gate: pass  hygiene_structural_check: pass  next_task:
```

## When full-file replacement is allowed

Allowed only for:

- new file creation;
- explicitly authorized full-body replacement;
- generated files where the entire file is the intended artifact;
- very small files where full content can be manually verified;
- emergency recovery with diff review and human approval.

## When full-file replacement is forbidden

Forbidden by default for:

- existing scaffold files with accepted doctrine;
- long files;
- files with many accepted entries;
- unclear or repeated anchors;
- broad rewrite instructions;
- missing verifier;
- missing preimage check.

---

# 11. Recommended canonical process update

Do **not** patch now. Recommended future updates:

|File|Recommended update|
|---|---|
|`APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`|Add explicit “mechanical GitHub update-file writes are complete replacement content; require preimage-checked patch mode for critical scaffold updates.”|
|`APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`|Add `PATCH_PLAN`, `PREIMAGE_CHECK`, and `DIFF_AUDIT` as required for `file_update` / `scaffold_update` tasks.|
|`TEMPLATES.md`|Add compact `PATCH_PLAN` template only after appendix update and validation.|
|`MISTAKES.md`|Add mistake pattern: “semantic-local diff produced from full-file reconstruction without preimage check can still drift.”|
|`BEST_PRACTICES.md`|Add best practice: “For accepted scaffold mutation, prefer preimage-checked search/replace over full replacement content unless explicitly authorized.”|
|`LEARNING_QUEUE.md`|Add candidate entry for formalizing the preimage-checked scaffold mutation workflow and assigning Hygiene/Meta Detective review.|

---

# 12. Final verdict packet

```
meta_detective_verdict:  artifact_reviewed: constant-frame-controlled KB integration  verdict: revise  confidence: VERIFIED  evidence_checked:    - meta_detective/ESSENCE.md    - meta_detective/BEST_PRACTICES.md    - meta_detective/TEMPLATES.md    - PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md    - APPENDIX_KB_CONSTANT_FRAME_PROCESS_CLOSE_REPORT.md    - TASK-00 through TASK-12 commits    - scaffold diffs for TEMPLATES.md, MISTAKES.md, BEST_PRACTICES.md, ESSENCE.md, LEARNING_QUEUE.md  main_finding: >    The process followed its declared macro-governance: appendices before scaffold,    compact scaffold updates, ESSENCE last, learning queue candidate-only,    and external claims not promoted.  main_risk: >    Scaffold updates appear to have used GitHub complete-file replacement mechanics    rather than a proven atomic preimage-checked search/replace operation.    The final diffs were localized, but non-drift was validated after the write,    not guaranteed before the write.  process_truth: >    Mechanically likely old file blob -> new file blob through GitHub contents/update-style write;    semantically the commits show localized diffs and no visible unrelated drift.  required_correction: >    Add a future required PATCH_PLAN / SEARCH_REPLACE_BLOCK / PREIMAGE_CHECK /    DIFF_AUDIT gate for critical scaffold updates.  recommended_owner: special_ops__prompts_workflows  recommended_validator: meta_detective + special_ops__hygiene_clean  may_process_be_reused: only_with_changes  required_future_guardrail: >    Existing scaffold files with accepted doctrine must use explicit old_text/new_text    preimage-checked patch operations or receive explicit full-body replacement authorization    before mutation.
```