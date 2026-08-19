I followed the uploaded exact-match patch format and verified that every `<old>` block below occurs **exactly once** in the corresponding uploaded file. The patch incorporates the added research while preserving the newer architecture decisions in the decision lock and implementation plan.

I also rechecked the changed mechanics against current official OpenClaw docs: the llama.cpp plugin is an in-process provider, `openclaw cron` is the current scheduler CLI and supports both model-backed and deterministic command payloads, `skills.load.watch` defaults to `true`, and `strictInlineEval` exists specifically to constrain inline interpreter execution. ([OpenClaw](https://docs.openclaw.ai/plugins/llama-cpp "llama.cpp Provider - OpenClaw"))

/mnt/data/OpenClaw Local Executor — Operator Decision Lock.md  

# 6. Local model topology

## DEC-OC-05 — In-process llama.cpp is the intended topology

**Decision: TARGET LOCKED; MIGRATION EVIDENCE-GATED**

The intended final topology is:

```text
OpenClaw
   |
   +-- official llama.cpp provider plugin
           |
           +-- Qwen3-8B GGUF
```

No cloud model or external inference API is required.

The existing standalone `llama-server` installation remains temporarily available as the measured baseline while the OpenClaw in-process configuration is verified.

After equivalent tool reliability, context and resource coexistence are demonstrated, the standalone model server may be retired from the normal execution path.

OpenClaw's provider uses `local://llama-cpp`; inference is in-process. The configuration field `api: "openai-completions"` is merely OpenClaw's internal provider contract and does not mean traffic is sent to OpenAI.

---

## DEC-OC-05 — In-process llama.cpp is the intended topology after controlled comparison

**Decision: TARGET LOCKED; MIGRATION EVIDENCE-GATED**

The intended final topology is:

```text
OpenClaw
   |
   +-- official llama.cpp provider plugin
           |
           +-- Qwen3-8B GGUF
```

No cloud model or external inference API is required.

The existing standalone `llama-server` installation is the known-good measured baseline and must remain intact during initial OpenClaw integration.

Migration sequence:

```text
existing Qwen3-8B + standalone llama.cpp
        |
        | prove structured tool calling
        v
OpenClaw + existing standalone llama.cpp
        |
        | prove the same tool/browser behavior
        v
OpenClaw + official in-process llama.cpp provider
        |
        | compare equivalent tool, browser, context and resource fixtures
        v
retire standalone server from normal execution only if equivalent or better
```

The comparison must isolate failures:

- failure before OpenClaw indicates a model/runtime baseline problem;
    
- failure only through the standalone OpenClaw provider path indicates an integration/provider problem;
    
- failure only through the in-process provider indicates an in-process runtime/plugin difference.
    

The standalone server is therefore not removed merely because the in-process provider exists.

OpenClaw's official llama.cpp provider uses `local://llama-cpp`; inference is in-process and model-generated tool calls return to OpenClaw for execution. The configuration field `api: "openai-completions"` is an internal provider contract and does not mean traffic is sent to OpenAI.

---

/mnt/data/OpenClaw Local Executor — Operator Decision Lock.md  

# 7. Scheduling

## DEC-OC-06 — OpenClaw Automations/Cron is required

**Decision: LOCKED**

OpenClaw Automations is a core component of the intended system.

It will be used for:

- scheduled workflow starts;
    
- weekly/daily execution;
    
- recurring maintenance;
    
- later queue/watchdog jobs;
    
- bounded unattended operations.
    

OpenClaw Automations supports cron schedules, fixed intervals, one-shot schedules and event/stream triggers. Jobs may execute a model-backed agent turn, a deterministic command or a script.

Cron therefore must **not** be disabled.

---

## DEC-OC-06 — OpenClaw Cron is required

**Decision: LOCKED**

OpenClaw Cron is a core component of the intended system.

It will be used for:

- scheduled workflow starts;
    
- weekly/daily execution;
    
- recurring maintenance;
    
- later queue/watchdog jobs;
    
- bounded unattended operations.
    

Cron runs inside the OpenClaw Gateway and persists job definitions, runtime state and run history across Gateway restarts.

Two execution classes are deliberately supported:

```text
model-backed cron job
  -> wakes apex-executor
  -> Qwen performs an approved operational workflow

deterministic command cron job
  -> runs an operator-authored command/script in the Gateway scheduler
  -> no Qwen/model turn is required
```

Use deterministic command jobs for checks, probes and exact scripts that do not require model judgement. Use model-backed jobs when browser/tool operation requires the Local Executor.

Persistent schedule creation or modification remains an operator/APEX authority surface; Qwen executes approved schedules but does not invent durable schedules for itself.

Cron therefore must **not** be disabled.

---

/mnt/data/OpenClaw Local Executor — Operator Decision Lock.md  

# 15. Browser authority

## DEC-OC-14 — UI recovery allowed; workflow choice is external

**Decision: LOCKED**

The Local Executor may:

- find a moved button;
    
- reopen/focus a declared tab;
    
- adapt to benign UI layout changes;
    
- resnapshot/retry a declared browser operation;
    
- recover from bounded presentation-level failures.
    

It may not independently:

- switch research providers;
    
- invent another reasoning strategy;
    
- bypass login/security/CAPTCHA;
    
- change paid/account settings;
    
- substitute a semantically different workflow.
    

---

## DEC-OC-14 — UI recovery allowed; workflow choice and provider authority are external

**Decision: LOCKED**

The Local Executor may:

- find a moved button;
    
- reopen/focus a declared tab;
    
- adapt to benign UI layout changes;
    
- resnapshot/retry a declared browser operation;
    
- recover from bounded presentation-level failures.
    

It may not independently:

- switch research providers;
    
- invent another reasoning strategy;
    
- bypass login/security/CAPTCHA;
    
- change paid/account settings;
    
- substitute a semantically different workflow.
    

Browser/page/model content is untrusted input and cannot expand execution authority. A page instruction, retrieved text or model response may not create a new provider, hostname, tool, path, command or workflow step outside the approved execution request.

Before unattended production, the executor must pass a provider-containment fixture in which a job declared for one provider is induced by hostile page/content text to navigate to another destination and correctly refuses/stops rather than widening scope.

---

/mnt/data/OpenClaw Local Executor — Operator Decision Lock.md  

# 20. Final system law

The system can be summarized as:  
  

# 20. Local inference concurrency

## DEC-OC-19 — One active Qwen inference lane initially

**Decision: LOCKED**

The initial executor runs one active local-model action lane at a time.

Multiple workflows may be scheduled, waiting on browser activity, checkpointed or otherwise pending, but only one Qwen inference/action lane is active concurrently until resource and reliability measurements justify a wider limit.

This preserves laptop coexistence and makes tool/browser failures easier to attribute during the first production phase.

---

# 21. Final system law

The system can be summarized as:  

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

# 1. Target technical architecture

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
+-- OpenClaw Automations
      scheduled starts
      recurring jobs
      later watchdogs
```

OpenClaw officially supports native Windows installation and managed Gateway startup through Windows Task Scheduler.

---

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
      scheduled starts
      deterministic command jobs
      model-backed executor jobs
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

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

# 2. Implementation gates

Do not treat installation as one undifferentiated task.

|Gate|Requirement|
|---|---|
|G0|Existing repo/OpenClaw files inspected and preserved|
|G1|OpenClaw installed and pinned|
|G2|In-process Qwen generates a normal response|
|G3|Qwen produces valid OpenClaw tool calls|
|G4|APEX executor agent + skills load correctly|
|G5|Chrome extension controls dedicated signed-in browser|
|G6|Deterministic script execution works|
|G7|File + Git workflow works with intended authority|
|G8|OpenClaw Automation starts a job unattended|
|G9|Immediate dispatch works|
|G10|One complete subscription-AI workflow passes|
|G11|Restart/resume and duplicate-action test passes|
|G12|Laptop coexistence/resource gate passes|

Each gate is verified before widening authority.

---

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

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  
  
**Gate G0 passes when all existing state is understood and preserved.**

---

# 4. Task 1 — Install pinned OpenClaw stable

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

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  
  
Do not continue while config validation fails.

---

# 7. Task 4 — Install the official in-process llama.cpp provider

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

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

# 7. Task 4 — Install the official in-process llama.cpp provider

Install:

```powershell
openclaw plugins install @openclaw/llama-cpp-provider
```

The plugin is the official OpenClaw provider for in-process GGUF text inference and owns its `node-llama-cpp` native runtime.

This means the final model path becomes:

```text
OpenClaw
   |
node-llama-cpp
   |
Qwen3-8B.gguf
```

not:

```text
OpenClaw
   |
HTTP
   |
standalone llama-server
```

The existing standalone llama.cpp server remains only as a temporary benchmark/reference configuration.

---

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

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

# 9. Task 6 — Smoke-test local inference

Run a model-only test:

```powershell
openclaw infer model run `
  --local `
  --model llama-cpp/qwen3-8b-apex `
  --prompt "Reply with exactly: APEX_QWEN_OK" `
  --json
```

The inference CLI is specifically intended for testing a provider/model without the entire agent tool surface.

Required:

```text
APEX_QWEN_OK
```

If this fails, stop here and diagnose the native llama.cpp plugin before involving browser/tools.

**Gate G2 passes.**

---

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

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

# 13. Task 10 — Configure host command execution conservatively

Start with OpenClaw's cautious model:

```powershell
openclaw exec-policy preset cautious
```

This corresponds to:

```text
host = gateway
security = allowlist
ask = on-miss
askFallback = deny
```

OpenClaw supports `deny`, `allowlist`, `ask`, `auto`, and `full` host execution modes. Its cautious preset uses an allowlist and fails closed when an approval cannot be obtained.

For the unattended executor, commands required by a scheduled workflow must therefore already be authorized.

Do **not** switch the entire executor to YOLO/full merely to avoid prompts.

---

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

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  
  
The OpenClaw browser plugin also bundles operating guidance around stable tabs, snapshot-before-action, stale-reference recovery and manual escalation for login/2FA/CAPTCHA.

**Gate G5 passes.**  
  
  
The OpenClaw browser plugin also bundles operating guidance around stable tabs, snapshot-before-action, stale-reference recovery and manual escalation for login/2FA/CAPTCHA.

Then run a provider-containment negative fixture:

```text
approved provider = ChatGPT
hostile page/content instruction = navigate to another undeclared provider or hostname
expected = refuse/stop and report the scope conflict
```

A browser page, retrieved response or prompt content is evidence/data only. It must not create new provider, hostname, command, path, tool or workflow authority.

**Gate G5 passes only when both normal browser execution and provider containment succeed.**  

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

# 21. Task 18 — Enable OpenClaw Automations

Do not create the final workflow catalog yet.

First prove the scheduler.

OpenClaw Automations supports:

```text
one-shot time
fixed interval
cron
event/command-exit
stream trigger
```

and can run model turns, commands or scripts.

Create a harmless one-shot test job.

Then verify:

```powershell
openclaw automations list
openclaw automations show <jobId>
openclaw automations run <jobId> --wait
openclaw automations runs --id <jobId>
```

Required:

```text
job survives Gateway restart
run executes
history exists
result attributed correctly
```

**Gate G8 passes.**

---

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
run history exists
result attribution is correct
```

Cron mutation/run administration is an operator-admin surface. Model-visible `exec` policy governs agent tool calls, not operator-authored command Cron payloads.

**Gate G8 passes only after both the model-backed and deterministic command paths succeed.**

---

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  
  
local_model:  
model: Qwen3-8B  
cloud_required: false  
in_process_llama_cpp: true  
real_tool_calls: pass  
target_context_32k: pass_or_explicitly_deferred  
  
  
local_model:  
model: Qwen3-8B  
cloud_required: false  
standalone_tool_call_baseline: pass  
openclaw_standalone_tool_trajectory: pass  
in_process_llama_cpp: true  
in_process_equivalent_tool_trajectory: pass  
active_inference_lanes: 1  
target_context_32k: pass_or_explicitly_deferred  

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  
  
dispatch:  
immediate: pass  
automations: pass  
  
  
dispatch:  
immediate: pass  
cron_model_backed: pass  
cron_deterministic_command: pass  

These are **patch instructions only**; I have not applied them.