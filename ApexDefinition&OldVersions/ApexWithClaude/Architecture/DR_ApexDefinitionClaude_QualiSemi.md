# 00_SYSTEM_INTENT.md

## Zweck des Vorbereitungs-Repos

Das Ziel ist **ein einziges kanonisches Claude-first Repository** für das Apex / Alfred Orchestration System. Dieses Repo ist nicht die Laufzeit selbst, sondern der **stabile, versionierte Vorbereitungsraum** für Instruktionen, Rollenentwürfe, Skill-Skelette, Artefaktverträge, Templates, Beispiele, Register, Quellenkarten und Entscheidungen, damit Claude Code später konsistent daraus bauen kann. Die offizielle Claude-Code-Dokumentation trennt dabei ausdrücklich zwischen immer geladenem Projektkontext in `CLAUDE.md` und bei Bedarf geladenen Skills in `SKILL.md`; genau diese Trennung ist für dieses Repo die Leitplanke. citeturn5view0turn11view1turn11view0

Die aktuelle interne Vorbereitung bestätigt denselben Fokus: vorhandenes Apex-Material soll **übersetzt**, nicht blind kopiert werden; Meta-Agenten-Material gehört in Rollen-/Soul-Drafts, prozedurales Material in Skill-Drafts, und Workflow-Beispiele bleiben Referenzmaterial. fileciteturn0file17 fileciteturn0file18

## Systemrolle und kanonisches Modell

**Alfred** ist der Kern-Orchestrator. Alfred ist nicht bloß eine Chat-Oberfläche, sondern trägt Intake-Kontinuität, Sequenzierung, Übergabe-Rahmung und den Eintritt in die tägliche und wöchentliche Schleife. Die drei unterstützenden Köpfe bleiben fest: **MetaStrategist** für Priorisierung und Hebel, **MetaOperations** für Prozessarchitektur, Artefakte, Routing und Build-Sequenz, sowie **MetaDetectiveController** für No-Drift-Prüfung, Widerspruchserkennung und Abnahme. Dieses Vierer-Modell ist sowohl im aktuellen Entscheidungsstand als auch in der Stage-0-Build-Pack-Logik ausdrücklich festgeschrieben. fileciteturn0file1 fileciteturn0file14

Das kanonische Kernloop-Modell bleibt:

```yaml
canonical_loop:
  - PreCapWeek
  - PreCapNextDay
  - OperatorExecutesPlannedFlow
  - FlowRecapSkill
  - AllProjectStatusPacketUpdate
  - PreCapNextDay_next_cycle
```

Diese Reihenfolge wird in den aktuellen Informationsflussdokumenten als Architektur und nicht nur als Empfehlung beschrieben. Zugleich sind `DayExecution`, `FlowExecution` und `DayExecutionController` aus dem Kernmodell entfernt; `RecapDay` ist ausdrücklich auf später verschoben und nicht Teil des verpflichtenden Kernloops. fileciteturn0file11 fileciteturn0file12 fileciteturn0file14

## Feste Prozessstruktur

Die tägliche Struktur bleibt auf vier feste Flows mit drei Sprints je Flow festgelegt:

```yaml
daily_flow_structure:
  F1: Leela
  F2: MasterOfArts
  F3: Apex_or_Alfred_orchestration
  F4: Residual

every_flow:
  S1: first_work_sprint
  S2: second_work_sprint
  S3: recap_planning_digest_sprint
```

Diese Struktur ist sowohl in der Detailarchitektur als auch im Überblicksdokument fest verankert. Der Operator bleibt die Ausführungsschicht; das System plant, rahmt, rekapituliert und verdichtet Status, führt die eigentliche Arbeit aber nicht autonom aus. fileciteturn0file11 fileciteturn0file12 fileciteturn0file18

## Was das Repo enthalten soll

Das Repo soll nur die **Claude-first Vorbereitungsoberfläche** enthalten:

- globalen Projektspeicher in `CLAUDE.md`
- formale Rollen-/SOUL-Drafts für Alfred und die drei Meta-Heads
- Skill-Skelette und Skill-nahe Vorlagen
- Artefaktvertragsregister
- Ziel-Dateibaum und Build-Reihenfolge
- Templates für Pläne, Flow-Pakete, Recaps, Status- und Handoff-Pakete
- Beispiele aus realen Flow-Situationen
- Register für konsumierte Recaps, Skips, Modellnutzung und Quellenaufnahme
- knappe Architektur- und Konvertierungsdokumente

Diese Aufteilung entspricht sowohl der offiziellen Lade- und Erweiterungslogik von Claude Code als auch der internen Vorübersetzung vorhandener Apex-Dateitypen in Claude-Primitiven. citeturn5view0turn11view1turn11view2turn11view3 fileciteturn0file17

## Was das Repo ausdrücklich nicht enthalten soll

In dieser Phase gehört **nicht** hinein:

- Produktions- oder Deployment-Planung
- Docker, Kubernetes, CI/CD oder Cloud-Infrastruktur
- finale Hermes-Laufzeitfiles
- finale `SKILL.md`-Implementierungen
- finale `SOUL.md`-Implementierungen
- aktive Cron-Jobs, aktive Kanban-Graphen oder Runtime-Installation
- Sicherheits- oder Observability-Operations
- ausführbare Produktionslogik

Der interne Build-Pack-Stand markiert diese Dinge ausdrücklich als außerhalb des aktuellen Scopes; die Claude-Code-Dokumentation unterstützt dieselbe Trennung, indem sie `CLAUDE.md`, Skills, Regeln und Subagents als Konfiguration und Arbeitsoberfläche beschreibt, nicht als Produktions-Deployment-Plan. fileciteturn0file14 citeturn5view0turn11view1turn11view2

## Erfolgsdefinition für den späteren Claude-Code-Build

Der spätere Claude-Code-Build ist erfolgreich, wenn er **nicht alles auf einmal baut**, sondern zuerst den Repo-Spine sauber anlegt, dann Rollen-/SOUL-Drafts, dann Skill-Skelette, danach Templates und Artefaktverträge und erst zuletzt Beispiele und Validierung. Das ist konsistent mit der offiziellen Empfehlung, klein zu starten, `CLAUDE.md` knapp zu halten, prozedurale Inhalte in Skills auszulagern und Skills nur bei Bedarf zu laden. citeturn5view0turn11view1turn12view0turn19view0turn20view1

Praktisch heißt Erfolg in dieser Phase daher:

```yaml
success_definition:
  - one_canonical_repo_exists_as_preparation_surface
  - Alfred_plus_three_heads_are_locked_and_not_reinterpreted
  - canonical_loop_is_preserved
  - removed_models_are_not_revived
  - artifacts_have_macro_contracts
  - repo_tree_is_proposed_but_not_overclaimed_as_runtime
  - only_missing_build_blockers_remain_open
  - Claude_Sonnet_can_read_the_package_and_build_in_stages
```

Diese Erfolgsdefinition folgt direkt aus dem aktuellen Architekturstand, dem internen Phase-1-Konvertierungsschema und den offiziellen Claude-Code-Prinzipien zu Memory, Skills und schrittweiser Projekterweiterung. fileciteturn0file11 fileciteturn0file14 fileciteturn0file17 fileciteturn0file18 citeturn5view0turn11view0turn11view1

# 01_SOURCE_MAP.md

## Priorisierte Quellenordnung

