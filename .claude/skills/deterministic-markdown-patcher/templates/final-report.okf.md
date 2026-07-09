**Final Report Template**

Use this template to compile a final report after running a deterministic
patch.  Replace the placeholders with concrete information from your
execution.  Reports should be concise and easy to audit.

```markdown
## Patch Summary

- **Target file**: `{{ target_file }}`
- **Mode used**: `{{ mode }}`
- **Intent description**: {{ intent_description }}

## Execution Details

1. **Original excerpt**
   
   ```text
   {{ original_excerpt }}
   ```

2. **Replacement applied**
   
   ```text
   {{ replacement_text }}
   ```

3. **Validation result**
   
   - Outcome: {{ validation_outcome }}
   - Notes: {{ validation_notes }}

4. **Unified diff**
   
   ```diff
   {{ unified_diff }}
   ```

## Outcome

- **Success?** {{ success_flag }}
- **Failure modes encountered**: {{ failure_modes }}

## References

Consult the supporting files for more information:

- Patching process contract (read_when: reviewing this report)
- Failure modes and recovery (read_when: encountered a failure)
```