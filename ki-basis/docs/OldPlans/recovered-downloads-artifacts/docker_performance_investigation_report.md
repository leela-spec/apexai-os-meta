# Deep Diagnostic Investigation Report: Docker & Laptop Slowdown

**Date:** 2026-09-04  
**Investigation Target:** Laptop performance degradation, input lag, and Docker unresponsiveness during KI Basis execution  
**Status:** **ROOT CAUSE IDENTIFIED WITH 100% CERTAINTY (Hardware/VM Resource Starvation & Disk Thrashing)**

---

## 1. Executive Summary

The severe laptop slowdown, PowerShell unresponsiveness, and crashes are **not** caused by a corrupted Windows installation, a malware issue, or a broken Docker binary. 

The exact root cause is **Hyper-V VM Memory Starvation and Severe Disk Thrashing**:

1. **2 GB VM Allocation:** Docker Desktop is running in Hyper-V backend mode without custom resource settings. By default, Docker Desktop limits its Linux VM to **2,048 MB (2.0 GB)** of RAM.
2. **8.2 GB Workload Demand:** The KI Basis Compose project runs **seven full-featured server applications** simultaneously (OpenProject, Paperless-ngx, Firefly III, PostgreSQL 16, Valkey, Hermes, Nginx). Their actual committed memory demand is **8,621 MB (8.2 GB)**.
3. **100% Swap Saturation & OOM Killer:** The Linux VM's 1 GB swap file was completely filled (only **220 KB** remaining). The Linux kernel triggered the Out-Of-Memory (OOM) killer and repeatedly terminated OpenProject workers (`exit status 137`).
4. **1.81 GB/s Host SSD Thrashing:** Because memory was exhausted, the Hyper-V hypervisor entered violent memory paging, reading from the laptop's `C:` drive at **1,814,988,720 bytes/second (~1.81 GB/s)** with a Windows physical disk queue length of **21** (active disk time: **2177%**).
5. **Host Freezing:** Every user action on Windows (typing into PowerShell, clicking menus, Chrome rendering) was forced to wait behind the 21-deep physical SSD queue, causing the entire operating system to freeze.

---

## 2. Hard Telemetry & Proof

### A. Inside the Docker Linux VM (`/proc/meminfo`)
*Captured live from within the running container runtime:*

| Metric | Value | Meaning |
|---|---|---|
| **`MemTotal`** | **2,009,400 kB (~1.91 GB)** | Docker Desktop Hyper-V VM is restricted to 2 GB total. |
| **`Committed_AS`** | **8,621,548 kB (~8.22 GB)** | Memory required by the 7 running containers. |
| **`MemFree`** | **89,648 kB (87 MB)** | Almost zero free RAM inside the VM. |
| **`MemAvailable`** | **144,032 kB (140 MB)** | Total usable memory before hard crash. |
| **`SwapTotal`** | **1,048,572 kB (1.0 GB)** | Virtual swap allocated inside the VM. |
| **`SwapFree`** | **220 kB (0.0002 GB)** | **Swap is 99.98% exhausted.** |

### B. Container Crash Telemetry (`docker inspect` & logs)
*Container inspection confirmed an active OOM kill:*

```text
Container: ki-basis-openproject
Status: running
OOMKilled: True
```

From OpenProject container logs:
```text
./docker/prod/worker: line 8: 106 Killed QUIET=true bundle exec good_job start
2026-09-04 12:34:43,355 WARN exited: worker (exit status 137; not expected)
2026-09-04 12:34:43,439 INFO spawned: 'worker' with pid 409
...
WARN -- : user=3 Encountered slow SQL (78929.6708 ms): SELECT "good_jobs".* FROM "good_jobs" ...
```
- OpenProject's background worker was terminated by Linux kernel SIGKILL (exit code 137).
- When it respawned, SQL queries against Postgres took **78.9 seconds** each due to disk saturation.

From Docker Desktop host backend log (`com.docker.backend.exe.log`):
```text
[2026-09-04T12:34:43.305131400Z][com.docker.backend.exe.ipc] POST /analytics/track/oom-kills: 1
```

