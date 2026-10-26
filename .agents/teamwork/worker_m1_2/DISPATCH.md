# Task Assignment: Milestone 1 Iteration 2 Remediation Worker

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m1_2`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- Project Scope: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md`
- Gate Status: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\GATE_STATUS.md`
- Challenger 2 Handoff Report with exact replacement table: `c:\GitDev\apexai-os-meta\.agents\teamwork\challenger_m1_2\handoff.md`
- Target Files Owned Exclusively:
  1. `apex-meta/informatics/final/research/06-layered-rule-kb/rule-02-product-first.md`
  2. `apex-meta/informatics/final/research/06-layered-rule-kb/rule-03-scope.md`
  3. `apex-meta/informatics/final/research/06-layered-rule-kb/rule-04-communication.md`
  4. `apex-meta/informatics/final/research/06-layered-rule-kb/rule-05-hold-position.md`
  5. `apex-meta/informatics/final/research/06-layered-rule-kb/rule-06-ground.md`
  6. `apex-meta/informatics/final/research/06-layered-rule-kb/rule-07-reuse.md`
  7. `apex-meta/informatics/final/research/06-layered-rule-kb/rule-08-context.md`

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Remediation Objectives
Apply the exact surgical link replacements across all 7 files as detailed in Challenger 2's handoff:
1. **Contract Lineage Links**:
   - Replace: `../../Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md`
   - With: `../../candidates/02-informatics-contract-block.md`
   - Replace: `../../Agent_Setup/NextIteration/v2-always-on-architecture/07-contract-block-v0.4.md`
   - With: `../../candidates/07-contract-block-v0.4.md`
   - Replace: `../../Agent_Setup/NextIteration/v2-always-on-architecture/09-contract-block-v0.5.md`
   - With: `../../candidates/09-contract-block-v0.5.md`

2. **Module Deepening Links**:
   - In `rule-02`: Replace `A01-substance-over-ceremony.md` with `A01-target-outcome-alignment/README.md`
   - In `rule-02`: Replace `A07-hierarchical-realization.md` with `A07-hierarchical-realization-verification-validation/README.md`
   - In `rule-03`: Replace `A02-scope-and-non-goals.md` with `A02-scope-non-goals/README.md`
   - In `rule-04`: Replace `A12-communication-economy.md` with `A12-communication-economy-actionable-visibility/README.md`
   - In `rule-05`: Replace `A05-intent-alignment.md` with `A05-intent-alignment-clarification-threshold/README.md`
   - In `rule-06`: Replace `A08-evidence-integrity.md` with `A08-evidence-integrity-uncertainty-calibration/README.md`
   - In `rule-06`: Replace `A13-external-grounding.md` with `A13-external-grounding-real-world-verification/README.md`
   - In `rule-07`: Replace `A03-reuse-before-invention.md` with `A03-reuse-before-invention/README.md`
   - In `rule-08`: Replace `A06-context-engineering.md` with `A06-context-engineering-progressive-disclosure/README.md`

3. Verify with Python that 100% of relative links across all 7 files resolve to actual existing files on disk.
4. Run pytest suite: `python -m pytest apex-meta/informatics/tests/ -q` (must remain 196/196 passing).
5. Document all changes in `handoff.md` and send completion message to Orchestrator (`a1918f04-9801-41c9-a8a4-6cebbbfab6ed`).

## 2026-10-22T11:52:59Z
You are Worker M1 Iteration 2 (Remediation Specialist).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m1_2
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m1_2\DISPATCH.md
Read the authoritative user request at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically Section ## 2026-10-22T11:10:20Z).
Read Challenger 2 feedback in: c:\GitDev\apexai-os-meta\.agents\teamwork\challenger_m1_2\handoff.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Write ownership: You own and write ONLY these 7 files in c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\:
1. rule-02-product-first.md
2. rule-03-scope.md
3. rule-04-communication.md
4. rule-05-hold-position.md
5. rule-06-ground.md
6. rule-07-reuse.md
7. rule-08-context.md

Task: Apply the exact surgical replacement mapping provided in Section 4 of Challenger 2's handoff to fix all 30 broken relative markdown links.
Verify that 100% of links resolve to real files on disk.
Run pytest suite: python -m pytest apex-meta/informatics/tests/ -q.
Write handoff.md and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
