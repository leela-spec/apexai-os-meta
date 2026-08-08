---
title: "Platform Research Result V2 — OpenClaw"
doc_type: platform_research_result
initiative: local-orchestration-engine
candidate: OpenClaw
evidence_date: 2026-08-08
prompt: apex-meta/local-orchestration-engine/research-prompts/PLATFORM-RESEARCH-OPENCLAW-2026-08-08-V2.md
status: "desk-research complete; local bake-off required; no implementation authorization"
---

# Platform Research Result V2 — OpenClaw

## 1. Executive finding

**Strongest role:** **OpenClaw runtime subset behind the FEE authority/evidence spine, combined with selected OpenClaw Detective/KB/hygiene/routing doctrine as a separate higher-level companion layer.**

OpenClaw is a materially stronger low-level runtime candidate than the earlier platform hypothesis suggested. Current OpenClaw provides configurable tool allow/deny policy, host-exec approval modes, per-agent allowlists, argument-pattern restrictions, Docker sandboxing with read/write workspace controls and bind mounts, managed and existing-session browser profiles, durable session/restart recovery, an activity/audit ledger, Windows installation paths, and local-model backends. Those capabilities map unusually well to the six APEX user flows.

The decisive qualification is that **OpenClaw is not secure-by-default in the exact APEX sense**. Sandboxing is optional and off by default; gateway/node host exec historically resolves to a permissive `full` security default unless deliberately tightened. OpenClaw's policy surfaces are agent/runtime controls, not the FEE contract of `authorized_action_id + externally validated bounded arguments`. Therefore APEX should not hand OpenClaw strategy or unrestricted tool authority. FEE must remain the work-packet, capability, checkpoint, evidence, and escalation authority.

**Biggest strength:** unusually complete runtime primitives in one system: browser/session control + tool/sandbox controls + restart recovery + audit + Windows support.

**Biggest blocker:** APEX-grade containment requires a deliberately hardened profile and an external FEE action broker; OpenClaw's powerful agent/runtime defaults cannot themselves be treated as the authority boundary.

**Overall confidence:** **84/100** for desk-research conclusions. Confidence is lower for authenticated subscription-browser reliability and resource coexistence because those require local repeated tests.

---

## 2. Current runtime reality map

### Current official runtime reviewed

- Latest stable release observed through GitHub API: **`v2026.7.1-2`**, published 2026-08-04.
- Current `main` inspected on 2026-08-08: **`c5d00cb47ddb7236980de8e0fbc938b23fdeaae0`**.
- Current documentation reviewed on 2026-08-08 for sandboxing, tool policy, exec approvals, browser control, sessions/restart recovery, audit, Windows, and local models.

### Executable runtime vs operator doctrine

| Surface | Reality | Evidence | APEX implication |
|---|---|---|---|
| Gateway/runtime | Executable current OpenClaw runtime | source/release + official docs | Candidate capability host behind FEE |
| Tool policy | Profiles + allow/deny; separate file mutation tools; exec can be fully denied | officially documented | Useful first containment layer, but not a substitute for FEE action schemas |
| Exec approvals | deny/allowlist/ask/auto/full; per-agent allowlists; `argPattern`; approval plan pins command/cwd/session | officially documented | Strong primitive for UF-B/UF-E; configure conservatively |
| Sandbox | Docker/SSH/OpenShell backends; Docker supports browser sandbox and bind mounts; workspace access can be none/ro/rw | officially documented | Strong containment primitive; Docker is most relevant for local APEX bake-off |
| Browser | Managed browser and existing-session Chromium profiles; uploads/downloads/dialogs/waits; existing-session path has capability limitations | officially documented | Strong UF-A candidate, but authenticated-session behavior must be measured |
| Sessions/restart | Durable session/transcript state and restart recovery with bounded redispatch identifiers | officially documented | Strong G-P3 baseline |
| Audit | Activity/audit surfaces and tool/run lifecycle data | officially documented | Can feed FEE ledger, but FEE remains canonical evidence owner |
| Windows | Native Windows Hub, PowerShell CLI path, and WSL2 Gateway path | officially documented | Practical host options exist |
| Local model | Ollama/LM Studio/OpenAI-compatible and other local backends supported | officially documented | Backend swapability is good; hardware/model quality remains separate research |
| Operator OpenClaw system | `MasterOfArts/OpenClaw/07_finalopenclawsystem/` contains managed rules, agents, knowledge, processes, rituals, config and user surfaces | operator-repo doctrine/process | Reuse valuable doctrine without making it low-level execution authority |

