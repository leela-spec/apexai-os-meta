# Hermes Multi-Repo Orchestration — Current State Architecture & Interaction Showcase

A technical architecture showcase and interaction blueprint of the live multi-repository AI agent orchestration system.

---

## 1. System Topology & Architecture Overview

The system operates across a dual-environment topology: a **Windows Host Environment** for operator tools and an **Ubuntu WSL2 Environment** running on native Linux ext4 as the canonical execution engine.

```mermaid
flowchart TB
    subgraph HostEnvironment["Windows Host Environment"]
        WinUser["Human Operator / Editors<br/>(Obsidian Vaults, VS Code, Git CLI)"]
        WinUNC["Windows UNC Path Access<br/><code>\\\\wsl.localhost\\Ubuntu\\root\\workspaces\\...</code>"]
        WinUser <===> WinUNC
    end

    subgraph WSLEnvironment["WSL2 Ubuntu Native ext4 Engine"]
        subgraph WorkspacesRoot["Canonical Workspace Directory (<code>/root/workspaces/</code>)"]
            WS_Apex["<b>apexai-os-meta</b><br/>Branch: <code>main</code><br/>Control Plane & Governance"]
            WS_MOA["<b>MasterOfArts</b><br/>Branch: <code>main</code><br/>Lika, IPOS, Health, BMAD"]
            WS_ACIM["<b>acim-secular</b><br/>Branch: <code>master</code><br/>Secular Edition & Finders"]
            WS_Inv["<b>Investment</b><br/>Branch: <code>main</code><br/>IPOS Engine, Advisor, Backtest"]
        end

        subgraph HermesRuntime["Hermes Multi-Agent Engine (v0.20.5)"]
            HermesCore["Hermes Agent Core CLI & TUI"]
            Profiles["Reusable Role Profiles<br/>(research-strategist, reviewer, etc.)"]
            KanbanStores["Per-Repo Kanban SQLite DBs<br/>(apex, moa, acim, investment)"]
            LearnedSkills["Runtime Deployed Skills<br/>(<code>/root/.hermes/skills/learned/</code>)"]
        end

        subgraph QMDRuntime["QMD Search & Vector Engine (v2.8.3)"]
            QMDCore["QMD CLI & MCP Server"]
            QMDIndex["SQLite Vector & AST Index<br/>(<code>/root/.cache/qmd/index.sqlite</code>)"]
            Collections["7 Scoped Named Collections<br/>(apex, investment, acim, moa-*)"]
            ReceiptGates["Git-HEAD Freshness Receipts<br/>(<code>implementation/evidence/receipts/</code>)"]
        end

        subgraph Sandboxing["Docker Worker Sandbox"]
            WorkerContainer["Task-Scoped Container<br/>(<code>/workspace:rw</code>)"]
            SecurityPolicy["Credential Isolation & Socket Exclusion"]
        end

        subgraph Automation["Systemd Automation"]
            RollupTimer["Systemd Daily Timer<br/>(09:00:00 Persistent)"]
            Publisher["Atomic Rollup Script<br/>(<code>apex_portfolio_rollup.py</code>)"]
            Snapshots["Portfolio Snapshot & Health State"]
        end
    end

    WinUNC <===> WorkspacesRoot
    HermesCore <--> Profiles
    HermesCore <--> KanbanStores
    Profiles --> WorkerContainer
    WorkerContainer <--> WorkspacesRoot
    SecurityPolicy -.-> WorkerContainer
    HermesCore <--> QMDCore
    QMDCore <--> Collections
    Collections <--> QMDIndex
    ReceiptGates -.-> QMDCore
    RollupTimer --> Publisher
    Publisher --> KanbanStores
    Publisher --> WorkspacesRoot
    Publisher --> Snapshots
```

---

## 2. Component Matrix & Workspace Registry

