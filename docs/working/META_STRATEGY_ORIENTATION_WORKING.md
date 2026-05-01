# Meta Strategy Orientation Working File

Status: `working`
Owner: `meta_strategy`
Primary validator: `meta_detective`
Created: `2026-05-01`
Purpose: persistent orientation surface for future Meta Strategy build flows, prompts, and KB updates.

> This is a working orientation file, not accepted canon. Use it to preserve current decisions and workflow logic. Promote only validated doctrine into `managed/agent_kb/meta_strategy/` through the normal validation path.

---

## 1. Current decision lock

### 1.1 What Meta Strategy is

Meta Strategy is the strategic reasoning coordinator for high-impact route decisions.

It owns:

- option framing
- scenario comparison
- timing analysis
- leverage analysis
- recommendation packets
- explicit assumptions, dependencies, reversibility notes, and validation handoffs

It produces decision-ready recommendations without executing them.

### 1.2 What Meta Strategy is not

Meta Strategy must not become:

- an execution controller
- a direct implementation agent
- a self-validator
- a KB promotion authority
- a taxonomy owner
- a config authority
- a universal CEO brain
- a project-specific product strategist only

Boundary formula:

```text
Strategy proposes.
Meta Ops orchestrates.
Meta Detective challenges.
Knowledge Bank/Informatics route and structure knowledge.
Operator or configured governance approves high-risk moves.
```

---

## 2. Main correction from the Business Plan extraction

Earlier extraction mixed two layers:

1. project-specific Leela strategy content
2. generic Meta Strategy doctrine

Corrected rule:

- Leela-specific concepts such as Meta-App, Epic/Rhythm/Sequencing, creator networks, Sid, data marketplace, blockchain, gamification mechanics, and micro-influencer strategy belong to project-specific strategy context.
- Generic tools such as option framing, scenario comparison, timing logic, leverage analysis, 5W, Why-How-What, Problem-Need-Solution, MECE, pre-mortem, assumption ledgers, and recommendation packets belong to Meta Strategy doctrine.

The Meta Strategy head should inherit reusable strategy mechanics, not the Leela product model.

---

## 3. Current recommendation on sub-heads

### 3.1 Decision

Do not create permanent Meta Strategy sub-agents yet.

Create internal sub-lanes / modes / templates first.

### 3.2 Reason

Permanent sub-agents would currently risk bloat. The stronger next step is to encode specialist strategy modes inside the Meta Strategy KB and use them through workflows/templates. Promote only after repeated use proves distinct value.

### 3.3 Candidate internal sub-lanes

| Sub-lane | Status now | Main tools | Function |
|---|---|---|---|
| Logic Architect | KB mode, not agent | MECE, issue trees, first principles, argument mapping, Pyramid Principle | Structure the problem and avoid gaps/overlap. |
| Scenario & Timing Strategist | KB mode, not agent | Scenario planning, Cynefin, OODA, Three Horizons, real options, reversibility | Handle uncertainty, timing, act/wait/stage decisions. |
| Creative Reframer | KB mode, not agent | Six Thinking Hats, Disney Method, Reframing Matrix, Blue Ocean | Expand option space and prevent local-optimum thinking. |
| Assumption & Leverage Mapper | KB mode, not agent | 5 Whys, root cause, Ladder of Inference, assumption ledger, leverage points | Surface load-bearing assumptions and high-leverage moves. |
| Strategy Synthesizer | KB mode, not agent | Problem-Need-Solution, Why-How-What, 5W, decision matrix, recommendation packet | Combine outputs into one decision-ready recommendation. |

### 3.4 Promotion rule for sub-lanes

A sub-lane becomes a true sub-agent only if all conditions hold:

- recurring bounded work across sessions or projects
- clear input and output packet
- distinct knowledge base need
- value not covered by adjacent agents
- independent validation benefit
- explicit handoff path
- bounded activation by Meta Ops
- overlap improves drift control more than it increases complexity

### 3.5 Sub-lane working-file registry

