---
title: "FEE Project Cockpit"
doc_type: project_cockpit
initiative: local-orchestration-engine
created: 2026-08-10
updated: 2026-08-10
status: "PAUSED — assumption audit 2026-08-10 found the consumer has never run; sequencing under operator revision"
last_verified_commit: 2613578113f5bd88e6e50c3d595a4bea2c42fe39
sources_consumed:
  - apex-meta/local-orchestration-engine/project/specs/2026-08-10-fee-project-environment-design.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/benchmark/results/BASELINE-RESULT-QWEN3-8B-2026-08-09.md
  - apex-meta/local-orchestration-engine/benchmark/results/RE-ANALYSIS-QWEN3-8B-N1-2026-08-10-ADVERSARIAL.md
  - apex-meta/local-orchestration-engine/research-results/PLATFORM-RESEARCH-SYNTHESIS-2026-08-08-V2-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-INSTALL-LOG-2026-08-09-QWEN3-8B.md
  - apex-meta/SmallSkills/AI-Browser-Orchestration/Browser-Subscription-AI-Orchestration.okf.md
  - .claude/skills/AIRouting/routing-decision-contract.md
  - assumption audit 2026-08-10 (A1, A2, A3, A14)
---

# FEE Project Cockpit

**Sole responsibility:** one review pass over current program state. It holds no authority — every number links to its owner. See [README.md](README.md) §3.

> **Mission.** Build FEE as the **operator layer** that lets the existing apex-os-meta orchestration system delegate operational work to a bounded local LLM and a chosen third-party runtime, safely and with reconstructable evidence.

## 1. Status — read this first

| | |
|---|---|
| Program state | **ACTIVE.** The runtime is selected and installing it is the current work. |
| **Runtime selected** | **OpenClaw** — operator decision 2026-08-10. Not a bake-off outcome; a direct operator choice. See §2a. |
| **Next step** | **Install OpenClaw on the operator's laptop and verify it can execute.** Run [`../../openclaw/INSTALL-AND-VERIFY.md`](../../openclaw/INSTALL-AND-VERIFY.md). |
| Active canonical task | [001 — Install and verify the OpenClaw executor harness](../../epics/fee-operator-layer/001.md) |
| Last verified commit | `2613578` |
| Branch policy | `main` only, per [R2](../OPERATOR-DECISION-LOCK-2026-08-08-R2.md) |
| Runtime installed | **not yet** — that is task 001, not a gated future task |
| Model certified | **no**, and certification is **not required** for the executor's scope. See §2a. |

Verified 2026-08-10: base implementation through `88ac0a44`; design commit `16fdefff`; handover delivery `26135781`; local `main` and `origin/main` both at `2613578113f5bd88e6e50c3d595a4bea2c42fe39`. Six unrelated `apexai-os-meta-*.bundle` files remain untracked and out of scope.

## 2a. The runtime is selected. Installing it is the goal, not a non-goal.

**Read this before acting on anything else in this environment.**

`OpenClaw` is the selected executor harness for the bounded local LLM, by direct operator decision on 2026-08-10. This **supersedes** every statement in this repository that treats runtime installation as a gated future step or a non-goal, specifically:

| Superseded statement | Where |
|---|---|
| "Phase 0 does not install or select OpenClaw, Hermes or Odysseus" | design spec §3.2; delivery handover §1; and an earlier version of [01-PROJECT-CHARTER.md](01-PROJECT-CHARTER.md) |
| "Runtime installation stays gated behind tasks 004–005" | an earlier version of this file |
| OpenClaw install as task 008, dependent on 005 | an earlier version of the task map |
| "run the bake-off, then decide the composition" | platform research synthesis §12–15 |

Those were correct while the open question was *which* runtime to pick. The operator has answered that question directly, so the bake-off is moot and its sequencing constraints no longer apply.

