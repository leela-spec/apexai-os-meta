## Correct diagnosis

The failure is broader than “asking unnecessary clarification questions.”

**Failure pattern: premature specialization caused by example fixation.**

```
Concrete example appears
        ↓
I treat its surface details as a distinct product concept
        ↓
I invent fields, scopes, options, and edge cases
        ↓
Each invention creates more clarification questions
        ↓
UI + Algorithm + data + code + tests + documentation all branch
        ↓
Delivery slows while product value stays unchanged
```

The `no_screen` mistake was only the latest instance. The governing concept is:

```
BlueprintViolationPolicy:
  appliesTo: every Blueprint rule
  mechanism:
    violationConsequence: BP_penalty
    bpPerViolatingMinute: 0.25
    maximumTotalPenaltyBp: 10
    resultingBpFloor: 0

examples:
  no_screen:
    role: acceptance_example
    dedicatedMechanism: false
```

```
Many Blueprint rules
          ↓
one generic violation mechanism
          ↓
one generic BP penalty policy
          ↓
one explanation/presentation path
```

`No screen` demonstrates the mechanism. It does not create the mechanism.

## Why my previous analysis failed

|Layer|Previous diagnosis|Why inadequate|
|---|---|---|
|Symptom|I asked a redundant repetition question|True, but downstream|
|Proposed fix|Ask only consequential clarification questions|Useful, but too late|
|Missed cause|I had already converted `no_screen` into a special product branch|The unnecessary questions were consequences of this earlier abstraction error|
|Repeated failure|My own “corrective” YAML was still `ruleCode: no_screen`|I remained fixated on the example while claiming to generalize|
|Actual correction|Generalize before designing or questioning|Prevents the branch from being created|

I attempted to stop unnecessary decomposition **after** specialization. The correct control must run **before** an example becomes a schema, rule, feature, UI state, or question.

## Research synthesis

