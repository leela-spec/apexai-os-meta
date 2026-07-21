from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import re
import shutil
import tempfile
from datetime import datetime, timezone
from importlib import resources
from pathlib import Path, PureWindowsPath
from typing import Any

import yaml
from jsonschema import Draft202012Validator


class ApexKBError(RuntimeError):
    def __init__(self, code: str, message: str, details: Any | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def canonical_hash(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()


def slug(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', value.strip().lower()).strip('-') or 'topic'


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=f'.{path.name}.', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        try:
            os.unlink(temp)
        except FileNotFoundError:
            pass


def atomic_json(path: Path, value: Any) -> None:
    atomic_text(path, json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + '\n')


def atomic_yaml(path: Path, value: Any) -> None:
    atomic_text(path, yaml.safe_dump(value, sort_keys=False, allow_unicode=True))


def schema(name: str) -> dict[str, Any]:
    return json.loads(resources.files('apex_kb.schemas').joinpath(name).read_text(encoding='utf-8'))


def template(name: str) -> str:
    return resources.files('apex_kb.templates').joinpath(name).read_text(encoding='utf-8')


def validate(value: Any, name: str) -> None:
    errors = sorted(Draft202012Validator(schema(name)).iter_errors(value), key=lambda e: list(e.absolute_path))
    if errors:
        rendered = [f"{'.'.join(map(str, e.absolute_path)) or '$'}: {e.message}" for e in errors[:20]]
        raise ApexKBError('schema_validation_failed', '; '.join(rendered), rendered)


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ApexKBError('config_missing', f'Configuration file does not exist: {path}')
    try:
        value = yaml.safe_load(path.read_text(encoding='utf-8-sig'))
    except Exception as exc:
        raise ApexKBError('config_invalid_yaml', f'Invalid YAML: {exc}') from exc
    if not isinstance(value, dict):
        raise ApexKBError('config_root_invalid', 'Configuration root must be a mapping')
    return value


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ApexKBError('artifact_missing', f'Required file does not exist: {path}')
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        raise ApexKBError('artifact_invalid_json', f'Invalid JSON in {path}: {exc}') from exc
    if not isinstance(value, dict):
        raise ApexKBError('artifact_root_invalid', f'JSON root must be an object: {path}')
    return value


def absolute_string(value: str) -> bool:
    return Path(value).expanduser().is_absolute() or PureWindowsPath(value).is_absolute()


def within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def overlaps(left: Path, right: Path) -> bool:
    return within(left, right) or within(right, left)


def resolved_paths(config: dict[str, Any]) -> tuple[Path, list[Path]]:
    for key, raw in [('source.root', config['source']['root']), ('destination.root', config['destination']['root'])]:
        if not absolute_string(raw):
            raise ApexKBError('repository_root_not_absolute', f'{key} must be an absolute path: {raw}')
    src_root = Path(config['source']['root']).expanduser().resolve()
    dst_root = Path(config['destination']['root']).expanduser().resolve()
    if not src_root.is_dir():
        raise ApexKBError('source_root_missing', f'Source repository root does not exist: {src_root}')
    if not dst_root.is_dir():
        raise ApexKBError('destination_root_missing', f'Destination repository root does not exist: {dst_root}')
    sources: list[Path] = []
    for raw in config['source']['folders']:
        rel = Path(raw)
        if rel.is_absolute() or '..' in rel.parts:
            raise ApexKBError('source_folder_invalid', f'Source folder must be relative: {raw}')
        value = (src_root / rel).resolve()
        if not within(value, src_root) or not value.is_dir():
            raise ApexKBError('source_folder_missing', f'Source folder does not exist: {value}')
        sources.append(value)
    folder = Path(config['destination']['folder'])
    if folder.is_absolute() or '..' in folder.parts:
        raise ApexKBError('destination_folder_invalid', 'destination.folder must be relative without ..')
    run_root = (dst_root / folder).resolve()
    for source in sources:
        if overlaps(source, run_root):
            raise ApexKBError('source_destination_overlap', f'Source and destination overlap: {source} <-> {run_root}')
    return run_root, sources


def preview(config: dict[str, Any]) -> tuple[Path, list[Path], dict[str, Any]]:
    validate(config, 'run-config.schema.json')
    if config['run_options']['source_handling'] != 'pointer_only':
        raise ApexKBError('source_handling_not_implemented', 'V1 implements pointer_only source handling only.')
    if config['run_options']['non_text'] == 'extract_when_supported':
        raise ApexKBError('non_text_extraction_not_implemented', 'V1 inventories non-text files but does not install extractors.')
    run_root, sources = resolved_paths(config)
    readback = {
        'source': config['source'],
        'destination': config['destination'],
        'exclusions': config.get('exclusions', []),
        'topics': [t['name'] for t in config['topics']],
        'target_questions': [q for t in config['topics'] for q in t['questions']],
        'source_handling': config['run_options']['source_handling'],
        'semantic_depth': config['run_options']['semantic_depth'],
        'output_level': config['run_options']['output'],
        'non_text_policy': config['run_options']['non_text'],
        'planned_files': ['run-config.yaml', 'run-manifest.json', 'run-state.json', 'runs/<run-id>/stage-results/', 'runs/<run-id>/semantic-tasks/', 'runs/<run-id>/incoming/'],
        'warnings': [],
    }
    return run_root, sources, readback


def create_manifest(config: dict[str, Any], run_root: Path, sources: list[Path]) -> dict[str, Any]:
    config_hash = canonical_hash(config)
    run_id = f"run-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{config_hash[:10]}"
    value = {
        'schema': 'apex.kb.run-manifest.v1', 'schema_version': 1, 'run_id': run_id,
        'config_hash': config_hash, 'created_at': now(),
        'source': {**config['source'], 'resolved_root': str(Path(config['source']['root']).resolve()), 'resolved_folders': [str(p) for p in sources]},
        'destination': {**config['destination'], 'resolved_root': str(Path(config['destination']['root']).resolve()), 'resolved_run_root': str(run_root)},
        'exclusions': config.get('exclusions', []), 'topics': config['topics'], 'run_options': config['run_options'],
        'artifact_layout': {'run_dir': f'runs/{run_id}', 'stage_results': f'runs/{run_id}/stage-results', 'semantic_tasks': f'runs/{run_id}/semantic-tasks', 'incoming': f'runs/{run_id}/incoming', 'semantic_results': f'runs/{run_id}/semantic-results'},
    }
    validate(value, 'run-manifest.schema.json')
    return value


def initial_state(manifest: dict[str, Any]) -> dict[str, Any]:
    value = {
        'schema': 'apex.kb.run-state.v1', 'schema_version': 1, 'run_id': manifest['run_id'],
        'config_hash': manifest['config_hash'], 'current_stage': 'setup_confirmed',
        'completed_stages': ['setup_confirmed'], 'blocked_reason': None,
        'expected_semantic_result': None, 'next_legal_stage': 'inventory',
        'artifact_references': {'manifest': 'run-manifest.json', 'config': 'run-config.yaml'}, 'updated_at': now(),
    }
    validate(value, 'run-state.schema.json')
    return value


def load_run(run_root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    manifest, state = load_json(run_root / 'run-manifest.json'), load_json(run_root / 'run-state.json')
    validate(manifest, 'run-manifest.schema.json'); validate(state, 'run-state.schema.json')
    if manifest['run_id'] != state['run_id'] or manifest['config_hash'] != state['config_hash']:
        raise ApexKBError('run_identity_mismatch', 'Manifest and state do not describe the same run')
    return manifest, state


def save_state(run_root: Path, state: dict[str, Any]) -> None:
    state['updated_at'] = now(); validate(state, 'run-state.schema.json'); atomic_json(run_root / 'run-state.json', state)


TEXT_EXT = {'.md', '.markdown', '.txt', '.rst', '.py', '.js', '.ts', '.tsx', '.jsx', '.json', '.yaml', '.yml', '.toml', '.csv'}


def excluded(path: Path, root: Path, rules: list[dict[str, str]]) -> tuple[bool, str | None]:
    rel = path.relative_to(root).as_posix()
    for rule in rules:
        pattern = rule['path'].replace('\\', '/').rstrip('/')
        if rel == pattern or rel.startswith(pattern + '/') or fnmatch.fnmatch(rel, pattern):
            return True, rule['reason']
    return False, None


def inventory(run_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for root_raw in manifest['source']['resolved_folders']:
        root = Path(root_raw)
        for path in sorted(root.rglob('*')):
            if not path.is_file():
                continue
            skip, reason = excluded(path, root, manifest.get('exclusions', []))
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            rows.append({'source_root': str(root), 'path': str(path.resolve()), 'relative_path': path.relative_to(root).as_posix(), 'extension': path.suffix.lower(), 'bytes': path.stat().st_size, 'sha256': digest, 'excluded': skip, 'exclusion_reason': reason, 'text_supported': path.suffix.lower() in TEXT_EXT})
    base = run_root / manifest['artifact_layout']['run_dir'] / 'inventory'
    atomic_text(base / 'source-inventory.ndjson', ''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in rows))
    summary = {'schema': 'apex.kb.inventory-summary.v1', 'run_id': manifest['run_id'], 'config_hash': manifest['config_hash'], 'created_at': now(), 'file_count': len(rows), 'included_count': sum(not r['excluded'] for r in rows), 'excluded_count': sum(r['excluded'] for r in rows), 'unsupported_count': sum((not r['text_supported']) and (not r['excluded']) for r in rows), 'total_bytes': sum(r['bytes'] for r in rows), 'inventory_path': str((base / 'source-inventory.ndjson').relative_to(run_root))}
    atomic_json(base / 'summary.json', summary)
    if manifest['run_options']['non_text'] == 'block_on_unsupported' and summary['unsupported_count']:
        raise ApexKBError('unsupported_files_blocked', f"{summary['unsupported_count']} unsupported in-scope files found.", {'summary_path': str(base / 'summary.json')})
    result = {'schema': 'apex.kb.stage-result.v1', 'run_id': manifest['run_id'], 'config_hash': manifest['config_hash'], 'stage': 'inventory', 'status': 'completed', 'started_at': summary['created_at'], 'completed_at': now(), 'artifacts': [summary['inventory_path'], str((base / 'summary.json').relative_to(run_root))], 'reason_code': None, 'message': f'Inventoried {len(rows)} files without modifying sources.'}
    validate(result, 'stage-result.schema.json'); atomic_json(run_root / manifest['artifact_layout']['stage_results'] / 'inventory.json', result)
    return {'summary': summary, 'rows': rows}


def task_id(manifest: dict[str, Any]) -> str:
    return f"phase1-001-{slug(manifest['topics'][0]['name'])}"


def make_packet(run_root: Path, manifest: dict[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    topic = manifest['topics'][0]; tid = task_id(manifest)
    packet = run_root / manifest['artifact_layout']['semantic_tasks'] / tid
    allow = [r['path'] for r in rows if not r['excluded'] and r['text_supported']]
    incoming = run_root / manifest['artifact_layout']['incoming'] / f'{tid}.json'
    imported = run_root / manifest['artifact_layout']['semantic_results'] / f'{tid}.json'
    task = {'schema': 'apex.kb.semantic-task.v1', 'run_id': manifest['run_id'], 'config_hash': manifest['config_hash'], 'task_id': tid, 'phase': 'phase1_source_grounded_analysis', 'semantic_depth': manifest['run_options']['semantic_depth'], 'topic': topic, 'target_questions': topic['questions'], 'source_allowlist_path': 'source-allowlist.json', 'source_paths': allow, 'stable_template': 'templates/ingest-analysis-template.md', 'allowed_output_paths': [str(incoming)], 'forbidden_writes': ['run-config.yaml', 'run-manifest.json', 'run-state.json', 'runs/*/stage-results/*', 'all source repository paths'], 'required_return_structure': 'output.schema.json', 'stop_conditions': ['Required source missing or unreadable.', 'Run identity mismatch.', 'Output requires a forbidden write.'], 'incoming_path': str(incoming), 'imported_result_path': str(imported), 'created_at': now()}
    validate(task, 'semantic-task.schema.json')
    atomic_json(packet / 'task.json', task); atomic_json(packet / 'source-allowlist.json', {'paths': allow}); atomic_json(packet / 'output.schema.json', schema('semantic-result.schema.json')); atomic_text(packet / 'expected-output-path.txt', str(incoming) + '\n')
    body = template('semantic-task-TASK.md').format(run_id=manifest['run_id'], config_hash=manifest['config_hash'], task_id=tid, topic=topic['name'], questions='\n'.join(f'- {q}' for q in topic['questions']), incoming=str(incoming))
    atomic_text(packet / 'TASK.md', body)
    return {'task': task, 'packet_dir': str(packet), 'incoming': str(incoming)}


def import_semantic(run_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    tid = task_id(manifest); incoming = run_root / manifest['artifact_layout']['incoming'] / f'{tid}.json'
    if not incoming.is_file():
        raise ApexKBError('semantic_result_missing', f'Place the result at {incoming} and continue again.', {'expected_path': str(incoming)})
    value = load_json(incoming)
    try:
        validate(value, 'semantic-result.schema.json')
    except ApexKBError as exc:
        repair = incoming.with_suffix('.repair.json')
        atomic_json(repair, {'schema': 'apex.kb.semantic-repair.v1', 'task_id': tid, 'reason_code': exc.code, 'message': 'Repair only the declared semantic result. Do not edit manifests or state.', 'validation_errors': exc.details, 'expected_path': str(incoming)})
        raise ApexKBError('semantic_result_invalid', exc.message, {'repair_instruction': str(repair)}) from exc
    for key, expected in {'run_id': manifest['run_id'], 'config_hash': manifest['config_hash'], 'task_id': tid}.items():
        if value.get(key) != expected:
            raise ApexKBError('semantic_result_identity_mismatch', f'{key} does not match the run')
    destination = run_root / manifest['artifact_layout']['semantic_results'] / f'{tid}.json'
    destination.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(incoming, destination)
    acceptance = {'schema': 'apex.kb.semantic-acceptance.v1', 'run_id': manifest['run_id'], 'config_hash': manifest['config_hash'], 'task_id': tid, 'verdict': 'structurally_accepted_pending_independent_semantic_acceptance', 'accepted_at': now(), 'result_path': str(destination.relative_to(run_root)), 'notes': ['Structural validation only; independent semantic acceptance remains required.']}
    validate(acceptance, 'semantic-acceptance.schema.json'); atomic_json(destination.with_suffix('.acceptance.json'), acceptance)
    return {'result_path': str(destination), 'acceptance': acceptance}
