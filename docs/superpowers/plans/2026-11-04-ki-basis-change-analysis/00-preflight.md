---
type: Plan
id: PLAN-KI-BASIS-PREFLIGHT-20261104
title: ki-basis change analysis preflight
description: Scope, source priorities, and execution boundaries for the laptop package analysis and reset backup.
status: current
tags: [ki-basis, backup, planning]
---

# ki-basis change analysis preflight

Target: Analyse the supplied laptop package against the existing stack and create a recoverable reset backup.

Scope: Inspect, back up, verify, plan, and execute the authorized private x86-64 integration. WSL import/reset and changes to unrelated stacks are excluded.

Authorization: The operator confirmed the process and explicitly authorized live inspection and consistent backup despite the workstation WSL restriction.

| Priority | Input | Purpose |
|---|---|---|
| 1 | Supplied INSTALL.md and MANIFEST.txt | Establish package intent and included artifacts. |
| 2 | Packaged compose files, overrides, template, and installer | Verify actual installation behavior. |
| 3 | Live Docker inspection and PostgreSQL inventory | Establish current services, data, mounts, and state. |
| 4 | ki-basis/docs/INFRASTRUCTURE.md and close-out PLAN.md | Cross-check documented topology and recovery constraints. |
| 5 | Existing backup scripts | Determine whether existing procedures fit the live stack. |

Output: [Change analysis](01-change-analysis.md), [x86-64 integration plan](04-wsl-integration-plan.md), [verified amd64 image pins](images.amd64.lock), and [backup and reset evidence](03-backup-and-reset.md).

Active step: Report the deployed x86-64 tools and the verified outcomes in [deployment result](05-deployment-result.md).

Reuse finding: Existing backup scripts assume obsolete database container names and cannot provide this reset point unchanged.

Failure guard: Never run the installer or restore over production during this analysis.
