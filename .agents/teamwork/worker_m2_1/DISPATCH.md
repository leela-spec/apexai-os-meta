# Task Assignment: Milestone 2 — Author Layered Rule KB Rules 09 through 15

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m2_1`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- Project Scope: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md`
- Prototype: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-01-target.md`
- Master Contract: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md`
- Comprehensive Survey 1 Extraction (Rules 09–15): `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_1\survey_report.md`
- Milestone 1 Reference: `rule-02-product-first.md` through `rule-08-context.md`

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Write Ownership
You own and write ONLY these 7 files in `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\`:
1. `rule-09-recovery.md`
2. `rule-10-stop-repairing.md`
3. `rule-11-current-truth.md`
4. `rule-12-surgical.md`
5. `rule-13-editing.md`
6. `rule-14-new-machinery.md`
7. `rule-15-detour.md`

Do NOT touch any other files in the repository. Do NOT touch root `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`.

## Deliverable Requirements
Each of the 7 files must match the depth, rigor, and structure of `rule-01-target.md` and `rule-02` through `rule-08`:
1. OKF v0.2 Frontmatter (`type: Reference`, unique durable `id: V2-LAYERED-KB-RULE-XX-...`, `title`, `description`, `status: current_truth`, `tags: [...]`).
2. Layer Positioning header (Layer 0, Layer 1, Layer 2 links).
3. §1 Original Rule & Atomic Semantic Block Inventory (exact 3A text, metrics, numbered bullet list with BPE and char counts).
4. §2 Chapter-by-Chapter Semantic Block Analysis & Alternatives (per block: meaning & failure mode, critique with `[P0-P3 | I/E/R]`, Option A Baseline, Option B Surgical, Option C Aggressive).
5. §3 Whole-Rule Recomposition Rollup Table (Baseline, Option B, Option C with BPE counts and percentage savings).
6. §4 Complete Bidirectional Research & Provenance Links (internal research corpus, external literature, Plane 4 canonical module owners).
7. §5 Failure Modes & Not-To-Dos (`WP-25`).

## Critical Lessons from Milestone 1 (Link Normalization Invariants):
- Contract Lineage Links MUST point to `../../candidates/02-informatics-contract-block.md`, `../../candidates/07-contract-block-v0.4.md`, `../../candidates/09-contract-block-v0.5.md` (NOT to stale `Agent_Setup/NextIteration/...`).
- Module Deepening Links in Section 4 MUST point to directory `README.md` files (e.g. `../../research/01-universal-instruction-research/module-deepening/A04-.../README.md`), not flat non-existent `.md` files. Verify that 100% of relative links resolve to existing files on disk!

## Verification Commands
After authoring, run:
1. Python validation to check file existence, section presence, and that 100% of relative links resolve on disk.
2. `python -m pytest apex-meta/informatics/tests/ -q` to confirm all 196 tests pass.

Report all commands, outputs, and results in `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m2_1\handoff.md`.
Send completion message to Orchestrator (Recipient: `a1918f04-9801-41c9-a8a4-6cebbbfab6ed`).


## 2026-10-22T12:06:28Z
You are assigned to Milestone 2: Author Layered Rule KB Rules 09 through 15.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m2_1
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m2_1\DISPATCH.md
Read the authoritative user request at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically Section ## 2026-10-22T11:10:20Z).
Read PROJECT.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md
Examine prototype rule-01-target.md and completed M1 files rule-02 through rule-08 in: c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\
Examine the comprehensive Survey 1 extraction at: c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_1\survey_report.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Write ownership: You own and write ONLY these 7 files in c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\:
1. rule-09-recovery.md
2. rule-10-stop-repairing.md
3. rule-11-current-truth.md
4. rule-12-surgical.md
5. rule-13-editing.md
6. rule-14-new-machinery.md
7. rule-15-detour.md

Every file must follow all 5 mandatory sections matching rule-01-target.md and M1 files.
CRITICAL LESSON FROM M1: Ensure 100% of relative links resolve to existing files on disk. Point lineage links to ../../candidates/... and module-deepening links to .../README.md.
Run verification commands: test suite python -m pytest apex-meta/informatics/tests/ -q.
Document all results in c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m2_1\handoff.md and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
