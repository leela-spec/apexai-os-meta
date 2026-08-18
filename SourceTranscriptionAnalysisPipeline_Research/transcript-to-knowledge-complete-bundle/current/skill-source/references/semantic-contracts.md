# Semantic Contracts

## Contents

1. Map result
2. Reduce result
3. Source support vs external truth
4. External verification
5. Recovery rules

The CLI owns packet/result paths and validation. The semantic worker must fill only the requested result file and echo the packet hash exactly.

## 1. Map result

Input: one `work/packets/map/window-XXXX.json`.

The packet contains:
- `packet_id`, `packet_sha256`, `window_id`;
- exact `core_segment_ids`;
- optional `context_only_segment_ids`;
- normalized `source_segments`, each labeled `core` or `context_only`.

### Goal

Read the bounded window once and produce a reusable evidence card. Capture all valuable semantic evidence in the same pass so later stages do not need separate raw-transcript reads for themes, claims, quotes, entities, and mechanisms.

### Required JSON shape

```json
{
  "schema": "ttk.map-result.v2",
  "packet_id": "map-window-0001",
  "packet_sha256": "<copy from packet>",
  "window_id": "window-0001",
  "subtopics": [
    {"label": "Topic label", "source_segment_ids": ["seg-000001", "seg-000002"]}
  ],
  "key_points": [
    {"text": "Important source-grounded point", "source_segment_ids": ["seg-000002"]}
  ],
  "mechanisms": [
    {"text": "How or why something works", "source_segment_ids": ["seg-000003"]}
  ],
  "protocols": [
    {
      "name": "Named process",
      "steps": ["Step one", "Step two"],
      "source_segment_ids": ["seg-000004", "seg-000005"]
    }
  ],
  "arguments": [
    {"speaker": "Speaker A", "position": "Position or reasoning", "source_segment_ids": ["seg-000006"]}
  ],
  "candidate_claims": [
    {
      "claim_text": "One self-contained proposition.",
      "claim_kind": "fact",
      "speaker": "Speaker A",
      "source_segment_ids": ["seg-000006"],
      "quote_evidence": [
        {"segment_id": "seg-000006", "quote": "verbatim normalized transcript substring"}
      ],
      "checkworthiness": "medium"
    }
  ],
  "entities": [
    {"name": "Entity Name", "type": "person", "source_segment_ids": ["seg-000006"]}
  ],
  "concepts": [
    {"name": "Concept Name", "source_segment_ids": ["seg-000003"]}
  ],
  "open_questions": [
    {"text": "Unresolved question", "source_segment_ids": ["seg-000007"]}
  ],
  "contradictions_or_uncertainty": [
    {"text": "Conflict, correction, caveat, or uncertainty", "source_segment_ids": ["seg-000008"]}
  ]
}
```

### Claim-kind vocabulary

Use exactly one:
- `fact` — externally testable assertion about the world;
- `opinion` — value judgment or subjective stance;
- `prediction` — future assertion;
- `recommendation` — advice / should statement;
- `decision` — a decision made in the conversation;
- `anecdote` — reported personal/event narrative;
- `definition` — proposed/explained meaning;
- `mechanism` — causal/operational explanation;
- `estimate` — explicitly approximate quantity;
- `hypothesis` — tentative explanatory claim.

Do not convert every sentence into `fact`.

### Checkworthiness

- `high`: consequential, specific factual assertion likely to affect downstream decisions.
- `medium`: useful factual assertion where external truth materially improves the knowledge note.
- `low`: factual but low consequence or expensive to verify relative to value.
- `none`: non-factual, trivially source-local, or not worth external research.

### Map invariants

- Cite only `core_segment_ids`.
- Context-only segments may shape understanding but must never supply evidence in this result.
- Every candidate claim must include at least one exact quote.
- A quote must be a literal substring of the normalized transcript segment.
- Keep corrections/contradictions separate.
- Empty arrays are correct when the category is absent.
- Never create fake protocols or entities merely to fill the schema.

## 2. Reduce result

Input: `work/packets/reduce.json`, generated only after all Map results pass deterministic validation.

The packet contains the compact evidence ledger, exact duplicate merging, and near-duplicate warnings. It deliberately omits the raw full transcript.

### Goal

Create the final hierarchy:
- **Macro:** global thesis, concise synthesis, high-value takeaways, taxonomy, context, uncertainty.
- **Meso:** real semantic modules/chapters independent of processing-window boundaries.
- **Micro:** refined atomic knowledge claims retaining exact transcript evidence.

### Required JSON shape

