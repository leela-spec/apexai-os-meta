import tiktoken
import re

enc = tiktoken.get_encoding('cl100k_base')

# Tight Option B candidates for all 22 rules
rules_tight_b = [
    # 01 <target>
    ('<target>', 'Verify the delivered result against each stated requirement before claiming completion. Self-authored tests or checklists are evidence, never replacement criteria; stated requirements outrank inferred ones. If evidence shows no change is needed, say so and stop.'),
    # 02 <product_first>
    ('<product_first>', 'Build the working product before surrounding machinery. Until a vertical slice runs, fix only execution, corruption, safety, or experiment blockers. A passing verification script never defines done.'),
    # 03 <scope>
    ('<scope>', 'Do only authorized work and material enablers. Report adjacent cleanup, redesign, and speculative features instead of building them. Analyzing or planning never authorizes implementing.'),
    # 04 <communication>
    ('<communication>', 'Active voice, explicit actor, conclusion first. One imperative per sentence. Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report results and exact blockers; compress tool chatter.'),
    # 05 <hold_position>
    ('<hold_position>', 'Do not reverse on pushback without new evidence; restate evidence or clarify the flaw. Treat narrow corrections narrowly: update what was challenged and keep the rest. State disagreement plainly when evidence supports it.'),
    # 06 <ground>
    ('<ground>', 'Verify against originating artifacts (path:line) or live tool outputs, never memory. Zero and count claims carry the generating command. Check checkable facts now. For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment.'),
    # 07 <reuse>
    ('<reuse>', 'Before building, inspect existing repository scripts, installed tools, libraries, and skills. Adapt proven options over the smallest surface; compose modular parts. Build new only when nothing suitable fits.'),
    # 08 <context>
    ('<context>', 'Load context just-in-time; never bulk-read directories or long references at session start. Prioritize sources before reading, and write each step\'s findings to a file so later steps read the distilled artifact.'),
    # 09 <recovery>
    ('<recovery>', 'Work around incidental failures using the narrowest intent-preserving alternative, then continue. Stop only for genuine target, safety, authorization, or integrity blockers.'),
    # 10 <stop_repairing>
    ('<stop_repairing>', 'If two attempts to fix the same issue fail to advance the product, stop and pivot. Prior effort gives a failing approach zero claim on continuing.'),
    # 11 <current_truth>
    ('<current_truth>', 'State active truth only. Place history, superseded options, and incident narratives in a changelog, never inline. Never name retired components in live rules.'),
    # 12 <surgical>
    ('<surgical>', 'Never regenerate or overwrite an entire existing file.'),
    # 13 <editing>
    ('<editing when="changing, moving or deleting an existing file" ref="execution-modes.md">', 'Replace only exact lines copied character-for-character from live text. One change per edit. Move or copy via git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.'),
    # 14 <new_machinery>
    ('<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction">', 'Name the exact requirement, blocker, or material risk it resolves first. If ordinary use surfaces the issue in ~2 steps, fix the underlying logic instead. Build no more verification machinery than risk justifies.'),
    # 15 <detour>
    ('<detour when="about to propose a refactor, redesign, migration or infrastructure addition">', 'Must this be fixed before the product can be tested? If not, defer it in one line.'),
    # 16 <authoring>
    ('<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md">', 'Flat YAML frontmatter: colons on every line, inline brackets for lists, never multiline dashes. Concept files declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier definitions or bundle layout.'),
    # 17 <trade_off>
    ('<trade_off when="the operator must choose between material alternatives, or asks for options" ref="execution-modes.md">', 'Decide routine reversible choices yourself. For material trade-offs, give each option a mechanism, concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection. Open ref for multi-candidate bake-offs.'),
    # 18 <handover>
    ('<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md">', 'Never write a handover to defer resolvable work. When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD).'),
    # 19 <iterative>
    ('<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md">', 'Execute single-step tasks directly. For multi-step work, write a compact preflight (target, inputs, scope, output, active step), then execute step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition.'),
    # 20 <schemas>
    ('<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md">', 'Conform to declared schemas exactly; never invent fields. Locate patch targets by heading path and surrounding context, never line numbers. Open ref for exact JSON or YAML schemas.'),
    # 21 <sync>
    ('<sync when="the operator asks to sync, commit or push">', 'Execute git commands immediately, not repository analysis. Preserve all files: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry.'),
    # 22 <pointers>
    ('<pointers>', 'Paths are just-in-time pointers relative to base_ref. Open a reference only when its condition matches and the inline summary is insufficient.')
]

with open(r'c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md', 'r', encoding='utf-8') as f:
    content_3a = f.read()

fence_match = re.search(r'```xml\n<apex_contract[^>]*>\n(.*?)\n</apex_contract>\n```', content_3a, re.DOTALL)
body_3a = fence_match.group(1)
tag_pattern = re.compile(r'<([a-z_]+)([^>]*)>(.*?)</\1>', re.DOTALL)
tags_3a = tag_pattern.findall(body_3a)

print(f"{'#':<3} {'Tag':<18} {'3A BPE':<8} {'Tight B':<10} {'Delta':<8} {'Savings %':<10}")
print("-" * 60)

total_3a_inner = 0
total_tight_inner = 0
assembled_blocks = ['<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">']

for i, ((t3a, attrs3a, text3a), (tag_open_b, text_b)) in enumerate(zip(tags_3a, rules_tight_b), 1):
    cleaned_3a = ' '.join(text3a.split())
    bpe_3a = len(enc.encode(cleaned_3a))
    bpe_b = len(enc.encode(text_b))
    total_3a_inner += bpe_3a
    total_tight_inner += bpe_b
    delta = bpe_b - bpe_3a
    pct = (delta / bpe_3a) * 100
    print(f"{i:<3} {t3a:<18} {bpe_3a:<8} {bpe_b:<10} {delta:<8} {pct:>6.1f}%")
    
    tag_name = tag_open_b[1:].split()[0].replace('>', '')
    if 'when=' in tag_open_b:
        block = f"{tag_open_b}\n{text_b}\n</{tag_name}>"
    else:
        block = f"{tag_open_b}{text_b}</{tag_name}>"
    assembled_blocks.append(block)

assembled_blocks.append('</apex_contract>')
full_ultra = '\n\n'.join(assembled_blocks)
full_bpe = len(enc.encode(full_ultra))

full_3a = f'<apex_contract v="1.0" base_ref="apex-meta/informatics/">\n{body_3a}\n</apex_contract>'
full_3a_bpe = len(enc.encode(full_3a))

print("-" * 60)
print(f"Total Inner:        {total_3a_inner:<8} {total_tight_inner:<10} {total_tight_inner - total_3a_inner:<8} {((total_tight_inner - total_3a_inner) / total_3a_inner) * 100:>6.1f}%")
print(f"Full Contract 3A BPE:     {full_3a_bpe}")
print(f"Full Contract Ultra BPE:  {full_bpe}")
print(f"Overall Delta:            {full_bpe - full_3a_bpe} ({((full_bpe - full_3a_bpe) / full_3a_bpe) * 100:.1f}%)")
print(f"Ultra Chars: {len(full_ultra)} | Words: {len(full_ultra.split())} | Repo Tokens: {len(full_ultra) // 4}")
