---
title: "Platform Research Result V2 — Odysseus"
doc_type: platform_research_result
initiative: local-orchestration-engine
candidate: Odysseus
evidence_date: 2026-08-08
prompt: apex-meta/local-orchestration-engine/research-prompts/PLATFORM-RESEARCH-ODYSSEUS-2026-08-08-V2.md
status: "desk-research complete; local bake-off required; no implementation authorization"
---

# Platform Research Result V2 — Odysseus

## 1. Executive finding

**Strongest role:** **Odysseus as a specialized self-hosted local-model/tool workspace behind FEE for selected local execution flows, not the first-choice general execution runtime until browser/resume and shell-containment gaps are proven in bake-off.**

Current Odysseus is much more safety-conscious than the original APEX hypothesis implied. The current source contains server-side privileged-tool gating, per-turn tool policies, a fail-closed read-only plan mode, explicit prompt-injection wrappers for untrusted source data, and tested workspace confinement for file/search/edit tools. It also runs natively on Windows, supports Docker, local/API models, MCP, a Playwright browser MCP, shell/Python, persistent workspace features, tasks/calendar/email and extensive local-model serving integrations.

The strongest remaining APEX mismatch is that the platform is explicitly built around **autonomous agents that plan, call tools and keep working**. The agent preamble says tool blocks execute automatically; its rules tell the agent to retry failed tools or keep going until done/blocked. More importantly, current workspace confinement is not a general process sandbox: file/search helpers are confined, while shell/Python execution is still a privileged capability whose process cwd is merely set to the workspace. In Docker, container boundaries can reduce host exposure, but an APEX job still needs per-job roots, ro/rw scopes, action schemas, and deterministic argument validation outside the model.

Browser capability also remains less proven for the specific UF-A subscription workflow than OpenClaw or Hermes. Odysseus ships/auto-registers an optional Playwright MCP and has strong web/deep-research features, but current primary documentation does not establish persistent authenticated subscription sessions, exact artifact capture, or reliable crash/logout/CAPTCHA resume semantics.

**Biggest strength:** unusually integrated self-hosted local workspace with strong local-model support and improving server-side tool/prompt-security enforcement.

**Biggest blocker:** the current autonomy/shell model and lack of demonstrated durable authenticated-browser/action-resume behavior make it harder to map cleanly to the FEE bounded-executor contract without significant brokering.

**Overall confidence:** **79/100**. Source-level confidence on tool/prompt policy is high; browser and resumability confidence is materially lower.

---

## 2. Current runtime reality map

### Current official runtime reviewed

- Repository: `odysseus-dev/odysseus`.
- Repository created 2026-05-31; current default branch is **`dev`**; README states `dev` receives newest changes while `main` is the more curated branch.
- Current `dev` commit inspected: **`e4fa4ae5dd1d709ce4168397bd1d200fec1b2494`** (2026-08-07).
- No formal current GitHub release was returned by the releases API during this research pass; current source/default branch is therefore the main executable evidence.

