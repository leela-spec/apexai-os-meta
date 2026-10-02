# W2 — Target Environment Provisioning & Engine Isolation Evidence

**Timestamp:** 2026-09-02T14:07:00+02:00  
**Phase:** W2 (Provision independent Docker host environment)  
**Status:** PASS  
**Isolation Verdict:** 100% PROVEN SEPARATION (`SOURCE_ENGINE_ID != TARGET_ENGINE_ID`)

---

## 1. Engine Comparison Matrix

| Property | Source Environment (Migration Source / Rollback) | Target Environment (Dedicated ki-basis Host) |
|---|---|---|
| **Host System** | Ubuntu 26.04 WSL2 | Windows 11 Pro (Docker Desktop Hyper-V) |
| **Docker Engine ID** | `e0f498ad-276a-4357-8af1-d5a81aabd876` | `e9c8ec3c-5306-43e3-8b37-a0803aa830d2` |
| **Docker Context** | `default` (`unix:///var/run/docker.sock`) | `desktop-linux` (`npipe:////./pipe/dockerDesktopLinuxEngine`) |
| **Operating System** | `Ubuntu 26.04 LTS` | `Docker Desktop` |
| **Kernel Version** | `6.18.33.2-microsoft-standard-WSL2` | `7.0.12-linuxkit` |
| **OS Type / Arch** | `linux` / `x86_64` | `linux` / `x86_64` |
| **Docker CLI Path** | `/usr/bin/docker` (in WSL) | `C:\Program Files\Docker\Docker\resources\bin\docker.exe` |

---

## 2. Target Gate Script Output (`00a-docker-desktop-target-gate.ps1`)

```text
Desktop Exists: True
CLI Exists: True
DOCKER_DESKTOP_PATH=C:\Program Files\Docker\Docker\Docker Desktop.exe
DOCKER_CONTEXT=desktop-linux
SOURCE_ENGINE_ID=e0f498ad-276a-4357-8af1-d5a81aabd876
TARGET_ENGINE_ID=e9c8ec3c-5306-43e3-8b37-a0803aa830d2
TARGET_OS_TYPE=linux
TARGET_KERNEL=7.0.12-linuxkit
TARGET_OPERATING_SYSTEM=Docker Desktop
DOCKER DESKTOP TARGET GATE PASS
```

---

## 3. Bidirectional Container Isolation Test

| Action | Target Engine (Docker Desktop) | Source Engine (Ubuntu WSL2) | Result |
|---|---|---|---|
| **1. Run container on Target (`target-iso-test`)** | `target-iso-test` visible in `docker ps` | Empty (`''` in `wsl docker ps`) | **PASS (Target container invisible to Source)** |
| **2. Run container on Source (`source-iso-test`)** | Empty (`''` in `docker ps`) | `source-iso-test` visible in `wsl docker ps` | **PASS (Source container invisible to Target)** |

---

## 4. G2 Acceptance Summary

- Target Docker Engine is up and reachable via `desktop-linux` context.
- Target storage is clean and isolated.
- Zero cross-talk or shared daemon state with Ubuntu WSL2.
- Ready for W3 configuration patching and W4 sequential service deployment.
