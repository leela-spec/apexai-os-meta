# NARM Index Preparation Session Packet

## Purpose

This session packet is for another chat/session. Its job is to prepare the project so Codex can later build the actual NARM and personal psychological indexes directly in the repo.

Do not build the final indexes in the handover chat. Prepare the definitions of done, workflow prompts, artifact plan, validation questions, and implementation-ready instructions.

## Source Basis

- Project epic: `apex-meta/epics/narm-support-knowledgebase/epic.md`
- Task records: `apex-meta/epics/narm-support-knowledgebase/001.md` through `008.md`
- H6 files: `apex-meta/handoff/task_plan.md`, `findings.md`, `progress.md`, `next-session.md`
- Operator source folder: `C:\Quasi Desktop\Leela New 26\Obsidian Leela New 01-26\X None Leela\Health\Therapy`
- Named source files:
  - `ET-Heller-NARM.md`
  - `Anamnesebogen AGehm.docx`
  - `Psychological_Handover_Medical_Grade_v1.md`
  - `PsychologicalHandover_ChatTherapeuticFramework_inACIM.md`
  - `shadow_insight_v1.md`
  - `shadow_insight_v2.md`
  - `shadow_insight_v3.md`
  - `ManifestationHowTo.md`
  - `MyTherapy.md`
  - `Notion_Surrender_Page.md`

## Operator Direction To Preserve

- If the operator says something that conflicts with the skill-package process, state the process mismatch and follow the process.
- The operator wants direct, truthful, behaviorally concrete output.
- Avoid vague reassurance, generic therapy language, and fluff.
- The system is private. Do not soften the material merely because it is psychologically direct.
- Diagnostic-style hypotheses are acceptable when clearly labeled as hypotheses, not as established fact unless source-backed by clinician or document.
- The indexes should be built by Codex later, but prepared by the other chat.
- Task 007 and Task 008 are later-phase work and should not drive the next preparation pass.

## Required Handover-Chat Work

The next chat should create implementation-ready definitions of done for each active task and save the specific preparation artifacts directly in the repo.

The handover chat should not perform the final indexing pass. It should prepare the artifact structure and validation questions so Codex can build the indexes afterward.

## Session Workflow

The next chat should execute this workflow in order.

1. Read the package process files:
   - `.claude/skills/apex-plan/SKILL.md`
   - `.claude/skills/apex-session/SKILL.md`
   - `.claude/skills/apex-sync/SKILL.md`
2. Read the current project files:
   - `apex-meta/epics/narm-support-knowledgebase/epic.md`
   - `apex-meta/epics/narm-support-knowledgebase/001.md` through `008.md`
   - `apex-meta/handoff/task_plan.md`
   - `apex-meta/handoff/findings.md`
   - `apex-meta/handoff/progress.md`
   - `apex-meta/handoff/next-session.md`
3. Create the artifact folder:
   - `apex-meta/artifacts/narm-support-knowledgebase/`
4. Prepare, but do not final-build, these artifacts:
   - `definitions-of-done.md`
   - `index-artifact-plan.md`
   - `index-validation-questions.md`
   - `source-file-map.md`
   - `workflow-prompts.md`
5. Use `apex-plan` reasoning for task-definition revisions, category proposals, and dependency implications.
6. Use `apex-session` for repo writes and updates to H6 handoff files.
7. Use `apex-sync` only if deterministic dependency validation or next-action computation is requested.
8. Stop when the preparation artifacts exist and the next Codex index-building pass has clear instructions.

## Session Prompts To Use

Use these prompts internally or visibly as the working structure for the next chat.

### Process Check Prompt

```text
Does this requested action belong to apex-plan, apex-session, or apex-sync?
If it conflicts with package boundaries, state the mismatch and route it to the correct package.
```

### Definition Of Done Prompt

```text
For this task, define observable completion conditions.
Separate:
- what artifact must exist;
- where it must be saved;
- what source basis it must preserve;
- what operator validation is needed;
- what is explicitly out of scope.
```

