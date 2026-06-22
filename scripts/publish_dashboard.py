#!/usr/bin/env python3
"""Copy a generated dashboard HTML file into the GitHub Pages directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Path to generated dashboard HTML")
    parser.add_argument("--destination", type=Path, default=ROOT / "docs/index.html")
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    destination = args.destination.expanduser().resolve()
    if not source.exists() or source.suffix.lower() != ".html":
        raise FileNotFoundError(f"Dashboard HTML not found: {source}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    (destination.parent / ".nojekyll").touch()
    print(f"Published dashboard to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
