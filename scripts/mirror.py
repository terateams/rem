from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tomllib
import uuid
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MPS_SCRIPTS = ROOT / '.agents/skills/teamspage/MPS/scripts'
sys.path.insert(0, str(MPS_SCRIPTS))

import mps

REQUIRED = [
    'Ego/Ego-rem.md', 'Ego/EdgeTeam.md', 'Ego/Naming.md', 'Ego/Working.md',
    '.github/copilot-instructions.md', 'Repo/today.md', 'Repo/now.md',
]
SECRET_PATTERN = re.compile(r'github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]+|-----BEGIN [A-Z ]*PRIVATE KEY-----')


def build_request(repo: Path, config: dict, actor: str, approval: str, reviewed: bool) -> dict:
    repo = repo.resolve()
    mps.require(reviewed and bool(actor.strip()) and bool(approval.strip()), 'Explicit permission and source custody review required')
    mps.require(set(config) == {'mission', 'eval', 'title', 'scope', 'sources'}, 'Unexpected request fields')
    mps.require(isinstance(config['sources'], list) and bool(config['sources']), 'Explicit file group required')
    mission, evaluation = config['mission'], config['eval']
    mps.require(isinstance(mission, str) and mission.startswith('Mission/Story-'), 'Invalid Mission binding')
    mps.require(isinstance(evaluation, str) and evaluation.startswith('Mission/EVAL/'), 'Invalid EVAL binding')
    mps.require(all(isinstance(config[key], str) and config[key].strip() for key in ('title', 'scope')), 'Missing title or scope')
    sources = list(dict.fromkeys([*REQUIRED, mission, evaluation, *config['sources']]))
    texts = {}
    for relative in sources:
        mps.require(isinstance(relative, str) and relative.endswith('.md'), 'R1 supports explicit Markdown sources only')
        text = mps.input_source(repo, relative).read_text(encoding='utf-8-sig')
        mps.require(SECRET_PATTERN.search(text) is None, 'Potential credential material; stop custody review')
        texts[relative] = text
    baseline = re.search(r'(?m)^# today - (\d{4}-\d{2}-\d{2})\s*$', texts['Repo/today.md'])
    mps.require(baseline is not None, 'Missing canonical date')
    claims = []
    voice = {}
    for relative in dict.fromkeys([mission, evaluation, *config['sources']]):
        for line in texts[relative].splitlines():
            if line.strip():
                claims.append(line)
                voice[f'claims.{len(claims) - 1}'] = {'kind': 'source_claim', 'source': relative}
    narrative = {
        'title': config['title'],
        'summary': 'Mirror Page: Mission source claims, output evidence and role responsibilities; not acceptance.',
        'claims': claims,
        'unknowns': ['Human review, role alignment and actual Sol/Luna runs require independent evidence.'],
        'decision_rights': actor,
        'next_action': 'Review the original sources; revise authorized content or execute authorized Tools in VSC.',
        'verification_route': 'Compare Agent outputs against the bound Mission EVAL and inspect action evidence.',
    }
    for slot in ('summary', 'unknowns.0', 'decision_rights', 'next_action', 'verification_route'):
        voice[slot] = {'kind': 'rule_marker', 'rule_id': 'rem-mission-review', 'sources': [mission, evaluation, '.github/copilot-instructions.md']}
    observations = {
        name: {'source_claims': [], 'Fact': [], 'Claim': [], 'Credence': 'unknown',
               'unknowns': ['No independent EGO observation supplied by this adapter.'], 'delta': []}
        for name in ('Ego-rem.md', 'EdgeTeam.md', 'Naming.md', 'Working.md')
    }
    structural = subprocess.run(
        [sys.executable, str(repo / 'scripts/verify.py'), '--repo', str(repo)],
        capture_output=True, text=True, encoding='utf-8', check=False, timeout=60,
    )
    request = {
        'snapshot': {
            'schema_version': '1.0', 'run_id': f'rem-{uuid.uuid4().hex[:16]}', 'slug': 'rem',
            'baseline_date': baseline.group(1), 'scope': config['scope'],
            'binding': {'mission': mission, 'eval': evaluation, 'authority': '.github/copilot-instructions.md'},
            'selected_method': None,
            'permission': {'snapshot_write': True, 'teamspage_write': True, 'approved_by': actor,
                           'approval_evidence': approval, 'allowed_sources': sources,
                           'content_reviewed_no_secrets': True},
            'observations': observations,
        },
        'rem_id': 'rem', 'repo_locator': 'terateams/rem',
        'target': {'namespace': 'REM', 'target_kind': 'instance', 'target_ref': 'rem', 'scope': config['scope']},
        'viewpoint': 'mission-output-and-responsibility-review', 'mission_context': mission,
        'narrative': narrative, 'voice_sources': voice, 'distortion_declarations': [],
        'reference_sources': {f'source-{index}': relative for index, relative in enumerate(sources)},
        'gate_evidence': {
            'g_tier': {'command': 'python scripts/verify.py --repo <target>',
                       'exit_code': structural.returncode,
                       'evidence': (structural.stdout + structural.stderr)[-4000:]},
            'g_orphan': {'status': 'not_applicable', 'reason': 'Explicit document group, not an ontology graph.'},
        },
        'source_link_policy': 'local',
    }
    return mps.capture_request(repo, request)


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate the built-in rem Mission Mirror Page')
    parser.add_argument('--repo', type=Path, default=ROOT)
    parser.add_argument('--request', type=Path, required=True)
    parser.add_argument('--approved-by', required=True)
    parser.add_argument('--approval-evidence', required=True)
    parser.add_argument('--content-reviewed', action='store_true')
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--previous', type=Path)
    args = parser.parse_args()
    try:
        config = tomllib.loads(args.request.read_text(encoding='utf-8-sig'))
        request = build_request(args.repo, config, args.approved_by, args.approval_evidence, args.content_reviewed)
        options = {'previous': mps.read_artifact_model(args.previous)} if args.previous else {}
        if args.check:
            model = mps.build_model(args.repo, request, sample=True, **options)
            mps.validate_html(model, mps.render_html(model))
            print(json.dumps({'request': 'pass', 'source_count': len(model['sources']), 'claims': len(model['semantic']['narrative']['claims'])}))
        else:
            artifact = mps.generate(args.repo, request, **options)
            print(artifact.relative_to(args.repo.resolve()).as_posix())
            print(json.dumps(mps.validate_artifact(artifact, args.repo), ensure_ascii=False, indent=2))
    except (OSError, ValueError, TypeError, KeyError, subprocess.TimeoutExpired) as error:
        parser.exit(1, f'blocked: {error}\n')


if __name__ == '__main__':
    main()
