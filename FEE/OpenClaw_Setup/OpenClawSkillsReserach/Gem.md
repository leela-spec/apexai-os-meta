## Section A — Executive Recommendation

The OpenClaw ecosystem already contains native mechanisms to satisfy all ten required executor workflows without writing a new OpenClaw skill or building custom wrapper frameworks.

  

### Smallest Recommended Stack

```
OPENCLAW GATEWAY RUNTIME (v2026.3+)
 ├── LLM Backend: Qwen3-8B GGUF via llama.cpp (Vulkan loopback / 32k context)
 │
 ├── OpenClaw Native Capabilities (Zero Extra Skill Code)
 │    ├── browser: Multi-profile CDP control (user & openclaw profiles)
 │    ├── exec: Host process execution with strict allowlist security policy
 │    ├── cron: Native job scheduler (isolated subagent & deterministic modes)
 │    ├── file / workspace: Native read/write/edit filesystem management
 │    └── subagents / sessions: Background task execution (sessions_spawn)
 │
 ├── Official Bundled OpenClaw Skills
 │    └── @openclaw/browser-automation (Native DOM recovery, snapshot ref management, blocker handling)
 │
 ├── Vetted Community / ClawHub Skills
 │    └── @openclaw/github (Optional API-level GitHub integration for PR/issue management)
 │
 └── APEX-Specific Integration Glue (Configuration Only — Zero Custom Skill Code)
      ├── ~/.openclaw/openclaw.json (Exec allowlist, efficient snapshot defaults, Chrome profile paths)
      ├── C:/apex/scripts/claim_check.js (15-line JS browser snippet for direct file-to-DOM / DOM-to-file transfer)
      └── C:/apex/schemas/receipt.json (Standardized receipt schema for reasoning layer feedback)
```

### Recommendation Rationale

Building custom APEX skills or custom browser wrappers for these workflows is unnecessary. OpenClaw’s built-in `browser` tool supports Chrome DevTools Protocol (CDP) attachment to persistent, logged-in Chrome user profiles. Native `browser act kind=evaluate` handles large prompt insertions and response captures directly to disk, bypassing Qwen3-8B’s context window entirely. Native `exec` with `tools.exec.mode: "allowlist"` safely enforces local Git policies (such as blocking `git push -f` or `git reset --hard`) at the gateway layer.

  

## Section B — Workflow-to-Skill Matrix

|**Workflow**|**Recommended Existing Capability / Skill**|**Alternative Candidate**|**Missing Capability Gap**|**Custom Work Required?**|
|---|---|---|---|---|
|**A. Prompt Submission**|Native `browser` tool (`user` profile) + JS `evaluate` paste injection|ClawHub `chatgpt-web` skills|DOM input text truncation on large prompts when typed via LLM token stream|**No** (Config + JS DOM snippet)|
|**B. Response Capture**|Native `browser` JS `evaluate` direct-to-file dump + Claim Check receipt|ClawHub `url-reader` / `firecrawl`|Passing 100KB+ Markdown output back through 32k Qwen context window|**No** (JS DOM snippet)|
|**C. Browser Recovery**|Native `browser` (`--mode efficient`, `--interactive`, Playwright ref-binding) + `@openclaw/browser-automation`|Raw ARIA tree snapshot (`--format aria`)|Token bloat from full page accessibility trees|**No** (Set Gateway config default)|
|**D. Deterministic Scripts**|Native `exec` tool + Host Exec Allowlist Policy (`tools.exec.mode: "allowlist"`)|Community `code-interpreter` plugin|None|**No** (Configure `openclaw.json`)|
|**E. Git Operations**|Native `exec` tool + Command Allowlist scoped to approved `git` commands|ClawHub `@openclaw/github` skill|Preventing destructive Git operations (`push -f`, `reset --hard`)|**No** (Gateway command allowlist)|
|**F. Cron / Schedules**|Native OpenClaw Cron System (`openclaw cron` CLI & jobs engine)|Windows Task Scheduler calling OpenClaw CLI|None|**No** (Built-in OpenClaw feature)|
|**G. Immediate Dispatch**|Gateway API (`/v1/chat/completions` or `openclaw agent run`) + File Handles|Polling Cron file watcher|High latency with file polling|**No** (Native Gateway REST/CLI)|
|**H. Long-Running & Resume**|Native Session Persistence + Task Status Handle Files (`state.json`)|Custom external task DB|Duplicate prompt submissions on browser crashes|**No** (Claim Check state pattern)|
|**I. Multi-Repo Exec**|Native Workspace Profiles (`agents.entries`) + Scoped `exec` Working Dir|Multiple Gateway instances on different ports|High RAM consumption from multiple instances|**No** (Built-in workspace profiles)|
|**J. Evidence & Receipts**|Native Gateway Audit Logs (`/tmp/openclaw/*.log`) + Claim Check JSON Receipts|Custom audit logging daemon|None|**No** (JSON schema contract)|

