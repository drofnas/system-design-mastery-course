lesson_id: L03

# Exact Search, HNSW, and Index Economics

## Outcomes

- Explain exact nearest-neighbor search as an oracle and capacity baseline.
- Trace seeded HNSW insertion and query navigation across layers.
- Tune `M`, `efConstruction`, and `efSearch` using recall, work, memory, and rebuild evidence.

## Prerequisites

Complete Lesson 2. Use Module 17 vector and memory arithmetic.

## Mechanism: exchange complete comparison for measured graph search

Exact search compares the query with every eligible vector. For `N` vectors of
dimension `D`, work is proportional to `N*D`; it establishes the top-k oracle
for a fixed snapshot. Approximate search visits fewer candidates and must report
recall against that oracle.

HNSW assigns a decreasing subset of nodes to higher graph layers. Search starts
at an entry point, moves greedily while a neighbor improves distance, descends,
then explores a broader candidate set at layer zero. Larger `M` raises
connectivity and memory. Larger `efConstruction` spends more build work seeking
neighbors. Larger `efSearch` usually visits more nodes and can recover recall.

Procedure:

1. Freeze vector model, normalization, corpus order, seed, filters, and exact oracle.
2. Sweep one HNSW parameter while holding the rest constant.
3. Report recall per risk slice, visited nodes, build work, memory, and p50/p95 query time.
4. Test insert, rebuild, delete/revocation, skew, and filter selectivity.
5. Choose the smallest operating envelope that clears the release gate; retain exact search for audit and small fallbacks.

## Worked example

CivicAid's five-vector lab assigns levels from seed 18 and uses `M=3`. Exact
search checks all five. HNSW begins at the highest-level node, descends toward
the solar-code cluster, and expands up to `efSearch=5` candidates. Matching the
oracle on five points proves code behavior only. The production decision needs
a representative corpus and filtered-query slices.

## Common expert mistakes

- Calling logarithmic average behavior a worst-case guarantee.
- Tuning on the same tiny friendly queries used to explain the graph.
- Reporting latency without recall or recall without visited work and memory.
- Forgetting that restrictive filters can disconnect useful candidates.
- Treating tombstoned vectors as revoked evidence without a served-result check.

## Guided practice

Draw two HNSW layers for six points. Trace a query for two values of `efSearch`.
Record visited nodes and Recall@2 against exact search. Predict what increasing
`M` changes in memory, build time, and recall, then state the experiment that
could falsify the prediction.

## Self-check

1. Why keep exact search after deploying ANN?
2. Which parameter primarily changes query-time candidate breadth?
3. What does a five-point recall result establish?

## Explained answers

1. It supplies the fixed-snapshot oracle, audits missed neighbors, and can serve small/rebuild cases.
2. `efSearch`; `M` and `efConstruction` shape the graph and build cost.
3. Only deterministic behavior on that fixture, not scale, population recall, or hardware performance.

## Sources and next work

- Malkov and Yashunin, HNSW: <https://arxiv.org/abs/1603.09320>
- Briggs, HNSW video: <https://www.youtube.com/watch?v=QvKMwLjdK-s>
- Inspect `lab/rag_agent_lab/retrieval.py`, then complete EX-05–EX-06.
