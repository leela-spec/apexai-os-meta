# R07 — Evidence Matrix V1 + Preliminary Recommendation — Result

Date: 2026-08-23  
Verdict: **V1_READY_FOR_ADVERSARIAL_AUDIT**  
Review: **PASS**

## Matrix notation and source keys

Each cell is `role / evidence-status / integration-class / evidence IDs / confidence`. `A` means direct current source, `B` means multiple strong sources, `C` means supported but live-unproven, `D` means open/vendor-only. Cross-cutting local/API/state/egress/context/platform consequences follow the full matrix and apply to every substantive cell for that candidate.

Keys: `B` R00 baseline sources; `C` CrewAI current repo/docs; `A` Agency current repo/plugin; `S` Superpowers current repo/issue; `SR` Semantic Router current repo; `AL` AnythingLLM current repo/docs/source.

## Complete capability matrix

| Dimension | Current Hermes stack | CrewAI | Agency Agents | Superpowers | Semantic Router | AnythingLLM |
|---|---|---|---|---|---|---|
| orchestration runtime | KEEP/VERIFIED_CAPABILITY/NATIVE/B-HERMES/B | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/C-REPO/B | SUPPLEMENT/VERIFIED_INTEGRATION/OFFICIAL_PLUGIN/A-HERMES/B | NO_FIT/VERIFIED_LIMITATION/OFFICIAL_PLUGIN/S-ISSUE/A | NO_FIT/OPEN/CUSTOM_REQUIRED/SR-REPO/A | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/B |
| durable task state and recovery | KEEP/VERIFIED_CAPABILITY/NATIVE/B-KANBAN/B | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/C-FLOWS/B | SUPPLEMENT/VERIFIED_INTEGRATION/OFFICIAL_PLUGIN/A-BUILDER/C | NO_FIT/OPEN/NOT_APPLICABLE/S-REPO/C | NO_FIT/OPEN/NOT_APPLICABLE/SR-REPO/A | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/C |
| macro/meso/micro context | KEEP/VERIFIED_CAPABILITY/DOCUMENTED_CONFIGURATION/B-ADR/C | DUPLICATE/VERIFIED_LIMITATION/ESTABLISHED/C-KNOWLEDGE/C | SUPPLEMENT/VERIFIED_INTEGRATION/OFFICIAL_PLUGIN/A-BUILDER/C | ORTHOGONAL/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/S-USING/C | NO_FIT/OPEN/CUSTOM_REQUIRED/SR-REPO/A | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/C |
| project knowledge truth | KEEP/VERIFIED_CAPABILITY/NATIVE/B-ADR/A | DUPLICATE/VERIFIED_LIMITATION/ESTABLISHED/C-KNOWLEDGE/B | ORTHOGONAL/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/A-REPO/B | ORTHOGONAL/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/S-REPO/B | NO_FIT/OPEN/NOT_APPLICABLE/SR-REPO/A | DUPLICATE/VERIFIED_LIMITATION/ESTABLISHED/AL-SYNC/A |
| retrieval and RAG | KEEP/VERIFIED_INTEGRATION/OFFICIAL_PLUGIN/B-QMD/C | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/C-KNOWLEDGE/B | ORTHOGONAL/OPEN/NOT_APPLICABLE/A-REPO/C | NO_FIT/OPEN/NOT_APPLICABLE/S-REPO/A | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/SR-REPO/B | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/B; SUPPLEMENT/VERIFIED_INTEGRATION/OFFICIAL_PROTOCOL_BOTH_SIDES/AL-MCP/C |
| reusable specialist agents | KEEP/VERIFIED_CAPABILITY/NATIVE/B-ADR/C | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/C-REPO/B | SUPPLEMENT/VERIFIED_INTEGRATION/OFFICIAL_PLUGIN/A-HERMES/B | DUPLICATE/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/S-REPO/C | NO_FIT/OPEN/CUSTOM_REQUIRED/SR-REPO/A | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/C |
| workflow method library | KEEP/VERIFIED_CAPABILITY/ESTABLISHED/B-ADR/C | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/C-FLOWS/B | SUPPLEMENT/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/A-REPO/C | DUPLICATE/VERIFIED_LIMITATION/OFFICIAL_PLUGIN/S-ISSUE/A | NO_FIT/OPEN/NOT_APPLICABLE/SR-REPO/A | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/C |
| marketing capabilities | KEEP/VERIFIED_CAPABILITY/ESTABLISHED/B-ADR/C | OPEN/OPEN/NOT_APPLICABLE/C-REPO/D | SUPPLEMENT/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/A-REPO/C | NO_FIT/OPEN/NOT_APPLICABLE/S-REPO/A | NO_FIT/OPEN/CUSTOM_REQUIRED/SR-REPO/A | OPEN/OPEN/NOT_APPLICABLE/AL-REPO/D |
| semantic routing | KEEP/SUPPORTED_INFERENCE/NATIVE/B-ADR/C | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/C-REPO/C | SUPPLEMENT/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/A-BUILDER/B | ORTHOGONAL/OPEN/NOT_APPLICABLE/S-REPO/A | REPLACE/VERIFIED_CAPABILITY/CUSTOM_REQUIRED/SR-REPO/A | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/C |
| learning and memory | KEEP/VERIFIED_CAPABILITY/DOCUMENTED_CONFIGURATION/B-ADR/C | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/C-MEMORY/B | ORTHOGONAL/VERIFIED_LIMITATION/OFFICIAL_PLUGIN/A-REPO/B | NO_FIT/OPEN/NOT_APPLICABLE/S-REPO/A | NO_FIT/OPEN/NOT_APPLICABLE/SR-REPO/A | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/C |
| maker/reviewer separation | KEEP/VERIFIED_CAPABILITY/NATIVE/B-KANBAN/C | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/C-HUMAN/C | ORTHOGONAL/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/A-HERMES/C | DUPLICATE/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/S-REPO/C | NO_FIT/OPEN/NOT_APPLICABLE/SR-REPO/A | DUPLICATE/OPEN/ESTABLISHED/AL-REPO/D |
| deterministic validation | KEEP/VERIFIED_CAPABILITY/NATIVE/B-ADR/C | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/C-REPO/C | SUPPLEMENT/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/A-CHECK/B | DUPLICATE/VERIFIED_CAPABILITY/OFFICIAL_PLUGIN/S-REPO/C | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/SR-REPO/B | OPEN/OPEN/ESTABLISHED/AL-REPO/D |
| provider/subscription path | KEEP/VERIFIED_CAPABILITY/NATIVE/B-PROVIDERS/B | DUPLICATE/VERIFIED_LIMITATION/ESTABLISHED/C-REPO/C | KEEP/VERIFIED_INTEGRATION/OFFICIAL_PLUGIN/A-HERMES/B | KEEP/VERIFIED_INTEGRATION/OFFICIAL_PLUGIN/S-HERMES/C | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/SR-REPO/C | DUPLICATE/VERIFIED_LIMITATION/ESTABLISHED/AL-REPO/C |
| local model support | KEEP/VERIFIED_CAPABILITY/NATIVE/B-PROVIDERS/B | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/C-REPO/B | KEEP/VERIFIED_INTEGRATION/OFFICIAL_PLUGIN/A-HERMES/B | KEEP/VERIFIED_INTEGRATION/OFFICIAL_PLUGIN/S-HERMES/C | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/SR-REPO/B | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/B |
| security and permissions | KEEP/VERIFIED_CAPABILITY/DOCUMENTED_CONFIGURATION/B-ADR/C | DUPLICATE/VERIFIED_CAPABILITY/ESTABLISHED/C-A2A/C | SUPPLEMENT/VERIFIED_LIMITATION/OFFICIAL_PLUGIN/A-HERMES/C | DUPLICATE/VERIFIED_LIMITATION/OFFICIAL_PLUGIN/S-ISSUE/A | DUPLICATE/VERIFIED_LIMITATION/CUSTOM_REQUIRED/SR-REPO/B | DUPLICATE/VERIFIED_LIMITATION/ESTABLISHED/AL-SECURITY/B |
| Windows/WSL support | KEEP/SUPPORTED_INFERENCE/DOCUMENTED_CONFIGURATION/B-ADR/C | SUPPLEMENT/SUPPORTED_INFERENCE/ESTABLISHED/C-REPO/C | KEEP/SUPPORTED_INFERENCE/OFFICIAL_PLUGIN/A-HERMES/C | KEEP/SUPPORTED_INFERENCE/OFFICIAL_PLUGIN/S-HERMES/C | SUPPLEMENT/SUPPORTED_INFERENCE/ESTABLISHED/SR-PROJECT/C | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/B |
| web-AI artifact portability | KEEP/VERIFIED_CAPABILITY/NATIVE/B-ADR/A | ORTHOGONAL/SUPPORTED_INFERENCE/ESTABLISHED/C-REPO/C | ORTHOGONAL/SUPPORTED_INFERENCE/OFFICIAL_PLUGIN/A-HERMES/C | ORTHOGONAL/SUPPORTED_INFERENCE/OFFICIAL_PLUGIN/S-REPO/C | NO_FIT/OPEN/NOT_APPLICABLE/SR-REPO/A | DUPLICATE/VERIFIED_LIMITATION/ESTABLISHED/AL-REPO/C |
| setup/maintenance burden | KEEP/SUPPORTED_INFERENCE/DOCUMENTED_CONFIGURATION/B-ADR/C | DUPLICATE/VERIFIED_LIMITATION/ESTABLISHED/C-REPO/B | SUPPLEMENT/SUPPORTED_INFERENCE/OFFICIAL_PLUGIN/A-HERMES/C | DUPLICATE/VERIFIED_LIMITATION/OFFICIAL_PLUGIN/S-ISSUE/A | DUPLICATE/VERIFIED_LIMITATION/CUSTOM_REQUIRED/SR-REPO/A | DUPLICATE/VERIFIED_LIMITATION/ESTABLISHED/AL-REPO/B |
| maturity/operational evidence | KEEP/REPORTED_OPERATIONAL_EVIDENCE/ESTABLISHED/B-HERMES/C | SUPPLEMENT/REPORTED_OPERATIONAL_EVIDENCE/ESTABLISHED/C-REPO/C | SUPPLEMENT/VENDOR_CLAIM_ONLY/OFFICIAL_PLUGIN/A-REPO/D | SUPPLEMENT/VERIFIED_LIMITATION/OFFICIAL_PLUGIN/S-ISSUE/A | SUPPLEMENT/REPORTED_OPERATIONAL_EVIDENCE/ESTABLISHED/SR-REPO/C | SUPPLEMENT/REPORTED_OPERATIONAL_EVIDENCE/ESTABLISHED/AL-REPO/C |
| licensing and cost | KEEP/VERIFIED_CAPABILITY/ESTABLISHED/B-ADR/B | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/C-REPO/B | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/A-REPO/B | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/S-REPO/B | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/SR-PROJECT/B | SUPPLEMENT/VERIFIED_CAPABILITY/ESTABLISHED/AL-REPO/B |

