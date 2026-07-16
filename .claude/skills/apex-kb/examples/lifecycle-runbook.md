# Apex KB Lifecycle Runbook

## A. Prepare


Author `manifests/topic-registry.json`, then run `control init` with the compact operator configuration. The control plane creates `manifests/run-intent.md` and `manifests/run-state.json`, executes only the empty scaffold before confirmation, runs topic sanity as part of `control run`, and writes `log/runs/<run-id>/operator-readback.md`. Read that file to the operator and use `control confirm` with the verbatim affirmative. No source intake, Phase 0, semantic packet, wiki write, or postflight may precede that state transition.

```yaml
output_tiers:
  source_only: custody and manifests only
  analysis_only: semantic analysis, no wiki pages
  compiled_minimal: minimum useful page topology with complete priority-query value
  compiled_full: complete priority-query value plus independently useful concept/entity pages
  query_ready: semantic acceptance plus deterministic postflight and fresh retrieval
```
## B. Ingest and compile


Use `control next` and `control run`. The control plane delegates source intake, payload manifest generation, preflight, and Phase 0 to the existing implementations and records each compact result. It fingerprints the exhaustive rankings and bounded work pack before rendering one Phase 1 packet per topic.

At semantic stages, send only the packet's one-line trigger. The packet fixes exact inputs, exact output path, allowed/forbidden writes, stop/success conditions, required readback, and completion response. After each semantic executor finishes, run `control reconcile`; it validates paths, schema owners, ledgers, candidate dispositions, input fingerprints, and legal transition from files. Phase 2 follows Phase 1 mechanically for compiled tiers, then an independent clean-context acceptance packet follows Phase 2.

If every critical/routine query is answerable and sampled material claims are supported, reconciliation records `compiled_unvalidated`; otherwise it records a reason-coded block or truthful partial state. A new executor resumes by reading `manifests/run-state.json` and the referenced packet, not chat history.
## C. Postflight


After semantic acceptance reconciles successfully, use `control run`; it delegates the existing bounded `postflight` implementation in-process and records the result in canonical run state. A deterministic pass cannot override missing or failed semantic acceptance. `query_ready` requires semantic pass, deterministic postflight pass, and fresh retrieval. Run `control git-state` whenever repository state is uncertain; Apex KB classifies only and never synchronizes or repairs Git.
## D. Query or maintain

Read `wiki/index.md` first, retrieve only the smallest sufficient evidence set, synthesize from compiled pages, and save query outputs when reusable. Run `lint`, `audit`, `status`, and `health` for maintenance. List repair actions, but do not mutate Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU, or personal orchestration artifacts from Apex KB.
> EXAMPLE ONLY — This runbook illustrates a terminal-backed execution sequence. Follow the execution-surface router in `SKILL.md` first.
