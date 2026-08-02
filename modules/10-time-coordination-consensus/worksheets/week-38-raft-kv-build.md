# Week 38 Worksheet: Raft-Backed Key/Value Build

## Observable contract

Implement in a chosen stack or operated system. Match the public scenario/trial
fields without copying Northstar policy values.

## State inventory

| State | Volatile/durable | Write-before-response boundary | Snapshot inclusion | Recovery probe |
|---|---|---|---|---|
| current term and vote | | | | |
| log entries | | | | |
| commit/applied indexes | | | | |
| key/value state | | | | |
| client sequence/results | | | | |
| fencing maximum | | | | |
| membership phase | | | | |

## Protocol traces

Provide one successful and one rejected trace for `RequestVote`, `AppendEntries`,
client command, linearizable read, snapshot install, and membership change.

## Safety proof ledger

| Property | Implementation rule | Observable evidence | Counterexample test | Exclusion |
|---|---|---|---|---|
| election safety | | | | |
| log matching | | | | |
| leader completeness | | | | |
| state-machine safety | | | | |

## Automated checks

Record command, environment/version, test names, pass/fail output, and hashes.
Do not convert a test result into a production guarantee.

## Internals review

Trace persistence, message handling, concurrency/cancellation, deterministic
application, error paths, telemetry, security boundary, and resource bounds.
