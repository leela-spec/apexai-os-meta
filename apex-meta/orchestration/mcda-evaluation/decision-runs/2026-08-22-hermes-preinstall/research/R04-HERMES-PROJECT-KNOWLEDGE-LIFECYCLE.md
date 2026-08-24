# R04 — Hermes Project Knowledge Lifecycle Research

Status: **RESEARCH REQUIRED / PRE-INSTALL**  
Priority: **P0 — blocks knowledge migration/design**  
Depends on: R02 project model, R03 QMD integration  
Decision owner: Human CEO

## Decision question

Using only established Hermes/project-file/QMD mechanisms, how should each Master of Arts project family and concrete project remain **current, understandable, retrievable and durable over time** without creating a custom KB platform or duplicate truth?

This is not a folder-design exercise. The researcher must derive the lifecycle from what Hermes, Git/project files, Agent Skills and QMD actually support.

## Required distinctions

The research must keep these categories separate:

1. organization-wide durable facts/policies;
2. project-family durable facts/decisions;
3. micro-project current brief/status/decisions;
4. raw research/source material;
5. final artifacts/outputs;
6. reusable procedures/skills;
7. Hermes profile/runtime memory;
8. Hermes agent-created learned skills;
9. QMD index/embeddings as derived retrieval state;
10. Kanban task/workflow state.

No category may silently become a second copy of another category.

## Primary sources

- Hermes Context Files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/
- Hermes Memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes Curator: https://hermes-agent.nousresearch.com/docs/user-guide/features/curator
- Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes QMD skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
- QMD: https://github.com/tobi/qmd
- Git/GitHub only for ordinary version history/storage behavior actually used by the selected setup.

## Research tasks

### 1. Identify the authoritative owner for every information type

Create:

| Information type | Canonical owner | Who writes it | Who reads it | Version/history | Auto-loaded? | Searchable via QMD? | Duplicated elsewhere? |
|---|---|---|---|---|---|---|---|

The goal is one source of truth per information type.

### 2. Determine what a project needs to remain operable

Using R02's upstream-native hierarchy, determine the complete information package required so that a fresh Hermes worker can enter a project and work correctly.

Do not optimize for the fewest files. Optimize for complete reliable operation with efficient context loading.

For every required artifact record:

```text
ARTIFACT:
PURPOSE:
UPSTREAM_CONSUMER:
CREATED/UPDATED_BY:
WHEN_UPDATED:
AUTO_LOADED_OR_ON_DEMAND:
QMD_INDEXED:
TOKEN_IMPACT:
WHAT_BREAKS_IF_STALE:
WHAT_BREAKS_IF_MISSING:
```

### 3. Freshness lifecycle

Trace:

```text
new source / new operator decision / completed task
 -> affected durable project information identified
 -> project artifact updated
 -> Git/version history records change
 -> QMD index refreshed
 -> next Hermes session sees/retrieves current state
```

Determine which steps are:

- Hermes-native automatic behavior;
- deterministic command/tooling;
- AI semantic judgment;
- human approval.

### 4. Conflict and staleness handling

Real repositories contain stale drafts and conflicting statements. Determine how the selected upstream mechanisms let an agent distinguish:

- active vs historical artifact;
- approved vs draft;
- current vs superseded decision;
- source evidence vs synthesized conclusion;
- project fact vs runtime memory;
- outdated QMD index vs current file.

Do not invent a large ontology. Prefer existing versioning/status mechanisms or explicit project artifacts already needed by the user stories.

If an additional convention is unavoidable, prove that it is only a data convention consumed by the selected systems, not a new framework.

### 5. Update responsibility

For each durable artifact answer:

- Which workflow/task is responsible for updating it?
- Can the update be deterministic?
- Does an AI need to decide what changed?
- Is there a reviewer/CEO gate?
- What happens if the update is skipped?

The design fails if the operator must manually update multiple parallel summaries after normal work.

### 6. QMD refresh integration

Using R03 findings, determine how file changes become searchable again.

Compare official supported choices such as:

- explicit `qmd update`/`embed` during defined workflows;
- any documented daemon/watch/update behavior if current upstream provides it;
- scheduled deterministic refresh through an existing supported scheduler if necessary.

Do not write a custom file watcher unless an upstream mechanism truly does not exist and the lack is accepted as a blocker.

### 7. Session/restart simulation

Run on paper:

1. Day 1: research creates new findings.
2. Reviewer rejects one claim and accepts another.
3. CEO changes project priority.
4. Final workshop artifact is produced.
5. QMD index is refreshed.
6. Hermes session closes.
7. Day 7: a new worker starts in the project.

Show exactly what the new worker automatically loads, what it retrieves, what task state it reads, and why it does not need the old chat transcript.

### 8. Cross-project learning without factual contamination

A finding from Project A may be:

- a Project A fact;
- an organization-wide fact;
- a reusable procedure;
- a marketing pattern;
- a one-off observation.

Determine how existing Hermes/project mechanisms distinguish these destinations without automatically copying all learning across projects.

This must link to R06 but stay focused on factual/project lifecycle.

### 9. Human/web AI access

Determine which durable files remain usable to a web subscription AI with repository access even if it cannot call local Hermes/QMD.

The project truth should remain inspectable by humans and other AI clients rather than being trapped inside Hermes databases/memory.

## Required user stories

### US-A — Existing messy project enters the system

Take one real project with loose files. Show how it becomes operable through the upstream-native project/context mechanism without mass rewriting all historical material.

### US-B — New concrete project under existing family

Show what gets created/reused at project start, what is inherited, what stays local and how QMD indexes it.

### US-C — Project changes over time

Show status/decision/source updates, QMD refresh and new-session retrieval.

### US-D — Project closes

Show final artifacts, retained knowledge, closed task state and what remains searchable for future work.

## Required output

1. source-of-truth matrix;
2. complete project knowledge package and each artifact's consumer;
3. freshness/update lifecycle;
4. staleness/conflict handling;
5. QMD refresh mechanism;
6. restart/resume simulation;
7. human/web-AI accessibility analysis;
8. manual maintenance burden;
9. unresolved gaps;
10. verdict:
   - `PROJECT_KNOWLEDGE_LIFECYCLE_CONFIRMED`
   - `DUPLICATE_MANUAL_TRUTH_REQUIRED`
   - `CUSTOM_KB_REQUIRED`.

## Failure condition

If keeping the system current requires a separate custom knowledge database, custom synchronization engine, or repeated manual rewriting of the same facts into multiple systems, report the failure rather than designing the missing subsystem.
