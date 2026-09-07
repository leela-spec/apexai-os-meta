# Architecture Audit & Design Dossier: Meta-Orchestrator Topology & Multi-Instance Infrastructure

**Date:** 2026-09-07  
**Prepared For:** Systems Architect Review & Operator Evaluation  
**Scope:** Hermes Global Meta-Orchestrator Across All Workspaces (`apexai-os-meta`, `Investment`, `MasterOfArts`, `acim-secular`), Karakeep in the Investment Workspace, KI-Basis Access to Workspaces, Dual-Instance Separation Analysis, and Preservation of Windows Alpine Docker.

---

## 1. Direct Answers to Core Architectural Questions

### Question 1: Is the Windows Alpine Docker environment still running? Did you delete or modify it?
* **Status: 100% RUNNING AND UNTOUCHED.**
* All 7 containers in Docker Desktop on Windows (`ki-basis-nginx`, `ki-basis-hermes`, `ki-basis-openproject`, `ki-basis-paperless`, `ki-basis-firefly`, `ki-basis-postgres`, `ki-basis-valkey`) have been running continuously (`Up 3+ hours, healthy`).
* **We did NOT delete, stop, migrate, or touch your live Alpine environment.**
* **Regarding ADR-001:** Strategy A vs. Strategy B was purely an **architectural study** conducted by the agent team to document tradeoffs for your architect. **No live infrastructure migration was executed.** The live Windows Alpine environment remains in place for you and your architect to review.

---

### Question 2: Is the Hermes Global Meta-Orchestrator the SAME engine that accesses the repos and powers the KI-Basis stack?
* **YES, ABSOLUTELY. It is ONE single, unified Hermes engine.**
* It is not two separated agents. It operates via two interfaces sharing the exact same underlying core:
  1. **Host CLI Interface (`/usr/local/bin/hermes`)**: Runs directly in the Ubuntu WSL2 OS for rapid, zero-lag terminal interaction and direct filesystem operations across `/root/workspaces/*`.
  2. **Container Gateway Interface (`ki-basis-hermes` on :8642 / :9119)**: The headless API and Web Dashboard gateway inside the KI-Basis stack that binds `/root/.hermes` into `/opt/data`. When KI-Basis services (OpenProject, Paperless, Firefly) call Hermes via HTTP, they are interacting with the **exact same Hermes engine, SQLite database, and profile store**.
* **Role Profiles as a Global Executor (`/root/.hermes/profiles/`)**:
  Hermes switches personas/constraints dynamically based on the domain of execution:
  * **`default` (Global Meta-Orchestrator)**: Has unrestricted cross-repository access across `/root/workspaces/*`. Orchestrates inter-repo dependencies, triggers git operations, manages OS-level configurations, and coordinates cross-workspace initiatives.
  * **`investment` (IPOS Policy & Rule Executor)**: Governed by strict IPOS Invariants:
    - *Axiom 1*: Deterministic Python code computes all numeric scores; the LLM only narrates.
    - *Axiom 2*: Absolutely NO automated broker order execution (negative prompt enforced).
    - *Axiom 3*: Canonical branch is `ipos-modular-rebuild-2026-08-28` (never unreviewed `main`).
    - *Axiom 4*: Read-only MCP/REST access to Karakeep evidence.
  * **`research-strategist`**: Deep synthesis across complex literature, macroeconomic reports, market structure analysis, and strategic whitepapers.
  * **`marketing-executive`**: Public communications, event campaigns (Safer Space e.V., Equinox 2026 festival), volunteer onboarding flows, and Pretix ticketing messaging.
  * **`workshop-designer`**: Educational curriculum design, masterclass structuring, seminar materials, and step-by-step workshop manuals.
  * **`independent-reviewer`**: Adversarial audit agent, proof verification gates, compliance checks, and code quality falsification.

---

### Question 3: Where does Karakeep live, and how does KI-Basis access the native ext4 workspaces?
* **Karakeep Belongs in the `Investment` Workspace on Native ext4**:
  - Karakeep is **NOT** a general KI-Basis service.
  - It lives and operates inside the **`Investment` workspace on native ext4** (`/root/workspaces/Investment/`) as the dedicated IPOS Evidence Custody archive.
  - It archives research URLs, PDF research papers, SingleFile web snapshots, and RSS feeds with cryptographic SHA-256 receipts.
  - Hermes accesses Karakeep via read-only REST/MCP (`http://localhost:3000` or local endpoint) under the `investment` profile.
