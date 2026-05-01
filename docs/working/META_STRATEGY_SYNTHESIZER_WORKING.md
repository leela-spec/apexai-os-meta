# Meta Strategy Synthesizer Working File

Status: `working`
Parent: `docs/working/META_STRATEGY_ORIENTATION_WORKING.md`
Owner: `meta_strategy`
Sub-lane: `strategy_synthesizer`
Primary validator: `meta_detective`
Created: `2026-05-01`
Purpose: define the Strategy Synthesizer sub-lane for Meta Strategy before any promotion into accepted KB or permanent sub-agent status.

> This file is a working orientation artifact. It is not accepted canon, not a managed agent seed, and not a standalone sub-agent. Promote only validated, compact entries into `managed/agent_kb/meta_strategy/`.

---

## 1. Decision lock

### 1.1 Current decision

`strategy_synthesizer` is an internal Meta Strategy sub-lane / mode, not a permanent sub-agent.

### 1.2 Why it exists

The Strategy Synthesizer prevents multi-frame strategy work from becoming parallel noise.

It catches when strategy outputs:

- collect several framework outputs without resolving conflicts
- average incompatible conclusions
- hide contradictions under vague consensus language
- produce recommendations without a clear option comparison
- omit validation handoffs
- omit execution handoffs
- fail to define stop or revisit triggers
- confuse synthesis with validation
- confuse synthesis with execution planning

### 1.3 Core value

The Strategy Synthesizer converts outputs from strategy sub-lanes into one decision-ready recommendation packet with explicit conflicts, assumptions, validation gates, and handoff targets.

Working formula:

```text
Frame outputs -> conflict ledger -> option comparison -> recommendation packet -> Detective handoff -> Ops handoff
```

---

## 2. Role boundary

### 2.1 Owns

- final cross-frame integration
- contradiction and delta resolution
- synthesis of lane outputs into one recommendation packet
- option comparison consolidation
- decision criteria alignment
- assumption visibility in the final packet
- validation handoff to Meta Detective
- execution handoff brief to Meta Ops
- stop / revisit trigger definition
- recommendation clarity and compactness

### 2.2 Does not own

- generating all raw strategy inputs by itself
- creative option expansion as main lane
- full logical decomposition as main lane
- detailed scenario construction as main lane
- assumption validation as final authority
- execution orchestration
- direct implementation
- KB promotion
- config or managed seed mutation

### 2.3 Boundary with neighboring lanes

| Neighbor | Split |
|---|---|
| `logic_architect` | Logic Architect creates structure and checks coherence; Synthesizer uses that structure to make the final packet readable and comparable. |
| `scenario_timing_strategist` | Scenario & Timing provides timing, reversibility, and scenario logic; Synthesizer integrates those into commitment level and recommendation. |
| `creative_reframer` | Creative Reframer expands frame/options; Synthesizer filters and integrates only useful, testable alternatives. |
| `assumption_leverage_mapper` | Assumption/Leverage ranks assumptions, validation gates, and leverage moves; Synthesizer makes them visible in recommendation and handoff. |
| `meta_detective` | Synthesizer prepares validation questions and unresolved risks; Detective challenges truth, evidence, drift, and plausibility. |
| `meta_ops` | Synthesizer writes the mission brief; Meta Ops owns orchestration, assignment, and execution flow. |

---

## 3. Activation triggers

Use Strategy Synthesizer when:

- two or more strategy lanes produced outputs
- multiple models or chats returned different recommendations
- the user needs one aligned version
- conflicts must be resolved rather than merely listed
- a recommendation packet is needed
- a Strategy -> Detective handoff is needed
- a Strategy -> Meta Ops mission brief is needed
- option comparison must be made executive-readable
- the system risks framework theater, voting theater, or false synthesis

Do not invoke as a full lane when:

- the task only needs raw extraction
- only one simple recommendation exists and no conflict is present
- evidence validation is the main work
- execution assignment is the main work
- creative expansion or logic structuring has not yet happened but is required first

---

## 4. Tool stack

### 4.1 Primary tools

