# ChatGPT Work Research Launchers — R01 to R07

Use these launchers inside the ChatGPT Project `MoA — Hermes Pre-Install Research` with **Work** selected.

The Rxx file is the authoritative research specification. The launcher does not replace or summarize it.

## Common launcher

```text
Use ChatGPT Work for this research run.

Repository: leela-spec/MasterOfArts
Branch: main

AUTHORITATIVE TASK SPECIFICATION:
<RESEARCH_SPEC_PATH>

CURRENT DECISION CONTEXT:
- Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-002-full-functional-hermes-target.md
- Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml

Execute the full research specification at decision-grade, high level. Do not simplify away any required capability, but do not descend into implementation work that the specification does not need to answer the decision.

Before researching:
1. read the specification completely;
2. use Plan mode if available;
3. inspect the current repo areas the specification identifies;
4. propose the research plan, official source plan, main decision questions and expected result sections;
5. identify only ambiguities that would materially change the research;
6. wait for my approval.

After approval:
- use current official documentation/repositories for load-bearing claims;
- use GitHub for current MasterOfArts repo evidence rather than stale uploaded copies;
- distinguish VERIFIED_OFFICIAL / SUPPORTED_INFERENCE / OPEN / CONTRADICTED;
- identify the exact mechanism for every system connection;
- distinguish deterministic vs AI/hybrid execution where relevant;
- identify token/context/cost/privacy/data-egress implications where relevant;
- do not invent custom infrastructure;
- do not install or modify Hermes, QMD, BMAD, MarketingSkills or the repo structure;
- satisfy every Required output item and Pass standard in the authoritative specification.

Draft the complete result in this Work thread first.
Do not write to GitHub until the evidence review is complete and I approve persistence.

After approval to persist, save the accepted report to:
<RESULT_PATH>

Do not modify the research prompt itself or architecture/installation state.
```

---

## R01 — Hermes local safety guardrails

**Specification**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R01-HERMES-LOCAL-SAFETY-GUARDRAILS.md`

**Result**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R01-HERMES-LOCAL-SAFETY-GUARDRAILS-WORK-RESULT.md`

**Decision focus**  
Prove a low-friction, officially supported Hermes safety configuration for the local Windows/WSL environment that blocks/isolates meaningful host and credential risks without making normal Master of Arts work unusable.

---

## R02 — Macro / meso / micro project + knowledge structure

**Specification**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE.md`

**Result**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE-WORK-RESULT.md`

**Decision focus**  
Prove how Hermes' existing project/workspace/context/Kanban mechanisms map the real MasterOfArts repository into repeatable macro, meso and micro project contexts without inventing a new project or KB framework.

---

## R03 — Hermes + QMD + real repository

**Specification**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R03-HERMES-QMD-REPO-INTEGRATION.md`

**Result**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R03-HERMES-QMD-REPO-INTEGRATION-WORK-RESULT.md`

**Decision focus**  
Prove the actual official Hermes ↔ QMD ↔ MasterOfArts-file path, including Windows/WSL support, collection/project scoping, index refresh, exact query/result flow, token behavior, security and recovery.

---

## R04 — Project knowledge lifecycle

**Specification**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE.md`

**Result**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE-WORK-RESULT.md`

**Decision focus**  
Prove how current project information, decisions, source evidence, outputs, stale material and accepted knowledge stay usable and current through existing Hermes/repo/QMD mechanisms rather than a custom knowledge lifecycle.

---

## R05 — Specialist agents and skill priming

**Specification**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING.md`

**Result**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING-WORK-RESULT.md`

**Decision focus**  
Prove how reusable specialists receive shared role/skill instructions plus the correct organization, project-family and micro-project context without creating one copied specialist per project or manual context handoffs.

---

## R06 — Hermes continuous learning

**Specification**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R06-HERMES-CONTINUOUS-LEARNING.md`

**Result**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R06-HERMES-CONTINUOUS-LEARNING-WORK-RESULT.md`

**Decision focus**  
Prove what Hermes actually learns, where it persists, how Curator/skills/memory differ, how approved learning becomes reusable, and how runtime learning avoids becoming a competing source of project truth.

---

## R07 — MarketingSkills + Hermes integration

**Specification**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R07-MARKETINGSKILLS-HERMES-INTEGRATION.md`

**Result**  
`Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R07-MARKETINGSKILLS-HERMES-INTEGRATION-WORK-RESULT.md`

**Decision focus**  
Prove the upstream installation/discovery path and, especially, whether the same MarketingSkills installation can work correctly across multiple Master of Arts project contexts without product-marketing context leakage or overwrite.

---

# Recommended run order

Use dependencies rather than arbitrary parallelism:

```text
R01 Safety -----------------------------+
                                        |
R02 Project/knowledge model --> R03 QMD |
             |                          |
             +--> R04 Knowledge lifecycle
             +--> R05 Specialist priming --> R07 MarketingSkills
             +---------------------------> R06 Continuous learning

Accepted R01-R07
      |
      v
Integrated user-story simulation in QA-VALIDATION-RUNBOOK-v2.md
```

R01 and R02 can begin independently. R03 should consume the accepted R02 project-scope model. R04-R06 should use the accepted R02 result where it resolves project/context semantics. R07 should consume the accepted R05 priming model.

Do not let an earlier result silently become truth: downstream Work threads must cite the accepted result file and still re-check any upstream product capability whose current behavior is load-bearing.
