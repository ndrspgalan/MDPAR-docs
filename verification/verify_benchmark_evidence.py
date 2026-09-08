from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify benchmark evidence files against runs/index.json.")
    parser.add_argument("--runs-root", default="runs")
    parser.add_argument("--index", default=None)
    args = parser.parse_args()

    runs_root = Path(args.runs_root)
    index_path = Path(args.index) if args.index else runs_root / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))

    failures: list[str] = []
    for entry in index.get("files", []):
        path = runs_root / entry["path"]
        if not path.exists():
            failures.append(f"MISSING {entry['path']}")
            continue
        if path.stat().st_size != int(entry["size_bytes"]):
            failures.append(f"SIZE {entry['path']}")
            continue
        actual = _sha256(path)
        if actual != entry["sha256"]:
            failures.append(f"SHA256 {entry['path']}")

    if failures:
        for failure in failures:
            print(failure)
        raise SystemExit(1)

    print(f"verified_files={len(index.get('files', []))}")
    print("evidence_integrity=PASS")


if __name__ == "__main__":
    main()