### Important runtime/doctrine distinction

The operator repository explicitly treats `managed/`, `user/`, `docs/`, and the final-system README as durable final-system surfaces, while staging/research directories are not runtime authority. Its managed architecture contains rules, agents, knowledge, and processes. That is valuable independent of whether OpenClaw wins the low-level runtime bake-off.

The clean APEX decomposition is therefore:

```text
OpenClaw Detective / KB / hygiene / routing doctrine
        (selected concepts/processes only)
                         |
                         v
APEX reasoning/orchestration layers
                         |
                         v
FEE deterministic spine  <--- sole execution authority/evidence owner
                         |
                         v
OpenClaw hardened runtime subset
  browser | bounded tools | sandbox | session/recovery | audit feed
```

OpenClaw should not collapse those layers into one autonomous agent authority.

---

## 3. UF-A..UF-F evidence table

Scores are desk-research estimates, not benchmark measurements.

| Flow | Score | Confidence | Finding |
|---|---:|---:|---|
| **UF-A Subscription research executor** | **88** | 75 | Strong managed/existing-session browser support, file transfer and waits. Existing-session profiles deliberately have fewer capabilities than the managed browser. Login/session continuity and CAPTCHA/logout stop behavior still require repeated local tests. |
| **UF-B Script failure recovery** | **85** | 83 | Exec modes, per-agent allowlists, argument patterns, pinned approval plans, process handling and restart recovery are strong. FEE must own the closed recovery ladder and retry budget rather than delegating open-ended repair to the agent. |
| **UF-C Detective evidence collection** | **93** | 88 | Read/status/diff/process/file tooling plus transcripts/audit are a strong match. FEE can keep observation outputs structured and prohibit judgement authority. |
| **UF-D Database / knowledge hygiene** | **83** | 80 | Constrained filesystem tools and sandbox scopes support bounded transformations. Transaction/dry-run semantics remain task/tool-specific and should be supplied by deterministic FEE actions. |
| **UF-E Multi-repo / multi-folder execution** | **91** | 82 | Docker bind mounts and workspace permissions can express multiple roots and ro/rw differences. The exact per-job mount compiler should remain FEE-owned and be tested for forbidden-root rejection. |
| **UF-F Personal weekly execution** | **79** | 70 | Separate profiles/agents/sessions and tool restrictions can support a stricter personal trust zone. Credential/session separation and sensitive-action gates must be designed and tested explicitly; generic OpenClaw channel autonomy is too broad as the policy layer. |

**Flow average:** 86.5/100. The average is not a selection decision; hard gates override it.

---

## 4. Hard-gate table

| Hard gate | Result | Evidence-backed rationale |
|---|---|---|
| **G-P1 Authority containment** | **PASS_WITH_EXTERNAL_BROKER** | OpenClaw can deny tools, sandbox execution, restrict host exec and arguments, but its native abstraction is still tool/agent policy rather than the locked FEE `action_id + validated arguments` contract. FEE must compile the frozen work packet and expose only bounded wrapper actions. |
| **G-P2 Job-scoped permissions** | **PASS_WITH_EXTERNAL_BROKER** | Docker workspace access and bind mounts can express roots and ro/rw scopes. FEE should generate the per-job mount/tool policy and independently reject undeclared paths/capabilities. |
| **G-P3 Resumability** | **PASS** | Official restart-recovery/session mechanisms preserve transcripts/state and re-dispatch interrupted work with durable identifiers. Exact browser-auth restoration still needs fixture testing. |
| **G-P4 Evidence capture** | **PASS** | Session transcripts plus activity/audit/tool lifecycle data provide sufficient raw material. FEE still normalizes this into the canonical APEX event ledger and artifact hashes. |
| **G-P5 Safe escalation** | **PASS_WITH_EXTERNAL_BROKER** | Denials and approval failures can be terminal/reported and restart recovery is bounded, but APEX escalation classes are not OpenClaw's native authority model. FEE must terminate the work packet on auth/security/consequential ambiguity. |
| **G-P6 Practical Windows viability** | **PASS** | Official native Windows Hub + PowerShell and WSL2 Gateway paths exist. The exact preferred deployment and resource profile must be measured on the operator laptop. |

