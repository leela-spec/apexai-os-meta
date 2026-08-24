# 04 — Pre-Implementation Minimum Coherent Correction Plan

- **Program:** Hermes Multi-Repo Orchestration v2
- **Target Repository:** `leela-spec/apexai-os-meta` (`main`)
- **Evaluation Date:** 2026-08-24
- **Reviewer Role:** Independent Architecture & Safety Evaluator
- **Governing Handover:** [14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md](../../14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md)
- **Status:** **COMPLETE — PROPOSED ACTION PLAN FOR OPERATOR SIGN-OFF**

---

## Executive Overview

This correction plan details the **minimum coherent set of five targeted adjustments (C01–C05)** required before executing the implementation roadmap. These corrections address concrete runtime gaps discovered during live host inspection and static failure simulations, without altering the accepted high-level architecture (D01–D10).

In accordance with patch safety rules, existing architecture files are **not directly edited** during validation. This document serves as the exact specification for implementation runbooks and future patch generation.

---

## Correction C01 — Docker Volume Configuration Sanitization

- **Target Risk:** `R21` (Hardcoded Docker Volume Mount in Global Config) / `R03` / `R04` / `R05`
- **Affected Roadmap Phase:** Phase 1 (Runtime Preflight) & Phase 8 (Docker Execution Boundary)
- **Priority:** **P0 (CRITICAL BLOCKER FOR MULTI-REPO WORK)**

### Rationale
Live inspection of `/root/.hermes/config.yaml` revealed that `terminal.docker_volumes` currently contains static mounts:
```yaml
terminal:
  docker_volumes:
    - /root/MasterOfArts:/root/MasterOfArts:rw
    - /root/MasterOfArts:/workspace:rw
```
If an agent executes a task in `~/workspaces/Investment` or `~/workspaces/acim-secular`, Docker will still bind-mount `MasterOfArts` into `/workspace`. This causes write contamination and breaks workspace isolation.

### Required Specification & Proposed Change
1. In `11-IMPLEMENTATION-ROADMAP.md` Phase 1 / Phase 8, mandate removing static repo paths from global `/root/.hermes/config.yaml`.
2. Configure dynamic workspace mapping:
```yaml
terminal:
  backend: docker
  cwd: .
  docker_mount_cwd_to_workspace: true
  docker_volumes: []  # Do not hardcode specific repository paths globally
```
3. If additional shared assets (e.g. shared skill directories) require container access, specify them explicitly as dedicated, read-only volume mounts:
```yaml
terminal:
  docker_volumes:
    - /root/.hermes/skills/shared:/root/.hermes/skills/shared:ro
```
4. Acceptance Gate: A disposable write inside container during an `acim-secular` task must modify `~/workspaces/acim-secular` and leave `MasterOfArts` untouched.

---

## Correction C02 — WSL User Identity & Filesystem Permissions Alignment

- **Target Risk:** `R22` (WSL User Identity Boundary Drift) / `R15` / `R16`
- **Affected Roadmap Phase:** Phase 1 (Runtime Preflight) & Phase 3 (WSL Workspace Pilot)
- **Priority:** **P1 (HIGH)**

### Rationale
The MasterOfArts pilot was executed entirely as `root` in `/root/` (`/root/.hermes`, `/root/MasterOfArts`). However, D07 and standard Linux development practices specify `~/workspaces/` (typically `/home/<operator>/workspaces/`). Running tools under inconsistent user accounts leads to permission denied errors, locked SQLite databases, and Windows File Explorer access barriers.

### Required Specification & Proposed Change
1. Standardize execution identity across the multi-repo orchestration lifecycle:
   - **Recommended Default:** Standardize on consistent execution user identity (e.g., `root` in WSL or explicit non-root user `ubuntu`) with mandatory `umask 022`.
   - Ensure all files created by Hermes have permissions `0644` (files) and `0755` (directories) so Windows File Explorer (`\\wsl.localhost\Ubuntu\...`) can read and edit seamlessly.
2. In `11-IMPLEMENTATION-ROADMAP.md` Phase 1, add an explicit user and permission preflight check:
```bash
# Verify execution user, umask, and directory ownership
whoami
umask
ls -ld ~/workspaces
```

---

## Correction C03 — Fail-Closed Atomic Apex Portfolio Rollup Contract

- **Target Risk:** `R24` (Partial Rollup Silent Corruption) / `R06` / `R07`
- **Affected Roadmap Phase:** Phase 11 (Apex Rollup Pilot) & Phase 12 (Scheduled Automation)
- **Priority:** **P1 (HIGH)**

