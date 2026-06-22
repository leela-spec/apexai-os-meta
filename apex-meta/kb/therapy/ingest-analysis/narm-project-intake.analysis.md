# NARM Project Intake Analysis

```yaml
ingest_analysis:
  analysis_id: "therapy-narm-project-intake"
  kb_slug: "therapy"
  source_slug: "narm-project-intake"
  created_at: "2026-06-22T00:00:00Z"
  created_by: "apex-kb first repo-backed test run"
  phase: ingest_phase_1
  status: operator_review_needed
  required_halt_after_completion: true
  phase_2_requires_operator_phrase: "approve ingest"
  write_scope:
    allowed_path: "apex-meta/kb/therapy/ingest-analysis/"
    phase_2_not_performed: true
```

## 1. Purpose

Create the first source-preserving intake and process packet for the NARM-support reflection knowledgebase.

This artifact does not compile the final wiki. It prepares the project intake, source map, evidence labels, first concept candidates, and Phase 2 questions.

## 2. Source Basis

```yaml
source_basis:
  epic:
    path: "apex-meta/epics/narm-support-knowledgebase/epic.md"
    role: "project goal, scope, constraints, named source files"
  raw_notes:
    root: "apex-meta/kb/therapy/raw/notes/"
    sampled_sources:
      - source_slug: "et-heller-narm"
        path: "apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md"
        role: "NARM theory source"
      - source_slug: "psychological-handover-medical-grade-v1"
        path: "apex-meta/kb/therapy/raw/notes/Psychological_Handover_Medical_Grade_v1.md"
        role: "personal working formulation / self-report synthesis"
      - source_slug: "psychologicalhandover-chattherapeuticframework-inacim"
        path: "apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md"
        role: "personal working formulation / spiritual frame"
      - source_slug: "shadow-insight-v1"
        path: "apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md"
        role: "anger-to-grief insight"
      - source_slug: "mytherapy"
        path: "apex-meta/kb/therapy/raw/notes/MyTherapy.md"
        role: "process-design and integration framing"
```

## 3. Clinical / Reflective Boundary

```yaml
boundary:
  intended_use:
    - self-reflection organization
    - preparation for sessions with a qualified practitioner
    - source-preserving pattern review
    - question generation
  not_intended_use:
    - diagnosis
    - treatment plan
    - emergency guidance
    - replacement for professional care
  claim_label_policy:
    required_labels:
      - raw_source
      - source_backed_summary
      - behavioral_inference
      - working_hypothesis
      - operator_question
      - practitioner_question
```

## 4. First Source-Backed Intake Summary

### 4.1 NARM theory anchor

**Label:** source_backed_summary

The NARM source presents NARM as a somatically grounded model for working with developmental trauma, emphasizing self-regulation, identity, self-esteem, relational capacity, and five biological core needs: contact, attunement, trust, autonomy, and love/sexuality.

### 4.2 Personal working formulation anchor

**Label:** source_backed_summary

The personal handover sources repeatedly describe a pattern around betrayal, exclusion, moral injury, non-reciprocity, narrative distortion, and anger-based protection. The central formulation is that ethical sensitivity may become fused with trauma charge, rumination, responsibility inflation, and a drive to correct the social field.

### 4.3 Anger-to-grief anchor

**Label:** source_backed_summary

The shadow insight material identifies anger, frustration, and irritation as surface states that may protect grief, sadness, vulnerability, and blocked self-compassion.

## 5. Candidate Concept Pages for Phase 2

```yaml
candidate_concept_pages:
  narm_theory:
    - slug: "five-core-needs"
      title: "Five Core Needs"
      source_basis:
        - "ET-Heller-NARM.md"
    - slug: "adaptive-survival-strategies"
      title: "Adaptive Survival Strategies"
      source_basis:
        - "ET-Heller-NARM.md"
    - slug: "self-regulation-and-relationship-capacity"
      title: "Self-Regulation and Relationship Capacity"
      source_basis:
        - "ET-Heller-NARM.md"
  personal_patterns:
    - slug: "moral-injury-and-betrayal-pattern"
      title: "Moral Injury and Betrayal Pattern"
      source_basis:
        - "Psychological_Handover_Medical_Grade_v1.md"
        - "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md"
        - "MyTherapy.md"
    - slug: "anger-as-protector-of-grief"
      title: "Anger as Protector of Grief"
      source_basis:
        - "shadow_insight_v1.md"
        - "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md"
    - slug: "builder-rescuer-to-selector-gatekeeper"
      title: "Builder / Rescuer to Selector / Gatekeeper"
      source_basis:
        - "Psychological_Handover_Medical_Grade_v1.md"
  fusion_links:
    - slug: "trust-autonomy-and-non-reciprocity"
      title: "Trust, Autonomy, and Non-Reciprocity"
      label: "working_hypothesis"
    - slug: "contact-attunement-and-exclusion-threat"
      title: "Contact, Attunement, and Exclusion Threat"
      label: "working_hypothesis"
```

## 6. First Process Design for the NARM Project

```yaml
narm_project_process:
  phase_1_intake:
    goal: "Create source map, boundary rules, first concept candidates, and review questions."
    output: "ingest-analysis/narm-project-intake.analysis.md"
    status: completed_for_initial_sample
  phase_2_compile_after_gate:
    requires_exact_operator_phrase: "approve ingest"
    intended_outputs:
      - "wiki/concepts/five-core-needs.md"
      - "wiki/concepts/adaptive-survival-strategies.md"
      - "wiki/concepts/moral-injury-and-betrayal-pattern.md"
      - "wiki/concepts/anger-as-protector-of-grief.md"
      - "wiki/summaries/narm-theory-summary.md"
      - "wiki/summaries/personal-pattern-summary.md"
      - "wiki/summaries/fusion-hypotheses-summary.md"
  phase_3_query_and_session_prep:
    intended_outputs:
      - "outputs/queries/session-prep-brief.md"
      - "outputs/queries/practitioner-questions.md"
      - "outputs/queries/self-exploration-prompts.md"
```

## 7. Operator Review Questions

```yaml
operator_review_questions:
  - id: Q1
    question: "Should Phase 2 compile only NARM theory first, or NARM theory plus personal pattern pages together?"
    default_recommendation: "Compile NARM theory and personal pattern summaries separately, then create fusion pages only after review."
  - id: Q2
    question: "Should fusion pages use the label working_hypothesis by default?"
    default_recommendation: true
  - id: Q3
    question: "Should personal material pages preserve stronger/direct language from the source notes, or normalize into practitioner-facing language?"
    default_recommendation: "Preserve direct language in source-backed sections; use practitioner-facing language in summary sections."
  - id: Q4
    question: "Should outputs avoid all external links and external sharing actions by policy?"
    default_recommendation: true
```

## 8. Phase Gate

Phase 2 wiki page generation is intentionally not performed in this artifact.

Required continuation phrase:

```text
approve ingest
```
