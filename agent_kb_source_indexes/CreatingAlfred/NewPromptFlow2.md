## Executive answer

The optimal Alfred KB should **not** continue by simply redirecting/deleting support files yet.

Before collapse, the better move is to define the **intended extended-KB architecture**:

> **Canonical five-file KB = accepted operational knowledge.**
> **Extended KB layer = source/audit/appendix/index material only when it improves traceability, retrieval, or source-gap control without becoming parallel doctrine.**

The Apex system is explicit: every first-wave KB root derives the same five files — `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`; `LEARNING_QUEUE.md` is candidate-only and never runtime truth.

The deeper policy confirms the system has distinct lanes:

|Lane|Location|Role|
|---|---|---|
|**Compact activation seed**|`managed/agents/<agent_id>.md`|compact runtime activation and KB pointer|
|**Per-agent KB root**|`managed/agent_kb/<agent_id>/`|rich accepted agent doctrine, practices, mistakes, templates, candidate queue|
|**Shared KB governance**|`managed/knowledge/`|KB placement, promotion, source routing, references, overlap checks|
|**Process contracts**|`managed/processes/`|handoff/orchestration/workflow authority|

That lane model is explicitly defined in `AGENT_KB_LANES.md`.

So the Alfred extended KB should exist, but only as a **controlled appendix layer**, not as a second scaffold.

---

# A. Intended Apex KB system — distilled

## A1. What the system is trying to prevent

The Apex KB architecture is designed to prevent these failures:

|Failure|System protection|
|---|---|
|Source becomes canon by being cited|`KB_STARTING_SOURCE_MAP.md` says source material is evidence, not canon.|
|Learning queue becomes runtime truth|`AGENT_KB_LANES.md`, `AGENT_KB_INDEX.md`, and promotion docs all forbid this.|
|Agent-specific doctrine bloats shared governance|`AGENT_KB_LANES.md` says rich doctrine belongs in the per-agent KB root, not shared governance.|
|Process contracts get hidden inside KB files|`AGENT_KB_LANES.md` routes handoff/workflow contracts to `managed/processes/`.|
|Promotion happens by convenience|`PROMOTION_PROTOCOL.md` says promotion is packetized, explicit, reviewable, and auditable.|
|Cross-agent boundary drift|`OVERLAP_VALIDATION_MATRIX.md` requires validator checks for drift-prone boundaries.|

## A2. What “extended KB” should mean

An extended KB file is valid only if it is one of these:

|Extended type|Valid?|Meaning|
|---|--:|---|
|**Source/audit control**|yes|Records source status, coverage gaps, evidence posture.|
|**Appendix**|yes, conditionally|Large detail too bulky for canonical files, but subordinate to them.|
|**Index**|yes|Helps navigate canonical files and appendices.|
|**Migration redirect**|yes, temporarily|Preserves old links while preventing duplicate doctrine.|
|**Duplicate doctrine file**|no|Should be merged into the canonical five or redirected/deleted.|
|**Process contract clone**|no|Belongs in `managed/processes/`.|
|**Promotion shortcut**|no|Must use promotion protocol / ledger route.|

## A3. Current Alfred state after our work

The five canonical files are now consolidated:

|Canonical file|Current role|
|---|---|
|`ESSENCE.md`|identity, authority, boundaries|
|`BEST_PRACTICES.md`|operating method|
|`MISTAKES.md`|failure patterns|
|`TEMPLATES.md`|reusable forms|
|`LEARNING_QUEUE.md`|candidate-only learning|

The README now correctly classifies support files as absorbed duplicate, possible appendix, or source/audit control.

---

# B. Q&A decision model for Alfred extended KB

## B.1 Canonical vs extended

