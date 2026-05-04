# SOURCE_MANIFEST

## Purpose

Source ledger for the Alfred KB base in `managed/agent_kb/alfred/`.

This file records the source basis for Alfred KB repair after the failed build flow. It is a source-control and coverage surface, not accepted doctrine by itself.

## Repair status

```yaml
agent_id: alfred
kb_root: managed/agent_kb/alfred/
source_phase: pass_a_source_bundle_complete
write_phase_file: managed/agent_kb/alfred/SOURCE_MANIFEST.md
write_scope: single_file_repair
source_repo: leela-spec/MasterOfArts
target_repo: leela-spec/apexai-os-meta
source_bundle: alfred_source_bundle_pass_a.md
current_status: repaired_from_pass_a_source_bundle
previous_status_classification: procedurally_flawed_or_incomplete
validator: meta_ops
next_action: create_or_update managed/agent_kb/alfred/COVERAGE_AUDIT.md
```

## Previous manifest classification

Before this repair, the existing Apex manifest was classified as `procedurally_flawed_or_incomplete` because it:

- stated that the direct source bundle artifact was not present in the write turn,
- relied on existing Apex Alfred KB files as local basis,
- stated Master Of Arts sources were not re-read during the Apex write phase,
- collapsed the many local/manual Night4 sources into one `IDX-N4` cluster,
- did not enumerate every local/manual source from the index with explicit `not_accessible` status.

This replacement uses the completed Pass A source bundle as the source basis and preserves source gaps instead of hardening them into doctrine.

## Source classes

| Class | Meaning | Use rule |
|---|---|---|
| `IDX` | Master Of Arts source index | Governs expected source coverage for this Alfred KB recovery pass. |
| `R` | Repo-accessible Master Of Arts source | May support doctrine only for claims extracted in the source bundle. |
| `M` | Local/manual Windows/Obsidian source listed by the index | Must remain `not_accessible` until directly attached/read in a separate manual-source pass. |
| `BUNDLE` | Pass A source bundle | Source extraction and write-planning bridge; not a substitute for future direct source reads if doctrine changes. |
| `APEX` | Apex repo convention/current file | May guide local file placement and compatibility only; must not substitute for Master Of Arts source reading. |
| `LOCK` | Corrected Apex working lock | May control this canonical patch pass when explicitly listed by the handover; remains working/control material unless compact-promoted. |
| `APPENDIX` | Subordinate Alfred appendix | May hold detail and retrieval support; does not become canonical doctrine merely by existing. |

## Read-status summary

| Category | Count | Status |
|---|---:|---|
| Master Of Arts source index | 1 | fully_read |
| Repo-accessible Master Of Arts sources | 5 | fully_read |
| Local/manual index sources | 40 | not_accessible |
| Apex writes before this file | 0 in Pass A; this file is first write in Pass B | controlled single-file repair |

## Source index

| source_id | path/name | role | required_read_mode | accessible | actual_read_status | notes |
|---|---|---|---|---|---|---|
| IDX | `agent_kb_source_indexes/ALFRED_KB_BASE_BUILD_INDEX.md` | source_index | read full | yes | fully_read | Master Of Arts source index; sha `1a400a47fa35056555c988b73f2c0a121d81e41b`. |

## Repo-accessible Master Of Arts sources

