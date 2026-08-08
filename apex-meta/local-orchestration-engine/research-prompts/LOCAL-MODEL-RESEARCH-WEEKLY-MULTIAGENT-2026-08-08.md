---
title: "Local Model Research Prompt — Weekly and Multi-Agent Execution"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
prompt_standard: apex-meta/SmallSkills/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md
authority:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
---

# Research Prompt C — Weekly + Multi-Agent Execution

## Target

Research and produce a **current candidate packet for non-coding APEX local execution**, focused on Weekly Orchestrator execution and Multi-Agent Orchestration support.

The goal is to identify high-reasoning local models/configurations that are especially reliable at constrained state interpretation, tool/action choice, browser recovery, evidence preparation, specialist-worker execution, hostile-content resistance and correct escalation — while remaining subordinate to the owning orchestration system.

## Binding architecture

Round-3 LM-6..LM-22 are authority.

Key boundaries:

- Weekly graph/work packet owns sequence;
- local model classifies only among declared states and can return `UNKNOWN`;
- multi-turn browser work follows predeclared follow-up classes;
- job state is externally durable and resumable;
- Meta Ops retains Multi-Agent orchestration;
- local worker may create candidate artifacts but never verify/promote them;
- Detective support is evidence/anomaly collection, not verdict;
- hostile source/browser/model/tool content is untrusted data;
- typed escalation is routed by enforced policy.

## Research questions

For each serious candidate determine current evidence about:

- instruction fidelity under long multi-step work packets;
- closed-set state classification and abstention/unknown behavior;
- tool selection and argument generation;
- structured outputs;
- browser/computer-use suitability where applicable;
- response classification and bounded conditional follow-ups;
- long-running task compatibility with external checkpoints;
- recovery judgement under UI/path/provider variation;
- evidence extraction, provenance and contradiction-candidate ability;
- schema/terminology cleanup without semantic redesign;
- prompt-template materialization without independent strategy rewrite;
- prompt-injection and untrusted-content behavior;
- multi-repo/path obedience;
- resource footprint and likely coexistence.

Use primary model/runtime sources first. Public agent benchmarks may prioritize but cannot certify these behaviors.

## Required fixture mapping

Map evidence and hypotheses to:

### Weekly
- WEEKLY-01 one prompt + capture;
- WEEKLY-02 conditional multi-turn;
- WEEKLY-03 browser/UI recovery;
- WEEKLY-04 interruption/resume;
- WEEKLY-05 multi-repo containment;
- WEEKLY-06 raw evidence + non-authoritative index.

### Multi-Agent
- MA-01 bounded Meta Ops packet;
- MA-02 Detective evidence without verdict;
- MA-03 Knowledge/Informatics hygiene;
- MA-04 prompt/workflow materialization;
- MA-05 typed escalation destination;
- MA-06 adversarial source containment.

### Injection
Assess suitability for INJECT-01..08, while keeping in mind that hard containment remains outside the model.

## Reasoning-first lens

Specifically test the hypothesis that higher-reasoning local models materially improve:

- recognition of genuine `UNKNOWN` states;
- distinction between equivalent UI recovery and workflow invention;
- correct escalation class;
- evidence comparison without premature verdict;
- nuanced hostile-content recognition;
- multi-root provenance;
- bounded semantic cleanup.

Also identify cases where more capable models may create **more scope drift** because they are more willing to solve beyond the packet.

## Deliverables

1. executive finding;
2. current candidate/version map;
3. reasoning-strength vs authority-drift comparison;
4. WEEKLY-01..06 evidence/hypothesis matrix;
5. MA-01..06 evidence/hypothesis matrix;
6. injection-resistance findings;
7. context and retrieval implications;
8. browser/tool implications;
9. resource/coexistence implications;
10. shortlist for APEX bake-off;
11. unknowns requiring local trials;
12. source appendix;
13. YAML:

```yaml
weekly_multiagent_model_research:
  evidence_date: null
  candidates: []
  benchmark_priority: []
  weekly_fixture_hypotheses: {}
  multiagent_fixture_hypotheses: {}
  injection_findings: {}
  reasoning_strengths: {}
  scope_drift_risks: {}
  context_findings: {}
  browser_tool_findings: {}
  resource_findings: {}
  local_test_unknowns: []
  overall_confidence_0_to_100: null
```

## Essential boundaries

- Do not redesign Weekly or Multi-Agent Orchestration.
- Do not confuse local reasoning quality with authority.
- Do not treat a model's self-reported confidence as a validity signal.
- Do not treat prompt-injection resistance as sufficient containment; system guards remain mandatory.
- Preserve differences between model failure and harness/runtime failure.
- No production selection.

## Success condition

The run succeeds when APEX has a current, evidence-backed shortlist for the **high-reasoning bounded operator role** and concrete hypotheses about where reasoning strength helps, where it creates drift risk, and what WEEKLY/MA/INJECT fixtures must decide locally.
