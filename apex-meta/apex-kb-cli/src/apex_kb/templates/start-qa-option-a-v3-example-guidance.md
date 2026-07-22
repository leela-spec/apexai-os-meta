# Apex KB Start Q&A — Option A

```yaml
schema: apex.kb.start-qa.option-a.v1
status: selected_design
scope: phase_0_setup_start_only
layout: compact_markdown_with_yaml_configuration
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
| **KB destination** | The repository and folder where Apex KB will save generated manifests, indexes, analyses, compiled pages, and retrieval artifacts |
| **Local clone root** | The absolute Windows path to an already available local repository clone; the CLI asks for it separately when it is not supplied in the configuration |

Source folders and the KB destination folder are repository-relative paths. The source and destination may be the same repository or two different repositories.

Apex KB uses the configured source ref, normally `main`. The CLI does not invent another branch or worktree.

## 1. Required run information

Fill the block below. Keep repository folders repository-relative. The CLI asks for local clone roots separately when they are not already present.

```yaml
kb:
  id: ""
  title: ""
  purpose: ""

source:
  repository: "owner/repository"
  ref: "main"
  folders:
    - "path/to/source-folder"
  exclusions:
    - path: "path/to/exclude"
      reason: ""

target:
  repository: "owner/repository"
  kb_folder: "path/to/knowledge-base"

topics:
  - id: ""
    name: ""
    phrases: [""]
    aliases: []
    supporting_terms: []
    ambiguous_or_negative_terms: []
    questions:
      - ""

run_options:
  source_handling: pointer_only
  semantic_depth: standard
  output: query_ready
  non_text: inventory_and_report
  ai_help_after_preflight: false

special_constraints: []
```

## 2. Option guide

| Setting | Option | Use when | Effect |
|---|---|---|---|
| **Source handling** | `pointer_only` **default** | Sources remain in the repository | Stores paths, repository state, and hashes without duplicating files |
|  | `copy_into_kb` | The generated KB must hold approved source copies | More storage and update management |
|  | `snapshot_copy` | A fixed historical evidence set is required | Strongest reproducibility; highest storage cost |
| **Semantic depth** | `quick` | The semantic questions are narrow or a concise answer is sufficient | Uses the strongest evidence first, answers locked questions concisely, and avoids optional expansion |
|  | `standard` **default** | Normal project or documentation KB | Reviews the complete bounded work pack with normal authority, contradiction, version, dossier, and source-atlas treatment |
|  | `deep` | The topic is highly versioned, contradictory, or strategically important | Performs maximum bounded cross-source reconciliation, evolution analysis, uncertainty treatment, and richer Macro/Meso/Micro synthesis |
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
