---
okf: open-knowledge-format
okf_version: 1
title: "FEE2 Weekly-Orchestration Pilot"
document_role: pilot_control_and_iteration_ledger
created: 2026-08-15
updated: 2026-08-15
status: static_readiness_pass_waiting_on_project_intake
authority_state: candidate
operator_validation: design_approved
workspace: FEE2
canonical_state_policy: references_only_no_duplicate_task_status
pilot_mode: contract_first_compressed_vertical_slice
live_controller: Claude_Code
coach_validator_improver: Codex
execution_harness: OpenClaw
subscription_target: ChatGPT
executor_order:
  - openai/gpt-4.1-nano
  - apex-local/qwen3-8b-q4km
verdicts:
  orchestration: not_run
  local_executor: not_run
next_gate: real_project_intake
---

# FEE2 Weekly-Orchestration Pilot

## 1. Purpose

This is the single living control document for testing one complete APEX weekly-orchestration slice, learning from the first real failures, and improving only what blocks useful operation.

The pilot proceeds in this order:

1. tabletop the whole loop;
2. verify minimum readiness and repair only blockers;
3. intake a scoped real project;
4. run one compressed G1-G5 slice;
5. compare the known-working cloud executor with Qwen on the same frozen ChatGPT task;
6. route only confirmed project changes through Session;
7. verify that updated state feeds the next planning cycle;
8. make one causal improvement at a time.

This file owns the plan, current findings, decisions, cross-links, run ledger, and next action. It owns no project or task truth.

## 2. Success criteria

### 2.1 Orchestration verdict

Pass only when:

- Plan, Session, and Sync exchange one real project item successfully;
- G1-G5 produce valid packets at their canonical paths;
- every applicable operator decision is recorded in its packet, not only in chat;
- OpenClaw produces independently verifiable ChatGPT evidence;
- only operator-confirmed changes are applied through Session;
- Sync and ProjectStatus can read the confirmed change;
- the confirmed result appears in the next planning input.

### 2.2 Local-executor verdict

Pass only when Qwen completes the same frozen ChatGPT task as the cloud control with:

- valid tool calls;
- correction after a tool error rather than repeated identical calls;
- proof of real ChatGPT page interaction;
- faithful response capture;
- bounded retries and explicit stopping;
- no fabricated result;
- recorded latency and operator intervention.

These verdicts are independent. Cloud success may prove the orchestration path while Qwen remains unqualified for the task class.

## 3. Non-goals

The first pilot does not:

- run a full Monday-Friday production week;
- add providers beyond ChatGPT;
- install another runtime or model;
- add a scheduler, Cron job, persistent service, database, dashboard, or queue;
- turn OpenClaw into a planner, evaluator, router, or orchestration authority;
- create a new workflow or execution-request schema;
- automatically promote Qwen from one successful task to general eligibility;
- copy the previous `FEE` folder or treat it as current truth;
- duplicate canonical task status in this file;
- commit or push repository changes without a separate operator request.

## 4. Authority and current-truth order

When evidence conflicts, apply this order:

1. current explicit operator instruction;
2. measured live evidence from this pilot;
3. active machine configuration and installed runtime behavior;
4. current Weekly Orchestrator and Plan-Sync-Session contracts;
5. newest applicable repository implementation and tests;
6. newer FEE/OpenClaw handovers and corrections;
7. latest commits;
8. older `FEE` design, research, and historical notes.

Historical content is useful for provenance but may not override newer measured facts.

## 5. Current-truth baseline

### 5.1 Repository and commit context

Recent commits established the bounded executor foundation:

| Commit | Current relevance |
|---|---|
| `e500d723` | Handed over the bounded OpenClaw executor, configuration, provider skill, policy plugin, dispatcher, and tests. |
| `3937fd6e` / `006b3533` | Recorded browser containment decisions. |
| `fda719a0` / `cffd1367` / `36908cee` | Added and verified protected immediate dispatch bound to a versioned guard. |
| `325b71d4` | Added the bounded validation and safety wrappers. |
| `3568e5ab` / `4dffe063` / `35ef223b` | Recorded provider limitations, installation gates, and the original local-executor architecture. |
| `b2e3e070` | Added subscription-AI browser-orchestration knowledge. |
| `26135781` | Handed over the earlier FEE project environment. |

The working tree contains newer user-owned OpenClaw changes. They must be preserved and validated rather than replaced from `HEAD`.

### 5.2 Measured state that supersedes the older framing

