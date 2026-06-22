# Artifact Root

Root path for this preparation pass:

```text
apex-meta/artifacts/narm-support-knowledgebase/
```

This folder contains preparation artifacts only. It does not contain final generated indexes yet.

# Prepared Artifacts

The current pass prepares these files:

| File | Role | Final index? |
|---|---|---|
| `definitions-of-done.md` | Implementation-ready DoD for Tasks 001-006; Tasks 007-008 preserved as later phase | No |
| `index-artifact-plan.md` | Artifact structure, schemas, placement rules, later Codex instructions | No |
| `index-validation-questions.md` | Operator validation questions before full extraction/build | No |
| `source-file-map.md` | Source folder, exact file names, planned roles, ambiguities | No |
| `workflow-prompts.md` | Reusable prompts for preparation and later index-building | No |

# Later Codex-Built Indexes

Later Codex pass may build these artifacts after operator validation:

```text
apex-meta/artifacts/narm-support-knowledgebase/final-indexes/
  narm-theory-index.md
  personal-material-index.md
  narm-personal-fusion-index.md
  self-exploration-flow-templates.md
```

Optional split-file structure, if the operator prefers modular indexes:

```text
apex-meta/artifacts/narm-support-knowledgebase/final-indexes/
  narm-theory/
    00-master-index.md
    core-concepts.md
    developmental-themes.md
    survival-strategies.md
    shame-pride-identifications.md
    somatic-regulation.md
    therapeutic-cautions.md
  personal-material/
    00-master-index.md
    anamnesis.md
    shadow-insights.md
    handover-formulations.md
    relationship-patterns.md
    spiritual-practice-context.md
  fusion/
    00-fusion-map.md
    theory-to-pattern-links.md
    therapist-questions.md
    self-exploration-seeds.md
  flows/
    00-flow-master.md
    anger-grief.md
    betrayal-moral-injury.md
    overgiving-boundaries.md
    recognition-hunger.md
    defensive-arrogance.md
```

Do not build these until the operator confirms destination, granularity, and validation answers.

# NARM Theory Index Plan

## Purpose

Prepare a later source-backed index of `ET-Heller-NARM.md` that can support therapy preparation, self-reflection, and later fusion with personal material.

## Source-To-Index Process

```text
source -> chunks -> categories -> questions -> recommendations -> operator validation -> later extraction
```

## Theory Entry Schema

```yaml
record_id: narm_theory_<slug>
source_type: narm_primary_theory
source_file: ET-Heller-NARM.md
source_pointer: "chapter/section/page/line when available"
source_excerpt_policy: "short excerpt or pointer, pending operator decision"
category:
  - core_concept
  - developmental_theme
  - survival_strategy
  - shame_pride_identification
  - self_regulation
  - somatic_mindfulness
  - agency_connection_aliveness
  - therapeutic_caution
narm_concept: ""
source_backed_summary: ""
quotable_definition: "optional; short only"
therapeutic_caution: ""
possible_personal_link_candidates: []
extraction_confidence: low | medium | high
open_questions: []
```

## Proposed Top-Level Categories

- NARM core concepts.
- Developmental themes.
- Five biological core needs.
- Five adaptive survival strategies.
- Connection, agency, contact, and aliveness.
- Self-regulation and affect regulation.
- Somatic mindfulness and body-based attention.
- Shame-based identifications and pride-based counteridentifications.
- Protest, anger, collapse, compliance, withdrawal, disconnection, and distorted life-force patterns when source-supported.
- Therapist cautions and non-pathologizing framing.
- Quotable/source-backed definitions.
- Links-to-personal-material candidates.

## Chunking Rules For Later Extraction

- Chunk by semantic section, not arbitrary token length, when possible.
- Preserve chapter/section headings.
- Keep tables as structured records, not prose-only summaries.
- Keep visual/table content separate when the source includes diagrams or tabular structures.
- Do not merge a clinical caution with a personal interpretation.
- Create one record per concept when a chunk contains multiple distinct concepts.
- Mark ambiguous concepts with `extraction_confidence: low` and add an operator question.

## Recommendations Before Full Extraction

- Use one theory master index first, then split into modules only if the result becomes hard to navigate.
- Require source pointers for every theory claim.
- Do not infer personal relevance in the theory index; store only `possible_personal_link_candidates`.

# Personal Material Index Plan

## Purpose

Prepare a later index of personal psychological material that distinguishes raw self-report, AI-generated formulation, spiritual practice context, behavioral inference, and therapist-facing questions.

## Personal Entry Schema

```yaml
record_id: personal_<source_slug>_<slug>
source_type:
  - personal_self_report
  - therapist_form
  - ai_generated_formulation
  - shadow_insight
  - spiritual_framework
  - adjacent_practice_context
source_file: ""
source_pointer: "section/page/heading/line when available"
raw_excerpt_or_pointer: ""
category:
  - raw_excerpt
  - concrete_behavior
  - repeated_relational_pattern
  - emotional_theme
  - self_belief
  - trigger
  - protective_strategy
  - avoidance_pattern
  - collapse_pattern
  - control_pattern
  - compliance_pattern
  - pursuit_pattern
  - withdrawal_pattern
  - protest_pattern
  - therapist_relevant_note
  - unresolved_question
  - diagnostic_style_hypothesis
behavioral_pattern: ""
emotional_theme: ""
relational_context: ""
body_or_activation_context: ""
source_backed_summary: ""
behavioral_inference: ""
diagnostic_style_hypothesis: "optional; labeled; not a diagnosis"
therapist_question: ""
operator_question: ""
confidence: low | medium | high
```

