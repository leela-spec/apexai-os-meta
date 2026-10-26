# DISPATCH: explorer_m5_2

## Identity
- Role: Explorer (Index Architect & Conformance Analyst)
- Working directory: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m5_2

## Mandatory References
- Authoritative User Request: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
- Scope Document: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_5\SCOPE.md
- Index Files:
  - `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\index.md`
  - `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\` directory
- Module Audits: `audit-module-01-writing-profile.md` through `audit-module-05-governance-schemas.md`

## Objective
Investigate requirements for index creation and linking:
1. Review all files in `apex-meta/informatics/final/research/06-layered-rule-kb/`:
   - 22 rule files (`rule-01-target.md` to `rule-22-pointers.md`)
   - 5 module audits (`audit-module-01-writing-profile.md` to `audit-module-05-governance-schemas.md`)
   - Any rollup / summary files
2. Design the complete content structure for `apex-meta/informatics/final/research/06-layered-rule-kb/index.md` following OKF standard and apex profile rules.
3. Review `apex-meta/informatics/final/index.md` and determine exact sections to update to reference `06-layered-rule-kb/index.md` and `candidates/16-candidate-3A-ultra.md`.
4. Check OKF validation requirements: examine `apex-meta/scripts/okf_validator.py` and frontmatter rules so newly generated/updated files pass OKF and profile validation with 0 errors.

Write your findings to `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m5_2\handoff.md`.
Update `progress.md` in your working directory.
Send completion message to orchestrator parent when done.


## 2026-10-22T15:35:33Z
From: 8ca44b74-952a-4cfd-afc5-fcda15705e76
Priority: MESSAGE_PRIORITY_HIGH

You are explorer_m5_2.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m5_2
MANDATORY: Read c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md before starting work.
Also read your dispatch instructions at: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m5_2\DISPATCH.md
And scope at: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_5\SCOPE.md

Your task is to investigate index requirements:
1. Examine `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\`: all 22 rule files, 5 module audits, and rollups. Design `index.md` for this directory following OKF and Apex profile standards.
2. Examine `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\index.md`. Determine exact sections to update to link `06-layered-rule-kb/index.md` and `candidates/16-candidate-3A-ultra.md`.
3. Check OKF validation requirements in `apex-meta/scripts/okf_validator.py` and test suite to ensure 0 errors.
Write your findings to `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m5_2\handoff.md`.
Update progress.md in your working directory.
When finished, send a message to your parent orchestrator with a summary and the path to your handoff.md.