|Research finding|Meaning for Leela|
|---|---|
|Examples and framing can fixate designers on presented solution features instead of the underlying problem. This occurs even with useful examples. [Requirements Fixation](https://www.paulralph.name/wp-content/uploads/2012/06/Requirements-Fixation.pdf)|Real examples must validate general rules; their surface properties must not automatically become architecture|
|Fine-grained variability quickly becomes difficult to manage and commonly produces unnecessary variability or duplicate variation mechanisms. [CMU SEI: Variability in Software Product Lines](https://www.sei.cmu.edu/library/variability-in-software-product-lines/)|Do not build a separate evaluator, schema path, or UX treatment for every Blueprint rule|
|Modularization should be based on stable responsibilities and system-level decisions, because correct decomposition improves comprehensibility, flexibility, and development time. [Parnas, 1972](https://www.cs.lafayette.edu/~gexia/cs301/resources/parnas.html)|The stable responsibility is “evaluate Blueprint violations,” not “evaluate no-screen,” “evaluate sleep,” etc.|
|Systems engineering separates stakeholder intent, technical requirements, logical decomposition, and design solutions. Skipping directly from one example to a detailed solution confuses these levels. [NASA Systems Engineering Handbook](https://science.nasa.gov/wp-content/uploads/2023/04/nasa_systems_engineering_handbook_0.pdf)|First establish the Blueprint-wide behavior; derive code/data structures afterward|
|Separating policy from mechanism preserves flexibility: the mechanism stays stable while higher-level policy supplies decisions. [Wulf et al., HYDRA design principles](https://cseweb.ucsd.edu/classes/wi19/cse221-a/papers/wulf74.pdf)|One evaluator should enforce the common penalty policy; Blueprint rules supply what constitutes a violation|
|Agent instructions should sit at the “right altitude”: concrete enough to direct behavior, but not a brittle collection of case-specific conditions. [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)|The agent instruction must say “generalize before specializing,” not list `no_screen`, Bundle, Quizlet, or repetitions|
|Clarification should be driven by the utility of resolving genuinely different plausible intents. [Zhang & Choi, NAACL 2025](https://aclanthology.org/2025.findings-naacl.306/)|If a higher-level principle already produces the same result, there is no decision to ask|

**My inference from these sources:** the core defect is not insufficient detail management. It is failure to identify commonality before variability.

## Repeated instances in this work

|Instance|General concept that already existed|Specialization I introduced|Cost created|
|---|---|---|---|
|Execution formats|`Variant`|Invented `ExecutionStyle`, fields, hierarchy, and six clarification questions|Duplicate vocabulary and proposed migration|
|Path allocation|Scope-level demand line and TP waterfall|Reframed parent allocation as a new open UI decision|Asked an already-settled question|
|Rhythm fit feedback|One week-wide calculation on pick-up|Proposed recalculation for every touched slot|More computation and interaction complexity|
|Recommendation ranking|Declared available-time window before ranking|Compared increasingly complex ranking formulas|Optimized the wrong layer|
|Bundle/Fusion XP|Creator-authored membership is the declaration|Split membership and creator declaration into separate qualifiers|Invented a second qualification concept|
|External execution|One user-confirmed Run process|Split app/screen/offline cases and invented paper flashcards|Fabricated modalities and tracking questions|
|Blueprint penalty|One Blueprint violation policy|Built a `no_screen`-specific policy|Would duplicate code/data/UI for every rule|
|Penalty cap|One globally capped penalty|Split by Chunk, occurrence, repetition, and identity|Questions with no added product value|

Repository evidence already records several of these failures: [invented ExecutionStyle (line 18)](/C:/GitDev/Leela-Cloud-2026/docs/ssot/decisions/2026-07-25-PROPOSED-execution-styles.md:18), [already-settled Path question (line 34)](/C:/GitDev/Leela-Cloud-2026/docs/ssot/decisions/2026-07-31-weekly-composition-and-timetarget.md:34), and [excessive per-slot calculation (line 81)](/C:/GitDev/Leela-Cloud-2026/docs/ssot/decisions/2026-07-30-blueprint-authoring-and-fit-zones.md:81).

## Complexity multiplication

### Wrong architecture

```
Blueprint rules × dedicated evaluator branches
                × UI states
                × schema fields
                × fixtures
                × tests
                × explanations
                × documentation edges
```

Every new rule expands several permanent surfaces.

### Correct architecture

```
one Blueprint violation mechanism
+ declarative rule definitions
+ representative examples/tests
```

A new Blueprint rule should normally add policy data and examples—not a new subsystem.

## Meta-principles

|Principle|Operational meaning|
|---|---|
|**Generalize before specializing**|Identify the highest existing owner concept before creating questions, types, fields, or flows|
|**Commonality before variability**|Establish one shared mechanism; represent only genuine differences as policy data|
|**Examples are tests, not architecture**|Quizlet, Duolingo, and `no_screen` prove behavior; they do not automatically create product concepts|
|**Special cases require proof**|Add a branch only when observable required behavior cannot be expressed by the general rule|
|**Derive instead of asking**|Apply settled principles to identities, repetitions, counts, and examples without asking the operator|
|**Optimize the whole app**|Judge every distinction by its total UI, UX, Algorithm, data, code, test, documentation, and maintenance cost|
|**Stop when the principle closes the space**|Do not enumerate combinations after a general invariant determines their result|

## Proposed permanent agent instruction

```
Generalize before specializing. Before turning an example into a question,
rule, type, field, UI state, algorithm branch, or exception, identify the
highest existing owner concept and formulate the reusable behavior there.

Treat examples as grounding and acceptance tests, never as separate mechanisms
unless the required user-visible behavior cannot be represented by the general
rule. Derive entity, count, ordering, iteration, and repetition consequences
from settled principles without asking the operator.

Before introducing variability, compare its demonstrated product value with
its total permanent cost across UI/UX, Algorithm, data, code, tests, fixtures,
documentation, and maintenance. If the distinction adds surfaces without
changing required behavior, remove it and stop decomposing.
```

## Storage recommendation

Only two surgical owners are justified:

|File|Addition|Purpose|
|---|---|---|
|[AGENTS.md (line 24)](/C:/GitDev/Leela-Cloud-2026/AGENTS.md:24)|Compact instruction above|Always-on behavior for every task|
|[LEARNINGS_anti_drift.md (line 1)](/C:/GitDev/Leela-Cloud-2026/docs/orchestration/LEARNINGS_anti_drift.md:1)|Evidence-backed “premature specialization / example fixation” postmortem|Rationale, research, and regression examples|

No new skill, framework, checklist file, registry, or product-specific instruction is justified. No files have been changed yet.