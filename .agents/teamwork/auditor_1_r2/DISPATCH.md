# Dispatch: Forensic Auditor (Iteration 2 Verification)

## Role
Forensic Integrity Auditor (Iteration 2)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_1_r2`

## Parent
Orchestrator 3 (`736cd41c-7e37-43d2-b265-c5d4f71a370c`)

## Authoritative Instructions
Read `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically `## 2026-10-21T16:45:38Z`).

## Mission & Scope
Perform rigorous forensic integrity audit on the Iteration 2 work products by Worker M4_2:
1. Verify that the edits in `13-candidate-3A-xml.md`, `01-decision-register.md`, `04-empirical-test-protocol.md`, and `FinalizationDossier/07-teamwork-independent-validation.md` are genuine, without hardcoded fakes or simulated test outputs.
2. Confirm that live root carriers (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) remain 100% unmutated by the iteration run (`git diff AGENTS.md CLAUDE.md GEMINI.md`).
3. Run live commands directly:
   - `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`
   - `python -m pytest apex-meta/informatics/tests/ -q`
4. Independently recompute token metrics for the modified Candidate 3A block.
5. Issue a binary verdict: `CLEAN` or `INTEGRITY VIOLATION`.
Notify parent orchestrator via `send_message`.

## 2026-10-21T17:32:01Z
[Message] timestamp=2026-10-21T17:32:01Z sender=736cd41c-7e37-43d2-b265-c5d4f71a370c priority=MESSAGE_PRIORITY_HIGH
You are assigned as Forensic Auditor (Iteration 2 Verification).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_1_r2
Your task assignment is in: c:\GitDev\apexai-os-meta\.agents\teamwork\auditor_1_r2\DISPATCH.md
Authoritative request is in: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically section ## 2026-10-21T16:45:38Z).
Your parent orchestrator conversation ID is: 736cd41c-7e37-43d2-b265-c5d4f71a370c

Forensic Verification Tasks:
1. Verify that Worker M4_2's edits in 13-candidate-3A-xml.md, 01-decision-register.md, 04-empirical-test-protocol.md, and FinalizationDossier/07-teamwork-independent-validation.md are authentic, genuine, and free of hardcoded fakes.
2. Verify git diff AGENTS.md CLAUDE.md GEMINI.md to ensure strictly zero live root carrier modifications.
3. Run live commands directly:
   - python apex-meta/scripts/okf_validator.py --target apex-meta/informatics
   - python -m pytest apex-meta/informatics/tests/ -q
4. Independently recompute token metrics for the modified Candidate 3A block.
5. Produce a forensic audit report and handoff.md in your working directory with a binary verdict: CLEAN or INTEGRITY VIOLATION.
6. Send a message to your parent orchestrator with your verdict, findings, and report path.
