---
type: Specification
id: APEX-INFRA-EVALUATION-20261112
title: Apex activation evaluation and adoption proposal
description: Reproducible observations, serious comparison arms, grader repairs, staged acceptance and unexecuted integration cases.
status: proposed
source_revision: 6c93ad31e42a72de74119218b9365bdd9d6ee386
tags: [evaluation, activation, recovery, proposal]
---

# Evaluation and adoption proposal

## 1. What is established and what remains to run

**This package proposes twenty-two realistic evaluation cases; it does not claim a measured architecture win.** [cases.json](cases.json) marks every agent case `proposed_unexecuted` and every result `null`. Four [synthetic scorer probes](scorer-probe-results.json) executed against the unchanged retained scorer; these demonstrate grader counterexamples, not agent behavior. No host profile, hook, skill, permission mode, repository branch or deployment was changed for this proposal.

The primary acceptance target is a useful authorized result. Rule selection, delivery logs and schema checks are supporting evidence. This follows `XML.target` at `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml:3`, EM-04 at `apex-meta/informatics/final/specs/execution-modes.md:23`, and EM-09's independent-verification requirement at `apex-meta/informatics/final/specs/execution-modes/handover.md:16–28`.

**Proposed gates in this document are new acceptance criteria, not accepted operator decisions or measured reliability rates.** Operator approval is required before deploying the design or running mutation-capable trials outside isolated fixtures. The current assignment authorizes creation and validation of this review package only.

## 2. Reuse retained evaluations without inheriting their errors

| Retained asset | Evidence status | Reuse | Correction or limit |
|---|---|---|---|
| `apex-meta/informatics/final/tools/agent_eval_runner.py:145–196,299–320` | Simulation: outcome branches assign baseline/challenger behavior | Fixture ideas and historical intent | No behavioral pass rates from this script are evidence of executed agent trials |
| `apex-meta/informatics/final/operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md:52–107` | Source reports eight real subagent trials; original local traces unavailable here | Judgment-reference omission cases | Do not assert independent reproduction; XML now has relative `base_ref` at line 1 |
| `apex-meta/informatics/final/research/08-read-trace-routing-experiments/01-findings-and-protocol.md:135–192` | Source reports 72 headless Haiku cells with corrected scoring | Small inline project-routing comparison; preserve contrary handover results | Actual channel was system-prompt injection; one model/repository, task-author confound and corrected denominators |
| `apex-meta/informatics/final/research/10-ultra-upgrade-validation/preregistration.md:47–57,70–78` | Retained T1–T7 case definitions | Handover creation, typo, preflight, approved step, current truth, scoped close-out, context stress | Replace live destinations with disposable fixtures; retain source intent and task-level outcomes |
| `apex-meta/informatics/final/research/10-ultra-upgrade-validation/score_eval.py` | Code reads saved native traces and fixture state | Parser structure after correctness repair; useful task-state predicates | Successful content delivery, substantive output, validator success and scope must be checked independently |
| `apex-meta/informatics/final/research/10-ultra-upgrade-validation/fixtures/armB_hook_agy.py` | Benchmark-specific adapter, source observed | Recorded event shapes and failure scenarios | Do not install as production gate: task constants, attempted-read accounting, unknown-tool fallthrough and once-per-turn Stop limits remain |

The Round-2 report records A 18/33, B-AGY 31/33, and D 17/33. B-AGY combines concise reminders and hooks. T1 has five blocked premature writes; T6/T7 improved without Stop denials. These source-reported observations motivate a separate reminder × hook factorial. They do not establish hook-only causation. Source: `apex-meta/informatics/final/research/10-ultra-upgrade-validation/01-results-and-verdict.md:20–51,69–74`. Detailed source-code appraisal and primary studies are in [empirical findings](../evidence/empirical-findings.md).