Für diese Phase gilt eine **Claude-docs-first, current-source-over-old-source**-Logik. Offizielle Claude-Code-Dokumentation ist für Repo-Struktur, `CLAUDE.md`, Skills, `.claude/` und Subagents maßgeblich; die Agent-Skills-Spezifikation ist für portable `SKILL.md`-Mindestanforderungen maßgeblich; aktuelle Apex/Alfred-Entscheidungs- und Prozessdateien definieren das fachliche Systemmodell. Ältere Hermes/OpenCLAW- oder Index-Dokumente bleiben Hintergrundmaterial, aber nicht Primärquelle für diese Repo-Vorbereitung. citeturn5view0turn11view0turn11view1turn11view2turn11view3turn19view0 fileciteturn0file1 fileciteturn0file11 fileciteturn0file14

| Priorität | Quellenkategorie | Wofür sie in dieser Phase verwendet wird | Konfliktstatus |
|---|---|---|---|
| P1 | Offizielle Claude Code Docs | `CLAUDE.md`, `.claude/`, Skills, Commands, Subagents, Ladeverhalten, Kontextkosten | höchste Autorität für Claude-first Repo-Mechanik citeturn5view0turn11view0turn11view1turn11view2turn11view3 |
| P2 | Offizielle Agent Skills Spezifikation | portables `SKILL.md`-Minimum, Verzeichnisstruktur, Progressive Disclosure, `references/`, `assets/` | höchste Autorität für offenen Skill-Standard citeturn18view0turn19view0turn19view2turn19view3 |
| P3 | `ClaudeSetupGeneral.md` | Übersetzung vorhandener Apex-Dateitypen in Claude-Primitiven; Repo noch nicht vorhanden; Claude-first Vorbereitung | aktuelle projektnahe Übersetzungshilfe fileciteturn0file18 |
| P4 | `ClaudePhase1FilePreparation.md` | konkrete Konvertierungsheuristik für SOUL/Skill/Examples/Templates und Namenskonventionen | aktuelle Konvertierungshilfe, aber nicht letzte Wahrheit über Repo-Pfade fileciteturn0file17 |
| P5 | aktuelle Apex/Alfred-Entscheidungs- und Prozessdateien | Rollen, Kernloop, Artefakte, Blocker, tägliche Flow-Struktur | höchste Autorität für fachliche Systemlogik fileciteturn0file1 fileciteturn0file11 fileciteturn0file12 |
| P6 | Review-Dateien zu PreCapNextDay, APSU, FlowRecap, Routing, Model Usage | nur offene Blocker, fehlende Pfade, fehlende Variablen, ungelöste Handoffs | maßgeblich für Build-Fragen, nicht für neue Architektur-Erfindungen fileciteturn0file4 fileciteturn0file5 fileciteturn0file6 fileciteturn0file9 fileciteturn0file10 |
| P7 | ältere Architektur-, Workflow- und Index-Dateien | Hintergrund, Handoff-Logik, Quelleninventar, spätere Skill-/Handoff-Kandidaten | nur sekundär, wenn aktuellere Quellen nichts sagen fileciteturn0file15 |

## Verwendungsregeln je Quellentyp

| Quellentyp | Verwenden für | Nicht verwenden für |
|---|---|---|
| Claude Code Docs | Entscheidung über `CLAUDE.md`, `.claude/settings.json`, `.claude/skills/`, `.claude/commands/`, `.claude/agents/`, Rules, Skill-Ladeverhalten | Rekonstruktion des Apex-Fachmodells citeturn5view0turn11view0turn11view1turn11view2turn11view3 |
| Agent Skills Spec | Mindestformat und portable Skill-Struktur | Claude-spezifische Erweiterungen wie `disable-model-invocation`, `context: fork`, Claude-spezifische Commands-Merge-Logik citeturn19view0 |
| `ClaudeSetupGeneral.md` / `ClaudePhase1FilePreparation.md` | Übersetzung vorhandener Agent-/Routine-/Example-Dateien in Claude-kompatible Doku-Familien | endgültige Entscheidung über Claude-native `.claude/skills/`-Pflicht oder finale Runtime-Struktur fileciteturn0file17 fileciteturn0file18 |
| aktuelle Entscheidungs-/Loop-Dateien | Rollen, Schleife, Artefakte, Deprications, Flow-Struktur | Claude-spezifische Tool- oder Konfigurationssemantik fileciteturn0file1 fileciteturn0file11 fileciteturn0file12 |
| Review-Dateien | nur Blocker und fehlende Entscheidungen | normative Architektur, sofern neuere Kernquellen schon etwas locken fileciteturn0file4 fileciteturn0file5 fileciteturn0file6 fileciteturn0file9 fileciteturn0file10 |

## Konfliktauflösung

```yaml
conflict_resolution:
  - official_claude_docs_over_any_older_runtime_assumption
  - agent_skills_spec_over_homegrown_skill_format_when_portability_is_the_question
  - current_project_decisions_over_older_architecture_notes
  - current_loop_docs_over_superseded_dayexecution_models
  - review_notes_raise_blockers_but_do_not_unlock_new_architecture_by_themselves
  - if_two_current_sources_conflict:
      choose_more_specific_source_for_the_topic
```

Beispiele dafür sind klar dokumentiert: Claude Code empfiehlt `CLAUDE.md` für immer nötige Regeln, Skills für wiederverwendbares Referenzmaterial und invokierbare Workflows, sowie `.claude/rules/` für pfadbezogene Regeln; zugleich sagen die internen Apex-Dateien, dass wiederholbare Verfahren Skills und Templates werden sollen und nicht neue Agenten/Profile. citeturn5view0turn11view1turn12view0 fileciteturn0file1 fileciteturn0file14

## Claude-docs-over-Hermes-runtime-Regel für diese Phase

Für **diese** Vorbereitungsphase gilt ausdrücklich:

```yaml
phase_rule:
  portable_skill_minimum: Agent_Skills_spec
  claude_repo_mechanics: Claude_Code_docs
  apex_domain_truth: latest_uploaded_apex_documents
  hermes_runtime_details: background_only_unless_explicitly_needed_later
```

Der Grund ist einfach: Das Ziel ist jetzt kein Hermes-Runtime-Plan, sondern ein **Claude-first Repo-Vorbereitungs-Paket**. Offizielle Claude-Dokumentation definiert, wie Projektkontext, Skills, Subagents und `.claude/` tatsächlich von Claude Code gelesen werden; Hermes-/OpenCLAW-Hintergrund darf dieses Mechanikmodell in dieser Phase nicht überschreiben. citeturn5view0turn11view0turn11view1turn11view2turn11view3 fileciteturn0file14

## Umgang mit älteren oder indirekten Repo-Quellen

Die ausgewählten GitHub-Repositories `leela-spec/MasterOfArts` und `leela-spec/apexai-os-meta` sind in den aktuellen Entscheidungsdateien als relevante Repo-Oberflächen referenziert, etwa über `managed/agents/AGENT_INDEX.md`, `AGENT_SWARM_INTERACTION_CANON.md` und `AGENT_HANDOFF_CONTRACTS.md`. In der für diese Antwort vorliegenden Evidenz wurden diese Repo-Oberflächen jedoch vor allem **indirekt** über aktuelle hochgeladene Dateien erschlossen, nicht über direkte, zitierbare Connector-Ausgaben. Deshalb werden sie hier als **sekundär bestätigt**, nicht als primäre Zeilenquelle behandelt. fileciteturn0file1

