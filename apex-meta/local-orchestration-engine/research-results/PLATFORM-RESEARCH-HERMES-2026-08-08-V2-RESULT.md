---
title: "Platform Research Result V2 — Hermes"
doc_type: platform_research_result
initiative: local-orchestration-engine
candidate: Hermes
evidence_date: 2026-08-08
prompt: apex-meta/local-orchestration-engine/research-prompts/PLATFORM-RESEARCH-HERMES-2026-08-08-V2.md
status: "desk-research complete; local bake-off required; no implementation authorization"
---

# Platform Research Result V2 — Hermes

## 1. Executive finding

**Strongest role:** **Hermes as a bounded tool/browser/session runtime behind the FEE authority/evidence spine, with autonomous planning/memory behavior minimized and dangerous local actions forced through FEE wrappers.**

Hermes is a substantially stronger current platform than the earlier research hypothesis implied. The current release provides native Windows 10/11 support, multiple local/cloud browser backends, persistent authenticated browser profiles, rich terminal/file/tool capabilities, Docker execution isolation, durable SQLite session history with full tool calls/results, profiles, local-model backends, checkpoints, signed lifecycle webhooks, and active recovery/approval mechanisms.

The key limitation is structural rather than feature-related: **Hermes profiles are explicitly not sandboxes**. With the default local terminal backend, the agent has the same filesystem access as the OS user, and `terminal.cwd` is only a starting directory. Hermes also defaults toward a capable autonomous agent experience: smart approval is model-assisted, tool self-recovery is extensive, and the current release raised the default tool-calling iteration ceiling substantially. That is useful for generic agent work but is not the APEX trust model.

Therefore Hermes should not itself decide the execution envelope. FEE must retain the frozen work packet, allowed action IDs, argument validation, root scopes, retry budget, checkpoints, evidence ledger and stop/escalation policy. Hermes may supply the runtime mechanics underneath those contracts.

**Biggest strength:** a very broad and current runtime stack with unusually good Windows support, local-model/provider flexibility, durable sessions and multiple browser modes.

**Biggest blocker:** native host profiles do not enforce filesystem boundaries; APEX-grade job containment requires Docker/external brokering plus FEE-generated permissions rather than relying on profile prompts or working directories.

**Overall confidence:** **82/100**. Confidence is highest for Windows/session/tool reality and lower for authenticated subscription reliability, browser file-transfer coverage and operator-laptop resource coexistence.

---

## 2. Current runtime capability map

### Current official runtime reviewed

- Current released line reviewed: **Hermes Agent v0.20.0 / tag `v2026.8.3`**, published 2026-08-03.
- Current `main` inspected on 2026-08-08: **`973c14b57c10874138b9696a2b300cc2f89e40e3`**.
- Current official documentation reviewed for Windows, profiles, tools/configuration, sessions, Docker terminal backend, browser automation, checkpoints, and provider/local-model support.

| Capability | Current reality | Evidence type | APEX implication |
|---|---|---|---|
| Windows | Native Windows 10/11 supported; PowerShell installer; no WSL/Docker required for base install | officially documented | Strong G-P6 baseline |
| Profiles | Separate Hermes config/state/session/memory/log/gateway namespaces | officially documented | Useful project/personal separation primitive |
| Profile isolation | Profiles **do not** sandbox filesystem access; local backend retains OS-user access | officially documented | G-P2 requires Docker/external FEE broker |
| Terminal | Local default plus Docker and other backends; Docker can isolate commands in persistent container | officially documented | Strong bounded executor substrate when local backend is not exposed directly |
| Docker mounts | Sandbox stays isolated unless cwd/workspace or explicit volumes are mounted | officially documented | FEE can compile job roots into explicit mounts |
| Sessions | `state.db` SQLite/WAL stores full messages, tool calls/results, model/config, timestamps; resume/search supported | officially documented | Strong evidence/session continuity input |
| Checkpoints | Tool/file/destructive-operation checkpoint/rollback capability exists; not the APEX job-state authority | officially documented | Useful secondary recovery layer |
| Browser | Browserbase, Browser Use, Firecrawl, Camofox, local Chromium CDP, local agent-browser | officially documented | Broad UF-A capability surface |
| Browser persistence | Camofox can use profile-scoped persistent identity; local Chromium CDP can use operator's live cookies/sessions | officially documented | Strong authenticated-session potential |
| Browser limitation | Official browser docs state **no file downloads** | officially documented | Material UF-A limitation; external/provider adapter may be required |
| Tool controls | Tools can be enabled/disabled; approval modes and unconditional deny patterns exist | officially documented | Useful defense-in-depth; FEE action schema remains primary authority |
| Approval model | Smart approval is default and uses auxiliary model judgement for flagged commands; manual/off also exist | officially documented | Do not use smart approval as APEX authority boundary |
| Audit/events | Sessions preserve tool events; current release adds signed lifecycle webhooks for session/turn/tool events | release + docs | Strong feed into FEE evidence normalizer |
| Local models | Ollama, LM Studio and custom/OpenAI-compatible endpoints supported | officially documented | Strong model swapability |
| Autonomous recovery | Current release emphasizes tool self-recovery and higher iteration ceiling | official release | Must be subordinated to FEE's bounded recovery ladder |

