# Transcript-to-Knowledge v2 — Micro Implementation Contract

## 1. Public CLI

Public entrypoint:

```text
.claude/skills/transcript-to-knowledge/scripts/ttk.py
```

The implementation is split by responsibility to keep each source file inspectable:

```text
ttk_base.py       parsing primitives, schemas, source normalization
ttk_windows.py    diagnostics + deterministic processing windows
ttk_source.py     content-bound Map packets + run initialization
ttk_map.py        Map validation + evidence ledger + Reduce packet
ttk_verify.py     Reduce validation + verification routing/validation
ttk_wiki.py       deterministic Macro/Meso/Micro wiki compiler
ttk_compile.py    run validation + compiled freshness + status/resume
ttk.py            small public CLI entrypoint
```

Python 3.10+, standard library only. The CLI makes **no network calls and no LLM calls**.

Commands:

```text
ttk.py doctor
ttk.py init <source> --output <run-dir>
ttk.py prepare <source> --output <run-dir>    # compatibility alias
ttk.py status <run-dir>
ttk.py next <run-dir>
ttk.py validate <run-dir> [--complete]
ttk.py make-reduce <run-dir>
ttk.py make-verify <run-dir> [--min-checkworthiness high|medium|low]
ttk.py compile <run-dir> [--allow-unsupported]
```

All commands accept `--json-output` before or after the subcommand for machine consumers.

PowerShell wrappers:

```text
scripts/ttk.ps1
scripts/prepare-transcript.ps1
```

Legacy Python entrypoint `prepare_transcript.py` remains only as a compatibility shim into the new CLI.

## 2. Deterministic run tree

```text
<run>/
  manifest.json
  validation.json
  source/
    transcript.json
    transcript.md
    diagnostics.json
  windows/
    index.json
  work/
    packets/
      map/window-XXXX.json
      reduce.json
      verify-queue.json
    results/
      map/window-XXXX.json
      reduce.json
      verify/results.json
  ledger/
    evidence.json
    coverage.json
  wiki/
    compiled.json
    index.md
    summaries/Macro.md
    modules/*.md
    claims/*.md
    concepts/*.md
    entities/*.md
```

## 3. Source format parsing

Supported:

- Whisper/faster-whisper/WhisperX-style JSON;
- JSONL/NDJSON;
- SRT;
- WebVTT;
- TXT/Markdown, including bracket timestamps.

Each segment receives stable `seg-XXXXXX` identity. Source hash is SHA-256 of original bytes.

The normalizer preserves when present:

- segment start/end;
- speaker label;
- word start/end;
- word probability/confidence;
- source pointer.

It never fabricates missing timestamps/speakers.

## 4. Processing-window algorithm

Inputs:

```text
--target-words      default 1100
--min-words         default 700
--max-words         default 1500
--block-segments    default 4
--pause-weight      default 0.15
--context-segments  default 1
```

At each inter-segment gap:

1. tokenize adjacent left/right blocks;
2. build TF-IDF weighted block vectors;
3. compute cosine similarity;
4. `lexical_dissimilarity = 1 - cosine_similarity`;
5. calculate timestamp pause score where timestamps permit;
6. combine lexical score with a small pause weight;
7. among candidate cuts within min/max bounds, favor a high boundary score while staying near target size;
8. force a boundary at max size when necessary.

Core segment lists are non-overlapping and concatenate exactly to the normalized transcript order.

Context halos are packet-visible but have `role=context_only`. Map evidence may reference only `role=core`.

## 5. Packet freshness

Every semantic packet includes a SHA-256 computed from the stable JSON packet content excluding the hash field itself. Every result must echo it.

Changing a packet makes the old result invalid without requiring a database state transition.

Dependency cascade:

```text
Map packets -> Map results
Map results -> evidence ledger / Reduce packet
Reduce packet -> Reduce result
Reduce result -> verification queue
verification queue -> verification results
Reduce + valid verification result -> compiled wiki manifest
```

## 6. Map hard validation

The CLI rejects:

- wrong schema;
- wrong packet/window ID;
- stale packet hash;
- unknown segment ID;
- context-only citation;
- quote not a normalized verbatim substring of its cited segment;
- invalid claim kind/checkworthiness;
- malformed structured evidence.

One invalid Map output does not invalidate already-valid sibling windows.

## 7. Ledger behavior

Exact normalized duplicate claims can be mechanically merged with provenance union.

Near duplicates use token Jaccard >= 0.80 only as a **review warning**. They are retained as separate candidates because lexical similarity is not sufficient proof of semantic equivalence.

Entity/concept spelling is case-insensitively consolidated while preserving a canonical display spelling.

## 8. Reduce hard validation

The CLI enforces:

- packet freshness;
- required Macro/Meso/Micro shapes;
- unique `meso_ref`/`claim_ref`;
- known source refs;
- literal quote evidence;
- allowed `source_support` and checkworthiness values;
- all Meso claim refs resolve to Micro;
- Macro Meso refs resolve;
- final evidence remains source-grounded.

Strict compilation rejects final Micro entries with `source_support=UNSUPPORTED`.

## 9. Two-axis claim truth model

### Axis A — transcript support

```text
SUPPORTED
PARTIAL
AMBIGUOUS
UNSUPPORTED
```

This asks whether the transcript supports the compiled proposition.

### Axis B — external factual status

```text
CONFIRMED
CONTRADICTED
MIXED
UNVERIFIED
```

This asks whether a routed factual proposition is true in the world according to external evidence.

Non-factual speech compiles to `NOT_APPLICABLE` on Axis B.

This separation prevents a classic provenance error: a transcript can faithfully contain a false assertion.

## 10. Verification queue

Default `medium` threshold routes only:

```text
claim_kind == fact
AND source_support != UNSUPPORTED
AND checkworthiness in {medium, high}
```

Each queue is content-hashed. A decisive verdict needs at least one evidence record with `http(s)` URL and a non-empty title.

## 11. Compilation freshness

`wiki/compiled.json` records:

- Reduce result hash;
- valid verification-result hash or null;
- object counts;
- verification state.

`status` reports `compiled` only when the hashes still match. If upstream semantic/verification results change, the state is `compile_stale` and compilation must rerun.

The compiler owns only the generated wiki subfolders. On each rebuild it removes generated `*.md` files in those folders before rewriting, preventing stale objects from surviving.

## 12. Deterministic vs semantic boundary

### Code owns

- parsing;
- hashing;
- IDs;
- diagnostics;
- processing-window transport;
- packet creation;
- exact source coverage;
- quote/ref validation;
- exact dedup;
- near-duplicate candidate detection;
- verification routing;
- filesystem lifecycle derivation;
- stable slugs/IDs/links;
- compilation freshness;
- Markdown generation.

### Reasoning model owns

- what the transcript means;
- theme interpretation;
- final Meso grouping;
- thesis/taxonomy;
- mechanism/protocol/argument interpretation;
- whether candidate propositions are useful;
- source-support semantic judgment;
- external evidence evaluation.

The code deliberately does **not** pretend to solve semantic tasks deterministically.
