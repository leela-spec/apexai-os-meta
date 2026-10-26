# Task Assignment: Survey 2 — Plane 4 Infrastructure Modules Audit Survey

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- 5 Plane 4 Infrastructure Modules in `apex-meta/informatics/`:
  - `writing-profile.md` (`WP-01`..`WP-25`)
  - `file-architecture.md` (`FA-01`..`FA-13`)
  - `execution-modes.md` (`EM-01`..`EM-12`)
  - `anti-drift-rules.md` (`AD-01`..`AD-26`)
  - `governance-schemas.md` (`GS-01`..`GS-17`)
- Single-Owner Rule Definition: `WP-23` in `writing-profile.md`
- Prototype Audit Target: Requirements under R2 of `ORIGINAL_REQUEST.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md` (Section `## 2026-10-22T11:10:20Z`).
2. Read the 5 canonical Plane 4 modules in `apex-meta/informatics/`.
3. For each module:
   - Enumerate all defined rules and their semantic scope.
   - Audit Single-Ownership discipline (`WP-23`): verify that each rule has one canonical definition module and other modules only reference it without redefining or conflicting.
   - Identify stale terms, redundant phrasing, or candidate simplifications.
   - Establish cross-traceability matrix to `<apex_contract v="1.0">` (the 22 tags) and `16-candidate-3A-ultra.md`.
4. Synthesize recommendations for authoring the 5 audit files:
   - `audit-module-01-writing-profile.md`
   - `audit-module-02-file-architecture.md`
   - `audit-module-03-execution-modes.md`
   - `audit-module-04-anti-drift-rules.md`
   - `audit-module-05-governance-schemas.md`
5. Write your comprehensive report to `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2\survey_report.md` and create a self-contained `handoff.md`.
6. Send completion message back to Orchestrator (Conversation ID: a1918f04-9801-41c9-a8a4-6cebbbfab6ed).

## 2026-10-22T11:15:48Z
You are assigned to Survey Task 2: Plane 4 Infrastructure Modules Audit Survey.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2\DISPATCH.md
Read the authoritative user request at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically Section ## 2026-10-22T11:10:20Z).

Your role is a read-only specification investigator:
1. Examine the 5 canonical Plane 4 modules in apex-meta/informatics/: writing-profile.md (WP-01..WP-25), file-architecture.md (FA-01..FA-13), execution-modes.md (EM-01..EM-12), anti-drift-rules.md (AD-01..AD-26), governance-schemas.md (GS-01..GS-17).
2. Audit single-ownership discipline (WP-23), find redundancies/stale terms, and map cross-traceability to 13-candidate-3A-xml.md and 16-candidate-3A-ultra.md.
3. Detail recommendations for authoring the 5 audit-module files.
4. Write your report to c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2\survey_report.md and create a self-contained handoff.md.
5. Notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
