---
task_id: TASK-01
target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
write_class: scaffold_update
audit_flags: [KB-ACHK-04, KB-ACHK-06, KB-ACHK-08]
created_at: 2026-05-07
---

```yaml
PATCH_PLAN:
  task_id: TASK-01
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
  target_file_sha: 5136459e6986bf8eb7e191c3c43e58aa2aca9d36
  write_class: scaffold_update
  operations:
    - op_id: OP-01
      priority: critical
      mode: search_replace
      old_text: |
        ## Appendix pointers
      new_text: |
        - id: `PW-BP-012`
          status: accepted
          practice: Structure KB files so active rules, checks, frontmatter, and machine-consumed templates are parse-valid YAML with explicit tier, prevents, evidence_refs, schema-contract, and validation metadata.
          context_conditions:
            - scaffold or appendix content is loaded as agent context
            - rule, checklist, template, or output contract may be machine-consumed
            - KB file lacks frontmatter fields needed for audit, staleness, or model-target validation
            - active policy prose can be compressed into YAML without losing meaning
          evidence_refs:
            - `KB_AUDIT_V2_UPDATE_PIPELINE.md#AUDIT-BASIS`
            - `KB_AUDIT_V2_UPDATE_PIPELINE.md#WRITE-CLASS-DECISION`
            - `KB_AUDIT_V2_UPDATE_PIPELINE.md#PATCH-FILE-CONTRACT`
          scores:
            EVD: 5
            IMP: 5
            RSK: 5
          owner: special_ops__prompts_workflows
          validator: meta_ops
          review_due: 2026-07-27
        
        ## Appendix pointers
      expected_occurrences: 1
      why_authorized: "KB audit checks KB-ACHK-04, KB-ACHK-06, and KB-ACHK-08 require schema-aware machine-consumed outputs, rule metadata, and frontmatter/validation discipline to be represented in accepted scaffold practices."
```

```yaml
PREIMAGE_CHECK:
  task_id: TASK-01
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
  op_id: OP-01
  old_text_occurrences: 1
  old_text_copied_from_live_file: true
  result: pass
```

## target: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md

<<<<<<< SEARCH
## Appendix pointers
=======
- id: `PW-BP-012`
  status: accepted
  practice: Structure KB files so active rules, checks, frontmatter, and machine-consumed templates are parse-valid YAML with explicit tier, prevents, evidence_refs, schema-contract, and validation metadata.
  context_conditions:
    - scaffold or appendix content is loaded as agent context
    - rule, checklist, template, or output contract may be machine-consumed
    - KB file lacks frontmatter fields needed for audit, staleness, or model-target validation
    - active policy prose can be compressed into YAML without losing meaning
  evidence_refs:
    - `KB_AUDIT_V2_UPDATE_PIPELINE.md#AUDIT-BASIS`
    - `KB_AUDIT_V2_UPDATE_PIPELINE.md#WRITE-CLASS-DECISION`
    - `KB_AUDIT_V2_UPDATE_PIPELINE.md#PATCH-FILE-CONTRACT`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

## Appendix pointers
>>>>>>> REPLACE
