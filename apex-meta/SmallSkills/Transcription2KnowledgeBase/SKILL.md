---
type: Procedure
name: transcript-to-vault
description: Extract source-grounded statements from a transcript via LangExtract, through Hermes' own gateway, and write them as minimal-frontmatter Markdown into an Obsidian vault, then refresh QMD. Use when given a transcript path and a vault target folder.
version: 1.0.0
---

# Transcript to Vault

Invoke chained with its two dependency skills, never alone:
```
/langextract-usage /obsidian /transcript-to-vault <transcript-path> <vault-folder>
```
(add `/qmd` to the chain once that skill is installed — see Pitfalls)

## When to Use

Operator gives a transcript file path and a target vault folder, asks for knowledge-base
notes. Not for: auto-triggering on new files (none exists — manual invocation only), any
output format other than Markdown-in-vault, any schema format other than inferred-per-run.

## Procedure

1. **Resolve credentials — do not ask the operator.**
   ```bash
   source "$HERMES_HOME/.env"   # HERMES_HOME defaults to /opt/data in this container
   # now $API_SERVER_KEY is set
   ```
2. **Verify the gateway before anything else.**
   ```bash
   curl -sf -H "Authorization: Bearer $API_SERVER_KEY" -H "Content-Type: application/json" \
     -d '{"model":"hermes-agent","messages":[{"role":"user","content":"ok"}]}' \
     http://127.0.0.1:8642/v1/chat/completions
   ```
   Non-200 or empty `choices[0].message.content` → **stop**. Report the failure verbatim.
   This is a Hermes-configuration problem, not something to retry or route around.
3. **Verify the vault target** — target folder must have `.obsidian/` somewhere in its
   ancestry. If not: stop, ask the operator. Never create a new vault implicitly.
4. **Draft the extraction schema** — one gateway call (same URL/key as step 2), full
   transcript text as input, asking for a JSON array:
   ```json
   [{"class_name": "...", "description": "...",
     "example_extraction": {"text": "...", "attributes": {}}}]
   ```
   Infer fresh from this document's actual content every run. No fixed preset list.
5. **Run LangExtract** — follow the loaded `/langextract-usage` skill for mechanics
   (`ExampleData`/`Extraction` construction, `lx.extract()` call shape). One deviation from
   its defaults, required every time:
   ```python
   from langextract.factory import ModelConfig
   config = ModelConfig(
       model_id="hermes-agent",   # advisory label only — see Pitfalls
       provider="openai",
       provider_kwargs={"api_key": api_server_key, "base_url": "http://127.0.0.1:8642/v1"},
   )
   result = lx.extract(
       text_or_documents=transcript_text,
       prompt_description=schema["prompt_description"],
       examples=build_examples(schema),   # from step 4's JSON
       config=config,
       use_schema_constraints=False,      # unknown model — do not assume JSON-schema support
   )
   grounded = [e for e in result.extractions if e.char_interval]
   ```
   Discard every extraction not in `grounded`. Do not write ungrounded text anywhere.
6. **Write vault notes** — one file per grounded extraction (or append to an existing
   same-topic note). Use the loaded `/obsidian` skill's own file-placement/linking
   convention; only the content body below is specific to this skill:
   ```markdown
   ---
   title: <short title>
   summary: <one sentence — the core claim>
   tags: [<3-5 lowercase keywords, not the raw class_name>]
   source: <transcript filename>
   ---

   ## <heading matching title>

   > <e.extraction_text, exact>

   <1-2 sentences of plain-prose context>
   ```
   Frontmatter is **exactly** these 4 fields. Never more. See Pitfalls.
7. **Refresh the index** — if `/qmd` is loaded in this invocation, follow its procedure.
   Otherwise:
   ```bash
   ${QMD_CLI:-qmd} update
   ```
   If output signals stale vectors: `${QMD_CLI:-qmd} embed`.
8. **Report**:
   ```
   Source: <path>
   Schema: <N> classes drafted
   Extracted: <N> grounded, <N> discarded (no char_interval)
   Notes: <list of file paths written>
   QMD: refreshed | skipped (<reason>)
   ```

## Pitfalls

- **`model_id` in step 5 does not select the model.** Hermes generates with whatever
  `config.yaml`'s `model.default`/`fallback_providers` has active (currently
  `nvidia/nemotron-3.5-lightning:free` + a 4-model free fallback chain, set 2026-10-01).
  Changing the model means editing `config.yaml`, not this skill or its `model_id` string.
- **Never call OpenRouter directly.** `execute_code`'s sandbox strips external credentials
  by design; Hermes' own gateway (`127.0.0.1:8642/v1`) is the only documented integration
  point for this. Reading `/opt/data/.env` for `API_SERVER_KEY` is safe because this skill
  runs inside Hermes' own container — it is not exporting that credential anywhere external.
- **Never exceed 4 frontmatter fields** (`title`/`summary`/`tags`/`source`). This repo has an
  operator-verified failure case for exactly this: rigid per-category schema fields degrade
  QMD's hybrid retrieval (`apex-meta/AI-Snippets/AIFailure/AI-Failure-RAG-Metadata-Overengineering.md`).
  If a future requirement needs more structure, re-read that file first.
- **Never write an extraction with `char_interval is None`.**
- **`qmd` is not yet installed on this instance** — `hermes skills install official/research/qmd`
  was attempted and the security scanner returned a **DANGEROUS** verdict (sudo/apt
  privilege escalation, a background daemon install, and a step that edits
  `~/.hermes/config.yaml`). It was not installed pending an explicit operator decision. Until
  installed, step 7 falls back to a bare `qmd` CLI call — confirm that binary actually exists
  on this host before relying on it; if it doesn't, report that and stop at step 7, do not
  skip indexing silently.
- **No automatic trigger exists.** Do not propose adding one as part of running this skill.
- **No adaptive/cross-document schema memory in this version.** Step 4 always starts cold.
  See `RESEARCH-HANDOVER-adaptive-schema-selection.md` for the open follow-up.

## Verification

- Step 2's `curl` returned a real completion, not an error.
- At least one Markdown file exists under `<vault-folder>` with exactly 4 frontmatter keys.
- Every written note's blockquote is a verbatim substring of the source transcript.
- `${QMD_CLI:-qmd} ls <collection>` (or a targeted `get` on one new page) shows it indexed —
  or step 8's report explicitly states indexing was skipped and why.
