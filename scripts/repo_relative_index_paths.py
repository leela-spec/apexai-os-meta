#!/usr/bin/env python3
"""Normalize index navigation to repository-root-relative paths.

Dry run: python scripts/repo_relative_index_paths.py
Apply:   python scripts/repo_relative_index_paths.py --apply
Source snapshots and the moved original brief remain untouched.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit

BUNDLE = "apex-meta/informatics/final/research/11-infrastructure-evidence-index"
OLD = "apex-meta/AI-Snippets/Inbetween_Delete/Untitled 5.md"
NEW = BUNDLE + "/sources/infrastructure-activation-research-brief.md"
LINK = re.compile(r"\]\((?P<target><[^>\r\n]+>|[^)\r\n]+)\)")


def apply_spans(path: Path, original: bytes, edits: list, apply: bool) -> int:
    """Copy untouched bytes exactly; replace only verified, nonoverlapping spans."""
    edits = [edit for edit in edits if edit[2] != edit[3]]
    if not edits:
        return 0
    edits.sort(key=lambda e: e[0])
    previous = 0
    for start, end, old, new in edits:
        if start < previous or original[start:end] != old:
            raise ValueError(f"Conflicting or stale edit in {path}")
        previous = end
    if apply:
        if path.read_bytes() != original:
            raise ValueError(f"File changed during conversion: {path}")
        fd, name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
        try:
            with os.fdopen(fd, "wb") as output:
                previous = 0
                for start, end, old, new in edits:
                    output.write(original[previous:start])
                    output.write(new)
                    previous = end
                output.write(original[previous:])
            os.replace(name, path)
        finally:
            if os.path.exists(name):
                os.unlink(name)
    return len(edits)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--bundle", default=BUNDLE)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.repo_root.resolve()
    bundle = (root / args.bundle).resolve()
    bundle.relative_to(root)
    changed = {}
    unresolved = set()
    root_names = {entry.name for entry in root.iterdir()}

    def repository_path(rel: str) -> str:
        rel = (NEW if rel == OLD else rel).rstrip("/")
        if rel == "scripts/github_index_links.py":
            rel = "scripts/repo_relative_index_paths.py"
        if not rel or rel.startswith("../") or Path(rel).is_absolute():
            raise ValueError(f"Path is outside repository: {rel}")
        return rel

    for path in sorted(bundle.glob("*.md")):
        data = path.read_bytes()
        text = data.decode("utf-8")
        blocked = [(m.start(), m.end()) for m in re.finditer(r"```[\s\S]*?```|`[^`\r\n]*`", text)]
        edits = []
        for match in LINK.finditer(text):
            start, end = match.span("target")
            if any(a <= start < b for a, b in blocked):
                continue
            target = match.group("target").strip().strip("<>")
            if target.startswith("#"):
                continue
            parsed = urlsplit(target.replace("\\", "/"))
            if parsed.scheme and not re.match(r"^[A-Za-z]:[/\\]", target):
                prefix = "/leela-spec/apexai-os-meta/"
                parts = parsed.path[len(prefix):].split("/", 2) if parsed.path.startswith(prefix) else []
                if parsed.netloc != "github.com" or len(parts) != 3 or parts[0] not in ("blob", "tree"):
                    continue
                rel = unquote(parts[2])
            else:
                local = unquote(target.split("#", 1)[0].split("?", 1)[0]) if re.match(r"^[A-Za-z]:[/\\]", target) else unquote(parsed.path)
                candidate = Path(local)
                if not candidate.is_absolute():
                    candidate = (root / candidate) if local.split("/", 1)[0] in root_names else path.parent / candidate
                try:
                    rel = Path(os.path.abspath(candidate)).relative_to(root).as_posix()
                except ValueError:
                    unresolved.add(target)
                    continue
            url = repository_path(rel)
            if parsed.query:
                url += "?" + parsed.query
            if parsed.fragment:
                url += "#" + parsed.fragment
            if any(char.isspace() or char in "()" for char in url):
                url = "<" + url + ">"
            old = text[start:end].encode("utf-8")
            offset = len(text[:start].encode("utf-8"))
            edits.append((offset, offset + len(old), old, url.encode("utf-8")))
        count = apply_spans(path, data, edits, args.apply)
        if count:
            changed[path.relative_to(root).as_posix()] = count

    for filename in ("files.tsv", "decision-evidence.tsv"):
        path = bundle / filename
        data = path.read_bytes()
        lines = data.splitlines(keepends=True)
        headers = next(csv.reader([lines[0].decode("utf-8")], delimiter="\t"))
        if "github_url" not in headers:
            continue
        if headers[-2:] != ["github_url", "online_status_at_conversion"]:
            raise ValueError(f"Unexpected URL column layout in {path}")
        edits = []
        offset = 0
        for line in lines:
            ending = b"\r\n" if line.endswith(b"\r\n") else b"\n" if line.endswith(b"\n") else b""
            content = line[:-len(ending)] if ending else line
            prefix = content.rsplit(b"\t", 2)[0]
            position = offset + len(prefix)
            old = content[len(prefix):]
            edits.append((position, position + len(old), old, b""))
            offset += len(line)
        count = apply_spans(path, data, edits, args.apply)
        if count:
            changed[path.relative_to(root).as_posix()] = count

    print(json.dumps({"applied": args.apply, "changed_spans": changed,
        "unresolved_external_paths": sorted(unresolved)}, indent=2))


if __name__ == "__main__":
    main()
