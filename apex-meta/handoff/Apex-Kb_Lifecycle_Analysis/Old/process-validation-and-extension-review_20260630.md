# Apex KB Process Validation and Extension Review

```yaml
validation_report:
  title: "Apex KB Process Validation and Extension Review"
  target_kb: "lika-verein-taxes-accounting"
  mode: "audit_and_extension_planning"
  generated_at: "2026-06-30"
  output_mode: "chat_artifact_not_repo_write"
  repo_ref_verified: "e4ba50499ce9503e215f7d80e9d08518d0dcc492"
```

## 1. source_availability_ledger

| Source/artifact | Availability | Evidence | Validation consequence |
|---|---:|---|---|
| `.claude/skills/apex-kb/` skill contract | Available through installed skill resource | Skill owns scaffold, source intake, Phase 0, Phase 1, Phase 2, deterministic validation, local retrieval, query packets, and lint/audit maintenance. | Lifecycle and ownership split validated. |
| KB root `apex-meta/kb/lika-verein-taxes-accounting/` | Exists in repo | README states it is a source-preserving KB and lists canonical paths. | KB root is valid. |
| `kb-schema.md` | Exists in repo | Schema locks `ingest_phase_2_requires_phrase: "approve ingest"` and `same_prompt_approval_allowed: false`. | Operator gate is valid and strict. |
| `source-manifest.json` | Exists in repo | Manifest contains `kb_slug`, schema version, sources array, source hashes, source paths, storage mode, status, and ingest status. | Custody model exists. |
| Deterministic lifecycle report | Exists in repo | Report records clean pre-run state, skill/script loading, 103 source candidates, 60 manifest additions, Phase 0 artifacts, pass lint/audit/status, and stop before semantic ingest. | Phase 0 and postflight-preflight are strongly verified. |
| Phase 0 artifacts | Exists according to lifecycle report | `corpus-profile.md`, frontmatter/heading/link maps, keyword hits, navigation report, source-priority candidates, topic-file map. | Phase 0 value is verified by script report. |
| Phase 1 grouped artifacts | Partially visible in project handover, not fully verified in repo search | Repo search did not surface the six grouped filenames from the handover. | Treat as project-resource/chat-output unless local repo confirms. |
| Phase 2 summary layer | Not present in verified repo index | Repo `wiki/index.md` says compiled page count is `0` and no LLM summary approved. | Treat summary pages as chat-output or pending application, not repo truth. |
| Phase 2 concept layer | Not found in verified repo search | Search for `invoice-core-fields` returned no repo result. | Treat 23 concept pages as generated bundle / candidate artifacts, not installed KB pages. |
| Retrieval index | Exists but low-content | Lifecycle says retrieval health/stale passed; index not forced because wiki contained only `wiki/index.md`. | Retrieval mechanics exist; retrieval value not yet proven. |

## 2. process_reconstruction

The validated Apex KB lifecycle is:

```text
Phase 0 — Deterministic Corpus Intelligence
  Build compact navigation artifacts without LLM semantic claims.

Phase 1 — LLM Semantic Ingest Analysis
  LLM reads selected/high-signal source sets and writes ingest-analysis files.

Operator Gate
  Phase 2 requires exact separate phrase: approve ingest.

Phase 2 — Compiled Wiki Generation
  LLM writes summaries, concepts, entities, semantic index sections, and audit items.

Postflight — Deterministic Validation
  Rebuild index/retrieval, lint, audit, status, and query-packet tests.
```

Current verified repo state is between Phase 0 and Phase 1/2 application: deterministic preparation completed, but installed wiki pages are not yet compiled in the verified commit.

## 3. artifact_inventory

