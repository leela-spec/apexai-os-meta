---
title: "OpenClaw Local Executor — Installation and Implementation Plan"
doc_type: implementation_plan
initiative: local-executor
created: 2026-08-10
status: ready-for-execution
platform: Windows 11
branch_policy: main-only
depends_on:
  - OPENCLAW-EXECUTOR-DECISION-LOCK-2026-08-10.md
---

# OpenClaw Local Executor — Installation and Implementation Plan

## 0. Goal

Install and configure:

```text
OpenClaw + Qwen3-8B
```

as the persistent **Local Executor** for APEX and project workflows.

The completed executor must be able to:

1. run locally on Windows;
2. use the already-installed Qwen3-8B model;
3. execute OpenClaw skills;
4. operate logged-in subscription-AI browser sessions;
5. run Python, PowerShell and deterministic scripts;
6. read/write approved repository files;
7. stage, commit and push approved Git changes;
8. execute bounded micro-fixes;
9. start work immediately when dispatched;
10. start scheduled work through OpenClaw Automations;
11. return results/evidence to the workflow that invoked it;
12. recover cleanly after restart without silently changing workflow intent.

There is no separate FEE service and no global queue requirement.

---

# 1. Target technical architecture

The **final intended topology** is:

```text
Windows 11
|
+-- OpenClaw Gateway
|     always running
|     Windows Scheduled Task
|
+-- apex-executor agent
|     |
|     +-- Qwen3-8B
|     |     official in-process llama.cpp provider
|     |
|     +-- APEX-owned skills
|     |
|     +-- browser
|     |     Chrome extension
|     |     dedicated APEX Chrome profile
|     |
|     +-- exec/process
|     |     Python
|     |     PowerShell
|     |     trusted scripts
|     |
|     +-- filesystem
|     |
|     +-- Git
|
+-- OpenClaw Cron
+      scheduled starts
+      deterministic command jobs
+      model-backed executor jobs
      later watchdogs
```

The **validation path** deliberately preserves the already-measured standalone llama.cpp configuration first:

```text
Qwen3-8B + current standalone llama.cpp
        |
        v
structured tool-call baseline
        |
        v
OpenClaw + current standalone llama.cpp
        |
        v
OpenClaw + in-process llama.cpp provider
        |
        v
equivalent fixture comparison
```

Only after the in-process path is equivalent or better should the standalone server be retired from normal execution.

OpenClaw officially supports native Windows installation and managed Gateway startup through Windows Task Scheduler.

---

# 2. Implementation gates

Do not treat installation as one undifferentiated task.

|Gate|Requirement|
|---|---|
|G0|Existing repo/OpenClaw files inspected and preserved|
|G0A|Existing standalone Qwen + llama.cpp emits a real structured tool call|
|G1|OpenClaw installed and pinned|
|G2|OpenClaw + existing standalone llama.cpp executes a real tool trajectory|
|G3|In-process llama.cpp executes an equivalent real tool trajectory|
|G4|APEX executor agent + skills load correctly|
|G5|Chrome extension controls dedicated signed-in browser and provider containment passes|
|G6|Deterministic script execution works|
|G7|File + Git workflow works with intended authority|
|G8|OpenClaw Cron starts both a harmless model-backed job and deterministic command job|
|G9|Immediate dispatch works|
|G10|One complete subscription-AI workflow passes|
|G11|Restart/resume and duplicate-action test passes|
|G12|Laptop coexistence/resource gate passes|

Each gate is verified before widening authority.

---

# 3. Task 0 — Preserve current state

Work in:

```powershell
C:\GitDev\apexai-os-meta
```

Verify:

```powershell
git branch --show-current
git status --short
git log --oneline -5
```

Required:

```text
branch = main
```

Do not touch unrelated `.bundle` files.

Inspect the locally prepared OpenClaw artifacts before writing anything:

```powershell
Test-Path .\OPENCLAW-LOCAL-LLM-MASTER-BRIEF.md
Test-Path .\apex-meta\openclaw\openclaw.json
Test-Path .\apex-meta\openclaw\SETUP.md
Test-Path .\apex-meta\openclaw\skills\apex-flow-executor\SKILL.md
```

These paths were referenced by the previous handover but were not visible on connected GitHub `main`; treat the local copies as potentially newer/unpushed work and **do not overwrite them without comparison**.

