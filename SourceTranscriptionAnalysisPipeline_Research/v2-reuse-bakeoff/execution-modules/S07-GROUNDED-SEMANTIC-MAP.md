# S07 — Grounded Semantic Map

**Execute only S07, then stop.**  
**Input:** TTK packets from S05 + optional hints decision from S06  
**Next:** S08

## Outcome

Produce real, source-specific semantic Map results from each TTK packet using an **actually invoked allowed subscription AI CLI**. This is the first stage where strong semantic reasoning is authoritative.

## Context to load

- this file;
- S05 and S06 handoffs;
- actual Map packet(s) being processed;
- TTK Map result contract/validator code;
- `06-TRIAL1-TRANSPORT-LOCK.yaml`;
- LangExtract registry entry and provider-plugin docs/code only if implementing the recommended grounded route;
- current `semantic_cli.py` / Map adapter code.

Do **not** load V1 semantic-worker plan, all benchmark transcripts, Reduce code, or failed final reports.

## Recommended route

1. **Preferred first implementation:** LangExtract grounded extraction with a bounded provider adapter that invokes a real allowed subscription CLI.
2. **Control/fallback:** direct real Claude Code CLI or Codex CLI Map over the same TTK packet.
3. Antigravity is allowed only if `agy` has a real headless subprocess smoke PASS.

If LangExtract cannot practically use an allowed CLI adapter, record `BLOCKED_FOR_TRIAL1` for that route and use the declared **real direct-CLI control**. Do not create a fake LangExtract or internal-agent substitute.

## Forbidden

- `antigravity_agent` internal Python/agent worker;
- current coding agent/subagent generating Map semantics;
- regex/keyword claim/entity/support authority;
- API-key/pay-as-you-go model calls;
- Gemini CLI/browser AI in Trial 1;
- synthetic one-token/sample outputs counted as product Map.

## Map semantic target

For each processing window, extract valuable distinct semantics rather than sentence-dumping. Preserve:

- important themes/subtopics;
- factual and non-factual candidate claims with correct semantic type;
- mechanisms/processes/protocols when genuinely present;
- arguments/positions;
- relevant entities/concepts;
- uncertainty, corrections, caveats, contradictions;
- exact source evidence for factual/testable assertions;
- valid source segment provenance for non-factual objects.

`context_only` may inform interpretation but must not be cited as evidence.

## Work sequence

1. Before all packets, prove **one representative packet** end-to-end through the real CLI process.
2. Preserve enough natural invocation evidence to identify executable, provider/transport, exit status, packet hash, and output hash. Do not build another giant receipt framework.
3. Inspect the actual Map content manually for semantic usefulness and source specificity.
4. If the route is good, process all pending packets using the same production adapter.
5. Use S06 hints only when its handoff says they earned use; label them hints, not evidence.
6. Do not silently change provider/route mid-run.

## Tests

Mechanical:

- real subprocess executable is launched;
- output parses and matches Map contract shape;
- packet SHA/result packet ID align;
- TTK Map validation passes or returns exact repair errors;
- failed CLI invocation does not produce a completed result.

Product inspection:

- claims are source-specific and meaningful;
- not every sentence becomes a claim;
- not every claim is `fact`;
- no discourse words as fake entities;
- factual evidence quotes actually occur in cited core segments;
- important uncertainty/corrections are preserved;
- later packets are not reduced to generic boilerplate.

## Outputs

- actual TTK Map result for every processed packet;
- minimal invocation logs/metadata adjacent to results or in run execution records;
- route decision (`langextract_cli|direct_cli`) and actual provider;
- S07 handoff.

Handoff must include ordered packet/result paths and hashes, actual executable/provider/transport, number succeeded/failed, route blocker if any, and a short product-quality observation from reading the results.

## Acceptance

PASS only if real external CLI semantics were produced and the actual Map content is useful. Schema PASS alone is insufficient.

Commit/push production adapter/tests/results permitted by repo policy, return handoff, **STOP. Do not run Reduce.**