| Artifact/path | Exists in repo? | Created by | Source grounded? | Reusable? | Main defect | Score | Action |
|---|---:|---|---:|---:|---|---:|---|
| `ingest-analysis/*.analysis.md` | Partial/uncertain for target grouped set | LLM | Medium | Yes | Grouped artifacts in handover not found by repo search | 68 | Verify local tree; backfill source-specific analyses. |
| `wiki/index.md` | Yes | Python + placeholder LLM section | Low semantic | Yes | Compiled page count `0`; no approved LLM summary | 72 | Rebuild after Phase 2 pages are installed. |
| `wiki/summaries/*.md` | Not verified | LLM candidate | Medium | Yes | Candidate only unless saved to repo | 55 | Save approved summaries or regenerate from Phase 1. |
| `wiki/concepts/*.md` | Not verified | LLM candidate | Medium-low | High | 23 concepts likely generated from grouped Phase 1; direct source pointers need review | 60 | Backfill source pointers before trust. |
| `wiki/entities/*.md` | Not verified | Missing/weak | Low | High | Entity layer absent | 35 | Generate authorities/tools/provider/entity nodes. |
| `manifests/source-manifest.json` | Yes | Python/source intake | High | Yes | Ingest status likely still `source_intake_only` for many sources | 86 | Update status after approved Phase 1/2. |
| `manifests/phase0/*` | Yes per lifecycle report | Python | High | Yes | No `source-inventory.*` artifact emitted | 88 | Add inventory artifact or reconcile report expectation. |
| `derived/search/*` | Yes | Retrieval script | Medium | Yes | Low content due no compiled pages | 70 | Rebuild after summaries/concepts/entities exist. |
| `log/lifecycle-run-report_*` | Yes | Deterministic run | High | Yes | Documents argparse quirks and missing inventory | 92 | Keep as provenance. |
| `outputs/queries/*` | At least one older query output exists | LLM/query | Medium | Partial | Not representative of final KB query-path tests | 50 | Create 8 query packets after Phase 2. |
| `audit/*` | Exists; no open items in run | Python/audit | Medium | Yes | Semantic audit items absent because Phase 2 not installed | 64 | Create semantic risk register after Phase 2. |

## 4. impact_evidence_risk_matrix

| Layer | Current status | Impact | Evidence | Risk | Simplicity | Token efficiency | Keep / change / remove | Required fix |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Phase 0 corpus intelligence | Verified run | 94 | 90 | 18 | 82 | 88 | Keep | Add missing source-inventory artifact and compact navigation report as first-read surface. |
| Source manifest / custody | Verified | 91 | 88 | 24 | 78 | 82 | Keep | Update ingest statuses and ensure every high-risk page carries source hash/pointer. |
| Phase 1 grouped ingest | Candidate / partially unverified | 88 | 62 | 48 | 76 | 78 | Change | Require source-specific analysis for legal/tax/high-risk sources. |
| Operator gate | Verified schema/skill | 92 | 92 | 12 | 90 | 70 | Keep | Preserve separate-turn `approve ingest` rule. |
| Phase 2 summaries | Candidate, not installed in verified repo | 86 | 48 | 42 | 74 | 80 | Change | Install or regenerate from verified Phase 1; rebuild index. |
| Phase 2 concepts | Candidate, not installed in verified repo | 92 | 45 | 55 | 64 | 88 | Change | Backfill direct source pointers and classify high-risk concepts. |
| Entity pages | Missing/weak | 80 | 30 | 58 | 65 | 78 | Add | Generate BMJ, BMF, AWV, LfSt Bayern, DRV/KSK, BZSt, pretix, Lika Verein. |
| Wiki index | Exists, semantically empty | 82 | 86 | 36 | 80 | 60 | Change | Add semantic summary section after Phase 2; rebuild machine section. |
| Retrieval/query packet | Mechanics exist; tests missing | 84 | 55 | 50 | 70 | 86 | Add | Run 8 representative query simulations and save outputs. |
| Lint/audit postflight | Verified pre/post Phase 0 | 90 | 90 | 20 | 82 | 74 | Keep | Make mandatory after every Phase 2 commit. |

## 5. token_efficiency_simulation

```yaml
token_simulation_inputs:
  raw_source_count: 103
  manifest_entries_before_delta: 35
  manifest_delta_records_added: 60
  phase1_file_count: "candidate grouped set: 6; repo verification incomplete"
  phase1_total_bytes: "not verified from repo in this audit"
  summary_page_count: "candidate: 6; repo verified: 0 compiled pages"
  concept_page_count: "candidate: 23; repo verified: 0 concept pages found"
  entity_page_count: "repo verified: 0"
  wiki_total_bytes: "repo verified index only: small; candidate bundle not installed"
  token_estimate_rule: "bytes / 4"
```