| source_id | path/name | role | required_read_mode | accessible | actual_read_status | sha | doctrine use |
|---|---|---|---|---|---|---|---|
| R01 | `OpenClaw/07_finalopenclawsystem/managed/agents/alfred.md` | primary | read full | yes | fully_read | `fc4014c0d4c7696edcf0d45f553b96034ffc5ceb` | Alfred identity, ownership, handoff contract, and role boundaries. |
| R02 | `OpenClaw/07_finalopenclawsystem/managed/processes/HOLDING_ORCHESTRATION_FLOW.md` | primary | read full | yes | fully_read | `9ac1f1373adb2198922e9143e7df7c67db5abb30` | Intake thresholding, smallest bounded activation, EVD/IMP/RSK, handoff minimums, promotion/hygiene guardrails. |
| R03 | `OpenClaw/04_final-system-setup/NewFinals/AfterProPromptIteration/FirstAgents/Agent_Alfred_GPT.md` | primary | read full | yes | fully_read | `8b1602127b4ce5b2502df705453de0b063e6199f` | Alfred role synthesis, Leela surfaces, Path/Rhythm/Sequencing/Stats/Sid/Algorithm boundaries. |
| R04 | `OpenClaw/04_final-system-setup/NewFinals/AfterProPromptIteration/FirstAgents/Agent_Alfred_Gem.md` | primary | read full | yes | fully_read | `a6b3b667312c846f48a7cdfaf270a299dc818bae` | Steward behavior, day/night concepts, life layer, operator-facing routing. |
| R05 | `OpenClaw/04_final-system-setup/NewFinals/AfterProPromptIteration/Alfred_Use_Case.md` | primary | read full | yes | fully_read | `db16e4841a6638aa05ee6bb6958c7cdce7fdc45a` | First contact, personal priorities, delegation, Meta Ops synchronization. |

## Local/manual sources from the index

These sources were listed by the Master Of Arts index, but are local Windows/Obsidian paths outside repo-accessible Master Of Arts content in this recovery pass. They are not read in Pass A and must not be treated as fully validated doctrine.

