# Original User Request

## 2026-09-07T08:29:59Z

Architect, benchmark, and evaluate dual-instance separation for `ki-basis` infrastructure across private entrepreneurship and community operations, resolving the WSL2/9p performance degradation, crash loops, and port collision risks.

Working directory: C:\GitDev\apexai-os-meta

## Requirements

### R1. Performance Diagnosis & Storage Architecture
Resolve the empirical performance bottleneck observed in Ubuntu WSL2 (350% CPU usage, OpenProject crash loop `exit status 1`, 9P filesystem latency on `/mnt/c`). Establish native ext4 volume configurations and proper non-interactive headless container runtime parameters.

### R2. Dual-Instance Isolation Architecture
Design an airtight, battle-proven isolation model between Private Entrepreneurship and Community operations:
- Independent Docker Compose project namespaces (`ki-basis-private` vs. `ki-basis-community`).
- Fully isolated Docker bridge networks preventing inter-stack routing and DNS discovery.
- Non-overlapping port assignment mapping (e.g. Private on 8080–8089, Community on 9080–9089).
- Completely segregated PostgreSQL databases, Valkey instances, Paperless data, and Firefly uploads.

### R3. Multi-Engine vs. Multi-Project Strategy Evaluation
Provide an evidence-based comparison between:
- **Strategy A (Dual Compose Projects on Single Engine)**: Running both instances in Docker Desktop or native WSL2 with project namespaces (`-p`), distinct `.env` files, and port bands.
- **Strategy B (Dual Daemon Split)**: Running Private in Ubuntu WSL2 (native dockerd on ext4) and Community in Windows Docker Desktop (Alpine LinuxKit), accounting for WSL2 `localhostForwarding` conflicts.

## Acceptance Criteria

### Performance & Stability
- [ ] OpenProject, Hermes, Paperless, and Firefly all reach healthy status with steady-state CPU under 5% at idle.
- [ ] All database and persistent volumes reside on native ext4/named Docker volumes rather than 9P Windows mounts.

### Isolation Verification
- [ ] Both instances can run concurrently without port binding errors.
- [ ] Zero shared database tables or volume mounts across private and community stacks.
- [ ] Comprehensive migration and daily operation runbook for both entities.

## 2026-09-29T09:38:08Z

Perform a rigorous, full multi-agent inventory, deep evaluation, quality-and-value ranking, and cross-repo lineage mapping of all agent definitions, doctrine files, orchestration workflows, and skills across the `apexai-os-meta` Git repository and the legacy `C:\Quasi Desktop\AI_PreperationUntil_06-26` staging archives.

Working directory: c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit
Integrity mode: development

## Requirements

### R1. Comprehensive Multi-Source Inventory & Discovery
Discover, inventory, and verify every agent-related document, specification, skill, and workflow file across both repositories:
1. `c:\GitDev\apexai-os-meta`:
   - Active Agent Contracts: `.claude/agents/*.md`
   - Orchestration Agent Doctrines & Manifests: `apex-meta/orchestration/agents/` (including `CORE.md`, `ESSENCE.md`, `DOCTRINE-MANIFEST.md`, and all subdirectories)
   - System Core & Workflows: `apex-meta/orchestration/` (`00-START-HERE.md`, `ARCHITECTURE.md`, `workflows/`, `schemas/`, `user-stories/`, `new_final_v4/`, `architecture-improvements/`)
   - Skill Implementations: `.claude/skills/` and `apex-meta/skills/` (including `apex-plan`, `apex-sync`, `apex-session`, `weekly-orchestrator`, `source-authority-and-verdict-packet`, etc.)
