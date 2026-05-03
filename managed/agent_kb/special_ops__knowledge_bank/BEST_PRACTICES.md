# BEST_PRACTICES

## Purpose

Compact operating doctrine for Special Ops Knowledge Bank. Detailed source material stays in appendices.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** scaffold guidance derived from source ledgers and candidate appendices
- **Promotion caution:** entries here guide KB-base operation; they do not approve shared governance or accepted-truth changes.

## Appendix pointers

- Source manifest: `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`
- Information ranking ledger: `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`
- Candidate ledger: `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`
- Anti-drift evidence: `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`

## Practices

### BP-KB-001 — Build appendix-first

- **Rule:** Create or update source manifest, ranking ledger, candidate ledger, and anti-drift appendix before scaffold drafting.
- **Why:** Scaffold files must remain activation and navigation surfaces, not deep storage.
- **Evidence:** `KB-KB-CAND-001`; `KB-KB-CAND-014`; `APPENDIX_KB_SOURCE_MANIFEST.md`.
- **Use when:** building or refreshing an agent KB base.

### BP-KB-002 — Preserve candidate status until promotion

- **Rule:** Treat source-derived ideas as candidate, strong_candidate, or evidence_only until a governed promotion path accepts them.
- **Why:** High-ranking evidence is not equivalent to accepted truth.
- **Evidence:** `KB-KB-CAND-002`; `KB-KB-CAND-008`; `APPENDIX_KB_CANDIDATE_LEDGER.md`.
- **Use when:** moving material from ledgers into `LEARNING_QUEUE.md`, scaffold summaries, or future promotion packets.

### BP-KB-003 — Use thin scaffold, deep appendices

- **Rule:** Store detailed source bodies in appendices and expose only compact operating guidance in `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, and `LEARNING_QUEUE.md`.
- **Why:** Retrieval clarity and anti-sprawl matter more than completeness theater.
- **Evidence:** `KB-KB-INFO-011`; `KB-KB-DRIFT-002`; `KB-KB-DRIFT-003`.
- **Use when:** a scaffold section starts accumulating source detail, long rationale, or raw archive material.

### BP-KB-004 — Capture out-of-mode improvements; do not apply them silently

- **Rule:** Better ideas discovered during a bounded KB update must be captured in `LEARNING_QUEUE.md` or an improvement section, not applied outside the current run mode.
- **Why:** Silent improvement application is scope drift and can mutate unapproved surfaces.
- **Evidence:** `AIHowTo/Codex/Improvement_Capture_Rule.md`; `KB-KB-CAND-013`; `KB-KB-DRIFT-004`.
- **Use when:** a useful idea appears but does not belong to the authorized target files or operation mode.

### BP-KB-005 — Keep authority stack narrow

- **Rule:** Use promptflow, source index, ranked ledgers, role map, current target files, and fetch-back verification as the execution authority stack.
- **Why:** Broad research context is explanatory unless the promptflow explicitly authorizes it.
- **Evidence:** `AIHowTo/Codex/CODEX_RESILIENT_MIGRATION_PROCESS.md`; `KB-KB-INFO-005`.
- **Use when:** deciding whether to read more sources or touch surfaces outside the KB root.

### BP-KB-006 — Route Apex project learning as candidate packets

- **Rule:** In ApexAI_OS, project-local KB learning routes upward as candidate material: project learning queue, project validation or hygiene check, LearningCandidate packet, meta review, promotion decision, and only then release-pack inclusion.
- **Why:** The meta repo learns from projects without allowing raw project data, uncontrolled sync, or candidate-to-runtime truth leakage.
- **Evidence:** `docs/LEARNING_SYSTEM.md`; `managed/knowledge/AGENT_KB_LANES.md`; `ApexAI_OS_Federated_Orchestration_Handover.md`.
- **Use when:** project KB findings, recurring mistakes, source-placement improvements, or template improvements may deserve meta-level reuse.

### BP-KB-007 — Keep meta-to-project KB changes release-pack shaped

- **Rule:** A KB improvement that should travel from ApexAI_OS meta to projects must be packaged as a reviewed meta release delta, not copied as raw history or an unreviewed full KB dump.
- **Why:** Projects receive the released operating kernel and selected KB deltas, not raw meta learning history or unrelated project context.
- **Evidence:** `ApexAI_OS_Federated_Orchestration_Handover.md`; `managed/knowledge/AGENT_KB_LANES.md`.
- **Use when:** preparing reusable KB improvements for downstream project repos.

### BP-KB-008 — Protect project isolation in KB evidence routing

- **Rule:** Store only sanitized, generalized, source-status-clear KB learnings in the meta Knowledge Bank lane; do not ingest raw coaching, investment, community, app, personal, secret, or project-local data into this KB.
- **Why:** ApexAI_OS uses a holding-layer/subsidiary model: the meta repo generalizes learning, while project repos keep local sensitive context.
- **Evidence:** `ApexAI_OS_Federated_Orchestration_Handover.md`; `docs/LEARNING_SYSTEM.md`.
- **Use when:** deciding whether a project-originated note belongs in this KB, a project-local KB, a promotion packet, or no shared surface.

## Quality gates

- **Gate:** Every scaffold summary has an appendix pointer.
- **Gate:** Evidence-only material stays out of accepted-practice language.
- **Gate:** No raw failure archive is copied into scaffold files.
- **Gate:** No candidate is self-promoted by the writer that captured it.
- **Gate:** Any future accepted-truth change routes through the governed promotion path.
- **Gate:** Apex project-originated material is sanitized and generalized before meta-level KB use.
- **Gate:** Meta-to-project KB changes are release-pack candidates, not uncontrolled sync.

## Review

- **Review cadence:** revisit after validator review or when the source ledgers change materially.
- **Review partner:** `special_ops__informatics_design`.
