# Apex KB Start Workflow

Start is the single public Setup entrypoint for a new Apex KB.

## First response for a new KB

1. Render `../templates/start-config-template.yaml` as one guided YAML block.
2. Preserve every repository, source, exclusion, destination, topic, question, and run-option value the operator already supplied.
3. Ask only for required values that are still unresolved.
4. Do not begin with an executor-capability question and do not ask the operator to author internal control fields.
5. Do not run `control init`, `source-intake`, or `phase0` manually.

## Public command

Preview first:

```text
python apex-meta/scripts/apex_kb.py start --config <start-config.yaml> --repo-root <repository-root> --json --dry-run
```

`start --help` must expose:

```text
--config
--repo-root
--allow-write
--dry-run
--strict
--json
```

The four boolean flags may appear before or after `start`.

## Preview contract

Preview validates the Start YAML, repository identity, primary `main` worktree, source folders, destination, overlap rules, topics, and run options. It returns:

- submitted configuration;
- deterministically derived configuration;
- current read-only Git/worktree evidence;
- configuration hash;
- warnings or blockers;
- the operator action required next.

Preview must not create the KB destination or any manifest, state, registry, analysis, wiki, audit, derived, output, or Phase 0 artifact.

Apex KB classifies Git read-only. Start never fetches, pulls, merges, switches branches, creates worktrees, resets, cleans, stashes, commits, or pushes.

## Confirmed Setup

After the operator accepts the preview readback, repeat the same command with explicit `--allow-write` and without `--dry-run`.

Confirmed Start may create only the Setup artifacts needed to initialize the existing controlled lifecycle:

- `manifests/start-input.json`;
- `manifests/worktree-safety.json`;
- `manifests/topic-registry.json`;
- `manifests/run-intent.md`;
- `manifests/run-state.json`;
- the initial run log/result files written by control initialization.

After initialization, canonical run state owns continuation through `control next`, `control run`, and `control reconcile`.

## Stop boundary

A Setup-only run stops after the Setup artifacts exist and canonical state identifies the first legal controlled action. It must not execute source intake, deterministic corpus intelligence, Phase 1, Phase 2, semantic acceptance, retrieval, or postflight.

## Existing KB routing

- If `manifests/run-state.json` exists, do not rerun Start. Resume through canonical control state.
- Read-only query, status, lint, audit, health, and retrieval requests keep their existing commands.
- A legacy KB without canonical run state uses its existing bounded command or an explicit migration; Start does not silently replace it.