- The OpenClaw harness and managed-browser path work with a cloud executor.
- `gpt-4o-mini` demonstrated real page interaction and tool-error correction; the active executor default is now `openai/gpt-4.1-nano`.
- Qwen3-8B repeatedly reused invalid tool calls and fabricated an answer after browser calls failed. It is not qualified for multi-step browser work.
- The Qwen Vulkan backend suffered repeatable device-loss failures as context grew. `GGML_VK_DISABLE_COOPMAT=1` prevented the observed crash at a throughput cost, but does not solve tool-use capability.
- Active OpenClaw uses a managed `openclaw` browser profile, 32K executor context, and a cloud default. The repository template has now been reconciled to that topology without copying active secrets.
- The active Gateway and Qwen listeners were both stopped during the 2026-08-15 readiness inspection.
- Existing weekly packets are from July 2026. Their gates are not current pilot evidence.
- The current Session handoff describes the unrelated NARM-support knowledgebase and must not seed this pilot.
- The installed browser-policy Node suite passed 10/10 on 2026-08-15. That selected-tab policy remains available but is disabled and is not on the managed-browser pilot path.
- Python wrapper failures observed inside the Codex process resolve to inherited PowerShell module-path shadowing: Windows PowerShell imports the Codex-bundled `Microsoft.PowerShell.Utility` module instead of its native module and cannot auto-resolve `Get-FileHash`. This is an execution-environment finding, not yet a wrapper regression.
- The installed OpenClaw `2026.7.1-2` browser action contract does not support every action shape currently written in provider guidance. Provider references must be verified against the installed schema before a paid/live turn.
- The readiness audit found several live-path automation blockers: the dispatcher required a pre-opened Chrome-extension tab, required the selected-tab policy plugin, forced reasoning off, timed out after 120 seconds, and the executor skill expected legacy packet fields absent from request v2. These blockers are removed for the ChatGPT pilot.
- OpenClaw now selects an existing ChatGPT tab or opens `https://chatgpt.com/` itself. The operator does not prepare provider tabs.
- A second automation-friction audit found no remaining tab freeze, provider-tab allowlist, or manual tab-preparation requirement on the managed-browser path. OpenClaw may open and navigate the declared provider itself; the remaining fixed fields are the task's provider/settings and evidence destinations, not browser movement.
- A zero-exit OpenClaw turn is no longer sufficient for success. The dispatcher now requires OpenClaw's completed status, a non-empty declared result, a matching executor receipt, and harness-owned browser transcript proof of one exact prompt insertion, one submission, and the captured response before it records completion.

## 6. User stories and role allocation

| Actor | User story | Owns | Must not own |
|---|---|---|---|
| Operator | I provide project intent once, approve consequential choices, and can see exactly where the loop is. | Real project facts, privacy approval, G1-G5 decisions, external submission approval, consequential mutation approval. | Fabricated evidence or implicit confirmations. |
| Claude Code | I conduct the implemented weekly system through its native skills and stage agents. | Weekly stage dispatch, packet handoffs, gate presentation, Session routing. | OpenClaw execution internals or unconfirmed project mutation. |
| Codex | I coach, inspect, validate, diagnose, and make the smallest approved improvement. | Tabletop, evidence audit, causal classification, focused repository changes, FEE2 ledger. | Pretending a manual emulation proves Claude's native wiring. |
| OpenClaw | I execute one frozen request in the declared browser/provider scope and return evidence. | Browser operation, exact prompt submission, capture, bounded error handling. | Planning, provider choice, evaluation, scheduling, or project-state mutation. |
| ChatGPT subscription | I produce the substantive answer requested by the frozen project prompt. | Requested web-AI output. | Authority over tools, paths, gates, or next actions. |
| Apex Plan | I turn approved source material into project/task proposals. | Capture, decomposition, dependencies, qualitative priority. | Exact ranking or durable mutation. |
| Apex Sync | I compute deterministic next actions, blockers, drift, and scores. | Read-side reports through `scripts/apex_sync.py`. | Narrative planning or task mutation. |
| Apex Session | I apply operator-confirmed changes and refresh handoff/planning context. | Confirmed mutation and H6 handoff artifacts. | Ranking, blocker scans, or silent writes. |
| Python/PowerShell/Git | We perform exact transformations, checks, hashes, and bounded dispatch. | Deterministic validation and evidence. | Semantic judgment. |

## 7. Artifact ownership