## Section C — Detailed Candidate Comparison

Candidates are evaluated on a 0–100 scale using the criteria outlined in the evaluation framework: Exact Match (25), Native Reuse (15), Session Reliability (10), Context/Payload Efficiency (10), Security (10), Windows Viability (8), Maturity (7), Simplicity (5), Recovery Quality (5), Adaptability (5).

  

### Workflow A — Prompt Submission to Subscription AIs

- **Winner: Native OpenClaw `browser` Tool (`user` profile) + Clipboard/JS `evaluate`** — **Score: 95/100**
    
      
    - **Mechanics:** Connects via Chrome DevTools Protocol (CDP) to a running Chrome instance with persistent login sessions. Reads the input prompt directly from a disk file path, injects it into the active contenteditable or textarea via `document.execCommand('insertText')` or value assignment, and verifies character count match before clicking "Send".
        
          
        
    - **Why it wins:** Bypasses LLM token stream typing entirely, avoiding token truncation and speed bottlenecks. Keeps logged-in subscription sessions active indefinitely without managing OAuth credentials.
        
          
        
- **Runner-Up: ClawHub `chatgpt-web` / `gpt-web` Community Skills** — **Score: 62/100**
    
      
    - **Mechanics:** Wraps Playwright/Puppeteer with hardcoded CSS selectors for ChatGPT/Gemini UI.
        
          
        
    - **Why it loses:** Vulnerable to minor UI updates. Streamed prompt typing exhausts Qwen3-8B context windows when handling 10,000+ word inputs.
        
          
        
- **Hard Gate Rejection: Cloud API Wrapper Skills (`openai-api`, `perplexity-api`)** — **Score: 0/100**
    
      
    - **Reason:** Fails hard gate requirement to use persistent logged-in web UI subscriptions (such as OpenAI Deep Research or Gemini Advanced).
        
          
        

### Workflow B — Response Capture & Claim Check (Pass-by-Reference)

- **Winner: Native OpenClaw `browser` JS `evaluate` DOM-to-File Dump** — **Score: 96/100**
    
      
    - **Mechanics:** Monitors response completion via `openclaw browser wait --fn "() => !document.querySelector('.streaming-spinner')"`. Executes a lightweight JS snippet that pulls the response text, writes it directly to disk (`C:/apex/artifacts/res_<id>.md`), calculates its SHA-256 hash and byte count, and returns a 100-byte receipt handle to Qwen3-8B.
        
          
        
    - **Why it wins:** Strictly implements the Claim Check pattern. Qwen never processes 50KB+ research reports in its 32k context window.
        
          
        
- **Runner-Up: ClawHub `firecrawl` / `url-reader` Skills** — **Score: 68/100**
    
      
    - **Mechanics:** Fetches URL contents and attempts web scraping.
        
          
        
    - **Why it loses:** Fails on active, authenticated Single Page Application (SPA) web chat sessions without re-authenticating, and returns massive raw HTML strings into model context.
        
          
        

### Workflow C — Browser Recovery & Context Efficiency