| source_id | path/name | role | required_read_mode | accessible | actual_read_status | doctrine area |
|---|---|---|---|---|---|---|
| M01 | `1stContentDevelopmentProcessChat.md` | primary | read full | no | not_accessible | Unified product flow / MVP |
| M02 | `2ndContentDevelopmentProcessChat.md` | primary | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M03 | `2ndContentDevelopmentProcessChat Rhythm.md` | primary | read full | no | not_accessible | Rhythm |
| M04 | `Skill Tree Update N4 v1.md` | primary | read full | no | not_accessible | Skill Tree / Epics / Chunks |
| M05 | `PathUpdatev2.md` | primary | read full | no | not_accessible | Path |
| M06 | `Sequencing SSOT Updatev2.md` | primary | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M07 | `Rhythm SSOT Updatev2.md` | primary | read full | no | not_accessible | Rhythm |
| M08 | `Rhythm_Feature_Screen_Spec.md` | primary | read full | no | not_accessible | Rhythm |
| M09 | `Skill Tree Specs v3.md` | supporting | read full | no | not_accessible | Skill Tree / Epics / Chunks |
| M10 | `Path - Specs & Docs (vSpark Prototype) v5.md` | supporting | read full | no | not_accessible | Path |
| M11 | `SCR_SequenceSelect Specs & Docs v2.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M12 | `SCR_SequenceRun Specs & Docs new.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M13 | `101 - Chunks & Chunk Database.md` | supporting | read full | no | not_accessible | Skill Tree / Epics / Chunks |
| M14 | `102 - Epics (Database + Skill Tree).md` | supporting | read full | no | not_accessible | Skill Tree / Epics / Chunks |
| M15 | `103 - Path.md` | supporting | read full | no | not_accessible | Path |
| M16 | `104 -Rhythm.md` | supporting | read full | no | not_accessible | Rhythm |
| M17 | `105 - Sequencing & Sequencing Template.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M18 | `105 - Sequencing.md` | duplicate | skim | no | not_accessible | Sequencing / Spark / Session / Flow |
| M19 | `101 Chunks & 102 Epics.md` | duplicate | skim | no | not_accessible | Skill Tree / Epics / Chunks |
| M20 | `Sequencing & Science.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M21 | `Sequencing Intertwinement.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M22 | `Sequencing Info.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M23 | `Sequence - Builder, Settings, Details and Examples.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M24 | `Sequence Instant Schema & Example.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M25 | `Sequence Template.md` | supporting | skim | no | not_accessible | Sequencing / Spark / Session / Flow |
| M26 | `Sequence Template DR.md` | supporting | skim | no | not_accessible | Sequencing / Spark / Session / Flow |
| M27 | `Daily Flows.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M28 | `Flows.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M29 | `A day of Sequences.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M30 | `Craft Flows - Holistic Work Sequences.md` | supporting | skim | no | not_accessible | Sequencing / Spark / Session / Flow |
| M31 | `Sequences Extraction 1.md` | evidence | use as evidence only | no | not_accessible | Sequencing / Spark / Session / Flow |
| M32 | `Sequnece Extraction 2.md` | evidence | use as evidence only | no | not_accessible | Sequencing / Spark / Session / Flow |
| M33 | `Learn2Learn Sequences, Epic, Chunks, Personas, Stories.md` | evidence | use as evidence only | no | not_accessible | Sequencing / Spark / Session / Flow |
| M34 | `Learn2Learn Epic - Use Cases and Sequences.md` | evidence | use as evidence only | no | not_accessible | Sequencing / Spark / Session / Flow |
| M35 | `Part 1 Chunks.md` | supporting | skim | no | not_accessible | Skill Tree / Epics / Chunks |
| M36 | `Part 4 Chunks Sequencing & Science.md` | supporting | read full | no | not_accessible | Sequencing / Spark / Session / Flow |
| M37 | `Gamification Research.md` | supporting | skim | no | not_accessible | Gamification / Kharma / Community |
| M38 | `Metric Update - BP & RB.md` | supporting | skim | no | not_accessible | Algorithm / BP / RB |
| M39 | `Leela User Story & Flow Map.md` | supporting | skim | no | not_accessible | Unified product flow / MVP |
| M40 | `Leela MVP User Story & Flow Map.md` | supporting | skim | no | not_accessible | Unified product flow / MVP |

## Extraction ledger pointer

The detailed claim ledger is in `alfred_source_bundle_pass_a.md`, section `EXTRACTION_LEDGER`, claims `C01` through `C19`.

### Stable high-confidence claim clusters

- `C01-C05`: Alfred identity, owns/does-not-own boundaries, and handoff partners.
- `C06-C09`: Holding orchestration, EVD/IMP/RSK, handoff minimums, promotion/hygiene guardrails.
- `C10-C11`: Alfred as first-contact executive aligner distinct from Meta Operations.
- `C16-C18`: Routing to Meta Ops, Strategy, Critic/Detective, and continuous Alfred/Meta Ops synchronization.
- `C19`: Failure modes and anti-drift safeguards.

### Medium-confidence / source-gap-dependent claim clusters

- `C12-C13`: Alfred's interpretation of Leela surfaces and the Path-Rhythm-Sequencing-Stats loop.
- `C14`: Information-design style requirements as applied to Alfred outputs.
- `C15`: day-start/day-close/night-bridge, voice-to-markdown intake, and policy-level tool/model routing details.

These claims may guide provisional Apex scaffolding but must remain gap-marked until the corresponding manual/local sources are read or attached in a separate source-extension pass.

## Process-handover correction ledger

The following Apex files form the source/control basis for the corrected Alfred process-handover patch pass. They supplement the existing source manifest for this bounded patch and do not imply that appendix detail is automatically canonical.

| source_id | path/name | class | role | status | doctrine use |
|---|---|---|---|---|---|
| LOCK-01 | `managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md` | LOCK | corrected decision lock | working_control | Corrects process-handover metric collision; preserves `EVD / IMP / RSK`; adds `URG` only for process handovers; rejects V/U/L/F as canonical. |
| LOCK-02 | `managed/agent_kb/alfred/working/APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md` | LOCK | corrected integration prompt flow | working_control | Blocks V/U/L/F regeneration and routes detail through the process-handover appendix. |
| LOCK-03 | `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md` | LOCK | parent workflow decision lock | working_control | Records resolved workflow questions against corrected priority model. |
| LOCK-04 | `managed/agent_kb/alfred/working/APEX_ALFRED_CANONICAL_PATCH_HANDOVER.md` | LOCK | handover prompt | working_handover | Defines the remaining patch sequence and final consistency gate for compact canonical promotion. |
| APPX-01 | `managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md` | APPENDIX | process-handover priority detail | subordinate_appendix | Detailed source for `EVD / IMP / RSK + URG`, readiness, lane, hard flags, P0-P3, and V/U/L/F rejection. |
| APPX-02 | `managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md` | APPENDIX | Daily Command Board and MetaOps handoff detail | subordinate_appendix | Detailed source for bounded board practice, craft-flow cap, P0 control, and MetaOps handoff shape. |
| APPX-03 | `managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md` | APPENDIX | trace/state/tracking detail | subordinate_appendix | Detailed source for Session Export as trace, OpState delta candidate separation, and minimal tracking. |
| APPX-04 | `managed/agent_kb/alfred/appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md` | APPENDIX | pattern learning and Rhythm profile detail | subordinate_appendix | Detailed source for candidate-first pattern learning, Rhythm profile posture, weekly preview, and monthly direction placeholders. |

### Relationship to `AGENT_HANDOFF_CONTRACTS.md`

`managed/processes/AGENT_HANDOFF_CONTRACTS.md` remains authoritative for first-wave inter-agent handoff contract semantics. Its `EVD / IMP / RSK` handoff model is preserved. The Alfred process-handover extension adds `URG` only for time-sensitive process handovers, Daily Command Board priority, and process-handover routing.

### Relationship to uploaded/manual Alfred, Rhythm, Sequencing, Daily, and Craft Flow source materials

Some uploaded source materials in the wider working context describe Alfred, Rhythm, Sequencing, Daily Flows, and Craft Flows. Unless those materials are directly read and recorded in this manifest during a source-extension pass, they remain outside the validated source ledger for canonical doctrine. They may inform operator-local reasoning but must not be claimed as fully read source evidence here.

## Doctrine-hardening rules

- **Rule:** Repo-accessible source claims may support Alfred KB doctrine only where the source bundle extracted them as stable or where later source reads validate them.
- **Rule:** Local/manual sources `M01-M40` must remain `not_accessible` and cannot be treated as read.
- **Rule:** No single cluster label such as `IDX-N4` may replace enumeration of the local/manual sources.
- **Rule:** Existing Apex KB files may guide local conventions, but must not substitute for Master Of Arts source reading.
- **Rule:** Leela feature details below high-level Alfred synthesis must be marked provisional unless supported by read source material.
- **Rule:** Corrected working locks may guide this bounded patch pass, but their stable content must be compact-promoted into canonical files before it becomes canonical doctrine.
- **Rule:** Subordinate appendices may hold detail; accepted canonical files should remain compact and should not duplicate whole schemas unnecessarily.
- **Rule:** Candidate learning is not accepted truth and must route through `LEARNING_QUEUE.md` or the governed promotion path.
- **Rule:** Any contradiction, inaccessible source, stale source, or overclaimed read status must be carried into `COVERAGE_AUDIT.md`.

## Coverage gaps to preserve

The following areas remain not fully validated from Pass A:

- Skill Tree / Epics / Chunks details
- Path demand, priority, and weekly planning details
- Rhythm capacity, time supply, placement, and four-pane planning details
- Sequencing / Spark / Session / Flow manual entry, ranked recommendation, and template/instance details
- Algorithm / BP / RB / XP ranking mechanics
- Stats and Sid specifics
- Gamification / Kharma / Community details
- unified product flow / MVP details
- day/night protocol mechanics
- 5V framework details
- voice-to-markdown/mobile intake mechanics

## Update boundary

This manifest repair does not create final doctrine. It establishes the source ledger required before writing doctrine-bearing Alfred KB files.

Next required file: `managed/agent_kb/alfred/COVERAGE_AUDIT.md`.