## Candidate-wide consequences

| Candidate | Exact mechanism | Local/remote and model/API | Persistent state / egress | Context/token / Windows / maturity limitations |
|---|---|---|---|---|
| Hermes baseline | native runtime + Kanban + config + skills + QMD | Codex OAuth/API/local provider | repo, Kanban, QMD derived index, governed memory; egress by provider | configured/on-demand context; WSL QA; target not installed |
| CrewAI | Python Crews/Flows/A2A | API or local providers; no direct subscription OAuth evidence | Flow DB, optional LanceDB/Chroma; provider/A2A egress | multi-agent/memory calls; Python WSL path; active framework but exact MoA path unproven |
| Agency | lazy official router plugin | uses Hermes providers | local JSON; Hermes task state; delegation causes model calls | four schemas at startup, selected body on demand; checker omits live delegation |
| Superpowers | official skill/bootstrap plugin | uses Hermes providers/tools | no new DB; tool/command egress follows Hermes | mandatory method context; WSL follows tools; current Hermes mappings contradicted |
| Semantic Router | Python routes/encoders/index | local or remote encoder; dynamic LLM optional | route config/index; remote encoder/index egress | new service/calibration; no Hermes edge; active library only |
| AnythingLLM | desktop/server app, RAG/agents/flows/MCP client | own API/local providers; no subscription OAuth evidence | SQLite/vector/workspace/chat; provider/tool egress | second UI/runtime; native Windows; beta sync and permission burden |

