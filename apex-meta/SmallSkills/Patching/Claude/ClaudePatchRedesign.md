You are right. My previous answer over-weighted **unified diff as the authoring artifact**. That is not aligned with your actual failure history.

The corrected model is:

> **Do not ask AI to author exact patches or exact search strings. Let AI describe intent and candidate locations. Let a local deterministic executor inspect, select, replace, validate, and diff.**

## Core correction

| Question                                     | Better answer now                                                                                | Why                                                                                                                                                                              |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Should AI create unified diff patches?       | **No, not as the primary mechanism.**                                                            | AI-generated unified diffs are fragile: wrong context, stale lines, bad hunk headers, paraphrased text, broken apply.                                                            |
| Should AI define exact search/replace pairs? | **Only if the target span is first selected from live file text.**                               | AI often paraphrases or normalizes the search text, so replacement fails or hits the wrong span.                                                                                 |
| What should AI provide?                      | **Intent, target file guess, function/section name, semantic change, validation expectation.**   | This uses AI for judgment, not exact byte-level operation.                                                                                                                       |
| What should deterministic tools provide?     | **File read, search, unique-match selection, replacement, diff, tests, commit.**                 | These are mechanical and must not depend on model memory.                                                                                                                        |
| What changes with Claude Code + VS Code?     | **The agent can operate inside a real repo clone and use editor/search/git/test tools locally.** | This gives it better file access and deterministic feedback than chat-only patch generation.                                                                                     |
| Is online GitHub required for git patching?  | **No. Most git operations are local.**                                                           | `git diff`, `git apply`, `git status`, `git commit`, branches, worktrees all work locally. Network is only needed for `git fetch`, `pull`, `push`, PRs, or checking remote main. |

## Recommended process: search/replace executor, not patch author

|Step|AI role|Claude Code / local tool role|Deterministic gate|
|---|---|---|---|
|1. Context lock|State repo, branch, likely files, mode|Run `git status`, `git branch`, `git rev-parse`|Stop if wrong repo/path/branch|
|2. Locate target|Give rough anchors: function name, heading, nearby phrase|Use `rg`, AST parser, editor symbols, VS Code search|Must find exact live span|
|3. Extract exact text|Do not invent exact search text|Tool copies exact current span from file|Exact span exists once|
|4. Replace|AI proposes replacement logic/content|Script/editor applies replacement to selected span|Replacement applied to one span only|
|5. Review diff|AI checks semantic result|`git diff -- <file>`|Only intended files/spans changed|
|6. Validate|AI says expected behavior|Run tests, compile, fixtures, lint|Pass/fail is deterministic|
|7. Commit|AI writes commit message|Git commits locally|Only intended files staged|
|8. Push/PR|Optional|Network Git only here|Push only after local pass|

This shifts the executable artifact from “AI-written diff” to **local file operations over exact live text**.

## Local vs online GitHub

|Operation|Needs internet?|Notes|
|---|--:|---|
|`git status`|No|Pure local|
|`git diff`|No|Pure local|
|`git apply --check`|No|Pure local|
|`git apply`|No|Pure local|
|`git commit`|No|Pure local|
|`git worktree add` from existing local branch/commit|No|Pure local|
|Search files with `rg` / VS Code search|No|Pure local|
|Run tests/scripts|No, unless tests need network|Depends on project|
|`git fetch`|Yes|Updates local view of remote|
|`git pull`|Yes|Fetch + merge/rebase|
|`git push`|Yes|Sends commit to remote|
|PR creation/review|Yes|GitHub/GitLab etc.|

So the answer is: **you can run almost the whole reliable patch process locally**. You only need online remote access when you want to sync with remote main, push, or open/review PRs.

For reliability, the safest mode is:

|Situation|Recommended mode|
|---|---|
|You are testing patch mechanics|Local clone only, no push|
|You want a validated change but not publish yet|Local branch or main commit, no push|
|You want remote main updated|Local validate → commit → push|
|You worry local clone is stale|`git fetch origin` / `git pull --ff-only` before execution|
|You need audit/review|Push and PR or push main only when explicitly requested|

## Better decision flow

|Question|Option A|Option B|Recommendation|
|---|---|---|---|
|Is the change exact text insertion/replacement?|AI writes exact diff|Claude Code selects live span and replaces|**Use live span selection.**|
|Is the target code structured Python/JS/etc.?|Text search|AST/symbol search|**Use AST/symbol when available.**|
|Is the file Markdown?|AI-generated unified diff|Heading-based section extraction + replace|**Use heading/section-aware replacer.**|
|Is it a move/reorg?|Edit while moving|Move-only, prove equality|**Move-only first.**|
|Is search pattern unique?|Proceed anyway|Stop or widen context|**Stop unless unique.**|
|Does AI want to “clean up nearby text”?|Allow|Capture as later improvement|**Do not apply silently.**|
|Does validation require behavior?|AI says “looks good”|Run deterministic fixture/test|**Run fixture/test.**|
|Does patch need online repo?|Always|Only pull/push/PR|**Mostly local.**|

## Revised architecture

|Layer|Tool|Responsibility|Failure it prevents|
|---|---|---|---|
|Intent layer|AI|Understand desired change|Human does not manually encode every detail|
|Location layer|`rg`, VS Code symbols, AST parser|Find exact live target|AI hallucinated path/anchor|
|Selection layer|Script/editor API|Extract exact current span|AI paraphrased search string|
|Transformation layer|Scripted replace|Replace one exact selected span|Bad search/replace drift|
|Proof layer|`git diff`, tests|Show actual landed change|“Looks right” judgment|
|Publication layer|Git remote / PR|Push/review only after local proof|Broken remote changes|

