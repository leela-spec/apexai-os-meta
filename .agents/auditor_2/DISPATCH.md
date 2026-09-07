# Task Assignment: Forensic Auditor (Iteration 2 Remediation Audit)

## Identity
- Role: Forensic Integrity Auditor
- Working Directory: C:\GitDev\apexai-os-meta\.agents\auditor_2
- Parent Orchestrator: orchestrator_1 (ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38)

## Mandatory Inputs to Read First
- `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`
- `C:\GitDev\apexai-os-meta\.agents\PROJECT.md`
- `C:\GitDev\apexai-os-meta\.agents\worker_remediate_2\remediation_report.md`
- `C:\GitDev\apexai-os-meta\.agents\worker_remediate_2\handoff.md`
- All files touched by worker_remediate_2:
  - `C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_RUNBOOK.md`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\backup-stack.sh`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\stop-ki-basis.ps1`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\stop-ki-basis.sh`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\start-ki-basis.sh`
  - `C:\GitDev\apexai-os-meta\ki-basis\docker\nginx\default.conf`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\populate_*.py`
  - `C:\GitDev\apexai-os-meta\ki-basis\tests\test_adversarial_isolation.py`

## Forensic Audit Protocol
Perform an uncompromising forensic audit on the remediation:
1. Static Analysis:
   - Check if changes are authentic and genuinely implement the requested functionality without cheating or shortcuts.
   - Verify that test assertions in `test_adversarial_isolation.py` are real and robust.
2. Independent Execution:
   - Run `python ki-basis/scripts/verify_dual_isolation.py`
   - Run `pytest ki-basis/tests/test_adversarial_isolation.py -v`
   - Verify zero errors, exit code 0.
3. Binary Verdict:
   - `CLEAN` or `INTEGRITY VIOLATION`.

## Output
Write your audit findings to:
`C:\GitDev\apexai-os-meta\.agents\auditor_2\audit_report.md`
And write `handoff.md` with your verdict. Send a message to orchestrator_1 when finished.

## 2026-09-07T08:59:45Z
You are auditor_2. Your working directory is C:\GitDev\apexai-os-meta\.agents\auditor_2.
Read your instructions in C:\GitDev\apexai-os-meta\.agents\auditor_2\DISPATCH.md and the authoritative request in C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md.
Perform a forensic integrity audit on all changes made by worker_remediate_2 across runbooks, scripts, client tooling, and tests.
Check for cheating, facades, dummy stubs, or bypassed validations.
Run python ki-basis/scripts/verify_dual_isolation.py and pytest ki-basis/tests/test_adversarial_isolation.py -v independently.
Write your audit report to C:\GitDev\apexai-os-meta\.agents\auditor_2\audit_report.md and handoff.md with verdict CLEAN or INTEGRITY VIOLATION.
When finished, notify orchestrator_1 via send_message.
