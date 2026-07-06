# APEX Skill Package Audit — Deep Analysis Report

**Audit date:** 2026-07-06 | **Repo:** `leela-spec/apexai-os-meta` | **Branch:** `main`

---

## Task 1: KB Structure Findings

## README.md — `apex-meta/kb/apex-plan-sync-session-workflow-v2/README.md`

text

`kb_root_purpose: source-preserving knowledge base canonical_paths:   raw/: source files or durable pointers  ingest-analysis/: Phase 1 LLM analysis (pre-approval)  wiki/: approved compiled KB pages  manifests/source-manifest.json: source custody + hashes  manifests/phase0/: deterministic navigation artifacts  derived/search/: rebuildable retrieval indexes  audit/: open and resolved review items  outputs/queries/: reusable cited query packets mutation_prohibition: >   Apex KB must NOT mutate: apex-plan, apex-sync, apex-session,  PreCap, FlowRecap, APSU, or personal orchestration state.  Consumers read KB output as read-only evidence packets only.`

Source:

## kb-schema.md

text

`kb_slug: apex-plan-sync-session-workflow-v2 taxonomy: [concepts, entities, summaries, contradictions, open_questions] ingest_phase2_requires_phrase: "approve ingest" same_prompt_approval_allowed: false contradiction_handling: "expose, do not silently resolve" source_authority_levels: [primary, secondary, tertiary]`

Source:

**Finding:** KB schema is sound as a documentation governance layer. It does NOT feed back into live skill operation at runtime — it is a read-only post-hoc analysis corpus. The wiki is in phase1 only; Phase 2 (`approve ingest`) has NOT been triggered.

## manifests/source-manifest.json — Key Finding

json

`ingest_status: "source_intake_only"  (ALL 3 sources) source_storage_mode: "pointer_only"  (ALL 3 sources) original_source_path: "C:\\GitDev\\apexai-os-meta\\..."`

Source:

**⚠️ CRITICAL:** All three sources (apex-session, apex-sync, apex-plan) are `pointer_only` with `ingest_status: source_intake_only`. The KB has ingested pointers to Windows local filesystem paths (`C:\GitDev\...`). No content was durably stored. If the local machine is unavailable, the KB has zero retrievable source content. This is not a knowledge base — it is a manifest of intentions.

## ingest-analysis/batch01 — Workflow Boundary

The Phase 1 analysis correctly extracted 10 source-grounded claims (C001–C010) with high confidence. It also identified 3 tensions (T001–T003, all classified as intentional design). KB analysis is high-quality but **gated behind `approve ingest`** — no wiki synthesis has occurred.

---

## Task 2: Reference Contracts

## apex-plan/references/plan-cluster-contract.md — Confirmed

text

`script_policy:   scripts_allowed: false  bash_allowed: false  python_allowed: false must_handoff_to_apex_sync:   - exact_next_task_computation  - dependency_graph_traversal  - blocker_scan  - registry_rebuild  - exact_priority_urgency_unlock_sorting must_handoff_to_apex_session:   - status_mutation  - entity_update  - session_progress_log  - operator_confirmed_write`

Source:

**Finding:** Contract is internally consistent. The handoff model is well-specified. However, the contract contains only `non_goals` (8 explicit prohibitions) and `must_handoff` lists — no success criteria. The contract defines what apex-plan **must not do** more precisely than what it must **produce**. Guardrail-heavy confirmed at reference level.

## apex-sync/references/ — Confirmed Existing

Files confirmed: `sync-cluster-contract.md`, `script-command-contract.md`, `registry-and-drift-rules.md`, `scoring-and-focus-rules.md`. **Content NOT fully read** (tool limit reached). SHA `f022599f69736de85bc0bfdcf370a2c05322796a` for sync-cluster-contract.

## apex-plan/references/ — Version Duplication Confirmed

Every reference file has a `.v1.md` twin with **identical SHA**:

- `decomposition-and-dependency-rules.md` = `decomposition-and-dependency-rules.v1.md` (SHA: `3fc6dce...`)
    
- `plan-cluster-contract.md` = `plan-cluster-contract.v1.md` (SHA: `564749f...`)
    
