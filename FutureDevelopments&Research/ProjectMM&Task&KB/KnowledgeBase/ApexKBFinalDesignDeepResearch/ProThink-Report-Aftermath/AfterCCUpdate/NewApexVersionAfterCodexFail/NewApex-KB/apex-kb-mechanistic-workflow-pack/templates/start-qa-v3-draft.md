# Apex KB Start Q&A — Deterministic-First Draft

## Status

```yaml
schema: apex.kb.start-qa.v3-draft
status: operator_review_required
scope: phase_0_setup_start_only
render_policy: fixed_verbatim
runtime_authority: none
creates_files_when_rendered: false
next_expected_action: operator_fills_run_configuration
```

This is the proposed fixed response to:

```text
apexkb start
```

The message is designed to be printed from a versioned file. It must not be rewritten, shortened, expanded, or reinterpreted by an AI during normal use.

---

# Start an Apex KB run

This setup defines **what sources Apex KB may inspect, where the KB will live, which topics and questions it must cover, and how far the run should go**.

Nothing is copied, analyzed, indexed, or written into the target KB during this step.

## What happens after you fill the configuration

1. The configuration is checked against a fixed schema.
2. A read-only preflight checks the selected repositories, folders, exclusions, formats, runtime capabilities, and likely workload.
3. You receive one compact report with facts, warnings, blockers, expected outputs, and lightweight statistics.
4. You revise the same configuration or confirm it.
5. Only after confirmation is the configuration fingerprinted, state initialized, and the minimum KB scaffold created.

## Choose the setup assistance mode first

### `deterministic_only` — recommended default

The runtime validates and inspects exactly what you entered. It reports facts, warnings, and blockers but does not suggest different topics, questions, folders, or settings.

**Value:** lowest drift risk, fully reproducible setup, no AI interpretation.

**Tradeoff:** you make every substantive choice yourself.

### `ai_recommendations`

The same deterministic preflight runs first. A bounded AI may then explain warnings and recommend changes for your review.

**Value:** useful when options or warnings are difficult to evaluate.

**Tradeoff:** adds interpretation risk and extra review work.

The AI cannot edit the configuration, invent topics, broaden scope, select folders, or confirm the run. Every recommendation must cite the deterministic fact that triggered it.

---

# Fields to fill

## 1. Source repository and folders

Specify where the original source materials live.

```text
source_repository: owner/repository
source_ref: branch, tag, or commit
source_roots:
  - repository-relative/folder
```

**Choose:**

- One narrow folder when the topic is concentrated there.
- Several folders when each contains necessary evidence.
- The repository root only when the full repository is genuinely in scope.

**Effect:** broader roots increase file counts, runtime, noise, and later semantic reading. Narrow roots reduce cost but can omit relevant evidence.

**Rule:** the KB output folder must not be inside an indexed source root unless it is explicitly excluded.

---

## 2. Target repository and KB folder

Specify where Apex KB may create generated artifacts.

```text
target_repository: owner/repository
target_ref: branch or working ref
target_kb_root: repository-relative/folder
```

**Recommended pattern:**

```text
apex-meta/kb/<kb-slug>
```

**Effect:** this folder becomes the permanent home of manifests, deterministic maps, semantic analyses, compiled pages, audits, and derived retrieval artifacts.

**Preflight checks:** existence, overlap with sources, write capability, existing contents, nested repositories, and likely collisions.

---

## 3. KB identity

Provide a stable machine name and a plain description.

```text
kb_slug: lowercase-kebab-case
kb_title: Human-readable title
kb_identity: One sentence describing what this KB is about
```

**Value:** prevents later stages from guessing the KB subject from filenames or chat history.

**Good identity:**

> This KB explains the Apex KB architecture, lifecycle, implementation history, and source evidence.

**Avoid:** broad aspirations such as “make everything understandable.”

---

## 4. Topic list

List the topics that this run must map and later compile.

```text
topics:
  - topic_id: stable-kebab-case-id
    name: Human-readable topic name
```

**Default recommendation:** begin with the smallest useful set of explicitly known topics.

**Effect:** every topic receives deterministic candidate mapping and later bounded semantic work. More topics increase Phase 1 and Phase 2 work substantially.

**Rule:** Apex KB does not add, merge, rename, or broaden topics automatically.

---

## 5. Topic vocabulary

For each topic, provide the deterministic vocabulary used to find candidate files and sections.

```text
phrases:
  - strong exact phrase
aliases:
  - alternative established name
supporting_terms:
  - term useful only with stronger context
ambiguous_terms:
  - broad term that may create false positives
negative_terms:
  - term or phrase that should reduce or exclude a match
```

### `phrases`

Strong names that should independently create a meaningful candidate signal.

**Example:** `skill tree`

### `aliases`

Established alternative names for the same topic.

**Example:** `spatial skill tree`

### `supporting_terms`

Words that help when they occur with a phrase, alias, or strong structural signal. They should not independently flood the candidate set.

### `ambiguous_terms`

Words that may be relevant but are too broad to trust alone.

**Example:** `tree`

### `negative_terms`

Known unrelated uses or contexts that should be flagged or down-weighted.

