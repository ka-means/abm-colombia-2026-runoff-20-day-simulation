#!/usr/bin/env python3
"""Generate a SHA-256 manifest for a directory tree."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=Path("MANIFEST.sha256"))
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    files = sorted(
        p for p in root.rglob("*")
        if p.is_file() and p.resolve() != output.resolve() and ".git" not in p.parts
    )
    lines = [f"{digest(path)}  {path.relative_to(root).as_posix()}" for path in files]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} checksums to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