| Repository | Remote URL | WSL Canonical Workspace | Windows UNC Path | Active Branch | Primary Responsibilities |
|---|---|---|---|:--:|---|
| **`apex`** | `leela-spec/apexai-os-meta` | `/root/workspaces/apexai-os-meta` | `\\wsl.localhost\Ubuntu\root\workspaces\apexai-os-meta` | `main` | Global control plane, shared skill canonical source, portfolio status aggregation. |
| **`masterofarts`** | `leela-spec/MasterOfArts` | `/root/workspaces/MasterOfArts` | `\\wsl.localhost\Ubuntu\root\workspaces\MasterOfArts` | `main` | Multi-domain hub: Lika Shift Planning, Health dossiers, BMAD agile framework, MarketingSkills. |
| **`acim`** | `leela-spec/acim-secular` | `/root/workspaces/acim-secular` | `\\wsl.localhost\Ubuntu\root\workspaces\acim-secular` | `master` | Secular ACIM text processing and practice finders. |
| **`investment`** | `leela-spec/Investment` | `/root/workspaces/Investment` | `\\wsl.localhost\Ubuntu\root\workspaces\Investment` | `main` | IPOS Quantitative Macro Engine, 126-rule advisor, backtesting suite, DuckDB warehouse. |

---

## 3. Module Connection Blueprints

```mermaid
graph TD
    classDef repo fill:#1e293b,stroke:#475569,stroke-width:2px,color:#f8fafc;
    classDef core fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef search fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#f8fafc;
    classDef sec fill:#450a0a,stroke:#f87171,stroke-width:2px,color:#f8fafc;

    Hermes["Hermes Core Engine"]:::core
    Kanban["Kanban SQLite DBs<br/>(4 Isolated Files)"]:::core
    QMD["QMD Search Engine<br/>(7 Collections)"]:::search
    Freshness["Git-HEAD Freshness Gate"]:::search
    Docker["Docker Worker Container"]:::sec
    Systemd["Linux Systemd Timer"]:::core
    Rollup["Atomic Rollup Publisher"]:::core

    MOA_Repo["MasterOfArts Repo"]:::repo
    BMAD["BMAD Agile Method"]:::repo
    MKTG["MarketingSkills"]:::repo

    Inv_Repo["Investment Repo"]:::repo
    Advisor["Macro Rule Advisor (775 lines)"]:::repo
    Backtest["Backtesting Engine (347 lines)"]:::repo

    Apex_Repo["Apex AIOS Meta Repo"]:::repo
    SharedSkills["Canonical Shared Skills Source"]:::repo

    Hermes <-->|Task Locking & Status| Kanban
    Hermes <-->|MCP Protocol / CLI| QMD
    Freshness -.->|Validates SHA before query| QMD
    Hermes -->|Dispatches task execution| Docker
    Docker <-->|Task-Scoped Bind Mount| Inv_Repo
    Docker <-->|Task-Scoped Bind Mount| MOA_Repo

    MOA_Repo --- BMAD
    MOA_Repo --- MKTG
    BMAD <-->|Retrieves epics/specs| QMD

    Inv_Repo --- Advisor
    Inv_Repo --- Backtest

    Systemd -->|Fires Daily 09:00:00| Rollup
    Rollup -->|Queries state| Kanban
    Rollup -->|Queries Git HEADs| Apex_Repo
    Rollup -->|Queries Git HEADs| Inv_Repo
    Rollup -->|Queries Git HEADs| MOA_Repo

    Apex_Repo --- SharedSkills
    SharedSkills -->|Deploys reviewed code| Hermes
```

---

### Detailed Interaction Specifications

#### A. Hermes $\longleftrightarrow$ Kanban Task Isolation
- **Storage:** Dedicated SQLite databases at `/root/.hermes/kanban/boards/<board>/kanban.db`.
- **Concurrency Contract:** `review_dispatch: false` is locked across all profile configs. Tasks are executed sequentially by active worker lanes.
- **Data Boundary:** Boards are strictly siloed; tasks in one board cannot query or alter tasks in another.

#### B. Hermes / Profiles $\longleftrightarrow$ QMD Semantic Search
- **Integration:** Reusable profiles (`research-strategist`, `independent-reviewer`) interface with QMD via Model Context Protocol (MCP) and direct CLI search.
- **Collection Scope:** Queries are directed to specific collections:
  - `apex` $\rightarrow$ Control plane docs & epics.
  - `investment` $\rightarrow$ IPOS macro plans, indicators, and scoring models.
  - `acim` $\rightarrow$ Secular ACIM text and tools.
  - `moa-lika`, `moa-ipos`, `moa-acim`, `moa-health` $\rightarrow$ Specialized MasterOfArts domains.