**No unmitigated desk-research hard-gate failure found.** This qualifies OpenClaw for local bake-off; it does not authorize production adoption.

---

## 5. Weighted score + confidence

Using the Platform Research Gate weights:

| Dimension | Score | Weight | Evidence note |
|---|---:|---:|---|
| FIT | 86 | 18 | Broad direct coverage of UF-A..UF-F |
| BOUND | 80 | 15 | Strong primitives, but hardening + FEE broker required |
| BROWSER | 84 | 14 | Mature control surfaces; authenticated reliability unmeasured |
| TOOLS | 90 | 12 | Extensive local/process/Git/file controls |
| RECOVERY | 90 | 10 | Durable session/restart behavior documented |
| AUDIT | 92 | 9 | Strong activity/transcript surfaces |
| MULTIROOT | 88 | 8 | Docker binds + ro/rw workspace model |
| LOCALMODEL | 70 | 5 | Flexible backends; operator hardware/full-agent quality concern |
| WINDOWS | 88 | 4 | Native and WSL2 paths |
| RESOURCE | 58 | 3 | No operator-machine measurements yet; full local agent loops can be demanding |
| MAINT | 62 | 2 | Large, fast-moving platform; integration needs version pinning |

**Weighted score: 84.4/100.**  
**Score confidence: 81/100.**

The score is intentionally subordinate to the hard gates.

---

## 6. Windows, browser, local-model, permission, and resume findings

### Windows fit

**Finding: PASS, pending local resource measurement.**

OpenClaw currently documents native Windows installation through the Windows Hub and PowerShell CLI, plus WSL2 as the more Linux-compatible Gateway runtime. This is materially better than a Linux-only candidate. For APEX, the first bake-off should compare only the deployment modes that preserve explicit root permissions and browser usability without adding unnecessary layers.

### Browser fit

**Finding: strong capability, incomplete reliability evidence.**

OpenClaw supports isolated managed profiles and attachment to existing logged-in Chromium sessions. The managed path has a richer automation surface; existing-session mode is intentionally constrained in areas such as some waits, response-body capture, PDF/download interception, batch operations and uploads. This is not automatically a defect: a restricted existing-session path may be desirable for subscription-account work, while provider-specific adapters can use richer managed sessions where policy permits.

Required local evidence:

1. persistent ChatGPT/Claude/Gemini subscription sessions;
2. exact output capture after long waits;
3. file upload/download;
4. logout/CAPTCHA/security-warning stop behavior;
5. browser crash and Gateway restart recovery;
6. selective screenshot capture at APEX evidence checkpoints.

### Local-model fit

**Finding: integration is good; resource/quality fit is unproven.**

OpenClaw can use Ollama, LM Studio and OpenAI-compatible local services. However, OpenClaw's own local-model guidance warns that comfortable full agent loops need substantial hardware/context headroom and that small or aggressively quantized models increase truncation and prompt-injection risk.

That warning does **not** invalidate the APEX design because APEX intends a bounded local operator, not a general autonomous OpenClaw agent. It does mean the bake-off must use the user-flow fixture corpus and should not infer success from transport compatibility alone.

### Permission model

**Finding: strong native primitives; FEE remains mandatory.**

Useful native controls include:

- tool profiles and allow/deny;
- hard denial of `exec`;
- exec modes `deny`, `allowlist`, `ask`, `auto`, `full`;
- per-agent command allowlists;
- argument-pattern matching;
- approved execution plans that pin command/cwd/session metadata;
- sandbox mode/scope/backend;
- Docker bind mounts and workspace access modes;
- browser `evaluate` disabling when arbitrary page JavaScript is unnecessary.

Critical warning: **sandboxing is off by default**, and host exec has permissive configurations available, including a documented `full` path. APEX must treat secure configuration as an invariant generated/checked by FEE, not as an operator habit.

### State and resumability

**Finding: strong documented baseline.**

OpenClaw persists session/transcript state and has explicit restart-recovery behavior. Requested Gateway restart can mark in-flight work and later resume it from the existing transcript with durable dispatch identifiers designed to avoid duplicate recovery.

APEX should still avoid letting transcript continuation redefine the frozen plan. FEE should resume from its own checkpoint and use OpenClaw session state only as capability/session continuity evidence.

---

## 7. Best OpenClaw composition with FEE

```text
Subscription / deep-reasoning layer
  creates plan, prompts, decision criteria
                |
                v
APEX/FEE deterministic spine
  freeze work packet + hash
  validate action_id + arguments
  compile per-job roots/capabilities
  own checkpoint/retry/escalation state
  own canonical evidence ledger
                |
                +--------------------------------------+
                |                                      |
                v                                      v
OpenClaw hardened runtime subset                OpenClaw doctrine subset
  sandbox=all where practical                     Detective / KB / hygiene
  explicit tool allowlist                         routing/process patterns
  exec deny/allowlist only                        NO execution authority
  per-job mounted roots
  managed/existing browser profiles
  session/restart + audit feed
                |
                v
bounded local model chooses only declared actions
                |
                v
blocked/auth/security/unknown -> FEE escalation packet
```

### FEE must retain

- frozen plan/work-packet authority;
- action registry and argument schemas;
- explicit root registry and ro/rw scopes;
- retry/recovery budget;
- stop/escalation taxonomy;
- evidence normalization, hashes and checkpoints;
- project/personal trust-profile policy;
- provider/session policy;
- permission-profile generation and validation.

### OpenClaw may provide

- browser control/session hosting;
- sandbox/container execution substrate;
- process/file/Git primitives behind wrappers;
- session persistence and restart support;
- runtime/audit events as evidence input;
- local-model transport/runtime integration.

---

## 8. Required external brokers/wrappers

1. **FEE action broker** — maps `authorized_action_id` to a fixed OpenClaw tool/wrapper and independently validates all arguments.
2. **Per-job permission compiler** — creates effective tool policy, sandbox profile, root mounts and ro/rw scopes from the frozen work packet.
3. **Browser policy adapter** — chooses managed vs existing-session/provider-specific mechanism from the work packet, never from captured content.
4. **Evidence normalizer** — converts OpenClaw runtime/session/audit events into the FEE event ledger and artifact provenance format.
5. **Escalation governor** — stops the run on auth/security/CAPTCHA/consequential ambiguity and blocks autonomous continuation beyond the declared recovery set.
6. **Configuration invariant check** — fails closed if sandbox/tool/exec/elevated configuration is broader than the work packet permits.

These are not optional if OpenClaw is used for consequential local tools.

---

## 9. Rejected roles and trade-offs

### Rejected: OpenClaw as APEX project-management/orchestration brain

Reason: conflicts with the operator lock. APEX Weekly Orchestrator and Multi-Agent Orchestration already own strategy/orchestration; FEE owns deterministic execution authority.

### Rejected: unrestricted OpenClaw agent with host shell

Reason: violates action-ID validation, zero-authority captured content, and bounded recovery requirements. OpenClaw can technically run this way; APEX must not.

### Rejected: doctrine-only OpenClaw, no runtime bake-off

Reason: current runtime primitives are now strong enough that excluding them without a bake-off would discard substantial browser/sandbox/recovery/audit capability and increase custom FEE engineering burden.

### Rejected: assume OpenClaw alone provides FEE evidence semantics

