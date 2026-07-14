Execute this deep research prompt and produce three outputs (A, B, C) as specified:

---

## 0. Anti-Contamination Guard — Read This First

Before reading any source, apply these rules without exception:

1. Newest explicit decision wins. When two project files contradict each other, the newer file wins.

2. Operator statement overrides AI output. Any constraint, limitation, or guardrail in the research files that cannot be traced to an explicit operator instruction must be flagged UNVERIFIED_ORIGIN and excluded from final decisions.

3. Phase 0 script is generic — not tied to any specific KB. Any place where a specific KB name (e.g. claude-skill-design) appears as a fixed target for the script is a contamination error and should be ignored/focused on the general process.

4. Contaminated decisions are dead. Do not carry them forward into Output B or C.

---

## 1. Source Index — Read These Files

### 1A. Project Files

Read all of the following. For each: note the file name, primary purpose, and flag any contamination matching Section 0.

| File | What to focus on |

|---|---|

| Apex Phase 0 Corpus Intelligence Implementation Decision.md | PRIMARY DECISION SOURCE. Locked decisions D1–D8. V1 artifact schemas (Sections 4.1–4.8). Script contract. V1 vs V1.5 scope boundary. Flag any hardcoded KB path. |

| DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md | What already exists in apex-kb skill vs. what is new. Integration patches. Check for hardcoded paths. |

| Claude_Apex KB_SQLiteFTS5BM25_CCv2.md | Most recent FTS5/BM25 research. Extract: schema decisions, index structure, query interface. Supersedes older versions. |

| Claude_Apex KB_SQLiteFTS5BM25_CC.md | Older version — use only if CCv2 is silent on a specific point. |

| Claude_Apex KB_SQLiteFTS5BM25_GPT.md | Cross-model validation of FTS5 approach. Note disagreements with CC versions. |

| KB-Researchv3_gpt_FB_claude.md | Feedback-integrated KB research. Key decisions on retrieval flow and ranking. Flag drift vs. CCv2. |

| KB-Researchv3_gpt.md | Earlier KB research round. Use only for context on what changed between rounds. |

| Pre-LLM Tool Stack Installability and Value Audit.md | CRITICAL for tool decisions. What is installable on Windows? What was verified working? What was deferred? |

| Pre-LLMToolStack.md | Earlier version of the tool audit. Flag differences vs. the full audit. |

| Markdown Structure Parser Spike for Apex KB Phase.md | Best parser approach for V1. Key decisions: Python state machine vs markdown-it-py. |

| markdown-parser-spike-report.md | Spike test results. What worked, what failed, parser warnings by file type. |

| Apex Link Graph and Process-Flow Representability Audit.md | What graph edges exist, what is Apex-specific vs. generic. V1 vs V1.5 graph scope. |

| process-flow-graph-audit.md | Process flow representability. What can be extracted deterministically. |

| graph-summary.md | Summary of graph findings. Only extract if it contradicts or extends the full audit. |

| link-graph.sample.json | Concrete sample of graph output format. Reference schema for V1.5 graph artifacts. |

exclude other project files

---

### 1B. GitHub Repo — leela-spec/apexai-os-meta (main branch)

Read the following paths in this exact order. For each: record path, read status (read / REPO_UNVERIFIED), and 2–3 key facts.

Priority 1 — Apex KB skill (highest relevance):

```

.claude/skills/apex-kb/SKILL.md

.claude/skills/apex-kb/package-manifest.md

.claude/skills/apex-kb/references/kb-contract.md

.claude/skills/apex-kb/references/script-command-contract.md

.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md

.claude/skills/apex-kb/templates/

```

Priority 2 — Scripts and KB structure:

```

apex-meta/scripts/

apex-meta/kb/

```

Priority 3 — Orchestration context (read briefly, reference only, not a target):

```

.claude/skills/plan/SKILL.md

.claude/skills/synch/SKILL.md

.claude/skills/session/SKILL.md

```

Priority 4 — Architecture history (context only, NOT as limitations or constraints):

