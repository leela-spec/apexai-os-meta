# Comprehensive Multi-Agent Doctrine Lineage, Lifecycle Classification, and Omitted Knowledge Audit

**Audit Date:** 2026-09-29  
**Auditor:** `explorer_lineage_delta`  
**Working Directory:** `c:\GitDev\apexai-os-meta\.agents\explorer_lineage_delta`  
**Parent Agent:** `orchestrator_3` (Conversation ID: `6ddb3813-515a-42e2-a565-70b43dfc69f4`)  
**Scope:** Cross-repository lineage mapping between legacy OpenClaw managed agent KB (`C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\`), legacy managed governance rules (`managed/rules/`, `managed/processes/`, `managed/knowledge/`), and modern APEX OS orchestration contracts (`c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\`, `c:\GitDev\apexai-os-meta\.claude\agents\`, `c:\GitDev\apexai-os-meta\apex-meta\orchestration\`).

---

## 1. Executive Summary & Ecosystem Architecture Evolution

### 1.1 The Evolutionary Arc
The APEX OS agent doctrine has evolved across three major architectural eras:
1. **Era 1: Legacy OpenClaw Swarm (`07_finalopenclawsystem`)**:
   - Designed around a multi-agent continuous swarm architecture with 9 distinct roles: 4 core coordinator/analysis roles (`alfred`, `meta_ops`, `meta_strategy`, `meta_detective`) and 5 "Special Ops" execution lanes (`special_ops__ai_handling_routing`, `special_ops__hygiene_clean`, `special_ops__informatics_design`, `special_ops__knowledge_bank`, `special_ops__prompts_workflows`).
   - Relied on complex runtime state relay mechanics: per-agent `LEARNING_QUEUE.md` promotion pipelines, state block continuations, and mutual cross-validation matrices (`OVERLAP_VALIDATION_MATRIX.md`).
2. **Era 2: Fable Orchestrator & Deterministic Move (2026-07-11 DOCTRINE-MANIFEST)**:
   - On 2026-07-11, a major consolidation audited 227 files across all 9 roles and executed a sha256-verified copy of 39 files into `apex-meta/orchestration/agents/`.
   - Established 5 Translation Rules:
     - (1) Always-on swarm $\to$ ephemeral invocations.
     - (2) Per-agent promotion queues $\to$ single mutation surface (`authority.state: candidate` $\to$ Detective review $\to$ operator gate $\to$ `apex-session`).
     - (3) Constant-frame state-block relay $\to$ file-backed state on disk.
     - (4) "Modes are not subagents" $\to$ ephemeral throwaway subagents permitted.
     - (5) Stale OpenClaw paths/model claims $\to$ historical only.
   - Introduced `CORE.md` files (distilled 80/20 operational cores) in 4 domains (`meta-detective`, `knowledge-bank`, `informatics-design`, `prompts-workflows`) to curb token consumption.
3. **Era 3: Modern APEX OS Live Operating Spine**:
   - Deployed active Claude agent contracts in `.claude/agents/*.md` (12 agents) wired to the Plan-Sync-Session Backbone (`apex-plan`, `apex-sync`, `apex-session`) and the dual-blind Detective review loop (`apex-review-validity`, `apex-review-alignment`).
   - Integrated with single-engine WSL2 Docker architecture.

### 1.2 Summary Audit Statistics
- **Total Legacy Managed Agent KB Files Audited:** 80+ files across 9 agent subdirectories, appendices, and index files.
- **Total Modern Orchestration Agent Files Audited:** 46 files in `apex-meta/orchestration/agents/` across 7 domain directories.
- **Total Active Modern Agent Contracts Audited:** 12 contracts in `.claude/agents/*.md`.
- **Legacy Verification Finding:**
  - DOCTRINE-MANIFEST accurately identified that `alfred`, `meta_ops`, and `meta_strategy` `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, and `LEARNING_QUEUE.md` files were 100% empty state schema stubs (EMPTY_STATE).
  - DOCTRINE-MANIFEST accurately verified that only `meta_detective` accumulated substantive real-world KB entries in the original v2 structure.
- **CRITICAL AUDIT DEFICIT IDENTIFIED:**
  - In the rush to eliminate swarm overhead and empty scaffolds, **at least seven high-value, operationally critical doctrine assets were prematurely discarded, classified as "reference-only", or lost in migration**. These include the 500-token prompt compliance rule and model directive ceilings, cognitive decision architectures, the 202-entry empirical failure ledger, patch transport and preimage-checked mutation protocols, and the P0–P3 / E0–E3 governance taxonomy.

---

## 2. Direct Cross-Repository Lineage Mapping

The table below maps every legacy OpenClaw agent/doctrine component directly to its modern counterpart in `apexai-os-meta`, indicating the exact evolution mechanism.

| Legacy OpenClaw Role / Component (`07_finalopenclawsystem/`) | Legacy Paths Audited | Modern Repo Location (`apexai-os-meta`) | Modern Active Contract (`.claude/agents/`) | Evolution & Lineage Mechanism |
|---|---|---|---|---|
| **Alfred** (Operator Intake & Interface) | `managed/agents/alfred.md`<br>`managed/agent_kb/alfred/ESSENCE.md`<br>`managed/agent_kb/alfred/{BEST_PRACTICES,MISTAKES,TEMPLATES,LEARNING_QUEUE}.md` | `apex-meta/orchestration/agents/alfred/ROLE-SEED.md`<br>`apex-meta/orchestration/agents/alfred/ESSENCE.md` | `.claude/agents/alfred.md` (1,902 bytes) | **Distilled & Active.** `ROLE-SEED` and `ESSENCE` moved verbatim on 2026-07-11. Empty scaffolds skipped. Main conversation intake and gate presentation contract codified in `.claude/agents/alfred.md`. |
| **Meta Ops** (Orchestration & Workflow Backbone) | `managed/agents/meta_ops.md`<br>`managed/agent_kb/meta_ops/ESSENCE.md`<br>`managed/agent_kb/meta_ops/{BP,MIS,TPL,LQ}.md`<br>`managed/rules/OPERATING_SPINE_CANON.md` | `apex-meta/orchestration/agents/meta-ops/ROLE-SEED.md`<br>`apex-meta/orchestration/agents/meta-ops/ESSENCE.md`<br>`meta-ops/legacy-hygiene-clean-TEMPLATES.md`<br>`meta-ops/INTEGRATION-apex-plan-sync-session.md` | `.claude/agents/meta-ops.md` (3,212 bytes)<br>`.claude/agents/apex-plan-ops.md`<br>`.claude/agents/apex-sync-ops.md` | **Evolved & Restructured.** Legacy empty scaffolds skipped. `legacy-hygiene-clean-TEMPLATES` imported to provide P0–P3 severity crib. Modern execution split: Meta Ops orchestrates the run loop while `apex-plan`, `apex-sync` (`scripts/apex_sync.py`), and `apex-session` execute deterministic state operations. |
| **Meta Strategy** (Direction, Leverage & Options) | `managed/agents/meta_strategy.md`<br>`managed/agent_kb/meta_strategy/ESSENCE.md`<br>`managed/agent_kb/meta_strategy/Appendices/DecisionMakingProcessReseearch_gem.md` | `apex-meta/orchestration/agents/meta-strategy/ROLE-SEED.md`<br>`apex-meta/orchestration/agents/meta-strategy/ESSENCE.md` | `.claude/agents/meta-strategy.md` (2,012 bytes) | **Truncated & Active.** `ESSENCE` moved verbatim. Empty scaffolds skipped. Modern contract requires 2–3 distinct direction options. *Omission:* Cognitive decision frameworks in `DecisionMakingProcessReseearch_gem.md` were left orphan in `.claude/skills/` without contract integration. |
| **Meta Detective** (Adversarial Review & Validity) | `managed/agents/meta_detective.md`<br>`managed/agent_kb/meta_detective/ESSENCE.md`<br>`managed/agent_kb/meta_detective/BEST_PRACTICES.md` (DET-BP-001..010)<br>`managed/agent_kb/meta_detective/MISTAKES.md` (DET-MIS-001..010)<br>`managed/agent_kb/meta_detective/TEMPLATES.md` (DET-TPL-001..008)<br>`managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md`<br>`managed/agent_kb/meta_detective/appendices/Failures/FAILURE_AND_ANTI_DRIFT_LEDGER.md` | `apex-meta/orchestration/agents/meta-detective/` (All files moved verbatim)<br>`meta-detective/CORE.md` (Distilled 138-line core) | `.claude/agents/meta-detective.md` (2,801 bytes)<br>`.claude/agents/apex-review-validity.md` (3,427 bytes)<br>`.claude/agents/apex-review-alignment.md` (3,444 bytes) | **Fully Distilled, Evolved & Split.** Verbatim files preserved. `CORE.md` synthesizes rules and 2 core templates. In addition, modern architecture split the role into dual blind reviewer contracts: `apex-review-validity` (Lens 1) and `apex-review-alignment` (Lens 2), with supplemental doctrine in `.claude/skills/weekly-orchestrator/references/roles/meta-detective-doctrine.md`. *Omission:* 202-entry failure ledger remained in legacy storage. |
| **Special Ops Knowledge Bank** (Corpus & Lifecycle) | `managed/agents/special_ops__knowledge_bank.md`<br>`managed/agent_kb/special_ops__knowledge_bank/` (`ESSENCE`, `BEST_PRACTICES`, `MISTAKES`, `TEMPLATES`, `APPENDIX_KB_DATABASE_SCHEMA`, `APPENDIX_KB_EXAMPLES`, `APPENDIX_KB_CANDIDATE_LEDGER`, `APPENDIX_KB_SOURCE_MANIFEST`, etc.) | `apex-meta/orchestration/agents/knowledge-bank/` (`ESSENCE`, `BEST_PRACTICES`, `MISTAKES`, `TEMPLATES`, `APPENDIX_KB_DATABASE_SCHEMA`, `APPENDIX_KB_EXAMPLES`)<br>`knowledge-bank/CORE.md` | `.claude/agents/knowledge-bank.md` (2,144 bytes)<br>`.claude/agents/apex-kb-operator.md` (1,844 bytes) | **Re-architected.** The appendix-first OpenClaw structure was replaced by the modern `apex-meta/kb/<slug>/` architecture and the installed `apex-kb` CLI skill. `CORE.md` distills custody, candidate-vs-accepted status, and fetch-back verification. `apex-kb-operator.md` drives the CLI. |
| **Special Ops Informatics Design** (Structure & QA) | `managed/agents/special_ops__informatics_design.md`<br>`managed/agent_kb/special_ops__informatics_design/` (`ESSENCE`, `BP`, `MIS`, `TPL`, `appendices/*`) | `apex-meta/orchestration/agents/informatics-design/` (`ESSENCE`, `BP`, `MIS`, `TPL` + `legacy-hygiene-clean-{ESSENCE,BP,MIS}`)<br>`informatics-design/CORE.md` | `.claude/agents/informatics-design.md` (1,947 bytes) | **Distilled.** Structural QA from `hygiene_clean` was merged into this domain. `CORE.md` enforces "one chunk, one job", functional headings, and terminology stability. Governs `apex-meta/orchestration/GLOSSARY.md`. |
| **Special Ops Prompts & Workflows** (Prompting & Contracts) | `managed/agents/special_ops__prompts_workflows.md`<br>`managed/agent_kb/special_ops__prompts_workflows/` (`ESSENCE`, `BP`, `MIS`, `TPL`, `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS`, `APPENDIX_KB_EXAMPLES`, `APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT`, plus 15 unmigrated appendices) | `apex-meta/orchestration/agents/prompts-workflows/` (7 files moved verbatim)<br>`prompts-workflows/CORE.md` | `.claude/agents/prompts-workflows.md` (1,994 bytes) | **Distilled & Bounded.** `CORE.md` distills 11 best practices and 11 mistakes. Modern contract enforces bounded deliverables and worked examples. *Omission:* Unmigrated appendices contained critical patch transport protocols and preimage-checked mutation rules. |
| **Special Ops AI Handling & Routing** (Model Selection) | `managed/agents/special_ops__ai_handling_routing.md`<br>`managed/agent_kb/special_ops__ai_handling_routing/` (`ESSENCE`, `BP`, `MIS`, `TPL`, `APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON`, `APPENDIX_KB_ROUTING_EXAMPLE`, `2Do_context_file_authority_reference.md`) | `.claude/skills/AIRouting/references/legacy-v2-doctrine/` (All 6 core files copied) | Delegated to `.claude/skills/AIRouting` (No active agent in `.claude/agents/`) | **Role Dropped; Migrated to Skill.** Dedicated agent role was retired because advisory routing belongs in execution skills. *Critical Omission:* `2Do_context_file_authority_reference.md` was dropped completely. |
| **Special Ops Hygiene Clean** (Structural QA & Backlog) | `managed/agents/special_ops__hygiene_clean.md`<br>`managed/agent_kb/special_ops__hygiene_clean/` (`ESSENCE`, `BP`, `MIS`, `TPL`, `appendices/*`)<br>`managed/rules/QA_HYGIENE_PROTOCOL.md` | Split across:<br>- `meta-ops/legacy-hygiene-clean-TEMPLATES.md`<br>- `informatics-design/legacy-hygiene-clean-*` | Folded into `meta-detective.md` and `informatics-design.md` | **Role Dropped; Doctrine Absorbed.** Dedicated agent eliminated to prevent circular handoff loops. P0–P3 severity model moved to Meta Ops; structural QA moved to Informatics Design; defect hunting folded into Meta Detective. |

---

## 3. Comprehensive Lifecycle State Classification

Every file surveyed across both repositories is classified into one of four mutually exclusive lifecycle states:
1. **`Canonical / Active`**: Directly executable, loaded by active agents, or binding runtime contracts in APEX OS.
2. **`Distilled / Migrated`**: Content whose durable core has been successfully absorbed into modern `CORE.md` or `.claude/agents/` contracts, remaining on disk as verbatim evidence.
3. **`Empty Scaffold / Stub`**: Boilerplate schema templates with zero substantive doctrine (e.g. `EMPTY_STATE` markers).
4. **`Reference-Only / Historical`**: Research dumps, superseded swarm mechanics, patch logs, or obsolete transport files that should be cited but not executed.

### 3.1 Classification Matrix

| File Path | Owning Domain | Size (Bytes) | Lifecycle Classification | Lineage & Operational Rationale |
|---|---|---:|---|---|
| `.claude/agents/alfred.md` | Alfred | 1,902 | **Canonical / Active** | Binding runtime contract for operator intake, constraints, and gate response capture. |
| `.claude/agents/meta-ops.md` | Meta Ops | 3,212 | **Canonical / Active** | Binding runtime contract for meso-workflow execution, packet routing, and backbone invocation. |
| `.claude/agents/meta-strategy.md` | Meta Strategy | 2,012 | **Canonical / Active** | Binding runtime contract for macro direction, leverage, and option framing. |
| `.claude/agents/meta-detective.md` | Meta Detective | 2,801 | **Canonical / Active** | Binding runtime contract for independent review and validation verdict packets. |
| `.claude/agents/apex-review-validity.md` | Meta Detective | 3,427 | **Canonical / Active** | Binding runtime contract for blind Lens 1 validity review in weekly loops. |
| `.claude/agents/apex-review-alignment.md` | Meta Detective | 3,444 | **Canonical / Active** | Binding runtime contract for blind Lens 2 strategic alignment review. |
| `.claude/agents/knowledge-bank.md` | Knowledge Bank | 2,144 | **Canonical / Active** | Binding runtime contract for source placement and candidate custody. |
| `.claude/agents/informatics-design.md` | Informatics Design | 1,947 | **Canonical / Active** | Binding runtime contract for taxonomy, chunking, and glossary consistency. |
| `.claude/agents/prompts-workflows.md` | Prompts & Workflows | 1,994 | **Canonical / Active** | Binding runtime contract for prompt packets, stage patterns, and templates. |
| `.claude/agents/apex-plan-ops.md` | Meta Ops / Planning | 875 | **Canonical / Active** | Binding runtime contract for project decomposition into `apex_plan_packet`. |
| `.claude/agents/apex-sync-ops.md` | Meta Ops / Sync | 735 | **Canonical / Active** | Binding runtime contract for deterministic Python sync reports. |
| `.claude/agents/apex-kb-operator.md` | Knowledge Bank | 1,844 | **Canonical / Active** | Binding runtime contract for driving the `apex-kb` CLI lifecycle. |
| `apex-meta/orchestration/00-START-HERE.md` | System Core | 4,628 | **Canonical / Active** | System entry point, 5 invariants, read order, and component locations. |
| `apex-meta/orchestration/ARCHITECTURE.md` | System Core | 8,811 | **Canonical / Active** | Architectural blueprint, single WSL2 engine integration, and non-goals. |
| `apex-meta/orchestration/agents/DOCTRINE-MANIFEST.md` | System Core | 5,950 | **Canonical / Active** | Binding translation rules and move record for all agent doctrine. |
| `apex-meta/orchestration/agents/meta-detective/CORE.md` | Meta Detective | 9,581 | **Canonical / Active** | Distilled operational core: owns/does-not-own, 5 modes, verdicts, 10 BPs, 10 mistakes. |
| `apex-meta/orchestration/agents/informatics-design/CORE.md` | Informatics Design | 3,670 | **Canonical / Active** | Distilled operational core: chunking, functional headings, 8 failure patterns. |
| `apex-meta/orchestration/agents/knowledge-bank/CORE.md` | Knowledge Bank | 3,965 | **Canonical / Active** | Distilled operational core: placement, candidate custody, fetch-back verification. |
| `apex-meta/orchestration/agents/prompts-workflows/CORE.md` | Prompts & Workflows | 5,303 | **Canonical / Active** | Distilled operational core: target locking, 11 BPs, 11 failure patterns. |
| `apex-meta/orchestration/agents/meta-ops/INTEGRATION-apex-plan-sync-session.md` | Meta Ops | 5,136 | **Canonical / Active** | Binding contract governing how Meta Ops routes into the Plan-Sync-Session backbone. |
| `apex-meta/orchestration/schemas/handoff-packet.schema.md` | Schemas | 5,607 | **Canonical / Active** | The one universal handoff packet schema required for all cross-role boundaries. |
| `apex-meta/orchestration/schemas/authority-state.schema.md` | Schemas | 4,742 | **Canonical / Active** | Enforced lifecycle field schema: candidate $\to$ verified $\to$ invalidated. |
| `apex-meta/orchestration/schemas/review-verdict.schema.md` | Schemas | 5,892 | **Canonical / Active** | Enforced schema for Detective review verdicts and falsification attempts. |
| `apex-meta/orchestration/agents/alfred/ESSENCE.md` | Alfred | 1,189 | **Distilled / Migrated** | Compact boundary specification; preserved verbatim from legacy OpenClaw. |
| `apex-meta/orchestration/agents/meta-ops/ESSENCE.md` | Meta Ops | 1,085 | **Distilled / Migrated** | Compact boundary specification; preserved verbatim from legacy OpenClaw. |
| `apex-meta/orchestration/agents/meta-strategy/ESSENCE.md` | Meta Strategy | 1,093 | **Distilled / Migrated** | Compact boundary specification; preserved verbatim from legacy OpenClaw. |
| `apex-meta/orchestration/agents/meta-detective/BEST_PRACTICES.md` | Meta Detective | 14,828 | **Distilled / Migrated** | DET-BP-001..010; full YAML entries kept as on-demand reference behind CORE.md. |
| `apex-meta/orchestration/agents/meta-detective/MISTAKES.md` | Meta Detective | 15,210 | **Distilled / Migrated** | DET-MIS-001..010; full failure patterns kept as on-demand reference. |
| `apex-meta/orchestration/agents/meta-detective/TEMPLATES.md` | Meta Detective | 10,447 | **Distilled / Migrated** | 8 inspection instruments; DET-TPL-001/002 distilled in CORE; 003–005 on demand. |
| `apex-meta/orchestration/agents/meta-detective/APPENDIX_INTERNAL_MODES.md` | Meta Detective | 16,842 | **Distilled / Migrated** | Detailed 5-mode validation playbook; distilled in CORE table. |
| `apex-meta/orchestration/agents/meta-ops/legacy-hygiene-clean-TEMPLATES.md` | Meta Ops / Hygiene | 7,370 | **Distilled / Migrated** | Migrated from hygiene_clean; provides P0–P3 severity crib and closure checklist. |
| `apex-meta/orchestration/agents/informatics-design/BEST_PRACTICES.md` | Informatics Design | 5,820 | **Distilled / Migrated** | Preserved verbatim; summarized into CORE.md default rules. |
| `apex-meta/orchestration/agents/informatics-design/MISTAKES.md` | Informatics Design | 6,104 | **Distilled / Migrated** | Preserved verbatim; summarized into CORE.md 8 failure patterns. |
| `apex-meta/orchestration/agents/informatics-design/TEMPLATES.md` | Informatics Design | 5,025 | **Distilled / Migrated** | Row shapes for chunk audits and source manifests; on-demand reference. |
| `apex-meta/orchestration/agents/knowledge-bank/BEST_PRACTICES.md` | Knowledge Bank | 7,120 | **Distilled / Migrated** | BP-KB-001..009; preserved verbatim; distilled into CORE constraints. |
| `apex-meta/orchestration/agents/knowledge-bank/MISTAKES.md` | Knowledge Bank | 6,840 | **Distilled / Migrated** | Preserved verbatim; distilled into CORE 5 failure patterns. |
| `apex-meta/orchestration/agents/knowledge-bank/APPENDIX_KB_DATABASE_SCHEMA.md` | Knowledge Bank | 12,410 | **Distilled / Migrated** | Database schema reference for structured KB storage; on-demand reference. |
| `apex-meta/orchestration/agents/knowledge-bank/APPENDIX_KB_EXAMPLES.md` | Knowledge Bank | 14,200 | **Distilled / Migrated** | Worked examples of KB placement; on-demand reference. |
| `apex-meta/orchestration/agents/prompts-workflows/BEST_PRACTICES.md` | Prompts & Workflows | 14,250 | **Distilled / Migrated** | PW-BP-001..011; preserved verbatim; distilled into CORE 11 practices. |
| `apex-meta/orchestration/agents/prompts-workflows/MISTAKES.md` | Prompts & Workflows | 13,810 | **Distilled / Migrated** | PW-MK-001..011; preserved verbatim; distilled into CORE 11 failure patterns. |
| `apex-meta/orchestration/agents/prompts-workflows/TEMPLATES.md` | Prompts & Workflows | 18,920 | **Distilled / Migrated** | 10 prompt/workflow templates; on-demand reference. |
| `apex-meta/orchestration/agents/prompts-workflows/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` | Prompts & Workflows | 21,400 | **Distilled / Migrated** | HALT/CLARIFY contracts and execution gates; on-demand reference. |
| `apex-meta/orchestration/agents/prompts-workflows/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md` | Prompts & Workflows | 19,800 | **Distilled / Migrated** | Drift regression cases; on-demand reference. |
| `.claude/skills/AIRouting/references/legacy-v2-doctrine/ESSENCE.md` | AI Routing | 4,003 | **Distilled / Migrated** | Boundary specification for advisory AI routing; stored in skill references. |
| `.claude/skills/AIRouting/references/legacy-v2-doctrine/APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` | AI Routing | 30,056 | **Distilled / Migrated** | Model tool variant comparison table; on-demand skill reference. |
| `managed/agent_kb/alfred/BEST_PRACTICES.md` | Alfred | 509 | **Empty Scaffold / Stub** | Contains only YAML schema and `EMPTY_STATE` marker. Zero substantive content. |
| `managed/agent_kb/alfred/MISTAKES.md` | Alfred | 556 | **Empty Scaffold / Stub** | Contains only YAML schema and `EMPTY_STATE` marker. Zero substantive content. |
| `managed/agent_kb/alfred/TEMPLATES.md` | Alfred | 507 | **Empty Scaffold / Stub** | Contains only YAML schema and `EMPTY_STATE` marker. Zero substantive content. |
| `managed/agent_kb/alfred/LEARNING_QUEUE.md` | Alfred | 1,027 | **Empty Scaffold / Stub** | Obsolete promotion queue boilerplate; empty pending entries. |
| `managed/agent_kb/meta_ops/BEST_PRACTICES.md` | Meta Ops | 521 | **Empty Scaffold / Stub** | Contains only YAML schema and `EMPTY_STATE` marker. Zero substantive content. |
| `managed/agent_kb/meta_ops/MISTAKES.md` | Meta Ops | 519 | **Empty Scaffold / Stub** | Contains only YAML schema and `EMPTY_STATE` marker. Zero substantive content. |
| `managed/agent_kb/meta_ops/TEMPLATES.md` | Meta Ops | 519 | **Empty Scaffold / Stub** | Contains only YAML schema and `EMPTY_STATE` marker. Zero substantive content. |
| `managed/agent_kb/meta_ops/LEARNING_QUEUE.md` | Meta Ops | 1,040 | **Empty Scaffold / Stub** | Obsolete promotion queue boilerplate; empty pending entries. |
| `managed/agent_kb/meta_strategy/BEST_PRACTICES.md` | Meta Strategy | 536 | **Empty Scaffold / Stub** | Contains only YAML schema and `EMPTY_STATE` marker. Zero substantive content. |
| `managed/agent_kb/meta_strategy/MISTAKES.md` | Meta Strategy | 534 | **Empty Scaffold / Stub** | Contains only YAML schema and `EMPTY_STATE` marker. Zero substantive content. |
| `managed/agent_kb/meta_strategy/TEMPLATES.md` | Meta Strategy | 532 | **Empty Scaffold / Stub** | Contains only YAML schema and `EMPTY_STATE` marker. Zero substantive content. |
| `managed/agent_kb/meta_strategy/LEARNING_QUEUE.md` | Meta Strategy | 1,050 | **Empty Scaffold / Stub** | Obsolete promotion queue boilerplate; empty pending entries. |
| `managed/agent_kb/special_ops__ai_handling_routing/LEARNING_QUEUE.md` | AI Routing | 1,120 | **Empty Scaffold / Stub** | Obsolete promotion queue boilerplate; empty pending entries. |
| `managed/agent_kb/special_ops__hygiene_clean/LEARNING_QUEUE.md` | Hygiene Clean | 1,080 | **Empty Scaffold / Stub** | Obsolete promotion queue boilerplate; empty pending entries. |
| `managed/agent_kb/special_ops__informatics_design/LEARNING_QUEUE.md` | Informatics Design | 1,090 | **Empty Scaffold / Stub** | Obsolete promotion queue boilerplate; empty pending entries. |
| `managed/agent_kb/special_ops__knowledge_bank/LEARNING_QUEUE.md` | Knowledge Bank | 1,110 | **Empty Scaffold / Stub** | Obsolete promotion queue boilerplate; empty pending entries. |
| `managed/agent_kb/special_ops__prompts_workflows/LEARNING_QUEUE.md` | Prompts & Workflows | 1,150 | **Empty Scaffold / Stub** | Obsolete promotion queue boilerplate; empty pending entries. |
| `managed/agent_kb/special_ops__ai_handling_routing/2Do_context_file_authority_reference.md` | AI Routing / Governance | 17,480 | **Reference-Only / Historical (CRITICAL OMISSION)** | Complete model directive ceilings, 500-token primacy rule, and anti-patterns. Never migrated to modern repo. |
| `managed/agent_kb/meta_strategy/Appendices/DecisionMakingProcessReseearch_gem.md` | Meta Strategy | 5,442 | **Reference-Only / Historical (HIGH-VALUE OMISSION)** | 5 cognitive decision frameworks (First Principles, Cynefin, WRAP, AoA, OODA). Copied loose to `.claude/skills/` but unintegrated. |
| `managed/agent_kb/meta_detective/appendices/Failures/FAILURE_AND_ANTI_DRIFT_LEDGER.md` | Meta Detective | 116,262 | **Reference-Only / Historical (HIGH-VALUE OMISSION)** | 202 empirical AI failure cases, drift mechanisms, and concrete countermeasures. Dropped as generic reference. |
| `managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md` | Prompts & Workflows | 19,884 | **Reference-Only / Historical (HIGH-VALUE OMISSION)** | Deterministic GitHub storage vs probabilistic AI generation; exact preimage patch rules. |
| `managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | Prompts & Workflows | 21,936 | **Reference-Only / Historical (HIGH-VALUE OMISSION)** | Complete patch transport selection chooser matrix (full-body, search/replace, diff, live-edit, manual). |
| `managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` | Prompts & Workflows | 43,007 | **Reference-Only / Historical** | Verification ledger preventing external model claims from leaking into accepted doctrine. |
| `managed/agent_kb/special_ops__prompts_workflows/appendices/KBAudit/AGENT_PATCH_CONTRACT.md` | Prompts & Workflows / Patch | 12,063 | **Reference-Only / Historical (HIGH-VALUE OMISSION)** | Hard blocker prevention gates and strict patch output formatting rules. |
| `managed/agent_kb/special_ops__prompts_workflows/appendices/KBAudit/OPENCLAW_CURRENT_AGENT_INTERACTION_FRAME_v1_1 (1).yaml` | System Architecture | 13,228 | **Reference-Only / Historical** | Formal YAML schema of first-wave agent interaction baseline. |
| `managed/rules/QA_HYGIENE_PROTOCOL.md` | System Rules / Hygiene | 15,103 | **Reference-Only / Historical (HIGH-VALUE OMISSION)** | 8 hygiene finding classes, P0–P3 severity model, and closure conditions. |
| `managed/rules/ESCALATION_EXCEPTION_BLOCK.md` | System Rules / Escalation | 11,788 | **Reference-Only / Historical (HIGH-VALUE OMISSION)** | E0–E3 escalation levels, authority ambiguity triggers, and truth-leakage stops. |
| `managed/rules/AGENT_SWARM_INTERACTION_CANON.md` | System Rules | 20,808 | **Reference-Only / Historical** | Swarm interaction rules, role-vs-state permission separation. Superseded by ephemeral orchestration. |
| `managed/rules/PROMOTION_PROTOCOL.md` | System Rules | 6,862 | **Reference-Only / Historical** | 4 truth promotion classes and packet lifecycle states. Superseded by `authority-state.schema.md`. |
| `managed/processes/AGENT_HANDOFF_CONTRACTS.md` | System Processes | 25,687 | **Reference-Only / Historical** | Precursor to modern `handoff-packet.schema.md`. |
| `managed/agent_kb/KB_SYSTEM_RELIABILITY_AUDIT_V1` | System Architecture | 3,537 | **Reference-Only / Historical** | Diagnostic audit proving human doctrine requires machine-executable control contracts. |
| `managed/agent_kb/AGENT_KB_INDEX.md` | System Index | 3,861 | **Reference-Only / Historical** | Legacy agent-to-root directory index. |

---

## 4. Critical Omitted Knowledge Audit (The Deep Delta)

This section details the highest-value operational rules, domain heuristics, verification protocols, and architectural insights that existed in legacy OpenClaw files but were **omitted or lost** during the migrations to `CORE.md`, `DOCTRINE-MANIFEST.md`, and `.claude/agents/*.md`.

### 4.1 Omission 1: Context File Authority Reference (`2Do_context_file_authority_reference.md`)
- **Legacy Source:** `managed/agent_kb/special_ops__ai_handling_routing/2Do_context_file_authority_reference.md` (392 lines, 17,480 bytes).
- **Migration Status:** Completely omitted. `DOCTRINE-MANIFEST.md` recorded that `special_ops__ai_handling_routing` was dropped and its files moved to `.claude/skills/AIRouting/references/legacy-v2-doctrine/`, but this specific file was never copied or integrated anywhere.
- **Specific High-Value Lost Doctrine:**
  1. **Empirical Directive Ceilings by Model (Frontmatter & Section 7):**
     ```yaml
     directive_ceilings:
       gpt_4o: 50                      # exponential decay
       claude_3_7_sonnet_standard: 50   # linear decay
       claude_3_7_sonnet_reasoning: 80  # linear decay, reasoning tasks
       gemini_2_5_pro: 100              # threshold decay, cliff onset 150-250
       o3: 100                          # threshold decay, cliff onset 150-250
     ```
     *Operational Impact:* Explains why complex agent system prompts fail. LLMs experience steep compliance degradation when total imperative directives exceed these thresholds.
  2. **The 500-Token Primacy Rule (CD-01, AP-07):**
     - *Rule:* Place all critical-tier directives in the first 500 tokens of every prompt/governance file.
     - *Empirical Basis:* Directives placed past the first 500 tokens suffer a 30% to 50% drop in compliance due to positional attention decay (lost-in-the-middle phenomenon). Compliance at position 0–500 is ~73% vs. <35% mid-document.
  3. **Modal Verb Elimination (CD-04, DWR-01, AP-05):**
     - *Rule:* Start every directive with an imperative verb (`Return`, `Halt`, `Validate`, `Split`). Ban modal hedging (`should`, `may`, `might`, `could`).
     - *Empirical Basis:* When models encounter modal verbs, they interpret mandatory governance constraints as optional suggestions, leading to non-deterministic compliance.
  4. **Four-Way File Type Taxonomy with Rigid Token Budgets (Section 2):**
     - `system_prompt`: $\le$ 2,000 tokens, directive count $\le$ model ceiling.
     - `knowledge_base`: $\le$ 100,000 tokens, directive count = 0 (strictly factual/lookup; no behavioral constraints).
     - `workflow`: $\le$ 4,000 tokens, directive count $\le$ 15 (steps, preconditions, stop conditions).
     - `tool_definition`: $\le$ 1,000 tokens, directive count $\le$ 5 (schemas, error handling).
     - *Anti-Pattern Prevented:* Monolithic mixed-type files (AP-09) that cause context clash and prevent modular context reloading.
  5. **Rule Proliferation Creep & The Deletion Test (DWR-06, AP-01):**
     - *Rule:* Run the deletion test before finalizing any directive set: remove any rule that changes model behavior in fewer than 10% of realistic test cases.
     - *Failure Prevented:* Accumulating dozens of post-incident rules until total directives exceed the model ceiling, causing wholesale omission of core rules.
  6. **Minimal Viable File Test (MVT-01..04):**
     - Concrete 4-question checklist to run before authorizing any prompt or instruction block for production.

### 4.2 Omission 2: Cognitive Decision Architectures (`DecisionMakingProcessReseearch_gem.md`)
- **Legacy Source:** `managed/agent_kb/meta_strategy/Appendices/DecisionMakingProcessReseearch_gem.md` (97 lines, 5,442 bytes).
- **Current Repo Status:** A copy was dropped loose into `c:\GitDev\apexai-os-meta\.claude\skills\DecisionMakingProcessReseearch_gem.md`, but it is completely unreferenced by any skill, agent contract, or doctrine manifest.
- **Specific High-Value Lost Doctrine:**
  - In modern APEX OS, `.claude/agents/meta-strategy.md` only contains a generic 24-line contract stating: *"Deliver 2–3 genuinely distinct direction options with leverage, timing, and risk — a recommendation is allowed, a single take-it-or-leave-it option is not."*
  - The legacy research codified **five established cognitive frameworks** specifically matched to decision types:
    1. **First Principles Thinking (Aristotelian / Axiomatic Deconstruction):** Strip analogies and industry "best practices" to find bedrock truths. *Rank #1 for Resilience.*
    2. **The Cynefin Framework (Dave Snowden / Problem Verification):** Categorize problems into Clear, Complicated, Complex, Chaotic, and Confused before choosing an approach. Prevents applying rigid deterministic plans to chaotic/complex environments. *Rank #2 for Multi-Dimensionality.*
    3. **The WRAP Process (Chip & Dan Heath / Bias Neutralization):**
       - **W**iden options (avoid binary "whether-or-not" framing).
       - **R**eality-test assumptions (evidence/source verification).
       - **A**ttain distance before deciding (evaluate emotional/friction cost).
       - **P**repare to be wrong (pre-mortems and failure mode mapping).
       - *Rank #3 for Broader Appeal.*
    4. **Analysis of Alternatives (AoA / GAO & DoD Standard):** Clinical, data-driven comparison of multiple strategies against baseline Key Performance Parameters with full Cost-Benefit Analysis (CBA) and lifecycle cost scoring. *Rank #4 for Logic.*
    5. **The OODA Loop (John Boyd / Adaptive Agility):** Observe, Orient, Decide, Act tempo optimization for fast-moving competitive environments. *Rank #5 for Agility.*
  - **The Hybrid First Principles + WRAP Recommendation:** Specifically recommended for formal Strategic Decision Memos: use First Principles to check bedrock axioms ("What is actually true?"), and WRAP to generate and reality-test alternatives ("Why might we be wrong?").

### 4.3 Omission 3: Empirical AI Failure Ledger (`FAILURE_AND_ANTI_DRIFT_LEDGER.md`)
- **Legacy Source:** `managed/agent_kb/meta_detective/appendices/Failures/FAILURE_AND_ANTI_DRIFT_LEDGER.md` (202 lines, 116,262 bytes).
- **Migration Status:** Classified as "REFERENCE" (stay in KB, cite only) and never distilled into modern `meta-detective/CORE.md` or `.claude/agents/meta-detective.md`.
- **Specific High-Value Lost Doctrine:**
  - Contains **202 granular, empirical AI failure cases**, cataloging:
    - `id` (e.g. `KB-INFORMATICS-DESIGN-017`, `KB-CODEX-EXECUTION-PROCESS-073`, `KB-META-OPS-025`, `KB-PROMPTS-WORKFLOWS-027`).
    - `failure_or_risk`: Exact failure pattern observed in real agent runs.
    - `evidence_summary`: Verbatim reproduction quotes from failed runs.
    - `safeguard`: Tested countermeasure.
    - `validator`: Assigned validating role pair.
    - `score`: Confidence / severity score (e.g. 77.8, 75.4).
    - `source`: Source file path in research archives.
  - Key empirical failure mechanisms documented:
    - *Reorganization Drift (`KB-CODEX-EXECUTION-PROCESS-055`):* During file/folder reorganization, agents tasked only with moving files also silently edit, rename, or compress contents, destroying git auditability.
    - *Helpfulness Reflex (`KB-CODEX-EXECUTION-PROCESS-019`):* LLMs explaining why they are patching, introducing conversational prose into machine-parsed diff streams. Countermeasure: "Silence by Default" enforcement.
    - *Summary Elevation (`KB-CODEX-EXECUTION-PROCESS-071`):* Derived summaries cited as outranking primary source code/documents.
    - *Waterfall Knowledge Creation Failure (`KB-META-OPS-025`):* Forcing rigid 7-stage skeleton signoffs before empirical discovery stabilizes, leading to compliance theater.

### 4.4 Omission 4: Preimage-Checked Scaffold Mutation & Patch Transport Selection
- **Legacy Sources:**
  - `managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md` (466 lines, 19,884 bytes).
  - `managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` (374 lines, 21,936 bytes).
- **Migration Status:** Dismissed in `DOCTRINE-MANIFEST.md` with the claim: *"hygiene_clean/prompt-transport appendices obsoleted by the Edit tool + deterministic-markdown-patcher skills."*
- **Specific High-Value Lost Doctrine:**
  1. **The Fundamental Architectural Distinction:**
     - *GitHub / File System Storage is Deterministic:* Stores exact submitted bytes.
     - *AI Replacement Content Construction is Probabilistic:* Models constructing full replacement files frequently omit subtle lines, hallucinate anchors, or compress context.
     - *Primary Risk Surface:* Exists entirely between live file read and write submission.
  2. **Patch Transport Chooser Matrix (Section 6 of `PATCH_TRANSPORT_PROTOCOLS`):**
     - Explicit decision criteria for choosing between:
       - *Full-body replacement:* Only for new file creation, explicit total rewrites, or small artifacts ($\le$ 50 lines).
       - *SEARCH/REPLACE blocks:* For localized edits on stable preimages; requires exact-once match and dry-run before write.
       - *Unified diff (`git apply`):* For targeted codebase edits where line-level hunks and diff inspection tooling are expected.
       - *Live-edit instruction:* For human-in-the-loop browser sessions.
       - *No-patch / Manual-review:* Mandatory when exact preimage cannot be matched uniquely or when source conflict is detected.
  3. **Direct Root of Repository Safety Rules:**
     - The strict rules in `c:\GitDev\apexai-os-meta\AGENTS.md` and `GEMINI.md` ("Apex KB Patch Safety: First read complete live target files, generate operator-reviewable exact-match patch pack using literal `<file>`, `<old>`, `<new>` blocks; one change per block; match exactly once") were directly adapted from these unmigrated appendices. Without these appendices, downstream agents treat the rules as arbitrary constraints rather than understanding the underlying failure mechanics.

### 4.5 Omission 5: Hard Patch Blocker Prevention Gates (`AGENT_PATCH_CONTRACT.md`)
- **Legacy Source:** `managed/agent_kb/special_ops__prompts_workflows/appendices/KBAudit/AGENT_PATCH_CONTRACT.md` (381 lines, 12,063 bytes).
- **Migration Status:** Omitted from modern orchestration docs.
- **Specific High-Value Lost Doctrine:**
  - Defines the machine-readable `blocker_prevention_rules`:
    - Ban Markdown fence wrappers around patch blocks (causes nested parser confusion).
    - Ban chat artifacts, search/replace commentary, and download wrappers inside patch streams.
    - Prohibit creating `_v2`, `_new`, replacement, sidecar, or backup files as a workaround for patch application failures (AP-Patch-03: Workaround Sprawl).
    - If search text matches 0 or $>$1 times: emit NO patch file and report exactly one HALT line.
    - Strict file naming: `TASK-{ID}_{short-description}.patch.md`.

### 4.6 Omission 6: Full QA Hygiene & Escalation Taxonomies
- **Legacy Sources:**
  - `managed/rules/QA_HYGIENE_PROTOCOL.md` (424 lines, 15,103 bytes).
  - `managed/rules/ESCALATION_EXCEPTION_BLOCK.md` (259 lines, 11,788 bytes).
- **Migration Status:** Collapsed into `legacy-hygiene-clean-TEMPLATES.md` and high-level rules, but the full taxonomy was not carried forward into `schemas/review-verdict.schema.md`.
- **Specific High-Value Lost Doctrine:**
  1. **Eight Formal QA Finding Classes:**
     - Interface failure, State integrity failure, Authority leakage, Dependency/pointer failure, Trace failure, Promotion integrity failure, Continuity failure, Legacy bridge risk.
  2. **Four-Tier Severity Model with Concrete Operational Defaults:**
     - `P0` (Critical governance failure): Immediate hold/escalate; normal continuation forbidden.
     - `P1` (High-risk integrity failure): Remediate before normal progression or declare bounded degraded mode.
     - `P2` (Material hygiene debt): Backlog with bounded due path.
     - `P3` (Low-risk hygiene issue): Batch cleanup or explicit deferment.
  3. **Four-Tier Escalation Levels:**
     - `E0` (Local clarification): Resolved from loaded sources without crossing boundaries.
     - `E1` (Local hold): Task cannot continue safely until a prerequisite is resolved.
     - `E2` (Structured escalation): Crosses surfaces/projects and requires explicit routing.
     - `E3` (Hard stop): Requires human operator intervention.

### 4.7 Omission 7: Information Compression Loss in `CORE.md` Distillations
- **Analysis of Modern `CORE.md` Distillations:**
  - In `meta-detective/CORE.md`, the 10 Best Practices and 10 Mistakes from the 1,150-line full files were compressed into 1-line bullet points.
  - *What was lost:* The rich YAML frontmatter of `DET-BP-001..010` and `DET-MIS-001..010`, including the exact `context_conditions`, edge-case triggering criteria, and risk scores.
  - Furthermore, `meta-detective/CORE.md` retained only 2 templates (`DET-TPL-001` Source verification checklist and `DET-TPL-002` Validation verdict packet), leaving `DET-TPL-003` (Contradiction audit table), `DET-TPL-004` (Boundary drift check), and `DET-TPL-005` (Risk red team packet) as on-demand references that active agents are instructed *not* to read by default.
  - Because `DOCTRINE-MANIFEST.md` explicitly commands: *"read ONLY CORE.md before substantive work... Do not also read ESSENCE/BEST_PRACTICES/MISTAKES/TEMPLATES 'to be thorough' — that defeats the point of CORE.md"*, modern agents running as `meta-detective` never see the specialized audit tables unless an explicit pointer directs them there.

---

## 5. Concrete Migration Recommendations and Re-Integration Roadmap

To restore this high-value legacy knowledge without re-introducing the bloated swarm overhead, token bloat, or dead promotion machinery, the following 6-phase roadmap is recommended.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        APEX DOCTRINE REVITALIZATION ROADMAP                            │
├─────────────────────────┬──────────────────────────┬───────────────────────────────────┤
│ Phase                   │ Target Asset / Location  │ Concrete Action                   │
├─────────────────────────┼──────────────────────────┼───────────────────────────────────┤
│ Phase 1: Context &      │ 2Do_context_file_...     │ Codify directive ceilings, 500-   │
│ Directive Ceilings      │ informatics-design/CORE  │ token rule & MVT into InfDesign.  │
├─────────────────────────┼──────────────────────────┼───────────────────────────────────┤
│ Phase 2: Cognitive      │ DecisionMakingProcess... │ Integrate 5 Decision Frameworks   │
│ Decision Frameworks     │ meta-strategy/CORE.md    │ (Cynefin/WRAP/AoA) into Strategy. │
├─────────────────────────┼──────────────────────────┼───────────────────────────────────┤
│ Phase 3: Empirical      │ FAILURE_AND_ANTI_DRIFT.. │ Index 202 failure cases into an   │
│ Failure Index           │ meta-detective/          │ on-demand retrieval index.        │
├─────────────────────────┼──────────────────────────┼───────────────────────────────────┤
│ Phase 4: Patch Safety & │ PREIMAGE_CHECKED... &    │ Re-ground AGENTS.md patch rules in│
│ Preimage Anchoring      │ AGENT_PATCH_CONTRACT     │ prompts-workflows doctrine.       │
├─────────────────────────┼──────────────────────────┼───────────────────────────────────┤
│ Phase 5: QA Taxonomy    │ QA_HYGIENE_PROTOCOL &    │ Formalize 8 finding classes & E0- │
│ & Escalation Matrix     │ ESCALATION_EXCEPTION     │ E3 levels in review-verdict schema│
├─────────────────────────┼──────────────────────────┼───────────────────────────────────┤
│ Phase 6: Skill Hygiene  │ .claude/skills/          │ Move orphan files out of .claude/ │
│ & Orphan Cleanup        │ DecisionMaking... & PDF  │ skills/ into proper references.   │
└─────────────────────────┴──────────────────────────┴───────────────────────────────────┘
```

### Phase 1: Codify Prompt & Directive Engineering into Informatics Design
- **Action:** Move the substantive rules from `managed/agent_kb/special_ops__ai_handling_routing/2Do_context_file_authority_reference.md` into `apex-meta/orchestration/agents/informatics-design/`.
- **Implementation:**
  - Add an appendix `APPENDIX_DIRECTIVE_AND_PROMPT_AUTHORITY.md` to `informatics-design/`.
  - Add a concise 10-line summary to `informatics-design/CORE.md` establishing the 500-token primacy rule, model directive ceilings (50/80/100), and modal verb ban.
  - Embed the Minimal Viable File Test (MVT-01..04) into `.claude/skills/informatics-authoring/` and `wiki-lint`.

### Phase 2: Formally Integrate Cognitive Decision Frameworks into Meta Strategy
- **Action:** Graduate `DecisionMakingProcessReseearch_gem.md` from a loose orphan file into authoritative doctrine for `meta-strategy`.
- **Implementation:**
  - Move `.claude/skills/DecisionMakingProcessReseearch_gem.md` to `apex-meta/orchestration/agents/meta-strategy/APPENDIX_COGNITIVE_DECISION_FRAMEWORKS.md`.
  - Update `.claude/agents/meta-strategy.md` and `meta-strategy/ESSENCE.md` (or create `meta-strategy/CORE.md`) to explicitly cite the 5 frameworks:
    - Clear/Complicated vs Complex/Chaotic $\to$ Cynefin problem classification.
    - Debiasing & pre-mortems $\to$ WRAP process.
    - Cost-benefit & KPP tradeoffs $\to$ Analysis of Alternatives (AoA).
    - Rapid operational shifts $\to$ OODA loop.

### Phase 3: Establish an On-Demand Empirical Failure Index for Meta Detective
- **Action:** Convert the 116 KB `FAILURE_AND_ANTI_DRIFT_LEDGER.md` into an on-demand searchable reference for adversarial review.
- **Implementation:**
  - Place a cleaned, indexed copy in `apex-meta/orchestration/agents/meta-detective/FAILURE_AND_ANTI_DRIFT_LEDGER.md`.
  - In `meta-detective/CORE.md` and `.claude/agents/meta-detective.md`, add an explicit instruction: *"When validating high-risk architectural changes or complex prompt workflows, query `FAILURE_AND_ANTI_DRIFT_LEDGER.md` for historical failure precedents and verified safeguards."*
  - Expose this ledger to the `impl-validator` and `source-authority-and-verdict-packet` skills.

### Phase 4: Anchor Patch Safety Rules to Preimage & Transport Doctrine
- **Action:** Formally link the root operating notes (`AGENTS.md` and `GEMINI.md`) to the underlying patch transport doctrine.
- **Implementation:**
  - Migrate `APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md` and `AGENT_PATCH_CONTRACT.md` into `apex-meta/orchestration/agents/prompts-workflows/`.
  - Cite these files in `AGENTS.md` under *Apex KB Patch Safety*, transforming arbitrary rules into an auditable evidence chain explaining *why* whole-file replacements fail and *why* exact-match preimages are mathematically necessary.

### Phase 5: Codify the 8 QA Finding Classes and E0–E3 Escalation in Review Schemas
- **Action:** Upgrade `apex-meta/orchestration/schemas/review-verdict.schema.md` and `workflows/detective-review.md`.
- **Implementation:**
  - Replace the ad-hoc finding types in `review-verdict.schema.md` with the 8 canonical classes from `QA_HYGIENE_PROTOCOL.md` (Interface failure, State integrity failure, Authority leakage, Pointer failure, Trace failure, Promotion integrity failure, Continuity failure, Legacy bridge risk).
  - Formalize the E0–E3 escalation levels in `schemas/handoff-packet.schema.md` to ensure standardized handling of blockers across all agents.

### Phase 6: Clean Up Repository Skill Artifact Hygiene
- **Action:** Address loose files polluting `.claude/skills/`.
- **Implementation:**
  - Move `.claude/skills/DecisionMakingProcessReseearch_gem.md` to `apex-meta/orchestration/agents/meta-strategy/` (per Phase 2).
  - Review and relocate `c:\GitDev\apexai-os-meta\.claude\skills\LDN_PEM_CFS_Allgemeiner_Report.pdf` (178 KB), which was accidentally placed into `.claude/skills/` instead of an appropriate reference or knowledge archive.

---

## 6. Audit Verification Log

| Target Surface | Direct Observation / Check Performed | Verification Tool | Verification Finding |
|---|---|---|---|
| `apex-meta/orchestration/agents/DOCTRINE-MANIFEST.md` | Inspected move claims, 39 files moved, 5 translation rules, skip criteria. | `view_file` L1–61 | Manifest confirms 2026-07-11 move; claims alfred/meta_ops/meta_strategy scaffolds were empty. |
| `managed/agent_kb/alfred/BEST_PRACTICES.md` | Checked whether file contained substantive content or empty template. | `view_file` L1–32 | Confirmed: 100% empty schema scaffold (`EMPTY_STATE: no accepted Alfred practices`). |
| `managed/agent_kb/meta_ops/BEST_PRACTICES.md` | Checked whether file contained substantive content or empty template. | `view_file` L1–32 | Confirmed: 100% empty schema scaffold (`EMPTY_STATE: no accepted Meta Ops practices`). |
| `managed/agent_kb/meta_strategy/BEST_PRACTICES.md` | Checked whether file contained substantive content or empty template. | `view_file` L1–32 | Confirmed: 100% empty schema scaffold (`EMPTY_STATE: no accepted Meta Strategy practices`). |
| `managed/agent_kb/special_ops__ai_handling_routing/2Do_context_file_authority_reference.md` | Checked contents, structure, and omission status. | `view_file` L1–392 | Confirmed: 392 lines of high-value operational directives; omitted from DOCTRINE-MANIFEST. |
| `managed/agent_kb/meta_strategy/Appendices/DecisionMakingProcessReseearch_gem.md` | Checked cognitive frameworks and current location. | `view_file` L1–97 | Confirmed: 5 cognitive frameworks; exists loose in `.claude/skills/` without contract integration. |
| `managed/agent_kb/meta_detective/appendices/Failures/FAILURE_AND_ANTI_DRIFT_LEDGER.md` | Checked size, entry count, and content structure. | `view_file` L1–100 | Confirmed: 116 KB, 202 failure cases; omitted from active agent doctrine. |
| `managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md` | Checked core distinction and relation to AGENTS.md. | `view_file` L1–60 | Confirmed: 466 lines; foundational source for AGENTS.md patch safety rules. |
| `managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | Checked transport selection matrix and protocols. | `view_file` L1–140 | Confirmed: Complete transport chooser; falsely dismissed as obsolete in manifest. |
| `apex-meta/orchestration/agents/meta-detective/CORE.md` | Checked distillation depth vs verbatim files. | `view_file` L1–138 | Confirmed: 10 BPs and 10 Mistakes condensed to single lines; 6 templates omitted from core. |
| `.claude/agents/*.md` | Audited all 12 active agent contracts. | `list_dir` & `view_file` | Confirmed: 12 active contracts; verified exact responsibilities, tools, and doctrine references. |
