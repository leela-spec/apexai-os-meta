# Task Assignment: M2 Exploration 3 — Consolidated General Router Design

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_3`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md`
- Project Architecture & Feature Inventory: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\PROJECT.md`
- Pilot Contract & Survey Reports:
  - `c:\GitDev\apexai-os-meta\apex-meta\handoff\universal-ai-instruction-system\08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`
  - `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_1\survey_report.md`
- Validator Script: `c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py`

## Objectives
1. Read `ORIGINAL_REQUEST.md` and `PROJECT.md`.
2. As a read-only explorer, investigate and produce detailed implementation strategies and exact structural templates for:
   - `apex-meta/informatics/index.md` (and `general-informatics-router.md`):
     - Lean XML routing tags (`<informatics when="..." ref="..." deepen_when="...">`).
     - Approximate ceiling: ~100 lines and ~400 tokens.
     - Top-loaded P0 invariants in first ~500 tokens.
     - Strict JIT routing: zero eager `@path` imports; explicit instructions for tools to view referenced file only *when* action trigger matches.
     - Valid OKF v0.2 frontmatter: `okf_version: "0.2"` and resolvable relative links to all modules (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`).
     - Substance Over Ceremony Exception Authority.
     - P0–P3 priority sorting with raw 3-metric tags `[P<tier> | I/E/R]` (uncomputed, scale 1–100, NO math formulas).
3. Do NOT modify or write any production files.
4. Write your findings and recommended file templates to `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_3\exploration_report.md` and `handoff.md`.
5. Notify orchestrator via `send_message` to Recipient `b50b8c99-9617-41ab-85e5-9b6924358d5a`.


## 2026-10-19T16:52:01Z
Received assignment from b50b8c99-9617-41ab-85e5-9b6924358d5a:
You are assigned to M2 Exploration Task 3: Consolidated General Router Design.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_3
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_3\DISPATCH.md
Read the authoritative user request at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Read the project architecture at: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\PROJECT.md

Investigate and design complete implementation strategies and exact structural templates for:
- index.md & general-informatics-router.md (lean XML <informatics when="..." ref="..." deepen_when="..."> tags, ~100 lines / ~400 tokens ceiling, top-loaded P0 invariants, zero eager @path imports, okf_version: "0.2", link integrity; P0-P3 sorting, raw uncomputed [P<tier> | I/E/R] tags).
Do NOT modify production files. Write exploration_report.md and handoff.md.
When done, notify orchestrator via send_message to Recipient b50b8c99-9617-41ab-85e5-9b6924358d5a.
