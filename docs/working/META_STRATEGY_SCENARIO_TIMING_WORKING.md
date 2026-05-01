# Meta Strategy Scenario & Timing Strategist Working File

Status: `working`
Parent: `docs/working/META_STRATEGY_ORIENTATION_WORKING.md`
Owner: `meta_strategy`
Sub-lane: `scenario_timing_strategist`
Primary validator: `meta_detective`
Created: `2026-05-01`
Purpose: define the Scenario & Timing Strategist sub-lane for Meta Strategy before any promotion into accepted KB or permanent sub-agent status.

> This file is a working orientation artifact. It is not accepted canon, not a managed agent seed, and not a standalone sub-agent. Promote only validated, compact entries into `managed/agent_kb/meta_strategy/`.

---

## 1. Decision lock

### 1.1 Current decision

`scenario_timing_strategist` is an internal Meta Strategy sub-lane / mode, not a permanent sub-agent.

### 1.2 Why it exists

The Scenario & Timing Strategist prevents strategic recommendations from assuming that:

- one future is enough
- acting now is always better than waiting
- waiting is always safer than acting
- high upside justifies high commitment
- reversible and irreversible decisions should use the same process
- uncertainty can be solved by false precision
- timing pressure can be ignored until execution

### 1.3 Core value

The Scenario & Timing Strategist converts a static strategy into a dynamic path decision across uncertainty, time pressure, reversibility, and option value.

Working formula:

```text
Option set -> uncertainty map -> scenario comparison -> timing pressure -> reversibility -> act / wait / stage recommendation
```

---

## 2. Role boundary

### 2.1 Owns

- scenario comparison
- strategic uncertainty framing
- timing analysis
- act / wait / stage logic
- reversibility analysis
- one-way vs two-way door classification
- real-options framing
- horizon mapping: now / next / future
- weak-signal watchlist
- timing-pressure and cost-of-delay reasoning
- scenario-dependent assumption notes

### 2.2 Does not own

- final recommendation by itself
- execution sequencing
- adversarial validation
- evidence verification as final authority
- creative option generation as main lane
- full logical decomposition as main lane
- KB promotion
- config or managed seed mutation

### 2.3 Boundary with neighboring lanes

| Neighbor | Split |
|---|---|
| `logic_architect` | Logic Architect structures the decision; Scenario & Timing tests whether that structure holds across futures and timing conditions. |
| `creative_reframer` | Creative Reframer expands possible paths; Scenario & Timing tests when and under which futures those paths make sense. |
| `assumption_leverage_mapper` | Assumption/Leverage ranks load-bearing assumptions and leverage points; Scenario & Timing turns them into watch signals, gates, and staged commitments. |
| `strategy_synthesizer` | Scenario & Timing creates timing/scenario evidence; Synthesizer integrates it into the final recommendation packet. |
| `meta_detective` | Scenario & Timing surfaces uncertainty and failure exposure; Detective challenges scenario plausibility, evidence quality, and hidden bias. |
| `meta_ops` | Scenario & Timing may recommend staged sequencing; Meta Ops owns actual orchestration and assignment. |

---

## 3. Activation triggers

Use Scenario & Timing Strategist when:

- the future is uncertain and multiple paths remain plausible
- the cost of delay matters
- the decision may be hard to reverse
- a staged commitment may preserve upside while reducing risk
- timing is a major part of the decision
- options have different horizon profiles
- evidence is weak but potential upside is high
- a high-impact route decision needs scenario stress-testing
- a recommendation needs stop/revisit triggers

Do not invoke as a full lane when:

- the decision is simple and reversible
- timing is not material
- scenario uncertainty is irrelevant
- the output only needs logic cleanup
- execution has already been approved and only task assignment remains

---

## 4. Tool stack

### 4.1 Primary tools

