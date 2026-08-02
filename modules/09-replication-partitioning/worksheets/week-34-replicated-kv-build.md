# Week 34 Replicated Key/Value Build

1. Expose topology, replication factor, read/write policy, versions, and acknowledgement events.
2. Implement at least two replication modes and selectable session behavior.
3. Preserve concurrent siblings unless a documented domain merge is valid.
4. Implement read repair or anti-entropy with convergence and foreground-cost evidence.
5. Implement hash, range, and consistent-hash placement plus a membership-change calculation.
6. Emit schema-valid trials with environment, evidence kind, shared-input/config hashes, and uncertainty.
7. Add deterministic tests; explain what the build deliberately excludes.
8. Write an internals review tracing one write, read, conflict, repair, and reshard.