### Documentation contradiction preserved

One provider/local-model guide still contains older Unix/WSL-oriented wording, while the dedicated current Windows guide explicitly states native Windows 10/11 operation. For the platform decision, the dedicated Windows guide and current Windows installer are the more specific current evidence. The stale wording is still a documentation-maintenance signal and should be checked during installation.

---

## 3. UF-A..UF-F evidence table

Scores are evidence-based desk estimates, not local benchmark results.

| Flow | Score | Confidence | Finding |
|---|---:|---:|---|
| **UF-A Subscription research executor** | **84** | 73 | Multiple browser backends and persistent authenticated profiles are strong. Local CDP can operate the operator's live browser. However official docs state browser downloads are unsupported, and exact login/logout/CAPTCHA/output-capture behavior is unmeasured. |
| **UF-B Script failure recovery** | **88** | 84 | Rich terminal execution, persistent process/sandbox options, checkpoints and tool self-recovery are strong. FEE must constrain recovery to declared routes rather than Hermes' generic autonomous repair behavior. |
| **UF-C Detective evidence collection** | **90** | 87 | Filesystem/terminal/browser evidence plus complete persisted tool calls/results and event hooks fit objective evidence collection well. Judgement must remain upstream. |
| **UF-D Database / knowledge hygiene** | **84** | 80 | File/tool primitives and containerized execution are strong for bounded transformations; deterministic transactions/dry-run and ambiguity queues remain FEE/tool-specific responsibilities. |
| **UF-E Multi-repo / multi-folder execution** | **76** | 78 | Docker volumes can expose explicit roots, but native profiles/cwd do not enforce root boundaries. Multi-root ro/rw policy must be compiled externally and tested. |
| **UF-F Personal weekly execution** | **78** | 76 | Profiles cleanly isolate Hermes state and can isolate tool HOME, but host credentials/filesystem are shared by default and `HERMES_REAL_HOME` remains exposed. A stricter personal trust profile needs container/credential brokering. |

**Flow average: 83.3/100.** Hard gates remain decisive.

---

## 4. Hard-gate table

| Hard gate | Result | Rationale |
|---|---|---|
| **G-P1 Authority containment** | **PASS_WITH_EXTERNAL_BROKER** | Individual tools can be disabled and deny patterns exist, but default smart approvals and broad agent/tool behavior are not equivalent to externally frozen action IDs. FEE must expose only authorized wrappers and independently validate arguments. |
| **G-P2 Job-scoped permissions** | **PASS_WITH_EXTERNAL_BROKER** | Official docs explicitly say profiles and `terminal.cwd` do not sandbox. Docker terminal isolation and explicit volumes provide a viable substrate, but FEE must create and enforce the per-job mount/capability set. |
| **G-P3 Resumability** | **PASS_WITH_EXTERNAL_BROKER** | Durable SQLite sessions, resume/search, persistent browser-profile modes and checkpoints provide strong continuity. FEE must still own the canonical work-packet checkpoint so conversational resume cannot alter execution sequence or duplicate consequential actions. |
| **G-P4 Evidence capture** | **PASS** | Full messages/tool calls/results, timestamps, runtime logs and signed tool/session lifecycle webhooks provide sufficient raw evidence for FEE normalization. |
| **G-P5 Safe escalation** | **PASS_WITH_EXTERNAL_BROKER** | Approval/denial controls and user clarification exist, but Hermes is intentionally optimized for self-recovery and long autonomous tool loops. FEE must impose the closed recovery set and terminal stop/escalation classes. |
| **G-P6 Practical Windows viability** | **PASS** | Native Windows 10/11 is explicitly supported. Browser dependencies and local inference still require operator-machine coexistence measurement. |

**No unmitigated desk-research hard-gate failure found if Docker/external brokering is part of the composition.** Native local-terminal Hermes by itself would not satisfy APEX job-scoped permission requirements.

---

## 5. Weighted score + confidence

