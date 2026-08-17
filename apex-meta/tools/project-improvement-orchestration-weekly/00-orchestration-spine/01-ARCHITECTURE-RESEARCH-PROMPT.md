# Architecture Research Prompt — Skills, Agents, and the Simplest Weekly Runtime

## Research role

Act as an independent architecture researcher. Determine the **simplest native Claude Code architecture** for the APEX Weekly Orchestration runtime. The purpose is to test, not defend, the current `weekly-orchestrator -> stage agents -> stage skills` structure.

Do **not** implement changes in this research run. Produce a decision-ready recommendation for the Master Orchestrator.

## Core question

Is the current combination of a central Weekly Orchestrator skill, multiple custom stage agents, and multiple stage skills justified by real runtime needs, or does it duplicate instructions/context and create avoidable drift?

The answer must be based on:

1. current official Claude Code architecture/documentation;
2. the actual repository implementation;
3. demonstrated APEX workflow requirements;
4. context/token cost and repeatability;
5. the already validated operator-output design.

Do not assume either "agents are necessary" or "skills alone are simpler" before testing the concrete requirements.

---

## Required official research sources

Use current **primary Anthropic/Claude Code documentation only** for product/runtime claims. At minimum verify:

- Skills: `https://code.claude.com/docs/en/slash-commands`
- Subagents: `https://code.claude.com/docs/en/sub-agents`
- Feature comparison / Skill vs Subagent: `https://code.claude.com/docs/en/features-overview`
- Agent SDK Skills: `https://code.claude.com/docs/en/agent-sdk/skills`
- Agent SDK Subagents when relevant: `https://code.claude.com/docs/en/agent-sdk/subagents`

Verify the current docs at research time; do not rely on remembered Claude Code behavior.

---

## Repository scope to inspect

Repository: `leela-spec/apexai-os-meta`
Branch: `main`

### Central runtime

