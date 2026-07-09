#!/usr/bin/env python3
"""Deterministic patch executor for Markdown and YAML files.

This script implements several modes (inspect, extract_span, replace_once,
replace_heading_section, front_matter_set, validate_scope, diff) that
conform to the patching process contract defined in the references.

Usage examples:

    python patch_executor.py inspect --file docs/intro.md
    python patch_executor.py replace_once --file docs/intro.md --old "old" --new "new"
    python patch_executor.py replace_heading_section --file docs/usage.md --heading "## Deprecated" --new-section "Replacement text"
    python patch_executor.py front_matter_set --file posts/post.md --front-matter '{"title": "New", "tags": ["a","b"]}'
    python patch_executor.py validate_scope --file docs/intro.md --old "old" --new "new"
    python patch_executor.py diff --file docs/intro.md

The script maintains an `.orig` backup of each modified file to support
validation and diff generation.  It never modifies files outside the current
working directory and refuses operations when the target file is not found
or contains multiple matches.
"""

import argparse
import json
import os
import sys
import difflib
from typing import Tuple, List, Optional, Dict, Any

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None  # YAML operations may not be available


def read_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8', newline='') as f:
        return f.read()


def write_text(path: str, content: str) -> None:
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)


def backup_path(path: str) -> str:
    return path + '.orig'


def ensure_within_root(path: str) -> None:
    # Refuse absolute paths or path traversal
    if os.path.isabs(path) or '..' in os.path.normpath(path).split(os.sep):
        raise ValueError(f"invalid path: {path}. Must be a relative path within the repository root")

    if not os.path.exists(path):
        raise FileNotFoundError(f"file not found: {path}")


def detect_newline_style(text: str) -> str:
    # If CRLF present, return CRLF; otherwise LF
    if '\r\n' in text:
        return '\r\n'
    return '\n'


def find_span_indices(content: str, span: str) -> List[int]:
    indices = []
    start = content.find(span)
    while start != -1:
        indices.append(start)
        start = content.find(span, start + 1)
    return indices


def replace_once(path: str, old: str, new: str) -> None:
    content = read_text(path)
    hits = find_span_indices(content, old)
    if not hits:
        raise ValueError(f"old text not found in {path}")
    if len(hits) > 1:
        raise ValueError(f"old text occurs {len(hits)} times in {path}; expected exactly one")
    # Back up original if not already backed up
    bpath = backup_path(path)
    if not os.path.exists(bpath):
        write_text(bpath, content)
    # Preserve newline style
    newline = detect_newline_style(content)
    updated = content.replace(old, new, 1)
    # Ensure newline style remains consistent
    if newline != '\n':
        updated = updated.replace('\n', newline)
    write_text(path, updated)


def replace_heading_section(path: str, heading: str, new_section: str) -> None:
    content = read_text(path)
    lines = content.splitlines(True)
    # Strip heading for matching
    target = heading.strip()
    # Find indices where the line matches exactly
    matches = [i for i, line in enumerate(lines) if line.strip() == target]
    if not matches:
        raise ValueError(f"heading not found: {heading}")
    if len(matches) > 1:
        raise ValueError(f"heading occurs {len(matches)} times; must be unique")
    start_index = matches[0]
    # Determine heading level by counting leading '#' characters
    level = 0
    stripped = target.lstrip('#')
    level = len(target) - len(stripped)
    # Find end of section
    end_index = len(lines)
    for i in range(start_index + 1, len(lines)):
        line = lines[i]
        if line.lstrip().startswith('#'):
            # compute level of this heading
            l = 0
            j = 0
            while j < len(line) and line[j] == '#':
                l += 1
                j += 1
            if l <= level:
                end_index = i
                break
    # Compose new content
    original_newline = detect_newline_style(content)
    # Ensure new_section ends with a newline
    ns = new_section
    if not ns.endswith('\n'):
        ns += original_newline
    replacement_lines = [lines[start_index].rstrip('\n').rstrip('\r') + original_newline, ns]
    new_content_lines = lines[:start_index] + replacement_lines + lines[end_index:]
    new_content = ''.join(new_content_lines)
    # Backup original
    bpath = backup_path(path)
    if not os.path.exists(bpath):
        write_text(bpath, content)
    write_text(path, new_content)


def front_matter_set(path: str, mapping: Dict[str, Any]) -> None:
    if yaml is None:
        raise RuntimeError("PyYAML is required for front_matter_set mode but is not available.")
    content = read_text(path)
    lines = content.splitlines(True)
    if not lines or not lines[0].strip() == '---':
        raise ValueError("file does not start with YAML front matter")
    # find end of front matter
    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_index = i
            break
    if end_index is None:
        raise ValueError("YAML front matter is not closed with a terminating '---'")
    yaml_str = ''.join(lines[1:end_index])
    try:
        data = yaml.safe_load(yaml_str) or {}
    except Exception as e:
        raise ValueError(f"failed to parse YAML: {e}")
    # Update keys
    for k, v in mapping.items():
        data[k] = v
    # Dump YAML preserving key order where possible
    yaml_dump = yaml.safe_dump(data, sort_keys=False).rstrip() + '\n'
    # Compose new content
    original_newline = detect_newline_style(content)
    new_yaml_block = '---' + original_newline + yaml_dump + '---' + original_newline
    new_content = new_yaml_block + ''.join(lines[end_index + 1:])
    # Backup
    bpath = backup_path(path)
    if not os.path.exists(bpath):
        write_text(bpath, content)
    write_text(path, new_content)


