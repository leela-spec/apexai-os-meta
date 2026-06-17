Here is the full audit.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/c3b490ae-f89d-430a-b50f-06a3d7136972/package-manifest-2.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=ZeEyw1ciHpM31wEKS3j1p1cso0E%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

---

## Score Summary

|Priority|File|MR|TE|RS|AVG|
|---|---|---|---|---|---|
|**P1**|`SKILL.md`|6|5|7|**6.0**|
|**P2**|`project-status-overview-contract.md`|4|3|5|**4.0**|
|**P3**|`ranking-and-validation-rules.md`|7|5|6|**6.0**|
|**P4**|`package-manifest.md`|5|3|4|**4.0**|
|**P5**|`current-project-status-overview-template.md`|6|7|8|**7.0**|
|**P6**|`starter-manual-test-overview.md`|7|8|9|**8.0**|
|**P7**|`PromptFlow.md`|8|5|6|**6.3**|

_10 = best practice · below 6 = significant rework needed_

---

## P1 — SKILL.md · Fix First, Highest Impact

**MR 6 · TE 5 · RS 7**

This is the entrypoint Claude routes through on every invocation — it carries the most weight and has the most critical failure points.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/6437db9d-1006-4269-ae5d-4a650ed2ab71/project-status-overview_SKILL-3.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=yqBEAckJ9BDUM8z0TD5RFaCxpyg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**Critical issues:**

- **Description fails as a routing key.** It starts with lowercase action verbs (`create, normalize, update...`) instead of a trigger-intent phrase. Claude's skill routing matches on _"Use this skill when..."_ intent language. A run-on action verb list is one of the weakest possible routing signals.
    
- **27 steps across 8 phases** is procedural over-engineering for a conceptually 6-action skill. Steps 3–5 (unassigned separation) collapse into one. Steps 21–25 (validate) duplicate the Completion Gate and cost ~90 tokens on every load.
    
- **No `Failure Modes` section.** Claude has no recovery path when input is missing, empty, or malformed — a skill this simple must handle the "no context supplied" case explicitly.
    
- **`Supporting Files` as prose bullets** cannot be machine-parsed. Claude cannot reliably determine _when_ to load each file from a dash-bullet list. It needs `read_when:` YAML conditions.
    

**Fix pattern for description:**

text

`description: >   Use this skill when the operator asks to create, update, rank, or validate  a compact cross-project status overview. Accepts manual notes, project  summaries, or previous overview text. Produces a project → task → subtask  overview with [priority/urgency/date] ratings. Does not create weekly plans,  daily plans, or detailed project databases.`

**Fix pattern for Supporting Files:**

text

`supporting_files:   - path: references/project-status-overview-contract.md    read_when: operator asks for contract structure or validation rules  - path: templates/current-project-status-overview-template.md    read_when: creating a blank template or initial overview  - path: references/ranking-and-validation-rules.md    read_when: ranking tasks or validating ratings`

---

## P2 — `project-status-overview-contract.md` · Biggest Token Waste[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/408477a3-4f08-44f7-96ab-066b8e68bf22/project-status-overview-contract-4.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=%2FEThsaHkXGBNvGEU%2BGfd3uUz1dM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**MR 4 · TE 3 · RS 5** — The worst scorer in the batch.

**Critical issues:**

- **YAML rendered as collapsed single-line strings throughout.** All YAML indentation was lost in export. This makes every block unparseable — Claude reads it as a flat string, not a structured object. This is a file-format defect that breaks machine readability completely and must be fixed before any other optimization.
    
- **Triple-definition of the same schema.** The artifact_contract block, the Normalized Structure section, and the Section Contracts section all define the same fields three times. This burns approximately 800 tokens of redundant context on every load.
    
- **Non-Goals at the bottom** repeat the same list already in the artifact_contract header. One location only.
    
- **Rating Contract** is defined here _and_ in `ranking-and-validation-rules.md`. Choose one canonical home (ranking-and-validation-rules.md is better) and reference it.
    

**Fix pattern:** Collapse to a single canonical YAML block defining: artifact_contract → required_sections → field_contracts → non_goals. Remove Sections 2–5 entirely. Total file should be under 80 lines.

---

## P3 — `ranking-and-validation-rules.md` · Strong Logic, Formatting Problems[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/13b2e954-11a3-4f12-bdcd-92149c4ca2d3/ranking-and-validation-rules-6.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=OcZkzGW9kFVDaodnkERNKLE%2Fu9w%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**MR 7 · TE 5 · RS 6**

This has the best-designed logic in the batch — the Rating Parser with invalid_examples is genuinely best-practice and Claude can use it reliably as a validation anchor.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/13b2e954-11a3-4f12-bdcd-92149c4ca2d3/ranking-and-validation-rules-6.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=OcZkzGW9kFVDaodnkERNKLE%2Fu9w%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**Issues:**

