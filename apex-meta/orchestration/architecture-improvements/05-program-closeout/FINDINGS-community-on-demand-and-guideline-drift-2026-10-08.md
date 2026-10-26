---
type: Findings
title: Learnings — Community On-Demand Conversion & Why Prior Guidelines Drifted
description: >
  Root-cause analysis of why the secondary community stack ran 24/7 consuming ~2.45 GB RAM,
  why legacy Docker Desktop scripts and guidelines in lika-community survived the Sept 2026
  remediation unexecuted/corrupted, and how test-induced lock-in reinforced the drift.
tags: [findings, learnings, community, wsl2, docker, lifecycle, drift]
created: 2026-10-08
status: current
canonical_current_state: ki-basis/docs/INFRASTRUCTURE.md
---

# Learnings: Community On-Demand Conversion & Guideline Drift Analysis

## 1. Executive Summary

On 2026-10-08, the `community` Docker Compose stack (`C:\GitDev\lika-community\compose.wsl.yaml`) was converted from 24/7 auto-start (`restart: unless-stopped`) to strictly **on-demand (`restart: "no"`)**, managed via `scripts/start-community-wsl.sh` and `scripts/stop-community-wsl.sh`. Stopping the 6 idle community containers immediately freed ~2.45 GB of WSL2 RAM.

Forensic inspection of `apexai-os-meta` and `lika-community` revealed **four compounding root causes** explaining why this change was necessary and why previous guidelines and scripts were corrupted or left unexecuted.

---

## 2. Root-Cause Analysis

### RC-1: Compose Template Cloning + Keepalive Interaction (`restart: unless-stopped`)
- **What happened:** During the ADR-002 WSL2 consolidation (2026-09-26, D-14), `lika-community/compose.wsl.yaml` was authored by cloning service blocks from `compose.yaml`. Every service inherited `restart: unless-stopped`.
- **Why it caused 24/7 RAM drain:** In Docker, `unless-stopped` persists container runtime state across daemon restarts unless `docker stop` was the final command executed before shutdown. Whenever an operator or agent ran `docker compose up -d` for testing or soak verification, Docker latched the 6 containers into the `running` state. Because `wsl-keepalive.vbs` (D-06) boots the WSL2 VM at Windows logon and prevents idle shutdown, `dockerd` automatically started all 6 community containers on every reboot.
- **Fix applied:** Set `restart: "no"` on all 6 services in `compose.wsl.yaml` and applied `docker update --restart=no` to the container instances. Even if started on-demand and left running when Windows reboots, Docker will not auto-start them on next boot.

### RC-2: Cross-Repository Remediation Blind Spot (`lika-community` Left in Docker Desktop Era)
- **What happened:** During the Sept 28–29 remediation waves (`T10` script guards + `R1–R7` documentation remediation), `apexai-os-meta/ki-basis` received:
  1. New WSL-aware lifecycle scripts (`ki-basis/scripts/start-ki-basis-shared-db.ps1` and `stop-ki-basis-shared-db.ps1`).
  2. Fail-closed guards (`exit 2`) on the legacy `ki-basis/scripts/{start,stop}-ki-basis.{sh,ps1}`.
  3. A single source of truth (`ki-basis/docs/INFRASTRUCTURE.md`).
- **Why `lika-community` was missed:** The audit and lint scripts (`05-program-closeout/tests/doc-integrity-lint.sh`) scoped their file scans strictly to `$APEX/ki-basis` and `$APEX/apex-meta`. The sibling repository `C:\GitDev\lika-community` was never scanned or remediated.
- **Resulting corruption in `lika-community`:**
  - `lika-community/AGENTS.md` (§Scripts & Operations) and `lika-community/README.md` (§1–2) still instruct operators and agents to run `.\scripts\start.ps1` and `.\scripts\stop.ps1`, reference `compose.yaml` instead of `compose.wsl.yaml`, and list retired container names (`ki-basis-community-*`).
  - `lika-community/scripts/start.ps1` and `stop.ps1` still attempt to launch `C:\Program Files\Docker\Docker\Docker Desktop.exe` (uninstalled per ADR-002) and target `-p ki-basis-community -f compose.yaml`.
  - `lika-community/scripts/start.sh` and `stop.sh` still invoke `docker --context desktop-linux compose -p ki-basis-community -f compose.yaml` with **no fail-closed guard**.

### RC-3: Asymmetric Lifecycle Tooling (`INFRASTRUCTURE.md` §7 Gap)
- **What happened:** `ki-basis/docs/INFRASTRUCTURE.md` §7 ("Start / stop / health") documented dedicated wrapper scripts for the Private stack (`start-ki-basis-shared-db.ps1` / `stop-ki-basis-shared-db.ps1`), but for Community it only listed a raw inline `docker compose ... up -d` one-liner with no corresponding `stop` command, no shared-DB pre-flight check, and no script path.
- **Why guidelines were not executed:** Operators and agents lacked a canonical, discoverable script pair for Community on-demand start/stop, defaulting either to leaving the stack running permanently or consulting `lika-community/README.md` (which pointed to the broken Docker Desktop scripts).

### RC-4: Test-Induced Policy Lock-In (`infra-health-test.sh`)
- **What happened:** `05-program-closeout/tests/infra-health-test.sh` (referenced at the top of `INFRASTRUCTURE.md` as the `GREEN 29/29` verification oracle) hardcodes in Check #2 (`Expected containers running (13)`) and Check #3 (`Endpoints respond`) that all 6 `community-*` containers **must** be running and responding on `:9642` and `:9084`, or the health test fails (`OVERALL: RED`).
- **Why it prevented on-demand operation:** Any agent following the instruction in `INFRASTRUCTURE.md` to verify infrastructure health via `infra-health-test.sh` would see 8 failures when Community is stopped, treating the stopped state as an outage rather than the intended default.

---

## 3. Structural Prevention Rules (Takeaways)

| Failure Mode | Prevention Rule |
|---|---|
| **Sibling-Repo Drift** | `doc-integrity-lint.sh` must include `/mnt/c/GitDev/lika-community` in its retired-topology scan alongside `ki-basis` and `apex-meta`. |
| **Unprotected Legacy Scripts** | Legacy scripts in `lika-community/scripts/{start,stop}.{sh,ps1}` must carry the same fail-closed guard (`exit 2`) or delegate directly to `start-community-wsl.sh` / `stop-community-wsl.sh`. |
| **Health Oracle Lock-In** | `infra-health-test.sh` must treat `community-*` containers as **on-demand (`exited` + `restart=no` by default)** unless a `--with-community` flag is passed or `community-nginx` is detected running. |
| **Single-Source Index Prominence** | Both `ki-basis/docs/INFRASTRUCTURE.md` (§4.2, §7) and `lika-community/{AGENTS.md,README.md}` must prominently index `start-community-wsl.sh` and `stop-community-wsl.sh`. |
