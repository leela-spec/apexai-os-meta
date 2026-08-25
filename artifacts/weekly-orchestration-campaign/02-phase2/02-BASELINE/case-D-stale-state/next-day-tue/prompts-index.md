# Prompt Files and Index - F1 (W36-D TUE)

> **Prompt access state:** READY   
> **Outcome:** Two drift-aware prompts ready; S3 reuses the standard classification prompt with a drift split.  
> **Next action:** OPEN_NEXT_PROMPT  
> **Review needed:** NONE

## Prompt index

### Flow `F1` (drift-aware validation walk)

| Sprint | Prompt file | Recommended surface | Use when | Status |
| :-- | :-- | :-- | :-- | :-- |
| `F1-S1` | [Pre-flight with freshness stamp](prompts/f1-s1-preflight-freshness.md)<br>`prompts/f1-s1-preflight-freshness.md` | session-local agent worker | schema + age stamping | READY |
| `F1-S2` | [Drift-aware walk](prompts/f1-s2-walk-drift.md)<br>`prompts/f1-s2-walk-drift.md` | session-local agent worker | full walk with DRIFT_SUSPECTED classing | READY |
| `F1-S3` | classification (standard f1-s3 pattern, two-list output) | session-local agent worker | error vs drift split | READY |

**Routing reference:** default-session-local; unverified pending operator confirmation.
