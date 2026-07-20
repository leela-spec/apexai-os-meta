# Apex KB Lifecycle Runbook

## A. Prepare a new KB

Create one schema-compatible Start configuration from `../templates/start-config-template.yaml`. Preserve every value already supplied by the operator and resolve only required missing fields.

Run the public Start entrypoint in mandatory preview mode:

```text
python apex-meta/scripts/apex_kb.py start --config <start-config.yaml> --repo-root <repository-root> --json --dry-run
```

Review the submitted configuration, derived values, repository/worktree evidence, target commit, configuration hash, warnings, blockers, and operator action. Preview creates no KB destination or KB files. After the operator accepts that readback, repeat with explicit `--allow-write` and without `--dry-run`.

Confirmed Start writes only Setup artifacts and initializes canonical control state. For a Setup-only request, stop after proving:

- `manifests/start-input.json`;
- `manifests/worktree-safety.json`;
- `manifests/topic-registry.json`;
- `manifests/run-intent.md`;
- `manifests/run-state.json`;
- the next legal stage is the first deterministic corpus stage.

Do not run scaffold, source intake, deterministic corpus intelligence, Phase 1, Phase 2, acceptance, retrieval, or postflight in a Setup-only run.

An existing controlled KB skips Start and resumes from `manifests/run-state.json` through `control next`, `control run`, or `control reconcile`.

```yaml
output_tiers:
  source_only: custody and manifests only
  analysis_only: semantic analysis, no wiki pages
  compiled_minimal: minimum useful page topology with complete priority-query value
  compiled_full: complete priority-query value plus independently useful concept/entity pages
  query_ready: semantic acceptance plus deterministic postflight and fresh retrieval
```

## B. Continue after Setup

Use `control next` and `control run`. The control plane delegates source intake, payload manifest generation, preflight, and deterministic corpus intelligence to the existing implementations and records each compact result. It fingerprints the exhaustive rankings and bounded work pack before rendering one Phase 1 packet per topic.

At semantic stages, send only the packet's one-line trigger. The packet fixes exact inputs, exact output path, allowed/forbidden writes, stop/success conditions, required readback, and completion response. After each semantic executor finishes, run `control reconcile`; it validates paths, schema owners, ledgers, candidate dispositions, input fingerprints, and legal transition from files. Phase 2 follows Phase 1 mechanically for compiled tiers, then an independent clean-context acceptance packet follows Phase 2.

If every critical/routine query is answerable and sampled material claims are supported, reconciliation records `compiled_unvalidated`; otherwise it records a reason-coded block or truthful partial state. A new executor resumes by reading `manifests/run-state.json` and the referenced packet, not chat history.

## C. Postflight

After semantic acceptance reconciles successfully, use `control run`; it delegates the existing bounded `postflight` implementation in-process and records the result in canonical run state. A deterministic pass cannot override missing or failed semantic acceptance. `query_ready` requires semantic pass, deterministic postflight pass, and fresh retrieval. Run `control git-state` whenever repository state is uncertain; Apex KB classifies only and never synchronizes or repairs Git.

## D. Query or maintain

Read `wiki/index.md` first, retrieve only the smallest sufficient evidence set, synthesize from compiled pages, and save query outputs when reusable. Run `lint`, `audit`, `status`, and `health` for maintenance. List repair actions, but do not mutate Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU, or personal orchestration artifacts from Apex KB.
