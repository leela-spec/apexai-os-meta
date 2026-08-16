# OpenClaw Trigger and Feedback Evaluation Matrix

## Decision summary

The current evidence does not support calling any option a verified complete planning-AI-to-OpenClaw-to-same-planning-context loop. Option 1 is now selected and its local forward trigger is live: OpenClaw Cron polls the repository inbox every 15 seconds with an exact command argument vector and no AI polling turn.

The repository already contains the valuable execution core: one bounded `apex.execution-request/v2`, request validation, immutable prompt hashing, serialized dispatch, idempotency state, browser execution, and independent transcript-backed evidence verification. The main missing seams are automatic request publication, automatic triggering, result publication to durable repository state, and return to the exact planning context.

On the evidence available today, the recommended order is:

1. **OpenClaw Cron plus a thin repository inbox processor** for the first automatic forward-trigger experiment.
2. **Windows Task Scheduler plus the same processor** if the OpenClaw Gateway/Cron service cannot be made reliable on this host.
3. **ChatGPT custom MCP synchronous dispatch** as the highest-potential complete-loop experiment, but only after account eligibility, confirmations, duration, reconnection, and same-turn return are proved.
4. **Hookaido** only if polling latency becomes a demonstrated problem that justifies another daemon, ingress boundary, credential, and durable queue.

The two leading current scores are intentionally modest. Both solve the forward trigger more convincingly than the feedback edge. A repository result does not automatically wake or resume a subscription-AI planning conversation.

## Evidence reconciliation

The three supplied research reports contain useful candidate discovery, but they disagree on important facts. This matrix uses the following authority order:

1. measured local runtime and CLI behavior;
2. current repository implementation and tests;
3. current primary vendor documentation;
4. claims in the supplied research reports.

| Question | Current evidence | Matrix treatment |
|---|---|---|
| Installed OpenClaw version | Local CLI reports `OpenClaw 2026.7.1-2 (0790d9f)`. | Verified locally. |
| Scheduler command | `openclaw cron` exists. `openclaw automations` returns `Unknown command`. | Use only the `cron` name and its locally exposed flags. |
| Deterministic Cron command payload | Job `f0dca634-237b-468e-85ad-66a9b7243127` runs the processor by exact `argv` every 15 seconds. Empty runs completed in about 0.2–0.3 seconds with zero claims. | Live E4 evidence on this host. No AI turn is used for polling. |
| Gateway availability | The supported Windows Scheduled Task service is installed and the Gateway health probe is green on loopback port `18789`. Cron resumed successfully after a live Gateway restart. | Service prerequisite passed for an interactive logon session; logout/reboot behavior remains untested. |
| Request-v2 shape | Live validator defines one bounded execution with one `prompt_ref`; it has no `steps[]` or dependency DAG. | Do not credit request-v2 with multi-step orchestration. The planning controller must issue sequential requests. |
| Duplicate admission | Dispatcher uses a global mutex and persistent idempotency state. Duplicate completed/in-flight requests are refused. | Existing high-value capability reused by every option. |
| Crash recovery | A request left in `started` or another unsafe state stops with `IDEMPOTENCY_INDETERMINATE`. | Fail-closed behavior, not full exactly-once remote-side-effect recovery. |
| Git result publication | Validator can describe Git grants, but dispatcher explicitly rejects Git execution at this gate. | Result commit/push is new work for every asynchronous option. |
| Inbox/outbox implementation | `scripts/openclaw/process_execution_inbox.py` and `apex-meta/orchestration/` now implement atomic claim, terminal receipt, deterministic ordering, overlap locking, and restart reconciliation. Six focused tests pass. | Local inbox is implemented. Remote Git request ingestion, result push, and planner callback remain open. |
| Same planning-context feedback | No verified ChatGPT, Gemini, or Perplexity callback/resume mechanism exists. | Cap every option without a proven same-context return. |
| ChatGPT custom MCP eligibility | The reports describe a conditional full-MCP capability, but the actual planning account and policy are unknown. | Keep the option, evidence-gate it, and cap its current score. |
| Hookaido | Described by the research as a maintained HMAC/durable-queue/subprocess option, but it is not installed or locally tested. | Treat as report-level evidence until independently verified. |

## Scoring method

Each fit dimension is scored from `0` to `5`, where `5` is best. The raw score is:

```text
Raw fit = sum((dimension score / 5) * dimension weight)
```

