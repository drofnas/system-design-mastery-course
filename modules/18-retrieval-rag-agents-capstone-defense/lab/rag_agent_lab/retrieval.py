from __future__ import annotations

import heapq
import math
import random
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Iterable


TOKEN = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    return TOKEN.findall(text.lower())


def cosine(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("vector dimensions differ")
    denominator = math.sqrt(sum(x * x for x in left)) * math.sqrt(sum(x * x for x in right))
    return 0.0 if denominator == 0 else sum(x * y for x, y in zip(left, right)) / denominator


def exact_search(vectors: dict[str, list[float]], query: list[float], k: int) -> list[tuple[str, float]]:
    return sorted(((key, cosine(vector, query)) for key, vector in vectors.items()), key=lambda row: (-row[1], row[0]))[:k]


def bm25(documents: dict[str, str], query: str, *, k1: float = 1.2, b: float = 0.75) -> list[tuple[str, float]]:
    tokens = {key: tokenize(value) for key, value in documents.items()}
    average_length = sum(map(len, tokens.values())) / max(len(tokens), 1)
    document_frequency: Counter[str] = Counter()
    for words in tokens.values():
        document_frequency.update(set(words))
    scores: dict[str, float] = defaultdict(float)
    for term in tokenize(query):
        frequency = document_frequency[term]
        inverse = math.log(1 + (len(tokens) - frequency + 0.5) / (frequency + 0.5))
        for key, words in tokens.items():
            term_frequency = words.count(term)
            length_norm = 1 - b + b * len(words) / max(average_length, 1)
            scores[key] += inverse * term_frequency * (k1 + 1) / (term_frequency + k1 * length_norm) if term_frequency else 0.0
    return sorted(scores.items(), key=lambda row: (-row[1], row[0]))


def reciprocal_rank_fusion(rankings: Iterable[list[str]], *, rank_constant: int = 60) -> list[tuple[str, float]]:
    scores: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        for position, key in enumerate(ranking, start=1):
            scores[key] += 1.0 / (rank_constant + position)
    return sorted(scores.items(), key=lambda row: (-row[1], row[0]))


def transparent_rerank(query: str, documents: dict[str, str], candidates: list[tuple[str, float]]) -> list[tuple[str, float]]:
    query_terms = set(tokenize(query))
    reranked = []
    for key, base in candidates:
        overlap = len(query_terms & set(tokenize(documents[key]))) / max(len(query_terms), 1)
        reranked.append((key, base + overlap))
    return sorted(reranked, key=lambda row: (-row[1], row[0]))


def filter_documents(documents: list[dict], *, scopes: set[str], source_version: int, revocation_epoch: int) -> list[dict]:
    return [
        document for document in documents
        if document["required_scope"] in scopes
        and document["source_version"] == source_version
        and (document.get("revoked_at_epoch") is None or document["revoked_at_epoch"] > revocation_epoch)
    ]


@dataclass
class SearchResult:
    ids: list[str]
    visited: int


class HNSWIndex:
    """Small seeded HNSW teaching implementation, not a production index."""

    def __init__(self, *, m: int = 3, ef_construction: int = 8, seed: int = 18) -> None:
        if m < 1 or ef_construction < m:
            raise ValueError("require ef_construction >= m >= 1")
        self.m = m
        self.ef_construction = ef_construction
        self.random = random.Random(seed)
        self.vectors: dict[str, list[float]] = {}
        self.levels: dict[str, int] = {}
        self.graph: dict[int, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.entry: str | None = None
        self.max_level = -1

    def _level(self) -> int:
        level = 0
        while level < 8 and self.random.random() < 0.5:
            level += 1
        return level

    def add(self, key: str, vector: list[float]) -> None:
        if key in self.vectors:
            raise ValueError(f"duplicate key: {key}")
        level = self._level()
        existing = dict(self.vectors)
        self.vectors[key] = list(vector)
        self.levels[key] = level
        for layer in range(level + 1):
            eligible = [item for item in existing if self.levels[item] >= layer]
            nearest = exact_search({item: existing[item] for item in eligible}, vector, self.ef_construction)[: self.m]
            for neighbor, _ in nearest:
                self.graph[layer][key].add(neighbor)
                self.graph[layer][neighbor].add(key)
                if len(self.graph[layer][neighbor]) > self.m:
                    keep = {item for item, _ in exact_search({item: self.vectors[item] for item in self.graph[layer][neighbor]}, self.vectors[neighbor], self.m)}
                    self.graph[layer][neighbor].intersection_update(keep)
        if level > self.max_level or self.entry is None:
            self.entry, self.max_level = key, level

    def build(self, vectors: dict[str, list[float]]) -> None:
        for key in sorted(vectors):
            self.add(key, vectors[key])

    def search(self, query: list[float], *, k: int, ef_search: int) -> SearchResult:
        if self.entry is None:
            return SearchResult([], 0)
        current = self.entry
        visited = {current}
        for layer in range(self.max_level, 0, -1):
            improved = True
            while improved:
                improved = False
                current_score = cosine(self.vectors[current], query)
                for neighbor in sorted(self.graph[layer].get(current, set())):
                    visited.add(neighbor)
                    score = cosine(self.vectors[neighbor], query)
                    if score > current_score:
                        current, current_score, improved = neighbor, score, True
        candidates = [(-cosine(self.vectors[current], query), current)]
        found: dict[str, float] = {current: -candidates[0][0]}
        expanded: set[str] = set()
        while candidates and len(expanded) < max(ef_search, k):
            _, node = heapq.heappop(candidates)
            if node in expanded:
                continue
            expanded.add(node)
            for neighbor in sorted(self.graph[0].get(node, set())):
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                score = cosine(self.vectors[neighbor], query)
                found[neighbor] = score
                heapq.heappush(candidates, (-score, neighbor))
        ids = [key for key, _ in sorted(found.items(), key=lambda row: (-row[1], row[0]))[:k]]
        return SearchResult(ids, len(visited))
