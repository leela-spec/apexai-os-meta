---
# CONSUMED RECAP REGISTRY
# Idempotency log — prevents duplicate FlowRecap merges.
# Append one consumed_recap_entry per FlowRecap merged. Never delete entries.
# Schema: recap_id, consumed_at (YYYY-MM-DD), project_id, session_id

last_updated: 2026-06-18
---

```yaml
consumed_recaps: []
# Example entry (remove # to activate):
# - recap_id: flow-recap-2026-06-18-F1
#   consumed_at: 2026-06-18
#   project_id: apex-os-meta
#   session_id: session-2026-06-18-F1
```
