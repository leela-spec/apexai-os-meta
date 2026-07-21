from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import click

from .core import ApexKBError, atomic_json, atomic_yaml, create_manifest, import_semantic, initial_state, inventory, load_run, load_yaml, make_packet, preview, save_state, template, validate


def emit(command: str, status: str, data: Any = None, error: ApexKBError | None = None, json_output: bool = False) -> None:
    envelope: dict[str, Any] = {'schema': 'apex.kb.result.v1', 'command': command, 'status': status}
    if data is not None:
        envelope['data'] = data
    if error is not None:
        envelope['error'] = {'code': error.code, 'message': error.message, 'details': error.details}
    if json_output:
        click.echo(json.dumps(envelope, indent=2, ensure_ascii=False, sort_keys=True))
    elif error:
        click.echo(f"ERROR [{error.code}]: {error.message}", err=True)
    elif data is not None:
        click.echo(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))


def abort(command: str, error: ApexKBError, json_output: bool) -> None:
    emit(command, 'error', error=error, json_output=json_output)
    raise click.exceptions.Exit(2)


def csv_prompt(label: str, current: list[str] | None = None) -> list[str]:
    default = ', '.join(current or []) or None
    raw = click.prompt(label, default=default, show_default=default is not None)
    return [part.strip() for part in raw.split(',') if part.strip()]


def complete_missing(config: dict[str, Any]) -> dict[str, Any]:
    source = config.setdefault('source', {})
    if not source.get('repository'):
        source['repository'] = click.prompt('Source repository (owner/name)')
    if not source.get('root'):
        source['root'] = click.prompt('Absolute source repository root')
    if not source.get('folders'):
        source['folders'] = csv_prompt('Source folders, comma-separated')
    destination = config.setdefault('destination', {})
    if not destination.get('repository'):
        destination['repository'] = click.prompt('Destination repository (owner/name)')
    if not destination.get('root'):
        destination['root'] = click.prompt('Absolute destination repository root')
    if not destination.get('folder'):
        destination['folder'] = click.prompt('Destination folder, relative to destination root')
    config.setdefault('exclusions', [])
    if not config.get('topics'):
        config['topics'] = [{'name': click.prompt('First topic name'), 'phrases': csv_prompt('Strong topic phrases, comma-separated'), 'ambiguous_or_negative_terms': [], 'questions': csv_prompt('Target questions, comma-separated')}]
    options = config.setdefault('run_options', {})
    if not options.get('source_handling'):
        options['source_handling'] = click.prompt('Source handling', type=click.Choice(['pointer_only', 'copy_into_kb', 'snapshot_copy']), default='pointer_only')
    if not options.get('semantic_depth'):
        options['semantic_depth'] = click.prompt('Semantic depth', type=click.Choice(['quick', 'standard', 'deep']), default='standard')
    if not options.get('output'):
        options['output'] = click.prompt('Output', type=click.Choice(['analysis_only', 'compiled_kb', 'query_ready']), default='query_ready')
    if not options.get('non_text'):
        options['non_text'] = click.prompt('Non-text policy', type=click.Choice(['inventory_and_report', 'extract_when_supported', 'block_on_unsupported']), default='inventory_and_report')
    options.setdefault('ai_help_after_preflight', False)
    return config


def next_action(run_root: Path, state: dict[str, Any]) -> str:
    stage = state['next_legal_stage']
    if stage in {'inventory', 'semantic_packet', 'postflight'}:
        return f'apex-kb continue --run-root "{run_root}"'
    if stage == 'semantic_import':
        return f'Place the result at "{state["expected_semantic_result"]}" then run apex-kb continue --run-root "{run_root}"'
    return 'No further action; run completed.'


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli() -> None:
    """Apex KB deterministic lifecycle with bounded semantic workers."""


@cli.command()
@click.option('--config', 'config_path', type=click.Path(path_type=Path))
@click.option('--yes', is_flag=True)
@click.option('--non-interactive', is_flag=True)
@click.option('--json-output', is_flag=True)
def start(config_path: Path | None, yes: bool, non_interactive: bool, json_output: bool) -> None:
    """Render the canonical template, preview, confirm, and initialize."""
    click.echo(template('start-qa-option-a-v3-example-guidance.md'), nl=False)
    try:
        config = load_yaml(config_path) if config_path else {}
        if non_interactive:
            validate(config, 'run-config.schema.json')
        else:
            config = complete_missing(config)
        run_root, sources, readback = preview(config)
        click.echo('\n# Apex KB deterministic readback')
        click.echo(json.dumps(readback, indent=2, ensure_ascii=False, sort_keys=True))
        if not (yes or click.confirm('Create the frozen manifest and initial state?', default=False)):
            emit('start', 'ok', {'status': 'preview_only', 'run_root': str(run_root), 'readback': readback}, json_output=json_output)
            return
        if (run_root / 'run-manifest.json').exists() or (run_root / 'run-state.json').exists():
            raise ApexKBError('run_exists', f'A run already exists at {run_root}')
        manifest = create_manifest(config, run_root, sources)
        state = initial_state(manifest)
        run_root.mkdir(parents=True, exist_ok=True)
        atomic_yaml(run_root / 'run-config.yaml', config)
        atomic_json(run_root / 'run-manifest.json', manifest)
        atomic_json(run_root / 'run-state.json', state)
        emit('start', 'ok', {'status': 'initialized', 'run_root': str(run_root), 'run_id': manifest['run_id'], 'config_hash': manifest['config_hash'], 'next_action': next_action(run_root, state)}, json_output=json_output)
    except ApexKBError as exc:
        abort('start', exc, json_output)


