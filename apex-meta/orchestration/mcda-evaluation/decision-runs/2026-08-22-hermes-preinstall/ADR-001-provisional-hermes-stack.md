# ADR-001 — Provisional Hermes-first Master of Arts stack

Status: **PROPOSED / PRE-INSTALL VALIDATION ONLY**  
Date: 2026-08-22  
Decision owner: Human CEO  
Implementation authorized: **NO**  
Supersedes: no prior accepted production architecture; this record supersedes only the informal conceptual diagrams that combined OKF/QMD/MCP as if already selected.

## 1. Decision statement

Master of Arts will **not build a custom orchestration, memory, knowledge-retrieval, workflow, or agent framework** before selecting and validating an existing upstream ecosystem.

The current system to validate first is:

> **Hermes Agent as the primary orchestration/runtime + Hermes Kanban for durable work state + existing MasterOfArts project folders as workspaces + upstream Agent Skills/BMAD installed through their documented Hermes integration + Hermes native project context and memory/learning mechanisms + optional official QMD integration only if native file access proves insufficient.**

The direct challenger is **OpenClaw as an alternative complete orchestration/runtime**, not as an additional layer inside Hermes.

This is a **provisional pilot decision**, not a production selection.

## 2. Why this record exists

The project has repeatedly lost time when AI-designed infrastructure was treated as if it were already proven. This decision run therefore applies a strict reuse rule:

1. upstream native capability;
2. official integration/plugin/skill;
3. established portable skill package through a documented standard;
4. small configuration using the selected system's documented mechanisms;
5. custom adapter only if unavoidable and bounded;
6. reject any design that requires a new custom subsystem.

Target: **90–95% existing/upstream; maximum 5–10% project-specific configuration/connection.**

## 3. Current candidate flow

```text
HUMAN CEO
   |
   v
HERMES AGENT
   |
   +----------------------+----------------------+----------------------+
   |                      |                      |                      |
   v                      v                      v                      v
HERMES KANBAN        SHARED SPECIALISTS     MODEL PROVIDER        PROJECT CONTEXT
work/state/review    + AGENT SKILLS         execution             existing repo folders
   |                      |                      |                      |
   |                      +-- BMAD               +-- ChatGPT/Codex      +-- root/project AGENTS.md
   |                      +-- other approved      +-- Copilot/etc.       +-- nested context
   |                          upstream skills     +-- local model        +-- existing files/assets
   |                                                                    |
   +------------------------------ task workspace ----------------------+
                                                                        |
                                              if native file retrieval is inadequate
                                                                        v
                                                              OPTIONAL QMD SEARCH
                                                              official Hermes skill
                                                              local index over files
                                                              Hermes <-> local MCP <-> QMD
```

OpenClaw is tested as an alternative stack:

```text
HERMES STACK  <---- compare on same user stories ---->  OPENCLAW STACK
```

Do not combine both unless an upstream-supported integration later proves a unique need.

## 4. Responsibility ownership — provisional

| Responsibility | Provisional owner | Evidence state | Custom work allowed? |
|---|---|---|---|
| Orchestration/runtime | Hermes Agent | VERIFIED upstream | Configuration only |
| Durable task/review state | Hermes Kanban | VERIFIED upstream | Configuration only |
| AI execution | Hermes provider adapters | VERIFIED upstream | Login/provider config only |
| Existing project files/artifacts | MasterOfArts Git repository | EXISTING | No migration until needed |
| Project context/orientation | Hermes `AGENTS.md` / context-file discovery | VERIFIED upstream | Project content must be authored/organized, mechanism is native |
| Shared specialist procedures | Agent Skills | VERIFIED upstream standard support in Hermes | Install/pin/configure only |
| BMAD roles/workflows | BMAD installer -> Hermes `.agents/skills/` target | VERIFIED upstream-to-upstream path | No middleware |
| Runtime personal/profile memory | Hermes `MEMORY.md` / `USER.md` | VERIFIED upstream | Native settings only |
| Learned skill maintenance | Hermes Curator | VERIFIED upstream | Native settings only |
| Large-corpus semantic retrieval | Native file tools first; QMD only if required | QMD integration VERIFIED, requirement UNPROVEN | Official skill/config only |
| Hermes <-> QMD connection | Hermes MCP client + QMD MCP server | VERIFIED official integration | Config only, no custom MCP service |
| Binary document conversion | None selected | UNPROVEN NEED | Do not add until a real gap exists |
| Web/subscription AI access | GitHub/repo access to files; native skill execution varies by client | PARTLY VERIFIED / MUST TEST | No custom bridge before test |
| Macro/meso/micro project model | Hermes boards/workdirs + project folders/context | MECHANICS VERIFIED; MoA fit UNPROVEN | Must pass user stories before adoption |

