---
okf_version: "0.2"
title: ki-basis x86-64 change analysis and reset backup
description: Entry point for the existing Windows/WSL stack analysis, amd64 build plan, and reset evidence.
tags: [ki-basis, planning, backup, amd64]
---

# ki-basis x86-64 change analysis and reset backup

The x86-64 private tools are deployed on the existing WSL Docker engine and shared PG16 cluster. See the [deployment result](05-deployment-result.md) for access, preserved state, verified outcomes and limits. WSL import/reset is excluded.

| Artifact | Value |
|---|---|
| [Deployment result](05-deployment-result.md) | Current service access, operating commands, acceptance evidence and verification limits. |
| [Change analysis](01-change-analysis.md) | Compares existing infrastructure with the supplied package and identifies data/configuration impacts. |
| [x86-64 integration plan](04-wsl-integration-plan.md) | Defines native amd64 builds, isolated compatibility tests, deployment sequence and reset conditions. |
| [amd64 image lock](images.amd64.lock) | Records registry-verified amd64 variants of the package's ten image indexes. |
| [Backup and reset evidence](03-backup-and-reset.md) | Records backup coverage, verification results, limits and recovery steps. |
| [Preflight](00-preflight.md) | Records scope, input priorities and authorization. |
| [Artifact log](log.md) | Records creation of the analysis bundle. |

## Process and purpose

```mermaid
flowchart TD
    A["Inspect package and live stack<br/>Establish the actual change surface"] --> B["Record original service state and mounts<br/>Preserve the reset baseline"]
    B --> C["Copy configuration and stop writers<br/>Preserve keys and cross-service consistency"]
    C --> D["Dump all databases and export WSL<br/>Capture data, images, engine and operating system"]
    D --> E["Restore original running-service set<br/>End the backup interruption"]
    E --> F["Check archive, hashes and isolated DB restores<br/>Verify recoverability and state restoration"]
    F --> G["Resolve amd64 image variants and build plan<br/>Adapt ARM source inputs to the x86 target"]
    G --> H["Deliver analysis, plan and reset evidence<br/>Make implementation reviewable"]
    H --> I["Build authorized amd64 applications and test copied data<br/>Prove compatibility before production changes"]
    I --> J["Apply accepted changes with a fresh backup<br/>Retain a matching reset point"]
```

Failure guard: A registry manifest, readable archive, or successful SQL restore does not prove that the new application builds work. Use the product acceptance cases in the integration plan before deployment.
