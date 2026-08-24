# 01 — D01–D10 Decision-by-Decision Adversarial Audit

- **Program:** Hermes Multi-Repo Orchestration v2
- **Repository:** `leela-spec/apexai-os-meta` (`main`)
- **Evaluation Date:** 2026-08-24
- **Reviewer Role:** Independent Architecture & Safety Evaluator
- **Governing Handover:** [14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md](../../14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md)
- **Status:** **COMPLETE**

---

## Audit Methodology & Evidence Standard

Every claim, test, and risk in this audit is classified using the strict validation labels:
- `EXECUTED` — Non-destructive verification performed directly on the live host/runtime.
- `STATIC_SIMULATION` — Explicit tabletop state-transition and failure-injection analysis.
- `SOURCE_VERIFIED` — Confirmed directly via official upstream documentation or repository source code.
- `INFERENCE` — Logical deduction derived from architectural constraints (not treated as raw fact).
- `UPSTREAM_DOC` / `UPSTREAM_ISSUE` / `REPO_EVIDENCE` — Specific primary source classifications.

---

## Decision D01 — Apex AIOS Meta as Portfolio Control Plane

- **Status in Architecture Ledger:** `ACCEPTED`
- **Validation Verdict:** **`PASS`**
- **Decision File:** [`decisions/D01-APEX-CONTROL-PLANE.md`](../../decisions/D01-APEX-CONTROL-PLANE.md)

### 1. Exact Claim Validated
`leela-spec/apexai-os-meta` serves as the durable portfolio and orchestration control plane, while managed repositories (`MasterOfArts`, `acim-secular`, `Investment`, `apexai-os-meta`) retain canonical ownership of their own project truth, files, and Git histories. No project-content warehouse or wholesale file mirroring into Apex is permitted.

### 2. Strongest Supporting Evidence
- **Single Source of Truth (`SOURCE_VERIFIED` / `UPSTREAM_DOC`):** Aligns with Google Multi-Agent Architecture and Anthropic Agentic Design Principles by isolating the control plane from the execution/data plane.
- **Git Authority Boundary (`REPO_EVIDENCE`):** Each managed repo possesses independent commit histories, distinct branch structures (`acim-secular` on `master`, others on `main`), and project-specific licensing.
- **Zero Token Duplication (`SOURCE_VERIFIED`):** Storing project files in source repos avoids multi-megabyte context pollution in Apex orchestrator sessions.

### 3. Strongest Contradicting & Risk Evidence
- **Drift Risk (`STATIC_SIMULATION`):** Cross-project decision objects in Apex can drift from actual implementation state in source repos if references are not validated during reviews.
- **Stale Rollup Illusion (`INFERENCE`):** Operators may mistakenly treat derived Apex rollup summaries as authoritative project facts rather than point-in-time snapshots.

### 4. Hidden Couplings & Dependencies
- Depends on source repositories maintaining clear internal governance (`AGENTS.md`) and standard Git hygiene.
- Relies on read-only reference pointers (`source_board`, `source_task_id`, `repo_path`) rather than active synchronization.

### 5. Token, Latency & Operational Cost
- **Provider Tokens:** 0 tokens for storage; on-demand tokens only when reading derived summaries.
- **Latency:** Instantaneous local access.
- **Operational Cost:** Minimal; standard Git version control.

### 6. Failure Modes & Mitigations
- *Failure Mode:* Apex starts copying project KBs to "ease access".
  - *Mitigation:* Explicit decision invariant forbidding project mirroring (`V5`); enforced via PR review and directory structure policies.
- *Failure Mode:* Stale portfolio decisions.
  - *Mitigation:* Rollup and decision objects must include mandatory ISO 8601 generation timestamps and source Git commit SHAs.

### 7. Revisit / Invalidation Triggers
- Upstream Hermes introduces a native, zero-copy multi-repo workspace manager that provides transactional cross-repo guarantees without file duplication.

---

## Decision D02 — Kanban Topology: Separate Repo Boards + Asynchronous Apex Rollup

- **Status in Architecture Ledger:** `ACCEPTED 2026-08-24`
- **Validation Verdict:** **`PASS`**
- **Decision File:** [`decisions/D02-KANBAN-TOPOLOGY.md`](../../decisions/D02-KANBAN-TOPOLOGY.md)

### 1. Exact Claim Validated
Use one dedicated Hermes Kanban board per managed repository (`apex`, `masterofarts`, `acim`, `investment`) backed by isolated SQLite databases. Reject Hermes tenants as the security/memory boundary. Aggregate board statuses asynchronously into a read-only Apex portfolio rollup via deterministic scripting.

