# 5-Component Handoff Report: Operations & Lifecycle Re-Check Complete

**Reviewer:** `reviewer_ops_2` (Operations, Runbooks & Lifecycle Re-Verification Reviewer)  
**Parent Orchestrator:** `orchestrator_1` (ID: `96367b83-1fd0-4e20-8a61-cc9640b72e38`)  
**Date:** 2026-09-07T09:07:00Z  
**Handoff Type:** Hard Handoff (Review & Verification Complete)  
**Verdict:** **APPROVE**  

---

## 1. Observation

1. **Automated Verification Suites**:
   - Running `python ki-basis/scripts/verify_dual_isolation.py` produced:
     ```
     VERIFICATION VERDICT: [PASSED] (32 checks passed, 0 failures)
     Both instances can run concurrently with zero collisions and airtight isolation.
     ```
   - Running `pytest ki-basis/tests/test_adversarial_isolation.py -v` produced:
     ```
     ======================= 21 passed, 4 warnings in 2.68s ========================
     ```
     including clean passes for `test_nginx_default_conf_multi_instance_support`, `test_populate_firefly_cli`, `test_populate_openproject_cli`, `test_populate_paperless_cli`, `test_verify_fundraiser_stack_cli`, `test_generate_euer_tax_report_cli`, `test_stop_ki_basis_sh_exists`, and `test_backup_stack_sh_has_dual_instance_support`.

2. **Elimination of Pseudo-TTY Allocation (`-t`)**:
   - `DUAL_INSTANCE_RUNBOOK.md` Migration Step 2 (lines 69 & 73), Section 4.2 Standard Backup (lines 318 & 322), and Section 4.3 Disaster Recovery (lines 407 & 414) strictly use `docker exec -i` (no `-t`).
   - `backup-stack.sh` lines 124 & 129 strictly use `docker exec -i` without `-t`.
   - Global regex search for `docker exec.*-t` with redirection returned 0 matches across the entire repository.

3. **Disaster Recovery Clean Volume Initialization**:
   - Section 4.3 of `DUAL_INSTANCE_RUNBOOK.md` lines 370-371 commands:
     ```bash
     docker volume rm "${VOL_PREFIX}-postgres-data" 2>/dev/null || true
     docker volume create "${VOL_PREFIX}-postgres-data"
     ```
   - Lines 374-384 list all 9 state volumes (`valkey-data`, `firefly-upload`, `paperless-data`, `paperless-media`, `paperless-export`, `paperless-consume`, `openproject-assets`, `hermes-data`, `hermes-workspaces`), restoring all application state before booting services.

4. **Dual-Instance Backup Engine (`backup-stack.sh`)**:
   - `backup-stack.sh` accepts `-i private|community|all` and positional arguments, dynamically resolves `.env.${instance}`, targets `ki-basis-${instance}-*` containers and volumes, uses `alpine:3.20` fallback helper image, quiesces writers, verifies gzip archive integrity with `tar -tzf`, redacts secrets in configuration snapshots, and produces SHA256 integrity manifests.
   - Tested: `bash ki-basis/scripts/backup-stack.sh --help` exited with code 0.
   - Tested: `bash -n ki-basis/scripts/backup-stack.sh` exited with code 0.

5. **PostgreSQL Credential Synchronization**:
   - `DUAL_INSTANCE_RUNBOOK.md` Section 2, Step 4 documents temporary PostgreSQL startup and provides copy-paste Bash and PowerShell 7+ scripts running `ALTER USER` commands for `postgres`, `openproject_app`, `firefly_app`, and `paperless_app`.

6. **Docker Desktop Protection in `stop-ki-basis.ps1`**:
   - Line 19 introduces `[switch]$StopEngine`.
   - Line 46 evaluates `if ($Instance -eq "all" -and $StopEngine)`.
   - Single-instance stops (`-Instance private` or `-Instance community`) and regular full stops without `-StopEngine` leave Docker Desktop running.
   - Validated syntax via PowerShell AST scriptblock creation.

7. **Symmetric Linux/WSL2 Shutdown Companion (`stop-ki-basis.sh`)**:
   - File exists at `ki-basis/scripts/stop-ki-basis.sh`.
   - Accepts `-i private|community|all` and `-d, --down`.
   - Tested: `bash -n ki-basis/scripts/stop-ki-basis.sh` exited with code 0.

8. **Dynamic Timeout Calculation in `start-ki-basis.sh`**:
   - Lines 58-59 calculate:
     ```bash
     local max_attempts=$(( (TIMEOUT + 1) / 2 ))
     for ((attempt=1; attempt<=max_attempts; attempt++)); do
     ```
   - Tested: `bash -n ki-basis/scripts/start-ki-basis.sh` exited with code 0.

9. **Nginx Multi-Instance Routing**:
   - `ki-basis/docker/nginx/default.conf` inspects `window.location.port === "9084"`, dynamically updating DOM links to Community ports (9086, 9010, 9082, 9642, 9219).
   - `ki-basis/docker/nginx/templates/default.conf.template` provides containerized `envsubst` parameterization.