## 5. What is already verified from upstream sources

### Hermes project context

Hermes officially supports hierarchical project context. `AGENTS.md` files are loaded from the Git root down to the current working directory, and additional subdirectory context is discovered progressively when the agent navigates there. This is specifically designed to reduce prompt bloat while allowing local project instructions.

Official source: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/

### Hermes Kanban

Hermes Kanban is durable task state stored in SQLite. It supports multiple boards, named profiles, dependencies, comments, attachments, review/request-changes, blocking/unblocking, retries/attempt history, scheduled starts, and a board-level `default_workdir` that can point to an existing Git repository or ordinary directory.

Official source: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban

### Hermes skills

Hermes supports Agent Skills, project-local `.agents/skills/`, external skill directories, on-demand skill loading, and project trust controls. Project-local skills are highest precedence and are not automatically modified by the Curator. External directories can be modified if writable, so write protection/configuration must be verified before using them as approved organization-wide libraries.

Official source: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/

### BMAD -> Hermes

BMAD's current installer configuration explicitly contains a `hermes` platform target:

```yaml
hermes:
  name: "Hermes Agent"
  installer:
    target_dir: .agents/skills
    global_target_dir: ~/.hermes/skills
```

This means BMAD-to-Hermes installation is an upstream-supported file/skill path, not a custom API bridge.

Official source: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml

### QMD -> Hermes

Hermes publishes an official optional QMD skill. The documented preferred connection is Hermes' native MCP client to a local QMD MCP server. In stdio mode Hermes launches QMD as a local subprocess; QMD exposes search/get/status tools. No hosted API is required for this connection.

Official source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd

Important: the official QMD skill currently declares macOS/Linux. Windows/WSL behavior must be verified on the target environment before QMD becomes part of the selected stack.

### Hermes model/provider paths

Hermes officially supports ChatGPT/Codex subscription OAuth, GitHub Copilot OAuth, Nous Portal subscription, API providers, and local/self-hosted endpoints. OpenRouter is optional, not required. Exact ChatGPT plan quota accounting through the Codex OAuth path is not fully documented by Hermes and remains a cost/usage question for validation.

Official source: https://hermes-agent.nousresearch.com/docs/integrations/providers

### Hermes memory and learning

Built-in memory is deliberately small and profile-scoped: `MEMORY.md` and `USER.md` are injected at session start. Hermes also provides session search, skills as procedural memory, and a Curator for agent-created skill lifecycle, audit, backup and rollback. Built-in memory should therefore not automatically be treated as the canonical Master of Arts knowledge base.

Official sources:
- https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/curator

## 6. Critical unproven hypotheses

These must be answered before installation approval.

### H1 — Shared specialist across isolated projects

A single reusable specialist, e.g. `Marketing Executive`, can work on Awakenings, another workshop family, and Business without duplicating the specialist definition and without contaminating project context.

Status: **UNPROVEN USER STORY**.

### H2 — Macro/meso/micro project management

Hermes native boards, tasks, dependencies, workdirs and context files are sufficient for:

- Macro: Master of Arts portfolio/organization;
- Meso: one program/project family;
- Micro: one concrete execution project.

Status: **UNPROVEN FIT**.

### H3 — Project knowledge organization

The existing project estate can be organized enough for Hermes to work reliably using native project folders + hierarchical context + normal file tools, without a new custom knowledge database.

Status: **UNPROVEN FIT**.

### H4 — QMD necessity

If project corpora become too large for normal file navigation, the official QMD integration materially improves retrieval and token efficiency without introducing unacceptable OS/maintenance complexity.

Status: **OPTIONAL / UNPROVEN NEED**.

### H5 — Learning boundary