@cli.command()
@click.option('--run-root', type=click.Path(path_type=Path, exists=True, file_okay=False), required=True)
@click.option('--json-output', is_flag=True)
def status(run_root: Path, json_output: bool) -> None:
    """Reconstruct status from durable files only."""
    try:
        manifest, state = load_run(run_root.resolve())
        data = {'run_id': manifest['run_id'], 'source': manifest['source'], 'destination': manifest['destination'], 'current_stage': state['current_stage'], 'completed_stages': state['completed_stages'], 'current_blocker': state['blocked_reason'], 'expected_semantic_result': state['expected_semantic_result'], 'exact_next_action': next_action(run_root.resolve(), state)}
        emit('status', 'ok', data, json_output=json_output)
    except ApexKBError as exc:
        abort('status', exc, json_output)


@cli.command(name='continue')
@click.option('--run-root', type=click.Path(path_type=Path, exists=True, file_okay=False), required=True)
@click.option('--json-output', is_flag=True)
def continue_command(run_root: Path, json_output: bool) -> None:
    """Execute the only legal next deterministic action."""
    run_root = run_root.resolve()
    try:
        manifest, state = load_run(run_root)
        stage = state['next_legal_stage']
        if stage == 'inventory':
            result = inventory(run_root, manifest)
            state['current_stage'] = 'inventory_complete'; state['completed_stages'].append('inventory'); state['next_legal_stage'] = 'semantic_packet'; state['artifact_references']['inventory'] = result['summary']['inventory_path']
            save_state(run_root, state)
            data = {'stage': 'inventory', 'result': result['summary'], 'next_action': next_action(run_root, state)}
        elif stage == 'semantic_packet':
            inventory_path = run_root / state['artifact_references']['inventory']
            rows = [json.loads(line) for line in inventory_path.read_text(encoding='utf-8').splitlines() if line.strip()]
            packet = make_packet(run_root, manifest, rows)
            state['current_stage'] = 'awaiting_semantic_result'; state['next_legal_stage'] = 'semantic_import'; state['expected_semantic_result'] = packet['incoming']; state['artifact_references']['semantic_task'] = packet['packet_dir']
            save_state(run_root, state)
            data = {'stage': 'semantic_packet', **packet, 'next_action': next_action(run_root, state)}
        elif stage == 'semantic_import':
            imported = import_semantic(run_root, manifest)
            state['current_stage'] = 'semantic_result_imported'; state['completed_stages'] += ['semantic_packet', 'semantic_import']; state['next_legal_stage'] = 'postflight'; state['expected_semantic_result'] = None; state['artifact_references']['semantic_result'] = imported['result_path']
            save_state(run_root, state)
            data = {'stage': 'semantic_import', **imported, 'next_action': next_action(run_root, state)}
        elif stage == 'postflight':
            acceptance = Path(state['artifact_references']['semantic_result']).with_suffix('.acceptance.json')
            if not acceptance.is_file():
                raise ApexKBError('acceptance_missing', f'Structural acceptance artifact is missing: {acceptance}')
            result = {'schema': 'apex.kb.stage-result.v1', 'run_id': manifest['run_id'], 'config_hash': manifest['config_hash'], 'stage': 'postflight', 'status': 'completed', 'started_at': state['updated_at'], 'completed_at': state['updated_at'], 'artifacts': [str(acceptance.relative_to(run_root))], 'reason_code': None, 'message': 'V1 structural postflight complete; independent semantic acceptance and retrieval remain future work.'}
            validate(result, 'stage-result.schema.json'); atomic_json(run_root / manifest['artifact_layout']['stage_results'] / 'postflight.json', result)
            state['current_stage'] = 'v1_canary_complete'; state['completed_stages'].append('postflight'); state['next_legal_stage'] = 'completed'; save_state(run_root, state)
            data = {'stage': 'postflight', 'status': 'v1_canary_complete', 'next_action': next_action(run_root, state)}
        elif stage == 'completed':
            data = {'stage': 'completed', 'next_action': next_action(run_root, state)}
        else:
            raise ApexKBError('illegal_next_stage', f'Unsupported next_legal_stage: {stage}')
        emit('continue', 'ok', data, json_output=json_output)
    except ApexKBError as exc:
        abort('continue', exc, json_output)


def main() -> None:
    try:
        cli(standalone_mode=True)
    except BrokenPipeError:
        sys.exit(1)


if __name__ == '__main__':
    main()
