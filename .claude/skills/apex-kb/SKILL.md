---
name: apex-kb
description: >
  Optional launcher for the installed Apex KB Python CLI. Use only to invoke
  apex-kb start, apex-kb status, apex-kb continue, or to execute one explicit
  semantic task packet produced by the application. The Python application is
  the sole lifecycle authority.
---

# Apex KB CLI Launcher

Apex KB is an installable, local, manifest-driven Python application. This Skill is an optional shell around that application; deleting this Skill must not affect direct CLI operation.

## Allowed actions

1. Invoke exactly the operator-requested public command:

```powershell
apex-kb start
apex-kb status --run-root <path>
apex-kb continue --run-root <path>
```

2. Display the application output without replacing it with an alternate workflow explanation.
3. When the operator explicitly supplies a generated semantic task packet, read that packet and perform only its bounded semantic assignment.
4. Write the semantic result only to the packet's declared incoming path.

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

For a new run, invoke `apex-kb start`. For an existing run, invoke `apex-kb status` or `apex-kb continue` with the operator's run root. The application validates durable files and derives the only legal next action.

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
