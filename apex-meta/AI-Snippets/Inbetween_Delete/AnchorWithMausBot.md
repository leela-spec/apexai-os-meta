Across open-source agent ecosystems, **Anchor** (`Redtropig/harness-anchor`) and **OpenMausBot** (`milind-soni/OpenMausBot`) are not direct competitors. They occupy completely different layers of the harness stack:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   CONTROL PLANE (OpenMausBot)                          │
│  • Multi-Engine Supervisor (Claude Code, Codex CLI, Grok)              │
│  • Channel Routing, Permissions Broker, VNC Desktop Streams            │
│  • Human-in-the-Loop Approval Cards & Composio/MCP Tools               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ spawns & dispatches tasks to
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   EXECUTION PLANE (Anchor Runtime)                     │
│  • File-as-State: feature_list.json, PROJECT-TOC.md, progress.md       │
│  • Schema-Gated Evidence (Test/Lint artifacts required for "Pass")     │
│  • Read-Only Fresh-Context Subagents (/verify, /test-plan, /gc)        │
│  • Compaction Sentinels & Anti-Slop Golden Rules                       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ runs inside
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   TARGET WORKSPACE / REPOSITORY (Git)                  │
└────────────────────────────────────────────────────────────────────────┘
```

- **OpenMausBot** is an **Outer Harness / Orchestration Supervisor** (orchestrates multiple CLI agents, desktop/VM sandboxes, human approvals, and event buses).
    
- **Anchor** is an **Inner Harness / Execution Guardrail** (a deterministic, file-backed runtime enforcing task scoping, evidence schemas, and evaluation hygiene within a single CLI agent's workspace).
    

Attempting to choose one over the other forces a false dichotomy: **OpenMausBot lacks repository-level verification hygiene, while Anchor lacks multi-agent routing and workspace oversight.** Combining them forms a layered orchestration pipeline.

### Structural Interconnection & Layer Separation

```
[User / Product Request]
         │
         ▼