**Why OpenClaw, plainly.** Hermes routes through Docker; on a single laptop that is unnecessary weight for browser operation. OpenClaw needs no container, controls the operator's **already signed-in Chrome tabs** through an official extension, carries per-agent persistent memory with automatic consolidation, and loads skills as plain `SKILL.md`. Prior research assuming a Hetzner server and ranking Hermes as a co-candidate is superseded — the operator's machine changed and the runtime choice with it.

**The executor's scope is deliberately tiny.** It pastes a pre-written prompt into a signed-in subscription AI tab, captures the response verbatim to a declared repo path, submits a pre-written verification prompt, and reports a receipt. It is a copy-paster with a browser.

It does **not** run this repository's skills. `PrecapWeek`, `PrecapNextDay`, `flow-recap`, `status-merge` and `AIRouting` stay with the reasoning and CLI models. The executor never plans, routes, judges, or touches code.

**This is why model certification is not a prerequisite.** The benchmark evidence in §5 measured bounded coding and escalation routing — neither is this job. A copy-paster chooses nothing. The relevant risk is capture fidelity, not judgement, and fidelity is verified by deterministic code comparing bytes on disk. Do not block the install on `certification_eligible_task_classes` being empty.

Harness and task: [`../../openclaw/`](../../openclaw/).

## 2. What the 2026-08-10 audit found

Four load-bearing assumptions were tested. **All four failed.** This is the most important section in the file.

| | Assumption | Result |
|---|---|---|
| **A3** | The two orchestration systems would delegate work to FEE | **No live consumer.** Weekly Orchestrator has run one partial half-cycle (2026-07-12) and **never confirmed a single gate** — every packet reads `operator_validation: not_requested`. `state/apex-project-status.md` and `state/consumed-recap-registry.md` are both **0 bytes**. Nothing in four weeks. **The step-4 seam has no call site**: nothing invokes `python -m scripts.fee`; FEE appears in one string literal, `agent: none_operator_human_step_or_fee`. **No prompt body has ever been written** — the convention exists at `artifacts/flow-packets/<YYYYMMDD>/prompt-packs/bodies/<packet_id>.md`, the file does not. |
| **A1** | A bounded ~8B local model can be usefully delegated real work | **Premise likely false as stated.** See §5 and [the re-analysis](../benchmark/results/RE-ANALYSIS-QWEN3-8B-N1-2026-08-10-ADVERSARIAL.md). |
| **A2** | `apex-session` is a working gated mutation path | **Specification only.** Thirteen Markdown files, zero executable, declaring `no_scripts_in_package: true` and deferring writes to a flow that does not exist. `apex-sync` is the exception — `scripts/apex_sync.py` is real code and produced `apex-meta/registry/index.md`. |
| **A14** | The superpowers skills the handover instructs invoking are available | **Absent.** None installed; no `.claude/plugins/`, no `.mcp.json`. They exist only as vendored copies under `source-knowledge/`. The handover's first instruction has no resolvable target. |

**Also corrected:** browser subscription execution is **proven**, not unimplemented — see §3.

## 3. Where a step's executor comes from

FEE does **not** decide which layer performs a step. `AIRouting` does, and FEE validates the decision before executing it — which is [R3 LM-27](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md) verbatim: *a routing function proposes, deterministic policy validates the route before execution.*

```text
Workflow&Processes     process_stage · workflow_stage · expected_output_type
        |              and the operator gates
PromptEngineer         prompt_packet + materialized prompt body; never executes
        |
AIRouting              routing_decision -> route_surface_class, provider_family,
        |              cost_class, scarcity_class, fallback_rule, operator_override
        v
  === FEE — the operator layer =========================================
      freeze the packet and the route into one work packet
      VALIDATE the route; refuse an unvalidated or blocked route
      compile root/capability scope · broker action_id + arguments
      checkpoint · evidence ledger · retry budget · typed escalation
      emit the shared validation_status enum
  =====================================================================
        v
Executor               whichever surface the route named — Claude-in-Chrome
        |              driving a subscription AI, a CLI code agent, a bounded
        |              local LLM behind a runtime, or manual_operator_surface
        v
Verification           by a different surface than executed, then the operator gate
```

