# Module 00 Glossary

- **Asymptotic analysis:** reasoning about how work grows as input size changes,
  independent of a particular machine's stopwatch.
- **Big-O:** an upper growth bound after a threshold; formally, `f(n) <= c*g(n)`
  for sufficiently large `n`.
- **Theta:** a tight growth bound, both upper and lower within constant factors.
- **Omega:** a lower growth bound.
- **Amortized cost:** a sequence-level bound that spreads occasional expensive
  operations, such as dynamic-array resize, across many cheap operations.
- **Average case:** expected cost under a stated input distribution; not the same
  as amortized cost.
- **Dynamic array:** an array with spare capacity that resizes when full.
- **Locality:** the advantage gained when nearby memory is accessed together and
  hardware/cache behavior can reuse fetched data.
- **Load factor:** entries divided by hash-table bucket count or capacity.
- **Collision:** two keys mapping to the same hash bucket or probe path.
- **Hash flooding:** adversarial collision behavior that turns expected constant
  work into a denial-of-service risk.
- **Balanced search tree:** an ordered tree that maintains logarithmic height by
  preserving a balance invariant.
- **Fanout:** number of children or branches per tree node; high fanout lowers
  tree height for page-shaped storage.
- **B-tree:** a high-fanout ordered tree used heavily in storage systems.
- **Heap:** a partial-order structure that returns the minimum or maximum item
  according to a priority policy.
- **Priority queue:** an interface that admits and removes work according to a
  comparison function rather than arrival order alone.
- **Adjacency list:** graph representation storing each node's neighbors.
- **Adjacency matrix:** graph representation storing possible node pairs in a
  matrix; useful for dense graphs but expensive for sparse large graphs.
- **Topological order:** an ordering of directed acyclic graph nodes where each
  dependency appears before its dependents.
- **Stable sort:** a sort that preserves original order among equal keys.
- **External sort:** a sort plan for data larger than memory, usually based on
  sorted runs and merge passes.
- **Selection:** finding a rank such as top-k or median without fully sorting all
  items.
- **NP-hard:** at least as hard as the hardest NP problems; a warning that exact
  search may be impractical at scale.
- **Tractability:** whether exact computation remains practical as problem size
  grows.