| Dimension | Score | Weight | Evidence note |
|---|---:|---:|---|
| FIT | 82 | 18 | Broad coverage, especially tools/session/runtime |
| BOUND | 70 | 15 | Strong controls but native host profile is not a sandbox |
| BROWSER | 82 | 14 | Rich backends/persistence; no-download limitation and reliability unknowns |
| TOOLS | 91 | 12 | Very broad terminal/file/browser/tool surface |
| RECOVERY | 88 | 10 | Strong session/checkpoint/self-recovery primitives |
| AUDIT | 90 | 9 | Full tool history + current signed lifecycle webhooks |
| MULTIROOT | 70 | 8 | Achievable with Docker volumes/external compiler, not native profile boundary |
| LOCALMODEL | 90 | 5 | Ollama/LM Studio/custom compatible endpoints |
| WINDOWS | 92 | 4 | Explicit native support |
| RESOURCE | 65 | 3 | No operator-machine measurement yet |
| MAINT | 52 | 2 | Very fast-moving, large platform; integration pinning required |

**Weighted score: 81.3/100.**  
**Score confidence: 79/100.**

---

## 6. Windows/browser/tool-permission/local-model/resume findings

### Windows

**Finding: strong documented fit.**

The current Windows guide explicitly supports native Windows 10/11 and a PowerShell installer into `%LOCALAPPDATA%\hermes` without administrator rights. That gives APEX a realistic native path rather than requiring WSL solely to run Hermes. Docker remains valuable specifically as an execution sandbox even when Hermes itself runs natively.

The bake-off must measure browser + Hermes + local model + development-tool coexistence on the operator hardware before selecting the exact deployment form.

### Browser

**Finding: feature-rich but not yet complete for UF-A.**

Hermes currently offers:

- cloud browser modes;
- local agent-browser/Chromium;
- local authenticated Chrome/Edge/Brave/Chromium via CDP;
- Camofox with persistent profile-scoped cookies/logins;
- headed mode for human-visible interventions;
- externally managed Camofox sessions.

Material qualification: official docs say **browser file downloads are not supported**. If UF-A requires downloadable artifacts, either a provider-specific external browser adapter or a separate bounded file-transfer mechanism is necessary. Exact behavior for long waits, downloads, login expiry, CAPTCHA and browser crash remains a local test item.

### Tool and permission model

**Finding: powerful, but use container/FEE boundaries rather than profile trust.**

The current profile documentation is explicit that:

- profile state separation is not filesystem sandboxing;
- local terminal execution has the same filesystem access as the user;
- `terminal.cwd` does not prevent access elsewhere;
- `SOUL.md` is behavioral guidance, not enforcement;
- host profiles normally share user-level CLI credentials/config.

For APEX, the viable pattern is:

```text
FEE job roots/capabilities
       |
       v
compile Docker volumes + isolated tool HOME + tool allowlist
       |
       v
Hermes terminal backend = docker
       |
       v
only FEE wrapper actions reachable
```

Do not expose generic local shell/filesystem tools to the bounded local model and then attempt to recover safety through prompts.

### Local-model fit

**Finding: excellent transport/backend flexibility; execution quality remains a separate model bake-off.**

Hermes officially supports Ollama, LM Studio and custom/OpenAI-compatible endpoints. That makes it easy to hold the local model constant across platform tests. Generic memory/performance guidance in Hermes documentation is not a substitute for the APEX user-flow fixture benchmark on the operator hardware.

### State and resumability

**Finding: strong session persistence; FEE remains canonical job state.**

Hermes stores full conversation and tool history in SQLite/WAL and supports session resume/search. Browser persistence can survive task restarts in configured Camofox profiles. Tool checkpoints can provide rollback for mutations.

Those features reduce runtime work, but they are not sufficient to replace the FEE work-packet/checkpoint contract. FEE must resume by checkpoint/action ID; Hermes session state is supporting context and evidence only.

---

## 7. Best Hermes composition with FEE

```text
Subscription/deep-reasoning layer
    creates plan and decision criteria
                 |
                 v
APEX/FEE deterministic spine
    freeze work packet + hash
    validate action_id + args
    compile root/mount/capability profile
    own retry/stop/escalation policy
    own canonical event/evidence ledger
                 |
                 v
Hermes bounded runtime
    native Windows host process
    terminal backend: Docker for local actions
    explicit mounted roots only
    browser backend selected by work packet
    persistent sessions/browser identity where declared
    signed lifecycle/tool events -> FEE evidence
    planning/memory/delegation minimized
                 |
                 v
bounded local model selects only declared action IDs
                 |
                 +--> auth/security/CAPTCHA/unknown -> FEE escalation
```

