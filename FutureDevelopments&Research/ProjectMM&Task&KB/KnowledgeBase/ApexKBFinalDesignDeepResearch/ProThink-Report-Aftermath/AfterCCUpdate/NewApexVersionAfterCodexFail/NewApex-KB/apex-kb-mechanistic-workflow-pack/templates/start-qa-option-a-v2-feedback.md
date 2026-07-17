# Apex KB Start Q&A — Option A v2

```yaml
schema: apex.kb.start-qa.option-a.v2
status: operator_review_required
scope: phase_0_setup_start_only
layout: compact_markdown_with_yaml_configuration
render_policy: fixed_verbatim
runtime_authority: none
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
| **Source corpus** | The existing repository folders Apex KB will inspect and index |
| **KB destination** | The folder in the same repository where Apex KB will save generated manifests, indexes, analyses, compiled pages, and retrieval artifacts |

The repository is stated once. Source folders and the KB destination are repository-relative paths inside that repository.

The operator does not choose a branch or worktree. Apex KB uses `main` as the default source and may inspect other available branches or worktrees only when the configured source produces missing, contradictory, or clearly incomplete evidence.

## 1. Fill the run configuration

The block contains examples so the format is obvious. **Replace or delete every example before submitting it.**

```yaml
repository: "leela-spec/example-repository"

source_folders:
  # Folder or folders containing the source corpus to index.
  - "docs"
  - "src/architecture"

optional_exclusions:
  # Delete this section when nothing must be excluded.
  - path: "generated-output"
    reason: "Generated files must not be indexed again"

kb_destination:
  # Folder where Apex KB will create the generated knowledge base.
  folder: "apex-meta/kb/example-knowledge-base"

topics:
  # Add one entry for every subject the generated KB must cover.
  - name: "Authentication architecture"

    # Strong exact names or phrases likely to appear in relevant files.
    # Examples: "authentication architecture", "identity service", "login flow"
    phrases:
      - "authentication architecture"
      - "identity service"

    # Broad or misleading terms that can create false-positive matches.
    # Examples: "auth example", "test login", "deprecated authentication"
    ambiguous_or_negative_terms:
      - "test login"
      - "deprecated authentication"

    # Exact questions the completed KB must answer.
    questions:
      - "How does authentication currently work?"
      - "Which files define the current authentication flow?"
      - "Which older or conflicting designs still exist?"

run_options:
  # Keep exactly one value after each colon.
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
|  | `copy_into_kb` | The generated KB must hold its own approved source copies | More storage and update management |
|  | `snapshot_copy` | A fixed historical evidence set is required | Strongest reproducibility; highest storage cost |
| **Run detail** | `quick` | The corpus is small and already understood | Inventory, formats, headings, and basic phrase matches |
|  | `standard` **default** | Normal project or documentation KB | Structured topic matching, duplicates, dates when available, work packs, and statistics |
|  | `deep` | The corpus is large, highly versioned, or relationship-heavy | Standard processing plus broader extraction and configured relationship analysis |
| **Output** | `analysis_only` | You need deterministic maps and reviewed semantic analysis only | Stops before durable compiled pages |
|  | `compiled_kb` | Future AIs should read durable dossiers and source atlases | Creates accepted compiled knowledge without requiring final retrieval |
|  | `query_ready` **default** | The KB should be directly searchable after completion | Adds final validation and the retrieval index |
| **Non-text files** | `inventory_and_report` **default** | Unsupported formats may exist | Lists every file and reports unsupported content honestly |
|  | `extract_when_supported` | Approved extractors may process PDFs, documents, or other formats | Uses available extractors and reports every failure |
|  | `block_on_unsupported` | Complete extraction is mandatory | Stops when any in-scope file cannot be processed |
| **AI help after preflight** | `false` **default** | You want deterministic facts only | Lowest drift risk; no AI recommendation layer |
|  | `true` | You want help interpreting factual warnings or option tradeoffs | AI may explain and recommend, but cannot edit or approve the configuration |

## 3. AI recommendation boundary

When `ai_help_after_preflight` is `true`, every recommendation must show:

| Required field | Meaning |
|---|---|
| Triggering fact | Exact preflight result that caused the recommendation |
| Current value | Your current setting |
| Suggested change | One explicit proposed edit |
| Expected effect | What should improve |
| Tradeoff | Cost or risk introduced |
| Operator action | Accept, reject, or edit |

AI may explain or recommend. It may not choose the repository, source folders, KB destination, topics, phrases, exclusions, questions, output level, or confirmation on your behalf.

## 4. What happens next

1. The configuration is schema-validated.
2. A read-only preflight checks the repository, source folders, KB destination, overlap, formats, capabilities, exclusions, and likely workload.
3. Apex KB uses `main` first and only investigates other available branches or worktrees when the configured source appears incomplete or contradictory.
4. You receive one compact status report with blockers, warnings, key statistics, and expected outputs.
5. When AI help is enabled, recommendations appear after the deterministic facts and remain non-binding.
6. You revise this same configuration or confirm it.
7. Only after confirmation are the configuration fingerprint, run state, and minimum KB scaffold created.
