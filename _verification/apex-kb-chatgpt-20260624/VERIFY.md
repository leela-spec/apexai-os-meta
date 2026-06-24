# Verification Checklist

1. Check local status:
   ``powershell
   git status --short
   ``
   Expected: only _verification/ changes before commit, or clean after archival.

2. Check backup branch:
   ``powershell
   git rev-parse origin/backup/apex-kb-before-chatgpt-20260624
   ``
   Expected: resolves to a commit SHA.

3. Inspect each audited commit:
   ``powershell
   git show --name-status --oneline --no-renames ac259b632f77d0836aef722b1b640392f623f24d
   ``
   ``powershell
   git show --name-status --oneline --no-renames 96b21e861c738fd2ccb2eaa7abecf509a924a487
   ``
   ``powershell
   git show --name-status --oneline --no-renames daa8e25e1758192ffc9632e9629070a38d7c1d8d
   ``
   ``powershell
   git show --name-status --oneline --no-renames cc9f69ad44280615368877d6234bc3983d7fba54
   ``
   ``powershell
   git show --name-status --oneline --no-renames ae59348c953b9a946638c4bd25f1a1f013e2c064
   ``
   ``powershell
   git show --name-status --oneline --no-renames d5e9dd0eac2ec44797764a3558f5087ff62c503d
   ``
   ``powershell
   git show --name-status --oneline --no-renames 84757a7b0498b76710c78bae0b1e25d48c2bfc48
   ``

   Expected: combined changed file set is exactly the seven Apex KB files in changed-files-ledger.json.

4. Compare exported before/after files:
   ``powershell
   git diff --no-index before/<path> after/<path>
   ``
   Expected: differences match the generated files in diffs/.