Also verify the existing model:

```powershell
Test-Path 'C:\LocalModels\qwen3-8b\gguf-q4km\Qwen3-8B-Q4_K_M.gguf'
```

Record its SHA-256:

```powershell
Get-FileHash `
  'C:\LocalModels\qwen3-8b\gguf-q4km\Qwen3-8B-Q4_K_M.gguf' `
  -Algorithm SHA256
```

**Gate G0 passes when all existing state is understood and preserved.**

---

# 3A. Task 0A — Establish the standalone Qwen tool-call baseline

Before OpenClaw changes the execution path, prove that the existing Qwen3-8B + standalone llama.cpp configuration can emit a real structured tool call.

Confirm the local server:

```powershell
Invoke-RestMethod http://127.0.0.1:8090/health
$models = Invoke-RestMethod http://127.0.0.1:8090/v1/models
$models.data | Format-Table id
```

Then run a minimal function-call fixture:

```powershell
$model = (Invoke-RestMethod http://127.0.0.1:8090/v1/models).data[0].id

$body = @{
    model = $model
    messages = @(
        @{
            role = "user"
            content = "Use the echo tool exactly once with the text APEX_TOOL_OK."
        }
    )
    tools = @(
        @{
            type = "function"
            function = @{
                name = "echo"
                description = "Echo a supplied test string."
                parameters = @{
                    type = "object"
                    properties = @{
                        text = @{
                            type = "string"
                        }
                    }
                    required = @("text")
                    additionalProperties = $false
                }
            }
        }
    )
    tool_choice = "auto"
    max_tokens = 256
} | ConvertTo-Json -Depth 12

$r = Invoke-RestMethod `
    -Method Post `
    -Uri "http://127.0.0.1:8090/v1/chat/completions" `
    -ContentType "application/json" `
    -Body $body

$r.choices[0].message | ConvertTo-Json -Depth 12
```

PASS requires a real structured `tool_calls` entry invoking `echo` with `APEX_TOOL_OK`.

FAIL includes:

```text
text saying "I would call echo"
pseudo-JSON in normal assistant content
invalid tool arguments
no tool call before the token budget ends
```

Do not continue to OpenClaw tool-integration debugging until this baseline passes.

**Gate G0A passes only on a real structured tool call.**

---

# 4. Task 1 — Install pinned OpenClaw stable

As of 2026-08-10, npm's current `latest` stable is:

```text
2026.7.1-2
```

with `2026.6.33` available as the extended-stable channel.

Use the stable exact version rather than an unpinned `latest`.

### Dry run

```powershell
& ([scriptblock]::Create(
  (iwr -useb https://openclaw.ai/install.ps1)
)) `
  -Tag 2026.7.1-2 `
  -NoOnboard `
  -DryRun