| Tool | Use | Failure mode |
|---|---|---|
| Recommendation Packet | Final output contract | Becoming a long report instead of a decision packet |
| Cross-Frame Confrontation | Compare frames and resolve deltas | Listing conflicts without resolving them |
| Decision Matrix | Compare options by common criteria | False precision or hidden weighting |
| Pyramid Principle | Put recommendation first, then reasons | Over-compressing caveats and evidence gaps |
| Assumption Ledger | Keep final recommendation challengeable | Treating mapped assumptions as validated truth |
| Problem -> Need -> Solution | Ensure recommendation still solves the original need | Substituting solution preference for real need |
| Why -> How -> What | Align purpose, mechanism, and action | Too much purpose language without concrete next step |
| 5W Check | Ensure ownership, timing, place, and process are included | Turning final packet into a checklist dump |
| Strategy -> Detective Handoff | Route high-risk assumptions and contradictions | Asking Detective vague questions |
| Strategy -> Meta Ops Mission Brief | Prepare bounded execution handoff | Accidentally assigning execution inside Strategy |

### 4.2 Secondary tools

| Tool | Use |
|---|---|
| RICE / weighted scoring | Only when criteria are explicit and evidence supports scoring |
| Pre-Mortem summary | Include major failure path if already surfaced |
| OODA / PECR loop | Define revisit/refinement loop when environment is unstable |
| Three Horizons | Preserve now/next/future structure in recommendation |
| 80/20 synthesis | Keep final output compact and focused on critical drivers |

---

## 5. Standard Strategy Synthesizer workflow

```text
1. Restate the decision question and objective.
2. Inventory lane outputs and source/model origins.
3. Extract agreements, conflicts, missing details, and assumptions.
4. Resolve or preserve conflicts explicitly.
5. Normalize options into a shared comparison matrix.
6. Select recommendation posture: act, wait, stage, defer, reject, or validate-first.
7. Write compact recommendation packet.
8. Define what Meta Detective must challenge.
9. Define what Meta Ops should coordinate if accepted.
10. Add stop/revisit trigger and unresolved questions.
```

---

## 6. Input contract

```yaml
strategy_synthesizer_input:
  decision_question:
  objective:
  constraints:
  lane_outputs:
    logic_architect:
    scenario_timing_strategist:
    creative_reframer:
    assumption_leverage_mapper:
    other_sources:
  candidate_options:
  known_conflicts:
  evidence_status:
  required_output:
```

If `lane_outputs` are missing, the Synthesizer should not fabricate them. It should either synthesize available inputs with caveats or route to the missing lane first.

---

## 7. Output contract

```yaml
strategy_synthesizer_output:
  decision_question:
  objective:
  source_outputs_used:
  agreements:
  conflicts:
  resolved_conflicts:
  unresolved_conflicts:
  option_comparison:
  recommendation:
  rationale:
  assumptions:
  validation_handoff:
  ops_handoff:
  stop_revisit_trigger:
  residual_risks:
  next_action:
```

---

## 8. Core templates

### 8.1 Cross-frame synthesis ledger

```md
## Cross-frame synthesis ledger

Decision question:

| Frame / lane | Main output | Key assumption | Useful contribution | Conflict introduced |
|---|---|---|---|---|
| Logic Architect | | | | |
| Scenario & Timing | | | | |
| Creative Reframer | | | | |
| Assumption & Leverage | | | | |

Agreements:

Conflicts:

Missing details:

Resolution:
```

### 8.2 Conflict resolution table

```md
## Conflict resolution table

| Conflict | Source A | Source B | Why it matters | Resolution | Residual risk |
|---|---|---|---|---|---|

Conflicts requiring Detective:
```

### 8.3 Final option comparison

```md
## Final option comparison

| Option | Upside | Risk | Cost | Evidence | Reversibility | Timing | Leverage | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|

Preferred option:

Second-best option:

Rejected options and why:
```

### 8.4 Recommendation packet

```md
# Meta Strategy Recommendation Packet

## 1. Decision question

## 2. Recommendation

## 3. Why this recommendation

## 4. Options considered

## 5. Key assumptions

## 6. Risks and mitigations

## 7. Timing / reversibility posture

## 8. Validation handoff to Meta Detective

## 9. Execution handoff to Meta Ops

## 10. Stop / revisit trigger
```

### 8.5 Strategy -> Detective handoff

