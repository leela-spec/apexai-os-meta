# Apex KB Lifecycle Runbook

## A. Prepare


Run Step 0 — Intake and intent lock (see `SKILL.md`) first, on every run. In one conversational pass capture the operator's intent, the KB identity ("this KB is about X"), the source locus and what is out of scope, and the success definition; lock stable target queries, priorities, answer requirements, and expected page routes per topic in `manifests/topic-registry.json`; run `topic-sanity-check` (or its manual equivalent) as a validation input; then read the whole understanding back — including your **recommended** output tier, execution route, and corpus breadth (default narrow), each with a one-line reason — and get the operator's explicit confirmation. Record it in `manifests/run-intent.md` with `operator_confirmed: true` and the verbatim affirmative. Creating the empty KB skeleton is fine as pre-gate setup, but **no source-intake, Phase 0, wiki writing, or commit/push runs until `manifests/run-intent.md` shows `operator_confirmed: true`.**

```yaml
output_tiers:
  source_only: custody and manifests only
  analysis_only: semantic analysis, no wiki pages
  compiled_minimal: minimum useful page topology with complete priority-query value
  compiled_full: complete priority-query value plus independently useful concept/entity pages
  query_ready: semantic acceptance plus deterministic postflight and fresh retrieval
```
## B. Ingest and compile


Add sources through `source-intake`, generate the payload manifest, and run Phase 0. Treat Phase 0 rankings as navigation candidates only, and start semantic reading from that topic's `manifests/phase0/work-packs/<topic-slug>.md` -- the bounded, concentrated set -- not the full exhaustive ranking map.

For each topic, maintain its semantic ledger. Continue reading canonical sources until critical/routine target queries are covered or evidence is genuinely unavailable. Complete query-linked Phase 1 analyses and dispose every concept/entity candidate. Draft the minimum answer-bearing page topology and include only reviewed, materially used evidence.

Run page-only query and claim-entailment acceptance in a clean context. If every critical/routine query is answerable and sampled material claims are supported, report `compiled_unvalidated`; otherwise report `partial` or `analysis_complete_unvalidated`.
## C. Postflight


Validate semantic-acceptance artifacts before deterministic promotion. Use `postflight` as the preferred bounded deterministic completion interface:

```powershell
python apex-meta/scripts/apex_kb.py --kb-root $KB --json semantic-acceptance-status
python apex-meta/scripts/apex_kb.py --kb-root $KB --json postflight
python apex-meta/scripts/apex_kb.py --kb-root $KB --allow-write --json postflight
```

A deterministic pass cannot override missing or failed semantic acceptance. `query_ready` requires semantic pass, deterministic pass, and fresh retrieval.
## D. Query or maintain

Read `wiki/index.md` first, retrieve only the smallest sufficient evidence set, synthesize from compiled pages, and save query outputs when reusable. Run `lint`, `audit`, `status`, and `health` for maintenance. List repair actions, but do not mutate Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU, or personal orchestration artifacts from Apex KB.
> EXAMPLE ONLY — This runbook illustrates a terminal-backed execution sequence. Follow the execution-surface router in `SKILL.md` first.
