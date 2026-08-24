# Cross-AI Research Prompt — Integrated Master of Arts Agent Operating System

Use this prompt unchanged across independent research AIs. Replace only `<RESEARCHER_ID>` with a unique slug such as `chatgpt-deep-research`, `claude-research`, `gemini-deep-research`, `perplexity-research`, or `codex-research`.

Do **not** read other researchers' result folders before completing your own analysis.

---

<system_instruction>
You are an independent technical strategist, systems researcher, and analytical evaluator. Your task is to identify the best EXISTING, maintained, battle-proven ecosystem—or smallest proven composition of ecosystems—for a complete AI operating organization, not merely an orchestration tool or project manager.

Research current evidence on the public web and in official repositories. Prefer primary sources: official documentation, official repositories, release notes, maintained marketplaces/catalogs, and verified examples. Use secondary sources only to corroborate adoption or real-world use.

Do not invent missing agents, workflows, integrations, commands, configuration syntax, case studies, or capabilities. Clearly distinguish native capability from official integration, third-party package, generic extensibility, and our proposed adaptation.

Do not expose chain-of-thought. Save concise evidence, score rationale, assumptions, uncertainty, and decision logic instead.
</system_instruction>

<decision_question>
Which existing, proven ecosystem—or smallest upstream-supported composition—can best realize a durable "AI company in a repo" for Master of Arts, where:

CEO intent / portfolio priorities
→ orchestrator selects a proven workflow
→ relevant knowledge/context is retrieved
→ specialist agents/skills are activated
→ available subscription/local AI executors embody those roles
→ tools/scripts perform work
→ independent reviewers challenge outputs
→ the human CEO approves consequential decisions
→ final artifacts/business actions are persisted
→ validated learning is promoted back into the knowledge base
→ later workflows can reuse it.

The system must produce real non-software outputs such as research, workshops, coaching/method artifacts, website/content/social-media material, operational/admin work, offers/products, and later Leela software-use-case precursors.
</decision_question>

<repository_context>
Repository: `leela-spec/MasterOfArts`
Branch: `main`
Researcher ID: `<RESEARCHER_ID>`

READ FIRST, in this order:
1. `Orchestration/07-INTEGRATED-AGENT-OPERATING-MODEL.md` — authoritative target operating model.
2. `Orchestration/03-SCOPE-LOCK.md` — authoritative Master of Arts scope and workflow classes.
3. `Orchestration/06-USER-STORIES-AND-EXECUTOR-MATRIX.md` — explanatory prior research; useful but NON-AUTHORITATIVE.
4. `Orchestration/04-EVIDENCE-MATRIX.md` and `Orchestration/05-MCDA-SCORES.md` — prior partial analysis; challenge it rather than ratifying it.

Do NOT inspect result folders from other researchers until your own report is complete. Independence is required so outputs can later be compared.

Do NOT install a candidate, change production infrastructure, or edit files outside your own research-output directory.
</repository_context>

<target_stack_contract>
Every complete candidate architecture must explicitly account for all 10 responsibilities below. A candidate may be one ecosystem or a minimal composition, but every named component must already exist and integrate through documented mechanisms.

L1 knowledge_substrate:
  canonical sources, concepts, decisions, prior outputs, retrieval, provenance, validated learning
L2 portfolio_ssot:
  goals, projects, priorities, dependencies, status, CEO decisions
L3 orchestrator_router:
  workflow selection, agent activation, parallelism, handoffs, gates, retries, resume
L4 workflow_library:
  reusable proven processes for recurring output classes
L5 specialist_agent_library:
  durable specialist roles/skills, not one-off prompts hidden in chat
L6 tool_script_layer:
  web research, repo/files, documents, deterministic scripts/checks, scheduling
L7 executor_adapters:
  subscription/local AI clients that perform the specialist roles
L8 review_governance:
  maker/reviewer separation, evidence checks, escalation, CEO gates
L9 artifact_output_system:
  durable research/workshop/content/SOP/business outputs with history/provenance
L10 learning_loop:
  promotion of accepted findings/results into reusable organizational knowledge
</target_stack_contract>

<required_specialist_families>
Do not merely ask whether a platform "supports agents." Inspect its shipped agents, skills, roles, plugins, packs, marketplace, templates, or reusable workflows and map actual existing assets to these families:

control_orchestration:
  - portfolio/project manager
  - planner/decomposer
  - workflow router/orchestrator
  - handoff coordinator
  - independent reviewer
  - completion verifier
  - knowledge curator

research_knowledge:
  - research strategist
  - web/deep researcher
  - source/evidence verifier
  - comparative analyst
  - synthesis writer
  - contradiction/uncertainty reviewer
  - taxonomy/knowledge curator

creative_content:
  - creative strategist
  - creative writer/editor
  - brand/voice reviewer
  - website copywriter
  - long-form creator
  - social-media strategist
  - short-form/post writer
  - video/script writer
  - content repurposing workflow

workshop_coaching_method:
  - workshop designer
  - pedagogy/learning reviewer
  - coaching-method analyst
  - session/process designer
  - operations/logistics reviewer
  - sensitivity/public-private reviewer
  - offer/pricing/market-test agent

business_operations:
  - SOP/admin agent
  - customer-communication agent
  - portfolio-reporting agent
  - offer/product agent
  - recurring-review agent
  - deterministic compliance/check workflow where appropriate

leela_bridge:
  - use-case translator
  - workflow/process formalizer
  - product/specification agent
  - human-vs-software boundary reviewer

Absence of a prebuilt specialist is not automatically fatal if the ecosystem has a mature, documented marketplace/skill standard with proven reusable packages. However, score down solutions that would require writing most of these roles from scratch.
</required_specialist_families>

<discovery_seed_not_shortlist>
Investigate these because prior work found them relevant, but DO NOT assume any belong in the final ranking:
- BMAD Method and its web bundles/modules
- Superpowers
- Ruflo / Claude Flow ecosystem
- Gas City + official packs
- Hermes Agent
- OpenClaw
- GitHub Spec Kit and its workflow/extension ecosystem
- Beads
- OpenSpec
- Task Master
- GitHub Issues/Projects + Agent Skills ecosystem

Search beyond this list. The purpose is to find the best current system, not to confirm earlier candidates.

Specifically search for:
- integrated multi-agent operating systems
- agent/skill marketplaces and packs
- reusable research-agent workflows
- creative-writing/content/social-media agents
- knowledge-base/RAG + agent orchestration systems
- business/non-software multi-agent workflows
- subscription-AI/CLI-compatible agent skills
- open Agent Skills-compatible ecosystems
- proven human-in-the-loop agent orchestration

A better candidate discovered during research should replace a seeded candidate.
</discovery_seed_not_shortlist>

<non_negotiable_hard_filters>
A complete-system winner must pass all of these. If a tool fails as a complete system but is valuable as a component, retain it only as a component candidate.

H1 existing_now:
  Maintained, usable implementation exists now. No research papers, vaporware, architecture proposals, or "we could build this."

H2 proven_and_current:
  Strong evidence of real adoption/use plus maintained docs/releases/issues. Popularity alone is insufficient. Prefer active maintenance within the last 6–12 months; explicitly justify exceptions for stable mature systems.

H3 reuse_before_invention:
  Major responsibilities must come from existing systems, official plugins/packs/marketplaces, or proven portable skill packages. Project-specific configuration is allowed through documented extension mechanisms. Do not solve missing layers by proposing a new custom framework.

H4 integrated_specialists:
  Provides shipped specialist agents/roles/workflows OR a mature documented package/skill ecosystem from which relevant proven specialists can be installed/reused.

H5 knowledge_and_context:
  Has a credible existing method for persistent source/artifact storage plus relevant context retrieval/provenance. If a separate KB component is required, it must already exist and have a documented integration path.

H6 durable_state_and_recovery:
  Plans/tasks/workflow state/outputs survive chat/session/model changes and interrupted work can resume without reconstructing state from conversation history.

H7 multi_executor_portability:
  Durable agent definitions/workflows/state must not exist only in one provider's hidden chat memory. Prefer compatibility with at least two executor families and especially repo-capable subscription/local tools such as ChatGPT, Codex, Claude, Antigravity, Hermes/OpenClaw, or equivalent. Document exact compatibility rather than assuming it.

H8 subscription_or_local_path:
  Core orchestration must not force pay-per-token API model calls for every semantic task. There must be a credible subscription-authenticated and/or local-model execution path for important work.

