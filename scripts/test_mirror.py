from __future__ import annotations

import copy
import json
import shutil
import subprocess
import tempfile
import tomllib
import unittest
from unittest.mock import patch
from datetime import datetime
from pathlib import Path

import mirror
import verify


class MirrorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name) / 'rem'
        shutil.copytree(mirror.ROOT, self.repo, ignore=shutil.ignore_patterns('.git', '__pycache__', '*.html'))
        template = self.repo / '.agents/skills/teamspage/MPS/assets/mps.html'
        template.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(mirror.ROOT / '.agents/skills/teamspage/MPS/assets/mps.html', template)
        baseline = datetime.now().astimezone().date().isoformat()
        (self.repo / 'Repo/today.md').write_text(f'# today - {baseline}\n', encoding='utf-8')
        (self.repo / 'Repo/now.md').write_text(f'# now\n{baseline}\n', encoding='utf-8')
        self.config = tomllib.loads((self.repo / 'Mission/Requests/bootstrap.toml').read_text(encoding='utf-8'))
        for arguments in (('init', '-b', 'main'), ('config', 'user.name', 'rem synthetic test'),
                          ('config', 'user.email', 'fixture@example.invalid'), ('add', '.'),
                          ('commit', '-m', 'synthetic fixture baseline')):
            subprocess.run(['git', '-C', str(self.repo), *arguments], check=True, capture_output=True)

    def request(self, config: dict | None = None) -> dict:
        return mirror.build_request(self.repo, config or self.config, 'fixture-owner', 'synthetic-test-only', True)

    def test_read_permission_required(self) -> None:
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            mirror.build_request(self.repo, self.config, 'fixture-owner', 'synthetic-test-only', False)

    def test_actor_required(self) -> None:
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            mirror.build_request(self.repo, self.config, '', 'synthetic-test-only', True)

    def test_unexpected_fields_denied(self) -> None:
        config = {**self.config, 'projection_sources': {'method': 'unapproved'}}
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            self.request(config)

    def test_path_escape_denied(self) -> None:
        config = {**self.config, 'sources': ['../outside.md']}
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            self.request(config)

    def test_missing_source_denied(self) -> None:
        config = {**self.config, 'sources': ['Mission/missing.md']}
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            self.request(config)

    def test_unsupported_source_denied(self) -> None:
        config = {**self.config, 'sources': ['Mission/Requests/bootstrap.toml']}
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            self.request(config)

    def test_credential_marker_denied(self) -> None:
        (self.repo / 'Mission/outputs.md').write_text('-----BEGIN PRIVATE KEY-----\nfixture only\n', encoding='utf-8')
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            self.request()

    def test_stale_date_denied(self) -> None:
        (self.repo / 'Repo/today.md').write_text('# today - 2000-01-01\n', encoding='utf-8')
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            mirror.mps.build_model(self.repo, self.request(), sample=True)

    def test_now_date_mismatch_denied(self) -> None:
        (self.repo / 'Repo/now.md').write_text('# now\n2000-01-01\n', encoding='utf-8')
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            mirror.mps.build_model(self.repo, self.request(), sample=True)

    def test_complete_selected_lines_with_provenance(self) -> None:
        request = self.request()
        expected = sum(bool(line.strip()) for relative in dict.fromkeys([
            self.config['mission'], self.config['eval'], *self.config['sources']
        ]) for line in (self.repo / relative).read_text(encoding='utf-8').splitlines())
        self.assertEqual(len(request['narrative']['claims']), expected)
        model = mirror.mps.build_model(self.repo, request, sample=True)
        self.assertIsNone(model['semantic']['selected_method'])
        self.assertEqual(model['semantic']['target']['namespace'], 'REM')
        self.assertEqual(model['checks']['g_tier'], 'pass')
        mirror.mps.validate_html(model, mirror.mps.render_html(model))

    def test_missing_voice_is_blocked(self) -> None:
        request = self.request()
        request['voice_sources'].pop('claims.0')
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            mirror.mps.build_model(self.repo, request, sample=True)

    def test_rebuild_freshness_and_previous_delta(self) -> None:
        first = mirror.mps.generate(self.repo, self.request())
        self.assertEqual(first.parent, self.repo / 'Repo/shape/TeamsPage')
        report = mirror.mps.validate_artifact(first, self.repo)
        self.assertEqual(report['projection'], 'pass')
        self.assertEqual(report['freshness'], 'matches_observed_files')
        previous = mirror.mps.read_artifact_model(first)
        source = self.repo / 'Mission/outputs.md'
        source.write_text(source.read_text(encoding='utf-8') + '\nfixture revision evidence\n', encoding='utf-8')
        stale = mirror.mps.validate_artifact(first, self.repo)
        self.assertEqual(stale['freshness'], 'stale')
        second = mirror.mps.generate(self.repo, self.request(), previous=previous)
        current = mirror.mps.read_artifact_model(second)
        self.assertIn('Mission/outputs.md', current['delta']['source_paths'])
        self.assertEqual(current['previous_snapshot_id'], previous['snapshot_id'])
        self.assertEqual(mirror.mps.validate_artifact(second, self.repo)['freshness'], 'matches_observed_files')

    def test_historical_allocator_checks_current_and_legacy_custody_paths(self) -> None:
        with patch.object(mirror.mps, 'git', side_effect=[
            'MPS-260930S3002-rem-instance-rem.html\n',
            'MPS-260930S3001-rem-instance-rem.html\n',
        ]) as git_call:
            history = mirror.mps._historical_mps_page_ids(self.repo)
        self.assertEqual({page_id for page_id, _path in history}, {'260930S3001', '260930S3002'})
        self.assertEqual([call.args[-1] for call in git_call.call_args_list], [
            'Repo/shape/TeamsPage', 'Repo/shape/teamspage',
        ])

    def test_source_hash_race_is_blocked(self) -> None:
        request = self.request()
        source = self.repo / 'Mission/outputs.md'
        source.write_text(source.read_text(encoding='utf-8') + '\nchanged after capture\n', encoding='utf-8')
        with self.assertRaises(mirror.mps.SnapshotBlocked):
            mirror.mps.build_model(self.repo, request, sample=True)

    def test_structure_and_unchanged_pins(self) -> None:
        result = verify.inspect(self.repo)
        self.assertEqual(result['failures'], [])
        manifest = json.loads((self.repo / 'EGO/TeamSkill/source-manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(len(manifest['unchanged_files']), 7)
        self.assertEqual({delta['path'] for delta in manifest['target_deltas']}, {
            '.agents/skills/teamspage/MPS/scripts/mps.py',
            '.agents/skills/teamspage/references/teamspage-runtime-contract.md',
        })


if __name__ == '__main__':
    unittest.main()