| Capability | Current reality | Evidence type | APEX implication |
|---|---|---|---|
| Runtime | Self-hosted Python web workspace; Docker recommended; native installs supported | source/docs | Viable local runtime substrate |
| Windows | Native Windows launcher and manual Python path; core app runs natively | official setup docs | Strong G-P6 baseline |
| Local models | Ollama, llama.cpp/Cookbook and multiple OpenAI-compatible/local servers | official docs/source | Excellent model swapability |
| Agents | Multi-round autonomous tool loop; model writes/calls tool blocks | source-code verified | Control-plane overlap risk unless FEE bypasses/subordinates loop |
| Tool gating | Server-side non-admin blocklist for shell/Python/files/MCP/email/admin capabilities | source-code verified | Strong defense-in-depth |
| Plan mode | Explicit allowlist of read-only tools; unknown/new mutators fail closed; shell/Python blocked | source-code verified | Strong UF-C/read-only primitive |
| Per-turn tool policy | Disabled/hidden tools plus guide-only mode; enforcement outside prompt compliance | source-code verified | Useful bounded-tool substrate |
| Prompt-injection handling | Retrieved/web/email/tool/memory/skill content wrapped as untrusted data with inert-use policy | source-code verified | Strong defense-in-depth for G-P1, but not deterministic authority proof |
| Workspace confinement | Shared resolver confines read/write/edit/grep/glob/ls; traversal/outside-root and sensitive-file tests exist | source-code verified + tests | Strong single-workspace file containment |
| Shell/Python | Privileged tools; subprocess cwd follows workspace but workspace is not documented/tested as general process sandbox | source/tests | Must be hidden behind FEE wrappers/container isolation |
| Browser | Optional built-in Playwright MCP; web/deep-research surfaces | official setup docs/source | Browser automation exists, authenticated subscription reliability unproven |
| Sessions/personal features | Chat sessions, memory, tasks, calendar, email, scheduled agent tasks | official product docs | Strong UF-F workspace potential, but introduces extra orchestration/state surface |
| Audit/logs | Tool execution logging and app/server logs exist | source/docs | Raw evidence exists; FEE normalization required |
| License | AGPL-3.0-or-later | repository metadata/README | Operational/legal consideration if distributed/modified as network service |

---

## 3. Control-plane overlap analysis

Odysseus' public product model is intentionally broad:

```text
chat + autonomous agents
  plan -> choose tools -> execute -> retry -> continue until done/blocked
  + persistent memory
  + skills
  + tasks/calendar/scheduled agents
  + deep research
```

That is useful as a standalone personal AI workspace, but APEX already has:

```text
Weekly Orchestrator + Multi-Agent Orchestration
                |
                v
FEE frozen work packet / capability / evidence spine
                |
                v
bounded executor
```

The overlap is therefore **medium-high** if Odysseus is adopted as-is. It falls to **low-medium** only if FEE invokes a narrow runtime/tool surface and does not delegate planning, task scheduling, memory-driven workflow changes, or agent-defined next steps.

Odysseus' current agent rules explicitly encourage action and continued retries after tool failure. That behavior is nearly the inverse of the APEX requirement to attempt only declared bounded recovery and then emit an escalation packet. It must be overridden structurally, not merely by another prompt.

---

## 4. UF-A..UF-F evidence table

Scores are desk-research estimates, not measured bake-off results.

| Flow | Score | Confidence | Finding |
|---|---:|---:|---|
| **UF-A Subscription research executor** | **68** | 61 | Playwright MCP/browser capability exists, but current primary docs do not establish persistent logged-in subscription sessions, exact artifact capture, file-transfer behavior or restart/logout/CAPTCHA recovery. Deep Research is not the same user flow. |
| **UF-B Script failure recovery** | **82** | 80 | Shell/Python and rich tool execution exist, with server-side policy and agent retry behavior. FEE must replace open-ended retry/autonomous repair with pre-authorized wrappers and a closed recovery set. |
| **UF-C Detective evidence collection** | **87** | 86 | Plan mode's fail-closed read-only allowlist plus confined file/search tools are an excellent objective-evidence substrate. |
| **UF-D Database / knowledge hygiene** | **84** | 81 | Strong local files/documents/memory/database workspace and bounded file tools. Semantic ambiguity and transaction policy must remain FEE/rule-owned. |
| **UF-E Multi-repo / multi-folder execution** | **73** | 72 | Current workspace binding strongly confines shared file tools to one workspace, but the APEX requirement is multiple explicit roots with distinct ro/rw scopes. Shell/Python need additional containment. |
| **UF-F Personal weekly execution** | **82** | 79 | Odysseus is naturally strong in personal workspace features (tasks, notes, calendar, email, memory), but those features can become a competing planning/scheduling authority unless constrained behind the APEX trust profile. |

**Flow average: 79.3/100.** Hard gates override it.

---

## 5. Hard-gate table