## Behandlung nicht zugänglicher oder unvollständiger Quellen

```yaml
inaccessible_source_handling:
  if_source_not_directly_accessible:
    - mark_as_unverified_for_line_level_claims
    - use_current_uploaded_derivatives_only_if_they_reference_it_explicitly
    - do_not_invent_missing_sections
    - turn_missing_data_into_build_question_if_it_blocks_build
  if_source_is_old_and_newer_current_source_exists:
    - prefer_newer_source
    - keep_older_source_only_as_background
```

Diese Regel ist besonders wichtig für Pfade, Registryspeicher, genaue Skill-Locations und Subagent- oder Permissions-Details: sobald die aktuellen Review-Dateien dort Lücken nennen, wird die Lücke als offene Build-Frage behandelt und nicht durch ältere Annahmen “gefüllt”. fileciteturn0file4 fileciteturn0file5 fileciteturn0file6 fileciteturn0file9 fileciteturn0file10

# 02_DECISION_REGISTER.md

## Eingefrorene Entscheidungen

Die folgenden Entscheidungen sind für diese Phase bereits fest. Der Registerzweck ist nicht, neue Architektur zu erfinden, sondern das spätere Claude-Code-Bauen gegen Drift abzusichern. Die Rollen- und Mechanikfestlegungen stammen aus dem aktuellen Entscheidungsstand; der Kernloop und die entfernten Modelle sind in den aktuellen Informationsflussdokumenten und im Build Pack konsistent beschrieben. fileciteturn0file1 fileciteturn0file11 fileciteturn0file12 fileciteturn0file14

| id | decision | rationale | affected_files | status |
|---|---|---|---|---|
| D-01 | Claude-first Repo-Vorbereitung statt Runtime-Implementierung | Offizielle Claude-Mechaniken für `CLAUDE.md`, Skills und `.claude/` sind für diese Phase maßgeblich; der interne Build Pack schließt Runtime-Installation ausdrücklich aus. citeturn5view0turn11view0turn11view2 fileciteturn0file14 | alle sieben Vorbereitungsdokumente | locked |
| D-02 | Es gibt genau **ein kanonisches Repo** | `CLAUDE.md` ist projektweiter Speicher; Projekt-Skills und Projekt-Subagents sind repo-spezifisch. Die Vorbereitung zielt daher auf einen zentralen Repo-Spine. citeturn5view0turn11view2 fileciteturn0file18 | `CLAUDE.md`, `SOURCE_MAP.md`, Ziel-Dateibaum | locked |
| D-03 | Alfred bleibt Core Sequencing Orchestrator | Alfred trägt Intake, Sequenzierung, Operator-Kontinuität und Handoff-Framing; diese Rolle ist im aktuellen Entscheidungsstand nicht optional. fileciteturn0file1 fileciteturn0file14 | `00_SYSTEM_INTENT.md`, SOUL-ALFRED.draft.md | locked |
| D-04 | Die vier Kernrollen bleiben fest | Alfred, MetaStrategist, MetaOperations und MetaDetectiveController sind die feste Topologie; keine frühe Agentenproliferation. fileciteturn0file1 fileciteturn0file14 | SOUL-Drafts, Entscheidungsregister, Ziel-Dateibaum | locked |
| D-05 | Wiederholbare Arbeit wird primär zu Skills, Templates und Docs, nicht zu neuen Agenten | Offizielle Claude-Doku trennt Skills und Subagents klar; interne Entscheidungen sagen ebenso, dass die meisten Workflows Skills und keine neuen Profile/Agenten sein sollen. citeturn11view1turn11view3 fileciteturn0file1 | Skill-Verzeichnis, SOUL-Drafts, Build Prompt | locked |
| D-06 | Der Kernloop bleibt `PreCapWeek → PreCapNextDay → OperatorExecutesPlannedFlow → FlowRecapSkill → AllProjectStatusPacketUpdate → next cycle` | Diese Loop wird in der aktuellen Prozessarchitektur mehrfach als verbindlich beschrieben. fileciteturn0file11 fileciteturn0file12 fileciteturn0file14 | System Intent, Artefaktregister, Beispiele | locked |
| D-07 | `DayExecution` und `FlowExecution` bleiben aus dem Kernmodell entfernt | Die neue Architektur ersetzt diese Ebenen durch genehmigte Flow-Pakete, Operator-Ausführung und FlowRecap/APSU-Handoffs. fileciteturn0file11 fileciteturn0file14 | System Intent, Decision Register, Build Prompt | locked |
| D-08 | `RecapDay` bleibt verschoben und nicht-core | `RecapDay` ist optionaler späterer Alfred-/Reflexions-Layer, aber kein Muss der Statuskette. fileciteturn0file11 fileciteturn0file14 | System Intent, Decision Register | locked |
| D-09 | Zuerst Macro/Meso-Skelett, dann Micro-Füllung | Sowohl die interne Build-Pack-Logik als auch die Agent-Skills-Spezifikation empfehlen knappe Kerndateien und spätere Auslagerung/Ergänzung statt sofortiger Vollausarbeitung. fileciteturn0file14 citeturn19view0turn19view2 | alle Vorbereitungsdokumente | locked |
| D-10 | In dieser Phase entstehen **keine finalen** `SKILL.md`- oder `SOUL.md`-Dateien | Die aktuellen Dokumente sprechen von Drafts, nicht von aktiven Runtime-Dateien; Claude Code soll staged bauen. fileciteturn0file14 fileciteturn0file17 | SOUL-Drafts, Skill-Skelette, Build Prompt | locked |
| D-11 | `CLAUDE.md` bleibt für immer nötige Regeln reserviert; Prozeduren gehören in Skills | Das ist offizielle Claude-Empfehlung und deckt sich mit der internen Übersetzungslogik. citeturn5view0turn11view1turn12view0 fileciteturn0file17 | `CLAUDE.md`, Skills, Rules | locked |
| D-12 | Projekt-Skills sollen Claude-nativ gedacht werden; portable Mindestanforderungen kommen aus Agent Skills | Claude fügt Claude-spezifische Felder hinzu, aber das portable Minimum bleibt `SKILL.md` als zentraler Skill-Einstiegspunkt im Skill-Ordner. citeturn11view0turn14view5turn19view0 | Skill-Skelette, Source Map, Build Prompt | locked |

## Superseded und nicht wiederbeleben

```yaml
superseded_do_not_revive:
  - DayExecution_as_standalone_process
  - FlowExecution_as_standalone_process
  - DayExecutionController_as_required_layer
  - RecapDay_as_required_core_layer
  - new_agent_for_every_repeatable_workflow
  - large_procedural_bodies_in_CLAUDE.md
  - immediate_runtime_installation_in_phase_one
```

Diese Punkte sind nicht “offen”, sondern bewusst verdrängt: die aktuelle Architektur hat sie ersetzt oder auf später verschoben. Das gilt besonders für jede Tendenz, früh wieder eine agentenschwere OpenCLAW/Hermes-Topologie zu bauen, obwohl die aktuelle Festlegung klar Skills, Dokumente und Artefaktverträge priorisiert. fileciteturn0file1 fileciteturn0file11 fileciteturn0file14

## Entscheidungslogik für spätere Wiedereröffnung

