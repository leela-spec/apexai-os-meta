---
type: Runbook
id: RUNBOOK-RESTRUCTURING-AND-NEXT-PHASE-v1.0
title: Apex Informatics Restructuring & Multi-Repo Alignment Handover
description: Master handover document for a fresh chat session detailing the complete current-truth state, operator directives for restructuring final/ into numbered system folders and unnumbered project-management/research, and next execution steps.
status: current_truth
tags: [handover, restructuring, project-management, candidates, specs, verification]
---

# Apex Informatics Restructuring & Multi-Repo Alignment Handover

> **Purpose:** Handover document for an incoming fresh chat session. It documents the exact current-truth state of the codebase, clarifies the operator's architectural restructuring directives, and provides a safe, step-by-step execution roadmap.

---

## 1. Executive Summary & Current State (Ground Truth)

- **Total Assets:** Exactly **213 files** are safely preserved inside `apex-meta/informatics/final/`.
- **Zero Data Loss:** **The specifications are 100% intact.** All 7 spec files live at `apex-meta/informatics/final/specs/`. No files have been deleted or moved.
- **Verification Engine:** The core 338 pytest tests pass in 0.7s (`python -m pytest apex-meta/informatics/final/verification/suites`). *(Note: An untracked draft file `test_m6_two_layer_carrier_drafts.py` was created in a separate turn and can be cleanly aligned or inspected).*
- **Empirical Antigravity Trial Completed:** Subagents confirmed that `<apex_contract v="1.0-ultra">` eliminates index file bloat and enforces surgical 20–40 line reading windows (`09-TRIAL-RUN-EVALUATION-REPORT.md`).

---

## 2. Operator's Directives for Restructuring `final/`

The operator requires a clean separation between **executable/referenced system files** (numbered `01`–`04`) and **human/meta-management folders** (un-numbered: `project-management` and `research`):

### The Target Directory Architecture:

```
apex-meta/informatics/final/
│
├── 01-candidates/                 <-- ACTIVE RATIFIED CONTRACT BLOCKS & BLUEPRINTS
│   ├── 16-candidate-3A-ultra.md   (Ratified v1.0-ultra pure XML candidate)
│   ├── 03-BLUEPRINT-agents.md     (Two-layer carrier blueprint)
│   ├── 13-candidate-3A-xml.md     (Baseline 3A pure XML)
│   ├── 14-candidate-3B-hybrid.md  (Benchmark 3B table)
│   ├── 15-candidate-3C-bullet-hybrid.md (Benchmark 3C bullets)
│   └── archive/                   <-- OLD CONTRACT DRAFTS (ISOLATED)
│       ├── 02-informatics-contract-block.md (v0.2 draft)
│       ├── 06-contract-block-revision-proposal.md (v0.3 proposal)
│       ├── 07-contract-block-v0.4.md (v0.4 draft)
│       └── 09-contract-block-v0.5.md (v0.5 draft)
│
├── 02-specs/                      <-- NORMATIVE SPECIFICATIONS (INTACT)
│   ├── standard.md
│   ├── writing-profile.md
│   ├── file-architecture.md
│   ├── anti-drift-rules.md
│   ├── execution-modes.md
│   ├── governance-schemas.md
│   ├── general-informatics-router.md
│   └── index.md
│
├── 03-sub-bundles/                <-- PROJECT FIXTURES (INTACT)
│   ├── Agent_Setup/
│   └── MMM/
│
├── 04-tools-and-verification/     <-- MERGED TOOLING & VERIFICATION
│   ├── suites/                    (The 7 pytest suites)
│   ├── test-kb/                   (Anti-fake-test rationales)
│   ├── okf_validator.py           (Canonical validator)
│   ├── agent_eval_runner.py       (Benchmark runner)
│   ├── 04-empirical-test-protocol.md (Test protocol moved from candidates)
│   └── README.md                  (Anti-Fake-Test Charter)
│
├── project-management/            <-- REPLACES operations/ (PROMINENT ACTIVE SECTIONS)
│   ├── active-discussions/        <-- PROMINENT: WHAT REQUIRES OPERATOR ATTENTION
│   │   ├── 08-discussion-and-open-threads.md
│   │   └── 05-LONG-LIST-IDEAS-AND-CLOSE-CUTS.md
│   ├── decisions/                 <-- RATIFIED BASELINE
│   │   └── 01-decision-register.md (DEC-01 through DEC-23)
│   ├── plans-and-runbooks/        <-- LIVE PLANS, REPORTS & HANDOVERS
│   │   ├── 06-EXECUTION-PLAN-AND-THINKING-PROCESS.md
│   │   ├── 07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md
│   │   ├── 08-AGENT-EVALUATION-AND-HANDOVER-RUNBOOK.md
│   │   ├── 09-TRIAL-RUN-EVALUATION-REPORT.md
│   │   ├── 10-MULTI-CLI-MULTI-REPO-INSTRUCTION-AUDIT-HANDOVER.md
│   │   ├── 11-TWO-LAYER-CARRIER-DRAFTS-MULTI-REPO.md
│   │   └── log.md
│   └── archive/                   <-- INACTIVE / SUPERSEDED / AUDIT ONLY
│       ├── 12-status-index.md
│       └── migration.md
│
├── research/                      <-- UN-NUMBERED (RESEARCH ARTIFACTS)
│   ├── 01-universal-instruction-research/
│   ├── 02-deep-reasoning/
│   ├── 03-research-of-file-10/
│   ├── 04-finalization-dossier/
│   ├── 05-analysis-after-research/
│   ├── 06-layered-rule-kb/
│   └── prompt-packets/            <-- RESEARCH HANDOVERS & PROMPTS
│       ├── 05-research-prompt-packets.md
│       ├── 10-RESEARCH-EXECUTION-HANDOVER.md
│       └── 11-instruction-surface-architecture.md
│
└── index.md                       <-- ROOT ENTRYPOINT ROUTER
```

---

## 3. Step-by-Step Instructions for the Next Chat Session

1. **Verify Live State:**
   - Run `python -m pytest apex-meta/informatics/final/verification/suites/test_informatics_e2e.py` to confirm current specs and tests are healthy.
2. **Execute the File Moves:**
   - Create the target directories (`01-candidates/archive/`, `02-specs/`, `03-sub-bundles/`, `04-tools-and-verification/`, `project-management/active-discussions/`, `project-management/decisions/`, `project-management/plans-and-runbooks/`, `project-management/archive/`).
   - Move the files per the map in Section 2.
3. **Synchronize Dependencies:**
   - Update path fixtures in `suites/*.py` to reflect the new directory names.
   - Update relative markdown links in `final/index.md` and moved files.
   - Run `qmd update` to refresh local BM25 and vector embeddings.
4. **Run Verification:**
   - Ensure 100% of tests pass cleanly.
