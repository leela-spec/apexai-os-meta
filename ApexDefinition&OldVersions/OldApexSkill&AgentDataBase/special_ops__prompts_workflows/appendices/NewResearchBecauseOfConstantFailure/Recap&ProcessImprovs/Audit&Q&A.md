I’ll run this as a read-only audit. I’ll fetch the Meta Detective doctrine first, then the process artifacts and commits, and I’ll distinguish what GitHub evidence proves from what it does not prove.

The tool definition itself confirms `update_file` is complete replacement content through GitHub’s contents API, while `fetch_file` returns the current blob SHA. That will be part of the mechanism verdict.

Received app response

I have the Meta Detective frame: it validates and challenges, requires evidence before approval, separates candidate/canon states, and must not patch while auditing. I’m now checking the process files and commit chain directly.

Received app response

Received app response

Thought for 1m 5s

# 1. Executive verdict

**Verdict:** `revise`

The completed process was **acceptable for this integration pass**, but it should **not be reused as-is for future critical scaffold mutation**.

**Why:** The repo evidence supports that the process followed its major declared controls: appendices before scaffold, compact scaffold updates, `ESSENCE.md` last, `LEARNING_QUEUE.md` candidate-only, and external/runtime claims not promoted. The closeout report records this sequence, and the commit chain supports it.

**Main correction:** future scaffold updates should not rely on “construct full updated file content → GitHub update file → inspect diff afterward” as the primary safety mechanism. For critical scaffold files, require explicit `PATCH_PLAN` / `SEARCH_REPLACE_BLOCK` / preimage checks before mutation.

---

# 2. Evidence basis

## Meta Detective doctrine inspected

Meta Detective’s own boundary says it validates/challenges, does not execute fixes, does not patch, requires evidence before approval, separates candidate/canon states, and returns verdicts with evidence gaps and owner routes.

Relevant Meta Detective practices inspected:

- Source authority before verification.
- No evidence, no approval.
- Validator/executor separation.
- Stop conditions.
- Source/candidate/canon separation.
- Verdict packet discipline.

Relevant Meta Detective templates inspected:

- Source/evidence verification checklist.
- Validation verdict packet.
- Boundary/authority drift check.
- Risk/failure-mode red-team packet.
- Detective → Hygiene handoff.
- Promotion-risk check.

## Process files inspected

- `PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md`
- `APPENDIX_KB_CONSTANT_FRAME_PROCESS_CLOSE_REPORT.md`

## Commits inspected

- TASK-00: `02e0d52f7878a4708c85aa300ab029dcad660b51`
- TASK-01: `ec6f3be90f04771fcb86ca65a262e4547533c2de`
- TASK-02: `4b51c6ee57d57da6761b4f6422ac9000becd524c`
- TASK-03: `e9abba2927a4b3513f7f45c768bf47c9c20d30ac`
- TASK-04: `434f57c35d29f202cad7c4324e2f82f569d998dd`
- TASK-05: `82fa0e41109e94d028a4ff0c6fae11e8185e0a45`
- TASK-06: `05b12b4eadd0c28d9069f6dc227f8d516fe37928`
- TASK-07: `6dfac0c05b9cb3581a3924dfb02a3d5804e4c8d4`
- TASK-08: `a3f2eafff1d5aeca94338c38b9e1133d32f3e167`
- TASK-09: `f622e30835e066d539586112467f803dd7b9ba8d`
- TASK-10: `483ddd932e21259507941cf25b9bbddb2a43f935`
- TASK-11: `b5b79a94b8dea22d098052515c642dd986170ba6`
- TASK-12: `fd470ad6a03004b5594c75741c73e31b994b0dc6`

---

# 3. Process reconstruction

## Step-by-step reconstruction

1. **Controller process established.**  
    `PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md` was created as the controlling process. It declared repo, target root, source root, immutable locks, task queue, promotion gates, drift detector, file-output contract, fetch-back validation, and completion condition.
2. **Operator/controller split used.**  
    The operator opened task-specific execution chats and returned `ARTIFACT_CLOSURE` blocks to the controller. The promptflow itself defines task payloads, gate checks, closure proof, and state updates as process primitives.
3. **Appendices created first.**  
    TASK-01 through TASK-06 created appendix files before any scaffold mutation. This is confirmed by the commit sequence and by the closeout report’s artifact ledger.
