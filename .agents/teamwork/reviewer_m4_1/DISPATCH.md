# Task Assignment: Milestone 4 Reviewer 1 (Architecture & 5-Chapter Structure)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m4_1`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (see Section `## 2026-10-22T11:10:20Z`, specifically R2)
- Project Scope: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md`
- Worker Handoff: `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_orch4_m4_1\handoff.md`
- Target Deliverables in `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\`:
  1. `audit-module-01-writing-profile.md`
  2. `audit-module-02-file-architecture.md`
  3. `audit-module-03-execution-modes.md`
  4. `audit-module-04-anti-drift-rules.md`
  5. `audit-module-05-governance-schemas.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md` and `PROJECT.md`.
2. Inspect the 5 module audit files authored by `worker_orch4_m4_1`:
   - Verify that all 5 files strictly adhere to OKF v0.2 frontmatter (`type: Reference`, `status: current_truth`, unique durable IDs `V2-AUDIT-MODULE-01`..`05`).
   - Verify that each file implements the complete 5-chapter structure:
     - Chapter 1: Module Scope & Governed Rule Inventory
     - Chapter 2: Single-Ownership Verification Ledger (`WP-23`)
     - Chapter 3: Redundancy & Stale Terminology Remediation Plan
     - Chapter 4: Cross-Traceability Matrix to `<apex_contract v="1.0">` / `16-candidate-3A-ultra.md`
     - Chapter 5: Failure Modes & Not-To-Dos (`WP-25`) in terminal position.
3. Run verification commands:
   - `python -m pytest apex-meta/informatics/tests/ -q`
   - `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`
4. Formulate structured verdict (**APPROVE** or **REQUEST_CHANGES**).
5. Write detailed `handoff.md` in your working directory and notify the orchestrator via `send_message` to Recipient `a1918f04-9801-41c9-a8a4-6cebbbfab6ed`.

## 2026-10-22T13:09:13Z
You are Reviewer 1 for Milestone 4 (Plane 4 Infrastructure Module Audits).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m4_1
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m4_1\DISPATCH.md
Read ORIGINAL_REQUEST.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Inspect the 5 module audit files authored by worker_orch4_m4_1 in apex-meta/informatics/final/research/06-layered-rule-kb/: audit-module-01-writing-profile.md through audit-module-05-governance-schemas.md.
Verify OKF v0.2 frontmatter, 5-chapter structure in every file, and run verification commands: python -m pytest apex-meta/informatics/tests/ -q and python apex-meta/scripts/okf_validator.py --target apex-meta/informatics.
Write handoff.md with structured verdict (APPROVE or REQUEST_CHANGES) and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
