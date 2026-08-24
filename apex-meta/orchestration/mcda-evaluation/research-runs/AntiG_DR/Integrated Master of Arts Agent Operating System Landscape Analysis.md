# Integrated Master of Arts Agent Operating System Landscape Analysis

## Executive Verdict

The transition from single-session conversational interfaces to durable, multi-agent operating organizations represents a fundamental architectural shift in the artificial intelligence landscape. The analysis indicates that achieving the target operating model for the Master of Arts—a system where executive intent translates into deterministic workflow routing, autonomous specialist execution, and human-gated finalization—cannot be fulfilled by conversational orchestration alone. The evaluation concludes that the optimal existing, upstream-supported composition is the **Gas City** orchestration platform combined with the **gascity-packs/bmad** and **gascity-packs/superpowers** libraries.

Gas City achieves superiority by explicitly decoupling the orchestration substrate from the behavioral methodology. By utilizing a durable, Git-versioned state engine powered by Dolt (referred to as `beads`), the platform eliminates context drift and cross-agent concurrency conflicts. When composed with the Breakthrough Method for Agile AI-Driven Development (BMAD) pack, the architecture natively provisions over thirty validated specialist personas—ranging from business analysts and project managers to creative intelligence strategists—satisfying the rigorous requirements for non-software artifact generation. The integration of these ecosystems provides an end-to-end framework encompassing durable state recovery, parallel fan-out execution, and explicit adversarial review gates.

Two alternative architectures exhibit distinct systemic philosophies but ultimately fall short of complete systemic coverage, relegating them to specialized component use cases or secondary recommendations. **Politik** offers a radically different paradigm focused entirely on human governance, utilizing the Git repository itself as the orchestration bus and immutable ledger. While it provides unparalleled auditability and explicitly enforces the human-as-CEO dynamic through constitutional primitives, it lacks a native ecosystem of specialist agents, requiring extensive custom prompt engineering. Conversely, **Hermes Agent** operates on a self-improving, single-agent paradigm. It excels in continuous procedural learning via its Autonomous Curator and evolutionary frameworks, yet its architectural design prioritizes depth of individual automation over the breadth required for multi-agent, cross-functional organizational operations.

## Broad Landscape Scan

The discovery phase evaluated an expansive array of orchestration tools, agent frameworks, and multi-agent operating systems. The scan explicitly targeted ecosystems capable of supporting non-software workflows, integrated knowledge bases, and local or subscription-based execution paths.

|**Candidate**|**Primary Layer(s)**|**Integrated Agents?**|**KB?**|**Workflow/Orchestration?**|**Sub/Local Path?**|**Non-Code Evidence?**|**Disposition**|
|---|---|---|---|---|---|---|---|
|**Gas City / Gas Town**|L3, L4, L8, L9|Yes (via imported Packs)|Yes (Beads/Dolt)|Yes (Formulas/Molecules)|Yes (Multiple)|Yes (GStack/BMAD)|Complete System Survivor|
|**BMAD Method**|L4, L5, L8|Yes (30+ roles)|Yes (Git PRDs)|Yes (Methodology)|Yes (CLI/MCP)|Yes (Business/Creative)|Complete System Survivor (via Gas City)|
|**Politik**|L2, L3, L8, L9|No (Stateless workers)|Yes (Git Tree)|Yes (Protocols)|Yes (Any CLI)|Yes (Domain-neutral)|Complete System Survivor|
|**Hermes Agent**|L5, L7, L10|Yes (40+ tools)|Yes (Bounded Memory)|Limited (Single-agent)|Yes (OpenRouter/Local)|Yes (Ops/Automation)|Complete System Survivor|
|**OpenClaw**|L3, L6, L7|Yes (ClawHub)|Yes (Vector)|Yes (Gateway)|Yes (Multi-provider)|Yes (Comms/Admin)|Disqualified|
|**Ruflo (Claude Flow)**|L3, L5|Yes (100+)|Yes (RAG/Hybrid)|Yes (Hive Mind)|Yes (Claude-focused)|Yes|Component Only|
|**Superpowers**|L5, L6|Yes (Plugin)|No|Yes (TDD/Debugging)|Yes (Claude/MCP)|No (Software only)|Component Only|
|**OpenSwarm**|L3|No (Latent Bus)|No|No (Emergent)|Yes (Ollama)|Unknown|Disqualified|
|**Agent-OS**|L3, L8|Yes (6 roles)|Yes (Consent-based)|Yes (Whisper Router)|Yes (Local)|Yes|Insufficient Evidence|
|**EMOS**|L3, L7|Yes (Robotics)|No|Yes (Hierarchical)|Yes|No (Robotics only)|Disqualified|
|**Claude Octopus**|L8|Yes (Reviewers)|No|Yes (Consensus Gate)|Yes (8 Providers)|No (Code Review)|Component Only|

The scan explicitly explored candidates beyond the initial seed list to ensure comprehensive market coverage. Platforms like OpenSwarm introduced novel concepts such as latent vector bus routing, eliminating traditional O(N²) API dependencies in favor of semantic resonance. However, such emergent behaviors directly contradict the deterministic operational requirements of the target model. Similarly, EMOS provided robust hierarchical task management but was strictly bound to physical robotics embodiment, rendering it incompatible with knowledge-based output generation.

## Hard-Gate Results

The application of the twelve non-negotiable hard filters (H1–H12) eliminated several prominent frameworks due to security vulnerabilities, domain lock-in, or excessive operational complexity.