Eine Entscheidung darf in der späteren Build-Phase nur wieder geöffnet werden, wenn **eine offizielle Claude-Regel** oder **eine aktuellere projektinterne Kernquelle** die Festlegung klar widerlegt, oder wenn eine Review-Datei einen **echten Build-Blocker** dokumentiert. Review-Dateien sind also Trigger für gezielte Build-Fragen, aber keine Erlaubnis, den Gesamtentwurf neu zu erfinden. citeturn5view0turn11view1 fileciteturn0file4 fileciteturn0file5 fileciteturn0file6 fileciteturn0file9 fileciteturn0file10

# 03_ARTIFACT_CONTRACT_REGISTRY.md

## Registerregel

Dieses Register definiert nur **macro-level Artefaktverträge**. Es legt Produzent, Konsument, Zweck, Pflichtfelder, Validierungslogik und Verhalten bei fehlendem Input fest, aber keine finalen Dateischemata. Die aktuelle Informationsarchitektur fordert genau diese Ebene: zuerst Artefakt-Taxonomie und logische Slots, erst später echte Pfade und Runtime-Dateien. fileciteturn0file11 fileciteturn0file14

## Kernartefakte für Planung, Ausführung und Merge

Die folgenden Verträge stammen direkt aus der aktuellen Loop- und Artefaktarchitektur für PreCapWeek, PreCapNextDay, Operator-Ausführung, FlowRecap und APSU. fileciteturn0file11 fileciteturn0file12

| artifact name | producer | consumer | purpose | required macro fields | validation rule | missing input behavior |
|---|---|---|---|---|---|---|
| `weekly_plan_packet` | PreCapWeek | PreCapNextDay | strategischer Wochencontainer für Prioritäten und Tagesrichtung | `week_id`, `weekly_priorities`, `project_allocations`, `day_by_day_direction`, `fixed_calendar_constraints`, `first_PreCapNextDay_trigger_context` | muss mindestens einen geplanten Ausführungstag oder expliziten Omissionsgrund enthalten | blockieren und Operator-Klärung verlangen |
| `next_day_plan` | PreCapNextDay | Operator, indirekt FlowRecap/APSU | gesamter Tagesplan mit vier Flows | `execution_day_id`, `day_intent`, `calendar_feasibility_notes`, `fixed_flow_sequence`, `model_usage_constraints`, `operator_review_status` | alle vier Flows müssen vorhanden sein; Operator-Gate muss sichtbar sein | blockieren; keine stillschweigende Teilplanung |
| `flow_packet` | PreCapNextDay | Operator, FlowRecap | konkrete Ausführungs- und Recap-Einheit pro Flow | `flow_id`, `project_id`, `fixed_position`, `flow_goal`, `why_this_flow_now`, `expected_outputs`, `three_sprints`, `prompt_packets`, `embedded_context_instructions`, `output_capture_instruction`, `FlowRecapSkill_instruction`, `usage_tracking_expectation` | ein Flow-Paket ist nur gültig, wenn Sprintstruktur und erwartete Outputs vorhanden sind | Flow als nicht planbar markieren; kein stiller Ersatz |
| `prompt_packet` | PreCapNextDay oder Prompt-and-AI-Routing | Operator, FlowRecap, ModelUsageTracking | Sprint-spezifische Prompt-/Modell-/Surfaceroute | `prompt_packet_id`, `project_id`, `flow_id`, `sprint_id`, `prompt_goal`, `suggested_AI_surface`, `suggested_model_or_mode`, `context_to_include`, `expected_prompt_output`, `fallback_route`, `usage_tracking_required` | Packet muss rückverfolgbar und sprintgebunden sein | markieren als “routing incomplete”; menschliche Auswahl verlangen |
| `raw_flow_dump` | Operator | FlowRecap | rohe Ausführungsevidenz pro Flow | `flow_id_or_original_flow_packet`, `what_was_done`, `outputs_created_or_missing`, `unresolved_items`, `model_or_AI_surface_usage_if_known`, `operator_guess_for_next_step_if_known` | ein Raw Dump muss einem Flow eindeutig zuordenbar sein | FlowRecap darf nicht laufen; fehlender Input explizit melden |
| `skipped_flow_marker` | Operator oder FlowRecap | APSU, PreCapNextDay | persistente Markierung für Skip/Block/Move | `flow_id`, `reason`, `project`, `recovery_note` | Skip muss Grund und Rückholhinweis tragen | als offener Blocker in nächsten Plan übernehmen |

## Kernartefakte für Recap, Modellnutzung und Statusverdichtung

Die folgenden Verträge kommen aus FlowRecap, APSU und ModelSubscriptionUsageTracking sowie deren Review-Dateien. fileciteturn0file6 fileciteturn0file4 fileciteturn0file9 fileciteturn0file10 fileciteturn0file11

| artifact name | producer | consumer | purpose | required macro fields | validation rule | missing input behavior |
|---|---|---|---|---|---|---|
| `flow_recap_packet` | FlowRecap | APSU, PreCapNextDay, ModelUsageTracking | strukturierte Ausführungserinnerung je Flow | `document_metadata`, `source_flow_packet_reference`, `raw_dump_sources`, `completion_state`, `planned_vs_actual`, `sprint_level_summary`, `completed_outputs`, `artifact_index`, `prompt_result_summary`, `model_usage_delta`, `project_status_delta`, `blockers`, `reusable_learning`, `next_step_proposal`, `operator_validated_next_step`, `context_for_future_PreCapNextDay` | nicht vollständig ohne validierten nächsten Schritt | blockieren und Operator-Validierung anfordern |
| `model_usage_delta` | FlowRecap | ModelUsageTracking; referenziert von APSU/PreCapNextDay | Soll-Ist-Delta pro eingesetztem Modell/Surface | `prompt_packet_id_or_equivalent_link`, `actual_surface`, `actual_model_or_mode`, `cost_or_scarcity_signal`, `route_success_or_failure`, `notes_for_future_routing` | muss mit geplantem Prompt-Paket oder Flow verknüpfbar sein | “usage unknown” markieren, aber keinen Fake-Datensatz erzeugen |
| `updated_all_project_status_packet` | APSU | PreCapNextDay, PreCapWeek | kanonischer projektübergreifender Status nach Merge | `document_metadata`, `source_inputs`, `consumed_flow_recap_registry`, `skipped_flow_marker_registry`, `project_status_entries`, `next_executable_chunks`, `blockers`, `priority_or_urgency_changes`, `unresolved_conflicts`, `model_usage_summary_pointer`, `next_PreCapNextDay_context` | Merge darf keine doppelten Recaps konsumieren und keine Konflikte verschweigen | blockieren oder als `validation_needed` ausweisen |
| `next_PreCapNextDay_input_context` | APSU | PreCapNextDay | verdichteter Seed für die nächste Tagesplanung | `execution_day_target`, `project_next_chunks`, `project_blockers`, `skipped_flow_markers_to_consider`, `prompt_routes_to_reuse_or_avoid`, `high_impact_changes_requiring_operator_review` | muss direkt aus dem letzten Merge ableitbar sein | manuellen Start erlauben, aber Kontext als unvollständig markieren |

## Ingestions- und Übergabeartefakte

