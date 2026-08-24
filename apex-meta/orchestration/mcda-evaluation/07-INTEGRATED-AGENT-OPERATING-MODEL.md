# 07 — Integrated Agent Operating Model

Status: **scope correction from operator feedback / authoritative for next research pass**  
Date: **2026-08-21**

## 1. Correction

The target is **not** merely an orchestration/project-management system that external AIs happen to use.

The target is an **integrated Master of Arts agent operating system** that combines, through existing battle-proven systems wherever possible:

1. knowledge and context;
2. portfolio/project state;
3. orchestration/routing;
4. reusable workflows;
5. specialist agent definitions/roles;
6. tools and deterministic scripts;
7. interchangeable AI executors/runtimes;
8. independent review and CEO gates;
9. durable outputs and provenance;
10. learning/promotion back into the knowledge base.

The system should feel to the operator like a company of specialists. The underlying AI runtime can change while the roles, workflows, knowledge, state and quality rules remain durable.

## 2. Critical distinction: specialist agent vs AI executor

### Specialist agent

A specialist agent is a durable role/capability package, for example:

- research strategist;
- web researcher;
- source verifier;
- synthesis writer;
- creative writer;
- workshop designer;
- pedagogy reviewer;
- social-media strategist;
- short-form content writer;
- website copywriter;
- offer/product designer;
- project manager/controller;
- independent reviewer;
- fact checker;
- knowledge curator;
- coaching-method analyst;
- operations/admin agent;
- Leela translation/specification agent.

A specialist agent should define as much as possible through proven reusable mechanisms:

- role and objective;
- when it is invoked;
- required inputs/context;
- allowed tools;
- method/process/skill;
- output contract;
- evidence/provenance requirements;
- review/acceptance criteria;
- handoff target;
- escalation/CEO boundary.

### AI executor/runtime

The executor is the model/client that performs the specialist role at runtime, for example:

- ChatGPT with repository/app/skill access;
- Codex CLI;
- Claude Code;
- Antigravity;
- Hermes;
- OpenClaw-managed agents;
- other compatible subscription/local agent clients.

The architecture should **not** require the business logic of `creative_writer`, `research_reviewer`, `workshop_designer`, etc. to live only inside one provider's hidden chat/session state.

The same specialist role should ideally be executable by more than one compatible AI client.

## 3. Target operating loop

```text
CEO intent / portfolio state
        ↓
Orchestrator chooses proven workflow
        ↓
Retrieve only relevant KB + project context
        ↓
Workflow activates specialist agent(s)
        ↓
Available AI executor embodies each specialist role
        ↓
Tools / scripts / web / repo operations
        ↓
Draft artifact(s)
        ↓
Independent specialist reviewer(s)
        ↓
Deterministic validation where possible
        ↓
CEO gate for consequential choices
        ↓
Final artifact / business action
        ↓
Project state updated
        ↓
Validated learning promoted into KB
        ↓
Future workflows can reuse it
```

This entire loop is the decision target.

## 4. Infrastructure layers

| Layer | Responsibility | Example question |
|---|---|---|
| **L1 Knowledge substrate** | Canonical sources, concepts, prior decisions, outputs, retrieval, provenance | What does MoA already know about surrender, self-defense pedagogy or an existing offer? |
| **L2 Portfolio SSOT** | Goals, projects, priorities, dependencies, status, CEO decisions | What should the organization work on now? |
| **L3 Orchestrator/router** | Chooses workflow, agents, sequence, parallelism, gates and recovery | Which team/process should handle this request? |
| **L4 Workflow library** | Proven repeatable processes for recurring output classes | How do we reliably create a research paper or workshop? |
| **L5 Specialist agent library** | Reusable expert roles with tools, context contracts and output standards | Which experts are needed and what exactly does each one do? |
| **L6 Tool/script layer** | Web research, files, GitHub, documents, deterministic validators, schedules | What can be automated mechanically instead of reasoned repeatedly? |
| **L7 Executor/runtime adapters** | ChatGPT/Claude/Codex/Antigravity/Hermes/OpenClaw execute roles | Which available subscription/local AI can perform this specialist job? |
| **L8 Review/governance** | Maker/reviewer separation, evidence checks, CEO gates, safety/visibility rules | Who challenges the output and what needs human approval? |
| **L9 Artifact/output system** | Research, workshop docs, content, SOPs, decisions, business actions | Where is the finished product and its history? |
| **L10 Learning loop** | Extract/promote validated findings so later work improves | What from this project should become reusable organizational knowledge? |

## 5. What “integrated” means

An architecture is not sufficiently integrated if the operator must manually:

- remember which agent to ask next;
- paste the same context between agents;
- explain the workflow every time;
- reconstruct project state from chats;
- decide which sources each agent needs;
- merge five agent outputs by hand;
- tell reviewers what they are supposed to review;
- copy validated learnings into the KB without a defined promotion step;
- maintain parallel incompatible truths for ChatGPT, Claude, Codex and local agents.

A good integrated system should make those responsibilities explicit and reusable.

## 6. Example: research → workshop → content → organizational learning

CEO request:

> Research surrender under pressure and determine whether it should become a 90-minute workshop and public content family.

### Orchestration

