# Task Assignment: Reviewer 2 (Operations, Runbooks & Lifecycle)

## Identity
- Role: Operations & Runbook Reviewer
- Working Directory: C:\GitDev\apexai-os-meta\.agents\reviewer_2
- Parent Orchestrator: orchestrator_1 (ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38)

## Mandatory Inputs to Read First
- `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`
- `C:\GitDev\apexai-os-meta\.agents\PROJECT.md`
- `C:\GitDev\apexai-os-meta\.agents\worker_impl_1\changes.md`
- `C:\GitDev\apexai-os-meta\.agents\worker_impl_1\handoff.md`
- `C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_RUNBOOK.md`
- `C:\GitDev\apexai-os-meta\ki-basis\scripts\start-ki-basis.ps1`
- `C:\GitDev\apexai-os-meta\ki-basis\scripts\start-ki-basis.sh`
- `C:\GitDev\apexai-os-meta\ki-basis\scripts\stop-ki-basis.ps1`

## Mission & Evaluation Criteria
Perform an independent, objective, and adversarial review of the operational procedures and lifecycle tooling:
1. Check Migration Runbook:
   - Is the migration from single-instance to dual-instance complete, clear, and actionable without risk of data loss?
   - Are volume copy / pg_dump commands technically accurate?
2. Check Daily Operations Runbook:
   - Are startup, shutdown, restart, and health check procedures clearly specified for both instances?
   - Are commands provided for managing Private independently from Community?
3. Check Backup & Restore:
   - Are backup procedures defined for each isolated database and volume?
   - Are restore procedures verified?
4. Check Scripts:
   - Do `start-ki-basis.ps1` and `start-ki-basis.sh` correctly handle `-Instance private`, `-Instance community`, and `-Instance all`?
   - Are port numbers and URLs verified?
5. Run verification commands:
   - Test script syntax and verify arguments.

## Output
Write your review report to:
`C:\GitDev\apexai-os-meta\.agents\reviewer_2\review.md`
And write `handoff.md` with an explicit verdict: `APPROVE` or `REQUEST_CHANGES`. Send a message to orchestrator_1 when finished.

## 2026-09-07T08:43:11Z
You are reviewer_2. Your working directory is C:\GitDev\apexai-os-meta\.agents\reviewer_2.
Read your instructions in C:\GitDev\apexai-os-meta\.agents\reviewer_2\DISPATCH.md and the authoritative request in C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md.
Review the operational procedures, migration runbook, daily ops, backup/restore, and lifecycle scripts (start-ki-basis.ps1 / .sh).
Write your report to C:\GitDev\apexai-os-meta\.agents\reviewer_2\review.md and handoff.md with verdict APPROVE or REQUEST_CHANGES.
When finished, notify orchestrator_1 via send_message.
