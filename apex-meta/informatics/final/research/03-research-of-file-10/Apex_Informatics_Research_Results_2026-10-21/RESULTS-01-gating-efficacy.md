---
type: Reference
id: RESULTS-01-gating-efficacy
title: Conditional instruction gating efficacy - Findings
description: Assesses whether task-conditioned instructions stop irrelevant file reads by coding agents.
status: current
tags: [research-result, gating, rp-01]
---

# RP-01 - Does conditional instruction gating actually work?

**Verdict (confidence: medium for conditional-instruction risk; low for file-read gating efficacy):** Models and coding agents do act on contextual instructions, but there is **no identified controlled, public test demonstrating that an XML `when=` attribute prevents a tool-using coding agent from opening nonmatching files**, or that it outperforms plain-language IF/THEN with identical rule bodies and links. Do not infer a functioning dispatch mechanism from a markup convention. The strongest pertinent controlled agent study found that repository context files increased exploration and inference cost by **more than 20% on average**, while their instructions were often followed. A second 1,650-session factorial experiment failed to detect significant effects for the tested file-structure variables. These findings warrant the repository's existing B-vs-C read-trace test, not a premature claim that conditional dispatch works.

## Evidence

| Claim | Source link | Evidence type | Supports / undermines |
|---|---|---|---|
| Agents follow operational instructions in AGENTS.md-style files, but context files generally failed to improve task completion and increased inference cost by >20%. This is not an IF-gating test. | [Gloaguen et al., 2026, arXiv:2602.11988](https://arxiv.org/abs/2602.11988) | Controlled coding-agent benchmark (SWE-bench Lite and CTXbench; multiple models/agents) | Supports instruction influence; undermines untested assumption that added instructions save effort |
| 1,650 coding-agent sessions and 16,050 function-level observations did not detect significant adherence contrasts from manipulated file size, instruction position, file architecture, or conflicting adjacent files after correction. The target was a function annotation, not scoped file reads. | [McMillan, 2026, arXiv:2605.10039](https://www.alphaxiv.org/abs/2605.10039) | Controlled factorial coding-agent study | Undermines strong assertions about markup/file architecture improving obedience; **not** direct evidence against conditional gating |
| Conditional instructions and irrelevant distractors can degrade task adherence; large and frontier models show 40-50% performance drops on the paper's knowledge-conditioned tasks. These are answer-modification tasks, not agent traces. | [Murthy et al., KCIF, LREC 2026](https://aclanthology.org/2026.lrec-1.339/) | Controlled benchmark of conditional instruction following | Undermines assumption that a task gate is reliably evaluated under competing instructions |
| AgentIF includes condition constraints and tools across 50 agent applications, with a 2026-10 revised evaluation setting. It does not isolate this repository's `when=` versus prose dispatch. | [AgentIF benchmark](https://agentif.github.io/) | Benchmark documentation | Supports feasibility of testing; cannot establish read-gate efficacy |
| AdvancedIF reports continued difficulty with complex, multi-turn/system-prompt instructions; a training method raises its benchmark score 6.7 absolute points. | [He et al., ACL 2026](https://aclanthology.org/2026.acl-long.820/) | Controlled model benchmark and training evaluation | Undermines any claim of universal obedience to multi-constraint instruction bundles |
| The local plan already isolates the gate from content: A=baseline, B=gated, C=ungated with same rules and refs, D=split file structure. | [`04-empirical-test-protocol.md`, sections 2 and 7](04-empirical-test-protocol.md) | Repo test design, **not measured outcome** | Supports valid *future measurement*, not efficacy |

## Strongest case that this does not work

`when=` is not an instruction-file feature with machine-enforced semantics. It is merely text presented to a model. The agent may regard the linked file as useful despite the predicate being false, or may confuse "possible future applicability" with the task actually in scope. The ETH coding-agent study provides a mechanism for harm: agents often obey unnecessary directions, perform more exploration/tests and spend more, without increasing task success. KCIF shows even seemingly irrelevant conditional and distractor instructions interfere in ordinary models. None of these sources demonstrates agents will resist speculative loads; there is no reason to credit the `when=` attribute as if it were runtime access control.

**Strongest case for the technique:** Modern agents can correctly interpret clear task conditions in many instances, and they obey context-file instructions that prescribe tools/commands. A short rule pointing at a distinct file plausibly saves substantial downstream context when the agent follows it. This is a credible hypothesis, not a demonstrated performance guarantee.

## Known failure modes

- **Over-trigger:** opens several candidate modules for a one-module task; no measured rate specific to the proposed syntax.
- **Under-trigger:** never opens the needed module; no measured rate.
- **Wrong scope classification:** chooses an irrelevant condition for an ambiguous task; no measured rate.
- **Negative-directive interference:** "do not read unless" itself adds a constraint. KCIF shows instruction/distractor interference, but does not quantify an equivalent negative-versus-positive gate comparison.
- **Instruction inflation:** longer agent trajectories and >20% cost in the Gloaguen et al. context-file comparison; do **not** relabel this as an over-trigger rate.
- **Long-session adherence loss:** McMillan reports an exploratory within-session odds ratio of 0.944 per additional generated function in the tested range; it is **not** a probability of ignoring `when=`.

## Concrete guidance

1. **Do not ship `DEC-16` as an established saving.** Run the existing A/B/C/D protocol with read-tool traces, not model self-reports.
2. Keep conditions as short, observable task predicates; link only the relevant canonical file. Prefer positive ``If editing an existing file, read X`` over multiple negative variants, **pending** a controlled comparison; this is design prudence, not an experimentally proven advantage.
3. Score unnecessary reads, necessary reads, task success, output quality, downstream tokens, and elapsed/cached cost separately.
4. Compare XML `when=`, plain IF/THEN, and an ungated `ref=` under equal task/model/harness conditions. The existing B/C control is essential; adding a prose-IF arm would isolate markup *syntax*.
5. Preserve the pre-registered local thresholds: B bloat below 20% **and** B beats C by more than 15 percentage points would support gates; B bloat above 40% would falsify the proposed split. Do not claim these thresholds were observed.

## What I could not find

- A controlled, public **tool-using agent** experiment isolating `when=` attribute syntax from otherwise identical plain IF/THEN conditions.
- A controlled experiment that compares conditional dispatch against unconditional prose using **read traces**, rather than answer quality.
- A valid rate for negative-versus-positive instruction **file-read** compliance, or specific over- and under-trigger rates for this design.
- An external guarantee that these custom XML attributes are parsed by the agent harness rather than inferred by the language model.

## Consequence for the contract

- `DEC-16`: **UNVERIFIED**, neither confirmed nor falsified. Its 83% potential module-read saving is arithmetic **conditional on correct routing**, not observed behavior.
- `DEC-M2`: gating's alleged precision benefit is **UNVERIFIED**; test B against C.
- `DEC-12`: always-on invariants do not depend on gating and survive this finding as a design proposition.
- `DEC-17`: evidence does not demonstrate named XML tags improve file-read gating; the operator's clarity preference can stand until an actual adverse result.
- Carry into `RP-08`/`RP-06`: `when=` and `deepen_when=` are **human/model-readable hints**, not enforced control flow.
