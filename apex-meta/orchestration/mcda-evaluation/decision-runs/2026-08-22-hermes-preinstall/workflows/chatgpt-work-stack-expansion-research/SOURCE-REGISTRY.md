# Source Registry — Stack Expansion Research

Status: **SEED REGISTRY / MUST BE RE-VERIFIED DURING EACH TRACK**  
Date: 2026-08-23

This registry prevents source drift and candidate-name confusion. It is not permission to cite a URL without opening it. Every research track must re-open the current source and record the version/date/commit where decision-relevant.

## Methodology / research workflow

| ID | Source | Authority | Use |
|---|---|---|---|
| M01 | https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026 | UK Government | MCDA, swing weighting, sensitivity and transparent appraisal |
| M02 | https://www.nasa.gov/reference/6-8-decision-analysis/ | NASA | alternatives, criteria, uncertainty, sensitivity, evidence-based decision analysis |
| M03 | https://openai.com/chatgpt-work/ | OpenAI | Work execution model |
| M04 | https://help.openai.com/en/articles/20001066 | OpenAI | Skills behavior/standard |

## Existing Hermes baseline

| ID | Source | Authority | Use |
|---|---|---|---|
| H01 | https://github.com/NousResearch/hermes-agent | Official repository | current implementation/release/source |
| H02 | https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban | Official docs | durable task/review state |
| H03 | https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/ | Official docs | root/family/micro context discovery |
| H04 | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/ | Official docs | Agent Skills, precedence, trust |
| H05 | https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/ | Official docs | runtime memory |
| H06 | https://hermes-agent.nousresearch.com/docs/user-guide/features/curator | Official docs | procedural learning lifecycle |
| H07 | https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd | Official docs | QMD integration |
| H08 | https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a | Official docs | A2A interoperability; verify exact current support |
| H09 | https://hermes-agent.nousresearch.com/docs/integrations/providers | Official docs | provider/subscription/local execution paths |
| H10 | https://hermes-agent.nousresearch.com/docs/user-guide/security/ | Official docs | safety controls |

## BMAD / MarketingSkills / QMD baseline components

| ID | Source | Authority | Use |
|---|---|---|---|
| B01 | https://github.com/bmad-code-org/BMAD-METHOD | Official repository | BMAD package/current workflows |
| B02 | https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml | Official source | Hermes install target; re-open current main |
| MK01 | https://github.com/coreyhaines31/marketingskills | Official repository | MarketingSkills package |
| MK02 | https://github.com/coreyhaines31/marketingskills/blob/main/skills/product-marketing/SKILL.md | Official source | project marketing context behavior |
| Q01 | https://github.com/tobi/qmd | Official repository | QMD local retrieval/MCP implementation |

## CrewAI — locked identity `crewAIInc/crewAI`

| ID | Source | Authority | Use |
|---|---|---|---|
| C01 | https://github.com/crewAIInc/crewAI | Official repository | implementation, release/activity/license |
| C02 | https://docs.crewai.com | Official docs | crews, flows, agents, memory, knowledge, guardrails, deployment/integrations |
| C03 | https://docs.crewai.com/concepts/flows | Official docs | event/state/control-flow behavior; locate current canonical page if redirected |
| C04 | https://docs.crewai.com/concepts/crews | Official docs | role-based collaborative agents; locate current canonical page if redirected |
| C05 | https://github.com/crewAIInc/crewAI/search?q=A2A&type=code | Official source search | prove current A2A classes/roles; follow exact files, do not cite search result alone |
| C06 | https://github.com/crewAIInc/skills | Official CrewAI repository if current | coding-agent skills package; verify ownership/existence/current use before citing |

CrewAI vendor adoption/production claims are not operational proof by themselves. Search current releases, tests, official case studies and current issue/PR evidence relevant to the exact capability.

## Agency Agents — locked identity `msitarzewski/agency-agents`

