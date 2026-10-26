import tiktoken

enc = tiktoken.get_encoding('cl100k_base')

def stats(name, text):
    bpe = len(enc.encode(text))
    chars = len(text)
    words = len(text.split())
    repo = chars // 4
    print(f'{name}: BPE={bpe}, chars={chars}, words={words}, repo={repo}')
    return bpe, chars, words, repo

print('=== RULE 09: <recovery> ===')
stats('Rule 09 Block', '<recovery>Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue. Stop only for a genuine target, safety, authorization or integrity blocker.</recovery>')
stats('Rule 09 Inner', 'Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue. Stop only for a genuine target, safety, authorization or integrity blocker.')
stats('SB-09.1', 'Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue.')
stats('SB-09.2', 'Stop only for a genuine target, safety, authorization or integrity blocker.')
stats('Rule 09 Opt B', '<recovery>Work around incidental failures using the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.</recovery>')
stats('Rule 09 Opt C', '<recovery>Work around incidental failures with the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.</recovery>')

print('=== RULE 10: <stop_repairing> ===')
stats('Rule 10 Block', '<stop_repairing>If two attempts to fix the same thing have not moved the product forward, stop and change approach. Prior effort gives a failing approach no claim on continuing.</stop_repairing>')
stats('Rule 10 Inner', 'If two attempts to fix the same thing have not moved the product forward, stop and change approach. Prior effort gives a failing approach no claim on continuing.')
stats('SB-10.1', 'If two attempts to fix the same thing have not moved the product forward, stop and change approach.')
stats('SB-10.2', 'Prior effort gives a failing approach no claim on continuing.')
stats('Rule 10 Opt B', '<stop_repairing>If two fix attempts fail to advance the product, stop and pivot. Prior effort gives a failing approach zero claim on continuing.</stop_repairing>')
stats('Rule 10 Opt C', '<stop_repairing>Two-strike rule: after two failed fix attempts on the same issue, stop and pivot. Sunk effort gives a failing approach zero claim on continuation.</stop_repairing>')

print('=== RULE 11: <current_truth> ===')
stats('Rule 11 Block', '<current_truth>State active truth only. History, superseded options and incident narrative go to a changelog, never inline. Do not name retired components in live rules.</current_truth>')
stats('Rule 11 Inner', 'State active truth only. History, superseded options and incident narrative go to a changelog, never inline. Do not name retired components in live rules.')
stats('SB-11.1', 'State active truth only.')
stats('SB-11.2', 'History, superseded options and incident narrative go to a changelog, never inline.')
stats('SB-11.3', 'Do not name retired components in live rules.')
stats('Rule 11 Opt B', '<current_truth>State active truth only. Place history, superseded options, and incident notes in a changelog, never inline. Never name retired components in live rules.</current_truth>')
stats('Rule 11 Opt C', '<current_truth>State active truth only; place history, superseded options, and incident logs in a changelog, never inline. Never mention retired components in live rules.</current_truth>')

print('=== RULE 12: <surgical> ===')
stats('Rule 12 Block', '<surgical>Never regenerate or overwrite a whole existing file.</surgical>')
stats('Rule 12 Inner', 'Never regenerate or overwrite a whole existing file.')
stats('SB-12.1', 'Never regenerate or overwrite a whole existing file.')
stats('Rule 12 Opt B', '<surgical>Never regenerate or overwrite an existing file in full.</surgical>')
stats('Rule 12 Opt C', '<surgical>Never overwrite an entire existing file.</surgical>')

print('=== RULE 13: <editing> ===')
r13_block = '''<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md">
Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.
</editing>'''
stats('Rule 13 Block', r13_block)
r13_inner = 'Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.'
stats('Rule 13 Inner', r13_inner)
stats('SB-13.1', 'Replace only the exact lines that must change, copied character-for-character from the file you just read.')
stats('SB-13.2', 'One change per edit.')
stats('SB-13.3', 'Move or copy with git mv or cp, never by rewriting contents.')
stats('SB-13.4', 'Open ref for AST patches or multi-block executors.')
r13_opt_b = '''<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md">
Replace only exact lines copied character-for-character from live text. One change per edit. Move or copy via git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.
</editing>'''
stats('Rule 13 Opt B', r13_opt_b)
r13_opt_c = '''<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md">
Replace only exact lines copied character-for-character from live text; one change per edit. Move or copy via git mv or cp. Open ref for AST patches or multi-block executors.
</editing>'''
stats('Rule 13 Opt C', r13_opt_c)

print('=== RULE 14: <new_machinery> ===')
r14_block = '''<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction">
Name the exact requirement, blocker or material risk it serves first; if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead. Do not build more verification machinery than the risk justifies.
</new_machinery>'''
stats('Rule 14 Block', r14_block)
r14_inner = 'Name the exact requirement, blocker or material risk it serves first; if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead. Do not build more verification machinery than the risk justifies.'
stats('Rule 14 Inner', r14_inner)
stats('SB-14.1', 'Name the exact requirement, blocker or material risk it serves first;')
stats('SB-14.2', 'if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead.')
stats('SB-14.3', 'Do not build more verification machinery than the risk justifies.')
r14_opt_b = '''<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction">
Name the exact requirement, blocker, or material risk it resolves first. If ordinary use surfaces the issue in ~2 steps, fix data or logic directly. Build no more verification machinery than risk justifies.
</new_machinery>'''
stats('Rule 14 Opt B', r14_opt_b)
r14_opt_c = '''<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction">
Name the exact requirement, blocker, or risk it serves first. If ordinary use reveals the issue in ~2 steps, fix underlying logic instead of adding machinery.
</new_machinery>'''
stats('Rule 14 Opt C', r14_opt_c)

print('=== RULE 15: <detour> ===')
r15_block = '''<detour when="about to propose a refactor, redesign, migration or infrastructure addition">
Ask whether this must be fixed before the product can be tested. If not, defer it in one line.
</detour>'''
stats('Rule 15 Block', r15_block)
r15_inner = 'Ask whether this must be fixed before the product can be tested. If not, defer it in one line.'
stats('Rule 15 Inner', r15_inner)
stats('SB-15.1', 'Ask whether this must be fixed before the product can be tested.')
stats('SB-15.2', 'If not, defer it in one line.')
r15_opt_b = '''<detour when="about to propose a refactor, redesign, migration or infrastructure addition">
Must this be fixed before testing the product? If not, defer it in one line.
</detour>'''
stats('Rule 15 Opt B', r15_opt_b)
r15_opt_c = '''<detour when="about to propose a refactor, redesign, migration or infrastructure addition">
Must this be fixed before testing the product? If not, defer it in one line.
</detour>'''
stats('Rule 15 Opt C', r15_opt_c)