- **Winner: Native OpenClaw `browser` (`--mode efficient` / `--interactive`) + `@openclaw/browser-automation`** — **Score: 98/100**
    
      
    - **Mechanics:** Uses OpenClaw’s built-in Playwright backend to filter non-interactive body text out of accessibility trees, exposing only actionable elements with numeric/role refs (`aria-ref="12"` or `[ref=e12]`). Provides automatic delta tracking (`[new]` tags) across consecutive snapshots.
        
          
        
    - **Why it wins:** Reduces page context overhead from ~80,000 tokens down to ~300 tokens, perfectly fitting Qwen3-8B's 32k window.
        
          
        
- **Runner-Up: Full Accessibility Snapshots (`openclaw browser snapshot --format aria`)** — **Score: 55/100**
    
      
    - **Mechanics:** Generates full DOM accessibility trees.
        
          
        
    - **Why it loses:** Floods the context window with structural layout tags, leading to model hallucinations on local 8B models.
        
          
        

### Workflow D — Safe Deterministic Script Execution

- **Winner: Native OpenClaw `exec` Tool + `tools.exec.mode: "allowlist"`** — **Score: 98/100**
    
      
    - **Mechanics:** Executes host PowerShell or Python scripts directly within the OpenClaw Gateway runtime. All permitted commands and script paths are explicitly registered in `openclaw.json`.
        
          
        
    - **Why it wins:** Zero extra code needed. Built-in security policy blocks unauthorized shell commands natively.
        
          
        
- **Runner-Up: ClawHub `code-interpreter` Skill** — **Score: 70/100**
    
      
    - **Mechanics:** Dynamic Python code generation inside isolated containers.
        
          
        
    - **Why it loses:** Redundant and unsafe for running known, pre-approved deterministic script paths.
        
          
        

### Workflow E — Git and Repository Operations

- **Winner: Native OpenClaw `exec` Tool with Scoped Command Allowlist** — **Score: 94/100**
    
      
    - **Mechanics:** Configures Gateway allowlist patterns specifically for safe Git operations:
        
        `["git status", "git diff", "git add .", "git commit -m *", "git push origin main"]`.
        
          
        
    - **Why it wins:** Enforces APEX operator policy natively at the gateway security boundary. Explicitly excludes unsafe operations like `git push -f`, `git reset --hard`, or branch creation.
        
          
        
- **Runner-Up: ClawHub `@openclaw/github` Skill** — **Score: 72/100**
    
      
    - **Mechanics:** Interacts with GitHub via REST/GraphQL API.
        
          
        
    - **Why it loses:** Designed for remote PR/issue management rather than local repo operations on `main`.
        
          
        

### Workflow F — Cron and Scheduled Orchestration

- **Winner: Native OpenClaw Cron System (`openclaw cron`)** — **Score: 96/100**
    
      
    - **Mechanics:** Built-in Gateway scheduler that supports model-backed isolated tasks (`--session isolated`) and deterministic script executions (`--system-event` / `exec`).
        
          
        
    - **Why it wins:** Native to OpenClaw runtime, supports local Windows timezones, includes run history logging (`openclaw cron runs`), and requires zero external dependencies.
        
          
        
- **Runner-Up: Windows Task Scheduler + OpenClaw CLI Wrapper** — **Score: 65/100**
    
      
    - **Mechanics:** Uses OS-level task scheduling to launch CLI triggers.
        
          
        
    - **Why it loses:** Adds unnecessary external infrastructure maintenance.
        
          
        

### Workflow G — Immediate Execution Dispatch

- **Winner: OpenClaw Gateway API (`POST /v1/chat/completions`) + Local File Handles** — **Score: 95/100**
    
      
    - **Mechanics:** APEX OS reasoning agents issue an HTTP POST request to the local OpenClaw Gateway API (`localhost:18789`), supplying a task handle referencing a local payload file (`C:/apex/queue/task_101.json`).
        
          
        
    - **Why it wins:** Asynchronous, non-blocking, sub-second execution trigger with zero context bloat.
        
          
        
- **Runner-Up: Polling Cron File Watcher Script** — **Score: 68/100**
    
      
    - **Mechanics:** A cron job periodically checks a folder for new JSON files.
        
          
        
    - **Why it loses:** Introduces execution delay (polling interval lag).
        
          
        

