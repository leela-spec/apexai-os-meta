# Meta Strategy Creative Reframer Working File

Status: `working`
Parent: `docs/working/META_STRATEGY_ORIENTATION_WORKING.md`
Owner: `meta_strategy`
Sub-lane: `creative_reframer`
Primary validator: `meta_detective`
Created: `2026-05-01`
Purpose: define the Creative Reframer sub-lane for Meta Strategy before any promotion into accepted KB or permanent sub-agent status.

> This file is a working orientation artifact. It is not accepted canon, not a managed agent seed, and not a standalone sub-agent. Promote only validated, compact entries into `managed/agent_kb/meta_strategy/`.

---

## 1. Decision lock

### 1.1 Current decision

`creative_reframer` is an internal Meta Strategy sub-lane / mode, not a permanent sub-agent.

### 1.2 Why it exists

The Creative Reframer prevents strategic outputs from becoming:

- trapped in the first frame
- over-optimized around local constraints
- too conservative too early
- blind to stakeholder perspectives
- narrow because of model monoculture
- correct inside the wrong problem definition
- logical but strategically unimaginative

### 1.3 Core value

The Creative Reframer expands and challenges the frame before commitment. It creates alternative lenses, roles, metaphors, stakeholder views, and option classes that the Logic Architect and Scenario & Timing Strategist can later structure and test.

Working formula:

```text
Current frame -> perspective shift -> alternative frames -> expanded option space -> stretch options -> handoff for structure and validation
```

---

## 2. Role boundary

### 2.1 Owns

- reframing the problem definition
- perspective switching
- stakeholder-lens generation
- creative option expansion
- role-based thinking passes
- value-innovation prompts
- analogy and metaphor generation when useful
- identifying excluded possibilities
- generating stretch options and non-obvious alternatives
- surfacing frame risks and hidden constraints

### 2.2 Does not own

- final recommendation by itself
- execution sequencing
- adversarial validation
- evidence verification
- detailed scenario/timing scoring
- final logical decomposition
- KB promotion
- config or managed seed mutation

### 2.3 Boundary with neighboring lanes

| Neighbor | Split |
|---|---|
| `logic_architect` | Creative Reframer expands or breaks the frame; Logic Architect cleans, decomposes, and tests structural coherence. |
| `scenario_timing_strategist` | Creative Reframer generates unconventional futures/options; Scenario & Timing checks plausibility, timing, and reversibility. |
| `assumption_leverage_mapper` | Creative Reframer reveals hidden assumptions by changing perspective; Assumption/Leverage ranks which assumptions and leverage points matter. |
| `strategy_synthesizer` | Creative Reframer supplies expanded options and frame risks; Synthesizer integrates only the useful options into the recommendation packet. |
| `meta_detective` | Creative Reframer challenges imagination boundaries; Detective challenges truth, plausibility, and bias. |

---

## 3. Activation triggers

Use Creative Reframer when:

- the option space is too narrow
- all options look like variants of the same idea
- the current frame may be wrong
- a strategy feels logically clean but strategically weak
- stakeholders likely see the problem differently
- the task asks for innovation, positioning, differentiation, or new paths
- a deadlock exists between two obvious options
- the system needs redundancy against one-model or one-frame bias

Do not invoke as a full lane when:

- the decision is already overloaded with options
- the task needs verification, not expansion
- the problem is simple and execution-ready
- the key failure is logical inconsistency rather than narrow framing
- creative divergence would create more noise than value

---

## 4. Tool stack

### 4.1 Primary tools

| Tool | Use | Failure mode |
|---|---|---|
| Six Thinking Hats | Separate data, emotion, risk, upside, creativity, and process perspectives | Treating hats as performance theater without changing output |
| Disney Method | Dreamer -> Realist -> Critic role cycling | Staying in Dreamer mode and skipping feasibility |
| Reframing Matrix | View the problem from multiple stakeholder or functional lenses | Picking shallow lenses that do not change the decision |
| Blue Ocean / ERRC | Eliminate, Reduce, Raise, Create value dimensions | Creating a lonely ocean with no real demand |
| Analogical Reasoning | Borrow patterns from other domains | Copying analogy blindly without checking fit |
| Inversion | Ask how to make the strategy fail or become impossible | Becoming pessimistic rather than generative |
| Constraint Reversal | Treat a constraint as a design lever | Ignoring real constraints entirely |
| Stakeholder Role Swap | Ask how each stakeholder would define success or risk | Confusing empathy with evidence |

### 4.2 Secondary tools

| Tool | Use |
|---|---|
| First Principles | Break inherited assumptions before creative rebuild |
| 5W | Ensure reframes include ownership and context |
| Problem -> Need -> Solution | Check whether new frames still solve the real need |
| Scenario Planning | Turn reframes into plausible futures for timing review |
| Pre-Mortem | Lightly test if the creative option has obvious fatal flaws; deeper version belongs to Detective |

