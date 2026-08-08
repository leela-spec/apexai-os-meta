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

The operator expects **~7–8B to be the practical optimum** for the main bounded executor. Research should determine whether that class has enough reasoning for constrained state interpretation, tool/action choice, browser recovery, evidence preparation, specialist-worker execution, hostile-content resistance and correct escalation while preserving laptop coexistence.

Smaller and larger models are comparators that may falsify the hypothesis; they are not the default research objective.

## Binding architecture

Round-3 LM-6..LM-22 are authority.

Key boundaries:

- Weekly graph/work packet owns sequence;
- local model classifies only among declared states and may return `UNKNOWN`;
- multi-turn browser work follows predeclared follow-up classes;
- job state is externally durable and resumable;
- Meta Ops retains Multi-Agent orchestration;
- local worker may create candidate artifacts but never verify/promote them;
- Detective support is evidence/anomaly collection, not verdict;
- hostile source/browser/model/tool content is untrusted data;
- typed escalation is routed by enforced policy.

## Candidate comparison

Research primarily:

1. strong current **~7–8B general/instruction/tool models**;
2. **~3–4B efficiency controls** to quantify what is lost or retained at lower resource cost;
3. **~12–14B challengers** when local deployment is credible and the extra reasoning may solve specific Weekly/MA failures;
4. larger models only when concrete hardware/runtime evidence makes them locally plausible and decision-relevant.

## Research questions

For each serious candidate determine current evidence about:

- instruction fidelity under multi-step work packets;
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
Assess suitability for INJECT-01..08 while keeping hard containment outside the model.

## Practical-center reasoning lens

Test three concrete hypotheses:

1. **~7–8B vs ~3–4B:** does the practical-center class materially improve `UNKNOWN` recognition, recovery judgement, escalation routing, evidence comparison and hostile-content handling?
2. **~7–8B vs ~12–14B:** do larger challengers materially improve the bounded role, or mostly consume more shared resources for small gains?
3. **Capability vs drift:** does greater model capability increase willingness to solve beyond the packet, and if so can the external harness reliably contain it?

Do not assume either that bigger is better or that 7–8B wins. Make the local APEX fixtures decide.

## Deliverables

1. executive finding;
2. current candidate/version map;
3. primary ~7–8B shortlist;
4. smaller/larger comparator table;
5. WEEKLY-01..06 evidence/hypothesis matrix;
6. MA-01..06 evidence/hypothesis matrix;
7. injection-resistance findings;
8. size/reasoning versus authority-drift comparison;
9. context and retrieval implications;
10. browser/tool implications;
11. resource/coexistence implications;
12. shortlist for APEX bake-off;
13. unknowns requiring local trials;
14. source appendix;
15. YAML:

```yaml
weekly_multiagent_model_research:
  evidence_date: null
  primary_7_8b_candidates: []
  smaller_controls: []
  larger_challengers: []
  benchmark_priority: []
  weekly_fixture_hypotheses: {}
  multiagent_fixture_hypotheses: {}
  injection_findings: {}
  size_tradeoff_hypotheses: {}
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
- Do not treat model self-confidence as a validity signal.
- Do not treat prompt-injection resistance as sufficient containment.
- Preserve differences between model failure and harness/runtime failure.
- **Do not replace the 7–8B practical-center prior with a largest-model search.**
- No production selection.

## Success condition

The run succeeds when APEX has a **7–8B-centered shortlist** and concrete evidence hypotheses showing what smaller controls or larger challengers would have to demonstrate to displace that expected optimum for Weekly or Multi-Agent execution.