1. **Project/controller agent** frames objective, constraints and success criteria.
2. **KB/context agent** retrieves relevant existing MoA concepts, decisions and sources.
3. **Research strategist** defines sub-questions and source standards.
4. **Research workflow** fans out to specialist research agents, e.g. scientific evidence, contemplative traditions, coaching application, embodied practice.
5. **Source verifier/fact checker** checks load-bearing claims.
6. **Synthesis agent** produces a bounded research synthesis.
7. **Independent reviewer** challenges omissions, contradictions and unsupported claims.
8. **CEO gate:** operator chooses whether findings are strong/useful enough to progress.
9. **Workshop designer** converts accepted findings into a rough 90-minute skeleton.
10. **Pedagogy/practice reviewer** checks sequencing and learning design.
11. **Operations/risk reviewer** checks room, equipment, audience, public/private and practical constraints.
12. **Creative/content agents** derive website article, video outline, social posts and invitation copy from the approved core—not from independent hallucinated reinterpretations.
13. **Final output** is stored with provenance and project links.
14. **Knowledge curator** proposes which validated concepts/results should be promoted into canonical MoA knowledge.
15. **CEO or defined quality gate** approves knowledge promotion.
16. Portfolio/task state records follow-up experiments and actual demand/results.

The AI executor for steps 1–15 may vary. The durable **agent definitions + workflows + knowledge + state + output contracts** should remain.

## 7. Required specialist-agent families for the research

The MCDA must no longer evaluate only workflow engines. It must determine how candidate ecosystems provide or support battle-proven agent/skill libraries across at least these families.

### Control and orchestration

- portfolio manager;
- project controller;
- workflow router/orchestrator;
- decomposition/planning agent;
- handoff coordinator;
- independent reviewer;
- completion verifier;
- knowledge curator.

### Research and knowledge

- research strategist;
- web/deep researcher;
- source/evidence verifier;
- comparative analyst;
- synthesis writer;
- contradiction/uncertainty reviewer;
- taxonomy/knowledge curator.

### Creative/content

- creative strategist;
- creative writer;
- editor;
- brand/voice reviewer;
- website copywriter;
- long-form content creator;
- social-media strategist;
- short-form/post writer;
- video/script writer;
- content repurposing agent.

### Workshops/coaching/method

- workshop designer;
- learning/pedagogy reviewer;
- coaching-method analyst;
- session/process designer;
- operations/logistics reviewer;
- public/private/sensitivity reviewer;
- offer/pricing/market test agent.

### Business/operations

- admin/SOP agent;
- customer-communication agent;
- project/portfolio reporting agent;
- offer/product agent;
- recurring-review agent;
- deterministic compliance/check agents where appropriate.

### Leela bridge

- use-case translator;
- workflow/process formalizer;
- product/specification agent;
- human-vs-software boundary reviewer.

This is a capability taxonomy for evaluating **existing proven agent/skill ecosystems**. It is not authorization to invent all of these agents ourselves.

## 8. Revised reuse-before-invention rule

For each capability family, the research order is:

1. **Existing integrated ecosystem** that already ships the relevant agent/workflow/skill.
2. **Existing upstream marketplace/packs/plugins/skills** officially supported by the ecosystem.
3. **Portable established agent/skill package** that integrates through a documented standard such as Agent Skills.
4. Project-specific configuration of an established agent/skill.
5. Only as last resort, create a new MoA-specific role definition where no proven reusable option exists.

Do not begin by writing dozens of custom MoA agent prompts.

## 9. Consequence for previous candidates

The previous MCDA compared only part of the actual decision.

### Foundational/control-plane candidates, not full winners by themselves

- GitHub Issues/Projects;
- Spec Kit;
- Beads;
- OpenSpec;
- Task Master.

They can supply durable state/process mechanics, but they do not alone constitute the full specialist-agent organization.

### Agent/workflow ecosystems now materially more important

- BMAD — because it ships agent roles/workflows and web bundles;
- Superpowers — because it ships reusable specialist process skills and review patterns;
- Ruflo — because it combines agent orchestration, workflows, plugins and memory capabilities;
- Gas City + official packs — because it can run packaged methodologies/agent flows, subject to non-software-fit evidence;
- Hermes — because it is both executor and skills/delegation/memory runtime;
- OpenClaw — because it can execute/manage subagents, skills and recurring work.

These must now be evaluated not merely as “donors/runtimes,” but for how much of the integrated operating loop they already provide without custom invention.

### No current overall winner

The prior Spec Kit/GitHub score remains evidence about **workflow/project control only**. It is not evidence that Spec Kit is the best full Master of Arts agent operating system.

## 10. Revised MCDA unit

The next comparison should rank **complete viable operating compositions/ecosystems**, not isolated tools.

Each candidate architecture must explicitly identify:

```yaml
portfolio_ssot: ...
knowledge_system: ...
orchestrator: ...
workflow_library: ...
specialist_agent_library: ...
skill_tool_library: ...
executor_clients:
  - ...
review_governance: ...
artifact_store: ...
learning_promotion: ...
```

A composition is acceptable only when its integration uses existing documented mechanisms and does not require us to invent a parallel orchestration/agent framework.

## 11. What future research must prove

For every complete candidate ecosystem/composition:

1. Which specialist agents/workflows already exist?
2. Are they battle-tested and maintained?
3. Can they be installed/reused instead of rewritten?
4. Can ChatGPT/Claude/Codex/Antigravity/local runtimes execute or participate in them?
5. How does the orchestrator choose and activate them?
6. What knowledge/context does each agent receive and how is it retrieved?
7. How do agents share/handoff durable state?
8. How are reviewers separated from makers?
9. Which steps are deterministic rather than AI-driven?
10. Where do outputs and provenance live?
11. How does accepted learning return to the knowledge base?
12. Can the operator see priorities, exceptions and CEO decisions without reading agent chatter?
13. Can the same system produce research, workshops, creative/content, operations and Leela precursor outputs?
14. What remains custom—and can that custom part be reduced by selecting a different existing ecosystem?

Only after this complete-system research should the final end-to-end pilots begin.
