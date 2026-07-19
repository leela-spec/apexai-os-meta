# Apex KB Start Workflow

Use this reference only for a **new KB or fresh Setup request** on a terminal-backed executor.

## Public entrypoint

The operator-facing entrypoint is:

```powershell
python apex-meta/scripts/apex_kb.py start --config <start-config.yaml> --repo-root <repository-root>
```

Start is the only supported translator from compact operator choices into the canonical control plane. Do not bypass it by manually assembling `control init` arguments for a new KB.

## Mechanistic sequence

1. Read `templates/start-config-template.yaml`.
2. Fill every value that is already explicit in the operator request.
3. Ask only for values still genuinely unresolved. Never infer repository, source folders, destination, exclusions, topics, questions, or run options.
4. Save a temporary Start YAML outside the selected KB destination.
5. Run Start without `--allow-write`; relay the structured preview and derived paths.
6. Ask the operator to approve or revise the preview.
7. After approval, rerun the identical Start command with `--allow-write`.
8. Follow only the returned `operator_action` and then `control next` / `control run`.

## Phase 0 test boundary

When the operator asks for a Setup or Phase 0 canary, stop when the configured Setup/Phase 0 boundary is reached. Do not enter Phase 1, Phase 2, semantic acceptance, retrieval, or postflight unless explicitly requested after the canary is reviewed.

## Safety

- Never mutate source corpus files.
- Never create, combine, prune, switch, or delete worktrees.
- Never manually recreate Start-derived machine fields.
- Never silently replace a Start configuration or an existing controlled run.
- Treat the runtime JSON result and canonical repository files as authority, not chat memory.
