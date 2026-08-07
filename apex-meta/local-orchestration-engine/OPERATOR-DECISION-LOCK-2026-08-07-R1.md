---
title: "FEE / Local Execution Layer — Operator Decision Lock, Round 1"
doc_type: operator_decision_lock
initiative: local-orchestration-engine
created: 2026-08-07
authority: operator-session-2026-08-07
status: "operator-confirmed round-1 decisions; platform/model/browser details remain research-gated"
base_commit: 0239c2c6c128210fab764133f1d0244a3028d12b
supersedes_when_conflicting:
  - apex-meta/local-orchestration-engine/DESIGN-LOCK-QA.md candidate assumptions from 2026-07-28
  - apex-meta/local-orchestration-engine/architecture/04-decision-ledger.md candidate rows whose premises conflict with this operator clarification
notes:
  - "This addendum does not itself change any live upstream contract or gate."
  - "Consolidate these decisions back into DESIGN-LOCK-QA.md and architecture/04-decision-ledger.md during the next architecture cleanup pass."
---

# Operator Decision Lock — 2026-08-07, Round 1

## 1. Why this addendum exists

The July design pass produced useful FEE architecture and implementation, but several decisions were made against a narrower interpretation of the local model: mainly a toolless adjudicator/narrator attached to Weekly Orchestrator step 4.

The operator clarified on 2026-08-07 that the long-term target is broader and more specific:

- the **subscription/deep-reasoning models** own substantive reasoning, planning, synthesis, project-management intelligence, and high-quality prompt creation;
- **Claude Code / Codex and similar CLI AIs** are scarce specialist resources for hard coding, architecture, difficult diagnosis, consequential verification, and work that genuinely requires their capabilities;
- the **local LLM** is primarily an **execution operator** that substitutes for human/CLI operational effort: it follows externally designed plans, operates subscription websites, runs bounded tools and scripts, captures outputs, handles small operational failures, and escalates when a problem exceeds its authority;
- the **deterministic layer** (Python, PowerShell, Git, validators, ledgers, exact transforms) should perform every task that can be made reliable without model judgement.

The local LLM is **not trusted as the substantive reasoning or project-management authority**.

This clarification is a valid reason to reopen July candidate decisions whose rationale depended on the narrower toolless-M5 premise.

---

## 2. Four-layer operating model — LOCKED

```text
Layer 4 — Subscription / deep-reasoning AI
  Thinks, plans, researches, synthesizes, judges, manages project reasoning.

Layer 3 — Scarce CLI AI
  Claude Code / Codex for difficult coding, architecture, hard diagnosis,
  consequential review and verification.

Layer 2 — Local LLM execution operator
  Executes plans, drives interfaces, runs bounded tools, captures evidence,
  performs small operational recovery, and escalates rather than inventing strategy.

Layer 1 — Deterministic execution
  Python / PowerShell / Git / validators / ledgers / exact transformations.
```

Allocation principle:

> Use the lowest-cost, least-reasoning layer that can perform the task reliably; escalate only when the lower layer cannot safely complete the work.

The purpose of the local layer is specifically to reduce routine human and scarce-CLI operational load without transferring substantive reasoning authority to a weaker model.

---

## 3. Round-1 decisions — OPERATOR CONFIRMED

The operator confirmed all recommended Round-1 choices on 2026-08-07.

| Decision | Confirmed option | Locked meaning |
|---|---|---|
| R1-Q1 Local-model role | **B — bounded execution operator** | The local LLM may execute plans and solve small operational problems. It is not a project manager or trusted substantive reasoner. |
| R1-Q2 Next-step authority | **A — deterministic/external plan owns sequence** | The local LLM advances a declared plan and may select only pre-authorized recovery routes. It does not invent the project workflow. |
| R1-Q3 Tool access | **B — bounded tool broker** | The local LLM may use explicitly permitted browser/filesystem/script/Git/test/process tools within job scope. No unrestricted computer authority. |
| R1-Q4 Failure handling | **B — local repair ladder** | Deterministic retry -> known recovery -> bounded local diagnosis -> one safe recovery attempt -> package evidence -> CLI escalation -> human if needed. |
| R1-Q5 Product scope | **B — step-4 MVP, generic execution substrate later** | Weekly Orchestrator step 4 remains the first seam, but the long-term execution substrate may serve multiple orchestration/user flows without becoming a new reasoning authority. |
| R1-Q6 Executor platform | **E — hybrid, research before selection** | Keep FEE/deterministic protocol concepts as a candidate spine; research and test OpenClaw, Hermes, and Odysseus against real user flows before choosing their roles. No platform is selected yet. |
| R1-Q7 Human approval | **B — bounded overnight execution, morning review initially** | The machine may execute an already-authorized bounded plan unattended; consequential acceptance/canonical progression remains human-reviewed until empirical evidence justifies changing that boundary. |
| R1-Q8 Project-management intelligence | **C — subscription/deep-reasoning models** | Subscription reasoning models create/interpret plans and research. The local executor performs them. CLI AI is reserved for scarce specialist work. |

