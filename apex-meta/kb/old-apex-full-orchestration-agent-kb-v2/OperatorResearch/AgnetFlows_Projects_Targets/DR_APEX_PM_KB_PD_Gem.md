# APEX PM/KB/PD — Execution Options Research

## Phase 1: Foundational Source Repositories

The orchestration of autonomous AI agents within a static, local-file repository requires a fundamental split between deterministic state management and probabilistic reasoning. An analysis of fifteen leading implementations reveals distinct paradigms for handling Project Management (PM), Knowledge Base Management (KB), and Product Development (PD) processes natively within a repository structure. The primary constraint of the Apex orchestration system is its reliance on Claude Code operating within a local filesystem, devoid of external databases or Software-as-a-Service (SaaS) execution layers. This constraint necessitates a rigorous evaluation of when to leverage pure `SKILL.md` instruction files and when to introduce Python scripts for deterministic graph traversal or state aggregation.

### CCPM (Critical Chain Project Management)

The CCPM repository architecture aims to provide a structured planning and execution framework for AI agents, transforming ambiguous requirements into actionable development steps. To understand the internal mechanics, a search was executed targeting the primary execution files via the query `site:github.com/automazeio/ccpm SKILL.md OR references/structure.md OR references/track.md`. While the raw source code of the individual markdown references was not exposed in the dataset, the repository's structural documentation outlines the decomposition logic meticulously. The mechanism begins with a Product Requirements Document (PRD) which is subsequently parsed into a technical epic. This epic is intelligently batched into parallel execution tasks, capped strictly at ten tasks per epic to prevent context window saturation.   

The field schema extracted from the documentation reveals that tasks rely heavily on explicit metadata, including `depends_on`, `parallel`, `conflicts_with`, `effort estimate`, and `acceptance criteria`. The `track.md` component defines the operator-facing output format, utilizing deterministic bash scripts to scan the repository and return status enum values of "in progress," "next," and "blocked" instantly to the terminal. The primary tradeoff of CCPM is its profound operational coupling to GitHub Issues and git worktrees as the definitive source of truth. This coupling invalidates its execution runtime for a strictly local, solo-operator orchestration system, rendering its utility purely conceptual for hierarchy extraction rather than direct code implementation.   

### Backlog.md

Backlog.md represents a highly capable Markdown-native task grammar system designed to bridge human project management with AI agent execution. Searches were executed to locate task examples and schema definitions using the queries `site:github.com/MrLesk/Backlog.md schema task.md`, `task file example`, and `backlog.config.yml`. Although the exact YAML frontmatter file templates were not retrieved in the provided dataset, the repository documentation and configuration artifacts such as `AGENTS.md` and `bunfig.toml` reveal the structural philosophy. Backlog.md utilizes a split architecture of YAML frontmatter to track required state variables, alongside structured Markdown body sections to hold unstructured task descriptions.   

The documentation indicates that the Markdown body section names frequently encompass areas such as Description, Plan, Notes, and Final Summary. The status enum values are flexible but fundamentally rely on states such as "To Do" or "in progress". The overarching tradeoff here lies in Backlog.md's dependency on a TypeScript CLI application for board rendering, file manipulation, and project initialization. Because the system relies on a compiled binary or Node.js runtime to orchestrate the Markdown files, it introduces unacceptable friction for a Python-based or pure-prompt orchestration system. Consequently, only the theoretical file schema—specifically the combination of YAML frontmatter for machine parsing and Markdown bodies for LLM reasoning—can be effectively extracted for the Apex architecture.   

### Task Master AI

Task Master AI provides a rigorous JSON-based dependency tracking architecture aimed at resolving context degradation during software delivery. The search query `task-master-ai claude github` or `github.com/eyalzh/task-master` was utilized to locate the underlying scoring mechanics. The implementation documentation (`docs/task-structure.md`) reveals a highly structured dependency field schema embedded within a `tasks.json` manifest. The complete field list consists of an `id`, a descriptive `title`, a `description`, a `status` utilizing enums such as "pending," "done," and "deferred," an array of integer `dependencies` representing blocking task IDs, a `priority` field utilizing enums of "high," "medium," and "low," detailed implementation `details`, a `testStrategy`, and an array of `subtasks`.   

The algorithmic scoring formula explicitly calculates the next available task by first evaluating tasks that are either pending or in-progress, checking that all prerequisite dependency IDs are fully satisfied, and subsequently computing a priority score derived from the priority level, the total dependency count, and the chronological task ID. The next-task computation logic outputs a comprehensive JSON block featuring the suggested action, contextual implementation details, and immediate subtask visibility. While the deterministic logic is architecturally robust, its reliance on a Node.js ecosystem and opaque JSON storage rather than human-readable Markdown creates an anti-pattern for local-file orchestration. Implementing this logic requires porting the theoretical dependency scoring algorithm into a native Python script to ensure compatibility with Apex.   

### GSD Core

GSD Core operates as an advanced session continuity and context management framework explicitly designed to solve "context rot" in long-running AI sessions. Searches were executed for the core templates using the query `GSD Core Claude agent STATE.md CONTEXT.md github`. While the literal raw template files for `STATE.md` and `CONTEXT.md` were not exposed, the system's operational documentation thoroughly details the session capture mechanism. The mechanism relies on forcing the agent to execute a constrained phase loop (Discuss, Plan, Execute). At the conclusion of a work session, the agent extracts phase-specific decisions and rationale into `CONTEXT.md`, acting as a permanent "decisions room," while the current milestone positions and structural anomalies are serialized into `STATE.md`.   

These files are formatted strictly as plain Markdown, devoid of complex schema enforcement. Upon the initialization of a subsequent session, these specific files are injected into the prompt of a fresh subagent, completely bypassing the accumulation of useless conversational bloat from previous interactions. The primary tradeoff is that GSD Core functions exclusively as a session-level continuity tool, lacking the durable task-graph tracking features or dependency validation necessary for multi-layered project management. Therefore, its application in Apex is limited to the handoff and session initialization protocols.   

### planning-with-files

The `planning-with-files` repository provides a highly resilient, file-based scratchpad optimized for long-running agentic research and coding tasks. The search query `planning-with-files Claude 2-action write rule github` successfully isolated the primary `SKILL.md` and `docs/quickstart.md` files which define the operational rules and the expected progress log format. The system utilizes a strict operational constraint known as the "2-action write rule" which explicitly mandates: "After every 2 view/browser/search operations, IMMEDIATELY save key findings to text files". This acts as a forced rate-limiter, preventing the LLM from overflowing its context window with retrieved data before persisting the state to the filesystem.   