## Proposed Personal Categories

- Current symptoms and constraints.
- PEM/PESE and autonomic dysregulation constraints.
- Anamnesis answers and therapist-facing material.
- Relationship patterns.
- Betrayal/moral-injury/grievance themes.
- Anger, grief, compassion, and self-protection themes.
- Overgiving, non-reciprocity, boundary difficulty.
- Recognition hunger and pressure when offering value.
- Defensive arrogance/inflation under social threat.
- Parent/family safety and early male rejection themes.
- Spiritual-practice context and adjacent frameworks.
- Open clinical questions.

## Recommendations Before Full Extraction

- Treat `Anamnesebogen AGehm.docx` as primary self-report/therapist form.
- Treat shadow insight files as personal self-reflection, not clinical diagnosis.
- Treat psychological handover files as AI-generated formulation unless they contain explicit raw source excerpts.
- Treat spiritual files separately unless the operator confirms they should be merged into psychological material.

# Fusion Model Plan

## Purpose

Define how later artifacts can connect NARM theory to personal material without erasing uncertainty or turning theory labels into diagnosis.

## Fusion Link Schema

```yaml
link_id: fusion_<slug>
theory_source:
  source_file: ET-Heller-NARM.md
  source_pointer: ""
  narm_concept: ""
personal_source:
  source_file: ""
  source_pointer: ""
  raw_excerpt_or_summary: ""
observed_pattern: ""
concrete_behavior: ""
body_or_activation_marker: ""
narm_concept: ""
fusion_statement: "source-backed, hypothesis-labeled"
diagnostic_style_hypothesis: "optional; not a diagnosis"
confidence:
  label: low | medium | high
  numeric: null
confidence_rationale: ""
evidence_basis:
  - raw_source
  - source_backed_summary
  - behavioral_inference
therapist_question: ""
self_exploration_prompt_seed: ""
contra_evidence_or_uncertainty: ""
```

## Fusion Rules

- Every link requires a theory source and personal source.
- Every hypothesis must have a confidence level and therapist-facing question.
- Do not link based on keyword similarity alone.
- Do not diagnose NARM survival structures; use exploratory language.
- Preserve contra-evidence and ambiguity.
- Prefer fewer high-quality links over many speculative links.

## Confidence Recommendation

Use both label and optional numeric score only after operator validation:

```yaml
confidence:
  label: low | medium | high
  numeric: 0-100 optional
```

# Self-Exploration Flow Plan

## Purpose

Prepare later guided self-exploration flow templates that are NARM-derived and grounded in the personal-material index, while remaining non-therapeutic.

## Flow Template Schema

```yaml
flow_id: flow_<slug>
flow_title: ""
source_basis:
  narm_theory_records: []
  personal_material_records: []
intended_use: therapy_preparation | integration | pattern_tracking
not_for: diagnosis | treatment | crisis_intervention
entry_conditions:
  activation_max: "operator-defined"
  physical_capacity_check: true
narm_concept: ""
personal_pattern: ""
concrete_behavior: ""
body_track:
  - "Where is it in the body?"
  - "Does attention increase or decrease activation?"
agency_track:
  - "What do you want for yourself here?"
  - "What choice is available now?"
relationship_track:
  - "What happens between you and the other person/system?"
  - "What boundary or request is clean?"
direct_questions: []
stop_conditions:
  - high_activation
  - crash_risk
  - dissociation_or_shutdown
therapist_prep_note: ""
output_schema:
  trigger: ""
  facts: ""
  interpretations: ""
  body_state: ""
  emotion_surface: ""
  emotion_deeper: ""
  possible_survival_strategy: "hypothesis"
  therapist_question: ""
  next_micro_step: ""
```

## Flow Organization Options

- By NARM concept.
- By personal pattern.
- By current-life situation.
- Hybrid: current-life situation as entry point, NARM concept and personal pattern as metadata.

## Recommendation

Use hybrid organization later. It matches actual usage: the operator will arrive with a current activation or situation, not with a theory category.

# Placement Rules

## Current Preparation Pass

Write only preparation artifacts under:

```text
apex-meta/artifacts/narm-support-knowledgebase/
```

## Later Final Index Pass

Default recommendation:

```text
apex-meta/artifacts/narm-support-knowledgebase/final-indexes/
```

## Obsidian Folder

Do not write generated indexes into:

```text
C:\Quasi Desktop\Leela New 26\Obsidian Leela New 01-26\X None Leela\Health\Therapy
```

unless the operator explicitly approves that destination.

## Repo-First Recommendation

Keep artifacts repo-first until:

- source classification is validated;
- privacy/redaction rules are defined;
- final index granularity is approved;
- operator approves any Obsidian mirror/write.
