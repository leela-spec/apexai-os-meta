# MISTAKES

## Purpose

Reusable Knowledge Bank failure patterns and countermeasures. This file is compact; detailed evidence remains in `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** scaffold guidance derived from source ledgers and anti-drift appendix
- **Promotion caution:** patterns here are operational safeguards, not shared governance mutation.

## Failure patterns

### MK-KB-001 — Candidate-to-canon leak

- **Pattern:** A strong candidate is copied into scaffold prose without status, evidence pointer, or validator boundary.
- **Trigger conditions:** high-ranked ledger item; urgency to make KB “complete”; missing candidate ledger row.
- **Consequence:** candidate material becomes de facto accepted truth.
- **Countermeasure:** store candidate details in `APPENDIX_KB_CANDIDATE_LEDGER.md`; summarize only compactly; route promotion through the governed path.
- **Evidence refs:** `KB-KB-CAND-008`; `KB-KB-DRIFT-001`; `KB-KB-DRIFT-004`.

### MK-KB-002 — Scaffold bloat / appendix bypass

- **Pattern:** `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, or `LEARNING_QUEUE.md` starts carrying raw source bodies, long rationale, or archive excerpts.
- **Trigger conditions:** broad source ingestion; desire to preserve every nuance; missing appendix pointer.
- **Consequence:** activation files become low-retrieval and context-heavy.
- **Countermeasure:** move detail to appendices; keep scaffold entries as rule, condition, evidence pointer, and next action.
- **Evidence refs:** `KB-KB-INFO-011`; `KB-KB-DRIFT-002`; `KB-KB-DRIFT-003`.

### MK-KB-003 — Density gate bypass

- **Pattern:** a scratchpad, source bundle, or generated artifact is treated as usable KB structure before density and self-containment are checked.
- **Trigger conditions:** staged generation fatigue; scaffold drafted before ranking ledger; missing validator pass.
- **Consequence:** prose blobs and ambiguous units enter reusable KB surfaces.
- **Countermeasure:** run density gate before scaffold drafting; ensure every scaffold item is compact and independently understandable.
- **Evidence refs:** `KB-META-OPS-023`; `KB-KB-DRIFT-001`.

### MK-KB-004 — Local grammar invention

- **Pattern:** the agent invents new bullet labels, relation types, status values, or file classes instead of using existing ledgers/canons.
- **Trigger conditions:** incomplete context; format discomfort; attempt to make the current artifact “cleaner.”
- **Consequence:** cross-agent retrieval and validation degrade.
- **Countermeasure:** reuse existing typed signal words and status semantics; unresolved grammar changes go to `LEARNING_QUEUE.md`.
- **Evidence refs:** `KB-META-OPS-009`; `KB-META-OPS-034`; `KB-KB-DRIFT-002`.

### MK-KB-005 — Blind rewrite of critical KB files

- **Pattern:** a critical KB scaffold or appendix is regenerated wholesale instead of patched or updated by bounded section.
- **Trigger conditions:** long document; stale source; pressure to harmonize everything at once.
- **Consequence:** omissions, semantic drift, and loss of auditability.
- **Countermeasure:** patch one named file or section at a time; define invariants before editing; fetch back after each write.
- **Evidence refs:** `KB-PROMPTS-WORKFLOWS-032`; `KB-KB-DRIFT-003`.

### MK-KB-006 — Waterfall overfit

- **Pattern:** the agent freezes a complete skeleton too early and forces emerging knowledge into premature structure.
- **Trigger conditions:** uncertain source body; demand for formal output before evidence stabilizes.
- **Consequence:** false completeness, missing hard sections, or structural debt hidden under neat headings.
- **Countermeasure:** use hypothesis-first structure for uncertain material, then density/validation before final scaffold summary.
- **Evidence refs:** `KB-META-OPS-025`; `KB-KB-DRIFT-006`.

### MK-KB-007 — Evidence overgeneralization

- **Pattern:** a failure/postmortem source is treated as universal doctrine instead of bounded evidence.
- **Trigger conditions:** vivid failure case; strong score; missing evidence-only marker.
- **Consequence:** local incident logic hardens into broad KB law.
- **Countermeasure:** mark postmortem-derived items as evidence_only unless separately validated by the owner/validator pair.
- **Evidence refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#evidence-only-register`.

### MK-KB-008 — Connector replacement disguised as patch execution

- **Pattern:** A GitHub connector `update_file` or `create_file` replacement is described as if it were native unified-diff patch execution.
- **Trigger conditions:** no local checkout; urgency to finish; patch pack treated as equivalent to applied git diff.
- **Consequence:** validation claims become false because `git apply --check`, `git apply`, `git diff --check`, and exact changed-file verification did not run.
- **Countermeasure:** when native `git apply` is unavailable, stop after producing exact unified diffs and a zero-freedom Codex prompt; do not execute connector whole-file replacement.
- **Evidence refs:** `PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED.md`; `KB_SYSTEM_RELIABILITY_AUDIT_V1`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#anti-drift-evidence-ledger`.

### MK-KB-009 — Legacy promptflow basis leak