4. **Scaffold updated second.**  
    TASK-07 through TASK-10 updated `TEMPLATES.md`, `MISTAKES.md`, `BEST_PRACTICES.md`, and `ESSENCE.md`. The closeout report records this as scaffold compact promotion after appendix support.
5. **`ESSENCE.md` updated last among scaffold files.**  
    TASK-10 added one compact bullet and one appendix pointer. The commit diff confirms only those two localized additions.
6. **Unresolved material routed to `LEARNING_QUEUE.md`.**  
    TASK-11 added `PW-LQ-005` through `PW-LQ-011`, all `candidate` or `needs_validation`.
7. **Closeout report created.**  
    TASK-12 created `APPENDIX_KB_CONSTANT_FRAME_PROCESS_CLOSE_REPORT.md`, documenting artifact ledger, promotion order, unresolved risks, and final operator handoff.

---

# 4. File-write mechanism truth check

## What is proven

The commits prove that:

- Each task changed only the expected file or created only the expected file.
- New appendices were created as whole new files.
- Existing scaffold files were changed through localized Git diffs.
- `TEMPLATES.md`, `MISTAKES.md`, `BEST_PRACTICES.md`, `ESSENCE.md`, and `LEARNING_QUEUE.md` were not shown as wholesale delete/re-add diffs.
- TASK-07 through TASK-11 diffs are localized hunks or appended blocks.

## What is not proven

The repo evidence does **not** prove that a true atomic search/replace operation was used.

There is no evidence of:

- a committed `.patch` file,
- a committed `v2` file,
- a standalone patch artifact,
- `git apply`,
- exact `old_text` / `new_text` preimage verification,
- a search/replace dry-run log,
- a search/replace tool output.

## Actual likely mechanism

The available GitHub connector exposes an update-file style operation that takes complete replacement file content and the current blob SHA. Therefore the safest description is:

```
fetch current file→ construct updated complete file content→ submit complete replacement content to GitHub for the same path→ GitHub creates a new blob and commit→ Git diff shows semantic delta→ fetch back / inspect diff
```

## Critical distinction

|Level|What happened|
|---|---|
|**Mechanical/API level**|Existing file blob was likely replaced by a new complete file blob at the same path.|
|**Semantic/Git diff level**|The actual content differences were localized, bounded, and mostly append-only.|

This distinction is central. The process was **not safe by construction** in the way an exact preimage search/replace would be. It was made safe by **post-write diff/fetch-back validation**.

---

# 5. Artifact ledger

|Task|File|Created / Updated|Commit|Diff shape|Scope match|Risk note|
|---|---|---|---|---|---|---|
|TASK-00|`PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md`|Created|`02e0d52...`|Full new file|Pass|New file creation is appropriate for full-body content.|
|TASK-01|`APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`|Created|`ec6f3be...`|Full new file|Pass|Appendix-only; no scaffold mutation.|
|TASK-02|`APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`|Created|`4b51c6e...`|Full new file|Pass|Source notes explicitly mark missing/rejected source risk.|
|TASK-03|`APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`|Created|`e9abba...`|Full new file|Pass|Strong process value; ironically shows current process still lacked explicit preimage patch artifact.|
|TASK-04|`APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`|Created|`434f57...`|Full new file|Pass|Regression evidence created before mistake promotion.|
|TASK-05|`APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`|Created|`82fa0e...`|Full new file|Pass|Keeps generated templates evidence-only.|
|TASK-06|`APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`|Created|`05b12b...`|Full new file|Pass|External claims explicitly not verified/promoted.|
|TASK-07|`TEMPLATES.md`|Updated|`6dfac0...`|Localized edit + appended entries/pointers|Pass|Existing `PW-TPL-007` intentionally extended; no whole-file diff.|
|TASK-08|`MISTAKES.md`|Updated|`a3f2ea...`|Evidence-ref insertion + appended entries/pointers|Pass|Existing `PW-MK-004` only got evidence refs.|
|TASK-09|`BEST_PRACTICES.md`|Updated|`f622e3...`|Appended entries/pointers|Pass|Existing `PW-BP-001` through `PW-BP-008` not rewritten in diff.|
|TASK-10|`ESSENCE.md`|Updated|`483ddd...`|Two localized insertions|Pass|Essence stayed compressed.|
|TASK-11|`LEARNING_QUEUE.md`|Updated|`b5b79a...`|Appended candidate entries|Pass|Candidate-only statuses preserved.|
|TASK-12|`APPENDIX_KB_CONSTANT_FRAME_PROCESS_CLOSE_REPORT.md`|Created|`fd470a...`|Full new file|Pass|Closeout only; no scaffold mutation.|

