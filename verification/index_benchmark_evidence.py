from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

INDEX_SCHEMA = "MDPAR_BENCHMARK_EVIDENCE_INDEX_V2"
CAPABILITIES = tuple(f"C{i}" for i in range(13))
_VERSION_DIR = re.compile(r"^MDPAR-v(?P<version>\d+\.\d+\.\d+)$")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _identity(root: Path, path: Path) -> tuple[str | None, str | None]:
    parts = path.relative_to(root).parts
    if not parts:
        return None, None
    match = _VERSION_DIR.match(parts[0])
    if match:
        version = match.group("version")
        instrument = parts[1] if len(parts) > 1 else None
        return version, instrument
    # A path without an explicit release directory has unknown release identity.
    return None, parts[0] if len(parts) > 1 else None


def build_index(runs_root: Path) -> dict[str, Any]:
    capabilities_root = runs_root / "capabilities"
    files: list[dict[str, Any]] = []
    capability_summary: dict[str, dict[str, Any]] = {}

    for capability in CAPABILITIES:
        root = capabilities_root / capability
        # Only release-qualified directories are canonical benchmark evidence.
        # Unversioned run directories may coexist as operational/raw run material,
        # but they are intentionally excluded from the reproducible evidence index.
        release_roots = sorted(
            path for path in root.iterdir()
            if path.is_dir() and _VERSION_DIR.match(path.name)
        ) if root.exists() else []
        capability_files = sorted(
            path
            for release_root in release_roots
            for path in release_root.rglob("*")
            if path.is_file()
        )
        versions: set[str] = set()
        instruments: set[str] = set()
        for path in capability_files:
            version, instrument = _identity(root, path)
            if version is not None:
                versions.add(version)
            if instrument is not None:
                instruments.add(instrument)
            files.append({
                "path": path.relative_to(runs_root).as_posix(),
                "capability": capability,
                "mdpar_version": version,
                "instrument": instrument,
                "size_bytes": path.stat().st_size,
                "sha256": _sha256(path),
            })
        capability_summary[capability] = {
            "file_count": len(capability_files),
            "versions": sorted(versions),
            "instruments": sorted(instruments),
        }

    files.sort(key=lambda entry: entry["path"])
    return {
        "schema": INDEX_SCHEMA,
        "capability_range": "C0-C12",
        "artifact_policy": "Evidence bytes are preserved; packaging paths are normalized by MDPAR version, instrument and execution regime. Internal provenance is not rewritten.",
        "capabilities": capability_summary,
        "files": files,
    }


def serialized_index(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the deterministic C0-C12 benchmark evidence index.")
    parser.add_argument("--runs-root", default="runs")
    parser.add_argument("--output", default=None)
    parser.add_argument("--check-existing", action="store_true", help="fail unless a rebuilt index is byte-equivalent to the retained index")
    args = parser.parse_args()

    runs_root = Path(args.runs_root)
    output = Path(args.output) if args.output else runs_root / "index.json"
    payload = build_index(runs_root)
    rendered = serialized_index(payload)
    if args.check_existing:
        if not output.exists() or output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("evidence index is not reproducible from current runs tree")
        print("evidence_index_rebuild=PASS")
        return
    output.write_text(rendered, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