- **Pattern:** an older Knowledge Bank promptflow is used as the basis for current KB updates after a corrected promptflow exists.
- **Trigger conditions:** old scaffold source-basis references; source manifest execution lock still names old promptflow; no quarantine step.
- **Consequence:** corrected execution rules are bypassed, including direct-main execution, no branch creation, and Codex-only git-apply requirements.
- **Countermeasure:** record legacy promptflows as historical_context_only; use only the corrected promptflow as current authority; stop if unresolved conflict appears.
- **Evidence refs:** `APPENDIX_KB_SOURCE_MANIFEST.md`; `ESSENCE.md`; `PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED.md`.

### MK-KB-010 — Cross-agent raw URL fetch assumed reliable

- **Pattern:** An agent (ChatGPT, Perplexity, etc.) is instructed to "fetch" a `raw.githubusercontent.com` URL via its own web-browsing/search tool and treat the fetched content as authoritative context, in place of pasting the file contents inline.
- **Trigger conditions:** bundle-size pressure from large source documents; assumption that public HTTPS reachability (confirmed independently via `curl`) implies the agent's own browsing tool will successfully fetch and read the same URL; no native repository connector configured for that agent.
- **Consequence:** the agent's response degrades to a list of search-result/citation chips (e.g., repeated "GitHub", "Inspect", "arXiv" reference markers) with no synthesized body text, while still returning HTTP 200 for the URL at the network level — a silent quality failure, not a thrown error. Confirmed empirically in APEX OS local-model research Round 2, ChatGPT Research Prompt E retry (chatgpt.com thread `6a783f26`, 2026-08-09): the response opened with a packet title but the entire body was citation markers, no prose.
- **Countermeasure:** do not rely on an agent's own browsing/search tool to fetch raw GitHub file URLs as a substitute for inline content. Prefer (a) a native repository connector/integration explicitly configured for that agent (e.g., a ChatGPT Connector for GitHub, added and authorized by the human operator) where the agent indexes/reads the repo through a first-class integration rather than ad-hoc browsing, or (b) condensed inline content (head/tail excerpts with an explicit omission note) sized within the agent's already-verified reliable prompt-length range, or (c) full inline paste when the source is small enough. Always verify success by inspecting actual response body length and content for real prose, not merely the absence of a thrown error.
- **Evidence refs:** this session's `get_page_text` capture of chatgpt.com thread `6a783f26` (garbled citation-only output, no body text); direct operator report of prior real-world failures of this same pattern.

### MK-KB-011 — Long chat-UI response reads as truncated immediately after generation stops

- **Pattern:** A browser-automation agent reads a long assistant response's DOM content (via `innerText` or a page-text extraction tool) in the same turn the generation-in-progress indicator (e.g. a stop button) disappears, and the extracted text ends abruptly mid-structure (mid-table, mid-list, or mid-YAML-block) with no closing marker, leading the operator to conclude the model's generation itself was cut off.
- **Trigger conditions:** very long responses (tens of thousands of characters); reading the DOM/page-text immediately after the generation-in-progress indicator clears, with no page reload in between; chat UIs that stream or virtualize long messages client-side, where the last chunk of a long message can lag behind the "generation complete" signal.
- **Consequence:** the agent sends an unnecessary "continue where you left off" follow-up message, consuming an extra turn and creating a redundant/duplicate continuation response that must be reconciled with (or discarded in favor of) the original. Confirmed empirically twice in APEX OS local-model research Round 2 on ChatGPT (2026-08-09): once on Research Prompt E's connector-based response, where `get_page_text`'s own internal ~50,000-character cap was the proximate cause (see the sibling append note in `LOCAL-MODEL-RESEARCH-E-BENCHMARK-HARNESS-2026-08-09-CHATGPT-ATTEMPT-FAILED.md`); and once on Research Prompt F's connector-based response, where the DOM read itself (via direct `element.innerText`, not `get_page_text`) returned an incomplete 64,449-character string missing the final required YAML keys, and only navigating away and back to the same chat URL (forcing a full reload from the server) revealed the true, complete 67,132-character response.
- **Countermeasure:** before concluding a long response is genuinely incomplete and sending a "continue" follow-up, (a) rule out a page-text extraction tool's own internal truncation cap by checking its output for an explicit truncation note or by cross-checking the reported length against a direct DOM read, and (b) rule out client-side rendering/virtualization lag by reloading the page (navigate to the same URL again) and re-extracting before treating the response as incomplete. Only send a continuation request after both checks confirm the response is truly missing required closing content (e.g. a named closing YAML key from the prompt's own deliverable list is absent from the reloaded, full-length extraction).
- **Evidence refs:** this session's two-chunk `get_page_text` extraction of chatgpt.com thread `6a7841f3` before and after a page reload (64,449 chars missing `reversal_triggers`/`operator_questions_remaining`/final `overall_confidence_0_to_100` pre-reload; 67,132 chars complete post-reload); the sibling Research Prompt E extraction note in `LOCAL-MODEL-RESEARCH-E-BENCHMARK-HARNESS-2026-08-09-CHATGPT-ATTEMPT-FAILED.md`.

## Closure rule

A mistake pattern is closed only when the triggering scaffold, appendix, or learning queue entry has been corrected and the correction remains traceable to the relevant candidate/evidence row.