| Hard gate | Result | Rationale |
|---|---|---|
| **G-P1 Authority containment** | **PASS_WITH_EXTERNAL_BROKER** | Source has good untrusted-context wrappers and server-side tool policy, but the autonomous agent still decides tool calls. FEE must provide the only action-ID/argument authority and keep captured text from expanding the action set. |
| **G-P2 Job-scoped permissions** | **PASS_WITH_EXTERNAL_BROKER** | Single-workspace file helpers are genuinely confined and traversal-tested. Multi-root ro/rw scopes and shell/Python containment are not equivalent; container/FEE brokering is required. |
| **G-P3 Resumability** | **UNKNOWN** | Chat/session persistence exists, but current primary evidence reviewed here does not establish durable in-flight work-packet/action resume after app/browser/model restart with duplicate-safe consequential operations. Must be measured. |
| **G-P4 Evidence capture** | **PASS_WITH_EXTERNAL_BROKER** | Tool execution/server logs and session artifacts exist, but an APEX-grade immutable action/provenance/checkpoint ledger is not demonstrated as a native contract. FEE can capture/normalize it. |
| **G-P5 Safe escalation** | **PASS_WITH_EXTERNAL_BROKER** | Agent rules support a BLOCKED state, but also explicitly encourage retries and continued action after failures. FEE must impose hard retry ceilings and closed escalation classes outside the model loop. |
| **G-P6 Practical Windows viability** | **PASS** | Core app runs natively on Windows 10/11 with Python; agent shell additionally needs Git for Windows/bash. Ollama is the simplest local-model path on Windows. |

**Odysseus remains bake-off eligible but cannot become the primary execution runtime while G-P3 remains UNKNOWN.**

---

## 6. Weighted score + confidence

| Dimension | Score | Weight | Evidence note |
|---|---:|---:|---|
| FIT | 79 | 18 | Strong local workspace, weaker exact UF-A/resume fit |
| BOUND | 76 | 15 | Strong improving source-level controls; shell/action broker still needed |
| BROWSER | 62 | 14 | Playwright MCP exists; authenticated subscription fixture unproven |
| TOOLS | 90 | 12 | Rich files/shell/Python/MCP/app tooling |
| RECOVERY | 72 | 10 | Agent retry behavior exists; durable deterministic resume unproven |
| AUDIT | 74 | 9 | Logs/tool events available; canonical evidence spine external |
| MULTIROOT | 72 | 8 | Strong single workspace, multi-root differentiated scopes not demonstrated |
| LOCALMODEL | 94 | 5 | Core strength; broad local serving/endpoints |
| WINDOWS | 86 | 4 | Native core + Ollama path; shell/browser deps add friction |
| RESOURCE | 65 | 3 | No operator-machine coexistence measurements |
| MAINT | 50 | 2 | Very young, highly active project with large issue/PR surface |

**Weighted score: 75.8/100.**  
**Score confidence: 75/100.**

---

## 7. Windows/browser/tool-permission/local-model/resume findings

### Windows

**Finding: PASS for the core runtime.**

Official setup supports native Windows through `launch-windows.ps1` or Python 3.11+. The core chat/agent/memory/documents/email/calendar/deep-research application runs natively. The agent shell requires Git for Windows (`bash.exe`). Local vLLM/SGLang serving remains Linux/WSL2-oriented; existing Windows Ollama is the simplest local backend.

This is practical enough for bake-off, but resource coexistence still needs direct measurement.

### Browser

**Finding: capability exists; subscription-session fit remains UNKNOWN.**

Odysseus can auto-register an optional `@playwright/mcp` browser server for navigation/screenshots/vision after its package is cached. That proves browser automation plumbing, not the required UF-A reliability profile. The reviewed primary docs do not establish:

- persistent authenticated browser profiles across restarts;
- provider-specific subscription handling;
- file uploads/downloads and exact result capture;
- safe CAPTCHA/logout/security-challenge stops;
- duplicate-safe resume of an interrupted browser job.

