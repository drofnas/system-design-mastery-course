"""Subprocess helper that terminates with an uncommitted stolen update."""

from __future__ import annotations

import argparse
import os

from .engine import ToyStore


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    store = ToyStore(args.root, {"committed": 0, "loser": 0})
    store.begin("LOSER")
    store.update("LOSER", "loser", 1, steal=True)
    os._exit(17)


if __name__ == "__main__":
    main()
