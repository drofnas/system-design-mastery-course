from __future__ import annotations

import hashlib
from typing import Iterable


def quorum_properties(replication_factor: int, read: int, write: int) -> dict[str, bool]:
    """State the two intersections that simple quorum arithmetic can establish."""
    return {
        "read_write_intersection": read + write > replication_factor,
        "write_write_intersection": write * 2 > replication_factor,
    }


def session_violations(versions: Iterable[int], required_version: int = 0) -> dict[str, int]:
    observed = list(versions)
    monotonic = sum(1 for left, right in zip(observed, observed[1:]) if right < left)
    read_your_writes = sum(1 for version in observed if version < required_version)
    return {"monotonic": monotonic, "read_your_writes": read_your_writes}


def merge_siblings(siblings: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    """Preserve unique concurrent siblings; do not invent a domain merge."""
    unique: dict[tuple[object, object, object], dict[str, object]] = {}
    for sibling in siblings:
        key = (sibling.get("replica"), sibling.get("version"), sibling.get("value"))
        unique[key] = dict(sibling)
    return [unique[key] for key in sorted(unique, key=lambda item: tuple(map(str, item)))]


def _score(key: str, node: str) -> int:
    return int(hashlib.sha256(f"{key}:{node}".encode()).hexdigest(), 16)


def owner(key: str, nodes: list[str], strategy: str) -> str:
    if strategy == "consistent_hash":
        return max(nodes, key=lambda node: _score(key, node))
    if strategy == "range":
        first = ord(key[0].lower()) if key else 0
        return nodes[min(len(nodes) - 1, first * len(nodes) // 256)]
    index = int(hashlib.sha256(key.encode()).hexdigest(), 16) % len(nodes)
    return nodes[index]


def movement(keys: Iterable[str], before: list[str], after: list[str], strategy: str) -> tuple[int, float]:
    key_list = list(keys)
    moved = sum(owner(key, before, strategy) != owner(key, after, strategy) for key in key_list)
    return moved, round(moved / len(key_list), 6) if key_list else 0.0


def imbalance(per_node: dict[str, int]) -> float:
    values = list(per_node.values())
    if not values or min(values) == 0:
        return float(max(values, default=0))
    return round(max(values) / min(values), 3)