Those are mandatory local fixtures, not assumptions.

### Permission model

**Finding: surprisingly strong for file/read-only modes, insufficient for arbitrary processes without FEE/container controls.**

Current source provides:

- non-admin blocking of shell/Python/file/MCP/email/admin tools;
- fail-closed plan-mode read-only allowlist;
- per-turn disabled/hidden tool policy enforced server-side;
- shared workspace resolver for file/search tools;
- traversal/outside-root denial tests;
- sensitive-file denial/enumeration tests;
- untrusted-source prompt wrappers.

However, the agent-loop preamble still gives tools to the model and executes tool blocks automatically. The workspace test suite confirms subprocess cwd is set to the workspace; that is not the same as a process sandbox. A bash process can only be considered bounded if it executes inside an externally controlled container/wrapper with explicit resources.

### Local-model fit

**Finding: strongest dimension.**

Odysseus is explicitly designed for local models, includes a hardware-aware Cookbook and supports Ollama and other local/OpenAI-compatible serving approaches. This makes it attractive as a local-model workspace and useful as a test harness even if it does not win the executor-runtime role.

### State and resumability

**Finding: insufficient primary evidence for G-P3.**

Sessions and persistent workspace data exist, but the required APEX semantic is stronger: after process/browser/model restart, resume a frozen work packet from an exact checkpoint without repeating a consequential action. That behavior was not established from current source/docs in this pass and therefore remains UNKNOWN rather than inferred.

---

## 8. Best Odysseus composition with FEE

```text
Subscription / deep-reasoning layer
              |
              v
APEX/FEE deterministic spine
  frozen work packet
  action_id + schema validation
  multi-root ro/rw capability map
  deterministic retry/stop policy
  checkpoint + evidence ledger
              |
              v
Odysseus narrow runtime/workspace layer
  local-model endpoint management
  selected read-only file/search tools
  selected bounded data/document tools
  Playwright MCP only when work packet authorizes it
  shell/Python hidden unless invoked through FEE wrapper/container
  memory/task/planning/scheduling excluded from execution authority
              |
              v
bounded local operator
              |
              +--> blocked/auth/security/unknown -> FEE escalation
```

### Odysseus should own, if selected

- local-model endpoint/workspace integration;
- selected file/search/data/document mechanics;
- optional browser MCP mechanics after fixture validation;
- possibly read-only Detective evidence tooling;
- raw runtime logs/events as evidence inputs.

### FEE must retain

- strategy, work-packet sequence and completion authority;
- action registry and argument validation;
- multi-root scopes and container/process boundaries;
- browser provider/session policy;
- retry/recovery limits;
- restart/resume checkpoint semantics;
- canonical evidence ledger;
- escalation and trust-zone policy.

---

## 9. External brokers/wrappers required

1. **FEE action broker** — converts authorized action IDs to specific Odysseus tools and validates every argument independently.
2. **Process sandbox wrapper** — shell/Python only through a job container or equivalent restricted process surface; workspace cwd alone is insufficient.
3. **Multi-root capability compiler** — maps multiple job roots with distinct read/write scopes; must not expose host-global paths.
4. **Browser/session adapter** — establishes persistent provider sessions, artifact transfer and safe stop conditions if Playwright MCP can meet them.
5. **Checkpoint/resume controller** — FEE-owned durable action state with idempotency/duplicate prevention.
6. **Evidence normalizer** — records tool/browser/model events and produced artifacts into FEE's canonical ledger.
7. **Autonomy suppressor** — bypasses or caps Odysseus planning/memory/task/self-evolving-skill behaviors for FEE execution jobs.

---

## 10. Rejected roles and trade-offs

### Rejected: Odysseus as APEX orchestration/project-management authority

Its autonomous agents, scheduled tasks, memory and self-evolving skills overlap too strongly with already-owned APEX control planes.

### Rejected: generic Odysseus agent loop as the primary FEE executor

