# Task Assignment: Survey 3 - Codebase Environment, Validator & Conformance Constraints

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_3`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md`
- Validator script: `c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py`
- Target directory: `c:\GitDev\apexai-os-meta\apex-meta\informatics`
- Existing scripts, test fixtures, or schema definitions in `c:\GitDev\apexai-os-meta\apex-meta\`

## Objectives
1. Read `ORIGINAL_REQUEST.md`.
2. Investigate `apex-meta/scripts/okf_validator.py`:
   - What are the exact checks performed? (OKF Errors vs. APEX_PROFILE Errors)
   - What frontmatter schema / YAML fields are required?
   - What line length, markdown heading, or structure rules are checked?
   - How does it validate files in `apex-meta/informatics`?
   - Can the validator script be executed directly? Test running it on existing files if any.
3. Inspect `apex-meta/informatics/`:
   - What currently exists in `apex-meta/informatics/`? Are there legacy files (`index.md`, `standard.md`, etc.)?
   - Check their structure, issues, or conformance.
4. Output a comprehensive report and handoff to `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_3\survey_report.md` and `handoff.md`.
5. Send completion message back to Orchestrator (Conversation ID: b50b8c99-9617-41ab-85e5-9b6924358d5a).


## 2026-10-19T16:15:22Z
Received from orchestrator (b50b8c99-9617-41ab-85e5-9b6924358d5a):
You are assigned to Survey Task 3.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_3
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_3\DISPATCH.md
Read the authoritative user request at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md

Your role is a read-only explorer. Probing:
- Validator script: c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py
- Target directory: c:\GitDev\apexai-os-meta\apex-meta\informatics\
- Existing schema or validation rules in apex-meta/

Analyze how okf_validator.py works (OKF Errors vs APEX_PROFILE Errors), what schema/YAML frontmatter is expected, how headings and line lengths are checked, test running the validator on existing files, and evaluate the current state of apex-meta/informatics/.

Write your findings to c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_3\survey_report.md and create a self-contained handoff.md.
When done, notify orchestrator via send_message to Recipient b50b8c99-9617-41ab-85e5-9b6924358d5a.