`source_ingestion_record` und `handoff_packet` sind im aktuellen Loop nicht die zentralen Tagesartefakte, aber sie sind für den späteren Claude-first Repo-Aufbau notwendig: Quellen sollen systematisch aufgenommen werden, und Übergaben zwischen Rollen/Chats/Skills sollen ein wiederverwendbares Format haben. Diese Artefakte sind in den aktuellen Architektur- und Entscheidungsdokumenten als Skill-/Workflow-Kandidaten angelegt. fileciteturn0file15 fileciteturn0file1

| artifact name | producer | consumer | purpose | required macro fields | validation rule | missing input behavior |
|---|---|---|---|---|---|---|
| `source_ingestion_record` | MetaOperations über Source-Scan/Workflow-Normalisierung | Source Map, project-routing, spätere source-scan-to-workflow-record Skills | nachvollziehbare Aufnahme eines Quellencorpus in den Repo-Wissensraum | `source_id`, `source_type`, `source_location_or_reference`, `ingestion_date`, `scope`, `extraction_status`, `normalized_outputs`, `open_ambiguities`, `review_status` | jede Quelle braucht Typ, Herkunft und Status; keine “black box”-Übernahme | Quelle als unvollständig registrieren; keine Normalisierung behaupten |
| `handoff_packet` | MetaOperations | Alfred, MetaHeads, Skills, Subagents oder menschliche Review-Stellen | kompakte, verlustarme Übergabe zwischen Rollen, Chats oder Build-Stufen | `objective`, `current_state`, `inputs`, `evidence_refs`, `expected_outputs`, `acceptance_criteria`, `risk_or_ambiguity_flags`, `stop_conditions` | Receiver muss Annahme/Ablehnung prüfen können; Paket darf Scope-Grenzen nicht verschleiern | Übergabe ablehnen oder zur Präzisierung zurückgeben |

## Registry- und Slot-Regel

Für alle Artefakte gilt bis zur späteren Implementierung:

```yaml
storage_rule:
  logical_slots_only_now: true
  absolute_paths_now: false
  every_artifact_needs:
    - one_primary_producer
    - at_least_one_consumer
    - stable_identifier
    - explicit_missing_input_behavior
    - no_silent_fabrication
```

Das folgt direkt aus der universellen Input/Output-Vertragsvorlage der aktuellen Informationsarchitektur und ist besonders wichtig, weil mehrere Review-Dateien fehlende Speicherorte, fehlende Registries und unklare Downstream-Handoffs als build-blocking markieren. fileciteturn0file11 fileciteturn0file4 fileciteturn0file5 fileciteturn0file6 fileciteturn0file9 fileciteturn0file10

# 04_TARGET_FILE_TREE_PROPOSAL.md

## Vorschlagsprinzip

Der folgende Baum ist **ein Claude-first Repo-Vorschlag**, kein Behaupten einer bereits existierenden Runtime-Struktur. Offizielle Claude-Code-Dokumentation sagt klar, dass Projektanweisungen, Settings, Skills, Commands und Agents in bekannten Repo-Orten liegen können; zugleich empfehlen die Docs, für wiederverwendbare Workflows Skills zu bevorzugen, während `.claude/commands/` als Kompatibilitätsmechanismus weiter funktioniert. citeturn11view2turn11view0turn14view0

Darum trennt dieser Vorschlag zwischen:

- **kanonischer Designquelle im Repo**
- **Claude-nativen Laufzeitoberflächen unter `.claude/`**
- **späterer, explizit freizugebender Spiegelung in Claude-spezifische Verzeichnisse**

## Zielbaum

```text
apex-alfred-orchestration/
├── CLAUDE.md
├── README.md
├── SOURCE_MAP.md
├── DECISION_REGISTER.md
├── ARTIFACT_CONTRACT_REGISTRY.md
├── BUILD_ORDER.md
├── CURRENT.md
├── .claude/
│   ├── settings.json
│   ├── commands/
│   │   └── README.md
│   ├── agents/
│   │   └── README.md
│   └── skills/
│       └── README.md
├── souls/
│   ├── SOUL-ALFRED.draft.md
│   ├── SOUL-META-STRATEGIST.draft.md
│   ├── SOUL-META-OPERATIONS.draft.md
│   └── SOUL-META-DETECTIVE-CONTROLLER.draft.md
├── skills/
│   ├── precap-week/
│   │   └── SKILL.draft.md
│   ├── precap-next-day/
│   │   └── SKILL.draft.md
│   ├── flow-recap/
│   │   └── SKILL.draft.md
│   ├── status-merge/
│   │   └── SKILL.draft.md
│   ├── prompt-and-ai-routing/
│   │   └── SKILL.draft.md
│   ├── model-usage-log/
│   │   └── SKILL.draft.md
│   ├── source-scan-to-workflow-record/
│   │   └── SKILL.draft.md
│   ├── handoff-packet/
│   │   └── SKILL.draft.md
│   ├── no-drift-validation/
│   │   └── SKILL.draft.md
│   └── project-routing/
│       └── SKILL.draft.md
├── templates/
│   ├── raw-flow-dump.template.md
│   ├── flow-packet.template.md
│   ├── prompt-packet.template.md
│   ├── flow-recap.template.md
│   ├── status-packet.template.md
│   ├── handoff-packet.template.md
│   ├── weekly-plan.template.md
│   └── next-day-plan.template.md
├── examples/
│   ├── four-flow-precap-next-day.example.md
│   ├── masterofarts-flow-recap.example.md
│   ├── leela-flow.example.md
│   ├── apex-alfred-orchestration-flow.example.md
│   └── residual-flow.example.md
├── registries/
│   ├── consumed-flow-recaps.registry.md
│   ├── skipped-flow-markers.registry.md
│   ├── model-usage.registry.md
│   └── source-ingestion.registry.md
└── docs/
    ├── claude-file-conversion-rules.md
    ├── alfred-architecture-guide.md
    ├── old-system-ingestion-map.md
    └── deprecated-models.md
```

Dieser Baum verbindet die offiziell vorgesehenen Claude-Orte unter `.claude/` mit einer klaren projektweiten Designbibliothek für Doku, Draft-Skills, Templates und Beispiele. Er folgt außerdem der aktuellen internen Konvertierungslogik, die SOUL-/Skill-/Example-/Template-Familien schon vor der Runtime-Installation separat behandeln will. citeturn11view2turn11view0 fileciteturn0file14 fileciteturn0file17

## Ordnerrollen

### Root

| Feld | Inhalt |
|---|---|
| purpose | Repo-Spine für immer nötige Projektrahmung und kanonische Register |
| what belongs here | `CLAUDE.md`, lesbare Startdoku, kanonische Register, aktueller Build- und Statusrahmen |
| what does not belong here | lange Verfahrensprosa, projektfremde Tools, aktive Runtime-Installationsdateien |

`CLAUDE.md` gehört hierher, weil Claude Code Projektanweisungen am Root oder in `.claude/CLAUDE.md` als Projektkontext lädt; kompakte Root-Dokumente sind daher sinnvoll, solange Prozeduren in Skills ausgelagert bleiben. citeturn5view0turn11view2turn12view0

### `.claude/`

| Feld | Inhalt |
|---|---|
| purpose | Claude-native Interface-Schicht für Settings, kompatible Commands, spätere projektgebundene Skills und optionale Subagents |
| what belongs here | `settings.json`, ggf. dünne Laufzeit-Spiegelungen, Kompatibilitäts-Commands, später echte Claude-Subagent-Definitionen |
| what does not belong here | kanonische Langdokumentation, gesamte Designbibliothek, unfreigegebene Runtime-Masse |