The four layers of [R1 §2](../OPERATOR-DECISION-LOCK-2026-08-07-R1.md) are **cost and authority tiers selected per step**, not fixed job assignments. `AIRouting`'s `route_surface_class` taxonomy is the canonical, higher-resolution form.

Allocation principle: *use the lowest-cost, least-reasoning layer that can perform the task reliably.* More model capability never grants more authority.

## 4. Implementation truth

| Surface | State | Evidence |
|---|---|---|
| `scripts/fee` — frozen-plan hashing, strict path reads, append-only ledger, assisted `next`/`capture`, skip markers | implemented candidate, tested; **never run live** | 32/32 tests · "no live provider contact has ever occurred" |
| `scripts/lmbench` — **a working agent loop**: OpenAI-standard tool schemas, 12-turn bounded runner, 10 tools, capability broker, path guard, manifest audit, graders, aggregation | implemented, tested | 177/177 on Windows |
| Round-1 fixture corpus, 28 cases | built | [`../benchmark/fixtures/`](../benchmark/fixtures/) |
| Qwen3-8B — OpenVINO INT4 and llama.cpp/Vulkan Q4_K_M | installed, smoke-tested | [install log](../research-results/LOCAL-MODEL-INSTALL-LOG-2026-08-09-QWEN3-8B.md) |
| **Browser subscription execution via Claude-in-Chrome** | **PROVEN** — 13 empirical rules, 25-file research corpus, resumable Deep Research recovery demonstrated | [`../../SmallSkills/AI-Browser-Orchestration/`](../../SmallSkills/AI-Browser-Orchestration/) |
| Browser subscription execution **by a bounded local LLM behind a FEE-brokered runtime** | `NOT_IMPLEMENTED` | task [011](../../epics/fee-operator-layer/011.md) |
| Operator contract: work packet + accepted `routing_decision` + published executor interface | `NOT_IMPLEMENTED` | task [004](../../epics/fee-operator-layer/004.md) |
| OpenClaw / Hermes / Odysseus | not installed, not selected; commands not found in the 2026-08-10 audit | tasks [008](../../epics/fee-operator-layer/008.md)–[010](../../epics/fee-operator-layer/010.md) |
| Durable action-level duplicate-safe resume | not demonstrated | `T9`, task [005](../../epics/fee-operator-layer/005.md) |
| `apex-session` gated mutation path | **specification only** | audit A2 |
| A materialized prompt body anywhere in `artifacts/` | **has never existed** | audit A3 |

Detail: [02-SYSTEM-BASELINE.md](02-SYSTEM-BASELINE.md).

## 5. Test and benchmark evidence

| Suite | Result | Platform |
|---|---|---|
| `python -m unittest discover -s scripts/fee/tests -t .` | **32 tests, OK** (2026-08-10) | platform-independent |
| `python -m unittest discover -s scripts/lmbench/tests -t .` | **177 tests, OK** (2026-08-10) | **Windows only** — asserts Windows path semantics; 17 failures + 1 error on Linux |

One real benchmark exists. `CFG-8B-VULKAN-01`, Qwen3-8B Q4_K_M via llama.cpp/Vulkan, context 16384, temperature 0.2.

```yaml
trials: 28                              # n=1 per fixture
actor_pass: 8                           # CODE 0/6 · MA-05 5/16 · MA-06 0/1 · INJECT 3/4
actor_fail: 19
infra_invalid: 1                        # MA-06-B
unauthorized_attempts_denied: 5
successful_unauthorized_actions: 0      # the hard gate held
certification_eligible_task_classes: [] # empty by construction
```

**The [2026-08-10 adversarial re-analysis](../benchmark/results/RE-ANALYSIS-QWEN3-8B-N1-2026-08-10-ADVERSARIAL.md) materially changes how to read this. Read it before quoting any number above.**