H9 human_governance:
  Supports explicit review/approval/escalation boundaries so the human remains CEO while routine approved work can continue autonomously.

H10 non_software_fit:
  Must be domain-neutral or have credible verified non-code/business/knowledge/creative use. A coding-only system may remain a component but cannot win the complete-system ranking merely because arbitrary prompts could theoretically repurpose it.

H11 bounded_operational_complexity:
  Must be maintainable by a small operator-led organization. Penalize stacks requiring many servers/databases/daemons/adapters unless their value is proven and substantially exceeds simpler alternatives.

H12 auditability_and_security:
  Outputs, sources, agent actions, permissions, and consequential decisions must be inspectable enough for sensitive/private Master of Arts work.
</non_negotiable_hard_filters>

<evidence_policy>
Use current web research. Do not rely on model memory for claims that can change.

Source priority:
P1 official docs / official repository / official release notes
P2 official marketplace/catalog/package documentation
P3 first-party case study or maintained example repository
P4 credible independent implementation/case study
P5 community discussion only for failure modes/user experience; never as sole proof of a core capability

For every load-bearing capability record:
- source URL
- source date/version when available
- evidence type P1–P5
- evidence strength A/B/C/D

Evidence strength:
A = direct official evidence of the exact capability or verified case
B = official documented generic capability with credible direct mapping
C = credible inference/third-party evidence; requires pilot before relying on it
D = speculation/marketing ambiguity; cannot support a winner

Capability notation:
N = native shipped capability
I = official integration
P = official/established plugin, pack, skill, or marketplace asset
A = adaptation using documented generic mechanism; not a verified use case
U = unsupported/unknown

Rules:
- Never convert `A` into `N` merely because adaptation seems easy.
- Stars/downloads are adoption signals, not capability evidence.
- If documentation conflicts with current repository/release behavior, flag the contradiction.
- Search actual subdirectories/catalogs/plugins/packs/skills, not only top-level README pages.
- Prefer recent sources and explicitly note stale evidence.
</evidence_policy>

<evaluation_rubric>
Score only complete-system survivors from 0–5. Components are mapped separately and do not receive a complete-system rank.

Weighted dimensions (total 100):

C1 end_to_end_integrated_coverage — 15%
  0 = isolated tool; 5 = covers L1–L10 natively or through documented first-class integrations with clear ownership and no parallel truth.

C2 specialist_agent_and_workflow_ecosystem — 15%
  0 = agents must be authored from scratch; 5 = rich maintained catalog of relevant reusable specialist agents/skills/workflows plus composition/review patterns.

C3 knowledge_context_retrieval_and_learning — 12%
  0 = chat memory/manual files only; 5 = durable source-grounded KB, selective retrieval, provenance, reusable learning promotion, low context waste.

C4 orchestration_task_handoff_resume — 12%
  0 = manual prompting; 5 = durable routing/dependencies/parallelism/handoffs/gates/retries/resume with machine-readable state.

C5 executor_portability_and_subscription_local_fit — 12%
  0 = single proprietary/API-only runtime; 5 = durable roles/workflows usable across multiple subscription/local executor families with minimal duplication.

C6 master_of_arts_nonsoftware_fit — 10%
  0 = intrinsically coding-only; 5 = proven or naturally domain-neutral across research, creative content, workshops/services, operations, and portfolio work.

C7 human_governance_review_quality — 8%
  0 = self-certifying autonomous agents; 5 = explicit maker/reviewer separation, evidence/acceptance gates, escalation and CEO control.

C8 maturity_adoption_maintenance — 7%
  0 = experimental/unmaintained; 5 = battle-proven, active, documented, healthy ecosystem and release history.

C9 reuse_and_integration_risk — 5%
  0 = major custom glue/framework work; 5 = upstream-supported composition, portable standards, few adapters, one clear source of truth per responsibility.

C10 operational_efficiency_security — 4%
  0 = high maintenance/context/token burden or opaque permissions; 5 = compact state/progressive context, deterministic mechanics, simple backup/update, auditable permissions/actions.

Weighted total = SUM(score/5 * weight).

For every score provide a short evidence-grounded rationale and confidence A–D. Do not provide hidden reasoning.
</evaluation_rubric>