---

## 5. Standard Creative Reframer workflow

```text
1. Restate the current decision question and current dominant frame.
2. Identify what the current frame assumes or excludes.
3. Run 2-4 perspective shifts.
4. Generate alternative problem framings.
5. Generate option classes under each frame.
6. Mark which options are conventional, stretch, or radical.
7. Identify frame risks and hidden constraints.
8. Select the few reframes worth structuring.
9. Hand off to Logic Architect, Scenario & Timing, or Strategy Synthesizer.
```

---

## 6. Input contract

```yaml
creative_reframer_input:
  decision_question:
  current_frame:
  objective:
  constraints:
  candidate_options:
  known_stakeholders:
  known_risks:
  desired_creativity_level: conservative | moderate | radical
  required_output:
```

If `current_frame` is missing, infer and label the likely implicit frame before generating alternatives.

---

## 7. Output contract

```yaml
creative_reframer_output:
  decision_question:
  current_frame:
  frame_assumptions:
  excluded_possibilities:
  alternative_frames:
  stakeholder_lenses:
  option_expansion:
  conventional_options:
  stretch_options:
  radical_options:
  frame_risks:
  options_to_structure:
  handoff_target:
  detective_questions:
```

---

## 8. Core templates

### 8.1 Frame audit

```md
## Frame audit

Decision question:

Current frame:

What this frame makes easy to see:

What this frame hides:

Implicit assumptions:

Excluded options:

Frame risk:
```

### 8.2 Reframing matrix

```md
## Reframing matrix

| Lens | How this lens defines the problem | New option it reveals | Risk it notices |
|---|---|---|---|
| User / customer | | | |
| Operator / execution | | | |
| System / architecture | | | |
| Economics / resources | | | |
| Future / uncertainty | | | |
```

### 8.3 Six Thinking Hats pass

```md
## Six Thinking Hats pass

| Hat | Question | Output |
|---|---|---|
| White - data | What do we know / not know? | |
| Red - feeling | What emotional or trust signal matters? | |
| Black - risk | What could go wrong? | |
| Yellow - upside | What could work unusually well? | |
| Green - creativity | What new option exists? | |
| Blue - process | What should happen next? | |
```

### 8.4 Disney Method pass

```md
## Disney Method pass

Dreamer:
- bold possibility:
- no-constraint version:

Realist:
- practical version:
- needed steps/resources:

Critic:
- weakest part:
- validation needed:

Synthesized option:
```

### 8.5 Blue Ocean / ERRC map

```md
## Blue Ocean / ERRC map

Decision context:

| Eliminate | Reduce | Raise | Create |
|---|---|---|---|
| | | | |

Resulting option:

Demand risk:

Evidence needed:
```

### 8.6 Stretch-option ledger

```md
## Stretch-option ledger

| Option | Frame that produced it | Upside | Constraint violated | How to make it testable |
|---|---|---:|---|---|

Options worth structuring:

Options to discard:
```

---

## 9. Cross-frame confrontation patterns

### 9.1 Creative Reframer vs Logic Architect

Purpose: prevent logical rigidity and creative incoherence.

| Check | Creative Reframer asks | Logic Architect asks | Synthesis |
|---|---|---|---|
| Frame | What does the current frame hide? | Is the new frame coherent? | Keep useful reframe, define boundaries. |
| Options | What option is missing? | Does it overlap with existing options? | Add if distinct; merge if duplicate. |
| Structure | Can we see the problem differently? | Can we compare options fairly? | Turn reframe into option tree. |

### 9.2 Creative Reframer vs Scenario & Timing Strategist

Purpose: prevent imagination from ignoring plausibility and timing.

| Check | Creative Reframer asks | Scenario & Timing asks | Synthesis |
|---|---|---|---|
| Possibility | What bold path exists? | Under what future does it work? | Convert to conditional bet. |
| Constraint | What if the constraint became a lever? | Is the lever reversible or time-sensitive? | Make staged experiment. |
| Future | What future are we not imagining? | Is it plausible and watchable? | Add scenario only if signals exist. |

### 9.3 Creative Reframer vs Assumption & Leverage Mapper

Purpose: convert new frames into concrete assumptions and leverage points.

| Check | Creative Reframer asks | Assumption & Leverage asks | Synthesis |
|---|---|---|---|
| Hidden belief | What assumption appears only under this frame? | Is it load-bearing? | Add to assumption ledger. |
| Leverage | What small change unlocks a new option? | How much leverage does it create? | Rank as no-regret, bet, or discard. |
| Risk | What did the old frame miss? | Which risk/assumption matters most? | Mark for Detective if severe. |

### 9.4 Creative Reframer vs Meta Detective

