from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'AGENTS.md',
    'Ego/Ego-rem.md', 'Ego/EdgeTeam.md', 'Ego/Naming.md', 'Ego/Rws.md',
    'Mission/Story-rem.md', 'Mission/EVAL/eval-rem-v1.md',
    'Repo/INTENT.md', 'Repo/today.md', 'Repo/now.md', 'Repo/DONE.md',
    'Repo/Motion/README.md', 'Repo/TeamsPage/README.md', 'Repo/Dojo/README.md',
]


def inspect(repo: Path) -> dict:
    repo = repo.resolve()
    failures = [f'missing:{relative}' for relative in REQUIRED if not (repo / relative).is_file()]
    for name in ('np0', 'rem-ready', 'motioner', 'shaping', 'teamspage'):
        if not (repo / f'.agents/skills/{name}/SKILL.md').is_file():
            failures.append(f'missing-skill:{name}')
    for source in repo.rglob('*.md'):
        if '.git' in source.parts or any(part.casefold() == 'teamspage' for part in source.parts) or source.name == 'np0-axiom-capsule.md':
            continue
        for target in re.findall(r'\]\(([^)]+)\)', source.read_text(encoding='utf-8-sig')):
            if target.startswith(('https://', 'http://', '#')):
                continue
            destination = (source.parent / target.split('#')[0]).resolve()
            if not destination.is_relative_to(repo) or not destination.exists():
                failures.append(f'link:{source.relative_to(repo)}:{target}')
    manifest_path = repo / 'Ego/TeamSkill/source-manifest.json'
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        for field, label in (('unchanged_files', 'pin'), ('target_deltas', 'target-delta')):
            for record in manifest.get(field, []):
                target = repo / record['path']
                if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != record['sha256']:
                    failures.append(f'{label}:{record["path"]}')
    else:
        failures.append('missing:source-manifest')
    return {'structure': 'pass' if not failures else 'fail', 'failures': failures,
            'human_review': 'not_run', 'runtime_models': 'not_run', 'role_alignment': 'not_run'}


def main() -> None:
    parser = argparse.ArgumentParser(description='Inspect target structure and source pins; no acceptance inference')
    parser.add_argument('--repo', type=Path, default=ROOT)
    parser.add_argument('--record-tool', action='store_true')
    parser.add_argument('--actor')
    parser.add_argument('--approval-evidence')
    args = parser.parse_args()
    result = inspect(args.repo)
    if args.record_tool:
        if not args.actor or not args.approval_evidence:
            parser.error('Tool evidence requires actor and explicit approval evidence')
        from datetime import datetime
        import uuid
        evidence = {'schema_version': '1.0', 'actor': args.actor, 'approval_evidence': args.approval_evidence,
                    'mission': 'Mission/Story-rem.md', 'action': 'python scripts/verify.py',
                    'observed_at': datetime.now().astimezone().isoformat(),
                    'source_commit': subprocess.check_output(['git', '-C', str(args.repo), 'rev-parse', 'HEAD'], text=True).strip(),
                    'result': result, 'side_effect': 'new local evidence only; no external tool call',
                    'human_acceptance': 'not_run'}
        destination = args.repo / 'Mission/evidence' / f'tool-{uuid.uuid4().hex}.json'
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open('x', encoding='utf-8', newline='\n') as output:
            output.write(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
        print(destination.relative_to(args.repo).as_posix())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result['failures']:
        parser.exit(1)


if __name__ == '__main__':
    main()