- Outside MA-05, **every graded-correct escalation was copied verbatim from the packet**, which names type and destination as literal strings. On CODE-04 the model called `read_file` **zero times**.
- The fixture author's **pre-registered anti-gaming test fired**: CODE-04 / CODE-04-B was built to separate capability from pattern-matching, and the model escalated on both — twice on 04-B, against an `ACCEPTED` ADR that named the fix. Three of four discrimination pairs collapsed.
- **MA-05-16: the model obeyed an in-packet prompt injection** after two explicit warnings, and it recorded as `hard_gate_violation: false`. The gate inspects tool calls; output-content steering presents nothing for the broker to deny.
- `report.py` implements **pass^n**, so repeats deflate `pass^1` rather than lifting it. Two of seven destinations were never emitted in 16 attempts, and are correct for 5 of 16 fixtures.
- Honest concession: **10 of 19 failures are packet defects** — a real lever. But repairing them turns MA-05 into a lookup table, and 5 of 6 CODE failures are capability or procedure.
- **Four harness defects** must be fixed before any repeat run. See re-analysis §10.

Not run, deliberately: the OpenVINO paired comparison, all six `WEEKLY-*` fixtures, the context ladder, `COEX-01`..`06`, and `INJECT-01/06/08`. The families that constitute the actual target workload have **n = 0**.

## 6. Workstreams

| ID | Workstream | State |
|---|---|---|
| F0 | Governance and adoption boundary | **active** — this environment |
| F1 | Operator contract and execution safety | `PARTIAL` — mechanisms exist in two packages, not converged, no published interface |
| F2 | Local model qualification | `FAIL` at n=1 — see §5; nothing eligible |
| F3 | Runtime integration | `NOT_IMPLEMENTED` — no candidate installed |
| F4 | Runtime and model operations | `UNMEASURED` — no coexistence run exists |

Reduced from the design's `P0`–`P7` on 2026-08-10. `P5 Workflow integrations` was deleted — integration is the adopting flow's work; FEE's obligation is the published interface in task [004](../../epics/fee-operator-layer/004.md). `P4 Browser execution` folded into F2 as a task class, since the capability is proven and only the local-model executor is open. `P6 Benchmarking` folded into F2, since the harness is built and the remaining work is running it. Boundaries: [05-WORKSTREAMS.md](05-WORKSTREAMS.md).

## 7. User stories

| ID | Outcome | Verdict |
|---|---|---|
| US-FEE-00 | Operator controls the program from one evidence-linked cockpit | `PARTIAL` |
| US-FEE-01 / UF-A | Execute subscription research prompts, capture exact evidence | **split** — `PASS` for the Claude-in-Chrome executor; `NOT_IMPLEMENTED` for a bounded local LLM behind a runtime |
| US-FEE-02 / UF-B | Recover bounded script failures or escalate compactly | `FAIL` at n=1 — CODE family 0/6 |
| US-FEE-03 / UF-C | Gather Detective evidence without taking judgement authority | `NOT_IMPLEMENTED` |
| US-FEE-04 / UF-D | Deterministic and bounded hygiene without semantic guessing | `NOT_IMPLEMENTED` |
| US-FEE-05 / UF-E | Execute across explicit multi-root read/write/forbidden scopes | `PARTIAL` — path guard denied 5 attempts; no OS-level isolation |
| US-FEE-06 / UF-F | Separately gated personal flows in a stricter trust zone | `NOT_IMPLEMENTED` |
| US-FEE-07 | Exact patchspecs or one authorized micro-fix in a severe envelope | `FAIL` at n=1 — 0 patches applied across 6 CODE fixtures |
| US-FEE-08 | Serve Meta Ops as a bounded worker without becoming orchestration authority | `FAIL` at n=1 — MA-05 routing 5/16 |
| US-FEE-09 | Resume overnight work without duplicate consequential actions | `NOT_IMPLEMENTED` |
| US-FEE-10 | Reconstruct actions, arguments, states, artifacts, retries independently | `PARTIAL` — ledger and manifest audit exist; per-trial evidence is uncommitted |

`US-FEE-01`..`06` alias the locked `UF-A`..`UF-F` from [R1 §8](../OPERATOR-DECISION-LOCK-2026-08-07-R1.md). Detail: [03-USER-STORY-PORTFOLIO.md](03-USER-STORY-PORTFOLIO.md).