Offiziell gehören projektweite Skills unter `.claude/skills/<name>/SKILL.md`, Commands unter `.claude/commands/`, und spezialisierte Subagents unter `agents/*.md`; zugleich sind Skills der empfohlene Ort für wiederverwendbare Workflows, während Commands nur noch denselben Mechanismus auf Single-File-Art nutzen. citeturn11view2turn11view0turn14view0turn16view4

### `souls/`

| Feld | Inhalt |
|---|---|
| purpose | makro-/meso-level Rollenentwürfe für Alfred und die drei Meta-Heads |
| what belongs here | SOUL-Drafts mit Rolle, Verantwortungen, harte Grenzen, Failure Modes, verlinkte Skill-Familien |
| what does not belong here | endgültige Claude-Subagent-Prompts, laufende Statusdateien, operative Checklisten |

Die aktuellen internen Konvertierungsdokumente behandeln Meta-Agent-Identität ausdrücklich als SOUL-/Rollenmaterial und nicht als Skill-Inhalt. Gleichzeitig sind Claude-Subagents technisch eine andere primitive Oberfläche; daher bleiben SOUL-Dateien zunächst als Design-Drafts außerhalb von `.claude/agents/`. fileciteturn0file17 fileciteturn0file18 citeturn11view3

### `skills/`

| Feld | Inhalt |
|---|---|
| purpose | kanonische Designquelle für Skill-Skelette und begleitende Referenzen |
| what belongs here | Prozess-Skelette, Referenzhinweise, Trigger-Logik, Artefaktbezug, spätere skill-lokale Referenzen/Assets |
| what does not belong here | finale Produktionsskills ohne Freigabe, unstrukturierte Prozessaufsätze, globale Projektregeln |

Der offene Agent-Skills-Standard definiert Skills als Ordner mit `SKILL.md` plus optionalen Referenzen, Assets und Skripten; Claude Code folgt demselben Modell und lädt den Skill-Body erst bei Nutzung. Deshalb ist ein Skill-Ordner pro Verfahren die richtige Speichereinheit. citeturn19view0turn11view0turn20view1

### `templates/`

| Feld | Inhalt |
|---|---|
| purpose | konkrete Output- und Input-Formate, die Skills ausfüllen oder validieren |
| what belongs here | Artefaktvorlagen für Flow-Dumps, Flow-/Prompt-/Status-/Handoff-Pakete, Wochen-/Tagesplan |
| what does not belong here | Skills selbst, Beispielinstanzen, globale Regeln |

Die Agent-Skills-Best Practices empfehlen Templates ausdrücklich, weil konkrete Formstrukturen zuverlässiger sind als reine proseartige Formatbeschreibungen; längere Templates sollen in separaten Dateien liegen und aus Skills referenziert werden. citeturn20view0turn19view0

### `examples/`

| Feld | Inhalt |
|---|---|
| purpose | Referenzinstanzen aus Leela, MasterOfArts, Apex/Alfred und Residual |
| what belongs here | reale oder kuratierte Beispielpakete, die Skill-Erwartungen konkretisieren |
| what does not belong here | allgemeine Regeln, lebender Status, operative Registry-Daten |

Die internen Konvertierungsregeln behandeln Workflow-Beispiele explizit als Referenzmaterial und nicht als aktive primitive Oberfläche. Claude Skills können Beispieloutputs aus Skill-Ordnern laden; hier bleiben repo-weite Beispiele jedoch bewusst als eigene Wissensfamilie sichtbar. fileciteturn0file17

### `registries/`

| Feld | Inhalt |
|---|---|
| purpose | langlebige, maschinenlesbare Nachverfolgung von verarbeiteten Artefakten |
| what belongs here | konsumierte Flow-Recaps, Skip-Marker, Modellnutzung, Quellenaufnahme |
| what does not belong here | unstrukturierte Langtexte, Einmal-Notizen, große Rohdumps |

Die aktuelle Informationsarchitektur verlangt explizit Registry- und Slot-Logik, damit Downstream-Prozesse Artefakte wiederfinden und Duplikate vermeiden können; mehrere Review-Dateien markieren fehlende Registry-Locations als build-blocking. fileciteturn0file11 fileciteturn0file4 fileciteturn0file5

### `docs/`

| Feld | Inhalt |
|---|---|
| purpose | kompakte Hintergrund- und Konvertierungsdokumentation, die nicht ständig in Claude-Kontext geladen werden muss |
| what belongs here | Konvertierungsregeln, Architekturleitfaden, Altsystem-Ingestionskarte, Deprecated-Model-Notizen |
| what does not belong here | aktive Projektregeln für jede Session, operative Skills, live registries |

Diese Trennung folgt direkt aus der Claude-Empfehlung, `CLAUDE.md` knapp zu halten und längere Referenzinhalte in Skills, Rules oder andere gezielt geladene Dateien auszulagern. citeturn5view0turn12view0turn20view1

# 05_BUILD_QUESTIONS.md

## Offene, build-blockierende Fragen

Nur Fragen, die den späteren Claude-Code-Build tatsächlich blockieren, gehören hier rein. Die meisten folgenden Punkte werden in den Review-Dateien als fehlende Speicherorte, fehlende Variablen, fehlende Handoffs oder unklare Runtime-Semantik markiert. fileciteturn0file4 fileciteturn0file5 fileciteturn0file6 fileciteturn0file9 fileciteturn0file10

## Repo-Root und kanonischer Name

```yaml
question:
  id: Q01
  question: Soll das kanonische Repo als neues dediziertes Claude-first Repo aufgebaut werden oder in einen bereits existierenden Projektbaum hinein?
  why_it_matters: Der Repo-Root entscheidet über Dateipfade, Claude-Startkontext, spätere Spiegelung in `.claude/` und das Risiko, aktive Runtime-Dateien mit Drafts zu vermischen.
  options:
    A: Neues dediziertes Repo mit klarem Root für alle sieben Dokumente und Draft-Familien.
    B: Ein vorhandenes Arbeitsrepo wird direkt erweitert.
    C: Zuerst nur ein docs-first Unterordner, später Ausgründung in eigenes Repo.
  recommendation: A
  default_if_unanswered: A
  affected_files:
    - CLAUDE.md
    - README.md
    - BUILD_ORDER.md
    - 04_TARGET_FILE_TREE_PROPOSAL.md
  blocking_level: blocking
```

## Kanonischer Skill-Ort

```yaml
question:
  id: Q02
  question: Ist `skills/` die kanonische Designquelle, während `.claude/skills/` nur die Claude-Laufzeitspiegelung ist, oder soll `.claude/skills/` selbst die kanonische Quelle sein?
  why_it_matters: Claude Code unterstützt projektweite Skills offiziell unter `.claude/skills/`, aber das Vorbereitungsprojekt braucht zugleich eine gut lesbare Designbibliothek. Ohne klare Entscheidung drohen Doppelpfade und Drift.
  options:
    A: `skills/` ist kanonische Designquelle; `.claude/skills/` wird später aus freigegebenen Skills gespiegelt.
    B: `.claude/skills/` ist die einzige kanonische Quelle.
    C: Beide werden parallel manuell gepflegt.
  recommendation: A
  default_if_unanswered: A
  affected_files:
    - 04_TARGET_FILE_TREE_PROPOSAL.md
    - BUILD_ORDER.md
    - 06_CLAUDE_SONNET_BUILD_PROMPT.md
  blocking_level: blocking
```