### Index Design Prompt

```text
For this source domain, prepare the index design using:
source -> chunks -> categories -> questions -> recommendations -> operator validation.
Do not extract the final index yet.
```

### Directness And Evidence Prompt

```text
Write directly and concretely.
Label each claim as one of:
- raw source;
- source-backed summary;
- behavioral inference;
- diagnostic-style hypothesis;
- operator question;
- therapist question.
Remove vague reassurance and generic therapeutic language.
```

### Fusion Model Prompt

```text
For each proposed NARM-to-personal-material link, preserve:
- source excerpt or source pointer;
- observed behavior or pattern;
- NARM concept;
- diagnostic-style hypothesis when useful;
- confidence;
- evidence basis;
- therapist-facing question;
- self-exploration prompt seed.
```

### Artifact Placement Prompt

```text
Save project-control files under apex-meta.
Save preparation artifacts under apex-meta/artifacts/narm-support-knowledgebase.
Do not write final generated indexes into the Obsidian Therapy folder unless the operator explicitly approves that destination.
```

## Proposed Repo Artifact Locations

Use these repo locations unless the operator explicitly changes them:

- `apex-meta/epics/narm-support-knowledgebase/` for task records.
- `apex-meta/handoff/` for session handover and continuation files.
- `apex-meta/artifacts/narm-support-knowledgebase/` for project artifacts prepared for later indexing.
- `apex-meta/artifacts/narm-support-knowledgebase/definitions-of-done.md`
- `apex-meta/artifacts/narm-support-knowledgebase/index-artifact-plan.md`
- `apex-meta/artifacts/narm-support-knowledgebase/index-validation-questions.md`
- `apex-meta/artifacts/narm-support-knowledgebase/source-file-map.md`
- `apex-meta/artifacts/narm-support-knowledgebase/workflow-prompts.md`

Do not write generated indexes into the Obsidian Therapy folder unless the operator explicitly approves that destination.

## Artifact Specifications

### `definitions-of-done.md`

Required sections:

- `# Task 001`
- `# Task 002`
- `# Task 003`
- `# Task 004`
- `# Task 005`
- `# Task 006`
- `# Later Phase: Task 007`
- `# Later Phase: Task 008`

Each active task section must include:

- current task title;
- proposed revised title when applicable;
- definition of done;
- required artifact outputs;
- validation questions;
- out-of-scope items;
- source basis.

### `index-artifact-plan.md`

Required sections:

- `# Artifact Root`
- `# Prepared Artifacts`
- `# Later Codex-Built Indexes`
- `# NARM Theory Index Plan`
- `# Personal Material Index Plan`
- `# Fusion Model Plan`
- `# Self-Exploration Flow Plan`
- `# Placement Rules`

The plan must distinguish preparation artifacts from final indexes.

### `index-validation-questions.md`

Required sections:

- `# Task 003: NARM Theory Questions`
- `# Task 004: Personal Material Questions`
- `# Task 005: Fusion Model Questions`
- `# Task 006: Flow Template Questions`
- `# Artifact Destination Questions`

Questions must be direct and validation-oriented. Avoid vague exploratory wording when a decision is needed.

### `source-file-map.md`

Required sections:

- `# Source Folder`
- `# Source Files`
- `# Planned Roles`
- `# Missing Or Ambiguous Roles`
- `# Relationship-Pattern Source Candidates`

The map must preserve exact file names and path references.

### `workflow-prompts.md`

Required sections:

- `# Process Routing Prompt`
- `# Definition Of Done Prompt`
- `# NARM Theory Index Preparation Prompt`
- `# Personal Material Index Preparation Prompt`
- `# Fusion Model Prompt`
- `# Self-Exploration Flow Prompt`
- `# Directness And Evidence Prompt`

These prompts should be ready to reuse in the later Codex index-building pass.

## Task-Specific Preparation Requirements

### Task 001

Current task title: `Define safety and scope boundaries for NARM-support system`

