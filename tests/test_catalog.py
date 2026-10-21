"""Unit tests for strict AppHub manifest gates."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate import InvalidCatalog, validate


class CatalogGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "store-config.json").write_text(
            json.dumps({"version": 2, "store_id": "com.rivanox.apphub"}), encoding="utf-8")
        (self.root / "supported-languages.json").write_text(
            '["de_DE", "en_US"]', encoding="utf-8")
        (self.root / "umbrel-app-store.yml").write_text(
            'id: "rivanoxapphub"\nname: "RIVANOX AppHub"\n', encoding="utf-8")

    def app(self, image, other=""):
        directory = self.root / "Apps" / "MediaCenter"
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "docker-compose.yml").write_text(
            'name: media-center\nservices:\n  web:\n    image: "' + image +
            '"\nx-casaos:\n  id: com.rivanox.media-center\n' + other,
            encoding="utf-8")

    def test_empty_catalog_is_valid_staging(self):
        self.assertEqual(validate(self.root), 0)

    def test_digest_pinned_public_ghcr_image_is_accepted(self):
        self.app("ghcr.io/rivanoxcom/media-center-web@sha256:" + "a" * 64)
        self.assertEqual(validate(self.root), 1)

    def test_version_tag_without_digest_is_rejected(self):
        self.app("ghcr.io/rivanoxcom/media-center-web:1.0.0")
        with self.assertRaises(InvalidCatalog):
            validate(self.root)

    def test_gitea_end_user_image_is_rejected(self):
        self.app("git.rivanox.com/rivanox/media-center-web@sha256:" + "b" * 64)
        with self.assertRaises(InvalidCatalog):
            validate(self.root)

    def test_shared_setup_secret_marker_is_rejected(self):
        self.app("ghcr.io/rivanoxcom/media-center-web@sha256:" + "a" * 64,
                 '  tips: __MEDIA_CENTER_INITIAL_SETUP_TOKEN__\n')
        with self.assertRaises(InvalidCatalog):
            validate(self.root)

    def test_partial_app_folder_is_rejected(self):
        (self.root / "Apps" / "HalfBuilt").mkdir(parents=True)
        with self.assertRaises(InvalidCatalog):
            validate(self.root)

    def test_umbrel_metadata_is_required(self):
        directory = self.root / "rivanoxapphub-mediacenter"
        directory.mkdir()
        (directory / "docker-compose.yml").write_text(
            'services:\n  web:\n    image: ghcr.io/rivanoxcom/media-center-web@sha256:' +
            'a' * 64 + '\n', encoding="utf-8")
        with self.assertRaises(InvalidCatalog):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
