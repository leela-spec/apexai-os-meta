---
title: "OpenClaw Local Executor — Operator Decision Lock"
doc_type: operator_decision_lock
initiative: local-executor
created: 2026-08-10
status: operator-verified
branch_policy: main-only
supersedes:
  - FEE as a separate runtime/service/agent between APEX and OpenClaw
  - browser-only OpenClaw executor assumptions
  - OpenClaw cron/automations disabled assumptions
  - OpenClaw skill watcher disabled assumptions
---

# OpenClaw Local Executor — Operator Decision Lock

## 1. Decision summary

The target architecture is:

```text
APEX OS + project repositories
  reasoning agents
  orchestration flows
  planning
  prompts
  evaluation
  operator gates
        |
        | approved execution request
        v
+------------------------------------------+
| LOCAL EXECUTOR                           |
|                                          |
|          OpenClaw + Qwen3-8B             |
|                                          |
| skills / automations / sessions          |
| browser / exec / scripts / files / Git   |
+-------------------+----------------------+
                    |
          +---------+---------+----------+
          |                   |          |
          v                   v          v
 subscription AIs         scripts      repositories
 ChatGPT/Gemini/...      Python/PS       Git
          |                   |          |
          +---------+---------+----------+
                    |
                    v
          results + evidence + status
                    |
                    v
           owning reasoning workflow
```

**OpenClaw + Qwen is one operational entity: the Local Executor.**

OpenClaw is the persistent runtime, scheduler, skills/tool host, browser controller, session manager and execution environment. Qwen is the local model providing the bounded intelligence needed to operate those capabilities.

They should not be represented as two independent architecture agents.

OpenClaw's native agent runtime already owns the agent loop, tool wiring, workspace and session store, while its official llama.cpp provider can perform local GGUF inference directly inside the OpenClaw process.

---

# 2. FEE decision

## DEC-OC-01 — Drop FEE as a separate subsystem

**Decision: LOCKED**

There will be **no separate FEE runtime, FEE agent, FEE daemon or FEE orchestration layer** between APEX and OpenClaw.

Previous useful FEE concepts are retained but redistributed to the systems that actually own them.

### Concepts that move into APEX / project workflows

- execution-request structure;
- workflow identity;
- project/repository ownership;
- approved plan;
- allowed roots;
- allowed actions;
- success conditions;
- stop conditions;
- operator gates;
- expected result location;
- workflow continuation logic.

### Concepts that move into OpenClaw configuration / skills

- browser operating procedures;
- tool usage;
- script execution procedures;
- Git execution procedures;
- UI recovery;
- task execution;
- runtime sessions;
- automation schedules;
- model/tool configuration.

### Concepts that become deterministic APEX helper scripts where necessary

- safe Git wrappers;
- path/root validation;
- safe script invocation;
- exact transformations;
- schema validation;
- other low-level guards that should not depend on model judgement.

Existing `scripts/fee` code must **not be deleted merely because the FEE name is deprecated**. It must later be audited component by component. Useful mechanisms may be migrated/renamed into APEX execution helpers; obsolete mechanisms may then be archived or removed.

The existing project design correctly identified work packets, capabilities, roots, evidence and checkpoints as important execution controls, but this decision supersedes the assumption that those controls require a separately named FEE runtime.

---

# 3. Workflow ownership

## DEC-OC-02 — Federated workflow ownership

**Decision: LOCKED CONCEPT; STORAGE DESIGN DEFERRED**

There will not be one mandatory global execution queue.

Some workflows will naturally belong to `apexai-os-meta`, for example:

- Weekly Orchestration;
- Meta Ops;
- cross-project orchestration;
- shared research processes;
- global maintenance.

Other workflows will naturally belong to individual repositories.

Example:

```text
apexai-os-meta/
  orchestration state
  cross-project workflows

project-a/
  project-local workflows
  implementation state

project-b/
  project-local workflows
  release/research state
```

The exact durable queue/storage topology will be designed later.

What must be common is only the **execution interface** through which any owning workflow invokes the Local Executor.

---

# 4. Reasoning authority

## DEC-OC-03 — Reasoning models own substantive decisions