|#|Question|Options|My decision|Recommendation|
|--:|---|---|---|---|
|1|Should Alfred have more than the five canonical files?|A. No extra files. B. Yes, appendices. C. Yes, second scaffold.|**B**|Extra files are valid only as appendices/source controls/indexes, never as a second scaffold.|
|2|Should `AGENT_CARD.md` stay?|A. Keep. B. Redirect. C. Delete.|**B now, maybe C later**|Redirect first for compatibility. Delete only after no references remain.|
|3|Should `DOCTRINE.md` stay?|A. Keep. B. Redirect. C. Delete.|**B**|Doctrine now belongs in `ESSENCE.md`; redirect avoids duplicate authority.|
|4|Should `ROLE_BOUNDARIES.md` stay?|A. Keep appendix. B. Redirect. C. Delete.|**A or B after audit**|If detailed boundary tables still exceed `ESSENCE.md`, keep as appendix. Otherwise redirect.|
|5|Should `ROUTING_CONTRACT.md` stay?|A. Keep appendix. B. Redirect. C. Delete.|**A likely**|A route matrix can be useful as appendix, but canonical routing method stays in `BEST_PRACTICES.md`.|
|6|Should `HANDOFF_SCHEMA.md` stay?|A. Keep appendix. B. Redirect. C. Delete.|**B likely**|Reusable handoff forms now belong in `TEMPLATES.md`; process-level handoff authority belongs in `managed/processes/AGENT_HANDOFF_CONTRACTS.md`.|
|7|Should `WORKFLOW_PLAYBOOK.md` stay?|A. Keep appendix. B. Redirect. C. Delete.|**A likely, but slimmed**|A long playbook can be useful as an appendix if it does not duplicate `BEST_PRACTICES.md`.|
|8|Should `SOURCE_MANIFEST.md` stay?|A. Keep. B. Merge. C. Delete.|**A**|It is source-status control, not doctrine.|
|9|Should `COVERAGE_AUDIT.md` stay?|A. Keep. B. Merge. C. Delete.|**A**|It is validation/source-gap control, not doctrine.|
|10|Should `LEELA_SURFACE_MAP.md` be created now?|A. Yes. B. No. C. Only after source extension.|**C**|Create only after manual/source-extension pass validates the relevant Leela source files.|

## B.2 Appendix taxonomy

|#|Question|Options|My decision|Recommendation|
|--:|---|---|---|---|
|11|What should appendices be called?|A. `APPENDIX_*`. B. Keep current names. C. `REFERENCE_*`.|**A**|Use `APPENDIX_` prefix for clarity and to prevent authority confusion.|
|12|Should appendices live in root `alfred/`?|A. Yes. B. In `appendices/`. C. In `managed/knowledge/`.|**B recommended**|Best architecture: `managed/agent_kb/alfred/appendices/`. Keeps root clean.|
|13|Should source/audit files move into `appendices/`?|A. Yes. B. No.|**B**|Keep `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md` at root because they govern the whole Alfred KB.|
|14|Should redirects remain at old paths?|A. Yes. B. No.|**A temporarily**|Old paths should become slim redirect stubs until references are updated.|
|15|Should README list every appendix?|A. Yes. B. Only active appendices. C. No.|**B**|README should list active appendices and absorbed redirects separately.|

## B.3 Promotion and validation

|#|Question|Options|My decision|Recommendation|
|--:|---|---|---|---|
|16|Can extension pass write accepted doctrine directly?|A. Yes. B. No.|**B**|Source extension creates evidence/candidates first; promotion applies accepted changes.|
|17|Should every appendix update use promotion packets?|A. Always. B. Only truth-bearing changes. C. Never.|**B**|If appendix only redirects or indexes, normal patch is OK. If it changes accepted truth, use promotion path.|
|18|Who validates Alfred KB changes?|A. Alfred. B. `meta_ops`. C. `meta_detective`.|**B default**|`meta_ops` is Alfred’s default validator; high-risk drift can route to `meta_detective`.|
|19|Should high-risk source-gap promotions require operator review?|A. Yes. B. No.|**A**|Promotion protocol requires operator approval by default for early/high-risk truth changes.|
|20|Should manual-source extraction go directly into canonical files?|A. Yes. B. No, ledger first.|**B**|Run source-extension audit, then candidate ledger, then patch plan.|

---

# C. Recommended optimal Alfred extended-KB architecture

## C1. Root folder target state