Furthermore, the error persistence mechanism strictly prohibits the agent from hiding errors and retrying operations silently in the console; instead, it forces the agent to document all execution failures, actions taken, and files modified directly into a `progress.md` file. The file format relies on pure Markdown separated into a trinity of files: `task_plan.md` for phase tracking, `findings.md` for discoveries, and `progress.md` for the append-only session log. The implementation confirms that maintaining state through frequent, small file writes significantly improves agent reliability, a pattern critical for maintaining the Apex knowledge base.   

### OpenClaw TaskFlow

OpenClaw provides an advanced detached execution runtime that separates the business logic of AI classification from the deterministic routing of state transitions. The search queried `skills/taskflow/SKILL.md`, `skills/model-usage/scripts/model_usage.py`, and `skills/taskflow/examples/inbox-triage.lobster`. The `model_usage.py` script serves as a structural blueprint for deterministic operations, demonstrating exactly how a pure Python script can parse command-line arguments, read structured JSON inputs, filter records logically by date, compute deterministic aggregates, and return structured text or JSON to the LLM without wasting expensive inference tokens on arithmetic.   

The lifecycle states of the overarching TaskFlow architecture include: Create flow, Run detached classification, Persist state, Wait, Resume, and Finish. The `stateJson` structure is designed to capture complete execution context, containing explicit fields for `flowId`, `owner`, `currentStep`, an arbitrary `stateJson` payload, a `waitJson` flag for blocking conditions, `linked children` for subtask routing, `lifecycle` tracking, and `revision tracking` to detect stale data. The critical architectural boundary established by the `.lobster` examples is that the deterministic Python runtime strictly owns state persistence and edge routing, while the LLM purely owns the unstructured reasoning and classification layer, outputting constrained JSON that the runtime then executes.   

### CrewAI design-task

CrewAI's task design principles offer a comprehensive schema for bounding LLM hallucinations during execution. The implementation files were analyzed via the query `skills/design-task/SKILL.md` and `skills/getting-started/SKILL.md`. The complete task contract field list extracted from the documentation includes: `description`, `expected_output` (or `expected_output_model`), `context` (which maps task dependencies), `guardrail`, `human_review`, `async execution`, and `output_file`.   

Within this contract, the `description` and `expected_output` are treated as required reasoning constraints, forcing the agent to articulate exactly what successful completion looks like before beginning. The guardrail definitions act as programmatic checks enforcing boundary constraints, while the human review gate is defined as an optional configuration flag that pauses runtime execution to solicit standard console input from the operator before allowing state mutation. The decision rules for abstraction dictate that pure LLM calls should handle unstructured text reasoning exclusively, whereas CrewAI `Flows` are mandated whenever deterministic sequential steps or conditional state transitions are required.   

### llm-wiki

The `llm-wiki-plugin` provides an autonomous, self-maintaining markdown knowledge base architecture. A search targeting `llm-wiki claude skill github` identified the Python index-build script `wiki_search.py`, which performs the primary indexing and querying operations utilizing a BM25 fuzzy search mechanism to scan local files. The file scanning logic incorporates an automatic sharding mechanism: when the primary `wiki/index.md` catalog exceeds 300 lines, the Python layer dynamically shards the index into granular, per-type files under a `wiki/indexes/` directory, ensuring the top-level index remains a highly compressed catalog suitable for LLM context windows.   

The system produces structured summaries by generating distinct entity and concept pages adorned with frontmatter filters, links, and operational metadata. The handoff format from Python to Claude is remarkably efficient; Python outputs the relevant text shards to standard output, prompting Claude to utilize surgical string replacement semantics (`/wiki:ingest`) to update the existing knowledge base pages directly on the filesystem. This architecture proves that Python indexers paired with LLM synthesis provide the highest architectural fit for knowledge base management.   

### kanban-skill

The `kanban-skill` provides a lightweight, serverless task board architecture specifically optimized for AI agents. The repository was analyzed via the search `site:github.com/mattjoyce/kanban-skill SKILL.md OR card`. While raw markdown card examples were not explicitly exposed in the dataset, the underlying mechanism is clearly and definitively defined: task cards exist purely as flat `.md` files residing in a dedicated `kanban/` directory.   

The critical fields governing the board logic, specifically status and priority, are tracked entirely within the YAML frontmatter of each file. Dependencies are not actively computed via a sophisticated graph engine but are managed through standard markdown text references. The tradeoff of this approach is its extreme simplicity; while it guarantees flawless portability across any AI assistant capable of reading files, it lacks the deterministic dependency validation required to compute complex next-action workflows automatically.   

### pm-skills

The `pm-skills` repository functions as a massive, open-source library containing 66 distinct project management skills designed for AI agents. The search query `pm-skills claude awesomeclaude.ai github` facilitated the extraction of its operational lifecycle. The repository covers the entire Triple Diamond product lifecycle, including discovery, definition, development, delivery, measurement, and iteration phases.   

Skills are triggered either via explicit Claude Code slash commands (e.g., `/market-sizing`, `/journey-map`) or through automatic workspace scanning driven by an `AGENTS.md` file configuration. The output produced by each skill is a highly standardized Markdown artifact strictly governed by a `references/TEMPLATE.md` definition file, ensuring that the AI agent produces consistent, predictable documentation regardless of the underlying LLM utilized. The reliance on pure prompt skills without a deterministic Python orchestration layer makes this repository an excellent source for prompt engineering but unviable for complex state reconciliation.   

### swarmvault

The `swarmvault` system compiles raw markdown into a sophisticated local knowledge graph, operating as an entirely local-first Retrieval-Augmented Generation (RAG) knowledge base. The search targeted `swarmvault claude skill github` and analyzed the `templates/llm-wiki-schema.md` template. The architecture defines a strict three-layer schema: raw immutable source documents (`raw/`), LLM-generated and human-authored wiki pages (`wiki/`), and the defining structural conventions.   

The Python script compilation process reads the raw markdown and processes it into a local SQLite Full-Text Search (FTS) index utilizing vector embeddings (`state/retrieval/`), alongside a machine-readable typed JSON knowledge graph (`state/graph.json`). The operational split between Python and Claude is absolute: the Python backend handles all parsing, contradiction detection, and index generation deterministically, while Claude interacts with the graph purely through a bundled MCP server to synthesize answers. While incredibly powerful, the reliance on SQLite and embedding models violates the "no external database" constraint of the Apex orchestration system.   

### Imprint