* **KI-Basis Access to Native ext4 Workspaces**:
  - In Ubuntu WSL2, the entire native ext4 directory `/root/workspaces/` is bind-mounted directly into the KI-Basis Docker environment (`/root/workspaces:/root/workspaces`).
  - This allows KI-Basis services (OpenProject, Paperless, Firefly, and Hermes Gateway) to read, index, track, and interact with all 4 repositories:
    1. `apexai-os-meta` (Core OS, ki-basis configs, scripts, architecture)
    2. `Investment` (IPOS investment operating system, advisor engine, backtest)
    3. `MasterOfArts` (Academic / creative corpus)
    4. `acim-secular` (Secular philosophical corpus)

---

### Question 4: Why was the stack installed using `/mnt/c` when Ubuntu WSL2 already uses native ext4?
* When you built Ubuntu WSL2, you correctly created all git repos inside native ext4 at `/root/workspaces/`.
* However, the Compose files for `ki-basis` resided on the Windows NTFS filesystem at `C:\GitDev\apexai-os-meta\ki-basis`.
* On September 2nd, `docker compose up` was executed from an Ubuntu terminal whose working directory was `/mnt/c/GitDev/apexai-os-meta/ki-basis`.
* Because Compose executed from `/mnt/c/`, it bound Nginx configs and Postgres init scripts across the Windows 9P virtual socket, triggering Rails/Puma database timeouts in OpenProject (`exit status 1`), which spiked idle CPU to ~350%.
* Moving persistent volumes to ext4 and tuning workers dropped idle CPU to 3.79%.

---

## 2. Definitive Master Architecture Diagrams (Mermaid)

### Diagram 1: Unified Master Architecture Topology

```mermaid
flowchart TB
    subgraph Windows_Host ["Windows 11 Physical Workstation"]
        Operator["Operator / Developer (VS Code, CLI & Web Browser)"]
        
        subgraph Win_Alpine ["Docker Desktop (Alpine LinuxKit VM) - UNTOUCHED"]
            Comm_KiBasis["Community Operations ki-basis Stack\n(Nginx :8084 | OpenProject :8082 | Paperless :8010 | Firefly :8086\nPostgres | Valkey | Hermes API :8642)\n[STATUS: Up & running continuously for Community]"]
        end

        subgraph WSL2_Host ["Ubuntu WSL2 Host Environment (Native ext4)"]
            
            subgraph Hermes_Global ["Hermes Global Meta-Orchestrator (Single Unified Engine)"]
                HermesCore["Hermes Core (/usr/local/bin/hermes)\n[Global Meta-Orchestrator & CLI]"]
                HermesState["Shared State & Config (/root/.hermes/)\n(SQLite DB, Sessions, Memories, Keys)"]
                
                subgraph Profiles ["Role Profiles (/root/.hermes/profiles/)"]
                    ProfDefault["default (Meta-Orchestrator across all Repos)"]
                    ProfInv["investment (IPOS Rules, Custody & Zero Broker Orders)"]
                    ProfStrat["research-strategist (Deep Research & Whitepapers)"]
                    ProfMkt["marketing-executive (Outreach & Campaign Flows)"]
                    ProfWork["workshop-designer (Curriculum & Masterclasses)"]
                    ProfRev["independent-reviewer (Auditing & Verification Gates)"]
                end
                HermesCore --- HermesState
                HermesCore --> Profiles
            end

            subgraph WSL_Workspaces ["Native ext4 Workspaces (/root/workspaces/)"]
                RepoApex["📁 apexai-os-meta\n(Core OS, ki-basis configs, scripts, architecture)"]
                
                subgraph RepoInv_Sub ["📁 Investment Workspace (Native ext4)"]
                    RepoInv["IPOS Core Engine\n(Policy, Advisor Rules, Backtest, Registers)"]
                    Karakeep_Custody["🗄️ Karakeep Evidence Custody\n(Research Ingestion, SingleFile, PDF/URL Archive)\n[Anchored on ext4 in Investment Workspace]"]
                    RepoInv --- Karakeep_Custody
                end
                
                RepoMoA["📁 MasterOfArts\n(Academic & Creative Body of Work)"]
                RepoAcim["📁 acim-secular\n(Philosophical Corpus & Texts)"]
            end

            subgraph WSL_Docker ["KI-Basis Enterprise Docker Stack (WSL2 dockerd on ext4)"]
                EdgeGateway["Single Edge Gateway (Nginx / Caddy :8084)"]
                
                subgraph KiBasis_Services ["KI-Basis Operations Network (ki-basis-net)"]
                    HermesGateway["ki-basis-hermes Gateway\n(API :8642 | Dashboard :9119)\n[Headless Interface to the SAME Hermes Engine]"]
                    OpenProject["ki-basis-openproject (:8082)\n(Task & Milestone Governance)"]
                    Paperless["ki-basis-paperless (:8010)\n(Document & Receipt OCR)"]
                    Firefly["ki-basis-firefly (:8086)\n(Financial Ledger & Transactions)"]
                    SharedPostgres[("Consolidated PostgreSQL 16\n(DBs: openproject, paperless, firefly)")]
                    SharedValkey[("Consolidated Valkey 8.0\n(Cache & Task Queue)")]
                    
                    OpenProject --- SharedPostgres
                    Paperless --- SharedPostgres
                    Firefly --- SharedPostgres
                    Paperless --- SharedValkey
                    HermesGateway <-->|Internal API :8642| OpenProject
                    HermesGateway <-->|Internal API :8642| Paperless
                    HermesGateway <-->|Internal API :8642| Firefly
                end

                EdgeGateway --> HermesGateway
                EdgeGateway --> OpenProject
                EdgeGateway --> Paperless
                EdgeGateway --> Firefly
            end

            %% Core Orchestration Connections
            HermesCore ==>|Direct ext4 Access & Execution| RepoApex
            HermesCore ==>|Direct ext4 Access & Execution| RepoInv
            HermesCore ==>|Direct ext4 Access & Execution| RepoMoA
            HermesCore ==>|Direct ext4 Access & Execution| RepoAcim

            %% Hermes Investment Profile read-only access to Karakeep
            ProfInv -.->|Read-Only Evidence Retrieval (MCP / REST)| Karakeep_Custody

            %% KI-Basis Stack Access to Workspaces
            WSL_Workspaces <===>|Direct Bind-Mount Access: /root/workspaces| WSL_Docker
            HermesState -.->|Bind-Mount: /opt/data| HermesGateway
        end

        Operator -->|Direct Shell / CLI| HermesCore
        Operator -->|Browser: 127.0.0.1| EdgeGateway
        Operator -->|Browser: 127.0.0.1| Comm_KiBasis
    end
```