```text
managed/agent_kb/alfred/
  README.md
  ESSENCE.md
  BEST_PRACTICES.md
  MISTAKES.md
  TEMPLATES.md
  LEARNING_QUEUE.md

  SOURCE_MANIFEST.md
  COVERAGE_AUDIT.md

  appendices/
    APPENDIX_ROUTING_MATRIX.md
    APPENDIX_WORKFLOW_PLAYBOOK.md
    APPENDIX_LEELA_SOURCE_EXTENSION.md   # only after source-extension pass
    APPENDIX_DEPRECATED_REDIRECTS.md     # optional index of absorbed files

  AGENT_CARD.md          # temporary redirect stub -> ESSENCE.md
  DOCTRINE.md            # temporary redirect stub -> ESSENCE.md
  ROLE_BOUNDARIES.md     # redirect or appendix move
  ROUTING_CONTRACT.md    # redirect or appendix move
  HANDOFF_SCHEMA.md      # redirect
  WORKFLOW_PLAYBOOK.md   # redirect or appendix move
```

## C2. Final role of each noncanonical file

|File|Recommended final state|Reason|
|---|---|---|
|`AGENT_CARD.md`|redirect stub → `ESSENCE.md`|Fully absorbed.|
|`DOCTRINE.md`|redirect stub → `ESSENCE.md`|Fully absorbed as doctrine.|
|`ROLE_BOUNDARIES.md`|redirect or move to `appendices/APPENDIX_ROLE_BOUNDARIES.md`|Only keep if detailed matrix adds value.|
|`ROUTING_CONTRACT.md`|move/slim to `appendices/APPENDIX_ROUTING_MATRIX.md`|Detailed route matrices can be useful.|
|`HANDOFF_SCHEMA.md`|redirect stub → `TEMPLATES.md` + `managed/processes/AGENT_HANDOFF_CONTRACTS.md`|Template forms absorbed; process authority lives in process contract.|
|`WORKFLOW_PLAYBOOK.md`|move/slim to `appendices/APPENDIX_WORKFLOW_PLAYBOOK.md`|Useful if kept as procedural appendix.|
|`SOURCE_MANIFEST.md`|keep root|Source ledger.|
|`COVERAGE_AUDIT.md`|keep root|Coverage / source-gap ledger.|

---

# D. Recommended prompt flow

## Phase 0 — Extended KB architecture audit, no writes

```md
# Alfred Extended KB Architecture Audit — No Writes

Repo:
- leela-spec/apexai-os-meta

Target:
- managed/agent_kb/alfred/

Mission:
Audit the intended Apex KB system and design the optimal extended-KB layer for Alfred.

Rules:
- Do not write files.
- Do not delete files.
- Do not create appendices yet.
- Fetch current repo files.
- Separate canonical KB, source/audit controls, process contracts, shared governance, appendices, redirects, and duplicates.
- Treat the five canonical files as primary.
- Treat SOURCE_MANIFEST.md and COVERAGE_AUDIT.md as source/audit controls.
- Treat managed/processes/ as process authority.
- Treat managed/knowledge/ as shared governance.
- Treat compact seed files as activation surfaces only.

Fetch:
1. managed/agent_kb/AGENT_KB_INDEX.md
2. managed/knowledge/AGENT_KB_LANES.md
3. managed/knowledge/KB_STARTING_SOURCE_MAP.md
4. managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md
5. managed/knowledge/CROSS_REFERENCE_MANIFEST.md
6. managed/knowledge/OVERLAP_VALIDATION_MATRIX.md
7. managed/rules/PROMOTION_PROTOCOL.md
8. managed/processes/AGENT_HANDOFF_CONTRACTS.md
9. managed/agents/alfred.md
10. managed/agent_kb/alfred/README.md
11. all files under managed/agent_kb/alfred/

Output:
1. INTENDED_KB_SYSTEM
   - compact seed lane
   - canonical KB lane
   - source/audit control lane
   - appendix lane
   - shared governance lane
   - process contract lane
   - promotion lane

2. CURRENT_ALFRED_FILE_CLASSIFICATION
   - file
   - current role
   - intended role
   - keep / redirect / move / delete / audit further
   - reason

3. EXTENDED_KB_DESIGN
   - final folder tree
   - appendix naming convention
   - redirect policy
   - source/audit policy
   - process-contract boundary
   - promotion boundary

4. DECISION_TABLE
   - each ambiguous file
   - options
   - recommended option
   - risk
   - verification needed

5. PATCH_PLAN
   - one file per iteration
   - exact order
   - expected operation
   - must-not-do rules

Stop after the audit.
```

