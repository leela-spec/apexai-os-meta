# Dispatch Assignment: Project Orchestrator (Generation 2)

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_2`

## Parent
- Conversation ID: `11548e6a-a920-403f-961e-9266012f5077` (Sentinel)
- Use this ID for all escalation, status reporting, and completion notifications via `send_message`.

## State & Predecessor Artifacts
Read the predecessor state and handoff at:
- Handoff: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\handoff.md`
- Predecessor Briefing: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\BRIEFING.md`
- Predecessor Progress: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\progress.md`
- Authoritative Request: `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md`
- Project Index & Architecture: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\PROJECT.md`
- Gate Status: `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_1\GATE_STATUS.md`
- E2E Test Suite Ready: `c:\GitDev\apexai-os-meta\TEST_READY.md`
- E2E Test Runner: `c:\GitDev\apexai-os-meta\apex-meta\informatics\tests\test_informatics_e2e.py`
- Validator: `c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py`

## Immediate Mission
1. Initialize your `BRIEFING.md` and `progress.md` in your working directory `c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_2\`.
2. Start your recurring heartbeat cron via `schedule(CronExpression="*/10 * * * *")`.
3. Milestone 1 is DONE and verified with 0 errors.
4. Milestone 2 exploration is complete. Read the pre-verified templates in:
   - `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_1\exploration_report.md` (anti-drift-rules.md)
   - `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_2\exploration_report.md` (governance-schemas.md)
   - `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_3\exploration_report.md` (index.md & general-informatics-router.md)
5. Execute Milestone 2:
   - Spawn M2 Worker (`teamwork_preview_worker`) with exclusive write ownership to author these 4 files using the exploration templates.
   - Run `okf_validator.py` and `test_informatics_e2e.py` (all 146 tests must pass).
   - Spawn M2 gate agents (2 Reviewers, 2 Challengers, 1 Forensic Auditor) and record verdicts in `GATE_STATUS.md`.
6. Execute Milestone 3 (Final Acceptance & Adversarial Hardening):
   - Verify 100% E2E test pass across all 146 tests.
   - Run Tier 5 adversarial hardening and forensic audit.
   - Synthesize final evidence and report completion to Sentinel (`11548e6a-a920-403f-961e-9266012f5077`).