```json
{
  "schema": "ttk.reduce-result.v2",
  "packet_id": "reduce-final",
  "packet_sha256": "<copy from packet>",
  "macro": {
    "thesis": "One global thesis.",
    "summary": "Compact global synthesis.",
    "takeaways": [
      {
        "text": "High-value takeaway",
        "source_segment_ids": ["seg-000010"],
        "meso_refs": ["meso-001"]
      }
    ],
    "taxonomy": ["Concept A", "Concept B"],
    "speaker_context": ["Only transcript-supported context"],
    "contradictions_or_uncertainty": ["Important unresolved tension"]
  },
  "meso": [
    {
      "meso_ref": "meso-001",
      "title": "Semantic Module Title",
      "summary": "Module synthesis.",
      "source_segment_ids": ["seg-000001", "seg-000002"],
      "concepts": ["Concept A"],
      "entities": ["Entity A"],
      "mechanisms": ["Mechanism statement"],
      "protocols": ["Process or ordered protocol when actually present"],
      "arguments": ["Position / counter-position"],
      "caveats": ["Scope limit / correction / exception"],
      "claim_refs": ["micro-001"]
    }
  ],
  "micro": [
    {
      "claim_ref": "micro-001",
      "claim_text": "One self-contained proposition.",
      "claim_kind": "fact",
      "speaker": "Speaker A",
      "source_segment_ids": ["seg-000006"],
      "quote_evidence": [
        {"segment_id": "seg-000006", "quote": "verbatim normalized transcript substring"}
      ],
      "source_support": "SUPPORTED",
      "checkworthiness": "medium",
      "topics": ["Concept A"],
      "entities": ["Entity A"],
      "context": "Nuance needed to avoid misreading the claim.",
      "verification_question": "Optional precise external fact-check question",
      "preferred_source_types": ["official statistics", "primary paper"]
    }
  ],
  "rejected_or_unresolved_candidates": []
}
```

### Reduce rules

- Meso modules may merge or split Map subtopics. Processing windows do not define chapter truth.
- Macro takeaways must cite source segments and may reference Meso modules.
- `claim_ref` and `meso_ref` must be unique inside the result.
- Every Meso `claim_ref` must resolve to a Micro claim.
- Near-duplicate claims in the evidence ledger are review candidates, not automatic equivalence.
- Prefer fewer, useful claims over exhaustive atomization.
- Do not keep a final claim with `UNSUPPORTED` source support unless it is intentionally retained as an audit/rejection object. Strict compile rejects unsupported final claims.

## 3. Source support vs external truth

These are two different questions.

**Source support:** “Does the transcript actually support this knowledge statement?”

Use:
- `SUPPORTED` — cited transcript evidence directly supports the proposition;
- `PARTIAL` — part is supported but wording/conditions overreach;
- `AMBIGUOUS` — source meaning is genuinely unclear;
- `UNSUPPORTED` — cited source does not support the proposition.

**External truth:** “Is the speaker's factual assertion true in the world?”

This is evaluated later and only for routed factual claims. A claim can be `SUPPORTED` by the transcript and externally `CONTRADICTED`.

## 4. External verification

Run `make-verify` after a valid Reduce result. The CLI creates `work/packets/verify-queue.json` containing only routed factual claims.

Write `work/results/verify/results.json`:

```json
{
  "schema": "ttk.verify-results.v2",
  "queue_sha256": "<copy from verification queue>",
  "results": [
    {
      "claim_ref": "micro-001",
      "status": "CONFIRMED",
      "rationale": "Why the evidence supports this verdict.",
      "evidence": [
        {
          "title": "Primary source title",
          "url": "https://example.org/source",
          "publisher": "Publisher",
          "date": "2026-08-18",
          "stance": "supports",
          "note": "Specific relevant finding, paraphrased."
        }
      ]
    }
  ]
}
```

Allowed statuses:
- `CONFIRMED`
- `CONTRADICTED`
- `MIXED`
- `UNVERIFIED`

Allowed evidence stances:
- `supports`
- `contradicts`
- `context`

Rules:
- Prefer official/primary evidence.
- Search iteratively only until the load-bearing claim has enough evidence or the gap is explicit.
- Use full document/page evidence when a search snippet is insufficient.
- `CONFIRMED`, `CONTRADICTED`, and `MIXED` require at least one evidence record.
- If live research is unavailable or inconclusive, keep `UNVERIFIED`.
- Never modify the transcript quote during external verification.

Non-factual claims compile with external status `NOT_APPLICABLE`; that value is produced by the compiler, not the verification result schema.

## 5. Recovery rules

- `ttk.py status <run>` derives state from files; do not reconstruct state from chat memory.
- `ttk.py next <run>` gives the exact next packet/result path.
- A result with an old packet hash is stale and must be regenerated.
- If one Map result fails, fix only that window. Do not rerun successful windows.
- If Map evidence changes, rerun `make-reduce`; the Reduce packet hash changes and invalidates an old Reduce result.
- If the Reduce result changes, rerun `make-verify`; its queue hash changes and invalidates old verification results.
- `wiki/compiled.json` records hashes of the Reduce and valid verification results used to build it. If either changes, `status` reports `compile_stale` until compilation is rerun.
- Compilation clears only compiler-owned `wiki/{summaries,modules,claims,entities,concepts}/*.md` before rebuilding so removed semantic objects cannot survive as stale pages.
- The compiler can run without completed external verification; routed factual claims without a valid result remain `UNVERIFIED`.