## Phase 1 — Redirect absorbed duplicates

````md
# Alfred Absorbed Duplicate Redirect — Single File

Patch exactly one absorbed duplicate file.

Target:
- managed/agent_kb/alfred/[FILE].md

Rules:
- Fetch current target and SHA.
- Verify its durable content is already represented in the canonical files.
- Replace the file with a slim redirect stub.
- Do not delete yet.
- Do not patch any other file.
- Fetch back and verify.

Redirect stub format:

# [OLD FILE NAME]

## Status

```yaml
file_status: absorbed_redirect
canonical_owner: managed/agent_kb/alfred/[CANONICAL_FILE].md
redirect_reason:
absorbed_in_commit:
source_posture: no_runtime_truth_here
````

## Redirect

This file no longer acts as an Alfred KB authority.

Use:

- `[CANONICAL_FILE].md` for [content type]

- `SOURCE_MANIFEST.md` / `COVERAGE_AUDIT.md` for source/audit status if relevant


## Maintenance rule

Do not add new doctrine here. Route new material to the canonical five-file scaffold or the promotion path.

Report:

- path

- operation

- commit SHA

- fetched blob SHA

- verification result

- next recommended file


````

Recommended order:

1. `AGENT_CARD.md`
2. `DOCTRINE.md`
3. `HANDOFF_SCHEMA.md`

## Phase 2 — Decide appendix vs redirect for dense support files

```md
# Alfred Appendix Decision Pass — Single File

Patch exactly one support file.

Target:
- managed/agent_kb/alfred/[FILE].md

Candidate files:
- ROLE_BOUNDARIES.md
- ROUTING_CONTRACT.md
- WORKFLOW_PLAYBOOK.md

Rules:
- Fetch current file and SHA.
- Compare against canonical files:
  - ESSENCE.md
  - BEST_PRACTICES.md
  - MISTAKES.md
  - TEMPLATES.md
- Decide:
  A. redirect only
  B. slim in-place appendix
  C. move to appendices/APPENDIX_*.md with old-path redirect
- Prefer redirect unless the file contains detailed matrix/procedure that materially improves retrieval.
- If keeping as appendix, remove duplicate doctrine and add clear subordination header.
- Do not update more than one file unless performing a move requires creating new appendix and redirecting the old file; if strict one-file policy applies, do not move, only mark pending move.

Output:
- decision
- reason
- patch performed
- commit SHA
- fetched blob SHA
- remaining risk
- next file
````

My expected decisions:

|File|Expected decision|
|---|---|
|`ROLE_BOUNDARIES.md`|redirect or slim appendix; leaning redirect|
|`ROUTING_CONTRACT.md`|keep as `APPENDIX_ROUTING_MATRIX.md` eventually|
|`WORKFLOW_PLAYBOOK.md`|keep as `APPENDIX_WORKFLOW_PLAYBOOK.md` eventually|

## Phase 3 — Source-extension pass

