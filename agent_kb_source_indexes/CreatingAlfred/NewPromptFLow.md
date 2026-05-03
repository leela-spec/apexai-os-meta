- meta_strategy KB
- meta_detective KB
- meta_strategy agent seed
- meta_detective agent seed

## 1. Repo orientation — current Alfred/Apex layout

I inspected the Apex AI repo `leela-spec/apexai-os-meta`.

**Confirmed root:** `managed/agent_kb/alfred/`

**Current Alfred KB has two overlapping layers:**

|Layer|Files|Meaning|
|---|---|---|
|**Canonical five-file KB scaffold**|`ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`|This is the repo-wide accepted KB convention. The repo index says every KB root derives this scaffold, and `LEARNING_QUEUE.md` is candidate-only, never runtime truth.|
|**Recovery/control extension files**|`AGENT_CARD.md`, `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md`, `ROLE_BOUNDARIES.md`, `ROUTING_CONTRACT.md`, `HANDOFF_SCHEMA.md`, `DOCTRINE.md`, `WORKFLOW_PLAYBOOK.md`, `README.md`|These were created by the recent Alfred recovery flow. The README marks them as repaired/created and says `LEELA_SURFACE_MAP.md` was intentionally skipped.|

**Important detective finding:** the recent prompt flow did create a serious recovery scaffold, but the next validation must check whether the **extension files are consistent with the canonical five-file scaffold**, not only whether the extension files look good.

---

## 2. Current source posture

The current `SOURCE_MANIFEST.md` says the previous manifest was flawed because it relied on existing Apex files, did not verify the Master Of Arts source phase properly, collapsed local/manual sources into `IDX-N4`, and failed to enumerate every local/manual source as `not_accessible`. The repaired manifest claims it uses the completed Pass A source bundle and preserves source gaps.

The current manifest also records:

|Source class|Status|
|---|---|
|Master Of Arts index|`fully_read`|
|5 repo-accessible Master Of Arts sources|`fully_read`|
|40 local/manual sources|`not_accessible`|
|Apex files|conventions only, not source substitutes|

The coverage audit repeats the same key doctrine boundary: stable Alfred identity/routing claims are validated, but detailed Leela product mechanics remain source-gap-dependent.

---

## 3. Initial control verdict

**Verdict:** the recovery flow appears procedurally repaired at the manifest/audit level, but not yet fully controlled.

**Why:** the repo now contains both:

1. **Older accepted scaffold files** that already include product-level Alfred claims, including Leela ladder, Rhythm repair, day-start sequencing, Algorithm/Stats/Sid references.

2. **Newer recovery files** that explicitly say detailed Leela mechanics remain source-gap-dependent.


That is the central validation risk.

### Primary suspected drift zones

|Zone|Risk|
|---|---|
|`ESSENCE.md`|May harden Leela surface mechanics as accepted doctrine before source extension.|
|`BEST_PRACTICES.md`|Contains accepted practices that reference `IDX-N4`; likely needs source-gap normalization.|
|`MISTAKES.md`|Some failure patterns cite inaccessible Night4/product sources; may be acceptable only if explicitly provisional.|
|`TEMPLATES.md`|Weekly alignment, day-start sequencing, and Rhythm repair templates may be too product-specific for accepted templates if source gaps remain.|
|`README.md`|Lists recovery extension files but does not foreground the canonical five-file scaffold, creating index mismatch.|
|`AGENT_CARD.md`|Strong useful summary, but likely contains product-surface details that must be checked against `COVERAGE_AUDIT.md`.|

---

## 4. Q&A round — understanding lock

