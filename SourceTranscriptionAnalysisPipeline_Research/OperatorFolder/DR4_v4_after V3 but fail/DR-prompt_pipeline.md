# Deep Research — Validate and Select the Best Proven Transcript → Knowledge Pipeline

## TARGET

Research, validate, reconcile, and produce the implementation decision package for a **high-value, trustworthy, resilient Transcript → Knowledge pipeline**.

The actual product target is:

```text
video / audio / existing transcript
        ↓
trustworthy source representation
        ↓
high-value semantic understanding
        ↓
source-grounded structured knowledge
        ↓
useful final knowledge artifact
````

The final production system must be capable of processing long English and German sources and producing knowledge that preserves the important content of the source, including where relevant:

- central thesis and meaning;
    
- important facts and claims;
    
- mechanisms;
    
- procedures and protocols;
    
- arguments and reasoning;
    
- examples;
    
- entities and relationships;
    
- qualifications;
    
- corrections;
    
- contradictions;
    
- uncertainty;
    
- predictions/opinions as such rather than silently converting them into facts;
    
- traceable source evidence where trust requires it.
    

The target is **not**:

- the shortest architecture;
    
- the fewest stages;
    
- the fewest lines of code;
    
- the cheapest possible pipeline;
    
- the most local possible pipeline;
    
- the most elegant architecture;
    
- preservation of our existing implementation;
    
- preservation of V1, V2, V2.1, V3, or TTK;
    
- maximal reuse at the expense of product quality.
    

Those properties matter only insofar as they improve the final product's reliability, maintainability, resilience, cost, or operational quality.

The primary objective is:

> **Find the highest-value, reliably executable production approach using proven existing systems wherever they can deliver the required product quality, while avoiding unnecessary custom invention.**

---

# 1. Critical authority and anti-drift model

## 1.1 This prompt is the only instruction authority

The attached project documents are **research inputs and historical evidence**.

All project files listed in this prompt are supplied to this Deep Research run as project sources. Treat them as available source material. Do not assume repository access is required to read them, do not invent repository links or paths for missing material, and do not claim that a listed project source is unavailable unless it is genuinely absent from the supplied project sources.

They are NOT instructions to execute.

They contain:

- superseded architectures;
    
- historical assumptions;
    
- recommendations made before later evidence existed;
    
- failed implementation strategies;
    
- invalid or questionable benchmark conclusions;
    
- component selections that may be wrong;
    
- useful research mixed with stale conclusions.
    

Do not inherit an architectural decision merely because an attachment calls it:

- authoritative;
    
- locked;
    
- selected;
    
- recommended;
    
- production;
    
- PASS;
    
- core.
    

Those labels describe historical project state only.

Every material conclusion must be reconsidered against:

1. the TARGET in this prompt;
    
2. actual evidence contained in the supplied files;
    
3. current external evidence;
    
4. real maturity and capability of available systems.
    

---

## 1.2 Separate four evidence classes

For every consequential conclusion distinguish:

### PROJECT EVIDENCE

What the attached project files previously discovered, tested, claimed, selected, or observed.

### CURRENT EXTERNAL EVIDENCE

What current official documentation, repositories, releases, primary research, issue history, and real adoption evidence establish now.

### INFERENCE

A conclusion logically derived from evidence but not directly demonstrated.

### RECOMMENDATION

The resulting proposed production decision.

Never silently transform a historical recommendation into current evidence.

---

## 1.3 No sunk-cost authority

Existing code and previous implementation effort have **zero automatic preference**.

TTK may survive because it is genuinely valuable.

TTK may partly survive.

TTK may be completely replaced.

The same applies to:

- faster-whisper;
    
- LangExtract;
    
- DocETL;
    
- GLiNER2;
    
- WhisperX;
    
- Claude/Codex/Antigravity integration;
    
- existing runners;
    
- existing schemas;
    
- existing compiler;
    
- existing evaluation machinery.
    

Judge them by present value to the TARGET.

---

# 2. Decision priorities

Use this priority order.

## Priority 1 — Product quality

The selected system must produce genuinely useful knowledge.

Evaluate:

- important-insight recall;
    
- source fidelity;
    
- semantic depth;
    
- long-context performance;
    
- grounding quality;
    
- uncertainty/caveat preservation;
    
- coherent global understanding;
    
- EN/DE performance;
    
- useful final artifact quality.
    

A simpler system that produces materially worse knowledge must not win because it is simpler.

---

## Priority 2 — Reliability and maturity

Prefer systems that have evidence of actually working:

- established implementation;
    
- real users;
    
- active maintenance;
    
- real examples;
    
- stable interfaces;
    
- documented behavior;
    
- reproducible execution;
    
- meaningful production/community history.
    

---

## Priority 3 — Reuse before invention

Where existing software solves a capability well, use it.

Prefer:

1. established end-to-end product/pipeline;
    
2. established near-complete product/pipeline;
    
3. established platform-native workflow/skill/plugin;
    
4. established specialist component;
    
5. configuration of an existing system;
    
6. supported plugin/extension/provider interface;
    
7. light adaptation or fork;
    
8. custom implementation only where evidence shows it is genuinely necessary.
    

This is a **reliability strategy**, not a mandate to sacrifice product quality.

---

## Priority 4 — Resilience and maintainability

Prefer systems that:

- recover cleanly;
    
- expose understandable failure modes;
    
- avoid fragile hidden state;
    
- have bounded dependencies;
    
- can be rerun;
    
- are maintainable by another AI/operator later;
    
- do not require constant architectural repair.
    

---

## Priority 5 — Efficiency

Consider:

- local hardware viability;
    
- token consumption;
    
- runtime;
    
- model calls;
    
- memory;
    
- incremental monetary cost;
    
- subscription usage;
    
- operational overhead.
    

Efficiency matters, but not when it materially damages the knowledge product.

---

## Priority 6 — Simplicity

All else being sufficiently equal, prefer fewer:

- custom components;
    
- fragile adapters;
    
- environments;
    
- provider seams;
    
- moving parts;
    
- bespoke contracts.
    

Simplicity is a **tie-breaker and reliability advantage**, not the main product target.

---

# 3. Core anti-invention rule

AI-generated bespoke infrastructure has repeatedly failed this project.

Therefore:

> **Never recommend custom implementation merely because it appears straightforward to build.**

Before recommending any new custom subsystem, demonstrate that credible existing alternatives cannot adequately satisfy the required capability.

Required evidence:

```yaml
custom_authorization:
  capability:
  why_the_capability_is_required_for_product_value:

  existing_alternatives_examined:
    - candidate:
      maturity:
      relevant_capability:
      observed_or_documented_limitation:
      evidence:

  why_configuration_is_insufficient:
  why_supported_extensions_are_insufficient:
  why_light_adaptation_or_fork_is_insufficient:

  custom_work_required:
  product_value_created:
  maintenance_risk:
  justification:
```

If that evidence cannot be supplied:

```text
CUSTOM BUILD NOT JUSTIFIED
```

Do not create custom equivalents of mature existing software.

---

# 4. First research question — Does an existing pipeline already solve the product?

Before decomposing the problem into individual components, perform a serious search for **existing complete or near-complete Transcript → Knowledge systems**.

We specifically want to know whether an existing system can already perform a substantial portion of:

```text
video/audio/transcript
→ transcript acquisition
→ long-source understanding
→ important-information extraction
→ grounding / citations / timestamps
→ global synthesis
→ structured knowledge
→ useful final artifact
```

An existing product does not need to use our terminology.

For example, it may produce:

- grounded research notes;
    
- structured notebook knowledge;
    
- atomic notes;
    
- claims;
    
- chapters;
    
- summaries plus source evidence;
    
- knowledge graphs;
    
- research reports;
    
- semantic cards;
    
- wiki pages.
    

Judge the **product behavior**, not naming compatibility with our previous architecture.

---

# 5. Ecosystems that must be searched

Research current reusable solutions across at least:

## Agent/platform ecosystems

- OpenClaw native capabilities;
    
- official/bundled OpenClaw skills/plugins;
    
- credible ClawHub/community skills;
    
- Claude Code skills/plugins/hooks/commands/workflows;
    
- Codex skills/workflows/instruction packages;
    
- Google Antigravity / `agy` reusable skills/workflows/capabilities.
    

Investigate whether someone has already created a workflow that we can install, copy, configure, or adapt.

Do not assume equivalent platform terminology.

Verify what each ecosystem actually supports.

---

## Existing standalone systems

Search broadly for current systems designed for:

- podcast → knowledge;
    
- YouTube → knowledge;
    
- lecture → knowledge;
    
- interview → knowledge;
    
- meeting → knowledge;
    
- transcript → structured knowledge;
    
- grounded long-document understanding;
    
- source-grounded summarization;
    
- research notebook generation;
    
- audio/video knowledge extraction;
    
- evidence-linked notes;
    
- automated wiki generation;
    
- long-form content distillation.
    

Do not restrict discovery to candidates already named in the supplied project files.

---

# 6. End-to-end candidate evaluation

For each credible complete or near-complete solution record:

|Dimension|Required analysis|
|---|---|
|Product|What final artifact does it actually produce?|
|Coverage|Which functional capabilities does it handle?|
|Knowledge quality|Does it preserve substantive source knowledge or merely summarize?|
|Long source|Can it handle hours-long sources reliably?|
|Grounding|Does it provide timestamps, quotes, spans, citations, or source linkage?|
|EN/DE|Actual multilingual suitability|
|Semantic fidelity|Does it preserve mechanisms, caveats, contradictions, etc.?|
|Input|Audio, video, URL, transcript|
|Output|Exact resulting artifact types|
|Maturity|Adoption, maintenance, history, releases|
|Real evidence|Examples, demos, tests, users|
|Locality|What remains local?|
|Privacy|What content is sent externally?|
|Providers|Required LLM/model/services|
|Cost|Free/local/subscription/metered|
|Windows|Practical viability|
|Recovery|Retry/resume behavior|
|Extensibility|Configuration/plugin/fork surface|
|Integration|What would we still have to implement?|
|Risks|Current known limitations|

---

# 7. Battle-proven rating

Assign serious candidates a maturity rating.

### BP4 — Established

Long-lived or broadly adopted, actively maintained, strong documentation, repeated real-world evidence.

### BP3 — Proven

Real working implementation with credible usage and maintenance, but less established than BP4.

### BP2 — Credible

Real and technically credible, but adoption/history/operational evidence remains limited.

### BP1 — Experimental

Immature, unstable, sparsely validated, or early-stage.

### BP0 — Ours/custom

Substantially new implementation we would need to create.

Maturity is important because reliability matters.

However:

> **BP rating does not override product capability.**

A BP4 generic summarizer is not automatically better than a BP3 system that materially satisfies the actual knowledge target.

Use maturity together with product evidence.

---

# 8. Only then reconstruct the required functional pipeline

After researching end-to-end systems, determine what capabilities the product actually requires.

Historical project work proposed capabilities such as:

1. invocation;
    
2. source acquisition;
    
3. media preparation;
    
4. transcription / ASR;
    
5. ASR quality handling;
    
6. alignment / speaker attribution;
    
7. source/evidence representation;
    
8. long-source segmentation;
    
9. semantic extraction;
    
10. structured output;
    
11. source-support checking;
    
12. global synthesis;
    
13. external factual verification;
    
14. knowledge compilation;
    
15. product evaluation;
    
16. recovery/resume;
    
17. delivery/integration.
    

These are **hypotheses**, not mandatory architecture.

You may determine that:

- a stage is unnecessary;
    
- two stages should be merged;
    
- a stage should be conditional;
    
- a system already owns several stages;
    
- an entirely different decomposition is more appropriate.
    

Preserve only capabilities that materially contribute to the TARGET.

---

# 9. Research every remaining capability

For each capability not adequately solved by the chosen whole-system candidates, research established alternatives.

Priority should generally favor:

- mature;
    
- reliable;
    
- open-source;
    
- free;
    
- local;
    
- deterministic where the operation itself is deterministic;
    
- Windows-compatible;
    
- actively maintained.
    

But those are not absolute requirements.

Also research:

- paid tools;
    
- hosted services;
    
- model APIs;
    
- subscription-backed solutions;
    

when they could deliver **materially higher product value or reliability**.

For paid/cloud alternatives explicitly report:

```yaml
paid_option:
  additional_product_value:
  reliability_gain:
  quality_gain:
  operational_gain:
  expected_cost:
  free_alternative:
  is_the_gain_material:
```

Do not reject high-value technology merely because it costs money.

Do not select it merely because it is commercial.

---

# 10. Deterministic vs semantic responsibility

Use deterministic software where the problem is mechanically deterministic.

Examples may include:

- downloading;
    
- hashing;
    
- file conversion;
    
- schema validation;
    
- exact substring/span verification;
    
- state tracking;
    
- compilation;
    
- reproducible transformations.
    

Use strong semantic systems where the problem requires actual interpretation.

Examples may include:

- meaning;
    
- importance;
    
- mechanisms;
    
- argument structure;
    
- uncertainty interpretation;
    
- chapter/theme synthesis;
    
- semantic support;
    
- global understanding.
    

Do not force local deterministic tools to solve semantic problems merely to reduce LLM usage.

Do not use LLMs for deterministic operations when mature software already solves them reliably.

---

# 11. Required capability decision matrix

Produce a complete matrix covering the final reconstructed pipeline.

At minimum:

| Capability | Why it exists | Product value | Existing whole-system coverage | Serious options | BP | Evidence | Product-quality implications | Reliability | Local/free status | Cost | Prior project recommendation | Current recommendation | Confidence | Fallback |

For each capability explicitly differentiate:

- previous project recommendation;
    
- current external reality;
    
- current decision.
    

Where a previous recommendation was wrong or unsupported, say so clearly.

---

# 12. Reconcile V1, V2, V2.1 and V3

Create a dedicated reconciliation table:

| Topic | V1 | V2 | V2.1 | V3 | What evidence actually supports | Current verdict |

Cover at least:

- overall product target;
    
- source acquisition;
    
- ASR;
    
- diarization/alignment;
    
- custody/provenance;
    
- chunking/windowing;
    
- Map/extraction;
    
- structured output;
    
- source-support checking;
    
- global synthesis;
    
- external verification;
    
- compiler/output;
    
- product evaluation;
    
- resumability;
    
- OpenClaw/execution architecture.
    

Do not choose a winner by version number.

V3 is newer but not automatically more correct.

V1 is older but may contain useful options research.

V2/V2.1 contain substantial research but also failed assumptions.

Treat chronology as context, not evidence quality.

---

# 13. Evaluate reuse at the level of product responsibility

For every final architecture, identify exactly who owns each responsibility.

Example:

```text
SOURCE
  ↓
