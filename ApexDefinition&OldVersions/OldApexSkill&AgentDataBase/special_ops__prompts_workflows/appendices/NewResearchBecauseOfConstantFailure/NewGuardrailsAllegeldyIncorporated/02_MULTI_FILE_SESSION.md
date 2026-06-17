[MULTI_FILE_SESSION v1.0]
TRIGGER: task requires 2+ files

PROTOCOL:
1. Output FILE_MANIFEST first — no content yet:
   FILE_MANIFEST:
   - [1] FILENAME_A.md | scope: {description}
   - [2] FILENAME_B.md | scope: {description}
   AWAITING: user confirmation → "proceed"

2. On "proceed": write FILE [1] only using TEMPLATE_01
3. End with: NEXT: [2] FILENAME_B.md | type "next" to continue
4. Repeat per file until manifest exhausted
5. Final line: SESSION_COMPLETE. FILES_WRITTEN: {n}

FORBIDDEN:
- Writing multiple files in one response
- Skipping manifest step
- Adding files not in manifest