---

## 4. Concrete control-flow rule — LOCKED

The normal execution shape is:

```text
subscription/reasoning model creates plan + prompts
                    |
                    v
deterministic layer materializes/freeze-validates work packet
                    |
                    v
local LLM execution operator performs bounded operational work
  - open provider/session
  - submit declared prompt
  - wait/capture
  - run declared scripts/tools
  - follow declared recovery branches
                    |
                    v
raw evidence / artifacts returned
                    |
                    v
subscription/reasoning model interprets results and produces the substantive output
                    |
        hard technical exception only
                    v
             Claude Code / Codex
```

The local model may answer **"which declared execution state am I in?"** and **"which allowed recovery branch applies?"**.

It must not answer **"what should the project strategically do next?"** unless a higher-reasoning layer explicitly delegated a bounded, non-consequential classification task.

---

## 5. Bounded tool-broker rule — LOCKED AT PRINCIPLE LEVEL

The exact implementation remains to be designed, but the authority model is confirmed.

Candidate allowed capabilities when explicitly granted by a job packet:

- browser interaction;
- clipboard/input/output capture;
- read/write inside declared job/repository paths;
- run specified Python/PowerShell commands or allowlisted command families;
- Git status/diff/read-only inspection and explicitly authorized worktree operations;
- run tests/validators;
- inspect process exit status and bounded logs;
- create execution/evidence artifacts;
- perform deterministic database/knowledge hygiene operations whose transformation rules were defined by a higher-reasoning layer.

Not granted by default:

- unrestricted filesystem access;
- credential extraction;
- arbitrary deletion;
- arbitrary shell generated from captured web/model content;
- force-push or destructive Git history changes;
- system-wide configuration changes;
- cross-project writes not declared in the current job;
- reinterpretation of reasoning-model outputs as new executable commands unless those commands were already part of a trusted/pre-authorized plan.

The exact capability schema, safe-command policy, and sandbox implementation remain open design work.

---

## 6. Local repair ladder — LOCKED AT PRINCIPLE LEVEL

A routine operational failure should not immediately consume scarce CLI AI.

Default ladder:

1. deterministic retry when the failure class explicitly permits it;
2. apply a known deterministic recovery recipe;
3. local LLM performs bounded diagnosis from the command, exit state, small log slice, and declared environment facts;
4. local LLM may choose one pre-authorized safe recovery and retry;
5. if unresolved, create a compact failure/evidence packet;
6. escalate to Claude Code/Codex only when specialist reasoning or code repair is genuinely needed;
7. escalate to the human operator for consequential ambiguity, permissions, security, or failed specialist recovery.

Target to test later, not yet measured:

- deterministic recovery should absorb the largest share of routine failures;
- local bounded recovery should absorb a meaningful second share;
- scarce CLI intervention should become the exception rather than the default.

No success percentages are considered proven until benchmarked on real failures.

---

## 7. Multi-repo and multi-folder future state — OPERATOR REQUIREMENT

### 7.1 Weekly Orchestrator future architecture

The present single-repository Weekly Orchestrator is an intentional simplification/MVP, not the final scope.

The intended future process is:

```text
project repo A -> project state --\
project repo B -> project state ----\
project repo C -> project state -----+-> apexai-os-meta Weekly Orchestrator
personal/project inputs -------------/          |
                                                v
                                      weekly priorities + sprint guidance
                                                |
                                                v
                                      execution across the relevant repos
```

The Weekly Orchestrator in `apexai-os-meta` is intended to coordinate work across the operator's other project repositories by ingesting their project states and producing weekly/sprint guidance.

This multi-repo project-state ingestion is **not implemented yet** and requires its own later Weekly-Orchestrator/project-design work.

### 7.2 Execution-layer path policy

The execution substrate must therefore be designed so that multi-repo support is possible without a rewrite.

Requirements:

- do not hardcode a permanent single-repository worldview into the generic executor;
- expect much work to live under `C:\GitDev\...`, but **do not make `C:\GitDev` the only permitted root forever**;
- allow jobs to declare one or more explicit allowed roots/repositories;
- default to job-scoped path permissions rather than machine-wide access;
- cross-repo reads/writes must be explicit in the work packet;
- support future non-GitDev folders and personal-life artifact locations through configured roots/capabilities rather than ad-hoc unrestricted access.

