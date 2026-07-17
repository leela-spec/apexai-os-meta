# Apex KB Start Q&A — Compact Draft v4

```yaml
schema: apex.kb.start-qa.v4-draft
status: operator_review_required
scope: phase_0_setup_start_only
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

## 1. Required run information

Fill the block below. Use repository-relative paths.

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
  detail: standard
  output: query_ready
  non_text: inventory_and_report
  ai_help_after_preflight: false

special_constraints: []
```

## 2. Option guide

### Source handling

| Option | Use when | Effect |
|---|---|---|
| `pointer_only` **default** | Sources stay in a repository | Stores paths, refs, and hashes; avoids duplicate files |
| `copy_into_kb` | The KB must hold its own source copies | More storage and update management |
| `snapshot_copy` | A fixed historical evidence set is required | Strongest reproducibility; highest storage cost |

### Run detail

| Option | Includes | Best fit |
|---|---|---|
| `quick` | Inventory, formats, headings, basic phrase matches | Small and already-understood corpora |
| `standard` **default** | Structured topic matching, duplicates, dates when available, work packs, statistics | Normal project KBs |
| `deep` | Standard plus broader extraction and configured relationship analysis | Large, version-heavy, or process-heavy corpora |

### Output

| Option | Stops after |
|---|---|
| `analysis_only` | Deterministic maps and reviewed semantic analysis |
| `compiled_kb` | Accepted dossiers and source atlases |
| `query_ready` **default** | Compiled KB, final validation, and retrieval index |

### Non-text files

| Option | Behavior |
|---|---|
| `inventory_and_report` **default** | Lists every file and reports unsupported content honestly |
| `extract_when_supported` | Uses available approved extractors and reports failures |
| `block_on_unsupported` | Stops when any in-scope file cannot be processed |

## 3. Topic guidance

For each topic, provide only what you already intend the KB to cover:

- **phrases:** strong names that can independently surface candidates
- **aliases:** established alternative names
- **supporting terms:** useful only together with stronger signals
- **ambiguous or negative terms:** likely false-positive language
- **questions:** exact questions the finished KB must answer

Apex KB may find candidate files from these values. It may not invent, rename, merge, or broaden topics or questions.

## 4. What happens next

1. The configuration is schema-validated.
2. A read-only preflight checks paths, overlap, formats, capabilities, exclusions, and workload.
3. You receive one compact status report with blockers, warnings, key statistics, and expected outputs.
4. When `ai_help_after_preflight` is `true`, AI may explain facts and recommend changes, but cannot edit or approve the configuration.
5. You revise this same configuration or confirm it.
6. Only after confirmation are the configuration fingerprint, run state, and minimum KB scaffold created.

## 5. AI recommendation boundary

Any recommendation must show:

| Required field | Meaning |
|---|---|
| Triggering fact | Exact preflight result that caused the recommendation |
| Current value | Your current setting |
| Suggested change | One explicit proposed edit |
| Expected effect | What should improve |
| Tradeoff | Cost or risk introduced |
| Operator action | Accept, reject, or edit |

AI may explain or recommend. It may not select repositories, folders, topics, vocabulary, questions, exclusions, output level, or confirmation on your behalf.