### Hermes should own

- runtime/browser mechanics selected by FEE;
- terminal/container process execution behind wrappers;
- local-model/provider transport;
- session persistence as a runtime service;
- raw lifecycle/tool event emission;
- optional secondary file-operation checkpoints.

### FEE must retain

- plan/sequence authority;
- action registry and schema validation;
- root/repo permissions and mount compilation;
- provider/browser-session policy;
- retry/recovery budget;
- escalation taxonomy;
- canonical checkpoint and evidence ledger;
- personal/project credential and trust separation.

---

## 8. External brokers/wrappers required

1. **FEE action broker** — the local model can choose only pre-authorized action IDs; Hermes generic terminal/file actions stay hidden.
2. **Docker/root permission compiler** — converts work-packet roots and ro/rw scopes into explicit mounts and tool configuration.
3. **Credential/home broker** — avoids host-wide shared CLI state, especially for personal/project separation.
4. **Browser adapter/policy layer** — chooses CDP/Camofox/provider-specific path and supplies file-transfer support where Hermes' browser lacks it.
5. **Evidence webhook/ledger adapter** — validates signed lifecycle events and records normalized FEE events/hashes.
6. **Escalation governor** — caps retries/tool iterations and terminates on authentication, security or consequential ambiguity.
7. **Autonomy minimizer** — disables or bypasses planning/memory/delegation behaviors that are unnecessary for the bounded execution role.

---

## 9. Rejected roles and trade-offs

### Rejected: Hermes as new APEX project-management brain

Conflicts directly with the R2 authority lock and duplicates Weekly/Multi-Agent orchestration.

### Rejected: default local-terminal Hermes as primary bounded executor

Official documentation says it has the same filesystem access as the OS user. `cwd` and profile boundaries do not satisfy job-scoped permissions.

### Rejected: smart approvals as the final action-security boundary

Smart approval is itself model-assisted. APEX requires deterministic external action/argument validation. Use Hermes deny/approval controls only as defense-in-depth.

### Rejected: Hermes session state as the FEE checkpoint model

Session continuity is useful but conversation history does not encode the full frozen work packet, dependency/root safety and canonical action ledger required by APEX.

### Rejected: Hermes browser alone for every UF-A artifact path

Official no-download limitation means some provider flows require another adapter or transfer mechanism.

---

## 10. Unknowns and minimal bake-off tests

### Material unknowns

- actual subscription-site persistence across Chrome/Camofox restarts;
- CAPTCHA/logout/security-warning stop fidelity;
- download/artifact workaround quality;
- multi-root Docker mount behavior including ro/rw and forbidden roots;
- local-model action selection under minimized autonomy;
- duplicate-safe restart/resume at the FEE action boundary;
- project/personal credential separation on Windows;
- runtime/browser/local-model resource coexistence;
- integration maintenance burden given Hermes' rapid release cadence.

### Minimal tests

1. **UF-A authenticated browser fixture** — persistent ChatGPT/Claude/Gemini session, prompt submit/capture, browser restart, logout/CAPTCHA stop, downloadable-output case.
2. **Host-escape fixture** — Docker root A rw, root B ro, root C absent; attempt direct/path-traversal access to C and write to B.
3. **Hostile-content inertness fixture** — page/source text requests shell/path/provider changes; verify only already-authorized action IDs remain callable.
4. **Script recovery fixture** — one declared repair path, bounded retry count, then compact escalation packet.
5. **Resume fixture** — kill Hermes/runtime between action selection and completion and verify FEE resumes without duplicate consequential execution.
6. **Evidence fixture** — reconstruct tool/browser/action history from FEE ledger plus Hermes session/webhook references.
7. **Trust-zone fixture** — separate project/personal profiles, tool HOME, browser identity, credentials and roots; verify denial across zones.
8. **Resource coexistence fixture** — Windows browser + chosen local model + Hermes + development tooling; capture peak RAM/CPU/GPU and human interventions.

---

## 11. Source appendix

### APEX authority sources

- `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md`
- `apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md`

### Current Hermes primary sources reviewed 2026-08-08

- Release: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3
- Current main commit inspected: https://github.com/NousResearch/hermes-agent/commit/973c14b57c10874138b9696a2b300cc2f89e40e3
- Native Windows: https://hermes-agent.nousresearch.com/docs/user-guide/windows-native
- Profiles and isolation: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Configuration / terminal backend / approvals: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- Sessions: https://hermes-agent.nousresearch.com/docs/user-guide/sessions
- Browser automation: https://hermes-agent.nousresearch.com/docs/user-guide/features/browser
- Docker: https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Tools: https://hermes-agent.nousresearch.com/docs/user-guide/features/tools
- Checkpoints and rollback: https://hermes-agent.nousresearch.com/docs/user-guide/checkpoints-and-rollback
- Provider/local-model integrations: https://hermes-agent.nousresearch.com/docs/integrations/providers