Operator correction: revise conceptually toward `Define directness, evidence, and clinical-use operating rules`.

Handover-chat output needed:

- A revised definition of done for Task 001.
- A proposed task-title revision.
- Operating rules for:
  - directness;
  - evidence labels;
  - source-backed claims versus inference;
  - diagnostic-style hypotheses;
  - therapist-facing use;
  - no-fluff output.

Workflow:

1. Treat the existing task title as outdated operator-reviewed context.
2. Propose the revised title without silently mutating the task file unless the operator confirms a write.
3. Write the Task 001 DoD into `definitions-of-done.md`.
4. Write reusable directness/evidence prompts into `workflow-prompts.md`.

Validation questions:

- Should diagnostic-style hypotheses be allowed in all artifacts, or only in personal-material and fusion artifacts?
- What labels should be mandatory on every psychological claim?
- What wording should replace generic safety/scope language?

### Task 002

Current task title: `Inventory and classify Therapy source files`

Handover-chat output needed:

- Definition of done for file inventory.
- Source-file classification schema.
- Decision packet for artifact destinations:
  - repo-only;
  - Obsidian-only;
  - repo plus Obsidian mirror.
- Recommendation: keep generated project artifacts in repo first.

Workflow:

1. Preserve the exact source folder path.
2. Preserve all listed file names.
3. Create a file-role map without reading or indexing file content yet unless the operator explicitly asks.
4. Record unresolved destination decisions in `index-validation-questions.md`.

Validation questions:

- Should generated artifacts remain repo-only until approved?
- Should final indexes later be mirrored into Obsidian?
- Are `ManifestationHowTo.md` and `Notion_Surrender_Page.md` psychological material or adjacent practice context?

### Task 003

Current task title: `Design NARM theory index structure`

Handover-chat output needed:

- Definition of done for NARM theory index structure.
- Proposed NARM theory index categories.
- Validation questions for the operator before full extraction.
- Artifact schema for later Codex-built theory index.

Important: Use a goal/task analysis style process: source -> chunks -> categories -> questions -> recommendations -> operator validation.

Workflow:

1. Define theory-index artifact schema.
2. Propose top-level NARM theory categories.
3. Define chunking rules for later extraction.
4. Define validation questions before full indexing.
5. Save the preparation output in `index-artifact-plan.md` and `index-validation-questions.md`.

Recommended category candidates:

- NARM core concepts.
- Developmental themes.
- Survival styles or adaptive strategies.
- Connection, agency, and aliveness.
- Shame, pride, collapse, protest, compliance, and disconnection patterns when source-supported.
- Therapist cautions and non-pathologizing framing.
- Quotable/source-backed definitions.
- Links-to-personal-material candidates.

### Task 004

Current task title: `Design personal psychological material index structure`

Handover-chat output needed:

- Definition of done for personal-material index structure.
- One schema covering all named personal/source files.
- File-by-file source map.
- Categories for:
  - raw excerpt;
  - behavioral pattern;
  - emotional theme;
  - relational pattern;
  - self-belief;
  - trigger;
  - protective strategy;
  - therapist-relevant note;
  - unresolved question;
  - diagnostic-style hypothesis.

Important: Use the same preparation process as Task 003.

Workflow:

1. Define one schema for all named personal files.
2. Preserve file-specific source references.
3. Define category labels for later extraction.
4. Prepare validation questions for ambiguous files and relationship-pattern sources.
5. Save the output in `source-file-map.md`, `index-artifact-plan.md`, and `index-validation-questions.md`.

Recommended category candidates:

- Raw excerpt or source pointer.
- Concrete behavior.
- Repeated relational pattern.
- Emotional theme.
- Self-belief or identity statement.
- Trigger or activation context.
- Protective strategy.
- Avoidance, collapse, control, compliance, pursuit, withdrawal, or protest pattern when source-supported.
- Therapist-relevant note.
- Diagnostic-style hypothesis.
- Open question.

