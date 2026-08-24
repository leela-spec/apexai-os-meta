# Integrated Master of Arts Agent Operating System — Independent Research Run

Researcher: `chatgpt-deep-research`  
Research date: 2026-08-21  
Repository scope ref at start: `b4dceb52abb7327d50887f085fe4db7326969d40`  
Decision status: **pilot recommendation only — no production selection**

## Executive Verdict

### Decision target

Master of Arts needs a durable **AI company in a repo**, not merely a coding-agent harness or project manager: CEO intent must become durable portfolio work; relevant knowledge must be retrieved selectively; reusable specialists and workflows must execute through subscription/local-capable AI clients; independent review and explicit human gates must control consequential decisions; final artifacts and provenance must survive sessions; and accepted learning must be reusable later. The authoritative repository model requires explicit ownership of L1–L10 and non-software output classes including research, workshops, coaching/method work, content, operations, offers/products, and later Leela precursors. [S001][S002]

### Independent verdict

| Rank | Complete architecture | Score /100 | Confidence | Hard gates | Why it leads / loses |
|---:|---|---:|:---:|---|---|
| **1** | **OpenClaw + bundled Workboard + builtin memory + curated ClawHub skills** | **89.5** | **B** | conditional pass | Best single-ecosystem L1–L10 coverage: native task board, dependencies/review, provenance-aware hybrid memory, subagents, automation, broad tools, subscription/local runtimes, and a live skill registry. Main risk is community-skill trust/quality and missing MoA-specific workshop/coaching/Leela specialists. |
| **2** | **Hermes Agent + BMAD Method/BMM/CIS through documented SKILL.md directories** | **87.7** | **B** | conditional pass | Strongest existing specialist-method composition: Hermes supplies durable Kanban/runtime/review/subscription-local execution; BMAD supplies decision-grade research, multi-lens review, Analyst/PM roles and Creative Intelligence agents. Main risk is that the cross-product skill bridge is standards-compatible but not a named upstream-tested integration. |
| **3** | **Hermes Agent native + official/established skills + qmd** | **84.7** | **B** | conditional pass | Smallest strong control: durable Kanban, dependencies, review/change loops, scheduling, profiles, open Agent Skills, local qmd retrieval and broad model paths. Loses because fewer relevant prebuilt specialist roles exist than in the two stacks above. |
| 4 | Dify + GitHub artifact/portfolio boundary + official LangGenius templates | 77.2 | B | conditional pass | Excellent first-party RAG/HITL/research/content workflow examples; weak subscription-client portability and no equally strong native CEO portfolio SSOT. |
| 5 | n8n + GitHub + local/vector knowledge layer + Ollama | 77.1 | B | conditional pass | Excellent business automation, SaaS integrations, HITL and non-code template ecosystem; weaker specialist-agent standard and higher multi-service/integration burden. |

**Recommended for pilot:** **OpenClaw integrated stack.** The late discovery of the current bundled Workboard changed this run’s provisional ranking: current official documentation shows durable relational board state with dependencies, claims, `review`/`blocked` states, run attempts, artifacts, proof, permissions, and direct Codex/Claude execution. That closes the portfolio/durable-state gap earlier Master of Arts research had attributed to OpenClaw. [S040]

OpenClaw’s builtin memory is also materially stronger than the earlier repo analysis assumed: canonical Markdown remains the source, while a per-agent SQLite index provides BM25 + vectors, deterministic relevance/recency/importance ranking, MMR, extra-path indexing, local embedding options, and SQLite-owned provenance (`owner|agent|untrusted|system`, session kind, observation time, supersession). QMD is explicitly retired in current OpenClaw. [S041]

**Runner-up:** Hermes + BMAD/BMM/CIS. Hermes has an unusually strong new Kanban substrate: shared durable SQLite state, dependency promotion, multiple profiles, retries, review/change loops, human comments/unblock, artifacts and structured handoffs; BMAD currently emits `SKILL.md` packages for agents/workflows/tasks/tools and has strong prebuilt research/review/creative assets. [S010][S030][S031][S033]

**Simplest control:** Hermes native with official skills/qmd. It is the most useful baseline against which to measure whether OpenClaw’s broader memory/marketplace and BMAD’s added specialist layer materially improve real MoA work.

### Important negative finding

No evaluated ecosystem ships the complete required Master of Arts specialist roster. The following remain **MISSING as verified prebuilt specialists** in the top systems: workshop designer, pedagogy/learning reviewer, coaching-method analyst, sensitivity/public-private reviewer tailored to MoA, and the Leela use-case/product-boundary family. This is not fatal under H4 because both OpenClaw and Hermes have mature reusable skill mechanisms, but it prevents production selection before pilots.

---

## Landscape

### Phase 1 — broad scan

| Candidate | Primary layer(s) | Integrated agents? | KB? | Workflow/orchestration? | Subscription/local path? | Non-code evidence? | Disposition |
|---|---|---|---|---|---|---|---|
| OpenClaw | L1–L10 candidate | Yes: agents/subagents + ClawHub | **Yes, native hybrid memory** | **Yes, Workboard + task flow + automations** | **Yes: ChatGPT/Codex OAuth; Claude/Gemini CLI; local providers** | **Strong** | complete_system_survivor |
| Hermes Agent + BMAD/BMM/CIS | L1–L10 composition | **Yes** | qmd + memory/files | **Yes, Kanban + profiles + cron** | **Yes: Codex subscription, Nous subscription, local/self-hosted** | Strong across research/creative; some software bias in BMAD | complete_system_survivor |
| Hermes Agent native | L1–L10 candidate | Yes: profiles + skills | qmd optional + persistent memory | **Yes, Kanban** | **Yes** | Strong generic/runtime evidence | complete_system_survivor |
| Dify + GitHub boundary | KB/workflows/HITL | Agent node + official templates | **Yes** | Yes | Local-model path; subscription-client path weak | **Strong first-party business/content/research templates** | complete_system_survivor, conditional |
| n8n + GitHub + vector/Ollama | business automation/workflows | AI Agent nodes; template teams | Yes via vector stores | **Yes** | Ollama/local; API-heavy otherwise | **Very strong** | complete_system_survivor, conditional |
| Agno AgentOS | agent runtime/teams/HITL | Yes, examples | Yes | Yes | Local models possible | First-party research/content/product-launch examples | component_only |
| CrewAI | crews/flows | Yes | memory/knowledge | Yes | Provider/local dependent | Generic | component_only |
| LangGraph / Deep Agents | durable agent graphs | Yes | integrations | **Strong** | Provider/local dependent | Generic | component_only |
| Langflow | visual agent flows | Yes | RAG components | Yes | Provider/local | Business templates exist | component_only |
| AutoGen | agent teams | Yes | memory integrations | Yes | Provider/local | Generic | component_only |
| Letta | stateful memory agents | Yes | **Strong memory** | limited portfolio orchestration | local/API | Generic | component_only |
| GitHub Spec Kit + GitHub | L3/L4/L9 | workflow steps, not specialist org | **No semantic KB** | **Very strong current workflow engine** | many AI-client integrations | Now explicitly supports business processes; non-code presets | component_only; major donor |
| BMAD Method standalone | L4/L5 | **Strong roles/workflows** | project context, not durable semantic KB | Workflow method, not durable runtime | IDEs + web bundles | Research/ideation/creative evidence | component_only; major donor |
| Beads | L2/L3 state | agent task graph | graph memories, not corpus RAG | strong dependencies/claims/formulas | multi-CLI | coding-agent centered | component_only |
| OpenSpec | specs/change artifacts | no broad specialist org | no | change workflow | broad coding assistants | coding-centric | component_only |
| Task Master | task decomposition | task personas limited | no durable corpus KB | task graph | Codex/Claude modes | dev/PRD centered | component_only |
| Superpowers | L4 process skills | reviewer/subagent patterns | no | plan/execution method | portable skills | software-development method | component_only |
| Ruflo / Claude Flow | swarm/runtime/memory | large agent catalog | yes | strong | Claude/Codex/local paths | mostly software engineering | disqualified as core: H10/H11 |
| Gas City | multi-agent factory | yes via packs | inherited components | strong | provider dependent | software-factory focus | disqualified as core: H10/H11 |
| GitHub Issues/Projects + Agent Skills | L2/L5/L9 control | via external clients/skills | no semantic KB | no first-class AI runtime | excellent client portability | **Strong domain neutrality** | component_only; control reference |

