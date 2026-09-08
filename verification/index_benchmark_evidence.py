from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

INDEX_SCHEMA = "MDPAR_BENCHMARK_EVIDENCE_INDEX_V1"
CAPABILITIES = tuple(f"C{i}" for i in range(13))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_index(runs_root: Path) -> dict[str, Any]:
    capabilities_root = runs_root / "capabilities"
    files: list[dict[str, Any]] = []
    capability_summary: dict[str, dict[str, Any]] = {}

    for capability in CAPABILITIES:
        root = capabilities_root / capability
        capability_files = sorted(path for path in root.rglob("*") if path.is_file()) if root.exists() else []
        instruments = sorted({path.relative_to(root).parts[0] for path in capability_files if len(path.relative_to(root).parts) > 1})
        capability_summary[capability] = {
            "file_count": len(capability_files),
            "instruments": instruments,
        }
        for path in capability_files:
            relative = path.relative_to(runs_root).as_posix()
            parts = path.relative_to(root).parts
            files.append(
                {
                    "path": relative,
                    "capability": capability,
                    "instrument": parts[0] if len(parts) > 1 else None,
                    "size_bytes": path.stat().st_size,
                    "sha256": _sha256(path),
                }
            )

    return {
        "schema": INDEX_SCHEMA,
        "mdpar_version": "2.0.0",
        "capability_range": "C0-C12",
        "artifact_policy": (
            "Historical evidence bytes are preserved. Canonical packaging names may differ "
            "from historical identifiers embedded in the original artifacts."
        ),
        "capabilities": capability_summary,
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the deterministic C0-C12 benchmark evidence index.")
    parser.add_argument("--runs-root", default="runs")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    runs_root = Path(args.runs_root)
    output = Path(args.output) if args.output else runs_root / "index.json"
    payload = build_index(runs_root)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