Imprint operates as an innovative session continuity skill utilizing a highly portable profile architecture. A search for `Imprint claude skill profile github` extracted the operational mechanics of the `.dna.md` profile template. The profile acts as the continuity mechanism by storing the operator's distinct behavioral patterns, maintaining a footprint strictly under 500 tokens.   

The explicit fields captured within this memory profile encompass code review standards, debugging habits, planning rhythms, testing preferences, and git workflows. The profile persists across sessions by remaining a static, version-controlled Markdown file alongside the codebase. Upon the initialization of any new session across 19+ compatible agents, the skill automatically injects this profile into the context window, guaranteeing that the standard operating procedures of the human operator are carried forward seamlessly without repetitive prompting.   

### Hermes-agent

The `tools/skills_hub.py` module within the Hermes agent establishes robust skill provenance and security gating. The required `SKILL.md` format definition mandates strict metadata fields to ensure parseability, specifically requiring `name`, `description`, `version`, `author`, and a `metadata` block containing operational tags. The trust level system differentiates between dangerous community skills and verified official skills by utilizing a hardcoded `TRUSTED_REPOS` dictionary, matching exact repository owners (e.g., `openai/skills`, `anthropics/skills`) to prevent supply-chain attacks.   

The source adapter structure handles multiple ingestion paths, supporting GitHub taps, direct URLs, and well-known skill registries via a `create_source_router` implementation. Crucially, the `HubLockFile` mechanism provides strict provenance tracking by capturing the cryptographic `content_hash` of all installed skill bundles within a local `.hub/lock.json` file. If the fetched remote hash fails to match the local lockfile, the update process is blocked, ensuring that the execution environment remains immune to silent upstream modifications.   

### LangGraph

LangGraph serves as the definitive escalation reference for stateful, multi-actor workflows where simple procedural scripts fail. Analyzed via searches for minimal stateful workflow examples, the library demands a rigorous architectural setup. The minimum code required for a durable stateful workflow involves defining a rigid `StateGraph` object, attaching pure Python functions to representing execution nodes, explicitly defining conditional edge functions for logic routing, and compiling the entire graph with a persistent memory checkpointer such as `SqliteSaver`.   

While it provides unparalleled execution durability and seamless human-in-the-loop interruption capabilities, the complexity cost relative to simple procedural Python scripts is immense. Implementing LangGraph requires migrating all execution logic into a strict graph topology, managing custom type serialization errors, and handling infinite loop mitigation. Consequently, it is classified strictly as an escalation path for multi-team scale rather than a baseline integration for a v1 orchestration system.   

### Process Framework Patterns

The integration analysis uncovered several universal process frameworks from the `ProcessRanking` index that dictate the methodology of the execution loops. The **PRC-CORE-001 (Goal-to-Artifact loop)** functions as the core creation engine, governing the sequence from project intake to structural decomposition, artifact writing, and final verification. The **TEMPLATE-KANBAN-001 (Durable task graph)** provides the abstract dependency and status graph model, mapping the transition stages from lane extraction to verification gating.   

The **PRC-HANDOFF-001 (Handoff packet)** engineers a self-contained state-transfer packet, complete with behavioral guardrails, generated at the end of a session to initialize the subsequent planning layer reliably. The **PRC-DATA-001 (CRISP-DM evidence flow)** dictates the evidence-based protocol for session writing, structured delta extraction, and index rebuilding. The **PRC-VERIFY-001 (Chain-of-verification gate)** implements a mandatory operator validation checkpoint to prevent silent database or file state drift. The **PRC-SCRUM-001 (Sprint artifact loop)** manages batch status updates and stall detection over multiple sessions. Finally, the **PRC-RISK-001 (Govern-map-measure-manage)** surfaces implicit blockers as flagged textual proposals requiring human operator approval before execution.   

## Phase 2: Process Options and Evaluation

The subsequent analysis evaluates the twenty required processes, mapping implementation options against token costs, maintenance burdens, and overall portability. The objective is to identify the optimal configuration for a solo operator functioning exclusively within local files via Claude Code, without external SaaS dependencies or complex graph orchestrations.

### Project Management (PM)

**PM1: Capture project**

What this process does: Captures the foundational state, scope, domain, and objectives of the project into a persistent file format.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Markdown Template||Claude reads a PRD template and generates a structured epic markdown file.|Medium|Low|Low|No|Yes|
|YAML Frontmatter||Claude creates a markdown file populated with YAML metadata at the top.|Low|Low|Low|No|Yes|
|Goal-to-Artifact||Claude executes a strict multi-step reasoning prompt to generate a verified contract.|High|Low|Medium|No|Yes|

  

_Best option for a solo operator:_ YAML Frontmatter (Backlog.md) ensures metadata is strictly machine-parseable while the body remains unstructured for human and Claude reading, avoiding complex intake flows. (Evidence: ).   

The decision to utilize YAML frontmatter combined with unstructured Markdown bodies allows the system to remain inherently portable. The operator avoids the overhead of managing a rigid database while simultaneously ensuring that Python scripts can parse core metadata deterministically.

**PM2: Decompose project**

What this process does: Breaks down the high-level project into actionable epics, chunks, and tasks following hierarchical splitting rules.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Batched File Generation||Claude logically splits work and creates up to 10 distinct task files per epic.|High|Low|Medium|No|Yes|
|Inline Markdown List||Claude generates nested bullet points within a single project markdown file.|Low|Low|Low|No|Yes|
|Task Contract||Claude generates structured YAML tasks featuring description, expected output, and context.|Medium|Low|Medium|No|Yes|

  

_Best option for a solo operator:_ Inline Markdown List utilizing CrewAI's task contract schema keeps all decomposition inside a single file until density necessitates a split, preventing premature filesystem overhead. (Evidence: ).   

Generating dozens of individual files for every micro-task immediately creates excessive filesystem clutter, which degrades the context window efficiency of the LLM. Retaining the tasks as an inline list until the complexity forces a split represents the safest approach for local execution.

**PM3: Assign dependencies**

What this process does: Maps the complex relationships between tasks using a "depends-on" and "unlocks" directed graph architecture.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|JSON Array Schema||Dependencies are written as arrays of blocking task IDs in a JSON file.|Low|Low|Low|No|Yes|
|Frontmatter Array||Task dependencies are written into the YAML frontmatter of the markdown file.|Low|Low|Low|No|Yes|

  

_Best option for a solo operator:_ Frontmatter Array allows Claude to map relationships purely in text via `depends_on` string IDs, eliminating the need for opaque JSON databases. (Evidence: ).   