```md
# Strategy -> Detective Handoff

## Recommendation under challenge

## Highest-risk assumptions

## Conflicts that were resolved by Strategy

## Conflicts left unresolved

## Evidence gaps

## Second-best option and why it lost

## Questions for Detective

## Requested output from Detective
- contradiction findings:
- evidence concerns:
- severity:
- validation gates:
```

### 8.6 Strategy -> Meta Ops mission brief

```md
# Strategy -> Meta Ops Mission Brief

## Objective

## Recommended path

## Constraints

## Required lanes / agents

## Proposed sequence

## Success criteria

## Risks to monitor

## Stop conditions

## Operator decision needed?
```

---

## 9. Cross-frame confrontation patterns

### 9.1 Synthesizer vs Logic Architect

Purpose: preserve clarity without flattening meaningful complexity.

| Check | Logic Architect asks | Synthesizer asks | Synthesis |
|---|---|---|---|
| Structure | Is the reasoning coherent? | Is the final packet decision-ready? | Keep structure, remove unnecessary detail. |
| Evidence | Are claims separated from assumptions? | Which assumptions must be visible in the final answer? | Include only load-bearing assumptions. |
| Output | Does the conclusion follow? | Does the recommendation answer the user's decision? | Convert logic into recommendation packet. |

### 9.2 Synthesizer vs Scenario & Timing Strategist

Purpose: convert uncertainty into commitment posture.

| Check | Scenario & Timing asks | Synthesizer asks | Synthesis |
|---|---|---|---|
| Scenarios | Which futures change the answer? | What recommendation survives enough futures? | Choose robust path or conditional bet. |
| Timing | Act, wait, or stage? | How should that be stated in the final packet? | Add timing/reversibility posture. |
| Signals | What should we watch? | Which signals become stop/revisit triggers? | Add trigger section. |

### 9.3 Synthesizer vs Creative Reframer

Purpose: retain useful novelty without adding noise.

| Check | Creative Reframer asks | Synthesizer asks | Synthesis |
|---|---|---|---|
| Option space | What new option exists? | Is it distinct, relevant, and testable? | Include, stage, or discard. |
| Frame | What did the old frame hide? | Does the new frame alter the recommendation? | Mention only if decision-changing. |
| Stretch idea | What bold move exists? | Can it become a bounded bet? | Convert to staged option or learning queue. |

### 9.4 Synthesizer vs Assumption & Leverage Mapper

Purpose: keep final packet challengeable and high-leverage.

| Check | Assumption & Leverage asks | Synthesizer asks | Synthesis |
|---|---|---|---|
| Assumptions | What must be true? | Which assumptions must the user see? | Include top load-bearing assumptions. |
| Leverage | What small move matters most? | Does it change the recommendation? | Include as no-regret move or first step. |
| Gates | What should be validated? | Who validates and before what commitment? | Route to Detective or Ops gate. |

### 9.5 Synthesizer vs Meta Detective

Purpose: keep synthesis separate from validation.

| Check | Synthesizer asks | Meta Detective asks |
|---|---|---|
| Coherence | Is there one usable recommendation? | Is it true enough and safe enough? |
| Conflicts | Were conflicts resolved transparently? | Were conflicts resolved incorrectly or prematurely? |
| Evidence gaps | What gaps remain? | Which gaps invalidate the recommendation? |
| Handoff | What should be challenged? | What severity and validation gates apply? |

---

## 10. Scoring model

Use light scoring only. Do not create false precision.

| Score | Meaning |
|---:|---|
| 1 | weak / unresolved / not ready |
| 2 | usable with caveats or validation |
| 3 | strong enough for Detective or Ops handoff |

### 10.1 Synthesis readiness score

- 1: lane outputs conflict too much or are incomplete
- 2: recommendation possible with explicit caveats
- 3: ready for Detective review or Ops handoff

### 10.2 Conflict resolution score

- 1: major conflicts unresolved
- 2: conflicts resolved but need Detective review
- 3: conflicts resolved and transparent

### 10.3 Recommendation clarity score

- 1: output is a report, not a decision
- 2: recommendation exists but caveats are messy
- 3: answer, rationale, risks, and handoffs are clear

### 10.4 Handoff readiness score

