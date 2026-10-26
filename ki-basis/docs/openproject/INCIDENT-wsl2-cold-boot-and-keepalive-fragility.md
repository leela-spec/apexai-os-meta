---
okf_version: "0.2"
type: incident
title: OpenProject 503 / Unreachable intermittent failure due to WSL2 idle termination and keepalive failure
description: Agents intermittently observe 503 Service Unavailable, socket hang-up, or ECONNRESET on http://127.0.0.1:8083. Investigation confirmed that Windows terminates the WSL2 virtual machine (vmmemWSL) after idle periods when host wsl.exe handles are missing. Subsequent requests trigger a cold WSL2 and OpenProject container boot where Puma warmup takes 30-45 seconds, during which Apache returns 503. The host-level wsl-keepalive.vbs in the Windows Startup folder had silently exited.
tags: [openproject, wsl2, keepalive, infrastructure, incident, puma, cold-boot]
status: open
opened: 2026-10-20
action_required: to be checked to resolve
program_ref: infrastructure-resilience
---

# Incident: OpenProject Intermittent 503 / Unreachable (WSL2 Idle VM Termination & Host Keepalive Fragility)

> **Status:** `open` | **Action Required:** `to be checked to resolve`  
> **Reported:** 2026-10-20  
> **Target Service:** Private Leela OpenProject (`http://127.0.0.1:8083`, container `leela-op178-openproject` in WSL2 native Docker)

---

## 1. Symptom

Autonomous agents (and interactive tooling) executing queries or skill commands against OpenProject intermittently experience complete connection failures:
- HTTP `503 Service Unavailable`
- Client errors: `socket hang up`, `ECONNRESET`, or polling timeouts (`Timeout waiting for OpenProject to respond on http://127.0.0.1:8083/health_checks/default`)
- The failure occurs repeatedly after periods of inactivity, then self-resolves ~45–60 seconds later or after manual intervention.

---

## 2. Root Cause Analysis

Investigation conducted on 2026-10-20 revealed a two-stage failure mechanism spanning the Windows host and the WSL2 Hyper-V boundary:

### 2.1 WSL2 Idle VM Automatic Shutdown
Windows WSL2 manages the `vmmemWSL` virtual machine lifecycle aggressively:
- When no active Windows-spawned interactive `wsl.exe` processes or console sessions are open on the host, Windows marks WSL2 as idle and shuts down the VM (observed via `journalctl --list-boots` showing rapid repeated boots: e.g. `15:52:26` and `15:57:08`).
- Internal Linux systemd services (such as `openproject-keepalive.service` inside Linux) **do not prevent Windows from shutting down WSL2**; Windows only tracks host-side Windows process handles to `wsl.exe`.

### 2.2 Cold Boot & Puma Warmup Gap (The 503 Window)
When an external HTTP request hits `127.0.0.1:8083` via the Windows WSL2 localhost port forwarder:
1. Windows awakens/cold-boots the WSL2 VM.
2. Systemd and Docker restart the `leela-op178-openproject` container.
3. The container's Apache/reverse-proxy frontend binds immediately to port `8080` (mapped to host `8083`).
4. However, OpenProject's Ruby on Rails backend (`puma 8.0.2` on Ruby 3.4/4.0 with GoodJob and heavy gem initialization) requires **30 to 45 seconds** to become operational.
5. During this warmup window, Apache has no active upstream Puma socket/port to proxy to and immediately returns `503 Service Unavailable` (or drops connections), failing all incoming agent requests.

### 2.3 Failure of Host Keepalive (`wsl-keepalive.vbs`)
To prevent the WSL2 idle shutdown, a VBScript keepalive was placed in the user's Windows Startup folder:
`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\wsl-keepalive.vbs`
- **What went wrong:** On inspection, `wscript.exe` was **not running** on the Windows host.
- Startup folder VBScripts have no supervision: if the user logs out, if a Windows update cycles the session, or if `wscript.exe` / `wsl.exe` crashes, Windows does not restart it.
- Once the host script died silently, WSL2 was left unprotected against Hyper-V idle reaping.

---

## 3. Immediate Mitigation Applied (2026-10-20)

1. Relaunched the host keepalive process via Windows `wscript.exe`:
   ```powershell
   Start-Process wscript.exe -ArgumentList "C:\Users\gehma\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\wsl-keepalive.vbs"
   ```
2. Verified `wscript.exe` is actively running and holding an open `wsl.exe --exec sleep infinity` process handle.
3. Verified OpenProject endpoint health:
   - `doctor`: passed
   - `whoami`: HTTP 200 OK (Admin, id 4)
   - `project.list`: HTTP 200 OK (14 projects returned)

---

## 4. Permanent Solutions to Evaluate & Implement (To Be Checked to Resolve)

The current mitigation (VBScript in user Startup folder) remains fragile against user logout, host crashes, or silent background terminations. The following permanent solutions must be checked and implemented:

### Option A: Windows Task Scheduler Daemon (Recommended)
- Create a Windows Scheduled Task (via `schtasks` / PowerShell) running as `SYSTEM` or the active user.
- **Triggers:** At system startup and at user logon.
- **Settings:**
  - `RestartOnFailure`: Restart every 1 minute up to 3 times on failure.
  - `ExecutionTimeLimit`: Indefinite (`PT0S`).
  - Run `wsl.exe -d Ubuntu-24.04 --exec sleep infinity`.
- **Benefit:** Supervised by Windows OS; automatically restarts if killed or after host reboots.

### Option B: Dedicated Windows Service (e.g. via NSSM or WinSW)
- Wrap a persistent WSL handle (`wsl.exe --exec sleep infinity`) as a genuine Windows Service.
- Automatically boots with Windows prior to user login, keeping Docker and OpenProject permanently warm.

### Option C: Health Check Watchdog / Self-Healing Agent
- Implement a scheduled health-check watchdog (or Antigravity `/schedule` daemon) that pings `http://127.0.0.1:8083/health_checks/default` every 5 minutes and automatically triggers a host wakeup/warmup if unreachable.

---

## 5. Acceptance Criteria to Close Incident

- [ ] Host-level WSL2 keepalive mechanism is replaced with a resilient, auto-restarting service or Windows Scheduled Task.
- [ ] WSL2 does not terminate after >60 minutes of host idle time.
- [ ] OpenProject responds to agent API calls with `<500ms` latency without experiencing 503 warmup errors.
- [ ] Documentation updated in `RUNBOOK-openproject-17.8-operations.md`.
