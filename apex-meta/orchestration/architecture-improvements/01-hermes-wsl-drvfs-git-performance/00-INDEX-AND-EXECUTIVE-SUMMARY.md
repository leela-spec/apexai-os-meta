# Hermes Architecture Improvement Package: WSL2/DrvFs Filesystem & Git Execution Architecture

**Record ID:** `ARCH-IMP-2026-08-01-HERMES-DRVFS-GIT-PERF`  
**Classification:** Critical Architecture Improvement & Operational Policy  
**Status:** PROPOSED & FULLY SPECIFIED FOR VERIFICATION  
**Author:** Architecture & Runtime Engineering  
**Date:** 2026-08-25  
**Target Repositories:** `apexai-os-meta`, `MasterOfArts`, `Investment`, `acim-secular`

---

## 1. Executive Summary

During an autonomous execution session, the **Hermes Agent** encountered a catastrophic performance degradation and task stall while attempting to stage, commit, and push a reviewer handover artifact (`artifacts/weekly-orchestration-campaign/04-phase4/HANDOVER-INDEPENDENT-REVIEWER.md`). 

The command trace demonstrated severe pathological behavior:
- `git status --short -- ...`: **120.4 seconds**
- `git commit -m ...`: **82.9 seconds** (timed out)
- `kill -9`: **failed to terminate** the process immediately due to Linux kernel **`D state` (uninterruptible disk sleep)**
- Stale `.git/index.lock` remediation: **300.3 seconds** before recovery

This package provides an exhaustive, evidence-backed architectural analysis, web-grounded research benchmarks, codebase drift auditing, and concrete remediation proposals.

---

## 2. Directory & File Structure

This improvement package is structured modularly for targeted review and verification:

| File | Purpose | Key Content |
| :--- | :--- | :--- |
| [`00-INDEX-AND-EXECUTIVE-SUMMARY.md`](./00-INDEX-AND-EXECUTIVE-SUMMARY.md) | Overview & Navigation | High-level synthesis, document index, and quick-reference verdict. |
| [`01-INCIDENT-DIAGNOSIS-AND-ROOT-CAUSE-ANALYSIS.md`](./01-INCIDENT-DIAGNOSIS-AND-ROOT-CAUSE-ANALYSIS.md) | Technical Root Cause Analysis | Trace breakdown, 9P/DrvFs mechanics, POSIX `lstat` syscall storm, and D-state locking dynamics. |
| [`02-KERNEL-FILESYSTEM-AND-WEB-BENCHMARKS-RESEARCH.md`](./02-KERNEL-FILESYSTEM-AND-WEB-BENCHMARKS-RESEARCH.md) | Web & Engineering Research | Microsoft WSL2 specifications, Linux ext4 vs. NTFS benchmarks (10x–50x delta), `git.exe` interop bridge, and Git config parameters. |
| [`03-RECENT-COMMITS-SCALE-AUDIT-AND-ARCHITECTURE-DRIFT.md`](./03-RECENT-COMMITS-SCALE-AUDIT-AND-ARCHITECTURE-DRIFT.md) | Repository & Vision Audit | Analysis of recent commits (53,866 tracked files, granular simulation logs), drift between Architecture Vision V2 and actual runtime launch environment. |
| [`04-ARCHITECTURE-FIX-PROPOSALS-AND-DECISION-MATRIX.md`](./04-ARCHITECTURE-FIX-PROPOSALS-AND-DECISION-MATRIX.md) | Multi-Option Solution Architecture | Comparative trade-off matrix across 4 architectural options (Ext4 Canonical, Git Interop Shim, Scoped Git Dispatch, Repository Scale Hygiene). |
| [`05-ACTIONABLE-REMEDIATION-ROADMAP-AND-RUNBOOKS.md`](./05-ACTIONABLE-REMEDIATION-ROADMAP-AND-RUNBOOKS.md) | Execution Plan & Runbooks | Exact configuration steps, `.git/config` templates, `AGENTS.md` patches, and incident recovery runbook. |

---

## 3. High-Level Findings & Verdict

1. **The Core Physical Bottleneck:** The root failure was caused by executing Linux Git within WSL2 against the Windows NTFS host path `/mnt/c/...` via the **9P virtual filesystem protocol**. Over 9P, every file comparison requires serialized RPC roundtrips across the VM hypervisor boundary.
2. **Compound Scale Inflation:** Recent granular simulation commits (`414e4170`, `db55b79d`, `d322703d`, etc.) added hundreds of leaf logs and checkpoint files, swelling `apexai-os-meta` to **53,866 tracked files**. On 9P/DrvFs, traversing 54k files requires tens of thousands of cross-boundary syscalls, stalling the kernel in uninterruptible disk wait (`D state`).
3. **Architecture Vision Drift:** The Hermes Multi-Repo Architecture V2 (`HERMES_MULTI_REPO_ORCHESTRATION_V2_ARCHITECTURE_SHOWCASE.md`) had correctly identified ext4 (`/root/workspaces/`) as the required single source of truth. However, the runtime session was launched targeting `/mnt/c/GitDev/...` without guardrails in `AGENTS.md` or git wrapper protections.
4. **The Direct Remedy:** Strict enforcement of the **Native ext4 Workspace Law** for all Linux agent sessions, augmented with repository-level Git caching configurations, scoped Git execution dispatch, and simulation log hygiene.
