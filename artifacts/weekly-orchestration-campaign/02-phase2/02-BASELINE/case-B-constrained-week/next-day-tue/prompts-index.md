# Prompt Files and Index - F1 (W37 TUE, Case B constrained day)

> **Prompt access state:** READY   
> **Outcome:** One sprint prompt active today (F1-S3 classification); no degraded items.  
> **Next action:** OPEN_NEXT_PROMPT  
> **Review needed:** NONE

## Prompt index

### Flow `F1` (Lika findings triage)

| Sprint | Prompt file | Recommended surface | Use when | Status |
| :-- | :-- | :-- | :-- | :-- |
| `F1-S3` | [Findings classification handoff](f1-s3-handoff.md)<br>`f1-s3-handoff.md` | session-local agent worker | classify Monday WALK_REPORT findings for THU intake | READY |

S1/S2 prompts exist in the Case-A pack but are NOT scheduled today (compressed day).

**Routing reference:** default-session-local; unverified pending operator confirmation.

## Missing or degraded prompt items

(none)

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Prompt_Files_and_Index"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-B-constrained-week/next-day-tue/prompts-index.md"
  flow_id: "F1"
  prompt_files:
    - sprint: "F1-S3"
      title: "Findings classification handoff"
      file: "f1-s3-handoff.md"
      target_surface: "session-local agent worker"
      routing_ref: "default-session-local"
      use_when: "classify walk findings"
      degraded_flag: "false"
  review_status: "clean"
  next_consumer: "operator_execution"
```