### Discovery conclusion

The seeded coding-agent candidates are useful, but they are not the dominant complete-system class once the decision boundary is L1–L10. The strongest new complete-system evidence came from **OpenClaw**, **Hermes**, **Dify**, and **n8n** because these systems combine durable workflows with knowledge, tools and non-software operation rather than only coding task decomposition.

---

## Hard-Gate Results

Legend: **PASS** = direct evidence; **PASS-C** = credible but requires MoA pilot; **FAIL** = cannot win as complete system; `component` = retained only for a layer.

| Architecture | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 | H10 | H11 | H12 | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OpenClaw integrated | PASS | PASS | PASS-C | PASS-C | **PASS** | **PASS** | **PASS** | **PASS** | PASS-C | **PASS** | PASS | PASS | **survivor** |
| Hermes + BMAD/BMM/CIS | PASS | PASS | PASS-C | **PASS-C** | PASS | **PASS** | **PASS** | **PASS** | **PASS** | PASS-C | PASS | PASS | **survivor** |
| Hermes native | PASS | PASS | PASS-C | PASS-C | PASS | **PASS** | **PASS** | **PASS** | **PASS** | PASS | **PASS** | PASS | **survivor** |
| Dify + GitHub boundary | PASS | PASS | PASS-C | PASS | **PASS** | PASS | PASS-C | PASS-C | **PASS** | **PASS** | PASS-C | PASS | **survivor conditional** |
| n8n composition | PASS | PASS | PASS-C | PASS-C | PASS | **PASS** | PASS-C | **PASS** local | **PASS** | **PASS** | PASS-C | PASS | **survivor conditional** |
| Agno AgentOS | PASS | PASS | **FAIL** | **FAIL** | PASS | PASS | PASS-C | PASS local | PASS | PASS | PASS-C | PASS | component: too much MoA role/workflow code would be authored |
| CrewAI | PASS | PASS | **FAIL** | **FAIL** | PASS-C | PASS | PASS-C | PASS-C | PASS-C | PASS-C | PASS-C | PASS | component |
| LangGraph / Deep Agents | PASS | PASS | **FAIL** | **FAIL** | PASS-C | **PASS** | PASS-C | PASS-C | PASS | PASS-C | PASS-C | PASS | component |
| Langflow | PASS | PASS | FAIL | FAIL/PASS-C | PASS | PASS | PASS-C | PASS local | PASS-C | PASS | PASS-C | PASS | component |
| AutoGen | PASS | PASS | FAIL | FAIL | PASS-C | PASS-C | PASS-C | PASS local | PASS-C | PASS-C | PASS | PASS | component |
| Letta | PASS | PASS | FAIL | FAIL | **PASS** | PASS | PASS-C | PASS local | PASS-C | PASS | PASS | PASS | component: memory specialist |
| Spec Kit + GitHub | PASS | **PASS** | PASS | PASS-C | **FAIL** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS-C** | PASS | PASS-C | component: excellent L3/L4, lacks L1/L5 whole-org coverage |
| BMAD standalone | PASS | **PASS** | PASS-C | **PASS** | **FAIL** | **FAIL as runtime state** | PASS-C | **PASS via supported tools/web bundles** | PASS-C | PASS-C | PASS | PASS | component: L4/L5 donor |
| Beads | PASS | PASS | PASS | **FAIL** | **FAIL** | **PASS** | PASS-C | PASS | PASS | **FAIL/PASS-C** | PASS-C | PASS | component: task graph |
| OpenSpec | PASS | PASS | FAIL | FAIL | FAIL | PASS change-state | PASS | PASS | PASS-C | **FAIL** | PASS | PASS | component |
| Task Master | PASS | PASS | FAIL | FAIL | FAIL | PASS | PASS | PASS | PASS-C | **FAIL** | PASS | PASS | component |
| Superpowers | PASS | PASS | FAIL | PASS-C | FAIL | **FAIL as portfolio runtime** | PASS | PASS | PASS | **FAIL** | PASS | PASS | component |
| Ruflo | PASS | PASS | PASS-C | PASS | PASS | PASS | PASS | PASS-C | PASS-C | **FAIL** | **FAIL** | PASS-C | disqualified as MoA core |
| Gas City | PASS | PASS-C | PASS | PASS-C | PASS-C | PASS | PASS-C | PASS-C | PASS | **FAIL** | **FAIL** | PASS | disqualified as MoA core |
| GitHub + Agent Skills | PASS | **PASS** | PASS-C | PASS-C | **FAIL** | **PASS** project state | **PASS** | PASS | PASS-C | **PASS** | **PASS** | **PASS** | component/control, not full runtime |

### Gate interpretations that matter

- **H3 reuse before invention:** generic support for custom agents is not enough. Agno/CrewAI/LangGraph can build the target, but doing so would make Master of Arts author most role definitions and orchestration semantics itself.
- **H4 integrated specialists:** OpenClaw passes only conditionally because ClawHub is mature and searchable but mostly community-authored. Hermes+BMAD is stronger because BMAD’s core/BMM/CIS specialists are upstream packages, yet their execution under Hermes is a cross-product adaptation requiring a compatibility pilot. [S031][S033][S046]
- **H5 knowledge/context:** OpenClaw is the cleanest verified implementation: canonical Markdown + derived local retrieval/provenance. Hermes qmd is credible and local but is an optional skill with additional dependencies/platform limits. [S015][S041]
- **H7/H8:** OpenClaw and Hermes both have real subscription/local paths rather than “just point an API model at it.” OpenClaw documents ChatGPT/Codex OAuth and CLI runtime reuse; Hermes documents OpenAI Codex subscription, Nous Portal subscription and local/custom endpoints. [S014][S042]
- **H10 non-software:** Dify/n8n are naturally business-oriented. OpenClaw/Hermes are general agent runtimes with explicit research/content/operations use cases. Coding-only systems remain components even when arbitrary prompts could technically repurpose them.

---

## Deep Evidence

## 1. OpenClaw integrated stack

### L1–L10 map

