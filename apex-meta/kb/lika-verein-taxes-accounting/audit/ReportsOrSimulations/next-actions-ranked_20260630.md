# Apex KB Ranked Action Plan — 2026-06-30

```yaml
target_kb: "lika-verein-taxes-accounting"
mode: "ranked_extension_plan"
priority_formula: "impact + risk + token_efficiency_gap - complexity_penalty, normalized to 1-100"
```

| Rank | Action | Impact | Evidence | Risk | Token-efficiency gain | Complexity penalty | Priority | Why |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Verify which Phase 1/Phase 2 artifacts are actually in the local repo versus chat-output only | 95 | 88 | 72 | 70 | 15 | 98 | Prevents false repo-state assumptions before any next KB run. |
| 2 | Backfill source-specific Phase 1 analyses for high-risk legal/tax sources | 96 | 76 | 68 | 82 | 20 | 96 | Grouped analysis is useful but too coarse for tax/accounting claims. |
| 3 | Install or regenerate approved summary pages, then rebuild `wiki/index.md` | 90 | 70 | 52 | 88 | 18 | 92 | Current verified index has zero compiled pages, so retrieval cannot yet work as intended. |
| 4 | Create concept pages only with direct source pointers and risk labels | 94 | 62 | 66 | 90 | 22 | 91 | Concepts are the real retrieval acceleration layer but can become false-confidence nodes. |
| 5 | Generate entity pages for authorities/tools/providers | 84 | 58 | 54 | 78 | 16 | 86 | Entities make BMJ/BMF/AWV/LfSt/DRV-KSK/BZSt/pretix retrievable as stable nodes. |
| 6 | Run 8 query packet simulations and save outputs | 88 | 55 | 50 | 92 | 18 | 86 | Proves whether the KB actually saves tokens at query time. |
| 7 | Rebuild retrieval index after Phase 2 pages | 86 | 74 | 42 | 86 | 14 | 84 | Retrieval health before compiled pages is not enough. |
| 8 | Create table-heavy PDF verification queue | 82 | 82 | 58 | 62 | 16 | 82 | Prevents silent errors from PDF table conversion. |
| 9 | Create noisy-source quarantine report | 78 | 82 | 46 | 70 | 12 | 80 | Web clutter audit found many candidates; cleanup improves semantic accuracy. |
| 10 | Add `source-inventory.json/csv` or reconcile Phase 0 report expectation | 74 | 90 | 34 | 70 | 14 | 76 | Lifecycle report explicitly flagged absent source-inventory artifacts. |
| 11 | Add postflight risk register after semantic Phase 2 | 82 | 62 | 56 | 62 | 18 | 74 | High-risk tax gaps must remain visible. |
| 12 | Compress operator prompts around installed skill logic | 76 | 80 | 32 | 64 | 10 | 72 | Reduces over-prescription and operator confusion. |

## Deferred-gap matrix

| Gap | Why it matters | Impact | Evidence | Risk | Fix priority | Proposed fix |
|---|---|---:|---:|---:|---:|---|
| source-specific Phase 1 backfill | Legal/tax claims need direct source inspection | 96 | 72 | 68 | 1 | One `.analysis.md` per high-risk source or source cluster of same authority. |
| concept page source-pointer precision | Concepts become primary retrieval nodes | 94 | 62 | 66 | 2 | Require direct source path/hash/pointer for each material claim. |
| entity page generation | Authorities/tools/providers need stable nodes | 84 | 50 | 54 | 5 | Generate authority/entity pages after summaries/concepts. |
| query packet tests | Token-saving must be proven, not assumed | 88 | 55 | 50 | 4 | Run 8 standard queries and save packets. |
| retrieval index freshness | Stale retrieval can mislead future AI | 86 | 74 | 42 | 6 | Rebuild after Phase 2; run stale check. |
| table-heavy PDF verification | Tables can invert tax/accounting details | 82 | 82 | 58 | 7 | Add manual verification queue and source flags. |
| noisy source cleanup | Web clutter contaminates summaries | 78 | 82 | 46 | 8 | Quarantine or clean noisy captures before source-specific backfill. |
| venue settlement gap | Venue settlements can drive VAT/revenue treatment | 78 | 40 | 70 | 9 | Create gap page and request source-specific evidence. |
| ticket-as-invoice gap | Ticketing docs and tax invoice requirements may conflict | 90 | 42 | 82 | 3 | Maintain as unresolved high-risk gap until reviewed. |
| 7% vs 19% VAT gap | Direct operational tax rate risk | 94 | 48 | 88 | 2 | Create event VAT risk concept with Steuerberater review flag. |
| foreign artist 50a workflow | High-risk withholding workflow | 94 | 52 | 90 | 2 | Source-specific BZSt/foreign artist analysis + workflow concept. |
| source authority hierarchy | Prevents low-trust source overuse | 88 | 65 | 55 | 5 | Create canonical authority hierarchy page and use it in query answers. |

## Mandatory next sequence

1. Confirm local repo contains or lacks Phase 1 grouped files, summary pages, concept pages, and entity pages.
2. If missing, decide whether to save the chat-output artifacts or regenerate from verified Phase 1.
3. Backfill high-risk source-specific analyses.
4. Generate summaries → concepts → entities.
5. Rebuild index and retrieval.
6. Run query simulations.
7. Produce postflight risk register.
