---
name: transcript-to-knowledge
description: Build a standalone, resumable Macro/Meso/Micro knowledge set from Whisper, faster-whisper, WhisperX, SRT, VTT, JSON, or plain-text transcripts. Use when converting podcasts, meetings, lectures, interviews, or videos into source-grounded Markdown/wiki artifacts with exact quote anchors, atomic claims, selective fact verification, deterministic validation, and no dependency on Apex KB or an external LLM API.
---

# Transcript to Knowledge

Treat the transcript as immutable evidence. Use deterministic code for custody, segmentation, validation, routing, resumability, deduplication warnings, and compilation; use the active reasoning model only for semantic interpretation.

## Control loop

1. **Initialize a standalone run.**

   ```powershell
   python scripts/ttk.py doctor
   python scripts/ttk.py init <transcript> --output <run-dir>
   ```

   On Windows, `scripts/ttk.ps1` is a thin PowerShell launcher. The CLI makes no network or LLM calls.

2. **Ask the CLI what is next.**

   ```powershell
   python scripts/ttk.py next <run-dir> --json-output
   ```

   Follow the returned packet/result paths. Do not invent an alternative lifecycle from chat state.

3. **Complete Map packets one at a time.**
   - Read `references/semantic-contracts.md` → **Map result**.
   - Read the returned `work/packets/map/window-XXXX.json`.
   - Write the matching `work/results/map/window-XXXX.json`.
   - Extract evidence only from `role: core` segments. `context_only` exists only to understand the boundary.
   - Every candidate claim requires a verbatim quote from a cited core segment.
   - Empty arrays are valid; never force a quota.

4. **Validate before reduction.**

   ```powershell
   python scripts/ttk.py validate <run-dir>
   python scripts/ttk.py make-reduce <run-dir>
   ```

   The CLI rejects stale packet hashes, invalid source references, non-verbatim quotes, missing core coverage, malformed result contracts, and decisive verification verdicts without evidence.

5. **Complete one compact Reduce packet.**
   - Read `references/semantic-contracts.md` → **Reduce result**.
   - Use `work/packets/reduce.json`, which contains the validated evidence ledger rather than the raw full transcript.
   - Produce final Macro synthesis, semantic Meso modules, and refined Micro claims.
   - Keep transcript support (`SUPPORTED|PARTIAL|AMBIGUOUS|UNSUPPORTED`) separate from external truth.

6. **Route only check-worthy factual claims for external verification.**

   ```powershell
   python scripts/ttk.py make-verify <run-dir> --min-checkworthiness medium
   ```

   - Read `references/semantic-contracts.md` → **External verification**.
   - Browse only queue items when live research is useful and available.
   - Prefer primary/official sources.
   - Leave insufficiently supported claims `UNVERIFIED`.
   - Do not externally verify opinions, recommendations, predictions, decisions, anecdotes, or other non-factual speech by default.

7. **Compile and validate the wiki.**

   ```powershell
   python scripts/ttk.py compile <run-dir>
   python scripts/ttk.py validate <run-dir> --complete
   ```

   The compiler creates Macro, Meso, claim, concept, entity, and index Markdown pages with resolvable Obsidian-style links.

## Non-negotiable boundaries

- **Standalone:** Do not require Apex KB, a graph database, vector database, workflow engine, or hosted API for correctness.
- **Processing windows are not chapters:** deterministic lexical/pause segmentation creates bounded transport windows; the Reduce pass decides final Meso structure.
- **Context halo is not evidence:** semantic Map results may cite only core segment IDs.
- **One raw semantic pass:** extract themes, mechanisms, claims, quotes, entities, and uncertainty together in each Map pass to avoid rereading the raw transcript for separate jobs.
- **No silent semantic dedupe:** exact duplicate claim text may merge mechanically; near-duplicates are warnings for the Reduce pass.
- **No fake provenance:** never fabricate timestamps, speaker identity, quotes, URLs, publication dates, evidence, or verification verdicts.
- **No hidden state:** resumability is derived from files, packet hashes, and validators, not conversation memory.

## Deterministic vs semantic work

**Deterministic CLI:** parsing, SHA-256 custody, diagnostics, lexical-cohesion/pause window candidates, exact core coverage, packet hashes, structural validation, quote substring checks, duplicate warnings, verification routing, stable claim IDs, wiki compilation, status/resume.

**Semantic worker:** theme interpretation, real chapter/module boundaries, argument/mechanism understanding, claim formulation/classification, source-support judgment, Macro synthesis, and external evidence judgment.

For rationale and rejected alternatives, read `references/architecture.md`. For exact JSON shapes, read `references/semantic-contracts.md`. For Windows operator commands and recovery, read `references/operator-runbook.md`. For regression scenarios, read `references/evals.md`.

## Tests

Run from `scripts/`:

```powershell
python test_ttk.py -v
```