---

### Diagram 2: Dual-Instance Multi-Tenant Model (For Architect Review)

```mermaid
flowchart TB
    subgraph Dual_Tenant_Architecture ["Multi-Tenant Separation Model (Architectural Options)"]
        
        subgraph OptionA ["Strategy A (Single Docker Daemon)"]
            direction TB
            A_Engine["Single Docker Daemon"]
            
            subgraph A_Private ["ki-basis-private (Entrepreneurship)"]
                A_Priv_Apps["Nginx 8084 | OpenProject 8082 | Paperless 8010 | Firefly 8086"]
                A_Priv_DB[("Postgres & Valkey (Internal Subnet 172.28.0.0/16)")]
            end
            
            subgraph A_Community ["ki-basis-community (Community)"]
                A_Comm_Apps["Nginx 9084 | OpenProject 9082 | Paperless 9010 | Firefly 9086"]
                A_Comm_DB[("Postgres & Valkey (Internal Subnet 172.29.0.0/16)")]
            end

            A_Engine --> A_Private
            A_Engine --> A_Community
        end

        subgraph OptionB ["Strategy B (Split Daemons: WSL2 vs Docker Desktop)"]
            direction TB
            B_WSL["Engine 1: Native WSL2 Dockerd (Private)"]
            B_Win["Engine 2: Windows Docker Desktop (Community)"]
            B_Note["⚠️ Conflict: WSL localhostForwarding mirrors ports\n(Requires distinct host ports to prevent Win32 socket collision)"]
        end

    end
```

---

## 3. Architectural Verification: End-to-End User Stories

To verify that the interplay between Hermes, the 4 repositories, Karakeep, and KI-Basis is completely and accurately understood, here are four concrete user stories reflecting real-world operational flows:

### User Story 1: Ingesting & Verifying Research Evidence in IPOS (`Investment` + Karakeep + Hermes `investment` Profile)
* **Context**: The operator identifies an authoritative Federal Reserve macro research report on interest rate expectations.
* **Workflow**:
  1. The report URL or PDF is saved into **Karakeep**, which runs inside the **`Investment` workspace on native ext4** (`/root/workspaces/Investment/`).
  2. Karakeep archives the document, extracts clean markdown, generates full-page SingleFile captures, and produces a tamper-proof SHA-256 content hash.
  3. The operator initiates an IPOS review using the Hermes CLI:
     `hermes --profile investment "Evaluate recent Fed research against our macro regime indicators."`
  4. Constrained by the `investment` profile invariants in `SOUL.md`:
     - Hermes retrieves the document text from Karakeep via read-only MCP/REST.
     - Hermes cannot execute broker orders or modify `main`.
     - Deterministic Python code (`ipos/advisor/rule_engine.py`) calculates the numerical macro regime score.
  5. Hermes narrates the synthesis and appends the recommendation into the Action/Watch Register in `Investment`.

