# Pipeline V4 Architectural Feedback & V4.1 Improvement Backlog

> **Status:** ACTIVE REFERENCE & IMPROVEMENT BACKLOG (TODO)  
> **Date:** 2026-08-25  
> **Target:** Transcript Pipeline V4 $\rightarrow$ V4.1 Hardening  
> **Location:** `SourceTranscriptionAnalysisPipeline_Research/FEEDBACK_AND_TODO_IMPROVEMENTS_V4.1.md`

---

## 1. Executive Summary & Evaluation Scorecard

The V4 pipeline architecture is fundamentally well-designed for a local, inspectable transcript-to-knowledge workflow. Its core architectural triumph is the **clear boundary between deterministic media acquisition/ASR processing and probabilistic LLM knowledge synthesis**.

The primary operational and architectural risks reside in Stage 3 and Stage 4: `obsidian-wiki` operates primarily as an agent-driven Markdown skill framework rather than a deterministic library compiler with strict API guarantees.

### Evaluation Dimensions Scorecard

| Dimension | Rating (1–10) | Evaluation & Rationale |
| :--- | :---: | :--- |
| **Lokale Datenhoheit** *(Local Data Sovereignty)* | **9/10** | Download, audio extraction, and ASR execute 100% locally. Excellent for privacy, reproducibility, and cost control. |
| **Architekturtrennung** *(Architectural Separation)* | **8/10** | Raw audio and ASR artifacts are strictly separated from the knowledge vault, limiting the blast radius of LLM synthesis errors. |
| **Nachvollziehbarkeit** *(Traceability / Provenance)* | **7/10** | SRT, source references, manifest, and audit logs form the right foundation; claim-level provenance granularity needs expansion. |
| **Inkrementalität** *(Incrementality)* | **7/10** | SHA-256 caching is effective for source changes, but does not capture compiler, prompt, model, or schema changes. |
| **Wissensqualität** *(Knowledge Quality)* | **6/10** | Concept extraction, merging, and wikilinking are valuable but heavily prompt- and LLM-dependent; semantic errors can compound persistently. |
| **Betriebssicherheit** *(Operational Reliability)* | **6/10** | Strong deterministic baseline in Stages 1–2, but Stage 3 integration presents supply chain, versioning, and non-deterministic execution risks. |
| **Skalierbarkeit** *(Scalability)* | **6/10** | Progressive chunk reading resolves context window overflow, but does not automatically resolve global consistency or entity disambiguation. |

---

## 2. Core Architectural Strengths (Was sehr gut ist)

1. **Deterministische Grenze ist sinnvoll gezogen (Proper Deterministic Boundary):**
   - Stages 1 & 2 are strictly deterministic: `yt-dlp` and `FFmpeg` create a clean, automated media intake.
   - `faster-whisper` on CPU with `int8` quantization is resource-efficient and robust.
   - Silero VAD effectively eliminates silent gaps (>2s) without losing speech.
   - Minimal artifact set (`transcript.txt`, `transcript.srt`, `run.log`) cleanly separates readable content, temporal anchors, and runtime diagnostics.
   - *Operational Rule:* `transcribe.py` must fully consume/materialize the `faster-whisper` generator stream before writing completion artifacts.

2. **Abkehr vom Single-Shot-Extraktionsprompt (Elimination of Single-Shot Bottleneck):**
   - Replaced fragile monolithic prompts (e.g., Fabric `extract_wisdom`) with bounded, progressive chunking.
   - Multi-hour transcripts no longer fail due to context limits or timeouts.
   - Errors are localized (ASR errors vs chunk errors vs entity/merge errors).
   - Preserves contradictions instead of smoothing them over.

3. **Vault als langlebiges Zielformat (Durable Target Vault Format):**
   - Plain Markdown with `[[wikilinks]]` prevents vendor lock-in and allows Git diffs, ripgrep, and local search.
   - Distinct folder ontology (`concepts/`, `entities/`, `references/`) mirrors differing entity lifecycles.

