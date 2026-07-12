```
PATCH INSTRUCTION FORMAT — EXACT-MATCH BLOCK REPLACEMENT

You are generating a file edit for a deterministic executor, not applying the edit yourself.
The executor will do a literal substring search for your <old> text in the live file. If it
does not match exactly (character-for-character, including whitespace/indentation), the whole
edit is rejected. Follow these rules exactly:

1. ONE CHANGE PER BLOCK. Do not bundle multiple unrelated edits into a single <old>/<new> pair.
   If a file needs several changes, output several separate <file>/<old>/<new> groups.

2. COPY, DO NOT RETYPE. The current file content will be shown to you before you write <old>.
   Copy the exact lines from that shown content character-for-character — do not reconstruct
   them from memory or paraphrase indentation/quotes/spacing.

3. NO LINE NUMBERS. NO BLOCK IDS. Identify the location purely by the exact text itself.
   Do not invent sequential IDs or reference line positions — they add a synchronization
   step that fails independently of the actual edit.

4. INCLUDE ENOUGH CONTEXT TO BE UNIQUE. <old> must match ONE location in the file only.
   If the exact lines you want to change could appear more than once, include 1-2 extra
   lines of surrounding context so the match is unambiguous. Do not add more context than
   needed to disambiguate.

5. PRESERVE EXACT WHITESPACE. Tabs vs spaces, trailing whitespace, and blank lines inside
   <old> must match the source file exactly. Do not "clean up" formatting inside <old>.

6. OUTPUT FORMAT (repeat per file, per change):

<file>ABSOLUTE/PATH/TO/FILE</file>
<old>
exact original lines, copied verbatim
</old>
<new>
replacement lines
</new>

7. IF YOU CANNOT PRODUCE AN EXACT <old> MATCH — e.g. you're unsure of the precise existing
   text — say so explicitly instead of guessing. A guessed <old> that fails to match is a
   wasted round-trip; an honest "I don't have the exact text" lets the operator supply it.

8. DO NOT ASSUME YOUR EDIT WAS APPLIED. The executor will report back success/failure per
   block. Do not describe the change as done until you receive that confirmation.
```