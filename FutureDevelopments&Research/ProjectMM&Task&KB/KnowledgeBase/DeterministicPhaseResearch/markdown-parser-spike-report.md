# Markdown Parser Spike Report

## 1. Verdict

- **Best V1 parser:** simple Python state-machine parser.
- **Best V1.5 parser:** hybrid: Python parser for stable repo-local output plus `markdown-it-py` for token-boundary validation where available.
- **Should use Node/remark now:** no.
- **Should use Python-only now:** yes.
- **Main reason:** Phase 0 needs low-friction deterministic structure extraction. The source corpus is mostly Markdown/MDX with headings, frontmatter, links, and fenced code blocks. A Python parser can capture those fields reliably enough for pre-LLM navigation artifacts without introducing a Node dependency chain.

Execution note: the Windows checkout path `C:\GitDev\apexai-os-meta` is not mounted in this ChatGPT environment. I therefore executed the spike as far as possible by reading repo files through the GitHub connector, checking parser availability locally, and writing downloadable artifacts instead of mutating the repo.

## 2. Operator-level explanation

The parser is a **table-of-contents and wiring extractor**.

It does **not** decide what the documents mean. It only records facts such as:

```text
this file has these headings
this file has these links
this file has this YAML/frontmatter
this file has these fenced code blocks
this file appears to be a converted PDF, MDX doc, skill entrypoint, or operator note
```

That helps the later LLM phase because the LLM does not need to blindly read every source file. It can first inspect a compact map and ask: “Which files have the headings, examples, links, and code blocks relevant to this ingest question?”

In practical terms, this becomes a cheap Phase 0 navigation layer before expensive Phase 1 semantic ingest.

## 3. Comparison Table

| Approach | Install needed | Complexity | Accuracy | Handles code blocks | Handles links | Handles wikilinks | Handles frontmatter | Output quality | Maintenance | Recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Simple Python parser | No | Low | Medium-high for this corpus | Yes, with state-machine fence tracking | Yes, with regex | Yes, with regex | Yes, delimiter-based | Good enough for Phase 0 | Low | **Use for V1** |
| `markdown-it-py` | Already available here; may need pip install in repo | Medium | High for Markdown tokenization | Yes | Yes | No native wikilink semantics | Needs plugin/custom prepass | Better boundaries than regex | Medium | **Use as V1.5 optional validator** |
| Node `remark` / unified | Node/npm available here; repo install still adds package footprint | Medium-high | Very high for Markdown/MDX AST if configured | Yes | Yes | Plugin/custom needed | Needs gray-matter or unified plugin | Excellent AST if maintained | Higher | **Do not use now; revisit if MDX edge cases matter** |
| Hybrid | Python + optional parser plugins | Medium | High | Yes | Yes | Yes by Python prepass | Yes | Best practical path | Medium | **Recommended after V1 baseline** |

## 4. Sample Output

Representative JSON record:

```json
{
  "path": "apex-meta/kb/claude-skill-design/sources/curated/official-repos/agentskills-agentskills/docs/skill-creation/using-scripts.mdx",
  "source_type": "official_mdx_doc_with_frontmatter_and_code",
  "h1_title": null,
  "frontmatter_if_detectable": {
    "start_line": 3,
    "end_line": 7,
    "fields": {
      "title": "Using scripts in skills",
      "sidebarTitle": "Using scripts",
      "description": "How to run commands and bundle executable scripts in your skills."
    }
  },
  "headings": [
    {"level": 2, "text": "One-off commands", "line": 11},
    {"level": 2, "text": "Referencing scripts from `SKILL.md`", "line": 91},
    {"level": 2, "text": "Self-contained scripts", "line": 124}
  ],
  "markdown_links": [
    {"text": "uvx", "target": "https://docs.astral.sh/uv/guides/tools/", "line": 17},
    {"text": "PEP 723", "target": "https://peps.python.org/pep-0723/", "line": 132}
  ],
  "wikilinks": [],
  "code_blocks": [
    {"language": "bash", "start_line": 19, "end_line": 22},
    {"language": "markdown SKILL.md", "start_line": 97, "end_line": 102},
    {"language": "python scripts/extract.py", "start_line": 134, "end_line": 145}
  ]
}
```