[OpenMausBot Channel: #triage / Chief of Staff]
         │
         ├──> Routes task & parameters to #dev (Worker Bot: Claude Code / Codex CLI)
         │
         ▼
[Target Workspace (e.g., C:\GitDev\Project)]
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                           Anchor Runtime                                │
  │  1. /status & /anchor read feature_list.json                            │
  │  2. Worker CLI implements feature (bounded scope)                       │
  │  3. Worker attempts completion                                          │
  │  4. Anchor intercepts -> dispatches ephemeral, read-only subagents:    │
  │     • verification-runner (evaluates test/lint output to disk)          │
  │     • coverage-analyst (/test-plan code obligations)                    │
  │     • drift-analyst (/gc against golden-rules.md)                       │
  │  5. Schema validates evidence -> updates feature_list.json             │
  │  6. Sentinels trigger /session-end & update progress.md                 │
  └──────────────────────────────────┬──────────────────────────────────────┘
                                     │
         ┌───────────────────────────┘
         ▼
[OpenMausBot Event Bus (127.0.0.1:8799)]
  • Receives structured completion payload & diff
  • Shows Interactive Approval Card (Allow/Deny diff + Evidence log)
  • Triggers Composio/GitHub PR sync
```

### Deep Dive: Addressing the Four Design Pillars

#### 1. CLI Agent Execution & Multi-Agent Coordination

- **OpenMausBot's Role:** Acts as the local process daemon on `127.0.0.1:8799`. It manages concurrent sessions across heterogeneous CLI binaries (`claude`, `codex`, `grok`). It isolates them into dedicated channels with distinct working directories, system instructions, and tool allowances.
    
- **Anchor's Role:** Enforces environment discipline _within_ each spawned CLI agent. It installs directly into the CLI tool runtime (e.g., as a Claude Code marketplace plugin) and runs native bash/git hooks. It ensures that an agent running headless does not go rogue, wander across directories, or silently skip build errors.
    

#### 2. Automated Learning Loops & Self-Correction

- **The Naive Flaw:** When an agent writes code and then reviews its own code in the same session, confirmation bias and degraded context cause it to hallucinate success.
    
- **The Combined Loop:**
    
    1. OpenMausBot routes an issue to the developer agent.
        
    2. The agent writes code and runs Anchor’s `/verify --fix`.
        
    3. Anchor automatically spawns a **fresh-context evaluator subagent** (`verification-runner`). By design, this subagent is read-only by frontmatter. It cannot edit the files to suppress errors; it can only execute builds and log compiler/test diagnostics to an explicit file path.
        
    4. If tests fail, Anchor feeds the compiler diagnostics into a bounded ($\le 2$ cycles) auto-fix loop.
        
    5. The loop stops deterministically: the task cannot transition to `status: pass` until `feature_list.schema.json` validates that a non-null, verifiable log path exists on disk.
        

#### 3. State-of-the-Art Informatics & State Management

- **Durable Disk Truth:** Chat scrollback is ephemeral. When agent sessions compact or reset, conversational context is compressed or lost.
    
- **Informatics Division:**
    
    - **Macro Informatics (OpenMausBot):** Real-time desktop UI, SSE event streams, approval queues, tool connection statuses, and per-channel message history.
        
    - **Micro Informatics (Anchor):** Spec-Driven Development (SDD) artifacts. Anchor structures state into plain-text files: `feature_list.json` (computable schema state), `PROJECT-TOC.md` (codebase map built by `index-curator`), `progress.md` (chronological session handoffs), and `golden-rules.md` (architectural constraints).
        
    - **Sentinels:** Anchor injects deterministic, warn-only triggers at four critical failure points: _context filling_, _compaction imminent_, _just-compacted_, and _session stopping_. When context compactor routines strike, the CLI agent immediately reloads its state from `progress.md` and `feature_list.json` rather than guessing.
        

#### 4. Token Efficiency & Context Hygiene

- **OpenMausBot Standalone Token Risk:** Multi-agent group chats quickly become token sinks when agents talk back and forth, dragging along whole conversational histories, environment dumps, and tool declarations.
    
- **Anchor Optimization:**
    
    - **Single Active Feature Rule:** Anchor restricts the active CLI agent to exactly one task item at a time, preventing token-wasting scope expansion.
        
    - **Offloaded Token Heavy-Lifting:** Heavy codebase scans, test analyses, and AST checks are offloaded to disposable sub-agents (`coverage-analyst`, `drift-analyst`). These subagents run in isolated temporary contexts, inspect the files, write a condensed summary report, and exit. The main agent context only ingests the distilled markdown artifact, reducing primary context token burn by up to 60–75%.
        

### Concrete Workflow Simulation

#### Scenario: Implementing an Authenticated Endpoint with Staged Verification

```
[Step 1: Ingestion & Orchestration]
  User sends prompt to OpenMausBot:
  "Implement JWT revocation endpoint in the auth service and add integration tests."
  │
  ▼
[Step 2: Task Allocation & Channel Dispatch]
  OpenMausBot's router assigns the task to the #backend channel running Claude Code.
  Anchor initializes context inside the target repo:
  • Reads PROJECT-TOC.md (structural map of the auth module).
  • Injects active feature item into feature_list.json:
    {"id": "feat_jwt_revoke", "status": "in_progress", "evidence": null}
  │
  ▼
[Step 3: Execution & Scope Enforcement]
  Claude Code modifies auth middleware and token handlers.
  Agent attempts to draft out-of-scope database migration logic.
  Anchor hook alerts: Scope jump detected (modifying outside active feature boundary).
  Agent restricts edits strictly to JWT token revocation logic.
  │
  ▼
[Step 4: Automated Verification Loop]
  Agent invokes /verify --fix.
  Anchor spawns read-only subagent `verification-runner`:
  • Executes: pytest tests/auth/test_revocation.py --json-report
  • Cycle 1: Revocation blacklist cache check returns 404 (Failure).
  • Subagent outputs failure log: /artifacts/run_01_fail.log
  • Anchor passes exact log back to Claude Code.
  • Claude Code patches Redis cache key lookup.
  • Cycle 2: All 8 integration assertions pass (Success).
  • Subagent outputs pass log: /artifacts/run_02_pass.log
  │
  ▼
[Step 5: Schema Validation & Compaction Protection]
  Anchor's `feature_list.schema.json` validates evidence path "/artifacts/run_02_pass.log".
  Status flips to "pass".
  Anchor sentinel detects token budget threshold:
  • Automatically runs /session-end: updates progress.md with handoff summary.
  • Commits changes cleanly with git tag: feat-jwt-revocation-verified.
  │
  ▼
[Step 6: Human-in-the-Loop Gate & PR Delivery]
  OpenMausBot intercepts git commit event via local daemon.
  Presents UI Approval Card on Desktop:
  • Diffs: 3 files changed (+42, -6).
  • Anchor Evidence: /artifacts/run_02_pass.log (100% green).
  • User clicks "Approve".
  OpenMausBot fires GitHub tool to publish PR #104.
```

### Implementation Blueprint

To set up this integrated architecture:

1. **Install OpenMausBot Supervisor:**
    
    - Run the local harness server (`npx openmausbot start` or native desktop binary).
        
    - Configure agent engine logins for your installed CLIs (`claude`, `codex`) via Settings → Engines.
        
2. **Install Anchor in Target Repositories:**
    
    - In your workspace repos, register the plugin in your CLI runtime:
        
        Bash
        
        ```
        claude /plugin marketplace add Redtropig/harness-anchor
        claude /plugin install harness-anchor@harness-anchor-local
        ```
        
    - Run `/anchor` inside each repository root to scaffold `feature_list.json`, `golden-rules.md`, and `PROJECT-TOC.md`.
        
3. **Configure Channel Boundaries in OpenMausBot:**
    
    - Create focused channels (e.g., `#core-api`, `#ui-components`, `#auditor`) mapped to respective repository roots.
        
    - Ensure the agent system prompt references the local Anchor state commands (`/status`, `/verify`, `/gc`) as mandatory quality gates.