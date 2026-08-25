# Prompt Files and Index - F1+F2 (W36 TUE, Case A)

> **Prompt access state:** READY   
> **Outcome:** Five sprint prompt files available for today's two flows; none degraded.  
> **Next action:** OPEN_NEXT_PROMPT  
> **Review needed:** NONE

## Operator actions

- [ ] Open the prompt file required by the active sprint.
- [ ] Fix a missing or degraded prompt before execution.
- [ ] Confirm the referenced route when approval is still pending.
- [ ] Return to the Flow Execution Card for work context.

**Flow Execution Cards:** `flow-execution-card-f1.md` / `flow-execution-card-f2.md`

## Prompt index

### Flow `F1` (Lika main-index validation walk)

| Sprint | Prompt file | Recommended surface | Use when | Status |
| :-- | :-- | :-- | :-- | :-- |
| `F1-S1` | [Pre-flight schema check](f1-s1-preflight.md)<br>`f1-s1-preflight.md` | session-local agent worker | before walking: confirm index schema unchanged since Monday | READY |
| `F1-S2` | [Full index validation walk](f1-s2-walk.md)<br>`f1-s2-walk.md` | session-local agent worker | after clean pre-flight: execute 100%-coverage walk producing classified findings | READY |
| `F1-S3` | [Findings classification handoff](f1-s3-handoff.md)<br>`f1-s3-handoff.md` | session-local agent worker | after walk: split findings fix-now vs defer-with-reason for WED intake | READY |

### Flow `F2` (ACIM outline source mapping)

| Sprint | Prompt file | Recommended surface | Use when | Status |
| :-- | :-- | :-- | :-- | :-- |
| `F2-S1` | [Section skeleton from locked TOC](f2-s1-sections.md)<br>`f2-s1-sections.md` | session-local agent worker | outline prep: derive ordered section list with purposes | READY |
| `F2-S2` | [Source-ID mapping](f2-s2-map.md)<br>`f2-s2-map.md` | session-local agent worker | after S1: attach canonical source IDs per section into mapping table | READY |

**Routing reference:** none approved this week; all prompts route to session-local agent workers by default. Route confirmation pending operator validation (not requested).

## Missing or degraded prompt items

(none)

## Reusable single-prompt-file template

Per production template `.claude/skills/PrecapNextDay/templates/prompt-files-and-index-template.md` blob `b4e95f47`. Individual files follow its block structure exactly.

## Prompt-file quality check

- [x] Each prompt states the task and desired return clearly.
- [x] Required context and hard constraints appear once.
- [x] Stop/review boundaries explicit where consequential.
- [x] No private chain-of-thought requests.
- [x] Prompts do not duplicate J4 tasks/dependencies/sequence - each carries only sprint-specific inputs and return contract.
- [x] Surfaces marked as default routing, unverified pending operator confirmation.

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Prompt_Files_and_Index"
  artifact_ref: "artifacts/weekly-orchestration-campaign/02-phase2/02-BASELINE/case-A-normal-week/next-day-tue/prompts-index.md"
  flow_id: "F1,F2"
  prompt_files:
    - sprint: "F1-S1"
      title: "Pre-flight schema check"
      file: "f1-s1-preflight.md"
      target_surface: "session-local agent worker"
      routing_ref: "default-session-local"
      use_when: "pre-walk schema confirmation"
      degraded_flag: "false"
    - sprint: "F1-S2"
      title: "Full index validation walk"
      file: "f1-s2-walk.md"
      target_surface: "session-local agent worker"
      routing_ref: "default-session-local"
      use_when: "100% coverage walk"
      degraded_flag: "false"
    - sprint: "F1-S3"
      title: "Findings classification handoff"
      file: "f1-s3-handoff.md"
      target_surface: "session-local agent worker"
      routing_ref: "default-session-local"
      use_when: "fix-now vs defer split"
      degraded_flag: "false"
    - sprint: "F2-S1"
      title: "Section skeleton from locked TOC"
      file: "f2-s1-sections.md"
      target_surface: "session-local agent worker"
      routing_ref: "default-session-local"
      use_when: "outline section derivation"
      degraded_flag: "false"
    - sprint: "F2-S2"
      title: "Source-ID mapping"
      file: "f2-s2-map.md"
      target_surface: "session-local agent worker"
      routing_ref: "default-session-local"
      use_when: "canonical ID attachment"
      degraded_flag: "false"
  review_status: "clean"
  next_consumer: "operator_execution"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/05-prompt-file-and-index-design.okf.yaml"
  round6_overlay_intent_ref: "canonical_name_projection_from_00-package-manifest.okf.yaml"
  overlay_application_status: "presentation_name_used_without_repository_mutation"
  domain_contract_refs:
    - ".claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md"
```
