All three L2 artifacts are written to the canonical paths from the simulation plan (Section 0). Full brief below — also saved at `apex-meta/orchestration/simulation/week-01/l2-daily-planning/day-mon/precap-next-day-brief-mon.md` (plus `flow-cards-f1..f4-mon.md` and `sprint-prompt-pack-mon.md`).

---

# PreCap Next-Day Brief — Day 1 (Monday)

```yaml
brief_type: precap_next_day_brief
producer: PrecapNextDay
simulation: APEX-E2E-SIM-2W-01
week: 1
day: mon
upstream_inputs:
  - l0-init/projectstatus-snapshot.yaml
  - l0-init/active-tasks-masterofarts.yaml
  - l0-init/capacity-model.yaml
  - l1-weekly-brief/weekly-command-brief.md   # G1 signed
gate: G2-Mon
leela_boundary: Leela app development OUT OF SCOPE — routed out, never planned.
```

## 1. Strategy & Focus for Day 1

**Headline (5-second test):** Monday is a cold start that proves the machine — one full chain L0→L5 on real work, four flows evidenced, every artifact checksummed before day close.

| :-- | Pri | Strategic Focus | Why It Leads Today | Success Signal |
| :-- | :-: | :-- | :-- | :-- |
| :-- | 🥇 | MoA/LHTL cold-start pipeline story | Highest-value front; sets the repeatable cadence the week depends on | Story closed with AC evidence at G3 |
| :-- | 🥈 | SuperHeroKids L0 baseline + task registry | Without a baseline, Tue–Fri SHK flows have no SSoT anchor | Snapshot + registry registered in ledger |
| :-- | 🥉 | Investment/IPOS W1 milestone scoping | Makes Tue–Thu decision-grade production deterministic | Scoped inputs with citations, zero fabrication |
| :-- | 4️⃣ | Apex Control full-chain dry-run (L0→L5) | The loop itself must prove it runs end-to-end on Day 1 | g3-checkpoint signed; zero fact bleed |

- **S1 (ship):** all four flows produce raw evidence at exact gate paths.
- **S2 (quality):** every evidence file sha256-registered before close.
- **S3 (compound):** baseline ledger live with token economics for F1–F4.

FreeT: AM 09:00–12:00 → F1 + F4 first half · PM 14:00–17:00 → F2, F3, F4 second half + operator review.

## 2. Flow Execution Cards

### 🥇 F1 — LHTL Cold-Start Pipeline Story

| :-- | Field | Value |
| :-- | :-- | :-- |
| :-- | Repo / Block | MasterOfArts · AM 09:00–12:00 (deep work) |
| :-- | Value prop | First link of a weekly LHTL cadence — one story closed with AC evidence, not ad-hoc grinding |
| :-- | Evidence | `l3-flow-execution/day-mon/flow-f1/raw-evidence/raw-flow-dump-f1-mon.{diff,md}` |
| :-- | Gate chain | G3-Mon/f1 → L3b → G4 → G5 |

ACs: (1) every story AC verified with evidence line from raw dump; (2) dump unmodified post-capture, sha256 registered; (3) zero foreign-repo facts; (4) blocked ACs fail closed with what/why/next-input notes — no silent partial completion.

### 🥈 F2 — SuperHeroKids Baseline Init & Task Registry

| :-- | Field | Value |
| :-- | :-- | :-- |
| :-- | Repo / Block | SuperHeroKids · PM 14:00–15:15 |
| :-- | Value prop | End of untracked drift — a real baseline every later flow can diff against |
| :-- | Evidence | `.../flow-f2/raw-evidence/raw-flow-dump-f2-mon.md` |
| :-- | Gate chain | G3-Mon/f2 → L3b → G4 → G5 |