The extraction of the dependency model from Task Master AI directly into the YAML frontmatter ensures that the dependency graph remains visible to the operator in standard text editors, facilitating manual intervention if the automated orchestrator encounters a parsing failure.

**PM4: Compute next action**

What this process does: Determines the immediately actionable task by evaluating the current completion state against the dependency graph.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Pure Prompt Reasoning|Base|Claude reads the markdown, visualizes the dependency tree, and guesses the next step.|High|Low|Low|No|Yes|
|Deterministic Traversal||A script evaluates all tasks, filters out blocked items, and computes the available next task.|Low|Medium|Medium|Yes|Yes|
|Stateful Graph||A dedicated checkpointer and graph engine tracks task node states and dynamically routes execution.|Low|High|High|Yes|Yes|

  

_Best option for a solo operator:_ Deterministic Traversal guarantees mathematical accuracy and saves massive token reasoning costs by ensuring an LLM does not hallucinate graph logic. (Evidence: ).   

LLMs are notoriously unreliable when attempting to traverse deep, cyclical, or branching graphs conceptually within a prompt. By extracting the exact Task Master AI dependency logic into a Python scanner script, the system achieves perfect accuracy while preserving the context window for actual task execution.

**PM5: Detect blockers**

What this process does: Identifies specific tasks that cannot proceed due to unsatisfied prerequisites or external environmental constraints.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Scripted Status Check||A Python script scans frontmatter arrays to report items waiting on incomplete prerequisites.|Low|Medium|Low|Yes|Yes|
|Wait State Flag||The lifecycle runtime sets a specific `waitJson` flag, suspending the task until conditions match.|Medium|High|High|Yes|Yes|
|Operator Validation||Claude reasons about implicit blockers and proposes a blocker flag for operator approval.|Medium|Low|Low|No|Yes|

  

_Best option for a solo operator:_ Scripted Status Check perfectly calculates explicit dependency blocks via Python, while Claude can simultaneously flag implicit environmental blocks for manual review. (Evidence: ).   

This hybrid approach acknowledges that blockers exist in two distinct paradigms: explicit structural blockers (Task B cannot start until Task A finishes) which are handled deterministically, and implicit contextual blockers (the API key is invalid) which require probabilistic reasoning and operator intervention to resolve.

**PM6: Update status**

What this process does: Modifies a task's status marker to reflect its current state after work operations are executed or completed.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|File Rewrite||Claude rewrites the entire task file or block, updating the string from 'pending' to 'done'.|Medium|Low|Low|No|Yes|
|Surgical Frontmatter||A script parses the file, updates only the `status` YAML key, and saves.|Low|Medium|Low|Yes|Yes|
|Sprint Update Loop||Batch update mechanism performed by Claude at the end of a sprint session.|High|Low|Medium|No|Yes|

  

_Best option for a solo operator:_ Surgical Frontmatter prevents Claude from accidentally hallucinating or deleting file body content during a simple status toggle. (Evidence: ).   

Allowing the LLM to rewrite entire files merely to update a boolean or enum string introduces severe risk of data loss or formatting corruption. Utilizing a Python script that explicitly targets the YAML key preserves the structural integrity of the human-authored markdown body.

**PM7: Detect stall**

What this process does: Flags items that have occupied the exact same active state across multiple sequential sessions without progressing.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Lifecycle Tracking||The `currentStep` and revision trackers mathematically compare state freshness against time.|Low|Medium|Medium|Yes|Yes|
|Session Counter Diff||A script increments a counter if the `next_action` string matches the previous session exactly.|Low|Medium|Low|Yes|Yes|

  

_Best option for a solo operator:_ Session Counter Diff rebuilding OpenClaw's stall detection as a simple Python string-comparison across three sessions requires zero LLM reasoning. (Evidence: ).   

This mechanism serves as a critical safety net against infinite loops or hidden deadlocks. If the LLM repeatedly outputs the identical next action without resolving it, the deterministic script immediately halts the cycle and alerts the operator, preserving compute resources and API budgets.

**PM8: Generate work registry**

What this process does: Compiles all distributed project state files into a single, compact, machine-readable index of project health.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Python BM25 Index||A script parses all markdown files and creates a fuzzy-searchable top-level index.|Low|Medium|High|Yes|Yes|
|Deterministic Aggregation||Python iterates through known project files, extracting frontmatter, and writing a flat `registry.md`.|Low|Medium|Low|Yes|Yes|

  

_Best option for a solo operator:_ Deterministic Aggregation ensures Claude does not waste tokens aggregating files; a Python script compiling a unified `registry.md` is efficient, fast, and entirely deterministic. (Evidence: ).   

The generated registry acts as the primary sensory input for the LLM during the planning phase. By offloading the aggregation of scattered frontmatter files to a fast Python scanner, the context window is populated exclusively with the high-density metadata required for decision-making.

### Knowledge Base Management (KB)

**KB1: Write session progress**

What this process does: Authors an unstructured narrative summary of operations, findings, and insights at the conclusion of a work session.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Markdown State Log||Claude drafts an unstructured summary into `STATE.md` capturing the narrative trajectory.|Medium|Low|Low|No|Yes|
|Append-only Log||Claude appends session actions, modifications, and test errors to `progress.md`.|Medium|Low|Low|No|Yes|
|Evidence Flow||Structured data logging strictly aligning with session data extraction logic.|High|Low|Medium|No|Yes|

  

_Best option for a solo operator:_ Append-only Log natively maintains historical context and avoids file corruption without requiring any scripting overhead. (Evidence: ).   

The append-only architecture ensures that no previous operational insights are accidentally overwritten during a session dump. It acts as an immutable ledger of agent actions, which is invaluable when debugging hallucinatory tangents or analyzing the trajectory of a complex research task.

**KB2: Extract state deltas**

What this process does: Translates the unstructured session narrative into precise, structured field updates such as status changes or new dependencies.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|JSON Proposal||Claude reasons over the narrative, outputting a strict JSON block of requested delta changes.|High|Low|Medium|No|Yes|
|Evidence Synthesis||Claude attempts to update files natively via prompt reasoning directly.|High|Low|High|No|Yes|

  

_Best option for a solo operator:_ JSON Proposal forces Claude to output a constrained schema that a Python script later executes, isolating reasoning from dangerous file I/O operations. (Evidence: ).   

This separation of concerns is the cornerstone of the OpenClaw TaskFlow architecture. By demanding that the LLM output its intended state mutations in a verifiable JSON array, the system ensures that corrupt edits or hallucinated file paths are caught by the Python validation layer before corrupting the knowledge base.