| Lane | Working file | Status | Promote now? |
|---|---|---|---|
| Logic Architect | `docs/working/META_STRATEGY_LOGIC_ARCHITECT_WORKING.md` | working | no |
| Scenario & Timing Strategist | `docs/working/META_STRATEGY_SCENARIO_TIMING_WORKING.md` | working | no |
| Creative Reframer | `docs/working/META_STRATEGY_CREATIVE_REFRAMER_WORKING.md` | working | no |
| Assumption & Leverage Mapper | `docs/working/META_STRATEGY_ASSUMPTION_LEVERAGE_WORKING.md` | working | no |
| Strategy Synthesizer | `docs/working/META_STRATEGY_SYNTHESIZER_WORKING.md` | working | no |

Registry rule:

```text
These files are orientation and workflow surfaces only. They are not accepted canon, not managed agent seeds, and not separate KB roots. Promote compact validated entries only through the governed Meta Strategy KB path.
```

Scoring note:

```text
Lane-local readiness or candidate-priority scores are internal working signals only. Governed handoff and promotion metadata uses the active EVD / IMP / RSK 1-100 scale.
```

---

## 4. Strategy tool stack

### 4.1 Expansion frames

Use when the option space is too narrow.

| Tool | Use |
|---|---|
| Six Thinking Hats | Separate data, emotion, risk, upside, creativity, and process. |
| Disney Method | Dreamer -> Realist -> Critic loop. |
| Reframing Matrix | Force stakeholder and perspective shifts. |
| Blue Ocean / ERRC | Eliminate, Reduce, Raise, Create dimensions. |

### 4.2 Structure frames

Use when the reasoning needs clean decomposition.

| Tool | Use |
|---|---|
| MECE | Avoid gaps and overlaps. |
| Issue Trees / Logic Trees | Break complex decisions into drivers. |
| First Principles | Strip inherited assumptions. |
| Argument Mapping | Separate claim, support, evidence, objection, rebuttal. |
| Pyramid Principle | Make final output answer-first and executive-readable. |

### 4.3 Uncertainty and timing frames

Use when futures, risk, timing, or reversibility matter.

| Tool | Use |
|---|---|
| Scenario Planning | Compare multiple plausible futures. |
| Cynefin | Classify problem type before selecting method. |
| OODA | Iterate in unstable environments. |
| Three Horizons | Separate now / next / future bets. |
| Real Options | Preserve upside without overcommitting. |
| One-way / Two-way doors | Decide speed versus caution. |
| Assumptions-Based Planning | Define assumptions and kill criteria. |
| Pre-Mortem | Imagine failure and work backward. |

### 4.4 Synthesis frames

Use when producing final strategy output.

| Tool | Use |
|---|---|
| Problem -> Need -> Solution | Clarify pain, required capability, and proposed intervention. |
| Why -> How -> What | Align purpose, mechanism, and action. |
| 5W | Check completeness: why, what, who, when, where, how. |
| Decision Matrix | Compare options by agreed criteria. |
| Assumption Ledger | Make the recommendation challengeable. |
| Recommendation Packet | Final output contract. |

---

## 5. Cross-frame workflow

### 5.1 Default loop

```text
1. Define decision question.
2. Clarify objective and constraints.
3. Run 2-5 independent strategy frames.
4. Confront frame outputs instead of averaging them.
5. Log agreements, conflicts, missing details, and assumptions.
6. Score options by impact, risk, cost, evidence, reversibility, timing, and leverage.
7. Produce recommendation packet.
8. Hand risky assumptions to Meta Detective.
9. Hand accepted execution coordination to Meta Ops.
10. Capture reusable patterns for KB promotion review.
```

### 5.2 Why-How-What vs 5W confrontation pattern

Use this when a recommendation must be both purpose-coherent and implementation-complete.

```text
Input: same decision question to two independent passes.
Pass A: Why -> How -> What.
Pass B: 5W.
Compare:
- What does A clarify that B missed?
- What does B clarify that A missed?
- Where do they conflict?
- What assumption explains the conflict?
- What synthesis survives both views?
```

