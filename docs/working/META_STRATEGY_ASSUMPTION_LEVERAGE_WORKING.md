# Meta Strategy Assumption & Leverage Mapper Working File

Status: `working`
Parent: `docs/working/META_STRATEGY_ORIENTATION_WORKING.md`
Owner: `meta_strategy`
Sub-lane: `assumption_leverage_mapper`
Primary validator: `meta_detective`
Created: `2026-05-01`
Purpose: define the Assumption & Leverage Mapper sub-lane for Meta Strategy before any promotion into accepted KB or permanent sub-agent status.

> This file is a working orientation artifact. It is not accepted canon, not a managed agent seed, and not a standalone sub-agent. Promote only validated, compact entries into `managed/agent_kb/meta_strategy/`.

---

## 1. Decision lock

### 1.1 Current decision

`assumption_leverage_mapper` is an internal Meta Strategy sub-lane / mode, not a permanent sub-agent.

### 1.2 Why it exists

The Assumption & Leverage Mapper prevents strategic recommendations from hiding the true sources of risk and value.

It catches when strategy outputs:

- treat assumptions as facts
- fail to identify load-bearing beliefs
- miss the small move that changes the whole system
- focus on big visible work instead of high-leverage intervention
- ignore what must be true for the strategy to work
- recommend commitment without kill/pivot/scale criteria
- confuse effort, leverage, and impact
- fail to define what should be validated next

### 1.3 Core value

The Assumption & Leverage Mapper converts a strategy into a ranked map of what must be true, what matters most, what can break the plan, and which small interventions create disproportionate value.

Working formula:

```text
Recommendation/options -> load-bearing assumptions -> leverage points -> validation gates -> risk-reducing moves -> handoff
```

---

## 2. Role boundary

### 2.1 Owns

- assumption extraction
- claim/fact/assumption/unknown separation
- load-bearing assumption ranking
- leverage-point identification
- bottleneck and constraint mapping
- effort-to-impact comparison
- 80/20 driver identification
- validation gate proposal
- kill / pivot / scale criteria draft
- dependency and fragility notes
- handoff questions for Meta Detective

### 2.2 Does not own

- final strategic recommendation by itself
- full adversarial validation
- final evidence verification
- execution assignment
- detailed market research
- full scenario construction as main lane
- creative option generation as main lane
- KB promotion
- config or managed seed mutation

### 2.3 Boundary with neighboring lanes

| Neighbor | Split |
|---|---|
| `logic_architect` | Logic Architect separates claims and builds structure; Assumption/Leverage ranks which assumptions and drivers matter most. |
| `scenario_timing_strategist` | Scenario & Timing maps futures and timing; Assumption/Leverage turns scenario-sensitive beliefs into validation gates and leverage moves. |
| `creative_reframer` | Creative Reframer reveals hidden frames and options; Assumption/Leverage identifies which new assumptions and leverage points those options introduce. |
| `strategy_synthesizer` | Assumption/Leverage provides ranked risks, gates, and leverage moves; Synthesizer integrates them into the final recommendation packet. |
| `meta_detective` | Assumption/Leverage identifies what should be challenged; Detective tests whether assumptions/evidence are trustworthy. |
| `meta_ops` | Assumption/Leverage may recommend validation gates; Meta Ops coordinates actual execution if approved. |

---

## 3. Activation triggers

Use Assumption & Leverage Mapper when:

- a recommendation depends on weak or implicit assumptions
- a decision has high upside but uncertain evidence
- the system needs to know what to validate first
- multiple options differ mainly by risk or dependencies
- a plan feels large but the true leverage point may be small
- there is a risk of overbuilding
- the user asks for impact ranking, 80/20, leverage, bottlenecks, constraints, or validation gates
- a strategy needs kill, pivot, or scale criteria
- different frame outputs disagree and the core assumption behind the disagreement must be found

Do not invoke as a full lane when:

- evidence validation is the main task, not assumption mapping
- the recommendation is simple and low-risk
- the only need is creative expansion
- the problem has not yet been structured enough to identify claims/options
- execution has already been approved and only assignment remains