## What Claude Code + VS Code likely improves

|Capability|Why it matters|
|---|---|
|Real repo clone access|No more patching from copied chat text|
|Terminal access|Can run `rg`, `git`, tests, scripts|
|Editor integration|Can use actual file buffers and selection ranges|
|Local feedback loop|Can inspect failure output immediately|
|Git awareness|Can diff exactly what changed|
|Extension/plugin/skills ecosystem|Can package repeatable patch workflows|

Claude Code is designed as an agentic coding tool that can run shell commands and edit files; public descriptions also emphasize local file read/write and command execution. ([Wikipedia](https://de.wikipedia.org/wiki/Claude_%28Sprachmodell%29?utm_source=chatgpt.com "Claude (Sprachmodell)")) The web version reportedly clones GitHub repos into a managed VM and can analyze, edit, test, push, and create PRs, but that is a cloud/GitHub-connected mode, not a requirement for local git operations. ([Windows Central](https://www.windowscentral.com/artificial-intelligence/anthropics-claude-code-is-now-available-on-the-web-for-its-pro-and-max-users?utm_source=chatgpt.com "Claude Code comes to the web - so you can pay to manage the AI that's taking your job"))

## Skill/package direction

I would not copy random third-party skills blindly. The skill ecosystem is large, but security research flags real risks around skills that perform system-level or state-changing actions. One analysis describes hundreds of thousands of skills across marketplaces/GitHub and identifies supply-chain risks such as abandoned repositories. ([arXiv](https://arxiv.org/abs/2603.16572?utm_source=chatgpt.com "Malicious Or Not: Adding Repository Context to Agent Skill Classification"))

For your case, the right move is not “find a big Claude Code skill pack.” It is to create **small local skills** around deterministic patch mechanics.

|Skill/package|Purpose|Should exist?|
|---|---|--:|
|`local-span-replacer`|Select exact live span, replace once, show diff|Yes|
|`markdown-section-replacer`|Replace one Markdown heading section by parsed heading boundaries|Yes|
|`python-function-replacer`|Replace one Python function by AST line span|Yes|
|`patch-run-validator`|Run git diff, scope check, compile/test, report|Yes|
|`fixture-runner`|Build fixture, run command, assert JSON paths|Yes|
|`unified-diff-author`|AI writes final diff directly|No|
|`broad-refactor-agent`|AI rewrites many files freely|No|

## Copy-paste Claude Code skill draft

This is the kind of skill I would actually use.

```md
---
name: deterministic-span-replacer
description: Use when editing existing repository files where AI must not hand-author unified diffs or approximate search/replace strings. The skill forces live file span extraction, single-span replacement, git diff review, and deterministic validation.
---

# Deterministic Span Replacer

## Rule

Do not hand-author unified diff patches as the primary edit mechanism.

Do not invent exact search strings from memory.

Use live repository text as the only source for search/replace anchors.

## Workflow

1. Lock context:
   - run `git rev-parse --show-toplevel`
   - run `git branch --show-current`
   - run `git status --porcelain`
   - identify exact repo-relative target file

2. Locate candidate span:
   - use `rg` for rough search
   - use language-aware structure when possible:
     - Python: `ast` line spans
     - Markdown: heading boundaries
     - JSON/YAML: parser path if possible

3. Extract exact current span:
   - print or save the exact span from the file
   - verify it exists exactly once
   - if not unique, stop and ask for narrower target

4. Apply replacement:
   - replace only the selected span
   - do not edit nearby text
   - do not reformat unrelated content

5. Verify:
   - run `git diff -- <target-file>`
   - verify only intended span changed
   - run relevant compile/test/fixture command
   - run `git status --porcelain`

6. Report:
   - target file
   - selected span method
   - changed files
   - validation commands
   - pass/fail result

## Forbidden

- AI-authored final unified diff as primary mechanism
- approximate search/replace
- fuzzy multi-match replacement
- full-file rewrite unless explicitly authorized
- adjacent cleanup
- changing files outside declared scope
```

## Copy-paste Python helper concept

This is the deterministic core I would want Claude Code to use instead of improvising search/replace:

```python
#!/usr/bin/env python3
import argparse
from pathlib import Path

def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"replace_once failed: expected 1 match, got {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("file")
    p.add_argument("--old-file", required=True)
    p.add_argument("--new-file", required=True)
    args = p.parse_args()

    replace_once(
        Path(args.file),
        Path(args.old_file).read_text(encoding="utf-8"),
        Path(args.new_file).read_text(encoding="utf-8"),
    )

if __name__ == "__main__":
    main()
```

The important part: **AI does not type the search string into the command.** Claude Code first extracts the exact old span into `old.txt`, writes the replacement into `new.txt`, then the helper refuses to run unless the old span appears exactly once.

## Practical recommendation

|Priority|Build/use|Why|
|--:|---|---|
|1|`replace_once.py` exact-span replacer|Solves broken search/replace by requiring one exact live match|
|2|Markdown heading-section extractor|Solves docs edits without unified diff authoring|
|3|Python AST function replacer|Solves function-level code patches|
|4|Git scope validator|Prevents unrelated file edits|
|5|Fixture/assertion runner|Replaces manual Bash/JSON checking|
|6|Claude Code skill wrapping the above|Makes the behavior repeatable|

## My corrected recommendation

Do **not** center the system on unified diff creation.

Center it on:

> **live span extraction → exact once-only replacement → git diff proof → deterministic validation**

Unified diff still matters, but as a **review/proof artifact generated by git after the edit**, not as the thing AI writes by hand.