- Same YAML collapse problem throughout.
    
- Failure Modes section (7 modes × 3-4 correction steps each) costs ~420 tokens. Compress each to: `trigger_condition: correction_in_one_line`. Keep multi-step correction only for `ranking_conflict` and `over_detailed_expansion`.
    
- **`Correction Behavior`** section at the bottom duplicates the failure modes. Remove it; its rules are implied by the failure modes already.
    
- **`Minimal Validation Record`** at the bottom is a template that belongs in the template file, not here.
    
- **`rules_metadata`** block at the top costs ~40 tokens with zero routing or execution value. Remove it.
    
- **Deadline pressure** uses "1-7 days / 8-30 days" windows that assume Claude knows the current date. Add: _"Apply deadline pressure relative to the date at skill execution time."_
    

**What to preserve exactly as-is:** rating_parser, ranking_rule, tie_breaking, and the validation_checks sub-blocks — these are the best-written sections in the entire package.

---

## P4 — `package-manifest.md` · Over-engineered, Low Execution Value[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/c3b490ae-f89d-430a-b50f-06a3d7136972/package-manifest-2.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=ZeEyw1ciHpM31wEKS3j1p1cso0E%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**MR 5 · TE 3 · RS 4**

The manifest is the second-worst scorer. A manifest should be a lightweight index that helps Claude know what files exist and when to load them. This file became a second contract document.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/c3b490ae-f89d-430a-b50f-06a3d7136972/package-manifest-2.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=ZeEyw1ciHpM31wEKS3j1p1cso0E%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**Issues:**

- YAML single-line collapse.
    
- File Inventory section has ~600 tokens of read_when bullets and validation_role bullets per file — this belongs in `CLAUDE.md`, not in an in-skill manifest.
    
- `Package-Level Acceptance Checks` and `Final Package Acceptance Criteria` are duplicated at the end — one must go.
    
- `First Manual Test Instruction` belongs in `starter-manual-test-overview.md`, not here.
    
- No `read_when: operator inspects package structure` condition telling Claude _when_ to load this file. Without it, Claude may load it on every invocation.
    

**Fix pattern:** Strip to: package_metadata → file_list (path + purpose + read_when, one line each) → package_boundaries (must_do / must_not_do flat list) → one acceptance_checks block. Target: under 60 lines.

---

## P5 — Template · Best Structure in the Batch[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/e4495fd0-cde8-430d-bb22-63b30500b745/current-project-status-overview-template.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=8vMulEGTcYwCCJfmuTPfsL6fYWs%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**MR 6 · TE 7 · RS 8**

Highest RS score for a reason — the template is compact, copy-paste ready, and correctly ordered.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/e4495fd0-cde8-430d-bb22-63b30500b745/current-project-status-overview-template.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=8vMulEGTcYwCCJfmuTPfsL6fYWs%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**Issues:**

- YAML single-line collapse (same root problem).
    
- `Operator Validation` section mixes blank state with schema definition. Template should only contain empty placeholders, not embed the full check list.
    
- Field names in `ranking_notes` use `pinned/promoted/demoted/frozen` but `ranking-and-validation-rules.md` uses `pin/promote/demote/freeze` as action names. Align these.
    
- Dual representation per project (markdown heading + code block) adds no value; pick one.
    

---

## P6 — Starter Example · Best File in the Batch[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/c83c1401-fdbc-437b-a260-68e6b6e6f593/starter-manual-test-overview-7.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=mKyCJdGCRsgqx52R9%2FeDUVTE6Qk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**MR 7 · TE 8 · RS 9**

This is the closest to best-practice of all seven files. Realistic data, correct format, honest review-needed markers.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/c83c1401-fdbc-437b-a260-68e6b6e6f593/starter-manual-test-overview-7.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=mKyCJdGCRsgqx52R9%2FeDUVTE6Qk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**One genuine structural error:** The `Others` project contains tasks (`inbox-container`, `assignment-review`) that should be in the `Unassigned` section — since `Others` is defined in the system as a temporary holding project, giving it permanent tasks contradicts the unassigned_policy. Move these to `Unassigned` with `assignment_status: unassigned`.

**Minor issue:** Field name mismatch — `operator_review_needed` vs the template's `operator_validation`. Align to one name.

---

## P7 — PromptFlow.md · Good Discipline, Redundancy Problem[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/1ae29411-851b-43d2-bd1a-c994f45b1a71/PromptFLow-5.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=x5bfbb%2FLDmd8T%2F2fiIxLjx0V2jU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**MR 8 · TE 5 · RS 6**

