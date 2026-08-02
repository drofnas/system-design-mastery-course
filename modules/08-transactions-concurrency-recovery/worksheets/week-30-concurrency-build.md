# Week 30: Concurrency Build and Internals Review

Implement the chosen business invariant with an explicit transaction API.
Record runtime, database/version if used, isolation configuration, schema,
constraint definitions, transaction pseudocode, and test commands.

Demonstrate lost-update and write-skew schedules, lock waits, deadlock victim,
complete rollback, bounded whole-transaction retry, authorization recheck, and
cleanup. Preserve read/write sets and raw traces. Explain which behavior is
application, database, or vendor-specific and identify starvation or overload
bounds. Review the lab's visibility, lock, WAL, and recovery code without
claiming production completeness.
