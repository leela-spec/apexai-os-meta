# Apex KB Start Q&A — Option A v3

```yaml
schema: apex.kb.start-qa.option-a.v3
status: operator_review_required
scope: phase_0_setup_start_only
layout: compact_markdown_with_guided_yaml
render_policy: fixed_verbatim
runtime_authority: frontend_input_only
creates_files_when_rendered: false
```

# Your about to start an Apex KB run

The Apex-KB skill will index a Knowledge Base and make it efficiently retrievable for AI

This setup defines:
- **what sources** Apex KB may inspect
- **where** the KB will live
- **which topics and questions** it must cover,
- and how **detailed** the run should be.

For that we will write a configuration of the Apex-KB run depending on your needs.

Nothing is copied, indexed, or written during this step.

## Terms used below

| Term | Meaning |
|---|---|
| **Source corpus** | Existing repository folders that Apex KB will inspect and index |
| **KB destination** | The folder in the same repository where Apex KB will save generated manifests, indexes, analyses, compiled pages, and retrieval artifacts |

The repository is stated once. Source folders and the KB destination are repository-relative paths inside it.

Apex KB uses `main` first. Other available branches or worktrees are inspected only when the selected source appears missing, contradictory, or clearly incomplete. Branch selection is not an operator field.

## 1. Fill the run configuration

The block is prefilled with a fictional example for **Velvet Vice**, a kinky cocktail bar with consent-based spanking sessions.

**Before submitting:** replace every example value with your real values. Keep the field names and indentation. Empty optional lists should be written as `[]`; do not leave half-deleted bullets.

```yaml
repository: "velvet-vice/bar-operations"
# EFFECT: Apex KB searches only this repository. It does not search unrelated repositories.

source_folders:
  # Add every repository folder that contains evidence for the KB.
  # EFFECT: Files below these folders become eligible for inventory and topic matching.
  # EFFECT: Files outside these folders are not searched unless the later preflight identifies a clear evidence gap and asks for review.
  - "operations"
  - "menus-and-cocktails"
  - "consent-and-play-guidelines"

exclusions:
  # Keep `exclusions: []` when nothing should be excluded.
  # Each exclusion is a machine-readable path plus a stable reason code.
  # EFFECT: Matching files remain visible in counts but are not opened or indexed as evidence.
  - path: "operations/generated-reports"
    reason: "generated_output"
  - path: "menus-and-cocktails/archive/duplicate-exports"
    reason: "duplicate_export"

kb_destination:
  # The generated Apex KB will live here. This folder must not overlap the source folders.
  # EFFECT: Manifests, analyses, compiled pages, audits, and retrieval files are created below this path after confirmation.
  folder: "apex-meta/kb/velvet-vice-operations"

topics:
  # Add one list item for every subject the completed KB must cover.
  # Every topic keeps its phrases, negative terms, and questions together.

  - name: "Cocktail program and service"
    # EFFECT: Creates one topic route and later one bounded semantic workstream.

    phrases:
      # Strong names that may independently surface candidate files or sections.
      # EFFECT: More precise phrases increase recall for this topic without broadly matching every bar-related file.
      - "signature cocktail menu"
      - "cocktail preparation standards"
      - "responsible alcohol service"

    ambiguous_or_negative_terms:
      # Broad, obsolete, test, or unrelated language that should not count as strong evidence by itself.
      # EFFECT: Reduces false positives; it does not automatically delete a file from review.
      - "sample cocktail"
      - "old menu"
      - "staff party drinks"

    questions:
      # Exact questions the compiled KB must answer and later acceptance must test.
      # EFFECT: A query-ready run cannot pass if critical questions remain unanswered.
      - "Which cocktails are currently offered and how are they prepared?"
      - "Which service and intoxication-safety rules apply?"
      - "Which menu files are current, historical, or conflicting?"

  - name: "Consent-based spanking sessions"
    # EFFECT: Creates a separate topic so consent rules are not diluted inside general venue operations.

    phrases:
      - "spanking session"
      - "explicit consent protocol"
      - "safe word procedure"
      - "aftercare guidance"

    ambiguous_or_negative_terms:
      - "joke punishment"
      - "disciplinary warning"
      - "deprecated consent form"

    questions:
      - "How must guests and staff establish and withdraw consent?"
      - "Which safety, hygiene, safe-word, and aftercare procedures apply?"
      - "Who may facilitate a session and what conduct is prohibited?"
      - "Which documents define the current process and which are obsolete?"

run_options:
  # Keep exactly one value after each colon; delete the alternatives.
  source_handling: pointer_only / copy_into_kb / snapshot_copy
  detail: quick / standard / deep
  output: analysis_only / compiled_kb / query_ready
  non_text: inventory_and_report / extract_when_supported / block_on_unsupported
  ai_help_after_preflight: false / true
```