**Decision: LOCKED**

Subscription/deep-reasoning models and the existing APEX orchestration systems decide:

- what should happen;
- which research is needed;
- which prompt to use;
- which provider/model to use;
- whether a result is acceptable;
- whether another iteration is required;
- what the next project step is.

The Local Executor does not independently redesign a workflow.

Qwen may reason only as necessary to perform an approved operational action, including bounded UI adaptation, failure classification and declared recovery.

This continues the authority boundary already locked in the local-model decisions. 

---

# 5. Executor identity

## DEC-OC-04 — OpenClaw + Qwen = Local Executor

**Decision: LOCKED**

OpenClaw and Qwen are treated as one operational worker.

Technical decomposition:

```text
Local Executor
├── OpenClaw
│   ├── persistent Gateway
│   ├── sessions
│   ├── skills
│   ├── automations
│   ├── browser
│   ├── exec/process
│   ├── filesystem tools
│   └── runtime evidence
│
└── Qwen3-8B
    └── bounded local tool-selection/recovery intelligence
```

OpenClaw's official llama.cpp provider supports in-process local GGUF inference and returns model-generated tool calls to OpenClaw for execution rather than executing them inside the model runtime.

---

# 6. Local model topology

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

# 7. Scheduling

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

# 8. Immediate execution

## DEC-OC-07 — Push/dispatch is the normal continuation mechanism

**Decision: LOCKED**

When a reasoning workflow creates new executable work, it should not normally wait for polling.

The owning workflow invokes the Local Executor immediately.

Target pattern:

```text
reasoning completes
      |
creates execution request
      |
      v
OpenClaw executor invoked
      |
      v
execution begins
```

OpenClaw supports direct agent execution from a message or UTF-8 message file, including an explicit agent/session target.

A later Automation-based watchdog may detect missed pending jobs, but polling is not the primary dispatch mechanism.

---

# 9. Pending work/state

## DEC-OC-08 — Exact storage topology deferred

**Decision: DEFERRED**

No global queue architecture will be selected during OpenClaw installation.

Workflow state may live in:

- `apexai-os-meta`;
- individual project repositories;
- later dedicated execution-state locations where evidence justifies them.

OpenClaw owns its own runtime/session/Automation state, but project workflow state remains owned by the corresponding project/orchestration system.

---

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

---

# 11. Root authority

## DEC-OC-10 — Explicit project/repository roots

**Decision: LOCKED**

Execution requests declare which repositories/folders are relevant and whether each is read-only or read/write.

Machine-wide implicit authority is not granted merely because OpenClaw runs under the operator's Windows account.

Exact enforcement implementation will combine:

- workflow declarations;
- OpenClaw tool policy;
- trusted APEX-owned execution helpers where deterministic enforcement is required.

---

# 12. Git authority

## DEC-OC-11 — Capability-based Git including push

**Decision: LOCKED**

An approved execution request may grant:

```text
git.read
git.write
git.stage
git.commit
git.push
```

For `apexai-os-meta`, work is performed directly on `main` unless the operator explicitly changes that policy.

Default-prohibited operations include:

```text
force push
reset --hard
destructive history rewriting
branch deletion
unrequested branch/worktree creation
```

Git push is therefore **not globally prohibited**. It is allowed when the approved workflow grants it.

---

# 13. Bounded code repair

## DEC-OC-12 — Micro-fix authority retained

**Decision: LOCKED**

Qwen may perform a bounded local repair when:

- the repository/root is declared;
- files/surface are bounded;
- no architecture redesign is required;
- acceptance tests exist;
- one local inferred-fix attempt is permitted;
- unexpected scope/failure causes escalation.

This preserves the previously verified R3 micro-fix envelope. 

---

# 14. Browser

## DEC-OC-13 — Dedicated signed-in Chrome profile is primary

**Decision: LOCKED**

Primary:

```text
Dedicated Chrome user profile
        +
OpenClaw official Chrome extension
```

The profile contains the logged-in subscription-AI sessions required for execution.

Fallback:

```text
OpenClaw-managed isolated browser
```

The official extension lets OpenClaw control signed-in Chrome tabs without requiring the standard remote-debugging approval prompt.

