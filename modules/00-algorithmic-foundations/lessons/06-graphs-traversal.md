---
lesson_id: L06
title: "Graphs and Traversal"
---

# Graphs and Traversal

## Outcomes

- Choose adjacency lists or matrices from density and access needs.
- Explain BFS, DFS, shortest paths, and topological order.
- Recognize graph problems inside architecture work.

## Mechanism

A graph is nodes plus edges. Adjacency lists fit sparse graphs. Matrices fit
dense graphs or constant-time edge existence checks when memory is acceptable.

BFS explores by distance in unweighted graphs. DFS explores depth and helps find
cycles. Shortest-path algorithms add weights. Topological ordering handles
directed acyclic dependencies.

## Worked Example

A service dependency map is a graph. To plan a migration, you may need to find
all downstream consumers, detect cycles, and order changes so dependencies move
before dependents.

## Common Expert Mistakes

- Using a matrix for a sparse graph at large scale.
- Ignoring cycles in dependency work.
- Calling the first found path the cheapest path when edges have weights.

## Guided Practice

Draw three services and their dependencies. Mark one cycle or prove no cycle
exists.

## Self-Check

Why does this connect to M14? Because ownership, dependency exit, and migration
order are graph-shaped problems.

## Sources And Next Work

Study RES-01 and RES-02. Then complete EX-05.
