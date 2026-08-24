# 01 — Candidate Screening

Status: **initial evidence screen; not a final ranking**

## 1. Candidate classes

The research deliberately separates three layers that are often conflated:

1. **Project/specification layer** — turns goals into persistent requirements/plans/work artifacts.
2. **Execution/orchestration layer** — owns durable task state, dependencies, agent assignment, handoffs, retries and resume.
3. **Skill/process layer** — packages repeatable methods so agents can invoke them consistently with progressive disclosure.

A single system may span more than one layer. A composition is allowed only if each layer is owned by an established system and there is one clear canonical source of truth for each kind of state.

## 2. Initial longlist

| Candidate | Layer(s) | Initial status | Why it is here | Main concern to test |
|---|---|---|---|---|
| **GitHub Spec Kit** | project/spec + workflow | **SURVIVES INITIAL SCREEN** | Mature spec-driven toolkit; persistent Markdown artifacts; current project explicitly supports broader business-process presets and many agent clients including Claude Code, Codex and Antigravity. | Historically developer-centric; must prove it can manage Master-of-Arts non-code projects without forcing software metaphors everywhere. |
| **Beads** | durable task/project state | **SURVIVES INITIAL SCREEN** | Git-backed dependency-aware task system built for agents; compact machine-readable state, claims/dependencies/history, CLI-friendly and repo-native. | It is primarily a work graph, not a complete CEO/project-method framework; likely needs a project/spec and skill layer. |
| **Gas City** | multi-agent execution/runtime | **SURVIVES, HIGHER COMPLEXITY** | Existing orchestration platform layered on Beads with formulas, scheduling, agent dispatch, retries/resume and pack architecture. | Operational complexity may be excessive for Master of Arts; must prove non-code and human-governed use, not merely software swarms. |
| **Superpowers** | skill/process + disciplined execution | **SURVIVES INITIAL SCREEN** | Established skill-based development workflow with reusable practices; installable as a ChatGPT plugin in this environment and used across coding agents. | Strong coding orientation; may be best as a skill/process reference rather than portfolio PM/runtime. |
| **BMAD Method** | project/process + multi-agent roles | **SURVIVES INITIAL SCREEN** | Popular structured agent methodology with planning, role separation, artifacts and implementation workflow. | Software/product-development orientation and potentially large instruction surface; portability to ChatGPT/repo-native business workflows needs proof. |
| **OpenSpec** | specification/change workflow | **SURVIVES INITIAL SCREEN** | Existing spec-driven workflow with structured change artifacts and broad agent-tool integrations. | Change/spec orientation may fit projects but not long-running portfolio scheduling/ownership by itself. |
| **Task Master / Claude Task Master** | task decomposition/PM | **RESEARCH FURTHER** | Existing AI task-management system designed to generate/manage dependent tasks. | Need stronger current evidence for cross-client state, non-code fit and long-term maintenance before promoting to finalist. |
| **Claude Code native teams/workflows/skills** | execution + skills | **REFERENCE / POSSIBLE COMPONENT** | Strong current native capabilities: skills, subagents/teams, dynamic workflows, hooks. | Vendor-specific runtime state cannot be the portfolio's sole source of truth; web ChatGPT/Codex interoperability would be weaker. |
| **OpenClaw/Hermes orchestration** | execution + skills | **REFERENCE / INCUMBENT** | Already present in this repo and prior research; supports skills, scheduling/delegation and local runtime. | Prior project experience shows risk of orchestration complexity/drift; must compete against newer repo-native systems rather than receive incumbent preference. |
| **GitHub Issues/Projects + agent skills** | project/task baseline | **CONTROL CANDIDATE** | Extremely mature, transparent, interoperable and directly visible to web/CLI agents with GitHub access. | Less agent-native dependency/context handling and skill workflow semantics than specialized systems. |

## 3. Candidates not promoted as standalone winners yet

These may be excellent components but do not currently appear to own the whole target problem:

