# ADR-002 — Full-functional Hermes target stack

Status: **ARCHITECTURE ACCEPTED / PRE-INSTALL VALIDATION ONLY**  
Date: 2026-08-22  
Architecture accepted by Human CEO: 2026-08-23  
Decision owner: Human CEO  
Implementation authorized: **NO**  
Supersedes for active guidance: `ADR-001-provisional-hermes-stack.md`

## 1. Decision statement

Master of Arts will validate **one complete, working Hermes-centered operating stack** before installing or reorganizing production project data.

The active target is:

> **Hermes Agent + Hermes Kanban + existing MasterOfArts project folders + Hermes native hierarchical project context + BMAD + MarketingSkills + official Hermes/QMD integration + approved model/provider path + Hermes memory/Curator + a verified low-friction local safety configuration.**

OpenClaw is **not part of the active validation run**. It is deferred to `Orchestration/future-development/OPENCLAW-ALTERNATIVE-EVALUATION.md` and is revisited only by an explicit future operator decision.

The 2026-08-23 operator review also **declined the proposed Agency Agents pre-install pilot**. Agency Agents, AnythingLLM, and Semantic Router are deferred to the same future-development backlog. None is part of the current Hermes realization or installation gate.

This is an accepted target-stack architecture decision, not installation approval.

## 2. Full-function rule

The project must not optimize for a "small", "minimal", "thin", "MVP", or deliberately reduced version of a required capability.

The target is the **complete functionality required by the Master of Arts user stories**.

Rules:

1. Use upstream-native functionality first.
2. Use official integrations/plugins/skills next.
3. Use established portable Agent Skills through documented support next.
4. Project-specific configuration is allowed when it uses documented mechanisms and is necessary for the complete end-to-end system.
5. Custom code, a custom orchestration subsystem, a custom memory synchronization system, or a custom KB engine is **not authorized in this phase**.
6. If a required capability cannot be completed through existing upstream mechanisms, stop and record the blocker. Do not replace it with a reduced substitute merely because that substitute is easy to implement.
7. A script or configuration is acceptable only when it performs the required function completely and is part of a documented upstream integration path; implementation size is not a quality criterion.

The previous percentage language about "5–10%" custom connection work is retired as an implementation target. It encouraged the wrong optimization. The controlling question is now: **does the complete required workflow work through existing supported mechanisms without us inventing a subsystem?**

## 3. Active target architecture

```text
HUMAN CEO
   |
   v
HERMES AGENT
   |
   +----------------------+----------------------+----------------------+
   |                      |                      |                      |
   v                      v                      v                      v
HERMES KANBAN        SPECIALISTS + SKILLS   MODEL EXECUTION       PROJECT WORKDIR
work/state/review    shared across projects provider/local        existing MoA folder
   |                      |                      |                      |
   |                      +-- BMAD               +-- ChatGPT/Codex      +-- AGENTS.md chain
   |                      +-- MarketingSkills    +-- local model        +-- project knowledge
   |                      +-- approved skills    +-- other verified     +-- sources/assets
   |                                                                    |
   +-------------------------- durable task workspace ------------------+
                                                                        |
                                                                        v
                                                               QMD RETRIEVAL
                                                               required target add-on
                                                               official Hermes skill
                                                               local index over repo files
                                                               Hermes <-> MCP <-> QMD
```

Supporting safety controls are part of the target and must use Hermes' documented security mechanisms rather than a new policy engine.

## 4. Component status

