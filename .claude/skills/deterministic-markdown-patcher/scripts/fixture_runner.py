#!/usr/bin/env python3
"""Run deterministic patch fixtures.

The fixture runner executes a sequence of patching steps defined in a
JSON file.  Each step corresponds to a mode supported by
`patch_executor.py`.  After running a step the runner may perform
simple assertions based on the fixture definition (e.g., expected
diff snippets or expected output strings).  If any assertion fails
or a step raises an exception, the runner exits with a non‑zero
status code.
"""

import json
import sys
import io
import contextlib
from typing import Dict, Any, List

try:
    # Import the patch executor as a module
    import deterministic_markdown_patcher.scripts.patch_executor as patch_executor  # type: ignore
except Exception:
    # Fallback to relative import when executed from repository root
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "patch_executor", 
        __file__.replace('fixture_runner.py', 'patch_executor.py')
    )
    patch_executor = importlib.util.module_from_spec(spec)  # type: ignore
    spec.loader.exec_module(patch_executor)  # type: ignore


def capture_output(argv: List[str]) -> str:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        try:
            patch_executor.main(argv)
        except SystemExit as e:
            if e.code != 0:
                raise RuntimeError(f"patch_executor exited with status {e.code}")
    return buf.getvalue()


def run_step(step: Dict[str, Any]) -> None:
    mode = step['mode']
    path = step['target_file']
    argv = [mode, '--file', path]
    # Add mode‑specific arguments
    if mode == 'replace_once':
        argv += ['--old', step['old_text'], '--new', step['new_text']]
    elif mode == 'replace_heading_section':
        argv += ['--heading', step['heading'], '--new-section', step['new_section']]
    elif mode == 'front_matter_set':
        fm_json = json.dumps(step['front_matter'])
        argv += ['--front-matter', fm_json]
    elif mode == 'extract_span':
        argv += ['--span', step['old_text']]
    elif mode in ('validate_scope', 'diff'):
        # Additional arguments may be provided
        if 'old_text' in step:
            argv += ['--old', step['old_text']]
        if 'new_text' in step:
            argv += ['--new', step['new_text']]
    # Execute the step and capture output
    output = capture_output(argv)
    # Assertions
    if 'expected_output' in step:
        if step['expected_output'] not in output:
            raise AssertionError(f"expected output not found: {step['expected_output']}")
    if 'expected_diff' in step:
        # Run diff and check for expected snippet
        diff_output = capture_output(['diff', '--file', path])
        if step['expected_diff'] not in diff_output:
            raise AssertionError(f"expected diff snippet not found: {step['expected_diff']}")


def run_fixture(spec: Dict[str, Any]) -> None:
    for step in spec.get('steps', []):
        run_step(step)


def main(argv: List[str]) -> None:
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <fixture.json>")
        sys.exit(1)
    fixture_path = argv[1]
    with open(fixture_path, 'r', encoding='utf-8') as f:
        spec = json.load(f)
    try:
        run_fixture(spec)
    except Exception as e:
        sys.stderr.write(f"Fixture failed: {e}\n")
        sys.exit(1)
    print("Fixture passed")


if __name__ == '__main__':
    main(sys.argv)