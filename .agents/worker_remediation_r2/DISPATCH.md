## 2026-09-22T10:29:00Z
You are worker_remediation_r2, a specialized remediation and implementation worker.
Your working directory is: C:\GitDev\apexai-os-meta\.agents\worker_remediation_r2
The authoritative user request is in: C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md (section ## 2026-09-22T10:15:42Z). Read this file first.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Context:
Challenger 1 conducted adversarial stress-testing and issued a REQUEST_CHANGES verdict with 4 concrete remediation requirements documented in:
- C:\GitDev\apexai-os-meta\.agents\challenger_1\handoff.md
- C:\GitDev\apexai-os-meta\.agents\challenger_1\challenge_report.md

Your Assigned Remediation Pack:
1. Remediate `ki-basis/scripts/hermes_telegram_intake.py`:
   - Remove lines 42 and 48 (`http://127.0.0.1:8010` and `http://127.0.0.1:8082`).
   - Replace with community-scoped fallback (`os.environ.get("COMMUNITY_PAPERLESS_URL", "http://127.0.0.1:9010")` and `os.environ.get("COMMUNITY_OPENPROJECT_URL", "http://127.0.0.1:9082")`) so community intake NEVER falls back to private ports.
2. Remediate root `ki-basis/compose.yaml`:
   - Add `external: true` to the `volumes:` block for all 10 volumes so that running `docker compose down -v` on root compose.yaml is immunized against data destruction.
3. Update `ki-basis/docs/OPERATOR_RUNBOOKS_AND_TEMPLATES.md`:
   - Add dedicated Nginx `default.conf` templates for `lika-community` (linking only to community ports 908x) and `private-business` (linking only to private ports 808x), preventing cross-tenant information disclosure on the edge proxy.
   - Harden `start.ps1` in both runbooks to poll actual service health (e.g. Paperless/OpenProject or `docker compose ps`) rather than just static Nginx `/healthz`.
4. Update `ki-basis/docs/WORKSPACE_ISOLATION_ARCHITECTURE.md`:
   - Verify all claims match live code exactly.
5. Re-run and update test suites:
   - Run `python ki-basis/scripts/verify_dual_isolation.py`.
   - Update `ki-basis/tests/test_adversarial_isolation.py` and `ki-basis/tests/test_deliverables_stress.py` to assert that fallback ports are community-scoped (:9010/:9082) or fail-closed (not :8010/:8082). Run pytest to verify all tests pass 100%.

Write a detailed handoff report in C:\GitDev\apexai-os-meta\.agents\worker_remediation_r2\handoff.md documenting all changes made and test execution results.
Send a message back to parent orchestrator when finished.