---

# 6. Guardrail compliance audit

|Guardrail|Declared rule|Evidence|Verdict|Note|
|---|---|---|---|---|
|One task per call|Promptflow requires atomic task payloads and one artifact or closed patch set per task.|Commit chain shows one file per task.|Pass|No commit shows multi-file mutation for a task.|
|Target-root lock|Writes must remain under `special_ops__prompts_workflows/`.|All inspected commits target that root.|Pass|No cross-root write found.|
|Appendices before scaffold|TASK-01 through TASK-06 must precede scaffold updates.|Commit sequence and closeout report confirm.|Pass|Strongly followed.|
|Scaffold compactness|Scaffold receives compact entries; appendices hold depth.|TASK-07 to TASK-10 diffs are localized.|Pass|No appendix-depth dumps in `ESSENCE.md`; `TEMPLATES.md` did add sizeable templates but scoped.|
|`ESSENCE.md` last|Essence update after templates, mistakes, best practices.|TASK-10 follows TASK-07/08/09.|Pass|Confirmed.|
|Learning queue candidate-only|`LEARNING_QUEUE.md` remains candidate-only.|TASK-11 adds `candidate` / `needs_validation`.|Pass|No accepted doctrine inserted there.|
|External claims not promoted|External claims must remain future research unless verified.|TASK-06 explicitly says it does not verify external claims; it inventories/routes them.|Pass|Strongly followed.|
|Fetch-back required|After writes, written file must be fetched back.|Closeout records this as pass.|Partial|Fetch-back closures were reported; for this audit I independently fetched several files/commits, but not every closure log exists as separate committed artifact.|
|No scaffold mutation during appendix tasks|Appendix creation cannot mutate scaffold.|TASK-01 through TASK-06 commits are new appendix files only.|Pass|Strong evidence.|
|No cross-repo target|Repo lock says `leela-spec/MasterOfArts` only.|All commits are in `leela-spec/MasterOfArts`.|Pass|Confirmed by commit metadata.|
|Patch preimage validation|Patch failure should HALT.|No explicit old_text/new_text preimage logs found.|Partial / revise|The final diffs passed, but pre-write proof is missing.|

---

# 7. Drift audit

## `TEMPLATES.md`

|Question|Finding|
|---|---|
|Existing text altered?|Yes: `PW-TPL-007` was altered.|
|Authorized?|Yes. TASK-07 explicitly allowed narrow update to `PW-TPL-007`; commit shows it expanded edit modes and evidence refs.|
|Exact diff hunks|Expanded `use_when`; expanded `recommended_mode`; added `search_replace`; added `no_patch_manual_review`; expanded validation-failure sentence; added `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`; added `PW-TPL-009`, `PW-TPL-010`, and appendix pointers.|
|Any unrelated drift?|None visible in commit diff.|
|Confidence|`VERIFIED` for diff shape; `PROBABLE` for underlying write mechanism.|

## `MISTAKES.md`

|Question|Finding|
|---|---|
|Existing text altered?|Yes, but only `PW-MK-004` evidence refs were added.|
|Authorized?|Yes; task allowed narrow evidence-ref update.|
|Exact diff hunks|Two evidence refs added to `PW-MK-004`; `PW-MK-009` through `PW-MK-011` appended; new appendix pointers appended.|
|Any unrelated drift?|None visible in commit diff.|
|Confidence|`VERIFIED`.|

## `BEST_PRACTICES.md`

|Question|Finding|
|---|---|
|Existing text altered?|No existing practice body appears altered in the diff.|
|Authorized?|Yes; new entries were requested.|
|Exact diff hunks|`PW-BP-009` through `PW-BP-011` appended; new appendix pointers appended.|
|Any unrelated drift?|None visible in commit diff.|
|Confidence|`VERIFIED`.|

## `ESSENCE.md`

