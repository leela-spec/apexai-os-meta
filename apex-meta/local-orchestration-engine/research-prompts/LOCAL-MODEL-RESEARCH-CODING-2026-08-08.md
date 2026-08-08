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

The goal is not to find a model that replaces Claude Code or Codex. Find current local configurations that are especially strong at the **bottom bounded portion of coding work**: exact patchspec execution, mechanical repair, tiny tested fixes, failure classification, minimal diffs and correct escalation when the problem exceeds local authority.

## Authority

Use Round-3 decisions LM-1..LM-5 as binding. The local coder may:

- execute exact patchspecs;
- repair known mechanical classes;
- make at most one tiny locally inferred fix inside the micro-fix envelope;
- inspect/stage/commit on `main` when explicitly granted;
- retrieve bounded context across declared roots;
- escalate ambiguous behavior, architecture, unknown regressions, security/permission issues and Git conflicts.

More coding skill does not grant broader authority.

## Research questions

For each serious candidate/configuration establish current evidence about:

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

Seek direct model cards, technical reports, official repositories and current runtime documentation first. Use independent coding-agent benchmarks only as secondary prioritization evidence.

## Candidate hypotheses

Compare:

1. strong general reasoning models used for bounded coding;
2. coding-specialized local models;
3. higher-reasoning stretch configurations that may reduce CLI escalation;
4. efficient models that may be sufficient for exact/mechanical work.

Do not decide in advance that APEX needs a separate coding model. Research whether any coding specialist is likely to earn the extra routing/load/maintenance complexity.

## APEX fixture mapping

All recommendations must map explicitly to:

- `CODE-01` test + failure classification;
- `CODE-02` exact mechanical patchspec;
- `CODE-03` tiny authorized inferred fix;
- `CODE-04` ambiguous bug where escalation is success;
- `CODE-05` bounded multi-repo operation.

For each candidate state which fixture appears strongest, weakest, and most uncertain.

## Safety emphasis

A coding model is not better merely because it fixes more tasks.

A candidate should be penalized for:

- editing outside declared files;
- changing public APIs without authorization;
- broad refactoring;
- multiple speculative repair attempts;
- masking failed tests;
- falsely declaring success;
- attempting destructive Git actions;
- failing to escalate architecture/ambiguity.

## Deliverables

1. executive finding;
2. current candidate/version table;
3. generalist-versus-code-specialist comparison;
4. evidence mapped to CODE-01..05;
5. scope/escalation-risk analysis;
6. structured/tool-use findings;
7. context requirements;
8. Windows/runtime/resource considerations;
9. shortlist for local bake-off;
10. hypotheses that the benchmark must falsify;
11. source appendix;
12. YAML:

```yaml
coding_model_research:
  evidence_date: null
  candidates: []
  benchmark_priority: []
  general_reasoning_candidates: []
  code_specialist_candidates: []
  stretch_candidates: []
  fixture_hypotheses:
    CODE_01: {}
    CODE_02: {}
    CODE_03: {}
    CODE_04: {}
    CODE_05: {}
  escalation_risks: {}
  context_findings: {}
  resource_findings: {}
  unknowns_for_local_test: []
  overall_confidence_0_to_100: null
```

## Boundaries

- No production model selection.
- No broad autonomous coding role.
- No assumption that coding leaderboards predict correct escalation.
- No branch-based workflow for this initiative unless the operator later changes the `main`-only policy.
- Keep benchmark claims distinct from public evidence.

## Success condition

The run succeeds when APEX has an evidence-backed shortlist capable of testing whether a coding-specialized or higher-reasoning local model **materially reduces routine Claude Code/Codex load without increasing scope drift, false success or missed escalation**.
