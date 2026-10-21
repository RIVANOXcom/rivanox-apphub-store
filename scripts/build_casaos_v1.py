#!/usr/bin/env python3
"""Build a reproducible legacy CasaOS v1 store ZIP from approved Apps/ sources.

The ZIP must NOT be published without upstream Workbench approval, GHCR image
digest checks, install/recovery tests and the protected AppHub release gate.
"""
from pathlib import Path
import sys
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from validate import InvalidCatalog, validate


def build(root: Path) -> Path:
    root = root.resolve()
    try:
        count = validate(root)
    except (InvalidCatalog, ValueError, OSError) as exc:
        raise ValueError(f"invalid catalog: {exc}") from exc
    if count == 0:
        raise ValueError("refuse to publish an empty app store")
    apps = root / "Apps"
    if not apps.is_dir() or not any(apps.glob("*/docker-compose.yml")):
        raise ValueError("no CasaOS apps to include")
    target = root / "dist" / "store" / "main.zip"
    target.parent.mkdir(parents=True, exist_ok=True)
    paths = sorted(p for p in apps.rglob("*") if p.is_file() or p.is_symlink())
    with ZipFile(target, "w", compression=ZIP_DEFLATED, compresslevel=9) as zf:
        for path in paths:
            if path.is_symlink():
                raise ValueError(f"symlink cannot be packaged: {path}")
            if not path.resolve().is_relative_to(apps.resolve()):
                raise ValueError(f"file outside app catalog: {path}")
            arcname = path.relative_to(root).as_posix()
            info = ZipInfo(arcname, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with path.open("rb") as fp:
                zf.writestr(info, fp.read(), compress_type=ZIP_DEFLATED, compresslevel=9)
    print(f"CasaOS v1 archive generated: {target.relative_to(root)} ({len(paths)} files)")
    return target


if __name__ == "__main__":
    try:
        build(Path(__file__).resolve().parents[1])
    except ValueError as exc:
        print(f"CASAOS_V1_BUILD_FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
