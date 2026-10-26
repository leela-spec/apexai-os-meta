## 2026-10-22T11:31:21Z

# Task Assignment: Milestone 1 — Author Layered Rule KB Rules 02 through 08

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m1_1`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- Project Scope: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md`
- Prototype Template: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-01-target.md`
- Survey 1 Report (Exhaustive extraction): `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_1\survey_report.md`
- Master Contract (Layer 0): `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md`

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Write Ownership
You own and write ONLY these 7 files:
1. `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-02-product-first.md`
2. `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-03-scope.md`
3. `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-04-communication.md`
4. `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-05-hold-position.md`
5. `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-06-ground.md`
6. `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-07-reuse.md`
7. `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-08-context.md`

Do NOT touch any other files in the repository. Do NOT touch root `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`.

## Deliverable Requirements
Each of the 7 files must match the depth, rigor, and structure of `rule-01-target.md`:
1. OKF v0.2 Frontmatter (`type: Reference`, `id: V2-LAYERED-KB-RULE-XX-...`, `title`, `description`, `status: current_truth`, `tags: [...]`).
2. Layer Positioning header (Layer 0, Layer 1, Layer 2 links).
3. §1 Original Rule & Atomic Semantic Block Inventory (exact 3A text, metrics, numbered bullet list with BPE and char counts).
4. §2 Chapter-by-Chapter Semantic Block Analysis & Alternatives (per block: meaning & failure mode, critique with `[P0-P3 | I/E/R]`, Option A Baseline, Option B Surgical, Option C Aggressive).
5. §3 Whole-Rule Recomposition Rollup Table (Baseline, Option B, Option C with BPE counts and percentage savings).
6. §4 Complete Bidirectional Research & Provenance Links (internal research corpus, external literature, Plane 4 canonical module owners).
7. §5 Failure Modes & Not-To-Dos (`WP-25`).

## Verification Commands
After authoring, run:
1. Python validation to check file existence and token counts.
2. `python -m pytest apex-meta/informatics/tests/ -q` to confirm all 196 tests continue passing.

Report all commands, outputs, and results in `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_m1_1\handoff.md`.
Send completion message to Orchestrator (Recipient: `a1918f04-9801-41c9-a8a4-6cebbbfab6ed`).