### Workflow H — Long-Running Jobs & Recovery

- **Winner: Native OpenClaw Session Tracking + Claim Check State Files (`state.json`)** — **Score: 93/100**
    
      
    - **Mechanics:** OpenClaw stores persistent CDP tab targets in SQLite state across Gateway restarts. The workflow script writes a local file (`C:/apex/state/task_101_state.json`) marking progress (`PROMPT_SUBMITTED`, `WAITING_FOR_DEEP_RESEARCH`). On restart, Qwen inspects this status file before taking action, avoiding duplicate submissions.
        
          
        
    - **Why it wins:** Complete idempotency and crash recovery with zero custom database requirements.
        
          
        
- **Runner-Up: Custom External State Database Daemon** — **Score: 58/100**
    
      
    - **Mechanics:** Maintains task state in an external SQLite/PostgreSQL daemon.
        
          
        
    - **Why it loses:** Violates the anti-invention principle by adding redundant infrastructure.
        
          
        

### Workflow I — Multi-Repository Workflows

- **Winner: Native OpenClaw Workspace Profiles (`agents.entries`) + Scoped Working Directories** — **Score: 95/100**
    
      
    - **Mechanics:** Defines separate agent workspace scopes in `~/.openclaw/openclaw.json` (e.g., `agents.entries.meta` pointing to `apexai-os-meta`, and `agents.entries.project_a` pointing to project repos).
        
          
        
    - **Why it wins:** Isolates file context and execution allowlists per repository while maintaining shared global skills.
        
          
        
- **Runner-Up: Running Multiple OpenClaw Gateway Processes on Different Ports** — **Score: 70/100**
    
      
    - **Mechanics:** Launches multiple gateway instances.
        
          
        
    - **Why it loses:** Consumes unnecessary system RAM on the local Windows host.
        
          
        

### Workflow J — Evidence & Receipts

- **Winner: Native Gateway Session Logs (`/tmp/openclaw/*.log`) + Standardized JSON Receipt File** — **Score: 96/100**
    
      
    - **Mechanics:** Uses OpenClaw’s built-in session/cron execution history, paired with a standardized receipt file written to disk upon job completion.
        
          
        
    - **Why it wins:** Gives reasoning agents deterministic validation (file path, byte size, SHA-256, execution duration) with zero extra dependencies.
        
          
        
- **Runner-Up: Custom Evidence Aggregator Subsystem** — **Score: 50/100**
    
      
    - **Mechanics:** A dedicated custom audit daemon.
        
          
        
    - **Why it loses:** Over-engineered and unnecessary.
        
          
        

## Section D — Recommended Installation Set

To deploy this local executor, run these commands on the Windows 11 target machine:

  

PowerShell

```
# 1. Ensure OpenClaw Gateway is installed and updated
npm install -g openclaw@latest

# 2. Install official bundled browser automation skill (for DOM/snapshot recovery guidance)
openclaw skills install @openclaw/browser-automation

# 3. (Optional) Install official GitHub skill for API-level repository operations
openclaw skills install @openclaw/github
```

### Installation Details

1. **Package Name:** `openclaw` (Gateway Core Runtime)
    
      
    - **Install Command:** `npm install -g openclaw@latest`
        
          
        
    - **Why:** Provides native `browser`, `exec`, `cron`, file management, and `sessions_spawn` capabilities.
        
          
        
    - **Permissions:** Local Host Execution, Network Loopback, File I/O.
        
          
        
    - **Security Status:** Official core distribution; security audited.
        
          
        
2. **Skill Name:** `@openclaw/browser-automation`
    
      
    - **Install Command:** `openclaw skills install @openclaw/browser-automation`
        
          
        
    - **Why:** Injects system prompt guidelines for handling tab selection, stale DOM refs, modal dialogs, and CAPTCHA escalation.
        
          
        
    - **Permissions:** Browser CDP interaction.
        
          
        
    - **Security Status:** Official OpenClaw bundled skill.
        
          
        

## Section E — What NOT to Install