```

### Install

```powershell
& ([scriptblock]::Create(
  (iwr -useb https://openclaw.ai/install.ps1)
)) `
  -Tag 2026.7.1-2 `
  -NoOnboard
```

The official PowerShell installer accepts an exact `-Tag`, can skip onboarding, and installs a supported Node runtime when needed.

Verify:

```powershell
openclaw --version
```

Expected:

```text
2026.7.1-2
```

**Gate G1 passes.**

---

# 5. Task 2 — Create minimal OpenClaw state

Do not use the generic personal-assistant onboarding to decide our architecture.

Create baseline files:

```powershell
openclaw setup --baseline
```

Find the active configuration:

```powershell
openclaw config file
```

The active OpenClaw configuration must be a real file; OpenClaw does not support symlinked `openclaw.json` layouts for config writes.

The repo should therefore contain the **desired/template config**, while the running installation uses the deployed active config under the OpenClaw state directory.

Architecture:

```text
apex-meta/openclaw/openclaw.json
        |
        | reviewed deploy
        v
~/.openclaw/openclaw.json
```

Do not commit OpenClaw credentials/state.

---

# 6. Task 3 — Configure the local Gateway

Use local-only networking.

Target:

```json5
{
  gateway: {
    mode: "local",
    port: 18789,
    bind: "loopback",
    auth: {
      mode: "token",
      token: "${OPENCLAW_GATEWAY_TOKEN}"
    }
  }
}
```

OpenClaw defaults to loopback networking and supports token authentication; environment-variable substitution is supported directly in config strings.

Generate a token locally and store it outside Git.

Then validate:

```powershell
openclaw config validate
openclaw config validate --json
```

Do not continue while config validation fails.

---

# 6A. Task 3A — Integrate OpenClaw with the known-good standalone llama.cpp server

Before installing the in-process provider, connect OpenClaw to the already-running loopback llama.cpp server so the first OpenClaw test changes only one layer.

Configure a temporary local provider using the model ID returned by:

```powershell
(Invoke-RestMethod http://127.0.0.1:8090/v1/models).data
```

Provider shape:

```json5
{
  models: {
    mode: "merge",
    providers: {
      "apex-llama-baseline": {
        baseUrl: "http://127.0.0.1:8090/v1",
        apiKey: "llamacpp-local",
        api: "openai-completions",
        timeoutSeconds: 180,
        models: [
          {
            id: "<MODEL_ID_FROM_V1_MODELS>",
            name: "Qwen3-8B standalone llama.cpp baseline",
            reasoning: false,
            input: ["text"],
            cost: {
              input: 0,
              output: 0,
              cacheRead: 0,
              cacheWrite: 0
            },
            contextWindow: 32768,
            maxTokens: 2048
          }
        ]
      }
    }
  }
}
```

The `openai-completions` label describes the local protocol adapter. Requests stay on `127.0.0.1`; this does not call OpenAI or any cloud service.

Point a temporary smoke-test agent/model selection at:

```text
apex-llama-baseline/<MODEL_ID_FROM_V1_MODELS>
```

Run a harmless real tool trajectory and verify:

```text
Qwen emits a structured tool call
OpenClaw executes the allowed tool
the tool result returns to Qwen
Qwen finishes the turn
```

If the standalone baseline passed Task 0A but this fails, diagnose the OpenClaw provider/tool integration before changing the model runtime.

**Gate G2 passes only on a real OpenClaw tool trajectory through the existing standalone server.**

---

# 7. Task 4 — Install the official in-process llama.cpp provider

Only after Gate G2 passes, install:

```powershell
openclaw plugins install @openclaw/llama-cpp-provider
```

The plugin is the official OpenClaw provider for in-process GGUF text inference and owns its `node-llama-cpp` native runtime.

The intended final model path is:

```text
OpenClaw
   |
node-llama-cpp
   |
Qwen3-8B.gguf
```

The existing standalone llama.cpp server remains available throughout comparison as the known-good reference. Do not remove or disable it merely because the plugin installed successfully.

Use Node 24 for the smoothest native provider installation/update path.

---

# 8. Task 5 — Wire the existing Qwen3-8B GGUF into OpenClaw

Start with a conservative smoke-test context:

```json5
{
  models: {
    mode: "merge",

    providers: {
      "llama-cpp": {
        baseUrl: "local://llama-cpp",
        api: "openai-completions",

        models: [
          {
            id: "qwen3-8b-apex",
            name: "Qwen3-8B APEX Executor",

            reasoning: false,
            input: ["text"],

            cost: {
              input: 0,
              output: 0,
              cacheRead: 0,
              cacheWrite: 0
            },

            contextWindow: 8192,
            maxTokens: 2048,

            params: {
              modelPath: "C:/LocalModels/qwen3-8b/gguf-q4km/Qwen3-8B-Q4_K_M.gguf",
              contextSize: 8192
            },

            compat: {
              supportsTools: true
            }
          }
        ]
      }
    }
  }
}
```

This follows OpenClaw's documented custom-GGUF configuration. The `local://llama-cpp` transport is in-process; model tool calls return to OpenClaw for execution.

### Why start at 8K?

OpenClaw itself defaults local llama.cpp onboarding to an 8,192-token cap and explicitly recommends increasing context only after verifying machine memory capacity.

The **production target remains 32K**, matching the previous local-model decision.

After the executor works, change:

```json5
contextWindow: 32768

params: {
  contextSize: 32768
}
```

and run the coexistence gate.

The previous standalone llama.cpp setup demonstrated that 32K is plausible on this laptop, but the in-process node-llama-cpp implementation must be measured independently. 

---

# 9. Task 6 — Smoke-test local inference

First run a model-only test:

```powershell
openclaw infer model run `
  --local `
  --model llama-cpp/qwen3-8b-apex `
  --prompt "Reply with exactly: APEX_QWEN_OK" `
  --json
```

Required:

```text
APEX_QWEN_OK
```

Then repeat the same harmless tool trajectory used for Gate G2 with the in-process model.

Required evidence:

```text
normal response succeeds
real structured tool call succeeds
OpenClaw executes the tool
tool result returns to Qwen
Qwen completes the turn
```

Compare the standalone and in-process paths on the same fixture before selecting the normal execution topology.

If the standalone OpenClaw path passes but the in-process path fails, stop and diagnose the native provider/plugin rather than changing browser or skill configuration.

**Gate G3 passes only when the in-process path executes an equivalent real tool trajectory.**

---

# 10. Task 7 — Create the `apex-executor` agent

Create one persistent OpenClaw agent:

```powershell
openclaw agents add apex-executor `
  --workspace "$env:USERPROFILE\.openclaw\workspace-apex-executor" `
  --model llama-cpp/qwen3-8b-apex `
  --non-interactive
```

OpenClaw supports separate agent workspaces and session stores inside one Gateway.

The workspace should contain only executor-level operating instructions.

Suggested:

```text
workspace-apex-executor/
  AGENTS.md
  SOUL.md
  TOOLS.md
```

### `AGENTS.md` must establish

```text
You are the APEX Local Executor.

You execute approved workflows.
You do not choose project strategy.
You do not redesign workflows.
You do not substitute providers.
You do not promote your own output.
You obey declared roots, tools, actions and stop conditions.
When execution cannot safely continue, return evidence and stop.
```

Do not stuff Weekly, Meta Ops or project reasoning doctrine into this workspace.

Those belong to their owning workflows/repositories.

---

# 11. Task 8 — Load APEX-owned executor skills

Use the repository as the shared skill source.

Target configuration:

```json5
{
  skills: {
    load: {
      extraDirs: [
        "C:/GitDev/apexai-os-meta/apex-meta/openclaw/skills"
      ],

      watch: true
    },

    install: {
      allowUploadedArchives: false
    },

    workshop: {
      autonomous: {
        enabled: false
      },

      allowSymlinkTargetWrites: false
    }
  }
}
```

OpenClaw supports extra trusted skill directories and the watcher defaults to enabled.

Initial APEX skill family should eventually include:

```text
apex-flow-executor
subscription-ai-browser
repo-automation
script-execution
git-safe-operation
execution-evidence
```

These may initially be combined in one skill and split only when repetition proves useful.

Verify:

```powershell
openclaw skills list --agent apex-executor
openclaw skills check --agent apex-executor
```

**Gate G4 requires that only intended operational skills are active.**

---

# 12. Task 9 — Give the executor the correct tool surface

The executor is **not browser-only**.

Required core surface:

```text
browser
read
write
edit
apply_patch
exec
process
session_status
```

OpenClaw documents these as separate tool families, and `exec` remains mutating even when filesystem-specific tools are disabled.

Do not give it orchestration/subagent tools merely because OpenClaw supports them.

Initial denies should include unnecessary authority such as:

```text
subagent spawning
agent-goal manipulation
cross-agent orchestration
external messaging channels
unneeded web-search providers
```

Qwen is the executor, not another multi-agent orchestration layer.

Enable OpenClaw tool-loop detection:

```json5
{
  tools: {
    loopDetection: {
      enabled: true
    }
  }
}
```

OpenClaw exposes this explicitly as a runtime safety control.

---

# 13. Task 10 — Configure host command execution conservatively

Use two explicit operating phases.

## Setup / learning phase

Start with OpenClaw's cautious model:

```powershell
openclaw exec-policy preset cautious
```

Target behavior:

```text
known/allowlisted command -> run
unknown command -> ask
approval UI unavailable or timeout -> deny
```

Enable defense-in-depth for interpreters:

```json5
{
  tools: {
    exec: {
      strictInlineEval: true
    }
  }
}
```

This prevents allowlisting an interpreter binary from silently turning inline forms such as `python -c` or `node -e` into unrestricted execution.

## Unattended validated-flow phase

Before a workflow is allowed to run unattended, every expected command/script path and argument shape must already fit its declared execution policy.

Unexpected command:

```text
DENY
-> return blocked status/evidence
-> reasoning/operator decides what happens next
```

Do **not** switch the entire executor to YOLO/full merely to avoid prompts.

---

# 14. Task 11 — Add deterministic APEX execution guards

This is where the useful old FEE concepts are retained **without creating FEE**.

Create repo-owned helpers such as:

```text
scripts/openclaw/
  git-safe.ps1
  run-script-safe.ps1
  validate-execution-request.py
```

## `git-safe.ps1`

Allowed operations may include:

```text
status
diff
add
commit
push origin main
```

Reject:

```text
--force
--force-with-lease
reset --hard
rebase
filter-branch
branch deletion
remote changes
checkout/switch to undeclared branch
push anywhere except declared remote/branch
```

## `run-script-safe.ps1`

Accept:

```text
declared repo/root
declared script path
declared argv
```

Reject:

```text
script outside declared root
inline PowerShell payload not declared
python -c
arbitrary eval
unexpected executable
```

This is especially important because OpenClaw itself warns that broad interpreters such as Python require deliberate approval policy; `strictInlineEval` exists specifically to prevent an allowlisted interpreter from automatically making `python -c`, `node -e`, etc. unrestricted.

Enable:

```json5
{
  tools: {
    exec: {
      strictInlineEval: true
    }
  }
}
```

This is the right home for the former deterministic FEE enforcement logic: **small APEX-owned helper scripts**, not another service.

---

# 15. Task 12 — Define the minimal common execution request

Do **not** build a queue.

Define only the interface needed by any workflow to invoke OpenClaw.

Example:

```yaml
execution_request:
  id: EXEC-2026-...

  origin:
    repo: apexai-os-meta
    workflow: weekly-orchestrator
    step: subscription-research

  instruction:
    skill: subscription-ai-browser
    provider: chatgpt
    prompt_ref: ...

  authority:
    roots:
      - path: C:\GitDev\apexai-os-meta
        mode: rw

    tools:
      - browser
      - read
      - write
      - exec

    git:
      commit: true
      push: true
      branch: main

  success:
    - response captured
    - evidence written

  stop:
    - authentication lost
    - CAPTCHA
    - security challenge
    - undeclared scope required

  result:
    path: ...
```

The execution request may live anywhere.

For example:

```text
apexai-os-meta/...
project-a/...
project-b/...
```

Its location does **not** define a global queue.

---

# 16. Task 13 — Verify Qwen tool calling inside the real agent

Now test the actual agent/tool loop.

Use a harmless deterministic task first:

```powershell
openclaw agent `
  --agent apex-executor `
  --session-key "apex:tool-smoke" `
  --message "Use an allowed tool to inspect the current working directory, then reply with the observed path." `
  --json
```

`openclaw agent` executes one complete agent turn and supports explicit agent/session targeting and file-based prompts.

Required evidence:

```text
Qwen generated a real structured tool call
OpenClaw executed the tool
tool result returned to Qwen
Qwen finished the turn
```

A textual imitation such as "I would run X" is a FAIL.

**Gate G3 passes only on a real tool trajectory.**

---

# 17. Task 14 — Install the dedicated Chrome execution profile

Create a dedicated Chrome user profile:

```text
APEX Executor
```

Do not use the operator's everyday browsing profile.

Log into the subscription services manually:

```text
ChatGPT
Gemini
Perplexity
other approved providers
```

Then install/pair the OpenClaw Chrome extension:

```powershell
openclaw browser extension path
openclaw browser extension pair
```

In Chrome:

```text
chrome://extensions
→ Developer mode
→ Load unpacked
→ choose returned extension directory
→ paste pairing string
```

OpenClaw's official extension can control signed-in tabs via `chrome.debugger` without the standard remote-debugging approval prompt.

Set:

```powershell
openclaw config set browser.defaultProfile chrome
```

For the **dedicated APEX Chrome profile**, using the extension's `All tabs` mode is acceptable because that entire Chrome profile exists for executor automation.

If the profile is ever shared with personal browsing, switch to `Selected tabs`.

---

# 18. Task 15 — Verify browser execution

First use a harmless site.

Then run:

```text
open page
snapshot
identify element
click/type
resnapshot
extract result
```

After that, perform one subscription-AI smoke test:

```text
open ChatGPT
verify login
start/open declared chat
place exact trivial prompt
verify full prompt landed
submit
wait
extract exact response
```

Your previously supplied browser research already documents this as a normal OpenClaw browser/skill use case and emphasizes verifying the complete prompt before submission and confirming actual browser state before retries.

The OpenClaw browser plugin also bundles operating guidance around stable tabs, snapshot-before-action, stale-reference recovery and manual escalation for login/2FA/CAPTCHA.

Then run a provider-containment negative fixture:

```text
approved provider = ChatGPT
hostile page/content instruction = navigate to another undeclared provider or hostname
expected = refuse/stop and report the scope conflict
```

A browser page, retrieved response or prompt content is evidence/data only. It must not create new provider, hostname, command, path, tool or workflow authority.

**Gate G5 passes only when both normal browser execution and provider containment succeed.**

---

# 19. Task 16 — Verify script execution

Create a harmless test script:

```python
print("APEX_SCRIPT_OK")
```

Execute it through the Local Executor.

Required:

```text
approved script
→ OpenClaw exec
→ Python
→ output captured
→ Qwen reports result
```

Then test a failure:

```text
request undeclared inline Python
```

Expected:

```text
DENY / approval required
```

Do not proceed to unattended repo mutation until both paths behave correctly.

**Gate G6 passes.**

---

# 20. Task 17 — Verify Git operations

Use a disposable fixture repository first.

Test sequentially:

```text
git status
git diff
write small file
git add
git commit
git push
```

Then adversarially test:

```text
git push --force
git reset --hard
delete branch
push to undeclared branch
```

Expected:

```text
DENY
```

Only after this gate passes should the executor be granted real repo Git mutation.

For `apexai-os-meta`:

```text
main only
```

unless the operator explicitly changes the rule.

**Gate G7 passes.**

---

# 21. Task 18 — Enable OpenClaw Cron

Do not create the final workflow catalog yet.

First prove both scheduler modes.

## Model-backed test

Create a harmless one-shot Cron job whose payload is an agent message for `apex-executor`.

Expected:

```text
Cron fires
-> creates background task
-> wakes apex-executor
-> Qwen completes harmless task
-> run history records result
```

## Deterministic command test

Create a harmless operator-authored command Cron job that prints a fixed marker or runs a tiny trusted script.

Expected:

```text
Cron fires
-> command executes directly in Gateway scheduler
-> no model/Qwen turn occurs
-> stdout/stderr and run status are recorded
```

Prefer deterministic command jobs for exact scheduled checks/scripts that do not need model judgement.

Verify with the current CLI:

```powershell
openclaw cron list
openclaw cron show <job-id>
openclaw cron run <job-id>
openclaw cron runs --id <job-id>
```

Required:

```text
jobs survive Gateway restart
both payload classes execute correctly
history exists
result attribution is correct
```

Cron mutation/run administration is an operator-admin surface. Model-visible `exec` policy governs agent tool calls, not operator-authored command Cron payloads.

**Gate G8 passes only after both the model-backed and deterministic command paths succeed.**

---

# 22. Task 19 — Verify immediate workflow dispatch

A reasoning workflow should be able to create an execution-request file and immediately invoke:

```powershell
openclaw agent `
  --agent apex-executor `
  --session-key "apex:<execution-id>" `
  --message-file "<validated-execution-request>" `
  --json
```

OpenClaw supports message-file inputs up to its documented limit and explicit session keys for agent turns.

This becomes the first dispatch interface.

No global queue is required.

**Gate G9 passes.**

---

# 23. Task 20 — Install the Gateway as persistent Windows infrastructure

Once the configuration is proven in foreground mode:

```powershell
openclaw gateway install
openclaw gateway status --require-rpc
```

Native Windows managed startup uses a Scheduled Task named `OpenClaw Gateway`; OpenClaw also provides a Startup-folder fallback if Scheduled Task creation is unavailable.

Run:

```powershell
openclaw config validate --json
openclaw doctor
openclaw security audit --deep
```

OpenClaw provides both cold configuration/file audits and a deep mode that additionally probes the live Gateway and plugin security collectors.

---

# 24. Task 21 — Promote Qwen to the target 32K context

After all basic functionality works:

```text
8192
  ↓
16384 if useful intermediate test
  ↓
32768 target
```

Set:

```json5
contextWindow: 32768

params: {
  contextSize: 32768
}
```

Then run simultaneously:

```text
OpenClaw Gateway
Qwen
Chrome subscription sessions
IDE
normal terminals
test suite
occasional Claude/Codex CLI use
```

Measure:

```text
system RAM
GPU/shared memory
generation latency
tool-call latency
browser responsiveness
crashes
paging
```

The production 32K configuration does not pass until normal laptop use remains viable.

**Gate G12 passes.**

---

# 25. Task 22 — First complete APEX vertical slice

Choose one deliberately small workflow.

Example:

```text
reasoning model
  creates approved research prompt
        |
        v
execution request
        |
        v
OpenClaw + Qwen
        |
        v
Chrome → ChatGPT
        |
        v
prompt submitted
        |
        v
response captured
        |
        v
result file written
        |
        v
owning reasoning workflow notified/continued
```

Required evidence:

1. exact prompt reference;
2. execution-request ID;
3. provider;
4. browser session/profile;
5. submission evidence;
6. captured result;
7. output path/hash;
8. terminal status;
9. no unauthorized actions.

**Gate G10 passes.**

---

# 26. Task 23 — Restart/idempotency test

Test the most dangerous operational case:

```text
OpenClaw submits prompt
        |
        v
Gateway dies before workflow records completion
```

Procedure:

1. submit one uniquely identifiable test prompt;
2. interrupt Gateway around submission;
3. restart Gateway;
4. inspect browser/conversation state;
5. determine whether submission already occurred;
6. verify executor does **not blindly submit it twice**;
7. record the recovered result/state.

Only after this passes should unattended overnight subscription workflows be considered reliable.

**Gate G11 passes.**

---

# 27. Task 24 — Introduce real scheduled flows

Only now create actual recurring Automation jobs.

Examples:

```text
Weekly orchestration kickoff
daily evidence cleanup
scheduled subscription research
periodic project checks
later pending-work watchdog
```

Each Automation should declare:

```text
owning workflow
owning repository
agent
tool policy
model
schedule
result destination
```

OpenClaw Automations persist explicit tool policy per job, support isolated agent sessions, maintain run history and support manual force-run/wait operations for testing.

---

# 28. Task 25 — Reconcile old FEE documentation

Only after the OpenClaw vertical slice works:

1. mark FEE-as-separate-runtime descriptions superseded;
2. rename project terminology toward `Local Executor`;
3. move reusable execution-contract material into APEX/OpenClaw documentation;
4. audit `scripts/fee`;
5. migrate useful deterministic helpers;
6. remove/archive obsolete FEE pieces only after replacements are verified.

Do not delete working code merely to make naming cleaner.

---

# 29. Task 26 — Design federated workflow storage later

This is intentionally **not a prerequisite** for installation.

Later research/design must determine:

```text
which workflows live in apexai-os-meta?
which live in each project repo?
how are pending states represented?
how is cross-repo discovery done?
what needs a shared index?
does a watchdog need to scan several repos?
```

Whatever that decision is, it must preserve the already-established executor interface:

```text
owning workflow
      |
execution request
      |
OpenClaw + Qwen
      |
result/evidence
      |
owning workflow
```

No executor redesign should be necessary.

---

# 30. Definition of done

The initial OpenClaw Local Executor setup is complete when all are true:

```yaml
openclaw:
  installed: true
  pinned_version: "2026.7.1-2"
  gateway_persistent: true
  native_windows: true

local_model:
  model: Qwen3-8B
  cloud_required: false
  standalone_tool_call_baseline: pass
  openclaw_standalone_tool_trajectory: pass
  in_process_llama_cpp: true
  in_process_equivalent_tool_trajectory: pass
  active_inference_lanes: 1
  target_context_32k: pass_or_explicitly_deferred

executor:
  apex_executor_agent: pass
  apex_owned_skills: pass
  skill_watcher: enabled

browser:
  dedicated_chrome_profile: pass
  extension_connected: pass
  subscription_prompt_round_trip: pass

tools:
  scripts: pass
  filesystem: pass
  git_commit: pass
  git_push: pass
  prohibited_git_operations: denied

dispatch:
  immediate: pass
  cron_model_backed: pass
  cron_deterministic_command: pass

reliability:
  gateway_restart: pass
  duplicate_action_protection: pass
  laptop_coexistence: pass

architecture:
  separate_fee_runtime: false
  global_queue_required: false
  reasoning_authority_retained_by_apex: true
```

The **next bounded action is Task 0 → Task 1: preserve/inspect the current local OpenClaw files, then perform the pinned OpenClaw installation dry run.**