|Question|Finding|
|---|---|
|Existing text altered?|No existing bullet changed; one bullet and one pointer added.|
|Authorized?|Yes; TASK-10 requested exactly this.|
|Exact diff hunks|Added `Constant frame control` bullet and `Constant frame control` appendix pointer.|
|Any unrelated drift?|None visible.|
|Confidence|`VERIFIED`.|

## `LEARNING_QUEUE.md`

|Question|Finding|
|---|---|
|Existing text altered?|No existing entries appear altered in the diff.|
|Authorized?|Yes; TASK-11 requested candidate-only entries.|
|Exact diff hunks|Added `PW-LQ-005` through `PW-LQ-011`; all are `candidate` or `needs_validation`.|
|Any unrelated drift?|None visible.|
|Confidence|`VERIFIED`.|

---

# 8. Why the process worked this time

The process worked because several independent safety factors overlapped:

1. **Small, single-file task packets.**  
    The promptflow required atomic tasks, exact targets, and one file or closed patch set at a time.
2. **Appendices first.**  
    The deep material was created before scaffold mutation, reducing pressure to dump large content into scaffold files.
3. **Clear scaffold anchors.**  
    Updates were naturally appendable after existing IDs: `PW-TPL-008`, `PW-MK-008`, `PW-BP-008`, core doctrine bullets, and learning queue entries.
4. **Existing-entry preservation instructions.**  
    The task prompts explicitly told executors to preserve existing entries and avoid broad rewrites.
5. **Diffs were localized.**  
    The actual Git diffs show localized changes, not whole-file delete/re-add patterns.
6. **External claims were quarantined.**  
    TASK-06 and TASK-11 explicitly kept model/API/platform claims in verification/future-research lanes.
7. **Closeout captured sequence and risks.**  
    TASK-12 documented the artifact ledger, promotion order, and remaining risks.

---

# 9. Where the process is fragile

The main fragility is that the write path appears to rely on **complete replacement content submitted to GitHub**, with safety enforced mostly by **after-the-fact diff inspection**.

That breaks when:

- target files are long enough that the executor cannot reliably hold unchanged content;
- target files have repeated anchors;
- instructions say “improve,” “clean up,” or “harmonize” without exact old/new text;
- no exact preimage is checked before mutation;
- no search/replace dry-run exists;
- the executor constructs a file from memory instead of fetched content;
- line endings or hidden formatting are normalized silently;
- the diff is not inspected;
- closure is accepted from self-report;
- scaffold is updated before appendices exist;
- external/runtime claims leak into accepted doctrine;
- no independent verifier or Meta Detective pass exists.

In short:

```
Current process safety = read + constrained task + commit diff + fetch-back.Gold-standard safety = preimage-checked patch + constrained task + commit diff + fetch-back + independent audit.
```

---

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

Improved future process.md

File

Questions: 1) Maybe I just understood a very important detail. It is not you that does the update file as a complete replacement. It is GitHub who does that. But GitHub is deterministic, so if it does a whole file replacement, since it is deterministic and not AI probabilistic, it can do the job reliably. Is that an important understanding that we can save, like, at least for me? 2) I do not fuly understand that paragraph: "Main correction: future scaffold updates should not rely on “construct full updated file content → GitHub update file → inspect diff afterward” as the primary safety mechanism. For critical scaffold files, require explicit PATCH_PLAN / SEARCH_REPLACE_BLOCK / preimage checks before mutation." I thought we were already doing pathc_plan and searh_replace_block? tell me what is different to what we did and explain that process for every step (what is the execution called, who is doing it, is it deterministic or probabilistic) 3) I dont understand: "Existing scaffold files were changed +through localized Git diffs+. TEMPLATES.md, MISTAKES.md, BEST_PRACTICES.md, ESSENCE.md, and LEARNING_QUEUE.md were not shown as wholesale delete/re-add diffs. Other chats already noticed that this step is not possible through the api connector (it only has read, write capabilities). what is meant by that here? 4) what is a blob and sha, explain how and why git uses them in their processes 5) how do we save the new process now? I want to first save it? create a process / prompt that creates a resileint, on target, non drift new process and save it to the repo. what is getting updated, is sth completly new? create a q&a with options and recommendations if this is not clear

I’ll answer the mechanics first, then give you a concrete save-to-repo path. The key distinction is deterministic Git storage versus probabilistic AI construction of the replacement content.

Thought for 12s