2. `C:\Quasi Desktop\AI_PreperationUntil_06-26`:
   - Managed Agent KB: `Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\` (all agent subfolders and index files)
   - Source Indexes: `agent_kb_source_indexes\` (`ALFRED_KB_BASE_BUILD_INDEX.md`, `META_HEADS_KB_BASE_BUILD_INDEX.md`, `SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`, `KB_INFORMATICS_DEEP_RESEARCH_ONLINE_REPO_INDEX.yaml`)
   - Additional uncurated documents or source corpora located directly in `AI_PreperationUntil_06-26`.

### R2. Agent Grouping & Multi-Metric Evaluation Matrix
Group all inventoried files by owning agent / functional domain:
- **Alfred** (Intake, operator interaction, intent lock)
- **Meta Ops** (Execution engine, run-loop orchestration, backbone coordination)
- **Meta Strategy** (Direction, hypothesis formulation, portfolio steering)
- **Meta Detective** (Adversarial review, two-lens verification, validity and alignment)
- **Knowledge Bank** (Corpus curation, knowledge lifecycle, database schema)
- **Informatics Design** (QA standards, document presentation, taxonomy)
- **Prompts & Workflows** (Prompt engineering patterns, execution harnesses)
- **AI Routing / Special Ops** (Model selection, routing policies)

Rate every individual file on an objective 1–10 scale across four dimensions:
1. **Content Quality**: Conceptual clarity, depth of actionable logic, rigor of constraints, absence of empty stubs or hallucinations.
2. **Content Quantity**: Useful substantive density (effective signal-to-noise ratio).
3. **Machine Readability**: Standardized YAML frontmatter, deterministic section schemas, structured contract compliance.
4. **Current Operational Value**: Alignment with live APEX OS architecture (file-backed state, WSL2 single-engine, deterministic sync) vs. superseded legacy runtime assumptions (always-on swarm, legacy bridges).

Provide a concise, 1–2 sentence evidence-backed rationale for each rating score.

### R3. Definitive Leaderboard & Cross-Repository Lineage Map
Synthesize the findings into clear, actionable maps:
1. **Top-Tier Leaderboard**: A ranked tier list of the top-performing files across the entire ecosystem based on weighted overall score.
2. **Lifecycle State Categorization**: Classify every file into one of four states:
   - `Canonical / Active`: Directly executable or load-bearing in current architecture.
   - `Distilled / Migrated`: Content has been successfully preserved in modern `CORE.md` or `.claude/agents/`.
   - `Empty Scaffold / Stub`: Boilerplate or abandoned template with zero substantive doctrine.
   - `Reference-Only / Historical`: Background research or superseded doctrine to cite but not execute.
3. **Lineage & Delta Mapping**: Explicitly cross-reference legacy OpenClaw files against `apex-meta/orchestration/agents/DOCTRINE-MANIFEST.md` to identify any valuable rules or insights that were omitted during prior migrations.

## Acceptance Criteria

### Coverage & Grounding
- [ ] 100% of files in `.claude/agents/`, `apex-meta/orchestration/agents/`, and `managed/agent_kb/` are included in the evaluation matrix.
- [ ] Every file entry includes its verified absolute file path, byte size, line count, and last modification timestamp.
- [ ] No phantom files: all paths referenced in the deliverable exist on disk.

### Metric Consistency & Deliverables
- [ ] All four metrics (Quality, Quantity, Machine Readability, Value) are scored for each file on a strict 1–10 integer scale with an aggregate composite score.
- [ ] Deliverable outputs are written to `c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit`:
  - `README.md`: Executive summary, top leaderboard, agent-by-agent synthesis, and migration roadmap.
  - `agent_knowledge_matrix.csv`: Full, filterable spreadsheet with columns `[Agent, File_Name, Absolute_Path, Quality, Quantity, Machine_Readability, Operational_Value, Composite_Score, Status, Lineage_Notes, Rationale]`.
  - `agent_knowledge_matrix.json`: Machine-readable dataset of the complete audit.

## 2026-09-29T20:18:23Z

Execute an exhaustive, single-agent deep audit, multi-metric file value ranking, and architectural synthesis across all remaining agent domains—beginning with the three core heads (Meta Ops, Meta Detective, Meta Strategy), followed by the five execution lanes—to identify each agent's highest-value assets and populate their canonical LostAgents structure.

Working directory: c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives
Integrity mode: development

## Requirements

### R1. Phased Multi-Repository Discovery & Census
Rigorously locate, verify, and catalog every related file, prompt, doctrine, postmortem, and index across `c:\GitDev\apexai-os-meta`, `C:\Quasi Desktop\AI_PreperationUntil_06-26`, and `agent_kb_source_indexes` in two sequential phases:
- **Phase 1: Core Heads (Priority)**:
  1. **Meta Ops Head** (Run-loop orchestration, Plan-Sync-Session backbone)
  2. **Meta Detective Head** (Adversarial two-lens review, empirical failure analysis)
  3. **Meta Strategy Head** (Direction, cognitive decision frameworks, option memos)
- **Phase 2: Execution & Special Ops Lanes**:
  4. **Prompts & Workflows / Prompt Engineer** (Harness design, execution contracts, patch safety)
  5. **Informatics Design** (Structural QA, "one chunk, one job", presentation standard)
  6. **Knowledge Bank** (Corpus curation, knowledge promotion, storage schemas)
  7. **AI Handling & Routing** (Model directive ceilings, 500-token rule, cost optimization)
  8. **Hygiene Clean** (P0–P3 triage, exception handling, backlog management)

### R2. Category Value Ranking & Substantive Value Analysis
For each agent, evaluate and rank all discovered assets across standard architectural categories:
1. **Essence / Functional Identity**
2. **Agent Contract / Role Card**
3. **Best Practices**
4. **Mistakes, Traps & Failure Modes**
5. **Operational Templates & Instruments**
6. **Appendices & Deep Research Blueprints**
7. **Execution Control & Interaction Workflows**

Identify the **Single Highest-Value File** in the entire ecosystem for that agent and provide a rigorous substantive analysis explaining *why* it is superior and *how* it delivers concrete orchestration value. Explicitly isolate empty scaffold stubs (e.g. `EMPTY_STATE`) from substantive doctrine.

### R3. Curated Packaging & LostAgents Ingestion
For each agent, package the findings into:
1. A dedicated deep-audit report (`<AGENT>_DEEP_AUDIT.md`) with ranked leaderboard tables, key capabilities analysis, and unmigrated lore extraction.
2. A populated staging workspace under `C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\<AgentName>\` mirroring the Alfred gold standard:
   - `00_INDEX\` (`INDEX.md`)
   - `01_CURRENT_<AGENT>\` (Active contracts & distilled core)
   - `02_RESEARCH_AND_DESIGN\` (Heavy blueprints, prompts, deep research)
   - `90_SUPERSEDED\` (Empty stubs, legacy scaffolds, obsolete files)

## Acceptance Criteria

### [Coverage & Grounding]
- [ ] 100% of analyzed files exist on physical disk with verified absolute paths, exact byte sizes, and line counts (0 phantom paths).
- [ ] All 3 Phase 1 core heads (Meta Ops, Meta Detective, Meta Strategy) are fully completed before proceeding to Phase 2.
- [ ] For every agent, the single highest-value file across the ecosystem is identified and justified with concrete line/section citations.

### [Deliverables & Structure]
- [ ] A master summary index `ALL_AGENTS_DEEP_AUDIT_INDEX.md` is generated at the working directory root.
- [ ] Dedicated audit dossiers are created for each agent in `FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\`.
- [ ] Rescued files are organized and populated into their respective `LostAgents\<AgentName>\` directory trees.