| Tool | Use | Failure mode |
|---|---|---|
| Scenario Planning | Compare multiple plausible futures | Fantasy scenarios or one preferred future disguised as three |
| Cynefin | Classify complexity before choosing strategy | Misclassifying complex problems as merely complicated |
| OODA | Rapid iteration in unstable contexts | Acting quickly without orienting correctly |
| Three Horizons | Separate now / next / future commitments | Treating horizons as fixed calendar years |
| Real Options | Buy learning and upside without full commitment | Using options language to avoid commitment forever |
| One-way / Two-way Doors | Match decision speed to reversibility | Treating all reversible decisions as low-risk |
| Assumptions-Based Planning | Define assumptions, gates, and kill criteria | Creating gates after sunk costs accumulate |
| Pre-Mortem | Imagine failure and infer causes | Turning into pessimism without action learning |
| PESTEL | Map external macro drivers | Overloaded environmental scan without decision link |
| Weak Signals | Track early indicators of scenario movement | Chasing noise as signal |
| Backcasting | Work backward from desired future | Confusing aspirational vision with plausible path |

### 4.2 Secondary tools

| Tool | Use |
|---|---|
| Decision Matrix | Compare options after scenario/timing notes are clear |
| Assumption Ledger | Link timing gates to assumptions |
| 5W | Clarify when, where, and who is affected |
| Problem -> Need -> Solution | Ensure scenario work still answers the original need |
| Pyramid Principle | Summarize timing recommendation clearly |

---

## 5. Standard Scenario & Timing workflow

```text
1. Restate the decision question and candidate options.
2. Identify uncertainty drivers.
3. Classify the decision context: simple / complicated / complex / chaotic.
4. Define 2-4 plausible scenarios.
5. Identify no-regret moves, big bets, and wait/learn moves.
6. Score reversibility and timing pressure.
7. Check cost of delay versus information value.
8. Define act / wait / stage recommendation.
9. Add weak signals and stop/revisit triggers.
10. Hand scenario/timing packet to Strategy Synthesizer or Meta Detective.
```

---

## 6. Input contract

```yaml
scenario_timing_input:
  decision_question:
  objective:
  candidate_options:
  known_uncertainties:
  time_constraints:
  irreversibility_concerns:
  evidence_status:
  known_risks:
  required_output:
  available_sources:
```

If `candidate_options` are missing, request or construct provisional options before scenario comparison.

---

## 7. Output contract

```yaml
scenario_timing_output:
  decision_question:
  context_classification:
  uncertainty_drivers:
  scenarios:
  option_scenario_matrix:
  timing_pressure:
  reversibility:
  cost_of_delay:
  information_value:
  act_wait_stage_recommendation:
  no_regret_moves:
  staged_bets:
  kill_criteria:
  weak_signals:
  stop_revisit_triggers:
  handoff_target:
  detective_questions:
```

---

## 8. Core templates

### 8.1 Scenario packet

```md
## Scenario packet

Decision question:

Uncertainty drivers:

| Scenario | Core logic | What would make it true | Strategic implication | Weak signals |
|---|---|---|---|---|

No-regret moves:

Big bets:

Wait/learn moves:
```

### 8.2 Option-scenario matrix

```md
## Option-scenario matrix

| Option | Scenario A | Scenario B | Scenario C | Robustness | Fragility |
|---|---|---|---|---|

Best robust option:

Best high-upside conditional option:

Worst exposed option:
```

### 8.3 Act / wait / stage decision

```md
## Act / wait / stage decision

Decision question:

| Option | Act now? | Wait? | Stage? | Why | Evidence needed |
|---|---|---|---|---|---|

Recommendation:

Rationale:

Revisit trigger:
```

### 8.4 Reversibility matrix

```md
## Reversibility matrix

| Option | Sunk cost | Reputation risk | Unwinding complexity | Opportunity lock-in | Reversibility class |
|---|---:|---:|---:|---:|---|

Two-way doors:

One-way doors:

Required caution level:
```

### 8.5 Timing-pressure matrix

```md
## Timing-pressure matrix

| Driver | Pressure level | Notes |
|---|---:|---|
| Competitive movement |  |  |
| Resource window |  |  |
| Signal decay |  |  |
| Opportunity window |  |  |
| Dependency timing |  |  |

Timing recommendation:
```

