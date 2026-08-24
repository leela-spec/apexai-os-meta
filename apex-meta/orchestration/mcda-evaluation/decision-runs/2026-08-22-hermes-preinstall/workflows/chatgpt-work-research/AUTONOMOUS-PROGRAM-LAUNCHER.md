# ChatGPT Work Autonomous Research Program Launcher

Status: **AUTHORITATIVE PROGRAM LAUNCHER**  
Date: 2026-08-23  
Repository: `leela-spec/MasterOfArts`  
Branch: `main`

Use this as the first message in one ChatGPT Work session inside the Project `MoA — Hermes Pre-Install Research`.

```text
Run the complete Master of Arts Hermes pre-install research program autonomously.

Repository: leela-spec/MasterOfArts
Branch: main

AUTHORITATIVE WORKFLOW FILES:
- Orchestration/decision-runs/2026-08-22-hermes-preinstall/workflows/chatgpt-work-research/PROJECT-INSTRUCTIONS.md
- Orchestration/decision-runs/2026-08-22-hermes-preinstall/workflows/chatgpt-work-research/state.yaml

CURRENT DECISION CONTEXT:
- Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-002-full-functional-hermes-target.md
- Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml

RESEARCH SPECIFICATIONS:
- R01: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R01-HERMES-LOCAL-SAFETY-GUARDRAILS.md
- R02: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE.md
- R03: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R03-HERMES-QMD-REPO-INTEGRATION.md
- R04: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE.md
- R05: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING.md
- R06: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R06-HERMES-CONTINUOUS-LEARNING.md
- R07: Orchestration/decision-runs/2026-08-22-hermes-preinstall/research/R07-MARKETINGSKILLS-HERMES-INTEGRATION.md

EXECUTION MODEL:
1. Read the common instructions and current decision context.
2. Read all seven research specifications and build the dependency graph.
3. Execute every research track autonomously in dependency order.
4. R01 and R02 are independent roots. Run them in parallel if Work can do that natively; otherwise run them sequentially without asking me which one to do first.
5. After R02 is complete, execute R03, R04, R05 and R06 using the accepted R02 findings where relevant.
6. Execute R07 after R05.
7. For each track:
   - inspect only the repo areas needed by that specification;
   - research current official upstream sources;
   - produce the complete decision-grade result;
   - run an evidence/coverage review against the specification and cited official sources;
   - if the review says REVISE, correct the result and re-review automatically;
   - if the result reaches PASS, persist it to its designated research-results/chatgpt-work path;
   - update the workflow status for that track if the available GitHub permissions allow it.
8. After all non-blocked tracks are complete, run a cross-track consistency review.
9. Produce a final synthesis for the existing QA-VALIDATION-RUNBOOK-v2.md. Do not authorize installation.

AUTONOMY RULE:
Do not stop for routine plan approval, source selection, repo inspection, evidence review, revisions, or persistence of designated research result files.

Pause and ask me only when one of these decision gates occurs:
- required repository/plugin/web access is unavailable and cannot be resolved by retrying or using an already-authorized equivalent route;
- official evidence shows a locked Hermes target component cannot perform a required function;
- a required connection would need custom infrastructure prohibited by ADR-002;
- a security/privacy decision requires me to accept materially broader host access or data egress;
- two authoritative sources materially contradict each other and the choice changes the architecture;
- the research would change ADR-002, authorize installation, migrate/reorganize project data, install software, or modify production architecture;
- a platform permission dialog requires my explicit confirmation.

Ordinary uncertainty is not a reason to stop. Record it, research it, and continue if the remaining uncertainty does not change the decision.

EVIDENCE RULES:
- Use current official documentation, official repositories/releases/source, official package/catalog documentation, and first-party examples for load-bearing claims.
- Do not rely on model memory for changing claims.
- Classify important findings as VERIFIED_OFFICIAL / SUPPORTED_INFERENCE / OPEN / CONTRADICTED.
- For every system linkage record: from | to | exact mechanism | local/remote | API/network | deterministic/AI/hybrid | persistent state/output | data egress | native/official/package/config/custom | source.
- Never invent a connection because it appears technically plausible.

FULL-FUNCTION RULE:
Do not replace a required capability with a toy, MVP, manually pasted handoff, small script, reduced simulation, or custom subsystem. If the complete required behavior is unsupported upstream, mark it as a blocker.

PERSISTENCE:
Persist PASS results automatically to the exact result paths defined in the workflow state. Do not overwrite the research specifications. Do not change ADR-002 or authorize installation.

FINAL OUTPUT:
When the autonomous program completes, return:
- track status R01-R07;
- PASS/BLOCK per track;
- decision-changing findings;
- cross-track contradictions;
- remaining human decisions;
- whether the complete Hermes target is ready for the interactive QA realization run;
- links/paths to every persisted result.

Begin now. Do not wait for a plan approval unless one of the explicit decision gates above is already triggered.
```

## Dependency graph

```text
R01 Safety ------------------------------+
                                         |
R02 Project/knowledge model --> R03 QMD  |
             |                           |
             +--> R04 Knowledge lifecycle
             +--> R05 Specialist priming --> R07 MarketingSkills
             +--> R06 Continuous learning

All completed tracks
        |
        v
Cross-track consistency review
        |
        v
QA-VALIDATION-RUNBOOK-v2 synthesis handoff
```

R01 and R02 are not operator checkpoints. They are simply the two dependency roots that can start immediately.