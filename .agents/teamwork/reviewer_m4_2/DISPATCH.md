# Task Assignment: Milestone 4 Reviewer 2 (Single-Ownership & Provenance)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m4_2`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (see Section `## 2026-10-22T11:10:20Z`, specifically R2)
- Project Scope: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_4\PROJECT.md`
- Survey Blueprint: `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2\survey_report.md`
- Worker Handoff: `c:\GitDev\apexai-os-meta\.agents\teamwork\worker_orch4_m4_1\handoff.md`
- Target Deliverables in `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\`:
  `audit-module-01-writing-profile.md` through `audit-module-05-governance-schemas.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md` and `PROJECT.md`.
2. Inspect Single-Ownership Discipline (`WP-23`):
   - Verify that across all 5 audit files, each of the 97 governed rules has exactly one canonical definition module.
   - Verify that cross-module references only cite canonical rules and do not duplicate schemas or full rule tables.
   - Verify handling of retired rules (`GS-16`, `GS-18`, `GS-19`) per `WP-15`.
3. Inspect Cross-Traceability Matrices (Chapter 4):
   - Verify mapping against the 22 contract clauses in `<apex_contract v="1.0">` (`13-candidate-3A-xml.md`) and the upcoming `16-candidate-3A-ultra.md`.
4. Inspect Chapter 5 Failure Modes & Not-To-Dos (`WP-25`) in terminal position.
5. Run test suite: `python -m pytest apex-meta/informatics/tests/ -q`.
6. Formulate structured verdict (**APPROVE** or **REQUEST_CHANGES**).
7. Write `handoff.md` and notify orchestrator via `send_message` to Recipient `a1918f04-9801-41c9-a8a4-6cebbbfab6ed`.


## 2026-10-22T13:09:13Z
You are Reviewer 2 for Milestone 4 (Plane 4 Infrastructure Module Audits).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m4_2
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_m4_2\DISPATCH.md
Read ORIGINAL_REQUEST.md at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Inspect the 5 module audit files in apex-meta/informatics/final/research/06-layered-rule-kb/: audit-module-01 through audit-module-05.
Verify Single-Ownership Discipline (WP-23), cross-traceability to <apex_contract v="1.0"> and 16-candidate-3A-ultra.md, and terminal failure modes (WP-25) across all 5 files.
Run pytest suite: python -m pytest apex-meta/informatics/tests/ -q.
Write handoff.md with structured verdict (APPROVE or REQUEST_CHANGES) and notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
