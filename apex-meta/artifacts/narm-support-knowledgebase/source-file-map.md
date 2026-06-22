# Source Folder

Operator source folder to preserve exactly:

```text
C:\Quasi Desktop\Leela New 26\Obsidian Leela New 01-26\X None Leela\Health\Therapy
```

This preparation pass does not read, extract, or index the source-file contents. It only preserves file names and maps planned roles.

# Source Files

| Exact file name | Initial classification | Planned role | Evidence weight | Ambiguity |
|---|---|---|---|---|
| `ET-Heller-NARM.md` | NARM primary theory | Source for NARM theory index | High for NARM concepts; not personal evidence | Check duplicate/source-version handling if multiple copies exist |
| `Anamnesebogen AGehm.docx` | Therapist form / personal self-report | Source for personal-material index; current symptoms, goals, history, relationship themes | High for self-report | Convert to Markdown before later indexing? |
| `Psychological_Handover_Medical_Grade_v1.md` | AI-generated or structured clinical-style formulation | Source for personal-material index with secondary-evidence label | Medium; formulation depends on source basis | Confirm whether it contains raw excerpts or only synthesized interpretation |
| `PsychologicalHandover_ChatTherapeuticFramework_inACIM.md` | AI-generated therapeutic/spiritual framework | Source for personal-material index or adjacent framework | Medium-low unless raw self-report is embedded | Confirm whether primary role is psychological formulation, ACIM/spiritual integration, or both |
| `shadow_insight_v1.md` | Shadow insight / personal self-reflection | Personal-material source for anger/grief and emotional integration patterns | High for self-reported insight | None known |
| `shadow_insight_v2.md` | Shadow insight / personal self-reflection | Personal-material source for recognition hunger and offering/pressure dynamics | High for self-reported insight | None known |
| `shadow_insight_v3.md` | Shadow insight / personal self-reflection | Personal-material source for defensive arrogance/inflation under social threat | High for self-reported insight | None known |
| `ManifestationHowTo.md` | Adjacent practice context | Optional spiritual/practice context; not primary clinical evidence unless operator confirms | Low-medium | Decide whether to include in psychological index or keep separate |
| `MyTherapy.md` | Personal therapy material | Candidate source for therapy goals, relationship pattern notes, and open questions | Unknown until inspected | Role ambiguous; needs source inspection later |
| `Notion_Surrender_Page.md` | Spiritual/emotional regulation practice context | Optional surrender/Hawkins regulation-context source | Low-medium | Decide whether to include in psychological index or separate practice-context index |

# Planned Roles

## NARM Primary Theory

- `ET-Heller-NARM.md`

Use only for source-backed NARM theory concepts, definitions, cautions, and possible link candidates. Do not use it as direct evidence about the operator.

## Therapist Form / Direct Self-Report

- `Anamnesebogen AGehm.docx`

Use as high-weight personal self-report and therapist-facing baseline. Preserve exact answers and avoid converting them into diagnosis.

## Personal Shadow Insight Sources

- `shadow_insight_v1.md`
- `shadow_insight_v2.md`
- `shadow_insight_v3.md`

Use as self-reported insight records. They can support behavioral inferences and therapist questions when clearly labeled.

## AI-Generated Formulation Sources

- `Psychological_Handover_Medical_Grade_v1.md`
- `PsychologicalHandover_ChatTherapeuticFramework_inACIM.md`

Use as secondary formulation material. Require source labels to prevent treating AI synthesis as raw fact or clinician-confirmed diagnosis.

## Adjacent Spiritual / Practice Context

- `ManifestationHowTo.md`
- `Notion_Surrender_Page.md`

Use only as adjacent context unless operator approves inclusion in the main personal-material index.

## Ambiguous Personal Therapy Source

- `MyTherapy.md`

Needs later inspection/classification before final indexing.

# Missing Or Ambiguous Roles

| File | Ambiguity | Decision needed |
|---|---|---|
| `ManifestationHowTo.md` | May be manifestation/spiritual practice rather than psychological evidence | Include in main personal index, adjacent context, or exclude from first pass? |
| `Notion_Surrender_Page.md` | May support surrender/emotional regulation but is not NARM theory | Include as practice context or keep separate? |
| `MyTherapy.md` | Unknown exact contents | Inspect later and classify by sections |
| `Psychological_Handover_Medical_Grade_v1.md` | Medical-grade title may imply authority; actual source basis may be self-report/AI synthesis | Label as AI-generated formulation unless proven otherwise |
| `PsychologicalHandover_ChatTherapeuticFramework_inACIM.md` | Mixed therapeutic and spiritual framing | Separate ACIM/spiritual lens from psychological claims |

# Relationship-Pattern Source Candidates

Primary candidates:

- `Anamnesebogen AGehm.docx`
- `Psychological_Handover_Medical_Grade_v1.md`
- `PsychologicalHandover_ChatTherapeuticFramework_inACIM.md`
- `shadow_insight_v1.md`
- `shadow_insight_v2.md`
- `shadow_insight_v3.md`
- `MyTherapy.md`

Possible relationship-pattern categories for later extraction:

- non-reciprocity;
- overgiving;
- high expectation after unspoken or weakly contracted giving;
- betrayal or moral-injury activation;
- grievance loop;
- anger protecting grief;
- recognition hunger;
- pressure while offering value;
- defensive arrogance under social threat;
- relational safety and trust baseline;
- sexuality/love/relationship integration themes;
- boundary timing and exit timing.

# Source Classification Schema

```yaml
source_file: "exact file name"
source_path: "operator source folder + exact file name"
source_type:
  - narm_primary_theory
  - therapist_form
  - personal_self_report
  - shadow_insight
  - ai_generated_formulation
  - spiritual_framework
  - adjacent_practice_context
  - ambiguous_pending_review
planned_indexes:
  - narm_theory_index
  - personal_material_index
  - fusion_index
  - self_exploration_flow_seed_index
evidence_weight: high | medium | low | unknown
classification_status: proposed | confirmed | needs_review
operator_questions: []
```

# Artifact Destination Recommendation

Keep generated artifacts repo-first under:

```text
apex-meta/artifacts/narm-support-knowledgebase/
```

Do not write generated index files into the Obsidian Therapy folder until the operator explicitly approves the destination and redaction rules.
