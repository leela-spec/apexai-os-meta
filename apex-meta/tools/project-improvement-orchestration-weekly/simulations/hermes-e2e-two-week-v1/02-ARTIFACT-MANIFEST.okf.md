# Artifact Manifest
```yaml
artifact_manifest:
  total_prompts: 120
  prompts_per_day: 12
  flows_per_day: 4
  days_per_week: 5
  schema_versions:
    rollup: "2.0"
    routing_record: "1.1"
    usage_ledger: "1.0"
    gate_record: "1.0"
```
All prompt references in execution cards point to physical `.md` files under `prompts/`.