| Layer | Exact owner | Capability status | Evidence / caveat |
|---|---|---|---|
| L1 knowledge | Builtin memory over canonical `MEMORY.md`, `USER.md`, `memory/*.md`, optional extra paths | **N** | Hybrid BM25/vector; relevance/recency/importance; MMR; provenance; local embeddings available. [S041] |
| L2 portfolio_ssot | Bundled Workboard | **N** | Durable SQLite boards/cards, priorities/statuses, dependencies, comments, attempts, proof/artifacts, assignments. Intentionally local/small, not enterprise PM. [S040] |
| L3 orchestrator | Workboard dispatch + task ledger + subagents/swarm | **N** | Claims, dependencies, direct dispatch, isolated subagents and tracked background work. [S040][S043] |
| L4 workflows | Skills, OpenProse/task-flow/automations, ClawHub packaged skills | **N/P** | Broad mechanism and registry; package quality varies. [S045][S046] |
| L5 specialists | ClawHub skills + configured agents | **P/A** | Verified assets exist for research, content and social ops. Missing MoA workshop/coaching/Leela specialists. [S048][S049][S050][S051] |
| L6 tools | web/browser/files/exec/PDF/media/MCP/plugins | **N/I** | Broad first-party capability surface. [S040][S045] |
| L7 executors | OpenAI/Codex OAuth, Claude CLI, Gemini CLI, API/local providers | **N/I** | Strong subscription + local portability. [S042] |
| L8 review/governance | Workboard `review` state; operator permissions; exec approvals; explicit manual `done` acceptance | **N/A** | Mechanics native; MoA maker/reviewer policy is configuration/adaptation. [S040] |
| L9 artifacts | Workboard artifact/proof refs + workspace/repo files | **N/A** | Canonical final artifact should remain Git; Workboard links execution evidence. |
| L10 learning | canonical memory promotion + self-learning/skills | **N/A** | Memory trust/provenance is native; CEO-approved promotion policy for organizational facts still needs a small MoA rule. [S041] |

### Actual specialist assets found

| Family | Existing asset | Status | Finding |
|---|---|---|---|
| research strategist / deep researcher | ClawHub `@brennerspear/research-agent`; several deep-research alternatives | **P** | Existing reusable workflow with living Markdown research output. Community asset. [S048] |
| comparative/market analyst | market-research and desk-research skills | **P** | Exists; package trust/provenance varies. |
| creative/content | `@ethagent/content`, Content Writer | **P** | Strategy, writing/editing, repurposing assets exist. [S050] |
| social-media pipeline | `@dougbtv/social-ops` | **P** | Six roles: Scout, Researcher, Content Specialist, Responder, Poster, Analyst with role I/O. [S049] |
| content research | `@hazy2go/content-research` | **P** | Research → create multi-platform workflow. [S051] |
| independent reviewer | generic reviewer can be configured; no MoA-domain reviewer pack verified | **A/MISSING** | Workboard supports separate review stage, but role must be selected/configured. |
| workshop designer | — | **MISSING** | No verified prebuilt asset found. |
| pedagogy reviewer | — | **MISSING** | No verified prebuilt asset found. |
| coaching-method analyst | — | **MISSING** | No verified prebuilt asset found. |
| sensitivity/public-private reviewer | — | **MISSING** | Generic safety/review assets are not this role. |
| offer/product | content/market/product skills exist, but exact MoA offer agent not verified | **P/A** | Partial. |
| Leela bridge | — | **MISSING** | Project-specific by nature. |

### Operational profile

- **Install/runtime:** one OpenClaw install plus Gateway; bundled Workboard is enabled, not separately installed. [S047][S040]
- **State:** Workboard relational SQLite; agent/session state; builtin memory SQLite index over canonical Markdown. [S040][S041]
- **Recovery:** automations persist state/run history; Workboard records attempts and lifecycle; subagents are tracked as background tasks. [S040][S044]
- **Security:** operator read/write separation; plugin permission surfaces; memory provenance stored outside recalled prose. Community skills still require audit/trust. [S040][S041][S046]
- **Primary failure mode:** marketplace breadth can look like specialist coverage while actually importing inconsistent third-party instructions/permissions; must pin and audit a small approved skill set.

## 2. Hermes Agent + BMAD/BMM/CIS

### L1–L10 map

| Layer | Exact owner | Status | Evidence / caveat |
|---|---|---|---|
| L1 knowledge | repo Markdown + Hermes memory + optional qmd | **N/P** | qmd is official optional local hybrid retrieval; not as native/integrated as OpenClaw builtin memory. [S015] |
| L2 portfolio_ssot | Hermes Kanban board | **N** | Durable SQLite tasks, states, dependencies, comments, attachments, board separation. [S010] |
| L3 orchestrator | Kanban dispatcher + named profiles | **N** | Ready promotion, retries, review loops, scheduled starts, decomposition, swarms. [S010] |
| L4 workflows | BMAD workflow/task/tool `SKILL.md` + Hermes skills | **P/A** | Both sides document SKILL.md; cross-product execution is generic standards-based adaptation, not a named official pairing. [S011][S033] |
| L5 specialists | BMAD Analyst/PM + CIS agents + Hermes skills | **P** | Better upstream specialist coverage than Hermes alone. Workshop/coaching/Leela still missing. [S031][S032] |
| L6 tools | Hermes terminal/files/web/browser/code + skills | **N** | broad runtime tools. [S013] |
| L7 executors | Codex subscription, Nous Portal, Anthropic path, local/custom endpoints | **N/I** | Strong. Some subscription semantics differ by provider. [S014] |
| L8 review | Kanban `review`/request-changes + BMAD `bmad-review` | **N/P** | Strong maker/reviewer mechanics and multi-lens artifact review. [S010][S030] |
| L9 artifacts | repo files + Kanban attachments/handoff metadata | **N/A** | Keep Git as final artifact truth. |
| L10 learning | Hermes memory/skill self-improvement + `/learn`; qmd over accepted docs | **N/A** | Procedure capture native; governed fact promotion still needs policy. [S011][S018] |

### Existing specialist assets

BMAD current official evidence materially improves its donor value relative to the prior Master of Arts analysis:

- `bmad-deep-recon`: decision-grade research on **any subject**, with draft/process/run modes; [S030][S035]
- `bmad-review`: multi-lens review for code **and documents**, including adversarial/edge-case/structure/prose; [S030]
- Analyst Mary: brainstorming, market/domain/technical research, brief, PRFAQ challenge, project context; [S032]
- PM John and UX Sally: product/experience planning; [S032]
- Creative Intelligence Suite: Innovation Strategist, Design Thinking Coach, Brainstorming Coach, Problem Solver, Creative Problem Solver, Storyteller and Presentation Master; [S031]
- installer-generated skills: one `SKILL.md` per agent/workflow/task/tool, with documented `.claude/skills/` and `.agents/skills/` target directories; [S033]
- **No current BMAD community marketplace should be credited:** current official module docs still say community modules/marketplace are coming. [S031]

### Integration risk

Hermes is compatible with the open Agent Skills standard and can scan external skill directories; BMAD generates `SKILL.md` packages. This establishes a documented mechanism on both sides, but **there is no official source saying “BMAD under Hermes is supported.”** Therefore this architecture is `A` at the cross-product seam and must be piloted before being treated as an upstream-supported production composition. [S011][S033]

### Primary failure mode

A nominally simple “skills interop” could conceal path/reference/activation assumptions tied to BMAD-supported IDEs. If BMAD skills do not run unmodified under Hermes, do **not** fork BMAD into a custom MoA framework; fall back to Hermes native or OpenClaw.

## 3. Hermes Agent native

### Strengths

Hermes Kanban is now a genuine durable agent operating substrate rather than an in-chat delegation primitive. Official docs distinguish `delegate_task` (fork/join, no human in loop, not resumable) from Kanban (durable queue/state machine, named profiles, retries, review, human comment/unblock, audit rows). It explicitly lists research triage, scheduled ops and persistent named assistants as target workloads. [S010]

Agent Skills use progressive disclosure; skills can be installed, created and gated for human approval before writes land. Memory writes can be similarly gated. [S011][S012]

### Weaknesses

The official/established skill catalog has useful research and creative skills, but the verified specialist roster is thinner than BMAD or ClawHub. Hermes therefore wins on orchestration/governance/portability but loses C2 until MoA-specific roles are added or a vetted external skill pack is proven.

## 4. Dify composition

First-party LangGenius marketplace evidence is materially stronger than generic “can make workflows” claims:

- official creator page currently exposes ~40 templates and ~40 plugins; [S080]
- `Human Input: Writing Assistant` has a real pause → human approve/feedback → refinement flow; [S081]
- `Market Research Agent` is an upstream non-code research workflow; [S082]
- `Knowledge Retrieval: A Smart Chatbot` is an upstream RAG template; [S083]
- a current work-ticket template demonstrates operations/knowledge/action integration. [S084]

This is credible H4/H5/H9/H10 evidence. It remains fourth because workflow/state definitions are Dify-centric, model execution is primarily provider-plugin/API/local rather than portable subscription AI clients, and a CEO portfolio SSOT still needs an external boundary.

## 5. n8n composition

n8n is the strongest **business automation component** discovered: execution history, waiting/approval patterns, very broad SaaS nodes, AI Agent nodes, multiple vector stores, Ollama models and a large live template marketplace. Official docs show human approval can pause AI tool calls; the integration catalog spans GitHub, Google Workspace, CRM, social and operations systems. [S070][S071][S072][S073][S074]

It remains fifth because the target is an AI organization, not an automation canvas. n8n workflows are durable, but specialist identity/skill reuse is less standardized; useful “executive team” and research/publishing templates are frequently community examples with API-specific assumptions. A complete MoA stack also introduces GitHub + n8n + vector store + model runtime, which is a larger operational surface than OpenClaw or Hermes.

---

## MCDA

Scores are 0–5. Weighted total = `SUM(score / 5 * weight)`. Confidence grades reflect evidence quality for that **score**, not software quality.

| Rank | Complete architecture | C1 15 | C2 15 | C3 12 | C4 12 | C5 12 | C6 10 | C7 8 | C8 7 | C9 5 | C10 4 | Total /100 | Confidence | Primary failure mode |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | OpenClaw integrated | 4.6 | 4.0 | 4.9 | 4.6 | 4.7 | 4.6 | 4.4 | 4.4 | 4.2 | 3.8 | **89.5** | B | Community skill trust/quality; MoA specialist gaps |
| 2 | Hermes + BMAD/BMM/CIS | 4.5 | 4.0 | 4.3 | 4.8 | 5.0 | 4.3 | 4.7 | 3.8 | 3.6 | 4.2 | **87.7** | B | Cross-product skill compatibility unproven |
| 3 | Hermes native | 4.3 | 3.4 | 4.2 | 4.8 | 4.9 | 3.8 | 4.5 | 3.9 | 4.5 | 4.3 | **84.7** | B | Missing relevant prebuilt specialist breadth |
| 4 | Dify + GitHub boundary | 3.8 | 3.6 | 4.6 | 4.0 | 2.8 | 4.6 | 4.1 | 4.5 | 3.0 | 3.2 | **77.2** | B | Dify-centric state; weak subscription-client portability |
| 5 | n8n + GitHub + vector/Ollama | 3.9 | 3.7 | 3.5 | 4.3 | 2.9 | 4.8 | 4.4 | 4.7 | 2.8 | 3.2 | **77.1** | B | Multi-service glue and weak specialist standard |

### Score rationales

#### OpenClaw

| Criterion | Score | Conf. | Evidence-grounded rationale |
|---|---:|:---:|---|
| C1 integrated coverage | 4.6 | A/B | Workboard + memory + runtime + skills + tools + automations + artifacts cover nearly every L layer; governed learning promotion remains partly policy. |
| C2 specialists | 4.0 | B/C | Live ClawHub provides real reusable research/content/social packages, but these are mostly third-party and several MoA families are missing. |
| C3 knowledge/learning | 4.9 | A | Native hybrid retrieval, canonical Markdown, local providers, provenance and deterministic trust/ranking are direct official evidence. |
| C4 orchestration/resume | 4.6 | A | Durable Workboard task/dependency/attempt state, subagents, dispatch and automations are native. |
| C5 executor portability | 4.7 | A | ChatGPT/Codex OAuth plus CLI/provider/local runtime choices; state is not confined to one model chat. |
| C6 non-software fit | 4.6 | B | Research/content/social/community skills and general task model are naturally non-code. |
| C7 governance | 4.4 | A/B | Review state, operator scopes, approval surfaces and memory provenance are native; MoA review policy is configuration. |
| C8 maturity | 4.4 | B | Active 2026 docs/releases and broad ecosystem; still newer/less institutionally mature than GitHub/n8n. |
| C9 reuse/integration risk | 4.2 | B | Core is one ecosystem; ClawHub quality introduces vetting risk but no mandatory bespoke framework. |
| C10 ops/security | 3.8 | B | One gateway + SQLite is bounded, but plugin/skill permission surface and always-on runtime require discipline. |

#### Hermes + BMAD/BMM/CIS

| Criterion | Score | Conf. | Rationale |
|---|---:|:---:|---|
| C1 | 4.5 | B | Hermes owns runtime/state; BMAD supplies methods/specialists; qmd supplies retrieval. L10 still partly configured. |
| C2 | 4.0 | A/B | BMAD/CIS has strong upstream roles for research, product and creativity; MoA workshop/coaching families missing. |
| C3 | 4.3 | B | qmd is credible local retrieval and repo files remain canonical; integration is less native than OpenClaw memory. |
| C4 | 4.8 | A | Hermes Kanban directly supports dependencies, review/change, retries, scheduling, resumability and structured handoffs. |
| C5 | 5.0 | A/B | Strongest verified model/client spectrum among finalists, including Codex subscription, Nous subscription and local/custom endpoints. |
| C6 | 4.3 | B | Hermes is general; BMAD research/creative assets are domain-neutral, though BMM vocabulary remains software/product heavy. |
| C7 | 4.7 | A | Native review/request-changes/human unblock plus BMAD adversarial review. |
| C8 | 3.8 | B | Both are active, but Hermes Kanban is very recent and composition lacks long production history. |
| C9 | 3.6 | C/B | Two ecosystems joined through generic skill standards; seam requires pilot. |
| C10 | 4.2 | B | One runtime + local DB + optional qmd; bounded, but external skill paths add trust/update concerns. |

#### Hermes native

| Criterion | Score | Conf. | Rationale |
|---|---:|:---:|---|
| C1 | 4.3 | B | Owns most control/runtime responsibilities; specialist and knowledge layers are less rich. |
| C2 | 3.4 | B | Official/skills.sh mechanism is mature, but verified MoA-relevant prebuilt specialists are sparse. |
| C3 | 4.2 | B | Persistent memory + optional qmd + repo files; credible but not a unified native organizational KB. |
| C4 | 4.8 | A | Same native Kanban strengths as above. |
| C5 | 4.9 | A | Very strong subscription/local executor range. |
| C6 | 3.8 | B | General agent runtime and research/creative skills fit, but fewer packaged business workflows. |
| C7 | 4.5 | A | Strong explicit review/change/human block semantics and write-approval gates. |
| C8 | 3.9 | B | Rapid active maintenance; newest Kanban functionality has limited battle age. |
| C9 | 4.5 | B | Small composition with little glue. |
| C10 | 4.3 | B | Local SQLite, progressive skills and narrow profile toolsets can be kept compact/auditable. |

#### Dify composition

| Criterion | Score | Conf. | Rationale |
|---|---:|:---:|---|
| C1 | 3.8 | B | Strong workflow/KB/HITL/output; external portfolio/repo boundary remains. |
| C2 | 3.6 | B | First-party LangGenius templates are real but not a deep durable persona library. |
| C3 | 4.6 | A/B | First-class knowledge retrieval and RAG patterns. |
| C4 | 4.0 | B | Durable workflows and human-input pause; portfolio-level routing/resume weaker. |
| C5 | 2.8 | B | Model/provider flexibility exists, but subscription repo-capable AI-client portability is weak. |
| C6 | 4.6 | A/B | Official research, writing, support and ticket workflows prove non-code fit. |
| C7 | 4.1 | A/B | Human Input is first-party and explicit; maker/reviewer organization still configured per workflow. |
| C8 | 4.5 | A/B | Mature active platform and marketplace. |
| C9 | 3.0 | B | GitHub/portfolio integration and Dify-specific state add seams. |
| C10 | 3.2 | B | Self-hosting is heavier than one-runtime finalists; cloud reduces ops but increases platform dependence. |

