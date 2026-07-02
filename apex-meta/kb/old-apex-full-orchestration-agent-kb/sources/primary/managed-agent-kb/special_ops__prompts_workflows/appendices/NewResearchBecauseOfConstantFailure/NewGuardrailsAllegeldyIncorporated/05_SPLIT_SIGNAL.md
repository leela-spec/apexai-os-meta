[SPLIT_SIGNAL v1.0]
TRIGGER: file content will exceed single response limit (~3000 tokens safe ceiling)

PROTOCOL:
1. Before writing: output → SPLIT_REQUIRED: {n} parts estimated
2. Write PART_1 with header:
   # FILE: {FILENAME.ext} | PART: 1 of {n}
   {content chunk — ends at clean logical boundary}
   CONTINUE → type "part 2"
3. On "part 2": write next chunk with:
   # FILE: {FILENAME.ext} | PART: 2 of {n}
   {content — no preamble}
4. Final part ends with:
   # END_OF_FILE: {FILENAME.ext} | PARTS: {n} | SCOPE_RESPECTED: yes

FORBIDDEN:
- Summarizing remaining content instead of writing it
- Adding new sections not in original scope during continuation
- Mixing file parts with explanation text
