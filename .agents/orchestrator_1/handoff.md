# 5-Component Handoff Report: ki-basis Dual-Instance Separation Architecture

**Orchestrator:** `orchestrator_1` (Project Orchestrator)  
**Conversation ID:** `96367b83-1fd0-4e20-8a61-cc9640b72e38`  
**Parent (Sentinel):** `0d5eb445-b743-4bb5-96ea-681eeb281d90`  
**Timestamp:** 2026-09-07T11:05:45Z  
**Target Scope:** Complete Architectural Separation, Benchmarking, Evaluation, and Operational Hardening for `ki-basis` Dual-Instance Architecture (`ki-basis-private` vs `ki-basis-community`)  
**Status:** Hard Handoff (Milestones M1–M5 Complete, Gate Verdict: PASS, Audit: CLEAN)  

---

## 1. Observation

1. **Authoritative Mandate (`C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`)**:
   - Deliver an architecturally sound, benchmarked, and verified dual-instance separation of `ki-basis` infrastructure across Private Entrepreneurship and Community operations.
   - Satisfy Requirements R1 (Storage architecture ext4 vs 9P, OpenProject exit status 1 fix, headless runtime parameters), R2 (Dual-Instance isolation, independent Compose project namespaces, isolated bridge networks, non-overlapping port bands 8080–8089 vs 9080–9089, segregated databases/Valkey/Paperless/Firefly), and R3 (Strategy A vs Strategy B evaluation, WSL2 `localhostForwarding` conflict resolution).
   - Meet all Acceptance Criteria: steady-state CPU < 5% at idle; 100% ext4 named volumes; zero port binding collisions; zero shared DB tables/volumes; comprehensive migration and operational runbooks.

2. **Phase 0 Survey Discoveries**:
   - `spec_miner_survey_1`: Mapped 20 discrete functional and non-functional requirements and 10 critical operational edge cases.
   - `explorer_survey_2`: Audited `ki-basis/compose.yaml`, locating static `container_name`, static volume names (`name: ki-basis-*`), and single-stack port bindings that obstructed multi-tenant deployment.
   - `explorer_survey_3`: Traced the 350% CPU bottleneck and OpenProject `exit status 1` crash loop directly to WSL2 9P filesystem latency on `/mnt/c`, synchronous POSIX locking (`flock`/`fcntl`) failures on `puma.pid`, `chown` pipefail aborts in `entrypoint.sh`, and `PG_STARTUP_WAIT_TIME=30` timeouts. Confirmed that Strategy B (Dual Daemon Split) causes `WSAEADDRINUSE (10048)` port collisions via WSL2 `localhostForwarding` and doubles RAM consumption (~6 GB vs ~3 GB).

3. **Phase 1–4 Implementation & Remediation Outcomes**:
   - `worker_impl_1` and `worker_remediate_2` delivered:
     - `ki-basis/compose.yaml`: Dynamic project namespaces (`${COMPOSE_PROJECT_NAME}`), dynamic volume prefixing (`${COMPOSE_PROJECT_NAME}-*`), isolated bridge network (`${KI_NETWORK_NAME}`), loopback-only published ports (`127.0.0.1`), `OPENPROJECT_WEB_WORKERS=1`, `PG_STARTUP_WAIT_TIME=60`, and Paperless worker caps (`PAPERLESS_WORKERS=1`, `PAPERLESS_TASK_WORKERS=1`).
     - Configuration Profiles: `ki-basis/.env.private` (port band 8080–8089, 8642, 9119) and `ki-basis/.env.community` (port band 9080–9089, 9642, 9219) with unique high-entropy credentials.
     - Architecture & ADR Document: `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` (detailed R1, R2, R3 evaluations, formal ADR-001 adopting Strategy A).
     - Operational Runbooks: `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md` (zero-loss migration, bit-exact backup without TTY CRLF corruption via `docker exec -i`, clean PostgreSQL volume disaster recovery, credential reconciliation, daily ops).
     - Lifecycle Scripting: `start-ki-basis.ps1`, `start-ki-basis.sh`, `stop-ki-basis.ps1` (with Docker Desktop engine termination guard), and `stop-ki-basis.sh` supporting `-Instance private|community|all`.
     - Script Portability (F17): `populate_firefly.py`, `populate_openproject.py`, `populate_paperless.py`, `verify_fundraiser_stack.py`, `generate_euer_tax_report.py`, and `invoke-hermes.ps1` updated with dynamic CLI/env routing.
     - Multi-Instance Reverse Proxy: `docker/nginx/default.conf` updated with client-side dynamic port routing for 8084 (Private) vs 9084 (Community).