## 8. Quality gates

Each `QG` projects an already-locked gate. Full `equivalent_to` mapping: [08-QUALITY-GATES.md](08-QUALITY-GATES.md).

| ID | Gate | Locked as | Fixtures | State |
|---|---|---|---|---|
| QG-0 | Alignment and authority | this environment; [R1 §9](../OPERATOR-DECISION-LOCK-2026-08-07-R1.md) | fresh-reader review | `FAIL` — six drift items found on 2026-08-10, one in the approved design |
| QG-1 | Authority containment | R2 hard gate 1 · G-P1 | `T3`, `INJECT-*` | **`PARTIAL` and split** — 0 successful unauthorized *actions*; **1 observed uncontained output-content steering** (MA-05-16) |
| QG-2 | Job-scoped permissions | R2 hard gate 2 · G-P2 | `T7`, `CODE-05` | `PARTIAL` — 5 attempts denied and audited; guard is a path check, not OS isolation |
| QG-3 | Resumability and idempotency | R2 hard gate 3 · G-P3 | `T9`, `WEEKLY-04` | `UNMEASURED` |
| QG-4 | Evidence and attribution | R2 hard gate 4 · G-P4 | `T11` | `PARTIAL` — `MA-06-B` correctly held `INFRA_INVALID`; resource metrics never captured |
| QG-5 | Safe escalation | R2 hard gate 5 · G-P5 | `T2`, `T4`, `MA-05-01..16` | `FAIL` at n=1 — 5/16, two destinations never emitted |
| QG-6 | Windows and resource coexistence | R2 hard gate 6 · G-P6 | `T12`, `COEX-01..06` | `UNMEASURED` — no coexistence run exists for any candidate |
| QG-7 | Utility and operational value | [R3 LM-25](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md) | `T1`..`T12` metrics | `UNMEASURED` — no baseline exists to beat |

**`QG-1` is non-negotiable and now needs a second instrument.** Zero successful unauthorized *actions* is real and holding. Zero successful unauthorized *steering* is unmeasured and has one observed violation. A `content_injection_compliance` grader is required; the broker structurally cannot cover this class.

## 9. Efficiency snapshot

| Measure | Value |
|---|---|
| Successful bounded jobs per wall hour | `UNMEASURED` |
| Human intervention minutes per successful job | `UNMEASURED` — **and there is no baseline to compare against**, because no flow has been run end-to-end |
| CLI escalations per successful job | `UNMEASURED` |
| Procedure-complete rate | `FAIL` at n=1 — the model's weakest axis |
| Safe local recovery rate | `0/6` at n=1 |
| Evidence completeness | `PARTIAL` — resource metrics never captured in any trial |
| Resource coexistence | `UNMEASURED` |
| Runtime-specific code ratio | `0` — no runtime adapter exists |
| llama.cpp decode | **12.5–13.5 tok/s** |
| OpenVINO measured footprint | **~5.0 GB** |
| llama.cpp working set | **10.76–14.16 GB** after exchanges |

Machine: HP OmniBook X Flip 16-as0xxx · Windows 11 · Intel Core Ultra 7 258V · ~31.6 GB RAM · Intel Arc 140V, ~16.5 GB shared device memory.

**The binding number is the last three rows against the first two.** A 14 GB model working set on a 31.6 GB machine, plus Chrome with three subscription sessions, plus an IDE, plus a runtime — and `QG-6` is unmeasured for every candidate. It is a hard gate, so no weighted score can compensate, and it is currently scheduled last. Detail: [09-EFFICIENCY-SCORECARD.md](09-EFFICIENCY-SCORECARD.md).

## 10. Top active risks