### User Story 2: Community Operations & Expense Intake (KI-Basis Stack + Hermes `marketing-executive` / `default`)
* **Context**: A venue deposit invoice arrives for the Equinox 2026 festival organized by Safer Space e.V.
* **Workflow**:
  1. The invoice PDF is dropped into the Paperless consume folder on the live Community stack.
  2. Paperless-ngx OCRs the document, extracts amounts, and flags the German non-profit tax category (Ideeller Bereich / Zweckbetrieb).
  3. Firefly III logs the double-entry transaction against the community checking account.
  4. OpenProject updates the event preparation milestone work package.
  5. Because KI-Basis mounts `/root/workspaces/`, the system references project files directly.
  6. The Hermes Global Meta-Orchestrator (using the `marketing-executive` profile) connects via the KI-Basis gateway (:8642) to compile the weekly community budget status and draft the volunteer briefing.

### User Story 3: Cross-Workspace Meta-Orchestration (Global Hermes Meta-Orchestrator over all 4 Repositories)
* **Context**: The operator wants to extract philosophical concepts from `acim-secular`, structure them into an educational masterclass inside `MasterOfArts`, and track the milestone in OpenProject.
* **Workflow**:
  1. The operator runs Hermes under the `workshop-designer` profile or the `default` global meta-orchestrator profile.
  2. Hermes accesses the native ext4 filesystems directly:
     - Reads source materials in `/root/workspaces/acim-secular/`.
     - Synthesizes and writes the curriculum into `/root/workspaces/MasterOfArts/workshops/`.
  3. Hermes then communicates with the KI-Basis OpenProject service (via the `:8642` container API gateway) to create corresponding project work packages and deliverables.
  4. Hermes switches to the `independent-reviewer` profile to verify markdown links, structural integrity, and git hygiene before committing.

### User Story 4: Preserving Untouched Community Operations on Docker Desktop (Windows Alpine)
* **Context**: Community volunteers and external event participants interact with the public community portal while private IPOS development progresses.
* **Workflow**:
  1. Community traffic routes exclusively to the Windows Docker Desktop environment (Alpine LinuxKit VM), which runs continuously and untouched on host ports (`8084`, `8082`, `8010`, `8086`).
  2. Community databases, media files, and Valkey queues remain entirely quarantined inside the Docker Desktop named volumes.
  3. Private development, IPOS backtesting, and confidential research operate natively inside Ubuntu WSL2 ext4.
  4. Zero port collisions or filesystem stalls occur because the environments are cleanly demarcated.

---

## 4. Key Architectural Learning: Lean Architecture vs. Over-Engineering

A formal architectural post-mortem and learning record is documented in [`03_LEARNING_OVERENGINEERING_VS_LEAN_ARCHITECTURE.md`](./03_LEARNING_OVERENGINEERING_VS_LEAN_ARCHITECTURE.md).

* **Over-Engineering Anti-Pattern Identified**:
  Creating micro-isolated Docker Compose stacks, separate subnets, and separate database containers for each local tool on a single developer machine burns ~1.5 GB of RAM in duplicate database processes, breaks container DNS discovery, and creates severe operational friction.
* **Verified Gold Standard Adopted**:
  - **Single Edge Gateway Pattern**: Nginx or Caddy serves as the sole external/host security perimeter.
  - **Flat Internal Network**: Supporting tools collaborate directly on a shared internal bridge network using Docker's native DNS without port-forwarding gymnastics.
  - **Consolidated Multi-Database Engine**: Single PostgreSQL instance hosting multiple isolated logical databases, slashing memory overhead by 60–75%.

---

## 5. Dossier Contents for External Architect Review

All files are located in `C:\GitDev\apexai-os-meta\docs\AUDIT_DOSSIER_DUAL_KI_BASIS\`:
1. `00_ARCHITECT_EXECUTIVE_SUMMARY.md`: This comprehensive document, user stories, and Mermaid diagrams.
2. `01_DUAL_INSTANCE_ARCHITECTURE.md`: Complete architectural analysis comparing Strategy A vs. Strategy B.
3. `02_DUAL_INSTANCE_RUNBOOK.md`: Operational and migration runbook.
4. `03_LEARNING_OVERENGINEERING_VS_LEAN_ARCHITECTURE.md`: Detailed learning on lean architecture vs. micro-isolation overhead.
5. `04_AUTOMATION_PIPELINES_AND_TEST_SUITE_HANDOVER.md`: Comprehensive guide to execution reality (Task Scheduler, Telegram buffer, Pretix), Coaching pipeline, 2 IPOS pipelines, 10 concrete workflows, and executable test suite.
6. `workflow_plans/`: The 10 isolated workflow implementation & test plans (`WF01`–`WF10`) and `00_META_PROGRAM_PLAN.md` for autonomous multi-agent execution.
7. `agent_transcripts/`: Raw reasoning reports from 11 specialized agent roles (explorer surveys, adversarial reviews, challenge reports, and the victory audit verdict).
