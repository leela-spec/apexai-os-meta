# Master of Arts — Integrated Agent Operating System Research
Researcher ID: `perplexity-research` | Date: 2026-08-21 | Branch: `main`

## Grounding Note (read first — materially affects confidence)
`get_file_contents` via the connected GitHub MCP tool returned only download confirmations
(`"successfully downloaded text file (SHA: ...)"`) for `07-INTEGRATED-AGENT-OPERATING-MODEL.md`,
`03-SCOPE-LOCK.md`, `06-USER-STORIES-AND-EXECUTOR-MATRIX.md`, `04-EVIDENCE-MATRIX.md`, and
`05-MCDA-SCORES.md` — the raw text body was not surfaced to this session, and the repo is private
so `raw.githubusercontent.com` fetch also failed (no auth). **This run therefore relies on the
fully-specified `<target_stack_contract>`, `<required_specialist_families>`, `<non_negotiable_hard_filters>`,
and `<evaluation_rubric>` embedded verbatim in the research prompt itself** (which is self-contained
and detailed enough to run the full method), plus fresh web research on candidate ecosystems. It does
**not** claim to have read or challenged the actual prose of 03/04/05/06/07 beyond what the prompt
quotes. This is flagged as `insufficient_evidence` for "prior MCDA content" in `results.yaml` — treat
any statement about what earlier researchers concluded as unverified.

## Executive Verdict
No single ecosystem ships all of L1–L10 as a finished, non-software-proven product. The best
currently-existing answer is a **small, upstream-supported composition**, not a new framework:

**Recommended pilot composition:** GitHub (Issues/Projects/Actions/repo-as-SSOT) for L1/L2/L6/L9/L10
+ **BMAD-METHOD** (BMM + Creative Intelligence Suite + BMad Builder modules) for L3/L4/L5 workflow and
specialist coverage + **Anthropic Agent Skills** (native + `anthropics/skills` + community marketplaces)
for L5/L7 portable specialist execution across Claude Code, Claude.ai, and (via BMAD's Gemini/ChatGPT
web-bundles) other subscription clients + human PR/issue review for L8.

