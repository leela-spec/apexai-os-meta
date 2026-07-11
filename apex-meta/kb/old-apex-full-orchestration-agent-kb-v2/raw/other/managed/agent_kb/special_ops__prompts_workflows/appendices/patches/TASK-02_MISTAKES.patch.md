---
task_id: TASK-02
target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
write_class: scaffold_update
audit_flags: [KB-ACHK-04, KB-ACHK-05, KB-ACHK-06, KB-ACHK-07, KB-ACHK-08]
created_at: 2026-05-07
---

```yaml
PATCH_PLAN:
  task_id: TASK-02
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
  target_file_sha: "cf5a8ae1ec562963a7edd13fd312032d126fa357"
  write_class: scaffold_update
  operations:
    - op_id: OP-01
      priority: critical
      mode: search_replace
      old_text: |
        ## Appendix pointers
      new_text: |
        - id: `PW-MK-012`
          status: accepted
          pattern: KB scaffold or appendix rules are encoded as malformed YAML, prose-only machine contracts, duplicate paraphrases, metadata-light entries, or bloated active policy, causing downstream agents to misread priority, skip validation, or treat machine-consumed contracts as optional.
          trigger_conditions:
            - active rules, checks, or templates appear outside parse-valid YAML
            - rule entries lack tier, prevents, or evidence_refs
            - machine-consumed output contracts rely on prose-only instructions
            - required frontmatter fields are missing
            - active policy contains prose bloat or duplicated rules
          countermeasure: Run KB_Audit_v2 active checks before promotion. Encode active policy as compact YAML, keep evidence prose in appendices, require schema-enforced machine outputs, and fetch back patch artifacts before validation.
          evidence_refs:
            - `KB_Audit_v2.md#active-deployment-checks-8`
            - `KB_Audit_v2.md#appendix-a--anti-patterns`
            - `KB_Audit_v2.md#audit-report-template`
          scores:
            EVD: 5
            IMP: 5
            RSK: 5
          owner: special_ops__prompts_workflows
          validator: meta_ops
          review_due: 2026-07-27
        
        ## Appendix pointers
      expected_occurrences: 1
      why_authorized: "KB audit checks require compact representation of KB audit failure modes in the mistakes scaffold."
```

```yaml
PREIMAGE_CHECK:
  task_id: TASK-02
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
  op_id: OP-01
  old_text_occurrences: 1
  old_text_copied_from_live_file: true
  result: pass
```

## target: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md

<<<<<<< SEARCH
## Appendix pointers
=======
- id: `PW-MK-012`
  status: accepted
  pattern: KB scaffold or appendix rules are encoded as malformed YAML, prose-only machine contracts, duplicate paraphrases, metadata-light entries, or bloated active policy, causing downstream agents to misread priority, skip validation, or treat machine-consumed contracts as optional.
  trigger_conditions:
    - active rules, checks, or templates appear outside parse-valid YAML
    - rule entries lack tier, prevents, or evidence_refs
    - machine-consumed output contracts rely on prose-only instructions
    - required frontmatter fields are missing
    - active policy contains prose bloat or duplicated rules
  countermeasure: Run KB_Audit_v2 active checks before promotion. Encode active policy as compact YAML, keep evidence prose in appendices, require schema-enforced machine outputs, and fetch back patch artifacts before validation.
  evidence_refs:
    - `KB_Audit_v2.md#active-deployment-checks-8`
    - `KB_Audit_v2.md#appendix-a--anti-patterns`
    - `KB_Audit_v2.md#audit-report-template`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

## Appendix pointers
>>>>>>> REPLACE
