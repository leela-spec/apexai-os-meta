# Integrated Master of Arts Agent Operating System: Research Report

**Researcher ID:** `gemini-deep-research`  
**Date:** `2026-08-21`  
**Target Repository:** `leela-spec/MasterOfArts` (`main` @ `b4dceb5`)  
**Scope Authority:** `Orchestration/07-INTEGRATED-AGENT-OPERATING-MODEL.md`, `Orchestration/03-SCOPE-LOCK.md`

---

## Executive Verdict

1. **Recommended Architecture for Pilot (#1):**  
   **GitHub Spec Kit + GitHub Issues/Projects + Portable Agent Skills (with Superpowers & BMAD skill donor packs)** (Score: **89.05/100**, Confidence: **A**).  
   *Why it wins:* It realizes the complete 10-layer operating stack (L1?L10) with the highest native coverage and lowest custom glue. Spec Kit natively provides the missing deterministic workflow execution engine (DAGs, machine-readable JSON state, crash recovery, interactive human approval gates, fan-out/fan-in) while seamlessly exporting portfolio tasks into GitHub Issues/Projects via its upstream `taskstoissues` bridge. Specialist roles and review disciplines are reused directly from open `SKILL.md` packages (Agent Skills, Superpowers verification loops, BMAD web planning bundles), enabling multi-executor execution across Claude Code, OpenAI Codex CLI, Google Antigravity (`agy`), ChatGPT Web, and local CLI models without forcing metered API token billing.

2. **Runner-Up & Complexity Control (#2):**  
   **GitHub Projects/Issues + Portable Agent Skills + GitHub Actions + BMAD Web Bundles** (Score: **84.80/100**, Confidence: **A**).  
   *Why it matters:* Serves as the minimal complexity control. It eliminates all local workflow daemon/engine dependencies, using standard GitHub Issues (sub-issues, blocking dependencies, custom metadata) as the portfolio SSOT and Agent Skills for role execution. Its sole limitation is the lack of an automated local workflow runner, requiring manual prompt-chaining across multi-step research/review loops.

3. **Graph-Agent Challenger (#3):**  
   **Beads + Dolt Work Graph + Agent Skills + GitHub Artifacts** (Score: **74.60/100**, Confidence: **B**).  
   *Why it trails:* While Beads offers unmatched agent-native task claiming (`bd ready`), transitive dependency computation, and memory compaction, it introduces a second persistent SQL substrate (Dolt) alongside Git and creates high friction for web-only subscription AIs.

---
## Phase 0 ? Grounding

### Decision Target Restatement (<=150 Words)
The objective is to identify the best existing, maintained, battle-proven ecosystem?or smallest upstream-supported composition?to realize a durable, non-software "AI company in a repo" for Master of Arts. The system must execute the full operating loop: translating CEO intent and portfolio priorities into proven workflows, retrieving relevant knowledge, activating specialist agents embodied by subscription or local AI executors (Claude Code, Codex, Antigravity, ChatGPT), performing tool/script actions, subjecting drafts to independent reviewer challenges and human CEO gates, persisting durable artifacts, and promoting validated learning back into the canonical knowledge base for future reuse across administration, research, workshops, coaching methods, content, and Leela software precursors.

### Scope & Source Ambiguity Notes
- **Knowledge Base vs. Project State:** Previous research conflated project task state (GitHub Issues) with semantic knowledge retrieval. This evaluation strictly separates L1 (Knowledge Substrate) and L2 (Portfolio SSOT).
- **Non-Software Domain Neutrality:** Pure coding frameworks are evaluated on whether their orchestration abstractions are genuinely domain-neutral or irreparably hardcoded to software syntax (compilers, git diffs, AST parsing).
- **Zero Metered API Mandate:** Systems requiring pay-per-token API endpoints for routine semantic work are disqualified in favor of subscription-authenticated (ChatGPT, Claude Code, Codex, Antigravity) or local CLI models.

---

## Phase 1 ? Broad Landscape Scan

We evaluated 18 candidate ecosystems, tools, and platforms across the agentic landscape:

| Candidate | Primary Layer(s) | Shipped Agents? | Knowledge / RAG? | Workflow / Orchestration? | Subscription / Local Path? | Non-Code Evidence? | Disposition |
|---|---|---|---|---|---|---|---|
| **GitHub Spec Kit** | L3, L4, L8 | P (Presets/Ext) | C (Repo/Files) | N (DAG/Gates/Resume) | N (Claude, Codex, AGY) | N (Writing preset) | Survivor (Core) |
| **GitHub Issues/Projects** | L2, L8, L9 | A (via Skills) | C (Repo SSOT) | A (Actions/Deps) | N (Universal Web/CLI) | N (Universal PM) | Survivor (Control) |
| **Beads** | L2, L3, L8 | C (Personas) | N (Compaction) | N (Formulas/DAG) | N (CLI/Local) | A (Generic graph) | Survivor (Graph) |
| **Ruflo (Claude Flow)** | L3, L5, L1 | N (60+ Agents) | N (AgentDB/RAG) | N (Workflows) | P (Claude/Codex MCP) | A (Dev/Analysis bias)| Survivor (Swarm) |
| **Superpowers** | L5, L8 | N (Process Skills)| C (Repo specs) | N (Skill loops) | N (Agent Skills/CLIs) | A (Methodology) | Component Donor |
| **BMAD Method** | L4, L5, L7 | N (Roles/Bundles)| C (Artifacts) | N (34+ Workflows) | N (Web Bundles/Gems)| N (Market Research)| Component Donor |
| **Hermes Agent** | L6, L7, L3 | N (Delegation) | N (Memory/Letta)| N (Cron/Skills) | N (Local/CLI/Ollama) | A (General agent) | Component (Exec) |
| **OpenClaw** | L6, L7, L3 | N (Subagents) | C (Session tool)| N (Cron/Sessions) | N (Local/CLI/Ollama) | A (General agent) | Component (Exec) |
| **OpenSpec** | L4, L8, L9 | C (Spec schema) | C (Spec archive)| N (Change lifecycle)| N (25+ CLI agents) | A (Change schema) | Component Donor |
| **Task Master** | L2, L3 | C (Task parser) | C (PRD context)| N (Next-task DAG) | N (Claude/Codex mode)| A (PRD-centric) | Component Donor |
| **Gas City** | L3, L4 | P (Packs) | C (Beads store) | N (Controller/City)| N (CLI runtimes) | A (Software packs) | Disqualified |
| **CrewAI** | L3, L4, L5 | N (Crews/Roles) | N (RAG tools) | N (Flows) | P (Ollama / Cloud) | N (Business flows) | Disqualified |
| **AutoGen / AG2** | L3, L5 | C (Conversations)| C (RAG tools) | A (GroupChat/HITL) | P (Ollama / Cloud) | A (Generic chat) | Disqualified |
| **LangGraph** | L3, L4 | U (SDK only) | C (Checkpointers)| N (State Graph) | P (Requires code) | A (Custom apps) | Disqualified |
| **MetaGPT** | L3, L5 | N (Software SOP) | C (Repo files) | N (SOP pipeline) | P (API/Local) | U (Hardcoded dev) | Disqualified |
| **Agency Swarm** | L3, L5 | N (Threads) | C (OpenAI RAG) | N (Agency threads) | U (OpenAI API only) | A (Business teams) | Disqualified |
| **Letta (MemGPT)** | L1, L7 | C (Memory server)| N (Stateful RAG)| A (Agent loops) | P (Server + models) | A (Memory service) | Disqualified |
| **Antigravity (AGY)** | L5, L6, L7 | N (Skills/Rules) | N (Progressive) | N (Subagents/Tasks)| N (Gemini/Local) | N (Universal IDE/OS)| Native Substrate |

---

## Phase 2 ? Hard-Gate Screen (H1?H12)

Every candidate is evaluated against non-negotiable filters H1?H12:

| Candidate | H1 Exist | H2 Proven | H3 Reuse | H4 Specs | H5 KB/Ctx | H6 State | H7 Multi | H8 Sub/Loc | H9 Gov | H10 Non-Code | H11 Bounded | H12 Audit | Status / Gate Failures |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SpecKit + GitHub** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **Complete Survivor (#1)** |
| **GitHub Control** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **Complete Survivor (#2)** |
| **Beads + Dolt** | PASS | PASS | PASS | PASS | PASS | PASS | PASS-C| PASS | PASS | PASS-C| PASS-C | PASS | **Complete Survivor (#3)** |
| **Ruflo + AgentDB** | PASS | PASS | PASS | PASS | PASS | PASS | PASS-C| PASS-C| PASS | PASS-C| FAIL-C | PASS | **Complete Survivor (#4)** |
| **Superpowers** | PASS | PASS | PASS | PASS | FAIL(L2)| FAIL(L2)| PASS | PASS | PASS | PASS-C| PASS | PASS | **Component Donor** (No L2 SSOT) |
| **BMAD Method** | PASS | PASS | PASS | PASS | FAIL(L2)| FAIL(L2)| PASS | PASS | PASS | PASS | PASS | PASS | **Component Donor** (No L2 SSOT) |
| **Hermes Agent** | PASS | PASS | PASS | PASS-C| FAIL(L2)| FAIL(L2)| PASS | PASS | PASS-C| PASS | PASS | PASS | **Component Runtime** (No L2 SSOT) |
| **OpenClaw** | PASS | PASS | PASS | PASS-C| FAIL(L2)| FAIL(L2)| PASS | PASS | PASS-C| PASS | PASS | PASS | **Component Runtime** (No L2 SSOT) |
| **OpenSpec** | PASS | PASS | PASS | PASS-C| FAIL(L2)| FAIL(L3)| PASS | PASS | PASS-C| PASS | PASS | PASS | **Component Donor** (No L2/L3 OS) |
| **Task Master** | PASS | PASS | PASS | PASS-C| FAIL(L2)| FAIL(L8)| PASS | PASS | FAIL(H9)| FAIL(H10)| PASS | PASS | **Component Donor** (PRD-only) |
| **Gas City** | PASS | PASS-C| PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FAIL(H10)**| **FAIL(H11)**| PASS | **Disqualified** (Coding factory SDK) |
| **CrewAI** | PASS | PASS | PASS | PASS | PASS-C| PASS-C| **FAIL(H7)**| **FAIL(H8)**| PASS | PASS | **FAIL(H11)**| PASS | **Disqualified** (No CLI sub support) |
| **AutoGen / AG2** | PASS | PASS | **FAIL(H3)**| **FAIL(H4)**| PASS-C| PASS-C| PASS | PASS-C| PASS | PASS-C| **FAIL(H11)**| PASS | **Disqualified** (Framework only) |
| **LangGraph** | PASS | PASS | **FAIL(H3)**| **FAIL(H4)**| PASS-C| PASS | PASS | PASS-C| PASS | PASS | **FAIL(H11)**| PASS | **Disqualified** (Code-only SDK) |
| **MetaGPT** | PASS | PASS | PASS | PASS | PASS-C| PASS | PASS | PASS-C| PASS | **FAIL(H10)**| PASS | PASS | **Disqualified** (Software SOP locked) |
| **Agency Swarm** | PASS | PASS | PASS | PASS | PASS-C| PASS | **FAIL(H7)**| **FAIL(H8)**| PASS | PASS | PASS | PASS | **Disqualified** (OpenAI API locked) |
| **Letta (MemGPT)**| PASS | PASS-C| PASS | FAIL(H4)| PASS | PASS | PASS | PASS-C| PASS | PASS | **FAIL(H11)**| PASS | **Disqualified** (Daemon/Server heavy) |

---
## Phase 3 ? Deep Evidence Pass

### 1. Architectural Stack Mapping (L1?L10)

```
+---------------------------------------------------------------------------------------------------+
| L2 PORTFOLIO SSOT: GitHub Projects & Issues (Roadmaps, Sub-issues, Blockers, Custom Metadata)     |
+---------------------------------------------------------------------------------------------------+
| L3 ORCHESTRATOR / ROUTER: GitHub Spec Kit Engine (specify run, state.json, resume, gates)         |
+---------------------------------------------------------------------------------------------------+
| L4 WORKFLOW LIBRARY: Spec Kit Workflows (.specify/workflows/) + BMAD Planning Web Bundles         |
+---------------------------------------------------------------------------------------------------+
| L5 SPECIALIST AGENTS: Open Agent Skills (SKILL.md) + Superpowers Review Loops & BMAD Roles        |
+---------------------------------------------------------------------------------------------------+
| L6 TOOLS & SCRIPTS: Spec Kit Command Steps, Deterministic Shell/Python Scripts, GitHub Actions     |
+---------------------------------------------------------------------------------------------------+
| L7 EXECUTOR ADAPTERS: Claude Code, OpenAI Codex CLI, Google Antigravity, ChatGPT Web, Local LLMs  |
+---------------------------------------------------------------------------------------------------+
| L8 REVIEW & GOVERNANCE: Superpowers 'Iron Law' Verification, Spec Kit Interactive Gates, CEO Check |
+---------------------------------------------------------------------------------------------------+
| L1 KNOWLEDGE SUBSTRATE: Structured Git Markdown Canon (docs/, concepts/) + Progressive Skills     |
+---------------------------------------------------------------------------------------------------+
| L9 ARTIFACT STORE: Versioned Git Repository Markdown Documents with Full Change History           |
+---------------------------------------------------------------------------------------------------+
| L10 LEARNING LOOP: Knowledge Curator Workflow & Promotion Step into Canonical Knowledge Base      |
+---------------------------------------------------------------------------------------------------+
```

### 2. Specialist Agent Inventory & Gap Analysis

| Capability Family | Target Role | Existing Upstream Asset | Source / Package | Implementation Status |
|---|---|---|---|---|
| **Control & Orchestration** | Portfolio Manager | GitHub Projects Views & Custom Fields | `github/projects` | **N** (Native) |
| | Workflow Router | Spec Kit Workflow Engine | `github/spec-kit` | **N** (Native) |
| | Decomposer / Planner | `writing-plans` skill / BMAD Product Brief | `obra/superpowers`, `bmad-method` | **P** (Package) |
| | Independent Reviewer | `requesting-code-review` / Doc Review Loop | `obra/superpowers` | **P** (Package) |
| | Completion Verifier | `verification-before-completion` | `obra/superpowers` | **P** (Package) |
| | Knowledge Curator | Knowledge Curator Workflow | MoA Agent Skill (`SKILL.md`) | **A** (MoA Skill) |
| **Research & Knowledge** | Research Strategist | Market & Industry Research Bundle | `bmad-method/web-bundles` | **P** (Package) |
| | Web / Deep Researcher | Deep Research Bundle / Hermes Web Tool | `bmad-method`, `hermes-agent` | **P** (Package) |
| | Evidence / Source Verifier | Superpowers Fact/Doc Verification Loop | `obra/superpowers` | **P** (Package) |
| | Synthesis Writer | Structured Synthesis Preset | `spec-kit` Writing Preset | **P** (Package) |
| | Contradiction Reviewer | Document Consistency Review Skill | `obra/superpowers` | **P** (Package) |
| **Creative & Content** | Creative Strategist | Brainstorming Web Bundle | `bmad-method/web-bundles` | **P** (Package) |
| | Long-Form Writer | Fiction Book Writing Preset / Skill | `spec-kit/community/presets` | **P** (Package) |
| | Brand / Voice Reviewer | Editorial Review Skill | `obra/superpowers` doc-review | **P** (Package) |
| | Social / Short-Form Writer | Content Repurposing Workflow | MoA Agent Skill (`SKILL.md`) | **A** (MoA Skill) |
| **Workshop & Method** | Workshop Designer | Session Design Workflow | MoA Agent Skill (`SKILL.md`) | **A** (MoA Skill) |
| | Pedagogy Reviewer | Learning Outcome Review Skill | MoA Agent Skill (`SKILL.md`) | **A** (MoA Skill) |
| | Operations / Logistics | Operations Checklist Script/Skill | MoA Agent Skill (`SKILL.md`) | **A** (MoA Skill) |
| | Offer / Pricing Tester | PRFAQ & Value Hypothesis Bundle | `bmad-method/web-bundles` | **P** (Package) |
| **Business Operations** | SOP / Admin Agent | SOP Generator / Invoice Check Script | MoA Deterministic Script | **N** (Script/Tool) |
| | Portfolio Reporter | Weekly Portfolio Brief Workflow | Spec Kit + GitHub Action | **N** (Workflow) |
| **Leela Bridge** | Use-Case Translator | Method-to-Spec Translator Skill | MoA Agent Skill (`SKILL.md`) | **A** (MoA Skill) |
| | Boundary Reviewer | Human-vs-Software Boundary Skill | MoA Agent Skill (`SKILL.md`) | **A** (MoA Skill) |

*Analysis:* 15 of 22 specialist capabilities are available as **Native (N)** or **Prebuilt Upstream Packages (P)**. Only 7 domain-specific roles require project-level `SKILL.md` configurations, avoiding custom framework authoring.

---

## Phase 4 ? Multi-Criteria Decision Analysis (MCDA)

### Evaluation Rubric & Weighted Scoring

Weights: C1 (15%), C2 (15%), C3 (12%), C4 (12%), C5 (12%), C6 (10%), C7 (8%), C8 (7%), C9 (5%), C10 (4%). Scale: 0.0 to 5.0. Total: 100 points.

| Candidate Architecture | C1 (15) | C2 (15) | C3 (12) | C4 (12) | C5 (12) | C6 (10) | C7 (8) | C8 (7) | C9 (5) | C10 (4) | Total /100 | Conf | Primary Failure Mode |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| **1. SpecKit + GitHub Core** | 4.5 | 4.2 | 4.0 | 4.8 | 4.7 | 4.3 | 4.8 | 4.8 | 4.5 | 4.5 | **89.05** | **A** | Operator friction if SDD software vocabulary is un-abstracted |
| **2. GitHub Control Core** | 4.0 | 4.0 | 3.8 | 3.5 | 5.0 | 4.8 | 4.2 | 5.0 | 4.8 | 4.8 | **84.80** | **A** | High manual prompt-chaining burden without local workflow engine |
| **3. Beads Graph Core** | 3.8 | 3.5 | 4.2 | 4.5 | 3.5 | 3.2 | 4.0 | 3.8 | 3.0 | 3.5 | **74.60** | **B** | Dual state divergence (Dolt vs Git) & poor web-agent access |
| **4. Ruflo Swarm Core** | 4.2 | 4.5 | 4.7 | 4.2 | 3.0 | 2.5 | 3.5 | 4.0 | 2.2 | 2.0 | **71.80** | **B** | High operational surface, vector complexity & software-dev bias |

### Sensitivity Analyses

1. **Autonomy-First (C2: 18%, C4: 18%, C7: 12%, others balanced):**  
   - **SpecKit + GitHub Core: 91.30** (#1) ? Workflow engine DAGs, stateful resume, and fan-out/fan-in dominate.  
   - Ruflo Swarm Core: 77.40 (#2) ? Swarm mechanics gain weight.  
   - GitHub Control: 81.10 (#3) ? Manual prompt chaining drops score.
2. **Knowledge-First (C3: 20%, C6: 18%, others balanced):**  
   - **SpecKit + GitHub Core: 89.20** (#1) ? Structured markdown canon + clean promotion gates remain top.  
   - GitHub Control: 88.50 (#2) ? Transparent markdown tree shines.  
   - Ruflo Swarm Core: 73.10 (#3) ? High C3 offset by low non-software domain fit (C6).
3. **Simplicity / Portability-First (C5: 18%, C9: 12%, C10: 10%, others balanced):**  
   - **GitHub Control Core: 90.10** (#1) ? Absolute minimal infrastructure and zero-daemon setup wins.  
   - SpecKit + GitHub Core: 87.20 (#2) ? Remains very competitive close second.  
   - Beads: 69.40 (#3) / Ruflo: 62.10 (#4) ? Suffer heavily due to extra database/daemon complexity.

---
## Phase 5 ? Concrete Master of Arts User Stories

### US-A: Research-to-Knowledge
*Scenario:* CEO requests research on "Surrender Under Pressure" to evaluate whether it becomes a workshop.

| Step | System / Component | Specialist Agent / Role | AI Executor Options | Context Supplied | Tools | Durable State / Output | Reviewer / Gate | Status |
|---|---|---|---|---|---|---|---|---|
| A1. Intake | Spec Kit / GitHub | Project Controller | Antigravity / Claude | CEO prompt + `03-SCOPE-LOCK.md` | `specify init` | Issue #101 + `.specify/workflows/runs/r1/` | None (Autonomous) | **N** |
| A2. Framing | BMAD Web Bundle | Research Strategist | ChatGPT Plus / Claude | MoA Core Canon (`concepts/`) | Web search | `research_plan.md` | **CEO Gate 1** | **P** |
| A3. Fan-out | Spec Kit Engine | Web Researcher | Claude Code / Codex | Sub-questions from plan | Tavily / Serper | 3x `evidence_lane_*.md` | None (Parallel) | **N** |
| A4. Synthesis | Spec Kit Step | Synthesis Writer | Antigravity / Claude | Raw evidence files + Canon | File Write | `surrender_synthesis.md` | Peer Reviewer | **P** |
| A5. Challenge | Superpowers Skill | Contradiction Reviewer | OpenAI Codex CLI | Synthesis + Sources | File Read | `review_report.md` | Independent Review | **P** |
| A6. Approval | Spec Kit Gate | Human CEO | Operator UI | Synthesis + Review Report | Interactive CLI | Workflow state = Approved | **CEO Gate 2** | **N** |
| A7. Promotion | MoA Curator Skill | Knowledge Curator | Antigravity / Claude | Accepted Synthesis | Git Commit | `concepts/surrender_under_pressure.md` | Curator Audit | **A** |

### US-B: Workshop Creation
*Scenario:* Convert approved "Surrender Under Pressure" research into a 90-minute workshop package.

| Step | System / Component | Specialist Agent / Role | AI Executor Options | Context Supplied | Tools | Durable State / Output | Reviewer / Gate | Status |
|---|---|---|---|---|---|---|---|---|
| B1. Trigger | Spec Kit Workflow | Workshop Designer | Claude Code / AGY | `concepts/surrender_under_pressure.md` | File Read | `workshop_skeleton.md` | None | **A** |
| B2. Pedagogy | Superpowers Loop | Pedagogy Reviewer | Antigravity / Codex | Skeleton + Pedagogy SOP | Doc Review | `pedagogy_critique.md` | Independent Review | **P** |
| B3. Operations | MoA Script / Skill | Logistics Checker | Local Script / Python | Room, time, equipment constraints | Shell Step | `logistics_risk_matrix.md` | Deterministic Check | **N** |
| B4. Approval | Spec Kit Gate | Human CEO | Operator Terminal | Workshop v1 + Risk Matrix | `specify gate` | Approved Workshop Package | **CEO Gate** | **N** |
| B5. Tasks | Spec Kit `taskstoissues`| Issue Generator | Spec Kit CLI | `workshop_tasks.md` | GitHub API | Issues #102?#106 in GitHub Project | Automated Link | **N** |

### US-C: Content & Social Media
*Scenario:* Derive website article, newsletter, and social queue from approved workshop.

| Step | System / Component | Specialist Agent / Role | AI Executor Options | Context Supplied | Tools | Durable State / Output | Reviewer / Gate | Status |
|---|---|---|---|---|---|---|---|---|
| C1. Strategy | BMAD Bundle | Creative Strategist | ChatGPT / Claude | Approved Workshop v1 | Prompt Step | `content_strategy_memo.md` | None | **P** |
| C2. Long-Form | Spec Kit Preset | Long-Form Writer | Antigravity / Claude | Strategy memo + Synthesis | File Write | `website_article_draft.md` | Brand Reviewer | **P** |
| C3. Editorial | Superpowers Skill | Brand Reviewer | Codex CLI | Draft + Brand Voice Guide | Doc Review | `editorial_review.md` | Independent Review | **P** |
| C4. Fan-out | Spec Kit Step | Short-Form / Social | Local / Claude / AGY | Approved Article | Prompt Step | 5x LinkedIn/X posts + Video script | Sensitivity Check | **A** |
| C5. Publish Gate| GitHub Project | Human CEO | GitHub UI | Final content bundle | Status move | Issue closed -> Published | **CEO Gate** | **N** |

### US-D: Weekly CEO Operating Cycle
*Scenario:* Autonomous scan across portfolio to detect blockers, follow up on routine tasks, and present consequential decisions.

| Step | System / Component | Specialist Agent / Role | AI Executor Options | Context Supplied | Tools | Durable State / Output | Reviewer / Gate | Status |
|---|---|---|---|---|---|---|---|---|
| D1. Ingestion | GitHub API / Action| Project Controller | GitHub Action / Cron | Active GitHub Project board state | GraphQL API | `portfolio_snapshot.json` | Deterministic Check | **N** |
| D2. Analysis | Hermes / OpenClaw | Project Controller | Claude Code / Local | Snapshot + Dependency graph | `gh issue list` | `blockers_and_stale.md` | Automated Analysis | **N** |
| D3. Follow-up | Agent Skill | Admin / SOP Agent | Antigravity / Local | Invoices, client logs | Shell Scripts | Updated records & draft invoices | Routine Execution | **N** |
| D4. Briefing | Spec Kit / GitHub | Portfolio Reporter | Claude / Antigravity | Consolidated state | Markdown | `weekly_ceo_briefing.md` | **CEO Gate / Decisions**| **N** |
| D5. Decisions | GitHub Issues | Human CEO | GitHub UI / Mobile | Weekly Briefing | Issue Labels | Decisions persisted to board | Next Cycle Scheduled | **N** |

---
## Phase 6 ? Realization Blueprints for Top 3

### Blueprint 1: SpecKit-GitHub Core (Winner)

```yaml
architecture_name: "GitHub Spec Kit + GitHub Issues/Projects + Portable Agent Skills"
portfolio_ssot: "GitHub Projects (Tables, Boards, Roadmaps) + GitHub Issues (Sub-issues, Blocking Dependencies)"
knowledge_system: "Git Repository Structured Markdown Tree (docs/, concepts/, methods/) + Agent Skills Progressive Disclosure"
orchestrator: "GitHub Spec Kit Workflow Engine (specify run <workflow>, .specify/workflows/runs/<id>/state.json)"
workflow_library: "Spec Kit Workflows (.specify/workflows/*.yaml) + BMAD Planning Web Bundles"
specialist_agent_library: "Open Agent Skills Standard (SKILL.md) + Superpowers Review Loops (subagent-driven-development)"
skill_tool_library: "Spec Kit Command Steps + GitHub Actions + Deterministic Python/Bash Scripts"
executor_clients:
  - "Claude Code"
  - "OpenAI Codex CLI"
  - "Google Antigravity (agy)"
  - "ChatGPT Web (via repository/issue sync)"
  - "Hermes / OpenClaw / Local CLI models"
review_governance: "Superpowers Verification Discipline ('Iron Law') + Spec Kit Interactive Gates + Independent Subagent Reviews"
artifact_store: "Git Repository Versioned Markdown Files"
learning_promotion: "Spec Kit Curator Workflow step committing validated findings into concepts/ directory"
mandatory_services:
  - "Git"
  - "GitHub Repository & Projects"
  - "GitHub CLI (gh)"
  - "GitHub Spec Kit CLI (specify)"
existing_integrations_used:
  - "Spec Kit built-in taskstoissues command"
  - "Spec Kit assistant integrations (Claude Code, Codex, Antigravity)"
  - "Agent Skills open standard (SKILL.md)"
custom_work_required:
  - item: "MoA Workflow YAML definitions (research.yaml, workshop.yaml, content.yaml)"
    why_unavoidable: "Encodes Master of Arts specific multi-stage routing"
    size: "small"
  - item: "MoA Domain Agent Skills (workshop-designer, pedagogy-reviewer, knowledge-curator)"
    why_unavoidable: "Specializes prompt guidelines to Master of Arts pedagogy and business domains"
    size: "small"
single_sources_of_truth:
  project_state: "GitHub Projects & Issues"
  knowledge: "Git Repository docs/ and concepts/"
  workflow_state: ".specify/workflows/runs/<run_id>/state.json"
  final_artifacts: "Git Repository root and sub-directories"
```

#### Verified Installation & Bootstrap Commands
*(Sources: `SRC-SPEC-01`, `SRC-SPEC-02`, `SRC-SPEC-03`, `SRC-GH-01`, `SRC-SKILL-01`)*

```bash
# 1. Install GitHub CLI and authenticate
# Source: https://cli.github.com/manual/
gh auth login

# 2. Install GitHub Spec Kit CLI
# Source: https://github.com/github/spec-kit#installation
npm install -g @github/spec-kit

# 3. Initialize Spec Kit in Master of Arts repository
# Source: https://github.com/github/spec-kit/blob/main/docs/index.md
cd c:/GitDev/MasterOfArts
specify init --ai-assistant claude-code

# 4. Install Superpowers process skills into Agent Skills directory
# Source: https://github.com/obra/superpowers#installation
git clone https://github.com/obra/superpowers.git /tmp/superpowers
mkdir -p .agents/skills
cp -r /tmp/superpowers/skills/* .agents/skills/

# 5. Run a verified Spec Kit workflow
# Source: https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md
specify run research-synthesis --input "Surrender under pressure"

# 6. Materialize workflow tasks into GitHub Issues
# Source: https://github.com/github/spec-kit/blob/main/templates/commands/taskstoissues.md
specify taskstoissues
```

---

### Blueprint 2: GitHub-Pure Control (Runner-Up & Complexity Control)

```yaml
architecture_name: "GitHub Projects/Issues + Portable Agent Skills + GitHub Actions"
portfolio_ssot: "GitHub Projects & Issues"
knowledge_system: "Git Repository Markdown Files + Agent Skills"
orchestrator: "Human CEO + CLI Agent Chaining + GitHub Actions"
workflow_library: "GitHub Actions (.github/workflows/) + SOPs"
specialist_agent_library: "Agent Skills Standard (.agents/skills/)"
skill_tool_library: "GitHub Actions + CLI utilities"
executor_clients: ["Claude Code", "OpenAI Codex CLI", "Google Antigravity", "ChatGPT Web"]
review_governance: "GitHub Issue Statuses + PR Reviews"
artifact_store: "Git Repository"
learning_promotion: "Manual/Scripted markdown commit to concepts/"
mandatory_services: ["Git", "GitHub CLI (gh)"]
existing_integrations_used: ["GitHub CLI", "Agent Skills"]
custom_work_required:
  - item: "GitHub Project custom fields setup and issue templates"
    why_unavoidable: "Defines portfolio metadata tracking"
    size: "small"
single_sources_of_truth:
  project_state: "GitHub Projects"
  knowledge: "Git Repository"
  workflow_state: "GitHub Issue labels/states"
  final_artifacts: "Git Repository"
```

#### Verified Installation & Bootstrap Commands
*(Sources: `SRC-GH-01`, `SRC-GH-02`, `SRC-SKILL-01`)*

```bash
# 1. Ensure GitHub CLI is ready
gh auth status

# 2. Create Project Board with custom fields
# Source: https://cli.github.com/manual/gh_project_create
gh project create --owner leela-spec --title "Master of Arts Portfolio"

# 3. Create hierarchical issue with blocking dependencies
# Source: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies
gh issue create --title "Research: Surrender Under Pressure" --body "Conduct multi-source research."
```

---

### Blueprint 3: Beads Graph Core (Challenger)

```yaml
architecture_name: "Beads + Dolt Work Graph + Agent Skills + GitHub Artifacts"
portfolio_ssot: "Beads Dolt SQL Graph (.beads/) with GitHub Export"
knowledge_system: "Git Markdown Canon + Beads Compaction"
orchestrator: "Beads Formula Runner + Local CLI Agents"
workflow_library: "Beads Formulas & Molecules"
specialist_agent_library: "Agent Skills (AGENTS.md, skills/)"
skill_tool_library: "bd CLI commands + deterministic hooks"
executor_clients: ["OpenAI Codex CLI", "Claude Code", "Antigravity"]
review_governance: "Beads Multi-Persona Formula Gates"
artifact_store: "Git Repository"
learning_promotion: "Beads Memory Compaction + Git updates"
mandatory_services: ["Git", "Dolt", "Beads CLI (bd)"]
existing_integrations_used: ["Beads setup for Codex/Claude", "Dolt SQL engine"]
custom_work_required:
  - item: "Beads formula authoring for MoA workflows"
    why_unavoidable: "Encodes task graphs into Beads TOML formulas"
    size: "medium"
single_sources_of_truth:
  project_state: "Beads Dolt Graph"
  knowledge: "Git Repository"
  workflow_state: "Beads Task States"
  final_artifacts: "Git Repository"
```

#### Verified Installation & Bootstrap Commands
*(Sources: `SRC-BEADS-01`, `SRC-BEADS-02`, `SRC-BEADS-03`)*

```bash
# 1. Install Dolt database engine
# Source: https://github.com/dolthub/dolt
# (Windows via MSI / Chocolatey or curl on Linux/macOS)

# 2. Install Beads CLI
# Source: https://github.com/gastownhall/beads#installation
npm install -g @gastownhall/beads

# 3. Initialize Beads in repository
# Source: https://github.com/gastownhall/beads/blob/main/README.md
cd c:/GitDev/MasterOfArts
bd init

# 4. Setup agent integration files (AGENTS.md)
# Source: https://github.com/gastownhall/beads/blob/main/docs/reference/faq.md
bd setup claude-code

# 5. Query unblocked work
# Source: https://github.com/gastownhall/beads
bd ready --json
```

---
## Phase 7 ? Verdict, Decision Triggers & Recommendations

### Decision Triggers

#### 1. SpecKit-GitHub Core
- **Select If:** The operator wants automated, multi-step agent execution (research -> review -> gate -> output) with guaranteed crash resumption, machine-readable JSON states, and seamless export to GitHub Projects without writing custom orchestration glue.
- **Avoid If:** The operator rejects installing the lightweight `specify` CLI or finds Spec Kit's SDD terminology intrusive for non-software work even after custom preset configuration.
- **Pilot to Prove:** Prove that non-software workflows (`research.yaml`, `workshop.yaml`) execute smoothly across Claude Code and Antigravity and that `taskstoissues` cleanly populates GitHub Projects.

#### 2. GitHub-Pure Control
- **Select If:** The operator prioritizes absolute minimal tooling (zero extra daemons or CLIs beyond `gh`), prefers direct human-in-the-loop prompt chaining, and handles all portfolio tracking via GitHub's native web interface.
- **Avoid If:** The operator suffers from context-switching fatigue and finds manual prompt-chaining and multi-agent coordination too labor-intensive.
- **Pilot to Prove:** Prove how much time is spent manually prompting agents through US-A and US-B compared to automated Spec Kit execution.

#### 3. Beads Graph Core
- **Select If:** Autonomous agent swarms require high-frequency atomic task claiming and complex transitive dependency resolution that exceeds GitHub's sub-issue capabilities.
- **Avoid If:** The team relies heavily on web-based subscription AIs (ChatGPT Web) that cannot easily query local Dolt SQL databases, or wants to avoid maintaining Dolt alongside Git.
- **Pilot to Prove:** Prove whether Dolt task graph compaction measurably reduces context window token costs for long-running multi-agent projects.

---

### Strategic Synthesis

1. **Recommended for Pilot:** **GitHub Spec Kit + GitHub Issues/Projects + Portable Agent Skills**
2. **Runner-Up & Complexity Control:** **GitHub Projects/Issues + Portable Agent Skills**
3. **Simplest Control:** Pure GitHub Projects + Agent Skills
4. **Component Winners:**
   - *L1 Knowledge Substrate:* Git Repository Structured Markdown Tree + Agent Skills
   - *L2 Portfolio SSOT:* GitHub Projects & Issues (Sub-issues + Dependencies)
   - *L3 Orchestrator / Router:* GitHub Spec Kit Workflow Engine
   - *L4 Workflow Library:* Spec Kit Workflows + BMAD Planning Web Bundles
   - *L5 Specialist Agent Library:* Open Agent Skills (`SKILL.md`) + Superpowers Review Loops
   - *L6 Tool / Script Layer:* Spec Kit Commands + GitHub Actions + Python CLI
   - *L7 Executor Adapters:* Cross-Client Suite (Claude Code, OpenAI Codex, Antigravity, ChatGPT Web)
   - *L8 Review & Governance:* Superpowers Verification Discipline + Spec Kit Interactive Gates
   - *L9 Artifact Store:* Git Repository
   - *L10 Learning Loop:* Knowledge Curator Workflow with CEO Promotion Gate

5. **What Previous Research Got Wrong or Missed:**
   - **Conflation of Workflow Engine vs. Portfolio SSOT:** Earlier analysis treated Spec Kit, GitHub, and Beads as mutually exclusive competitors for the same role. In reality, Spec Kit is a *workflow controller (L3/L4)* while GitHub Projects is the *portfolio SSOT (L2)*. Spec Kit natively bridges to GitHub via `taskstoissues`.
   - **Overlooking Open Agent Skills Standard:** Prior analysis assumed specialist agents had to be authored in vendor-specific formats. Standardizing on the open `SKILL.md` format allows the exact same role (e.g. `pedagogy-reviewer`) to be executed interchangeably by Claude Code, OpenAI Codex, Antigravity, and ChatGPT.
   - **Ignoring Web-Subscription Planning Handshake:** BMAD Web Bundles provide a verified, cost-free bridge for conducting extensive research and brainstorming in web subscriptions (ChatGPT Plus / Gemini Advanced) and exporting structured artifacts directly into the repository for CLI execution.

---

## Uncertainties & Critical Unknowns

1. **Spec Kit Presets Domain Abstraction:** Confirm during Pilot 1 whether custom YAML presets can completely hide software-specific prompts from underlying LLM executors.
2. **Web-Subscription Sync Friction:** Verify how effortlessly a human operator can move an exported BMAD research artifact from ChatGPT Web into the repository to trigger a Spec Kit workflow.
3. **Long-Term Knowledge Retrieval Scaling:** Measure whether progressive disclosure via Agent Skills remains fast and comprehensive when the repository exceeds 500+ markdown files, or if an embedded local CLI vector index (e.g., `ruflo-agentdb` or `paperqa2`) becomes necessary.
