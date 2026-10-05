import copy
import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from runtime_snapshot import SnapshotBlocked, generate, prepare


class RuntimeSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name).resolve()
        files = {
            "Ego/Ego-fixture.md": "# Synthetic Ego\n",
            "Ego/EdgeTeam.md": "# Synthetic team\n",
            "Ego/Naming.md": "# Synthetic naming\n",
            "Ego/Working.md": "# Synthetic mode\n",
            "Mission/Story-fixture.md": "# Synthetic commitment\n",
            "Mission/EVAL/fixture.md": "# Synthetic acceptance\n",
            "AGENTS.md": "# Synthetic authority\n",
            "Repo/today.md": "# today - 2026-09-07\n",
            "Repo/now.md": "# now\n2026-09-07\n",
        }
        for relative, text in files.items():
            path = self.repo / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        (self.repo / "Repo/Dojo").mkdir()
        self.command("init", "-q")
        self.command("config", "core.autocrlf", "false")
        self.command("add", ".")
        self.command("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "-c", "commit.gpgsign=false", "commit", "-qm", "synthetic baseline")
        self.payload = {
            "schema_version": "1.0",
            "run_id": "first",
            "slug": "fixture",
            "source_commit": self.command("rev-parse", "HEAD"),
            "source_sha256": {relative: self.digest(relative) for relative in files},
            "observed_at": "2026-09-07T10:00:00+08:00",
            "baseline_date": "2026-09-07",
            "scope": "synthetic behavior test",
            "binding": {"mission": "Mission/Story-fixture.md", "eval": "Mission/EVAL/fixture.md", "authority": "AGENTS.md"},
            "selected_method": None,
            "permission": {"snapshot_write": True, "approved_by": "fixture-owner", "approval_evidence": "synthetic test grant", "allowed_sources": list(files), "content_reviewed_no_secrets": True},
            "observations": {
                name: {"source_claims": ["Fixture source statement"], "Fact": [], "Claim": [], "Credence": "unknown", "unknowns": ["No independent observation"], "delta": []}
                for name in ("Ego-fixture.md", "EdgeTeam.md", "Naming.md", "Working.md")
            },
        }

    def command(self, *arguments):
        return subprocess.run(["git", "-C", str(self.repo), *arguments], check=True, capture_output=True, text=True).stdout.strip()

    def digest(self, relative):
        return hashlib.sha256((self.repo / relative).read_bytes()).hexdigest()

    def test_method_free_reproducible_four_files_no_writeback(self):
        baseline = copy.deepcopy(self.payload["source_sha256"])
        output = generate(self.repo, self.payload)
        self.assertEqual(set(self.payload["observations"]), {item.name for item in output.iterdir()})
        self.assertEqual(prepare(self.repo, self.payload), prepare(self.repo, self.payload))
        for relative, digest in baseline.items():
            self.assertEqual(digest, self.digest(relative))
        self.assertIn('"Credence": "unknown"', (output / "Naming.md").read_text(encoding="utf-8"))

    def test_selected_crafts_is_explicit_source_not_global_requirement(self):
        relative = "Ego/CRAFTS.md"
        (self.repo / relative).write_text("# Synthetic selected CRAFTS\n", encoding="utf-8")
        self.payload["selected_method"] = {"name": "CRAFTS", "source": relative}
        self.payload["permission"]["allowed_sources"].append(relative)
        self.payload["source_sha256"][relative] = self.digest(relative)
        self.assertIn('"name": "CRAFTS"', prepare(self.repo, self.payload)[1]["Naming.md"])

    def test_missing_bindings_block(self):
        for key in ("mission", "eval", "authority"):
            with self.subTest(key=key):
                payload = copy.deepcopy(self.payload)
                del payload["binding"][key]
                with self.assertRaises(SnapshotBlocked):
                    prepare(self.repo, payload)

    def test_missing_ego_blocks(self):
        (self.repo / "Ego/Working.md").unlink()
        with self.assertRaises(SnapshotBlocked):
            generate(self.repo, self.payload)
        self.assertEqual([], list((self.repo / "Repo/Dojo").iterdir()))

    def test_permission_and_custody_gates(self):
        for key in ("snapshot_write", "content_reviewed_no_secrets", "approval_evidence", "allowed_sources"):
            with self.subTest(key=key):
                payload = copy.deepcopy(self.payload)
                del payload["permission"][key]
                with self.assertRaises(SnapshotBlocked):
                    prepare(self.repo, payload)

    def test_stale_date_and_hash_block(self):
        payload = copy.deepcopy(self.payload)
        payload["observed_at"] = "2026-09-08T10:00:00+08:00"
        with self.assertRaises(SnapshotBlocked):
            prepare(self.repo, payload)
        (self.repo / "Ego/Working.md").write_text("changed", encoding="utf-8")
        with self.assertRaises(SnapshotBlocked):
            prepare(self.repo, self.payload)

    def test_dirty_source_is_visible_when_hash_matches(self):
        relative = "Ego/Working.md"
        (self.repo / relative).write_text("# changed\n", encoding="utf-8")
        self.payload["source_sha256"][relative] = self.digest(relative)
        text = prepare(self.repo, self.payload)[1]["Working.md"]
        envelope = json.loads(text.split("```json\n")[1].split("\n```")[0])
        self.assertTrue(envelope["source_revision"]["dirty"])

    def test_rejects_path_traversal_and_existing_run(self):
        payload = copy.deepcopy(self.payload)
        payload["run_id"] = "../../EGO"
        with self.assertRaises(SnapshotBlocked):
            generate(self.repo, payload)
        generate(self.repo, self.payload)
        with self.assertRaises(SnapshotBlocked):
            generate(self.repo, self.payload)

    def test_unsubstantiated_fact_and_authority_injection_block(self):
        record = self.payload["observations"]["Naming.md"]
        record["Fact"] = [{"statement": "Invented admission"}]
        with self.assertRaises(SnapshotBlocked):
            prepare(self.repo, self.payload)
        record["Fact"] = []
        record["authority"] = "canonical"
        with self.assertRaises(SnapshotBlocked):
            prepare(self.repo, self.payload)

    def test_source_claim_and_conflicting_observation_remain_separate(self):
        record = self.payload["observations"]["Working.md"]
        record["Fact"] = [{"statement": "Observed state differs", "evidence": "synthetic observation fixture", "observed_at": self.payload["observed_at"]}]
        record["delta"] = ["Owner review required"]
        text = prepare(self.repo, self.payload)[1]["Working.md"]
        self.assertIn("Fixture source statement", text)
        self.assertIn("Observed state differs", text)
        self.assertIn("non-authority/no-writeback", text)


if __name__ == "__main__":
    unittest.main()
