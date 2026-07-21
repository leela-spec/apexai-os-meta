from __future__ import annotations

import json
from pathlib import Path

import yaml
from click.testing import CliRunner

from apex_kb.cli import cli
from apex_kb.core import absolute_string, canonical_hash, template


def setup(tmp_path: Path):
    source = tmp_path / 'leela'; destination = tmp_path / 'apex'
    corpus = source / 'LeelaAppDevelopment'; corpus.mkdir(parents=True); destination.mkdir()
    (corpus / 'skill-tree.md').write_text('# Skill Tree\nEpic, Block, Chunk.\n', encoding='utf-8')
    (corpus / 'diagram.png').write_bytes(b'png')
    config = {
        'source': {'repository': 'leela-spec/leela', 'root': str(source), 'folders': ['LeelaAppDevelopment']},
        'destination': {'repository': 'leela-spec/apexai-os-meta', 'root': str(destination), 'folder': 'apex-meta/kb/leela'},
        'exclusions': [],
        'topics': [{'name': 'Skill Tree', 'phrases': ['skill tree'], 'ambiguous_or_negative_terms': ['tree'], 'questions': ['What is the current Skill Tree and what does it own?']}],
        'run_options': {'source_handling': 'pointer_only', 'semantic_depth': 'standard', 'output': 'query_ready', 'non_text': 'inventory_and_report', 'ai_help_after_preflight': False},
    }
    draft = tmp_path / 'run-config.yaml'; draft.write_text(yaml.safe_dump(config, sort_keys=False), encoding='utf-8')
    return config, draft, corpus, destination / 'apex-meta/kb/leela'


def start(runner: CliRunner, draft: Path):
    return runner.invoke(cli, ['start', '--config', str(draft), '--non-interactive', '--yes', '--json-output'])


def packet(tmp_path: Path):
    runner = CliRunner(); config, draft, corpus, root = setup(tmp_path)
    assert start(runner, draft).exit_code == 0
    assert runner.invoke(cli, ['continue', '--run-root', str(root), '--json-output']).exit_code == 0
    assert runner.invoke(cli, ['continue', '--run-root', str(root), '--json-output']).exit_code == 0
    manifest = json.loads((root / 'run-manifest.json').read_text())
    state = json.loads((root / 'run-state.json').read_text())
    task_dir = Path(state['artifact_references']['semantic_task'])
    task = json.loads((task_dir / 'task.json').read_text())
    return runner, root, manifest, state, task_dir, task, corpus


def semantic_result(manifest, task):
    return {
        'schema': 'apex.kb.semantic-result.v1', 'run_id': manifest['run_id'], 'config_hash': manifest['config_hash'],
        'task_id': task['task_id'], 'phase': 'phase1_source_grounded_analysis', 'topic': 'Skill Tree',
        'source_reviews': [{'path': task['source_paths'][0], 'disposition': 'core', 'summary': 'Defines the hierarchy.'}],
        'synthesis': {'macro': 'Navigation.', 'meso': 'Learning structure.', 'micro': 'Epic, Block, Chunk.'},
        'contradictions': [], 'uncertainties': [],
        'citations': [{'source_path': task['source_paths'][0], 'pointer': '# Skill Tree'}],
    }


def test_start_first_output_is_canonical_template(tmp_path):
    _, draft, _, _ = setup(tmp_path)
    assert start(CliRunner(), draft).output.startswith(template('start-qa-option-a-v3-example-guidance.md'))


def test_start_template_matches_approved_runtime_asset():
    asset = template('start-qa-option-a-v3-example-guidance.md')
    assert asset.startswith('# Apex KB Start Q&A — Option A v3')
    assert 'render_policy: fixed_verbatim' in asset and 'Velvet Vice' in asset


def test_start_requests_only_missing_fields(tmp_path):
    config, draft, _, root = setup(tmp_path); del config['run_options']['semantic_depth']
    draft.write_text(yaml.safe_dump(config, sort_keys=False), encoding='utf-8')
    result = CliRunner().invoke(cli, ['start', '--config', str(draft), '--yes'], input='standard\n')
    assert result.exit_code == 0 and 'Semantic depth' in result.output and 'Source repository' not in result.output
    assert yaml.safe_load((root / 'run-config.yaml').read_text())['run_options']['semantic_depth'] == 'standard'