Reason: audit/transcript data is valuable but FEE's event ledger, frozen work packet, checkpoint and artifact-provenance contract remain APEX-specific.

---

## 10. Unknowns and minimal bake-off tests

### Material unknowns

- subscription-site authentication/session durability on the operator's actual accounts;
- CAPTCHA/challenge/logout detection and stop fidelity;
- exact Windows mode with the best containment/browser/resource trade-off;
- Arc 140V + ~32 GB coexistence with local model + browser + OpenClaw runtime;
- whether all dangerous OpenClaw tool paths can be made unreachable except through FEE wrappers;
- root-mount leakage/escape behavior under realistic multi-repo jobs;
- local-model action-selection quality with small/practical model classes;
- maintenance burden under OpenClaw's release cadence.

### Minimal tests

1. **UF-A persistent subscription fixture** — submit prompt, wait, capture output, restart browser/Gateway, resume; inject logout and CAPTCHA and require stop.
2. **Unauthorized action fixture** — hostile page instructs shell/file/network action; verify no new action ID/path/tool becomes callable.
3. **Script recovery fixture** — one allowlisted retry path succeeds; second failure produces escalation evidence rather than free-form repair.
4. **Multi-root fixture** — root A rw, root B ro, root C forbidden; verify writes and path traversal fail closed.
5. **Evidence reconstruction fixture** — rebuild action sequence from FEE ledger + OpenClaw event/session references.
6. **Restart checkpoint fixture** — kill runtime during browser wait and during tool execution; verify no duplicate consequential operation.
7. **Personal/project separation fixture** — separate session/profile/root/credential namespaces and prove cross-zone access denial.
8. **Resource coexistence fixture** — browser + representative local model + OpenClaw + development tools; record peak RAM/CPU/GPU and intervention rate.

No production selection should occur before those tests.

---

## 11. Reversal triggers

Reverse or demote this recommendation if any of the following is observed:

- a model/browser-captured instruction can bypass FEE and reach an undeclared tool/path/command;
- the multi-root sandbox cannot reliably enforce ro/rw/forbidden roots;
- authenticated subscription browser sessions are materially less reliable than the Hermes or custom-adapter alternative;
- restart/resume can duplicate consequential actions despite the FEE checkpoint envelope;
- local Windows resource coexistence is poor enough to impair routine development;
- integration requires continuous patching against OpenClaw release churn;
- a simpler FEE + provider-adapter composition meets the same gates with lower maintenance.

---

## 12. Source appendix

### APEX / operator sources

- `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md`
- `apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md`
- `apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md` — proposal/candidate architecture, not operator-confirmed runtime
- `leela-spec/MasterOfArts/OpenClaw/07_finalopenclawsystem/README-OpenClaw.md`
- `leela-spec/MasterOfArts/OpenClaw/07_finalopenclawsystem/managed/`

### Current OpenClaw primary sources reviewed 2026-08-08

- Release: https://github.com/openclaw/openclaw/releases/tag/v2026.7.1-2
- Current main commit inspected: https://github.com/openclaw/openclaw/commit/c5d00cb47ddb7236980de8e0fbc938b23fdeaae0
- Sandboxing: https://docs.openclaw.ai/gateway/sandboxing
- Sandbox vs tool policy vs elevated: https://docs.openclaw.ai/gateway/sandbox-vs-tool-policy-vs-elevated
- Exec approvals: https://docs.openclaw.ai/tools/exec-approvals
- Exec tool: https://docs.openclaw.ai/tools/exec
- Browser: https://docs.openclaw.ai/browser
- Browser CLI: https://docs.openclaw.ai/cli/browser
- Browser login: https://docs.openclaw.ai/tools/browser-login
- Restart recovery: https://docs.openclaw.ai/gateway/restart-recovery
- Audit: https://docs.openclaw.ai/cli/audit
- Windows: https://docs.openclaw.ai/windows
- Install: https://docs.openclaw.ai/install
- Local models: https://docs.openclaw.ai/gateway/local-models

---

## 13. Machine-readable result

