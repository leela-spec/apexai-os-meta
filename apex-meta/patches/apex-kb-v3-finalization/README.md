# Apex KB v3 Finalization Patch Pack

Patch pack root: `apex-meta/patches/apex-kb-v3-finalization/`

Apply from repository root in a full local checkout:

```bash
git apply --check apex-meta/patches/apex-kb-v3-finalization/patches/*.patch
git apply apex-meta/patches/apex-kb-v3-finalization/patches/*.patch
python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py
```

This pack was built from live GitHub connector reads and locally checked in an extracted-context workspace. Re-run full validation in the actual repository before commit.