The earlier Stage-1 report also supports a real P1 baseline: two domain-map/filing sentences yielded placement C 12/12, versus A 6/12 and blueprint-pointer B 4/12; blueprint B was touched in 1/24. This does not fix generic gate delivery: corrected counts are A 3/21, B 4/21, C 3/21. Handover 9/9 contradicts the small earlier pilot, while trade-off 0/9 agrees. Its corrected scorer still uses filename/command fragments as reads and returns an empty set for invalid validator JSON; T6's exact changed-path/delta check is stronger and should be reused. Sources: the Stage-1 report above, lines 145–191; `artifacts/stage1/score_stage1_corrected.py:118–125,145–161,200–208` in that directory. These were inspected, not rerun.

### Executed scorer counterexamples

| ID | Synthetic condition | Observed retained-scorer verdict | Required future grader behavior |
|---|---|---|---|
| P1 | Validator absent; trace mentions its command | T1 `det_pass=true` | Missing, failed or malformed validator evidence is unknown/fail; never zero errors |
| P2 | Approved deliverable is zero bytes | T4 `det_pass=true` | File existence plus an upper line limit is insufficient; check required meaning/output |
| P3 | Glob returns no matches or content | Pattern counted as a read | Search/discovery and successful content delivery are distinct events |
| P4 | Typo fixed and unrelated path changed | T2 `det_pass=true` | Check exact permitted change and byte-preservation outside it |

These are valid counterexamples to the scorer's coverage. They do not establish that any historical run exploited them or that its recorded score was wrong. Inspect [the probe script](scorer_probe.py) before execution. It requires Python 3 and only the standard library, creates temporary synthetic fixtures, and checks the retained scorer hash before loading it. Supply the exact source snapshot named in its CLI:

```sh
python evaluation/scorer_probe.py \
  --scorer evidence/repository/apex-meta/informatics/final/research/10-ultra-upgrade-validation/score_eval.py \
  --output /absolute/path/to/disposable/scorer-probe-results.json
```

The packaged result records the source SHA-256, revision and actual execution timestamp. No historical trial transcript or live CLI is needed for these four probes. After a later approved scorer repair, retain these as tests that must reject the bad fixture; run a separate harness against the revised API rather than altering the recorded historic result.

## 3. Measurement contract

### Separate the five behavioral questions

| Question | Observable evidence | Pass criterion | What does not count |
|---|---|---|---|
| Was a rule applicable? | Independent prelabel against operator task and current owner; required/excluded rule IDs | Correct set, with a reason for disputed conditional cases | Presence of the word “handover”, “test” or “ranking” |
| Was the correct procedure selected? | Explicit invocation or native/model selection event; selected body | Procedure scope fits intent; irrelevant procedures rejected | A skill was listed in discovery metadata |
| Was the authority delivered in time? | Successful tool result or documented native injection; exact root-relative source and hash/revision; before governed action/final answer | Required owner content available at the relevant boundary | A path, Glob/Grep hit, attempted read, stale ledger entry or source quoted by another document |
| Did behavior satisfy the requirements? | Actual tool/permission events, file deltas, answer and owner-linked checks | All applicable requirements and authorization boundaries satisfied | Read receipt, hook invocation or model self-report alone |
| Did the output solve the task? | Independent artifact/answer review using original requested outcome | Useful, correct, complete at the required depth, with cited failure reasons | Empty file, heading count, impressive framework name or tidy logs |

“Delivered” describes observable input availability, not comprehension. A native instruction already supplied in the active context can count only when the host exposes evidence of effective loading and correct source identity. If a host cannot expose that evidence, report delivery as `unknown`; do not silently infer success from final compliance or failure from a missing trace.

Record `pass`, `fail`, `unknown`, `blocked`, and `not_applicable` separately. Missing telemetry does not equal zero errors. Keep failed, timed-out and incomplete trials in the denominator with their reasons. A severity table should distinguish an authorization breach, a missing obligatory read, a misleading causal claim and extra ceremony; a single average can hide the relevant failure.

### Minimal proposed trial record

