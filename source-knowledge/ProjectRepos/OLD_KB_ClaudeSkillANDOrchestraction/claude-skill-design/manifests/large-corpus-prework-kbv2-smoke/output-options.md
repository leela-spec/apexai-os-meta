# Large Corpus Prework Output Options

This script is meant to create deterministic footing for later LLM work. It does
not decide truth, write wiki pages, create embeddings, or copy source material.

## Option 1: Inventory Only

Use when the corpus is unknown, huge, or risky.

- Reads file metadata only.
- Produces inventory, size/noise profile, and candidate path guesses.
- Best first run for unfiltered repos, databases, exports, and KB dumps.

## Option 2: Candidate Routing

Use when you want the LLM to read a bounded set first.

- Reads only text candidates under `--max-bytes-per-file`.
- Extracts headings, frontmatter keys, links, wikilinks, code-fence spans, and keyword groups.
- Produces `llm-routing-packet.md` and `candidate-files.*`.

## Option 3: Structure Maps

Use when Markdown/wiki navigation matters.

- Keeps detailed structure records in NDJSON.
- Good for later graph or broken-link work.
- Still avoids semantic interpretation.

## Option 4: Search/Retrieval Prep

Future extension, not enabled here by default.

- SQLite FTS5 or JSON search export.
- Requires local runtime checks and explicit derived-artifact policy.

## Questions To Decide Before Large Production Runs

1. Should the output optimize for human review, LLM routing, or machine indexing?
2. What is the maximum file size an LLM should be allowed to inspect in one pass?
3. Should code files be ranked equally with docs, or only included when path/keyword signals are strong?
4. Should hashes be computed for all files, only candidates, or never during fast inventory?
5. Should database files be inventoried only, exported by a domain tool, or excluded until a schema-specific pass exists?
6. Which keyword groups are project-specific enough to add before scanning?
7. Should future runs create a local lexical search index, or is the routing packet enough?