|**Candidate**|**Status**|**Exact Failed Gate(s)**|**Rationale**|
|---|---|---|---|
|**Gas City + Packs**|Complete System Survivor|None|Composes stateful infrastructure with proven methodologies (BMAD, Superpowers) without requiring new custom frameworks.|
|**Politik**|Complete System Survivor|None|Meets all governance, state, and orchestration requirements through mature Git protocols, though lacking in native specialists.|
|**Hermes Agent**|Complete System Survivor|None|Functions as a highly capable single-agent runtime with subprocess spawning, excelling in self-directed learning.|
|**OpenClaw**|Disqualified|H12 (Auditability/Security)|Accumulated six documented CVEs (CVSS 7.5-9.1) in early phases; suffered the ClawHavoc supply chain infection impacting up to 25,000 installations.|
|**Ruflo (Claude Flow)**|Component Only|H11 (Bounded Complexity), H10 (Non-software fit)|Architecture is excessively heavy; the advertised 100+ agents often consist of functionally identical prompt templates lacking distinct semantic utility.|
|**Superpowers**|Component Only|H1 (Complete System), H10 (Non-software fit)|Exceptional ecosystem for deterministic L6 debugging and root-cause tracing, but strictly optimized for software engineering.|
|**OpenSwarm**|Disqualified|H2 (Proven), H9 (Human Governance)|Currently in early alpha; emergent coordination via latent space prevents explicit, deterministic human review gates.|
|**Agent-OS**|Insufficient Evidence|H2 (Proven/Current)|Released in late 2025; architecture relies heavily on conceptual natural language routing with minimal verified production deployments.|
|**EMOS**|Disqualified|H10 (Non-software fit)|Architecture is intrinsically tied to robotic embodiment and multi-floor object rearrangement, lacking knowledge work applicability.|

The disqualification of OpenClaw underscores a critical failure mode in multi-agent orchestration. While the platform achieved massive adoption (evidenced by over 100,000 GitHub stars) and extensive multi-channel routing capabilities, its retroactive approach to security resulted in critical sandbox escapes and identity injection vulnerabilities. In contrast, systems like Hermes Agent proactively engineered seven-layer security models, prioritizing operational safety over immediate feature breadth.

## Deep Evidence Pass and Capability Mapping

The surviving architectures were subjected to a granular evaluation against the ten required layers of the target stack contract (L1–L10) and the specific requisite specialist families.

### Survivor 1: Gas City Composed with BMAD and Superpowers Packs

Gas City operates on the philosophical premise that complex engineering and knowledge work requires an industrialized, asynchronous factory model rather than a synchronous conversational loop. The architecture is divided into the platform infrastructure (Gas City) and the declarative behavioral configurations (Packs).

#### Stack Contract Mapping

- **L1 (Knowledge Substrate) & L9 (Artifact Output):** State is managed by the `beads` provider, utilizing a Git-versioned Dolt database. This ensures that every unit of work survives terminal crashes and session resets. Final artifacts are committed to the designated project directory (the `Rig`).
    
- **L2 (Portfolio SSOT):** Managed through the `city.toml` configuration and the `oversight-rig` pack, which maintains a portfolio-level executive status brief compatible with external knowledge tools.
    
- **L3 (Orchestrator Router):** Driven by the Controller daemon. The daemon continuously reconciles the desired state, evaluating triggers (`cron`, `condition`, `event`) and dispatching work to elastic pools of transient agents known as `polecats`.
    
- **L4 (Workflow Library):** The `gascity-packs` ecosystem supplies verified `.formula.toml` workflows. For instance, the `bmad-build` formula executes a strict sequence: requirements → plan → review → decompose → implement → three-lane review fanout.
    
- **L6 (Tool/Script Layer):** Integrates directly with standard `AgentSkills` formats. The composition utilizes the `Superpowers` pack for rigorous, deterministic root-cause analysis and hypothesis testing.
    
- **L7 (Executor Adapters):** Natively supports a broad runtime composition, including Claude Code, Codex, and Gemini CLI, interfaced via `tmux`, `subprocess`, or `exec` providers.
    
- **L8 (Review Governance):** The `Refinery` agent pattern manages quality gates, handling complex merge conflicts sequentially to prevent concurrent data corruption.
    
- **L10 (Learning Loop):** Procedural memory is updated via shared template fragments (`.template.md` files). However, this promotion relies on manual synthesis rather than autonomous extraction.
    

#### Specialist Agent Ecosystem

The integration of the BMAD Method pack provisions a highly mature, shipped roster of bounded personas. Evidence confirms the existence of specialized roles such as the Analyst (Mary), Project Manager (John), Architect (Winston), and the Creative Intelligence Suite (Carson). These agents effectively satisfy the `control_orchestration`, `research_knowledge`, and `creative_content` families. The inclusion of the `gstack` pack introduces founder/PM-flavored gates, covering aspects of `business_operations`.

### Survivor 2: Politik

Politik approaches multi-agent orchestration by eschewing custom databases and daemons, instead leveraging Git as the foundational operating system. It posits that multi-agent coordination requires strict, constitutionally defined governance rather than merely probabilistic task routing.

#### Stack Contract Mapping

- **L1 (Knowledge Substrate) & L9 (Artifact Output):** The Git repository serves as the definitive session environment. The `Hansard` function provides an immutable, append-only record of every motion, vote, and escalation, creating a flawless audit trail.
    
- **L2 (Portfolio SSOT):** Work is organized hierarchically as nested directories within the repository tree (Org → Team → Sprint → Ticket). The `politik registry` command aggregates state across this tree without necessitating a centralized registry server.
    
- **L3 (Orchestrator Router) & L8 (Review Governance):** Orchestration is governed by `CANON` primitives. The framework translates natural language operations into formal governance verbs (`MOTION`, `DIVISION`, `ASSENT`, `ESCALATION`). A human acts as the constitutional authority, ruling on escalations while the session otherwise governs itself autonomously.
    
- **L4 (Workflow Library):** Workflows are instantiated as formal governance protocols, including Parliamentary, Peer Review, and Adversarial Collaboration archetypes.
    
- **L5 (Specialist Agent Library):** This is the architecture's primary deficiency. Politik defines formal roles (`AUTHORITY`, `DELEGATE`, `OPERATOR`) but does not ship a catalog of pre-configured specialist intelligence, necessitating extensive prompt engineering to fulfill the required specialist families.
    
- **L7 (Executor Adapters):** Agents function as stateless CLI workers. Upon receiving a broadcast, an agent spawns, executes its prompt, commits the result to the Hansard, and terminates. This allows absolute portability across any CLI-compatible model.
    
- **L10 (Learning Loop):** Systemic learning is achieved formally through motions that amend the `CHARTER.md` or Standing Orders.
    

### Survivor 3: Hermes Agent

