Your research is highly accurate regarding the fundamental shift in the 2026 ecosystem, but there are some important additions to note regarding how **Claude Code** and **Claude Managed Agents** differ.

In late spring 2026, Anthropic split these features down a clear boundary:

- **Claude Managed Agents (Cloud REST API):** Features a fully hosted platform sandbox utilizing `/mnt/memory/{store-name}` with server-side async **Dreaming** (hippocampal replay consolidation) powered by Opus 4.7/Sonnet 4.6.
    
- **Claude Code (Local CLI):** Uses machine-local storage under `~/.claude/projects/[repo]/`. The recently rolled-out **Auto Memory** (v2.1.59+) and **Auto Dream** (`/dream`) routines operate locally by running lightweight background subagents to clean, merge, and index your local transcripts into `MEMORY.md` and custom topic files.
    

### The 1–100 Performance & Attribute Matrix

To address your request directly, here is the expanded evaluation of the `llm-wiki` and native options on a **1–100 scale**, assessing performance across the key variables.

|**Memory Option**|**Retrieval Quality (1-100)**|**Token Efficiency (1-100)**|**Incremental Flow Fit (1-100)**|**Setup Ease (1-100)**|**Multi-Project Isolation (1-100)**|**Claude Code Integration (1-100)**|
|---|---|---|---|---|---|---|
|**repomemory** (MCP)|85|88|98|65|96|88|
|**agentmemory** (MCP)|96|85|82|60|80|85|
|**MemCP** (MCP)|72|86|96|62|82|85|
|**Auto Dream** (Native CLI)|68|94|85|98|88|98|
|**Auto Memory** (Native CLI)|62|82|84|98|95|98|
|**claude-mem**|74|84|92|68|65|82|
|**ICM** (In-Context Mem)|80|65|78|70|70|68|
|**CLAUDE.md Hierarchical**|45|88|65|100|100|100|
|**Kairn**|65|60|60|45|45|50|

### Operational Archetypes: Costs, Autonomy, & Determinism

To help you choose the best stack for your incremental workflows, the options are categorized below by their operational costs and execution models.

#### 1. Completely Deterministic & Fully Local (Zero Token Cost)

These solutions run entirely via local code, Python scripts, or markdown file hierarchies. They do not invoke an LLM or use tokens to capture or structure their core data, making them entirely predictable.

- **CLAUDE.md Hierarchical Pattern (Score: 100% Local / 100% Deterministic)**
    
    - _How it works:_ Pure markdown configuration files split across structural layers (Global $\rightarrow$ Repo $\rightarrow$ Folder).
        
    - _Financial Cost:_ **$0.00**. Completely free.
        
    - _Token Impact:_ Static footprint (recommended under 800 tokens for the core file). It only consumes tokens as raw text context.
        
    - _Determinism:_ Absolute. There is zero AI variance; rules, styles, and flags stay exactly where you write them.
        
- **repomemory [MCP In-Repo Mode] (Score: 100% Local / 85% Deterministic)**
    
    - _How it works:_ A Model Context Protocol (MCP) server that isolates data directly within a `.context/` directory inside your specific Git repository. It performs hybrid keyword search via local scripting.
        
    - _Financial Cost:_ **$0.00**. Runs locally on your machine.
        
    - _Token Impact:_ High efficiency. It prevents text bleed across your different programming projects.
        
    - _Determinism:_ High. File read/write states use a predictable local file layout, though the final retrieval match uses a minor semantic ranking step.
        

#### 2. Self-Sufficient & Local (Uses Tokens, No External API Fees)

These tools execute directly on your local machine using your existing Claude Code framework. They require LLM tokens to synthesize or summarize text, but they run without third-party platform subscriptions or outside database costs.

- **Auto Memory & Auto Dream (Native Claude Code v2.1.59+)**
    
    - _How it works:_ Passive background capture. `Auto Memory` writes raw interaction snippets locally, and running `/dream` triggers a local subagent that parses your `~/.claude/projects/` JSONL logs to rewrite, clean, and compress long-term project knowledge into `MEMORY.md`.
        
    - _Financial Cost:_ Included with your standard Claude Code token consumption. No secondary billing.
        
    - _Token Impact:_ Excellent. The background consolidation trims your active index down to under 200 lines, protecting the active context window.
        
    - _Determinism:_ Low to Medium. Because a subagent autonomously chooses what to merge, delete, or flag as a "recurring pattern," memories can shift dynamically between sessions.
        
- **agentmemory (MCP Server)**
    
    - _How it works:_ Uses local BM25 keyword matching combined with an embedded vector database to execute Reciprocal Rank Fusion (RRF) search.
        
    - _Financial Cost:_ **$0.00** external infrastructure costs, but relies heavily on local system resources.
        
    - _Token Impact:_ Provides the highest benchmark recall efficiency, delivering highly precise context packages to the prompt window.
        
- **MemCP**
    
    - _How it works:_ Purpose-built to handle session compaction issues. It checkpoints task parameters right before Claude Code triggers a `/compact` boundary.
        
    - _Financial Cost:_ No external infrastructure costs.
        
    - _Determinism:_ High mechanical predictability, keeping track of transient multi-step state parameters.
        

#### 3. Incurs External/Extra Costs (Token and/or Subscription Fees)

These options require independent API calls, paid cloud platforms, or third-party subscription plans to function.

- **claude-mem**
    
    - _Extra Costs:_ Incurs an estimated **$5 to $15+ per month** in supplementary LLM API fees. It uses separate, real-time background orchestration calls to compress short-term inputs and inject them into your next prompt sequence.
        
- **Kairn**
    
    - _Extra Costs:_ Relies on a hosted cloud architecture and external indexing services. This setup introduces noticeable operational complexity, external dependencies, and potential data-privacy overhead for private local repositories.
        

### Recommended Setup for Incremental Workflows

If your goal is to build an isolated, per-project architecture that maximizes token efficiency while avoiding extra subscription bills, this layered implementation works best:

1. **The Foundation (Deterministic):** Use **CLAUDE.md Hierarchical** files to hardcode your permanent project architectures, paths, and technical requirements.
    
2. **The Working Memory (Local MCP):** Use **repomemory** or **MemCP** to track active file changes and handle state parameters across mid-task terminal resets.
    
3. **The Background Maintenance (Native Local):** Rely on Claude Code's native **Auto Memory** and **Auto Dream** to clean, compress, and index long-term project insights directly within your machine-local workspace.