| Information | Canonical owner/path | FEE2 behavior |
|---|---|---|
| Project and task records | `apex-meta/epics/` | Link and summarize only. |
| Session handoff and planning feed | `apex-meta/handoff/` | Link and record confirmation state only. |
| Weekly plan | `artifacts/weekly-plans/` | Link packet and gate result. |
| Next-day plan | `artifacts/next-day-plans/` | Link packet and gate result. |
| Flow packets and prompt packs | `artifacts/flow-packets/<YYYYMMDD>/` | Link exact files and validation state. |
| Prompt bodies | `artifacts/flow-packets/<YYYYMMDD>/prompt-packs/bodies/` | Link exact frozen body. |
| Normalized evidence/skip markers | `artifacts/flow-packets/<YYYYMMDD>/` | Link exact G3 input. |
| FlowRecap and Status Merge | `artifacts/flow-recap-packets/` | Link packet, candidate/confirmed status, and gate. |
| Sync computation | stdout/JSON from `scripts/apex_sync.py` or a declared report path | Record command, result, and evidence reference. |
| OpenClaw request/capture/receipt | Request-declared evidence directory | Link request, result, receipt, transcript evidence, and hashes. |
| Pilot plan/findings/decisions | `FEE2/00-WEEKLY-ORCHESTRATION-PILOT.okf.md` | Canonical here. |

## 8. End-to-end stage map

Connection states are `connected`, `missing`, `contradictory`, or `unproven`.

| Stage | Owner / AI surface | Input | Canonical output | Operator checkpoint | Failure condition | Next consumer | State |
|---|---|---|---|---|---|---|---|
| P0 real-data intake | Operator + Codex | Free-form scoped project material | Approved intake packet referenced from FEE2 until Plan consumes it | Privacy/shareability confirmation | Missing goal, current state, or safe ChatGPT subset | Apex Plan | `missing` — real data not supplied |
| P1 project proposal | Claude `apex-plan-ops` / CLI AI | Approved intake and relevant confirmed state | `apex-meta/handoff/apex_plan_packet-*.md` | Approve decomposition and dependencies | Proposal invents facts or enters Sync/Session scope | Apex Session and Sync | `connected` by contract; live pilot unproven |
| P2 confirmed project capture | Claude main thread + `apex-session` | Approved Plan packet | `apex-meta/epics/<slug>/` plus refreshed `apex-meta/handoff/` | Consequential mutation confirmation | No confirmation, invalid status, source conflict | Apex Sync and G1 | `unproven` — skill exists; no dedicated Session agent wrapper |
| P3 deterministic sync | Python | Confirmed task files | Native next/blocker/score JSON reports | None for dry-run | Malformed task graph or nonzero exit | PreCap Week and operator | `connected` — current unrelated NARM graph passes |
| G1 PreCap Week | Claude `apex-precap-week` | Weekly intent, confirmed Session feed, relevant Sync reports, calendar constraints | `artifacts/weekly-plans/weekly_plan_packet-<date>-<week>.md` | G1 weekly direction | Invalid envelope or unresolved priority conflict | PreCap Next Day | `connected` by contract; current pilot unproven |
| G2 PreCap Next Day | Claude `apex-precap-next-day` | G1 packet, Session/Sync context, daily constraints | Next-day plan, flow packet, prompt pack, prompt body under `artifacts/` | G2 day/flow plan and exact prompt approval | Missing weekly/daily intent, invalid pack, unresolved body | Execution actor | `connected` by contract; prompt-body materialization unproven |
| X0 freeze execution | `scripts/fee` + Codex/operator | Flow packet, prompt pack, materialized body | Frozen plan and ledger under the flow artifact family | Pre-run review when degraded | Unresolved ref, route ambiguity, hash mismatch | OpenClaw request preparation | `connected` for fixtures; no live prompt body proven |
| X1 OpenClaw request handoff | Codex/operator for pilot | Frozen prompt and approved ChatGPT route | Concrete `apex.execution-request/v2` in declared evidence directory | Exact external-submit approval | Provider tuple, roots, result path, or evidence path not explicit | OpenClaw dispatcher | `missing` as an automated G2 call site; direct dispatcher seam approved for the pilot |
| X2 cloud execution | OpenClaw + `gpt-4.1-nano` | Frozen request v2 | Captured ChatGPT result and execution evidence | Verify real page/result | No page transition, schema loop, capture mismatch, duplication | G3 normalization | `unproven` for ChatGPT; prior Perplexity cloud evidence exists |
| X3 Qwen comparison | OpenClaw + Qwen3-8B | Identical frozen request in fresh ChatGPT conversation | Capability evidence only | Approve second external submission | Cloud control failed, fabrication, repeated invalid calls, runtime crash | FEE2 local-executor verdict | `contradictory` — target architecture vs measured Qwen capability |
| G3 evidence intake | Operator + `apex-evidence-normalize` | Cloud execution result and evidence references | Normalized dump or skip marker under the flow folder | Confirm execution evidence/skip state | Evidence cannot be bound to a planned flow | FlowRecap | `connected` by contract; live OpenClaw evidence bundle unproven |
| G4 FlowRecap | Claude `apex-flow-recap` | Flow packet plus normalized dump | `artifacts/flow-recap-packets/flow_recap_packet-*.md` | G4 candidate delta and next-step approval | Evidence contradiction or invalid envelope | Status Merge | `connected` by contract; pilot unproven |
| G5 Status Merge | Claude `apex-status-merge` | G4-confirmed recap plus confirmed prior state | `artifacts/flow-recap-packets/status_merge_packet-*.md` | G5 conflict and mutation approval | Unresolved conflict or unconfirmed recap | Apex Session | `connected` by contract; pilot unproven |
| C1 confirmed mutation | Claude main thread + `apex-session` | G5-confirmed mutation proposal and evidence refs | Mutation receipt and refreshed planning feed | Final consequential write confirmation | Missing confirmation or source mismatch | Sync and ProjectStatus | `unproven` |
| C2 closure verification | Apex Sync + `apex-project-status` | Confirmed records and receipt | Sync report, compact status, next planning input | Accept orchestration verdict | Updated state not visible or candidate treated as truth | Next G1/G2 cycle | `unproven` |