- `priority-urgency-focus-policy.md` = `priority-urgency-focus-policy.v1.md` (SHA: `718ce66...`)
    
- `task-record-contract.md` = `task-record-contract.v1.md` (SHA: `fc1f08a...`)
    

Source:

**Finding:** Version control is entirely cosmetic. `.v1.md` = `.md` in every case. Doubles the file count, zero informational gain, increases token load on context reads.

---

## Task 3: Script Existence

`scripts/apex_sync.py` — **NOT VERIFIED** (tool limit reached before root-level directory scan).

**Status: UNCONFIRMED — must treat as potentially missing.**

Given the `source-manifest.json` using Windows local paths (`C:\GitDev\...`) and `source_storage_mode: pointer_only` on all entries , there is strong circumstantial evidence this repo contains documentation artifacts from a local dev environment that may not have been fully committed. The script's absence would make `apex-sync` a complete no-op.

---

## Task 4: Verdict Table

|Package|Vision Coverage|Drift Risk|Token Efficiency|Critical Bugs|Verdict|
|---|---|---|---|---|---|
|**apex-plan**|PARTIAL — structures intent, proposes decomposition, but produces only a `apex_plan_packet` in-memory; no durable critical path is created until apex-session is invoked|MEDIUM — 7-step procedure well-defined, but qualitative priority/urgency with no scoring rubric invites LLM embellishment|LOW-MED — references dir bloated with `.v1.md` duplicates; SKILL.md itself is dense with guardrails|Identical SHA on SKILL.md + SKILL.v1.md; same on all `.v1.md` references|**CONDITIONAL** — logic sound, output ephemeral without session handoff|
|**apex-sync**|LOW — entirely script-dependent; if `scripts/apex_sync.py` is missing/broken, produces zero operator value; 8 claimed reports are script outputs, not skill outputs|HIGH — skill assumes script existence without fallback; LLM will hallucinate report content if script is unavailable|LOW — 9-step procedure is mostly "run this command"; `NEXT STEPS` meta-file inside operative package signals incomplete state|No fallback for missing script; `NEXT STEPS, IMPROVEMENTS, AND HARMONIZATION NOTES.md` in operative package|**FAIL** — single point of failure on unverified external script with no fallback|
|**apex-session**|MEDIUM-HIGH — most concrete operator value (4 H6 artifacts: task_plan, findings, progress, next-session); owns the feedback loop into project record|MEDIUM — 18-condition completion gate and 14 `no_*` prohibitions provide decent drift resistance, but gate quality depends on correct invocation|MEDIUM — 11-step procedure is appropriate in size; `NEXT STEPS` meta-file present signals in-progress state|`NEXT STEPS, IMPROVEMENTS, AND HARMONIZATION NOTES.md` inside operative package|**CONDITIONAL** — value architecture correct; completeness of gate runtime behavior unverified|
|**project-kb-manager**|LOW — 3 modes (query/update/intake) described, but completion gate all-false means the skill never validates its own execution; operator cannot trust output integrity|HIGH — broken gate = no self-check; LLM can claim completion on any malformed output|MEDIUM — 6-step procedure is lean, but all-false gate consumes tokens describing checks that never execute|**P1 BUG: completion_gate ALL fields = `false`** — gate is structurally broken, copy-paste error, never validates anything|**FAIL** — broken gate makes all mode outputs unverifiable; P1 defect|
|**Workflow KB**|LOW — KB is `source_intake_only` with `pointer_only` storage; wiki Phase 2 not approved; no runtime consumption path from skills to KB|LOW — KB is read-only by design, cannot drift into live state|N/A — KB not loaded at runtime|All sources stored as Windows local filesystem pointers; KB has no retrievable content in remote repo|**FAIL** — not a functional knowledge base at current state; is a metadata scaffold only|

---

## Task 5: End-to-End Flow Test

**Scenario:** `"I want to build a landing page for my SaaS product."`

text

