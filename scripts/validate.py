#!/usr/bin/env python3
"""Validate public AppHub source definitions without accepting partial app manifests.

This is preflight defense-in-depth. Release provenance, Workbench authorization
and live host/device tests remain mandatory independent gates.
"""
from pathlib import Path
import json
import re
import sys


class InvalidCatalog(ValueError):
    pass


HEX_DIGEST = re.compile(r"@sha256:[0-9a-f]{64}$")
IMAGE_DECLARATION = re.compile(r"^\s*image:\s*['\"]?([^\s'\"#]+)", re.M)
SECRET_MARKER = re.compile(r"__[A-Z][A-Z0-9_]+__")
GIT_HOST = re.compile(r"(?:git\.rivanox\.com|https?://[^\s]*git\.rivanox\.com)", re.I)
YAML_STRING = re.compile(r'^\s*id:\s*["\']?([a-z0-9-]+)', re.M)


def fail(reason: str) -> None:
    raise InvalidCatalog(reason)


def validate(root: Path) -> int:
    try:
        config = json.loads((root / "store-config.json").read_text(encoding="utf-8"))
        languages = json.loads((root / "supported-languages.json").read_text(encoding="utf-8"))
        umbrel = (root / "umbrel-app-store.yml").read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as error:
        fail(f"missing or invalid store metadata: {error}")

    if config.get("version") != 2 or config.get("store_id") != "com.rivanox.apphub":
        fail("unexpected store schema or identity")
    if not isinstance(languages, list) or not {"de_DE", "en_US"}.issubset(set(languages)):
        fail("missing supported languages")
    if not re.search(r'^id:\s*["\']?rivanoxapphub["\']?\s*$', umbrel, re.M):
        fail("unexpected umbrel community store ID")

    casa_paths = list(root.glob("Apps/*/docker-compose.yml"))
    umbrel_paths = list(root.glob("rivanoxapphub-*/docker-compose.yml"))
    if any(p.is_dir() and not (p / "docker-compose.yml").is_file() for p in (root / "Apps").iterdir() if (root / "Apps").exists() and p.is_dir()):
        fail("app directory missing docker-compose.yml")
    for path in umbrel_paths:
        if not (path.parent / "umbrel-app.yml").is_file():
            fail(f"missing umbrel metadata: {path.parent}")

    for path in casa_paths + umbrel_paths:
        data = path.read_text(encoding="utf-8")
        if SECRET_MARKER.search(data):
            fail(f"unresolved install secret marker: {path}")
        if GIT_HOST.search(data):
            fail(f"end-user manifest references home-office Gitea: {path}")
        if re.search(r"(?<![a-z0-9]):latest\b", data):
            fail(f"floating latest tag in {path}")
        if "password123" in data.lower() or "changeme" in data.lower():
            fail(f"default credentials marker in {path}")
        if not re.search(r"^x-casaos:\s*$", data, re.M) and path in casa_paths:
            fail(f"missing x-casaos metadata in {path}")
        images = IMAGE_DECLARATION.findall(data)
        if not images:
            fail(f"no referenced Docker images in {path}")
        if not any(image.startswith("ghcr.io/rivanoxcom/") for image in images):
            fail(f"no GitHub-hosted RIVANOX image in {path}")
        for image in images:
            if not HEX_DIGEST.search(image):
                fail(f"unpinned image digest in {path}: {image.split('@')[0]}")
            if image.startswith("git.rivanox.com/"):
                fail(f"Gitea container image in {path}")
        print(f"Validated {path.relative_to(root)}")
    print(f"AppHub manifest validation passed: {len(casa_paths)} CasaOS/ZimaOS and {len(umbrel_paths)} umbrelOS manifests")
    return len(casa_paths) + len(umbrel_paths)


if __name__ == "__main__":
    try:
        validate(Path(__file__).resolve().parents[1])
    except (InvalidCatalog, OSError, TypeError) as e:
        print(f"APPHUB_VALIDATION_FAILED: {e}", file=sys.stderr)
        sys.exit(1)