## 9. Tabletop simulation

### 9.1 Hypothetical item

```yaml
hypothetical_project_item:
  project: Pilot Project Alpha
  goal: Choose an evidence-backed implementation direction for one bounded feature.
  current_state: Source notes exist; no confirmed task record exists.
  weekly_outcome: Produce and confirm one recommendation with cited trade-offs.
  task_for_chatgpt: Synthesize the approved non-sensitive source subset into a recommendation.
  constraints:
    - use only the supplied subset
    - separate evidence from inference
    - return one recommendation and named uncertainties
  expected_status_change: proposed task moves from open to done only after evidence and operator review
```

### 9.2 Simulated trace

1. Codex normalizes the operator's free-form notes without creating canonical status.
2. Claude Plan proposes the epic/task and source references.
3. The operator approves; Session writes the task and planning feed.
4. Sync reports the task as actionable.
5. PreCap Week includes the project in the weekly direction; G1 confirms it.
6. PreCap Next Day creates one active flow and materializes a ChatGPT prompt body; G2 confirms the exact body.
7. `scripts/fee` freezes the referenced prompt and hashes the plan.
8. The pilot Codex/Claude seam constructs one request-v2 packet and calls the OpenClaw dispatcher.
9. `gpt-4.1-nano` selects or opens ChatGPT and captures the real answer. Independent checks verify URL, bytes, hash, and one submission.
10. Only after cloud success, Qwen receives a paired request-v2 envelope referencing the same frozen prompt hash and provider settings in a fresh conversation. Its result is retained only as model evidence.
11. The cloud evidence is normalized at G3.
12. FlowRecap produces a candidate project delta; G4 confirms or revises it.
13. Status Merge compares it with confirmed Session/Sync state; G5 confirms or rejects the mutation proposal.
14. Session applies the confirmed change and produces the receipt/planning feed.
15. Sync and ProjectStatus read the new state, proving the loop closed.

### 9.3 Tabletop result

```yaml
tabletop_result:
  status: complete
  architecture_understood: true
  canonical_path_map_complete: true
  gate_map_complete: true
  connections:
    connected_by_contract: 8
    missing: 2
    contradictory: 1
    unproven: 8
  decisive_missing_connections:
    - real_project_intake
    - automated_flow_pack_to_openclaw_request_bridge
  accepted_pilot_workaround:
    - operator_reviewed_manual_request_v2_handoff_for_the_first_slice
  verdict:
    orchestration: not_run
    local_executor: not_run
```

## 10. Minimum readiness blockers

Only these items may block the first live slice:

| ID | Blocker | Class | Minimum resolution | Status |
|---|---|---|---|---|
| R1 | Active OpenClaw configuration and repository template described different topologies. | contract/config drift | Reconcile documented template and tests with the active managed-browser/cloud-control design without exposing secrets. | complete |
| R2 | Provider guidance and dispatch required selected/pre-opened tabs and contained action shapes conflicting with installed OpenClaw. | UI/tool contract | Let OpenClaw open the declared provider URL; align ChatGPT type/press actions and request-v2 executor fields with `2026.7.1-2`. | complete |
| R3 | Gateway, browser, and Qwen server are stopped. | runtime | Use the already-installed start procedures; do not reinstall. Confirm listeners and browser profile before the external gate. | open |
| R4 | Claude's native weekly dispatch had not been proven in the current repository state. | wiring | Run a bounded native dry/tabletop invocation that stops before operational writes or external execution. | complete |
| R5 | No real project data or privacy-approved ChatGPT subset exists. | operator input | Operator supplies free-form data; Codex prepares a scoped intake preview for approval. | waiting_on_operator |
| R6 | No concrete prompt body/request/evidence directory exists for the pilot. | execution input | Materialize during G2, freeze through FEE, then prepare one reviewed request-v2 packet. | waits_for_R5_and_G2 |
| R7 | `scripts/fee emit` cannot yet assemble a completed evidence bundle. | integration | For the first slice, bind the OpenClaw result and receipt directly into the normalizer input by explicit references; assess automation after the run. | accepted_manual_seam |
| R8 | Python wrapper tests inherit an incompatible Codex PowerShell module path. | test environment | Run those tests with `PSModulePath` cleared so native Windows PowerShell initializes its own modules; do not change production wrappers. | complete |
| R9 | A zero-exit OpenClaw CLI result could be recorded as complete even when the actual turn timed out or produced no verified capture; model-authored result/receipt files alone could not disprove fabrication; Qwen could also run without a genuine completed cloud control. | evidence/ordering | Freeze the exact prompt as a file; verify the result/receipt against harness-owned browser transcript evidence; bind the verified receipt to dispatcher-owned completion state; require that complete evidence chain before Qwen dispatch. | complete |

## 11. Readiness sequence

1. Claude Code discovered the Weekly Orchestrator, all named G1-G5 stage agents, and Plan/Session/Sync in a read-only native invocation.
2. Active OpenClaw settings were compared without printing secret values; the repository template was reconciled and accepted by `openclaw config patch --dry-run`.
3. Focused tests were written before correcting the managed-browser, ChatGPT action, request-v2, model-selection, and dispatcher contracts.
4. OpenClaw may now select or open the declared provider URL; no pre-opened tab or browser-policy plugin is required.
5. Cloud/Qwen executor selection is explicit; Qwen requires the verified cloud receipt for the identical prompt and settings.
6. Completion requires a result/receipt bundle corroborated by the harness-owned browser transcript, not merely a zero-exit process or model-authored files. Focused Python tests pass; browser-policy tests remain an independent regression suite.
7. Runtime processes remain stopped until a real, approved prompt exists. Then use the commands below and verify the page before submission.
8. Stop for the real-project intake gate.

### 11.1 Reproducible runtime start and health commands

Cloud and managed-browser preflight, in separate native PowerShell processes:

```powershell
$env:OPENCLAW_GATEWAY_TOKEN = [Environment]::GetEnvironmentVariable('OPENCLAW_GATEWAY_TOKEN', 'User')
openclaw gateway run

openclaw browser start --browser-profile openclaw
openclaw browser status --browser-profile openclaw --json
openclaw browser tabs --browser-profile openclaw --json
```

Qwen comparison only, after cloud success:

```powershell
$env:GGML_VK_DISABLE_COOPMAT = '1'
& 'C:\LocalModels\runtimes\llama.cpp\llama-server.exe' --model 'C:\LocalModels\qwen3-8b\gguf-q4km\Qwen3-8B-Q4_K_M.gguf' --host 127.0.0.1 --port 8090 --ctx-size 32768 --parallel 1 --gpu-layers 999 --jinja --reasoning-budget 128
```

The cloud dispatch uses the default `-ExecutorModel openai/gpt-4.1-nano`; the comparison uses `-ExecutorModel apex-local/qwen3-8b-q4km`. OpenClaw itself opens ChatGPT when no matching tab exists.

## 12. Real-project intake contract

The operator may provide unstructured notes. Codex will prepare a reviewable subset with:

```yaml
project_intake:
  project_name: required
  project_goal: required
  current_state: required
  desired_weekly_outcome: required
  known_tasks: []
  dependencies: []
  blockers: []
  deadlines: []
  constraints: []
  bounded_chatgpt_task: required
  chatgpt_context_subset: required
  excluded_sensitive_material: []
  safe_to_submit_to_chatgpt: operator_confirmation_required
```

No canonical project record or external submission occurs before operator review.

## 13. Live-run gates

| Checkpoint | Required operator decision | Durable record |
|---|---|---|
| Intake/privacy | The scoped subset is accurate and safe for ChatGPT. | This file plus the Plan source reference. |
| Plan mutation | The proposed epic/tasks may become confirmed state. | Session mutation record/receipt. |
| G1 | Weekly direction is accepted. | Weekly packet `operator_validation`. |
| G2 | Day/flow plan and exact prompt are accepted. | Next-day/flow packet validation. |
| External submit 1 | The frozen prompt may be submitted through the cloud executor. | OpenClaw request and operator decision reference. |
| G3 | Cloud execution evidence is accepted as the flow's raw evidence. | Normalized dump/skip marker. |
| External submit 2 | The same prompt may be submitted through Qwen for comparison. | Separate OpenClaw request/evidence set. |
| G4 | Candidate delta and proposed next step are accepted. | FlowRecap packet validation. |
| G5 | Merged candidate changes may be routed to Session. | Status Merge validation. |
| Final mutation | Consequential project changes may be written. | Session receipt and refreshed planning feed. |

## 14. Failure and improvement loop

At the first useful failure:

1. stop the affected stage;
2. preserve the artifact as candidate, blocked, or invalidated;
3. classify the failure as `contract`, `wiring`, `runtime`, `ui_drift`, `model_capability`, `evidence`, or `operator_input`;
4. identify evidence for one causal hypothesis;
5. make the smallest change that tests that hypothesis;
6. rerun the failed segment;
7. rerun the complete thin slice once after the segment passes;
8. defer every unrelated improvement.

Hard failures are fabricated output, missing evidence, gate bypass, duplicate submission, undeclared authority, and unconfirmed durable mutation.

## 15. Iteration ledger

| Iteration | Expected behavior | Actual evidence | Verdict | Smallest improvement | Rerun | Deferred |
|---|---|---|---|---|---|---|
| I0 Tabletop | Every actor, artifact, gate, and seam is identified. | Sections 5-10; live repo/CLI/config inspection on 2026-08-15. | pass | None. Move to readiness. | not needed | Full-week simulation. |
| I1 Readiness | Claude/OpenClaw contracts are internally consistent and do not push browser setup onto the operator. | Claude native discovery passed; OpenClaw config dry-run passed; 65 focused Python tests passed with 3 live-only skips; browser-policy tests passed 10/10. | pass_static | Removed pre-opened-tab/policy requirements, selected the managed profile, aligned request v2, set a 600-second turn, honored model reasoning, froze the exact prompt, corroborated capture with the harness browser transcript, and bound Qwen comparison to dispatcher-confirmed cloud evidence. | 65 Python pass, 10 Node pass | Live auth/UI proof at the approved external gate; Gemini/Perplexity expansion, persistence, Cron. |
| I2 Project intake | One scoped real project is confirmed and Sync-readable. | Waiting for operator data. | not_run | None until intake exists. | not_run | Additional projects. |
| I3 Cloud slice | Cloud executor closes the real G1-G5 loop with direct evidence. | Not run. | not_run | Stop at first useful failure. | not_run | Five-day run. |
| I4 Qwen comparison | Qwen completes the identical request without fabrication or schema-loop failure. | Not run. | not_run | One model/runtime/workflow change only if evidence supports it. | not_run | General Qwen qualification. |
| I5 Closure | Session mutation is confirmed and visible in next planning context. | Not run. | not_run | Repair only the failed handoff. | not_run | Production automation. |

## 16. Current verdict and next action

```yaml
current_verdict:
  tabletop: pass
  readiness: static_pass
  orchestration: not_run
  cloud_executor: not_run_for_chatgpt_pilot
  local_executor: not_qualified
  production_readiness: not_assessed

next_action:
  owner: Operator_then_Codex
  action: provide_and_normalize_real_project_data_for_the_scoped_intake_preview
  stop_condition: safe_to_submit_to_chatgpt_is_not_confirmed

next_operator_input_after_readiness:
  request: provide_free_form_real_project_data_for_the_scoped_intake_preview
  privacy_rule: no_external_submission_until_safe_to_submit_to_chatgpt_is_confirmed
```