|#|Question|Working answer|
|--:|---|---|
|1|**What is the mission?**|Validate the created Alfred KB files against the repo’s canonical KB rules, the recovered source manifest, and the coverage audit; then produce one-file-at-a-time correction prompts.|
|2|**What is the target repo?**|`leela-spec/apexai-os-meta`.|
|3|**What is the target folder?**|`managed/agent_kb/alfred/`.|
|4|**Should we write now?**|No. Current phase should be audit/Q&A/prompt-flow design only.|
|5|**What is the highest priority?**|Prevent source-gap hardening: no local/manual Night4 source should be treated as fully read unless directly read in this validation pass.|
|6|**What is the second priority?**|Reconcile the canonical five-file scaffold with the newer recovery extension files.|
|7|**What files must be checked first?**|`SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md`, `AGENT_KB_INDEX.md`, `AGENT_KB_LANES.md`, then Alfred files.|
|8|**What files are most likely to need patches?**|`README.md`, `ESSENCE.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, possibly `AGENT_CARD.md`.|
|9|**What should not happen?**|Do not collapse source gaps back into `IDX-N4`; do not make `LEELA_SURFACE_MAP.md` unless explicitly re-authorized; do not patch multiple files in one turn.|
|10|**What does “done correctly” mean?**|Every Alfred file has clear source posture, no hidden source substitution, no conflict with canonical scaffold, and no accepted doctrine derived from unread local/manual files.|
|11|**What do I not yet know?**|Whether you want the attached local/manual files in this project to now be treated as readable source-extension inputs. Several are present in `/mnt/data`, but the prior recovery flow intentionally excluded them to keep Pass A clean.|
|12|**My recommended answer to #11**|Yes, use them now — but only in a separate **Pass C: Manual Source Extension Audit**, not mixed into the already-completed Pass A/Pass B narrative.|

---

## 5. Proposed validation priorities

### Priority 0 — No writes

Establish a complete audit table first.

### Priority 1 — Control current source state

Check:

- `SOURCE_MANIFEST.md`

- `COVERAGE_AUDIT.md`

- `README.md`

- `AGENT_KB_INDEX.md`

- `AGENT_KB_LANES.md`

- `KB_STARTING_SOURCE_MAP.md`


Reason: these define what counts as source, canon, candidate, process contract, or governance. `AGENT_KB_LANES.md` says the per-agent KB root owns accepted doctrine/practices/mistakes/templates and keeps `LEARNING_QUEUE.md` candidate-only.

### Priority 2 — Check the canonical accepted files

Check:

1. `ESSENCE.md`

2. `BEST_PRACTICES.md`

3. `MISTAKES.md`

4. `TEMPLATES.md`

5. `LEARNING_QUEUE.md`


Reason: these are the accepted scaffold files. If they contain overhardened Leela mechanics, the KB is still partially flawed even if `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md` are repaired.

### Priority 3 — Check recovery extension files

Check:

1. `AGENT_CARD.md`

2. `ROLE_BOUNDARIES.md`

3. `ROUTING_CONTRACT.md`

4. `HANDOFF_SCHEMA.md`

5. `DOCTRINE.md`

6. `WORKFLOW_PLAYBOOK.md`

7. `README.md`


Reason: these should remain compatible with the accepted scaffold and should not duplicate process contracts that belong in `managed/processes/`.

### Priority 4 — Decide whether to run manual-source extension

Several of the previously missing local/manual sources are now attached in the project context. That means we can run a new pass that reads them directly and updates the source posture from `not_accessible` to `attached_read` or equivalent.

---

## 6. Prompt flow for the next iterations

### Phase A — Alfred KB Control Audit, no writes

```md
# Alfred KB Control Audit — No Writes

You are validating the already-created Alfred KB in Apex AI.

Repo:
- leela-spec/apexai-os-meta

Target folder:
- managed/agent_kb/alfred/

Rules:
- Do not write or patch anything.
- Fetch current files only.
- Build a validation matrix.
- Treat `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md` as current source-control surfaces, not doctrine by themselves.
- Treat `AGENT_KB_INDEX.md`, `AGENT_KB_LANES.md`, and `KB_STARTING_SOURCE_MAP.md` as repo convention controls.
- Detect conflicts between the canonical five-file scaffold and the newer Alfred recovery extension files.

Fetch and inspect these files first:

1. managed/agent_kb/AGENT_KB_INDEX.md
2. managed/knowledge/AGENT_KB_LANES.md
3. managed/knowledge/KB_STARTING_SOURCE_MAP.md
4. managed/agent_kb/alfred/SOURCE_MANIFEST.md
5. managed/agent_kb/alfred/COVERAGE_AUDIT.md
6. managed/agent_kb/alfred/README.md

Then fetch and inspect:

7. managed/agent_kb/alfred/ESSENCE.md
8. managed/agent_kb/alfred/BEST_PRACTICES.md
9. managed/agent_kb/alfred/MISTAKES.md
10. managed/agent_kb/alfred/TEMPLATES.md
11. managed/agent_kb/alfred/LEARNING_QUEUE.md
12. managed/agent_kb/alfred/AGENT_CARD.md
13. managed/agent_kb/alfred/ROLE_BOUNDARIES.md
14. managed/agent_kb/alfred/ROUTING_CONTRACT.md
15. managed/agent_kb/alfred/HANDOFF_SCHEMA.md
16. managed/agent_kb/alfred/DOCTRINE.md
17. managed/agent_kb/alfred/WORKFLOW_PLAYBOOK.md

Output exactly:

1. FILE_INVENTORY
   - path
   - exists
   - SHA
   - role
   - scaffold class: canonical / extension / governance / process-reference

2. VALIDATION_MATRIX
   - path
   - validated claims
   - provisional claims
   - source-gap claims
   - conflicts with SOURCE_MANIFEST/COVERAGE_AUDIT
   - conflicts with AGENT_KB_INDEX/AGENT_KB_LANES
   - recommended action: keep / patch / split / deprecate / needs source extension

3. DRIFT_FINDINGS
   - source-gap hardening
   - scaffold mismatch
   - stale next-file pointers
   - duplicate doctrine
   - process-contract leakage
   - candidate/canon leakage

4. PATCH_BACKLOG
   - one row per required correction
   - target file
   - severity
   - exact reason
   - patch strategy
   - source basis
   - must-not-do rules

5. NEXT_ITERATION_ORDER
   - one file per iteration
   - highest-risk first
   - no file writes in this audit phase

Stop after the audit.
```

---

### Phase B — Single-file patch iteration

```md
# Alfred KB Single-File Patch

Patch exactly one file.

Repo:
- leela-spec/apexai-os-meta

Target path:
- managed/agent_kb/alfred/[FILE].md

Inputs:
- Alfred KB Control Audit
- current SOURCE_MANIFEST.md
- current COVERAGE_AUDIT.md
- current AGENT_KB_INDEX.md
- current AGENT_KB_LANES.md
- current target file

Rules:
1. Fetch the current target file and SHA.
2. Classify the current defect:
   - source-gap hardening
   - scaffold mismatch
   - stale pointer
   - duplicate doctrine
   - process-contract leakage
   - candidate/canon leakage
   - missing source posture
3. Patch only this one file.
4. Do not create or modify any other file.
5. Preserve useful content where possible.
6. Mark source-gap-dependent content explicitly.
7. Do not cite local/manual files as read unless this exact phase has read them.
8. Fetch back after writing.
9. Verify the fetched content.
10. Report:
   - path
   - operation
   - commit SHA
   - fetched blob SHA
   - verification result
   - remaining risk
   - next recommended file
11. Stop.
```

---

### Phase C — Manual-source extension pass

Use only if you want the currently attached project files to repair the missing Night4/local/manual coverage.

```md
# Alfred Manual Source Extension Audit — Attached Files

Goal:
Read the attached local/manual files that were previously marked `not_accessible` in SOURCE_MANIFEST.md and determine which source gaps can now be upgraded.

Rules:
- Do not write to Apex.
- Do not mix this with old Pass A. This is a new Pass C.
- For every attached source, record exact read status.
- If a source listed in SOURCE_MANIFEST.md is still not attached, keep it `not_accessible`.
- Do not promote claims directly into doctrine.
- Produce a source-extension bundle only.

Output:

1. ATTACHED_SOURCE_INDEX
   - manifest source_id
   - filename
   - attached path
   - read status
   - doctrine area
   - notes

2. NEW_EXTRACTION_LEDGER
   - claim_id
   - claim
   - source_refs
   - confidence
   - affected existing Alfred file(s)
   - whether claim upgrades an existing source gap

3. SOURCE_GAP_DIFF
   - gap before
   - evidence now available
   - new status: validated / partially_validated / still_gap
   - target file affected

4. PATCH_PLAN
   - files requiring updates
   - one-file iteration order
   - exact claim IDs to use
   - claims still blocked

Stop after producing the extension bundle.
```

---

## 7. My recommended next step

Run **Phase A: Alfred KB Control Audit — No Writes**.

Likely first patch after that: `README.md`, because it should reconcile the canonical scaffold with the recovery extension files before doctrine-bearing files are changed.