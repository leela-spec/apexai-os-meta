# Dispatch: Forensic Auditor (Integrity Forensics)

## Role
Forensic Integrity Auditor

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_1`

## Parent
Orchestrator 3 (`736cd41c-7e37-43d2-b265-c5d4f71a370c`)

## Authoritative Instructions
Read `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically `## 2026-10-21T16:45:38Z`).

## Mission & Scope
Perform rigorous, independent forensic integrity verification on all work products:
1. Verify that no test results, tokens, or outputs were fabricated, faked, or hardcoded.
2. Verify that `git diff AGENTS.md CLAUDE.md GEMINI.md` is strictly empty (zero live root carrier modifications).
3. Run live commands directly:
   - `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`
   - `python -m pytest apex-meta/informatics/tests/ -q`
   - Inspect test suite execution logs to confirm all 196 tests actually ran and executed genuine test logic.
4. Verify that `FinalizationDossier/07-teamwork-independent-validation.md` contains genuine, unmanipulated findings and adheres to OKF frontmatter and anti-drift rules.
5. Issue a binary verdict: `CLEAN` or `INTEGRITY VIOLATION`.
Notify parent orchestrator via `send_message`.

## 2026-10-21T17:12:57Z
From: 736cd41c-7e37-43d2-b265-c5d4f71a370c
Content:
You are assigned as Forensic Auditor (Integrity Forensics).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_1
Your task assignment is in: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_1\DISPATCH.md
Authoritative request is in: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically section ## 2026-10-21T16:45:38Z).
Your parent orchestrator conversation ID is: 736cd41c-7e37-43d2-b265-c5d4f71a370c

Forensic Verification Tasks:
1. Perform forensic integrity checks across all work products:
   - Check if any test outputs, token counts, or assertions were hardcoded, fabricated, or simulated.
   - Run python apex-meta/scripts/okf_validator.py --target apex-meta/informatics directly and verify genuine execution.
   - Run python -m pytest apex-meta/informatics/tests/ -q directly and inspect test output to verify that all 196 tests ran genuinely.
   - Run git diff AGENTS.md CLAUDE.md GEMINI.md to verify strictly zero live carrier modifications.
   - Verify that FinalizationDossier/07-teamwork-independent-validation.md is authentic, complete, and contains genuine analysis.
2. Produce a comprehensive forensic audit report and handoff.md in your working directory.
3. Issue a binary verdict: CLEAN or INTEGRITY VIOLATION.
4. Send a message to your parent orchestrator with your verdict, findings, and report path.