#### n8n composition

| Criterion | Score | Conf. | Rationale |
|---|---:|:---:|---|
| C1 | 3.9 | B | Excellent execution/integration; weaker unified specialist/knowledge/portfolio ownership. |
| C2 | 3.7 | B/C | Very large template ecosystem, but reusable roles are often workflow-specific/community-authored. |
| C3 | 3.5 | B | RAG/vector nodes are powerful; canonical KB governance requires external design/storage. |
| C4 | 4.3 | A/B | Durable workflow executions, waits, branches, subworkflows and retries are core strengths. |
| C5 | 2.9 | B | Local Ollama is strong H8 evidence; subscription CLI agent reuse is not a native center of gravity. |
| C6 | 4.8 | A | Business/non-code automation is n8n’s native domain. |
| C7 | 4.4 | A | HITL approval before AI tool calls and explicit wait patterns are documented. |
| C8 | 4.7 | A | Mature, widely used, active ecosystem. |
| C9 | 2.8 | B | Complete MoA composition adds GitHub + vector DB + model + n8n semantics. |
| C10 | 3.2 | B | Powerful security/credentials controls, but larger operational and credential surface. |

### Sensitivity checks

The raw 0–5 scores above were held constant; only weights changed.

| Architecture | Balanced | Autonomy-first | Knowledge-first | Simplicity/portability-first |
|---|---:|---:|---:|---:|
| **OpenClaw** | **89.5** | **88.4** | **90.9** | **88.6** |
| Hermes + BMAD | 87.7 | 87.9 | 87.6 | 87.7 |
| Hermes native | 84.7 | 84.6 | 84.2 | 87.1 |
| Dify composition | 77.2 | 77.1 | 80.4 | 71.9 |
| n8n composition | 77.1 | 78.4 | 77.9 | 71.9 |

**Result:** the #1 architecture does not change. The gap narrows materially under autonomy-first and simplicity/portability-first, so a poor OpenClaw pilot can still reverse the decision. Knowledge-first strengthens OpenClaw because its current builtin memory is unusually well aligned with L1.

---

## User Stories

The same four paper prototypes are applied to the top three. `MISSING` is intentional where no verified prebuilt specialist exists.

## Top 1 — OpenClaw integrated

### US-A research_to_knowledge

| Step | System/component | Specialist agent/workflow | AI executor options | KB/context supplied | Tools | Durable state/output | Reviewer/gate | Status |
|---:|---|---|---|---|---|---|---|:---:|
| 1 | Workboard | orchestrator agent | Codex OAuth / Claude CLI / local model | CEO brief + portfolio card | Workboard tools | card + comments | CEO defines consequential gate | N/A |
| 2 | builtin memory | — | same | relevant canonical Markdown with provenance | memory search | retrieval trace/index | — | N |
| 3 | ClawHub skill | Research / deep-research skill | any supported executor | brief + retrieved context | web/search/browser | living `research.md` + Workboard artifact ref | — | P |
| 4 | separate Workboard child | source/evidence verifier | separate executor/session | research output + sources | web fetch/search | verifier findings card | **verified prebuilt dedicated verifier: MISSING** | A/MISSING |
| 5 | Workboard child | synthesis writer / content skill | executor | evidence + verifier findings | files | synthesis draft | — | P/A |
| 6 | Workboard review | independent reviewer | separate agent/session | draft + source registry | review task | review comments/proof | maker/reviewer separation configured | A |
| 7 | Workboard | — | human | draft + review | Control UI | acceptance event | **CEO** | N |
| 8 | Git repo/workspace | — | executor | approved artifact | files/git | final research artifact/history | CEO accepted | A |
| 9 | builtin memory | learning promotion | executor + human | accepted findings/procedure | memory/skills | canonical memory/skill update | require human approval for consequential org learning | A |

### US-B workshop_creation

| Step | System/component | Specialist agent/workflow | AI executor options | KB/context supplied | Tools | Durable state/output | Reviewer/gate | Status |
|---:|---|---|---|---|---|---|---|:---:|
| 1 | Workboard | orchestrator | any | desired workshop outcome | Workboard | root card | — | N |
| 2 | builtin memory | retrieval | any | prior workshops/research/method | memory search | retrieved context | — | N |
| 3 | specialist skill | **workshop designer: MISSING** | any | brief + knowledge | files | workshop draft | — | MISSING |
| 4 | specialist skill | **pedagogy/learning reviewer: MISSING** | separate | workshop draft | review tools | review artifact | gate before finalization | MISSING |
| 5 | specialist skill | **operations/logistics reviewer: MISSING as domain specialist** | separate | draft + constraints | generic reviewer | risk/logistics notes | — | MISSING/A |
| 6 | Workboard | — | human | draft + reviews | UI | accepted card | **CEO** | N |
| 7 | repo + Workboard | launch/task formalizer | any | approved workshop | files + board | final workshop + launch cards | — | A |
| 8 | builtin memory | post-delivery learning | any + CEO | retrospective | memory | promoted lesson | CEO promotion policy | A |

### US-C content_social

| Step | Component | Specialist | Executor | Context | Tools | Durable output | Reviewer/gate | Status |
|---:|---|---|---|---|---|---|---|:---:|
| 1 | Workboard + memory | creative strategist | any | approved research/workshop concept | memory/files | content brief | — | P/A |
| 2 | ClawHub | Content / Content Writer | any | brief + voice refs | files | long-form draft | — | P |
| 3 | review card | **brand/voice reviewer: MISSING as verified specialist** | separate | draft + brand canon | files | review notes | review | MISSING/A |
| 4 | ClawHub Social Ops | Scout/Researcher/Content Specialist/etc. | parallel sessions | approved long-form + channel rules | web/social tools | derivative posts/campaign state | — | P |
| 5 | specialist | **video/script specialist: MISSING in vetted shortlist** | any | content | media tools | scripts | — | MISSING |
| 6 | specialist | **public/private sensitivity reviewer: MISSING** | separate | all public outputs | review | sensitivity decision | mandatory for flagged content | MISSING |
| 7 | Workboard | publish coordinator | any/human | approved assets | channel tools | publication-ready artifacts | CEO gate when consequential | A |
| 8 | Workboard | portfolio updater | agent | publication result | board | status/metrics links | — | N |

### US-D weekly_ceo_operating_cycle

| Step | Component | Specialist/workflow | Executor | Context | Tools | Durable state | Reviewer/gate | Status |
|---:|---|---|---|---|---|---|---|:---:|
| 1 | Workboard | portfolio collection | agent | all active cards/boards | Workboard list/stats | board DB | — | N |
| 2 | Workboard | blocker/stale/dependency analysis | orchestrator | lifecycle/attempt metadata | diagnostics/dependencies | comments/proof | — | N/A |
| 3 | specialist | **portfolio project-controller specialist: MISSING** | agent | portfolio state | board | recommendation artifact | — | MISSING/A |
| 4 | automations | routine follow-ups | agent/local script | approved rules | automations | run history/tasks | only exceptions surface | N |
| 5 | Workboard | exception routing | orchestrator | blockers/review items | board | review/blocked cards | **CEO only on consequential items** | N/A |
| 6 | Workboard/comments | decision persistence | human/agent | CEO response | UI/tools | durable comments/events | CEO | N |
| 7 | automations + board | next-cycle scheduling | agent | accepted decisions | scheduler | persisted jobs + cards | — | N |