def test_start_accepts_windows_absolute_paths():
    assert absolute_string('C:/GitDev/leela') and absolute_string(r'C:\GitDev\apexai-os-meta')


def test_preview_writes_nothing(tmp_path):
    _, draft, _, root = setup(tmp_path)
    result = CliRunner().invoke(cli, ['start', '--config', str(draft), '--non-interactive'], input='n\n')
    assert result.exit_code == 0 and not root.exists()


def test_confirmation_creates_manifest_and_reproducible_hash(tmp_path):
    config, draft, _, root = setup(tmp_path); assert start(CliRunner(), draft).exit_code == 0
    manifest = json.loads((root / 'run-manifest.json').read_text())
    assert manifest['config_hash'] == canonical_hash(config)
    assert (root / 'run-config.yaml').is_file() and (root / 'run-state.json').is_file()


def test_status_and_interrupted_resume_use_files_only(tmp_path):
    _, draft, _, root = setup(tmp_path); runner = CliRunner(); start(runner, draft)
    runner.invoke(cli, ['continue', '--run-root', str(root), '--json-output'])
    result = CliRunner().invoke(cli, ['status', '--run-root', str(root), '--json-output'])
    assert json.loads(result.output)['data']['current_stage'] == 'inventory_complete'
    assert not list(root.glob('.run-state.json.*.tmp'))


def test_invalid_state_does_not_advance(tmp_path):
    _, draft, _, root = setup(tmp_path); start(CliRunner(), draft)
    path = root / 'run-state.json'; state = json.loads(path.read_text()); state['next_legal_stage'] = 'teleport'; path.write_text(json.dumps(state))
    before = path.read_bytes(); result = CliRunner().invoke(cli, ['continue', '--run-root', str(root), '--json-output'])
    assert result.exit_code == 2 and path.read_bytes() == before


def test_semantic_packet_contains_exact_questions_and_allowlist(tmp_path):
    _, _, _, _, task_dir, task, _ = packet(tmp_path)
    assert task['target_questions'] == ['What is the current Skill Tree and what does it own?']
    assert json.loads((task_dir / 'source-allowlist.json').read_text())['paths'] == task['source_paths']
    assert any(path.endswith('skill-tree.md') for path in task['source_paths']) and not any(path.endswith('diagram.png') for path in task['source_paths'])


def test_invalid_semantic_result_produces_bounded_repair(tmp_path):
    runner, root, _, state, _, _, _ = packet(tmp_path); incoming = Path(state['expected_semantic_result']); incoming.parent.mkdir(parents=True, exist_ok=True); incoming.write_text('{}')
    assert runner.invoke(cli, ['continue', '--run-root', str(root), '--json-output']).exit_code == 2
    repair = json.loads(incoming.with_suffix('.repair.json').read_text())
    assert 'Do not edit manifests or state' in repair['message']


def test_semantic_worker_cannot_update_run_state(tmp_path):
    runner, root, manifest, state, _, task, _ = packet(tmp_path); path = root / 'run-state.json'; before = path.read_bytes()
    value = semantic_result(manifest, task); value['next_stage'] = 'completed'; incoming = Path(state['expected_semantic_result']); incoming.parent.mkdir(parents=True, exist_ok=True); incoming.write_text(json.dumps(value))
    assert runner.invoke(cli, ['continue', '--run-root', str(root), '--json-output']).exit_code == 2 and path.read_bytes() == before


def test_valid_import_postflight_and_source_mutation_check(tmp_path):
    runner, root, manifest, state, _, task, corpus = packet(tmp_path); before = (corpus / 'skill-tree.md').read_bytes()
    incoming = Path(state['expected_semantic_result']); incoming.parent.mkdir(parents=True, exist_ok=True); incoming.write_text(json.dumps(semantic_result(manifest, task)))
    assert runner.invoke(cli, ['continue', '--run-root', str(root), '--json-output']).exit_code == 0
    assert runner.invoke(cli, ['continue', '--run-root', str(root), '--json-output']).exit_code == 0
    final = json.loads((root / 'run-state.json').read_text())
    assert final['current_stage'] == 'v1_canary_complete' and (corpus / 'skill-tree.md').read_bytes() == before