The raw score is then multiplied by the evidence confidence of the weakest essential seam. The lowest applicable cap is applied last.

```text
Current overall = min(raw fit * evidence multiplier, applicable caps)
```

### Fit dimensions

| Dimension | Weight | `5` anchor | `3` anchor | `1` anchor |
|---|---:|---|---|---|
| Low novel-derivation risk | 25 | Configuration of supported existing capability | Thin deterministic adapter plus limited state | New service/state architecture or speculative integration |
| Existing reuse/copyability | 20 | At least 80% of required path is existing and verified | 40–59% reusable | Under 20% reusable |
| End-to-end automation | 15 | Proven two-batch loop returning to the same planner | Unattended forward execution and durable results, but manual planner resume | Routine manual trigger and feedback |
| Determinism and recovery | 15 | Tested duplicate prevention and crash reconciliation | Persistent admission/idempotency with fail-closed indeterminate crash state | Best-effort delivery or AI/UI-owned state |
| User value and impact | 10 | Solves trigger and feedback with no routine operator work | Solves forward dispatch only | Supporting component with little direct workflow closure |
| Low implementation investment | 5 | Under half a day | One to three days | More than a week or a new platform |
| AI-token efficiency | 5 | Trigger uses no model and all AI turns are bounded work turns | One extra AI coordination turn per cycle | Continuous or unbounded AI monitoring |
| Operations, security, maintenance | 5 | No new service or credential | One supported service/credential | Public ingress or multiple new daemons/credentials |

### Evidence confidence

| Grade | Evidence | Multiplier |
|---|---|---:|
| E0 | Absent or contradicted | 0.20 |
| E1 | Research-report or secondary-source claim only | 0.40 |
| E2 | Current primary documentation | 0.65 |
| E3 | Present in the local CLI or repository | 0.80 |
| E4 | Live component smoke test on this host | 0.90 |
| E5 | Complete two-dependent-batch test | 1.00 |

Evidence is not averaged across a topology. The weakest essential seam sets the confidence grade for the claim being scored.

### Score caps

| Condition | Maximum current score |
|---|---:|
| Planning-account feature eligibility unknown | 50 |
| No proven return to the same planning context | 60 |
| No live trigger smoke test | 75 |
| Essential capability contradicted locally | 35 |
| Unacceptable security boundary | Disqualified |

## Overall evaluation matrix

Scores are evidence-adjusted current estimates, not success verdicts. The POC ceiling shows the highest score the same topology can reach after its proposed bounded test without adding a different feedback architecture.

| Rank | Option | Raw fit | Evidence | Limiting condition | Current overall | POC ceiling | Current verdict |
|---:|---|---:|---|---|---:|---:|---|
| 1 | OpenClaw Cron + repository inbox | 73 | E4 / 0.90 | No remote Git publication/result push or same-planner feedback | **60/100** | **60/100** | **Selected; local forward trigger live, complete loop still open** |
| 2 | Windows Task Scheduler + repository inbox | 72 | E3 / 0.80 | No live integrated test; no same-planner feedback | **58/100** | **60/100** | Strong fallback and independent wake-up surface |
| 3 | ChatGPT custom MCP synchronous dispatch | 68 | E1 / 0.40 | Account eligibility unknown; bridge and return behavior unverified | **27/100** | **68/100** | Highest complete-loop potential; highest uncertainty among viable options |
| 4 | Hookaido webhook queue + local dispatch | 58 | E1 / 0.40 | Not installed/tested; new ingress/daemon; no same-planner feedback | **23/100** | **52/100** | Event-driven fallback only after polling fails a measured requirement |

The Cron and Task Scheduler scores round to the same whole number. Cron wins the tie because it is the native OpenClaw operator surface, exposes command-job history, and adds no separate scheduler product. Task Scheduler becomes preferable when the Gateway cannot keep Cron alive or must itself be started/recovered by an external Windows service.

## Dimension scores

| Option | Low derivation risk `25` | Reuse `20` | Automation `15` | Determinism `15` | Value `10` | Low investment `5` | Token efficiency `5` | Ops/security `5` | Raw |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| OpenClaw Cron inbox | 4 | 4 | 3 | 3 | 3 | 4 | 5 | 4 | **73** |
| Windows Scheduler inbox | 4 | 4 | 3 | 3 | 3 | 4 | 5 | 3 | **72** |
| ChatGPT MCP synchronous | 2 | 4 | 5 | 3 | 5 | 2 | 4 | 2 | **68** |
| Hookaido webhook queue | 2 | 3 | 3 | 4 | 3 | 2 | 5 | 2 | **58** |

