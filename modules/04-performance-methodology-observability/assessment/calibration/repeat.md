# Transit Signal Calibration Submission: Invalid

## Submission identity

- Artifact commit: `9c8d7e6-repeat`
- No frozen baseline commit or environment record is supplied.
- The document says an AI tool "cleaned up" the raw files.

## Investigation claim

The service was slow, so the database was optimized. No user percentile,
workload boundary, useful-work definition, hypotheses, or falsifier is frozen.

## Fault workflow

The learner opened each fixture definition, copied its `fault.kind` into the
diagnosis table, and then collected screenshots. There is no diagnosis commit
before reveal and no alternative or discriminating test.

## Telemetry evidence

Only summary charts remain. Raw traces, metrics, logs, profiles, metadata, hashes,
and schemas are absent. The chart reports 120 successes while the text says 100.
`request_id`, rider email, and an authorization token appear as metric labels.
The connection-leak run is terminated without cleanup evidence.

## Benchmark and change

One before timing is compared with one after timing. The after version removes a
route branch and has a different response checksum. The report calls the 40%
timing difference a production-safe improvement and defines no regression budget.

## Decision and defense

The recommendation is to deploy globally. There is no owner, cost, failover,
privacy, retention, migration, canary, rollback, or reversal condition. During
review, the workload changes whenever a question challenges the conclusion.
The required distinct A11 regression-policy ADR is absent; the benchmark report
is incorrectly relabeled as both experiment evidence and a decision record.