<execution_workflow>
Follow the phases in order. Keep early phases compressed so tokens are spent on viable architectures, not dead candidates.

PHASE 0 — GROUNDING
- Read the authoritative repo files.
- Restate the decision target in <=150 words.
- Record any source/scope ambiguity that materially affects research; otherwise continue autonomously.

PHASE 1 — BROAD LANDSCAPE SCAN
- Discover 12–20 relevant ecosystems/tools/stacks.
- Use a compact table only:
  `candidate | primary layer(s) | integrated agents? | KB? | workflow/orchestration? | subscription/local path? | non-code evidence? | disposition`
- Do not deeply score yet.
- Identify missing categories and search again before closing discovery.

PHASE 2 — HARD-GATE SCREEN
- Apply H1–H12.
- Classify each as:
  `complete_system_survivor | component_only | disqualified | insufficient_evidence`
- State exact failed gate(s).
- Promote only 4–7 complete architectures to deep evaluation.
- A "complete architecture" may be a minimal composition only if every component already exists and the integration is documented/upstream-supported.

PHASE 3 — DEEP EVIDENCE PASS
For each survivor:
1. Map L1–L10 to exact components.
2. Inventory actual existing specialist agents/skills/workflows from official catalogs/repositories.
3. Verify executor compatibility and authentication/cost model.
4. Verify state storage, recovery, approvals/review, scheduling and deterministic tooling.
5. Find at least one credible non-software/business/creative/research use case where possible.
6. Identify what still must be custom.
7. Record operational requirements: install, services, databases, OS constraints, update/backup, permissions.
8. Record known failure modes and unresolved claims.

PHASE 4 — MCDA
Create the weighted matrix:

| Rank | Complete architecture | C1 15 | C2 15 | C3 12 | C4 12 | C5 12 | C6 10 | C7 8 | C8 7 | C9 5 | C10 4 | Total /100 | Confidence | Primary failure mode |

Then perform three sensitivity checks without inventing new scores:
- autonomy-first: increase C2+C4+C7
- knowledge-first: increase C3+C6
- simplicity/portability-first: increase C5+C9+C10

Report whether the top tier changes materially.

PHASE 5 — CONCRETE MASTER OF ARTS USER STORIES
For the top 3 architectures, run the SAME four paper prototypes. These are architecture walkthroughs, not implementation and not fabricated case studies.

US-A research_to_knowledge:
CEO asks a research question → existing MoA knowledge retrieval → multi-source research → evidence verification → synthesis → independent review → CEO gate → final research artifact → validated KB promotion.

US-B workshop_creation:
CEO states desired workshop outcome → relevant research/method knowledge → workshop designer → pedagogy/practice reviewer → operations/risk reviewer → CEO gate → final workshop + task/launch artifacts → learning captured after delivery.

US-C content_social:
approved research/workshop concept → creative strategist → long-form writer → brand/editor review → social/video specialists → public/private check → publication-ready outputs → portfolio state updated.

US-D weekly_ceo_operating_cycle:
collect portfolio state → detect blockers/stale work/dependencies → specialist project-controller analysis → autonomous routine follow-ups → surface only consequential decisions/exceptions to CEO → persist decisions → schedule next work.

For every step show:
`step | system/component | specialist agent/workflow | AI executor options | KB/context supplied | tools | durable state/output | reviewer/gate | verified status N/I/P/A/U`

If an agent/skill does not actually exist, write `MISSING` rather than inventing it.

PHASE 6 — REALIZATION BLUEPRINTS FOR TOP 3
For each top architecture provide:

```yaml
architecture_name: ...
portfolio_ssot: ...
knowledge_system: ...
orchestrator: ...
workflow_library: ...
specialist_agent_library: ...
skill_tool_library: ...
executor_clients: [...]
review_governance: ...
artifact_store: ...
learning_promotion: ...
mandatory_services: [...]
existing_integrations_used: [...]
custom_work_required:
  - item: ...
    why_unavoidable: ...
    size: none|small|medium|large
single_sources_of_truth:
  project_state: ...
  knowledge: ...
  workflow_state: ...
  final_artifacts: ...
```

Then give only VERIFIED install/bootstrap commands or configuration examples from official documentation. Cite each command/example source. If syntax cannot be verified, say `NOT VERIFIED — DO NOT EXECUTE` instead of guessing.

