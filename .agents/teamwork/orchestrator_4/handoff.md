# Orchestrator Soft Handoff: Layered Rule KB (Rules 02–22), Plane 4 Audits & 16-candidate-3A-ultra

> **Handoff Type:** Soft Handoff (Context Succession at Spawn Threshold 18 >= 16)  
> **Agent:** Orchestrator 4 (`c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4`)  
> **Successor Workspace:** `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_5` (or successor working directory)  
> **Original Parent Conversation ID:** `fcf0dbd9-0bbc-4346-a896-8b7cf81a5163`  
> **Target Scope:** Sections R1 through R5 of `ORIGINAL_REQUEST.md` (Section `## 2026-10-22T11:10:20Z`)  
> **Date:** 2026-10-22T12:25:30Z  

---

## 1. Milestone State

| # | Milestone Name | Scope | Status | Verification & Artifacts |
|---|---|---|:---:|---|
| **Phase 0** | Scope Survey | Full survey of Rules 02–22, 5 Plane 4 modules, 3A-Ultra compression, validator & pytest | **DONE** | 3 reports delivered: `spec_miner_survey_4_1/survey_report.md` (1,756 lines), `spec_miner_survey_4_2/survey_report.md`, `explorer_survey_4_3/survey_report.md`. |
| **M1** | Layered Rule KB Phase 1 (Rules 02–08) | Author `rule-02-product-first.md` through `rule-08-context.md` | **DONE** | Gate PASSED. All 7 files authored. 112/112 links resolved on disk. Pytest 196/196 passed. Clean auditor verdict. |
| **M2** | Layered Rule KB Phase 2 (Rules 09–15) | Author `rule-09-recovery.md` through `rule-15-detour.md` | **DONE** | Gate PASSED. All 7 files authored (18,168 BPE total). 125/125 links resolved on disk. Pytest 196/196 passed. Clean auditor verdict. |
| **M3** | Layered Rule KB Phase 3 (Rules 16–22) | Author `rule-16-authoring.md` through `rule-22-pointers.md` | **PLANNED** | Concrete next step for Successor: Dispatch `worker_m3_1` using `spec_miner_survey_4_1/survey_report.md` extraction. |
| **M4** | Plane 4 Infrastructure Module Audits | Author `audit-module-01` through `audit-module-05` | **PLANNED** | Dispatch worker using `spec_miner_survey_4_2/survey_report.md` 5-chapter blueprint. |
| **M5** | 3A-Ultra Compilation, Indexes & Gates | Compile `16-candidate-3A-ultra.md`, author `06-layered-rule-kb/index.md`, update `final/index.md`, final gates | **PLANNED** | Assemble 22 Option B compressions (~935 BPE), generate indexes, run `okf_validator.py` and `pytest`. |

---

## 2. Active Subagents

All 18 spawned subagents have completed and delivered their handoffs. Zero subagents are currently active.
Spawn count at succession: **18 / 16**.

---

## 3. Pending Decisions & Key Invariants

1. **Link Normalization Rule (Mandatory for M3 & M4)**:
   - Contract Lineage Links must point to `../../candidates/02-informatics-contract-block.md`, `../../candidates/07-contract-block-v0.4.md`, `../../candidates/09-contract-block-v0.5.md` (NOT to stale `Agent_Setup/NextIteration/...`).
   - Module Deepening Links in Section 4 must point to directory `README.md` files (e.g. `../../research/01-universal-instruction-research/module-deepening/A06-.../README.md`), not flat `.md` files.
2. **Zero Live Mutation**:
   - `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` must not have any new modifications.
3. **Research Preservation**:
   - Zero changes to `final/research/01-universal-instruction-research/` and `final/research/03-research-of-file-10/`.
4. **Sub-Bundle Isolation**:
   - In Milestone 5, creating `apex-meta/informatics/final/research/06-layered-rule-kb/index.md` establishes an isolated sub-bundle in `okf_validator.py` (line 206), ensuring 0 OKF Errors.

---

## 4. Remaining Work (Concrete Next Steps for Successor)

1. **Milestone 3 Execution (Rules 16–22)**:
   - Target files in `apex-meta/informatics/final/research/06-layered-rule-kb/`:
     - `rule-16-authoring.md` (`<authoring>`)
     - `rule-17-trade-off.md` (`<trade_off>`)
     - `rule-18-handover.md` (`<handover>`)
     - `rule-19-iterative.md` (`<iterative>`)
     - `rule-20-schemas.md` (`<schemas>`)
     - `rule-21-sync.md` (`<sync>`)
     - `rule-22-pointers.md` (`<pointers>`)
   - Draw all pre-calculated BPE metrics, semantic blocks (`SB-16.1`..`SB-22.2`), options A/B/C, and Plane 4 owners directly from `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_1\survey_report.md`.
   - Dispatch Worker -> 2 Reviewers, 2 Challengers, 1 Auditor -> Gate check.
2. **Milestone 4 Execution (Module Audits 01–05)**:
   - Target files in `apex-meta/informatics/final/research/06-layered-rule-kb/`:
     - `audit-module-01-writing-profile.md`
     - `audit-module-02-file-architecture.md`
     - `audit-module-03-execution-modes.md`
     - `audit-module-04-anti-drift-rules.md`
     - `audit-module-05-governance-schemas.md`
   - Use `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2\survey_report.md` 5-chapter blueprint.
   - Dispatch Worker -> 2 Reviewers, 2 Challengers, 1 Auditor -> Gate check.
3. **Milestone 5 Execution (3A-Ultra, Indexes & Gates)**:
   - Compile `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md` concatenating Option B compressions (~935 BPE, target ~900–980 BPE).
   - Include rule-by-rule delta table against `13-candidate-3A-xml.md`.
   - Create `apex-meta/informatics/final/research/06-layered-rule-kb/index.md` linking all 22 rules and 5 audits.
   - Update `apex-meta/informatics/final/index.md` linking the new KB and candidate.
   - Run deterministic gate: `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` (0 errors).
   - Run test suite: `python -m pytest apex-meta/informatics/tests/ -q` (196/196 passed).
   - Final audit and delivery to parent (`fcf0dbd9-0bbc-4346-a896-8b7cf81a5163`).

---

## 5. Key Artifacts

- Project Document: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md`
- Gate Ledger: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\GATE_STATUS.md`
- Survey 1 Report (Rules 02–22): `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_1\survey_report.md`
- Survey 2 Report (Plane 4 Audits): `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2\survey_report.md`
- Survey 3 Report (3A-Ultra & Gates): `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_4_3\survey_report.md`
- Completed Rule Deep-Dives: `apex-meta/informatics/final/research/06-layered-rule-kb/rule-01-target.md` through `rule-15-detour.md` (15 rules complete).