---

## 4. Tool stack

### 4.1 Primary tools

| Tool | Use | Failure mode |
|---|---|---|
| Assumption Ledger | Separate known facts, assumptions, unknowns, and bets | Listing too many assumptions without ranking |
| Load-bearing Assumption Ranking | Identify assumptions that break the plan if false | Ranking by fear instead of strategic dependency |
| 5 Whys | Drill from symptom to cause | Asking why mechanically without new insight |
| Root Cause Analysis | Identify causal drivers behind a problem | Treating one cause as the whole system |
| Ladder of Inference | Trace jumps from data to belief | Becoming a full Detective review instead of a map |
| 80/20 Analysis | Identify the few drivers causing most impact | Overlooking rare but fatal risks |
| Leverage Points | Find small interventions with large downstream effect | Calling everything a leverage point |
| Constraint / Bottleneck Mapping | Find what limits system output | Mistaking local bottleneck for global bottleneck |
| Dependency Mapping | Identify what must exist before an option works | Overloading the map with low-value dependencies |
| Kill / Pivot / Scale Criteria | Predefine decision gates | Setting gates after commitment already happened |

### 4.2 Secondary tools

| Tool | Use |
|---|---|
| Decision Matrix | Compare options after assumptions and leverage are clear |
| Scenario Planning | Check whether assumptions differ by scenario |
| Pre-Mortem | Generate candidate failure assumptions; Detective owns deeper challenge |
| Problem -> Need -> Solution | Ensure assumptions relate to the real need |
| Pyramid Principle | Summarize ranked assumptions and leverage clearly |

---

## 5. Standard Assumption & Leverage workflow

```text
1. Restate the decision question and candidate recommendation/options.
2. Extract explicit and implicit assumptions.
3. Separate facts, assumptions, unknowns, bets, and dependencies.
4. Identify load-bearing assumptions.
5. Rank assumptions by impact if false and uncertainty level.
6. Identify constraints, bottlenecks, and leverage points.
7. Define the smallest validation moves.
8. Draft kill / pivot / scale criteria.
9. Produce Detective handoff questions.
10. Hand ranked map to Strategy Synthesizer or Meta Detective.
```

---

## 6. Input contract

```yaml
assumption_leverage_input:
  decision_question:
  candidate_recommendation:
  candidate_options:
  known_facts:
  known_assumptions:
  known_unknowns:
  known_dependencies:
  constraints:
  known_risks:
  required_output:
```

If `candidate_recommendation` is missing, map assumptions by option instead.

---

## 7. Output contract

```yaml
assumption_leverage_output:
  decision_question:
  option_or_recommendation_under_review:
  fact_assumption_unknown_split:
  load_bearing_assumptions:
  assumption_rankings:
  dependencies:
  bottlenecks:
  leverage_points:
  validation_moves:
  kill_criteria:
  pivot_criteria:
  scale_criteria:
  residual_risks:
  handoff_target:
  detective_questions:
```

---

## 8. Core templates

### 8.1 Fact / assumption / unknown split

```md
## Fact / assumption / unknown split

Decision question:

| Statement | Type | Why classified this way | Confidence | Needed validation |
|---|---|---|---:|---|
|  | Fact / Assumption / Unknown / Bet / Dependency |  |  |  |

Most dangerous misclassification:
```

### 8.2 Load-bearing assumption ledger

```md
## Load-bearing assumption ledger

| Assumption | What depends on it | If false | Impact | Uncertainty | Priority |
|---|---|---|---:|---:|---:|

Top 3 assumptions to validate:
1.
2.
3.
```

### 8.3 Leverage map

```md
## Leverage map

Decision context:

| Leverage point | Mechanism | Effort | Expected impact | Confidence | Risk |
|---|---|---:|---:|---:|---:|

Highest leverage move:

Why it matters:

What could make it fail:
```

### 8.4 Bottleneck / constraint map

