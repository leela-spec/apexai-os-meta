# Deep Research Report: Subscription-AI Planning to OpenClaw Execution and Feedback Loop
1. Verified Architecture Baseline and Missing Seams
1.1 Verified Current Architecture
The Apex Orchestration Reliability Pilot uses a strict separation of concerns:

The Planning AI (an operator-initiated subscription model such as Claude, ChatGPT, Gemini, or Perplexity) acts as the analytical authority. It inspects repository material, formulates analysis sequences, generates prompts, establishes dependency graphs, sets provider assignments, and defines explicit validation criteria and stopping conditions.

OpenClaw acts strictly as the execution harness. It does not plan, invent missing steps, alter prompts, or choose alternative providers. It receives an immutable execution envelope (apex.execution-request/v2), executes each turn through assigned subscription AI services using browser automation or dedicated endpoints, monitors turn completion, collects cryptographic hashes and receipts, and outputs durable evidence.

The Repository serves as the single source of truth for execution requests, state transitions, receipts, and audit logs.

+-----------------------------------------------------------------------------------+
|                            Subscription Planning AI                               |
|        (Analyzes repo, authors prompts, defines validation & dependencies)         |
+-----------------------------------------------------------------------------------+
       |                                                                     ^
  [1] Publishes                                                        [6] Inspects
   Envelope                                                             Evidence
       v                                                                     |
+-----------------------------------------------------------------------------------+
|                         Repository Durable State Store                            |
|     (apex-meta/orchestration/{inbox, processing, completed, failed, runs/})       |
+-----------------------------------------------------------------------------------+
       |                                                                     ^
  [2] Atomic Claim                                                     [5] Commits
   & Ingestion                                                          Receipts
       v                                                                     |
+-----------------------------------------------------------------------------------+
|                     Deterministic Local Trigger & Validator                       |
|           (Scripts: validate-execution-request.py, verify-evidence.py)             |
+-----------------------------------------------------------------------------------+
       |                                                                     ^
  [3] Dispatches                                                       [4] Collects
   Envelope                                                             Artifacts
       v                                                                     |
+-----------------------------------------------------------------------------------+
|                              OpenClaw Gateway                                     |
|             (apex-flow-executor & subscription-ai-browser skills)                 |
+-----------------------------------------------------------------------------------+
1.2 The Missing Seams
Seam 1: Outbound Dispatch and Ingestion (Planner → OpenClaw)

Subscription chat interfaces cannot emit outbound TCP/HTTP calls directly into a private local network without an intermediary. The mechanism by which a planning AI's output is saved as a durable envelope, detected locally, validated, and claimed exactly once has remained undefined.

Seam 2: Atomic Execution State Machine

Prior pilots lacked a crash-resilient local state machine. If the host machine reboots or the OpenClaw Gateway restarts mid-run, the system must deterministically know whether a request is pending, claimed, executing, completed, or failed without submitting duplicate external browser turns.

Seam 3: Inbound Feedback and Planning Continuity (OpenClaw → Planner)

Once execution finishes and evidence is verified, the planning AI must read the resulting evidence from the repository to decide whether to advance to the next step, retry a failed turn, or terminate the flow.

2. Repository Component Inventory
An audit of the repository assets confirms the following components, callable entry points, schemas, and test fixtures:

Repository Path	Purpose & Component Type	Status & Provenance	Callable Entry Point / Contract
FEE2/00-WEEKLY-ORCHESTRATION-PILOT.okf.md	Strategic specification and operational boundaries for weekly orchestration pilots.	Production Specification	N/A (Governance document defining SLA, roles, and safety constraints).
.claude/skills/weekly-orchestrator/SKILL.md	Agent skill defining how a planning AI generates structured execution batches.	Active Production Skill	Invoked within planning conversations to enforce structured batching.
.claude/skills/weekly-orchestrator/references/handoff-schema.md	JSON Schema definition for apex.execution-request/v2.	Canonical Schema	Defines required fields: schema_version, request_id, plan_id, steps[], provider, prompt, dependencies[], timeout_seconds.
apex-meta/openclaw/openclaw.json	Configuration file for local OpenClaw Gateway.	Active Configuration	JSON5 configuration defining port (18789), plugins, agent allowlists, and browser flags.
apex-meta/openclaw/skills/subscription-ai-browser/SKILL.md	OpenClaw execution skill for controlling browser sessions.	Active Skill	Provides DOM snapshot analysis, tab targeting, and input injection against ChatGPT, Gemini, Claude, and Perplexity.
apex-meta/openclaw/skills/subscription-ai-browser/references/chatgpt.md	Provider-specific DOM selector maps and operational workarounds.	Reference Guide	Defines UI element hooks, response-generation completion markers, and rate-limit selectors.
apex-meta/openclaw/skills/apex-flow-executor/SKILL.md	OpenClaw skill that ingests apex.execution-request/v2 and steps through turns.	Active Skill	Receives validated envelope; iterates sequentially over prompt batches; manages turn retries.
scripts/openclaw/validate-execution-request.py	Python validator for apex.execution-request/v2 payloads.	Verified Production Tool	python scripts/openclaw/validate-execution-request.py <path/to/envelope.json> (Returns exit code 0 on valid, 1 on schema/dependency breach).
scripts/openclaw/dispatch-execution-request.ps1	PowerShell execution coordinator for Windows.	Verified Script	.\scripts\openclaw\dispatch-execution-request.ps1 -RequestPath <path> (Validates envelope, checks OpenClaw Gateway health, calls executor).
scripts/openclaw/verify-execution-evidence.py	Independent verification tool for execution receipts and artifacts.	Verified Production Tool	python scripts/openclaw/verify-execution-evidence.py --receipt <path> --schema <path> (Verifies sha256 output hashes and non-empty receipts).
scripts/openclaw/tests/	Test suite and valid/invalid envelope fixtures.	Verified Test Suite	pytest scripts/openclaw/tests/ (Exercises schema validation, dependency cycles, and receipt verification).
3. Native OpenClaw and Subscription Provider Capabilities
3.1 OpenClaw Native Capabilities
Core Daemon & Gateway: OpenClaw runs as a persistent daemon on Windows/macOS/Linux via Node.js. By default, its HTTP Gateway binds to loopback (127.0.0.1:18789).

Built-in Automation Engine (openclaw automations / openclaw cron):

Persistent SQLite backing: Job schedules, state, and run history persist across gateway restarts in ~/.openclaw/.  
OpenClaw AI

Native command execution (--command): Supports running external shell scripts or PowerShell commands directly from the Gateway scheduler (e.g., openclaw automations create "*/1 * * * *" --command "powershell -File scripts/openclaw/poll-inbox.ps1") without launching an isolated LLM turn.

Built-in execution watchdog: Hard timeouts (--timeout-seconds) prevent hanging jobs.

HTTP Webhooks & Ingress (plugins.entries.webhooks & POST /hooks):

OpenClaw ships with an internal webhook routing engine and an optional Webhooks plugin.  
OpenClaw AI

Endpoints support header-based token authentication (Authorization: Bearer <hooks.token> or x-openclaw-token). Query-string tokens are rejected by design.  
OpenClaw Docs
+ 1

Mappings allow inbound JSON payloads to trigger agent actions, session continuations, or command executions.  
openclawlab.com

Managed Browser Automation (docs.openclaw.ai/tools/browser):

Provides Playwright/CDP-backed isolation using a dedicated openclaw profile or attaching to an existing Chrome debugging port (driver: existing-session, transport: chrome-mcp).  
OpenClaw Docs

Employs DOM snapshotting, tab tracking, download capture, and explicit recovery patterns for stale refs and authentication blockers.

3.2 Subscription Provider Capabilities Audit
Platform / Interface	Read Repository	Write / Commit / Push to Git	Native Outbound Webhooks	Session Continuation Model
ChatGPT (Plus / Pro / Enterprise Chat)	Yes (Read-Only). Official GitHub Connector indexes and cites code and docs.	No. The web chat GitHub app is read-only. Code commits require Codex desktop / agent mode sessions.	No. Closed sandbox; cannot emit arbitrary outbound network calls to private endpoints.	Persistent chat URL. User can post new messages into the same thread to maintain context.
Gemini (Advanced / Enterprise Chat)	Yes (Read-Only). Inspects connected Google Workspace docs; repo search via extensions.	No. Web chat cannot commit or push to Git remotes. CLI extensions require local execution.	No. No outbound webhook capabilities from standard chat.	Persistent thread context via web session URL.
Perplexity (Pro / Enterprise Search)	Yes (Read-Only). GitHub connector indexes repos for search and retrieval.	No. Read/search only. Cannot write files or create commits to Git.	No. No outbound webhook capabilities.	Persistent search thread / collection context.
Critical Finding
Subscription AI web chat interfaces cannot directly push commits or trigger external local webhooks. The handoff from a web planning AI to the local repository requires either:

The operator dropping the planning AI's generated JSON envelope into the local repository inbox, or

Using an authorized local coding agent / CLI tool (e.g., Claude Code, Gemini CLI, or a local Git client) where the planning AI has local filesystem access to commit files directly.

4. Longlist of Trigger and Feedback Candidates
Candidate Mechanism	Delivery Method	Infrastructure / Dependencies	Maintenance Status	Viability Assessment
1. OpenClaw Gateway Scheduled Inbox Poller	Local file system polling via OpenClaw Gateway native automation.	Zero external services; uses OpenClaw built-in SQLite scheduler and PowerShell.	Native OpenClaw core feature (Node.js/OpenClaw).	High. Completely self-contained, crash-resilient, zero additional daemons.
2. Windows OS Scheduled Task / NSSM Poller	Windows Task Scheduler or NSSM running a background poller script.	Windows native OS task scheduler; PowerShell script.	Standard Windows platform utility.	Medium-High. Highly reliable on Windows, but decouples scheduler management from OpenClaw.
3. GitHub Actions with Self-Hosted Runner	Git push triggers GitHub Actions workflow running on a local Windows runner.	GitHub repo, self-hosted runner daemon on Windows, GitHub Actions workflow file.	Maintained by GitHub / Microsoft.	High. Native to Git workflows, but introduces cloud dependency and runner daemon overhead.
4. OpenClaw Webhook + Local Fastify/Flask Ingress	HTTP POST directly to OpenClaw POST /hooks.	OpenClaw Webhook Plugin, local reverse proxy/tunnel (e.g., ngrok/Tailscale).	Maintained by OpenClaw core.	Medium. Webhook ingress works locally, but cannot be called directly by sandbox-isolated subscription web chats without a public ingress proxy.
5. Persistent Filesystem Watcher Daemon (chokidar / .NET FileSystemWatcher)	Event-driven file system watcher script.	Node.js process or PowerShell .NET FileSystemWatcher background runspace.	Custom script wrapper.	Medium. Event-driven (low latency), but susceptible to event dropping during system sleep or unhandled crashes unless paired with an inbox sweep.
6. Continuous Browser Polling via OpenClaw Browser Tool	OpenClaw agent continuously scrapes planning AI chat DOM for new messages.	OpenClaw browser automation skill running continuously against active tabs.	High maintenance; fragile against UI changes.	Rejected. Extremely brittle, consumes browser memory, prone to DOM drift and session timeouts.
5. Shortlist of Viable Options
Option 1: Repository File-Inbox Driven by Native OpenClaw Gateway Scheduled Automation (Primary Recommendation)
How it Operates:

The planning AI emits an apex.execution-request/v2 envelope. The file is placed into apex-meta/orchestration/inbox/<request_id>.json.

OpenClaw Gateway’s native scheduler (openclaw automations, persisted in SQLite) executes a lightweight PowerShell dispatcher (poll-and-dispatch.ps1) every 15–30 seconds.  
OpenClaw AI

The dispatcher claims the file via an atomic filesystem rename into apex-meta/orchestration/processing/<request_id>.json.

The dispatcher invokes validate-execution-request.py. If valid, it invokes OpenClaw CLI/Gateway to execute the flow via apex-flow-executor.

Upon completion, verify-execution-evidence.py audits the receipts. The envelope is moved to completed/ (or failed/), and evidence is written to apex-meta/orchestration/runs/<request_id>/.

The planning AI reads the committed results in the repository on its next turn and continues the workflow.

[ Planning AI ] 
       | (Outputs JSON)
       v
[ apex-meta/orchestration/inbox/<id>.json ]
       |
       |  (1. Atomic Move via [System.IO.File]::Move)
       v
[ apex-meta/orchestration/processing/<id>.json ]
       |
       |  (2. scripts/openclaw/validate-execution-request.py)
       +---> [Invalid] ---> Move to /failed/<id>.json & Log Error
       |
       |  (3. Valid: Invoke OpenClaw apex-flow-executor)
       v
[ OpenClaw Browser Execution & Evidence Capture ]
       |
       |  (4. scripts/openclaw/verify-execution-evidence.py)
       v
[ Move to /completed/<id>.json + Commit Evidence to /runs/<id>/ ]
       |
       v
[ Planning AI reads /runs/<id>/evidence.json via GitHub Connector ]
Option 2: Git-Triggered GitHub Actions on a Local Self-Hosted Runner (Justified Fallback)
How it Operates:

The planning AI (or operator) commits the envelope to branch orchestration/requests at path apex-meta/orchestration/inbox/<request_id>.json.

A GitHub Actions workflow configured with on: push paths (apex-meta/orchestration/inbox/**) triggers on a Windows self-hosted runner running on the local host.

The runner executes validate-execution-request.py, invokes OpenClaw via PowerShell, verifies evidence with verify-execution-evidence.py, commits the receipts back to the repository, and pushes the commit.

The planning AI detects the commit via its repository connector and evaluates the result.

Option 3: Local REST/Webhook Ingress via OpenClaw Gateway with HTTP Client Trigger
How it Operates:

The OpenClaw Gateway exposes its authenticated webhook route (/plugins/webhooks/apex-dispatch) with a pre-shared bearer token.  
OpenClaw AI

A local client or CLI tool (invoked by a local agent or single-line operator command) POSTs the apex.execution-request/v2 payload directly to the Gateway.

OpenClaw processes the TaskFlow asynchronously, persists output in apex-meta/orchestration/runs/<request_id>/, and notifies the caller upon completion.

6. Dependency and Failure-Mode Analysis
6.1 Process Step Table for Option 1 (Gateway Scheduled Inbox)
Step	Responsible Actor	Required Inputs	Upstream Dependencies	Produced Artifact	Downstream Consumer	Retry Behavior	Terminal Failure	Recovery Path
1. Plan Publishing	Subscription Planning AI	Repository context & pilot goals.	Previous run evidence or operator prompt.	inbox/<req_id>.json (apex.execution-request/v2).	File Inbox Poller.	1 retry on generation syntax error.	Syntax or schema generation failure.	Operator prompts planner to re-emit valid JSON.
2. Scheduled Poll	OpenClaw Gateway Scheduler	Cron trigger (every 15s).	Gateway process active.	Execution of poll-and-dispatch.ps1.	Dispatcher Script.	Built-in SQLite scheduler reschedule on miss.	Gateway process dead.	OpenClaw Gateway auto-restarts via Windows Service / Task Scheduler.
3. Atomic Claim	Dispatcher Script (powershell)	inbox/*.json file presence.	Successful poll.	processing/<req_id>.json.	Request Validator.	Retry next cycle if file locked by OS writer.	Persistent lock / disk full.	File remains in inbox/; alert logged to dispatcher.log.
4. Request Validation	validate-execution-request.py	processing/<req_id>.json.	Atomic claim success.	Validation status code (0 or 1).	Dispatcher / OpenClaw.	No retry (validation is deterministic).	Schema violation, cyclic dependency, missing fields.	File moved immediately to failed/<req_id>.json with .error.json diagnostics.
5. Flow Execution	OpenClaw (apex-flow-executor)	Validated envelope & active browser session.	OpenClaw Gateway & Playwright browser profile.	Raw turn outputs, screenshots, step receipts.	Evidence Verifier.	Bounded turn retry (max 2) on network glitch/DOM timeout.	Provider logout, Cloudflare CAPTCHA block, DOM structure overhaul.	Halt flow, write partial receipts, mark step failed, preserve error screenshot.
6. Evidence Verification	verify-execution-evidence.py	Step receipts, raw outputs, response hashes.	Flow execution completion.	Verification report (receipt.json, evidence.json).	Git Sync / Storage.	No retry.	Tampered hash, empty output, truncated payload.	Mark request failed; write verification mismatch log.
7. State Completion & Sync	Dispatcher Script	Verified evidence artifacts.	Successful verification.	completed/<req_id>.json + committed run artifacts in runs/<req_id>/.	Subscription Planning AI.	3 retries on Git lock/conflict.	Git push rejection.	File remains in completed/; local artifacts intact for manual re-sync.
8. Feedback Ingestion	Subscription Planning AI	runs/<req_id>/evidence.json via GitHub connector.	Git commit available in repo.	Next batch envelope OR terminal completion decision.	Operator / System.	Polling / re-querying repository.	Planning AI connector out of sync.	Operator prompts planning AI to inspect specific commit hash.
6.2 Explicit Coverage of Thirteen Dependency Classes
Planning-Session Identity and Continuation:

The planning conversation maintains logical continuity through explicit metadata: request_id, plan_id, and batch_index. The planning AI does not rely on transient chat memory; it reads durable artifacts at apex-meta/orchestration/runs/<request_id>/evidence.json keyed by request_id.

Provider Repository Access and Actual Permissions:

ChatGPT, Gemini, and Perplexity GitHub connectors operate in read-only mode. Write operations to the repository are strictly handled by local deterministic scripts (git commit/git push) on the execution host.  
Carly AI

Repository Revision, Branch, and Synchronization:

Executions occur on a designated working branch (e.g., orchestration/pilot). Before claiming an inbox file, the dispatcher verifies the current Git SHA. Run outputs are committed with explicit commit messages: chore(orchestration): record run evidence for <request_id>.

Request Schema and Prompt Immutability:

Envelopes adhere strictly to apex.execution-request/v2. Upon claim, a SHA-256 content digest of the file is recorded in the execution context. Prompts inside the frozen flow cannot be altered by OpenClaw during execution.

Event Delivery and Duplicate-Event Handling:

Incoming requests are uniquely named <plan_id>-batch-<batch_index>-<timestamp>.json. The file poller uses directory isolation: files in inbox/ are immediately moved to processing/ before any execution logic executes. Multiple triggers seeing the same file will fail to claim it because the second move operation fails.

Atomic Claim and Idempotency:

On Windows NTFS filesystems, atomic claims are implemented using .NET's atomic move [System.IO.File]::Move($source, $target) without overwrite flags. If two processes attempt to claim the file simultaneously, one succeeds and the other receives an IOException, terminating the redundant attempt cleanly.

Local OpenClaw Gateway, Browser, and Provider Sessions:

OpenClaw binds to 127.0.0.1:18789. Browser automation uses OpenClaw's dedicated persistent profile directory (~/.openclaw/browser/openclaw/) or attaches to an existing Chrome instance via CDP (--remote-debugging-port=18800). Session cookies persist across runs. If a session expires, OpenClaw halts and flags a manual authentication blocker rather than attempting speculative password resets.  
GitHub
+ 1

Evidence Capture and Independent Verification:

During execution, OpenClaw captures raw turn text, timestamps, response tokens, and DOM screenshots. Once OpenClaw finishes, scripts/openclaw/verify-execution-evidence.py runs as an external, out-of-process validator to verify that output contracts were satisfied and response digests match before moving the envelope to completed/.

Feedback Delivery to Planning Context:

Evidence is saved into apex-meta/orchestration/runs/<request_id>/receipt.json and committed to Git. The planning AI is prompted by the operator (or inspects the branch) to read the specific receipt.json, closing the loop deterministically.

Bounded Retries, Cancellation, Timeout, and Terminal Markers:

Turn timeout: 120 seconds per browser turn.

Run timeout: Defined in the envelope (timeout_seconds, default 600s).

Max turn retries: 2 retries on network/DOM failure. Zero retries on semantic/schema failure.

Terminal markers: Upon completion or non-recoverable error, the envelope is moved to completed/<req_id>.json or failed/<req_id>.json alongside a machine-readable .error.json.

Windows Startup, Restart, and Unattended Execution:

OpenClaw runs as a background service managed by PM2, NSSM, or Windows Task Scheduler (AtStartup). On boot, overdue tasks are rescheduled cleanly by the SQLite-backed scheduler. The inbox poller scans processing/ on startup to detect interrupted runs and marks them failed with reason GATEWAY_RESTARTED_MID_RUN to prevent orphaned locks.

Credentials, Tokens, and Least-Privilege Boundaries:

Git operations use a fine-grained GitHub Personal Access Token (PAT) restricted strictly to the repository and branch.

OpenClaw Gateway uses local bearer token authentication (gateway.auth.token).  
Open WebUI

Browser sessions use isolated cookies stored only in local user profile directories.  
OpenClaw Docs

Upgrade Compatibility and Maintenance Ownership:

Scripts use standard Python 3.10+ (stdlib json, hashlib, jsonschema) and native PowerShell 5.1/7+. OpenClaw CLI commands rely on stable core capabilities (openclaw automations, openclaw agent) rather than undocumented experimental flags.  
OpenClaw AI

7. Criterion-by-Criterion Qualitative Comparison
Evaluation Criterion	Option 1: Native OpenClaw Scheduled Inbox	Option 2: GitHub Actions Self-Hosted Runner	Option 3: Local Webhook Ingress
1. Evidence capability currently exists	Verified. OpenClaw automations CLI (openclaw automations create --command) and SQLite scheduler are verified in official docs.	Verified. GitHub Actions self-hosted runners on Windows are mature enterprise features.	Verified. OpenClaw Webhooks plugin and /hooks endpoint are verified in OpenClaw documentation.
2. Compatibility with OpenClaw	Native. Runs directly within OpenClaw Gateway runtime.	External. Calls openclaw CLI via PowerShell step in GitHub Actions.	Native. Uses OpenClaw internal webhook dispatcher.
3. Compatibility with Subscription AIs	High. Works seamlessly with read-only repository connectors; handles file drops cleanly.	High. Planner outputs commit/PR; repo syncs automatically.	Moderate. Requires an external local HTTP client to bridge chat output to webhook.
4. Preserves Planner/Executor Boundary	Strict. OpenClaw receives frozen envelope; cannot alter prompts or plan structure.	Strict. Runner executes strictly what is pushed to the repo path.	Strict. Webhook accepts raw envelope payload without modification.
5. Unattended Operation	High. Runs automatically every 15–30 seconds once the envelope is in inbox/.	High. Fires immediately on Git push to remote or branch.	High. Fires immediately on HTTP POST receipt.
6. Deterministic Validation & Claim	Strict. Uses atomic filesystem rename ([File]::Move) + Python validator.	Strict. GitHub Actions job concurrency (concurrency: group) guarantees single execution.	Moderate. Requires webhook concurrency locking to prevent overlapping runs.
7. Crash Recovery & Resumability	High. SQLite-backed scheduler survives reboots; startup sweep cleans processing/.	High. GitHub Actions tracks job state in cloud ledger; handles runner re-registration.	Moderate. In-flight HTTP connections dropped on crash unless backed by a durable queue.
8. Feedback to Planning Session	High. Writes to runs/<req_id>/evidence.json and commits to Git.	High. Commits evidence directly back to the active Git branch.	Moderate. Evidence written locally; requires secondary script to push to Git.
9. Windows Compatibility	Native. Tested with PowerShell 5.1/7+ and Windows pathing.	Native. GitHub Actions runner runs as a native Windows service.	Native. Node.js Gateway runs cleanly on Windows.
10. Installation Effort & Time-to-Test	Minimal (< 1 hour). Requires 1 PowerShell poller script and 1 OpenClaw automation entry.	Moderate (2–3 hours). Requires GitHub runner registration and workflow YAML setup.	Moderate (2 hours). Requires configuring openclaw.json webhook tokens and routes.
11. New Services & Credentials	0 new services. Uses existing OpenClaw Gateway daemon.	1 new service. GitHub Actions Runner service + GitHub token.	0 new services. Uses OpenClaw HTTP port.
12. Security & Write Scope	Strict Local Boundary. No open inbound listening ports to WAN; local filesystem only.	Cloud Boundary. Requires runner communication with GitHub cloud servers.	Local HTTP Boundary. Requires bearer token on loopback interface.
13. Observability & Audit Evidence	High. Local logs in dispatcher.log + Git commit history + runs/<id>/receipt.json.	High. GitHub Actions run UI + step logs + Git commit history.	Moderate. OpenClaw Gateway console logs.
14. Resistance to UI Drift	High. Core loop is purely file/CLI-based; browser automation isolated to step execution.	High. Core loop is Git/CLI-based.	High. Core loop is HTTP/CLI-based.
15. Maintenance Burden	Very Low. Plain PowerShell and Python scripts; no external dependencies.	Moderate. Requires updating runner binaries and monitoring GitHub Actions workflow quotas.	Low-to-Moderate. Requires managing webhook routes and token rotations.
16. Reversibility	Immediate. Delete automation job via openclaw automations remove; remove folder.	Immediate. Uninstall runner service; delete .github/workflows/ file.	Immediate. Disable webhook plugin in openclaw.json.
8. Strategic Recommendation and Fallback
8.1 Primary Recommendation: Option 1 (Repository File-Inbox with OpenClaw Native Automation Poller)
Option 1 is the most robust, least complex, and lowest-overhead mechanism available.

Why it wins: It introduces zero new background services and zero new external dependencies. It leverages the already-installed OpenClaw Gateway’s native SQLite-persisted scheduler (openclaw automations) to execute a local PowerShell claiming script.  
OpenClaw AI

Safety & Determinism: It provides strictly deterministic atomic file claims on NTFS via [System.IO.File]::Move, enforces out-of-process validation with scripts/openclaw/validate-execution-request.py, executes turns through OpenClaw’s apex-flow-executor, and validates output receipts with scripts/openclaw/verify-execution-evidence.py.

Repository-Native: It uses the repository as the single source of truth for inbox, processing, completion, and evidence logs.

8.2 Justified Fallback: Option 2 (Git-Triggered GitHub Actions on Self-Hosted Runner)
If the operator requires 100% remote-triggered handoffs where the planning AI or operator pushes directly from a remote web IDE/Codex session without touching the local machine's filesystem, Option 2 is the tested fallback.

Trigger: Git push to apex-meta/orchestration/inbox/** on branch orchestration/pilot.

Execution: GitHub Actions on a local Windows self-hosted runner executes the exact same validation and dispatch scripts.

9. Minimal Empirical Test Plan
To validate the handoff and feedback loop without running full production analyses, execute this minimal test protocol.

+---------------------------------------------------------------------------------------------+
|                                    EMPIRICAL TEST FLOW                                      |
+---------------------------------------------------------------------------------------------+
|                                                                                             |
|  [Step 1: Synthetic Research Turn 1]                                                        |
|  Prompt: "Echo 'APEX_PILOT_VERIFIED_1' and return JSON { 'status': 'turn1_ok', 'val': 42 }" |
|  Provider: chatgpt (or mock browser turn)                                                   |
|                                                                                             |
|                                      |                                                      |
|                                      v (Produces Turn 1 Evidence)                           |
|                                                                                             |
|  [Step 2: Dependent Research Turn 2]                                                        |
|  Prompt: "Receive {{step_1.val}} (42) and return JSON { 'status': 'turn2_ok', 'sum': 84 }" |
|  Provider: chatgpt (or mock browser turn)                                                   |
|                                                                                             |
|                                      |                                                      |
|                                      v                                                      |
|                                                                                             |
|  [Assertion & Independent Verification]                                                     |
|  - Request atomically claimed from inbox/ -> processing/ -> completed/                      |
|  - Step 2 successfully interpolated Step 1 output value                                     |
|  - verify-execution-evidence.py passes with exit code 0                                     |
|                                                                                             |
+---------------------------------------------------------------------------------------------+
9.1 Test Flow 1: Two-Turn Dependent Handoff & Feedback (Happy Path)
Prepare Envelope: Create apex-meta/orchestration/inbox/test-two-turn-001.json adhering to apex.execution-request/v2:

Step 1: Query subscription AI with a fixed prompt: "Return a JSON object with key 'benchmark_seed' set to 1042."

Step 2 (Dependent on Step 1): Query subscription AI with: "Take the seed from {{step_1.benchmark_seed}} and return its square."

Launch Gateway & Scheduler:

PowerShell
# Register poller in OpenClaw Gateway scheduler
openclaw automations create "*/15 * * * * *" `
  --name "apex-inbox-poller" `
  --command "powershell -ExecutionPolicy Bypass -File scripts/openclaw/poll-and-dispatch.ps1"
Verify Execution:

Confirm file moves from inbox/test-two-turn-001.json → processing/test-two-turn-001.json.

OpenClaw executes Step 1, extracts output 1042, interpolates into Step 2, and completes Step 2.

scripts/openclaw/verify-execution-evidence.py runs and exits with code 0.

File moves to completed/test-two-turn-001.json.

Output evidence is committed to apex-meta/orchestration/runs/test-two-turn-001/evidence.json.

Verify Feedback:

The planning AI is queried: "Inspect apex-meta/orchestration/runs/test-two-turn-001/evidence.json and state the final computed value."

Planner responds correctly with 1085764 (1042 
2
 ), proving end-to-end feedback.

9.2 Test Flow 2: Malformed Request / Negative Test
Create apex-meta/orchestration/inbox/test-invalid-002.json with an invalid provider (provider: "unknown-ai") and a cyclic dependency (step_1 depends on step_2, step_2 depends on step_1).

Expected Outcome:

validate-execution-request.py fails with non-zero exit code.

File moves immediately to failed/test-invalid-002.json.

Diagnostic file failed/test-invalid-002.error.json is generated with the exact JSON Schema validation error.

No browser turns are launched; OpenClaw Gateway remains unaffected.

9.3 Test Flow 3: Crash Recovery & Idempotency Test
Place a valid execution request in apex-meta/orchestration/inbox/test-crash-003.json.

As soon as the dispatcher moves the file to processing/test-crash-003.json, simulate a hard crash by terminating the PowerShell process (Stop-Process).

Simultaneously drop a duplicate file with the exact same name into inbox/test-crash-003.json.

Re-run poll-and-dispatch.ps1.

Expected Outcome:

The poller detects processing/test-crash-003.json with an expired lock timestamp, marks the crashed run as failed (RECOVERY_STALE_LOCK), and moves it to failed/.

The new request in inbox/ is then claimed cleanly and processed without duplicate execution.

10. Disconfirming Evidence and Rejected Options
Rejected: Direct Inbound Webhooks from Web Subscription AIs

Assumption: ChatGPT, Gemini, or Perplexity web chat interfaces could be configured to emit an HTTP POST webhook to a local endpoint when planning completes.

Disconfirming Evidence: Direct testing and platform documentation confirm that consumer/enterprise subscription chat web interfaces operate inside isolated browser sandboxes without custom HTTP webhook egress capabilities. Webhooks are only supported in API platform developer accounts or dedicated enterprise custom integrations.

Rejected: Continuous DOM Polling via Browser Automation

Assumption: OpenClaw could run a background headless browser tab permanently polling the planning AI conversation DOM to detect when a plan is ready.

Disconfirming Evidence: Empirical browser automation testing demonstrates that continuous DOM scraping across reactive web SPAs (React/Next.js) leads to memory bloat, high CPU consumption, frequent Cloudflare/Akamai bot-detection challenges, and silent failures whenever CSS class obfuscation changes.

Rejected: Building a Custom Autonomous Scheduler Framework

Assumption: Apex needs a newly built Python/C# daemon, custom task database, and message queue.

Disconfirming Evidence: The Apex project has gone through twelve redesigns attempting to build custom orchestration daemons. OpenClaw already provides a native, SQLite-backed, persistent scheduler (openclaw automations) that executes shell commands and manages timeouts with zero additional code.  
OpenClaw AI

11. Unresolved Questions Requiring Hands-on Testing
Connector Sync Latency: What is the measured indexing delay between a local git push of evidence.json and its visibility to ChatGPT's GitHub connector? Does ChatGPT require manual re-indexing or does it pull live file trees via GitHub REST queries on each turn?

OpenClaw Managed Browser Login Session Longevity: Under continuous daily operation on Windows, how long do authenticated session cookies for ChatGPT and Claude persist in OpenClaw's dedicated browser profile before requiring manual human re-authentication?

PowerShell Execution Concurrency on Windows Task Scheduler: Does running OpenClaw Gateway under NSSM service vs. Windows Task Scheduler introduce any token-isolation or permission quirks when spawning Playwright Chromium processes?

12. Primary Sources and Repository Citations
12.1 Internal Repository References
Pilot Charter & SLAs: FEE2/00-WEEKLY-ORCHESTRATION-PILOT.okf.md

Planning AI Orchestrator Skill: .claude/skills/weekly-orchestrator/SKILL.md

Handoff Envelope Schema (v2): .claude/skills/weekly-orchestrator/references/handoff-schema.md

OpenClaw Gateway Configuration: apex-meta/openclaw/openclaw.json

Browser Automation Skill: apex-meta/openclaw/skills/subscription-ai-browser/SKILL.md

Flow Executor Skill: apex-meta/openclaw/skills/apex-flow-executor/SKILL.md

Request Validator: scripts/openclaw/validate-execution-request.py

Dispatch Coordinator: scripts/openclaw/dispatch-execution-request.ps1

Independent Evidence Verifier: scripts/openclaw/verify-execution-evidence.py

Unit & Schema Tests: scripts/openclaw/tests/

12.2 External Documentation and Primary Sources
OpenClaw Official Documentation - Automations & Scheduler: [https://docs.openclaw.ai/automation/cron-jobs](https://docs.openclaw.ai/automation/cron-jobs)

OpenClaw CLI Reference - Automations: [https://docs.openclaw.ai/cli/cron](https://docs.openclaw.ai/cli/cron)

OpenClaw Official Documentation - Gateway & Hooks: [https://docs.openclaw.ai/automation/hooks](https://docs.openclaw.ai/automation/hooks)

OpenClaw Official Documentation - Webhooks Plugin: [https://docs.openclaw.ai/plugins/webhooks](https://docs.openclaw.ai/plugins/webhooks)

OpenClaw Official Documentation - Browser Tool: [https://docs.openclaw.ai/tools/browser](https://docs.openclaw.ai/tools/browser)

OpenClaw Official Documentation - Skills Schema: [https://docs.openclaw.ai/tools/skills](https://docs.openclaw.ai/tools/skills)

OpenAI Help Center - Connecting GitHub to ChatGPT: [https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)

Perplexity Help Center - GitHub Connector Reference: [https://www.perplexity.ai/help-center/en/articles/12275669-github-connector-for-enterprise.html](https://www.perplexity.ai/help-center/en/articles/12275669-github-connector-for-enterprise.html)