## Process coverage matrix

Legend: `Existing` means the current Apex/OpenClaw path already supplies the behavior; `Native` means the candidate supplies it but it is not yet integrated; `New` means Apex-specific work must be derived; `Unknown` means a capability test is required; `Missing` means the topology does not currently solve it.

| Process seam | ChatGPT MCP | OpenClaw Cron inbox | Windows Scheduler inbox | Hookaido webhook queue |
|---|---|---|---|---|
| Operator starts planning | Existing subscription workflow | Existing subscription workflow | Existing subscription workflow | Existing subscription workflow |
| Planning AI authors prompts/dependencies | Existing planning responsibility | Existing planning responsibility | Existing planning responsibility | Existing planning responsibility |
| Publish one frozen request | **New** MCP tool action | **New** repo writer/inbox handoff | **New** repo writer/inbox handoff | **New** Git/webhook publisher |
| Detect/wake execution | **Unknown** synchronous tool call | **Live** 15-second exact-argv `openclaw cron` job | **Native** Windows scheduled task | **Native/report-only** webhook delivery |
| Validate request-v2 | Existing validator | Existing validator | Existing validator | Existing validator |
| Claim/admit once | Existing dispatcher mutex/state | Existing dispatcher mutex/state | Existing dispatcher mutex/state | Queue is at-least-once; existing dispatcher still provides admission guard |
| Execute provider prompt | Existing OpenClaw executor/browser skills | Existing | Existing | Existing |
| Independently verify result | Existing verifier | Existing | Existing | Existing |
| Publish verified result to repository | **New** MCP/result publisher | **New** deterministic Git publisher | **New** deterministic Git publisher | **New** deterministic Git publisher |
| Return to exact planning context | **Unknown but structurally plausible** tool result | **Missing** | **Missing** | **Missing** |
| Planner creates dependent request B | **Unknown; decisive POC** | Manual resume required | Manual resume required | Manual resume required |
| Duplicate wake-up | Existing idempotency | Existing idempotency | Existing idempotency | Hookaido retry plus existing idempotency |
| Crash before external submission | Query/retry adapter required | Existing state can permit safe reconciliation before `started` | Same | Same |
| Crash after durable `started` | Existing fail-closed indeterminate state | Existing fail-closed indeterminate state | Same | Same |
| Gateway/service recovery | MCP service still depends on OpenClaw Gateway | **Live:** supported service installed; Cron resumed after Gateway restart | Scheduler can start/check Gateway, but integration is new | Local delivery still depends on Gateway health |

## Reuse, copying, and new derivation

All reuse estimates concern the bounded execution path, not the complete weekly orchestration system.

| Option | Estimated reusable share | Existing components reused unchanged | New derived work | Derivation risk |
|---|---:|---|---|---|
| OpenClaw Cron inbox | **80–90% for the local forward path** | Request-v2 validator, dispatcher mutex/state, prompt freeze, OpenClaw execution skills, evidence verifier, live Cron command surface, inbox processor, terminal receipts | Remote Git request ingestion, result publisher, planner handoff marker | Low for local forward path; medium for complete feedback loop |
| Windows Scheduler inbox | **75–85%** | Same execution core and evidence chain | Same inbox/result adapters, scheduled-task definition, Windows identity/startup configuration, Gateway health/start behavior | Low–medium |
| ChatGPT MCP synchronous | **60–70%** | Existing execution backend, validator, dispatcher, verifier | Narrow MCP server/tool contract, authentication/tunnel, synchronous wait/status query, Git result publisher, lost-call recovery, account policy validation | High |
| Hookaido webhook queue | **50–60%** | Existing execution backend after local delivery | Hookaido install/config, reachable signed ingress, event mapping, queue/DLQ operations, subprocess adapter, Git publisher, planner handoff | High |

Copying an existing product or native feature does not eliminate Apex-specific integration risk. Cron and Task Scheduler can be configured rather than invented, but the inbox state transitions and result/feedback bridge still need to be derived. Hookaido supplies durable event delivery but does not supply the Apex request contract or planning-context return. MCP may eliminate asynchronous callback design, but only if the exact account and tool call behave as required.