## 2. Option guide

| Setting | Option | Use when | Effect |
|---|---|---|---|
| **Source handling** | `pointer_only` **default** | Sources remain in the repository | Stores paths, repository state, and hashes without duplicating files |
|  | `copy_into_kb` | The generated KB must hold approved source copies | More storage and update management |
|  | `snapshot_copy` | A fixed historical evidence set is required | Strongest reproducibility; highest storage cost |
| **Run detail** | `quick` | The corpus is small and already understood | Inventory, formats, headings, and basic phrase matches |
|  | `standard` **default** | Normal project or documentation KB | Structured topic matching, duplicates, dates when available, work packs, and statistics |
|  | `deep` | The corpus is large, highly versioned, or relationship-heavy | Standard processing plus broader extraction and configured relationship analysis |
| **Output** | `analysis_only` | You need deterministic maps and reviewed semantic analysis only | Stops before durable compiled pages |
|  | `compiled_kb` | Future AIs should read durable dossiers and source atlases | Creates accepted compiled knowledge without requiring final retrieval |
|  | `query_ready` **default** | The KB should be directly searchable after completion | Adds final validation and the retrieval index |
| **Non-text files** | `inventory_and_report` **default** | Unsupported formats may exist | Lists every file and reports unsupported content honestly |
|  | `extract_when_supported` | Approved extractors may process PDFs or office documents | Uses available extractors and reports every failure |
|  | `block_on_unsupported` | Complete extraction is mandatory | Stops when any in-scope file cannot be processed |
| **AI help after preflight** | `false` **default** | You want deterministic facts only | Lowest drift risk; no AI recommendation layer |
|  | `true` | You want help interpreting factual warnings or option tradeoffs | AI may explain and recommend, but cannot edit or approve the configuration |

## 3. AI recommendation boundary

When `ai_help_after_preflight` is `true`, every recommendation must show:

| Required field | Meaning |
|---|---|
| Triggering fact | Exact preflight result that caused the recommendation |
| Current value | Current operator setting |
| Suggested change | One explicit proposed edit |
| Expected effect | What should improve |
| Tradeoff | Cost or risk introduced |
| Operator action | Accept, reject, or edit |

AI may explain or recommend. It may not choose the repository, source folders, KB destination, topics, phrases, exclusions, questions, output level, or confirmation on the operator's behalf.

## 4. What happens next

1. The frontend parses this operator configuration and rejects malformed YAML, leftover slash alternatives, example placeholders, empty topic names, or incomplete exclusion rows.
2. It derives internal machine fields such as run ID, KB slug, topic slugs, execution route, corpus breadth, output rationale, and provisional target commit without asking the operator to author them.
3. The derived configuration is validated against the canonical runtime schemas.
4. A read-only preflight checks the repository, source folders, KB destination, overlap, formats, capabilities, exclusions, and likely workload.
5. Apex KB uses `main` first and investigates other available branches or worktrees only when the configured evidence appears incomplete or contradictory.
6. The operator receives one compact readback containing both the submitted values and every derived value that materially affects the run.
7. When AI help is enabled, recommendations appear after deterministic facts and remain non-binding.
8. The operator revises this same configuration or confirms it.
9. Only after confirmation are the configuration fingerprint, run state, and minimum KB scaffold created.