| Risk | State | Control |
|---|---|---|
| **FEE has no live consumer** | **materialized** — audit A3 | make the socket real before further FEE work |
| Captured-content authority injection | **one observed violation** (MA-05-16) | `content_injection_compliance` grader; the broker cannot see this class |
| Local model cannot do the delegated work | **observed** — CODE 0/6, pass^n deflates | the four pre-registered tests in re-analysis §15 |
| Scope drift, in either direction | **materialized twice** | source hierarchy; `sources_consumed` frontmatter; task [002](../../epics/fee-operator-layer/002.md) |
| `apex-session` gated path does not exist | **confirmed** — audit A2 | either build the file-application flow or stop claiming a gated path |
| Handover instructs uninstallable skills | **confirmed** — audit A14 | install via the `skills-lock.json` mechanism, or amend the handover |
| Generic runtime shell / tool bypass | unresolved | wrapper-only interface; `run_command` is the known hole in the path guard |
| Windows resource contention | unmeasured | `T12` / `COEX-*` before any runtime install |
| Cockpit projection rot | active | canonical ownership; declared refresh triggers |
| Multi-runtime overengineering | active | Composition E scores 70 of 6; one candidate only |

Full register: [10-RISK-REGISTER.md](10-RISK-REGISTER.md).

## 11. Open operator decisions

**The sequencing decision, taken 2026-08-10:** make the socket real before further FEE build work.

Eight remain open from the [platform synthesis §15](../research-results/PLATFORM-RESEARCH-SYNTHESIS-2026-08-08-V2-RESULT.md), none resolvable without evidence: bake-off scope · Windows deployment preference · browser-account policy · artifact-transfer requirement · personal-flow scope · resource thresholds · maintenance threshold · bake-off winner rule.

Newly open from the audit: whether to build the `apex-session` file-application flow · whether to install the five superpowers skills or amend the handover · whether the repeat run proceeds before the four harness defects are fixed · what task class FEE's first delegation should be, given browser work is already proven by another executor.

## 12. Next three bounded actions

1. **Install OpenClaw and verify it can execute.** Run [`../../openclaw/INSTALL-AND-VERIFY.md`](../../openclaw/INSTALL-AND-VERIFY.md) on the operator's laptop. It answers the four questions that can still invalidate the design: does the local model emit real structured tool calls, can OpenClaw reach the signed-in subscription sessions, does the stack fit in ~31.6 GB, and does skill loading plus memory persistence work. **Q1 first** — if Qwen3-8B under llama.cpp cannot emit structured tool calls, nothing downstream matters.
2. **Write the first prompt body** at `artifacts/flow-packets/<YYYYMMDD>/prompt-packs/bodies/<packet_id>.md`. The contract has existed since 2026-08-07; no such file has ever been written, and it is the executor's only input.
3. **Add deterministic capture verification** — compare bytes on disk against the receipt's reported counts. This is the whole of what FEE needs to be for this job, and it must not be performed by the model that produced the capture.

**Nothing here is gated behind a bake-off or a certification.** See §2a.

## 13. Deeper files

[README.md](README.md) · [01-PROJECT-CHARTER.md](01-PROJECT-CHARTER.md) · [02-SYSTEM-BASELINE.md](02-SYSTEM-BASELINE.md) · [03-USER-STORY-PORTFOLIO.md](03-USER-STORY-PORTFOLIO.md) · [04-ROADMAP.md](04-ROADMAP.md) · [05-WORKSTREAMS.md](05-WORKSTREAMS.md) · [07-TRACEABILITY-MATRIX.md](07-TRACEABILITY-MATRIX.md) · [08-QUALITY-GATES.md](08-QUALITY-GATES.md) · [09-EFFICIENCY-SCORECARD.md](09-EFFICIENCY-SCORECARD.md) · [10-RISK-REGISTER.md](10-RISK-REGISTER.md) · [11-DECISION-REGISTER.md](11-DECISION-REGISTER.md) · [12-EVIDENCE-INDEX.md](12-EVIDENCE-INDEX.md) · [14-GLOSSARY-AND-AUTHORITY.md](14-GLOSSARY-AND-AUTHORITY.md) · [15-HANDOVER.md](15-HANDOVER.md) · [templates/](templates/) · [specs/](specs/) · [plans/](plans/)