Full sample map: `heading-link-frontmatter-map.sample.json`.

## 5. Failure Cases

1. **Regex-only heading extraction can be fooled by headings inside code fences.**  
   Mitigation: use a state-machine parser that ignores headings while inside fenced code blocks.

2. **MDX components are not ordinary Markdown.**  
   Examples like `<Tabs>`, `<Tab>`, `<Note>`, and `<Tip>` appear in official docs. A simple parser can ignore them safely for headings/links/code, but cannot fully model component nesting.

3. **Collapsed inline examples are structurally poor.**  
   Some operator notes contain large inline backtick examples rather than fenced code blocks. A parser will not treat these as code blocks, which is correct mechanically but may hide useful embedded YAML examples.

4. **Converted PDF Markdown contains artifacts.**  
   The PDF conversion includes picture placeholders, repeated chapter headings, and page numbers. A parser will extract duplicate/noisy headings unless Phase 0 adds normalization rules.

5. **Wikilinks may be absent in this sample but still need support.**  
   The selected sample had no confirmed `[[wikilink]]` examples. The parser should still include wikilink extraction so the same artifact format works for future Obsidian-style material.

6. **Line numbers from GitHub connector fetches can be offset by connector metadata.**  
   The downloaded sample records preserve the source line markers from fetched content, but a local script should compute line numbers from actual files in the Windows checkout.

7. **Frontmatter parsing needs YAML validation, not just delimiter detection.**  
   V1 can detect frontmatter blocks; V1.5 should parse YAML fields with `yaml.safe_load` and report malformed frontmatter.

## 6. Final Recommendation

Build **Phase 0 V1** as a repo-local Python script that produces:

```text
apex-meta/kb/claude-skill-design/manifests/markdown-parser-spike-report.md
apex-meta/kb/claude-skill-design/manifests/heading-link-frontmatter-map.sample.json
```

Recommended V1 fields:

```yaml
fields:
  - path
  - source_type_guess
  - h1_title
  - headings:
      - level
      - text
      - line
  - markdown_links:
      - text
      - target
      - line
  - wikilinks:
      - raw
      - target
      - alias
      - line
  - code_blocks:
      - language
      - start_line
      - end_line
  - frontmatter_if_detectable
  - parser_warnings
```

Recommended parser strategy:

1. Walk `apex-meta/kb/claude-skill-design/sources/`.
2. Include `.md`, `.mdx`, `.markdown`.
3. Exclude logs, manifests, binary assets, and generated analysis/wiki outputs.
4. Track fenced code-block state before extracting headings and links.
5. Detect frontmatter only at the top of the file.
6. Extract Markdown links and wikilinks line-by-line.
7. Write JSON deterministically with sorted paths.
8. Use `markdown-it-py` only as an optional cross-check, not as a hard dependency for V1.
9. Defer Node/remark until a concrete MDX parsing failure proves Python insufficient.

## 7. Executed Sample Selection

The best-effort sample covered:

| Category | Sample |
|---|---|
| Converted PDF Markdown | `official-pdfs/anthropic-complete-guide-to-building-skills-for-claude.md` |
| Official skill entrypoint | `anthropics-skills/skills/skill-creator/SKILL.md` |
| Official MDX with frontmatter | `agentskills.../docs/skill-creation/using-scripts.mdx` |
| Official MDX best-practices doc | `agentskills.../docs/skill-creation/best-practices.mdx` |
| Official repo README with links | `anthropics-skills/README.md` |
| Official quickstart MDX | `agentskills.../docs/skill-creation/quickstart.mdx` |
| Curated repo extract | `repo-extracts/anthropics-skills__skills__mcp-builder__SKILL.md` |
| Official reference doc with code | `mcp-builder/reference/python_mcp_server.md` |
| Operator-supplied guide | `operator-supplied/notes/Apex_Alfred_Skill_Definition_Guide.md` |
| Operator-supplied preparation note | `operator-supplied/notes/ClaudePhase1FilePreparation.md` |
