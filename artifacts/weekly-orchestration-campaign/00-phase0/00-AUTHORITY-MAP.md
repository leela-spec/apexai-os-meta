# 00-AUTHORITY-MAP — Weekly Orchestration Loop

> Campaign: Weekly Orchestration eval-driven improvement
> Snapshot: repo `/workspace` (leela-spec/apexai-os-meta), branch `main`, HEAD at time of mapping
> Scope: production authority required to map the weekly loop (Phase 0 read-only freeze)

## A. Primary production authorities (read in full)

| # | Role | Path | Blob SHA | Last commit | Last commit date |
| :-- | :-- | :-- | :-- | :-- | :-- |
| A1 | Loop control plane | `.claude/skills/weekly-orchestrator/SKILL.md` | `05e0b3a6443c52a5079ef3d6f70bd44fb8838e8c` | `d8d0d25e` | 2026-08-17 |
| A2 | Weekly planning stage | `.claude/skills/PrecapWeek/SKILL.md` | `6648abb4c88a526112403b6446a675729dcabb49` | `4dc3d7a8` | 2026-08-17 |
| A3 | Weekly output template | `.claude/skills/PrecapWeek/weekly-command-brief-template.md` | `04ed26629719247f25ae3cc186d157b8d8d33f41` | `a0f32917` | 2026-08-18 |
| A4 | Daily planning stage | `.claude/skills/PrecapNextDay/SKILL.md` | `7e9a2b6fdf618cb56aa5cc5f65e2ae3d095e55a2` | `7478f4b5` | 2026-08-17 |
| A5 | Next-day brief template | `.claude/skills/PrecapNextDay/templates/precap-next-day-brief-template.md` | `c96747e21fca5a02debcc397a9c88d33c3f0f53c` | `772432887` | 2026-07-23 |
| A6 | Flow execution card template | `.claude/skills/PrecapNextDay/templates/flow-execution-card-template.md` | `ca404e6027e3be60c22a9fd500edc0e82f500255` | `66ed8a3ad` | 2026-07-11 |
| A7 | Prompt files & index template | `.claude/skills/PrecapNextDay/templates/prompt-files-and-index-template.md` | `b4e95f47a5b8da3dda38a4488818e825f45ca7e3` | `66ed8a3ad` | 2026-07-11 |

## B. Routing / activation authority above the loop

| # | Role | Path | Notes |
| :-- | :-- | :-- | :-- |
| B1 | Project activation surface | `.claude/CLAUDE.md` | Declares **two** orchestration systems. Weekly Orchestrator activates only for weekly-loop intent; Multi-Agent Orchestration is a separate system (`apex-meta/orchestration/00-START-HERE.md`). Explicitly states the two systems do not share an orchestration contract. |
| B2 | Multi-Agent entrypoint | `apex-meta/orchestration/00-START-HERE.md` | Confirms non-absorption of the weekly loop; five invariants (state-in-files, one mutation surface, one gate primitive, independent review, candidate-no-auto-promote). |

## C. Stage ownership as declared by A1 (`stage_routing`, verified consistent)

| Gate | Stage | Owner skill | Execution mode | Trigger |
| :-- | :-- | :-- | :-- | :-- |
| G1 | precap_week | PrecapWeek | context_fork | "run precap-week \| week start" |
| G2 | precap_next_day | PrecapNextDay | context_fork | after G1 or after status merge |
| G3 | operator_execution | operator / external surface | external | operator returns evidence or skip signal |
| — | evidence_normalize | raw-flow-dump-normalize | conditional_context_fork | raw evidence arrives |
| G4 | flow_recap | flow-recap | context_fork_per_flow, parallelizable | normalized dump + flow packet ready |
| G5 | status_merge | status-merge | context_fork_per_batch | once daily, manual |
| — | project_status | ProjectStatus | optional_context_fork | after confirmed Session mutation |
| — | review | apex-review-validity, apex-review-alignment | custom subagents (not forks) | consequential packet per review-wiring |
| — | durable_mutation | apex-session | shared backbone | after G5 confirmation |
| — | deterministic_read_side | apex-sync | shared backbone | per Sync contract |