### Rationale
If one source board query fails during rollup (e.g. SQLite database locked or process timeout), a naive script might aggregate the remaining three boards and publish an incomplete snapshot, falsely showing the failed repo as having zero tasks. Furthermore, writing directly to `kanban-rollup.json` risks publishing a corrupted file if the process crashes midway.

### Required Specification & Proposed Change
1. The deterministic rollup script must enforce **Fail-Closed Semantics**:
   - Collect JSON from all configured boards: `apex`, `masterofarts`, `acim`, `investment`.
   - If **ANY** board query fails or returns invalid JSON:
     - **ABORT** snapshot generation immediately.
     - **DO NOT** overwrite existing `kanban-rollup.json`.
     - Write `kanban-rollup-health.json` with status `DEGRADED`, exit code `1`, timestamp, and error details.
2. The rollup script must use **Atomic File Writes**:
   - Write new rollup to temporary file: `apex-meta/portfolio/current/kanban-rollup.json.tmp`.
   - Validate JSON schema.
   - Atomically rename `.tmp` to `kanban-rollup.json`.
3. Health receipt schema:
```yaml
schema_version: 1
last_attempt: "2026-08-24T18:30:00Z"
last_success: "2026-08-24T18:30:00Z"
status: HEALTHY  # HEALTHY | DEGRADED
boards_polled: [apex, masterofarts, acim, investment]
failed_boards: []
rollup_sha256: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
```

---

## Correction C04 — QMD Index Freshness Verification Protocol

- **Target Risk:** `R25` (QMD Index Stale State Drift) / `R12` / `R14`
- **Affected Roadmap Phase:** Phase 6 (QMD Registry Pilot) & Phase 8 (Direct Repo Work)
- **Priority:** **P2 (MEDIUM)**

### Rationale
QMD indexes are static snapshots. When Git commits or ADR updates occur in a managed repository, QMD does not automatically update its collection index until `qmd update` is executed. An agent answering architecture or policy questions may retrieve obsolete context if the index is stale.

### Required Specification & Proposed Change
1. Define a lightweight, deterministic freshness check script:
```bash
# Compare latest Git commit timestamp against QMD collection update time
LATEST_GIT_TS=$(git log -1 --format=%ct)
QMD_UPDATED_TS=$(qmd collection list --json | jq '.[] | select(.name=="<collection>") | .updated_at')

if [ "$LATEST_GIT_TS" -gt "$QMD_UPDATED_TS" ]; then
    echo "QMD index is stale. Triggering incremental update..."
    qmd update -c <collection>
fi
```
2. Integrate this check into pre-task dispatch hooks for research and review roles.

---

## Correction C05 — Multi-Repo Default Branch Resolution

- **Target Risk:** `R23` (Git Default Branch Asymmetry) / `R15`
- **Affected Roadmap Phase:** Phase 3 (WSL Migration) & Phase 13 (MasterOfArts Migration)
- **Priority:** **P2 (MEDIUM)**

### Rationale
Live inspection revealed that `acim-secular` uses default branch `master`, while `apexai-os-meta`, `MasterOfArts`, and `Investment` use `main`. Any migration or sync script that hardcodes `origin/main` will fail on `acim-secular`.

### Required Specification & Proposed Change
1. Ensure all orchestration and migration scripts resolve the default branch dynamically:
```bash
DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')
# Fallback to local HEAD if remote HEAD is not set
[ -z "$DEFAULT_BRANCH" ] && DEFAULT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
```
2. Ensure `projects.yaml` and `state.yaml` explicitly declare default branches per repository (already present in `state.yaml`).

---

## Correction Dependency & Execution Order

```text
+-------------------------------------------------------------------------------+
| PHASE 1: RUNTIME PREFLIGHT                                                    |
|  ├── Apply C01 (Sanitize Docker volume mounts in global config)               |
|  ├── Apply C02 (Align WSL execution user & permissions umask)                 |
|  └── Apply C05 (Configure dynamic Git default branch resolution)              |
+---------------------------------------+---------------------------------------+
                                        |
                                        v
+-------------------------------------------------------------------------------+
| PHASES 3–6: WORKSPACE & RETRIEVAL PILOTS                                      |
|  ├── Verify C01 & C02 during ACIM WSL Workspace Pilot                         |
|  └── Apply C04 (Integrate QMD Git timestamp freshness check)                  |
+---------------------------------------+---------------------------------------+
                                        |
                                        v
+-------------------------------------------------------------------------------+
| PHASES 11–12: ROLLUP & AUTOMATION                                             |
|  └── Apply C03 (Implement Fail-Closed Atomic Apex Portfolio Rollup)           |
+-------------------------------------------------------------------------------+
```