Current source explicitly lets the model decide tool use and encourages continued action/retry after failures. That is not the frozen-plan bounded-recovery model.

### Rejected: workspace cwd as sufficient shell containment

Current code/tests establish strong file-tool confinement but only set process cwd for Python/shell execution. FEE must impose a real process/container boundary.

### Rejected: assume Deep Research equals UF-A

Deep Research is useful, but UF-A specifically requires authenticated subscription surfaces, deterministic prompt submission, exact capture, session errors and resumability. Those properties remain unproven.

### Rejected: production primary-runtime selection before resume test

G-P3 remains UNKNOWN from desk evidence.

---

## 11. Unknowns and minimal bake-off tests

### Material unknowns

- persistent authenticated subscription browser behavior;
- file upload/download and exact-output capture through browser MCP;
- crash/browser/model restart and duplicate-safe action resume;
- shell/Python containment under a practical Windows deployment;
- multi-root differentiated ro/rw scopes;
- whether generic agent planning/tool continuation can be fully bypassed for FEE jobs;
- event/provenance completeness for canonical evidence reconstruction;
- operator-laptop resource coexistence;
- maintenance stability of a very young rapidly changing codebase.

### Minimal tests

1. **UF-A browser fixture** — persistent logged-in subscription profile, prompt submit/capture, file transfer, restart, logout and CAPTCHA stop.
2. **Read-only Detective fixture** — run plan mode against a repo and verify no mutating/MCP/shell tool is callable.
3. **Workspace escape fixture** — file helpers reject parent/absolute escape and sensitive files; verify shell/Python also cannot escape when FEE wrapper/container is active.
4. **Multi-root fixture** — A rw, B ro, C forbidden, with both file and process tools.
5. **Hostile-source fixture** — web/document/tool output requests new tools/paths; verify FEE action set remains unchanged.
6. **Failure-recovery fixture** — one declared retry path, then BLOCKED/escalation; prove the native agent loop cannot continue autonomously outside the closed set.
7. **Restart/resume fixture** — kill Odysseus/browser/model mid-job and verify exact FEE checkpoint resume with no duplicated consequential action.
8. **Evidence reconstruction fixture** — reproduce action/provenance history from FEE ledger plus Odysseus event/log references.
9. **Windows coexistence fixture** — browser + Odysseus + chosen local model + normal development workload; record peak memory/CPU/GPU and interventions.

---

## 12. Source appendix

### APEX authority sources

- `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md`
- `apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md`

### Current Odysseus primary sources reviewed 2026-08-08

- Repository/default-branch metadata: https://github.com/odysseus-dev/odysseus
- Current dev README: https://github.com/odysseus-dev/odysseus/blob/dev/README.md
- Setup/Windows/security/browser-MCP docs: https://github.com/odysseus-dev/odysseus/blob/dev/docs/setup.md
- Current dev commit inspected: https://github.com/odysseus-dev/odysseus/commit/e4fa4ae5dd1d709ce4168397bd1d200fec1b2494
- Agent loop: `src/agent_loop.py`
- Tool security: `src/tool_security.py`
- Per-turn tool policy: `src/tool_policy.py`
- Prompt-injection hardening: `src/prompt_security.py`
- Workspace confinement tests: `tests/test_workspace_confine.py`
- Security policy: `SECURITY.md`
- Project landing page: https://odysseus-dev.github.io/odysseus/

---

## 13. Machine-readable result

