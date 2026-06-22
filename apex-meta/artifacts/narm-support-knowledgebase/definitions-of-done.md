# Definitions of Done

## Source Basis

- Handover: `apex-meta/handoff/narm-index-prep-handover.md`
- Epic: `apex-meta/epics/narm-support-knowledgebase/epic.md`
- Task records: `apex-meta/epics/narm-support-knowledgebase/001.md` through `008.md`
- Prior H6 files: `apex-meta/handoff/task_plan.md`, `findings.md`, `progress.md`, `next-session.md`
- Operator source folder: `C:\Quasi Desktop\Leela New 26\Obsidian Leela New 01-26\X None Leela\Health\Therapy`

## Global Completion Rules

- Preparation artifacts are repo-local under `apex-meta/artifacts/narm-support-knowledgebase/`.
- Final indexes are not built in this pass.
- Theory, personal source evidence, behavioral inference, diagnostic-style hypothesis, and therapist question remain separate fields.
- Diagnostic-style hypotheses are allowed only when labeled as hypotheses and grounded in source pointers.
- No generated file claims to replace therapy, diagnose, treat, or overrule the NARM therapist.
- Output style is direct, concrete, evidence-labeled, and non-fluffy.

# Task 001

## Current Task Title

Define safety and scope boundaries for NARM-support system

## Proposed Revised Title

Define directness, evidence, and clinical-use operating rules

## Definition of Done

Task 001 is done when a repo artifact defines the operating rules that govern all later NARM-support artifacts.

Required conditions:

- Directness rules specify that outputs should be behaviorally concrete, plain, and source-aware.
- Evidence labels are defined and reusable:
  - raw source
  - source-backed summary
  - behavioral inference
  - diagnostic-style hypothesis
  - operator question
  - therapist question
- Clinical-use boundaries are stated without generic reassurance:
  - the system supports therapy preparation and integration;
  - it does not diagnose, treat, replace therapist judgment, or act as an emergency service;
  - high-risk distress or crisis content is routed to human/professional support.
- Psychological claims must preserve source basis and uncertainty.
- Therapist-facing use is framed as preparation material, not clinical conclusion.
- No-fluff rule is explicit: avoid vague reassurance, generic therapy language, motivational filler, and unsupported certainty.

## Required Artifact Outputs

- `definitions-of-done.md`: this Task 001 section.
- `workflow-prompts.md`: Directness And Evidence Prompt and Process Routing Prompt.
- Optional later: dedicated policy file if the operator wants the operating rules separated from index artifacts.

## Validation Questions

- Should diagnostic-style hypotheses be allowed in all artifacts, or only in personal-material and fusion artifacts?
- Should every psychological claim carry one mandatory label, or only interpretive claims?
- Should generic safety language be replaced with a shorter operational rule set such as: `support, prepare, reflect, do not diagnose, do not treat, do not escalate activation`?

## Out of Scope

- Building final indexes.
- Rewriting Task 001 itself without explicit operator confirmation.
- Producing therapy advice as if it were clinical treatment.
- Redacting or editing source files.

## Source Basis

- `001.md`
- `narm-index-prep-handover.md`

# Task 002

## Current Task Title

Inventory and classify Therapy source files

## Proposed Revised Title

Inventory and classify Therapy source files

## Definition of Done

Task 002 is done when all named source files are preserved exactly by file name, mapped to planned roles, and any ambiguous roles are listed for operator validation.

Required conditions:

- Exact operator source folder is preserved.
- Exact source file names are preserved.
- File-role categories are assigned without content extraction unless explicitly requested.
- Destination decision packet is prepared:
  - repo-only;
  - Obsidian-only;
  - repo plus Obsidian mirror.
- Recommendation is recorded: keep generated project artifacts repo-first until operator approves any Obsidian write or mirror.
- Ambiguous files are flagged rather than silently classified.

## Required Artifact Outputs

- `source-file-map.md`
- `index-validation-questions.md`: Artifact Destination Questions and Task 004 ambiguity questions.
- `index-artifact-plan.md`: Placement Rules.

## Validation Questions