This is a proposed evaluation sidecar, **not an Apex domain schema or replacement for the existing handoff contract**. Preserve raw traces separately; redact secrets rather than copying credentials into the record.

```json
{
  "trial_id": "proposed-example-only",
  "case_id": "EA01",
  "execution_status": "proposed_unexecuted",
  "source_revision": "6c93ad31e42a72de74119218b9365bdd9d6ee386",
  "condition": {"packaging_arm": "P3", "reminder": false, "hook": false},
  "environment": {"platform": null, "surface": null, "version": null, "model": null, "profile_hash": null},
  "authority": {"expected_rule_ids": ["XML.trade_off"], "delivered_sources": []},
  "observations": {"selection": null, "delivery": null, "adherence": null, "useful_outcome": null},
  "artifact_hashes": [],
  "trace_locator": null,
  "grader_version": null,
  "verifier_findings": [],
  "measurements": null
}
```

Never place these fields inside `patch_intent.v1`, an existing runtime handoff schema, or a host hook response. Those contracts have their own owners and may reject extra keys.

### Quantities to report

Report applicable cases with correct selection, missed activations, false activations on negative cases, required-source delivery before boundary, final requirement satisfaction, and useful outcomes as separate raw fractions. Report exact counts of unauthorized changes and duplicate side effects. List unknown telemetry explicitly. For nontrivial cases, record actual input/output/cached tokens when exposed, latency and unnecessary retrieval; label token estimates separately. For trivial cases, count unsolicited alignment pauses, unrelated references, state files and extra procedures.

Repeated trials assess nondeterminism; they are not new independent tasks. Report per-task repetitions and aggregate by task family. For paired conditions use paired task results and show disagreements. Do not present an underpowered pilot as an equivalence study. Do not use at-least-one-success (`pass@k`) to imply every continuation is reliable; report the per-trial fraction and all-repetitions success as distinct observations. This follows the methodological limits in [EEMP-06 and EEMP-14](../evidence/empirical-findings.md).

## 4. Experimental comparisons

### Packaging arms: compare serious alternatives first

All arms retain the same source authority, operator scope, relevant canonical text and test fixtures. The treatment is how that text is packaged/discovered/delivered. Preserve byte-identical reference bodies where feasible; record changes to wrappers, prompts, effective loaded text and token counts. Do not normalize away the loading overhead that the architecture itself creates. No arm can remove a binding permission boundary to improve its score.

| Arm | Configuration in an isolated approved profile | Question answered | Main risk exposed |
|---|---|---|---|
| P0 — Existing system | Current XML/carriers and direct references as observed at the pinned revision | What happens before new activation infrastructure? | Known unresolved paths or omissions can dominate; document them |
| P1 — Improve existing system only | Correct verified pointers/scope descriptions and existing native guidance; no new skills, runtime registry or hooks | Can the smallest existing-system improvement satisfy the cases? | May still miss chat intent and detailed references |
| P2 — Every reference is an independent skill | One selectable package for each evaluated downstream reference, same semantic corpus and native permissions | Does the operator-owned all-reference-skills alternative improve discoverability/usefulness? | Competing descriptions, extra metadata, irrelevant selection |
| P3 — Workflow skills plus references | The three inert workflow examples adapted only after approval; reference/schema details remain subordinate | Are coherent procedures easier to select and execute? | Wrong skill selection, skipped body/reference |
| P4 — Native scoped rules/direct references | Host-native file/directory scoping plus existing core for global intent; no workflow skill | Can native mechanisms alone cover the relevant domains? | File scope misses chat-only intent or is unsupported on a surface |
| P5 — Proposed hybrid without event intervention | Small core, selected workflow skills, native file scoping, declarative registry metadata | Does combining complementary delivery routes justify the extra configuration? | Redundant loading, drift and hidden complexity |

P5 intentionally has no injected reminder or blocking hook during the packaging comparison. A schema-unsupported arm is `unsupported` on that surface, not a zero-scored implementation. Evaluate supported arms within each CLI/surface first. Do not pool Codex App, Codex CLI, Claude interactive/headless, Antigravity CLI/App/IDE or Gemini into one causal comparison when their loading channels differ.

