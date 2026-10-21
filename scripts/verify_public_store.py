#!/usr/bin/env python3
"""Read-only production endpoint health check for ZimaOS and CasaOS catalogs.

No credentials are used or transmitted. The check validates artifact transport
and basic formats, not device-level installation or release authorization.
"""
import argparse
from io import BytesIO
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zipfile import ZipFile

BASE = "https://rivanoxcom.github.io/rivanox-apphub-store"


def fetch(path, content_type=None):
    url = f"{BASE}/{path}"
    req = Request(url, headers={"User-Agent": "RIVANOX-AppHub-Store-HealthCheck/1.0"})
    try:
        with urlopen(req, timeout=20) as reply:
            body = reply.read(10 * 1024 * 1024 + 1)
            if reply.status != 200 or len(body) > 10 * 1024 * 1024:
                raise RuntimeError(f"{path}: non-200 or unexpectedly large response")
            if content_type and content_type not in reply.headers.get("Content-Type", ""):
                raise RuntimeError(f"{path}: wrong Content-Type")
            print(f"PASS {path}: {len(body)} bytes")
            return body
    except (HTTPError, URLError) as err:
        raise RuntimeError(f"{path}: cannot download public artifact: {err}") from err


def main(require_apps):
    store = json.loads(fetch("store.json"))
    if store.get("version") != 2 or store.get("store_id") != "com.rivanox.apphub":
        raise RuntimeError("store.json: unexpected protocol or store identity")

    index = json.loads(fetch("index.json"))
    if not isinstance(index, (dict, list)):
        raise RuntimeError("index.json: invalid store-wide index type")

    website = fetch("index.html").decode("utf-8")
    if "RIVANOX AppHub" not in website or "<title>" not in website:
        raise RuntimeError("index.html: website SEO title missing")

    archive = fetch("store/main.zip")
    try:
        with ZipFile(BytesIO(archive)) as zf:
            if zf.testzip() is not None:
                raise RuntimeError("store/main.zip: corrupt ZIP")
            apps = [name for name in zf.namelist()
                    if name.startswith("Apps/") and name.endswith("/docker-compose.yml")]
    except Exception as err:
        raise RuntimeError(f"store/main.zip: invalid ZIP: {err}") from err

    print(f"CasaOS catalog app definitions: {len(apps)}")
    if require_apps and not apps:
        raise RuntimeError("no installable approved apps in CasaOS ZIP")
    print("Public catalog download checks passed; device installation is independently required.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-empty", action="store_true",
                        help="Test catalog transport only, not app availability")
    args = parser.parse_args()
    try:
        main(require_apps=not args.allow_empty)
    except (RuntimeError, ValueError, json.JSONDecodeError) as err:
        parser.exit(1, f"APPHUB_PUBLIC_ENDPOINT_FAILED: {err}\n")
