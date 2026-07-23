# 1. New canonical phase model

```
PHASE 0 — SETUP
Define and lock what the run is supposed to do.

PHASE 1 — DETERMINISTIC CORPUS INTELLIGENCE
Map the Leela corpus mechanically and prepare bounded semantic inputs.

PHASE 2 — SEMANTIC COMPILATION
Read, interpret, reconcile, and compile durable knowledge.

PHASE 3 — FINISH AND PROVE
Independently evaluate, validate, index, and close the run.
```

## Old and new terminology

|New phase|Contains previous terminology|
|---|---|
|**Phase 0 — Setup**|Previous Step 0, intake, intent lock, scaffold, configuration, preflight|
|**Phase 1 — Deterministic**|Previous Phase 0 corpus intelligence and source intake|
|**Phase 2 — Semantic**|Previous semantic Phase 1 analysis plus semantic Phase 2 compilation|
|**Phase 3 — Finish**|Semantic acceptance, deterministic postflight, retrieval rebuild, completion|

This prevents the confusing situation where “Phase 0” meant corpus analysis even though substantial setup happened before it.

---

# 2. Whole live-development flow

```
Leela source folder
C:\GitDev\leela\LeelaAppDevelopment
        │
        ▼
┌──────────────────────────────┐
│ PHASE 0 — SETUP              │
│ Define target and contracts  │
└──────────────┬───────────────┘
               │ approved inputs
               ▼
┌──────────────────────────────┐
│ PHASE 1 — DETERMINISTIC      │
│ Inventory and corpus maps    │
└──────────────┬───────────────┘
               │ bounded evidence packs
               ▼
┌──────────────────────────────┐
│ PHASE 2 — SEMANTIC           │
│ Understand and compile KB    │
└──────────────┬───────────────┘
               │ compiled pages and claims
               ▼
┌──────────────────────────────┐
│ PHASE 3 — FINISH             │
│ Evaluate, index, prove       │
└──────────────┬───────────────┘
               │
               ▼
     Tested Apex KB process
     + first real Leela KB
     + evidence for corrections
```

---

# 3. Phase 0 module — Setup

## Purpose

Phase 0 answers:

> What exactly are we building, from which sources, for which questions, into which target, using which execution options?

Nothing expensive should happen until these decisions are understandable and approved.

## Phase 0 steps

|Step|Concrete purpose|Likely existing Apex capability|Live test activity|
|---|---|---|---|
|0.1|Read the minimal Apex KB overview|Current `SKILL.md` summary and operating contract|Understand Apex KB boundaries|
|0.2|Define the Leela canary run|Intake/run configuration|Set source and target paths|
|0.3|Define KB identity and intended value|Run intent fields|Define what future AIs must understand|
|0.4|Define the first topic or topic set|Topic registry|Lock exact target questions|
|0.5|Decide source handling|Pointer/copy/snapshot support|Usually use repository pointers|
|0.6|Select output depth|Existing output tiers|Analysis-only, compiled, or query-ready|
|0.7|Validate paths and capabilities|Existing preflight/control logic|Check paths, runtime, overlap, Git state|
|0.8|Show operator readback|Existing confirmation gate|You correct any misunderstanding|
|0.9|Lock approved inputs|Existing run intent/state or corrected replacement|Freeze the canary configuration|
|0.10|Create only required target scaffold|Existing scaffold command|Establish target KB structure|

## Primary Phase 0 information flow

```
Operator answers
      ↓
Run configuration / run intent
      ↓
Preflight checks
      ↓
Operator readback
      ↓
Confirmed canonical run configuration
      ↓
Run state and target scaffold
```

## Main files to review in the Phase 0 chat

These are candidates, not automatically all retained:

1. Operator run configuration or existing `run-intent.md`
2. Topic registry
3. Run state
4. Stage-result output
5. Welcome/intake projection
6. Preflight report
7. Any scaffold template directly consumed by the scripts

The Phase 0 chat must decide whether the new workpack’s proposed `run-config.okf.json` and `run-manifest.json` improve the existing `run-intent.md` model or merely duplicate it. The current live system already treats `run-intent.md`, `run-state.json`, and `topic-registry.json` as canonical paths.

---

# 4. Phase 1 module — Deterministic corpus intelligence

## Purpose

Phase 1 answers:

> What files exist, where is the topic discussed, why did each source match, which sources are duplicates or versions, and what bounded evidence should semantic AI receive?

