---
title: "Platform Research Prompt V2 — OpenClaw"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
candidate: OpenClaw
prompt_standard: apex-meta/SmallSkills/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md
---

# Deep Research Prompt V2 — OpenClaw

## Target

Research, synthesize, and produce an **OpenClaw platform decision packet** for the APEX bounded local execution architecture.

The packet must tell the operator, with evidence, **what OpenClaw actually is today, what role it should play, which APEX execution user flows it can support, which hard gates it passes, what requires an external FEE broker, and what still needs a local bake-off**.

The primary result is a decision-quality research packet. It is **not** an implementation plan, generic OpenClaw overview, or argument that OpenClaw must win.

## Role

You are the platform-research and systems-integration lead for this candidate. Optimize for accurate fit to APEX, not maximum generic agent autonomy.

## Authority model

Use this order when sources conflict:

1. `apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md` — operator requirements and boundaries.
2. `apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md` — evaluation rubric, six user flows, hard gates and scoring.
3. Current OpenClaw source code / official releases — executable reality.
4. Current official OpenClaw documentation — supported behavior and deployment.
5. `leela-spec/MasterOfArts/OpenClaw/07_finalopenclawsystem/` — the operator's existing OpenClaw doctrine, agents and processes.
6. Relevant current issues/discussions — verified limitations or unresolved operational problems.
7. Secondary sources — supporting context only.

Do not let marketing claims override source-code reality or APEX authority.

## What you must understand

Before settling the recommendation, reconstruct enough of OpenClaw to distinguish:

- executable runtime from prompts/configuration/doctrine/process;
- browser/session capabilities;
- tool, filesystem, shell and Git authority controls;
- state, resumability and evidence/logging;
- local-model integration and model swapability;
- Windows deployment and maintenance reality;
- overlap with APEX Weekly Orchestrator / Multi-Agent Orchestration;
- which existing OpenClaw Detective, KB, Hygiene, routing and workflow concepts remain valuable even if another runtime executes the work.

Use whatever internal research sequence is most effective. Do not produce a long reading diary.

## Current research questions

Answer only with current primary evidence where possible:

- Can OpenClaw operate **behind the FEE work-packet / capability / evidence spine** rather than becoming the controlling orchestration brain?
- Can dangerous actions be constrained to authorized action IDs and externally validated arguments?
- Can jobs be restricted to explicit multi-repo/multi-folder roots with different read/write permissions?
- Can authenticated subscription browser work be made reliable and resumable?
- What survives restart, browser failure, logout or model restart?
- Can captured web/model/source text remain inert evidence rather than executable authority?
- Can project and personal trust profiles be meaningfully separated?
- Is practical Windows 11 operation realistic on the operator's Core Ultra 7 258V / ~32 GB RAM / Arc 140V laptop while browser, development tools and local inference coexist?
- What external FEE wrappers/brokers are required to satisfy missing controls?
- Which OpenClaw role gives the most value with the least duplicated orchestration and maintenance burden?

## Required evaluation

Use the exact six user flows and hard gates defined in the Platform Research Gate:

- UF-A Subscription research executor
- UF-B Script failure recovery
- UF-C Detective evidence collection
- UF-D Database / knowledge hygiene
- UF-E Multi-repo / multi-folder execution
- UF-F Personal weekly execution

For each hard gate return one of:

- `PASS`
- `PASS_WITH_EXTERNAL_BROKER`
- `FAIL`
- `UNKNOWN`

Hard gates are:

1. authority containment;
2. job-scoped permissions;
3. resumability;
4. evidence capture;
5. safe escalation;
6. practical Windows viability.

A hard-gate failure overrides a high aggregate score.

## Role hypotheses to compare

Compare at least:

1. primary low-level executor behind FEE;
2. browser/tool capability provider behind FEE;
3. higher-level Detective/KB/Hygiene/agent doctrine only;
4. runtime subset + higher-level doctrine hybrid;
5. not recommended in the execution stack.

You may add a better evidence-supported role.

## Evidence and scoring

For consequential claims label the evidence as:

- source-code verified;
- officially documented;
- operator-repo doctrine/process;
- measured;
- inferred;
- unknown.

Score 0–100 with confidence 0–100 using the weights in the Platform Research Gate. Also score UF-A..UF-F individually. Do not manufacture precision when evidence is weak.

## Required deliverables

Produce one coherent decision packet containing:

1. **Executive finding** — strongest role, biggest strength, biggest blocker, confidence.
2. **Runtime reality map** — executable vs doctrine/config/process.
3. **UF-A..UF-F evidence table**.
4. **Hard-gate table**.
5. **Weighted score + confidence**.
6. **Windows/browser/local-model/permission/resume findings**.
7. **Best OpenClaw composition with FEE**, shown as a simple architecture diagram.
8. **Rejected roles and trade-offs**.
9. **Unknowns and minimal bake-off tests** needed to resolve them.
10. **Source appendix** with dates, versions and commit SHAs where available.
11. The YAML result below.

```yaml
platform_research_result:
  candidate: OpenClaw
  evidence_date: null
  versions_or_commits_reviewed: []
  runtime_reality: {}
  per_user_flow_scores: {}
  weighted_scores: {}
  score_confidence: {}
  hard_gate_results: {}
  windows_fit: {}
  browser_fit: {}
  local_model_fit: {}
  permission_model: {}
  state_and_resumability: {}
  audit_and_evidence: {}
  duplicated_orchestration_risk: {}
  strongest_role: null
  required_external_brokers: []
  unresolved_unknowns: []
  benchmark_tests_required: []
  rejected_roles: []
  reversal_triggers: []
  overall_confidence_0_to_100: null
```

## Essential boundaries

- Do not invent missing platform behavior.
- Do not treat a recommendation as implementation authorization.
- Do not let candidate defaults override the operator decision locks.
- Preserve important contradictions and uncertainty.
- Do not confuse evidence collection with consequential judgement.
- Continue through ordinary uncertainty using the best-supported interpretation; convert material unknowns into explicit bake-off tests.

## Validation

Before delivery, verify that:

- all six user flows were evaluated;
- all six hard gates have evidence-backed statuses;
- runtime reality is separated from doctrine/marketing;
- consequential claims point to current evidence;
- Windows viability is concrete rather than theoretical;
- the recommendation states the strongest role **and** what FEE must still own;
- unknowns have tests rather than guesses;
- no implementation was silently authorized.

Revise the packet if those checks fail.

## Success condition

The run is successful when the operator can use this packet, alongside the Hermes and Odysseus packets, to decide whether OpenClaw should be the executor, a capability provider, higher-level doctrine, a hybrid component, or excluded — with the remaining uncertainty expressed as concrete bake-off tests rather than assumptions.
