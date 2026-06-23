---
task_id: TASK-03
target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
write_class: scaffold_update
audit_flags: [KB-ACHK-04, KB-ACHK-06, KB-ACHK-08]
created_at: 2026-05-07
---

```yaml
PATCH_PLAN:
  task_id: TASK-03
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
  target_file_sha: "a195fde9cd13d74fa144b006e303204f2174c880"
  write_class: scaffold_update
  operations:
    - op_id: OP-01
      priority: critical
      mode: search_replace
      old_text: |
        ## Appendix pointers
      new_text: |
        - id: `PW-TPL-011`
          status: accepted
          use_when: A scaffold or appendix update must be audited against KB_Audit_v2 before patch generation or promotion.
          template_body: |
            # KB Audit v2 Patch Packet

            ```yaml
            kb_audit_patch_packet:
              target_file: <repo-relative-path>
              source_policy: KB_Audit_v2.md
              active_checks:
                - KB-ACHK-01
                - KB-ACHK-02
                - KB-ACHK-03
                - KB-ACHK-04
                - KB-ACHK-05
                - KB-ACHK-06
                - KB-ACHK-07
                - KB-ACHK-08
              required_contracts:
                - parse_valid_yaml
                - critical_rules_early
                - rule_metadata_present
                - schema_enforced_machine_outputs
                - active_policy_prose_bounded
                - required_frontmatter_present
                - fetch_back_validation
              machine_output_contract:
                schema_enforced: true
                prose_only_allowed: false
              patch_validation:
                fetch_live_target_first: true
                copy_old_text_verbatim: true
                expected_old_text_occurrences: 1
                fetch_back_patch_file: true
              write_class_decision: scaffold_update | full_body_replace | no_op
              patch_output: <patches/TASK-XX_FILE.patch.md>
            ```

            Run checks before writing. For search/replace patches, copy `old_text` verbatim from the live file and require exactly one occurrence. Use `full_body_replace` only when the file is structurally broken and the patch plan authorizes it.
          evidence_refs:
            - `KB_Audit_v2.md#active-deployment-checks-8`
            - `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
          scores:
            EVD: 5
            IMP: 5
            RSK: 5
          owner: special_ops__prompts_workflows
          validator: meta_ops
          review_due: 2026-08-07

        ## Appendix pointers
      expected_occurrences: 1
      why_authorized: "KB audit checks require a reusable template for KB_Audit_v2-governed scaffold and appendix patch packets."
```

```yaml
PREIMAGE_CHECK:
  task_id: TASK-03
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
  op_id: OP-01
  old_text_occurrences: 1
  old_text_copied_from_live_file: true
  result: pass
```

## target: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md

<<<<<<< SEARCH
## Appendix pointers
=======
- id: `PW-TPL-011`
  status: accepted
  use_when: A scaffold or appendix update must be audited against KB_Audit_v2 before patch generation or promotion.
  template_body: |
    # KB Audit v2 Patch Packet

    ```yaml
    kb_audit_patch_packet:
      target_file: <repo-relative-path>
      source_policy: KB_Audit_v2.md
      active_checks:
        - KB-ACHK-01
        - KB-ACHK-02
        - KB-ACHK-03
        - KB-ACHK-04
        - KB-ACHK-05
        - KB-ACHK-06
        - KB-ACHK-07
        - KB-ACHK-08
      required_contracts:
        - parse_valid_yaml
        - critical_rules_early
        - rule_metadata_present
        - schema_enforced_machine_outputs
        - active_policy_prose_bounded
        - required_frontmatter_present
        - fetch_back_validation
      machine_output_contract:
        schema_enforced: true
        prose_only_allowed: false
      patch_validation:
        fetch_live_target_first: true
        copy_old_text_verbatim: true
        expected_old_text_occurrences: 1
        fetch_back_patch_file: true
      write_class_decision: scaffold_update | full_body_replace | no_op
      patch_output: <patches/TASK-XX_FILE.patch.md>
    ```

    Run checks before writing. For search/replace patches, copy `old_text` verbatim from the live file and require exactly one occurrence. Use `full_body_replace` only when the file is structurally broken and the patch plan authorizes it.
  evidence_refs:
    - `KB_Audit_v2.md#active-deployment-checks-8`
    - `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-08-07

## Appendix pointers
>>>>>>> REPLACE