The exact multi-repo state schema and cross-repo write policy remain open.

---

## 8. User-flow evaluation set — LOCKED AS THE DESIGN BASIS

Architecture/platform decisions must be tested against concrete user flows, not generic agent benchmarks.

### UF-A — subscription research executor

A reasoning model creates a set of prompts for Claude/ChatGPT/Gemini/deep-research surfaces. The local executor runs the prompts, captures results/artifacts, and returns them to the reasoning model for synthesis.

### UF-B — script failure recovery

A deterministic script fails for a small operational reason. The local executor classifies the failure, uses a permitted recovery recipe if available, retries safely, and escalates with evidence if unresolved.

### UF-C — Detective evidence collection

The local executor gathers diffs, tests, hashes, missing files, logs, contradictory source claims, and structural evidence. A stronger reasoning/CLI Detective performs consequential interpretation and judgement.

### UF-D — database / knowledge hygiene

A reasoning model defines transformation rules. Deterministic scripts handle exact cases; the local model handles bounded format anomalies; ambiguous semantic cases escalate.

### UF-E — multi-repo execution

The Weekly Orchestrator selects work across multiple project repositories. Each execution job declares the repositories/folders it may access. The local executor performs bounded work only inside those declared scopes.

### UF-F — personal weekly execution

A reasoning model creates personal/work weekly guidance from permitted sources. The local executor performs bounded operational steps, while sensitive/consequential actions remain gated according to a separately defined personal-security policy.

These flows are the minimum evaluation corpus for platform and local-model research.

---

## 9. July candidate decisions explicitly reopened or amended

The following older candidate positions must not be treated as settled when they conflict with this addendum:

| Prior decision | 2026-08-07 status | Reason |
|---|---|---|
| D-M5 `toolless adjudicator/narrator` | **superseded** | The operator explicitly requires a bounded tool-using execution operator. |
| D-M4 `deterministic + typed LLM edges` | **amended** | Deterministic/external plans remain authoritative, but the local operator may perform bounded operational diagnosis/recovery through a tool broker. |
| D-M2 `step-4 attach only` | **amended** | Step 4 remains the MVP seam; long-term scope is a reusable execution substrate for multiple flows/projects. |
| D-M9 `Odysseus executor / Hermes notifier` | **reopened** | OpenClaw/Hermes/Odysseus must be compared against the confirmed user flows before platform roles are selected. |
| D-S5 `7-8B model selected` | **reopened** | Model size was selected for a narrower classifier/narrator role; the execution-operator role needs dedicated research and benchmarking. |
| D-S4 exact browser channel mapping | **reopened for current research** | Provider capabilities and supported automation surfaces must be re-verified before implementation. |
| D-I5 old build order | **reopened** | Build order depends on the new tool/recovery/platform design. |
| Q15 wording that local LLM "holds state, decides what runs next" | **amended** | It advances externally designed plans and bounded recovery states; project-management intelligence belongs to reasoning models. |

The following principles remain compatible and should be preserved unless later evidence disproves them:

- deterministic-first execution where possible;
- frozen/pre-authorized plans for bounded runs;
- quarantining untrusted captured content from command generation;
- append-only/resumable execution evidence;
- bodies/artifacts on disk rather than repeatedly spending scarce model context;
- human review before consequential/canonical progression during the initial autonomy phase.

---

## 10. What is NOT decided by this round

Round 1 does **not** select:

- OpenClaw vs Hermes vs Odysseus vs a hybrid role split;
- the exact browser automation mechanism for each subscription provider;
- the local model family or parameter size;
- the local inference runtime;
- the capability/tool schema implementation;
- the sandbox/isolation technology;
- the exact cross-repo state schema;
- the personal-life security zone;
- exact concurrency limits;
- exact token/context budgets;
- exact overnight scheduler implementation;
- revised implementation/build order.

Those require research and/or a subsequent operator Q&A round.

---

## 11. Implementation hold

**Do not interpret this decision lock as authorization to continue Phase 2 or build M5/M7/browser automation.**

Next architecture work is:

1. platform research/bake-off design for OpenClaw, Hermes, Odysseus, and custom/FEE components against UF-A through UF-F;
2. follow-up operator Q&A using that evidence;
3. local-model research and task-specific benchmark design;
4. only then revise the implementation plan and sequence.

This preserves the useful existing FEE code while preventing the implementation from hardening assumptions that the operator has now reopened.