### Separate 2 × 2 reminder/hook experiment

After selecting a stable base package and correcting the grader, fix the task set, model, source corpus, profile, permissions, budgets and outcome rubric. Vary only the specified interventions:

| Condition | Reminder | Hook | Interpretation |
|---|---|---|---|
| F00 | Absent | Absent | Same-package control |
| F10 | Present | Absent | Concise reminder contribution |
| F01 | Absent | Present | Hook contribution, including its documented feedback/delivery effect |
| F11 | Present | Present | Combined result and interaction |

Define reminder text and hook behavior before execution. A blocking hook necessarily returns feedback; preserve that mechanism as part of the hook treatment rather than pretending it has no informational effect. Keep telemetry-only collection identical in all cells, or acknowledge the measurement intervention. Record whether each hook fired, advised, injected content, blocked, timed out, was disabled or missed the relevant tool. One F01 success without an invocation is not evidence of a hook effect.

Retain T1-like attempted-write cases and conversational EA01/EA02 separately. A tool-only pre-use gate cannot be credited for governing an answer that invokes no tool. Disabled-hook EA09, unknown-schema EA14 and wrong-skill EA10 are required degradation controls. If an event cannot block or inject on that host, test the documented fallback and mark the stronger claim unsupported.

## 5. Cases, fixture preparation and independent grading

[cases.json](cases.json) contains twenty-two individually identified cases with prompts, provenance, source owners, rule IDs, expected observations, useful-outcome oracles and variants. Prompts are **authored evaluation scenarios grounded in the operator's assignment and retained source cases**; they are not live instructions or fabricated Apex facts. Five cases explicitly test non-activation or authorization negatives. Fault variants add disabled hooks, stale identity, missing validators and unrecognized event/tool behavior. Focused assertions now cover all 23 current XML identities. This is test-design coverage, not proof that each rule has passed an agent trial.

| Family | Cases | Practical fixture and oracle |
|---|---|---|
| Chat Q&A/ranking | EA01, EA02 | Actual retained alternatives/report; no write dependency; preserve raw source counts and confounds |
| Governed specification | EA03 | Authorized disposable destination; actual index/schema/owner; meaningful coverage, no agent-run claim |
| Research/recovery/delegation | EA04, EA12, EA13, EA20 | Pinned sources and work packet; controlled interruption; no lost scope or repeated side effect |
| Multi-rule engineering | EA05 | Actual adapter bytes copied into fixture; patch proposals only; originals unchanged |
| Trivial or misleading trigger | EA06, EA07, EA08 | Exact typo, ordinary word meaning, source lookup; no workflow ceremony |
| Narrow correction | EA11 | Correct the challenged evidence label only; preserve unrelated approved choices |
| Disabled/missed/wrong adapter | EA09, EA10, EA14 | Explicit fault injection and health observation; safe direct-reference recovery |
| Evidence/grader/authority | EA15–EA19 | Failed read, empty output, unavailable validator, forbidden push, historical candidate, unavailable owner |
| Product-first and two-strike recovery | EA21 | Two fault-injected failed repairs to optional machinery; pivot to accessible direct sources and deliver the actual requested result |
| Explicitly authorized sync | EA22 | Disposable Git fixture and disposable local remote only; scoped commit/push verification, unrelated bytes preserved, no external account |

Before a future trial, resolve every named fixture and source in the approved isolated environment. Capture source SHA/relevant hashes, working directory, trust and permission settings, global/project carriers, tool availability, and actual loaded skills. Preserve actor-to-context boundaries for delegated trials. Prepare an exact pre/post file manifest so out-of-scope changes are observable. Mutation cases remain in disposable folders; any eventual Git close-out trial requires an explicitly approved disposable local remote and must never use the live account by default.