---

## 3. Core Risks & Recommendations (Die zentralen Risiken)

1. **Terminology Correction ("Compiler" vs. Synthesis):**
   - Stage 3 (`obsidian-wiki`) is an agent-guided skill framework, not a byte-deterministic compiler. Output depends on model, temperature, system prompt, context, and existing vault state.
   - **Recommendation:** Define Stage 3 internally as **"LLM-assisted, evidence-bounded knowledge synthesis"**. Treat output as a verifiable derivative, not absolute truth.

2. **Supply Chain & Version Tracking:**
   - Document resolved dependency identities. Upstream public releases differ from local wheel/fork metadata.
   - Capture full runtime execution descriptor in every run:
     ```json
     {
       "pipeline_version": "v4",
       "git_commit": "<repository commit>",
       "python_version": "3.x.y",
       "faster_whisper_version": "x.y.z",
       "ctranslate2_version": "x.y.z",
       "asr_model_id": "exact model/revision",
       "asr_model_sha256": "<if local>",
       "wiki_distribution": "wheel|git|pypi",
       "wiki_version": "...",
       "wiki_commit_or_wheel_sha256": "...",
       "agent": "...",
       "llm_provider": "...",
       "llm_model": "...",
       "prompt_skill_hash": "..."
     }
     ```

3. **Composite Build-Key for Cache Invalidation:**
   - Source hash alone is insufficient. Cache identity must encompass:
     $$\text{build\_key} = H(\text{source\_hash} \parallel \text{normalization\_spec} \parallel \text{ASR\_identity} \parallel \text{compiler\_identity} \parallel \text{schema\_version})$$
   - Distinguish between `skip`, `recompile`, `retranscribe`, and `rebuild`.

4. **Machine-Verifiable Claim-Level Provenance:**
   - Every major claim in a concept note should carry structured evidence frontmatter:
     ```yaml
     ---
     type: concept
     schema_version: 3
     claims:
       - id: claim-01J...
         status: extracted
         review: unreviewed
         evidence:
           - source_id: youtube-abc123
             transcript_sha256: "..."
             start_ms: 734200
             end_ms: 751600
     ---
     ## Core Proposition
     The system utilizes SHA-256 manifest tracking for incremental ingestion.

     > [!evidence]
     > [[references/youtube-abc123#t=734.2-751.6]]
     ```

5. **Diarization & ASR Quality Gates:**
   - Provide an optional **Interview/Meeting Mode** with speaker diarization (e.g., WhisperX / pyannote) to prevent speaker conflation.
   - Implement measurable ASR quality metrics: detected language probability, audio duration vs. covered segment duration, VAD rejection ratio, and hallucination heuristics.

---

## 4. Target Architecture: V4 $\rightarrow$ V4.1 Hardening

```
Input Source
   │
   ├─► Immutable Source Registry (source_id, URL, timestamp, media hash, metadata snapshot)
   │
   ▼
Deterministic Media + ASR
   ├─► Audio artifact + SHA-256
   ├─► Canonical JSON segments (transcript.segments.json)
   ├─► transcript.txt / transcript.srt
   ├─► ASR run manifest + ASR quality report
   │
   ▼
Evidence Preparation
   ├─► Stable chunk IDs & transcript anchors (start_ms / end_ms)
   ├─► Chunk hashes
   ├─► Source metadata, language, optional diarization
   │
   ▼
LLM Knowledge Synthesis
   ├─► Extraction: Append-only claim candidates
   ├─► Validation: Schema + evidence anchor checks
   ├─► Merge Proposal: Explicit structured diff (never silent overwrite)
   ├─► Link Proposal: Confidence threshold / review queue
   │
   ▼
Vault Publication
   ├─► Atomic Staging (.staging/<run_id>/) ──> Validate ──> Promote
   ├─► Per-note provenance & generator build ID
   ├─► Lint + link integrity + orphan checks
   └─► Immutable Run Ledger (runs/<run_id>.json)
```

