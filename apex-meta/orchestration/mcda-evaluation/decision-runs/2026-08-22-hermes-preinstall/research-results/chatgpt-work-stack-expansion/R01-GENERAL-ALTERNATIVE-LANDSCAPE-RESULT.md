# R01 — General Alternative Landscape — Result

Date: 2026-08-23  
Verdict: **INDIVIDUAL_RESEARCH_READY**  
Review: **PASS**

## Candidate taxonomy

| Candidate | Primary role | Plausible MoA entry point | Preliminary finding |
|---|---|---|---|
| CrewAI | workflow/runtime framework | bounded event-driven Flow exposed by A2A | technically substantial, but duplicates runtime/state/model layers |
| Agency Agents | specialist package + official Hermes plugin | lazy search/load of missing specialist prompts | strongest direct supplement hypothesis; quality and delegation need QA |
| Superpowers | software-development workflow-method package | selected Hermes skills | heavy BMAD/review overlap and software bias; current Hermes issue matters |
| Semantic Router | routing component/library | measured semantic routing bottleneck | no selected-stack integration; custom wrapper required |
| AnythingLLM | knowledge/RAG UI and agent application | separate human-facing UI, or QMD tools through MCP | second UI/runtime/state plane; freshness and ownership are central risks |

## Preliminary module matrix

`V` verified capability, `I` verified/official integration, `D` duplication, `O` open, `C` custom required, `—` no fit.

| Baseline module | CrewAI | Agency Agents | Superpowers | Semantic Router | AnythingLLM |
|---|---|---|---|---|---|
| Hermes runtime/orchestration | V/D | supplement | method only | C | D |
| Kanban task/review state | Flow persistence V/D | uses Hermes | method overlap | — | agent-flow D |
| Hierarchical repo context | manual knowledge/input | selected prompt only | skill bootstrap | route utterances only | workspace ingestion D |
| Profiles/specialists | agents V/D | I, roster | development roles | routing only | workspace agents D |
| BMAD/workflow methods | D | some persona overlap | strong D | — | flow overlap |
| MarketingSkills | — | roster overlap | — | — | skills overlap O |
| QMD retrieval | knowledge V/D | uses current context | — | index D | MCP client I; native RAG D |
| Memory/learning | memory V/D | static upstream definitions | — | route/index state | workspace/chat memory D |
| Provider/model execution | own providers D | Hermes-owned | Hermes-owned | optional LLM | own providers D |

## Verified integration surfaces

| Edge | Evidence | Class | Limitation |
|---|---|---|---|
| Hermes ↔ CrewAI | both publish A2A client/server behavior | OFFICIAL_PROTOCOL_BOTH_SIDES | Hermes documents A2A v1.0 while CrewAI exposes configurable/default 0.3.0; exact cross-version live path is OPEN pending QA |
| Hermes ↔ Agency Agents | first-party generated router plugin and install instructions | OFFICIAL_PLUGIN | search/load are source-verifiable; optional `toolsets` delegation argument may not match current Hermes naming |
| Hermes ↔ Superpowers | first-party Hermes plugin manifest/bootstrap | OFFICIAL_PLUGIN | current main carries stale Hermes tool names reported in open issue #2157 |
| Hermes ↔ Semantic Router | none found | CUSTOM_REQUIRED | a Python service/wrapper and ownership rules would have to be designed |
| Hermes ↔ AnythingLLM | none found | NO_INTEGRATION_FOUND | shared files are not an integration |
| AnythingLLM → QMD | AnythingLLM MCP client plus QMD MCP server | OFFICIAL_PROTOCOL_BOTH_SIDES | generic protocol edge, not a product-specific recipe; exact config/runtime QA needed |

## Maturity and value evidence

| Candidate | Current evidence | What it does not prove |
|---|---|---|
| CrewAI | active repository, package, extensive docs/tests; Crews, Flows, persistence, memory/knowledge/MCP/A2A | vendor “production-ready” language and adoption do not prove MoA value or recovery quality |
| Agency Agents | 270 generated agents and current first-party Hermes builder/checker | checker does not execute live Hermes delegation; roster count does not prove role quality |
| Superpowers | v6.3.0, tests and official Hermes plugin | code-focused methodology is not evidence of non-software fit; open compatibility issue limits reliability |
| Semantic Router | v0.1.16, maintained library, local/remote encoders/indexes | library capability is not a Hermes integration or proof routing is currently deficient |
| AnythingLLM | v1.16.0, desktop/server product, RAG, agents, flows, MCP client | adoption does not prove repo freshness, QMD replacement value or cross-workspace isolation for MoA |

## Substitution and duplication map

- CrewAI would duplicate orchestration, task/flow persistence, agents, memory, knowledge and provider execution unless isolated to one bounded workflow.
- Agency Agents duplicates some specialist prompts but can remain derived/on-demand; Hermes still owns task, review and project context.
- Superpowers duplicates BMAD planning/review and imposes a code/TDD/branch workflow not aligned to most MoA work.
- Semantic Router adds a new route/index/config state and code service while Hermes already routes through tasks, profiles and skills.
- AnythingLLM native ingestion creates another document/vector/workspace state; using QMD via MCP avoids a second vector index but still adds an application runtime and chat/workspace state.

## Cross-cutting constraints

| Candidate | Models/cost | Local/privacy | Windows/WSL | Maintenance |
|---|---|---|---|---|
| CrewAI | provider API or local model; no direct Codex-subscription OAuth evidence | local Ollama possible; telemetry/cloud optional | Python 3.10–3.13 path | second Python runtime, DBs and workflow definitions |
| Agency Agents | Hermes provider calls only; delegation adds calls | prompt package is local | Hermes/WSL path | plugin + generated roster updates |
| Superpowers | Hermes provider calls; extra mandatory methodology context | local skills | Hermes/WSL path | plugin updates; current mapping drift |
| Semantic Router | static local encoder can avoid LLM; dynamic routes add calls | local encoder/index possible | Python service burden | custom wrapper/config/index |
| AnythingLLM | own provider/API keys or local models; no subscription-OAuth evidence | desktop/server and local models available | native Windows desktop or Docker | separate app, DB/vector index, backups, permissions |

## Decision-changing R02–R06 questions

1. CrewAI: exact A2A roles/version compatibility; state/review ownership; whether any bounded workflow earns a second runtime.
2. Agency Agents: lazy context behavior, representative content quality, and current delegation argument compatibility.
3. Superpowers: whether current issue #2157 affects main and whether useful non-software methods remain after overlap removal.
4. Semantic Router: whether an official edge exists and whether current routing failures are measured.
5. AnythingLLM: MCP direction, file refresh/delete behavior, isolation/security, and whether any UI need justifies another control plane.

## Sources

- L-HERMES-A2A — [Hermes A2A](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a).
- L-CREW — [CrewAI repository](https://github.com/crewAIInc/crewAI/tree/f4731f5025f861c78e3af0487cc80bf5e7c64782).
- L-AGENCY — [Agency Agents Hermes integration](https://github.com/msitarzewski/agency-agents/tree/ebe9c99acb5c96f9468de368d8bead775387d1a7/integrations/hermes).
- L-SUPER — [Superpowers at audited main](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797).
- L-SEM — [Semantic Router at audited main](https://github.com/aurelio-labs/semantic-router/tree/a4576168d9589397a7e0c6ff77f5d05469a56e2e).
- L-ANY — [AnythingLLM at audited master](https://github.com/Mintplex-Labs/anything-llm/tree/72aabbd15481ae405434efd4c83d46026eef1173).

No final winner is selected here. The detailed tracks can falsify each entry-point hypothesis. **PASS**.