[Existing System A owns acquisition + ASR]
  ↓
[Existing System B owns grounded long-source extraction + synthesis]
  ↓
[Existing System C owns final knowledge representation]
  ↓
KNOWLEDGE PRODUCT
```

Prefer handing responsibility to proven systems over recreating that responsibility ourselves.

But do not force reuse if a reused system materially degrades:

- insight recall;
    
- grounding;
    
- semantic depth;
    
- multilingual quality;
    
- reliability;
    
- final artifact usefulness.
    

---

# 14. Whole-product quality must dominate selection

For every serious architecture ask:

> If we actually ran this on a two-hour technical interview or German financial discussion, which architecture is most likely to produce the knowledge artifact we actually want?

Evaluate architectures on:

## Knowledge value

- important insight recall;
    
- non-generic synthesis;
    
- useful hierarchy/organization;
    
- mechanisms retained;
    
- procedures retained;
    
- arguments retained;
    
- examples retained;
    
- caveats retained;
    
- uncertainty retained;
    
- contradictions retained.
    

## Trust

- source traceability;
    
- claim grounding;
    
- hallucination/overstatement behavior;
    
- distinction between source support and external truth.
    

## Language/source breadth

- English;
    
- German;
    
- long-form;
    
- multi-speaker where relevant;
    
- technical terminology.
    

## Operational reliability

- reproducibility;
    
- recovery;
    
- failure handling;
    
- maintainability.
    

## Efficiency

- runtime;
    
- tokens;
    
- local compute;
    
- cost.
    

## Implementation burden

- required adapters;
    
- required custom code;
    
- fragile seams.
    

Do not compress these into one simplistic score.

Make the trade-offs visible.

---

# 15. Implementation strategies

After completing the research, produce **1–3 implementation strategies**, depending on what the evidence supports.

Do not artificially create multiple strategies if one clearly dominates.

Possible strategy shapes include:

### Adopt existing pipeline

A mature existing solution already provides most or all required product behavior.

### Extend a near-complete pipeline

A mature solution provides most of the product and only defined gaps need adaptation.

### Proven-component composition

No suitable whole system exists, so combine established components.

These are categories, not required outputs.

Use whatever architecture the evidence actually supports.

---

# 16. Implementation-plan objective

The implementation plan must enable another AI/CLI executor to **realize the selected architecture without reopening the architecture research**.

It should still be allowed to diagnose implementation problems.

It should not be allowed to redesign the pipeline merely because it encounters ordinary integration friction.

Each plan must therefore clearly state:

- what was selected;
    
- what is already proven;
    
- what remains locally unknown;
    
- exact implementation target;
    
- required inputs;
    
- tools/systems involved;
    
- configuration;
    
- expected outputs;
    
- actual product tests;
    
- failure/retry behavior;
    
- reversal triggers.
    

---

# 17. Human-readable implementation plan

For each selected strategy provide:

## Target

What real product will exist after implementation.

## Selected systems

For every system:

- responsibility;
    
- current verified version/release where material;
    
- license;
    
- installation method;
    
- required provider/model;
    
- configuration;
    
- why it was selected.
    

## Architecture

Show the complete actual flow.

## Implementation sequence

Define the concrete sequence from clean/preflight state through first real product.

## Vertical product test

Specify the first real representative source and what useful artifact must be produced.

## Inspection

Specify what aspects of the artifact must be inspected to determine whether the system actually delivers value.

## Repair rules

Prefer:

1. correct configuration;
    
2. documented usage;
    
3. supported plugin/extension;
    
4. known workaround;
    
5. alternate proven component;
    
6. only then reconsider custom implementation.
    

## End-to-end acceptance

Define the real final product evidence required.

---

# 18. Machine-readable implementation plan

Also produce a machine-readable YAML plan.

Its purpose is not to micromanage every command.

Its purpose is to prevent architectural drift and make execution state explicit.

Use approximately:

```yaml
schema: transcript-knowledge-implementation-plan.v1