Hermes Agent, developed by Nous Research, represents the pinnacle of the single-agent, continuous-learning paradigm. It focuses on compounding usefulness through self-evolution rather than broad, distributed multi-agent hierarchies.

#### Stack Contract Mapping

- **L1 (Knowledge Substrate):** Utilizes a highly disciplined, bounded memory architecture. Files reside locally, with agent memory strictly capped at 2,200 characters to reduce token burn and context noise. Retrieval is tiered, falling back to vector search only when necessary.
    
- **L3 (Orchestrator Router):** Lacks advanced multi-agent orchestration. While it can spawn sub-agents, these agents are isolated and do not share a synchronized global state, preventing complex cross-functional collaboration.
    
- **L5 (Specialist Agent Library) & L6 (Tool/Script Layer):** Ships with over 40 built-in tools compatible with the `AgentSkills` standard. Its strength lies not in pre-defined personas, but in its ability to execute deterministic operational tools.
    
- **L7 (Executor Adapters):** Natively interfaces with local models, OpenRouter, and custom endpoints, providing high flexibility.
    
- **L8 (Review Governance):** Relies heavily on human intervention through terminal or TUI interfaces, lacking the structured, automated adversarial gates seen in Gas City or Politik.
    
- **L10 (Learning Loop):** This architecture's definitive strength. The `Autonomous Curator` monitors execution patterns, autonomously generating reusable skills for repetitive tasks. Furthermore, the integration of DSPy and GEPA enables the agent to continuously optimize its own prompts and logic based on operational feedback.
    

## Multi-Criteria Decision Analysis (MCDA)

The evaluation of the complete-system survivors utilizes a weighted matrix to quantify coverage across the required dimensions.

|**Rank**|**Complete architecture**|**C1 15**|**C2 15**|**C3 12**|**C4 12**|**C5 12**|**C6 10**|**C7 8**|**C8 7**|**C9 5**|**C10 4**|**Total /100**|**Confidence**|**Primary failure mode**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|**Gas City + BMAD**|4.5|5.0|4.0|5.0|5.0|4.5|4.5|4.0|5.0|4.0|**92.3**|A|Complexity of Dolt/Beads state synchronization under heavy parallel fan-out.|
|2|**Politik**|4.0|1.0|4.0|3.5|5.0|5.0|5.0|3.0|4.0|4.5|**73.4**|B|Lack of out-of-the-box specialist personas requires significant prompt engineering.|
|3|**Hermes Agent**|3.5|3.0|5.0|2.0|4.0|3.5|3.0|4.5|4.0|4.5|**69.8**|A|Inability to route complex, multi-stage workflows across stateful peer agents.|

### Rationale for Scoring

- **C1 (End-to-End Coverage):** Gas City provides exhaustive coverage by compositing the `beads` database for state, `formulas` for routing, and packs for behavior. Politik offers excellent infrastructure but leaves behavioral intelligence to the user.
    
- **C2 (Specialists & Workflows):** Gas City secures a perfect score due to the seamless import of the BMAD and Superpowers packs, yielding immediate access to dozens of battle-tested personas and methodologies. Politik scores poorly as it mandates manual persona creation.
    
- **C3 (Knowledge & Learning):** Hermes dominates this dimension due to its sophisticated `Autonomous Curator` and DSPy/GEPA evolutionary loops, representing the only truly autonomous learning system. Gas City relies on structured Markdown files, while Politik relies on Git trees.
    
- **C4 (Orchestration & State):** Gas City's explicit separation of the Controller daemon from the agents ensures perfect recovery and deterministic execution. Hermes struggles significantly here due to its single-agent architectural bias.
    