Hermes can learn useful procedures without allowing runtime memory or Curator behavior to become a competing source of organizational truth. Accepted learning can be reviewed and promoted through existing repo/skill mechanisms without a custom synchronization system.

Status: **PARTLY VERIFIED, POLICY/WORKFLOW FIT UNPROVEN**.

### H6 — Web subscription AI portability

A web AI with GitHub repository access can reliably read the same project knowledge and skill files for bounded work. Native automatic skill activation should **not** be assumed; the test must distinguish `can read/follow a SKILL.md` from `client natively installs/activates Agent Skills`.

Status: **UNPROVEN PER CLIENT**.

### H7 — OpenClaw switching condition

OpenClaw only displaces Hermes if it solves H1–H6 materially better while remaining a single simpler system and avoiding parallel state or untrusted marketplace dependencies.

Status: **UNPROVEN COMPARISON**.

## 7. Input/output and execution-class model

Every pre-install simulation must classify each step:

- **D — deterministic:** database state transition, file lookup, exact script/check, dependency resolution, schema/path validation;
- **AI — semantic reasoning:** interpretation, research synthesis, creative drafting, prioritization under ambiguity;
- **H — hybrid:** deterministic retrieval/tool call followed by AI reasoning.

And record:

```text
INPUT: exact data/files/prompt/state
TRIGGER: human / board event / workflow / skill
COMPONENT: Hermes / Kanban / skill / model / QMD / GitHub
EXECUTION_CLASS: D | AI | H
MODEL_CALL: yes/no
TOKEN_COST_DRIVER: none | injected context | retrieved text | skill text | reasoning output
OUTPUT: exact artifact/state
PERSISTENCE: where it survives
REVIEW: who/what checks it
UPSTREAM_STATUS: native | official integration | portable package | configuration | custom
```

No step may remain described as "the system somehow knows" or "the agent just retrieves it."

## 8. Knowledge-base position before validation

There is **no approved new KB architecture yet**.

The current no-invention hypothesis is:

1. existing MasterOfArts project folders remain the source estate;
2. the project/family is made understandable using Hermes' native hierarchical project-context mechanism;
3. actual project files remain in the project;
4. normal file/search tools are used first;
5. QMD is added only if a measured retrieval problem exists;
6. Hermes personal memory is not canonical project truth;
7. reusable procedure learning belongs in reviewed skills, not duplicated factual KBs;
8. no mass reorganization of the repository occurs until user-story simulations prove the target structure.

The validation run must determine the **minimum project-local organization Hermes actually requires**. It may not invent a full ontology in advance.

## 9. Consequences if Hermes passes

- Install one primary orchestration system rather than combining several control planes.
- Use upstream BMAD/Agent Skills instead of recreating specialist prompts.
- Organize only the project knowledge necessary for the validated workflows.
- Add QMD only if the retrieval test demonstrates measurable value.
- Use Hermes memory/Curator as runtime learning, with explicit boundaries from canonical project files.
- Preserve the possibility that Codex/Claude/web AIs can read the same repository artifacts even when they cannot execute Hermes-only tools.

## 10. Consequences if Hermes fails

Do not repair Hermes with a custom Master of Arts subsystem. Compare the failed requirements directly against OpenClaw's native implementation. If OpenClaw also fails, reopen the shortlist using the evidence already in `Orchestration/research-runs/`.

## 11. Rejected / deferred architecture elements

- central custom OKF knowledge warehouse: **deferred/not selected**;
- custom RAG/vector server: **rejected unless native options fail**;
- generic MCP infrastructure: **rejected**; only use a concrete upstream integration such as Hermes <-> QMD;
- Docling ingestion pipeline: **deferred until binary-document need is proven**;
- Hermes + OpenClaw combined control plane: **rejected**;
- Hermes Kanban + GitHub Projects duplicate task truth: **rejected unless a proven unavoidable visibility gap is demonstrated**;
- cross-runtime memory synchronization: **rejected**;
- one custom agent per project: **rejected as default**.

## 12. Confidence and decision status

Current confidence in **Hermes as the first system to validate:** B+.

Current confidence in **production suitability:** C / unproven until the pre-install validation run passes.

The next artifact is `QA-VALIDATION-RUNBOOK.md`. No installation is authorized until that run ends with an explicit human `APPROVE_INSTALL` decision.
