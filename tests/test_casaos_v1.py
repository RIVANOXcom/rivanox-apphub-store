"""Regression checks for deterministic CasaOS ZIP packaging."""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_casaos_v1 import build


class CasaosLegacyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "store-config.json").write_text(
            json.dumps({"version": 2, "store_id": "com.rivanox.apphub"}), encoding="utf-8")
        (self.root / "supported-languages.json").write_text('["de_DE", "en_US"]', encoding="utf-8")
        (self.root / "umbrel-app-store.yml").write_text(
            'id: "rivanoxapphub"\nname: "RIVANOX AppHub"\n', encoding="utf-8")

    def add_test_app(self):
        app = self.root / "Apps" / "MediaCenter"
        app.mkdir(parents=True)
        (app / "docker-compose.yml").write_text(
            'services:\n  web:\n    image: ghcr.io/rivanoxcom/media-center-web@sha256:' +
            'a' * 64 + '\nx-casaos:\n  id: com.rivanox.media-center\n',
            encoding="utf-8")
        (app / "icon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"/>',
                                      encoding="utf-8")

    def test_empty_store_cannot_be_published(self):
        with self.assertRaises(ValueError):
            build(self.root)

    def test_zip_contains_casaos_app_tree_and_is_deterministic(self):
        self.add_test_app()
        output = build(self.root)
        first = hashlib.sha256(output.read_bytes()).hexdigest()
        with ZipFile(output) as zf:
            self.assertEqual(zf.namelist(), [
                "Apps/MediaCenter/docker-compose.yml",
                "Apps/MediaCenter/icon.svg",
            ])
        second = hashlib.sha256(build(self.root).read_bytes()).hexdigest()
        self.assertEqual(first, second)

    def test_reject_symlink(self):
        self.add_test_app()
        (self.root / "Apps" / "MediaCenter" / "shadow").symlink_to("/etc/passwd")
        with self.assertRaises(ValueError):
            build(self.root)


if __name__ == "__main__":
    unittest.main()