## Bedeutung der SOUL-Dateien

```yaml
question:
  id: Q03
  question: Sind die SOUL-Dateien in dieser Phase reine Claude-Rollendokumente oder bewusst Hermes-kompatible Zukunftsdrafts?
  why_it_matters: Die Antwort bestimmt, wie technisch oder wie Claude-spezifisch diese Dateien werden dürfen und ob `.claude/agents/` früh mitgedacht werden muss.
  options:
    A: Reine Claude-first Rollendokumente für diese Phase; Hermes-Übersetzung später.
    B: Zukunftsdrafts mit Hermes-Kompatibilitätsziel, aber ohne Runtime-Installation.
    C: Direkt als Claude-Subagent-Definitionen modellieren.
  recommendation: B
  default_if_unanswered: B
  affected_files:
    - souls/SOUL-ALFRED.draft.md
    - souls/SOUL-META-STRATEGIST.draft.md
    - souls/SOUL-META-OPERATIONS.draft.md
    - souls/SOUL-META-DETECTIVE-CONTROLLER.draft.md
  blocking_level: blocking
```

## Exakte Artefaktpfade

```yaml
question:
  id: Q04
  question: Werden in dieser Phase bereits konkrete Artefaktpfade festgelegt oder nur logische Slots?
  why_it_matters: Mehrere Review-Dateien markieren fehlende Output-Locations als build-blocking, zugleich warnt die aktuelle Architektur davor, echte Pfade vor Repo-Inspektion zu erfinden.
  options:
    A: Bereits jetzt feste Pfade für alle Artefaktfamilien.
    B: Nur logische Slots; echte Pfade erst nach Repo-Inspektion.
    C: Ein Hybrid aus Root-Pfaden für Register und logischen Slots für Flow-Artefakte.
  recommendation: B
  default_if_unanswered: B
  affected_files:
    - 03_ARTIFACT_CONTRACT_REGISTRY.md
    - 04_TARGET_FILE_TREE_PROPOSAL.md
    - 06_CLAUDE_SONNET_BUILD_PROMPT.md
  blocking_level: blocking
```

## Scope von CURRENT.md

```yaml
question:
  id: Q05
  question: Soll `CURRENT.md` ein einziges Root-Dokument sein oder nur eine kompakte Startdatei, die auf projekt- oder artefaktspezifische Statuspakete verweist?
  why_it_matters: Interne Vorbereitungsdokumente sehen `current.md` als Zustandsanker, die Prozessarchitektur arbeitet jedoch mit `all_project_status_packet` als kanonischem Merge-Output. Ohne klare Scope-Regel wird Zustand doppelt gepflegt.
  options:
    A: Ein einziges Root-`CURRENT.md` als knapper Navigator auf den letzten kanonischen Status.
    B: Pro Projekt ein eigenes Current-Dokument.
    C: Kein `CURRENT.md`; nur Statuspakete.
  recommendation: A
  default_if_unanswered: A
  affected_files:
    - CURRENT.md
    - ARTIFACT_CONTRACT_REGISTRY.md
    - BUILD_ORDER.md
  blocking_level: blocking
```

## Archivieren oder Übersetzen

```yaml
question:
  id: Q06
  question: Sollen Altsystem-Dateien roh archiviert werden, aktiv übersetzt werden, oder beides?
  why_it_matters: Das Vorbereitungsprojekt lebt von sauberer Übersetzung statt Kontextmüll. Gleichzeitig dürfen wichtige Quellen für spätere Nachvollziehbarkeit nicht verschwinden.
  options:
    A: Nur Übersetzung; Altdateien bleiben außerhalb des Repos.
    B: Übersetzen plus ein klarer `docs/old-system-ingestion-map.md`, der Originale referenziert.
    C: Alles vollständig in das neue Repo kopieren.
  recommendation: B
  default_if_unanswered: B
  affected_files:
    - docs/old-system-ingestion-map.md
    - SOURCE_MAP.md
    - BUILD_ORDER.md
  blocking_level: blocking
```

## Settings und Permissions jetzt oder später

```yaml
question:
  id: Q07
  question: Soll `.claude/settings.json` in dieser Phase bereits inhaltlich definiert werden oder nur als Platzhalter bestehen?
  why_it_matters: Claude Code erlaubt dort Permissions, Hooks, Env und Defaults. Zu frühe Definition kann Runtime-Verhalten implizit festlegen; zu spätes Definieren kann Build-Prompts unklar lassen.
  options:
    A: Nur Platzhalterdatei mit Kommentar zur späteren Freigabe.
    B: Minimaldefinition nur für ungefährliche Defaults, ohne weitreichende Freigaben.
    C: Vollständige Permissions-/Hooks-Ausgestaltung jetzt.
  recommendation: B
  default_if_unanswered: B
  affected_files:
    - .claude/settings.json
    - 04_TARGET_FILE_TREE_PROPOSAL.md
    - 06_CLAUDE_SONNET_BUILD_PROMPT.md
  blocking_level: blocking
```

## Namenskonvention für Artefakte

```yaml
question:
  id: Q08
  question: Welche Artefakt-Namensregel ist kanonisch: menschenlesbares Dateinamensschema, ID-first-Schema oder Mischschema?
  why_it_matters: FlowRecap-, Status- und Usage-Artefakte müssen über Upstream-/Downstream-Ketten wiederfindbar sein; Review-Dateien markieren fehlende IDs und unklare Dateimuster als echte Integrationslücken.
  options:
    A: ID-first-Schema, z. B. `flow-recap-<date>-<flow-id>-<project>.md`.
    B: Menschenlesbare Titel ohne harte IDs.
    C: Mischschema mit stabiler ID im YAML-Block und lesbarem Dateinamen.
  recommendation: C
  default_if_unanswered: C
  affected_files:
    - ARTIFACT_CONTRACT_REGISTRY.md
    - templates/flow-recap.template.md
    - registries/*
  blocking_level: blocking
```

## Invocation-Modell für prozedurale Arbeit

```yaml
question:
  id: Q09
  question: Sollen Kernprozesse wie FlowRecap und PreCapNextDay später primär per Skill-Aufruf oder primär über gefütterte Artefakt-/Prompt-Pakete laufen?
  why_it_matters: Der Unterschied beeinflusst Skill-Descriptions, Template-Struktur und ob Claude automatisch oder nur explizit triggern darf.
  options:
    A: Skill-first mit expliziten `/name`-Aufrufen für side-effect-nahe Prozesse.
    B: Artefakt-first; Skills sind nur Referenzlogik.
    C: Hybrid: Skill-Aufruf liest normierte Eingangsartefakte.
  recommendation: C
  default_if_unanswered: C
  affected_files:
    - skills/flow-recap/SKILL.draft.md
    - skills/precap-next-day/SKILL.draft.md
    - templates/*
  blocking_level: non_blocking
```

## Quelle für AI-Surface- und Routing-Inventar