## Investment, tokens, and operating value

| Option | First POC investment | New services | New credentials | Trigger AI tokens | Ongoing operator work | Main value | Main cost/risk |
|---|---|---:|---:|---|---|---|---|
| OpenClaw Cron inbox | Local trigger implemented in one focused session | 0 beyond existing Gateway | None for local trigger; Git publication credentials may be required | **0** | Resume planner manually; intervene on auth/indeterminate failures | Fastest reuse of installed stack | Remote request/result transport and feedback remain open |
| Windows Scheduler inbox | About one focused day | Windows built-in scheduler | Execution identity and possibly Git credentials | **0** | Same manual planner resume | Independent startup and recovery surface | Split observability between Windows and OpenClaw |
| ChatGPT MCP synchronous | Several days for a credible POC | MCP service plus secure connection/tunnel where required | MCP/app and scoped repository credentials | No trigger model; planner/tool turns remain | Potentially none after initial planning if confirmations are avoidable | Only shortlist option designed to return directly to the same planner | Eligibility, confirmations, timeout, reconnect, and beta-surface risk |
| Hookaido webhook queue | Several days | Hookaido daemon and ingress path | Webhook secret plus local/Git credentials | **0** | Manual planner resume remains | Durable event-driven delivery, retries, and DLQ | New daemon, ingress exposure, and no solved feedback edge |

AI-token cost is not the dominant differentiator between the three asynchronous triggers: each can wake deterministically without a model call. The major token risk is an architecture that uses an AI turn merely to poll, route, validate, or retry. None of the shortlisted implementations should do that. Subscription-AI tokens should be spent on planning, research, synthesis, and evaluation—not trigger plumbing.

## Candidate workflows and decisive tests

### 1. OpenClaw Cron plus repository inbox

**Process:** the planning surface publishes one complete frozen request; an exact-argv Cron command runs a thin scanner; the scanner validates and invokes the existing dispatcher; the existing verifier produces a verified receipt; a separate deterministic publisher records the result; the planner is resumed manually until a feedback mechanism is proven.

**Dependencies:** the Gateway service, Cron command execution, declared inbox/state paths, and current dispatcher/verifier are live. Remote request publication, result publication, existing provider login, and same-planner feedback remain dependencies for a complete loop.

**Likely failures:** Gateway stopped, job registered under the wrong Windows identity, request observed before publication is complete, invalid request repeated forever, Git conflict, provider logout, UI drift, or crash after `started`.

**Decisive POC status:** exact-argv registration, empty Cron runs, invalid-request quarantine, overlap protection, and Gateway-restart resumption pass. A valid real browser submission remains behind its explicit external-submit gate. Remote request publication, durable result push, and dependent request B remain unproved.

### 2. Windows Task Scheduler plus repository inbox

**Process:** identical to the Cron topology after wake-up, but a Windows scheduled task performs reconciliation and may also start or health-check the Gateway.

**Dependencies:** stable Windows execution identity, working directory, environment/module paths, Git credentials if publication is added, Gateway start procedure, and the same inbox processor.

**Likely failures:** task succeeds under an interactive user but fails while logged out, missing environment variables, browser profile unavailable to the task identity, working-directory drift, or task/Gateway logs becoming disconnected.

**Decisive POC:** run the same Cron test set across logout and reboot. Reject the option if the intended service identity cannot launch the managed browser and provider session reliably.

### 3. ChatGPT custom MCP synchronous dispatch

**Process:** the operator starts the planning chat; the planner invokes a narrow tool with one frozen request; the tool validates, dispatches, waits or queries by the same idempotency key, publishes verified artifacts, and returns immutable evidence references to that same tool call; only then may the planner create request B.

**Dependencies:** actual account eligibility, enabled custom MCP actions, acceptable confirmation policy, secure tool connectivity, bounded tool duration, reconnect/status-query contract, scoped repository credentials, and the existing dispatcher/verifier.

**Likely failures:** feature unavailable on the account, mandatory confirmation on every call, tool timeout before browser completion, lost tool result, reconnect minting a new idempotency key, unsupported local/private connection, or planner continuing without verified evidence.

**Decisive POC:** before building general infrastructure, expose one harmless idempotent tool that returns a delayed canary. Prove the exact planning conversation receives the result and derives request B from a nonce present only in result A. Repeat delivery of the same tool result and prove only one B is created.