## Top 2 — Hermes + BMAD/BMM/CIS

### US-A research_to_knowledge

| Step | Component | Specialist/workflow | Executor | KB/context | Tools | Durable output | Gate | Status |
|---:|---|---|---|---|---|---|---|:---:|
| 1 | Hermes Kanban | orchestrator profile | Codex subscription / Nous / local | CEO brief | kanban | task graph | — | N |
| 2 | qmd | retrieval | same | relevant repo corpus | qmd | cited retrieval | — | P |
| 3 | BMAD | `bmad-deep-recon` | Hermes if compatibility pilot passes; otherwise supported BMAD client | brief + corpus | web/research | cited research report | — | P/A |
| 4 | BMAD | deep-recon verification + separate reviewer | independent profile | report/sources | web | verification notes | maker/reviewer | P/A |
| 5 | BMAD Analyst | synthesis | profile | evidence | files | synthesis | — | P |
| 6 | BMAD | `bmad-review` | separate profile/client | draft | review lenses | findings | reviewer | P/A |
| 7 | Hermes Kanban | — | human | draft/review | review state | accepted task | CEO | N |
| 8 | Git repo | writer | executor | accepted draft | files/git | final artifact | — | A |
| 9 | Hermes `/learn` + qmd | procedural/fact promotion | agent + CEO | accepted learning | skill/memory/files | skill or canonical KB update | CEO promotion rule | N/A |

### US-B workshop_creation

| Step | Component | Specialist | Executor | Context | Output | Gate | Status |
|---:|---|---|---|---|---|---|:---:|
| 1 | Kanban | orchestrator | Hermes | outcome | root task | — | N |
| 2 | qmd | retrieval | Hermes | method/research | context packet | — | P |
| 3 | BMAD/CIS | **workshop designer: MISSING**; Design Thinking Coach is adjacent, not equivalent | supported client | brief | workshop draft | — | MISSING/A |
| 4 | reviewer card | **pedagogy reviewer: MISSING** | separate | draft | review | gate | MISSING |
| 5 | reviewer card | **operations/logistics reviewer: MISSING as specialist** | separate | draft | risk notes | gate | MISSING/A |
| 6 | Kanban | — | human | draft/reviews | accepted state | CEO | N |
| 7 | repo/Kanban | task formalizer | executor | approved workshop | final workshop + launch tasks | — | A |
| 8 | `/learn`/qmd | retrospective promotion | agent+CEO | delivery feedback | reusable lesson | CEO | A |

### US-C content_social

| Step | Component | Specialist | Executor | Context | Output | Gate | Status |
|---:|---|---|---|---|---|---|:---:|
| 1 | CIS | Innovation Strategist / Storyteller | BMAD-supported client or Hermes after pilot | concept + qmd | creative brief | — | P/A |
| 2 | CIS | Storyteller | same | brief/voice | long-form | — | P |
| 3 | BMAD review | prose/structure reviewer | separate | draft | review | reviewer | P |
| 4 | Hermes official skill | social-media content calendar | Hermes | approved content | social plan/assets | — | P |
| 5 | specialist | video/script writer | — | — | — | — | MISSING unless separately vetted |
| 6 | specialist | public/private sensitivity reviewer | — | — | — | mandatory if flagged | MISSING |
| 7 | Kanban/repo | publisher | agent/human | accepted assets | final files/status | CEO as required | A |

### US-D weekly_ceo_operating_cycle

| Step | Component | Specialist | Executor | Context | Output/state | Gate | Status |
|---:|---|---|---|---|---|---|:---:|
| 1 | Kanban | orchestrator | Hermes | active board | state snapshot | — | N |
| 2 | Kanban | deterministic dependency/blocker analysis | Hermes/script | board | next/blocked set | — | N |
| 3 | BMAD `bmad-help` | adjacent project guidance; exact portfolio controller MISSING | BMAD/Hermes | artifacts/state | recommendations | — | P/A |
| 4 | Hermes cron/Kanban | routine follow-ups | Hermes | approved policy | new/updated tasks | exceptions only | N |
| 5 | Kanban | review/blocked escalation | Hermes | exceptions | review queue | CEO | N |
| 6 | comments/metadata | decision persistence | human/agent | decision | durable handoff | CEO | N |

## Top 3 — Hermes native

The same flow is mechanically strong, but the specialist column is materially emptier:

- US-A: qmd + Hermes research skills can gather/synthesize, but a verified upstream research-strategist/source-verifier/synthesis-writer trio is incomplete.
- US-B: workshop designer, pedagogy reviewer, coaching-method analyst and operations/sensitivity specialists are **MISSING**.
- US-C: official creative-ideation and social-content-calendar skills help, but long-form brand/editor/video/public-private specialist coverage is incomplete.
- US-D: Kanban/cron/profile mechanics are **N** and are the stack’s main strength; exact portfolio-controller/knowledge-curator specialists remain **MISSING/A**.

This is why Hermes native is the simplicity control rather than the specialist-ecosystem winner.

---

## Top-3 Realization Blueprints

### Blueprint 1 — OpenClaw integrated

```yaml
architecture_name: OpenClaw + Workboard + builtin memory + curated ClawHub skills
portfolio_ssot: OpenClaw Workboard SQLite boards/cards for operating work
knowledge_system: canonical repository Markdown indexed by OpenClaw builtin memory; local embeddings permitted
orchestrator: Workboard dispatcher/task ledger + subagents/swarm + automations
workflow_library: OpenClaw skills/task-flow/OpenProse/automations + small audited ClawHub set
specialist_agent_library: curated ClawHub research/content/social skills; configured reviewer agents; MoA workshop/coaching/sensitivity/Leela specialists missing
skill_tool_library: OpenClaw bundled tools/plugins + audited ClawHub skills
executor_clients:
  - ChatGPT/Codex subscription OAuth
  - Claude CLI reuse
  - Gemini CLI runtime
  - API providers
  - local/self-hosted model providers
review_governance: Workboard review state + separate reviewer cards/agents + operator permissions + CEO acceptance on consequential items
artifact_store: MasterOfArts Git repository; Workboard stores artifact/proof references and run evidence
learning_promotion: builtin memory indexes accepted canonical Markdown; procedural learning via approved skills; MoA promotion policy required
mandatory_services:
  - OpenClaw Gateway
  - Git
existing_integrations_used:
  - bundled Workboard plugin
  - builtin memory
  - Codex/CLI runtimes
  - OpenClaw automations
  - ClawHub registry
custom_work_required:
  - item: define and audit a minimal approved ClawHub skill allowlist
    why_unavoidable: marketplace packages are community-authored and vary in permissions/quality
    size: small
  - item: create missing MoA workshop/pedagogy/coaching/sensitivity/Leela specialist skills only after proving no upstream package exists
    why_unavoidable: no verified prebuilt assets found
    size: medium
  - item: define CEO-approved knowledge-promotion rule
    why_unavoidable: retrieval/provenance is native, but organizational acceptance semantics are project governance
    size: small
single_sources_of_truth:
  project_state: OpenClaw Workboard
  knowledge: repository canonical Markdown; OpenClaw SQLite is derived retrieval index
  workflow_state: Workboard task/run/automation state
  final_artifacts: MasterOfArts Git repository
```

#### Verified bootstrap commands