Purpose: separate imaginative expansion from adversarial validation.

| Check | Creative Reframer asks | Meta Detective asks |
|---|---|---|
| New frame | What else could be true? | Is there evidence or only imagination? |
| Stakeholder lens | Who sees the problem differently? | Is that stakeholder model accurate? |
| Stretch option | What bold option exists? | What would falsify its viability? |
| Constraint reversal | What if constraint becomes lever? | Is the constraint actually movable? |

---

## 10. Scoring model

Use light scoring only. Do not create false precision.

| Score | Meaning |
|---:|---|
| 1 | weak / likely noise |
| 2 | usable with structure and validation |
| 3 | strong candidate for next-lane handoff |

### 10.1 Novelty score

- 1: same option with new wording
- 2: genuinely different frame but needs structure
- 3: new path or option class

### 10.2 Relevance score

- 1: creative but off-target
- 2: related but needs adaptation
- 3: directly improves the decision space

### 10.3 Testability score

- 1: cannot be validated or staged
- 2: testable with extra design
- 3: can become a bounded experiment or decision option

---

## 11. Failure modes for MISTAKES.md candidates

| Mistake | Description | Correction |
|---|---|---|
| Creativity theater | Many reframes are listed but none change the decision | Keep only reframes that reveal new options or risks |
| False novelty | Same option renamed as innovation | Require distinct mechanism or option class |
| Constraint denial | Creative path ignores real constraints | Mark violated constraints and make testable version |
| Stakeholder cosplay | Assumed stakeholder view without evidence | Route to Detective or research validation |
| Lonely ocean | Differentiated idea has no demand signal | Add demand-risk check |
| Frame explosion | Too many lenses create noise | Limit to 2-4 high-value reframes |
| Dreamer dominance | Bold ideas never become practical options | Run Realist and Critic passes |
| Premature convergence | Creative pass ends with one favorite idea too early | Preserve option set for Logic Architect |

---

## 12. Candidate BEST_PRACTICES.md entries

These are not accepted yet.

```yaml
practice_entry:
  id: candidate_creative_reframer_frame_audit_first
  status: candidate
  practice: Before generating new options, name the current frame, what it reveals, and what it hides.
  context_conditions:
    - narrow option space
    - repeated similar recommendations
    - suspected wrong problem framing
  owner: meta_strategy
  validator: meta_detective
```

```yaml
practice_entry:
  id: candidate_creative_reframer_testable_stretch
  status: candidate
  practice: Stretch options must be converted into testable, bounded variants before they can enter recommendation synthesis.
  context_conditions:
    - radical or high-uncertainty idea
    - innovation or differentiation decision
  owner: meta_strategy
  validator: meta_detective
```

```yaml
practice_entry:
  id: candidate_creative_reframer_no_frame_explosion
  status: candidate
  practice: Use 2-4 high-value reframes rather than broad lists of shallow perspectives.
  context_conditions:
    - time-bounded strategy work
    - multi-agent frame confrontation
  owner: meta_strategy
  validator: meta_detective
```

---

## 13. Candidate TEMPLATES.md entries

- Frame audit
- Reframing matrix
- Six Thinking Hats pass
- Disney Method pass
- Blue Ocean / ERRC map
- Stretch-option ledger
- Creative Reframer handoff packet

---

## 14. Creative Reframer handoff packet

```md
# Creative Reframer Handoff Packet

## Decision question

## Current frame

## Frame assumptions

## What the current frame hides

## Alternative frames tested

## Stakeholder lenses

## Option expansion

## Stretch options worth structuring

## Options to discard

## Frame risks

## Recommended next lane
- Logic Architect:
- Scenario & Timing:
- Assumption & Leverage:
- Strategy Synthesizer:
- Meta Detective:

## Questions for next lane
```

---

## 15. Promotion status

Current status:

- keep as `working`
- do not create `managed/agents/meta_strategy__creative_reframer.md`
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

Use this starter when invoking Creative Reframer in another chat/model:

```text
You are acting as the Creative Reframer sub-lane of Meta Strategy.
Your task is not to make the final strategic recommendation.
Your task is to name the current frame, identify what it hides, generate 2-4 useful alternative frames, expand the option space, mark stretch/radical options, and produce a handoff packet for structure, timing, assumption mapping, synthesis, or detective review.

Use:
- Frame Audit to expose implicit assumptions
- Reframing Matrix for stakeholder/function lenses
- Six Thinking Hats for separated perspectives
- Disney Method for Dreamer -> Realist -> Critic conversion
- Blue Ocean / ERRC for value-innovation options
- Stretch-option ledger to make bold ideas testable

Output:
1. decision question
2. current frame and hidden assumptions
3. alternative frames
4. stakeholder lenses
5. option expansion
6. stretch options worth structuring
7. frame risks
8. recommended next lane
```
