[OUTPUT_ROUTER v1.0]
PURPOSE: maps task_type to exact output schema — agent selects and follows

ROUTE_TABLE:
┌─────────────────┬──────────────────────────────────────────────┐
│ task_type       │ output_schema                                │
├─────────────────┼──────────────────────────────────────────────┤
│ file_write      │ TEMPLATE_05: FILE_OUTPUT                     │
│ diff_patch      │ TEMPLATE_06: DIFF_OUTPUT                     │
│ research_block  │ TEMPLATE_07: RESEARCH_OUTPUT                 │
│ state_update    │ TEMPLATE_02: STATE_BLOCK (write mode)        │
│ manifest        │ TEMPLATE_10: MANIFEST_OUTPUT                 │
│ gate_check      │ TEMPLATE_08: GATE_CHECK                      │
│ clarify/halt    │ TEMPLATE_09: CONTROL_SIGNALS                 │
└─────────────────┴──────────────────────────────────────────────┘

RULE: agent outputs ONLY the schema for its assigned task_type.
      Any additional keys or prose outside schema = SCOPE_VIOLATION.