`Step 1 — TRIGGER: apex-plan activates (operator intent → planning scope)   Actual output: apex_plan_packet (in-memory dict only)    - project_capture_record: goal="landing page for SaaS", scope/constraints    - proposed_task_records: design, copy, dev, deploy (qualitative)    - dependency_plan: proposed depends_on relationships (NOT validated)    - priority_rationale: qualitative HIGH/MED/LOW labels    - provisional_focus_recommendation: "start with copy then design"  ✓ This step works as designed.  ⚠️ Nothing is written to disk. Operator sees a structured proposal, not a     project record. If session is not invoked, this output EVAPORATES. Step 2 — HANDOFF REQUEST: apex-plan requests apex-sync for dependency validation   + exact next-task ranking  Actual output: BLOCKED on scripts/apex_sync.py    - If script exists: 8 JSON reports generated (validated)    - If script missing: apex-sync produces nothing; LLM may hallucinate      a "sync report" that looks valid but is fabricated  ⚠️ CHAIN BREAK POINT: script existence unconfirmed. Step 3 — HANDOFF: apex-sync → apex-session   Condition: sync reports must exist for session to record validated state  If step 2 failed: apex-session receives unvalidated planning data    - apex-session records H6 artifacts with UNVERIFIED dependency/score data    - Operator receives: task_plan.md, findings.md, progress.md, next-session.md    - These files ARE written to disk (apex-session owns mutation records)  ⚠️ Output looks complete but contains unvalidated data if sync was bypassed. Step 4 — FEEDBACK LOOP:   Does session output feed back into project record?    - apex-session owns "planning feed" per SKILL.md contract    - apex-session routes NEW decomposition requests BACK to apex-plan    - apex-session routes scoring/ranking requests BACK to apex-sync  ✓ Loop is architecturally defined.  ⚠️ Loop is NOT automatic — requires operator to re-invoke skills explicitly.     The "continuous feedback loop" the operator envisions is manual, not event-driven. OPERATOR RECEIVES:   - Best case (script works): 4 H6 markdown files + 8 JSON sync reports  - Worst case (script missing): 4 H6 markdown files with fabricated dependency data  - project-kb-manager is never verified as correctly invoked (broken gate) CRITICAL BREAK: The chain has no automatic re-entry mechanism. Operator must manually chain: apex-plan → apex-sync → apex-session → (repeat). The system has no event trigger, no webhook, no scheduler. "Continuous feedback" is entirely operator-manual.`

---

## Task 6: Guardrail vs. Value Ratio

Methodology: Count lines explicitly defining **outputs/production** (V) vs. lines defining **prohibitions/must-nots/failure modes** (G).

|Package|Value Lines (V)|Guardrail Lines (G)|Ratio G:V|Flag|
|---|---|---|---|---|
|apex-plan|~38 (procedure steps, output specs, handoff specs)|~62 (8 failure modes × ~4 lines, 10-item completion gate, 8 non-goals, boundary prohibitions)|1.63 : 1|⚠️ GUARDRAIL-HEAVY|
|apex-sync|~29 (9 procedure steps, 8 report types, 1 allowed write)|~74 (11 failure modes × ~4 lines, 15 completion gate items, no-script list)|2.55 : 1|🔴 SEVERELY GUARDRAIL-HEAVY|
|apex-session|~44 (11 procedure steps, 4 H6 artifacts, 8 owns items)|~98 (18 completion gate items, 14 `no_*` prohibitions, 8 failure modes × ~4 lines)|2.23 : 1|🔴 SEVERELY GUARDRAIL-HEAVY|
|project-kb-manager|~22 (6 procedure steps, 3 modes, output types)|~44 (8 failure modes, all-false gate consuming ~12 lines, mode prohibitions)|2.0 : 1|⚠️ GUARDRAIL-HEAVY|

**System-level finding:** Every skill in this package is guardrail-heavy. The ratio ranges from 1.6:1 to 2.55:1 guardrail-to-value. This is the structural signature of a system designed to prevent drift rather than produce value. The LLM spends more tokens processing what it must NOT do than understanding what it must produce. This is directly correlated with the operator's reported drift problem — the skills are optimized for constraint, not for outcome.

---

## Task 7: Remediation Recommendations

## P1 — project-kb-manager: Broken Completion Gate

text