| Component | Role | Active target? | Current evidence status | Installation status |
|---|---|---:|---|---|
| Hermes Agent | Primary orchestration/runtime | YES | verified upstream | not installed by this decision run |
| Hermes Kanban | Durable tasks, dependencies, review, retry, workspaces | YES | verified upstream | pending validation |
| Existing MasterOfArts folders | Project source/artifact estate | YES | existing | no migration authorized |
| Hermes hierarchical context | Repo/project orientation through context files | YES | verified upstream mechanism | project fit must be proven |
| BMAD | Reusable research/review/creative workflows and agents | YES | Hermes install target verified upstream | pending validation |
| MarketingSkills | Reusable marketing/content/offer skills | YES | Agent Skills package and `.agents/skills/` install verified upstream | pending validation |
| QMD | Local hybrid retrieval over project files | YES | official Hermes integration + QMD upstream verified | platform and repo mapping must be proven |
| MCP | Local Hermes <-> QMD transport only | YES as part of QMD integration | official integration path | no generic MCP infrastructure |
| Hermes memory | Runtime/profile factual memory | YES | verified upstream | must not replace project truth |
| Hermes Curator | Agent-created skill lifecycle/learning | YES | verified upstream | governance must be proven |
| Provider path | Semantic model execution | YES | OpenRouter is an upstream-supported Hermes provider; `stealth/ox-alpha` is currently live through OpenRouter | first non-sensitive integration trial uses OpenRouter + Ox Alpha; production provider remains unapproved |
| Local safety configuration | Protect host while preserving normal work | YES | R01 PASS: WSL2 + smart approvals + denies + write-safe roots + checkpoints; official Docker backend available for stronger isolation | live QA pending; Docker is conditional for untrusted, command-heavy, or isolation-sensitive work rather than the normal default |
| OpenClaw | Alternative orchestration system | NO, deferred | prior research exists | future-only |

## 5. Verified upstream linkages already established

### Hermes -> project context

Hermes officially loads a chain of `AGENTS.md` files from Git root to the working directory and progressively discovers deeper subdirectory context. This gives an upstream mechanism for organization-wide, project-family, and project-local instructions without loading every project into every prompt.

Official source: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/

### Hermes Kanban -> project folders

Hermes Kanban provides durable boards/tasks and workspaces. Board/task work can operate in existing directories rather than requiring project data to be moved into Hermes-specific storage.

Official source: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban

### BMAD -> Hermes

BMAD's current installer configuration explicitly defines `Hermes Agent` and installs project skills to `.agents/skills/`, which Hermes supports as a project skill location.

Official source: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml

### MarketingSkills -> Agent Skills -> Hermes

MarketingSkills is an upstream Agent Skills collection. Its official README documents installation to the universal `.agents/skills/` location. Hermes officially discovers project-local `.agents/skills/` after the project is trusted.

MarketingSkills also ships a `product-marketing` skill that creates `.agents/product-marketing.md` and expects other marketing skills to use that context. The exact interaction of this single context file with Master of Arts macro/meso/micro projects is therefore a required research question, not something to improvise.

Official sources:
- https://github.com/coreyhaines31/marketingskills
- https://github.com/coreyhaines31/marketingskills/blob/main/skills/product-marketing/SKILL.md
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/

### Hermes -> QMD

Hermes publishes an official QMD skill. QMD is a locally installed search engine over Markdown/text collections. Its upstream repository supports local BM25 search, vector search and reranking, and exposes CLI and MCP interfaces. The active target uses only the already-documented Hermes/QMD connection; no custom search service is authorized.

QMD is **available on demand rather than automatically injected into every Hermes task**. A Hermes worker invokes the QMD skill/MCP tools when repository evidence is needed, under an explicit authorized collection/path scope where applicable. QMD performs retrieval locally and returns ranked snippets or exact requested passages; only the selected retrieval result needs to enter the provider-model context. Tasks that already contain sufficient exact context do not require a QMD call. The derived index is refreshed through native `qmd update` and `qmd embed` after material accepted changes or before retrieval when freshness is uncertain.

Official sources:
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
- https://github.com/tobi/qmd

### Hermes safety controls

Hermes publishes first-party security guidance covering dangerous-command approvals, user deny rules, write-safety roots, container isolation, credential filtering, context-file scanning and messaging authorization. Hermes also publishes a dedicated guide for running on a personal/work machine. The active safety task is to select and verify the correct official combination, not to invent a separate guardrail framework.