**KB3: Maintain entity files**

What this process does: Safely and securely applies the extracted structured deltas to the persistent Markdown knowledge base files.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Direct AI Write|Base|The LLM overwrites file contents dynamically using native filesystem tool calls.|Medium|Low|Medium|No|Yes|
|2-Action Rule||Hard constraint limiting write operations to prevent massive cascade overwrites.|Low|Low|Low|No|Yes|
|Verification Gate||A Python script applies the JSON delta payloads to the files deterministically.|Low|Medium|Medium|Yes|Yes|

  

_Best option for a solo operator:_ Verification Gate merged with the 2-Action Rule dictates that Python must own the deterministic file I/O to apply deltas safely without LLM formatting errors. (Evidence: ).   

Providing an LLM with unbounded write access to a repository introduces extreme systemic risk. The Python script acting as a strict write-gate ensures that only valid, pre-approved structural mutations touch the disk, while the 2-action rule prevents the LLM from attempting to execute massive, multi-file refactors in a single pass.

**KB4: Rebuild index**

What this process does: Regenerates the comprehensive search or reference index following any state mutations in the entity files.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Python Sharding||Python reconstructs `wiki/index.md` from all sub-files, sharding if over 300 lines.|Low|Medium|Medium|Yes|Yes|
|Graph Compilation||Python compiles a complex SQLite FTS / vector index and typed JSON graph.|Low|High|High|Yes|Yes|

  

_Best option for a solo operator:_ Python Sharding is virtually free on tokens and easily portable, avoiding the complex database requirements of embedding vectors. (Evidence: ).   

While vector embeddings offer superior semantic retrieval, the installation and management of SQLite and embedding models contradict the core principle of a flat-file, Git-native orchestration system. Sharding a Markdown index using procedural Python ensures immediate readability and perfect synchronization with version control.

**KB5: Detect drift**

What this process does: Identifies discrepancies between the actively tracked project state and the previous session's registered state snapshot.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|AI Narrative Diff||Claude reads `STATE.md` and attempts to guess if reality matches the documentation.|High|Low|Low|No|Yes|
|Scripted Registry Diff||Python performs a literal `diff` between the current `registry.md` and the last session's snapshot.|Low|Medium|Low|Yes|Yes|

  

_Best option for a solo operator:_ Scripted Registry Diff circumvents the fact that LLMs are poor at exact string matching across massive contexts, providing a token-free deterministic alert. (Evidence: ).   

State drift is the silent killer of autonomous agent architectures. Relying on an LLM to notice that a variable was subtly altered three sessions prior is mathematically unviable. A simple script calculating a file hash or text diff immediately surfaces inconsistencies before they compound into systemic failure.

**KB6: Produce next-session context**

What this process does: Packages the current state, progress, and goals into a self-contained handoff file designed to instantly orient the next Claude session.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Context Injection||Claude drafts a `CONTEXT.md` file summarizing technical and contextual state.|Medium|Low|Low|No|Yes|
|Guardrail Packet||Claude generates a highly structured packet containing goals, blockers, and next actions.|Medium|Low|Low|No|Yes|

  

_Best option for a solo operator:_ Guardrail Packet formatted as `next-precap-context.md` ensures the handoff is self-contained, portable, and seamlessly ingested upon the initialization of the next session. (Evidence: ).   

This handoff packet acts as the connective tissue across execution bounds. By rigidly structuring the packet to include explicitly identified goals and explicit operational guardrails, the orchestrator guarantees that the subsequent agent inherits exactly the constraints required to resume work flawlessly.

### Product Management (PD)

**PD1: Score priority**

What this process does: Evaluates and ranks the baseline architectural importance of tasks based on overarching goals and structural dependencies.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Heuristic Guessing||Claude estimates priority via natural language prompt guidelines.|High|Low|Low|No|Yes|
|Numeric Formula||A script computes priority strictly via baseline inputs (e.g., base priority + dependency weight).|Low|Medium|Low|Yes|Yes|

  

_Best option for a solo operator:_ Numeric Formula extracted from Task Master avoids expensive LLM context-window sorting failures by reducing priority ranking to a solvable mathematical equation. (Evidence: ).   

LLMs frequently struggle with stable sorting algorithms across large datasets due to attention mechanism limitations. Offloading the priority calculation to a deterministic Python integer calculation guarantees that critical path items will continuously bubble to the top of the queue without hallucinated deviations.

**PD2: Score urgency**

What this process does: Evaluates the time-sensitivity and external scheduling constraints of tasks independently from their baseline architectural priority.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Semantic Evaluation||Claude assesses urgency based on sprint context, blockers, and external factors.|Medium|Low|Low|No|Yes|
|Formulaic Decay||A script modifies urgency scores dynamically based on time elapsed since task creation.|Low|Medium|Medium|Yes|Yes|

  

_Best option for a solo operator:_ Semantic Evaluation acknowledges that urgency often requires qualitative business context, empowering Claude to parse the environment to flag time-sensitive goals. (Evidence: ).   

Unlike dependency mathematics, urgency is frequently derived from unstructured external factors such as client demands, upcoming milestone deadlines, or sudden API deprecations. The LLM excels at processing these qualitative semantics and appropriately flagging tasks for immediate intervention.

**PD3: Compute unlock depth**

What this process does: Calculates exactly how many subsequent, downstream tasks are unblocked by the successful completion of a specific parent task.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|AI Traversal|Base|Claude reads dependency strings and attempts to count recursive unlocks.|High|Low|High|No|Yes|
|Graph Script||A recursive Python function traverses the `unlocks` array graph to sum total downstream nodes.|Low|Medium|Medium|Yes|Yes|

  

_Best option for a solo operator:_ Graph Script guarantees mathematical precision for recursive counting tasks where probabilistic LLMs predictably fail. (Evidence: ).   

Computing unlock depth requires a strict traversal of a directed acyclic graph (DAG). Attempting to prompt an LLM to navigate a multi-layered DAG and return an accurate sum inevitably leads to off-by-one errors or total hallucination. A simple fifteen-line Python script executed prior to the planning phase solves this flawlessly.

**PD4: Synthesize focus recommendation**

What this process does: Integrates priority metrics, urgency indicators, state variables, and context into a final ranked list of actionable tasks featuring explicit reasoning.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Expected Output Contract||Claude generates a structured text reasoning block defending a specific focus rank.|High|Low|Medium|No|Yes|
|Constrained JSON||Claude outputs the focus recommendation into strict JSON for downstream routing.|Medium|Low|Medium|No|Yes|

  