- **Agent Skills standard / `SKILL.md` alone** — excellent portability and progressive disclosure, but not a durable portfolio/task orchestration system.
- **LangGraph / Temporal / Prefect** — proven workflow runtimes, but would require us to design much of the Master-of-Arts project/skill semantics ourselves; use only if finalists reveal a real runtime gap they solve better natively.
- **CrewAI / AutoGen-style agent frameworks** — capable agent runtimes, but they tend to center API/programmatic agents rather than subscription-client interoperability and repo-native human project management.
- **Generic SaaS PM tools** — useful for humans but do not automatically provide the repo-installed skill/workflow behavior or deterministic agent execution substrate required here.

They may re-enter if evidence shows an existing packaged solution that directly meets the hard gates.

## 4. Early structural hypotheses to test — not decisions

### H1 — Spec Kit + Beads + portable Agent Skills

Potential division of responsibility:

- **Spec Kit:** persistent goals/specifications/plans and project-level artifact discipline;
- **Beads:** durable execution graph, dependencies, claims, status, handoffs and resume;
- **Agent Skills:** reusable Master-of-Arts methods/workflows loaded only when relevant;
- **ordinary scripts/hooks/CI:** deterministic validation and mechanical transitions;
- **human operator:** consequential decision authority.

Why it is promising: each layer is an established system rather than a custom subsystem, and the repository remains the interoperability boundary.

What could kill it: duplication between Spec Kit tasks and Beads tasks, or too much translation glue. The pilot must prove one canonical task truth and one clean mapping from project specification to execution work.

### H2 — Gas City + Beads, with an established spec/skill pack

Potential advantage: more complete autonomous execution, scheduling, retries and multi-agent coordination out of the box.

What could kill it: operational burden, coding-centric defaults, unnecessary swarm complexity, or inability to expose a clean CEO-level project view to web agents.

### H3 — BMAD (or OpenSpec) + repo-native task state + portable skills

Potential advantage: mature role/process guidance and existing artifact structures.

What could kill it: instruction bloat, software-specific assumptions, duplicate task state, or weak continuous orchestration/resume compared with Beads/Gas City.

### H4 — GitHub-native baseline + portable skills

Use GitHub Issues/Projects as canonical work state, agent skills for methods, Actions/hooks/scripts for deterministic automation.

Why it must remain in the bake-off: it is the **complexity control**. A specialized orchestration system only wins if it produces material value over this very mature baseline.

## 5. Current strongest evidence-backed observations

### 5.1 Master of Arts requires more than a coding task manager

The repository's current Master-of-Arts architecture explicitly spans operating-business and knowledge-production work: client delivery, method formalization, website/content/offer multiplication, research, administration and later Leela productization. Therefore any framework that only shines at code implementation cannot win G9 without a convincing real pilot.

### 5.2 Prior repo research correctly identified required mechanisms, but mostly proposed building them

Existing process-ranking material identifies useful capabilities such as:

- goal → verified artifact loops;
- durable multi-agent task graphs;
- fan-out/fan-in specialization;
- guarded handoffs;
- risk/verification gates;
- recurring project cycles;
- knowledge-bank workflows.

Those become **requirements and pilot behaviors**, not custom implementation instructions. The new MCDA asks which established system already provides them.

### 5.3 Repo-native state is the primary interoperability strategy

No evidence currently supports a magical runtime shared natively by every web and CLI subscription model. The practical interoperability boundary is therefore **durable repository state in open formats**, plus adapters/instructions that let each agent client read and act on the same state.

This means a candidate may have an excellent local runtime, but if its essential state is opaque or trapped inside one vendor/client, it loses heavily on C2 and can fail G4.

## 6. Evidence still required before scoring

For each surviving candidate, gather from official/current sources:

- current release/activity and maintainer status;
- adoption signals;
- exact persistent artifact/state format;
- dependency/task semantics;
- human approval/review mechanisms;
- resume/recovery behavior;
- skills/workflow packaging model;
- deterministic hooks/scripts/automation;
- agent/client compatibility, especially Claude Code, Codex, Antigravity and repo-connected ChatGPT;
- non-code examples or proof that workflows are domain-neutral;
- install/update/backup requirements;
- security/permissions model;
- known failure modes/limitations.

Then score against `00-MCDA-CHARTER.md` and reduce to **2–3 finalists plus the GitHub-native control**.

## 7. No-selection warning

Nothing in this file authorizes implementation. Names in the longlist are research targets. A final recommendation must survive weighted scoring, sensitivity analysis and the real-work pilot in `02-PILOT-PROTOCOL.md`.