- Should generated artifacts remain repo-only until approved?
- Should final indexes later be mirrored into the Obsidian Therapy folder?
- Are `ManifestationHowTo.md` and `Notion_Surrender_Page.md` psychological source material or adjacent practice context?
- Does `MyTherapy.md` contain relationship-pattern material, therapy goals, source references, or mixed material?

## Out of Scope

- Reading, extracting, or indexing source-file content.
- Moving, copying, or mutating source files.
- Writing generated indexes into Obsidian.

## Source Basis

- `002.md`
- `narm-index-prep-handover.md`

# Task 003

## Current Task Title

Design NARM theory index structure

## Proposed Revised Title

Design NARM theory index structure

## Definition of Done

Task 003 is done when the later Codex index-building pass has a schema, category plan, chunking rules, and validation questions for indexing `ET-Heller-NARM.md` without extracting the final theory index yet.

Required conditions:

- Theory-index schema exists.
- Top-level NARM theory categories are proposed.
- Chunking rules are defined.
- Every future theory entry can preserve:
  - source file;
  - source pointer or excerpt;
  - NARM concept;
  - category;
  - definition or summary;
  - cautions;
  - possible link-to-personal-material candidates;
  - extraction confidence.
- Goal/task analysis structure is preserved: source -> chunks -> categories -> questions -> recommendations -> operator validation.

## Required Artifact Outputs

- `index-artifact-plan.md`: NARM Theory Index Plan.
- `index-validation-questions.md`: Task 003 questions.
- `workflow-prompts.md`: NARM Theory Index Preparation Prompt.

## Validation Questions

- Should the later theory index preserve source excerpts or only source pointers plus summaries?
- Should NARM survival structures be indexed as separate files or as records inside one index file?
- Should quotable/source-backed definitions be separated from interpretive summaries?
- Should the theory index include therapist cautions as a required field?

## Out of Scope

- Extracting final NARM theory records.
- Creating the final `narm_theory_index.md` or equivalent final index.
- Making personal psychological interpretations from the theory source.

## Source Basis

- `003.md`
- `ET-Heller-NARM.md`
- `narm-index-prep-handover.md`

# Task 004

## Current Task Title

Design personal psychological material index structure

## Proposed Revised Title

Design personal psychological material index structure

## Definition of Done

Task 004 is done when one index schema covers all named personal/source files and supports later extraction without collapsing raw material into interpretation.

Required conditions:

- One schema exists for all personal-material sources.
- File-specific source references are preserved.
- Category labels are defined for later extraction:
  - raw excerpt or source pointer;
  - concrete behavior;
  - repeated relational pattern;
  - emotional theme;
  - self-belief or identity statement;
  - trigger or activation context;
  - protective strategy;
  - avoidance/collapse/control/compliance/pursuit/withdrawal/protest pattern when source-supported;
  - therapist-relevant note;
  - unresolved question;
  - diagnostic-style hypothesis.
- Ambiguous relationship-pattern source candidates are listed.
- Ambiguous adjacent practice files are marked for operator decision.

## Required Artifact Outputs

- `source-file-map.md`
- `index-artifact-plan.md`: Personal Material Index Plan.
- `index-validation-questions.md`: Task 004 questions.
- `workflow-prompts.md`: Personal Material Index Preparation Prompt.

## Validation Questions

- Which files should be treated as direct psychological self-report?
- Which files should be treated as AI-generated formulation rather than raw source?
- Which files contain relationship-pattern evidence?
- Should spiritual frameworks be indexed separately from personal psychological evidence?

## Out of Scope

- Extracting final personal records.
- Assigning clinical diagnoses.
- Treating AI-generated handovers as equivalent to raw self-report or clinician notes.

## Source Basis

- `004.md`
- Named source files in the epic and handover packet.

# Task 005

## Current Task Title

Define cross-reference model between NARM theory and personal material

## Proposed Revised Title

Define fusion model between NARM theory and personal material

## Definition of Done

Task 005 is done when a fusion-link schema exists that can later connect NARM theory records to personal-material records without converting theory labels into diagnosis.

Required conditions:

- Fusion schema exists before any links are generated.
- Every future link must preserve:
  - theory source pointer;
  - personal source pointer;
  - source excerpt or summary;
  - observed pattern;
  - NARM concept;
  - diagnostic-style hypothesis when useful;
  - confidence;
  - evidence basis;
  - therapist question;
  - self-exploration prompt seed.
