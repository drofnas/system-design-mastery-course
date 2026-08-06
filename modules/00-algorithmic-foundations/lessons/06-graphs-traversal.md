---
lesson_id: L06
title: "Graphs and Traversal"
---

# Graphs and Traversal

## Outcomes

- Choose adjacency lists or matrices from density and access needs.
- Explain BFS, DFS, shortest paths, and topological order.
- Recognize graph problems inside architecture work.

## Prerequisites

Algebra, comfort reading loops and arrays in any language, and the ability to separate a model from a measurement.

## Mechanism

A graph is nodes plus edges. Adjacency lists fit sparse graphs. Matrices fit
dense graphs or constant-time edge existence checks when memory is acceptable.

BFS explores by distance in unweighted graphs. DFS explores depth and helps find
cycles. Shortest-path algorithms add weights. Topological ordering handles
directed acyclic dependencies.

### Representation math and traversal purpose

Sparse graph memory is dominated by edges. With 10 million nodes and average degree 3, an undirected adjacency list stores roughly 30 million neighbor entries if the degree is counted per node, plus per-node offsets. An adjacency matrix needs `10^7 * 10^7 = 10^14` cells. Even one bit per cell is about 12.5 TB before overhead. The representation decision is not stylistic.

BFS finds shortest paths in unweighted graphs because it explores all nodes at distance `k` before distance `k+1`. DFS is useful for reachability, cycle detection, and topological sorting support. Weighted shortest paths need algorithms such as Dijkstra's when weights are nonnegative; negative weights need different assumptions.

Topological order is the systems workhorse: migrations, build graphs, schema dependencies, and organizational handoffs all need a safe order. A cycle means there is no topological order until a dependency is removed or a joint cutover is designed.

### Repeatable technique

1. Name nodes and directed edge meaning.
2. Estimate density before choosing list or matrix.
3. Choose traversal by question: reachability, shortest unweighted path, weighted path, cycle, or order.
4. Record what edge weights or missing edges mean.
5. Treat cycles as design facts, not graph-library errors.

## Worked example

A service dependency map is a graph. To plan a migration, you may need to find
all downstream consumers, detect cycles, and order changes so dependencies move
before dependents.

## Common expert mistakes

- Using a matrix for a sparse graph at large scale.
- Ignoring cycles in dependency work.
- Calling the first found path the cheapest path when edges have weights.

## Guided practice

Use EX-05's graph: 10 million nodes, average degree 3. Estimate adjacency-list edge entries and adjacency-matrix cells. Then choose BFS, DFS, weighted shortest path, or topological sort for a service migration plan.

## Self-check

1. When is an adjacency matrix reasonable?
2. Why does BFS find unweighted shortest paths?
3. What does topological sort require?
4. What does a cycle reveal in a dependency migration?

## Explained answers

1. When the graph is dense or constant-time edge checks justify the memory.
2. It explores by increasing number of edges from the start node.
3. A directed acyclic graph.
4. Some dependency must be broken, abstracted, or migrated jointly. For the practice, the list is about 30 million edge entries; the matrix is `10^14` cells; migration ordering usually needs topological sort plus cycle detection.

## Sources and next work

Study RES-01, RES-02, RES-05, and RES-07. Then complete EX-05.
