# Northstar Repeat Calibration Fixture

## Submission identity and chronology

Manifest `manifests/repeat.json` omits frozen A01/A04 chronology. Predictions
were edited after the runtime was known and raw F06/F07 output was replaced.

## Equivalent contract and four runtimes

The Rust build is missing. Node skips runtime validation and counts malformed
responses as success. Java runs with twice the memory and Go performs fewer
children, so the comparison is not equivalent.

## Memory, scheduler, visibility, and boundary evidence

Offered work spawns before admission. The repaired Go service still writes a
shared map without synchronization. Missing cancellation leaves child work
active after the caller deadline, and an exception path leaves responses open.

## Failure and measurement evidence

Several pairs change workload and multiple controls. Broken input hashes differ
from repairs; F06–F08 repaired target invariants remain failed. The report calls
a clean sample proof and claims Rust has no leaks because it has no tracing GC.

## Decision, defense, and Gate 5

The decision selects Rust as universally fastest without a complete build,
security operations, migration, owner, rollback, or reversal. Gate 5 is missing.
The unsafe evidence and broken chronology require Repeat with new frozen work.
