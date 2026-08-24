# ChatGPT Work Autonomous Stack Expansion Research Launcher

Status: **AUTHORITATIVE PROGRAM LAUNCHER**  
Date: 2026-08-23

Use this as the first message in one ChatGPT Work session.

```text
@GitHub

Run the complete Master of Arts Hermes stack expansion research program autonomously.

Repository: leela-spec/MasterOfArts
Branch: main

AUTHORITATIVE WORKFLOW DIRECTORY:
Orchestration/decision-runs/2026-08-22-hermes-preinstall/workflows/chatgpt-work-stack-expansion-research/

First read completely:
- README.md
- PROJECT-INSTRUCTIONS.md
- state.yaml
- SOURCE-REGISTRY.md
- MATRIX-SCHEMA.yaml
- REVIEW-PROTOCOL.md

CURRENT BASELINE CONTEXT:
- Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-002-full-functional-hermes-target.md
- Orchestration/decision-runs/2026-08-22-hermes-preinstall/workflows/chatgpt-work-research/state.yaml
- completed R01-R07 results under Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/

RESEARCH PROGRAM:
- R00 research/R00-VERIFIED-CURRENT-PIPELINE-BASELINE.md
- R01 research/R01-GENERAL-ALTERNATIVE-LANDSCAPE.md
- R02 research/R02-CREWAI-INTEGRATION-AND-FIT.md
- R03 research/R03-AGENCY-AGENTS-INTEGRATION-AND-FIT.md
- R04 research/R04-SUPERPOWERS-INTEGRATION-AND-FIT.md
- R05 research/R05-SEMANTIC-ROUTER-INTEGRATION-AND-FIT.md
- R06 research/R06-ANYTHINGLLM-INTEGRATION-AND-FIT.md
- R07 research/R07-EVIDENCE-MATRIX-V1.md
- R08 research/R08-ADVERSARIAL-EVIDENCE-AUDIT.md
- R09 research/R09-SOPHISTICATED-V2-SYNTHESIS.md

EXECUTION ORDER:
1. Execute R00 completely. It establishes what the existing Hermes stack has actually proven, what still needs configuration, and what remains a pilot/inference.
2. Execute R01 using R00 plus current web research to frame the alternatives and module boundaries. Do not make a final recommendation yet.
3. Execute R02-R06. Run them in parallel only if Work can do that natively without losing source/repo discipline; otherwise sequence them autonomously.
4. Execute R07 only after R02-R06 have accepted results.
5. Execute R08 as an adversarial re-verification of every decision-changing matrix cell and integration edge.
6. If R08 requires revisions, revise R07 evidence/matrix conclusions before proceeding.
7. Execute R09 last and produce the sophisticated v2 recommendation.

PER-TRACK LOOP:
- read the complete specification;
- inspect only the current repo material required;
- search the current web;
- use official sources for load-bearing claims;
- verify implementation/integration paths, not marketing language;
- distinguish technical existence from established operational value;
- produce a complete result;
- run REVIEW-PROTOCOL.md;
- revise and re-review automatically until PASS or BLOCK;
- persist the result to the exact path in state.yaml;
- continue to unlocked downstream research.

MATRIX LAW:
Every substantive matrix cell must cite current evidence. If no evidence exists, mark the cell OPEN/UNVERIFIED. Do not fill gaps using model logic.

For every integration edge record:
from | to | exact mechanism | transport/protocol | local/remote | auth/API | deterministic/AI/hybrid | persistent state | data egress | integration class | source

Do not claim two systems integrate merely because both expose a generic protocol. Verify the actual supported roles on both sides.

CANDIDATE IDENTITIES:
- CrewAI: crewAIInc/crewAI + docs.crewai.com
- Agency Agents: msitarzewski/agency-agents
- Superpowers: obra/superpowers
- Semantic Router: aurelio-labs/semantic-router
- AnythingLLM: Mintplex-Labs/anything-llm + docs.anythingllm.com

AUTONOMY:
Do not stop for routine planning, source selection, web search, repository inspection, evidence review, revision, scoring preparation, or persistence of designated result files.

Pause only if:
- required access cannot be recovered;
- candidate identity is genuinely ambiguous;
- authoritative evidence conflicts in a decision-changing way;
- a security/privacy choice requires operator consent;
- the next action would install software, modify production architecture, migrate project data, or change ADR-002;
- the product UI requires explicit permission.

Ordinary uncertainty is not a reason to stop. Preserve uncertainty and continue when it does not change the decision.

FULL-FUNCTION / NO-INVENTION:
Do not make a candidate look viable by reducing the Master of Arts requirement.
Do not design custom glue, wrappers, routers, sync layers, or databases to connect candidates.
If a useful feature requires custom integration, mark CUSTOM_REQUIRED and assess it accordingly.

FINAL R09 OUTPUT MUST INCLUDE:
- plain-language recommendation;
- exact module-by-module KEEP / ADD_NOW / PILOT / REPLACE / DEFER / REJECT decisions;
- current baseline vs recommended v2 stack flowchart;
- exact verified integration mechanism for every retained added component;
- components that duplicate existing responsibility;
- maturity/operational-evidence assessment;
- model/API/subscription/local execution consequences;
- token/context implications;
- security/privacy implications;
- Windows/WSL implications;
- user-story comparison;
- MCDA result with swing-weight/sensitivity logic;
- switching conditions and unresolved evidence gaps;
- explicit statement of whether any recommendation requires custom infrastructure.

Do not install anything and do not authorize installation.

Begin now and run the full program through R09 unless a genuine human decision gate is reached.
```

## Dependency graph

```text
R00 Verified baseline
      |
      v
R01 General landscape
      |
      +--> R02 CrewAI
      +--> R03 Agency Agents
      +--> R04 Superpowers
      +--> R05 Semantic Router
      +--> R06 AnythingLLM
              |
              v
        R07 Matrix V1
              |
              v
        R08 Adversarial audit
              |
              v
        R09 Sophisticated V2 synthesis
```