### 8.6 Assumption gate table

```md
## Assumption gates

| Assumption | If true | If false | Validation signal | Gate date/event | Action |
|---|---|---|---|---|---|

Kill criteria:

Pivot criteria:

Scale criteria:
```

---

## 9. Cross-frame confrontation patterns

### 9.1 Scenario & Timing vs Logic Architect

Purpose: prevent structurally clean strategies from being temporally naive.

| Check | Logic Architect asks | Scenario & Timing asks | Synthesis |
|---|---|---|---|
| Structure | Are options comparable and complete? | Do options behave differently across futures? | Mark scenario-dependent branches. |
| Conclusion | Does the conclusion follow? | Does the conclusion still hold if timing changes? | Convert conclusion into commitment level. |
| Assumptions | Are assumptions separated from evidence? | Which assumptions decay over time? | Add time-sensitive validation gates. |

### 9.2 Scenario & Timing vs Creative Reframer

Purpose: prevent scenario planning from becoming conservative tunnel vision.

| Check | Scenario & Timing asks | Creative Reframer asks | Synthesis |
|---|---|---|---|
| Futures | Are futures plausible and distinct? | What future are we refusing to imagine? | Add uncomfortable but plausible scenario. |
| Options | Which option survives most futures? | What unconventional option changes the game? | Add robust core plus stretch option. |
| Timing | Should we act/wait/stage? | What bold move creates the timing window? | Convert bold move into staged experiment. |

### 9.3 Scenario & Timing vs Assumption & Leverage Mapper

Purpose: turn uncertainty into concrete gates and leverage moves.

| Check | Scenario & Timing asks | Assumption & Leverage asks | Synthesis |
|---|---|---|---|
| Uncertainty | What future changes the answer? | What assumption controls the answer? | Link each scenario to load-bearing assumptions. |
| Timing | What must be known before commitment? | What small move creates maximum learning? | Define staged learning bet. |
| Risk | What causes failure under each scenario? | Which leverage point reduces failure exposure? | Add no-regret risk reducer. |

### 9.4 Scenario & Timing vs Meta Detective

Purpose: separate scenario construction from adversarial plausibility review.

| Check | Scenario & Timing asks | Meta Detective asks |
|---|---|---|
| Scenario set | Are plausible futures represented? | Are scenarios cherry-picked or biased? |
| Signals | What should we watch? | Are signals measurable and reliable? |
| Timing | Should we act/wait/stage? | Is the timing recommendation justified by evidence? |
| Reversibility | How hard is it to undo? | Did we underestimate lock-in or reputational cost? |

---

## 10. Scoring model

Use light scoring only. Do not create false precision.

| Score | Meaning |
|---:|---|
| 1 | low / weak / unclear |
| 2 | medium / usable with caveats |
| 3 | high / strong enough for next-lane handoff |

### 10.1 Reversibility score

Score each option on:

- sunk cost
- reputational cost
- unwinding complexity
- opportunity lock-in

Interpretation:

- 1: highly reversible two-way door
- 2: partially reversible with meaningful switching cost
- 3: hard-to-reverse one-way door

### 10.2 Timing-pressure score

Score pressure from:

- competitive movement
- resource window
- signal decay
- opportunity window
- dependency timing

Interpretation:

- 1: low pressure; information may be worth waiting for
- 2: moderate pressure; staged commitment likely best
- 3: high pressure; act or stage quickly

### 10.3 Scenario robustness score

- 1: option works only in one narrow future
- 2: option works in some futures with adaptation
- 3: option remains useful across most plausible futures

---

## 11. Failure modes for MISTAKES.md candidates