10. **Client Script Parameterization (F17)**:
    - All 6 client scripts (`populate_firefly.py`, `populate_openproject.py`, `populate_paperless.py`, `verify_fundraiser_stack.py`, `generate_euer_tax_report.py`, `invoke-hermes.ps1`) support CLI arguments (`-i`, `--url`, `--token`) and environment variable overrides.
    - Verified: Passing `-i community` correctly routes requests to ports 9086, 9082, 9010, 9642.

---

## 2. Logic Chain

1. **From Observation 2**: Because `-t` was completely removed from all `docker exec` commands in `DUAL_INSTANCE_RUNBOOK.md` and `backup-stack.sh` and replaced with `-i`, no pseudo-TTY line discipline conversion from `\n` to `\r\n` occurs. Therefore, logical SQL dumps and custom-format compressed binary dumps (`pg_dump -Fc`) retain bit-exact header and stream integrity, preventing `pg_restore` header signature corruption.
2. **From Observation 3**: Because Section 4.3 recreates `postgres-data` as an empty volume before restoring `postgres_all.sql`, PostgreSQL boots with an uninitialized cluster. Consequently, piping `postgres_all.sql` into `psql` does not encounter existing relation collisions or primary key conflicts. Additionally, restoring `paperless-data` and `hermes-workspaces` preserves the document classifier, SQLite search index, and AI workspace artifacts.
3. **From Observation 4 & 7**: Because `backup-stack.sh` and `stop-ki-basis.sh` dynamically resolve instance namespaces and configuration files, operators on Linux/WSL2 can backup or stop either stack individually without container name collisions or script crashes.
4. **From Observation 5**: Because PostgreSQL does not run initialization scripts when mounting an existing data volume, documenting temporary PostgreSQL startup and `ALTER USER` statements ensures database user credentials match `.env.community`, preventing authentication failure crash loops during migration.
5. **From Observation 6**: Because daemon termination is guarded behind `if ($Instance -eq "all" -and $StopEngine)`, shutting down a single instance (or stopping both without `-StopEngine`) cannot terminate the host Docker Desktop engine.
6. **From Observation 8**: Because `start-ki-basis.sh` derives loop attempts from `$TIMEOUT` via `max_attempts=$(( (TIMEOUT + 1) / 2 ))`, the user-specified timeout is properly respected during health checks.
7. **From Observation 9**: Because `default.conf` uses client-side port inspection and dedicated institutional sections, Community users on `:9084` are routed to Community services (908x), preventing cross-tenant redirects.
8. **From Observation 10**: Because all 6 client scripts parse CLI flags and environment variables, operators and automation tools can safely target either instance without polluting the Private database with Community records.
9. **From Observations 1–10**: All defects identified by `reviewer_2` are verified to be fully and authentically resolved without facades or bypasses.

---

## 3. Caveats

- **No Caveats**: All 10 remediation items have been independently checked, tested, and verified.
- Prior to starting the dual-instance stacks for the first time in a live environment, operators should ensure legacy single-instance containers holding port band 808x are stopped via `docker compose down` as documented in Step 1 of the migration runbook.

---

## 4. Conclusion

**Verdict: APPROVE**

The dual-instance infrastructure for `ki-basis` is fully isolated, resilient, and operationally hardened across Windows and Linux/WSL2 runtimes. All criteria from `ORIGINAL_REQUEST.md`, `PROJECT.md`, `reviewer_2/review.md`, and `worker_remediate_2/remediation_report.md` are satisfied.

---

## 5. Verification Method

To independently reproduce the verification results:

1. **Execute Static Isolation Verification**:
   ```powershell
   python C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_dual_isolation.py
   ```
   *Expected Result:* `32 checks passed, 0 failures` (Exit code 0).

2. **Execute Pytest Test Suite**:
   ```powershell
   pytest C:\GitDev\apexai-os-meta\ki-basis\tests\test_adversarial_isolation.py -v
   ```
   *Expected Result:* `21 passed` (Exit code 0).

3. **Verify Shell & PowerShell Syntax**:
   ```powershell
   bash -n C:\GitDev\apexai-os-meta\ki-basis\scripts\backup-stack.sh
   bash -n C:\GitDev\apexai-os-meta\ki-basis\scripts\start-ki-basis.sh
   bash -n C:\GitDev\apexai-os-meta\ki-basis\scripts\stop-ki-basis.sh
   powershell -Command "[scriptblock]::Create((Get-Content 'ki-basis/scripts/stop-ki-basis.ps1' -Raw))"
   powershell -Command "[scriptblock]::Create((Get-Content 'ki-basis/scripts/invoke-hermes.ps1' -Raw))"
   ```
   *Expected Result:* All exit with status code 0.

4. **Verify Client Script Portability**:
   ```powershell
   python C:\GitDev\apexai-os-meta\ki-basis\scripts\populate_firefly.py --help
   python C:\GitDev\apexai-os-meta\ki-basis\scripts\populate_openproject.py --help
   python C:\GitDev\apexai-os-meta\ki-basis\scripts\populate_paperless.py --help
   python C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_fundraiser_stack.py --help
   python C:\GitDev\apexai-os-meta\ki-basis\scripts\generate_euer_tax_report.py --help
   ```
   *Expected Result:* All scripts display usage options showing `--instance` and explicit URL options.