Example expected synthesis:

```text
Why-How-What clarifies purpose and mechanism.
5W exposes ownership, timing, location, and execution path.
Final recommendation must include both.
```

### 5.3 Cross-frame confrontation table

| Frame A | Frame B | Agreement | Conflict | Missing detail | Resolution |
|---|---|---|---|---|---|
| Why-How-What | 5W | | | | |
| MECE / Issue Tree | Creative Reframe | | | | |
| Scenario Planning | Reversibility | | | | |
| Assumption Ledger | Pre-Mortem | | | | |

---

## 6. Multi-agent routing pattern

### 6.1 Minimal routing

| Need | Route |
|---|---|
| More than one viable path | Meta Strategy |
| Sequencing or assignment of work | Meta Ops |
| Contradiction, evidence weakness, plausibility challenge | Meta Detective |
| Reusable prompt/process needed | Prompts / Workflows lane |
| Model/tool/subscription choice matters | AI Handling / Routing lane |
| Knowledge placement, accepted vs candidate status | Knowledge Bank |
| Taxonomy, file structure, readability, chunking | Informatics Design |

### 6.2 Strategic redundancy principle

Use overlap intentionally, but only with bounded purpose.

Good overlap:

- Strategy proposes and Detective challenges.
- Logic Architect structures and Creative Reframer expands.
- Scenario & Timing checks Assumption & Leverage.
- Synthesizer resolves conflicts into one recommendation.

Bad overlap:

- several agents produce independent answers with no confrontation table
- agents vote without evidence criteria
- Strategy validates itself
- Strategy starts executing
- new sub-agents are created before repeat need exists

---

## 7. Model / subscription usage pattern

Use model diversity to reduce shared blind spots, not to create voting theater.

| Model type | Best use | Avoid |
|---|---|---|
| Deep reasoning model | final synthesis, contradiction reconciliation, scenario comparison | cheap extraction |
| Creative model/chat | reframing, option expansion, Six Hats, Disney Dreamer | final authority |
| Research assistant | external evidence and framework validation | internal repo truth |
| Repo-grounded model/tool | existing repo logic, file boundaries, source verification | speculative strategy |
| Detective/adversarial model | pre-mortem, red-team, base-rate challenge, assumption testing | primary recommendation generation |
| Fast/cheap model | extraction, tagging, duplicate detection, first-pass option inventory | high-stakes synthesis |

Rule:

```text
Model diversity creates independent frame outputs.
Meta Strategy synthesizes.
Meta Detective challenges.
Meta Ops coordinates any accepted execution.
```

---

## 8. Recommendation packet template

```md
# Meta Strategy Recommendation Packet

## 1. Decision question

## 2. Objective

## 3. Constraints

## 4. Evidence status
- known facts:
- assumptions:
- unknowns:
- evidence gaps:

## 5. Independent frame outputs
- Why -> How -> What:
- 5W:
- MECE / Issue Tree:
- Scenario / Timing:
- Creative Reframe:
- Assumption / Root Cause:

## 6. Cross-frame confrontation
| Frame A | Frame B | Agreement | Conflict | Missing detail | Resolution |
|---|---|---|---|---|---|

## 7. Option comparison
| Option | Upside | Risk | Cost | Reversibility | Evidence | Timing | Leverage |
|---|---:|---:|---:|---:|---:|---:|---:|

## 8. Recommendation

## 9. Validation handoff to Meta Detective

## 10. Execution handoff to Meta Ops

## 11. Stop / revisit trigger
```

---

## 9. Strategy -> Detective handoff

Use whenever the recommendation is high-risk, weakly evidenced, irreversible, or politically/architecturally sensitive.

Questions for Detective:

- What load-bearing assumption is weakest?
- What evidence would falsify this recommendation?
- What second-best option was unfairly dismissed?
- Where did Strategy jump from fact to interpretation?
- What conflict did the synthesis smooth over too quickly?
- What base-rate or comparable case contradicts the recommendation?
- What hidden incentive could bias the recommended path?
- What would a pre-mortem say caused failure?

Detective should not rewrite the strategy by default. It should return findings, contradictions, severity, and suggested validation gates.

---

## 10. Strategy -> Meta Ops mission brief

Use only after Strategy has produced a recommendation and Detective review is complete or explicitly waived.

```md
# Strategy -> Meta Ops Mission Brief

## Objective

## Recommended path

## Constraints

## Required agents / lanes

## Sequence proposal

## Success criteria

## Risks to monitor

## Stop conditions

## Human/operator decision needed?
```

---

## 11. KB update plan

### 11.1 Put into `ESSENCE.md` only after validation

- Meta Strategy is the strategic reasoning coordinator.
- It owns decision-shaping, not execution.
- It uses multi-frame triangulation.
- It produces challengeable recommendation packets.
- It routes high-risk assumptions to Meta Detective.

### 11.2 Put into `BEST_PRACTICES.md` after validation

- Use multiple independent frames before recommending.
- Use frame confrontation, not aggregation.
- Separate expansion, structure, uncertainty, synthesis, and challenge.
- Use timing/reversibility before recommending commitment.
- Use the smallest useful activation set.
- Route model/tool choice to AI Handling/Routing when material.
- Route reusable patterns to Prompts/Workflows.

### 11.3 Put into `TEMPLATES.md` after validation

- Cross-frame recommendation packet
- Why-How-What vs 5W confrontation
- Scenario packet
- Reversibility/timing matrix
- Strategy -> Detective handoff
- Strategy -> Meta Ops mission brief

### 11.4 Put into `MISTAKES.md` after validation

| Mistake | Meaning |
|---|---|
| Single-frame confidence | One framework is treated as truth. |
| Council bloat | Too many agents activated before bounded need exists. |
| Strategy absorbs Ops | Strategy starts assigning/executing instead of recommending. |
| Strategy self-validates | Strategy marks its own assumptions as safe. |
| Framework theater | Framework labels are used without real comparison. |
| False synthesis | Conflicts are smoothed over instead of resolved. |
| Model monoculture | One model family creates all views. |
| Voting theater | Multiple agents vote without evidence criteria or conflict ledger. |

### 11.5 Put into `LEARNING_QUEUE.md` as candidate-only

- candidate sub-lane: `logic_architect`
- candidate sub-lane: `scenario_timing_strategist`
- candidate sub-lane: `creative_reframer`
- candidate sub-lane: `assumption_leverage_mapper`
- candidate sub-lane: `strategy_synthesizer`

---

## 12. Future-flow starting protocol

For every future Meta Strategy flow, start here:

```text
1. Read this working orientation.
2. Check current accepted Meta Strategy ESSENCE.
3. Identify whether the task is project-specific or generic strategy doctrine.
4. Do not import Leela-specific product strategy into generic Meta Strategy doctrine.
5. Select the smallest useful strategy frame set.
6. Run independent frame passes.
7. Confront outputs.
8. Produce recommendation packet.
9. Route validation to Meta Detective if risk/uncertainty is high.
10. Route execution coordination to Meta Ops only after recommendation is bounded.
```

---

## 13. Non-negotiable current decisions

- Do not create permanent Meta Strategy sub-agents yet.
- Do create sub-lanes as KB modes/templates.
- Do not treat one scenario analysis as sufficient truth.
- Do use cross-frame confrontation.
- Do use model diversity when it materially reduces blind spots.
- Do not use model diversity as voting theater.
- Do not let Strategy absorb Detective, Meta Ops, Knowledge Bank, Informatics, or config authority.
- Do not promote this working file directly into canon without validation.

---

## 14. Working-file maintenance rule

Update this file when a major architecture decision changes. Do not treat it as accepted runtime law. For canon, promote validated entries into the Meta Strategy KB scaffold only after review.