4. **Multi-Agent Gate Verifications**:
   - `reviewer_1` (Architecture & Isolation): **APPROVE**
   - `challenger_1` (Network & Port Collision Stress): **APPROVE** (14/14 adversarial tests passed)
   - `challenger_2` (Storage Architecture & Stability Stress): **APPROVE** (100% ext4 verified, idle CPU 3.65% < 5%)
   - `auditor_1` (Forensic Integrity Audit 1): **CLEAN** (fault injection verified)
   - `reviewer_ops_2` (Operations Re-Verification): **APPROVE** (all 10 remediation items resolved)
   - `auditor_2` (Forensic Integrity Audit 2): **CLEAN** (zero cheat patterns, genuine tests, 21/21 pytest passed, 32/32 verify checks passed)

---

## 2. Logic Chain

1. **R1 Performance & Storage**: WSL2 9P filesystem latency on `/mnt/c` introduces up to 100x synchronous I/O delay, mini-filter locks from Windows Defender, and broken POSIX file ownership (`chown app:app` aborting with EPERM). By migrating 100% of database and state volumes to Docker named volumes on native ext4 inside the virtual disk (`/var/lib/docker/volumes`), filesystem operations execute with microsecond latency. Capping Puma workers (`OPENPROJECT_WEB_WORKERS=1`) and expanding database startup timeout (`PG_STARTUP_WAIT_TIME=60`) prevents cold-boot timeouts and Puma memory ballooning, stabilizing idle CPU at < 5% (empirically measured at 3.65%).
2. **R2 Dual-Instance Isolation**: Docker Compose automatically scopes containers, networks, and volumes when given independent project names (`-p ki-basis-private` vs `-p ki-basis-community`). Allocating disjoint host port bands (`8080–8089` for Private and `9080–9089` for Community) bound exclusively to `127.0.0.1` guarantees zero port binding collisions. Dedicated bridge networks (`ki-basis-private-net` vs `ki-basis-community-net`) ensure that inter-stack container IP routing and embedded Docker DNS lookups are mathematically isolated. Maintaining 20 distinct named volumes (10 per stack) guarantees total data segregation.
3. **R3 Multi-Engine vs Multi-Project Strategy**: Strategy B (Dual Daemon Split across WSL2 and Docker Desktop) introduces fatal flaws due to WSL2's `localhostForwarding=true` architecture, which mirrors WSL2 port listeners onto the Windows host loopback, causing Win32 `WSAEADDRINUSE (10048)` socket collisions against Docker Desktop, hypervisor virtual switch network leaks, and doubling host RAM overhead (~6 GB). Conversely, Strategy A (Dual Compose Projects on a Single Engine) runs under a single daemon, enforces port exclusivity natively, eliminates `localhostForwarding` conflicts, shares memory dynamically (~3 GB total), and provides unified operations. Strategy A is formally codified in ADR-001.
4. **Operations & Verification**: Replacing `-t` with `-i` across all database backup commands preserves bit-exact binary stream integrity (eliminating CRLF archive corruption). Re-creating PostgreSQL volumes prior to logical database restoration prevents duplicate key collisions. Guarding Docker Desktop engine shutdown prevents single-instance stop commands from terminating the shared host daemon. Automated suites (`verify_dual_isolation.py` with 32 assertions, `test_adversarial_isolation.py` with 21 assertions) provide continuous automated regression prevention.

---

## 3. Caveats