The prompt flow has the best machine readability score because its YAML metadata is actually correct and the one-file-per-prompt contract is clean.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/1ae29411-851b-43d2-bd1a-c994f45b1a71/PromptFLow-5.md?AWSAccessKeyId=ASIA2F3EMEYESFNGTRGI&Signature=x5bfbb%2FLDmd8T%2F2fiIxLjx0V2jU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIFRKpeaook%2FvVtyfjdakbeGjYRGQUSW2DCDqu1OXJz8tAiAyqVyJr43yJctrMpeT9YLtUkUbm5x2rmPjibbrves%2B%2BSrzBAhxEAEaDDY5OTc1MzMwOTcwNSIMYxyLj0af2F1EeC4KKtAEF52WOW4FsOC1ZPiUyq1b2NyJpfGwk6XIAStg1OX37q2g6KOCz2pATMGT6t1veHk%2FP5JD3igI98FiLgl%2BW0kYa7fB1vvaHS9453H%2FaZsRbN7ZE1NZF148Gq9by7VVe5i9Wmvv1yS2JkvI1CTpjn2Mczcv5Z%2FI%2BhOvsdmWBsabI5caVLm95n31ITS2t1PME2wp0g6nCZVu3IYOQRMhRbj3nOqb3ItYKLgGmRmYaVJJb7a%2BnNDq7KbYAyXXCI6cC7B3SIC6ZLwAVpMeRKrpEajDp0Xx%2F2%2FircKFBu4KPapg12Z0S7jnaLWAP6m%2Bd8%2FDlwRpgQXI2uuG6GMEuOyfR58L%2Fw%2FJ8XDH4agTGvfyxyViVtvqfIU1q0l95sWRuPl8vFPcdNn05MhUGcVaGkdhvmOTwhW6yDyk7Y66pMSdsfDyoPta%2B%2FH8NVVTAuMLCMDz1bwmls6dpFwotmUMKiHFFAViyFVMfK7oxibATjvLMeTXWKtY2ID8xerkHw4ptlYZLTDdUPuzqGj59N0tggl%2BXfXAnXIoAGclwlPRlCkPoHmOvoXB4OUcFpUAFkS8w7tW6nw0jEKwYEufsm9Mvik2OswOnqvslfowB87gif30d9IdJz13yi8C2YUVP%2F7oME79buUSdY3xti2vL0HmwdZNroqILNDltdmGl5%2FNimbEk9%2FOJe%2BsTvnUJ1Yu8LsjyKGxGgIbVaEOshRc0HxTgmU%2FDboA3OD7Dhf1z4KrMtJn26I9Er9CIzQiyvjKNITFv199DEVVXUsM8ByuMrU3CfDOCZtN7TDngMTRBjqZAeG061WFKfwIYybgN1LH7KJrregQv6JgBdgrpyKOUXI8b2QI7atHoB0UIsyn9A9biiSCZxNkuQxneRHvmK0eMsgtQboCMTY6nfbqn1txCG%2B%2BGUEsNBdPoQCYgYm11Q7EhANgFMm6J8wPKd7yEzt8gps9xtERN7V435C3b5Pkr4iTN4paYcVzA9T9fWecwwfd3i7YAAtIUT%2FYOQ%3D%3D&Expires=1781599802)]

**Issues:**

- **Prompt 0 (Package Plan Validation)** costs one full GPT extended-thinking turn but produces an output that is immediately discarded. The binding_decisions block at the top already does this job. Remove Prompt 0.
    
- **Each prompt's VALIDATION CHECKLIST** repeats the same 6–8 common items with minor variation. Define a `global_validation_checklist` at the top; each prompt checklist should only add file-specific items (2–3 max).
    
- `canonical_projects_initial` is defined in binding_decisions but also hardcoded in Prompts 3 and 4. One source only.
    
- Prompt 5's requirements paragraph re-specifies the full ranking rules that already exist in the generated file. Compress to 3 bullets max.
    

---

## Consolidated Fix Priorities for the Next Skill Creation Cycle

**Fix these before writing the next skill file:**

1. **YAML formatting** — Every file suffers the same collapse-to-single-line defect. The root cause is the export/generation step losing indentation. Fix this in the GPT prompt flow output contract: require indented YAML in all generated files, test by checking that the first YAML block parses with a YAML linter.
    
2. **Description trigger pattern** — Every SKILL.md must start with `"Use this skill when..."` — not action verbs. This is the single highest-impact routing fix.
    
3. **Deduplicate contracts** — Define each schema once. The contract file defines fields; the SKILL.md references the contract file; the template uses the fields. No field definition should appear in more than one file.
    
4. **Compress failure modes** — One-line trigger + one-line correction for 5 of 7 modes. Reserve multi-step correction for complex cases only.
    
5. **Trim the manifest** — A manifest is an index, not a second contract. Keep it under 60 lines.
    
6. **Add `read_when` to all support files** — Every file that Claude might lazy-load needs a YAML `read_when:` condition so it is not loaded on every invocation.
    
7. **Align field names across all files** — `operator_validation` vs `operator_review_needed`, `pin` vs `pinned` — pick one form per concept and use it everywhere.