# Prompt Files and Index - F1-F3 (W36-E TUE)

> **Prompt access state:** READY_WITH_DEGRADED_ITEMS   
> **Outcome:** Small-context prompts ready; the full-context walk prompt is DEGRADED on the available surface and says so.  
> **Next action:** OPEN_NEXT_PROMPT  
> **Review needed:** F1-S2 routing decision

## Prompt index

### Flow `F1` (Lika prep + walk)

| Sprint | Prompt file | Recommended surface | Use when | Status |
| :-- | :-- | :-- | :-- | :-- |
| `F1-S1` | [Pre-flight with freshness stamp](prompts/f1-s1-preflight-freshness.md)<br>`prompts/f1-s1-preflight-freshness.md` | local model (small ctx) | schema + age stamping | READY |
| `F1-S2` | [Full walk](prompts/f1-s2-walk-full.md)<br>`prompts/f1-s2-walk-full.md` | PRIMARY SURFACE ONLY | full-context validation | **DEGRADED** - surface unavailable (quota); do not run on fallback without chunked variant approval |
| `F1-S2'` | [Chunked walk variant](prompts/f1-s2-walk-chunked.md)<br>`prompts/f1-s2-walk-chunked.md` | local model | fallback if operator approves chunking | READY (pending decision) |
| `F1-S3` | classification (standard pattern) | any | post-walk classification | READY |

### Flow `F2` / `F3`

| Sprint | Prompt file | Recommended surface | Use when | Status |
| :-- | :-- | :-- | :-- | :-- |
| `F2-S1` | mapping extension (standard f2-s2-map pattern, next batch) | local model | extend source map | READY |
| `F3-S1` | ADR spot-check (small sample pass) | local model | pointer hygiene fill | READY |

## Missing or degraded prompt items

### F1-S2 full walk

- **Issue:** recommended surface exhausted (quota); fallback unproven at this context size.
- **Execution impact:** full walk cannot safely proceed as-is.
- **Required action:** operator chooses CHUNKED_FALLBACK or DEFER_TO_RESET.

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Prompt_Files_and_Index"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-E-usage-scarcity/next-day-tue/prompts-index.md"
  flow_id: "F1,F2,F3"
  prompt_files:
    - {sprint: "F1-S1", title: "Pre-flight freshness", file: "prompts/f1-s1-preflight-freshness.md", target_surface: "local", routing_ref: "default-local", use_when: "stamp+schema", degraded_flag: "false"}
    - {sprint: "F1-S2", title: "Full walk", file: "prompts/f1-s2-walk-full.md", target_surface: "primary-only", routing_ref: "quota-blocked", use_when: "full validation", degraded_flag: "true"}
    - {sprint: "F1-S2c", title: "Chunked walk", file: "prompts/f1-s2-walk-chunked.md", target_surface: "local", routing_ref: "pending-approval", use_when: "fallback validation", degraded_flag: "false"}
  review_status: "degraded item open"
  next_consumer: "operator_execution"
```
