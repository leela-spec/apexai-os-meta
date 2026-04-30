# SOURCE_MANIFEST

## Purpose

Source ledger for the Alfred KB base in `managed/agent_kb/alfred/`.

This file records which sources informed the current Alfred KB files, how each source should be treated, and where source gaps must remain visible. It is a source-control surface, not accepted doctrine by itself.

## Manifest status

```yaml
manifest_status:
  agent_id: alfred
  kb_root: managed/agent_kb/alfred/
  build_status: apex_side_source_manifest_created
  created_at: 2026-04-30
  owner: alfred
  validator: meta_ops
  next_audit_file: managed/agent_kb/alfred/COVERAGE_AUDIT.md
```

## Source classes

| Class | Meaning | Use rule |
|---|---|---|
| `S` | Master Of Arts source reference used by the Alfred KB synthesis | May support doctrine only when the claim is already present in the verified KB base or later re-read during audit. |
| `A` | Apex AI repo source or convention reference | May support local Apex scaffold, ownership, naming, and compatibility decisions. |
| `IDX` | Source-index or gap-derived reference | May identify intended source coverage, but must not be represented as fully read doctrine. |
| `LOCAL_MANUAL_GAP` | Local/manual source named by an index but not accessible in the write turn | Must remain explicit in this manifest and in `COVERAGE_AUDIT.md`. |

## Source ledger

| ID | Source | Role | Current treatment | Candidate outputs informed | Notes |
|---|---|---|---|---|---|
| `S0` | `leela-spec/MasterOfArts/agent_kb_source_indexes/ALFRED_KB_BASE_BUILD_INDEX.md` | primary index | index authority for expected Alfred source coverage | all Alfred KB files | The index is treated as the source-map basis; unresolved source-access gaps route to `COVERAGE_AUDIT.md`. |
| `S1` | `leela-spec/MasterOfArts/OpenClaw/07_finalopenclawsystem/managed/agents/alfred.md` | primary seed | source-reference carried by existing Alfred KB files | `AGENT_CARD.md`, `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | Establishes Alfred identity, boundaries, and routing role. |
| `S2` | `leela-spec/MasterOfArts/OpenClaw/07_finalopenclawsystem/managed/processes/HOLDING_ORCHESTRATION_FLOW.md` | supporting process source | source-reference carried by existing Alfred KB files | `AGENT_CARD.md`, `BEST_PRACTICES.md`, `TEMPLATES.md` | Supports route-ready handoff and orchestration-flow boundaries. |
| `S3` | `leela-spec/MasterOfArts/OpenClaw/04_final-system-setup/NewFinals/AfterProPromptIteration/FirstAgents/Agent_Alfred_GPT.md` | primary Alfred behavior source | source-reference carried by existing Alfred KB files | all doctrine and template files | Supports first-contact alignment, route framing, and recommendation behavior. |
| `S4` | `leela-spec/MasterOfArts/OpenClaw/04_final-system-setup/NewFinals/AfterProPromptIteration/FirstAgents/Agent_Alfred_Gem.md` | parallel Alfred behavior source | source-reference carried by existing Alfred KB files | `AGENT_CARD.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | Supports cross-model Alfred consistency and Leela-ladder framing. |
| `S5` | `leela-spec/MasterOfArts/OpenClaw/04_final-system-setup/NewFinals/AfterProPromptIteration/Alfred_Use_Case.md` | applied use-case source | source-reference carried by existing Alfred KB files | `AGENT_CARD.md`, `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | Supports operational examples, day/week alignment, and recommendation boundaries. |
| `A1` | `leela-spec/apexai-os-meta/managed/agents/alfred.md` | Apex seed reference | local Apex seed pointer | `AGENT_CARD.md`, folder identity, scaffold compatibility | Used to keep the KB root aligned with the Apex agent seed surface. |
| `A2` | `leela-spec/apexai-os-meta/managed/agent_kb/AGENT_KB_INDEX.md` | Apex KB convention source | local convention reference | naming, file set, validator, promotion routing | Used for scaffold compatibility and agent-KB placement. |
| `IDX-N4` | Night4/local/manual product sources referenced by Alfred synthesis | gap/source-index cluster | index-derived only unless later directly accessible | Path/Rhythm/Sequencing/Algorithm/Stats/Sid claims | Must remain visibly marked as local/manual or inferred. Do not harden as fully read doctrine. |

## Apex KB files verified as local basis

| File | Role in this manifest | Source-relevant observations |
|---|---|---|
| `AGENT_CARD.md` | source-basis anchor | Lists the Alfred source IDs and Apex pointers; establishes KB root, seed pointer, validator, and handoff partners. |
| `ESSENCE.md` | doctrine anchor | Points to `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md`; preserves accepted compact boundary doctrine. |
| `BEST_PRACTICES.md` | source-to-practice ledger | Carries evidence refs per practice and marks `IDX-N4` as not directly accessible where relevant. |
| `MISTAKES.md` | source-gap protection | Contains the explicit hidden-source-gap failure pattern and requires source gaps to be recorded here and in coverage audit. |
| `TEMPLATES.md` | reusable-output source ledger | Carries evidence refs for first-contact, weekly alignment, day-start, rhythm repair, handoff, and escalation templates. |
| `LEARNING_QUEUE.md` | candidate-only learning intake | Confirms learning entries are not runtime truth and must route through governed promotion. |

## Access and confidence rules

- **Rule:** Claims supported only by `IDX-N4` or other local/manual references must be marked as `index-derived`, `inferred`, or `needs_validation` unless a later audit directly reads the source.
- **Rule:** Alfred doctrine may use stable source synthesis already present in the verified KB base, but later substantive changes require source review or a `LEARNING_QUEUE.md` candidate.
- **Rule:** This manifest does not promote new truth. It records the source status behind the current KB base.
- **Rule:** Any contradiction, inaccessible source, stale source, or overclaimed read status must be carried into `COVERAGE_AUDIT.md`.

## Known source gaps

| Gap ID | Gap | Impact | Required handling |
|---|---|---|---|
| `GAP-001` | Direct source bundle artifact was not present in this single-file write turn. | Manifest relies on verified existing Apex Alfred KB files for source IDs and source-gap semantics. | Treat as a coverage-audit note, not as a blocker to creating the Apex-side manifest. |
| `GAP-002` | Night4/local/manual product sources behind `IDX-N4` were not directly readable in this write turn. | Product-specific Path, Rhythm, Sequencing, Algorithm, Stats, and Sid details may be incomplete. | Mark related claims as inferred/index-derived and audit them before any future promotion. |
| `GAP-003` | Master Of Arts sources were not re-read during this Apex write phase. | Source ledger reflects prior synthesis and current KB evidence refs rather than a fresh extraction pass. | Re-read Master Of Arts only if `COVERAGE_AUDIT.md` or future change work requires it. |

## Promotion and update boundary

- Source updates are candidates until validated.
- Learning entries go to `LEARNING_QUEUE.md`.
- Coverage failures go to `COVERAGE_AUDIT.md`.
- Accepted doctrine changes must route through the governed promotion path.
- This file may be updated without doctrine change when a source becomes newly accessible, deprecated, contradicted, or superseded.