| Query | Old path without KB | New path with KB | Pages needed | Estimated token reduction | Confidence | Missing page/gap |
|---|---|---|---:|---:|---|---|
| What invoice fields does Lika need? | Read UStG, UStDV, BMF FAQ, Phase 1 group | Index + invoice concept + core summary | 2-3 | 80-90% if concept exists | Medium | `invoice-core-fields` not installed. |
| When can a Kleinbetragsrechnung be used? | Read UStDV/BMJ/IHK PDF | Index + `kleinbetragsrechnung` | 1-2 | 85-92% | Medium | Table-heavy PDF verification. |
| What changes for E-Rechnung? | Read BMF FAQ, UStG, association guidance | Index + `e-rechnung-verein` + core summary | 2-3 | 75-88% | Medium | Need direct source pointers. |
| Can a ticket function as an invoice? | Read pretix docs, VAT/event sources, tax sources | Index + `ticket-as-invoice-gap` | 2-4 | 70-85% | Low-medium | Explicit gap page needed. |
| Which VAT rate applies to events? | Read LfSt PDF, UStG, event notes | Index + event VAT concept + source authority | 2-4 | 70-88% | Medium | 7% vs 19% gap unresolved. |
| What must be done for artist payments / KSK? | Read DRV/KSK PDFs and contractor notes | Index + KSK concept + artist obligations summary | 2-3 | 80-90% | Medium | Needs source-specific KSK analysis. |
| What is the foreign artist §50a risk? | Read BZSt and foreign artist docs | Index + `foreign-artist-50a` + entity BZSt | 2-3 | 80-90% | Medium | Workflow page and authority entity missing. |
| Which sources are noisy or low-trust? | Inspect many source/meta files and web-clutter audit | Index + source quality summary + web clutter concept | 2-3 | 85-95% | High for detection, lower for cleanup | Quarantine/noisy source report needs final save. |

## 6. retrieval_path_simulation

The ideal retrieval path is validated as a design target but not yet proven in the installed repo because the verified `wiki/index.md` has `Compiled page count: 0`.

Recommended post-Phase-2 retrieval test:

1. Read `wiki/index.md`.
2. For each of the eight representative queries, select one summary page plus one to three concept/entity pages.
3. Compare answer quality against raw-source-only answer.
4. Save query packets under `outputs/queries/`.
5. Rebuild `derived/search/` and confirm retrieval index freshness.

## 7. source_grounding_audit

Current verdict: **architecture is source-grounding-aware; installed semantic pages are not yet verifiable**.

Required checks per Phase 2 page:

```yaml
required_fields:
  - source_refs
  - source_path
  - source_hash_or_no_hash_reason
  - source_pointer
  - confidence
  - claim_label
  - open_questions
  - review_flags_if_needed
fail_conditions:
  - truncated_or_malformed_source_hash
  - legal_or_tax_claim_without_direct_source_pointer
  - grouped_phase1_only_citation_when_direct_source_exists
  - high_risk_issue_written_as_settled
  - confidence_and_claim_label_conflated
```

Tax/accounting/legal-adjacent KB pages must preserve uncertainty and should not be treated as professional tax/legal advice.

## 8. concept_page_quality_audit