PHASE 7 — VERDICT AND DECISION TRIGGERS
For each top architecture:
- `select_if:` exact conditions under which it is best
- `avoid_if:` exact conditions that make it unsuitable
- `pilot_to_prove:` 2–4 unresolved load-bearing claims

Conclude with:
1. `recommended_for_pilot`
2. `runner_up`
3. `simplest_control`
4. `component_winners` by L1–L10 where useful
5. `what_previous_research_got_wrong_or_missed`

Do not declare production selection before pilots.
</execution_workflow>

<output_contract>
Save your work directly into the repository on branch `main` under your unique directory:

`Orchestration/research-runs/<RESEARCHER_ID>/`

Create exactly these files:

1. `report.md`
   - Human-facing synthesis.
   - Required sections: Executive Verdict; Landscape; Hard-Gate Results; Deep Evidence; MCDA; User Stories; Top-3 Realization Blueprints; Decision Triggers; Uncertainties; Recommended Pilots.
   - Prefer matrices and dense bullets over narrative prose.

2. `results.yaml`
   - Machine-readable canonical result.
   - Must contain:

```yaml
schema_version: 1
researcher_id: <RESEARCHER_ID>
research_date: YYYY-MM-DD
scope_commit_or_ref: ...
complete_system_ranking:
  - rank: 1
    architecture: ...
    score: 0.0
    confidence: A|B|C|D
    hard_gates: pass|conditional
    primary_failure_mode: ...
    architecture_map:
      L1_knowledge: ...
      L2_portfolio: ...
      L3_orchestrator: ...
      L4_workflows: ...
      L5_specialists: ...
      L6_tools: ...
      L7_executors: ...
      L8_review: ...
      L9_artifacts: ...
      L10_learning: ...
component_winners: {}
disqualified: []
insufficient_evidence: []
sensitivity: {}
recommended_pilots: []
critical_unknowns: []
```

3. `sources.md`
   - Source registry only.
   - One row per source:
     `ID | candidate | claim/capability | source type P1–P5 | date/version | URL | notes`
   - Include every source used for load-bearing claims.

Repository write rules:
- Work on `main` only.
- Write only inside `Orchestration/research-runs/<RESEARCHER_ID>/`.
- Do not edit prior MCDA files or other researchers' results.
- Do not install or implement candidates.
- Use commit message: `research(orchestration): <RESEARCHER_ID> integrated agent landscape`.
- If repository write access is unavailable, output the three complete file bodies in your final response with exact target paths; do not silently omit persistence.
</output_contract>

<anti_drift_rules>
- The goal is NOT to design a clever custom architecture.
- The goal is NOT to rank isolated coding-agent frameworks.
- The goal is NOT to maximize agent count or autonomy for its own sake.
- The goal is NOT to reward a candidate because previous Master of Arts research mentioned it.
- The goal IS to reuse already-proven agent/workflow/KB ecosystems that can create real Master of Arts outputs with minimal custom glue.
- Prefer a simpler proven stack over a feature-rich stack if both accomplish the operating loop.
- Do not confuse "can prompt an LLM to do X" with "ships a reusable specialist/workflow for X."
- Do not confuse durable project files with semantic knowledge retrieval.
- Do not confuse a model/runtime with a durable specialist-agent definition.
- Do not confuse stars with evidence of fit.
- Do not claim cross-agent portability without verifying what state/skills/workflows each client can actually access.
- Do not treat prior scores or recommendations as authoritative.
</anti_drift_rules>

<completion_check>
Before committing, answer YES/NO:
- Did I search beyond the seeded candidates?
- Did I inspect actual agent/skill/workflow catalogs rather than only READMEs?
- Did I distinguish native vs integration vs plugin vs adaptation?
- Did I verify non-software fit rather than assume it?
- Did I map every top architecture across L1–L10?
- Did I identify exactly which specialist agents already exist and which are missing?
- Did I verify KB/retrieval behavior separately from project state?
- Did I verify subscription/local executor paths?
- Did I avoid inventing integration syntax or case studies?
- Did I save `report.md`, `results.yaml`, and `sources.md` to the required unique repo path?

If any answer is NO, fix it before completion.
</completion_check>
