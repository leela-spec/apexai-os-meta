# Process Routing Prompt

```text
Does this requested action belong to apex-plan, apex-session, or apex-sync?

Use apex-plan for:
- task-definition revisions;
- planning packets;
- category proposals;
- dependency proposals;
- qualitative priority/urgency rationale.

Use apex-session for:
- repo writes;
- H6 handoff updates;
- status mutation records;
- session progress;
- next-session context.

Use apex-sync only for deterministic read-side reports:
- dependency validation;
- next-action computation;
- blocker reports;
- registry previews;
- drift/stall/score reports.

If the operator request conflicts with package boundaries, state the mismatch and route it to the correct package. Do not silently perform out-of-scope work.
```

# Definition Of Done Prompt

```text
For this task, define observable completion conditions.

Separate:
- what artifact must exist;
- where it must be saved;
- what source basis it must preserve;
- what operator validation is needed;
- what is explicitly out of scope.

Do not build final indexes while preparing definitions of done.
```

# NARM Theory Index Preparation Prompt

```text
Prepare the NARM theory index design for the later Codex pass.

Use this process:
source -> chunks -> categories -> questions -> recommendations -> operator validation.

Source:
- ET-Heller-NARM.md

Output only the preparation design, not the final index.

For each proposed category, define:
- category name;
- purpose;
- expected source basis;
- fields required in final index records;
- chunking rules;
- ambiguity handling;
- validation questions.

Required categories to consider:
- NARM core concepts;
- developmental themes;
- biological core needs;
- adaptive survival strategies;
- self-regulation and affect regulation;
- somatic mindfulness;
- connection, agency, contact, and aliveness;
- shame-based identifications and pride-based counteridentifications;
- protest, anger, collapse, compliance, withdrawal, disconnection, and distorted life-force patterns when source-supported;
- therapist cautions and non-pathologizing framing;
- quotable/source-backed definitions;
- links-to-personal-material candidates.

Never infer personal conclusions in the theory index. Store only possible link candidates for later fusion.
```

# Personal Material Index Preparation Prompt

```text
Prepare the personal psychological material index design for the later Codex pass.

Use this process:
source -> chunks -> categories -> questions -> recommendations -> operator validation.

Sources:
- Anamnesebogen AGehm.docx
- Psychological_Handover_Medical_Grade_v1.md
- PsychologicalHandover_ChatTherapeuticFramework_inACIM.md
- shadow_insight_v1.md
- shadow_insight_v2.md
- shadow_insight_v3.md
- ManifestationHowTo.md
- MyTherapy.md
- Notion_Surrender_Page.md

Output only the preparation design, not the final index.

For each source, preserve:
- exact file name;
- source type;
- evidence weight;
- planned index role;
- ambiguity or validation questions.

For the later extraction schema, include fields for:
- raw excerpt or source pointer;
- concrete behavior;
- repeated relational pattern;
- emotional theme;
- self-belief or identity statement;
- trigger or activation context;
- protective strategy;
- avoidance, collapse, control, compliance, pursuit, withdrawal, or protest pattern when source-supported;
- therapist-relevant note;
- diagnostic-style hypothesis;
- open question.

Treat AI-generated handovers as secondary formulation unless raw self-report is explicitly embedded.
Treat spiritual/practice files as adjacent context unless the operator approves inclusion in the main psychological index.
Do not diagnose.
```

# Fusion Model Prompt

```text
For each proposed NARM-to-personal-material link, preserve separate fields for:
- theory source pointer;
- personal source pointer;
- source excerpt or source-backed summary;
- observed behavior or pattern;
- NARM concept;
- fusion statement;
- diagnostic-style hypothesis when useful;
- confidence;
- evidence basis;
- contra-evidence or uncertainty;
- therapist-facing question;
- self-exploration prompt seed.

Rules:
- Define the link schema before making links.
- Do not make final links during preparation.
- Every future link must preserve source basis.
- Keep theory, personal evidence, and hypothesis separate.
- Use exploratory language: `may be explored through`, not `is`.
- Do not convert NARM theory labels into diagnosis.
- Prefer fewer high-quality links over broad speculative mapping.
```

# Self-Exploration Flow Prompt

```text
Prepare the self-exploration flow template schema for a later Codex pass.

Do not create final flows yet.

Each future flow must be built from:
- NARM concept;
- personal pattern;
- concrete behavior;
- direct question;
- body noticing;
- agency noticing;
- relationship noticing;
- therapist-prep note.

Required fields:
- flow title;
- intended use;
- source basis;
- entry conditions;
- activation or capacity check;
- NARM concept;
- personal pattern;
- concrete behavior;
- body track;
- agency track;
- relationship track;
- direct questions;
- stop conditions;
- therapist-prep note;
- compact output schema.

Style:
- direct questions, not vague reflective prompts;
- no therapy-replacement framing;
- stop inquiry when activation is high, dissociation/shutdown appears, or PEM/crash risk is elevated;
- output should support later discussion with the NARM therapist.
```

# Directness And Evidence Prompt

```text
Write directly and concretely.

Label each psychological claim as one of:
- raw source;
- source-backed summary;
- behavioral inference;
- diagnostic-style hypothesis;
- operator question;
- therapist question.

Rules:
- Remove vague reassurance.
- Remove generic therapeutic language.
- Do not soften psychologically direct material merely because it is sensitive.
- Do not present diagnostic-style hypotheses as established fact.
- Do not present AI-generated formulation as clinician-confirmed diagnosis.
- Preserve source basis and uncertainty.
- Use therapist-facing questions when a claim needs clinical validation.
```

# Artifact Placement Prompt

```text
Save project-control files under apex-meta.
Save preparation artifacts under apex-meta/artifacts/narm-support-knowledgebase.
Do not write final generated indexes into the Obsidian Therapy folder unless the operator explicitly approves that destination.
Do not build final indexes during the preparation pass.
```

# Later Codex Index-Building Prompt

```text
You are executing the later Codex index-building pass for the NARM-support knowledgebase.

Before writing final indexes:
1. Read apex-meta/artifacts/narm-support-knowledgebase/definitions-of-done.md.
2. Read apex-meta/artifacts/narm-support-knowledgebase/index-artifact-plan.md.
3. Read apex-meta/artifacts/narm-support-knowledgebase/index-validation-questions.md.
4. Read apex-meta/artifacts/narm-support-knowledgebase/source-file-map.md.
5. Read apex-meta/artifacts/narm-support-knowledgebase/workflow-prompts.md.
6. Confirm or resolve operator validation questions that block extraction.

Then build only the approved final indexes, preserving source labels, confidence, and uncertainty.

Do not write to Obsidian unless explicitly approved.
```