| ID | Source | Authority | Use |
|---|---|---|---|
| A01 | https://github.com/msitarzewski/agency-agents | Official repository | roster, current state, license/activity |
| A02 | https://github.com/msitarzewski/agency-agents/blob/main/integrations/hermes/README.md | Official integration source | Hermes router plugin, lazy specialist loading, install path/tool surface |
| A03 | https://github.com/msitarzewski/agency-agents/issues | Official issue tracker | operational defects/limitations/current fixes |
| A04 | https://github.com/msitarzewski/agency-agents/actions | Official CI | current integration/test evidence where available |

The README currently describes a generated Hermes `agency-agents-router` with search/inspect/load/delegate tools and a lazily loaded roster. Re-open current main and verify generated count/schema/install behavior before using it in the matrix.

## Superpowers — locked identity `obra/superpowers`

| ID | Source | Authority | Use |
|---|---|---|---|
| S01 | https://github.com/obra/superpowers | Official repository | current methodology, installation, support |
| S02 | https://github.com/obra/superpowers/tree/main/skills | Official source | current skills/workflows |
| S03 | https://github.com/obra/superpowers/issues | Official issue tracker | Hermes install/tool-mapping/security-scan operational evidence |
| S04 | https://github.com/obra/superpowers/releases | Official releases | version/support timing |

Do not assume Hermes support from an old file/path. Search the current repository/release for Hermes support and inspect current open/closed issues that can falsify it. Superpowers is heavily software-development-oriented; non-software MoA fit must be proven by actual skill semantics, not brand/generalization.

## Semantic Router — locked identity `aurelio-labs/semantic-router`

| ID | Source | Authority | Use |
|---|---|---|---|
| SR01 | https://github.com/aurelio-labs/semantic-router | Official repository | architecture, releases, dependencies, license |
| SR02 | https://github.com/aurelio-labs/semantic-router/tree/main/docs | Official source/docs | routes/encoders/indexes/router types; locate current canonical docs |
| SR03 | https://github.com/aurelio-labs/semantic-router/releases | Official releases | maintenance/current version |
| SR04 | https://github.com/aurelio-labs/semantic-router/issues | Official issue tracker | operational limitations/security/dependency evidence |

Semantic Router is initially classified only as a routing component candidate. Research must prove an existing supported insertion point into the MoA stack; Python-callability alone does not establish Hermes integration.

## AnythingLLM — locked identity `Mintplex-Labs/anything-llm`

| ID | Source | Authority | Use |
|---|---|---|---|
| AL01 | https://github.com/Mintplex-Labs/anything-llm | Official repository | implementation, desktop/docker, release/activity/license |
| AL02 | https://docs.anythingllm.com | Official docs | workspaces/RAG/agents/flows/MCP/model routing/skills/scheduled jobs |
| AL03 | https://github.com/Mintplex-Labs/anything-llm/issues | Official issue tracker | workspace isolation, security, regressions, operational evidence |
| AL04 | https://github.com/Mintplex-Labs/anything-llm/releases | Official releases | current version/cadence |

Do not infer Hermes integration from shared MCP support. Determine whether AnythingLLM acts as MCP client/server for the relevant direction and whether Hermes exposes/consumes a compatible endpoint for the desired function. If not, classify as separate/duplicate application or `CUSTOM_REQUIRED`.

## Protocol standards used only when a candidate claims them

| ID | Source | Authority | Use |
|---|---|---|---|
| P01 | https://a2a-protocol.org/latest/ | A2A standard | exact peer/delegation protocol roles if CrewAI/Hermes path relies on A2A |
| P02 | https://modelcontextprotocol.io/specification | MCP standard | transport/tool/resource semantics only; does not prove product integration |
| P03 | https://agentskills.io/specification | Agent Skills standard | portable skill structure/activation contract |

## Source capture requirements

Each research result must include a source registry with:

```text
EVIDENCE_ID
URL
SOURCE_TYPE
PUBLISHER/OWNER
DATE_OR_COMMIT_OR_RELEASE
CLAIM_SUPPORTED
EXACT_EVIDENCE_LOCATION
CURRENTNESS_CHECK
LIMITATIONS
```

For GitHub operational evidence, record issue/PR status and date. An issue from an old version does not prove a current defect unless unresolved or reproduced/current release evidence supports it.