- Theory, personal evidence, and hypothesis are separate fields.
- Confidence format is defined or flagged for operator validation.
- Therapist questions are mandatory for diagnostic-style hypotheses unless operator decides otherwise.

## Required Artifact Outputs

- `index-artifact-plan.md`: Fusion Model Plan.
- `index-validation-questions.md`: Task 005 questions.
- `workflow-prompts.md`: Fusion Model Prompt.

## Validation Questions

- Should confidence be low/medium/high, numeric, or both?
- Should therapist questions be mandatory for every diagnostic-style hypothesis?
- Should self-exploration prompts be generated only from medium/high confidence links?
- Should all fusion links require both a NARM source pointer and a personal source pointer?

## Out of Scope

- Generating final fusion links.
- Diagnosing survival structures.
- Presenting NARM-to-personal links as clinical conclusions.

## Source Basis

- `005.md`
- `narm-index-prep-handover.md`

# Task 006

## Current Task Title

Design guided self-exploration flow templates

## Proposed Revised Title

Design NARM-derived self-exploration flow template schema

## Definition of Done

Task 006 is done when the later flow-building pass has a schema and reusable prompts for self-exploration flows derived from both the NARM theory index and the personal-material index.

Required conditions:

- Flow-template schema exists.
- Flows depend on both:
  - NARM concept/category;
  - personal pattern/category.
- Each flow can include:
  - NARM concept;
  - personal pattern;
  - concrete behavior;
  - direct question;
  - body noticing;
  - agency noticing;
  - relationship noticing;
  - therapist-prep note;
  - stop/containment condition.
- Prompts are direct, not vague reflective language.
- Flows do not pretend to be therapy.
- Flows are not final-built yet.

## Required Artifact Outputs

- `index-artifact-plan.md`: Self-Exploration Flow Plan.
- `index-validation-questions.md`: Task 006 questions.
- `workflow-prompts.md`: Self-Exploration Flow Prompt.

## Validation Questions

- Should flows be organized by NARM concept, personal pattern, or current-life situation?
- Should each flow end in a therapist-facing question?
- Should body/agency/relationship tracks be mandatory separate fields?
- What activation threshold should stop self-inquiry and switch to regulation/containment only?

## Out of Scope

- Creating final guided flows.
- Running self-exploration sessions.
- Treating flow output as clinical intervention.

## Source Basis

- `006.md`
- `narm-index-prep-handover.md`

# Later Phase: Task 007

## Current Task Title

Design compact NARM therapist session-prep output format

## Later-Phase Status

Preserve as later-phase work. Do not use it to drive the current preparation pass.

## Later Definition of Done

Task 007 will be done when a compact therapist-facing session-prep template exists that separates observations, source references, questions, themes, and desired therapist support.

## Required Artifact Outputs Later

- Therapist session-prep output format.
- Redaction rules.
- Example output after operator approval.

## Validation Questions Later

- How compact should therapist-facing output be?
- Which personal details require redaction?
- Should therapist-facing summaries include diagnostic-style hypotheses or only questions?

## Out of Scope Now

- Building therapist-prep template now.
- Generating therapist-facing summaries from personal files.
- Mutating Task 007 status.

## Source Basis

- `007.md`
- `narm-index-prep-handover.md`

# Later Phase: Task 008

## Current Task Title

Prepare operator-approved implementation handoff

## Later-Phase Status

Preserve as later-phase work. Do not use it to drive the current preparation pass.

## Later Definition of Done

Task 008 will be done when the operator has approved the implementation handoff, dependency validation is complete, and Codex has clear instructions for index-building.

## Required Artifact Outputs Later

- Final implementation handoff.
- Operator-approved destination decisions.
- Dependency validation reference if requested through apex-sync.

## Validation Questions Later

- Has the operator approved the final index-building scope?
- Has artifact destination been confirmed?
- Has dependency validation been completed or explicitly deferred?

## Out of Scope Now

- Building final indexes.
- Mutating Task 008 status.
- Computing exact next action through apex-sync unless explicitly requested.

## Source Basis

- `008.md`
- `narm-index-prep-handover.md`