---

## 5. Prioritized Action Items (TODO Backlog)

### P0: Critical Prerequisite Tasks (Before Next Major Production Run)
- [ ] **Document Resolved Dependency Identity:** Clarify upstream vs local wheel/fork for `obsidian-wiki`, pin exact wheel SHA-256 or Git commit.
- [ ] **Implement Composite Build-Key in Manifest:** Update `.manifest.json` cache logic to include `source_sha256`, `transcript_sha256`, `pipeline_build_id`, `compiler_build_id`, and `schema_version`.
- [ ] **Implement Atomic Vault Staging & Promotion:** Ingest new notes to `knowledge/transcript-wiki/.staging/<run_id>/`, run lint/validation, and promote atomically. Never leave the vault in a half-updated state.
- [ ] **Ensure Complete Generator Materialization in `transcribe.py`:** Verify that all `faster-whisper` segments are fully materialized in memory/disk before writing success receipts.
- [ ] **Establish Immutable Raw Layer:** Ensure raw audio and segment-level ASR JSON are permanently archived and never overwritten by normalized text.
- [ ] **Create Machine-Readable Run Ledger:** Add `runs/<run_id>.json` alongside human-readable `log.md`.

### P1: Knowledge Quality & Trust Hardening
- [ ] **Enforce Claim-Level Evidence:** Ensure every extracted claim note includes `source_id`, `start_ms`/`end_ms`, and type tag (`extracted` vs `inferred`).
- [ ] **Treat Merges as Reviewable Patches:** Save newly extracted claims as candidates first; update existing concepts via structured diffs rather than silent overwrites.
- [ ] **Formalize Entity Resolution:** Implement canonical entity registries with alias maps and disambiguation rules (e.g., distinguishing "OpenAI Whisper" from generic "Whisper").
- [ ] **Canonicalize Transcript Segments as JSON:** Export format-stable `transcript.segments.json` with `segment_id`, `start_ms`, `end_ms`, `speaker`, `language`, `text_raw`, and `text_normalized`.
- [ ] **Maintain Corpus Regression Test Suite:** Standardize test runs on diverse benchmark audio (long monologues, multi-speaker dialogues, DE/EN mixed audio, noisy sources).
- [ ] **Add Optional Diarization Mode:** Integrate WhisperX/pyannote for multi-speaker interviews and panels.
- [ ] **Add ASR Quality Gates:** Measure language confidence, audio-to-segment duration ratio, and VAD drop ratio.

### P2: Scaling, Lifecycle & Governance
- [ ] **Use Semantic Search for Retrieval Only:** Keep vector/semantic search as a candidate discovery tool, not as the ground-truth evidence store.
- [ ] **Separate Source Freshness from Claim Freshness:** Track recording date vs. current validity of claims.
- [ ] **Periodic Full Rebuild Audit:** Periodically perform clean rebuilds in a separate vault to verify semantic convergence against the incremental vault.
- [ ] **Define Media Retention & Purge Policy:** Establish retention rules for downloaded media, especially for sensitive inputs.
- [ ] **Audit Licensing & Copyright Compliance:** Review copyright and data retention rules for stored full transcripts and media.

---

## 6. Original Raw Feedback Archive (German)

The raw, unedited feedback is preserved below for reference:

```text
Die Pipeline ist architektonisch stark und für einen lokalen, nachvollziehbaren Transcript-to-Knowledge-Workflow gut ausgerichtet. Ihre größte Stärke ist die klare Trennung zwischen deterministischer Medien-/ASR-Verarbeitung und der probabilistischen Wissensverdichtung; ihr größtes Risiko liegt in Stage 3/4: obsidian-wiki ist primär ein agentengesteuertes Skill-Framework, kein vollständig deterministischer Compiler mit stabiler API-Garantie.[[github](https://github.com/Ar9av/obsidian-wiki)]

Gesamturteil
Dimension	Bewertung	Begründung
Lokale Datenhoheit	9/10	Download, Audioextraktion und ASR laufen lokal. Das ist für Datenschutz, Reproduzierbarkeit und Kostenkontrolle sehr gut.
Architekturtrennung	8/10	Rohdaten/ASR-Artefakte sind sauber vom Wissensvault getrennt. Das begrenzt den Schaden fehlerhafter LLM-Synthese.
Nachvollziehbarkeit	7/10	SRT, Quellenbereiche, Manifest und Audit-Log sind die richtigen Bausteine. Die Granularität der Claim-Provenance sollte aber geprüft und wahrscheinlich erweitert werden.
Inkrementalität	7/10	SHA-256-basierte Skips sind sinnvoll, aber Hashing allein bildet keine Änderungen am Compiler, Modell oder an Extraktionsregeln ab.
Wissensqualität	6/10	Konzeptextraktion, Merging und Wikilinks sind nützlich, aber hochgradig LLM- und Prompt-abhängig; semantische Fehler können persistent werden.
Betriebssicherheit	6/10	Gute deterministische Basis, jedoch erscheint die Stage-3-Integration als Supply-Chain- und Versionsrisiko.
Skalierbarkeit	6/10	Progressive Chunk-Verarbeitung löst Kontextfenster-Probleme, aber nicht automatisch globale Konsistenz, Entitätsauflösung oder wachsendes Reprocessing.

Kurz gesagt: Als persönliches oder kleines Team-Knowledge-System ist V4 deutlich besser als ein Single-Shot-extract_wisdom-Pfad. Als „Production System“ im engeren Sinn würde ich es erst nach zusätzlichen Qualitäts-, Versions-, Sicherheits- und Wiederaufbaukontrollen so bezeichnen.

Was sehr gut ist
1. Die deterministische Grenze ist sinnvoll gezogen
Stage 1 und 2 sind genau dort deterministisch, wo sie es sein sollten:
- yt-dlp und FFmpeg erzeugen einen klaren, automatisierbaren Medieneingang.
- faster-whisper auf CPU mit int8 ist eine vernünftige Wahl, wenn lokale Verarbeitung und Ressourcenverbrauch wichtiger sind als maximale Durchsatzrate.
- Silero-VAD reduziert lange stille Passagen. faster-whisper unterstützt dies direkt; standardmäßig ist das Filtering konservativ und entfernt Stille ab zwei Sekunden, mit konfigurierbaren VAD-Parametern.[[github](https://github.com/SYSTRAN/faster-whisper)]
- transcript.txt, transcript.srt und run.log sind ein guter Minimal-Artefaktsatz. Er trennt lesbaren Inhalt, zeitliche Referenzen und Betriebsdiagnostik.

Die Wahl für faster-whisper ist technisch tragfähig: Es basiert auf CTranslate2, unterstützt CPU-int8, VAD und Zeitstempel; das Projekt weist zudem ausdrücklich darauf hin, dass die Segmentausgabe ein Generator ist und tatsächlich vollständig konsumiert werden muss, bevor ein Lauf als abgeschlossen gelten darf.[[github](https://github.com/SYSTRAN/faster-whisper)]

Wichtige operative Konsequenz: Dein transcribe.py sollte die Segmente zwingend vollständig materialisieren, bevor es Erfolg/Manifest/Artefakte schreibt. Sonst kann ein technisch erfolgreicher Prozess eine unvollständige Transkription erzeugen.

2. Die Abkehr vom Single-Shot-Extraktionsprompt ist richtig
Die Ablösung eines einzelnen „alles rein, Weisheit raus“-Prompts ist eine klare Verbesserung:
- Lange Transkripte brechen nicht mehr an einem einzelnen Kontextlimit.
- Fehler werden lokalisiert: ASR-Fehler, Chunk-Fehler, Entitätsfehler und Merge-Fehler sind unterscheidbar.
- Der Compiler kann alte und neue Evidenz zusammenführen statt jedes Mal nur eine Momentaufnahme zu erzeugen.
- Widersprüche sollen erhalten bleiben, statt glattgebügelt zu werden. Das ist für technische Entscheidungen, sich verändernde Produktinformationen und Meinungsinhalte wesentlich.

Das Upstream-Projekt beschreibt selbst einen vierstufigen Ablauf aus Ingest, Extraktion, Merge und emergenter Schemaentwicklung. Es führt außerdem Manifest-Delta-Tracking, Quellzuordnung, Linting, Cross-Linking und eine Unterscheidung zwischen extrahierten, inferierten und mehrdeutigen Aussagen als Konzept auf.[[github](https://github.com/Ar9av/obsidian-wiki)]

3. Der Vault ist ein gutes langlebiges Zielformat
Markdown plus Obsidian-Wikilinks ist ein pragmatischer, portabler Speicher:
- Kein Vendor Lock-in auf ein proprietäres Knowledge-Graph-Backend.
- Git-Diffs, Backups, lokale Suche, ripgrep, QMD oder spätere Graph-Exporte bleiben möglich.
- Der getrennte Aufbau concepts/, entities/, references/ entspricht den unterschiedlichen Lebenszyklen der Objekte.
- Ein reiner Transcript-Store bleibt von einer verdichteten, editierbaren Wissensebene getrennt.

Für einen technisch versierten Self-Hosting-Workflow passt dieses Format sehr gut.

Die zentralen Risiken
1. „Compiler“ suggeriert mehr Determinismus, als Stage 3 liefert
Das wichtigste Architekturproblem ist begrifflich und praktisch: obsidian-wiki ist laut Projektbeschreibung ein Framework aus Markdown-Skills, die von AI-Coding-Agents gelesen und ausgeführt werden. Es ist damit keine klassische, fest definierte Library-Pipeline, bei der derselbe Input unter derselben Version garantiert byteidentische Output-Dateien erzeugt.[[github](https://github.com/Ar9av/obsidian-wiki)]

Das bedeutet:
- Das Ergebnis hängt nicht nur vom Transcript ab, sondern auch von LLM-Modell, Modellversion, Temperatur, Systemprompt, Agent, Skill-Version, Kontextzustand und vorhandenen Vault-Inhalten.
- „Bounded progressive chunk reading“ verhindert Kontextüberlauf, kann aber lokale und globale Aussagen voneinander entkoppeln.
- Das Zusammenführen in bestehende Konzeptseiten ist besonders riskant: Ein fehlerhaftes Update kann frühere, korrekte Information semantisch überschreiben, ohne dass ein Dateikonflikt sichtbar wird.
- Wikilinks sind wertvoll, aber Auto-Linking kann falsche Homonyme oder zu breite Beziehungen dauerhaft verstärken.

Empfehlung: Benenne Stage 3 intern nicht „deterministic knowledge compilation“, sondern etwa:
LLM-assisted, evidence-bounded knowledge synthesis
Das schärft Betriebs- und Qualitätsanforderungen: Der Output ist ein überprüfbares Derivat, nicht die neue Wahrheitsschicht.

2. Versionsangabe und Release-Stand müssen geprüft werden
Deine Angabe obsidian-wiki v2026.8.4 ist in der öffentlich auffindbaren Upstream-Lage nicht verifizierbar. Das GitHub-Repository zeigt als neuesten Release v2026.05.3 vom 28. Mai 2026, fünf Releases insgesamt; die Repository-Seite weist zugleich „No packages published“ aus.[[github](https://github.com/Ar9av/obsidian-wiki)]

Daraus folgen drei Möglichkeiten:
- Ihr verwendet ein internes Wheel bzw. einen Fork.
- Ihr verwendet eine nicht sichtbare oder später publizierte Distribution.
- Die Dokumentation benennt Version/Paketquelle ungenau.

Das ist kein kleiner Dokumentationsfehler, sondern ein Supply-Chain- und Rebuild-Risiko. Für jeden Lauf sollte daher nicht nur obsidian-wiki==…, sondern mindestens Folgendes erfasst werden:
{ "pipeline_version": "v4", "git_commit": "<repository commit>", "python_version": "3.x.y", "faster_whisper_version": "x.y.z", "ctranslate2_version": "x.y.z", "asr_model_id": "exact model/revision", "asr_model_sha256": "<if local>", "wiki_distribution": "wheel|git|pypi", "wiki_version": "…", "wiki_commit_or_wheel_sha256": "…", "agent": "…", "llm_provider": "…", "llm_model": "…", "prompt_skill_hash": "…" }

Ein pip freeze allein genügt nicht, wenn ein Agent-Framework über symlinked Skill-Dateien und lokale Projektanweisungen arbeitet.

3. SHA-256-Cache braucht eine Build-Identität
Ein Manifest, das nur den Input-Hash speichert, erlaubt zwar schnelle Skips, ist aber fachlich unvollständig. Derselbe Transcript-Hash muss neu verarbeitet werden, wenn sich eines der folgenden Elemente ändert:
- ASR-Modell, Whisper-/CTranslate2-Version, VAD-Konfiguration oder Normalisierungsregeln.
- Chunking-Strategie, Prompt-/Skill-Dateien oder das ausführende LLM.
- Entitäts-/Konzept-Schema.
- Linker-/Merge-Logik.
- Fehlerbehebungen im Compiler.
- Sicherheits- oder Qualitätsregeln.

Die richtige Cache-Identität ist näherungsweise:
\text{build\_key} = H(\text{source\_hash} \Vert \text{normalization\_spec} \Vert \text{ASR\_identity} \Vert \text{compiler\_identity} \Vert \text{schema\_version})

Praktisch: Ergänze .manifest.json um source_sha256, transcript_sha256, pipeline_build_id, compiler_build_id, schema_version und einen pro erzeugter Note gespeicherten content_sha256.

Dann kannst du unterscheiden zwischen:
- skip: Inhalt und alle Transformationsparameter gleich.
- recompile: derselbe Transcript, aber neuer Compiler/Prompt/Schema.
- retranscribe: andere ASR- oder Audio-Normalisierung.
- rebuild: globale Regeln haben sich geändert oder der Vault ist semantisch gedriftet.

4. Provenance muss Claim-genau und maschinenprüfbar sein
Ein Ordner references/ und Transcript-Anker sind sehr gut, aber nicht ausreichend, falls Konzepte zusammengeführt werden. Du brauchst im Idealfall für jeden wichtigen Claim:
- stabile source_id;
- einen unveränderlichen transcript_revision;
- mindestens Zeitbereich start_ms/end_ms;
- optional Textspanne oder Segment-ID;
- Typ: extracted, inferred, ambiguous, operator_verified;
- Konfidenz oder besser: Review-Status;
- Zeitdimension: „im Source gesagt am …“ versus „gilt aktuell“.

Beispiel einer robusteren Note:
--- type: concept schema_version: 3 claims: - id: claim-01J... status: extracted review: unreviewed evidence: - source_id: youtube-abc123 transcript_sha256: "..." start_ms: 734200 end_ms: 751600 --- ## Kernaussage Das System verwendet SHA-256-Manifest-Tracking für inkrementelle Ingestion. > [!evidence] > [[references/youtube-abc123#t=734.2-751.6]]

Ein Satz wie „X unterstützt Y“ darf nicht ohne Herkunftsanker in einem dauerhaften Konzept landen. Das Upstream-Projekt beschreibt zwar Claim-Markierungen wie ^[inferred] und ^[ambiguous]; überprüfe aber in eurem konkreten Wheel/Fork, ob diese tatsächlich systematisch erzeugt, beibehalten und gelintet werden.[[github](https://github.com/Ar9av/obsidian-wiki)]

5. Fehlende Sprechertrennung und ASR-Qualitätskontrolle
Für Vorträge, YouTube-Content und Monologe kann die jetzige ASR-Stufe sehr gut funktionieren. Für Gespräche, Interviews, Meetings und Podcasts fehlt jedoch vermutlich mindestens eine explizite Sprechertrennung.

Ohne Diarisierung entstehen folgende Fehlerklassen:
- Aussagen verschiedener Sprecher werden zusammengezogen.
- Zitate und Zuständigkeiten werden falschen Personen zugeordnet.
- Ein Widerspruch ist eventuell nur ein Sprecherwechsel, wird aber als Sachwiderspruch gespeichert.
- Entitäten und Rollen können falsch extrahiert werden.

faster-whisper liefert Zeitstempel und kann Word-Level-Timestamps ausgeben; für Sprechertrennung verweist das Projekt allerdings auf separate Integrationen wie WhisperX oder diarization-spezifische Tools. Für deine Pipeline wäre ein optionaler „Meeting/Interview-Modus“ sinnvoll, nicht zwingend der Default.[[github](https://github.com/SYSTRAN/faster-whisper)]

Zusätzlich fehlen in der Beschreibung messbare ASR-Qualitätsgates:
- erkannte Sprache und Sprachwahrscheinlichkeit;
- Audiolänge vs. abgedeckte Segmentdauer;
- Anteil von VAD-verworfener Zeit;
- Wiederholungs-/Halluzinationsheuristiken;
- Leere oder ungewöhnlich kurze Transkripte;
- stichprobenhafte manuelle WER-/CER-Referenzsets je Quelltyp und Sprache.

Konkrete Zielarchitektur
Ich würde V4 nicht ersetzen, sondern zu V4.1 härten:
Input source │ ├─ Immutable source registry │ source_id, URL, capture timestamp, media hash, metadata snapshot │ ▼ Deterministic media + ASR │ ├─ audio artifact + SHA-256 ├─ canonical JSON segments ├─ transcript.txt / .srt ├─ ASR run manifest └─ ASR quality report │ ▼ Evidence preparation │ ├─ stable chunk IDs and transcript anchors ├─ chunk hashes ├─ source metadata and language └─ optional diarization │ ▼ LLM knowledge synthesis │ ├─ extraction: append-only claim candidates ├─ validation: schema + evidence checks ├─ merge proposal: explicit diff, never silent overwrite └─ link proposal: confidence threshold / review queue │ ▼ Vault publication │ ├─ atomic staging → validate → promote ├─ per-note provenance and generator build ID ├─ lint + link integrity + orphan checks ├─ semantic diff report └─ immutable run ledger

Der entscheidende Unterschied: Extraktion, Validierung, Merge und Veröffentlichung werden getrennte Zustände. Gerade beim Merge darf ein LLM nicht stillschweigend die kanonische Fassung umschreiben.

Priorisierte Maßnahmen
P0: Vor dem nächsten breiten Produktionslauf
1. Aufgelöste Dependency-Identität dokumentieren.
Kläre, ob v2026.8.4 ein internes Artefakt, Fork oder ein abweichender Paketname ist. Pinne Wheel-Hash oder Git-Commit, nicht nur einen beweglichen Namen. Die öffentlich sichtbare Upstream-Release-Lage weist derzeit v2026.05.3 als Latest aus.[[github](https://github.com/Ar9av/obsidian-wiki)]
2. Build-Key statt reinem Source-Hash einführen.
Cache-Invaliderung muss ASR-, Compiler-, Prompt-/Skill- und Schema-Version umfassen.
3. Atomare Veröffentlichung umsetzen.
In knowledge/transcript-wiki/.staging/<run_id>/ schreiben, vollständig linten, dann per Rename/Commit veröffentlichen. Ein abgebrochener LLM-Lauf darf keinen halbaktualisierten Vault hinterlassen.
4. Immutable Raw Layer einführen.
Die Originalaudio-Datei beziehungsweise ein dauerhaft adressierbarer lokaler Verweis sowie Roh- bzw. segmentiertes ASR-JSON dürfen niemals durch „clean text“ ersetzt werden.
5. Maschinenlesbares Run Ledger ergänzen.
log.md ist gut für Menschen; ergänze runs/<run_id>.json für Abfragen, Rebuilds und Incident-Analyse.

P1: Qualität des Wissens erhöhen
1. Claim-Level-Evidence erzwingen.
Keine Fakt- oder Architekturbehauptung ohne source_id und Zeitanker; keine abgeleitete Aussage ohne Kennzeichnung inferred.
2. Merge als Review-fähigen Patch behandeln.
Neu extrahierte Claims zuerst als Kandidaten speichern; bestehende Konzepte per strukturiertem Diff aktualisieren. Kritische Änderungen können in eine Review-Queue gehen.
3. Entity Resolution formalisieren.
Für Personen, Organisationen, Repositories und Tools stabile IDs, Aliaslisten und Disambiguierungsregeln verwenden. OpenAI, „OpenAI Whisper“ und ein gleichnamiges lokales Tool dürfen nicht durch reine Textähnlichkeit kollabieren.
4. Transkriptsegmente als JSON kanonisieren.
Neben TXT und SRT empfehle ich ein formatstabiles transcript.segments.json mit segment_id, start_ms, end_ms, speaker, language, text_raw, text_normalized und optional Word-Timestamps.
5. Korpusbasierte Regressionstests pflegen.
Die Bake-off-Idee sollte in eine dauerhafte Test-Suite übergehen: lange Monologe, Dialoge, Deutsch/Englisch-Mischung, schlechte Audioqualität, technische Eigennamen, widersprüchliche Quellen und Wieder-Ingest desselben Inhalts.

P2: Skalierung und Bedienbarkeit
1. Verwende semantische Suche nur als Retrieval- und Kandidatenhilfe, nicht als alleinige Evidenzinstanz.
2. Führe „source freshness“ getrennt von „claim freshness“. Ein alter Vortrag kann historisch wertvoll, aber faktisch veraltet sein.
3. Erzeuge periodisch einen vollständigen Rebuild in einem separaten Zielvault und vergleiche ihn semantisch mit dem inkrementell gewachsenen Vault.
4. Ergänze eine Lösch- und Retention-Strategie für heruntergeladene Medien, vor allem bei sensitiven Quellen.
5. Prüfe Lizenz-, Nutzungs- und Urheberrechtsfragen bei gespeicherten Downloads und dauerhaft abgelegten Volltranskripten, insbesondere wenn der Vault geteilt oder veröffentlicht wird.

Fazit
Die Grundentscheidung ist richtig: lokale ASR + persistente, quellengestützte Markdown-Wissensbasis ist der richtige Gegenentwurf zu flüchtigen Einmalzusammenfassungen und externen Black-Box-Workflows. faster-whisper mit CPU-int8 und Silero-VAD ist dafür eine belastbare technische Basis.[[github](https://github.com/SYSTRAN/faster-whisper)]

Ich würde aber zwei Aussagen aus der aktuellen Beschreibung abschwächen:
1. Stage 3 ist kein deterministischer Compiler, sondern ein agentisch/LLM-getriebener Syntheseschritt.
2. SHA-256-Incrementality ist erst dann fachlich korrekt, wenn der Hash auch alle transformationsrelevanten Versionen und Regeln einbezieht.

Mit Build-Identität, atomarem Publish, Claim-Evidence, schema-versioniertem Manifest, ASR-Qualitätsgates und diff-basierten Merges wird aus einer sehr guten persönlichen Pipeline ein wirklich belastbares, langfristig wartbares Wissenssystem.
```