_Best option for a solo operator:_ Expected Output Contract ensures the human operator can read and audit the reasoning Claude used to synthesize the recommendation. (Evidence: ).   

While JSON is highly efficient for machine routing, the final focus recommendation is fundamentally a communication artifact bridging the autonomous orchestrator and the human operator. Presenting this synthesis in structured narrative Markdown fosters trust and enables rapid human auditing of the AI's strategic alignment.

**PD5: Validate with operator**

What this process does: Enforces a strict human-in-the-loop review gate before allowing AI-proposed state mutations to be permanently written to the repository.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|Configured Pause||The workflow halts, requesting console input from the user before continuing execution.|Low|Low|Low|No|Yes|
|Validation Gate||Claude outputs "proposed flags" into the terminal, requiring the operator to manually trigger the write script.|Low|Low|Low|No|Yes|

  

_Best option for a solo operator:_ Validation Gate prevents dangerous silent state mutations by forcing the operator to issue the explicit update command after reviewing the text proposals. (Evidence: ).   

The primary failure mode of highly autonomous systems is runaway execution leading to destructive overwrites. By implementing a hard validation gate where the LLM can only _propose_ changes textually, the human operator retains absolute sovereignty over the definitive state of the knowledge base.

**PD6: Feed planning layer**

What this process does: Bridges the finalized session output into the initialization sequence for the subsequent daily planning phase, closing the execution loop.

|Option|Source|Mechanism in plain language|Token cost per run|Maintenance cost|Complexity|Requires a script?|Portable without SaaS?|
|---|---|---|---|---|---|---|---|
|File Read||The next session subagent natively loads `CONTEXT.md` into its context window upon startup.|Low|Low|Low|No|Yes|
|Handoff Packet||A predefined chunk of YAML/Markdown is passed directly to the orchestrator layer.|Low|Low|Low|No|Yes|

  

_Best option for a solo operator:_ Handoff Packet utilizing the generated `next-precap-context.md` file ensures the transfer is self-contained and seamlessly ingested upon initialization. (Evidence: ).   

This structural continuity guarantees that the agent awakens with immediate awareness of what was just accomplished, what obstacles remain, and what its immediate focus should be, drastically reducing the token expenditure required to re-orient the model from scratch.

## Phase 3: Sub-Skill Grouping Analysis

The architectural mapping of the twenty operational processes reveals that they do not function in isolation; they exhibit significant structural clustering based on shared triggers, overlapping file I/O operations, and identical execution contexts.

### First: Natural Groupings

Three highly cohesive natural groupings emerge from the analysis:

1. **The Planning Engine (PM1, PM2, PM3, PD1, PD2, PD3, PD4):** This cluster shares the execution context of intake, structural decomposition, and analytical synthesis. The engine reads the raw project markdown files, parses dependencies and YAML frontmatter, calculates priorities alongside unlock depth, and generates the final focus recommendation. The overarching trigger for this entire grouping is an orchestration request from the operator (e.g., "What should I work on next?").
    
2. **The State Synchronizer (PM4, PM5, PM7, PM8, KB4, KB5):** This cluster shares the execution context of deterministic state reconciliation. It strictly handles reading active project files against previous state snapshots to compute mathematically sound next actions, identify stall conditions, detect state drift, and compile the overarching machine-readable `registry.md`. The trigger for this grouping is any state update or sync request across the repository.
    
3. **The Session Executor & Handoff (PM6, KB1, KB2, KB3, KB6, PD5, PD6):** This cluster revolves entirely around the conclusion and transition of a work session. It manages the extraction of deltas from narrative logs, applies surgical updates to YAML frontmatter, validates changes with the operator, appends artifacts to the progress log, and generates the `next-precap-context.md` handoff file. The trigger is the explicit termination of an active work session.
    

### Second: Implementation Architecture per Grouping

The implementation requirements vary drastically between these groupings, heavily dictating where Python scripts must be introduced versus where pure `SKILL.md` prompt reasoning is sufficient.

- **The Planning Engine:** This cluster represents a hybrid implementation. The initial project capture, heuristic urgency scoring, and focus synthesis can be implemented via pure `SKILL.md` instruction files utilizing the Claude Code reasoning engine directly. However, the priority scoring and dependency mapping _require_ a Python script to ensure deterministic logic and prevent LLM hallucination during graph operations. The open-source `skills/design-task/SKILL.md` from CrewAI serves as the optimal base for the task design constraints. It must be adapted by stripping its multi-agent configuration details and focusing strictly on the expected-output reasoning constraints to suit a solo operator model.   
    
- **The State Synchronizer:** This grouping heavily necessitates Python scripting. Deterministic operations like recursive graph traversal, file metadata aggregation, and string-matching diffs (for stall detection) are fundamentally unsuited for probabilistic LLMs. The open-source baseline here is the OpenClaw `model_usage.py` script logic. To integrate it, the script must be fundamentally rewritten: instead of parsing cost logs, the adapted script will parse the local markdown frontmatter, compute the next-action arrays, and output the compiled `registry.md`. To manage maintenance overhead, all read/compute operations for this cluster must be consolidated into a single master `kb_scan.py` script.   
    
- **The Session Executor & Handoff:** This cluster is also a hybrid. The unstructured narrative summary and the handoff generation can be implemented purely in `SKILL.md`. Conversely, extracting deltas and safely maintaining entity files require a Python script to apply surgical updates to the YAML frontmatter, strictly honoring the "2-action write rule". The baseline for the prompt logic is the `planning-with-files` error persistence rules , which must be modified to output constrained JSON proposals that a secondary `kb_write.py` script executes deterministically.   
    

### Third: Unviable Patterns and Scratch Builds

An exhaustive review reveals that there are specific processes for which none of the fifteen source repositories provide a directly portable implementation pattern.

The most glaring architectural gap is **PD3: Compute unlock depth**. While Task Master AI relies heavily on this dependency scoring concept, its actual algorithmic implementation is inextricably bound to a Node.js/JSON environment. There is no existing Python script within the analyzed source data that performs this explicit directed acyclic graph (DAG) traversal across local Markdown files. Therefore, the unlock depth calculation must be built entirely from scratch. The solution requires a recursive Python function capable of parsing the `unlocks` and `depends_on` YAML frontmatter arrays across all project files, traversing the connecting nodes, and appending an accurate `unlock_depth` integer to the dynamically generated `registry.md`.   