| Concept slug | Exists in repo? | Source grounding | Retrieval value | Duplication risk | Operational clarity | Legal/tax risk | Action |
|---|---:|---:|---:|---:|---:|---:|---|
| invoice-core-fields | No | 55 | 95 | 20 | 88 | 70 | backfill_sources |
| kleinbetragsrechnung | No | 58 | 92 | 25 | 86 | 68 | backfill_sources |
| e-rechnung-verein | No | 52 | 90 | 28 | 82 | 75 | backfill_sources |
| belegablage-verfahrensdokumentation | No | 50 | 84 | 55 | 78 | 62 | merge_review |
| belegfunktion | No | 48 | 72 | 60 | 68 | 58 | merge_or_subpage |
| accounting-source-custody | No | 62 | 80 | 55 | 75 | 45 | merge_review |
| reimbursement-evidence | No | 45 | 78 | 35 | 72 | 55 | backfill_sources |
| event-business-area-assignment | No | 45 | 82 | 30 | 70 | 72 | backfill_sources |
| event-vat-rate-risk | No | 50 | 94 | 25 | 78 | 86 | keep_high_risk_gap |
| ticketing-tax-configuration | No | 46 | 86 | 35 | 76 | 70 | backfill_sources |
| ticket-as-invoice-gap | No | 42 | 92 | 20 | 80 | 82 | keep_gap_page |
| kuenstlersozialabgabe-event | No | 55 | 92 | 20 | 84 | 78 | backfill_sources |
| foreign-artist-50a | No | 52 | 94 | 15 | 82 | 90 | keep_high_risk_gap |
| artist-contract-source-of-truth | No | 45 | 80 | 55 | 76 | 70 | merge_review |
| foreign-artist-vat-recipient-liability | No | 42 | 82 | 55 | 72 | 86 | merge_review |
| source-authority-hierarchy | No | 65 | 90 | 20 | 88 | 55 | keep |
| transfer-safety | No | 40 | 72 | 35 | 70 | 45 | backfill_or_gap |
| unresolved-tax-risk-register | No | 60 | 95 | 15 | 88 | 92 | keep |
| venue-settlement-gap | No | 35 | 82 | 20 | 70 | 78 | downgrade_to_gap_page |
| web-clutter-filter | No | 70 | 78 | 70 | 80 | 30 | merge_reduce |
| duplicate-source-custody | No | 70 | 76 | 70 | 78 | 30 | merge_reduce |
| table-heavy-pdf-risk | No | 82 | 88 | 20 | 84 | 60 | keep |
| phase1-placeholder-replacement | No | 60 | 65 | 75 | 65 | 35 | merge_reduce |

## 9. postflight_validation_status

Verified postflight status at deterministic layer:

- Pre/post lint passed.
- Pre/post audit passed with zero items.
- Index/status freshness passed.
- Retrieval health/stale passed.
- Phase 0 applied successfully with eight artifacts.

Not yet verified:

- Postflight after installed Phase 2 pages.
- Retrieval index after summary/concept/entity population.
- Query-packet reproducibility after compiled pages exist.

## 10. simplification_opportunities

| Opportunity | Keep? | Simplified rule |
|---|---:|---|
| Long natural-language prompts duplicating script commands | Remove | Operator prompt should specify mission, KB slug, boundaries, and stop condition only. |
| Manual source inventory instructions | Change | Let `apex_kb.py phase0/source-intake` own deterministic inventory. |
| Grouped Phase 1 everywhere | Change | Group low-risk homogeneous sources only; high-risk legal/tax sources get source-specific analysis. |
| Concept/entity generation in one giant pass | Change | Generate summaries first, concepts second, entities third, query packets last. |
| Repeated package scope explanations | Remove | Installed `apex-kb` skill is canonical. |

## 11. reliability_improvements

| Improvement | Reason | Priority |
|---|---|---:|
| Source-specific Phase 1 backfill for high-risk sources | Prevents overgeneralization from grouped summaries | 96 |
| Concept page source-pointer audit | Prevents legal/tax false confidence | 94 |
| Entity layer generation | Stabilizes authority/provider/tool retrieval | 86 |
| Query packet tests | Proves token-efficiency claims | 88 |
| Retrieval rebuild after Phase 2 | Prevents stale compiled context | 90 |
| Table-heavy PDF verification | Prevents conversion-derived tax/accounting errors | 84 |
| Noisy source quarantine | Prevents web clutter from contaminating synthesis | 80 |

## 12. next_kb_runbook_v2

See separate artifact: `apex-kb-next-runbook-v2.md`.

## 13. ranked_action_plan

See separate artifact: `next-actions-ranked_20260630.md`.

## 14. top_level_conclusion

The likely conclusion is **mostly validated with an important caveat**:

> The Apex KB process is structurally valuable and likely token-saving, but the verified repo state currently proves the deterministic lifecycle more strongly than the installed semantic wiki layer. The main remaining weakness is validation depth and artifact installation: source-specific Phase 1 backfill, concept/entity grounding, query simulation, and post-Phase-2 deterministic checks must be mandatory before this KB is used as a high-confidence operational reference.

