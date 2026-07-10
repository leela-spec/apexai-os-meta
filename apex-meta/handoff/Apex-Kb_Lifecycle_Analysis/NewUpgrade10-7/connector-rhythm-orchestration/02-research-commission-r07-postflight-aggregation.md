# Research Commission R07 — Minimal Postflight Aggregation

Execute the full read-only investigation now.

```yaml
research_job:
  id: R07
  repo: leela-spec/apexai-os-meta
  branch: main
  question: >
    Would one aggregate postflight command materially reduce terminal execution
    errors without turning apex_kb.py into a workflow engine?
  constraints:
    - current main only
    - no repository writes
    - no retrieval ranking changes
    - no new lifecycle states
    - preserve default dry-run and allow-write rules
```

Inspect only command dispatch and existing index, lint, quality, status, stale, and retrieval build interfaces.

Compare:

- existing multi-command postflight;
- a thin orchestration command that invokes existing functions;
- documentation-only command sequencing.

Return a binary recommendation with exact evidence, failure behavior, output schema, and target files. Reject the command if it duplicates logic or weakens evidence.
