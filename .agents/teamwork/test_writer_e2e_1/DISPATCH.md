# Task Assignment: E2E Test Suite Creation (Tiers 1–4)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\test_writer_e2e_1`

## Inputs
- Authoritative User Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md`
- Project Architecture & Feature Inventory: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\PROJECT.md`
- E2E Test Infrastructure Design: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\TEST_INFRA.md`
- Validator Script: `c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py`
- Survey Reports:
  - `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_1\survey_report.md`
  - `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_2\survey_report.md`
  - `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_3\survey_report.md`

## Objectives
1. Read `ORIGINAL_REQUEST.md`, `PROJECT.md`, and `TEST_INFRA.md`.
2. Design and implement an automated, opaque-box E2E test runner at `apex-meta/informatics/tests/test_informatics_e2e.py` without modifying any production implementation files.
3. The test suite must implement the 4-tier methodology:
   - **Tier 1 (Feature Coverage, >=5 per feature)**: Verify OKF frontmatter parsing, Significance & Ranking tag syntax `[P<tier> | I<impact>/E<evidence>/R<risk>]`, uncomputed raw estimates (scale 1–100, NO math formulas), top-loaded primacy (P0 rules within first ~500 tokens), STE word limits (~20 words procedural, ~25 words descriptive), heading depth <= 3, router XML IF-tags, zero eager `@path` imports.
   - **Tier 2 (Boundary & Corner Cases, >=5 per feature)**: Missing colons in YAML lines, empty files, malformed tags, negative/overflow metric values, deeply nested headers, long sentences, missing OKF version.
   - **Tier 3 (Cross-Feature Combinations, pairwise coverage)**: Router IF-gating with writing-profile isolation; file-architecture with okf_validator; execution-modes with patch intent schema; anti-drift with operator challenge.
   - **Tier 4 (Real-World Application Scenarios, >=5 scenarios)**:
     1. Pure writing task simulation (context isolation: agent loads only `writing-profile.md`).
     2. Q&A Game Decision Matrix formulation (structured options with raw I/E/R scores and one-line rejection notes).
     3. Exact-Match Patch execution simulation (verbatim whitespace, rollback safety).
     4. Two-strike subsystem drift recovery simulation.
     5. Full `okf_validator.py` deterministic verification producing 0 OKF and 0 APEX errors.
4. Execute the test runner (it should cleanly run and report which files exist/pass or what is pending).
5. Produce `TEST_READY.md` at `c:\GitDev\apexai-os-meta\TEST_READY.md` (and copy to `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\TEST_READY.md`).
6. Write a comprehensive report to `test_suite_report.md` and `handoff.md`.
7. Notify orchestrator via `send_message` to Recipient `b50b8c99-9617-41ab-85e5-9b6924358d5a`.


## 2026-10-19T16:27:14Z
You are assigned to the E2E Testing Track: E2E Test Suite Creation.
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\test_writer_e2e_1
Read your assignment at: c:\GitDev\apexai-os-meta\.agents\teamwork\test_writer_e2e_1\DISPATCH.md
Read the authoritative user request at: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md
Read the project architecture and test infra at:
- c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\PROJECT.md
- c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\TEST_INFRA.md

Your role is a test writer. Implement the automated opaque-box E2E test runner at:
c:\GitDev\apexai-os-meta\apex-meta\informatics\tests\test_informatics_e2e.py
Covering Tiers 1–4 (>=140 tests/assertions) per TEST_INFRA.md.
Do NOT modify production implementation files in apex-meta/informatics/.
Execute the tests via Python to verify test harness runs cleanly.
Produce TEST_READY.md at c:\GitDev\apexai-os-meta\TEST_READY.md (and in your working directory).
Write a comprehensive report to test_suite_report.md and create a self-contained handoff.md.
When done, notify orchestrator via send_message to Recipient b50b8c99-9617-41ab-85e5-9b6924358d5a.