Furthermore, **KB2: Extract state deltas** lacks a fully portable execution script. While OpenClaw perfectly demonstrates the abstract pattern of LLM → JSON → Deterministic Router, the exact schema mapping and the specific string-replacement mechanisms required to apply those JSON deltas to the unique Apex markdown files must be authored cleanly from scratch.   

## Phase 4: Final Summary Table

The architectural synthesis determines whether each of the twenty required processes should be cloned exactly as they exist (FULL), adapted for language or internal format (ADAPT), rebuilt purely conceptually from scratch (CONCEPT), or skipped entirely for v1 orchestration (SKIP).   

|Process ID|Process name|Best source|Mechanism|Needs script|Copy type|Priority rank|
|---|---|---|---|---|---|---|
|PM4|Compute next action|Task Master AI|Dependency logic calculation|Yes|ADAPT|1|
|KB2|Extract state deltas|OpenClaw TaskFlow|LLM delta JSON extraction|Yes|ADAPT|3|
|PM3|Assign dependencies|Task Master AI|YAML frontmatter `depends_on`|No|FULL|5|
|PD4|Synthesize focus recommendation|CrewAI|`expected_output` LLM reasoning|No|ADAPT|6|
|KB6|Produce next-session context|PRC-HANDOFF-001|Handoff context packet output|No|FULL|7|
|PM2|Decompose project|CCPM|Hierarchical epic-to-task splitting|No|ADAPT|9|
|PD3|Compute unlock depth|Task Master AI|Graph node traversal scoring|Yes|CONCEPT|10|
|KB4|Rebuild index|llm-wiki|File aggregation via directory scan|Yes|ADAPT|11|
|PM8|Generate work registry|OpenClaw|Deterministic metadata compilation|Yes|ADAPT|13|
|PD6|Feed planning layer|PRC-HANDOFF-001|Session handoff ingestion|No|FULL|14|
|KB1|Write session progress|planning-with-files|Append-only narrative log|No|FULL|15|
|PD5|Validate with operator|PRC-RISK-001|Human-in-the-loop validation gate|No|FULL|17|
|PM5|Detect blockers|CCPM|Scripted prerequisite constraint check|Yes|ADAPT|18|
|KB3|Maintain entity files|planning-with-files|2-action write rule safety limit|Yes|FULL|19|
|PM6|Update status|kanban-skill|Surgical YAML string replacement|Yes|ADAPT|21|
|PM7|Detect stall|OpenClaw TaskFlow|3-session `next_action` string diff|Yes|CONCEPT|22|
|PD1|Score priority|Task Master AI|Numeric priority variable math|Yes|CONCEPT|24|
|KB5|Detect drift|GSD Core|Previous vs current registry diff|Yes|CONCEPT|25|
|PD2|Score urgency|CCPM|Semantic deadline evaluation|No|CONCEPT|26|
|PM1|Capture project|Backlog.md|Foundational Markdown + YAML file|No|ADAPT|27|

