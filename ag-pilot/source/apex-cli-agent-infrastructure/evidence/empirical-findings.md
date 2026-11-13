---
type: Reference
id: APEX-INFRA-EMPIRICAL-20261112
title: Empirical support, contrary evidence, and evaluation implications
description: Primary research appraisal and retained Apex evaluator audit supporting a proposed activation design.
status: proposal
research_date: 2026-11-12
---

# Empirical findings and their design consequences

## 1. Conclusion and evidence standard

**Use a small persistent contract, coherent workflow skills with explicit references, and surface-specific deterministic checks only where a concrete failure warrants them.** This is a proposed design inference, not a measured Apex architecture result. The evidence supports testing this combination; it does not establish one universal best packaging strategy.

The most important measurement distinction is:

1. A rule is applicable to the task.
2. The correct capability or reference is selected.
3. The authoritative content is successfully delivered before the governed action or answer.
4. The agent follows the relevant requirements.
5. The delivered result solves the operator's actual problem.

Each step needs separate evidence. A matching filename, a hook invocation, a source read, a schema pass, and a useful outcome are different observations. A missing source read is a procedural defect when the live rule requires it. A source read never proves comprehension or final adherence. This directly follows the live contract's target and pointer obligations at `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml:3,74` and the scorer counterexamples in §4.

**Evidence classes used here:** original empirical study; vendor engineering guidance; open specification; repository-observed implementation; retained source-reported execution; executed synthetic scorer probe; proposed unexecuted evaluation. No local Codex, Claude Code, Antigravity, or Gemini agent trial was run for this research module.

## 2. Primary evidence appraisal

### EEMP-01 — Instruction density is a risk, not a universal numerical budget