Official sources:
- https://hermes-agent.nousresearch.com/docs/user-guide/security/
- https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine

## 6. Required project/knowledge behavior

The final system must support the following pattern without creating a separate agent copy for every project:

```text
MASTER OF ARTS ORGANIZATION CONTEXT
            |
            v
SHARED SPECIALIST + SHARED SKILLS
            |
            +-------------------------------+
            |                               |
            v                               v
PROJECT FAMILY A                    PROJECT FAMILY B
local knowledge/context             local knowledge/context
            |                               |
            v                               v
MICRO PROJECT A1                    MICRO PROJECT B1
current brief/assets/state          current brief/assets/state
```

Required properties:

- the same Marketing/Research/Workshop/Operations specialist can serve multiple project families;
- organization-wide context is not recopied into each agent definition;
- project-family and micro-project information remains isolated and current;
- project knowledge remains in durable project files rather than hidden runtime memory;
- QMD indexes/retrieves those files instead of becoming a second canonical KB;
- Hermes Kanban supplies durable execution state;
- skills supply reusable procedures;
- runtime memory and Curator learning are governed separately from factual project truth;
- web/subscription AI clients can still perform repo-backed tasks to the extent their connectors and skill support permit.

## 7. Research tracks that must be completed before installation

Each question has its own authoritative specification under `research/`:

1. `R01-HERMES-LOCAL-SAFETY-GUARDRAILS.md`
2. `R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE.md`
3. `R03-HERMES-QMD-REPO-INTEGRATION.md`
4. `R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE.md`
5. `R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING.md`
6. `R06-HERMES-CONTINUOUS-LEARNING.md`
7. `R07-MARKETINGSKILLS-HERMES-INTEGRATION.md`

The active interactive entrypoint is `QA-VALIDATION-RUNBOOK-v2.md`.

## 8. Required simulations

Before installation, the validating chat must demonstrate on paper, with verified upstream mechanisms, at least:

1. **Research -> knowledge -> workshop:** project knowledge retrieval, BMAD research/review, durable artifact, review and CEO gate.
2. **Workshop -> marketing:** one shared marketing specialist uses MarketingSkills on one workshop without manually restating the project.
3. **Same marketing specialist -> second project:** same role and skill library, different project context, no context contamination.
4. **Macro portfolio review:** Hermes can identify work across several project families and preserve durable next actions.
5. **Failure/recovery:** interrupted worker, rejected review and model/provider failure resume without chat archaeology.
6. **QMD retrieval:** project-local query returns scoped relevant passages; index refresh reflects changed files; QMD does not become canonical truth.
7. **Continuous learning:** a useful procedural lesson enters Hermes learning/skills without silently mutating project facts or approved shared skills.
8. **Safety:** normal file edits, Git operations, QMD searches and approved workflows succeed while destructive/credential-sensitive operations are stopped or isolated by official controls.
9. **Web AI:** identify exactly which repo-backed tasks a subscription web AI can execute without pretending it can call local Hermes/QMD software.

## 9. Installation gate

Installation approval requires all of the following:

- every required component edge is verified as native, official integration, or established portable package;
- the project/knowledge hierarchy works with the real repository and not only a toy folder;
- QMD has a supported execution path for the target Windows/WSL environment;
- the safety profile allows normal work and blocks/isolates the defined high-risk operations;
- BMAD and MarketingSkills have verified install/discovery paths in Hermes;
- shared specialists work across at least two project contexts without duplicated role definitions;
- continuous learning has a clear native lifecycle and does not create competing project truth;
- user-story simulations are complete end to end;
- no required capability depends on a custom subsystem or a deliberately reduced substitute;
- the CEO explicitly authorizes installation.

Possible final decisions for this active run:

- `APPROVE_INSTALL_HERMES_TARGET_STACK`
- `RESEARCH_BLOCKER`
- `REJECT_HERMES_TARGET_STACK`

OpenClaw is not an option in this active decision run.