### 4. Hookaido webhook queue plus local dispatch

**Process:** a repository or other authorized event sends a signed webhook; Hookaido verifies and durably queues it; local subprocess delivery maps the event to the existing validator/dispatcher; acknowledgement occurs only after durable local acceptance; results are published separately.

**Dependencies:** verified current Hookaido package, signed ingress reachable from the event source, daemon lifecycle, durable queue storage, event-to-request mapping, credentials, dispatcher integration, and result publisher.

**Likely failures:** accepting an unauthenticated or replayed event, duplicate at-least-once delivery, unavailable ingress, DLQ accumulation, event payload not containing complete request bytes, queue accepted while Gateway remains unavailable, and still no planning-context callback.

**Decisive POC:** prove one signed event is accepted, one bad signature is rejected, one local delivery is NACKed and retried with the same delivery identity, and the dispatcher still produces only one external submission. Do not adopt it unless polling latency is measured to be unacceptable.

## Scenario decisions

| Scenario | Decision |
|---|---|
| Current host, MCP eligibility unknown, Gateway and local Cron trigger healthy | Keep Option 1 selected; test one approved valid browser request next, then implement only the remote publication/feedback seam actually required by the planning surface. |
| ChatGPT full MCP actions are available and the delayed canary returns to the same chat without routine confirmation | Promote MCP to the first complete-loop POC; retain the existing dispatcher/verifier as its backend. |
| Full MCP is unavailable, times out, or cannot reconnect idempotently | Reject synchronous MCP for this pilot; use repository-backed forward dispatch and keep planner resumption explicit. |
| OpenClaw Cron does not survive Gateway restart or cannot run under the required Windows identity | Use Windows Task Scheduler with the same scanner and execution backend. |
| Polling works and latency is operationally acceptable | Do not install Hookaido. |
| A measured use case requires immediate remote Git-triggered delivery and polling fails the requirement | Test Hookaido before building a custom webhook receiver or workflow engine. |
| Any option reaches `IDEMPOTENCY_INDETERMINATE` after `started` | Stop and preserve evidence; do not automatically resubmit. |

## Required acceptance evidence before declaring a winner

The selected topology must pass all of these tests with durable evidence:

1. one harmless direct X1 execution proving the existing live browser and evidence chain;
2. planning or publication of request A without changing its prompt bytes;
3. automatic trigger and one external submission;
4. verified result A published durably;
5. request B authored only after the planner receives a nonce from A;
6. malformed request produces a terminal validation record and zero browser submissions;
7. duplicate delivery produces one external submission;
8. crash before `started` safely reconciles;
9. crash after `started` fails closed without blind resubmission;
10. provider logout/UI failure preserves the frozen request and does not switch provider or relax success criteria;
11. duplicate feedback produces only one planning decision for B;
12. the final evidence identifies the exact repository revision, request hash, prompt hash, provider turn, result hash, and planning context.

Until one option passes this complete two-dependent-batch test, the correct status is:

> **No verified complete loop. OpenClaw Cron is the preferred first trigger experiment; synchronous MCP is the preferred complete-loop hypothesis to falsify when the account supports it.**

## Sources used

### Supplied research

- `Subscription-AI-to-OpenClaw-Trigger-Feedback-Research.md`
- `Apex Orchestration Reliability Pilot — GitHub Deep Research Decision Report.md`
- `Deep Research Report: Subscription-AI Planning to OpenClaw Execution and Feedback Loop` (pasted text)

### Live repository and runtime authority

- `FEE2/00-WEEKLY-ORCHESTRATION-PILOT.okf.md`
- `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
- `scripts/openclaw/validate-execution-request.py`
- `scripts/openclaw/dispatch-execution-request.ps1`
- `scripts/openclaw/verify-execution-evidence.py`
- `scripts/openclaw/tests/`
- Local `openclaw --version`, `openclaw cron --help`, `openclaw cron add --help`, and `openclaw gateway status --json` observations from 2026-08-15.

### Primary references to recheck immediately before implementation

- OpenClaw Cron CLI: <https://docs.openclaw.ai/cli/cron>
- Microsoft `schtasks`: <https://learn.microsoft.com/windows-server/administration/windows-commands/schtasks>
- The current official OpenAI documentation for custom MCP apps/actions and the exact planning account's enabled features.
- The current Hookaido repository/package documentation and release metadata.