- `.claude/skills/weekly-orchestrator/SKILL.md`
- `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
- `.claude/skills/weekly-orchestrator/references/review-wiring.md`
- all files under `.claude/skills/weekly-orchestrator/references/roles/`

### Stage agents

Inspect all weekly-loop agents, including at minimum:

- `.claude/agents/apex-precap-week.md`
- `.claude/agents/apex-precap-next-day.md`
- `.claude/agents/apex-evidence-normalize.md`
- `.claude/agents/apex-flow-recap.md`
- `.claude/agents/apex-status-merge.md`
- `.claude/agents/apex-project-status.md`
- `.claude/agents/apex-review-validity.md`
- `.claude/agents/apex-review-alignment.md`

### Stage/domain skills

Inspect at minimum:

- `.claude/skills/PrecapWeek/`
- `.claude/skills/PrecapNextDay/`
- `.claude/skills/PromptEngineer/`
- `.claude/skills/AIRouting/`
- `.claude/skills/raw-flow-dump-normalize/` if present
- `.claude/skills/flow-recap/`
- `.claude/skills/status-merge/`
- `.claude/skills/ProjectStatus/`
- `.claude/skills/apex-session/`
- `.claude/skills/apex-sync/`

### Validated design sources

- `apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml`
- `apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml`
- `apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml`
- `apex-meta/operator-output-design/step3-output-design-system/05-prompt-file-and-index-design.okf.yaml`
- `apex-meta/operator-output-design/step5-template-promotion/02-template-promotion-map.yaml`
- `apex-meta/operator-output-design/step6-activation-validation/00-activation-validation-report.okf.md`

### Project-improvement control context

- `apex-meta/tools/project-improvement-orchestration-weekly/README.md`
- `apex-meta/tools/project-improvement-orchestration-weekly/PROJECT-CHARTER.md`
- `apex-meta/tools/project-improvement-orchestration-weekly/ORCHESTRATOR-DEFINITION.md`
- `apex-meta/tools/project-improvement-orchestration-weekly/00-orchestration-spine/README.md`

---

## Requirements the architecture must satisfy

Evaluate architecture against these real requirements rather than directory neatness.

### R1 — One production home

There must be one obvious canonical home that defines how the Weekly Orchestration lifecycle composes. A fresh runtime must not reconstruct the architecture from scattered stale files.

### R2 — Bounded AI judgment

The architecture must make stable and repeatable:

- stage ownership;
- input precedence;
- output ownership;
- transaction order;
- persistence rules;
- state authority;
- gate/review rules;
- AI versus deterministic versus operator responsibilities.

AI remains free to reason where judgment is intentionally required, such as weekly synthesis, prioritization, sprint planning, and prompt construction.

### R3 — Context efficiency

Do not preload instructions merely because they might become relevant. Prefer progressive/on-demand loading unless a worker cannot safely perform its job without the full rule set at startup.

### R4 — Context isolation only when valuable

A separate subagent is justified only when its isolated context, tool restrictions, model choice, parallelism, or reusable specialist behavior creates concrete value. Do not use an agent merely as a wrapper around one skill if the same workflow is safer and simpler in the main context.

### R5 — No duplicated authority

An agent prompt and its preloaded skill must not each independently encode the same domain contract. Identify any current duplication between stage-agent bodies and stage-skill entrypoints.

### R6 — Human-facing design is runtime behavior

The already validated operator-output design must be produced by the active workflow, not merely stored as unused templates.

### R7 — Fresh-context repeatability

The real test is whether a fresh session invoking the production entrypoint receives the correct rules automatically and produces the intended artifact from the same input class without relying on prior design conversation.

### R8 — Simple failure recovery

The architecture must make it easy to know:

- where the loop is;
- what stage owns the current problem;
- what input is missing;
- what can continue in degraded mode;
- what genuinely blocks.

### R9 — Change locality

Updating one output module should normally require changing that module's owning contract/template and only the minimal central interface, not editing many duplicate architectural descriptions.

---

## Architectures to compare

At minimum evaluate:

### A. Current pattern — orchestrator skill + custom stage agents + stage skills

Test whether every custom stage agent creates enough isolation/control value to justify the additional layer.

### B. Skill-centered main-session orchestration

Central Weekly Orchestrator remains in the main session and invokes stage skills directly where possible. Use subagents only for tasks that genuinely require isolated context or specialist constraints.

### C. Agent-centered stage workers with preloaded skills

Retain stage agents, but make their prompts extremely thin and place reusable/domain behavior only in owning skills. Central orchestrator remains the sole lifecycle authority.

### D. Skill `context: fork` / isolated skill execution where applicable

Check whether this can replace some custom wrapper agents without losing required context isolation or tool constraints.

### E. Any simpler native alternative found in current official docs

Only include it if it maps to a real APEX requirement. Do not introduce agent teams, SDK infrastructure, hooks, MCP, plugins, or new services merely because they exist.

---

## Required analysis per current agent

For each weekly-loop custom agent, answer:

1. What unique job does this agent perform that its skill does not?
2. Does it need a separate context window?
3. Does it need special tool restrictions or permissions?
4. Does it need a different model/effort setting?
5. Is it used for parallel work where isolation matters?
6. Does its prompt duplicate its preloaded skill?
7. Could the central Weekly Orchestrator call the skill directly with equal or better repeatability?
8. Verdict: `KEEP_AGENT`, `THIN_AGENT`, `REPLACE_WITH_SKILL`, or `RESEARCH_REQUIRED`.

Do the same for any stage skill that appears to exist only because an agent wrapper expects it.

---

## Required output

Produce one decision-ready report with these sections.

### 1. Executive decision

State the recommended production composition in no more than one page.

### 2. Native Claude architecture facts

Distinguish verified current product behavior from repository conventions.

### 3. Current APEX topology

Show the actual current routing graph and where each instruction source loads.

### 4. Duplication/context audit

For every stage agent/skill pair, identify duplicated instructions, unique value, and context cost.

### 5. Architecture comparison

Compare A-E against R1-R9. Avoid arbitrary numeric scoring unless a measurement is real. Use qualitative evidence and concrete trade-offs.

### 6. Recommended minimal topology

Show exactly which agents and skills remain, merge, become thin wrappers, or disappear.

### 7. Authority map

Identify the one canonical owner for:

- lifecycle composition;
- weekly planning;
- daily planning;
- flow execution preparation;
- prompt creation;
- evidence normalization;
- recap;
- state merge/mutation;
- project-state projection;
- deterministic read-side computation.

### 8. Migration impact

Name exact repo files/classes that would change if the recommendation is adopted. Do not implement them.

### 9. Rejected complexity

Explicitly identify tempting but unnecessary mechanisms and why they are rejected.

### 10. Verification plan

Define how a fresh Claude Code session can prove that the resulting architecture loads the correct rules and produces the expected stage behavior without design-chat memory.

---

## Research standards

- Use primary official Claude documentation for Claude capability claims.
- Use actual repository files for APEX architecture claims.
- Distinguish `VERIFIED`, `INFERENCE`, `PROPOSAL`, and `UNRESOLVED`.
- Cite exact repo paths and official source links close to claims.
- Do not defend existing architecture because it is already implemented.
- Do not recommend deletion solely because a component looks complex.
- Do not recommend a new abstraction unless a concrete requirement cannot be satisfied more simply.
- Optimize for **simple, resilient, efficient, repeatable, operator-comprehensible** behavior.

## Stop condition

Stop after producing the architecture recommendation and migration implications. The Master Orchestrator decides whether to adopt it and performs the integration work separately.