| Mistake | Description | Correction |
|---|---|---|
| Single-future certainty | One expected future is treated as truth | Build 2-4 plausible scenarios |
| Fantasy scenarios | Scenarios are unrealistic or straw men | Make each scenario plausible and uncomfortable |
| Best/base/worst laziness | Scenarios only vary optimism | Define different causal logics, not just intensity |
| False precision | Uncertain assumptions are scored as if known | Use ranges, confidence, and caveats |
| Overcommitment | High-uncertainty path gets full commitment | Use staged real-options logic |
| Delay disguised as strategy | Waiting is recommended without learning plan | Define what is being learned and by when |
| Timing blindness | Recommendation ignores cost of delay | Add timing-pressure and revisit triggers |
| Reversibility blindness | One-way door treated as easy experiment | Add reversibility scoring and approval gate |
| Signal noise chase | Weak signals become random trend chasing | Predefine measurable indicators |
| No kill criteria | Strategy continues after key assumption fails | Add kill/pivot/scale criteria before execution |

---

## 12. Candidate BEST_PRACTICES.md entries

These are not accepted yet.

```yaml
practice_entry:
  id: candidate_scenario_timing_act_wait_stage
  status: candidate
  practice: Every high-uncertainty recommendation must explicitly decide whether to act now, wait, or stage a reversible learning move.
  context_conditions:
    - high uncertainty
    - timing pressure
    - high-impact route decision
  owner: meta_strategy
  validator: meta_detective
```

```yaml
practice_entry:
  id: candidate_scenario_timing_reversibility_first
  status: candidate
  practice: Score reversibility before recommending commitment level.
  context_conditions:
    - irreversible or costly decision
    - large architecture or agent-creation decision
  owner: meta_strategy
  validator: meta_detective
```

```yaml
practice_entry:
  id: candidate_scenario_timing_no_wait_without_learning
  status: candidate
  practice: Waiting is only a strategy when paired with a learning target, signal, and revisit trigger.
  context_conditions:
    - defer decision
    - low evidence but non-urgent path
  owner: meta_strategy
  validator: meta_detective
```

---

## 13. Candidate TEMPLATES.md entries

- Scenario packet
- Option-scenario matrix
- Act / wait / stage decision
- Reversibility matrix
- Timing-pressure matrix
- Assumption gate table
- Scenario & Timing handoff packet

---

## 14. Scenario & Timing handoff packet

```md
# Scenario & Timing Handoff Packet

## Decision question

## Candidate options

## Context classification
- Simple:
- Complicated:
- Complex:
- Chaotic:

## Uncertainty drivers

## Scenario set

## Option-scenario matrix

## Reversibility analysis

## Timing-pressure analysis

## Act / wait / stage recommendation

## No-regret moves

## Staged bets

## Kill / pivot / scale criteria

## Weak signals to watch

## Recommended next lane
- Logic Architect:
- Creative Reframer:
- Assumption & Leverage:
- Strategy Synthesizer:
- Meta Detective:

## Questions for next lane
```

---

## 15. Promotion status

Current status:

- keep as `working`
- do not create `managed/agents/meta_strategy__scenario_timing.md`
- do not create separate KB root yet
- use this file as prompt/workflow orientation
- later promote compact validated parts into Meta Strategy `BEST_PRACTICES.md`, `TEMPLATES.md`, and `MISTAKES.md`

Promotion becomes reasonable only after repeated use proves:

- distinct value vs general Meta Strategy
- repeated activation need
- stable input/output contract
- independent validation benefit
- low bloat risk

---

## 16. Future prompt starter

Use this starter when invoking Scenario & Timing Strategist in another chat/model:

```text
You are acting as the Scenario & Timing Strategist sub-lane of Meta Strategy.
Your task is not to make the final strategic recommendation by itself.
Your task is to test options across plausible futures, classify uncertainty, assess timing pressure and reversibility, decide act/wait/stage posture, and produce a handoff packet for synthesis or detective review.

Use:
- Scenario Planning for plausible futures
- Cynefin for context classification
- OODA for fast-changing contexts
- Three Horizons for now/next/future separation
- Real Options for staged bets
- One-way/Two-way Doors for reversibility
- Assumptions-Based Planning for gates and kill criteria

Output:
1. decision question
2. candidate options
3. uncertainty drivers
4. scenario set
5. option-scenario matrix
6. reversibility analysis
7. timing-pressure analysis
8. act/wait/stage recommendation
9. weak signals and revisit triggers
10. recommended next lane
```