From official OpenClaw documentation [S047][S040][S042]:

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw plugins enable workboard
openclaw gateway restart
openclaw dashboard
openclaw onboard --auth-choice openai
```

Example vetted-marketplace installs are **registry-verified package commands**, not endorsements of package safety [S048][S049][S050]:

```bash
openclaw skills install @brennerspear/research-agent
openclaw skills install @dougbtv/social-ops
openclaw skills install @ethagent/content
```

Do not install these automatically in a pilot. Review their current files/security scan first.

### Blueprint 2 — Hermes + BMAD/BMM/CIS

```yaml
architecture_name: Hermes Agent + BMAD Method/BMM/CIS via Agent Skills
portfolio_ssot: Hermes Kanban board SQLite
knowledge_system: canonical repo Markdown + Hermes memory + official qmd optional skill
orchestrator: Hermes Kanban dispatcher and named profiles
workflow_library: BMAD core/BMM/CIS SKILL.md packages plus Hermes skills
specialist_agent_library: BMAD Analyst/PM/UX + CIS Innovation Strategist/Design Thinking Coach/Brainstorming Coach/Problem Solvers/Storyteller/Presentation Master; MoA-specific roles missing
skill_tool_library: Hermes tools/hub + BMAD-generated skills
executor_clients:
  - OpenAI Codex / ChatGPT subscription path
  - Nous Portal subscription
  - Anthropic supported path
  - local/custom OpenAI-compatible endpoints
review_governance: Hermes request-review/request-changes + BMAD bmad-review + human-only review configuration where required
artifact_store: MasterOfArts Git repo + Kanban attachments/handoff metadata
learning_promotion: Hermes procedural skill memory / learn + qmd indexing of accepted repository knowledge
mandatory_services:
  - Hermes gateway
  - Git
  - qmd dependencies if qmd selected
  - Node.js 20.12+ for BMAD installer
existing_integrations_used:
  - Hermes external/project Agent Skills directories
  - BMAD installer-generated SKILL.md
  - Hermes Kanban
custom_work_required:
  - item: validate BMAD-generated skills execute unmodified under Hermes
    why_unavoidable: both products document compatible skill files/directories, but the pair is not an upstream-tested named integration
    size: small
  - item: add only missing MoA specialist skills
    why_unavoidable: workshop/pedagogy/coaching/sensitivity/Leela families were not found upstream
    size: medium
  - item: define governed fact-promotion rule
    why_unavoidable: procedural learning exists; organizational acceptance semantics are local policy
    size: small
single_sources_of_truth:
  project_state: Hermes Kanban
  knowledge: repository KB Markdown indexed by qmd
  workflow_state: Hermes Kanban plus BMAD-produced workflow artifacts
  final_artifacts: MasterOfArts Git repository
```

#### Verified bootstrap commands

Hermes official [S019]:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes model
hermes kanban init
hermes gateway start
```

Optional Nous subscription path [S019]:

```bash
hermes setup --portal
```

BMAD official [S034]:

```bash
npx bmad-method install
npx bmad-method install --list-tools
npx bmad-method install --yes --modules bmm,bmb,cis --tools claude-code
```

Cross-runtime wiring:

`NOT VERIFIED — DO NOT EXECUTE`: no official source directly documents running BMAD-generated skills under Hermes. The pilot should first use `--list-tools`/generated skill directories and Hermes’ documented external-directory discovery to test the seam without copying or rewriting BMAD assets.

### Blueprint 3 — Hermes native

```yaml
architecture_name: Hermes Agent native + official/established skills + qmd
portfolio_ssot: Hermes Kanban SQLite
knowledge_system: canonical repo Markdown + Hermes memory + official qmd skill
orchestrator: Hermes Kanban dispatcher + profiles
workflow_library: Hermes bundled/official/skills.sh-compatible skills
specialist_agent_library: official/established research and creative skills; substantial MoA specialist gaps
skill_tool_library: Hermes toolsets, optional skills and trusted external Agent Skills
executor_clients:
  - Codex subscription
  - Nous Portal subscription
  - supported API providers
  - local/self-hosted endpoints
review_governance: Kanban review/change/block/unblock + separate reviewer profile + CEO human-only gate where configured
artifact_store: MasterOfArts Git repository + Kanban evidence/attachments
learning_promotion: skill_manage and memory with optional write-approval + qmd over accepted Markdown
mandatory_services:
  - Hermes gateway
  - Git
  - qmd dependencies if selected
existing_integrations_used:
  - Hermes Kanban
  - Hermes Agent Skills
  - Hermes memory/write approval
  - official qmd skill
custom_work_required:
  - item: MoA specialist package
    why_unavoidable: required workshop/coaching/sensitivity/Leela roles are not prebuilt in verified official catalog
    size: medium
  - item: governed knowledge promotion rule
    why_unavoidable: acceptance semantics are MoA-specific
    size: small
single_sources_of_truth:
  project_state: Hermes Kanban
  knowledge: repo Markdown indexed by qmd
  workflow_state: Hermes Kanban
  final_artifacts: MasterOfArts Git repository
```

Verified Hermes commands are the same as Blueprint 2. The qmd skill install is documented in its official catalog page [S015]; execute only after confirming supported OS/runtime in the pilot environment.

---

## Decision Triggers

### 1. OpenClaw integrated

**select_if:**
- one ecosystem owning portfolio work, retrieval, agent execution, automation and tools is more valuable than importing a stronger methodology layer;
- local/provenance-aware knowledge retrieval is load-bearing;
- ChatGPT/Codex subscription and CLI-runtime reuse are strategic;
- the operator is willing to maintain a **small audited skill allowlist**, not indiscriminately install marketplace packages.

**avoid_if:**
- Workboard’s intentionally local/small project model proves too weak for portfolio planning across MoA projects;
- ClawHub package provenance/quality creates more review burden than specialist reuse saves;
- all specialist roles must come from upstream first-party packages.

**pilot_to_prove:**
1. Run US-A end-to-end with Workboard + builtin memory + one audited research skill; verify provenance, review separation, restart recovery and final Git artifact.
2. Run US-D for one week; test whether Workboard is sufficient as the CEO operating SSOT without a second project tracker.
3. Audit/install at most three ClawHub packages and measure instruction conflicts, permission surface and update drift.
4. Test memory promotion: accepted knowledge must be canonical repo Markdown; derived SQLite state must be rebuildable.

### 2. Hermes + BMAD/BMM/CIS

**select_if:**
- prebuilt research/review/creative methodology is more valuable than a single-stack purity goal;
- Hermes Kanban’s explicit worker/reviewer lifecycle is preferred;
- the BMAD skill bridge works **without modifying upstream BMAD assets**.

**avoid_if:**
- BMAD references fail under Hermes or require forks/shims/custom translations;
- BMAD’s software/product vocabulary dominates non-software work;
- two update channels create unacceptable drift.

**pilot_to_prove:**
1. Install BMAD to an official skill directory and execute `bmad-deep-recon`, `bmad-review` and one CIS agent through Hermes without modifying their generated files.
2. Confirm referenced source files and relative paths resolve correctly.
3. Run US-A and US-C; measure context overhead against Hermes-native and OpenClaw.
4. Verify human-only consequential review can coexist with automated low-risk completion.

### 3. Hermes native

**select_if:**
- simplicity and low integration risk dominate specialist reuse;
- the operator accepts adding a small MoA-specific specialist layer only after workflow pilots;
- strong durable Kanban/review semantics matter more than sophisticated native RAG.

**avoid_if:**
- authoring missing specialists would recreate the custom-framework problem;
- qmd/runtime platform constraints are poor on the target host;
- the same workflows require repeated prompt construction due insufficient reusable assets.

**pilot_to_prove:**
1. US-A with qmd and isolated reviewer profile.
2. US-D with real dependencies, blocked work, review changes, restart and scheduled follow-up.
3. Compare manual specialist prompting against BMAD/ClawHub package reuse.

---

## Uncertainties

