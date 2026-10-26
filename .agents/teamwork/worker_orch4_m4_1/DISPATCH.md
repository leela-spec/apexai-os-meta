# Task Assignment: Milestone 4 Worker (Plane 4 Infrastructure Module Audits)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\worker_orch4_m4_1`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (see Section `## 2026-10-22T11:10:20Z`, specifically R2)
- Project Scope: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md`
- Canonical Plane 4 Source Modules in `c:\GitDev\apexai-os-meta\apex-meta\informatics\`:
  1. `writing-profile.md` (25 rules: `WP-01`..`WP-25`)
  2. `file-architecture.md` (13 rules: `FA-01`..`FA-13`)
  3. `execution-modes.md` (12 rules: `EM-01`..`EM-12`)
  4. `anti-drift-rules.md` (28 rules: `AD-01`..`AD-28`)
  5. `governance-schemas.md` (22 rules: `GS-01`..`GS-22`, with `GS-16`, `GS-18`, `GS-19` retired)
- Blueprint & Survey Report: `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2\survey_report.md`
- Target Directory: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\`

## Mandatory Write Ownership
You own and write ONLY these 5 files in `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\`:
1. `audit-module-01-writing-profile.md`
2. `audit-module-02-file-architecture.md`
3. `audit-module-03-execution-modes.md`
4. `audit-module-04-anti-drift-rules.md`
5. `audit-module-05-governance-schemas.md`

You MUST NOT modify root `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or upstream research corpora (`01-universal-instruction-research/`, `03-research-of-file-10/`).

## MANDATORY INTEGRITY WARNING
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Structure & Depth Requirements
Every one of the 5 module audit files must be a thorough, genuine, full-depth analytical document (~2,000–3,500 BPE tokens each) adhering to OKF v0.2 frontmatter (`type: Reference`, `status: current_truth`) and the 5-chapter structure detailed in `spec_miner_survey_4_2/survey_report.md` §6:

1. **Chapter 1: Module Scope & Governed Rule Inventory**
   - Frontmatter + Module domain, role in Plane 4 information architecture.
   - Comprehensive rule-by-rule inventory table covering every governed rule in the module with columns: `#`, `Category`, `Rule ID`, `Tier & Metrics [P<tier> | I<impact>/E<evidence>/R<risk>]`, `Title`, `Description & Scope`, `Preconditions / Inputs`, `Outputs / Behaviors`, `Error / Halt Behavior`, `Canonical Owner`.
2. **Chapter 2: Single-Ownership Verification Ledger (`WP-23`)**
   - Detailed audit of Single-Ownership Discipline (`WP-23`).
   - Distinguish rules canonically owned by this module from rules owned by other Plane 4 modules and merely referenced.
   - Explicit confirmation that no duplicated schemas or multi-line directives exist across modules.
3. **Chapter 3: Redundancy & Stale Terminology Remediation Plan**
   - Concrete audit of duplicate concept clusters and stale terminology.
   - Actionable remediation advice for future plane consolidations.
4. **Chapter 4: Cross-Traceability Matrix to XML `<apex_contract>` and Ultra Contract**
   - Bidirectional matrix mapping how this module's rules map to the 22 semantic tags in `<apex_contract v="1.0">` (`13-candidate-3A-xml.md`) and the upcoming `16-candidate-3A-ultra.md`.
5. **Chapter 5: Failure Modes & Not-To-Dos (`WP-25`)**
   - Placed in terminal position per `WP-25`.
   - Concrete boundaries, forbidden shortcuts, and anti-patterns for anyone editing or implementing this module.

## Critical Invariants & Lessons
- Ensure 100% of relative markdown links resolve to real files on disk. Use relative paths:
  - Lineage candidates: `../../candidates/02-informatics-contract-block.md`, `07-contract-block-v0.4.md`, `09-contract-block-v0.5.md`, `13-candidate-3A-xml.md`.
  - Upstream research: `../../research/01-universal-instruction-research/RESULTS-01-foundations.md` (or `module-deepening/.../README.md`).
  - Sibling rules: `./rule-01-target.md` etc.
- Significance tags MUST follow `[P<tier> | I<int>/E<int>/R<int>]` with raw integers 1–100. NEVER use calculated formulas (no `*`, `+`, `=`, `^`).
- Maintain zero new modifications to root carrier files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`).
- Run verification commands:
  - `python -m pytest apex-meta/informatics/tests/ -q` (must pass 100%).
  - `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` (must report 0 errors).

## Completion
Document all findings in `handoff.md` in your working directory and notify the orchestrator via `send_message` to Recipient `a1918f04-9801-41c9-a8a4-6cebbbfab6ed`.

## 2026-10-22T12:51:35Z
You are assigned to Milestone 4: Author the 5 Plane 4 Infrastructure Module Audits.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_orch4_m4_1
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\worker_orch4_m4_1\DISPATCH.md
Read the authoritative user request at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically Section ## 2026-10-22T11:10:20Z, R2).
Read PROJECT.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md
Examine the comprehensive Survey 2 extraction at: c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2\survey_report.md
Examine the 5 canonical Plane 4 source modules in: c:\GitDev\apexai-os-meta\apex-meta\informatics\ (writing-profile.md, file-architecture.md, execution-modes.md, anti-drift-rules.md, governance-schemas.md).

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Write ownership: You own and write ONLY these 5 files in c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\:
1. audit-module-01-writing-profile.md
2. audit-module-02-file-architecture.md
3. audit-module-03-execution-modes.md
4. audit-module-04-anti-drift-rules.md
5. audit-module-05-governance-schemas.md

Every file must be a full-depth, genuine analytical document adhering to OKF v0.2 frontmatter and the 5-chapter structure detailed in spec_miner_survey_4_2/survey_report.md (Scope & Rule Inventory, Single-Ownership WP-23 Ledger, Redundancy & Stale Terminology Remediation, Cross-Traceability Matrix, Failure Modes WP-25).
Ensure 100% of relative markdown links resolve to real files on disk.
Run verification commands: python -m pytest apex-meta/informatics/tests/ -q and python apex-meta/scripts/okf_validator.py --target apex-meta/informatics.
Document all results in c:\GitDev\apexai-os-meta\.agents\teamwork\worker_orch4_m4_1\handoff.md and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.

