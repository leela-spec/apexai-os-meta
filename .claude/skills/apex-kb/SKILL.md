---
name: apex-kb
description: >
  Optional launcher for the installed Apex KB Python CLI. Use to invoke the
  public commands apex-kb start, status, continue, drive, query, doctor, and
  update, or to execute one explicit semantic task packet produced by the
  application. apex-kb query is the compiled-KB retrieval interface. The Python
  application is the sole lifecycle authority.
---

# Apex KB CLI Launcher

Apex KB is an installable, local, manifest-driven Python application. This Skill is an optional shell around that application; deleting this Skill must not affect direct CLI operation.

## Allowed actions

1. Invoke exactly the operator-requested public command. The full surface is:

```bash
apex-kb start                                   # render template, confirm, scaffold a new run
apex-kb status   --run-root <path>              # read-only reconstructed status
apex-kb continue --run-root <path>              # perform exactly one legal lifecycle action
apex-kb drive    --run-root <path>              # run deterministic actions to the next semantic/terminal boundary
apex-kb query    --run-root <path> --query "<text>" [--topic <id>] [--limit N]   # search the compiled KB (retrieval)
apex-kb doctor   --run-root <path>              # read-only runtime/health probe
apex-kb update   --run-root <path>              # controlled incremental run / selective invalidation
```

Prefer `--json-output` on every command for a machine-readable envelope.

2. Display the application output without replacing it with an alternate workflow explanation.
3. When the operator explicitly supplies a generated semantic task packet, read that packet and perform only its bounded semantic assignment.
4. Write the semantic result only to the packet's declared incoming/expected-output path.

## Binding boundary

The Skill must not:

- choose or change a lifecycle stage;
- select or recreate the Start template;
- construct, normalize, or reinterpret run configuration;
- derive source or destination paths;
- modify `run-config.yaml`, `run-manifest.json`, `run-state.json`, or stage results;
- decide whether a run is complete;
- create commands that were not returned by the application;
- widen a semantic source allowlist;
- write outside a semantic packet's declared output path;
- treat legacy `apex_kb.py`, `apex_kb_start.py`, or `apex_kb_control.py` command surfaces as the normal operator workflow.

## Public flow

For a new run, invoke `apex-kb start`. For an existing run, invoke `apex-kb status` (read-only) or advance it with `apex-kb continue` (one action) or `apex-kb drive` (runs deterministic actions to the next semantic or terminal boundary), passing the operator's run root. Once the run reaches `query_ready`, use `apex-kb query` to retrieve compiled answers; use `apex-kb doctor` for a health probe and `apex-kb update` for a controlled incremental rebuild. The application validates durable files and derives the only legal next action; the skill never chooses stages itself.

## Semantic packet flow

Before semantic work, read all files in the generated task directory:

```text
TASK.md
task.json
source-allowlist.json
output.schema.json
expected-output-path.txt
```

Follow the packet exactly. Do not infer missing identity values, sources, paths, or lifecycle actions. Stop on any mismatch. The application validates and imports the returned result on the next `apex-kb continue` invocation.

## Retrieval contract for future agents

When a run is `query_ready`, prefer the KB over re-reading raw notes: run `apex-kb query --run-root <path> --query "<question>" [--topic <id>] --json-output` **first**. The JSON result carries a `future_agent_contract` (retrieval policy, context budget, authority rules, answer contract) and `raw_source_reopen_guidance`. Load the top answer-bearing dossier chunks first; open a source-atlas chunk only for provenance; reopen a raw source only when the answer is absent or `source_drift` is not fresh. Never emit a diagnosis or assert beyond cited evidence.

## Installation

From the repository root:

```powershell
python -m pip install -e ".\apex-meta\apex-kb-cli[test]"
```

The stable executable is defined by:

```toml
[project.scripts]
apex-kb = "apex_kb.cli:main"
```
