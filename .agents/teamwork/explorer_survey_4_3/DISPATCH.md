# Task Assignment: Survey 3 — 3A-Ultra Compression Strategy, Conformance Gates & Index Architecture

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_4_3`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically Section `## 2026-10-22T11:10:20Z`)
- Layer 0 Master Contract: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md`
- Conformance Scripts & Tests:
  - Validator: `c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py`
  - Test Suite: `c:\GitDev\apexai-os-meta\apex-meta\informatics\tests/`
- Existing Index Files:
  - `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\index.md`
  - `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb/`

## Objectives
1. Read `ORIGINAL_REQUEST.md` (Section `## 2026-10-22T11:10:20Z`).
2. Analyze the requirements for `16-candidate-3A-ultra.md`:
   - Root tag `<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">`.
   - Exact 22 semantic tags.
   - Concatenating all 22 Option B surgical compressions.
   - Metric target: ~900–980 BPE tokens (target ~950 BPE, ~30% reduction from 1,350 BPE in 3A).
   - Delta table structure against `13-candidate-3A-xml.md`.
3. Check and analyze the validation toolchain:
   - What checks does `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` run? What are the common failure modes for OKF v0.2 and Apex Profile?
   - What tests exist in `apex-meta/informatics/tests/` (196 tests)? Are there tests checking candidate files, rule IDs, frontmatter, or contract tags?
4. Analyze requirements for `06-layered-rule-kb/index.md` and updates to `final/index.md`.
5. Identify any risks to Zero Live Mutation (preventing changes to root `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) and Research Bytes Preservation (no edits to `research/01-universal-instruction-research/` or `research/03-research-of-file-10/`).
6. Write your comprehensive report to `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_4_3\survey_report.md` and create a self-contained `handoff.md`.
7. Send completion message back to Orchestrator (Conversation ID: a1918f04-9801-41c9-a8a4-6cebbbfab6ed).


## 2026-10-22T11:15:48Z
You are assigned to Survey Task 3: 3A-Ultra Compression Strategy, Conformance Gates & Index Architecture.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_4_3
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_4_3\DISPATCH.md
Read the authoritative user request at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically Section ## 2026-10-22T11:10:20Z).

Your role is a read-only exploration agent:
1. Analyze requirements for 16-candidate-3A-ultra.md (~900-980 BPE tokens target, delta table vs 13-candidate-3A-xml.md).
2. Examine the validation toolchain: python apex-meta/scripts/okf_validator.py and python -m pytest apex-meta/informatics/tests/ -q (196 tests).
3. Analyze requirements for 06-layered-rule-kb/index.md and updates to final/index.md.
4. Verify safety constraints (Zero Live Mutation to AGENTS.md, CLAUDE.md, GEMINI.md; preserve existing research directories).
5. Write your report to c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_4_3\survey_report.md and create a self-contained handoff.md.
6. Notify orchestrator via send_message to Recipient a1918f04-9801-41c9-a8a4-6cebbbfab6ed.