# 1) Yes — that is an important understanding

Your understanding is basically correct:

> **GitHub is not the probabilistic part. The AI is.**

More precise:

|Stage|Actor|Deterministic?|Risk|
|---|---|---|---|
|Read current file|GitHub/API connector|Mostly deterministic|Low|
|Decide what changed content should be|AI/executor|Probabilistic|High|
|Submit updated content|AI/tool call|Mixed|Medium|
|Replace old blob with submitted new blob|GitHub|Deterministic|Low|
|Compute Git diff|Git|Deterministic|Low|
|Interpret whether diff is safe|AI/human verifier|Probabilistic unless rules are strict|Medium|

So the saved principle should be:

> **GitHub whole-file replacement is deterministic and reliable for storing exactly the submitted content; the danger is not GitHub replacing the file, but the AI constructing the replacement content incorrectly before GitHub receives it.**

That is worth codifying.

---

# 2) Difference between what we did and true `PATCH_PLAN` / `SEARCH_REPLACE_BLOCK`

You thought we were already doing this because the **process language** contained patch concepts. But the actual execution evidence does **not** prove that we used a strict preimage-checked patch artifact.

## What we did

```
1. AI reads current target file.2. AI decides what final updated file should look like.3. AI submits complete file content to GitHub update-file API.4. GitHub replaces old file blob with new file blob.5. Git computes localized diff.6. AI/operator checks diff/fetch-back and says pass/fail.
```

This is:

> **Full-content update with post-write diff validation.**

## What strict preimage-checked patching would do

```
1. AI reads current target file.2. AI copies exact old text from the live file.3. AI creates PATCH_PLAN.4. AI creates SEARCH_REPLACE_BLOCK.5. Deterministic checker verifies old_text occurs exactly once.6. If zero or multiple matches: HALT.7. If exactly one match: deterministic replacement happens.8. GitHub stores resulting full file blob.9. Git diff is inspected after commit.
```

This is:

> **Bounded replacement with pre-write proof and post-write validation.**

## Step-by-step comparison

|Step|What happened before|Gold-standard version|Who does it|Deterministic?|
|---|---|---|---|---|
|1. Fetch file|File was fetched/read|Same|GitHub/API|Yes|
|2. Determine change|AI decided final content|AI drafts explicit patch plan|AI|No|
|3. Identify old content|Usually implicit by anchor/diff|Exact `old_text` copied from live file|AI, then checker|AI part no; checker yes|
|4. Verify old content|Not externally proven|Count exact occurrences before writing|Script/tool/Git checker|Yes|
|5. Apply edit|GitHub received complete replacement content|Deterministic replace only after exact match|Tool/GitHub|Yes|
|6. Store file|GitHub stored new blob|Same|GitHub|Yes|
|7. Inspect diff|Yes|Yes|Git/GitHub + verifier|Git yes; verifier mixed|
|8. Close task|Closure block|Closure block plus preimage proof|AI/operator|Mixed|

The uploaded improvement note captures the missing stricter pieces: `PATCH_PLAN`, `SEARCH_REPLACE_BLOCK`, `PREIMAGE_CHECK`, `DIFF_AUDIT`, `META_DETECTIVE_COMPLIANCE_GATE`, `HYGIENE_CLEAN_STRUCTURAL_CHECK`, and `ARTIFACT_CLOSURE`.

---

# 3) What “localized Git diffs” means

This sentence does **not** mean the API connector literally edited only those lines.

It means:

> After GitHub stored the new full file blob, Git compared old blob vs new blob and showed that only localized sections were different.

So:

```
Mechanical write:old complete file blob -> new complete file blobSemantic diff:Git shows only a few changed hunks
```

A connector with only read/write can still produce a localized Git diff because Git computes the diff **after** the write.

Example:

```
Old file:ABCNew file submitted:AB changedCGit stores the whole new file, but the diff shows only:- B+ B changed
```

So when I said “localized Git diffs,” I meant:

> The resulting commit diff did not show wholesale file replacement, mass deletion, mass re-addition, or unrelated text drift.

It does **not** prove that the connector performed an in-place line patch.

---

# 4) Blob and SHA

## Blob

In Git, a **blob** is the stored content of a file.

Git does not primarily think:

```
file path = text file
```

It thinks more like:

