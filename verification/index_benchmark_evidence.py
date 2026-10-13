"""Deterministic complete C0–C13 index verification for the MDPAR-docs evidence snapshot.

Preserves source-provided instrument and version metadata; never fabricates labels
for non-C13 evidence. Uses the MDPAR v2.3.0 index contract (V3).
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path


def build_index(runs_root: Path, previous: Path | None = None) -> dict:
    runs_root = Path(runs_root)
    previous = previous or runs_root / 'index.json'
    old = json.loads(Path(previous).read_text(encoding='utf-8'))
    if old.get('schema') != 'MDPAR_BENCHMARK_EVIDENCE_INDEX_V3':
        raise ValueError('Expected V3 evidence index; refuse silent schema migration')
    prior = {entry['path']: entry for entry in old['files']}
    files = []
    for path in sorted((runs_root / 'capabilities').rglob('*')):
        if not path.is_file():
            continue
        parts = path.relative_to(runs_root / 'capabilities').parts
        cap = parts[0]
        if cap == 'C13.previous' or cap.startswith('c13-build-'):
            continue
        if cap not in {f'C{i}' for i in range(14)}:
            raise ValueError(f'Unexpected capability directory: {cap}')
        rel = path.relative_to(runs_root).as_posix()
        if cap == 'C13':
            instrument = ('algorithm-experiments' if rel.startswith('capabilities/C13/batches/algorithms/')
                else 'scientific-protocol' if rel.startswith('capabilities/C13/batches/science/')
                else 'regression' if rel.startswith('capabilities/C13/batches/regression/')
                else 'evidence-ledger')
            entry = {'path': rel, 'capability': cap, 'mdpar_version': '2.3.0', 'instrument': instrument}
        else:
            if rel not in prior:
                raise ValueError(f'Unindexed non-C13 evidence requires provenance review: {rel}')
            entry = {key: prior[rel][key] for key in ('path','capability','mdpar_version','instrument')}
        raw = path.read_bytes()
        entry.update(size_bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        files.append(entry)
    caps = {}
    for entry in files:
        info = caps.setdefault(entry['capability'], {'file_count': 0, 'versions': set(), 'instruments': set()})
        info['file_count'] += 1
        info['versions'].add(entry['mdpar_version'])
        info['instruments'].add(entry['instrument'])
    summaries = {cap: {'file_count': info['file_count'], 'versions': sorted(info['versions']),
                        'instruments': sorted(info['instruments'])}
                 for cap,info in sorted(caps.items(), key=lambda item: int(item[0][1:]))}
    return {'schema': old['schema'], 'capability_range': 'C0-C13',
            'artifact_policy': 'One authoritative C13 evidence tree; every listed hash is computed from current file bytes.',
            'capabilities': summaries, 'files': files}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--runs-root', default='runs')
    parser.add_argument('--output')
    parser.add_argument('--check-existing', action='store_true')
    args = parser.parse_args()
    root = Path(args.runs_root)
    output = Path(args.output) if args.output else root/'index.json'
    result = json.dumps(build_index(root, output), indent=2, ensure_ascii=False) + '\n'
    if args.check_existing:
        if output.read_text(encoding='utf-8') != result:
            raise SystemExit('evidence index is not reproducible from current runs tree')
        print('evidence_index_rebuild=PASS')
    else:
        output.write_text(result, encoding='utf-8')
        print(f'indexed_files={len(json.loads(result)["files"])}')

if __name__ == '__main__':
    main()