**Important:** deterministic vocabulary finds candidates; it does not prove semantic relevance or authority.

---

## 6. Target questions

For each topic, list the exact questions the completed KB must answer.

```text
priority_questions:
  - question_id: stable-question-id
    priority: critical | routine | supporting
    question: Exact question
    answer_requirements:
      - required part of the answer
```

### Priorities

- `critical` — the KB cannot pass semantic acceptance if this remains unanswered.
- `routine` — expected future-use question; should normally be answerable from compiled pages.
- `supporting` — useful context but not a completion blocker by itself.

**Value:** questions define the required semantic result and later acceptance test.

**Rule:** scripts and AI cannot replace or silently rewrite them. In AI recommendation mode, wording suggestions must preserve the original question beside the suggestion.

---

## 7. Explicit exclusions

List folders or files that must not be analyzed, each with a reason.

```text
explicit_exclusions:
  - path: repository-relative/path
    reason: generated_output | dependency | cache | archive | irrelevant | other explanation
```

**Typical exclusions:** generated KB output, dependencies, build output, caches, vendored files, large irrelevant archives, previous generated indexes.

**Value:** makes omissions visible and prevents recursive indexing.

**Rule:** an excluded path remains visible in the preflight report with its exclusion reason and estimated excluded file count where cheaply available.

---

## 8. Source handling

Choose how the KB refers to or stores source material.

### `pointer_only` — recommended for repository sources

The KB records durable repository paths, refs, identities, and hashes without copying the corpus.

**Value:** lowest storage cost; avoids duplicate corpora.

**Tradeoff:** future use depends on continued source-repository access and stable references.

### `copy_into_kb`

Copies approved sources into KB custody.

**Value:** self-contained KB source custody.

**Tradeoff:** higher storage use, duplicate management, and update complexity.

### `snapshot_copy`

Creates a point-in-time source snapshot tied to the run.

**Value:** strongest reproducibility for a historical or audit-sensitive run.

**Tradeoff:** highest storage use and no automatic freshness after the snapshot.

```text
source_storage_mode: pointer_only | copy_into_kb | snapshot_copy
```

---

## 9. Deterministic corpus-intelligence depth

Choose how much mechanical mapping Phase 1 should perform before semantic analysis.

### `quick`

Basic inventory, formats, titles, headings, and simple phrase signals.

**Best for:** small, clean, well-known corpora.

**Value:** fastest and cheapest.

**Tradeoff:** weaker discovery, duplicate, date, and version intelligence.

### `standard` — recommended default

Inventory, structure, field-separated topic signals, duplicates, dates when available, candidate maps, work packs, and statistics.

**Best for:** normal project and documentation KBs.

**Value:** strong balance of discovery, auditability, and cost.

### `deep`

Standard mapping plus configured expensive extraction, broader format handling, and process/graph signals.

**Best for:** large, highly versioned, or relationship-heavy corpora.

**Tradeoff:** greater runtime and implementation dependency risk. Deep does not make semantic judgments.

```text
corpus_profile: quick | standard | deep
```

---

## 10. Git date handling

Choose whether Git history should contribute deterministic change-date signals.

### `off`

Do not inspect Git dates.

### `when_available` — recommended default

Use Git dates where the repository and selected ref permit it; continue with visible warnings when unavailable.

### `required`

Block the run when reliable Git date evidence cannot be obtained.

```text
git_dates: off | when_available | required
```

**Important:** dates are freshness clues, not proof that a source is current or authoritative.

---

## 11. Graph and relationship signals

Choose which explicit file relationships should contribute to deterministic discovery.

### `off`

No relationship-derived candidate signals.

**Best for:** simple corpora where paths, titles, headings, and text are sufficient.

### `links_only`

Include Markdown links, wiki links, and resolved file references.

**Value:** finds linked context and navigation hubs at relatively low cost.

### `full_process_edges`

Include configured links plus YAML fields, path relationships, dependency references, workflow handoffs, and contract/process edges.

**Value:** highest relationship visibility for orchestration or architecture corpora.

**Tradeoff:** more parsing rules, more false-positive risk, and higher maintenance cost.

```text
graph_signals: off | links_only | full_process_edges
```

---

## 12. Non-text files

Choose how unsupported or extraction-limited formats are handled.

### `inventory_and_report` — safe default

Record every file and its format, but do not silently claim its content was analyzed. The report identifies formats requiring another extractor or manual route.

### `extract_when_supported`

Use installed deterministic extractors when available; report every extraction failure.

### `block_on_unsupported`

Stop when any in-scope file cannot be read through an approved extraction route.

```text
non_text_policy: inventory_and_report | extract_when_supported | block_on_unsupported
```

**Tradeoff:** stricter modes improve completeness guarantees but can block otherwise useful runs because of a small number of difficult files.

---

## 13. Output tier

Choose the intended stopping point.

### `analysis_only`

Stop after deterministic corpus intelligence and validated semantic source/topic analysis. No durable compiled wiki is required.

**Creates value through:** source understanding, candidate dispositions, contradictions, and an evidence-backed analysis layer.

**Does not create:** finished concept pages or a query-ready KB.