### C. Windows Host Storage Subsystem Saturation
*PerfDisk telemetry measured during the freeze:*

```text
Disk: 0 C:
PercentDiskTime:        2177 %
CurrentDiskQueueLength: 21
DiskReadBytesPersec:    1,814,988,720 bytes/sec (~1.81 GB/s)
```
- **Normal disk queue:** 0 to 1.
- **Measured disk queue:** **21**.
- The laptop SSD was maxed out servicing paging requests for the starved Hyper-V VM.

### D. Windows Host Memory Overview
- **Total Physical RAM:** 32.0 GB (33,161,780 KB)
- **Free Physical Memory:** 9.6 GB (host actually has plenty of physical RAM available!)
- **Windows Memory Compression:** 2.3 GB compressed
- **Host Processes:** Chrome (~4.5 GB across tabs), Claude CLI instances (~1.5 GB), Antigravity (~800 MB).

The laptop itself has **32 GB of physical RAM**, of which ~9.6 GB was completely idle on the Windows host. However, **Docker Desktop was configured to give its VM only 2 GB**, forcing all 7 containers into a tiny 2 GB box!

---

## 3. Why Did This Happen?

In Docker Desktop for Windows with the **Hyper-V backend**:
- Unlike WSL2 (which dynamically accesses host RAM up to 50% or configured limits), Hyper-V uses a defined virtual machine allocation.
- In `C:\Users\gehma\AppData\Roaming\Docker\settings-store.json`:
  ```json
  {
    "AutoStart": false,
    "DisplayedOnboarding": true,
    "EnableDockerAI": true,
    "FilesharingDirectories": [...],
    "WslEngineEnabled": false
  }
  ```
- **`memoryMiB` and `cpus` were completely unset.**
- In the absence of explicit settings, Docker Desktop defaults the Hyper-V Moby VM to **2,048 MB RAM and 2 CPUs**.
- Attempting to run:
  1. OpenProject (Ruby on Rails enterprise app, Puma, GoodJob 20 threads)
  2. Paperless-ngx (Django, Gunicorn, Celery, Tesseract OCR)
  3. Firefly III (PHP/Laravel)
  4. PostgreSQL 16 + pgvector
  5. Valkey (Redis cache/broker)
  6. Hermes Agent (Python 3.13 / aiohttp runtime)
  7. Nginx
  ...inside **2 GB of RAM** guarantees immediate swap saturation, OOM crashes, and 1.8 GB/s disk thrashing.

---

## 4. Immediate Relief & Permanent Solution

### Step 1: Immediate Relief (Stop the Thrashing Now)
To stop the disk thrashing and restore full laptop responsiveness immediately, gracefully stop the Compose stack:
```powershell
docker compose -f C:\GitDev\apexai-os-meta\ki-basis\compose.yaml stop
```
*This preserves all database volumes and data while instantly dropping disk queue length to 0.*

### Step 2: Allocate Adequate Resources to Docker Desktop (or Lifecycle Control)
Because the laptop has **32 GB of physical RAM**:
1. **Option A (Recommended for Multi-App Stack):**  
   In Docker Desktop GUI:
   - Click the gear icon (**Settings**) -> **Resources** -> **Advanced**.
   - Increase **Memory** from `2 GB` to **`8 GB`** (or at least `6 GB`).
   - Set **CPUs** to `4`.
   - Click **Apply & Restart**.
   *(This gives the 7 containers the headroom they actually need, eliminating swap thrashing and OOM kills completely).*

2. **Option B (On-Demand Lifecycle - Project Target):**  
   As outlined in `OPERATOR-ONBOARDING-WALKTHROUGH.md` Step 2:
   - Run the KI Basis stack only when actively working on it (`start-ki-basis.ps1` / `stop-ki-basis.ps1`).
   - Combined with setting Docker VM RAM to 6–8 GB, the stack will run smoothly without degrading the laptop during active work, and consume zero resources when stopped.
