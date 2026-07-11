# Glossary — canonical meaning for drifted terms

Rule: when any repo file uses these terms in a conflicting sense, this file wins for interpretation; the owning skill contract still wins for schema fields. Referenced from `ORCHESTRATION-SYSTEMS-INDEX.md` and `.claude/skills/weekly-orchestrator/SKILL.md`.

| term | canonical meaning | not |
|---|---|---|
| role | a named accountability with scoped tools and a precise description; says who may act | a unit of permission over artifacts — permission over an artifact comes from `authority.state`, never from role identity |
| state (of an artifact) | the artifact's `authority.state` (candidate / verified / invalidated) plus its `lifecycle_stage` (proposal / computed / confirmed) | the runtime memory of any agent |
| agent | an ephemeral, context-isolated subagent invocation from a durable definition file under `.claude/agents/` | an always-on process holding independent state; a skill |
| accountability | one of the four durable ownership surfaces — alfred, meta_strategy, meta_ops, meta_detective — carried as a field on packets and as subagent definitions | a persistent named agent with memory |
| skill | a reusable procedure/contract package under `.claude/skills/` that runs inside the invoking context (main thread or preloaded into a subagent) | an agent; a mechanism that grants isolation |
| workflow | the fixed stage sequence of the weekly loop, held in files (CLAUDE.md core_loop + weekly-orchestrator SKILL.md), not in any agent's memory | whatever sequence a session improvised |
| packet | any stage output carrying the shared handoff envelope (`.claude/skills/weekly-orchestrator/references/handoff-schema.md`) — the one shape for all handoffs | a free-form chat summary |
| candidate | produced but not independently reviewed; may not justify a canon-changing write | wrong, rejected, or low-quality |
| verified | independently reviewed at the current basis_digest with a pass verdict | operator-approved for write (that is `operator_validation: confirmed`) |
| canon / accepted | durable state under `state/` or `.claude/kb/` after a gated write | anything under `artifacts/` |
| validation | checking a packet against its contract/evidence (can be done by a reviewer agent) | approval — only the operator approves |
| approval | the operator setting `operator_validation: confirmed` on a specific packet | a reviewer pass verdict; silence; a prior approval of a different packet |