```yaml
platform_research_result:
  candidate: Odysseus
  evidence_date: 2026-08-08
  versions_or_commits_reviewed:
    - "dev e4fa4ae5dd1d709ce4168397bd1d200fec1b2494"
    - "main identified as curated branch; dev is current default"
  runtime_reality:
    self_hosted_workspace: true
    autonomous_agent_loop: true
    local_model_focus: strong
    native_windows_core: true
    docker_recommended: true
    server_side_tool_policy: true
    fail_closed_plan_mode: true
    untrusted_context_wrapper: true
    single_workspace_file_confinement: true
    general_process_sandbox_from_workspace: false
    authenticated_subscription_resume: unproven
  per_user_flow_scores:
    UF-A: 68
    UF-B: 82
    UF-C: 87
    UF-D: 84
    UF-E: 73
    UF-F: 82
  weighted_scores:
    FIT: 79
    BOUND: 76
    BROWSER: 62
    TOOLS: 90
    RECOVERY: 72
    AUDIT: 74
    MULTIROOT: 72
    LOCALMODEL: 94
    WINDOWS: 86
    RESOURCE: 65
    MAINT: 50
    total: 75.8
  score_confidence:
    total: 75
    tool_policy: 90
    browser_subscription_fit: 55
    resumability: 45
  hard_gate_results:
    authority_containment: PASS_WITH_EXTERNAL_BROKER
    job_scoped_permissions: PASS_WITH_EXTERNAL_BROKER
    resumability: UNKNOWN
    evidence_capture: PASS_WITH_EXTERNAL_BROKER
    safe_escalation: PASS_WITH_EXTERNAL_BROKER
    practical_windows_viability: PASS
  windows_fit:
    status: viable_native_core
    shell_requirement: "Git for Windows/bash.exe"
    recommended_local_model_path: Ollama
    resource_measurement_required: true
  browser_fit:
    playwright_mcp_available: true
    authenticated_subscription_persistence: unknown
    file_transfer_and_exact_capture: unknown
    restart_resume: unknown
  local_model_fit:
    status: excellent
    cookbook: true
    Ollama: true
    OpenAI_compatible_endpoints: true
  permission_model:
    non_admin_privileged_tool_blocking: true
    plan_mode_readonly_allowlist: true
    per_turn_tool_deny_policy: true
    file_workspace_confinement: true
    shell_process_confinement_from_workspace: false
    fee_broker_required: true
  state_and_resumability:
    chat_sessions_exist: true
    durable_action_resume_proven: false
    hard_gate_status: UNKNOWN
    fee_checkpoint_required: true
  audit_and_evidence:
    tool_execution_logging: true
    app_server_logs: true
    canonical_fee_ledger_native: false
  duplicated_orchestration_risk:
    full_odysseus_workspace: medium_high
    narrow_runtime_subset: low_medium
  strongest_role: "specialized local-model/tool workspace behind FEE for selected flows; not primary general executor until browser/resume bake-off passes"
  required_external_brokers:
    - FEE action-id and argument-validation broker
    - process sandbox wrapper
    - multi-root capability compiler
    - browser/session adapter
    - checkpoint/resume idempotency controller
    - evidence normalizer
    - autonomy suppressor
  unresolved_unknowns:
    - authenticated subscription browser reliability
    - file transfer through browser path
    - durable duplicate-safe resume
    - shell/Python Windows containment
    - multi-root differentiated scopes
    - complete bypass of autonomous continuation
    - evidence completeness
    - Windows resource coexistence
  benchmark_tests_required:
    - UF-A authenticated browser fixture
    - plan-mode read-only fixture
    - workspace/process escape fixture
    - multi-root ro/rw/forbidden fixture
    - hostile-source inertness fixture
    - bounded failure-recovery fixture
    - restart/resume idempotency fixture
    - evidence reconstruction fixture
    - Windows resource coexistence fixture
  rejected_roles:
    - APEX orchestration brain
    - generic autonomous agent loop as primary executor
    - workspace cwd as shell sandbox
    - Deep Research treated as equivalent to UF-A
    - production primary selection before G-P3 resolution
  reversal_triggers:
    - authenticated browser proves materially stronger than desk evidence
    - durable action resume is demonstrated cleanly
    - process/multi-root containment can be configured more simply than expected
    - alternatively any hostile-content/tool bypass is observed
    - maintenance burden exceeds competing compositions
  overall_confidence_0_to_100: 79
```
