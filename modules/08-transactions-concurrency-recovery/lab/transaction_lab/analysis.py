from __future__ import annotations

from typing import Any


def serialization_edges(transactions: list[dict[str, Any]]) -> list[list[str]]:
    edges: set[tuple[str, str]] = set()
    for left in transactions:
        left_reads = set(left["reads"])
        left_writes = set(left["writes"])
        for right in transactions:
            if left["id"] == right["id"]:
                continue
            right_reads = set(right["reads"])
            right_writes = set(right["writes"])
            if left_writes & (right_reads | right_writes):
                edges.add((left["id"], right["id"]))
    return [list(edge) for edge in sorted(edges)]


def has_cycle(edges: list[list[str]]) -> bool:
    graph: dict[str, set[str]] = {}
    for source, target in edges:
        graph.setdefault(source, set()).add(target)
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        if any(visit(child) for child in graph.get(node, set())):
            return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in graph)


def wait_for_cycle(waits: list[list[str]]) -> bool:
    return has_cycle(waits)