## Hard filters by proposed use

| Proposal | F01 | F02 | F03 | F04 | F05 | F06 | F07 | Result |
|---|---|---|---|---|---|---|---|---|
| CrewAI replaces Hermes | pass | n/a | fail: second/replacement truth lacks value case | conditional | pass | open | pass | DEFER |
| CrewAI bounded A2A Flow | pass | conditional pass; version QA | pass if Hermes outer/CrewAI inner ownership | conditional | pass | conditional | pass | viable only after named need |
| Agency lazy roster pilot | pass | pass, official plugin | pass; static prompt data only | pass | conditional QA | conditional sample | pass | PILOT |
| Superpowers global method | pass | fail current compatibility | pass | pass | conditional | fail broad non-software fit | pass | DEFER |
| Semantic Router insertion | pass | fail | conditional | pass | conditional | open | fail | REJECT |
| AnythingLLM replaces QMD/Hermes | pass | fail Hermes edge | fail duplicate truth/state | conditional | pass | pass | pass | DEFER/REJECT replacement |
| AnythingLLM separate UI using QMD MCP | pass | conditional pass | pass if QMD remains index owner | conditional | pass | pass | pass | viable only after named UI need |

## Module actions

| Baseline module | Action |
|---|---|
| Hermes runtime, Kanban, repo truth, context, QMD, profiles, BMAD, MarketingSkills, memory/Curator, providers, safety | KEEP_BASELINE |
| specialist gap roster | PILOT Agency Agents, optional and on-demand |
| bounded event-flow runtime | NO_CHANGE; DEFER CrewAI until a named unmet workflow |
| workflow-method library | NO_CHANGE; DEFER Superpowers |
| semantic routing | NO_CHANGE; REJECT Semantic Router custom insertion |
| knowledge UI/RAG | NO_CHANGE; DEFER AnythingLLM separate UI |

