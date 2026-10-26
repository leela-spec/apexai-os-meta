# DISPATCH: spec_miner_m5_1

## Identity
- Role: Spec Miner (Candidate Specification & Delta Structure Analyst)
- Working directory: c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_m5_1

## Mandatory References
- Authoritative User Request: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
- Scope Document: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_5\SCOPE.md
- Baseline Candidate: c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md

## Objective
Analyze specifications for `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`:
1. Inspect `13-candidate-3A-xml.md` and any sibling candidates (e.g. 14, 15 if present) to understand structure:
   - Frontmatter requirements (if any, or markdown heading style)
   - Contract code block formatting
   - Metrics table format (lines, words, chars, repo tokens, cl100k_base BPE tokens)
   - Rule-by-rule delta table against `13-candidate-3A-xml.md` format
2. Determine how repo tokens and cl100k_base BPE tokens are measured in this project (check existing test suite or scripts in `apex-meta/scripts/` or `apex-meta/informatics/tests/`).
3. Document exact requirements and formatting rules for `16-candidate-3A-ultra.md` so the worker can author it perfectly.

Write your findings to `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_m5_1\handoff.md`.
Update `progress.md` in your working directory.
Send completion message to orchestrator parent when done.

## 2026-10-22T15:35:33Z
You are spec_miner_m5_1.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_m5_1
MANDATORY: Read c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md before starting work.
Also read your dispatch instructions at: c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_m5_1\DISPATCH.md
And scope at: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_5\SCOPE.md

Your task is to analyze candidate specifications for `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`:
1. Inspect `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md` and sibling candidates to determine exact structure: frontmatter, contract code block formatting, metrics table format, rule-by-rule delta table against 13-candidate-3A-xml.md.
2. Investigate how repo tokens and cl100k_base BPE tokens are computed in `apex-meta/informatics/tests/` or `apex-meta/scripts/`.
3. Provide precise requirements and templates for the worker to build 16-candidate-3A-ultra.md.
Write your findings to `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_m5_1\handoff.md`.
Update progress.md in your working directory.
When finished, send a message to your parent orchestrator with a summary and the path to your handoff.md.