```yaml
question:
  id: Q10
  question: Wo liegt die kanonische Quelle für verfügbare AI-Surfaces, Modelle und Routing-Präferenzen?
  why_it_matters: PreCapNextDay, Prompt-and-AI-Routing und Model-Usage-Tracking nennen dieses Inventar als Input; die Review-Dateien markieren seine Quelle derzeit als unklar.
  options:
    A: Dedizierte Repo-Datei unter `registries/` oder `docs/`.
    B: Nur Operator-Eingabe pro Session.
    C: Später nur aus externem Tooling.
  recommendation: A
  default_if_unanswered: A
  affected_files:
    - skills/prompt-and-ai-routing/SKILL.draft.md
    - skills/model-usage-log/SKILL.draft.md
    - skills/precap-next-day/SKILL.draft.md
  blocking_level: blocking
```

# 06_CLAUDE_SONNET_BUILD_PROMPT.md

## Prompttext

```markdown
Du bist Claude Sonnet in Claude Code mit Dateisystemzugriff.

Arbeite an einem Claude-first Vorbereitungs-Repository für das **Apex / Alfred Orchestration System**.

Wichtiger Kontext:
- Dieses Repo ist in dieser Phase **kein** Produktions- oder Runtime-Implementierungsprojekt.
- Alfred ist der Core Sequencing Orchestrator.
- Die drei festen unterstützenden Köpfe sind MetaStrategist, MetaOperations und MetaDetectiveController.
- Der kanonische Kernloop ist:
  1. PreCapWeek
  2. PreCapNextDay
  3. OperatorExecutesPlannedFlow
  4. FlowRecapSkill
  5. AllProjectStatusPacketUpdate
  6. nächster PreCapNextDay-Zyklus
- Revive diese entfernten Modelle nicht:
  - DayExecution als Standalone-Prozess
  - FlowExecution als Standalone-Prozess
  - DayExecutionController als Standalone-Prozess
  - RecapDay als verpflichtende Core-Schicht

## Dein Arbeitsvertrag

### Zuerst immer inspizieren
Bevor du irgendetwas erzeugst:
1. inspiziere den lokalen Repo-Zustand
2. finde den wahrscheinlichen Projekt-Root
3. prüfe, welche der folgenden Dateien schon existieren
4. lies danach die sieben Vorbereitungsdokumente vollständig

Pflichtlektüre:
- 00_SYSTEM_INTENT.md
- 01_SOURCE_MAP.md
- 02_DECISION_REGISTER.md
- 03_ARTIFACT_CONTRACT_REGISTRY.md
- 04_TARGET_FILE_TREE_PROPOSAL.md
- 05_BUILD_QUESTIONS.md
- 06_CLAUDE_SONNET_BUILD_PROMPT.md

### Erste Antwort, bevor du Dateien erzeugst
Deine erste inhaltliche Antwort muss genau diese Teile enthalten:
- Repo-Inspektionszusammenfassung
- Zusammenfassung deines Verständnisses des Systems
- Liste der ungelösten Blocker aus 05_BUILD_QUESTIONS.md
- sichere empfohlene Build-Reihenfolge
- erste Batch-Empfehlung: welche Dateien jetzt erzeugt werden dürfen
- welche Dateien ausdrücklich noch **nicht** erzeugt werden sollen

### Staged Build Contract
Baue nie alles auf einmal. Arbeite nur in diesen Stufen:

stage_1: repo spine
- Root-Dateien
- kanonische Register
- Build-Reihenfolge
- Platzhalter unter `.claude/` nur wenn gefahrlos

stage_2: role/SOUL drafts
- nur Draft-Rollendokumente
- keine aktive Runtime-Installation
- keine endgültigen Claude-Subagents, außer ausdrücklich angefordert

stage_3: skill skeletons
- nur Makro-/Meso-Skelette
- keine voll ausgearbeiteten Final-Skills
- klare Trigger, Inputs, Outputs, Failure Modes

stage_4: templates and artifact contracts
- Templates für Plans, Flow-Pakete, Recaps, Status und Handoffs
- nur so viel Detail, wie für saubere Verträge nötig ist

stage_5: examples and validation
- Beispielinstanzen
- Validierungsnotizen
- keine Produktionsautomatisierung

### Erzeugungsregel
Erzeuge nur die **erste freigegebene Batch**.
Wenn der Nutzer keine klare Batch freigegeben hat:
- mache keine stillschweigende Vollerzeugung
- schlage die Batch kurz vor
- wenn schon implizit freigegeben, beschränke dich auf Stage 1

### Claude-first Regeln
- Nutze offizielle Claude-Code-Mechaniken als Standard:
  - `CLAUDE.md` für immer nötigen Projektkontext
  - Skills für wiederverwendbares Wissen und invokierbare Workflows
  - `.claude/agents/` nur für echte Claude-Subagents
  - `.claude/commands/` nur wenn aus Kompatibilitätsgründen sinnvoll
- Halte `CLAUDE.md` knapp.
- Lagere prozedurale Inhalte aus `CLAUDE.md` in Skill-Skelette aus.
- Bleibe auf Macro-/Meso-Ebene, bis der Nutzer ausdrücklich das Ausfüllen einzelner Dateien verlangt.

### Was du vermeiden musst
- keine Hermes-Runtime-Implementierung, außer ausdrücklich angefordert
- kein Docker
- kein Kubernetes
- kein CI/CD
- keine Cloud- oder Produktionsinfrastruktur
- keine Observability- oder Security-Ops-Planung
- keine aktiven Cron-Jobs
- keine aktiven Kanban-Graphen
- keine finalen `SKILL.md`- oder `SOUL.md`-Runtime-Dateien
- keine Install-Kommandos
- keine erfundenen Pfade, wenn der Repo-Root sie nicht stützt

### Regeln für ungelöste Fragen
Wenn eine ungelöste Frage den aktuellen Batch blockiert:
- nenne sie explizit
- entscheide nicht stillschweigend gegen das Decision Register
- verwende sichere Defaults aus 05_BUILD_QUESTIONS.md
- dokumentiere jede angewandte Default-Entscheidung

### Qualitätsregeln
Für jede Datei, die du anlegst oder änderst, prüfe:
- passt sie zum Decision Register
- stärkt sie den kanonischen Loop
- belebt sie kein entferntes Modell wieder
- bleibt sie Claude-first
- bleibt sie Draft-/Vorbereitungsoberfläche statt Runtime-Installationsfläche

### Abbruchregel
Wenn du bemerkst, dass eine angeforderte Aktion in Runtime-Implementierung, Deployment oder Produktionsautomatisierung kippt:
- stoppe
- erkläre kurz, warum das außerhalb des aktuellen Vertrags liegt
- schlage nur die nächste sichere Vorbereitungsstufe vor
```

## Begründung des Prompt-Designs

Dieser Prompt spiegelt die offiziellen Claude-Code-Prinzipien wider: Repo zuerst inspizieren, `CLAUDE.md` als immer geladenen Kontext knapp halten, Skills für wiederverwendbare oder invokierbare Prozeduren nutzen, Subagents nur bei echter Isolationsnotwendigkeit einsetzen und Konfiguration unter `.claude/` von projektweiter Hintergrunddokumentation trennen. citeturn5view0turn11view0turn11view1turn11view2turn11view3

Er spiegelt außerdem die aktuellen Projektfestlegungen wider: Design-first statt Runtime, Repo-Inspektion vor Schreibaktionen, keine Wiederbelebung der entfernten DayExecution-/FlowExecution-Modelle und ein schrittweiser Dateiaufbau mit erstem Schwerpunkt auf dem Repo-Spine. fileciteturn0file14 fileciteturn0file11 fileciteturn0file18