```

ApexDefinition&OldVersions/ApexWithClaude/Architecture/

```

Personal workflow reference (orientation only — operator use patterns, not a technical spec):

```

ApexDefinition&OldVersions/ApexDefiniton/Routines/WeeklyRoutine_Overview_Marco&Meso.md

```

If any file is unreadable: label REPO_UNVERIFIED, continue. Hard abort only if GitHub connector fails entirely.

---

### 1C. Web Search — Validation Only

Use web search only for validating the research and fit and integration as new processes/files/scripts in the apex-kb . Do not use web for anything Apex-orchestration specific.

---

## 2. Contamination Audit

After reading all sources, understand the contamination that might be present and write a short paragraph to show your understanding and reflection to not carry them forward

---

## 3. Output A — Research Summary

### A1. What the Apex KB is and does

3–5 sentences. Based on SKILL.md and package-manifest.md from the repo. Current invocation model. What scripts/tools it currently uses.

### A2. What Phase 0 Corpus Intelligence is

3–5 sentences. Based on the Implementation Decision file. What problem it solves. What it produces. Who consumes its outputs.

### A3. How Phase 0 connects to the apex-kb skill

3–5 sentences. Based on repo reads. Where phase0_corpus_intelligence.py fits into the existing skill structure. What it extends vs. what it leaves untouched.

### A4. Locked decisions

| Decision | Locked value | Source file | Contamination-free? |

|---|---|---|---|

Flag any decision that contains a contamination error.

### A5. Open questions

Only genuine gaps the operator has not resolved. Not architectural options.

### A6. Tool validation from web search

| Tool | Version confirmed | Install command (Windows) | FTS5 available | Notes |

|---|---|---|---|---|

---

## 4. Output B — Integration Map

### B1. Files to create

| Target path in repo | Action | What it contains | Depends on repo read | Risk |

|---|---|---|---|---|

| apex-meta/scripts/phase0_corpus_intelligence.py | CREATE | Generic Phase 0 script | no | low |

| .claude/skills/apex-kb/references/phase0-corpus-intelligence-contract.md | CREATE | Script contract and artifact schemas | yes — references/ | low |

Add any additional rows based on live repo reads.

### B2. Files to patch

For each: quote the exact section heading from the live repo read where the append goes.

| Target path | Action | Where exactly (exact heading) | What to add | Verified from repo |

|---|---|---|---|---|

| .claude/skills/apex-kb/SKILL.md | APPEND | [exact heading from repo read] | Phase 0 commands block | yes / REPO_UNVERIFIED |

| .claude/skills/apex-kb/package-manifest.md | APPEND | [exact heading from repo read] | phase0 script registration | yes / REPO_UNVERIFIED |

| .claude/skills/apex-kb/references/script-command-contract.md | APPEND | end of file | phase0 subcommand entry | yes / REPO_UNVERIFIED |

### B3. Setup steps

Ordered, numbered. PowerShell commands for the operator's Windows machine.

---

## 5. Output C — Code-Ready Spec

### C1. Script contract

```yaml

script: apex-meta/scripts/phase0_corpus_intelligence.py

language: Python 3.9+

runtime_v1: stdlib only (os, sys, json, csv, hashlib, pathlib, re, collections, argparse)

runtime_v1_5_optional: markdown-it-py, python-frontmatter

no_llm: true

no_network: true

no_hardcoded_kb: true

subcommands:

profile:

inputs: source-inventory.json (if present) + os.walk(kb_root)

outputs: corpus-profile.md

parse-markdown:

inputs: all .md files under kb_root

outputs: heading-map.json, markdown-link-map.json, frontmatter-map.json

parser_v1: Python state-machine (stdlib only)

parser_v1_5: markdown-it-py (optional, --use-mdit flag)

keyword-map:

inputs: all text files under kb_root

outputs: keyword-hits.ndjson, topic-file-map.json

default_engine: python re (stdlib)

optional_engine: rg (ripgrep, --use-rg flag)

priority-candidates:

inputs: corpus-profile.md + frontmatter-map.json + path rules

outputs: source-priority-candidates.md

ranking_factors: [path_depth, source_group, frontmatter_fields, file_size]

forbidden_ranking_factors: [semantic_content, LLM_judgment]

navigation-report:

inputs: all previous outputs in output_root

outputs: phase0-navigation-report.md

all:

runs: profile → parse-markdown → keyword-map → priority-candidates → navigation-report

exit_on_first_error: false

flags:

--kb-root PATH required. Any KB directory. Generic.

--output-root PATH required. Where to write manifests/.

--check dry-run. Compute but write nothing.

--keywords STR comma-separated keyword additions.

--exclude STR path patterns to exclude. Default: derived/,outputs/,.git/,__pycache__/

--use-mdit activate markdown-it-py parser (v1.5)

--use-rg activate ripgrep for keyword scan (v1.5)

--verbose print per-file progress

exit_codes:

0: all outputs written successfully

1: error (no outputs written)

2: partial (some v1.5 steps skipped due to missing optional deps)

```