```md
# Alfred Manual Source Extension Pass — No Writes

Goal:
Read attached/manual Alfred and Leela-related project sources and determine what source gaps can be upgraded.

Rules:
- Do not write to Apex.
- Do not promote claims directly.
- Do not change SOURCE_MANIFEST.md yet.
- Produce an evidence bundle and patch plan only.
- Preserve distinction between:
  - validated claim
  - partially validated claim
  - source-gap-dependent claim
  - candidate-only claim

Inputs:
- current SOURCE_MANIFEST.md
- current COVERAGE_AUDIT.md
- attached source files
- current canonical Alfred five files

Output:
1. ATTACHED_SOURCE_INDEX
   - source id
   - filename
   - attached path
   - read status
   - matching manifest entry
   - area covered

2. CLAIM_EXTRACTION_LEDGER
   - claim id
   - claim
   - source refs
   - confidence
   - affected canonical file
   - proposed candidate type
   - EVD / IMP / RSK

3. SOURCE_GAP_DIFF
   - previous gap
   - new evidence
   - new status
   - still blocked?

4. PROMOTION_CANDIDATE_QUEUE
   - candidate id
   - target canonical file
   - validator
   - operator review required?
   - risk if promoted
   - risk if rejected

5. PATCH_PLAN
   - one file per iteration
   - exact order
   - source IDs to use
   - must-not-do rules
```

## Phase 4 — Promotion-aware canonical update

```md
# Alfred Canonical Source-Extension Patch — Single File

Patch exactly one canonical file using an approved source-extension candidate bundle.

Target:
- managed/agent_kb/alfred/[ESSENCE | BEST_PRACTICES | MISTAKES | TEMPLATES | LEARNING_QUEUE].md

Rules:
- Fetch target and SHA.
- Fetch SOURCE_MANIFEST.md and COVERAGE_AUDIT.md.
- Use only claims from the approved source-extension ledger.
- Preserve source refs and source status.
- Do not harden blocked claims.
- Do not patch source/audit controls in same iteration.
- Fetch back and verify.

Report:
- target
- claim IDs applied
- operation
- commit SHA
- fetched blob SHA
- verification result
- remaining source gaps
- next file
```

## Phase 5 — Source/audit control update

```md
# Alfred Source/Audit Control Update — Single File

Patch exactly one source/audit control file.

Candidate targets:
- SOURCE_MANIFEST.md
- COVERAGE_AUDIT.md

Rules:
- Patch only after source-extension audit is complete.
- Do not convert source claims into doctrine.
- Record read status and coverage status only.
- Keep provenance separate from accepted canonical content.
- Fetch back and verify.

Report:
- target
- source statuses changed
- claims affected
- commit SHA
- fetched blob SHA
- verification result
- remaining source gaps
```

---

# E. My recommended next decision for you

I recommend this path:

1. **Do not delete anything yet.**

2. Redirect fully absorbed duplicates first:

    - `AGENT_CARD.md`

    - `DOCTRINE.md`

    - `HANDOFF_SCHEMA.md`

3. Keep `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md`.

4. Run an appendix decision pass for:

    - `ROLE_BOUNDARIES.md`

    - `ROUTING_CONTRACT.md`

    - `WORKFLOW_PLAYBOOK.md`

5. Only then run the manual-source extension pass and consider `LEELA_SURFACE_MAP.md`.


## F. Verification questions for you

1. **Redirect vs delete:** Should absorbed files become redirect stubs first, instead of deletion? My recommendation: **yes**.

2. **Appendix folder:** Should we create `managed/agent_kb/alfred/appendices/` for durable appendices? My recommendation: **yes**, but only after deciding which files genuinely deserve appendix status.

3. **Routing matrix:** Should `ROUTING_CONTRACT.md` become `appendices/APPENDIX_ROUTING_MATRIX.md`? My recommendation: **yes**.

4. **Workflow playbook:** Should `WORKFLOW_PLAYBOOK.md` become `appendices/APPENDIX_WORKFLOW_PLAYBOOK.md`? My recommendation: **yes, slimmed**.

5. **Role boundaries:** Should `ROLE_BOUNDARIES.md` redirect to `ESSENCE.md` / `BEST_PRACTICES.md` / `MISTAKES.md` rather than survive as an appendix? My recommendation: **redirect**.

6. **Leela surface map:** Should `LEELA_SURFACE_MAP.md` remain blocked until source-extension audit? My recommendation: **yes**.

7. **Promotion strictness:** Should manual-source findings become promotion candidates before canonical patches? My recommendation: **yes for material truth changes; no for purely clerical source-status updates**.


This matches the corrected direction captured in our current validation history: five canonical files as the KB, additional material only as source/audit/appendix/control, never as a second scaffold.