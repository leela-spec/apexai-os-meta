# Task Assignment: Reviewer Operations Re-Check (Iteration 2)

## Identity
- Role: Operations & Runbook Re-Verification Reviewer
- Working Directory: C:\GitDev\apexai-os-meta\.agents\reviewer_ops_2
- Parent Orchestrator: orchestrator_1 (ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38)

## Mandatory Inputs to Read First
- `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`
- `C:\GitDev\apexai-os-meta\.agents\PROJECT.md`
- `C:\GitDev\apexai-os-meta\.agents\reviewer_2\review.md`
- `C:\GitDev\apexai-os-meta\.agents\worker_remediate_2\remediation_report.md`
- `C:\GitDev\apexai-os-meta\.agents\worker_remediate_2\handoff.md`
- All remediated files:
  - `C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_RUNBOOK.md`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\backup-stack.sh`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\stop-ki-basis.ps1`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\stop-ki-basis.sh`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\start-ki-basis.sh`
  - `C:\GitDev\apexai-os-meta\ki-basis\docker\nginx\default.conf`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\populate_firefly.py`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\populate_openproject.py`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\populate_paperless.py`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_fundraiser_stack.py`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\generate_euer_tax_report.py`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\invoke-hermes.ps1`

## Mission & Evaluation Criteria
Independently verify whether all 9 defects identified in `reviewer_2/review.md` have been satisfactorily resolved:
1. Are all binary backup commands in `DUAL_INSTANCE_RUNBOOK.md` and `backup-stack.sh` free of `-t`?
2. Does the disaster recovery procedure initialize a clean/empty postgres volume and restore all 9 volumes?
3. Does `backup-stack.sh` support dual-instance namespaces without crashing?
4. Is database password synchronization clearly documented in the migration runbook?
5. Does `stop-ki-basis.ps1` avoid terminating Docker Desktop when stopping a single instance?
6. Does `stop-ki-basis.sh` work as a symmetric companion to `start-ki-basis.sh`?
7. Is timeout handling in `start-ki-basis.sh` dynamic?
8. Does Nginx route Community users on `:9084` to Community services rather than Private?
9. Are client scripts properly parameterized with CLI flags and environment variables (F17)?
10. Run verification commands:
   - `python ki-basis/scripts/verify_dual_isolation.py`
   - `pytest ki-basis/tests/test_adversarial_isolation.py -v`

## Output
Write your review report to:
`C:\GitDev\apexai-os-meta\.agents\reviewer_ops_2\review.md`
And write `handoff.md` with an explicit verdict: `APPROVE` or `REQUEST_CHANGES`. Send a message to orchestrator_1 when finished.

## 2026-09-07T08:59:45Z
You are reviewer_ops_2. Your working directory is C:\GitDev\apexai-os-meta\.agents\reviewer_ops_2.
Read your instructions in C:\GitDev\apexai-os-meta\.agents\reviewer_ops_2\DISPATCH.md and the authoritative request in C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md.
Review and verify all 10 remediation items from worker_remediate_2 in response to reviewer_2's defects:
- TTY CRLF elimination in DUAL_INSTANCE_RUNBOOK.md and backup-stack.sh
- Disaster recovery clean volume initialization and full volume list
- backup-stack.sh dual-instance namespace support
- Postgres password sync documentation in migration runbook
- Docker Desktop protection in stop-ki-basis.ps1
- Creation of stop-ki-basis.sh
- Timeout calculation in start-ki-basis.sh
- Nginx multi-instance dashboard routing
- F17 client script parameterization across populate_*.py, verify_*.py, generate_*.py, invoke-hermes.ps1
Run python ki-basis/scripts/verify_dual_isolation.py and pytest ki-basis/tests/test_adversarial_isolation.py -v.
Write your report to C:\GitDev\apexai-os-meta\.agents\reviewer_ops_2\review.md and handoff.md with verdict APPROVE or REQUEST_CHANGES.
When finished, notify orchestrator_1 via send_message.
