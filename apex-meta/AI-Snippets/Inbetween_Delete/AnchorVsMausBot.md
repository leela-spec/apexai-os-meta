Compare anchor and openmausbot as alternatives to create an agent orchestration harness.. specifically for using several cli agents, having automated learning loops, state of the art informatics design and token efficiency

### Architecture & Foundational Philosophy

|Dimension|**Anchor** (`Redtropig/harness-anchor` / Anchor harness design)|**OpenMausBot** (`milind-soni/OpenMausBot`)|
|---|---|---|
|**Primary Paradigm**|**Spec-driven state & evidence runtime** layer (file/git-centric harness).|**Multi-bot desktop & local harness server** (process supervisor & channel bus).|
|**Execution Surface**|Headless CLI runtime, Git repo workspace, POSIX shell hooks.|Local harness server on `127.0.0.1:8799`, Electron UI, local/cloud VM sandbox.|
|**Core Abstraction**|Schema gates, feature lists, evidence trails, and isolated evaluator subagents.|Agent channels, bot rosters, responder rules, and Composio/OAuth tools.|
|**State Storage**|Plain-text Markdown/JSON files (`feature_list.schema.json`, `PROJECT-TOC.md`, `progress.md`).|App config & SQLite/JSON state in `~/.openmausbot`.|

### CLI Agent Management & Sub-Agent Execution

- **Anchor:** Operates as a runtime layer directly over coding CLIs (e.g., Claude Code, Codex CLI). Rather than launching a heavy UI shell, Anchor runs on disk with targeted commands (`/verify`, `/test-plan`, `/gc`, `/status`). Sub-agents are spawned as **isolated, fresh-context evaluators**. The builder agent cannot grade its own output; verification agents have read-only frontmatter constraints to guarantee verification integrity.
    
    GitHub+ 3
    
- **OpenMausBot:** Acts as a unified process supervisor wrapper. It sits on localhost and drives external binaries (`claude`, `codex`, `grok`) installed on your host system. It maps agents to discrete chat channels with dedicated roles (e.g., Chief of Staff, Developer, Researcher).
    
    GitHub+ 1
    
- **Verdict:** **OpenMausBot** is superior if you want a collaborative multi-agent workspace with multiple distinct CLI engines operating concurrently in isolated channels. **Anchor** is superior if your goal is strict engineering orchestration, avoiding context pollution by dispatching read-only sub-agents for automated validation.
    
    GitHub+ 1
    

### Automated Learning Loops & Self-Correction

- **Anchor:** Built specifically around deterministic feedback loops:
    
    - **Evidence-Gated Progression:** An agent cannot mark a task `status: pass` in `feature_list.json` without an explicit evidence path (test run log, compiler diagnostic, lint artifact) validated against a JSON schema.
        
        GitHub
        
    - **Bounded Auto-Fix Cycles:** Commands like `/verify --fix` run a bounded auto-correction loop (≤2 cycles) in a fresh context, feeding exact terminal diagnostics back to the fixing agent.
        
        GitHub
        
    - **Drift & Anti-Slop Analysis:** The `/gc` routine runs a clean-context evaluator against `golden-rules.md` to flag architectural drift and unneeded boilerplate.
        
        GitHub
        
- **OpenMausBot:** Primarily conversational and workflow-driven:
    
    - Feedback loops rely on interactive approval cards (Allow/Deny diffs), `@mention` relay hops between bots, and automated routines.
        
        Software Mirrors
        
    - Does not have native schema-level enforcement that blocks agent completion until regression tests and deterministic evidence trails pass.
        
- **Verdict:** **Anchor** is far more capable for autonomous, closed-loop technical execution. OpenMausBot requires manual human intervention or external loop scripts to guarantee convergence.
    

### Informatics Design & State Persistence

- **Anchor (File-as-State / Spec-Driven):**
    
    - **Context Survival:** Solves the context compaction problem by maintaining truth strictly in Git and flat files (`PROJECT-TOC.md`, `progress.md`, `feature_list.json`).
        
    - **Deterministic Sentinels:** Four warn-only triggers fire at critical session junctures: _context filling_, _compaction imminent_, _just-compacted_, and _session stopping_. When compaction occurs, state is re-anchored directly from disk rather than relying on degraded rolling conversational history.
        
        GitHub+ 1
        
- **OpenMausBot (Channel & Session Model):**
    
    - **Context Isolation via Channels:** Partitions work by channel, each holding its own transcript, working directory, and roster.
        
        GitHub
        
    - **Decision Routing:** Integrates fast-routing decision models (via TypeSafe Jev or OpenRouter) to determine which agent should respond to an unmentioned message.
        
        GitHub
        
    - Informatics design leans heavily on desktop UI visibility (Electron, sandbox stream cards, Composio connections) rather than repository-native metadata structures.
        
- **Verdict:** For repository-level software informatics, **Anchor** follows spec-driven engineering standards. For organizational/cross-tool project coordination, **OpenMausBot** offers a more accessible channel-based informatics plane.
    
    GitHub
    

### Token Efficiency & Context Management

```
┌─────────────────────────────────────────────────────────────┐
│                 TOKEN CONSUMPTION PROFILE                   │
├──────────────────────────────┬──────────────────────────────┤
│ Anchor                       │ OpenMausBot                  │
│ • Fresh-context evaluators   │ • Long-running channels      │
│ • Strict schema gating       │ • Multi-turn chat history    │
│ • Warn-only sentinels        │ • Full tool-definition trees │
│ • Lean file-based retrieval  │ • Periodic summarization     │
│ [High token discipline]      │ [Moderate token burn]        │
└──────────────────────────────┴──────────────────────────────┘
```

- **Anchor:**
    
    - **Task Scoping:** Enforces "one active feature at a time" to eliminate prompt bloat and prevent out-of-scope actions.
        
    - **Offloaded Compaction:** Heavy inspection routines (building ASTs, scanning project tables of contents, running coverage audits) happen inside disposable sub-agents. The main orchestrator context remains unpolluted, receiving only the condensed evidence path or diff.
        
- **OpenMausBot:**
    
    - Maintains conversational history inside channel threads. When chats stretch long, idle summarization compacts history, but multi-agent group chats can burn significant tokens through back-and-forth chat exchanges and verbose environment logs.
        
- **Verdict:** **Anchor** is significantly more token-efficient for complex technical workloads because it delegates token-heavy exploration and evaluation to ephemeral worker contexts.
    

### Recommendation Matrix

- **Choose Anchor if:** Your core focus is automated software engineering, headless CLI orchestration, strict test/lint evidence validation, and maximizing token mileage through spec-driven development and ephemeral sub-agents.
    
- **Choose OpenMausBot if:** You want a localized, multi-agent control room where different CLI agents (Claude, Codex, Grok) act as distinct department teammates with access to virtual machines, host OS environments, and external apps via Composio.
    
    Software Mirrors
    
- **Hybrid Approach:** A common high-leverage pattern is using **OpenMausBot** as the high-level routing harness and UI channel supervisor, while installing **Anchor** within individual coding agents' working directories to enforce evidence schemas, context sentinels, and validation gates.