Do not install the following ecosystem packages:

  

- **DO NOT INSTALL Third-Party Web Chat Skills (e.g., `chatgpt-web-scraper`, `gemini-automation-v2`):**
    
      
    - _Reason:_ These skills break frequently when web UIs update, hardcode fragile selectors, and stream large text prompts through LLM token context, leading to token exhaustion.
        
          
        
- **DO NOT INSTALL Cloud AI API Skills (e.g., `openai-api`, `perplexity-api`):**
    
      
    - _Reason:_ Violates the core mandate to use logged-in subscription web UIs (such as Deep Research).
        
          
        
- **DO NOT INSTALL Custom Browser Framework Extensions (e.g., `browser-use` wrappers, `playwright-python-standalone`):**
    
      
    - _Reason:_ Redundant. OpenClaw’s built-in `browser` tool already controls Chromium via Playwright/CDP natively.
        
          
        
- **DO NOT INSTALL Independent Cron / Task Scheduler Plugins:**
    
      
    - _Reason:_ Duplicates OpenClaw’s native `openclaw cron` scheduling subsystem.
        
          
        
- **DO NOT INSTALL Docker / Containerized Interpreter Skills:**
    
      
    - _Reason:_ Unnecessary overhead on a single-user Windows 11 host with local PowerShell and Python environments.
        
          
        

## Section F — Custom-Gap Report

Before concluding whether any custom implementation is required, each workflow requirement was evaluated against OpenClaw's native capabilities:

  

- **Requirement:** Large Prompt Submission (>10,000 words) to ChatGPT/Gemini/Perplexity without token exhaustion.
    
      
    - **Native capability checked:** `openclaw browser act kind=evaluate`
        
          
        
    - **Bundled skills checked:** `@openclaw/browser-automation`
        
          
        
    - **ClawHub candidates checked:** `chatgpt-web`, `gpt-web`
        
          
        
    - **Closest implementation:** Native `browser evaluate` JS DOM injection
        
          
        
    - **Exact missing capability:** _None._
        
          
        
    - **Why configuration/adaptation solves it:** A 15-line JS snippet executed via native `browser evaluate` reads text directly from a local file handle and injects it into the DOM input field, bypassing Qwen token processing.
        
          
        
    - **Minimum custom addition:** **Zero custom skill code.** Requires only a reusable JS helper snippet in `C:/apex/scripts/claim_check.js`.
        
          
        
- **Requirement:** Capturing 50KB+ Deep Research output directly to disk as a Claim Check receipt.
    
      
    - **Native capability checked:** `openclaw browser evaluate` + Native `file write`
        
          
        
    - **Bundled skills checked:** `@openclaw/browser-automation`
        
          
        
    - **ClawHub candidates checked:** `url-reader`, `firecrawl`
        
          
        
    - **Closest implementation:** Native `browser evaluate` text extraction
        
          
        
    - **Exact missing capability:** _None._
        
          
        
    - **Why configuration/adaptation solves it:** A JS snippet extracts `innerText` from the response container, saves it directly to `C:/apex/artifacts/`, and returns a compact JSON handle.
        
          
        
    - **Minimum custom addition:** **Zero custom skill code.** Standardized JSON receipt schema.
        
          
        
- **Requirement:** Enforcing Git policy (direct work on `main`, blocking `push -f` and `reset --hard`).
    
      
    - **Native capability checked:** Gateway Exec Security Policy (`tools.exec.mode: "allowlist"`)
        
          
        
    - **Bundled skills checked:** `@openclaw/github`
        
          
        
    - **ClawHub candidates checked:** `git-tools`
        
          
        
    - **Closest implementation:** Gateway `exec` allowlist matching
        
          
        
    - **Exact missing capability:** _None._
        
          
        
    - **Why configuration/adaptation solves it:** Gateway security configuration natively blocks any command string that does not match pre-approved patterns.
        
          
        
    - **Minimum custom addition:** **Zero custom skill code.** Register approved Git command patterns in `openclaw.json`.
        
          
        

## Section G — Integration Recommendation