ACs: snapshot schema conforms field-for-field to `l0-init/projectstatus-snapshot.yaml`; no empty required fields (nulls allowed); top-3 targets flagged as candidates only (decision is Tuesday's flow); zero fact bleed.

### 🥉 F3 — Investment/IPOS Macro Scope

| :-- | Field | Value |
| :-- | :-- | :-- |
| :-- | Repo / Block | Investment · PM 15:15–16:15 |
| :-- | Value prop | Scoped, citation-backed milestone — Tuesday's decision-grade artifact becomes assembly, not discovery |
| :-- | Evidence | `.../flow-f3/raw-evidence/raw-flow-dump-f3-mon.md` |
| :-- | Gate chain | G3-Mon/f3 → L3b → G4 → G5 |

ACs: every input carries a verifiable source or explicit `unverified` flag; single-sentence testable decision statement ("decide X given Y"); risk-register candidate entries; hard zero-fabrication tolerance.

### 4️⃣ F4 — Apex Control Plane Full-Chain Dry-Run

| :-- | Field | Value |
| :-- | :-- | :-- |
| :-- | Repo / Block | apexai-os-meta · AM 11:00–12:00 + PM 16:15–17:00 |
| :-- | Value prop | Proof the machine works — or a loud, specific failure instead of silent drift |
| :-- | Evidence | `.../flow-f4/raw-evidence/raw-flow-dump-f4-mon.log` |
| :-- | Gate chain | G3-Mon/f4 → L3b → G4 → G5 → L5 closure record |

ACs: deterministic verification rerun is byte-identical (hash match recorded); one deliberate bad-path probe shows clean fail-closed behavior; ledger writes append-only; checkpoint scaffolds match ledger schema fields (`state, evidence_path, sha256, decided_at, decision_note`).

## 3. Production Sprint Prompt Packs

Full executable packs saved in `sprint-prompt-pack-mon.md`. Contract summary:

| :-- | Pack | Exact Inputs | Output Contract | Definition of Done |
| :-- | :-- | :-- | :-- | :-- |
| :-- | PP-F1 | Story id + verbatim AC list from `active-tasks-masterofarts.yaml`; ProjectStatus row | Unified diff + AC→evidence log at f1 paths | All ACs evidenced or explicit blocked notes; raw dump unmodified; sha256 registered; zero bleed |
| :-- | PP-F2 | Repo tree + docs; snapshot schema field list | ProjectStatus snapshot + task registry YAMLs at f2 path | Schema-conformant; nulls OK/blanks not; top-3 flagged not decided |
| :-- | PP-F3 | IPOS task file + in-repo source inventory | Input inventory w/ citations + decision statement + risk candidates at f3 path | 100% inputs sourced or `unverified`; zero fabricated numbers |
| :-- | PP-F4 | Ledger YAML + expected F1–F3 evidence paths/sha256 + checkpoint templates | Verification log at f4 path + g3/g4/g5 scaffolds + token-economics rows | Rerun hash match; bad-path probe logged clean-fail; append-only registrations |

Standing pack rules: one repo per pack; missing/malformed input → fail closed naming the missing path, produce nothing partial; Leela items routed out only; raw evidence immutable after capture.

## 4. Code Architect Verification — Schemas & Paths

Path audit vs Plan Section 0:

| :-- | Artifact | Path | Status |
| :-- | :-- | :-- | :-: |
| :-- | Daily brief | `.../l2-daily-planning/day-mon/precap-next-day-brief-mon.md` | ✅ written |
| :-- | Flow cards | `.../day-mon/flow-cards-f1..f4-mon.md` | ✅ written |
| :-- | Prompt pack | `.../day-mon/sprint-prompt-pack-mon.md` | ✅ written |
| :-- | Checkpoint | `.../day-mon/g2-checkpoint-mon.yaml` | ⏳ pending G2 challenge round |
| :-- | Evidence roots | `.../l3-flow-execution/day-mon/flow-f{1..4}/raw-evidence/...` | ⏳ created during L3 only |

Schema rulings:
- Brief frontmatter keys conform to the PrecapNextDay contract — no drift vs Plan §2.
- All four cards carry uniform YAML keys (`card_id … value_proposition`); evidence filenames follow `raw-flow-dump-f{K}-day{N}.{log|diff|md}` exactly.
- Determinism ruling: model-generated material (F1 code, F3 text) counts as *input*, never gate evidence — only deterministic capture/registration steps do.
- Fail-closed imposed on every pack: missing input aborts named; malformed upstream YAML aborts; registration writes nothing unless the sha256 computed successfully.

---

Gate G2-Mon status: **open** — awaiting the BMAD / MarketingSkills / Observer-panel challenge round, then sign `g2-checkpoint-mon.yaml`. Want me to run that challenge round now?