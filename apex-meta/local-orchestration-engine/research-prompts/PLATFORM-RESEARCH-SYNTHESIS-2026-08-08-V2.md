---
title: "Platform Research Prompt V2 — Cross-Candidate Synthesis"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
candidates:
  - OpenClaw
  - Hermes
  - Odysseus
  - Custom/FEE
  - Hybrid
prompt_standard: apex-meta/SmallSkills/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md
---

# Cross-Candidate Synthesis Prompt V2

## Target

Research, reconcile, synthesize, and produce a **platform composition decision packet** for the APEX bounded local execution layer using the independent OpenClaw, Hermes and Odysseus research packets plus the existing FEE architecture evidence.

The packet must tell the operator **which composition should enter local bake-off first, which composition is the runner-up, which components are worth reusing regardless of winner, what evidence supports those choices, what contradictions remain, and which tests will decide the unresolved questions**.

The primary result is a decision packet for the next operator Q&A. It is **not** implementation authorization and it must not force a single-platform winner when a simpler hybrid is better.

## Role

You are the synthesis and architecture-comparison lead. Optimize for safe operational absorption, reversibility, maintainability and fit to the operator's actual user flows — not generic agent autonomy.

## Authority model

Use this order when sources conflict:

1. `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md` — locked operator requirements.
2. `apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md` — common user flows, hard gates, scoring and research protocol.
3. The three **V2 candidate research packets** — independent candidate findings and evidence.
4. Current primary candidate sources, only where needed to resolve a material contradiction or stale claim.
5. Existing APEX/FEE architecture/code evidence — current custom-spine capabilities and implementation burden.

Do not silently average away contradictions or let a candidate's defaults override operator authority.

## What you must understand

Before recommending a composition, reconcile:

- what each candidate actually executes today;
- which hard gates are native, externally brokerable, failed or unknown;
- which candidate is strongest for each of UF-A..UF-F;
- where FEE is already the cleaner deterministic owner;
- duplicated orchestration/control-plane risk;
- Windows/browser/local-model/resource realities;
- integration and maintenance cost;
- what remains unverified and therefore belongs in bake-off rather than in the recommendation as fact.

Use whatever synthesis method best reveals the answer. Preserve material disagreements instead of smoothing them over.

## Composition space

Evaluate at least these hypotheses, but add a better one if the evidence supports it:

1. FEE spine + Hermes execution/tool runtime + selected OpenClaw higher-level doctrine.
2. FEE spine + Odysseus runtime/workspace + selected OpenClaw higher-level doctrine.
3. FEE spine + OpenClaw runtime capabilities + authority-separated OpenClaw doctrine.
4. Custom/FEE executor + provider-specific browser adapters + selected reusable components only.
5. FEE spine + specialized runtime per user-flow class.
6. Another evidence-supported hybrid.

Do not reward extra components unless they deliver material value that justifies their interfaces and maintenance surface.

## Required comparison

Use the exact six user flows:

- UF-A Subscription research executor
- UF-B Script failure recovery
- UF-C Detective evidence collection
- UF-D Database / knowledge hygiene
- UF-E Multi-repo / multi-folder execution
- UF-F Personal weekly execution

And the exact six hard gates:

1. authority containment;
2. job-scoped permissions;
3. resumability;
4. evidence capture;
5. safe escalation;
6. practical Windows viability.

A composition with an unmitigated hard-gate failure cannot be the primary recommendation.

Use the scoring weights from the Platform Research Gate. Also compare, with confidence:

- CLI_SAVE;
- HUMAN_SAVE;
- DRIFT resistance;
- INTEGRATION simplicity;
- REVERSIBILITY;
- resource/maintenance burden.

Keep measured findings, evidence-based estimates and unknowns distinct.

## Contradictions and uncertainty

For each material disagreement across reports:

- state the conflicting claims;
- identify evidence type, version and recency;
- resolve from primary evidence when practical;
- otherwise preserve the uncertainty and define the smallest local test that settles it.

Do not choose the more confident-sounding report by default.

## Required bake-off design

For the strongest surviving compositions, define a **minimal common bake-off** that resolves only decision-relevant unknowns.

It must cover the Platform Research Gate's critical behaviors, including:

- authenticated prompt submission/capture and session continuity;
- browser failure / logout / CAPTCHA stop behavior;
- safe script recovery and unauthorized-action rejection;
- evidence collection without judgement drift;
- bounded KB/data hygiene;
- multi-root containment and forbidden-root rejection;
- personal/project trust separation;
- hostile source/browser instructions remaining inert;
- restart/resume;
- blocked overnight job plus safe continuation of independent work;
- event/provenance reconstruction;
- Windows resource coexistence;
- human interventions and Claude Code/Codex escalations.

Use the same local-model candidate across platform tests where technically possible so platform quality is not confused with model quality.

## Required deliverables

Produce one coherent decision packet containing:

1. **Executive recommendation** — first bake-off composition, runner-up, confidence.
2. **Evidence freshness/version map** for the three reports.
3. **Side-by-side candidate table**.
4. **Hard-gate comparison**.
5. **UF-A..UF-F comparison**.
6. **Composition matrix** with scores and confidence.
7. **Contradictions / unresolved evidence table**.
8. **Recommended composition diagram** and **runner-up diagram**.
9. **Reusable components regardless of winner**.
10. **Rejected compositions and why**.
11. **Minimal bake-off plan** with pass/fail evidence to collect.
12. **Directional resource/token/maintenance economics** without invented measurements.
13. **Reversal triggers**.
14. **Remaining operator decisions** before implementation.
15. The YAML result below.

```yaml
platform_synthesis_result:
  evidence_date: null
  candidate_reports: []
  report_versions_or_commits: {}
  hard_gate_summary: {}
  per_user_flow_comparison: {}
  composition_scores: {}
  score_confidence: {}
  contradictions: []
  recommended_architecture_hypothesis: null
  runner_up_architecture: null
  reusable_components: []
  rejected_compositions: []
  required_bakeoff_tests: []
  resource_unknowns_to_measure: []
  operator_questions_remaining: []
  reversal_triggers: []
  overall_confidence_0_to_100: null
```

## Essential boundaries

- Do not treat weighted score as a substitute for hard gates.
- Do not fabricate missing resource or reliability measurements.
- Do not collapse APEX into a candidate platform's orchestration model.
- Do not treat recommendation as implementation authorization.
- Preserve consequential uncertainty and contradictions.
- Prefer the simplest composition that meets the user flows and hard gates.

## Validation

Before delivery, verify that:

- all candidates were compared on the same six flows and six hard gates;
- evidence freshness/version differences are visible;
- contradictions are resolved or converted into tests;
- the recommendation names what FEE retains versus what external components provide;
- Windows/resource/maintenance concerns are represented honestly;
- the bake-off is minimal but sufficient to reverse the recommendation if reality differs;
- the result prepares an operator choice rather than silently making an implementation decision.

Revise the packet if needed.

## Success condition

The run is successful when the operator can use this packet to choose **which platform composition to bake off first and what evidence would reverse that choice**, while preserving APEX authority boundaries and postponing implementation until the subsequent operator platform/composition Q&A is explicitly locked.
