A structured comparison of these frameworks across the key engineering dimensions shows how each fulfills different architectural layers.

  

### Framework Matrix

|**Framework / Tool**|**Primary Nature & Focus**|**Multi-Model / BYO Subscription & Local AI**|**CLI Agent Orchestration**|**Automated Learning & Verification Loops**|**Informatics & State Persistence**|**Token Efficiency & Context Hygiene**|
|---|---|---|---|---|---|---|
|**Anchor** (`harness-anchor`)|**Inner Execution Harness** (Git/File-as-State runtime layer)|Direct CLI runtime layer; uses whatever model the underlying CLI (`claude`, `codex`, local bridge) exposes.|Manages single CLI sessions via rigid bash hooks; spawns isolated read-only subagents.|**S-Tier** (Schema-gated evidence, bounded `/verify --fix` cycles, anti-drift `/gc`).|**S-Tier** (Strict spec-driven files: `feature_list.json`, `PROJECT-TOC.md`, sentinels).|**S-Tier** (Single-task scoping; ephemeral worker contexts prevent token bloat).|
|**OpenMausBot** (`MausBot`)|**Outer Multi-Bot Supervisor** (Local server daemon + desktop app)|**S-Tier** (Bridges existing subscriptions for Claude, Codex, Grok CLIs via local processes; no extra API fees).|**A-Tier** (Channel-based routing, Jev fast-routing, Composio tools, host/VM permissions).|**C-Tier** (Relies on chat approval cards and manual relay; lacks deterministic verification).|**B-Tier** (Channel transcripts, JSON/SQLite configs in `~/.openmausbot`).|**B-Tier** (Long channel histories cause token drag; relies on periodic compaction).|
|**Orca ADE** (`stablyai/orca`)|**Agent Development Environment** (Fleet IDE / multiplexer)|**S-Tier** (Runs Claude Code, Codex, Hermes, local models side-by-side on existing subscriptions).|**S-Tier** (Git worktrees, split WebGL terminals, element-select UI, mobile companion).|**B-Tier** (Human annotation feedback batches; lacks native self-evaluating test loops).|**A-Tier** (Git worktree isolation, live visual previews, diff inspectors).|**A-Tier** (Worktree isolation prevents cross-branch context bleed).|
|**Agent OS** (Workflow Layer / Architecture)|**Meta-Orchestrator & Business Engine** (Playbooks & operational routines)|Decoupled; sits on top of API/subscription engines (often paired with Hermes / OpenCode / Orca).|**B-Tier** (Focuses on end-to-end task flows, cross-department role templates, and playbooks).|**A-Tier** (Workflow loops, mentor-agent reviews, task progression stages).|**B-Tier** (Procedural documentation, Markdown playbooks, high-level project status).|**B-Tier** (Depends heavily on prompt design and execution script discipline).|
|**Zed** (`zed.dev`)|**High-Performance Code Editor** (Rust-based IDE with integrated AI)|**A-Tier** (Direct Ollama/LM Studio/llama.cpp support, Anthropic/OpenAI keys, Anthropic subscription integration).|**C-Tier** (Inline assistant, assistant panel, and terminal threads; not a multi-agent manager).|**D-Tier** (Standard inline code generation; no automated evaluation loops).|**B-Tier** (File-system native, fast indexing, but no autonomous agent state tracking).|**A-Tier** (Context control via manual `@` mentions and lean edit predictions).|
|**OpenWebUI** (`openwebui.com`)|**Full-Stack Self-Hosted AI Interface** (Multi-user Web UI)|**S-Tier** (Zero API fees for local Ollama/vLLM; native multi-model chat, pipeline routing).|**F-Tier** (Conversational UI; not designed for autonomous CLI coding agent execution).|**D-Tier** (Conversational interaction only; RAG/eval pipelines are static).|**B-Tier** (RAG databases, user role profiles, shared chat archives).|**C-Tier** (Standard chat history window; token burn scales with chat depth).|

### Dimensional Rankings

#### 1. CLI Agent Fleet Orchestration & Multi-Tenancy

1. **Orca ADE (Rank 1):** Purpose-built for parallel agent fleets. It manages multiple CLI agents (Claude Code, Codex, Hermes, OpenClaw) simultaneously, each assigned to an isolated Git worktree so agents do not overwrite each other's work.
    
      
    
2. **OpenMausBot (Rank 2):** Strong channel-based daemon routing with desktop UI, background VMs, and Composio tool integrations.
    
      
    
3. **Anchor (Rank 3):** Deep execution guardrails for individual CLI agents via headless hooks, but requires an external driver for multi-agent multiplexing.
    
      
    
4. **Agent OS (Rank 4):** Standardizes team playbooks and departmental delegation, but relies on an underlying terminal or runtime to handle raw processes.
    
      
    
5. **Zed (Rank 5):** Fast editor with assistant panels, but fundamentally single-user and conversational.
    
      
    
6. **OpenWebUI (Rank 6):** Not a CLI harness.
    
      
    