```md
## Bottleneck / constraint map

Current goal:

| Constraint | Type | What it limits | Workaround | Owner / next lane |
|---|---|---|---|---|
|  | Resource / Knowledge / Time / Authority / Technical / Trust |  |  |  |

True bottleneck:

False bottlenecks:
```

### 8.5 Validation gate table

```md
## Validation gates

| Gate | Assumption tested | Signal | Pass action | Fail action | Deadline / trigger |
|---|---|---|---|---|---|

Kill criteria:

Pivot criteria:

Scale criteria:
```

### 8.6 80/20 driver map

```md
## 80/20 driver map

Goal:

| Driver | Estimated contribution | Evidence | Confidence | Action |
|---|---:|---|---:|---|

Critical few:

Useful many:

Discard / defer:
```

---

## 9. Cross-frame confrontation patterns

### 9.1 Assumption & Leverage vs Logic Architect

Purpose: prevent clean logic from hiding fragile assumptions.

| Check | Logic Architect asks | Assumption & Leverage asks | Synthesis |
|---|---|---|---|
| Claims | Are claims separated from evidence? | Which claims rely on weak assumptions? | Mark load-bearing assumptions under key claims. |
| Tree | Is the issue tree complete? | Which branch controls most of the outcome? | Add 80/20 driver ranking. |
| Coherence | Does the conclusion follow? | What must be true for it to work? | Add validation gates before synthesis. |

### 9.2 Assumption & Leverage vs Scenario & Timing Strategist

Purpose: connect assumptions to futures and commitment timing.

| Check | Scenario & Timing asks | Assumption & Leverage asks | Synthesis |
|---|---|---|---|
| Futures | Which future changes the answer? | Which assumption makes that future matter? | Link scenario shifts to assumption gates. |
| Timing | Should we act/wait/stage? | What smallest test reduces uncertainty? | Use staged validation moves. |
| Reversibility | What is hard to undo? | Which assumption justifies irreversible commitment? | Require Detective review before one-way door. |

### 9.3 Assumption & Leverage vs Creative Reframer

Purpose: convert creative alternatives into testable strategy.

| Check | Creative Reframer asks | Assumption & Leverage asks | Synthesis |
|---|---|---|---|
| New frame | What hidden possibility appears? | What new assumption does this introduce? | Add to assumption ledger. |
| Stretch option | What bold path could work? | What small test proves viability? | Convert into bounded experiment. |
| Constraint | What if constraint becomes lever? | Is the constraint movable and high-impact? | Rank leverage and validation priority. |

### 9.4 Assumption & Leverage vs Meta Detective

Purpose: separate assumption mapping from adversarial validation.

| Check | Assumption & Leverage asks | Meta Detective asks |
|---|---|---|
| Assumption list | What must be true? | Is the assumption actually supported or contradicted? |
| Priority | Which assumption matters most? | Did Strategy under-rank a dangerous assumption? |
| Leverage | What small move has high impact? | Is the claimed leverage plausible? |
| Gates | What should be validated? | Are the signals reliable and sufficient? |

---

## 10. Scoring model

Use light scoring only. Do not create false precision.

| Score | Meaning |
|---:|---|
| 1 | low / weak / unclear |
| 2 | medium / usable with caveats |
| 3 | high / strong enough for next-lane handoff |

### 10.1 Assumption criticality score

- 1: minor if false
- 2: would require meaningful adjustment
- 3: breaks the recommendation if false

### 10.2 Assumption uncertainty score

- 1: well supported
- 2: partially supported or context-dependent
- 3: weakly supported or unknown

### 10.3 Validation priority score

Use the combination of criticality and uncertainty.

- 1: monitor only
- 2: validate before scaling
- 3: validate before commitment

### 10.4 Leverage score

- 1: low impact relative to effort
- 2: meaningful but bounded value
- 3: disproportionate downstream value

---

## 11. Failure modes for MISTAKES.md candidates