def inspect(path: str) -> None:
    content = read_text(path)
    sys.stdout.write(content)


def extract_span(path: str, span: str) -> None:
    content = read_text(path)
    hits = find_span_indices(content, span)
    if not hits:
        raise ValueError("span not found")
    if len(hits) > 1:
        raise ValueError("span appears multiple times; provide a more specific span")
    index = hits[0]
    before = content[:index]
    line_number = before.count('\n') + 1
    sys.stdout.write(f"Found at line {line_number}: {span}\n")


def validate_scope(path: str, old: str, new: str) -> None:
    bpath = backup_path(path)
    if not os.path.exists(bpath):
        raise FileNotFoundError(f"no backup found for {path}; cannot validate scope")
    original = read_text(bpath)
    patched = read_text(path)
    # Ensure new appears and old does not
    if old in patched:
        raise ValueError("validation failed: old text still present in patched file")
    if new not in patched:
        raise ValueError("validation failed: new text not found in patched file")
    # Ensure only expected difference occurs
    diff_lines = list(difflib.unified_diff(original.splitlines(True), patched.splitlines(True)))
    # Consider diff valid if it contains at least one change and does not exceed a small threshold
    if not diff_lines:
        raise ValueError("validation failed: no differences detected")
    # Additional heuristic: no more than 20 changed lines
    changes = [line for line in diff_lines if line.startswith(('+', '-')) and not line.startswith(('+++', '---'))]
    if len(changes) > 20:
        raise ValueError("validation failed: too many lines changed; expected a small scope")
    print("validation succeeded")


def diff(path: str) -> None:
    bpath = backup_path(path)
    if not os.path.exists(bpath):
        raise FileNotFoundError(f"no backup found for {path}; cannot compute diff")
    original = read_text(bpath)
    patched = read_text(path)
    diff_lines = difflib.unified_diff(
        original.splitlines(True), patched.splitlines(True), fromfile=path + '.orig', tofile=path
    )
    sys.stdout.writelines(diff_lines)


def parse_front_matter_arg(arg: str) -> Dict[str, Any]:
    # Accept JSON or YAML mapping in command line
    try:
        return json.loads(arg)
    except json.JSONDecodeError:
        if yaml is None:
            raise
        return yaml.safe_load(arg)


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Deterministic patch executor")
    subparsers = parser.add_subparsers(dest='mode', required=True)

    # inspect
    p_inspect = subparsers.add_parser('inspect', help='Inspect a file')
    p_inspect.add_argument('--file', required=True, dest='path')

    # extract_span
    p_extract = subparsers.add_parser('extract_span', help='Extract span from file')
    p_extract.add_argument('--file', required=True, dest='path')
    p_extract.add_argument('--span', required=True)

    # replace_once
    p_replace = subparsers.add_parser('replace_once', help='Replace exactly one occurrence of old text')
    p_replace.add_argument('--file', required=True, dest='path')
    p_replace.add_argument('--old', required=True)
    p_replace.add_argument('--new', required=True)

    # replace_heading_section
    p_replace_section = subparsers.add_parser('replace_heading_section', help='Replace a section under a heading')
    p_replace_section.add_argument('--file', required=True, dest='path')
    p_replace_section.add_argument('--heading', required=True)
    p_replace_section.add_argument('--new-section', required=True, dest='new_section')

    # front_matter_set
    p_fm = subparsers.add_parser('front_matter_set', help='Set YAML front matter values')
    p_fm.add_argument('--file', required=True, dest='path')
    p_fm.add_argument('--front-matter', required=True, dest='fm')

    # validate_scope
    p_validate = subparsers.add_parser('validate_scope', help='Validate that only the intended change occurred')
    p_validate.add_argument('--file', required=True, dest='path')
    p_validate.add_argument('--old', required=True)
    p_validate.add_argument('--new', required=True)

    # diff
    p_diff = subparsers.add_parser('diff', help='Show unified diff between original and patched file')
    p_diff.add_argument('--file', required=True, dest='path')

    args = parser.parse_args(argv)
    mode = args.mode
    path = args.path

    # Ensure within root
    ensure_within_root(path)

    try:
        if mode == 'inspect':
            inspect(path)
        elif mode == 'extract_span':
            extract_span(path, args.span)
        elif mode == 'replace_once':
            replace_once(path, args.old, args.new)
        elif mode == 'replace_heading_section':
            replace_heading_section(path, args.heading, args.new_section)
        elif mode == 'front_matter_set':
            fm_mapping = parse_front_matter_arg(args.fm)
            if not isinstance(fm_mapping, dict):
                raise ValueError("front_matter must be a mapping")
            front_matter_set(path, fm_mapping)
        elif mode == 'validate_scope':
            validate_scope(path, args.old, args.new)
        elif mode == 'diff':
            diff(path)
        else:
            parser.error(f"Unknown mode: {mode}")
    except Exception as e:
        # Print error to stderr and exit with nonzero
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()