#### 2. Subscription Utilization & Zero-Extra-API-Cost Operation

_(Answering the question: "Which tool best allows using multiple models including local AI inside paid subscriptions without extra API costs?")_

  

1. **Orca ADE & OpenMausBot (Tie - Rank 1):** Both execute existing, pre-authenticated CLI sessions (`claude`, `codex`, `grok`) installed on your host machine. They consume standard subscription quotas directly through your web/CLI login tokens rather than billing per token via metered developer APIs. Both connect simultaneously to local inference endpoints (Ollama, LM Studio).
    
      
    
2. **OpenWebUI (Rank 2):** Connects to any local endpoint (Ollama) with zero operational cost, but cannot natively hijack or broker official Claude/ChatGPT Pro/Team web subscription sessions without third-party proxy bridges.
    
      
    
3. **Zed (Rank 3):** Supports local Ollama and subscription-backed providers, but primarily as an editor assistant rather than an autonomous swarm runner.
    
      
    
4. **Anchor (Rank 4):** Inherits the credentials of the host CLI environment.
    
      
    

#### 3. Automated Verification & Learning Loops

1. **Anchor (Rank 1):** Built on deterministic gatekeeper logic. Tasks cannot be marked complete without schema-validated evidence files (`/verify`), auto-repair loops are strictly bounded, and `/gc` subagents audit code against architectural invariants.
    
      
    
2. **Agent OS (Rank 2):** Provides high-level operational review routines and structured approval stages across multi-step deliverables.
    
      
    
3. **Orca ADE (Rank 3):** Offers interactive human-in-the-loop batch feedback (visual element inspection and batch annotations), but lacks programmatic automated unit test fix cycles.
    
      
    
4. **OpenMausBot (Rank 4):** Interactive Allow/Deny execution cards, but minimal self-healing verification.
    
      
    
5. **Zed & OpenWebUI (Rank 5/6):** Zero automated learning or auto-fix loop capabilities.
    
      
    

#### 4. Informatics Design & State Persistence

1. **Anchor (Rank 1):** Uses file-as-state Spec-Driven Development (SDD). Plain-text schema files (`feature_list.json`, `PROJECT-TOC.md`, `progress.md`) survive context resets and terminal crashes.
    
      
    
2. **Orca ADE (Rank 2):** Tracks live visual state, Git branch differences across worktrees, terminal process outputs, and token metrics across panes.
    
      
    
3. **OpenMausBot (Rank 3):** Local event daemon tracking process states, permissions, and channel history in `~/.openmausbot`.
    
      
    
4. **OpenWebUI (Rank 4):** Centralized SQLite/Postgres persistence for RAG embeddings, user histories, and chat branches.
    
      
    
5. **Zed (Rank 5):** Transient workspace index.
    
      
    

#### 5. Token Efficiency & Context Hygiene

1. **Anchor (Rank 1):** Strict "one active feature at a time" boundary. Token-heavy tasks (repo scanning, test analysis) are delegated to ephemeral, read-only subagents that report back only the final diff or diagnostic.
    
      
    
2. **Orca ADE (Rank 2):** Git worktree partitioning ensures that Agent A's terminal context never collides with or bloats Agent B's context window.
    
      
    
3. **Zed (Rank 3):** Highly selective context loading using manual `@` symbol injection and tree-sitter AST queries.
    
      
    
4. **OpenMausBot (Rank 4):** Group channel chats risk context bloating unless sub-tasks are kept in isolated channels.
    
      
    
5. **OpenWebUI (Rank 5):** Conversational chat models continuously append turn history, resulting in rapid token consumption over long sessions.
    
      
    

### The Unified Power Stack

Rather than competing, the optimal setup stacks these tools hierarchically:

  

```
┌─────────────────────────────────────────────────────────────┐
│ 1. SYSTEM & ROUTINE LAYER: Agent OS                         │
│    High-level business playbooks, triage rules, role scopes │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. CONTROL ROOM & WORKTREE HARNESS: Orca ADE / OpenMausBot  │
│    • Multi-agent terminal splits (Claude Code + Codex)      │
│    • Running under active Pro/Team subscription logins      │
│    • Git worktree isolation per feature                     │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. EXECUTION GUARDRAILS: Anchor                             │
│    • Installed in each repo root                            │
│    • Enforces /verify, /gc, and feature_list.json evidence  │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. DAILY CODING & LOCAL AUDIT: Zed                          │
│    Fast, local Rust editor connected to Ollama for review   │
└─────────────────────────────────────────────────────────────┘
```

For team collaboration or general-purpose chatting with local models (via Ollama), **OpenWebUI** serves as an accessible internal portal, while **Orca + Anchor** handles software development.

  

Check out this [Orca ADE tutorial and multi-agent IDE review](https://www.youtube.com/watch?v=cwL9_EsOvZE), which illustrates how running parallel coding agents across isolated git worktrees operates in practice without extra API costs.