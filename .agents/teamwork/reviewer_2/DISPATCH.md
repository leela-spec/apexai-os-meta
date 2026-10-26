# Dispatch: Reviewer 2 (Traceability & Completeness Reviewer)

## Role
Traceability & Report Completeness Reviewer

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_2`

## Parent
Orchestrator 3 (`736cd41c-7e37-43d2-b265-c5d4f71a370c`)

## Authoritative Instructions
Read `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically `## 2026-10-21T16:45:38Z`).

## Mission & Scope
Review `07-teamwork-independent-validation.md` and related artifacts for Requirements R3 and R4:
1. Bidirectional traceability between `<apex_contract v="1.0">` and Plane 4 library files (WP, FA, EM, AD, GS).
2. Verification of all surgical remediations applied by Worker M4_1 (Candidate 3A §3 provenance table, AD-26/AD-22 corrections, Dossier 00 token sync, Dossier 06 phantom tag purge, index.md linking).
3. Conformance with standard `[P<tier> | I/E/R]` tags (no computed formulas), structured Q&A decision matrices, and file-by-file PASS/WARN/FAIL verdicts.
4. Run deterministic validation commands:
   - `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`
   - `python -m pytest apex-meta/informatics/tests/ -q`
   - `git diff AGENTS.md CLAUDE.md GEMINI.md`
5. Issue an explicit verdict: `APPROVE` or `REQUEST_CHANGES` in your `handoff.md`.
Notify parent orchestrator via `send_message`.

## 2026-10-21T17:12:57Z
You are assigned as Reviewer 2 (Traceability & Completeness Reviewer).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_2
Your task assignment is in: c:\GitDev\apexai-os-meta\.agents\teamwork\reviewer_2\DISPATCH.md
Authoritative request is in: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically section ## 2026-10-21T16:45:38Z).
Your parent orchestrator conversation ID is: 736cd41c-7e37-43d2-b265-c5d4f71a370c

Focus on R3 and R4:
1. Review FinalizationDossier/07-teamwork-independent-validation.md and related files for R3 (Bidirectional traceability between contract clauses and Plane 4 library) and R4 (Report completeness, structured Q&A decision matrices, [P | I/E/R] tags, surgical remediations).
2. Check that FinalizationDossier/index.md properly links 07.
3. Verify surgical remediations in 13-candidate-3A-xml.md, 12-status-index.md, Dossier 00, Dossier 06, v2 index.md.
4. Run validation commands:
   - python apex-meta/scripts/okf_validator.py --target apex-meta/informatics
   - python -m pytest apex-meta/informatics/tests/ -q
   - git diff AGENTS.md CLAUDE.md GEMINI.md
5. Write your review to review.md and handoff.md in your working directory. Explicitly include your verdict: APPROVE or REQUEST_CHANGES.
6. Send a message to your parent orchestrator with your verdict, report summary, and path.