### C2. V1 artifact schemas

Extract and reproduce the exact field definitions from the Implementation Decision file (Sections 4.1–4.8) for each artifact. Schemas only, no prose.

- corpus-profile.md: required sections list

- heading-map.json: per-record fields

- markdown-link-map.json: per-record fields

- frontmatter-map.json: per-record fields

- keyword-hits.ndjson: per-line fields and default keyword groups

- topic-file-map.json: structure

- source-priority-candidates.md: ranking factors and forbidden factors

- phase0-navigation-report.md: required sections

### C3. Source inventory reuse logic

```python

# Pseudocode — implement exactly as described

def get_file_list(kb_root, output_root, exclude_patterns):

inventory_path = output_root / "source-inventory.json"

if inventory_path.exists():

base_list = json.load(open(inventory_path))

live_paths = set(walk_kb(kb_root, exclude_patterns))

inventory_paths = set(r["path"] for r in base_list)

new_files = live_paths - inventory_paths

# supplement base_list with new files, compute fields

return base_list

else:

return generate_inventory(kb_root, exclude_patterns)

# source-inventory.json schema: extract from live repo read if file is accessible

```

### C4. Apex KB skill integration points

Based on live repo reads. Fill in exact values where files were read successfully. Label REPO_UNVERIFIED where not.

```

SKILL.md:

last_section_heading: [exact heading from repo read]

append_after: [exact heading]

block_to_append: |

## Phase 0 Corpus Intelligence

Command: python apex-meta/scripts/phase0_corpus_intelligence.py

Subcommands: profile | parse-markdown | keyword-map | priority-candidates | navigation-report | all

Use when: preparing a KB for LLM ingest. Run before first ingest of any new KB.

Output location: {kb_root}/manifests/

package-manifest.md:

section_heading: [exact heading from repo read]

entry_to_add: |

- name: phase0_corpus_intelligence

path: apex-meta/scripts/phase0_corpus_intelligence.py

type: preprocessing

kb_target: generic

v1_deps: stdlib

v1_5_deps: markdown-it-py, python-frontmatter, ripgrep (optional)

references/script-command-contract.md:

exists: [yes / REPO_UNVERIFIED]

last_entry: [exact last entry or heading from repo read]

entry_to_add: |

### phase0_corpus_intelligence

subcommands: profile | parse-markdown | keyword-map | priority-candidates | navigation-report | all

flags: --kb-root --output-root --check --keywords --exclude --use-mdit --use-rg --verbose

exit: 0=ok 1=error 2=partial

```

---

## 6. Degradation Rules

| Failure | Response |

|---|---|

| One project file missing | Continue. Note in source table. |

| GitHub repo file unreadable | Label REPO_UNVERIFIED in B2 and C4. Continue. |

| GitHub connector fails entirely | Complete project files and web. Mark all B2/C4 repo fields REPO_UNVERIFIED. Produce full A, B, C. |

| FTS5 not available on operator Python | Flag in A6. Note in C1 that FTS5 is v1.5 conditional. |

| Hard abort | Only if no project files are readable AND no web AND no GitHub. |

'''