### Task 005

Current task title: `Define cross-reference model between NARM theory and personal material`

Operator correction: this is the fusion layer.

Handover-chat output needed:

- Definition of done for the fusion model.
- Link schema:
  - source excerpt;
  - observed pattern;
  - NARM concept;
  - diagnostic-style hypothesis;
  - confidence;
  - evidence basis;
  - therapist question;
  - self-exploration prompt seed.
- Recommendation for how NARM theory and personal material should be fused without losing source traceability.

Workflow:

1. Define the link schema before making links.
2. Require every link to preserve source basis.
3. Keep theory, personal evidence, and hypothesis in separate fields.
4. Save the fusion schema in `index-artifact-plan.md`.
5. Save fusion validation questions in `index-validation-questions.md`.

Validation questions:

- Should confidence be low/medium/high, numeric, or both?
- Should therapist questions be mandatory for every diagnostic-style hypothesis?
- Should self-exploration prompts be generated only from medium/high confidence links?

### Task 006

Current task title: `Design guided self-exploration flow templates`

Operator clarification: flows should come from NARM and build on the personal psychological material index.

Handover-chat output needed:

- Definition of done for self-exploration flow templates.
- Flow schema built from:
  - NARM concept;
  - personal pattern;
  - concrete behavior;
  - direct question;
  - body/agency/relationship noticing;
  - therapist-prep note.
- Do not create final flows yet unless the operator explicitly asks.

Workflow:

1. Define flow-template schema only.
2. Make flows depend on both NARM theory categories and personal-material categories.
3. Include direct questions, not vague reflective prompts.
4. Include a therapist-prep note field.
5. Save flow prompt patterns in `workflow-prompts.md`.

Validation questions:

- Should flows be organized by NARM concept, personal pattern, or current-life situation?
- Should each flow end in a therapist-facing question?
- Should flows include body/agency/relationship tracks as separate fields?

### Task 007

Current task title: `Design compact NARM therapist session-prep output format`

Operator direction: later; skip for now.

Handover-chat output needed:

- Preserve as later-phase.
- If status mutation is requested, route to `apex-session` and create the required mutation record.

### Task 008

Current task title: `Prepare operator-approved implementation handoff`

Operator direction: later; skip for now.

Handover-chat output needed:

- Preserve as later-phase.
- If status mutation is requested, route to `apex-session` and create the required mutation record.

## Process Instructions For The Other Chat

1. Read:
   - `.claude/skills/apex-plan/SKILL.md`
   - `.claude/skills/apex-session/SKILL.md`
   - `.claude/skills/apex-sync/SKILL.md`
2. Read this handover file.
3. Read task records `001.md` through `008.md`.
4. Use `apex-plan` for task-definition revisions and planning packets.
5. Use `apex-session` for repo writes, H6 handoff updates, and any status mutation.
6. Use `apex-sync` only for deterministic dependency/next-action reports.
7. Save preparation artifacts under `apex-meta/artifacts/narm-support-knowledgebase/`.
8. Do not build the final indexes in that chat unless the operator explicitly changes the assignment.

## Exact Next-Chat Opening Instruction

The next chat can start with this instruction:

```text
Read apex-meta/handoff/narm-index-prep-handover.md and execute it as an apex-session continuation. Create the preparation artifacts under apex-meta/artifacts/narm-support-knowledgebase/. Do not build the final indexes yet.
```

## Completion Criteria For The Other Chat

- `definitions-of-done.md` exists and covers Tasks 001 through 006 in implementation-ready form, with Tasks 007 and 008 marked later-phase.
- `index-artifact-plan.md` defines the artifact set Codex will build later.
- `index-validation-questions.md` lists operator validation questions for Tasks 003, 004, 005, and 006.
- `source-file-map.md` maps named Therapy files to planned index roles.
- `workflow-prompts.md` contains reusable prompts for the preparation and later index-building workflows.
- H6 `next-session.md` is updated to point Codex toward the actual index-building pass.