- 1: no clear next owner
- 2: next owner exists but task is vague
- 3: Detective/Ops handoff is bounded and actionable

---

## 11. Failure modes for MISTAKES.md candidates

| Mistake | Description | Correction |
|---|---|---|
| False synthesis | Conflicting outputs are smoothed over instead of resolved | Use conflict resolution table |
| Aggregation theater | Several outputs are pasted together without integration | Produce one recommendation packet |
| Voting theater | Majority view wins without evidence criteria | Compare by criteria and assumptions, not votes |
| Missing second-best option | Recommendation hides the nearest alternative | Include second-best and why it lost |
| Caveat burial | Major risks are hidden at the end | Surface key assumptions and risks in final packet |
| Validation bypass | Synthesizer treats coherence as proof | Route high-risk assumptions to Meta Detective |
| Ops bleed | Synthesizer starts assigning work directly | Write mission brief; Meta Ops orchestrates |
| Recommendation fog | Final answer is too broad to act on | State act/wait/stage/defer/reject/validate-first posture |
| Triggerless strategy | No stop or revisit condition is defined | Add stop/revisit trigger |

---

## 12. Candidate BEST_PRACTICES.md entries

These are not accepted yet.

```yaml
practice_entry:
  id: candidate_strategy_synthesizer_conflict_before_recommendation
  status: candidate
  practice: Resolve or explicitly preserve cross-frame conflicts before issuing a final recommendation.
  context_conditions:
    - multiple lane outputs
    - multi-model disagreement
    - high-impact recommendation
  owner: meta_strategy
  validator: meta_detective
```

```yaml
practice_entry:
  id: candidate_strategy_synthesizer_second_best_visible
  status: candidate
  practice: Every high-impact recommendation should name the second-best option and why it lost.
  context_conditions:
    - option comparison
    - route decision
    - high uncertainty
  owner: meta_strategy
  validator: meta_detective
```

```yaml
practice_entry:
  id: candidate_strategy_synthesizer_handoff_required
  status: candidate
  practice: Final recommendation packets must include Detective validation handoff and Ops mission brief when risk or execution follow-up exists.
  context_conditions:
    - high-risk recommendation
    - execution likely after approval
  owner: meta_strategy
  validator: meta_detective
```

---

## 13. Candidate TEMPLATES.md entries

- Cross-frame synthesis ledger
- Conflict resolution table
- Final option comparison
- Recommendation packet
- Strategy -> Detective handoff
- Strategy -> Meta Ops mission brief
- Strategy Synthesizer handoff packet

---

## 14. Strategy Synthesizer handoff packet

```md
# Strategy Synthesizer Handoff Packet

## Decision question

## Source outputs used

## Agreements

## Conflicts and resolution

## Final option comparison

## Recommendation

## Why this recommendation

## Second-best option and why it lost

## Key assumptions

## Residual risks

## Validation handoff to Meta Detective

## Execution handoff to Meta Ops

## Stop / revisit trigger

## Next action
```

---

## 15. Promotion status

Current status:

- keep as `working`
- do not create `managed/agents/meta_strategy__synthesizer.md`
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

Use this starter when invoking Strategy Synthesizer in another chat/model:

```text
You are acting as the Strategy Synthesizer sub-lane of Meta Strategy.
Your task is not to generate all raw strategy inputs, validate truth by yourself, or orchestrate execution.
Your task is to integrate strategy lane outputs into one decision-ready recommendation packet. Resolve or explicitly preserve conflicts, compare options using shared criteria, name the second-best option, surface assumptions, route high-risk assumptions to Meta Detective, and prepare a bounded Meta Ops mission brief if execution may follow.

Use:
- Cross-frame synthesis ledger to inventory lane outputs
- Conflict resolution table to handle disagreements
- Decision matrix to compare options
- Recommendation packet for final output
- Strategy -> Detective handoff for validation
- Strategy -> Meta Ops mission brief for execution coordination

Output:
1. decision question
2. source outputs used
3. agreements and conflicts
4. conflict resolutions
5. final option comparison
6. recommendation and rationale
7. second-best option and why it lost
8. key assumptions and residual risks
9. Detective validation handoff
10. Meta Ops mission brief
11. stop/revisit trigger
```