---

## 12. Machine-readable result

```yaml
platform_research_result:
  candidate: Hermes
  evidence_date: 2026-08-08
  versions_or_commits_reviewed:
    - "Hermes Agent v0.20.0 / tag v2026.8.3"
    - "main 973c14b57c10874138b9696a2b300cc2f89e40e3"
  runtime_reality:
    native_windows: true
    broad_tool_runtime: true
    docker_terminal_sandbox: true
    persistent_sessions: true
    multiple_browser_backends: true
    profile_is_filesystem_sandbox: false
    browser_downloads_supported: false
  per_user_flow_scores:
    UF-A: 84
    UF-B: 88
    UF-C: 90
    UF-D: 84
    UF-E: 76
    UF-F: 78
  weighted_scores:
    FIT: 82
    BOUND: 70
    BROWSER: 82
    TOOLS: 91
    RECOVERY: 88
    AUDIT: 90
    MULTIROOT: 70
    LOCALMODEL: 90
    WINDOWS: 92
    RESOURCE: 65
    MAINT: 52
    total: 81.3
  score_confidence:
    total: 79
    windows: 92
    authenticated_browser: 70
    resource: 55
  hard_gate_results:
    authority_containment: PASS_WITH_EXTERNAL_BROKER
    job_scoped_permissions: PASS_WITH_EXTERNAL_BROKER
    resumability: PASS_WITH_EXTERNAL_BROKER
    evidence_capture: PASS
    safe_escalation: PASS_WITH_EXTERNAL_BROKER
    practical_windows_viability: PASS
  windows_fit:
    status: strong_documented_native_fit
    local_measurement_required: true
  browser_fit:
    status: strong_but_incomplete
    persistent_authenticated_profiles: true
    live_local_cdp: true
    file_downloads: unsupported_by_official_browser_tool
  local_model_fit:
    backend_swapability: strong
    backends: [Ollama, LM_Studio, OpenAI_compatible]
    execution_quality: unknown_until_fixture_bakeoff
  permission_model:
    profiles_sandbox: false
    terminal_cwd_sandbox: false
    docker_isolation_available: true
    tool_enable_disable: true
    approval_modes: [smart, manual, off]
    fee_action_broker_required: true
  state_and_resumability:
    sqlite_state_db: true
    full_tool_call_results_persisted: true
    browser_persistence_options: true
    fee_checkpoint_remains_canonical: true
  audit_and_evidence:
    full_session_history: true
    signed_lifecycle_webhooks: true
    runtime_logs: true
    fee_normalization_required: true
  duplicated_orchestration_risk:
    default_autonomous_agent_mode: medium_high
    bounded_runtime_only: low
  strongest_role: "FEE spine + Hermes bounded tool/browser/session runtime with autonomous planning/memory minimized"
  required_external_brokers:
    - FEE action-id and argument-validation broker
    - Docker/root permission compiler
    - credential and tool-HOME broker
    - browser policy and artifact-transfer adapter
    - evidence webhook normalizer
    - escalation governor
    - autonomy minimizer
  unresolved_unknowns:
    - authenticated subscription reliability
    - CAPTCHA/logout stop fidelity
    - download/artifact workaround
    - multi-root containment on operator Windows host
    - duplicate-safe action resume
    - personal/project credential separation
    - resource coexistence
    - maintenance burden under rapid releases
  benchmark_tests_required:
    - UF-A authenticated browser and download fixture
    - host/root escape fixture
    - hostile-content inertness fixture
    - bounded script recovery fixture
    - duplicate-safe resume fixture
    - event/provenance reconstruction fixture
    - project/personal trust-zone fixture
    - Windows resource coexistence fixture
  rejected_roles:
    - APEX project-management brain
    - default local-terminal primary executor
    - smart approvals as final security boundary
    - Hermes session DB as FEE checkpoint authority
    - Hermes browser as sole artifact-transfer mechanism
  reversal_triggers:
    - Docker/root containment failure
    - inability to close generic tool bypass paths
    - materially unreliable subscription sessions
    - unacceptable duplicate-action resume behavior
    - unacceptable Windows resource contention
    - simpler composition provides same value with less maintenance
  overall_confidence_0_to_100: 82
```