## Comparative stories

Agency is relevant only to specialist selection; CrewAI to bounded parallel/event workflows; AnythingLLM to a human-facing RAG UI. The baseline remains strongest for repo-scoped context, QMD retrieval, reviewer separation, recovery ownership, procedural learning, local/provider choice and web-artifact portability. Superpowers does not beat BMAD/current review for non-code stories, and Semantic Router cannot enter without a prohibited subsystem.

## Swing-weight pilot-priority model

This model ranks **optional pilot opportunities**, not asymmetric products as whole stacks. Scores are anchored to observed evidence bands: 0 absent/contradicted, 25 weak/open, 50 present but duplicative/live-unproven, 75 upstream-supported/good fit, 100 strongest observed fit in this candidate set. Weights reflect the value of the observed worst-to-best swing after hard filters.

| Dimension | Weight | Agency roster | CrewAI Flow | AnythingLLM UI |
|---|---:|---:|---:|---:|
| full MoA workflow fit | 12 | 75 | 50 | 50 |
| verified upstream integration | 12 | 75 | 50 | 75 |
| demonstrated operational value | 10 | 25 | 50 | 50 |
| specialist/method quality | 12 | 100 | 50 | 25 |
| knowledge/context fit | 8 | 75 | 25 | 75 |
| durable state/recovery | 8 | 50 | 100 | 50 |
| privacy/security/locality | 8 | 75 | 50 | 50 |
| subscription/local economics | 7 | 75 | 50 | 50 |
| context/token efficiency | 6 | 100 | 25 | 50 |
| cross-client portability | 4 | 75 | 50 | 25 |
| operator comprehensibility | 6 | 75 | 25 | 50 |
| maintenance/update burden | 7 | 75 | 25 | 25 |
| **weighted opportunity value** | **100** | **72.50** | **47.25** | **49.25** |

These are not adoption scores: operational-value uncertainty prevents `ADD_NOW`. Agency’s high result means “first bounded pilot if any,” not “best stack.”

## Sensitivity and switching

| Scenario | Result |
|---|---|
| simplicity/low maintenance first | baseline only; every addition loses |
| knowledge/retrieval first | QMD baseline; AnythingLLM switches to pilot only when a human UI is a required benefit |
| specialist quality first | Agency pilot leads; reject if six-role sample finds no recurring non-duplicative gap |
| autonomy/parallelism first | CrewAI switches to pilot only when a named recoverable event Flow is required and A2A passes |
| privacy/local first | baseline; local options exist but additional permission/state surfaces lose |
| subscription-cost first | baseline; candidates do not document direct Codex subscription OAuth |

Decision switching is requirement-driven rather than a fake global score: Agency changes from PILOT to DEFER if the role sample produces fewer than two recurring gaps or live plugin compatibility fails; CrewAI changes only with a concrete Flow need plus verified A2A/recovery; AnythingLLM changes only with an approved UI need plus QMD MCP/isolation/security QA. No plausible reweighting makes Semantic Router viable while F02/F07 fail or Superpowers viable while current compatibility is contradicted.

## Complexity ledger and preliminary action

| Candidate | New burden | Verified value that pays | Action |
|---|---|---|---|
| CrewAI | runtime, workflow code, DBs, model config, A2A auth/recovery | no current named workflow | DEFER |
| Agency | one plugin/JSON, update/security review, selected prompt and delegation calls | lazy breadth with official Hermes path | PILOT |
| Superpowers | bootstrap/method context, tool permissions, compatibility drift | no unique broad MoA value | DEFER |
| Semantic Router | custom service, routes/index/eval/fallback | no measured routing defect | REJECT |
| AnythingLLM | app, DB/workspaces/permissions/providers/backups | no named UI requirement | DEFER |

## Evidence gaps that can change V2

Agency live delegate compatibility and six-role value sample; CrewAI A2A version/recovery only if a workflow is named; AnythingLLM MCP/isolation only if a UI requirement appears. All other gaps cannot change the current action and do not justify more research now.

Method sources: [Green Book 2026](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026) and [NASA Decision Analysis](https://www.nasa.gov/reference/6-8-decision-analysis/). Candidate source IDs resolve in R00–R06. **PASS**.
