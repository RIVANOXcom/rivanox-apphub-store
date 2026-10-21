#!/usr/bin/env python3
"""Fail-closed checks on store metadata, before platform-specific packaging."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
config = json.loads((root / "store-config.json").read_text(encoding="utf-8"))
langs = json.loads((root / "supported-languages.json").read_text(encoding="utf-8"))
assert config["version"] == 2
assert config["store_id"] == "com.rivanox.apphub"
assert {"de_DE", "en_US"}.issubset(set(langs))
umbrel = (root / "umbrel-app-store.yml").read_text(encoding="utf-8")
assert re.search(r'^id: "rivanoxapphub"$', umbrel, re.M)

paths = list(root.glob("Apps/*/docker-compose.yml"))
paths += list(root.glob("rivanoxapphub-*/docker-compose.yml"))
for path in paths:
    data = path.read_text(encoding="utf-8")
    assert "__MEDIA_CENTER_" not in data, f"Unresolved secret marker in {path}"
    assert "git.rivanox.com/rivanox/media-center-" not in data, f"Public Gitea image in {path}"
    assert ":latest" not in data, f"Floating image tag in {path}"
    assert "ghcr.io/rivanoxcom/" in data, f"Missing GHCR images in {path}"
    print("Validated", path.relative_to(root))
print("AppHub source validation passed (does not imply live store publication)")