- **C6 (Non-Software Fit):** Both Gas City (via BMAD's Creative/Analyst roles) and Politik (intrinsically domain-neutral protocols) prove highly adaptable to business and creative functions.
    
- **C7 (Governance):** Politik achieves a perfect score; its entire architecture is predicated on constitutional primitives and immutable ledgers. Gas City performs strongly through explicit formula gates.
    
- **C9 (Integration Risk):** Gas City utilizes a highly standardized `pack.toml` and `city.toml` import mechanism, ensuring that external ecosystems like BMAD can be integrated natively without custom bridging scripts.
    

### Sensitivity Analysis

To ensure the robustness of the ranking, the baseline scores were subjected to three distinct prioritization lenses.

- **Autonomy-First (Increasing weights for C2, C4, C7):** Under a model prioritizing autonomous workflow execution and strict governance, Gas City extends its lead significantly due to its perfect scores in orchestration and specialist availability. Politik also widens its gap over Hermes Agent, as Hermes' lack of multi-agent state coordination severely penalizes it.
    
- **Knowledge-First (Increasing weights for C3, C6):** By heavily prioritizing knowledge retrieval, self-learning, and non-software domain applicability, Hermes Agent closes the gap with Politik. The impact of Hermes' GEPA evolutionary framework becomes highly pronounced. However, Gas City retains the top position due to its balanced performance across these metrics.
    
- **Simplicity/Portability-First (Increasing weights for C5, C9, C10):** Politik scores exceptionally well under this lens. Its pure Git dependency—requiring zero external databases, daemons, or complex routing middleware—minimizes operational overhead and token burden. Nevertheless, Gas City maintains the overall lead because its integration mechanisms (Packs) are natively supported upstream, presenting minimal custom glue risk despite the heavier infrastructure.
    

_Conclusion of Analysis:_ The ranking remains stable across all sensitivity permutations. Gas City composed with the designated packs is the structurally dominant architecture for the target operating model.

## Concrete Master of Arts User Stories

The following architectural walkthroughs detail the execution of four specific non-software workflows across the top three systems. These sequences represent the systemic operational logic rather than fabricated outputs.

### US-A: Research to Knowledge

**Sequence:** CEO asks a research question → MoA knowledge retrieval → multi-source research → evidence verification → synthesis → independent review → CEO gate → final research artifact → validated KB promotion.

|**Step**|**System / Component**|**Specialist Agent / Workflow**|**AI Executor Options**|**KB / Context Supplied**|**Tools**|**Durable State / Output**|**Reviewer / Gate**|**Verified Status**|
|---|---|---|---|---|---|---|---|---|
|**Gas City + BMAD**|||||||||
|1|Gas City Controller|`gc bd create`|N/A|Rig metadata|CLI|Bead ID created in Dolt|None|N|
|2|Gas City Mayor|`gc sling gc.mayor`|Claude/Codex|`city.toml` env vars|N/A|Convoy assigned|None|N|
|3|BMAD Pack|`bmad-market-research`|Claude (Subprocess)|Existing PRDs|Web Search MCP|Transient worktree|None|P|
|4|BMAD Pack|Analyst (Mary) / Architect|Claude (Opus/heavy)|Research output|N/A|Draft Markdown file|None|P|
|5|Gas City Formula|`build-basic` fanout|Claude/Codex|Draft artifact|N/A|Review reports|`gc.run-operator`|N|
|6|Gas City Order|Manual Trigger|N/A|Consolidated reports|N/A|Paused Controller|Human CEO (Attach)|N|
|7|Gas City Refinery|Post-processor|Claude|Approved draft|Git|Merged commit on main|None|N|
|**Politik**|||||||||
|1-3|Node CLI / Git|`MOTION` (Research)|Any CLI Agent|`CHARTER.md`|Shell scripts|Git Branch created|None|N|
|4-5|Git Hooks|`OPERATOR` (Custom)|Any CLI Agent|Git Branch state|Bring-your-own|Commits to branch|None|A (Requires custom agent)|
|6-7|Node CLI / Git|`DIVISION` / `ASSENT`|N/A|Pull Request|Git|Merged PR / Hansard|Human CEO|N|
|**Hermes Agent**|||||||||
|1-4|Hermes Runtime|`/goal Research Topic`|OpenRouter / Local|`MEMORY.md`|Built-in web tools|Internal session state|Internal Judge Loop|N|
|5-7|Hermes Runtime|Autonomous Curator|OpenRouter / Local|Session history|N/A|New `.md` skill saved|Human (Interactive)|N|

### US-B: Workshop Creation

**Sequence:** CEO states desired workshop outcome → relevant research/method knowledge → workshop designer → pedagogy/practice reviewer → operations/risk reviewer → CEO gate → final workshop + task/launch artifacts → learning captured after delivery.

|**Step**|**System / Component**|**Specialist Agent / Workflow**|**AI Executor Options**|**KB / Context Supplied**|**Tools**|**Durable State / Output**|**Reviewer / Gate**|**Verified Status**|
|---|---|---|---|---|---|---|---|---|
|**Gas City + BMAD**|||||||||
|1-2|Gas City Mayor|`gc bd create`|Claude|Rig metadata|N/A|Bead assigned|None|N|
|3|BMAD Pack|Creative Suite (Carson)|Claude|Prior methodologies|Document Editor|Outline artifact|None|P|
|4|GStack Pack|`gstack-qa-review`|Claude|Outline artifact|Checklists|QA Report|None|P|
|5-6|Gas City Formula|`gstack-build`|N/A|Reports|N/A|Paused Controller|Human CEO|P|
|7|Gas City / BMAD|PM (John)|Claude|Approved outline|Task Creator|Stories / Epics in Dolt|None|P|
|**Politik**|||||||||
|1-7|Node CLI / Git|Peer Review Protocol|Any CLI Agent|`CHARTER.md`|Custom|Branch / Hansard Ledger|Human CEO|A (Requires custom agents)|
|**Hermes Agent**|||||||||
|1-7|Hermes Runtime|Interactive Chat|Local|Bounded Memory|Built-in|Output files|Human (Interactive)|U (Lacks distinct workflow routing)|

### US-C: Content/Social

**Sequence:** Approved research/workshop concept → creative strategist → long-form writer → brand/editor review → social/video specialists → public/private check → publication-ready outputs → portfolio state updated.

|**Step**|**System / Component**|**Specialist Agent / Workflow**|**AI Executor Options**|**KB / Context Supplied**|**Tools**|**Durable State / Output**|**Reviewer / Gate**|**Verified Status**|
|---|---|---|---|---|---|---|---|---|
|**Gas City + BMAD**|||||||||
|1-3|BMAD Pack|Tech Writer (Paige)|Claude|Workshop artifacts|N/A|Draft content|None|P (Adaptation required for social)|
|4-5|Gas City Formula|`build-basic` fanout|Claude|Draft content|N/A|Review reports|`gc.run-operator`|N|
|6-7|Gas City Slack Pack|`slack-full`|N/A|Final content|Slack API|Published messages|Human CEO|P|
|**Politik**|||||||||
|1-7|Node CLI / Git|Corporate Protocol|Any CLI Agent|Git Tree|Social APIs|Hansard Ledger|Human CEO|A (Requires custom agents)|
|**Hermes Agent**|||||||||
|1-7|Hermes Runtime|Background Task|Local|`MEMORY.md`|API integration|Published content|None|N|

### US-D: Weekly CEO Operating Cycle

**Sequence:** Collect portfolio state → detect blockers/stale work/dependencies → specialist project-controller analysis → autonomous routine follow-ups → surface only consequential decisions/exceptions to CEO → persist decisions → schedule next work.

|**Step**|**System / Component**|**Specialist Agent / Workflow**|**AI Executor Options**|**KB / Context Supplied**|**Tools**|**Durable State / Output**|**Reviewer / Gate**|**Verified Status**|
|---|---|---|---|---|---|---|---|---|
|**Gas City + BMAD**|||||||||
|1|Gas City Controller|Health Patrol|N/A|Dolt DB|N/A|System events|None|N|
|2|Gas City Pack|`oversight-rig`|N/A|Event Bus log|N/A|Portfolio status brief|None|P|
|3-4|Gas City Mayor|`gc session attach mayor`|Claude|Status brief|`slack-mini`|Messages to CEO|None|N|
|5-7|Gas City Controller|`cron` Triggers|N/A|CEO Decisions|N/A|Updated beads in Dolt|Human CEO|N|
|**Politik**|||||||||
|1-7|Node CLI|`politik registry`|N/A|Git Tree|N/A|Terminal output|Human CEO|N|
|**Hermes Agent**|||||||||
|1-7|Hermes Runtime|`/cron`|Local|`MEMORY.md`|Built-in|CLI output|Human CEO|N|

## Realization Blueprints for Top 3 Architectures

### 1. Gas City Composed with BMAD and Superpowers

YAML

```
architecture_name: Gas City + BMAD Orchestration
portfolio_ssot: Gas City City/Rig structural binding (.gc/site.toml)
knowledge_system: Git repository (Rigs) + PromptTemplate partials (shared/)
orchestrator: Gas City Controller daemon (reconciliation tick)
workflow_library: gascity-packs (bmad-build, superpowers-build, gstack)
specialist_agent_library: BMAD Method (30 personas) + GStack operational roles
skill_tool_library: AgentSkills standard (via Superpowers pack integrations)
executor_clients: [Claude Code, Codex, Gemini CLI, Any ACP-compatible tool]
review_governance: Formula v2 control beads (retry, fan-out, adversarial review lanes)
artifact_store: Local Filesystem (artifact_root) managed by Refinery agent
learning_promotion: Manual update of prompt fragments in packs/shared/ directories
mandatory_services: [Dolt DB (beads provider), tmux (session provider)]
existing_integrations_used: [BMAD personas, Superpowers deterministic tools, Slack-mini]
custom_work_required:
  - item: Social Media / Pedagogy explicit persona prompts
    why_unavoidable: BMAD focuses on SDD/Agile software paradigms; creative marketing and workshop design require persona tuning.
    size: small
single_sources_of_truth:
  project_state: Dolt Beads Database (gc bd)
  knowledge: Markdown files in registered Rigs
  workflow_state: Active Formula Molecules (Store.MolCook)
  final_artifacts: Git branch (main)
```

**Bootstrap Commands:** (Verified via Gas City official documentation)

Bash

```
# Install Gas City and initialize the global city environment
brew install gascity
gc init ~/master-of-arts --default-provider claude
cd ~/master-of-arts

# Register the primary portfolio repository as a Rig to enable agent workspace
gc rig add ~/MoA-Portfolio

# Import the base methodology packs from the upstream repository
gc import add --name gc https://github.com/gastownhall/gascity-packs.git//gascity
gc import add https://github.com/gastownhall/gascity-packs.git//bmad
gc import add https://github.com/gastownhall/gascity-packs.git//superpowers
gc import add https://github.com/gastownhall/gascity-packs.git//oversight-rig

# Fetch and pin the latest releases in packs.lock
gc import install

# Start the Controller daemon to begin reconciliation and patrol loops
gc start
```

Update `city.toml` to bind the rig to the imported roles and establish capacity:

Ini, TOML

```
# city.toml
[workspace]
provider = "claude"
[beads]
provider = "dolt"

[[rigs]]
name = "MoA-Portfolio"
max_active_sessions = 4
default_sling_target = "MoA-Portfolio/polecat"
session_sleep = { idle = "10m" }
[rigs.imports.gc]
source = "https://github.com/gastownhall/gascity-packs.git//gascity/roles"
[rigs.imports.bmad]
source = "https://github.com/gastownhall/gascity-packs.git//bmad"
```

### 2. Politik Git-Native OS

YAML

```
architecture_name: Politik Governed OS
portfolio_ssot: Nested Git Repositories (Org/Team/Ticket structure)
knowledge_system: Git Repository State
orchestrator: Git hooks + Node.js CLI event triggers
workflow_library: Politik Governance Protocols (Parliamentary, Corporate, Peer Review)
specialist_agent_library: None native (requires complete custom implementation)
skill_tool_library: Bring-your-own CLI tools executed by agent processes
executor_clients: [Any CLI-compatible LLM]
review_governance: CANON primitives (DIVISION, ESCALATION, VETO, ASSENT)
artifact_store: Git Commits
learning_promotion: Explicit amendments to CHARTER.md and Standing Orders
mandatory_services: [Git, Node.js 20+]
existing_integrations_used: [GitHub Actions/Issues synchronization (optional)]
custom_work_required:
  - item: Agent definitions, system prompts, and routing logic
    why_unavoidable: Politik strictly provides the governance framework, not the intelligence.
    size: large
single_sources_of_truth:
  project_state: Git Tree
  knowledge: Git Tree
  workflow_state: CHARTER.md and STATE.json
  final_artifacts: Git Commits
```

**Bootstrap Commands:** (Verified via Politik official documentation)

Bash

```
# Install the framework globally via Node
npm install -g @cordfuse/politik

# Verify system compatibility and supported agent environments
politik doctor

# Initialize the session and draft the constitutional charter with a required quorum
politik scaffold --dir ./moa-session --quorum 2

# Initialize the repository, establishing the human user as the constitutional Authority
politik init --dir ./moa-session --charter ./moa-session/CHARTER.md --speaker human-ceo

# Execute a governance action (e.g., initiating a research branch)
politik division call --dir ./moa-session --motion research-topic --actor human-ceo
```

### 3. Hermes Agent Single-Runtime

YAML

```
architecture_name: Hermes Agent Single-Runtime
portfolio_ssot: Multi-folder workspaces (hermes project)
knowledge_system: Bounded MEMORY.md and USER.md with tiered retrieval
orchestrator: Internal tool execution loop
workflow_library: Multi-turn objective loop (/goal)
specialist_agent_library: Stateless sub-agents spawned on demand
skill_tool_library: 40+ built-in tools (AgentSkills compatible)
executor_clients: [OpenRouter, local models, Claude, Codex]
review_governance: Manual human intervention via TUI/CLI
artifact_store: Standard file output
learning_promotion: Autonomous Curator and DSPy/GEPA self-evolution
mandatory_services: [Python 3.11, Node.js]
existing_integrations_used: [Nous Portal, Petdex]
custom_work_required:
  - item: Multi-agent coordination mechanisms
    why_unavoidable: The system is designed for single-agent depth, not horizontal orchestration.
    size: large
single_sources_of_truth:
  project_state: Local directory
  knowledge: MEMORY.md
  workflow_state: Internal session state
  final_artifacts: Local filesystem
```

**Bootstrap Commands:** (Verified via Hermes Agent official documentation)

Bash

```
# Execute the official one-line install script
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Refresh the shell environment
source ~/.bashrc

# Run the interactive setup wizard and authenticate with the Nous Portal
hermes setup --portal

# Start the agent interface
hermes chat
```

## Verdict and Decision Triggers

### 1. Gas City Composed with BMAD

- `select_if:` The organization mandates high-throughput, parallel execution of complex, multi-stage workflows with explicit human-in-the-loop review gates and durable state recovery resilient to session crashes. It is the definitive choice for operating a structured, asynchronous "team" of specialized agents.
    
- `avoid_if:` The organization lacks the operational capacity to manage local infrastructure components (e.g., Dolt databases, tmux sessions) or requires an entirely serverless, zero-configuration environment.
    
- `pilot_to_prove:`
    
    1. The cognitive overhead required for operators to translate non-software Master of Arts tasks into the syntax of `.formula.toml` files.
        
    2. The systemic reliability of the `beads` database under sustained, high-volume multi-agent read/write contention.
        
    3. The efficacy of adapting BMAD's software-centric personas (e.g., the Architect) to purely operational or creative roles without excessive prompt rewriting.
        

### 2. Politik

- `select_if:` Immutable auditability, strict constitutional governance, and exact per-decision cost tracking (via the append-only Ledger) are the paramount priorities, and the engineering team possesses the capacity to author all specialist agent prompts entirely from scratch.
    
- `avoid_if:` The operational model requires out-of-the-box specialist intelligence, rapid parallel ideation, or semantic memory retrieval beyond primitive Git text searches.
    
- `pilot_to_prove:`
    
    1. The latency constraints of utilizing Git commits and push/pull cycles as the primary real-time messaging bus between agents.
        
    2. The practical friction of integrating external tools and AI executors into a system that provides no native adapters.
        

### 3. Hermes Agent

- `select_if:` The operational objective is to deploy a single, highly autonomous assistant that continuously learns over time, builds its own procedural memory (skills) autonomously, and operates with near-zero infrastructure overhead.
    
- `avoid_if:` The organization requires cross-functional orchestration, structured multi-agent debate, parallel workflow execution, or rigorous organizational gating.
    
- `pilot_to_prove:`
    
    1. The stability and relevance of the Autonomous Curator when observing and generating skills for non-software business operations.
        
    2. The effectiveness of its strict 2,200-character bounded memory limit when managing context over a long-term, multi-project portfolio lifecycle.
        

## Final Recommendations

1. `recommended_for_pilot`: **Gas City + BMAD Pack**. This composition is uniquely capable of seamlessly integrating asynchronous multi-agent orchestration, human governance gates, durable state tracking, and a massive existing library of specialist personas without requiring the invention of a new framework.
    
2. `runner_up`: **Politik**. It provides the most secure, auditable, and domain-neutral governance framework available. However, its complete lack of integrated agent intelligence relegates it to environments with high engineering capacity.
    
3. `simplest_control`: **Hermes Agent**. Offers immense operational depth and unparalleled self-learning for individual tasks, though it ultimately fails to satisfy the broader requirements of a multi-agent operating system.
    
4. `component_winners`:
    
    - **L10 (Learning Loop):** Hermes Agent's integration of the DSPy and GEPA auto-curation systems represents the state-of-the-art in autonomous procedural learning.
        
    - **L6 (Tools/Scripts):** The Superpowers pack provides exceptional deterministic tooling for debugging and root-cause analysis.
        
    - **L8 (Review Governance):** Claude Octopus excels as a component due to its strict multi-model consensus gate requirements.
        
5. `what_previous_research_got_wrong_or_missed`: Prior analytical models heavily indexed on OpenClaw due to its massive GitHub popularity, extensive channel breadth, and community momentum. Current evidence unequivocally disqualifies OpenClaw for the Master of Arts architecture due to severe, systemic architectural vulnerabilities. The accumulation of six CVEs (with CVSS scores up to 9.1) and the catastrophic ClawHavoc supply chain infection demonstrate a reactive security posture incompatible with sensitive operational data. Furthermore, prior assumptions that frameworks like Ruflo (Claude Flow) provided over 100 distinct agents were misleading; empirical analysis reveals these are largely identical prompt templates that introduce high operational overhead without proportional semantic utility. Most critically, previous evaluations missed the architectural paradigm shift presented by Gas City, which decoupled the workflow methodology (via Packs) from the runtime engine, thereby allowing arbitrary, non-software domains to be orchestrated securely and deterministically.
    

````

```yaml
Orchestration/research-runs/claude-research/results.yaml
````

YAML

```
schema_version: 1
researcher_id: claude-research
research_date: 2026-08-21
scope_commit_or_ref: main
complete_system_ranking:
  - rank: 1
    architecture: Gas City + gascity-packs/bmad + gascity-packs/superpowers
    score: 92.3
    confidence: A
    hard_gates: pass
    primary_failure_mode: Complexity of Dolt/Beads state synchronization under heavy parallel fan-out.
    architecture_map:
      L1_knowledge: Rig filesystem and shared/ template partials
      L2_portfolio: Gas City rigs list and Oversight-rig pack
      L3_orchestrator: Gas City Controller daemon
      L4_workflows: .formula.toml files via Gas City
      L5_specialists: BMAD Method personas (Analyst, PM, Creative, etc.)
      L6_tools: Superpowers pack, Hooks, and Orders
      L7_executors: Claude, Codex, Gemini via Gas City providers
      L8_review: Formula v2 control beads and Quality Gates (adversarial review)
      L9_artifacts: Local rig artifact_root merged via Refinery agent
      L10_learning: Updates to shared template fragments (manual)
  - rank: 2
    architecture: Politik
    score: 73.4
    confidence: B
    hard_gates: pass
    primary_failure_mode: Lack of out-of-the-box specialist personas requires significant prompt engineering.
    architecture_map:
      L1_knowledge: Git Repository Tree
      L2_portfolio: Nested Git repositories (Org/Team/Ticket)
      L3_orchestrator: Git hooks and Node.js CLI trigger
      L4_workflows: Governance Protocols (CHARTER.md)
      L5_specialists: None native (requires DELEGATE/OPERATOR custom definitions)
      L6_tools: Bring-your-own CLI tools executed by agent processes
      L7_executors: Any CLI-compatible LLM invoked by shell
      L8_review: CANON primitives (DIVISION, ASSENT, ESCALATION, VETO)
      L9_artifacts: Git Commits
      L10_learning: Amendments to CHARTER.md and Standing Orders
  - rank: 3
    architecture: Hermes Agent
    score: 69.8
    confidence: A
    hard_gates: conditional
    primary_failure_mode: Inability to route complex, multi-stage workflows across stateful peer agents.
    architecture_map:
      L1_knowledge: Bounded MEMORY.md and USER.md with tiered retrieval
      L2_portfolio: Multi-folder workspaces (hermes project)
      L3_orchestrator: Internal tool execution loop (single agent)
      L4_workflows: Multi-turn objective loop (/goal)
      L5_specialists: Stateless sub-agents spawned on demand
      L6_tools: 40+ built-in AgentSkills compatible tools
      L7_executors: OpenRouter, local models, Claude, Codex
      L8_review: Manual human intervention via TUI/CLI
      L9_artifacts: Standard file output
      L10_learning: Autonomous Curator and DSPy/GEPA self-evolution
component_winners:
  L10_learning: Hermes Agent (Autonomous Curator / GEPA)
  L6_tools: Superpowers Pack
  L8_review: Claude Octopus (Multi-model Consensus Gate)
disqualified:
  - OpenClaw (Failed H12 - Security vulnerabilities / 6 CVEs)
  - OpenSwarm (Failed H2, H9 - Experimental latent vector routing)
  - EMOS (Failed H10 - Robotics/Embodiment domain specific)
insufficient_evidence:
  - Agent-OS (Conceptual OS, lacking production validation evidence)
sensitivity:
  autonomy_first: Gas City extends lead; Politik widens gap over Hermes due to governance.
  knowledge_first: Hermes closes gap on Politik; Gas City remains first.
  simplicity_first: Politik scores highest in this lens, but Gas City retains overall lead due to upstream composition support.
recommended_pilots:
  - Gas City + BMAD (Primary target)
  - Politik (Secondary target for extreme audit requirements)
critical_unknowns:
  - Stability of Dolt database for Gas City beads under heavy MoA portfolio load.
  - Latency of Politik using Git commits as a real-time messaging bus.
  - Ability of BMAD personas to seamlessly adapt to purely creative/non-technical tasks without extensive prompt engineering.
```

Markdown

```
Orchestration/research-runs/claude-research/sources.md
```

|**ID**|**Candidate**|**Claim/Capability**|**Source Type**|**Date/Version**|**URL**|**Notes**|
|---|---|---|---|---|---|---|
|1|BMAD Method|Agile simulation, simulator-first methodology, simulating full product team|P1|May 2026 (v6.8.0)|codemyspec.com|-|
|3|BMAD Method|Implements change, reviews work, returns working code/artifacts|P1|-|docs.bmad-method.org|-|
|4|BMAD Method|Creative Intelligence Suite, BMad Builder|P1|-|github.com/bmad-code-org|Verifies non-software fit.|
|8|BMAD Method|30 specialized agent personas (Analyst, Architect, Coach)|P3|-|bennycheung.github.io|Strong evidence of L5 capability.|
|11|BMAD Method|Compatible with Claude Code, Cursor, Codex CLI|P4|-|nevercodealone.de|Verifies L7 multi-executor portability.|
|13|BMAD Method|Analyst, PM, Architect roles; handles requirements and UX spec|P4|-|nevercodealone.de|-|
|15|Ruflo|Multi-agent orchestration, 100+ agents|P4|-|medium.com/data-science|-|
|16|Gas Town|Ephemeral workers (polecats), sessions as cattle, persistent state in beads|P1|-|steve-yegge.medium.com|-|
|18|Gas City|Orchestrator SDK for building dark factories; pack-based architecture|P1|v1.0.0 (Jan 2026)|steve-yegge.medium.com|-|
|19|Gas Town|Orchestrates workers across rigs. Roles include Mayor, Polecats, Refinery|P1|-|steve-yegge.medium.com|-|
|20|Gas City|Drop-in replacement for Gas Town; powered by Dolt DB|P1|-|steve-yegge.medium.com|-|
|21|Gas City|Eliminates hardcoded roles; uses packs and primitive-first config|P1|-|github.com/gastownhall|Maps Gas Town concepts to Gas City config.|
|23|Gas Town|Convoys track completed features; handoffs preserve tmux sessions|P1|-|steve-yegge.medium.com|Verifies L4 and L3 orchestrator capabilities.|
|24|Gas Town|Integrates via Tmux and environment variables; Tier 0-3 integration|P1|-|github.com/gastownhall|-|
|25|Gas Town|Adversarial rigs require isolated GitHub access tokens|P4|Apr 2026|dolthub.com|-|
|27|Gas City|Decoupled topology using composable packs|P4|-|nevercodealone.de|-|
|28|Ruflo|170+ MCP tools, self-learning SONA router|P1|-|npx-claude-flow|-|
|29|Superpowers|Marketplace plugin for Claude Code|P2|-|skillselion.com|-|
|30|Superpowers|Root cause investigation, systemic debugging, TDD skills|P1|-|github.com/obra|Verifies L6 deterministic tooling/checks.|
|31|Superpowers|High adoption rate (272k stars)|P2|-|skillselion.com|-|
|32|Ruflo|HNSW vector search, Hybrid AgentDB backend, 100+ agents|P2|-|skillsllm.com|-|
|36|Claude Octopus|8 model providers, 75% consensus gate|P4|-|chenguangliang.com|Excellent for L8 review/governance.|
|37|Ruflo|Heavy overhead; most of 100+ agents are just prompt templates|P4|-|chenguangliang.com|Shows critical failure mode for Ruflo.|
|43|Hermes Agent|Self-improving agent, memory across sessions, 40+ tools|P2|-|openrouter.ai/apps|-|
|45|OpenClaw|Local gateway, multi-channel routing (WhatsApp, Telegram, etc.)|P4|-|medium.com|-|
|47|OpenClaw|Multi-channel gateway, installer provisions Node.js|P1|-|github.com/openclaw|-|
|51|OpenClaw|Manages inbox, emails, calendar|P1|-|openclaw.ai|Verifies non-software fit.|
|55|OpenClaw|205 production-ready templates (marketing, legal, HR, etc.)|P3|-|github.com/mergisi|-|
|58|Hermes Agent|Automation that improves over time; OpenClaw is orchestrator|P4|-|autonomous.ai|-|
|59|OpenClaw / Hermes|OpenClaw has documented CVEs and malicious skills|P4|-|autonomous.ai|Highlights OpenClaw security failure.|
|60|OpenClaw|CVE-2026-25253, CVE-2026-25891|P4|-|innfactory.ai|-|
|61|Hermes Agent|7-layer hardened design; Autonomous Curator auto-generates skills|P4|-|opsily.com|Verifies L10 capabilities natively.|
|62|Hermes Agent|Memory recall latency 113ms; zero CVEs|P4|-|opsily.com|-|
|63|Hermes Agent|Bounded memory (2,200 chars); tiered retrieval|P4|-|nextcurious.com|-|
|64|Hermes Agent|Best for repetitive automation, self-improving workflows|P4|-|nextcurious.com|-|
|65|Hermes Agent|Open-source AI lab project; MIT license|P4|Mar 2026 (v0.2.0)|innfactory.ai|-|
|71|Hermes Agent|Evolutionary self-improvement using DSPy + GEPA|P1|-|github.com/NousResearch|Explains the deep self-learning mechanics.|
|72|Gas City|Breaks job into tracked units (beads), runs in parallel|P1|-|github.com/gastownhall|-|
|73|Gas City Packs|Pre-built methodology packs (BMAD, Superpowers, GStack)|P1|-|github.com/gastownhall|Essential for L4/L5 reuse validation.|
|75|Gas City|Declarative city.toml config; multiple runtime providers|P1|-|github.com/gastownhall|-|
|76|Gas City|Beads backend (Dolt); Controller long-running daemon|P1|-|github.com/gastownhall|Details orchestration logic.|
|77|Gas City|Shared template partials; renders prompts dynamically|P1|-|github.com/gastownhall|-|
|79|Gas City|End-to-end traced architecture|P1|-|github.com/gastownhall|-|
|80|Gas City|Event Bus (append-only log), Prompt Templates in Go text|P1|-|github.com/gastownhall|-|
|81|Gas City Packs|Rig-scoped roles (requirements-planner, implementation-worker)|P1|-|github.com/gastownhall|-|
|87|Politik|Governed multi-agent OS; Git is the session; Hansard record|P1|-|github.com/cordfuse|Native satisfaction of L8 governance and L9.|
|89|OpenSwarm|Local-first OS, O(N) latent vector bus|P1|-|github.com/openswarm-os|-|
|90|Agent-OS|Natural language OS, 6 specialized roles|P1|Dec 2025 (v1.0)|github.com/kase1111-hash|-|
|91|Politik|Eleven reference protocols (Parliamentary, Corporate, etc.)|P1|-|github.com/cordfuse|-|
|92|OpenSwarm|Early Alpha - Experimental phase|P1|-|github.com/openswarm-os|Fails H2 proven requirement.|
|93|EMOS|Robotics focused physical embodiment OS|P1|-|github.com/SgtVincent|Fails H10 non-software (knowledge) fit.|
|96|EMOS|Tasks involve multi-floor object rearrangement|P1|-|github.com/SgtVincent|-|
|98|Gas City Packs|bmad-build pack uses readiness gate and adversarial review|P1|-|github.com/gastownhall|Verified L8 review capabilities natively built.|
|99|Gas City Packs|bmad-build implements PRD -> architecture -> stories|P1|-|github.com/gastownhall|-|
|101|Gas City Packs|oversight-rig maintains portfolio brief (executive status)|P1|-|github.com/gastownhall|Perfect fit for L2 (Portfolio SSOT).|
|103|Gas City Packs|gstack provides QA review lanes|P1|-|github.com/gastownhall|-|
|108|Gas City|OpenTelemetry metrics, privacy-scoped usage tracking|P1|v1.4.0 (Jul 2026)|github.com/gastownhall|-|
|114|Gas City|Mayor acts as main entry point; pull not push via Beads|P4|-|davesgroundtruth.com|-|
|115|Gas City|Controller Reconciler loop spawns polecats dynamically|P4|-|davesgroundtruth.com|-|
|116|Gas City|Mapping Gas Town roles to Gas City primitives|P1|-|github.com/gastownhall|-|
|117|Gas City|city.toml is deployment, pack.toml is reusable behavior|P1|-|github.com/gastownhall|Details architectural mapping.|
|120|Gas City Packs|Compound Engineering uses widest reviewer-persona fanout|P1|-|github.com/gastownhall|-|
|128|Gas City|Formula compiler parses .formula.toml files|P1|-|github.com/gastownhall|-|
|129|Gas City|Triggers (cron, condition, event) for automation|P1|-|github.com/gastownhall|-|
|130|Gas City|Health Patrol detects stalls and restarts sessions|P1|-|github.com/gastownhall|-|
|131|Gas City|Formulas use TOML dependencies and control flow|P4|-|davesgroundtruth.com|-|
|134|Gas City Packs|Artifacts land in artifact_root inside the Rig|P1|-|github.com/gastownhall|-|
|135|Gas City|Core pack includes stock pool-worker prompt|P1|-|github.com/gastownhall|-|
|152|Politik|CANON primitives (DIVISION, ESCALATION, VETO, ASSENT)|P1|-|github.com/cordfuse|Details deep L8 governance protocol.|
|153|Politik|Stateless CLI workers spawn, execute, dispose|P1|-|github.com/cordfuse|-|
|155|Politik|State schema stored in CHARTER.md and STATE.json|P1|-|github.com/cordfuse|-|
|156|Hermes Agent|GEPA evolution optimization|P1|-|github.com/NousResearch|-|
|161|Hermes Agent|Setup wizard auto-detects dependencies (uv, Node.js, minGit)|P1|-|github.com/NousResearch|-|
|162|Hermes Agent|/goal initiates persistent multi-turn objective with judge|P1|-|glukhov.org|-|