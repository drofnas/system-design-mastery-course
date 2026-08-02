# Week 27 Workload and Amplification Matrix

## Frozen experiment contract

- Baseline commit and scenario hashes:
- Runtime/filesystem/evidence kind:
- Ratio definitions and included bytes/probes:

## Workload matrix

For both engines preserve raw read-, write-, range-, skew-, and delete-heavy
trials. Record operation counts, p50/p95/p99/max, page/block probes, cache,
logical/physical bytes, amplification, runs, compaction, tombstones, live/disk
bytes, correctness, and cleanup.

## Six failure pairs

For F01–F06 record prediction, shared input fingerprint, one changed variable,
raw observations, at least two causal explanations, smallest discriminating
check, repaired result, same-input proof, recovery, and uncertainty.

## Integrity and safety

Point/range/reopen results must equal the reference map; deleted values must not
reappear. Never rewrite raw JSON or the pre-result hypothesis.

## Reflection

Which average hid the most important tail or maintenance behavior?