[IFScale, v1](https://arxiv.org/html/2507.11538v1), §§3–6, evaluates 20 models using 10–500 keyword-inclusion instructions in a business-report task, with five runs. Adherence degrades as density grows; the best reported result at 500 instructions is 68%. Its narrow keyword task does not establish a maximum safe number of Apex rules, nor does it test lifecycle hooks. **Implication:** measure active instruction burden and omission by task; avoid loading every downstream definition. Preserve required semantics instead of treating a token ceiling as the product objective.

### EEMP-02 — Curated skills help some tasks and hurt others

[SkillsBench, v1](https://arxiv.org/html/2602.12670v1), §§3–5 and Appendix C, reports seven model–harness configurations and 7,308 trajectories, with 84 evaluated tasks from an 86-task collection. Curated skills yield a 16.2-point average pass-rate improvement; 16/84 task deltas are negative. Self-generated skills show no average benefit. The authors identify context-length confounding and limited terminal/container generalization. Their observed advantage for focused bundles is not proof that every workflow needs exactly two or three skills. **Implication:** use curated reusable procedures, test irrelevant-skill controls, and retain a no-new-framework baseline. Freeze the paper version rather than mixing its denominators with the later 87-task website.

### EEMP-03 — Realistic skill selection is materially harder than forced loading

[How Well Do Agentic Skills Work in the Wild, v1](https://arxiv.org/html/2604.04323v1), §§3–4 and Appendix B, separates forced load, autonomous selection, retrieval from 34,000 skills, and adaptation without curated skills. Three model–harness combinations use repeated containerized trials; the hardest settings approach the no-skill baseline. Query-specific refinement can help when initial skills are relevant. **Implication:** assess discovery and successful execution separately. Do not infer that a portable `SKILL.md` will activate correctly. For Apex's bounded corpus, explicit trigger/exclusion descriptions and opening the selected body are a simpler starting mechanism than an external retrieval service.

### EEMP-04 — Metadata is a candidate filter, not sufficient evidence of fit

[SkillRouter, v1](https://arxiv.org/html/2603.22455v1), §§2–5 and Limitations, studies roughly 80,000 skills with 75 expert-verified queries. Removing full bodies worsens routing substantially; the proposed pipeline reports 74% Hit@1. The small, single-benchmark query set and majority multi-skill structure constrain generalization; retrieval accuracy is not end-task completion. **Implication:** names/descriptions cheaply identify candidates, then inspect selected instructions and scope. This does not justify installing a learned router for a small owned registry, or putting every skill body in the persistent context.

### EEMP-05 — More repository guidance can increase activity without useful gains

[Evaluating AGENTS.md, v1](https://arxiv.org/html/2602.11988v1), §§3–5, combines SWE-bench Lite with 138 tasks in 12 Python repositories. The paper reports marginal gains for human context and small losses for generated context, alongside more than 20% extra inference cost. Its task-resolution metric omits properties such as security and code efficiency. **Implication:** put non-obvious constraints, ownership, and routing in persistent guidance; avoid a generated repository encyclopedia. Required operator boundaries remain binding even when a benchmark's correctness metric does not reward them.

### EEMP-06 — The retained July preprint does not prove context useless

[Do Context Files Help Coding Agents, v1](https://arxiv.org/html/2607.27250v1), §§3.3–3.6, 4.5 and Limitations, includes 288 evaluated runs over 17 tasks in three Python repositories. No correctness gain is detected. The full methods qualify the abstract: 10–15-point equivalence bounds are descriptive, not a powered equivalence claim; minimum detectable effects exceed 30 points. Two selective corpora are much larger than their persistent counterparts. Claude receives system-prompt injection and Codex receives a user-turn prepend. **Implication:** compare equal-content delivery within each harness and avoid cross-agent causal claims. This run inspected the methods beyond the abstract originally retained by Apex.

### EEMP-07 — Configuration checks require version-specific semantics

[Scanning the Harness, v3](https://arxiv.org/html/2609.07360v3), §§3–6, reviews declarations in 3,171 sampled repositories. After semantic correction, 17.9% of setups contain one of six reported issues. These are declaration/conformance findings, not measured runtime vulnerabilities. Both mechanical checkers shared an erroneous interpretation of wildcard `find` grants; current documented semantics removed 62 findings. Sampling, copied configurations, and author-led review limit generalization. **Implication:** pin adapter assumptions to platform/version/surface, distinguish broad preapproval from allowed-tool restriction, and require actual installed probes. Two validators agreeing is not independent confirmation when both encode the same wrong rule.

### EEMP-08 — Compaction must preserve execution position

[TRACE, v2](https://arxiv.org/html/2608.06503v2), §§3–5 and §7, compares pre-/post-compaction continuations from the same environment state with frozen models. Its preliminary AppWorld experiments use a 4,096-token compression window and a 50-step cap. Compression can produce repeated exploration and blocked actions; the verifier may miss silent state corruption. **Implication:** keep a current action frontier, completed actions, constraints, unresolved choices, and source/version anchors in recovery state. Evaluate the first actions after resumption as well as final task success. No TRACE runtime is proposed for installation.

### EEMP-09 — Learned compaction results do not transfer to a prompt-only adapter

[AutoCompact, paper](https://arxiv.org/pdf/2610.02163), §§2–3, trains Qwen3-Coder-30B-A3B-Instruct through corrected trajectories and reinforcement learning. Evaluation shares a REPL scaffold and reports repeated SWE-bench results. Ablation by ignoring learned compaction calls supports a role for compaction, but the full gain combines training, summary construction, timing, and continuation. **Implication:** preserve decision-relevant working state and investigate appropriate boundaries. Do not promise the paper's improvement from adding a checkpoint prompt to an untrained CLI. PDF opened after the HTML route failed; project-page and paper headline numbers were not mixed.

### EEMP-10 — Deterministic checks cover only operationalized constraints

[IFEval](https://arxiv.org/html/2311.07911v1), §2 and §4, defines machine-checkable instruction types and distinguishes strict and relaxed evaluation. It supplies a useful reproducibility pattern, but its countable constraints are not a complete usefulness rubric. **Implication:** retain deterministic checks for actual schema, scope, and state requirements; add independent source/meaning review for decision quality. An empty file can satisfy an existence test while failing Apex's target requirement.

### EEMP-11 — Vary wording and length, not only a single trigger phrase

[LIFBench](https://aclanthology.org/2025.acl-long.803.pdf), §§3–5, expands instructions across length, expression, and variables, covering 11 tasks and 2,766 instructions. Its rubric-based scoring provides repeatable stability measurements in designed long-context scenarios. It does not validate a CLI's hook delivery or installed permissions. **Implication:** include paraphrases and misleading lexical matches in the Apex cases, and vary instruction position and research length while preserving the intended task.

### EEMP-12 — Large context capacity is not evidence of reliable access

[Lost in the Middle, v3](https://arxiv.org/html/2307.03172v3), §§2–5, varies evidence position in multi-document QA and key-value retrieval and finds substantial position sensitivity. The models and tasks are older than this run. **Implication:** use it as motivation for position-shift regression cases, not as a numerical estimate of current Apex performance. Stable artifact references and selective re-reading reduce reliance on remembered conversation position.

### EEMP-13 — Portable skill syntax is a packaging contract

[Agent Skills specification](https://agentskills.io/specification), Frontmatter and Progressive disclosure, requires `name` and `description`, with optional references/scripts/assets. `allowed-tools` is experimental and host-dependent. Validation checks format and naming; it does not establish correct activation or safe execution. **Implication:** package a coherent workflow with focused supporting references and preserve native host permissions separately. A reference-only definition need not become an independently selectable skill.

### EEMP-14 — Outcome grading needs traces and repeated trials

[Anthropic's evaluation guidance](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), Evaluation structure and Non-determinism, distinguishes task, trial, grader, transcript, and environmental outcome. It contrasts at-least-one-success with all-trials-success measures. This is vendor engineering guidance, not an independent controlled comparison. **Implication:** record observable traces and artifact state, audit disagreements, and report raw fractions before aggregate headlines. Avoid success claims based solely on an agent saying a check ran.

### EEMP-15 — Context engineering supports selective retrieval, with no automatic guarantee

[Anthropic's context-engineering guidance](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) describes curating context over an evolving agent loop. It is practice-oriented vendor guidance, not proof of a particular Apex improvement. **Implication:** compact evidence into a reusable state artifact and retrieve detailed owners on demand. Preserve enough high-signal state to continue the task; do not replace source authorities with an unverified summary.

## 3. Serious packaging alternatives

| Alternative | Strongest use | Material weakness | Proposed disposition |
|---|---|---|---|
| Improve existing XML/pointers/native files only | Cheapest baseline; minimal distribution changes | The retained Apex pilot reports missed judgment-gate reads; prose alone cannot establish delivery | Keep as measured baseline and viable fallback for surfaces without hooks |
| One independent skill for every reference | Discoverability and explicit invocation for independently meaningful procedures | Closely related descriptions compete; fixed definitions and subordinate fragments gain metadata without autonomy | Retain as operator-owned comparison; reject blanket conversion, allow independently useful workflows |
| Workflow skill with references | Research, Q&A/ranking, governed specifications, iterative delivery | Selection can be wrong or absent; a loaded skill may still omit references | Recommended procedural default, tested with negative routing cases |
| Native scoped rules | Instructions tied to actual governed paths | File scope cannot reliably recognize a chat-only comparison; semantics vary by host | Use for file-scoped obligations, with separate intent routing for conversation |
| Full always-on inlining | Small universal invariants; unsupported-hook fallback for a small critical rule | Context cost, duplication, unrelated ceremony, possible adherence dilution | Keep a small kernel; evaluate critical slices if measured routing remains unreliable |
| Hooks plus registry plus workflow references | Deterministic checks and recovery around observed tool/lifecycle events | Missed/disabled hooks, tool-coverage gaps, false positives, bad schemas, read-ledger shortcuts | Recommended only as thin adapters around common semantics, with explicit degraded behavior |

These are qualitative design judgments grounded in §2 and §4. No synthetic composite score is presented as empirical reliability. Preserve existing authored I/E/R and priority tiers in the main decision register; any new estimates belong in explicitly proposed decision entries.

## 4. Retained Apex evaluation audit

All repository citations in this section refer to `6c93ad31e42a72de74119218b9365bdd9d6ee386`.

### 4.1 Retained artifacts with different evidentiary value

| Artifact | What it actually establishes | Reuse decision |
|---|---|---|
| `apex-meta/informatics/final/tools/agent_eval_runner.py:145-196,299-320` | Baseline/challenger behavior is assigned in Python branches; no agent is invoked for those outcomes | Retain as historical simulation/illustration; never use its behavioral metrics as empirical trial evidence |
| `apex-meta/informatics/final/operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md:52-107` | Source reports eight real Claude subagent trials and names transcript paths; judgment refs omitted, schema refs read inconsistently | Reuse task structures and reported failure signal; local transcript bytes were not available to independently reproduce this run |
| `apex-meta/informatics/final/research/08-read-trace-routing-experiments/01-findings-and-protocol.md:135-192` | Source reports 72 headless Haiku cells; small inline domain-map guidance improved placement, while a blueprint pointer had no demonstrated advantage | Preserve contrary handover results, injection channel, corrected-scoring caveats and exact task denominators; use as support for improving existing project guidance before adding a router |
| `apex-meta/informatics/final/research/10-ultra-upgrade-validation/score_eval.py:108-414,520-745` | Parser consumes saved native traces and checks fixture state; it is more than a shape-only runner | Reuse parser and task structures after correcting scorer gaps, against pinned artifacts and live capability probes |

The pilot's current absolute-path finding is historical. The inspected XML now has a repository-relative `base_ref` at line 1. The design must preserve the old incident without asserting its exact path defect still exists. Cross-repository resolution still requires a declared base and source hash; basename discovery is insufficient.

### 4.1a Stage-1 evidence favors specific inline routing, with contrary gate results

The retained Mindful Bar study first reports eighteen read-only Explore subagents over nine tasks. A's rubric score is 40/45 and B's 37/45, **n=1, scorer not blind**; instructions explicitly told agents to read `AGENTS.md` and follow repository standards. Agents could not write, the fixture came from a dirty tree, and `<align>` was directly prompted. These are observed source-reported agent runs, not a deterministic simulation, but they do not establish comparative reliability or read-before-write behavior. [Source: `apex-meta/informatics/final/research/08-read-trace-routing-experiments/01-findings-and-protocol.md:28–43,70–107`.]

The same source's later Stage 1 reports 72 headless Haiku sessions: three arms × eight tasks × three repetitions. With the corrected scorer, gate delivery before write is A 3/21, B 4/21, C 3/21; placement is A 6/12, B 4/12, C 12/12. B's blueprint was touched in 1/24 cells. C added two specific domain-map/filing sentences. `<handover>` succeeds in 9/9 cells, contrary to the earlier pilot's 0/2; `<trade_off>` is 0/9, consistent with that pilot. **Do not summarize all conditional gates as uniformly failing or uniformly fixed.** The task and delivery method matter. [Same source:135–178.]

Stage 1 used one model/repository, task and arm author were the same, and the actual instruction channel was system-prompt injection rather than a native project file. The frozen scorer missed Bash reads and over-required index frontmatter; five cell scores changed after correction. The report distinguishes its preregistered 12 placement cells from a printed 15-cell aggregate. These observations justify precise denominator and delivery-channel recording. Raw stage-1 traces are referenced as archived; this module inspected the report and scorer, not a full archive replay. [Same source:180–192.]

The accompanying design review recommends generic routing in the contract and project-specific facts in Layer 2, avoiding a second router that repeats both. Its explanation at line 39 quotes an older “inline summary insufficient” condition; current XML line 74 has the stronger matching-condition read requirement. Preserve the recommendation as scoped source evidence, not a claim that an old pointer condition is still live. [Source: `apex-meta/informatics/final/research/08-read-trace-routing-experiments/03-design-review-routing-carriers.md:22–51`.]

**Corrected scorer audit:** `artifacts/stage1/score_stage1_corrected.py:145–161` counts a Read path or any eligible Bash command containing a known fragment without requiring successful returned owner content. `118–125` turns invalid validator JSON into an empty finding set. T5's `200–201` tests I/E/R-shaped strings and “recommend”, not grounding or decision usefulness. T6's `202–208`, however, verifies exact changed paths and a one-phrase delta; that is a stronger scope predicate worth reusing. These are static code findings, not newly executed Stage-1 probes. All paths here are under `apex-meta/informatics/final/research/08-read-trace-routing-experiments/`.

The original comparison retained three options with authored raw scores: repeat Explore agents `I40/E55/R20`; headless real-write cells `I85/E70/R35`; full protocol matrix `I90/E75/R55`. It chose the second, rejected repeated confounds in the first, and deferred the expensive full matrix before establishing the relevant question. These values are historical author estimates, not empirical reliability or scores of today's architecture. The proposal reuses the smallest-informative-pilot principle while independently testing the operator's material alternatives. [Source: `01-findings-and-protocol.md:111–133`, same directory.]

### 4.2 Round-2 result and causal limits

The retained result reports 18/33 passes for A, 31/33 for B-AGY, and 17/33 for D, with 99 batch runs and 14 smoke runs. B-AGY combines the baseline, concise reminders, and hooks. T1 records five premature writes intercepted; T6/T7 record no Stop blocks and first-pass close-out compliance. **The aggregate uplift is a combined-intervention result.** Intervention logs show that a hook changed the T1 write boundary; they do not provide the missing reminder-only versus hook-only counterfactuals. The report's phrase “separate their effects cleanly” is stronger than its factorial design warrants. [Repository: `apex-meta/informatics/final/research/10-ultra-upgrade-validation/01-results-and-verdict.md:20-51`.]

The model/profile, CLI surface, fixture content, global carrier contamination, and paired task repeats limit transfer. T7's roughly 58k context stress is not a measured compaction/restart test. The global carrier exclusion of Arm C and absent Gemini credentials are explicitly recorded. Treat zero reported thinking tokens as telemetry for that run, not proof of absent internal reasoning or justification for changing another model's instructions. [Same file:69-74; `preregistration.md:60-78` in the same directory.]

### 4.3 Executed synthetic scorer probes

Four isolated probes executed in this research run using the unchanged retained scorer. They created temporary synthetic fixtures, invoked no agent or network, and performed no Git operation. Results and source hash are in [scorer-probe-results.json](../evaluation/scorer-probe-results.json); [scorer_probe.py](../evaluation/scorer_probe.py) reproduces them from a supplied copy of `score_eval.py`.

| Probe | Observed result | Why it matters |
|---|---|---|
| P1: no validator exists, but the trace mentions its command | T1 `det_pass=true` | `_validator_errors_map` returns an error sentinel with an empty set; T1 discards the sentinel and sees no new errors |
| P2: approved-step file is zero bytes | T4 `det_pass=true` | Existence and maximum line count do not establish useful content |
| P3: Glob returns no matches/content | Parser counts the pattern as a read | Discovery or an attempted path is not successful source delivery |
| P4: typo fixed and unrelated file changed | T2 `det_pass=true` | This case has no exact changed-path scope check |

Source locations: `score_eval.py:477-497,539-559` (P1), `613-624` (P2), `228-233` (P3), `569-581` (P4), under `apex-meta/informatics/final/research/10-ultra-upgrade-validation/`.

These probes establish scorer weaknesses. They do **not** show that any retained historical trial exploited them or that its recorded verdict is wrong. Before reusing that scorer, make failed/missing validators unknown/fail; distinguish search, attempted read, successful delivered bytes, and executed write; verify exact paths/hashes; and add task-specific substance/scope criteria.

### 4.4 Hook fixture transfer limits

`fixtures/armB_hook_agy.py` is a benchmark adapter, not a general production implementation. It hard-codes T5/T7 retired markers and dirty fixture paths at lines 32–37, tracks reads at pre-tool time (222–232), uses substring `_has_ref` (194–195), and falls open on malformed input (468–475). A cached ledger accumulates across a conversation; no document hash or source-version validation is recorded. Stop allows a second stop in a turn after one intervention (359–362,458–464). Unknown tools are allowed (344–345). The metadata is useful for learning exact recorded payloads; the production proposal must not silently install this fixture as a universal enforcement layer.

General-purpose shell parsing cannot prove all mutations are covered. The fixture's Python command regex, fixed tool table, and substring match leave material coverage limits. Hook health must be visible; high-impact mutation gating needs the platform permission boundary or explicit unsupported status when coverage is absent. A once-per-turn warning prevents loops but cannot honestly be called an unbreakable hard gate.

## 5. Evaluation proposal that follows the evidence

The [evaluation plan](../evaluation/evaluation-plan.md) owns the concrete comparison arms, observation contract, staged acceptance criteria and adoption dependencies. This section explains their empirical rationale.

The [companion case file](../evaluation/cases.json) contains realistic unexecuted scenarios and separates applicability, source delivery, adherence, and useful outcomes. It reuses retained T1–T7 patterns without inheriting a blanket authorization to push or modify existing files. Any future commit/push trial uses a disposable local remote; the current research run authorizes none.

**Baseline first:** freeze sources and installed versions, record effective loaded instructions, prove trace completeness with a known successful read and a denied action, and run the difficult chat ranking, governed specification, correction, and negative cases. Compare the existing mechanism with an improved-native-only option before adding adapters.

**Attribution:** for relevant observed failures, compare the same base with reminder absent/present × hook absent/present. Hold the selected rule content, model, task, permissions, and time budget fixed. Run workflow packaging and per-reference skills separately; those arms change routing structure and must not be labeled a pure hook test.

**Recovery:** replay a task before and after interruption/compaction from equivalent artifact state. Record lost constraints, repeated retrieval, duplicate side effects, first incorrect resumed action, and final outcome. A checkpoint that merely parses is insufficient.

**Judgment:** an independent verifier reads the task and authoritative sources, evaluates evidence and domain meaning, and gives cited failure reasons. Blinded artifact review should ignore whether the agent used an impressive framework name. LLM judgment is advisory for semantic questions, calibrated against operator-reviewed examples; deterministic checks handle schema/scope/state.

**Reporting:** report raw task-level fractions, failures, unknown/blocked cases, latency, measured token categories, and irrelevant-loading overhead. Small pilots identify defects; they do not establish precise reliability. Do not pool repeated variants as independent tasks to manufacture narrow confidence bounds. Record failed and timed-out trials instead of quietly deleting them.

**Adoption gate:** all authorization/scope invariants must hold in the covered cases; relevant refs must be delivered before action/final answer where required; each accepted output must solve its actual task; negative cases must avoid ceremony; disabled-hook runs must honestly enter the documented fallback. Broaden testing only when a material uncertainty remains.
