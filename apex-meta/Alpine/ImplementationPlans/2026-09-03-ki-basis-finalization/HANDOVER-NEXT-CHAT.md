# Handover & Process Evaluation — ki-basis Finalization

**Date**: 2026-09-04  
**Current Git HEAD**: `02b0cd94` (pushed to `origin/main`)  
**Active Project**: `ki-basis` on Docker Desktop Hyper-V (Windows 11)

---

## 1. Executive Summary & Progress Checklist

The implementation sequence follows the canonical program at `apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/00-START-HERE.md`:

| Module | Description | Status | Verification Evidence / Commit |
| :--- | :--- | :--- | :--- |
| **M01** | Security / operator secret gate | **DONE** | Documentation & sanitized dossier (`6774db64`) |
| **M02** | Minimal backup fail-close hardening | **DONE** | Validated fail-close in `backup-stack.sh` (`6774db64`) |
| **M03** | Independent restore SHA oracle | **DONE** | Live restore verified, adversarial suite passed (`abe7ffdb`) |
| **M04** | Strict auth + fail-closed stack verifier | **DONE** | Verifier fail-closed gate passed, edge cleaned (`2fb60bf4` $\rightarrow$ `02b0cd94`) |
| **M05** | Hermes AI control stack + OpenRouter + 3 skills | **READY** | Implementation plan drafted, operator gate ready |
| **M06** | Documentation truth correction | *Pending* | Post-M05 |
| **M07** | Windows cold reboot + second-copy backup | *Pending* | Post-M05/M06 |
| **M08** | Performance tuning explicitly deferred | *Pending* | Note application |
| **M09** | Final independent audit | *Pending* | Final closure |

---

## 2. Process Evaluation & Diagnostic Retrospective (What Happened During M04)

During the execution of Module 04, a severe stall occurred. For another agent or human reviewer evaluating the process, here is the exact factual root-cause breakdown:

### A. The Underlying Physical Failure (Host Standby / Hyper-V Disconnect)
1. **Sleep Cycle**: The Windows 11 host entered sleep/standby for ~1.5 hours.
2. **Network Route Severance**: Resuming from standby severed the Hyper-V virtual network switch route (`connect tcp 192.168.65.7:2376: no route to host`).
3. **Internal IPC Stats Deadlock**:
   - While containers inside the Linux VM remained alive and responded to localhost HTTP ports (`curl.exe` to `8084`, `8086`, `8010`, `8082` succeeded), Docker Desktop's Windows Go backend (`com.docker.backend.exe`) deadlocked on an internal IPC stats loop:
     ```text
     [com.docker.backend.exe.ipc] stats C->S stats GET /ping ... context deadline exceeded
     ```
   - In the Docker Desktop GUI, this presented as:
     - *"Container CPU/memory usage: Data unavailable at this time"*
     - `N/A` for all container CPU and Memory metrics
     - Bottom bar showing `RAM 0.00 GB / CPU 0.00%`
   - **Consequence**: The Windows named pipe `\\.\pipe\dockerDesktopLinuxEngine` became serialized behind this stuck lock. Any subsequent CLI command (`docker ps`, `docker inspect`, `docker exec`) hung indefinitely on the Windows pipe.

### B. Agent Errors & Missteps
1. **Spawning Repeated CLI Checks Against a Blocked Pipe**: When `docker ps` timed out, the agent initially spawned alternative `docker` commands that queued behind the same blocked pipe, compounding the perceived unresponsiveness.
2. **Out-of-Scope Compose Edits**: The agent briefly attempted to edit `compose.yaml` to add `stdin_open/tty` to Hermes. This was out-of-scope for Module 04 and was promptly reverted.
3. **Win32 CRT Subshell Poisoning**: Attempting to invoke native `curl.exe` from inside Git Bash subshells (`$(curl.exe ... -w '%{http_code}')`) caused Windows CRT environment variable expansion to eat `%{http_code}` into literal `%http_coden`, giving false `HTTP 000` test results.

### C. The Resolution
1. **Clean GUI Daemon Reset**: A clean restart of Docker Desktop via the Troubleshoot interface freed the deadlocked IPC stats collector and immediately restored <1s response times on `docker ps`.
2. **CRLF & Subshell Cleanliness**: Reverted to standard `curl` in `verify-stack.sh` with explicit CRLF stripping (`| tr -d '\r\n[:space:]'`).
3. **Successful Fail-Closed Verification**: `verify-stack.sh` executed cleanly (30 PASS, 2 WARN, 0 unexpected failures) and proved that `STRICT_AUTH=1` strictly halts when credentials are missing.

---

## 3. Current Live Technical State

### Docker Project: `ki-basis`
All 7 canonical containers are online and attached to `ki-basis-net`:
- `ki-basis-postgres` (PostgreSQL 16 + pgvector 0.8.6 in designated `postgres` DB; port 5432 unmapped to host)
- `ki-basis-valkey` (Valkey 8.0.2; port 6379 unmapped to host)
- `ki-basis-paperless` (Paperless-ngx; localhost:8010)
- `ki-basis-firefly` (Firefly III; localhost:8086)
- `ki-basis-openproject` (OpenProject 14; localhost:8082)
- `ki-basis-nginx` (Nginx edge; localhost:8084, `/healthz` and `/` dashboard operational)
- `ki-basis-hermes` (NousResearch Hermes Agent; isolated: no Docker socket, no WSL host mounts)

### Security Boundaries Active:
- No Docker socket mounted into Hermes (`/var/run/docker.sock` absent).
- No legacy WSL host mounts (`/mnt/c` or `wsl$` absent).
- Databases have no published host ports.
- Deliberately invalid credentials to Paperless, Firefly, and OpenProject are actively rejected (HTTP 401/403).

---

## 4. Instructions for Next Chat (Executing Module 05)

The next step is **Module 05: Hermes as the AI Control Stack**.

### Core Target:
Transform Hermes from an isolated container into the operator-facing AI that securely queries Paperless, Firefly, and OpenProject via version-controlled Hermes skills using an OpenRouter-backed model.

### Key Rules:
1. **Never Ask for Secrets in Chat**: Do not ask the operator to paste their OpenRouter key or application tokens into the AI prompt.
2. **Phase 5A Operator Gate**:
   - The operator configures OpenRouter via the interactive Hermes CLI:
     ```powershell
     docker exec -it ki-basis-hermes /opt/hermes/.venv/bin/hermes model
     ```
   - The key is saved to persistent `/opt/data/.env` (backed by volume `hermes_data`).
3. **Canonical Skill Directory**:
   - Author three version-controlled skills in `ki-basis/hermes-skills/`:
     - `paperless-local/` (`SKILL.md` + `scripts/paperless_client.py`)
     - `firefly-local/` (`SKILL.md` + `scripts/firefly_client.py`)
     - `openproject-local/` (`SKILL.md` + `scripts/openproject_client.py`)
   - All v1 skills must be **strictly read-only**.
   - Scripts must use Python standard library `urllib.request` (no extra pip dependencies), enforce timeouts (10-15s), use `Authorization` headers, and never leak credentials.
4. **Hermes Configuration**:
   - Configure Hermes `skills.external_dirs` to point to `/root/workspaces/apexai-os-meta/ki-basis/hermes-skills`.
   - Set `skills.write_approval: true` so Hermes cannot overwrite version-controlled skills.
5. **Acceptance Criteria**:
   - Operator asks conversational questions in `docker exec -it ki-basis-hermes ...`:
     - Paperless: Query document "Antigravity M5 Test Document".
     - Firefly: Query identity/accounts.
     - OpenProject: Query work package 37.