This module does not decide what sources mean.

## Phase 1 steps

|Step|Concrete purpose|Output value|
|---|---|---|
|1.1|Register or point to every in-scope source|Complete source custody|
|1.2|Inventory every file|No silent omissions|
|1.3|Hash files|Stable identity and duplicate detection|
|1.4|Extract structural facts|Titles, headings, sections, links, dates|
|1.5|Identify exact duplicates and possible versions|Prevent repeated reading|
|1.6|Build topic-specific postings|Know where phrases and aliases occur|
|1.7|Rank or classify every candidate with reasons|Navigation, not semantic authority|
|1.8|Produce corpus and per-topic statistics|Operator visibility|
|1.9|Generate concentrated work packs|Small semantic input|
|1.10|Generate Phase 2 semantic instructions|Exact AI assignment|
|1.11|Validate deterministic outputs|Reconcile counts and paths|

The mechanistic pack currently proposes eight Phase 1-style outputs, including inventory, source facts, heading map, duplicate map, rankings, work packs, and statistics.

The module review must determine whether all eight are independently useful or whether some should be:

- combined;
- generated views;
- retained only as internal structures;
- removed because an existing Apex artifact already provides the same value.

## Main information flow

```
Locked Phase 0 configuration
          ↓
Source intake and inventory
          ↓
Structure / hash / duplicate extraction
          ↓
Topic candidate mapping
          ↓
Statistics and work pack
          ↓
Generated semantic assignment
```

---

# 5. Phase 2 module — Semantic compilation

## Purpose

Phase 2 answers:

> What do the sources actually mean, which are authoritative or historical, where do they disagree, and what durable knowledge should future AIs read?

This phase contains two internal semantic subphases, but they belong in one module because they form one continuous meaning-making process.

## Phase 2A — Source and topic analysis

|Step|Purpose|
|---|---|
|2.1|Read one bounded source batch|
|2.2|Determine actual relevance|
|2.3|Assess source role and authority|
|2.4|Record target-question coverage|
|2.5|Extract claims with exact pointers|
|2.6|Preserve contradictions and uncertainty|
|2.7|Classify current, historical, proposed, prototype, duplicate, or incidental value|
|2.8|Identify concept/entity candidates|
|2.9|Update cumulative topic analysis|
|2.10|Continue only while unresolved questions justify another source batch|

## Phase 2B — Durable compilation

|Step|Purpose|
|---|---|
|2.11|Determine minimum useful page topology|
|2.12|Compile the topic dossier|
|2.13|Compile the complete source atlas|
|2.14|Create concept/entity pages only when independently useful|
|2.15|Preserve Macro/Meso/Micro distinctions|
|2.16|Preserve claim, source, version, and contradiction provenance|
|2.17|Reread and repair outputs|
|2.18|Return exact semantic completion artifacts|

## Main information flow

```
Phase 1 work pack
      +
locked questions
      +
generated semantic instructions
          ↓
Bounded source analysis batches
          ↓
Cumulative topic analysis
          ↓
Compiled dossier + source atlas
          ↓
Candidate pages and audit items
```

The live skill already says the semantic worker must treat Phase 0 rankings only as navigation, preserve unopened sources as non-evidence, continue while readable sources can resolve critical questions, and create answer-bearing Phase 2 pages.

---

# 6. Phase 3 module — Finish and prove

## Purpose

Phase 3 answers:

> Does the KB actually work, are the claims supported, can future AIs answer the target questions, and are all deterministic artifacts healthy?

## Phase 3 steps

|Step|Purpose|
|---|---|
|3.1|Structural validation|
|3.2|Independent semantic acceptance|
|3.3|Reason-coded repair loop|
|3.4|Build wiki index|
|3.5|Build retrieval index|
|3.6|Run strict lint and quality checks|
|3.7|Verify retrieval freshness|
|3.8|Produce final statistics|
|3.9|Assign truthful completion state|
|3.10|Record lessons about the Apex KB process|
|3.11|Close the canary run|

## Main information flow

```
Compiled KB pages
       ↓
Independent semantic evaluation
       ↓
Repair if necessary
       ↓
Index + retrieval + lint + postflight
       ↓
Completion evidence
       ↓
Apex KB process improvements
```

The live Apex KB already reserves `query_ready` for runs that pass semantic acceptance, deterministic postflight, and retrieval freshness.