- **Freshness Gate:** Each collection maintains a deterministic receipt (`qmd-refresh-receipt-<collection>.yaml`). Queries check live `git rev-parse HEAD` against the receipt; stale collections trigger re-indexing before retrieval.

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Hermes Reusable Role
    participant Gate as Freshness Gate (Receipt Check)
    participant QMD as QMD Vector Engine
    participant Workspace as Target Repository

    Agent->>Gate: Verify collection freshness ('investment')
    Gate->>Workspace: git rev-parse HEAD
    Gate->>Gate: Compare with receipt SHA
    alt Live HEAD == Receipt SHA
        Gate-->>Agent: Verification PASS (Fresh)
    else Live HEAD != Receipt SHA
        Gate->>QMD: qmd update && qmd embed -c investment
        Gate->>Gate: Write updated refresh receipt
        Gate-->>Agent: Re-indexing Complete (Fresh)
    end
    Agent->>QMD: qmd search "macro implementation plan" -c investment
    QMD-->>Agent: Scored, ranked semantic snippets & AST nodes
```

#### C. BMAD Method & MarketingSkills $\longleftrightarrow$ MasterOfArts & QMD
- **Scoping Rule:** BMAD (Agile Method / Sprint Planning) and MarketingSkills are strictly **repo-local** to `MasterOfArts`.
- **Interaction with QMD:** Inside `MasterOfArts`, BMAD agents query sprint backlogs and epics through scoped QMD collections (`moa-lika`, `moa-ipos`, `moa-acim`, `moa-health`).
- **Isolation:** Agents working in `acim-secular` or `Investment` do not load BMAD or Marketing tools.

#### D. Docker Sandbox $\longleftrightarrow$ Workspace & Credential Security
- **Task-Scoped Bind Mounting:** Docker worker containers bind only the active task workspace (`-v /root/workspaces/<repo>:/workspace:rw`). Sibling repository mounts are excluded.
- **Host Persistence:** File modifications and Git commits created inside `/workspace` persist on the host filesystem immediately upon container completion.
- **Credential Boundary:** Host environment variables are blocked by default. Only explicit entries in `terminal.docker_forward_env` pass into the container.
- **Docker Socket Security:** `/var/run/docker.sock` is absent from worker containers to prevent host privilege escalation.

```mermaid
graph LR
    subgraph HostEnvironment["WSL2 Host Environment"]
        HostSecrets["Host Secrets & Environment<br/><code>HOST_CANARY_SECRET=***</code>"]
        AllowlistedVar["Allowlisted Variable<br/><code>ALLOWED_VAR=***</code>"]
        HostWS["Host Target Workspace<br/><code>/root/workspaces/Investment</code>"]
    end

    subgraph DockerContainer["Worker Sandbox Container"]
        ContainerSecrets["Host Secrets: <b>ABSENT (Blocked)</b>"]
        ContainerAllow["Allowlisted Var: <b>PRESENT</b>"]
        ContainerWS["Container Workspace<br/><code>/workspace (rw)</code>"]
    end

    HostWS ===|Task-Scoped Bind Mount| ContainerWS
    HostSecrets -.->|Blocked by Security Policy| ContainerSecrets
    AllowlistedVar -->|Explicit docker_forward_env| ContainerAllow
```

#### E. Linux Systemd $\longleftrightarrow$ Atomic Portfolio Rollup Publisher
- **Execution:** Managed by a native Linux systemd timer (`apex-portfolio-rollup.timer`) executing daily at 09:00:00 (`Persistent=true`).
- **Resource Footprint:** Pure Python, Git CLI, and SQLite queries; consumes **0 LLM tokens**.
- **Atomic Swap:** Outputs `portfolio-snapshot.json` and `portfolio-snapshot.md` via `tempfile` + `os.replace`.
- **Fail-Closed Protection:** If any repository branch mismatches or a board query fails, the publication halts, the existing valid snapshot remains untouched, and a degraded receipt (`health-receipt.yaml`) is emitted.

```mermaid
flowchart TD
    Start([Systemd Timer: Daily 09:00:00]) --> Query[Query 4 Repositories & 4 Kanban DBs]
    Query --> Validate{All Inputs Valid & Branches Match?}

    Validate -- YES --> TempWrite[Write Temporary JSON & Markdown Artifacts]
    TempWrite --> AtomicSwap[Atomically Replace via os.replace]
    AtomicSwap --> HealthyReceipt[Emit health-receipt.yaml: HEALTHY]
    HealthyReceipt --> Done([Rollup Completed Successfully])

    Validate -- NO --> Abort[ABORT PUBLICATION]
    Abort --> Preserve[Preserve Last-Known-Good Snapshot]
    Preserve --> DegradedReceipt[Emit health-receipt.yaml: DEGRADED_BLOCKED]
    DegradedReceipt --> FailDone([Exit with Non-Zero Status])