```
blob = exact bytes of file contenttree = directory structure pointing file paths to blobscommit = snapshot pointing to a tree plus metadata
```

So if `ESSENCE.md` changes by one line, Git stores a new blob for the new exact content of `ESSENCE.md`.

## SHA

A **SHA** is a cryptographic hash ID for Git objects.

For a file blob:

```
blob content -> hash function -> SHA
```

If the file content changes by even one character, the blob SHA changes.

## Why Git uses this

Git uses blobs and SHAs because they make version control precise:

|Concept|Purpose|
|---|---|
|Blob|Stores exact file content|
|SHA|Identifies exact content|
|Tree|Maps filenames/paths to blob SHAs|
|Commit|Records a snapshot of the repo tree|
|Diff|Compares old blob content vs new blob content|

This is why Git is strong for audit:

> If the old blob SHA and new blob SHA are known, Git can deterministically compute what changed.

---

# 5) How to save the new process now

## Recommendation

Do **not** first update all scaffold files.

First create **one new appendix** that formally documents the safer process:

```
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md
```

Why this first:

- It is a **new file**, so full-file creation is safe.
- It does not risk mutating accepted scaffold doctrine yet.
- It captures the learning in a durable KB artifact.
- Later tasks can update `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`, `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`, `TEMPLATES.md`, `MISTAKES.md`, `BEST_PRACTICES.md`, and `LEARNING_QUEUE.md`.

This follows the same appendix-before-scaffold pattern.

---

# Q&A: options for saving

|Option|What gets changed|Safety|Recommendation|
|---|---|---|---|
|A|Create one new appendix only|Highest|**Do first**|
|B|Update `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` directly|Medium|Do after new appendix exists|
|C|Update `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` directly|Medium|Do after new appendix exists|
|D|Update scaffold files immediately|Lower|Avoid for now|
|E|Update `LEARNING_QUEUE.md` only|Medium-high|Good if you want to defer implementation|
|F|Create a full new controlling promptflow|Medium|Useful if this becomes a larger process|

**Best path:** A → B → C → scaffold updates.

---

# Proposed task sequence

## TASK-13

Create:

```
appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md
```

Purpose:

> Document the distinction between deterministic GitHub full-file storage and probabilistic AI replacement-content construction, then define the required preimage-checked mutation process for critical scaffold updates.

## TASK-14

Update:

```
appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
```

Add:

> GitHub contents/update-file writes store complete replacement content; for critical scaffold files, use preimage-checked search/replace or explicit full-body authorization.

## TASK-15

Update:

```
appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
```

Add:

- `PATCH_PLAN`
- `SEARCH_REPLACE_BLOCK`
- `PREIMAGE_CHECK`
- `DIFF_AUDIT`
- `MECHANICAL_WRITE_TRUTH_CHECK`

## TASK-16

Update:

```
TEMPLATES.md
```

Add compact template pointer only.

## TASK-17

Update:

```
MISTAKES.md
```

Add failure pattern:

> mistaking localized Git diff for proof of pre-write bounded mutation.

## TASK-18

Update:

```
BEST_PRACTICES.md
```

Add practice:

> for accepted scaffold mutation, require preimage-checked patching unless full-body replacement is explicitly authorized.

## TASK-19

Update:

```
LEARNING_QUEUE.md
```

Only if unresolved questions remain.

---

# Copy-paste prompt to save the process as TASK-13

Use this in a new execution chat:

