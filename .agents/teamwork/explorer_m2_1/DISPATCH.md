# Dispatch for Explorer M2_1 (Token-Metric & Equivalence Investigator)

## Role
Token-Metric & Behavioral Equivalence Investigator

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_1`

## Parent
Orchestrator 3 (`c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_3`)

## Authoritative Instructions
Read `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically `## 2026-10-21T16:45:38Z`).

## Mission & Objectives (R2)
Independently verify `13-candidate-3A-xml.md`, `14-candidate-3B-hybrid.md`, and `03-BLUEPRINT-agents.md`:
1. Recompute exact line count, word count, character count, repo-estimator (`words * 1.3`), and `cl100k_base` BPE token count (via Python tiktoken or standard encoding script) from live file bytes.
2. Confirm or falsify the numbers reported in the Dossier (`00`–`06`).
3. Compare `3A` and `3B` rule-for-rule to verify 100% behavioral equivalence between the XML and Hybrid serializations.
4. Check `03-BLUEPRINT-agents.md` for:
   - Any remaining duplication between Layer 1 (`<apex_contract>`) and Layer 2 (repo-specific sections).
   - Any broken relative links or invalid path references.
   - Any formatting or schema defects.

## Output Requirements
Produce `analysis.md` and `handoff.md` in your working directory with full reproduction tables and command outputs.
Notify parent orchestrator via `send_message`.

## 2026-10-21T16:49:04Z
You are assigned as Explorer M2_1 (Token-Metric & Equivalence Investigator).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_1
Your task assignment is in: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_1\DISPATCH.md
Authoritative request is in: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically section ## 2026-10-21T16:45:38Z).
Your parent orchestrator conversation ID is: 736cd41c-7e37-43d2-b265-c5d4f71a370c

Focus on R2:
1. Recompute exact line, word, character, repo-estimator (words * 1.3), and cl100k_base BPE token counts for:
   - 13-candidate-3A-xml.md
   - 14-candidate-3B-hybrid.md
   - 03-BLUEPRINT-agents.md
   Confirm or falsify the metrics stated in FinalizationDossier/ (00, 02, 06, etc.).
2. Compare 13-candidate-3A-xml.md and 14-candidate-3B-hybrid.md rule-for-rule to verify 100% behavioral equivalence between XML and Hybrid formats.
3. Audit 03-BLUEPRINT-agents.md for Layer 1 vs Layer 2 duplication, broken links, or inconsistencies.
4. Write your findings and exact data to c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_1\analysis.md and handoff report to c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_1\handoff.md.
5. When finished, send a message to your parent (736cd41c-7e37-43d2-b265-c5d4f71a370c) with summary and report path.
