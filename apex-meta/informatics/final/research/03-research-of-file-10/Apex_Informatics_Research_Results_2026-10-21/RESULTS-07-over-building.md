---
type: Reference
id: RESULTS-07-over-building
title: Interventions against agent over-building - Findings
description: Evidence review of pre-action checks, budgets, scope contracts, audits and permission gates.
status: current
tags: [research-result, over-building, rp-07]
---

# RP-07 - What actually reduces over-building?

**Verdict (confidence: medium):** Over-building is principally an **objective/scope and completion-signal failure**, with action bias and planning contributing. The strongest first intervention is an **explicit product deliverable and an allowance for 'no change necessary'**, followed by a **narrow pre-action check for additional machinery**. The pre-action idea has **partial analog evidence**, but no controlled study here establishes the candidate's exact wording as an effective anti-overbuilding fix. Runtime budgets, independent review and permission checks can contain consequences, but blanket caps or universal approval gates can suppress necessary work. **Do not solve unwanted extra machinery by building a large new monitoring system.**

## Evidence

| Claim | Source link | Evidence type | Supports / undermines |
|---|---|---|---|
| A **200-task** benchmark of issues already resolved found coding agents proposed unwanted changes in **35%-65% of cases** depending on tested system. An explicit *reproduce before modifying* instruction partly mitigated the action bias, but also produced false abstention on partially fixed bugs. | [Gloaguen et al., *Coding Agents Don't Know When to Act*, May 2026](https://arxiv.org/abs/2605.07769) | Controlled coding-agent benchmark (preprint) | Supports a pre-action check **in an analogous no-change task**; warns against too-timid agents |
| Repo context files increase broad code exploration, test activity and cost by **over 20%** in the tested settings, often without better task success. | [Gloaguen et al., *Evaluating AGENTS.md* (2026)](https://arxiv.org/abs/2602.11988) | Controlled coding-agent benchmark | Undermines the 'just add more guardrail prose' response |
| Agent vendor specifically documents **overengineering tendencies** in selected Claude models and recommends scope limits: avoid unsolicited refactors, helpers, extra validation and speculative flexibility. | [Anthropic Claude prompting best practices - Overeagerness](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Vendor guidance / production observations, not controlled efficacy measure | Supports targeted explicit scope language, not quantified prevention |
| A controlled **web-search-agent** study finds more tool budget alone does not improve performance; budget awareness can improve cost-performance trade-offs. It does **not** test coding-agent extra files. | [Liu et al., *Budget-Aware Tool-Use* (Nov 2025)](https://arxiv.org/abs/2511.17006) | Controlled experiment in adjacent agent domain | Supports targeted budget awareness, undermines unlimited steps as a solution |
| Vendor engineering experience across dozens of deployments favors minimal composable systems and adding complexity only when justified. | [Anthropic, *Building Effective Agents* (Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents) | Vendor production synthesis | Supports simple-first heuristic but is **not** a randomized test of overbuilding |
| A 2026 controlled coding-agent study demonstrates chasing a passing test signal can yield a demo with a missing/dead reusable library - a **wrong completion target**, not just excess code. | [Ma et al., *Building to the Test* (June 2026)](https://arxiv.org/abs/2606.28430) | Controlled coding-agent study, narrow task | Supports primary classification as objective/completion error |
| OpenAI's own Codex engineering report rejected a giant all-in-one agent instruction manual after poor experiences; it gives agents a navigation map plus task-relevant details. | [OpenAI, *Harness engineering* (Feb 2026)](https://openai.com/index/harness-engineering/) | Vendor production report | Reinforces scarce-context priority and avoiding policy accumulation |
| The particular P0 problem is an autonomous run spending budget on verification machinery instead of its deliverable; the pre-action candidate applies when **about to add a script/test/gate/schema/wrapper**. | [`09-contract-block-v0.5.md`, section 2; `08-discussion-and-open-threads.md`, section 8](09-contract-block-v0.5.md) | Repository problem statement and proposed wording | Defines intervention target; not measured evidence |

## Ranking of requested interventions

| Rank | Intervention | Mechanism and evidence | Failure mode | Cost |
|---:|---|---|---|---|
| **1** | **Outcome/scope output contract**: name concrete deliverable, verify that before optional changes | Prevents success being redefined as scripts, tests and checklists. Supported by [Ma et al.](https://arxiv.org/abs/2606.28430) as a failure diagnosis and [OpenAI engineering](https://openai.com/index/harness-engineering/) production practice; **not a matched prompt ablation** | Agent over-narrows interpretation of what product must include | Low prompt cost; task-dependent review |
| **2** | **Pre-action check**: reproduce a defect or identify a blocking dependency before new machinery | Partial measured analog from [FixedBench](https://arxiv.org/abs/2605.07769). Locates judgment before side-effect. **Exact new-script gate untested.** | Falsely skips necessary regression tests, safety controls, or partially fixed bug | One reasoning decision per meaningful addition |
| **3** | **Selective post-hoc review / change-diff audit** against originally requested functionality | Separates claimed success from actual product and unsolicited delta; [Ma et al.](https://arxiv.org/abs/2606.28430) independently inspected delivered library | Turns into another verification treadmill if done after every trivial edit | Additional inspection; proportionate to impact |
| **4** | **Budget awareness**, not hard caps | Adjacent evidence: [Liu et al.](https://arxiv.org/abs/2511.17006) budget-aware agents more cost-effective than merely increasing calls | Arbitrary limit stops a legitimate difficult feature; optimizing token/step count replaces user requirement | Low when lightweight; high if building new tracker infrastructure |
| **5** | **Permission gate** before adding machinery | Real human can reject scope creep; no controlled evidence found for its ROI in agent code tasks | Frequent confirmations block autonomous operation and add oversight burden | Potentially high workflow latency; clashes with no-confirmation operator preference |
| **6** | **Simpler verified tool/process design** rather than general new gates | Vendor [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) production approach, [OpenAI](https://openai.com/index/harness-engineering/) production report | Existing complexity may be genuinely necessary for safety or scale | Usually reduces maintenance, but environment-specific |

**What the ranking means:** This is a synthesis of **different kinds of evidence**, not a quantitative winner-takes-all ranking. No matched randomized study comparing all six interventions for coding-agent scaffolding was located.

## Is pre-action checking the right point?

**Conditionally yes**: It is less expensive to decline an unnecessary file **before** writing it than to reverse it later. The controlled [FixedBench](https://arxiv.org/abs/2605.07769) result provides unusually direct evidence for a check at this point: reproduce before patching partly reduces unsupported action, but at the risk of skipping partially needed fixes. Thus the rule must ask **'Does this action materially enable the specified result, protect it, or test it appropriately?'**, not **'Can I avoid writing any new file?'**. A pre-action cue still depends on model discretion and may never fire; `DEC-20` needs an observed action/trace comparison.

### Preferred compact directive (34 words; under 40)

> Deliver the requested product before optional infrastructure. Before adding a script, test, gate or abstraction, identify the requirement, blocker or material risk it serves. Otherwise defer it; do not mistake verification activity for completion.

This formulation allows genuinely needed test and safety work. **Research-only**; no live contract modification.

## Root-cause classification

- **Scope/objective (primary):** the agent treats adjacent engineering enhancements as authorized without showing they enable the user's deliverable.
- **Completion signal (primary):** tests and validation scripts become the apparent product; passing them crowds out user acceptance (`RP-05` / [Ma et al.](https://arxiv.org/abs/2606.28430)).
- **Planning/action bias (contributing):** a model assumes 'doing something' is always success (`FixedBench`); a longer plan creates more steps that feel obligatory.

A tool/runtime mechanism is justified **only after** tests show prompt-only interventions fail at an unacceptable frequency or when damage warrants authorization enforcement. Do not jump from 'overbuilding exists' to 'build another gate.'

## Strongest case against the verdict

The 'product-first' instruction could make an agent prematurely skip critical security checks, integration tests and architecture that the product **genuinely** needs. The [FixedBench](https://arxiv.org/abs/2605.07769) reproduction-first instruction already illustrates the false-abstention trade-off. Moreover, some work is *primarily* infrastructure or verification, so a global 'avoid machinery' style rule would directly conflict with the requested product. A runtime allowlist for file creation, bounded execution or enforced change approval is more reliable than subjective natural-language policy for high-impact edits. If `DEC-20` shows the model repeatedly adds unrequested machinery despite prompts, the pre-action gate **must not be advertised as effective**, and a narrow structural control may be necessary. Evidence currently supports **testing** rather than certifying the phrase.

## What I could not find

- A controlled *same agent / same tasks* comparison of the six intervention points **specifically measuring unnecessary scripts, validators, wrappers and schemas**.
- A verified false-positive/false-negative rate for the exact current `<new_machinery>` and `<detour>` clauses.
- A cost threshold at which adding a human approval gate improves net completion under the operator's autonomous-one-go preference.
- Evidence that a fixed file count or tool-call budget safely prevents scope creep without harming task completion in coding agents generally.

## Consequence for the contract

- **`DEC-20`**: underlying behavioral failure **supported**; proposed **observable-action gates still NEED_TEST**, not confirmed. Compare requested-product completion, unsolicited-new-file rate and safety/quality across arms.
- **`<new_machinery>` / `<detour>`:** keep as **candidate** and assess as an adjunct to existing `<scope>`, `<target>` and `<product_first>`. Check whether separate gates add anything beyond these universal rules.
- **`DEC-18`, `DEC-19`**: same lesson applies: placement or prohibition alone cannot be assumed causally effective.
- **Avoid additional process layers** until a clear, measured failure demonstrates the need for them.