This also matches the previously supplied browser-automation research, which established Chrome/session control, prompt submission, response extraction and scheduled browser workflows as appropriate OpenClaw capabilities.

---

# 15. Browser authority

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

## DEC-OC-14A — Browser containment is enforced before tool execution

**Decision: LOCKED**

Provider containment is not delegated to Qwen, a skill, or page-level instructions. The validated dispatcher must establish a request-scoped browser policy before the agent turn. That policy binds the OpenClaw session to exactly one explicitly shared tab, browser profile, provider hostname, and expiry.

An APEX-owned OpenClaw plugin must enforce the policy through OpenClaw's official `before_tool_call` hook. Browser calls fail closed before execution when the policy is missing or expired, the agent/session does not match, the requested profile or tab differs, a navigation target leaves the declared hostname, or the current tab can no longer be verified inside the declared hostname.

The request-scoped policy is stored outside the agent workspace. Qwen may read the authorized values supplied to its turn but cannot create, widen, or replace the enforcement policy. The dispatcher owns policy creation and cleanup; the plugin owns enforcement. Skills remain operating guidance rather than security boundaries.

The bundled `browser-automation` skill remains the source for general browser mechanics. The APEX-owned `subscription-ai-browser` skill adds only provider-specific state verification, exact prompt insertion, completion detection, and verbatim capture for ChatGPT, Perplexity, and Gemini. No community skill is required for the initial provider lane.

---

# 16. Skills

## DEC-OC-15 — Skill watcher stays enabled

**Decision: LOCKED**

`skills.load.watch` remains enabled for trusted APEX-owned skill roots.

OpenClaw currently defaults this setting to `true` and refreshes its skill snapshot when `SKILL.md` files change.

Execution evidence should record the relevant Git commit/config identity rather than disabling iterative skill loading.

---

# 17. Skill ownership

## DEC-OC-16 — APEX-owned skills first

**Decision: LOCKED**

The executor primarily uses skills maintained inside the APEX/project repositories.

Community ClawHub skills are not a dependency of the initial architecture.

Reusable OpenClaw-native mechanics may still be used, particularly the bundled browser/browser-automation functionality. OpenClaw's browser plugin includes dedicated guidance for stable tab selection, snapshot-before-action, stale-reference recovery and reporting login/2FA/CAPTCHA blockers rather than guessing.

---

# 18. Automation-authority boundary

## DEC-OC-17 — Workflows define schedules; executor executes them

**Decision: LOCKED**

Qwen does not autonomously invent persistent schedules.

A reasoning/workflow layer may propose a recurring execution schedule.

A trusted operator/APEX mechanism then creates or updates the corresponding OpenClaw Automation.

OpenClaw Automation jobs store explicit tool policies, and an agent-created job cannot widen its tool set beyond the creating turn.

---

# 19. Local model fallback

## DEC-OC-18 — No cloud fallback initially

**Decision: LOCKED**

The executor initially uses Qwen3-8B only.

If it cannot perform the approved task:

```text
fail / block
   |
   v
return evidence
   |
   v
reasoning layer / CLI / operator
```

It does not silently switch to a cloud reasoning model.

A later benchmark-certified local-model registry may replace this single-model policy.

---

# 20. Local inference concurrency

## DEC-OC-19 — One active Qwen inference lane initially

**Decision: LOCKED**

The initial executor runs one active local-model action lane at a time.

Multiple workflows may be scheduled, waiting on browser activity, checkpointed or otherwise pending, but only one Qwen inference/action lane is active concurrently until resource and reliability measurements justify a wider limit.

This preserves laptop coexistence and makes tool/browser failures easier to attribute during the first production phase.

---

# 21. Final system law

The system can be summarized as:

> **APEX and individual projects decide what needs to happen. OpenClaw + Qwen is one persistent local executor that performs approved browser, script, filesystem and Git work either immediately or on an OpenClaw Automation schedule. Results return to the workflow that owns the reasoning.**

There is **no separate FEE execution service**.

Unknown future storage topology is intentionally deferred rather than allowing it to block installation of the Local Executor.