Authority grants in A1: lifecycle=weekly-orchestrator; weekly_planning=PrecapWeek;
daily_planning=PrecapNextDay; prompt_content=PromptEngineer; AI_routing=AIRouting;
evidence_normalization=raw-flow-dump-normalize; recap=flow-recap;
candidate_merge=status-merge; durable_mutation=apex-session;
deterministic_computation=apex-sync; project_projection=ProjectStatus;
review_validity=apex-review-validity; review_alignment=apex-review-alignment.

A1 boundary: must_not_own = [stage_packet_schemas, project_work_execution,
skill_contract_content, calendar_or_scheduler_creation].

## D. Downstream artifact chain (templates → consumers)

```
PrecapWeek ──(G1)──► Weekly Command Brief [A3]
                        │  compact downstream handoff block (the seed; no separate duplicate artifact)
                        ▼
PrecapNextDay ──(G2)──► PreCap Next Day Brief [A5]
                        ├─► Flow Execution Card per represented full flow [A6]
                        │      └─ S1–S3 sprint detail, prompt access, done/stop/evidence conditions
                        └─► Prompt Files and Index [A7] + real per-sprint prompt files
                              └─ next_consumer: operator_execution
Operator executes (G3) → raw-flow-dump-normalize → flow-recap (G4)
                        → status-merge (G5) → apex-session (durable mutation) → feed refresh
```

Ownership rules actually encoded in the live files:

- A3's "Compact downstream handoff" yaml block *is* the PrecapNextDay seed
  (A2 §downstream: `reference_plus_minimal_seed`; A2 procedure step 6 forbids
  duplicating the full weekly result into a separate machine artifact).
- A4 boundary: the Brief carries only the compact cross-flow summary; each Flow
  Execution Card owns its own workspace content ("Do not duplicate the full flow
  context across the Brief, a Flow Execution Card, and its prompt files").
- A7 quality check explicitly requires: "The prompt file does not duplicate J4
  tasks, dependencies, or execution sequence."

## E. Referenced-but-not-authoritative design material

| Ref | Status |
| :-- | :-- |
| `.claude/skills/PrecapWeek/references/weekly-plan-output-contract.md` | **Does not exist on main.** Named as `source_gap` inside A3 itself (template self-declares the gap). No contract conflict possible; treat A3 + A2 as the sole weekly output authority. |
| `apex-meta/operator-output-design/step3-output-design-system/*.okf.yaml` (source_design_ref of A3/A5/A6/A7) | Design lineage pointers. Present as provenance metadata only. Not runtime authority; not read as authority for this campaign unless a Phase 4+ design question requires it. |
| Module 01 walkthroughs under `apex-meta/kb/Weekly-Orchestrator/architecture/*` | Descriptive KB records (macro decision, trace verification, patch plan). Consistent with A1's stage/gate semantics (G1–G5 = stage gates). Read-only corroboration; not edited during evaluation. |

## F. Contradiction resolution summary

Full register: `00-CONTRADICTION-REGISTER.md`. Resolution applied for this campaign:

1. **G1–G5 stage-gate semantics (owner: A1)** are the ONLY semantics valid inside
   the Weekly Orchestrator loop. Any document using G1–G5 to mean portfolio
   milestone locks or MCDA screening criteria is outside this campaign's control
   plane and must be disambiguated before any simulation references it.
2. The generic blueprint at `apex-meta/orchestration/workflows/WEEKLY_ORCHESTRATION_BLUEPRINT.md`
   is **demoted to a foreign cadence document**: it may describe a Monday–Friday
   cadence but its G1–G5 milestone gates are NOT the weekly loop's gates.
3. MCDA charter criteria G1–G10 are renamed-by-context only: they are evaluation
   rubric IDs for tool selection and share nothing with either gate system.

Gate condition satisfied: after this mapping, every tested concept has exactly
one owning authority (A1 for control-plane semantics; A2+A3 for weekly planning;
A4–A7 for daily planning).