```
You are executing one atomic repo task for the OpenClaw Special Ops Prompts Workflows KB.ROLE:You are the executor for TASK-13 under the controlling promptflow:OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.mdFRAME_BLOCK:  frame_id: special_ops_constant_frame_controlled_kb_integration  active_task_id: TASK-13  active_agent_role: executor  working_repo: leela-spec/MasterOfArts  target_repo: leela-spec/MasterOfArts  target_branch: main  target_agent: special_ops__prompts_workflows  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/  source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/  immutable_locks:    - no_cross_repo_targeting    - no_apex_write_or_runtime_target    - one_atomic_task_per_call    - no_implicit_state_inference    - appendices_before_scaffold    - scaffold_compact    - essence_last    - learning_queue_candidate_only  completed_tasks:    - TASK-00 through TASK-12 completed and verified  active_constraints:    - output_must_match_task_type    - scope_must_be_repeated_in_gate_and_closure    - source_claims_must_have_route_status    - external_claims_future_research_only_until_verified    - fetch_back_every_written_file    - create_only_target_appendix    - do_not_update_scaffold_files    - do_not_promote_external_claims    - distinguish_mechanical_write_from_semantic_diff    - distinguish_deterministic_git_storage_from_probabilistic_ai_content_constructionTASK_PAYLOAD:  id: TASK-13  type: appendix_create  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md  scope: Create an appendix defining the preimage-checked scaffold mutation process and the GitHub full-file replacement versus localized diff distinction.  output_format: markdown_file  input_refs:    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FRAME_PROCESS_CLOSE_REPORT.md    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/LEARNING_QUEUE.md  constraints:    - create the target appendix only    - do not update TEMPLATES.md, MISTAKES.md, BEST_PRACTICES.md, ESSENCE.md, or LEARNING_QUEUE.md    - preserve existing scaffold files untouched    - define GitHub blob/full-file replacement mechanics as deterministic storage behavior    - define AI replacement-content construction as the probabilistic risk surface    - define why localized Git diffs prove localized semantic change but not preimage-checked mutation    - define PATCH_PLAN, SEARCH_REPLACE_BLOCK, PREIMAGE_CHECK, DIFF_AUDIT, META_DETECTIVE_COMPLIANCE_GATE, HYGIENE_CLEAN_STRUCTURAL_CHECK, and ARTIFACT_CLOSURE    - define when full-body replacement is allowed    - define when full-body replacement is forbidden    - include a future integration map for TASK-14 through TASK-19    - no external model/platform/runtime claims    - no schema dump into scaffold    - fetch back written file and verify changed-file setGATE_CHECK REQUIRED BEFORE EXECUTION:Return or internally verify:  task_id: TASK-13  task_type_understood: appendix_create  scope_understood: Create an appendix defining the preimage-checked scaffold mutation process and the GitHub full-file replacement versus localized diff distinction.  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md  ambiguity_detected: false  ready_to_execute: trueEXPECTED APPENDIX CONTENT:  Required sections:    1. Purpose    2. Core distinction: deterministic GitHub storage versus probabilistic AI construction    3. Git object model: blob, tree, commit, SHA, diff    4. Mechanical write versus semantic diff    5. Why the previous whole-file update worked    6. When whole-file update breaks    7. Required preimage-checked scaffold mutation process    8. PATCH_PLAN contract    9. SEARCH_REPLACE_BLOCK contract    10. PREIMAGE_CHECK contract    11. DIFF_AUDIT contract    12. Meta Detective compliance gate    13. Hygiene Clean structural check    14. Allowed full-body replacement cases    15. Forbidden full-body replacement cases    16. Operator execution flow    17. Future integration mapVALIDATION REQUIREMENTS:  - target appendix exists under the target KB root  - no files other than the target appendix changed  - scaffold files untouched  - distinction between GitHub deterministic write and AI probabilistic content construction is explicit  - no claim that search/replace was used in TASK-07 through TASK-11 unless evidence proves it  - no external/runtime/model/platform claim promoted  - future scaffold updates are routed as later tasks onlyFINAL RESPONSE FORMAT:Return only this YAML block plus short summary:ARTIFACT_CLOSURE:  task_id: TASK-13  output_type: file_write | halt | clarify  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md  commit_sha:  display_url:  scope_respected: yes | no  additions_beyond_scope: none | one-line explanation  source_refs_used:    - list exact files used  validation:    fetch_back: pass | fail    repo_root: pass | fail    target_root: pass | fail    only_target_appendix_changed: pass | fail    scaffold_files_untouched: pass | fail    deterministic_vs_probabilistic_distinction_present: pass | fail    mechanical_write_vs_semantic_diff_present: pass | fail    preimage_checked_process_present: pass | fail    no_unproven_search_replace_claim: pass | fail    external_claims_not_promoted: pass | fail  next_suggested_task: TASK-14 update APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md with preimage-checked scaffold mutation guardrail
```

---

# Practical recommendation

Do **TASK-13 first** as a new appendix. It saves the crucial understanding without risking existing scaffold drift.

Then decide whether to promote it into existing scaffold. The uploaded improvement plan already identifies the likely canonical targets: patch transport appendix, execution-control appendix, templates, mistakes, best practices, and learning queue.