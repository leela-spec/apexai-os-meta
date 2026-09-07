# Progress — worker_remediate_2

**Last visited**: 2026-09-07T10:59:30Z
**Current status**: All 10 remediation tasks completed, verified, and documented.

## Task Breakdown
- [x] 1. Fix TTY CRLF corruption in DUAL_INSTANCE_RUNBOOK.md (remove -t, use -i only for pg_dump/pg_dumpall/tar)
- [x] 2. Fix Disaster Recovery in DUAL_INSTANCE_RUNBOOK.md (clean postgres volume first, add paperless-data and hermes-workspaces)
- [x] 3. Upgrade backup-stack.sh for dual-instance namespaces and use -i (no -t)
- [x] 4. Add PostgreSQL password synchronization step in migration runbook
- [x] 5. Fix stop-ki-basis.ps1 so stopping a single instance does NOT terminate Docker Desktop engine
- [x] 6. Create stop-ki-basis.sh
- [x] 7. Fix timeout handling in start-ki-basis.sh
- [x] 8. Fix nginx/default.conf dashboard links for multi-instance support
- [x] 9. Implement F17: parameterize client scripts (populate_firefly.py, populate_openproject.py, populate_paperless.py, verify_fundraiser_stack.py, generate_euer_tax_report.py, invoke-hermes.ps1) with env vars and CLI args
- [x] 10. Residual ki-basis/.env safety
- [x] 11. Verify with verify_dual_isolation.py (32/32 PASS) and test_adversarial_isolation.py (21/21 PASS)
- [x] 12. Write remediation_report.md and handoff.md
- [x] 13. Notify orchestrator_1 via send_message
