---
title: "Local Model Research Prompt — Bounded Coding Execution"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
prompt_standard: apex-meta/SmallSkills/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md
authority:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
---

# Research Prompt B — Bounded Coding Execution

## Target

Research and produce a **coding-execution candidate packet** for the APEX local execution layer.

The goal is not to replace Claude Code or Codex. Find current local configurations that are strong at the bounded bottom portion of coding work: exact patchspec execution, mechanical repair, tiny tested fixes, failure classification, minimal diffs and correct escalation.

The operator expects **~7–8B to be the practical center**. Test whether that class provides enough coding reasoning to absorb routine CLI work without the resource cost of larger models.

## Authority

Use Round-3 LM-1..LM-5 as binding. The local coder may:

- execute exact patchspecs;
- repair known mechanical classes;
- make at most one tiny locally inferred fix inside the micro-fix envelope;
- inspect/stage/commit on `main` when explicitly granted;
- retrieve bounded context across declared roots;
- escalate ambiguous behavior, architecture, unknown regressions, security/permission issues and Git conflicts.

More coding skill does not grant broader authority.

## Candidate comparison

Center research on:

1. **strong current ~7–8B general models** for bounded coding;
2. **~7–8B coding-specialized models** where credible;
3. **~3–4B efficiency controls** to determine whether 7–8B materially improves tiny-fix and escalation behavior;
4. **~12–14B challengers** only when practical local deployment appears realistic and the extra capability may materially reduce CLI escalation;
5. larger configurations only when concrete evidence makes them decision-relevant on this hardware.

Do not decide in advance that APEX needs a separate coding model.

## Research questions

For each serious configuration establish current evidence about:

- patch/instruction adherence;
- code-edit precision and unwanted-diff tendency;
- repository/tool use;
- test/log interpretation;
- structured output and action selection;
- coding reasoning under bounded context;
- ability to stop/escalate rather than confidently continue;
- long-context coding behavior where documented;
- local deployment artifacts and runtimes;
- memory/latency implications on ~32 GB Windows hardware.

Use direct model cards, technical reports, official repositories and current runtime documentation first. Independent coding-agent benchmarks are secondary prioritization evidence.

## APEX fixture mapping

Map recommendations explicitly to:

- `CODE-01` test + failure classification;
- `CODE-02` exact mechanical patchspec;
- `CODE-03` tiny authorized inferred fix;
- `CODE-04` ambiguous bug where escalation is success;
- `CODE-05` bounded multi-repo operation.

For each candidate state which fixture appears strongest, weakest and most uncertain.

Explicitly compare:

- does ~7–8B materially reduce errors/missed escalation versus ~3–4B?
- does ~12–14B materially outperform the best ~7–8B candidate on the actual bounded role?
- is any larger-model gain worth its additional loading, memory and coexistence cost?

## Safety emphasis

A coding model is not better merely because it fixes more tasks.

Penalize:

- editing outside declared files;
- public-API changes without authorization;
- broad refactoring;
- multiple speculative repair attempts;
- masking failed tests;
- false success;
- destructive Git attempts;
- failure to escalate architecture/ambiguity.

## Deliverables

1. executive finding;
2. current candidate/version table;
3. primary ~7–8B generalist-versus-code-specialist comparison;
4. smaller and larger comparator table;
5. evidence mapped to CODE-01..05;
6. scope/escalation-risk analysis;
7. structured/tool-use findings;
8. context requirements;
9. Windows/runtime/resource considerations;
10. shortlist for local bake-off;
11. hypotheses the benchmark must falsify;
12. source appendix;
13. YAML:

```yaml
coding_model_research:
  evidence_date: null
  primary_7_8b_candidates: []
  code_specialist_candidates: []
  smaller_controls: []
  larger_challengers: []
  benchmark_priority: []
  fixture_hypotheses:
    CODE_01: {}
    CODE_02: {}
    CODE_03: {}
    CODE_04: {}
    CODE_05: {}
  escalation_risks: {}
  size_tradeoff_hypotheses: {}
  context_findings: {}
  resource_findings: {}
  unknowns_for_local_test: []
  overall_confidence_0_to_100: null
```

## Boundaries

- No production model selection.
- No broad autonomous coding role.
- Do not assume coding leaderboards predict correct escalation.
- **Do not silently substitute a larger-model optimization goal for the 7–8B practical-center hypothesis.**
- No branch-based workflow for this initiative unless the operator later changes the `main`-only policy.

## Success condition

The run succeeds when APEX has a **7–8B-centered coding shortlist** plus the minimum smaller/larger comparators needed to test whether another class materially reduces routine Claude Code/Codex load without increasing scope drift, false success or missed escalation.