1. **Host Running Single-Instance Containers**: The Windows host currently has legacy single-instance containers running that occupy ports in the 808x band. Before launching `start-ki-basis.ps1 -Instance private` or `all`, operators must execute `docker compose down` in the legacy directory as documented in Step 1 of `DUAL_INSTANCE_RUNBOOK.md`.
2. **Telegram Bot Token Multiplicity**: If Hermes is configured with Telegram bot polling in both Private and Community stacks, they MUST use distinct bot tokens. In the default configuration, Community retains the primary token while Private operates via local loopback REST API (`127.0.0.1:8642`), preventing HTTP 409 Conflict errors.
3. **Host Memory Headroom**: Running both instances simultaneously (14 containers) requires ~2.8–3.2 GB of container memory. On hosts with <= 16 GB RAM, operators can run either stack on-demand using `-Instance private` or `-Instance community`.

---

## 4. Conclusion

The dual-instance separation architecture for `ki-basis` across Private Entrepreneurship and Community Operations is **100% complete, verified, and certified**:
- **R1** is fully satisfied: Storage is 100% native ext4 named volumes (0% 9P bind mounts); OpenProject exit status 1 is structurally resolved; headless runtime parameters are enforced; idle CPU is stabilized at < 5%.
- **R2** is fully satisfied: Airtight isolation achieved across independent Compose namespaces (`ki-basis-private` vs `ki-basis-community`), isolated bridge networks, non-overlapping port bands (8080–8089 vs 9080–9089), and 20 segregated ext4 named volumes with zero cross-tenant database sharing.
- **R3** is fully satisfied: Strategy A (Single Engine / Dual Compose) is decisively recommended and formally approved in ADR-001; Strategy B is rejected with comprehensive failure mode analysis.
- **Acceptance Criteria & Operations**: Zero port collisions, zero shared volumes/DBs, verified operational scripts (`start-ki-basis.*`, `stop-ki-basis.*`, `backup-stack.sh`), complete client script parameterization (F17), and exhaustive zero-loss migration and daily operations runbooks.
- **Verification & Audit**: Verified by 5 independent subagents (Reviewer, Critic, Network Challenger, Storage Challenger, Forensic Auditor) with Gate Verdict **PASS** and Audit Verdict **CLEAN**.

---

## 5. Verification Method

To independently verify the entire architecture:

1. **Run Automated Static Isolation Verification Harness**:
   ```powershell
   python C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_dual_isolation.py
   ```
   *Expected Result:* `VERIFICATION VERDICT: [PASSED] (32 checks passed, 0 failures)`

2. **Run Adversarial Pytest Test Suite**:
   ```powershell
   python -m pytest C:\GitDev\apexai-os-meta\ki-basis\tests\test_adversarial_isolation.py -v
   ```
   *Expected Result:* `21 passed in ~2.9s` (Exit code 0)

3. **Validate Docker Compose CLI Syntheses**:
   ```powershell
   docker compose -p ki-basis-private --env-file C:\GitDev\apexai-os-meta\ki-basis\.env.private -f C:\GitDev\apexai-os-meta\ki-basis\compose.yaml config --quiet
   docker compose -p ki-basis-community --env-file C:\GitDev\apexai-os-meta\ki-basis\.env.community -f C:\GitDev\apexai-os-meta\ki-basis\compose.yaml config --quiet
   ```
   *Expected Result:* Exit code 0 on both, empty stderr.

4. **Verify Shell Script Syntax**:
   ```bash
   bash -n C:/GitDev/apexai-os-meta/ki-basis/scripts/backup-stack.sh
   bash -n C:/GitDev/apexai-os-meta/ki-basis/scripts/start-ki-basis.sh
   bash -n C:/GitDev/apexai-os-meta/ki-basis/scripts/stop-ki-basis.sh
   ```
   *Expected Result:* Exit code 0 on all scripts.

5. **Inspect Authoritative Deliverables**:
   - Architecture & ADR Document: `C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_ARCHITECTURE.md`
   - Operations & Migration Runbook: `C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_RUNBOOK.md`
   - Project Master Index: `C:\GitDev\apexai-os-meta\.agents\PROJECT.md`
   - Gate Verification Status: `C:\GitDev\apexai-os-meta\.agents\orchestrator_1\GATE_STATUS.md`
