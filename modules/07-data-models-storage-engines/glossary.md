# Module 7 Glossary

| Term | Operational meaning |
|---|---|
| Access path | Physical route used to find records for an operation, such as a scan, tree traversal, hash probe, or inverted posting list. |
| Amplification | Physical work or space divided by the logical work or live data requested by the application. |
| Bloom filter | Probabilistic membership filter with false positives but no false negatives for correctly inserted keys. |
| Buffer pool | Database-owned cache of pages with explicit replacement, pinning, and dirty-page policy. |
| Compaction | Background merge that reconciles sorted runs, discards obsolete versions, and moves bytes to a new layout. |
| Compaction debt | Work required to restore the intended LSM shape after ingest or deletion outpaces compaction. |
| Covering index | Index containing all columns needed by an operation, permitting an index-only path when visibility rules allow. |
| Evidence kind | Label that bounds a result, such as measured Python/file-system evidence rather than device or production evidence. |
| Inverted index | Mapping from a term or token to the records containing it. |
| LSM tree | Write-optimized structure that buffers updates, flushes sorted runs, and reconciles them through compaction. |
| Logical bytes | Application key/value bytes accepted by put or delete operations, before storage-engine maintenance. |
| Page | Fixed-size unit of storage management and caching. |
| Point lookup | Lookup for one exact key. |
| Range scan | Ordered iteration over keys between declared bounds. |
| Read amplification | Physical page or block probes divided by logical reads. |
| Selectivity | Fraction of candidate rows expected to satisfy a predicate. |
| Space amplification | On-disk bytes divided by live logical bytes. |
| Sparse index | Index containing selected fence keys and offsets rather than one entry per record. |
| SSTable | Immutable sorted-string table produced by an LSM flush or compaction. |
| Tombstone | Deletion marker that must dominate older values until compaction can discard both safely. |
| Write amplification | Physical bytes written by the engine divided by logical bytes written by the application. |
| Write stall | Admission delay or rejection used when flush or compaction cannot keep up with writes. |

Terms describe mechanisms, not guaranteed implementations. A vendor may use a
name differently; inspect its documented and measured behavior.