### 2. Strongest Supporting Evidence
- **Hard Storage Isolation (`EXECUTED` / `UPSTREAM_DOC`):** Live execution of `hermes kanban boards list --json` confirms each board receives an independent SQLite database (e.g., `/root/.hermes/kanban.db` vs `/root/.hermes/kanban/boards/website-research/kanban.db`).
- **Tenant Memory Pollution Defect (`UPSTREAM_ISSUE` #85497):** Primary upstream issue #85497 proves tenant-level memory namespacing is not enforced by the Hermes runtime; workers across tenants write to shared profile memory. Board isolation avoids this bug entirely.
- **Zero Model Cost Rollup (`SOURCE_VERIFIED`):** `hermes kanban --board <slug> list --json` enables 100% deterministic, zero-token JSON aggregation.

### 3. Strongest Contradicting & Risk Evidence
- **Lack of Native Cross-Board DAG (`UPSTREAM_DOC`):** Hermes explicitly forbids `kanban_link` dependencies across boards, preventing native automatic task triggers across repos.
- **Partial Query Publication Risk (`STATIC_SIMULATION`):** A transient failure in reading one board's SQLite database could cause a naive rollup script to omit that repo, falsely reporting zero active tasks.

### 4. Hidden Couplings & Dependencies
- The rollup script depends on the stability of `hermes kanban --board <slug> list --json` output schema.
- Cross-project dependencies require explicit Apex tracking records.

### 5. Token, Latency & Operational Cost
- **Provider Tokens:** $0.00 (Zero remote LLM calls for rollup generation).
- **Compute:** < 250ms local CPU execution per rollup run.

### 6. Failure Modes & Mitigations
- *Failure Mode:* Rollup script publishes incomplete data when one board query times out.
  - *Mitigation:* Rollup script must implement **Fail-Closed Semantics** (Correction C03): if any configured board fails, abort snapshot generation and record a degraded health receipt.

### 7. Revisit / Invalidation Triggers
- Upstream Hermes resolves #85497, implements verified tenant memory isolation, and provides cross-tenant dependency graphs within a single board.

---

## Decision D03 — Reusable Role Profiles Across Repositories (Sequential Execution)

- **Status in Architecture Ledger:** `ACCEPTED WITH CONSTRAINTS`
- **Validation Verdict:** **`PASS_WITH_CONDITIONS`**
- **Decision File:** [`decisions/D03-REUSABLE-ROLE-PROFILES.md`](../../decisions/D03-REUSABLE-ROLE-PROFILES.md)

### 1. Exact Claim Validated
Hermes profiles represent durable roles (`research-strategist`, `independent-reviewer`, `portfolio-orchestrator`, `workshop-designer`, `marketing-executive`) rather than repositories. Profiles are reused sequentially across repositories. Concurrent execution of multiple worker processes sharing the same writable profile is strictly forbidden.

### 2. Strongest Supporting Evidence
- **Upstream Process Isolation Rule (`UPSTREAM_DOC` / `SOURCE_VERIFIED`):** Official Hermes Profiles documentation states: *"Never point two agent processes at the same profile."* Agents automatically write to profile memory at session end; concurrent writers corrupt memory and SQLite state.
- **Concurrency Limit Scope Defect (`UPSTREAM_ISSUE` #78122):** Upstream issue #78122 confirms `max_in_progress_per_profile` is enforced per board, not gateway-wide. If four boards run simultaneously, four workers with the same profile could be spawned concurrently.
- **Compounding Procedural Skill (`REPO_EVIDENCE`):** MasterOfArts pilot evidence (`P13`, `P14`) proved specialist profiles build procedural proficiency when applied to different tasks.

### 3. Strongest Contradicting & Risk Evidence
- **Throughput Constraint (`INFERENCE`):** Sequential execution restricts parallel execution throughput across repositories.
- **Path Leakage via Profile Config (`EXECUTED`):** Live inspection of `/root/.hermes/profiles/*/config.yaml` shows profile configs can inherit global cwd or tool configurations. If a profile hardcodes a workspace, cross-repo reuse breaks.

### 4. Hidden Couplings & Dependencies
- Requires global execution locking or Safe Mode A orchestration to prevent accidental concurrent dispatch of the same profile across boards.

### 5. Token, Latency & Operational Cost
- **Provider Tokens:** Profile `MEMORY.md` (~2,200 chars / ~550 tokens) and `USER.md` (~1,375 chars / ~350 tokens) are loaded on session start. Reusing thin profiles keeps startup overhead under 1,000 tokens.

### 6. Required Conditions & Mitigations
- **Condition:** All reusable role profile definitions must be strictly stripped of repo-specific `terminal.cwd` and static volume mounts.
- **Condition:** Enforce single-process execution per profile via Safe Mode A or deterministic script locks.

---

## Decision D04 — Learning Spillover via Reviewed Agent Skills

- **Status in Architecture Ledger:** `ACCEPTED WITH CONSTRAINTS`
- **Validation Verdict:** **`PASS`**
- **Decision File:** [`decisions/D04-LEARNING-SPILLOVER.md`](../../decisions/D04-LEARNING-SPILLOVER.md)

### 1. Exact Claim Validated
Raw Hermes profile memory stays profile-local. Project facts remain in their source repository. Cross-repo and cross-role knowledge spillover occurs exclusively through independently reviewed, generalized procedures promoted as Agent Skills. No raw `MEMORY.md` synchronization between profiles or repos.

### 2. Strongest Supporting Evidence
- **Context Hygiene & Factual Contamination (`STATIC_SIMULATION`):** Copying raw memory across repos would inject Investment ticker facts or confidential credentials into ACIM spiritual analysis, causing severe context pollution and privacy breach.
- **Progressive Disclosure Standard (`SOURCE_VERIFIED` / `UPSTREAM_DOC`):** Agent Skills (`agentskills.io`) use progressive disclosure: metadata (~30–50 tokens) is indexed at startup; instructions load only upon explicit activation.
- **Zero-Token Candidate Discovery (`SOURCE_VERIFIED`):** Deterministic SHA-256 hash comparison of learned skills in `~/.hermes/profiles/<role>/skills/learned/` identifies new candidates at zero model token cost.

### 3. Strongest Contradicting & Risk Evidence
- **Spillover Latency (`INFERENCE`):** Learning is delayed (batched/scheduled) rather than instantaneous.
- **Cognitive Review Overhead (`STATIC_SIMULATION`):** Semantic generalization review consumes model tokens when candidates change.

### 4. Hidden Couplings & Dependencies
- Depends on the `independent-reviewer` role properly sanitizing domain-specific paths, credentials, and project facts before promoting to Apex Git.

### 5. Token, Latency & Operational Cost
- **Candidate Detection:** $0.00 (Local Python/Bash hashing script).
- **Semantic Review:** ~2,000–4,000 tokens per changed candidate (only when new procedures are detected).

### 6. Failure Modes & Mitigations
- *Failure Mode:* Unreviewed auto-promotion of learned skills causes skill catalog bloat.
  - *Mitigation:* Two-stage promotion gate: Stage 1 (deterministic hash inventory) -> Stage 2 (mandatory `independent-reviewer` evaluation).

---

## Decision D05 — Apex as Reviewed Shared-Skill Canonical Source

- **Status in Architecture Ledger:** `ACCEPTED DIRECTION / PILOT REQUIRED`
- **Validation Verdict:** **`PASS_WITH_CONDITIONS`**
- **Decision File:** [`decisions/D05-SHARED-SKILL-SOURCE.md`](../../decisions/D05-SHARED-SKILL-SOURCE.md)

### 1. Exact Claim Validated
Apex becomes the canonical Git source for reviewed project-neutral shared skills after a live pilot. Runtime learned-skill scratch state remains separate from canonical Git source.

### 2. Strongest Supporting Evidence
- **Self-Modification Vulnerability (`UPSTREAM_DOC` / `SOURCE_VERIFIED`):** Hermes official skills documentation confirms that writable directories configured under `skills.external_dirs` can be modified in-place by the agent's built-in `skill_manage` tool.
- **Version Control & Rollback (`REPO_EVIDENCE`):** Storing reviewed skills in Apex Git provides commit history, diff auditing, and instantaneous rollback capability.

### 3. Strongest Contradicting & Risk Evidence
- **Deployment Divergence Risk (`STATIC_SIMULATION`):** If the deployment mechanism from Apex Git to the runtime skills directory is manual or ad-hoc, runtime skills will drift from Git truth.

### 4. Hidden Couplings & Dependencies
- Requires a deterministic deployment step (symlink or export script) that synchronizes Apex Git skills to the runtime environment without granting the agent write-access to Apex Git.

### 5. Token, Latency & Operational Cost
- Zero token overhead; standard filesystem discovery.

### 6. Required Conditions & Mitigations
- **Condition:** The runtime deployment path must be strictly read-only for agent processes or maintained via a deterministic promotion script with SHA verification.
- **Condition:** Phase 10 pilot must validate discovery across at least two distinct role profiles before general enablement.

---

## Decision D06 — BMAD and Domain-Specific Skill Placement Policy

- **Status in Architecture Ledger:** `ACCEPTED`
- **Validation Verdict:** **`PASS`**
- **Decision File:** [`decisions/D06-BMAD-AND-DOMAIN-SKILLS.md`](../../decisions/D06-BMAD-AND-DOMAIN-SKILLS.md)

### 1. Exact Claim Validated
BMAD remains repo-local in every repository that actively uses it. MarketingSkills remains MasterOfArts-only until another repo establishes a concrete marketing requirement. Apex KB remains Apex-specific. No custom global BMAD linker or global domain-skill dumping.

### 2. Strongest Supporting Evidence
- **BMAD Project Architecture (`SOURCE_VERIFIED` / `UPSTREAM_DOC`):** Official BMAD Method documentation (`npx bmad-method install`) establishes project-local `_bmad/` and `_bmad-output/` state structures.
- **BMAD Global Link Proposal Status (`UPSTREAM_ISSUE` #1728):** Upstream issue #1728 (global link/unlink) is an open community proposal, not a stabilized feature. Relying on custom global symlinks would introduce brittle unverified plumbing.
- **MarketingSkills Context Scope (`SOURCE_VERIFIED`):** MarketingSkills v2.1 relies on `.agents/product-marketing.md`, which is strictly MasterOfArts product context. Installing 49 marketing skills into ACIM or Investment adds prompt clutter and tool-selection ambiguity without benefit.

### 3. Strongest Contradicting & Risk Evidence
- **Disk Redundancy (`INFERENCE`):** Minor duplication of BMAD tool files across repos on disk (~15MB per repo). (Negligible compared to context isolation benefits).

### 4. Hidden Couplings & Dependencies
- Apex capability registry must record which repos use which framework versions.

### 5. Token, Latency & Operational Cost
- **Prompt Token Savings:** Saves ~1,500–3,000 tokens of skill catalog metadata per session in ACIM, Investment, and Apex by omitting irrelevant marketing and agile tools.

### 6. Failure Modes & Mitigations
- *Failure Mode:* Uncontrolled version drift between BMAD installations across repos.
  - *Mitigation:* Document installed BMAD versions in `state.yaml` and update deliberately per repo.

---

## Decision D07 — Canonical WSL Workspace Migration

- **Status in Architecture Ledger:** `ACCEPTED / MIGRATION NOT AUTHORIZED`
- **Validation Verdict:** **`PASS_WITH_CONDITIONS`**
- **Decision File:** [`decisions/D07-WSL-CANONICAL-WORKSPACE.md`](../../decisions/D07-WSL-CANONICAL-WORKSPACE.md)

### 1. Exact Claim Validated
Converge each managed repository to one canonical WSL2 Linux ext4 checkout under a common root (`~/workspaces/`). Windows accesses files via `\\wsl.localhost\Ubuntu\...`. Maintain no parallel live Windows checkouts. Reconcile differences via pre-migration divergence audit; do not delete old Windows copies automatically.

### 2. Strongest Supporting Evidence
- **WSL Filesystem Performance Guidance (`UPSTREAM_DOC` / `SOURCE_VERIFIED`):** Microsoft official documentation explicitly advises keeping Linux development files in the Linux filesystem; accessing `/mnt/c/GitDev` from WSL Linux tools incurs heavy 9P cross-filesystem protocol latency during Git and build operations.
- **Docker Desktop Recommendation (`UPSTREAM_DOC`):** Docker independently recommends storing source files in the Linux distribution for high-performance Linux container bind mounts.
- **Elimination of Dual-Authority Drift (`STATIC_SIMULATION`):** Running two active checkouts (one in Windows, one in WSL) inevitably leads to untracked local edits, merge conflicts, and lost work.

### 3. Strongest Contradicting & Risk Evidence
- **Windows File Explorer Latency (`UPSTREAM_DOC`):** High-frequency file indexing from Windows applications over `\\wsl.localhost` can experience 9P overhead. (Mitigated because heavy tool execution runs natively inside WSL).
- **Root vs Non-Root User Discrepancy (`EXECUTED` / Risk R22):** Live inspection reveals the MasterOfArts pilot was installed under `/root/` as the root user. Migrating to `~/workspaces/` under a standard Linux user requires reconciling Linux file ownership (`chown`) and Hermes configuration paths (`/root/.hermes` vs `~/.hermes`).

### 4. Hidden Couplings & Dependencies
- Requires updating Windows IDE paths, scripts, and terminal shortcuts to point to `\\wsl.localhost\Ubuntu\...`.

### 5. Required Conditions & Mitigations
- **Condition:** Enforce pre-migration divergence audit script (comparing HEAD SHA, uncommitted diffs, untracked files, and branch names) before freezing any Windows repository.
- **Condition:** Standardize Linux execution identity (Root vs Standard User) and file creation mask (`umask 022`) prior to migration.

---

## Decision D08 — QMD Multi-Repo Retrieval (Single Local Engine, Scoped Collections)

- **Status in Architecture Ledger:** `ACCEPTED / LIVE ACCEPTANCE PENDING`
- **Validation Verdict:** **`PASS`**
- **Decision File:** [`decisions/D08-QMD-MULTI-REPO.md`](../../decisions/D08-QMD-MULTI-REPO.md)

### 1. Exact Claim Validated
One machine-level QMD engine indexes curated named collections across all managed repositories. Collection scoping (`-c` / `collections: [...]`) is explicit per task. Large project collections are excluded from default unscoped search (`includeByDefault: false`). Every profile needing retrieval receives the QMD MCP configuration.

### 2. Strongest Supporting Evidence
- **Live QMD Verification on Host (`EXECUTED`):** QMD 2.8.3 (`facd35e`) is operational in WSL with 4 collections (`moa-lika`, `moa-ipos`, `moa-acim`, `moa-health`). Retrieval operates with sub-second latency.
- **CWD Independence (`EXECUTED` / `UPSTREAM_DOC`):** `qmd query -c <collection>` and MCP `collections: ["..."]` execute accurately from any working directory, allowing an agent in `~/workspaces/Investment` to query Investment collections without changing directories.
- **Zero API Egress & Zero Provider Token Cost (`SOURCE_VERIFIED`):** Hybrid BM25, local vector embeddings (`embeddinggemma-300M`), and local reranking run 100% locally on CPU/GPU without cloud API dependencies.
- **Context Isolation via Default Exclusion (`UPSTREAM_DOC`):** Setting `includeByDefault: false` prevents accidental cross-repo context pollution during general search queries.

### 3. Strongest Contradicting & Risk Evidence
- **MCP Plural Syntax Requirement (`UPSTREAM_DOC` / `SOURCE_VERIFIED`):** QMD MCP strictly parses plural `collections`; singular `collection` is silently ignored.
- **Index Staleness (`STATIC_SIMULATION` / Risk R25):** QMD indexes are snapshots in SQLite. Edits in Git repositories do not automatically reflect in QMD until `qmd update` is triggered.

### 4. Hidden Couplings & Dependencies
- Profiles isolate MCP configurations; each new role profile requiring retrieval must have the QMD MCP block in its `config.yaml`.

### 5. Token, Latency & Operational Cost
- **Indexing / Retrieval Token Cost:** $0.00.
- **Query Latency:** ~150–400ms for hybrid local search.

### 6. Failure Modes & Mitigations
- *Failure Mode:* Agent makes decisions based on stale indexed documentation.
  - *Mitigation:* Implement pre-task freshness check comparing Git commit timestamps against QMD collection metadata (Correction C04).

---

## Decision D09 — External Shared Memory Deferred

- **Status in Architecture Ledger:** `DEFERRED / ACCEPTED`
- **Validation Verdict:** **`PASS`**
- **Decision File:** [`decisions/D09-EXTERNAL-MEMORY-DEFERRED.md`](../../decisions/D09-EXTERNAL-MEMORY-DEFERRED.md)

### 1. Exact Claim Validated
Do not add an external shared-memory provider (e.g. Mem0, Letta, Zep) in initial v2. Reconsider only if the combination of profile-local memory, Git repository truth, QMD retrieval, and reviewed skill promotion demonstrates a measured operational gap.

### 2. Strongest Supporting Evidence
- **Anti-Overengineering Compliance (`SOURCE_VERIFIED`):** Directly follows OpenAI, Anthropic, and Google production guidance: do not add external state services when local deterministic files and scoped RAG satisfy the operational requirement.
- **Privacy & Security Boundaries (`REPO_EVIDENCE`):** Avoids external cloud memory sync, API egress risks, subscription costs, and vendor lock-in.
- **Single Source of Truth Protection (`STATIC_SIMULATION`):** External memory services frequently create shadow truth that conflicts with Git-versioned documentation.

### 3. Strongest Contradicting & Risk Evidence
- **Tacit Memory Transfer Gap (`INFERENCE`):** Non-procedural operator nuances must be explicitly recorded in `USER.md` or repo documentation rather than automatically synced across all agent profiles.

### 4. Reopen Triggers
- Reopen only if multiple independent roles repeatedly fail to perform tasks due to lack of shared evolving state, despite QMD and shared skills.

---

## Decision D10 — Background Multi-Board Autonomy Deferred (Safety Gate)

- **Status in Architecture Ledger:** `DEFERRED SAFETY GATE`
- **Validation Verdict:** **`PASS`**
- **Decision File:** [`decisions/D10-BACKGROUND-MULTI-BOARD-AUTONOMY.md`](../../decisions/D10-BACKGROUND-MULTI-BOARD-AUTONOMY.md)
- **Incident Link:** [`incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md`](../../incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md)

### 1. Exact Claim Validated
Do not enable autonomous background gateway dispatch across multiple repo boards in initial v2. Operate in Safe Mode A (sequential execution on one active repo board). Reconsider background autonomy only after the installed Hermes version passes 10 explicit host-persistence, mount-scope, and profile-concurrency acceptance tests.

### 2. Strongest Supporting Evidence
- **Upstream Defect Cluster (`UPSTREAM_ISSUE` / `SOURCE_VERIFIED`):**
  - Issue #73556: Profile `terminal.cwd` overrides Kanban workspace and broadens Docker mounts.
  - Issue #83856: Host/container cwd provenance mismatch across terminal, file, and code tools.
  - Issue #91568: Kanban Docker worker changes/commits fail to persist to host filesystem.
  - Issue #78122: Concurrency limits apply per-board, multiplying concurrent workers.
- **Live Host Configuration Proof (`EXECUTED` / Risk R21):** Live inspection of `/root/.hermes/config.yaml` revealed a static volume mount `[/root/MasterOfArts:/root/MasterOfArts:rw, /root/MasterOfArts:/workspace:rw]`. Running multi-board background workers today would cause immediate mount collisions across repositories!

### 3. Strongest Contradicting & Risk Evidence
- **Throughput Limitation (`INFERENCE`):** Initial v2 cannot run parallel autonomous worker swarms across all four repositories overnight. (Accepted by operator: user explicitly stated multi-repo work does not require simultaneous execution).

### 4. Hidden Couplings & Dependencies
- Safe Mode A relies on `dispatch_in_gateway: false` in Hermes configuration.

### 5. Failure Modes & Mitigations
- *Failure Mode:* Unattended worker reports `git commit` successful, but code was committed inside an ephemeral container and lost upon container exit.
  - *Mitigation:* Gate D10 strictly blocks background dispatch until the 10 acceptance tests prove host-side Git commit persistence on the installed runtime.

---

## Decision Audit Summary Matrix

```text
+----------+--------------------------------------+-----------------------+---------------------+
| Decision | Subject Area                         | Architecture Status   | Validation Verdict  |
+----------+--------------------------------------+-----------------------+---------------------+
| D01      | Apex Control Plane                   | ACCEPTED              | PASS                |
| D02      | Separate Kanban Boards + Rollup      | ACCEPTED              | PASS                |
| D03      | Reusable Role Profiles (Sequential)  | ACCEPTED W/ CONSTR.   | PASS_WITH_CONDITIONS|
| D04      | Learning Spillover via Skills        | ACCEPTED W/ CONSTR.   | PASS                |
| D05      | Apex Shared-Skill Canonical Source   | ACCEPTED PILOT REQ.   | PASS_WITH_CONDITIONS|
| D06      | BMAD & Domain Skill Placement        | ACCEPTED              | PASS                |
| D07      | Canonical WSL Workspace Migration    | ACCEPTED MIGR. PEND.  | PASS_WITH_CONDITIONS|
| D08      | QMD Multi-Repo Retrieval             | ACCEPTED LIVE PEND.   | PASS                |
| D09      | External Memory Deferred             | DEFERRED / ACCEPTED   | PASS                |
| D10      | Background Multi-Board Autonomy Gate | DEFERRED SAFETY GATE  | PASS                |
+----------+--------------------------------------+-----------------------+---------------------+
```
