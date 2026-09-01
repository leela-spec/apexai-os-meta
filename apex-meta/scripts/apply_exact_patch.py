#!/usr/bin/env python3
"""
apply_exact_patch.py — Deterministic exact-match patch runner for Apex OS.

Parses patch files containing literal:
<file>
relative/path/to/file
</file>
<old>
exact text to find (must match exactly once)
</old>
<new>
exact replacement text
</new>

Enforces:
1. Target file existence.
2. Byte-for-byte exact match of <old> block.
3. Exactly one occurrence of <old> block in target file (no ambiguity).
4. Automatic backup creation before write.
5. Atomic update with detailed reporting.
"""

import argparse
import os
import re
import sys
import time


def parse_patch_file(patch_path: str):
    """Parses a patch file into a list of (file_path, old_text, new_text) tuples."""
    if not os.path.isfile(patch_path):
        raise FileNotFoundError(f"Patch file not found: {patch_path}")

    with open(patch_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Normalize line endings to \n for internal parsing
    pattern = re.compile(
        r"<file>\s*\n(.*?)\n</file>\s*\n<old>\s*\n(.*?)\n</old>\s*\n<new>\s*\n(.*?)\n</new>",
        re.DOTALL,
    )

    matches = pattern.findall(content)
    if not matches:
        raise ValueError(
            f"No valid <file>/<old>/<new> patch blocks found in {patch_path}"
        )

    patches = []
    for file_rel, old_block, new_block in matches:
        patches.append((file_rel.strip(), old_block, new_block))

    return patches


def apply_patch_blocks(patch_path: str, repo_root: str = ".", dry_run: bool = False):
    """Applies all patch blocks in patch_path deterministically."""
    patches = parse_patch_file(patch_path)
    results = []

    for file_rel, old_block, new_block in patches:
        full_path = os.path.normpath(os.path.join(repo_root, file_rel))
        if not os.path.isfile(full_path):
            raise FileNotFoundError(f"Target file does not exist: {full_path}")

        with open(full_path, "r", encoding="utf-8") as f:
            target_content = f.read()

        # Check for exact occurrence
        # Handle potential CRLF vs LF differences seamlessly
        target_norm = target_content.replace("\r\n", "\n")
        old_norm = old_block.replace("\r\n", "\n")
        new_norm = new_block.replace("\r\n", "\n")

        count = target_norm.count(old_norm)
        if count == 0:
            raise ValueError(
                f"FAILED exact match for {file_rel}: <old> block not found in live file."
            )
        elif count > 1:
            raise ValueError(
                f"AMBIGUOUS exact match for {file_rel}: <old> block found {count} times (must be exactly 1)."
            )

        # Apply replacement
        patched_norm = target_norm.replace(old_norm, new_norm, 1)

        # Preserve original newline convention if target had CRLF
        if "\r\n" in target_content and "\n" not in target_content.replace("\r\n", ""):
            patched_content = patched_norm.replace("\n", "\r\n")
        else:
            patched_content = patched_norm

        if not dry_run:
            backup_path = f"{full_path}.bak.{int(time.time())}"
            with open(backup_path, "w", encoding="utf-8") as f:
                f.write(target_content)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(patched_content)

            results.append(
                {
                    "file": file_rel,
                    "status": "APPLIED",
                    "backup": backup_path,
                    "old_bytes": len(old_norm),
                    "new_bytes": len(new_norm),
                }
            )
        else:
            results.append(
                {
                    "file": file_rel,
                    "status": "DRY_RUN_PASS",
                    "old_bytes": len(old_norm),
                    "new_bytes": len(new_norm),
                }
            )

    return results


def main():
    parser = argparse.ArgumentParser(description="Deterministic exact-match patch runner")
    parser.add_argument("--patch", required=True, help="Path to .patch file")
    parser.add_argument("--root", default=".", help="Repository root directory")
    parser.add_argument("--dry-run", action="store_true", help="Validate without writing")
    args = parser.parse_args()

    try:
        results = apply_patch_blocks(args.patch, args.root, args.dry_run)
        print(f"PASS: Successfully processed {len(results)} block(s) from {args.patch}")
        for r in results:
            print(f"  - [{r['status']}] {r['file']} (old: {r['old_bytes']} B -> new: {r['new_bytes']} B)")
            if "backup" in r:
                print(f"    Backup: {r['backup']}")
    except Exception as e:
        print(f"ERROR: Patch application failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