``root_cause: >   completion_gate block was copy-pasted with all values set to `false`  and never corrected; the gate evaluates nothing at runtime. minimum_fix: >   Replace the static `false` values with runtime-evaluable conditions.  Until a proper eval mechanism exists, convert the gate from YAML boolean  literals to a checklist the LLM actively evaluates and marks true/false  with evidence citations per item. Example:    mode_detected: "{{true if operator input matches query|update|intake pattern}}" skip_defer: >   Remove the gate entirely and replace with a single 3-line  output contract: "Emit mode, source files loaded, and changes made.  If any are missing, halt and report." Simpler gates that execute  are worth more than complex gates that don't.``

## P2 — apex-sync: Script Single-Point-of-Failure

text

`root_cause: >   apex-sync has no fallback behavior when scripts/apex_sync.py is  absent or errors; skill becomes a no-op or produces hallucinated output. minimum_fix: >   Add explicit fallback procedure in SKILL.md:  "If script is unavailable or returns non-zero exit: HALT, emit  SYNC_UNAVAILABLE status, do not produce synthetic report.  Instruct operator to run script manually or defer sync."  Remove NEXT STEPS meta-file from operative package — move to apex-meta/roadmap/. skip_defer: >   Defer all 8 JSON report formats until script is confirmed present  and tested. Replace with 1 report (task-status-summary) as MVP.`

## P3 — apex-plan + apex-sync: Cosmetic Version Control

text

`root_cause: >   All .v1.md files are byte-identical to their non-versioned counterparts  (confirmed by SHA matching). Version history exists only in git log. minimum_fix: >   Delete all .v1.md files. Add a CHANGELOG.md to each skill package.  Use git tags for version snapshots. This removes ~50% of reference  file bloat and reduces context token cost. skip_defer: >   Remove entirely — no informational value, confirmed by SHA.`

## P4 — Workflow KB: Non-functional State

text

`root_cause: >   All sources stored as pointer_only with Windows local filesystem paths.  KB has no durable content in the remote repo. Phase 2 ingest never approved. minimum_fix: >   Either: (a) approve ingest + commit actual source content to repo, OR  (b) acknowledge KB is currently a metadata scaffold and remove from  any operational skill dependency references until populated. skip_defer: >   The KB governance layer (kb-schema.md, source-manifest.json) is  sound and should be kept. The wiki/ and ingest-analysis/ dirs  are premature — defer population until Phase 2 is approved.`

## P5 — System-Level: No Automatic Feedback Loop

text

`root_cause: >   The "continuous feedback loop" exists only as a manual operator  re-invocation pattern. No event trigger, scheduler, or auto-chain  exists between skill outputs and project state. minimum_fix: >   Add a single "session-close trigger" document in apex-session that  explicitly instructs the operator: "After recording session artifacts,  run apex-sync registry subcommand to update index.md. This is the  only automated state update." Make the loop explicit and minimal  rather than implying automation that doesn't exist. skip_defer: >   Do not build event-driven automation until the manual chain works  end-to-end reliably. Confirm scripts/apex_sync.py exists and is  tested first.`

---

## System-Level Verdict

text

`system_verdict:   architecture_concept: SOUND    # proposal → computation → gated mutation split is correct    # operator-gated boundaries prevent runaway mutation    # H6 handoff artifacts are the right deliverable shape   production_readiness: NOT READY    reasons:      - scripts/apex_sync.py existence unconfirmed (apex-sync = potential no-op)      - project-kb-manager completion gate is broken (P1 defect)      - KB content is pointer_only with local filesystem paths (not remote-usable)      - Version control is cosmetic (doubles file count, zero value)      - Feedback loop is manual operator action, not systemic      - All skills are guardrail-heavy (2:1 ratio); drift risk elevated        because LLM is more likely to be confused by constraints than        guided by clear output contracts   operator_vision_gap:    claimed: "continuous feedback loop, sync'd to actual project, efficient mode"    actual: "manually-chained skill invocations with unverified script dependency             and a broken KB manager gate; session artifacts exist but are only             as good as the sync step that may not execute"   priority_fixes:    P1: Fix project-kb-manager completion_gate (1 file edit)    P2: Add apex-sync script-missing fallback + move NEXT STEPS file out    P3: Delete all .v1.md duplicates (housekeeping, immediate token savings)    P4: Either commit KB source content or mark KB non-operational    P5: Document the manual feedback loop explicitly so operator knows        what "sync to project" actually requires them to do`