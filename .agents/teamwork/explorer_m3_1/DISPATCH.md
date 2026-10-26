# Dispatch for Explorer M3_1 (Traceability & Cross-Dependency Investigator)

## Role
Traceability & Cross-Dependency Investigator

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m3_1`

## Parent
Orchestrator 3 (`c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_3`)

## Authoritative Instructions
Read `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically `## 2026-10-21T16:45:38Z`).

## Mission & Objectives (R3)
Audit every clause in `<apex_contract v="1.0">` against the canonical Plane 4 library files:
- Canonical library files: `writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`, `index.md`, `general-informatics-router.md`, `log.md`.
- Verify that every rule in `<apex_contract v="1.0">` is backed by its claimed canonical rule ID (`WP-xx`, `FA-xx`, `EM-xx`, `AD-xx`, `GS-xx`) without contradiction, stale `v0.3`/`v0.4` tag names, or single-owner violations (`WP-23`).
- Inspect `04-empirical-test-protocol.md`, `01-decision-register.md`, and `11-instruction-surface-architecture.md` for any lingering cross-file inconsistencies or broken references.
- Check compliance with the existing pytest suite `apex-meta/informatics/tests/` and validator `apex-meta/scripts/okf_validator.py`.

## Output Requirements
Produce `analysis.md` and `handoff.md` in your working directory with full traceability matrices and discrepancy logs.
Notify parent orchestrator via `send_message`.


## 2026-10-21T16:49:04Z
From: 736cd41c-7e37-43d2-b265-c5d4f71a370c (parent)
Priority: MESSAGE_PRIORITY_HIGH
Content:
You are assigned as Explorer M3_1 (Traceability & Cross-Dependency Investigator).
Your working directory is: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m3_1
Your task assignment is in: c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m3_1\DISPATCH.md
Authoritative request is in: c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md (specifically section ## 2026-10-21T16:45:38Z).
Your parent orchestrator conversation ID is: 736cd41c-7e37-43d2-b265-c5d4f71a370c

Focus on R3:
1. Audit every clause in <apex_contract v="1.0"> against canonical Plane 4 library files:
   - writing-profile.md
   - file-architecture.md
   - execution-modes.md
   - anti-drift-rules.md
   - governance-schemas.md
   - index.md
   - general-informatics-router.md
   - log.md
2. Verify that every rule is backed by its claimed canonical rule ID (WP-xx, FA-xx, EM-xx, AD-xx, GS-xx) without contradiction, stale v0.3/v0.4 tags, or single-owner violations (WP-23).
3. Inspect 04-empirical-test-protocol.md, 01-decision-register.md, and 11-instruction-surface-architecture.md for cross-file inconsistencies.
4. Verify current status of okf_validator.py and pytest test suite.
5. Write your findings to c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m3_1\analysis.md and handoff report to c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m3_1\handoff.md.
6. When finished, send a message to your parent (736cd41c-7e37-43d2-b265-c5d4f71a370c) with summary and report path.