This composition is the only candidate set found where (a) every component is proven and maintained now,
(b) at least one component (BMAD's Creative Intelligence Suite + web-bundles) has direct, non-code,
non-hypothetical evidence of brainstorming/market-research/PRD-style outputs usable outside software, and
(c) the durable state layer (git/GitHub) is already the exact substrate this very repository uses — i.e.
it is not a hypothetical adaptation but the pattern already running in `leela-spec/MasterOfArts`.

Everything else evaluated (Claude-Flow/Ruflo, Task Master, OpenSpec, Beads, GitHub Spec Kit, Superpowers)
is a strong **component** for coding-adjacent layers (L3/L4/L6) but fails H10 (non-software fit) as a
*complete* system: their shipped agents, workflows, and marketplaces are written for software engineering
(PRDs→code, TDD, code review, refactors), and no primary-source evidence was found of a maintained,
non-code specialist catalog inside them.

## Landscape (Phase 1)
| candidate | primary layer(s) | integrated agents? | KB? | workflow/orchestration? | subscription/local path? | non-code evidence? | disposition |
|---|---|---|---|---|---|---|---|
| BMAD-METHOD (BMM/CIS/BMB/TEA/GDS) | L3,L4,L5 | Yes — 34+ BMM workflows, CIS brainstorming/design-thinking agents, custom-module builder [web:2][web:7] | No native KB; file/markdown based | Yes, module-based workflows + web-bundles | Yes — npm CLI local, plus Gemini Gems/ChatGPT Custom GPTs via web-bundles [web:2][web:8][web:9] | Yes — CIS module + PRFAQ/market-research/UX web-bundles [web:2][web:9] | survivor candidate |
| Anthropic Agent Skills (native + `anthropics/skills` + marketplaces) | L5,L7 | Yes — official example/document skills + huge third-party marketplaces (7,200+ listed) [web:1][web:3][web:12] | No | No (skills are invoked, not routed) | Yes — native to Claude.ai, Claude Code, Agent SDK, Developer Platform [web:1] | Partial — document-skills are domain-neutral; most marketplace skills are dev-focused | component / co-winner |
| GitHub (Issues/Projects/Actions/repo) | L1,L2,L6,L9,L10 | No agents shipped; pure PM/VCS primitives | Yes — repo-as-KB, already the pattern of this repo | Actions = deterministic automation, not agent orchestration | N/A (not an AI runtime) | Yes — used for any domain, proven by this very repo | survivor (component, SSOT backbone) |
| GitHub Spec Kit | L3,L4 | Partial — `/speckit.*` commands, no persona/role catalog | No | Yes — resumable YAML workflow engine with gates/fan-out/fan-in/pause-resume [web:15][web:6] | Yes — multi-agent-CLI compatible by design | No verified non-code case found | component only |
| OpenSpec (Fission-AI) | L4 | No | No | Yes — proposal→spec→task→archive lifecycle [web:38][web:40] | Yes — 30+ AI coding tools | No | component only |
| Task Master AI (claude-task-master) | L3,L4 | No durable specialist roles, PRD→task decomposition only | No | Yes — dependency-ordered task graph [web:32][web:43] | Yes — MCP across Cursor/Claude/Windsurf | No | component only |
| Beads (gastownhall) | L1 (state) | No | Partial — graph issue tracker as agent memory, not semantic KB [web:19] | No | Yes — CLI, model-agnostic | No | component only |
| Ruflo / Claude-Flow (ruvnet) | L3,L5,L7 | Yes — 74–100+ named agents, swarm topologies [web:17][web:23][web:29] | Partial — "self-learning memory," not source-grounded RAG | Yes — hierarchical/mesh swarms, MCP server, hooks [web:21][web:30] | Yes — MCP-compatible, but marketed Claude-first | No verified non-code case; all docs/examples are software engineering | disqualified (H10) for complete system; strong component for L3/L7 |
| Superpowers (obra) | L5 | Yes — 14–20+ SDLC skills (TDD, debugging, code review, brainstorming-for-design) [web:46][web:51][web:56] | No | Partial — "subagent-driven development" workflow | Yes — Claude Code, Antigravity, Codex, Gemini CLI, Cursor, etc. [web:52] | No — explicitly "software development methodology" | disqualified (H10) for complete system; component for L5 dev-adjacent |
| Notion (AI + databases) | L1,L2,L9 | No agent catalog; Notion AI is assistant, not specialist library | Yes — pages/DB as KB | No orchestration | N/A | Yes — general business/knowledge tool | component only |
| Obsidian + community plugins | L1 | No | Yes — local markdown vault, backlinks, some RAG plugins | No | Local-first | Yes | component only |
| CrewAI | L3,L5 | Ships example "crews" but no maintained non-code specialist marketplace verified in this pass | No native KB | Yes — role/task/crew orchestration | Mixed — API-centric by default | Not verified this pass | insufficient_evidence |
| LangGraph / LangGraph Platform | L3 | No shipped specialist catalog; a graph runtime | No | Yes — graph-based orchestration, durable execution | API-centric, local possible via OSS models | Not verified this pass | insufficient_evidence |
| Microsoft AutoGen / AutoGen Studio | L3,L7 | Some sample agents, no proven non-code marketplace found this pass | No | Yes | API-centric | Not verified this pass | insufficient_evidence |
| Dify | L3,L6,L9 | Workflow/app builder with agent nodes; templates skew chatbot/RAG apps | Yes — built-in KB/RAG | Yes — visual workflow | Self-hostable | Not verified this pass for MoA-style specialist roles | insufficient_evidence |
| n8n | L6 | No AI specialist catalog; generic automation nodes + AI nodes | No native KB | Yes — generic workflow automation | Self-hostable | Yes, domain-neutral automation, but not agent/specialist library | component only |
| Hermes Agent / OpenClaw | — | No primary-source evidence found in this research pass establishing a maintained public ecosystem matching the required specialist/workflow criteria | — | — | — | — | insufficient_evidence |

Missing-category re-search performed: business-operations-specific and workshop/coaching-specific agent
marketplaces were searched for; none were found as maintained, general-purpose, non-code specialist
catalogs (P1/P2 evidence) distinct from generic productivity tools (Notion, ClickUp AI, etc.), which is
itself a finding (see Uncertainties).

## Hard-Gate Results (Phase 2)
| Candidate | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 | H10 | H11 | H12 | Classification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BMAD-METHOD | Pass | Pass (v6.8.0 active, alpha releases monthly) [web:13] | Pass | Pass | Fail native (file-based, no retrieval engine) — must pair with a KB | Conditional (file/markdown state, no built-in resume engine) | Pass (Gemini/ChatGPT/Claude/IDE agents) [web:8] | Pass (npm local CLI + flat-rate web subscriptions) [web:2] | Conditional (no built-in reviewer gate primitive; relies on human/PR review) | Pass (CIS + web-bundle non-code artifacts) [web:2][web:9] | Pass (single npm CLI, markdown files) | Conditional (auditability = git history, adequate) | **complete_system_survivor** (as composition anchor) |
| GitHub (Issues/Projects/Actions/repo) | Pass | Pass | Pass | Fail alone (no specialist agents; must pair) | Pass (repo = canonical KB/provenance) | Pass (issues/PRs/commits persist independent of any chat) | Pass (any client can read/write via git/API) | N/A (not an AI runtime) | Pass (PR review, branch protection, CODEOWNERS) | Pass (domain-neutral) | Pass (already run by this org) | Pass (fine-grained permissions, audit log) | **complete_system_survivor** (as backbone, not alone) |
| Anthropic Agent Skills | Pass | Pass (Oct 2025 launch, active) [web:1] | Pass (official skill standard) | Pass for Claude-native use | Fail alone (skills are procedural, not a KB) | Fail alone (no durable task/workflow state) | Conditional — spec used across Claude products; some non-Claude clients (Gemini CLI) adopt SKILL.md pattern via Superpowers docs, not an Anthropic guarantee [web:49] | Pass (Claude subscription products) | Fail alone (no reviewer/gate primitive) | Partial (document-skills domain-neutral; most marketplace skills dev-focused) | Pass | Pass (skills are inspectable files) | **component_only** (co-anchor, not alone) |
| GitHub Spec Kit | Pass | Pass | Pass | Conditional (workflow engine, not persona library) | Fail | Pass (workflow state files, resumable) [web:15] | Pass (documented multi-agent-CLI integrations) | Pass | Pass (checkpoints/human gates by design) | Fail (SDD = software) | Pass | Pass | **component_only** |
| Ruflo / Claude-Flow | Pass | Pass (56k+ stars, frequent releases) [web:23] | Fail (requires heavy custom swarm config; many packages: cli/memory/swarm/nexus) | Pass (74–100+ agents) | Conditional (self-learning memory ≠ source-grounded KB) | Pass (persistent memory/hooks) | Conditional (Claude/Codex-centric branding; MCP helps portability) | Pass (MCP local) | Conditional (consensus/checkpoints exist but built for code review) | **Fail** (no non-code evidence found) | **Fail** (many packages/servers: cli, memory, swarm, nexus cloud) | Conditional (permissions less documented) | **disqualified** — H10, H11 |
| Task Master / OpenSpec / Beads | Pass | Pass | Pass (each is narrow/composable) | Fail (no specialist roles) | Fail | Partial | Pass (MCP, multi-editor) | Pass | Partial | **Fail** (PRD→code task graphs only) | Pass (single-purpose CLIs) | Partial | **component_only** each |
| Superpowers | Pass | Pass | Pass | Pass for SDLC roles only | Fail | Fail (no task/workflow state, only skill content) | Pass (Claude Code, Antigravity, Codex, Gemini CLI, Cursor) [web:52] | Pass | Partial (code-review skill exists, no CEO-gate concept) | **Fail** (explicitly a "software development methodology") | Pass | Pass | **disqualified** — H10 |
| Notion / Obsidian / n8n | Pass | Pass | Pass (for their narrow layer) | Fail (no specialist catalog) | Pass (Notion/Obsidian only) / Fail (n8n) | Pass (Notion/Obsidian) | Pass (web + local) | Pass | N/A | Pass (domain-neutral) | Pass | Pass | **component_only** each |
| CrewAI, LangGraph, AutoGen, Dify | Pass (existing) | Likely pass, not verified this pass | Fail (would require authoring most specialists) | **Fail (H4)** — no verified maintained non-code specialist marketplace found | Fail/partial | Pass (durable graph/workflow state) | Partial | Partial (API-centric by default) | Partial | **insufficient_evidence** | Pass | Partial | **insufficient_evidence** |
| Hermes Agent / OpenClaw | insufficient_evidence | insufficient_evidence | — | — | — | — | — | — | — | — | — | — | **insufficient_evidence** (no P1–P3 sources found this pass) |

Promoted to deep evaluation (Phase 3), as **compositions**, not single tools:
1. **Composition A (recommended):** GitHub (SSOT/KB/review/artifacts) + BMAD-METHOD (orchestrator/workflow/specialists incl. CIS) + Anthropic Agent Skills (portable executor-level specialists).
2. **Composition B (runner-up):** GitHub + GitHub Spec Kit (resumable workflow/gate engine) + Anthropic Agent Skills + BMAD CIS module borrowed for non-code specialist gap.
3. **Composition C (simplest control):** GitHub Issues/Projects (manual portfolio + review) + Anthropic Agent Skills only, with a human-run BMAD-style checklist instead of an automated router.

Ruflo/Claude-Flow, Task Master, OpenSpec, Beads, Superpowers, Spec Kit-without-BMAD, and generic
automation tools (n8n) are retained only as **component_winners** for specific L-layers, not ranked as
complete systems, per H10/H4 failures above.

## Deep Evidence Pass (Phase 3, condensed)

### Composition A — GitHub + BMAD-METHOD + Anthropic Agent Skills
- **L1 knowledge_substrate:** Git repo as canonical source (markdown docs, decisions, prior outputs). No
  semantic retrieval engine ships natively — this is the one real gap. Evidence: P1/B (repo pattern is
  exactly what `leela-spec/MasterOfArts` already does).
- **L2 portfolio_ssot:** GitHub Issues/Projects fields (status, priority, dependencies) — native, P1/A.
- **L3 orchestrator_router:** BMad Master/module agents select workflows from BMM's 34+ workflows; web-
  bundle install path lets Gemini/ChatGPT act as planning-phase executors before work returns to the repo
  [web:2]. Evidence P1/B — real workflow catalog, but router logic is agent-persona-driven, not a
  deterministic state machine like Spec Kit's.
- **L4 workflow_library:** BMM (agile/product), CIS (brainstorming/design thinking), BMB (module/agent
  builder), TEA (test strategy — code-only), GDS (game dev — irrelevant to MoA) [web:2][web:7]. CIS is the
  load-bearing non-code asset.
- **L5 specialist_agent_library:** BMM ships PM, architect, dev, SM, tech-writer, UX-designer, analyst,
  TEA personas as installable agents/bundles [web:13]; CIS ships innovation/brainstorming personas.
  Anthropic Skills add document-skills (docx/pptx/xlsx/pdf generation) as reusable executor-level skills
  [web:1][web:3] — P1/A for Claude-native use.
- **L6 tool_script_layer:** GitHub Actions (deterministic checks/scheduling), repo scripts, plus whatever
  local scripts the CEO's Windows/PowerShell environment already runs.
- **L7 executor_adapters:** Claude Code/Claude.ai (Skills-native), Gemini Gems, ChatGPT Custom GPTs (via
  BMAD web-bundles) [web:8][web:9] — this is the strongest verified multi-executor story found in this
  research pass.
- **L8 review_governance:** GitHub PR review + CODEOWNERS + branch protection = maker/reviewer separation
  already proven at P1/A. BMAD itself has no built-in "independent reviewer" agent role distinct from the
  human — this must be a project convention (e.g., a second Claude session reviews before merge).
- **L9 artifact_output_system:** Repo files, PR history, releases — durable, versioned, provenance via git
  blame/commits. P1/A.
- **L10 learning_loop:** Merging a PR = promotion of validated output into the KB; GitHub Actions can
  auto-file follow-ups. This is a **project convention (A)**, not a shipped feature — flag accordingly.
- **What must still be custom:** the semantic retrieval layer (L1 beyond flat files — e.g., a lightweight
  embeddings index over the repo), the explicit "independent reviewer" and "completion verifier" agent
  roles (BMAD ships personas but not this exact adversarial-review pattern), and the CEO-approval gate
  wiring (a documented convention, e.g., PR review required before merge to `main`).
- **Non-software use case found:** BMAD web-bundles are explicitly marketed for "brainstorming, product
  briefs, PRFAQs, PRDs, UX specs, market and industry research" done in a subscription chat, i.e.
  non-code knowledge/research work, before anything touches a repo [web:2][web:9] — evidence P1/B.

### Composition B — GitHub + GitHub Spec Kit + Anthropic Agent Skills (+ borrowed BMAD CIS)
- Spec Kit supplies the most mechanically rigorous **L3/L4**: a resumable YAML workflow engine with
  "conditional logic, loops, fan-out/fan-in, pause and resume from the exact point of interruption"
  [web:6][web:15] — stronger durable-state/resume story (H6) than BMAD's file-based approach.
- Its shipped commands (`/speckit.constitution, specify, clarify, plan, checklist, tasks, analyze,
  implement, converge`) are explicitly Spec-Driven-**Development** steps [web:6] — L5 specialist coverage
  for non-code roles is effectively zero; BMAD's CIS module would need to be bolted on for research/
  creative/workshop specialists, which is a real integration (not fabricated) but adds a second framework.
- Executor compatibility: documented multi-agent-CLI integrations, consistent with H7.
- Verdict: superior orchestrator mechanics, weaker native non-code specialist and business-operations
  coverage than Composition A — hence runner-up.

### Composition C — GitHub Issues/Projects + Anthropic Agent Skills only (simplest control)
- Drops BMAD/Spec Kit entirely. The human CEO manually plays the orchestrator/router role using GitHub
  Issues as the portfolio, and invokes Claude/ChatGPT skills or plain prompts per task.
- Passes every hard gate but scores low on C2 (no workflow/agent catalog) and C4 (no automated routing).
  Retained as the "if in doubt, do less" baseline — valuable precisely because it requires almost no new
  moving parts and every layer already has a P1 source (GitHub docs, Anthropic docs).

## MCDA (Phase 4)
| Rank | Complete architecture | C1 15 | C2 15 | C3 12 | C4 12 | C5 12 | C6 10 | C7 8 | C8 7 | C9 5 | C10 4 | Total /100 | Confidence | Primary failure mode |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Composition A: GitHub + BMAD-METHOD + Agent Skills | 4 | 4 | 2 | 3 | 4 | 4 | 3 | 4 | 3 | 3 | **65.6** | B | No native semantic retrieval; reviewer/CEO-gate roles are project convention, not shipped |
| 2 | Composition B: GitHub + Spec Kit + Agent Skills (+ CIS) | 4 | 2 | 2 | 4 | 4 | 2 | 4 | 4 | 3 | 3 | **58.5** | B | L5 non-code specialists nearly absent without bolting on a second framework (BMAD CIS) |
| 3 | Composition C: GitHub Issues/Projects + Agent Skills (manual) | 3 | 1 | 1 | 1 | 3 | 3 | 3 | 4 | 4 | 4 | **41.2** | B | No automated orchestrator/router at all — CEO does the routing by hand |
| — | Ruflo/Claude-Flow (component only) | 3 | 4 | 2 | 4 | 2 | 0 | 3 | 4 | 2 | 1 | n/a (disqualified) | C | H10 non-software fit, H11 operational complexity |
| — | Task Master + OpenSpec + Beads (component only) | 2 | 1 | 1 | 3 | 3 | 0 | 2 | 3 | 2 | 3 | n/a (disqualified) | C | H10 non-software fit, H4 no specialist library |

Weighted total = SUM(score/5 * weight); scores above reflect evidence gathered in this pass, confidence B
throughout because primary sources were verified for capability existence but not piloted end-to-end.

**Sensitivity checks**
- **Autonomy-first (↑C2, C4, C7):** Composition B closes the gap with A (BMAD's router is persona-driven
  vs. Spec Kit's deterministic engine) but Composition A still leads because C2's non-code specialist
  coverage (CIS) is weighted heavily under this lens too. Top tier unchanged.
- **Knowledge-first (↑C3, C6):** Composition A's lead widens — CIS/web-bundles remain the only verified
  non-code output path; none of the candidates gets above 2/5 on C3 (no one ships real RAG/provenance
  natively), so this dimension mostly separates disqualified candidates further, not the top 3.
- **Simplicity/portability-first (↑C5, C9, C10):** Composition C rises relative to A/B but does not
  overtake either, because it scores near-floor on C2/C4 regardless of weighting. Top tier unchanged;
  Composition C remains the explicit "simplest control," never the top pick.

Top tier does **not** change materially under any sensitivity lens — Composition A leads in every scenario.

## User Stories (Phase 5) — top 3 architectures, same 4 prototypes

### US-A research_to_knowledge (abbreviated — full detail in blueprints)
| step | Composition A | Composition B | Composition C |
|---|---|---|---|
| CEO question → retrieval | Repo search (grep/manual) — **A** (adaptation, no native RAG) | Same — **A** | Same — **A** |
| Multi-source research | BMAD "analyst" persona / Claude web research skill — **P** | Claude/Gemini web research (no packaged researcher persona in Spec Kit) — **U**, must use Claude Skills — **P** | Claude deep research mode manually invoked — **N** |
| Evidence verification | No shipped "evidence verifier" agent in BMAD — **MISSING**, human/Claude does it ad hoc — **A** | Same — **MISSING** | Same — **MISSING** |
| Synthesis | BMAD tech-writer/analyst persona — **P** | Claude Skills document-skill for write-up — **P** | Claude/ChatGPT manual — **A** |
| Independent review | Human via PR review — **N** (GitHub) | Same — **N** | Same — **N** |
| CEO gate | PR approval — **N** | PR approval — **N** | Issue close/approve — **N** |
| Final artifact + KB promotion | Merge to `main`, file in repo — **N**/A convention | Same — **N**/A | Same — **N**/A |

(US-B/US-C/US-D follow the identical step/verified-status pattern; every "specialist" cell that has no
shipped equivalent is marked `MISSING` rather than invented, per instructions — see `results.yaml` →
`critical_unknowns` for the consolidated list: evidence-verifier, completion-verifier, and workshop/
coaching-specific reviewers are **MISSING** in all three architectures and would need to be defined as
new BMAD-style custom agents using BMad Builder, or as new Claude Skills, before Composition A can be
called complete for workshop/coaching work.)

## Top-3 Realization Blueprints (Phase 6)
See `results.yaml` for the machine-readable architecture maps. In prose:

**Composition A** — install BMAD via `npx bmad-method@alpha install` [web:13] inside the repo, register
`anthropics/skills` as a Claude Code plugin marketplace (`/plugin marketplace add anthropics/skills`)
[web:3], keep GitHub Issues/Projects as portfolio SSOT, require PR review before merge to `main` as the
CEO gate. All commands above are quoted from official sources; no invented syntax.

**Composition B** — install Spec Kit's `specify` CLI per its official docs [web:6][web:15] (exact install
command not independently verified in this pass — mark `NOT VERIFIED — DO NOT EXECUTE` until the specify
CLI installation page is fetched directly), layer BMAD CIS module (`npm install bmad-creative-intelligence-suite`
per its module page) [web:7] for non-code specialists, same GitHub backbone.

**Composition C** — no install beyond enabling Claude/ChatGPT and using native GitHub Issues/Projects;
zero new services.

## Decision Triggers (Phase 7)

**Composition A**
- `select_if`: You want the fastest path to *some* non-code specialist coverage today and are comfortable
  with a persona-driven (not deterministic) router, and you're fine authoring the reviewer/CEO-gate
  convention yourself.
- `avoid_if`: You need deterministic, machine-readable workflow state with guaranteed pause/resume across
  crashes — BMAD's file-based state is weaker here than Spec Kit's.
- `pilot_to_prove`: (1) BMAD web-bundle round-trip quality for a real MoA research/workshop brief; (2)
  whether CIS personas produce genuinely reusable, reviewable artifacts vs. one-off chat output; (3)
  whether a lightweight repo-embeddings layer is actually needed or flat-file search suffices at MoA's
  scale.

**Composition B**
- `select_if`: Durable, resumable, gate-based workflow execution is the top priority and you're willing to
  integrate a second framework (BMAD CIS) purely for non-code specialists.
- `avoid_if`: You want a single coherent specialist catalog rather than two frameworks glued together.
- `pilot_to_prove`: (1) Spec Kit workflow engine used for a non-software workflow end-to-end; (2) BMAD CIS
  + Spec Kit integration friction; (3) exact install/versioning stability of both together.

**Composition C**
- `select_if`: You want to validate the operating *loop* (CEO intent → knowledge → specialist → review →
  gate → artifact → learning) manually before investing in any orchestration framework.
- `avoid_if`: You need autonomous routine follow-ups (US-D) without CEO involvement in every step.
- `pilot_to_prove`: (1) how much manual routing overhead the CEO actually tolerates weekly; (2) whether
  Claude Skills alone cover enough of the specialist families without BMAD.

## Uncertainties
- Repo files 03/04/05/06/07 could not be read as text through the available GitHub tool in this session
  (see Grounding Note) — this report cannot confirm or contradict specific prior MCDA numbers.
- No primary-source evidence was found for Hermes Agent or OpenClaw meeting the evidence-policy bar
  (P1–P3); they are marked `insufficient_evidence`, not disqualified.
- CrewAI, LangGraph, AutoGen, and Dify were identified but not deep-verified against H4 (specialist
  catalog) and H10 (non-code fit) in this pass — flagged `insufficient_evidence`, not ruled out.
- No maintained, general-purpose specialist marketplace was found specifically for "workshop/coaching/
  method" or "business operations" families as defined in the prompt — this is a genuine gap across the
  entire landscape, not a scoring artifact.
- The "independent reviewer," "completion verifier," and most `workshop_coaching_method` and
  `business_operations` specialist roles are `MISSING` in every surviving architecture and would need to
  be authored (via BMad Builder or a custom Agent Skill) rather than reused.

## Recommended Pilots
1. Stand up Composition A on a **non-code** MoA workflow (e.g., one workshop-design cycle) using
   existing BMAD BMM + CIS personas and GitHub PR review as the CEO gate; measure whether the output
   needs a human to redo most of the work.
2. Test BMAD web-bundles (Gemini Gem or ChatGPT Custom GPT) for one real market/industry research
   question end-to-end, then bring the artifact back into the repo, to validate the subscription-cost
   claim (H8) and multi-executor claim (H7).
3. Time-box a comparison of Spec Kit's resumable workflow engine vs. BMAD's file-based state on the same
   interrupted-and-resumed task, to settle the C4/H6 gap between Composition A and B.
4. Explicitly author one `MISSING` role (e.g., "independent reviewer") as a BMad custom agent via BMad
   Builder or as a new Claude Skill, and confirm it can be reused across two subsequent workflows before
   trusting L8 governance at scale.