| Unknown | Consequence | Evidence status | Resolution |
|---|---|---|---|
| OpenClaw Workboard adequacy for portfolio-level CEO planning | Could require GitHub Projects/another L2 and reduce simplicity advantage | B | one-week US-D pilot |
| ClawHub skill trust/version stability | Could turn reuse into audit/update burden | C/B | pin 2–3 skills, inspect files/scans, no auto-update during pilot |
| BMAD-on-Hermes execution compatibility | Load-bearing for rank #2 | C/B | execute generated skills unmodified; reject composition if shim needed |
| Hermes qmd on target operating environment | Affects L1 quality | B | install/read/retrieve pilot; compare to OpenClaw builtin memory |
| Reliable independent reviewer isolation in non-code workflows | Self-certification risk | B | force separate profile/session/model and inspect handoff inputs |
| Governing factual learning vs procedural learning | Risk of contaminating KB with agent guesses | C | explicit CEO promotion rule; canonical repo Markdown only |
| Missing workshop/coaching/sensitivity/Leela specialists | Requires project-specific work | A finding | search again during pilot; create only truly missing skills after reuse scan |
| Subscription terms/provider semantics can change | Cost/availability risk | B | verify sign-in and quotas at pilot time; do not assume API-equivalent quota |

---

## Recommended Pilots

### P1 — OpenClaw integrated, highest priority

Use **one real MoA research question** and implement only enough configuration to exercise the native loop:

`CEO question → Workboard → builtin-memory retrieval → audited research skill → independent review card → CEO review → Git artifact → approved memory promotion`.

Success criteria:
- no second project/task SSOT;
- restart preserves task/review/automation state;
- relevant prior MoA context is retrieved with inspectable provenance;
- reviewer does not inherit maker’s hidden session context;
- final artifact and accepted knowledge are reconstructible from the repo;
- fewer than three custom MoA rules are needed beyond governance/paths.

### P2 — Hermes + BMAD seam test

Do **not** reproduce the whole MoA architecture. Prove only the load-bearing seam:

`BMAD installer → generated SKILL.md → Hermes external/project skill discovery → run bmad-deep-recon → run bmad-review → persist through Kanban`.

Failure criterion: if execution requires rewriting/forking BMAD skill files or a translation layer, reject the composition and retain BMAD only as a donor/reference.

### P3 — Hermes-native simplicity control

Run the same research and weekly-CEO scenarios with no BMAD and no OpenClaw. Measure:
- manual prompting required;
- context loaded;
- number of durable objects created;
- recovery after interruption;
- review independence;
- operator comprehensibility;
- total integration/config surface.

### P4 — do not pilot Dify/n8n unless top-three fail

They are credible complete-system challengers but would introduce more service-specific state and weaker subscription-agent portability. Preserve them as fallback patterns for **automation/integration-heavy** processes after the agent OS core is chosen.

---

## Component Winners

| Layer | Best current component | Why |
|---|---|---|
| L1 knowledge_substrate | **OpenClaw builtin memory** | Native canonical-Markdown indexing, hybrid retrieval, local provider options and stored provenance. [S041] |
| L2 portfolio_ssot | **OpenClaw Workboard for small local agent ops; GitHub Projects for human-visible broader portfolio control** | Workboard best integrates agent run lifecycle; GitHub remains stronger enterprise/human PM boundary. [S040][S111] |
| L3 orchestrator_router | **Hermes Kanban / OpenClaw Workboard** | Both now have durable dependency/review dispatch; Hermes has especially explicit worker lifecycle. [S010][S040] |
| L4 workflow_library | **Spec Kit for generic durable workflow definitions; BMAD for methodology workflows** | Spec Kit current engine is far broader than prior research credited; BMAD has strong decision/review/research methods. [S090][S030] |
| L5 specialist_agent_library | **BMAD/CIS first-party roles; ClawHub for breadth** | BMAD higher trust, ClawHub broader but community-heavy. [S031][S046] |
| L6 tool_script_layer | **OpenClaw/n8n** | OpenClaw agent-native tools; n8n strongest SaaS/business connector surface. [S040][S070] |
| L7 executor_adapters | **Hermes / OpenClaw** | Best verified subscription/local/runtime breadth. [S014][S042] |
| L8 review_governance | **Hermes Kanban + BMAD review** | Explicit durable request-review/change plus adversarial artifact review. [S010][S030] |
| L9 artifact_output_system | **Git/GitHub repo** | Durable, inspectable history and cross-client handoff. [S001][S111] |
| L10 learning_loop | **No complete winner** | OpenClaw strongest factual retrieval/provenance; Hermes strongest explicit procedural skill-memory/write approval. Governed promotion remains project policy. [S011][S012][S041] |

---

## What Previous Research Got Wrong or Missed

1. **Decision-unit mismatch:** earlier MCDA ranked portfolio/orchestration cores as if that approximated the complete AI company. The authoritative target now requires L1–L10 plus actual specialist reuse, so old totals such as Spec Kit/GitHub 91.2 are not comparable to this run. [S001][S005]
2. **OpenClaw is materially more complete now:** current Workboard is a bundled durable board with dependencies, claims, lifecycle, attempts, artifacts/proof and permissions; current builtin memory has replaced QMD with provenance-aware hybrid retrieval over canonical Markdown. Earlier analysis that treated OpenClaw as “runtime/parallel agents but no canonical project/semantic KB” is stale. [S040][S041]
3. **Hermes evolved materially:** current Kanban is a durable multi-profile queue/state machine with review/change, human unblock, dependencies, scheduled work and structured evidence; it should no longer be assessed as session/todo/cron only. [S010]
4. **Spec Kit also evolved:** current official docs explicitly target the SDLC **or any business process**, and its workflow engine supports persisted state, gates, loops and fan-out/fan-in with a growing extension/preset catalog. It is a much stronger L3/L4 component than a coding-only label suggests, but still lacks an integrated semantic KB and relevant specialist organization. [S090][S091]
5. **BMAD is a stronger L4/L5 donor than previously scored:** current core includes decision-grade `bmad-deep-recon` and document-capable `bmad-review`; CIS adds a real creative specialist pack; installer-generated `SKILL.md` files make the assets portable at the file level. [S030][S031][S033]
6. **Do not over-credit BMAD marketplace breadth:** official docs still say its community module marketplace is coming. Existing first-party modules count; hypothetical future community breadth does not. [S031]
7. **n8n/Dify prove non-software HITL workflows but not the whole target:** their current template ecosystems demonstrate business/research/content operations, yet neither naturally solves the repo-visible CEO portfolio + cross-subscription-agent portability requirement as compactly as the top three. [S080][S081][S070]
8. **No ecosystem eliminates MoA-specific method work:** workshop/pedagogy/coaching/sensitivity/Leela specialists are still absent in verified catalogs. The correct response is a bounded pilot and reuse scan, not pretending generic “custom agent” capability is a prebuilt organization.

---

## Completion Check

- YES — searched beyond seeded candidates.
- YES — inspected actual agent/skill/workflow catalogs, including BMAD modules/skills, ClawHub packages, Dify first-party marketplace and current workflow catalogs.
- YES — distinguished native (`N`), official integration (`I`), package/plugin (`P`), adaptation (`A`) and unsupported/missing (`U/MISSING`).
- YES — verified non-software fit rather than inferring it solely from arbitrary prompts.
- YES — mapped every top architecture across L1–L10.
- YES — identified actual existing specialists and explicit missing families.
- YES — evaluated KB/retrieval separately from project/task state.
- YES — verified subscription/local executor paths and documented limitations.
- YES — avoided invented integration syntax and fabricated case studies.
- YES — prepared exactly `report.md`, `results.yaml`, and `sources.md` for `Orchestration/research-runs/chatgpt-deep-research/`.