| Mistake | Description | Correction |
|---|---|---|
| Assumption laundering | Assumptions are written as if they were facts | Classify statements explicitly |
| Unranked assumption dump | Many assumptions listed but no priority | Rank by criticality and uncertainty |
| Fake leverage | A big task is called high-leverage because it feels important | Score effort vs downstream impact |
| Validation after commitment | Gates are defined after execution begins | Define gates before handoff to Meta Ops |
| Ignored dependency | Plan depends on unstated external condition | Add dependency map |
| 80/20 overreach | Critical edge risks are discarded as low-frequency | Preserve fatal risks for Detective review |
| Weak signal confusion | Any interesting data point becomes validation | Define measurable pass/fail signals |
| No kill criteria | Strategy cannot stop after assumption failure | Add kill/pivot/scale criteria |
| Detective bypass | Strategy maps assumptions and treats that as validation | Route high-risk assumptions to Detective |

---

## 12. Candidate BEST_PRACTICES.md entries

These are not accepted yet.

```yaml
practice_entry:
  id: candidate_assumption_leverage_classify_before_recommend
  status: candidate
  practice: Classify statements as facts, assumptions, unknowns, bets, or dependencies before final recommendation.
  context_conditions:
    - high-impact recommendation
    - weak evidence
    - multi-agent disagreement
  owner: meta_strategy
  validator: meta_detective
```

```yaml
practice_entry:
  id: candidate_assumption_leverage_rank_load_bearing
  status: candidate
  practice: Rank assumptions by criticality and uncertainty, not by salience or fear.
  context_conditions:
    - recommendation depends on assumptions
    - validation budget is limited
  owner: meta_strategy
  validator: meta_detective
```

```yaml
practice_entry:
  id: candidate_assumption_leverage_validate_before_commit
  status: candidate
  practice: Define validation gates and kill/pivot/scale criteria before handing a high-risk recommendation to Meta Ops.
  context_conditions:
    - staged decision
    - irreversible or expensive commitment
  owner: meta_strategy
  validator: meta_detective
```

---

## 13. Candidate TEMPLATES.md entries

- Fact / assumption / unknown split
- Load-bearing assumption ledger
- Leverage map
- Bottleneck / constraint map
- Validation gate table
- 80/20 driver map
- Assumption & Leverage handoff packet

---

## 14. Assumption & Leverage handoff packet

```md
# Assumption & Leverage Handoff Packet

## Decision question

## Option / recommendation under review

## Fact / assumption / unknown split

## Load-bearing assumptions

## Top validation priorities

## Leverage points

## Bottlenecks / constraints

## Dependencies

## Validation gates

## Kill / pivot / scale criteria

## Residual risks

## Recommended next lane
- Logic Architect:
- Scenario & Timing:
- Creative Reframer:
- Strategy Synthesizer:
- Meta Detective:
- Meta Ops:

## Questions for next lane
```

---

## 15. Promotion status

Current status:

- keep as `working`
- do not create `managed/agents/meta_strategy__assumption_leverage.md`
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

Use this starter when invoking Assumption & Leverage Mapper in another chat/model:

```text
You are acting as the Assumption & Leverage Mapper sub-lane of Meta Strategy.
Your task is not to make the final strategic recommendation and not to validate truth by yourself.
Your task is to extract facts, assumptions, unknowns, bets, and dependencies; identify load-bearing assumptions; rank assumptions by criticality and uncertainty; identify leverage points and bottlenecks; define validation gates; and produce a handoff packet for synthesis or detective review.

Use:
- Assumption Ledger to classify statements
- Load-bearing Assumption Ranking to prioritize validation
- 5 Whys / Root Cause Analysis to find deeper drivers
- Ladder of Inference to identify jumps from facts to beliefs
- 80/20 Analysis to find critical drivers
- Leverage Points to identify disproportionate moves
- Validation Gates for kill/pivot/scale criteria

Output:
1. decision question
2. option/recommendation under review
3. fact/assumption/unknown split
4. load-bearing assumption ledger
5. top validation priorities
6. leverage map
7. bottleneck/dependency map
8. validation gates and kill/pivot/scale criteria
9. residual risks
10. recommended next lane
```