[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

automazeio/ccpm: Project management skill system for Agents that uses GitHub Issues and Git worktrees for parallel agent execution.

Opens in a new window](https://github.com/automazeio/ccpm)

![](https://drive-thirdparty.googleusercontent.com/32/type/text/code)

ConceptRating_Claude.md

[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Backlog.md - A tool for managing project collaboration between humans and AI Agents in a git ecosystem · GitHub

Opens in a new window](https://github.com/MrLesk/Backlog.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Backlog.md/AGENTS.md at main · MrLesk/Backlog.md · GitHub

Opens in a new window](https://github.com/MrLesk/Backlog.md/blob/main/AGENTS.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Backlog.md/bunfig.toml at main · MrLesk/Backlog.md · GitHub

Opens in a new window](https://github.com/MrLesk/Backlog.md/blob/main/bunfig.toml)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

BACK-467 - Add local file preview with syntax highlighting and line numbers by kuwork · Pull Request #634 · MrLesk/Backlog.md - GitHub

Opens in a new window](https://github.com/MrLesk/Backlog.md/pull/634)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

claude-task-master/docs/task-structure.md at main - GitHub

Opens in a new window](https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md)[

![](https://t0.gstatic.com/faviconV2?url=https://docs.task-master.dev/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

docs.task-master.dev

Task Structure - Task Master

Opens in a new window](https://docs.task-master.dev/capabilities/task-structure)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

James-Cherished-Inc/AI-task-master: An AI-powered task-management system for Cursor, Roo and Cline, based on https://x.com/EyalToledano work · GitHub - GitHub

Opens in a new window](https://github.com/James-Cherished-Inc/AI-task-master)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

claude-task-master/docs/tutorial.md at main - GitHub

Opens in a new window](https://github.com/eyaltoledano/claude-task-master/blob/main/docs/tutorial.md)

![](https://drive-thirdparty.googleusercontent.com/32/type/text/code)

PMSkillDBResearch_GPT.md

[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

open-gsd/gsd-core: Git. Ship. Done - Core - GitHub

Opens in a new window](https://github.com/open-gsd/gsd-core)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

gsd-core/README.md at next - GitHub

Opens in a new window](https://github.com/open-gsd/gsd-core/blob/next/README.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

feat: add Business Context section to PROJECT.md template · Issue #72 - GitHub

Opens in a new window](https://github.com/open-gsd/gsd-core/issues/72)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

gsd-core/docs/tutorials/your-first-project.md at next - GitHub

Opens in a new window](https://github.com/open-gsd/gsd-core/blob/next/docs/tutorials/your-first-project.md)[

![](https://t0.gstatic.com/faviconV2?url=https://www.msbiro.net/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

msbiro.net

Testing GSD: From a Docs-Only Repo to Working Go Code in One Session

Opens in a new window](https://www.msbiro.net/posts/gsd-sbom-drift-spec-driven-development/)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

gsd-core/docs/COMMANDS.md at next - GitHub

Opens in a new window](https://github.com/open-gsd/gsd-core/blob/next/docs/COMMANDS.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

gsd-core/docs/CONFIGURATION.md at next - GitHub

Opens in a new window](https://github.com/open-gsd/gsd-core/blob/next/docs/CONFIGURATION.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

GitHub - OthmanAdi/planning-with-files: Persistent file-based planning for AI coding agents and long-running agentic tasks. Crash-proof markdown plans that survive context loss and /clear, plus a deterministic completion gate and multi-agent shared state on disk. Manus-style. Works with Claude Code, Codex CLI, Cursor, Kiro, OpenCode and 60+ agents via the SKILL.md standard.

Opens in a new window](https://github.com/othmanadi/planning-with-files)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

ok-skills/planning-with-files/SKILL.md at main - GitHub

Opens in a new window](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

planning-with-files/docs/quickstart.md at master - GitHub

Opens in a new window](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)[

![](https://t3.gstatic.com/faviconV2?url=https://tessl.io/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

tessl.io

planning-with-files • othmanadi • Skills • Registry - Tessl

Opens in a new window](https://tessl.io/registry/skills/github/othmanadi/planning-with-files/planning-with-files)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

model-usage: handle numeric-string costs and ignore non-finite

Opens in a new window](https://github.com/openclaw/openclaw/issues/37878)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Docs: Add model-level usage summary via CodexBar CLI · Issue #10964 - GitHub

Opens in a new window](https://github.com/openclaw/openclaw/issues/10964)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

feat: Expose TaskFlow managed mode as Agent-accessible tools

Opens in a new window](https://github.com/openclaw/openclaw/issues/88611)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

crewAIInc/skills - GitHub

Opens in a new window](https://github.com/crewaiinc/skills)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

llm-wiki-plugin/integrations/paperclip/README.md at main - GitHub

Opens in a new window](https://github.com/praneybehl/llm-wiki-plugin/blob/main/integrations/paperclip/README.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Andrej Karpathy's LLM Wiki pattern as a Claude Code plugin - GitHub

Opens in a new window](https://github.com/praneybehl/llm-wiki-plugin)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

swarmvault/templates/llm-wiki-schema.md at main - GitHub

Opens in a new window](https://github.com/swarmclawai/swarmvault/blob/main/templates/llm-wiki-schema.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

mattjoyce/kanban-skill: an AI skill to manage a markdown file based kanban workload. - GitHub

Opens in a new window](https://github.com/mattjoyce/kanban-skill)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

GitHub - phuryn/pm-skills: PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth.

Opens in a new window](https://github.com/phuryn/pm-skills)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

GitHub - product-on-purpose/pm-skills: 66 plug-and-play, best-practice, product management skills for AI agents: 30 Triple Diamond phase + 8 foundation + 10 utility + 15 tool (Foundation Sprint + Design Sprint)... Plus 4 sub-agents, templates, workflows, samples, learning resources & guides, CI-enforced contracts. Apache 2.0.

Opens in a new window](https://github.com/product-on-purpose/pm-skills)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

[Resource]: PM Skills · Issue #744 · hesreallyhim/awesome-claude-code - GitHub

Opens in a new window](https://github.com/hesreallyhim/awesome-claude-code/issues/744)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Product-Manager-Skills/docs/Using PM Skills with Claude.md at main - GitHub

Opens in a new window](https://github.com/deanpeters/Product-Manager-Skills/blob/main/docs/Using%20PM%20Skills%20with%20Claude.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Releases · product-on-purpose/pm-skills - GitHub

Opens in a new window](https://github.com/product-on-purpose/pm-skills/releases)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

SwarmVault #1539 - hesreallyhim/awesome-claude-code - GitHub

Opens in a new window](https://github.com/hesreallyhim/awesome-claude-code/issues/1539)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

GitHub - swarmclawai/swarmvault: The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory.

Opens in a new window](https://github.com/swarmclawai/swarmvault)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Releases · swarmclawai/swarmvault - GitHub

Opens in a new window](https://github.com/swarmclawai/swarmvault/releases)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

BehiSecc/awesome-claude-skills - GitHub

Opens in a new window](https://github.com/BehiSecc/awesome-claude-skills)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

GitHub - ilang-ai/Imprint: Your AI's DNA: one skill for memory, compression, onboarding, code review, debugging, planning, progress tracking, testing, git workflow, and SEO. It learns your patterns from conversations, encodes them in structure, and carries them across platforms. Use it for any code, project, document, feature, commit, or new session.

Opens in a new window](https://github.com/ilang-ai/Imprint)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

[Feature]: Add Imprint to optional-skills — portable working profile across agents · Issue #12484 · NousResearch/hermes-agent - GitHub

Opens in a new window](https://github.com/NousResearch/hermes-agent/issues/12484)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Clarify whether auxiliary.skills_hub is reserved or stale · Issue #40703 · NousResearch/hermes-agent - GitHub

Opens in a new window](https://github.com/NousResearch/hermes-agent/issues/40703)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

hermes-agent/AGENTS.md at main - GitHub

Opens in a new window](https://github.com/NousResearch/hermes-agent/blob/main/AGENTS.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

hermes-agent/website/docs/user-guide/features/skills.md at main - GitHub

Opens in a new window](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

security: skills_guard._resolve_trust_level prefix-match grants trusted tier to attacker-controlled identifiers · Issue #31141 · NousResearch/hermes-agent - GitHub

Opens in a new window](https://github.com/NousResearch/hermes-agent/issues/31141)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Support persistent custom well-known skill hub sources in Hermes · Issue #44602 - GitHub

Opens in a new window](https://github.com/NousResearch/hermes-agent/issues/44602)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

[Bug]: hermes skills update doesn't refresh lock content_hash, causing permanent false 'update_available' #41176 - GitHub

Opens in a new window](https://github.com/NousResearch/hermes-agent/issues/41176)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

langchain-ai/langgraph-example - GitHub

Opens in a new window](https://github.com/langchain-ai/langgraph-example)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

langchain-ai/langgraph: Build resilient agents. - GitHub

Opens in a new window](https://github.com/langchain-ai/langgraph)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

RFC: AMP (Agent Message Protocol) — standard for LangGraph agents to be discoverable across frameworks · Issue #7208 - GitHub

Opens in a new window](https://github.com/langchain-ai/langgraph/issues/7208)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Checkpoint deserialization silently loses state when JsonPlusSerializer encounters unknown types · Issue #7066 · langchain-ai/langgraph - GitHub

Opens in a new window](https://github.com/langchain-ai/langgraph/issues/7066)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Proposal: Trust-Gated Checkpoint Node for LangGraph · Issue #6824 - GitHub

Opens in a new window](https://github.com/langchain-ai/langgraph/issues/6824)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

Long tool calls (~180s+) silently re-executed from checkpoint on LangGraph Cloud #7417

Opens in a new window](https://github.com/langchain-ai/langgraph/issues/7417)[

![](https://t1.gstatic.com/faviconV2?url=https://github.com/&client=BARD&type=FAVICON&size=256&fallback_opts=TYPE,SIZE,URL)

github.com

claude-task-master/README-task-master.md at main · eyaltoledano/claude-task-master - GitHub





](https://github.com/eyaltoledano/claude-task-master/blob/main/README-task-master.md)