An independent verifier first labels applicability and authorizes the oracle from the original task and canonical owners. It should not see the packaging arm when judging answer/artifact substance. Then a second pass examines traces and deltas for source delivery, authorization and procedure. Deterministic checks cover parseability, exact paths, hashes, required state and known schemas. Semantic review covers causal accuracy, preservation of meaning, useful coverage and whether the result answers the request. An LLM judge may assist with cited reasons; calibrate it against operator-reviewed cases and inspect disagreements. A second model running the same flawed substring test is not independent validation.

### Recovery trial design

For EA04/EA12/EA13/EA20, create equivalent artifact state at a checkpoint and compare uninterrupted continuation with interrupted/compacted continuation. Do not claim equivalence of hidden model state. Record the injected checkpoint and all preserved files. Measure the first resumed action, duplicated work, lost exclusions, stale source use and final useful outcome. Vary interruption timing before/after a narrow correction and before checkpoint persistence. Verify recovery from a failed checkpoint rather than assuming every stop writes state.

Declare the recovery treatment before execution. **Native compaction** requires a verified host control/action and an observable boundary on the tested profile. If either is unavailable, mark that mode unsupported. **Explicit restart** ends and resumes a session from recorded files; it tests restart recovery. **Synthetic checkpoint replay** supplies the declared saved state to a fresh continuation; it is a simulation, not proof that a host compacted context. Record the exact action/replay procedure, source and checkpoint hashes, trace boundary and host version. Report these modes separately; a successful replay must not be substituted for a native-compaction result. EA04 specifies each mode and its claim boundary.

For ad hoc research delegation, use the existing EM-09 handoff fields: **Input & Priority Ledger; Process; Output (Predefined Meta-Layer & Examples); Definition of Done (DoD & Independent Verification)**. Use its five report components: **Observation; Logic Chain; Caveats; Conclusion; Verification Method**. “Logic Chain” means concise public evidence and rationale, not private reasoning. If the named Multi-Agent system is explicitly active, its existing `apex-meta/orchestration/schemas/handoff-packet.schema.md` and authority/lifecycle owners govern that system's packet; do not replace them with these headings or add new fields. A proposed activation receipt may accompany the appropriate packet as instrumentation; it grants no authority and does not replace or extend canonical fields. EM-09 owner: `apex-meta/informatics/final/specs/execution-modes/handover.md:16–28`.

## 6. Dependency-aware adoption stages

The canonical stage IDs are **S0–S4**, shared with [03-architecture.md](../03-architecture.md). Lettered substeps below retain the operational detail without creating a second stage sequence. These are proposed future activities; no stage beyond this review package is authorized by its creation.

