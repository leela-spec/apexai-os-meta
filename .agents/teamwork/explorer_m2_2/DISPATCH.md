# Task Assignment: M2 Exploration 2 — Governance Schemas & Directive Ceilings Specification

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_2`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md`
- Project Architecture & Feature Inventory: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\PROJECT.md`
- Survey Reports:
  - `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_1\survey_report.md`
  - `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_3\survey_report.md`
- Patch Intent Schema: `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json`

## Objectives
1. Read `ORIGINAL_REQUEST.md` and `PROJECT.md`.
2. As a read-only explorer, investigate and produce detailed implementation strategies and exact structural templates for:
   - `apex-meta/informatics/governance-schemas.md`:
     - OKF v0.2 frontmatter schema specification (required keys, flat format, type declarations, unique durable IDs).
     - Patch Intent Schema specification (`patch_intent.v1`, AST block matching, safety thresholds).
     - Decision Matrix and Bake-off evaluation schemas.
     - Model-calibrated directive ceilings (50 for GPT-4o, 80 for Claude Reasoning, 100 for Gemini/o3).
     - Priority tier sorting (P0–P3) and raw 3-metric tags `[P<tier> | I<impact>/E<evidence>/R<risk>]` (uncomputed, scale 1–100, NO math formulas).
     - Top-loaded P0 invariants in first ~500 tokens.
     - Flat/inline YAML frontmatter (`type: Governance`, `id: GOV-SCHEMAS-v0.2`).
3. Do NOT modify or write any production files.
4. Write your findings and recommended file templates to `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_2\exploration_report.md` and `handoff.md`.
5. Notify orchestrator via `send_message` to Recipient `b50b8c99-9617-41ab-85e5-9b6924358d5a`.


## 2026-10-19T16:52:01Z
[Message] timestamp=2026-10-19T16:52:01Z sender=b50b8c99-9617-41ab-85e5-9b6924358d5a priority=MESSAGE_PRIORITY_HIGH content=You are assigned to M2 Exploration Task 2: Governance Schemas & Directive Ceilings Specification.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_2
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_2\DISPATCH.md
Read the authoritative user request at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Read the project architecture at: c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\PROJECT.md

Investigate and design complete implementation strategies and exact structural templates for:
- governance-schemas.md (OKF v0.2 frontmatter schemas, patch_intent.v1 AST schema, Decision Matrix schemas, model directive ceilings; P0-P3 sorting, raw uncomputed [P<tier> | I/E/R] tags, top-loaded P0 invariants).
Do NOT modify production files. Write exploration_report.md and handoff.md.
When done, notify orchestrator via send_message to Recipient b50b8c99-9617-41ab-85e5-9b6924358d5a.