### `compiled_kb`

Create semantically accepted durable concept dossiers, source atlases, and supporting pages.

**Creates value through:** a maintained future-AI reading surface that should replace routine raw-source rereading.

**Does not guarantee:** a fresh deterministic retrieval index unless separately included by the final contract.

### `query_ready`

Create and accept the compiled KB, complete deterministic postflight, and build or refresh the approved retrieval surface.

**Creates value through:** direct future querying over accepted compiled knowledge.

**Tradeoff:** highest runtime and strongest completion requirements.

```text
output_tier: analysis_only | compiled_kb | query_ready
```

---

## 14. Preflight assistance

```text
preflight_assistance: deterministic_only | ai_recommendations
```

Choose `deterministic_only` unless you specifically want a bounded explanation and recommendation layer after the factual report.

---

## 15. Preflight report detail

### `compact` — recommended default

Shows status, blockers, warnings, key statistics, selected options, and expected outputs.

### `detailed`

Adds format tables, top folders, largest files, exclusion counts, weak topic signals, capability details, and all recommendations.

```text
preflight_detail: compact | detailed
```

The complete machine-readable preflight remains available regardless of display level.

---

## 16. Special constraints

List run-specific rules that are not represented above.

```text
special_constraints:
  - Never modify the source repository
  - Preserve historical and prototype sources
  - Do not treat dates as authority
```

**Rule:** constraints must be testable or operationally meaningful. Broad wishes belong in target questions or KB identity, not here.

---

# Exact operator configuration draft

Save the following as a new draft configuration and replace all placeholder values.

```json
{
  "schema": "apex.kb.run-config.v3-draft",
  "schema_version": "3-draft",
  "config_revision": 1,
  "run_kind": "new_kb",
  "preflight_assistance": "deterministic_only",
  "kb": {
    "slug": "replace-with-kb-slug",
    "title": "Replace with KB title",
    "identity": "This KB explains ..."
  },
  "sources": {
    "repository": "owner/repository",
    "ref": "main",
    "roots": [
      "repository-relative/source-folder"
    ],
    "explicit_exclusions": [
      {
        "path": "repository-relative/excluded-path",
        "reason": "generated_output"
      }
    ],
    "storage_mode": "pointer_only",
    "follow_symlinks": false,
    "duplicate_policy": "representative_plus_all_paths"
  },
  "target": {
    "repository": "owner/repository",
    "ref": "main",
    "kb_root": "apex-meta/kb/replace-with-kb-slug"
  },
  "topics": [
    {
      "topic_id": "primary-topic",
      "name": "Primary Topic",
      "phrases": [
        "strong exact phrase"
      ],
      "aliases": [],
      "supporting_terms": [],
      "ambiguous_terms": [],
      "negative_terms": [],
      "priority_questions": [
        {
          "question_id": "primary-topic-current-definition",
          "priority": "critical",
          "question": "What is the current definition and scope of this topic?",
          "answer_requirements": [
            "current definition",
            "scope and ownership",
            "current versus proposed distinction"
          ]
        }
      ]
    }
  ],
  "deterministic": {
    "corpus_profile": "standard",
    "git_dates": "when_available",
    "graph_signals": "off",
    "non_text_policy": "inventory_and_report"
  },
  "outputs": {
    "tier": "query_ready"
  },
  "operator_display": {
    "preflight_detail": "compact"
  },
  "special_constraints": [
    "Never modify source materials"
  ],
  "safety": {
    "fail_closed": true
  }
}
```

## Submit the draft

```text
apexkb start --config <path-to-run-config.json>
```

The command must return one of:

```text
INVALID_CONFIGURATION
PREFLIGHT_BLOCKED
READY_TO_CONFIRM
```

No later phase may start from this command without a separate explicit confirmation action.

---

# Required preflight summary

Before confirmation, the compact report should show:

```text
STATUS
Selected repositories and refs
Source roots and target root
Source/output overlap result
Runtime capability result
Files and bytes in scope
Counts by major format
Excluded paths and estimated excluded files
Unreadable and unsupported files
Largest-file warnings
Symlink, hidden, generated, cache, and dependency candidates
Weak path/filename signals for each operator topic
Selected source handling, corpus profile, graph depth, output tier, and assistance mode
Expected deterministic outputs
Expected semantic/final outputs
Blockers
Warnings
Exact confirmation or revision instruction
```

These are factual setup signals. They must not be presented as semantic relevance, source authority, expected answer quality, or guaranteed business value.

---

# AI recommendation guardrail

When `preflight_assistance` is `ai_recommendations`, the AI receives only:

1. the operator configuration;
2. the deterministic preflight report;
3. this option guide.

Every recommendation must use this format:

```text
RECOMMENDATION ID:
TRIGGERING FACT:
CURRENT OPERATOR VALUE:
SUGGESTED VALUE OR WORDING:
EXPECTED EFFECT:
TRADEOFF:
OPERATOR ACTION REQUIRED: accept | reject | edit manually
```

The AI must output `NO_RECOMMENDATION` when the deterministic evidence does not justify a change.

The AI cannot write the configuration or invoke confirmation.