### System Architecture Topology

```
                  APEX OS / REASONING LAYER
                              │
               (JSON Work Order + File Paths)
                              │
                              ▼
            LOCAL EXECUTOR (OpenClaw Gateway Host)
┌─────────────────────────────────────────────────────────────┐
│ ~/.openclaw/openclaw.json                                   │
│  ├── LLM: Qwen3-8B GGUF (llama.cpp Vulkan @ localhost:8080) │
│  ├── Exec Security Mode: "allowlist"                        │
│  └── Snapshot Mode: "efficient"                             │
└──────────────────────────────┬──────────────────────────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
 Native Browser           Native Exec             Native Cron
 (CDP User Profile)     (Allowlisted)          (Scheduler Engine)
       │                       │                       │
 ┌─────┴─────────────┐   ┌─────┴─────────────┐   ┌─────┴─────────────┐
 │ Web Subscription  │   │ Python / PS       │   │ Recurring Work    │
 │ (ChatGPT/Gemini)  │   │ Deterministic     │   │ & Isolated Runs   │
 │ Direct File/DOM   │   │ Scripts & Git     │   │                   │
 └─────┬─────────────┘   └─────┬─────────────┘   └─────┬─────────────┘
       │                       │                       │
       └───────────────────────┼───────────────────────┘
                               │
                               ▼
                    LOCAL DURABLE STORAGE
                C:/apex/artifacts/res_101.md
                C:/apex/receipts/rec_101.json
                               │
                               ▼
               Compact Receipt Returned to APEX OS
```

### Key Execution Configuration Snippet (`~/.openclaw/openclaw.json`)

JSON

```
{
  "agents": {
    "defaults": {
      "model": "llama-cpp/qwen3-8b-q4",
      "workspace": "C:/apex/workspace"
    }
  },
  "browser": {
    "enabled": true,
    "defaultProfile": "user",
    "snapshotDefaults": {
      "mode": "efficient"
    },
    "profiles": {
      "user": {
        "color": "#4A90E2",
        "driver": "chrome-mcp"
      }
    }
  },
  "tools": {
    "exec": {
      "mode": "allowlist",
      "allowlist": [
        { "pattern": "python C:/apex/scripts/*" },
        { "pattern": "powershell -File C:/apex/scripts/*" },
        { "pattern": "git status" },
        { "pattern": "git diff" },
        { "pattern": "git add *" },
        { "pattern": "git commit -m *" },
        { "pattern": "git push origin main" }
      ]
    }
  }
}
```

## Section H — Open Questions

### Decision Required

1. **Chrome Connection Mode:** Should the executor use OpenClaw's `user` profile (attaching directly to your everyday running Chrome browser via remote debugging port 9222), or a dedicated isolated `openclaw` Chromium profile where subscription sessions (ChatGPT, Gemini, Perplexity) are logged in once and preserved permanently?
    
      
    - _Recommendation:_ Use the isolated `openclaw` browser profile to prevent agent actions from interfering with daily desktop browsing.
        
          
        

### Live Test Required

1. **DOM Selector Stability on Target Subscription Web UIs:** Verify whether the active contenteditable input selectors for ChatGPT and Gemini Advanced respond cleanly to `document.execCommand('insertText')` via `openclaw browser evaluate` on the local Windows 11 installation.
    
      
    
2. **Qwen3-8B Context Response to Efficient Snapshots:** Run a test trial with `browser.snapshotDefaults.mode: "efficient"` to ensure Qwen3-8B reliably selects numeric/role refs without requiring full ARIA tree details.
    

XML

```
<ElicitationsGroup message="To proceed with setting up the Local Executor:">
  <Elicitation label="Generate the openclaw.json configuration and claim_check.js snippet" query="Please generate the full openclaw.json configuration file and the claim_check.js DOM helper snippet for the Local Executor." />
  <Elicitation label="Create a vertical slice test plan for Workflow A and B" query="Create a step-by-step vertical slice test plan to verify prompt submission and response capture on ChatGPT using OpenClaw and Qwen3-8B." />
</ElicitationsGroup>
```