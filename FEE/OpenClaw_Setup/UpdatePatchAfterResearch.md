Yes. I’m treating your latest instruction as an **architecture constraint**: **reuse OpenClaw native capability and vetted community skills before writing APEX-specific mechanics**. Current OpenClaw already provides compact browser snapshots, file upload/download, configurable skill loading, and management of loopback local-model services; ClawHub also already has reusable ChatGPT Web and browser-automation skills. ([OpenClaw](https://docs.openclaw.ai/tools/browser?utm_source=chatgpt.com "Browser (OpenClaw-managed) - OpenClaw"))

The patches below also lock your **1A payload-bypass decision**, keep **32K native context + compact observations**, and explicitly defer SYCL/in-process/backend optimization until actual operation shows a reason to optimize. That follows the useful common ground in the two added research reports rather than importing their speculative hardware numbers.

I followed the literal exact-match patch format you supplied.

/mnt/data/OpenClaw Local Executor — Operator Decision Lock.md  
  
OpenClaw's native agent runtime already owns the agent loop, tool wiring, workspace and session store, while its official llama.cpp provider can perform local GGUF inference directly inside the OpenClaw process.

---

# 2. FEE decision

## Implementation law — reuse before invention

**Decision: LOCKED**

For executor mechanics, the implementation order is:

```text
OpenClaw native capability
        ↓
bundled OpenClaw skill/plugin
        ↓
vetted ClawHub/community skill
        ↓
adapt/fork the closest proven implementation
        ↓
custom APEX implementation only if a concrete capability gap remains
```

Do not create an APEX-specific browser stack, file-transfer mechanism, Git wrapper, scheduler, session manager or equivalent runtime component merely because it is straightforward to design.

Before custom implementation is authorized, the implementation task must record:

- what existing OpenClaw capabilities were checked;
    
- which relevant bundled/community skills were inspected;
    
- why they do not satisfy the requirement;
    
- the smallest remaining capability gap.
    

APEX-specific skills should primarily encode APEX workflow intent, authority and integration conventions around proven OpenClaw mechanics rather than reimplementing those mechanics.

---

# 2. FEE decision

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
  

# 6. Local model topology

## DEC-OC-05 — Use the existing Qwen runtime first; optimize later

**Decision: INITIAL TOPOLOGY LOCKED; BACKEND OPTIMIZATION DEFERRED**

The initial implementation uses the already-installed and verified Qwen3-8B + llama.cpp configuration.

Conceptually this remains one Local Executor:

```text
OpenClaw + Qwen3-8B
```

The fact that the first implementation may communicate with the already-running local llama.cpp process through loopback is an internal runtime detail, not a separate architecture component and not a cloud dependency.

Do not block the first working OpenClaw executor on:

- migrating immediately to OpenClaw's in-process llama.cpp provider;
    
- Vulkan-versus-SYCL optimization;
    
- KV-cache tuning beyond what is required to run;
    
- day/night inference profiles;
    
- replacing the known-working local runtime.
    

Those remain future optimization possibilities.

The existing standalone runtime should first be used to prove the actual OpenClaw browser, tool, script, Git, Cron and workflow loops. Runtime/backend optimization is reopened only when measured execution reliability, latency, context, memory or coexistence creates a reason to optimize.  

/mnt/data/OpenClaw Local Executor — Operator Decision Lock.md  

# 10. Tool authority

## DEC-OC-09 — Work-authorized operational tool use

**Decision: LOCKED**

The Local Executor is **not browser-only**.

Depending on the approved workflow it may use:

- browser;
    
- filesystem read/write/edit;
    
- deterministic scripts;
    
- Python;
    
- PowerShell;
    
- process execution;
    
- Git;
    
- tests and validators;
    
- artifact movement;
    
- other explicitly approved tools.
    

OpenClaw provides typed filesystem, browser and exec surfaces; `exec` is explicitly a mutating shell surface capable of modifying the host, so it requires deliberate execution policy.  
  

# 10. Tool authority

## DEC-OC-09 — Work-authorized operational tool use

**Decision: LOCKED**

The Local Executor is **not browser-only**.

Depending on the approved workflow it may use:

- browser;
    
- filesystem read/write/edit;
    
- deterministic scripts;
    
- Python;
    
- PowerShell;
    
- process execution;
    
- Git;
    
- tests and validators;
    
- artifact movement;
    
- other explicitly approved tools.
    

### Large-payload invariant

Large authored prompts, research responses, source documents and generated artifacts must not pass through Qwen's context merely because the executor needs to transfer them.

Use reference-based transfer:

```text
payload stored on disk / durable storage
        ↓
Qwen receives compact reference/receipt
  path or handle
  byte count
  hash
  relevant status
        ↓
existing OpenClaw/tool/skill implementation
moves or consumes the payload directly
```

The same principle applies in reverse when capturing large subscription-AI responses.

Before implementing any new payload-transfer mechanism, inspect and test OpenClaw's existing browser/file capabilities and relevant vetted skills. If an existing skill nearly satisfies the requirement, prefer configuring or minimally adapting that implementation rather than building a separate APEX transfer stack.

A successful receipt must not rely on byte count/hash alone where semantic completion matters. The executing skill/tool should use the provider-specific completion or UI-state checks already available in the chosen browser workflow before declaring the capture complete.  

/mnt/data/OpenClaw Local Executor — Operator Decision Lock.md  

# 17. Skill ownership

## DEC-OC-16 — APEX-owned skills first

**Decision: LOCKED**

The executor primarily uses skills maintained inside the APEX/project repositories.

Community ClawHub skills are not a dependency of the initial architecture.

Reusable OpenClaw-native mechanics may still be used, particularly the bundled browser/browser-automation functionality. OpenClaw's browser plugin includes dedicated guidance for stable tab selection, snapshot-before-action, stale-reference recovery and reporting login/2FA/CAPTCHA blockers rather than guessing.  
  

# 17. Skill ownership

## DEC-OC-16 — OpenClaw ecosystem first; APEX skills for APEX-specific integration

**Decision: LOCKED**

The executor should first reuse:

1. OpenClaw-native tools and functionality;
    
2. bundled OpenClaw skills/plugins;
    
3. vetted ClawHub/community skills;
    
4. minimally adapted/forked existing skills when necessary.
    

APEX/project-owned skills are appropriate where the missing concern is genuinely APEX-specific, for example:

- how an APEX execution request is interpreted;
    
- which workflow owns the result;
    
- authority and stop conditions;
    
- project-specific paths or conventions;
    
- orchestration handoff and evidence conventions.
    

APEX-owned skills should not reimplement generic browser, file-transfer, session, scheduler, Git or automation mechanics when a suitable existing OpenClaw implementation can be integrated instead.

Community skills are not trusted automatically. Relevant candidates must be inspected for behavior, dependencies, permissions, maintenance state and available security/audit signals before being enabled for unattended execution.  

/mnt/data/OpenClaw Local Executor — Operator Decision Lock.md  

# 20. Final system law

The system can be summarized as:  
  

# 20. Context and observation policy

## DEC-OC-19 — Native 32K context with mandatory context discipline

**Decision: LOCKED**

Qwen3-8B runs at a target context of 32,768 tokens.

Do not increase the normal executor context beyond 32K merely to compensate for avoidable payload or browser-observation bloat.

The executor instead follows these rules:

```text
large payload
→ pass by reference

browser state
→ compact/scoped observation first

stable instructions/tool definitions
→ keep stable and reusable

dynamic execution state
→ append only the bounded information needed now
```

For browser work, prefer compact, efficient, interactive or selector-scoped observations rather than repeatedly placing full raw accessibility trees into the model context.

64K+, YaRN, KV-cache quantization changes and day/night context profiles are future optimizations only if real executor fixtures demonstrate that native 32K plus observation/payload discipline is insufficient.

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
  

# 1. Target technical architecture

```text
Windows 11
|
+-- OpenClaw Gateway
|     always running
|     persistent scheduler/runtime
|
+-- apex-executor agent
|     |
|     +-- Qwen3-8B
|     |     existing local llama.cpp runtime initially
|     |
|     +-- OpenClaw/bundled/community skills
|     |     APEX-specific skills only where genuinely needed
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
      deterministic scheduled work
      model-backed executor work
      later watchdogs
```

The first objective is a working end-to-end executor, not an optimized inference stack.

Use the already-installed Qwen3-8B + llama.cpp runtime first. In-process llama.cpp, SYCL, alternative KV-cache settings and other backend changes remain future optimizations unless the running executor demonstrates a concrete performance or reliability problem.

The local llama.cpp process is a local implementation detail of the OpenClaw + Qwen executor. It does not represent a cloud API or an additional orchestration actor.  

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
  

# 2. Implementation gates

Do not treat installation as one undifferentiated task.

|Gate|Requirement|
|---|---|
|G0|Existing repo/OpenClaw files inspected and preserved|
|G1|OpenClaw installed and pinned|
|G2|Existing Qwen3-8B + llama.cpp emits a real structured tool call|
|G3|OpenClaw executes a real Qwen tool trajectory through the existing local runtime|
|G4|Required OpenClaw/bundled/community skills are discovered, reviewed and loaded|
|G5|Chrome extension controls dedicated signed-in browser with compact observations|
|G5A|Large prompt/result transfer works by reference without routing the raw payload through Qwen|
|G6|Deterministic script execution works|
|G7|File + Git workflow works with intended authority|
|G8|OpenClaw Cron starts an unattended job|
|G9|Immediate dispatch works|
|G10|One complete subscription-AI workflow passes|
|G11|Restart/resume and duplicate-action test passes|
|G12|32K context and laptop coexistence/resource gate pass|

Each gate is verified before widening authority.

Inference-backend comparison is intentionally **not** an initial gate. Vulkan/SYCL/in-process alternatives are future optimization work if the functioning executor provides evidence that optimization is needed.  

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

Do not replace the known-working local runtime during initial OpenClaw setup.

Verify the current llama.cpp service:

```powershell
Invoke-RestMethod http://127.0.0.1:8090/health
$models = Invoke-RestMethod http://127.0.0.1:8090/v1/models
$models.data | Format-Table id
```

Then verify one genuine structured function/tool call through the current Qwen runtime.

PASS requires a structured tool invocation with valid arguments.

FAIL includes:

```text
"I would call the tool" in prose
pseudo-JSON in assistant text
malformed arguments
no structured tool call
```

This isolates model/runtime capability before OpenClaw is introduced.

**Gate G2 passes only after the existing runtime produces a genuine structured tool call.**

---

# 8. Task 5 — Connect OpenClaw to the existing local Qwen runtime

Configure OpenClaw to use the already-running loopback model endpoint.

Use the actual model ID returned by `/v1/models`.

Target shape:

```json5
{
  models: {
    mode: "merge",

    providers: {
      "apex-local": {
        baseUrl: "http://127.0.0.1:8090/v1",
        apiKey: "local-only",
        api: "openai-completions",
        timeoutSeconds: 180,

        models: [
          {
            id: "<MODEL_ID_FROM_V1_MODELS>",
            name: "Qwen3-8B APEX Executor",

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

`127.0.0.1` means the traffic stays on this machine. The protocol adapter is an implementation detail; no OpenAI/cloud inference is involved.

Keep the existing llama.cpp launch configuration unchanged unless OpenClaw integration proves a specific change is required.

Do not install or migrate to another inference backend during this task.

---

# 9. Task 6 — Smoke-test the real OpenClaw + Qwen tool loop

Create the smallest possible OpenClaw tool-call test using the existing local model.

Required trajectory:

```text
OpenClaw sends bounded instruction + tool schema
        ↓
Qwen emits real structured tool call
        ↓
OpenClaw executes allowed tool
        ↓
tool result returns to Qwen
        ↓
Qwen completes turn
```

PASS is based on the observed tool trajectory, not a textual statement from Qwen that it intended to use a tool.

If Task 4 passes but this task fails, diagnose OpenClaw/provider integration. Do not change inference backend, context technology or browser architecture simultaneously.

**Gate G3 passes only on a real OpenClaw tool trajectory.**

---

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  
  
openclaw agents add apex-executor `--workspace "$env:USERPROFILE\.openclaw\workspace-apex-executor"`  
--model llama-cpp/qwen3-8b-apex `--non-interactive </old> <new> openclaw agents add apex-executor`  
--workspace "$env:USERPROFILE.openclaw\workspace-apex-executor" `--model apex-local/<MODEL_ID_FROM_V1_MODELS>`  
--non-interactive  

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

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

Start by inventorying the existing OpenClaw capability surface:

```powershell
openclaw skills list --agent apex-executor
openclaw skills check --agent apex-executor
```

For every required executor capability, use this order:

```text
native OpenClaw tool/capability
        ↓
bundled skill/plugin
        ↓
vetted ClawHub/community skill
        ↓
adapt/fork existing implementation
        ↓
new APEX implementation only after a proven gap
```

Initial capability areas to investigate include:

```text
subscription-AI browser operation
persistent ChatGPT/browser sessions
browser upload/download
prompt submission
response capture
Git/repository operation
script execution
execution evidence
```

Relevant community skills are candidates, not automatic dependencies. Inspect their `SKILL.md`, included scripts/files, dependencies, required permissions, security/audit status and maintenance state before installation.

When a suitable implementation exists, integrate and test it instead of rebuilding the mechanism.

Keep the repository skill directory available for genuinely APEX-specific integration:

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

APEX-owned skills should focus on:

```text
execution-request interpretation
workflow ownership
authority/stop rules
project conventions
result/evidence handoff
```

Do not create a new generic browser, session, file-transfer, Git or scheduler implementation unless Task 8 records why the existing ecosystem could not satisfy the requirement.

**Gate G4 passes when the selected reusable skills/capabilities are reviewed, installed/configured and visible only where intended.**

---

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

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

Do not start by creating APEX wrapper scripts.

First map each required restriction to existing OpenClaw policy/configuration and reusable skills.

At minimum inspect/test:

```text
OpenClaw exec approval/allowlist policy
strict inline-eval handling
agent/tool allowlists
browser hostname/SSRF controls
skill-scoped operating procedures
existing Git/repository skills
existing script-execution skills
```

Enable the relevant built-in controls, including strict inline-eval protection when interpreters are exposed.

Then test the actual required operations and denials:

```text
Git status/diff/add/commit/push when authorized
force/destructive Git operations denied
declared script execution succeeds
undeclared inline interpreter execution denied
declared roots respected
```

If the native controls plus a vetted existing skill satisfy the requirement, stop there.

If they do not, search the OpenClaw/ClawHub ecosystem for the nearest existing implementation and prefer adapting/forking it.

Only create a new APEX helper after a reproducible test demonstrates a remaining enforcement gap. Record that gap and make the new code as narrow as possible.

The purpose of APEX integration is to compose proven execution primitives, not to recreate an alternative execution framework.

---

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

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

**Gate G5 passes.**  
  

# 18. Task 15 — Verify compact browser execution and reference-based payload transfer

Configure browser observations to prefer compact/efficient snapshots.

During normal execution use the smallest observation sufficient for the current action:

```text
selector/target-scoped observation
        ↓
interactive/compact observation
        ↓
efficient snapshot
        ↓
larger raw accessibility output only for exceptional diagnosis
```

First use a harmless site.

Then run:

```text
open page
compact snapshot
identify element
click/type
compact resnapshot
extract bounded result/receipt
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
capture result
```

Then test the large-payload invariant.

Select an existing OpenClaw-native, bundled or vetted community workflow capable of handling file-backed/reference-backed browser input/output as directly as the provider surface allows.

Test:

```text
large prompt stored as artifact
        ↓
Qwen receives reference + compact metadata only
        ↓
selected existing browser/skill implementation transfers the payload
        ↓
submission is deterministically verified
```

and:

```text
large response
        ↓
selected existing browser/skill implementation captures it to storage
        ↓
Qwen receives path/handle + byte count + hash + completion status
```

Do not pass the entire payload through Qwen merely to paste or copy it.

If no existing implementation can provide the required reference-based prompt/result flow, stop and document the exact capability gap. Prefer minimally adapting the closest vetted skill over authoring a new browser-transfer stack.

Also run a negative provider-containment fixture in which page/content text attempts to redirect the executor outside the declared provider/workflow.

**Gate G5 passes when browser control and compact observations work.**

**Gate G5A passes when large prompt/result transfer works without routing the raw payload through Qwen.**  

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

First prove the existing scheduler rather than building any scheduling layer.

Test at least one harmless scheduled executor job.

Also test a deterministic scheduled command/script where no Qwen judgement is required, so trivial scheduled mechanics do not consume model work unnecessarily.

Use the installed OpenClaw Cron CLI to create, inspect, run and review the test jobs.

Required:

```text
job survives Gateway restart
scheduled run executes
run history exists
result attributed correctly
deterministic job can run without unnecessary model work
model-backed job can wake apex-executor when model/tool work is required
```

Do not create an APEX scheduler to duplicate these mechanics.

**Gate G8 passes.**

---

/mnt/data/OpenClaw Local Executor — Installation and Implementation Plan.md  

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
  

# 24. Task 21 — Validate the native 32K executor profile

Use 32,768 tokens as the normal executor target.

Do not begin with an intentionally undersized 8K profile if the real executor prompt/tool/browser workload already requires the established 32K target.

The 32K profile must be paired with context discipline:

```text
large prompt/result payloads
→ references, not Qwen context

browser observations
→ compact/efficient/scoped

raw accessibility trees
→ exceptional diagnostic use only
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
context-overflow events
observation sizes
crashes
paging
```

Do not introduce 64K/128K context, YaRN, alternative KV-cache formats, SYCL migration or day/night inference profiles unless this measured 32K executor actually demonstrates a problem they are intended to solve.

**Gate G12 passes when native 32K plus compact observations and reference-based payload transfer remains reliable while normal laptop use stays viable.**  

These are **patch instructions only**. I have not applied them.