```yaml
platform_research_result:
  candidate: OpenClaw
  evidence_date: 2026-08-08
  versions_or_commits_reviewed:
    - "stable release v2026.7.1-2"
    - "main c5d00cb47ddb7236980de8e0fbc938b23fdeaae0"
  runtime_reality:
    executable_runtime: true
    browser_runtime: true
    sandbox_runtime: true
    durable_sessions_and_restart_recovery: true
    activity_audit_surface: true
    operator_doctrine_is_separable_from_runtime: true
  per_user_flow_scores:
    UF-A: 88
    UF-B: 85
    UF-C: 93
    UF-D: 83
    UF-E: 91
    UF-F: 79
  weighted_scores:
    FIT: 86
    BOUND: 80
    BROWSER: 84
    TOOLS: 90
    RECOVERY: 90
    AUDIT: 92
    MULTIROOT: 88
    LOCALMODEL: 70
    WINDOWS: 88
    RESOURCE: 58
    MAINT: 62
    total: 84.4
  score_confidence:
    total: 81
    browser_authenticated_reliability: 70
    resource_profile: 55
  hard_gate_results:
    authority_containment: PASS_WITH_EXTERNAL_BROKER
    job_scoped_permissions: PASS_WITH_EXTERNAL_BROKER
    resumability: PASS
    evidence_capture: PASS
    safe_escalation: PASS_WITH_EXTERNAL_BROKER
    practical_windows_viability: PASS
  windows_fit:
    status: strong_documented_fit
    options: [native_windows_hub, powershell_cli, wsl2_gateway]
    local_measurement_required: true
  browser_fit:
    status: strong_candidate
    managed_browser: true
    existing_authenticated_session: true
    existing_session_has_feature_limits: true
    repeated_subscription_fixture_required: true
  local_model_fit:
    backend_swapability: strong
    operator_hardware_quality: unknown_until_bakeoff
    caution: "official guidance warns full local agent loops can require much more hardware/context headroom"
  permission_model:
    native_controls: [tool_allow_deny, exec_modes, per_agent_allowlists, arg_patterns, pinned_approval_plan, sandbox, workspace_access, docker_binds]
    secure_by_default_for_apex: false
    fee_broker_required: true
  state_and_resumability:
    durable_session_state: true
    restart_recovery: true
    fee_checkpoint_remains_canonical: true
  audit_and_evidence:
    native_activity_audit: true
    transcripts: true
    fee_normalization_required: true
  duplicated_orchestration_risk:
    raw_openclaw_agent_mode: high
    bounded_runtime_subset: low
    separated_operator_doctrine: low
  strongest_role: "FEE spine + hardened OpenClaw runtime subset + separately reused OpenClaw Detective/KB/hygiene/routing doctrine"
  required_external_brokers:
    - FEE action-id and argument-validation broker
    - per-job permission/root compiler
    - browser policy adapter
    - evidence normalizer
    - escalation governor
    - effective-configuration invariant checker
  unresolved_unknowns:
    - authenticated subscription reliability
    - CAPTCHA/logout stop fidelity
    - exact Windows deployment mode
    - operator-laptop resource coexistence
    - full closure of dangerous tool bypass paths
    - long-term integration maintenance burden
  benchmark_tests_required:
    - UF-A authenticated session/restart fixture
    - hostile-content inertness fixture
    - bounded script recovery fixture
    - multi-root ro/rw/forbidden fixture
    - event/provenance reconstruction fixture
    - duplicate-safe restart fixture
    - personal/project trust separation fixture
    - Windows resource coexistence fixture
  rejected_roles:
    - APEX project-management/orchestration brain
    - unrestricted host-shell agent
    - doctrine-only without runtime bake-off
    - sole evidence authority
  reversal_triggers:
    - undeclared tool/path/command bypass
    - multi-root containment failure
    - materially inferior authenticated-browser reliability
    - duplicate consequential actions on resume
    - unacceptable Windows resource contention
    - excessive release-integration churn
    - simpler FEE/provider-adapter composition proves equivalent
  overall_confidence_0_to_100: 84
```