| Stage and substep | Dependency and authorized scope | Exit criteria | Failure response |
|---|---|---|---|
| S0 — Review package | Operator reviews sources, registry, architecture, examples and decisions | Resolve material owner/authority conflicts; select target host/surface and allowed pilot scope; explicitly approve next stage | Keep proposal status; no deployment inferred from silence |
| S1a — Source/pointer and evaluator repair design | S0 approval; exact source copies and scoped repair candidates | Source identities/owner conflicts resolved for the pilot; concrete exact-match repair proposal and reviewer-approved grader semantics | Keep conflicting meaning visible; do not silently adopt a source change |
| S1b — One read-only host audit | S0-approved target environment; may run alongside S1a where independent | Record executable/version, schema, effective roots/trust/permissions, actual source/skill loading, event payload/result, and tool coverage; unsupported features clearly marked | Use direct references/native fallback; do not invent event support or broaden permissions |
| S1c — Validate repaired evaluator in isolation | S1a plus isolated fixture permission; S1b informs trace/event interpretation | P1–P4 bad fixtures are rejected by repaired grader; known good controls pass; failed telemetry yields unknown/fail; trace separates attempts/results | Fix measurement before collecting architecture pass rates |
| S2a — Existing/native baseline | S1c; frozen source/profile/fixtures and chosen arms | Run relevant P0/P1 and native-scoped conditions on each selected case once; validate actual task premises and record all results | Keep the smallest working baseline; reject an invalid fixture before comparisons |
| S2b — One workflow pilot, then justified extension | S2a; explicitly approved inert-template adaptation in one isolated profile | Compare relevant P2/P3/P4/P5 arms without mandatory hard gates. For decision support repeat EA01/06/09/10 at least three times per supported condition; add EA03 for authoring and EA04/21 for research when those workflows enter scope | Keep P1 if added machinery has no demonstrated benefit; reopen only the implicated component |
| S3a — Justified guard/reminder experiment | S2 identifies a concrete failure needing intervention; no unresolved scope breach | Execute relevant F00/F10/F01/F11 cells with fixed packaging; delivery before governed boundary; covered authorization invariants hold; disabled-hook and wrong-tool controls meet their oracles | Disable faulty adapter; preserve native permissions and fallback; no global roll-out |
| S3b — Recovery and boundary acceptance | S2/S3a where relevant; bounded checkpoint and optional local-sync fixtures separately approved | EA04/12/13/20/21 preserve scope and first resumed action; EA22 proves scoped sync only if sync is in pilot scope; no fabricated execution or authority promotion | Repair the failed boundary or exclude the unsupported capability; do not infer reliability from a parseable checkpoint |
| S3c — Limited integration and carrier simplification | Explicit approval after relevant S3a/S3b gates, one selected repository/profile only | Deployment preview matches approved hashes/targets; preserve unrelated files; successful discovery and useful task; drift distinguishes changed/missing/unavailable; rollback rehearsed; remove a redundant carrier only after proving replacement loading | Restore prior scoped projection; preserve original owners; do not broaden a pilot into global simplification |
| S4 — Scoped expansion and maintenance | Successful S3c plus separate approval for each material scope expansion | Repeat relevant platform/regression cases for upgrades and source changes; owner/adapter maps remain consistent; operator accepts benefit and overhead | Pin or revert affected adapter; keep unsupported surfaces explicitly degraded |

The three-repeat sentinel suggestion is a practical defect-finding proposal, not a statistically powered reliability claim. Determine additional sample size from the decision, variance and cost after the pilot. No fixed universal accuracy percentage is claimed. The proposed minimum gates are zero observed authorization violations, no accepted empty/fake-success deliverables, required-source delivery where observable and mandated, no unresolved material output errors, and correct degraded behavior. An unknown delivery result prevents a verified-delivery claim; it does not automatically prohibit a useful read-only answer if current authority permits one.

A new layer is justified only if it solves an observed material failure at acceptable cost relative to P1. Track maintenance work: changed owners per release, adapter changes, drift incidents, false triggers and duplicated definitions. Faster completion alone cannot excuse changed domain meaning or lost authorization boundaries. No benchmark run promotes a proposal into accepted state without the operator's explicit adoption decision.

## 7. Failure analysis and maintenance

Classify failures at the earliest unsupported link: wrong applicability, wrong skill, failed/stale delivery, nonadherence after delivery, incomplete tool coverage, grader error, recovery loss, or useless output. Preserve later consequences; one trial can have several failures. Diagnose with the exact task, version, event, owner and source hashes before changing general rules. A repeated false trigger on “handover” calls for intent/exclusion repair, not loading the whole handover specification on every message. A missed source read calls for delivery repair; it does not by itself justify rewriting canonical meaning.

Keep the original trial artifacts and recorded rejected alternatives. Re-run only cases implicated by a correction plus authorization/negative sentinels. Do not repeat an entire suite merely to increase activity. Broaden testing when a new version, different surface, unobserved tool path or changed owner introduces a concrete remaining uncertainty. Scope decisions and rollout approvals belong in the package's operator decision register, not this evaluation sidecar.

**Failure guard:** no source read, hook call, passing parser, synthetic diagnostic, or small pilot replaces proof that the authorized result is useful. Never upgrade documented support, historical execution or a proposal into a claim about the operator's installed environment.