target:
  product:
  product_quality_requirements:
  languages:
  source_types:

architecture:
  strategy:
  rationale:
  components:
    - id:
      responsibility:
      existing_system:
      bp_rating:
      evidence_status:
      configuration:
      custom_code_required:

decision_lock:
  selected:
  explicitly_rejected:
  unresolved_local_facts:
  architecture_research_must_not_be_reopened_for:

preflight:
  - id:
    objective:
    read_only_actions:
    expected_result:
    if_missing:

work_units:
  - id:
    objective:
    product_value:
    inputs:
    context_required:
    systems_used:
    actions:
    observable_outputs:
    product_inspection:
    acceptance:
    failure_classes:
    retry:
    reversal_trigger:
    next:

vertical_slice:
  source:
  complete_flow:
  expected_artifact:
  quality_requirements:
  acceptance:

end_to_end:
  sources:
  expected_artifacts:
  quality_requirements:
  reliability_requirements:
  acceptance:

custom_code:
  - item:
    authorization:
    smallest_required_surface:

final_success:
```

Improve the schema where useful.

Do not add fields merely for completeness.

---

# 19. Context-aware execution requirement

The execution AI should not need the full research report in every context.

For each work unit specify only the necessary execution context.

Example:

```yaml
context_required:
  architecture_decision:
  component_documentation:
  previous_outputs:
  local_files_to_inspect:
  explicitly_not_required:
```

The architecture decision package should remain the stable authority.

Individual work units should be bounded around real product progress.

---

# 20. Iterative execution principle

Implementation should operate as:

```text
execute selected proven approach
→ observe real result
→ inspect product
→ repair concrete implementation problem
→ rerun affected work
→ continue
```

Ordinary defects should not trigger architecture redesign.

Architecture should be reconsidered only when real evidence demonstrates a material problem such as:

- required capability absent;
    
- unacceptable product quality;
    
- unacceptable reliability;
    
- unsupportable platform incompatibility;
    
- unacceptable cost;
    
- integration requires substantial custom architecture not discovered during research.
    

Define these reversal triggers explicitly.

---

# 21. Evaluation must remain proportional

Testing exists to determine whether the **product works**.

Do not create a giant evaluation architecture.

Use the smallest amount of evidence capable of answering the consequential question.

Prefer:

- actual system execution;
    
- actual final artifacts;
    
- direct source comparison;
    
- existing test suites;
    
- bounded human review;
    
- focused benchmarks where candidates genuinely differ.
    

Automated PASS labels never override visibly poor product output.

---

# 22. External research evidence quality

Extensive current web research is mandatory. Do not rely on the supplied project sources or prior project research as a substitute for searching the current external ecosystem.

Search broadly enough to discover credible systems, skills, pipelines, plugins, tools, models, frameworks, and implementation patterns that the prior project work may have missed. Then search deeply enough on serious candidates to verify what they actually do, how current they are, their limitations, and whether they can materially satisfy the TARGET.

For every major capability and every serious end-to-end or near-end-to-end candidate:

- perform current web search rather than relying on memory;

- verify current existence, maintenance status, versions/releases where material, supported platforms, licensing, provider requirements, and documented capabilities;

- inspect primary sources for the strongest candidates;

- inspect relevant current issue/discussion evidence when practical limitations, Windows viability, broken integrations, or known failure modes could materially affect the decision;

- search for competing alternatives beyond those already named in the project sources;

- use multiple independent search formulations where a single query could miss an ecosystem, alternative terminology, or differently named workflow;

- continue discovery until additional searches are producing mostly duplicates or clearly lower-value candidates rather than materially new solution classes.


Do not interpret this breadth requirement as a requirement to produce a bloated catalog. The research may inspect many candidates while only carrying serious, evidence-backed contenders into the final decision matrices.

For current technical claims prefer:

1. official documentation;

2. official repositories;

3. official package/model documentation;

4. official releases/changelogs;

5. maintainer issue/discussion evidence;

6. primary research;

7. credible independent implementation/adoption evidence.


For community skills/workflows, inspect enough evidence to distinguish:

- real reusable capability;

- thin prompt wrapper;

- demo;

- abandoned repository;

- production-quality tool.


Do not rank candidates from marketing descriptions alone.

Where primary sources establish advertised capability but not real-world maturity or operational reliability, supplement them with credible independent adoption or implementation evidence.

Record enough source attribution that a later reviewer can distinguish what was verified on the current web from what came from the supplied project sources.

---

# 23. Required final deliverables

## D1 — Executive product recommendation

Answer plainly:

> What should we actually use/build to obtain the highest-value reliable Transcript → Knowledge product?

Include:

- selected strategy;
    
- confidence;
    
- major systems;
    
- expected product quality;
    
- reuse level;
    
- custom surface;
    
- largest risks;
    
- important alternatives.
    

---

## D2 — Existing whole-pipeline landscape

List serious complete and near-complete candidates.

Explain what each genuinely replaces.

---

## D3 — Final functional pipeline

Produce the corrected functional lifecycle.

Clearly mark stages/capabilities as:

- OWNED_BY_EXISTING_SYSTEM;
    
- SEPARATE_COMPONENT;
    
- CONDITIONAL;
    
- REMOVED;
    
- CUSTOM_REQUIRED.
    

---

## D4 — Complete capability/options matrix

For every required capability provide:

- credible options;
    
- evidence;
    
- maturity;
    
- value;
    
- drawbacks;
    
- current recommendation.
    

---

## D5 — V1/V2/V2.1/V3 reconciliation

Explain what survived and what was wrong.

---

## D6 — Recommended architecture(s)

Produce 1–3 only where justified.

For every architecture show the actual end-to-end flow and responsibility ownership.

---

## D7 — Custom-code audit

List everything we would still own ourselves.

For each explain why existing solutions do not remove the need.

---

## D8 — Human-readable implementation plan(s)

Detailed enough for another AI to implement.

---

## D9 — Machine-readable implementation plan(s)

Suitable as direct architecture authority for the implementation AI.

---

## D10 — Product validation plan

Define the real executions/artifacts required to prove the selected pipeline delivers the intended knowledge value.

---

## D11 — Evidence register

For each important current conclusion include:

- evidence source;
    
- date/version where relevant;
    
- fact supported;
    
- confidence.
    

---

# 24. Final anti-drift review

Before finalizing, explicitly audit your own recommendation:

### TARGET audit

Does this architecture maximize the likelihood of producing a genuinely valuable, trustworthy knowledge artifact?

### Completeness audit

Does it cover every capability actually necessary for the product?

### Reuse audit

Are we building anything that a credible existing system already solves adequately?

### Quality audit

Did simplicity, locality, cost, or reuse cause us to choose a materially worse knowledge product?

If yes, reconsider.

### Sunk-cost audit

Did existing TTK/V1/V2/V2.1 implementation receive preference merely because it already exists?

If yes, reconsider.

### Complexity audit

Is every added component earning its place through product value, reliability, or major efficiency?

### Custom-code audit

Is every custom component backed by evidence showing existing solutions are insufficient?

### Evidence audit

Are current claims based on current evidence rather than stale attachments?

### Execution audit

Can another AI implement the recommendation without having to rediscover the architecture?

Revise consequential failures before delivering the result.

---

# SUCCESS CONDITION

This research is successful when it identifies and justifies the **best currently achievable, battle-proven architecture for producing high-value, trustworthy Transcript → Knowledge artifacts**, using existing systems wherever they meet the required quality and reliability, while introducing custom implementation only where existing solutions demonstrably cannot satisfy a necessary product capability.

The winning architecture does **not** have to be the shortest, smallest, cheapest, most local, or most reused.

It must be the architecture with the strongest overall case for delivering the TARGET reliably.

Reuse, simplicity, efficiency, locality, and cost are important decision factors because they affect reliability and sustainability.

They do not replace the TARGET.

```

## 3. The key correction in one sentence

The previous prompt effectively said:

> **Find the least we need to build.**

That was wrong.

This one says:

> **Find the best reliable way to produce the knowledge product we actually want, and whenever proven existing systems can deliver that value, use them instead of trusting an AI to reinvent them.**

That preserves the anti-invention principle **without turning minimalism into the product objective**.
```
