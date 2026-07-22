# Apex KB operator guide

## Install and inspect

From the package root:

```powershell
python -m pip install .
apex-kb doctor
apex-kb --help
```

`doctor` reports runtime capabilities without advancing a run.

## Start a run

`apex-kb start` prints the canonical Start guidance before collecting configuration. Source and destination roots are independent absolute paths. Keep the destination outside the configured source corpus.

```powershell
apex-kb start
apex-kb start --config C:\path\to\run-config.yaml
apex-kb start --config C:\path\to\run-config.yaml --non-interactive --yes
```

Review the normalized readback before confirmation. Do not hand-edit `run-manifest.json` or `run-state.json`.

## Continue and status

```powershell
apex-kb status --run-root C:\path\to\kb
apex-kb continue --run-root C:\path\to\kb
```

Each `continue` performs one legal action. Repeat it until it returns a semantic task, a terminal result, or a concrete blocker. `status` is read-only and can reconstruct the current action in a fresh process.

For a semantic task, execute only the generated packet described in the semantic-worker guide. Place the result at `expected-output-path.txt`, then invoke `continue` again. If validation emits repair instructions, correct only the declared result and retry; never advance state manually.

## Query and update

```powershell
apex-kb query --run-root C:\path\to\kb --query "What owns Skill Tree navigation?"
apex-kb update --run-root C:\path\to\kb
```

Query verifies run identity, page hashes, database identity, SQLite integrity, and FTS5 health before use. Update is valid only from a stable completed or explicitly blocked run and preserves prior control evidence.

## Safety

- Never write generated KB output into the configured source corpus.
- Never use internal functions to bypass public lifecycle transitions.
- Preserve task allowlists and exact identity fields.
- Treat `derived/search/search.sqlite` as disposable and rebuildable.
- Back up or version operator-authored configuration; application-owned control files are already archived during supported migration and update flows.