```

#### F. Shared-Skill Promotion & Deployment Pipeline
- **Candidate Ingestion:** Procedural skills are hashed with SHA-256.
- **Independent Classification:** An independent reviewer evaluates whether the procedure is **generic** or **project-specific**.
- **Repository Boundary:** Project-specific logic remains within the source repository. Generic procedures are staged in the Apex Git control plane (`apex-meta/skills/shared/<name>/SKILL.md`).
- **Runtime Deployment:** Staged skills are deployed into `/root/.hermes/skills/learned/<name>/SKILL.md` and verified against the canonical hash.

```mermaid
flowchart LR
    DiscoveredSkill[Discovered Procedure Candidate] --> Hash[Deterministic SHA-256 Hashing]
    Hash --> Classifier{Independent Review Classification}

    Classifier -- "Project-Specific Logic" --> RetainLocal[Retain in Project Repository Only]
    Classifier -- "Generic Reusable Procedure" --> ApproveShared[Approve for Promotion]

    ApproveShared --> Staging[Stage in Apex Git Source<br/><code>apex-meta/skills/shared/</code>]
    Staging --> RuntimeDeploy[Deploy to Hermes Runtime<br/><code>/root/.hermes/skills/learned/</code>]
    RuntimeDeploy --> HashVerify[Verify SHA-256 Match]
```

---

## 4. Current Operating Principles

1. **Native ext4 Execution:** All active agent operations, builds, Docker runs, and QMD vector indexing execute within `/root/workspaces/` on Linux ext4. Windows tools access these checkouts directly via UNC paths (`\\wsl.localhost\Ubuntu\root\workspaces\...`).
2. **Single Trunk Discipline:** Commits are made directly to `main` (or `master` for `acim-secular`). Long-lived feature branches and worktrees are avoided to maintain trunk clarity.
3. **Living State Discipline:** Working sessions end by updating the repository living index (`PROJECT_STATE.md` / `AGENTS.md`), ensuring full operational continuity without dependence on chat transcripts.
4. **Deterministic Computation:** Mathematical calculations, signal transformations, backtests, and score aggregations are computed entirely by Python and DuckDB. LLMs perform strictly last-mile narrative synthesis.
5. **Fail-Closed State Management:** Partial failures halt automated publication rather than generating synthetic or degraded replacement figures.

---

## 5. Technical Constraints & Future Research

### Current System Constraints
- **Gateway Concurrency Scoping:** Hermes evaluates worker concurrency limits per Kanban board rather than across the entire gateway process. To ensure isolation, the system operates in sequential single-role execution.
- **Profile Memory Walls:** Hermes does not implement multi-tenant memory sandboxing in its central daemon. Fact persistence is managed via repository files while profile `memories/` directories remain empty.
- **CWD Normalization:** Profile working directories are normalized to `.` with empty volume binds to ensure task-specific Docker mounts always govern container execution.

### High-Value Research Frontiers
1. **Multi-Repo AST Knowledge Graph Retrieval:** Developing multi-hop cross-repository graph search by traversing QMD AST nodes and symbol references.
2. **Automated Deterministic Patch Engine:** Advancing dry-run exact-match patch application logic to automatically validate multi-file diffs against live repositories before operator review.
3. **Continuous Quantitative Backtesting Pipelines:** Integrating the IPOS backtesting engine (`ipos/backtest/engine.py`) into scheduled systemd workflows for weekly walk-forward parameter simulation.
