# Module 8 Explained Answers

These answers explain Northstar reasoning and acceptable variation. They do not
specify commerce transactions or a canonical capstone architecture.

## EX-01

N-02 fits uniqueness; N-03 needs one result/audit transaction plus a
completeness oracle; N-01 spans rows and needs serializable validation or safe
materialization. N-05 treats result rows as authority and summary as derived.
N-04/N-06 require log/restore evidence, not a schema label. Owners differ across
application, database, security, and incident response.

## EX-02

Result and audit commit together. Summary and notification carry provenance and
reconcile. A physical telescope command occurs outside the database; persist an
idempotent intent and verify its outcome. A wider local transaction cannot roll
back a physical action.

## EX-03

Both transactions read 0 and write 1, so the second write replaces rather than
combines the first. Expected authoritative result count is 2; observed counter
is 1. Atomic increment, lock, version validation, or rebuilding a derived
counter are valid repairs with different costs.

## EX-04

Each transaction reads A+B and writes a different controller row. The
read/write dependencies form a cycle even without same-row writes. Serializable
validation can abort one; a coverage row makes both writes conflict but creates
a hotspot and migration cost.

## EX-05

Shared/shared is compatible; exclusive conflicts with shared/exclusive. Actual
mode names vary by DBMS. Exclusivity should ultimately be enforced by a unique
or exclusion constraint so absence races do not bypass an application lock.

## EX-06

T1→T2 and T2→T1 is a cycle. The victim choice is not portable. Roll back the
victim completely, release resources, recheck authorization/deadline, apply
capped jitter, and restart the whole transaction. Canonical order reduces this
specific cycle.

## EX-07

Both initial snapshots see A+B. After T1 commits, T2's old snapshot remains
unchanged. Serializable validation detects that T2's assumption conflicts with
T1; T2 aborts. Its retry gets a fresh snapshot and refuses to remove B.

## EX-08

With equal work per attempt, useful-work fractions are roughly 99%, 90%, and
60% before retry amplification. Real cost depends on conflict correlation,
transaction duration, retry collision, and read-only work. A reversal threshold
must be tied to measured abort tail and useful throughput.

## EX-09

Use uniqueness/exclusion for one controller per telescope window and keys/
foreign keys for result/audit identity where the schema supports it. A simple
row constraint cannot count certified controllers across multiple mutable rows.

## EX-10

One transaction writes result and audit or neither. A device command needs a
durable intent, scoped idempotency, bounded execution, outcome record, and
reconciliation because the device is outside the database commit protocol.

## EX-11

Before commit, no success may be claimed; stolen loser updates need undo. A
durable commit whose page is absent needs redo. After flush-before-ack, retry
may occur because the client did not hear success, so idempotency is necessary.
After acknowledgement, loss violates the durability promise.

## EX-12

Ideal minimum flushes are 64, 16, and 4. This ignores arrival timing, maximum
batch wait, log bandwidth, flush latency distribution, failures, and whether
all commit records fit before each flush boundary.

## EX-13

Archive continuity ends at 125; 126 breaks recovery toward 140. The last safe
target is 125 unless another valid source supplies 126. RPO is the authoritative
operations after 125 through the required restore target, not merely elapsed
wall time.

## EX-14

Fail closed on version/identity/checksum/archive gaps; transaction and business
invariant failures; missing credentials/audit isolation; stale derived state;
incompatible dependencies; or failed user journey. Each probe needs an owner,
timestamp, evidence path, and explicit traffic decision.

## EX-15

Strong work preserves prediction and raw trials, proves pair hashes, checks
correctness before latency, proposes alternative causes, changes one control,
and records uncertainty. F04 and F07 cannot generalize local timings to
production hardware or data volume.

## EX-16

A defensible matrix maps each invariant to authority, constraint/isolation,
retry, durable acknowledgement, backup, tested target, telemetry, owner, cost,
migration, rollback, and reversal. Different designs pass when their evidence
supports the same published drivers and failure model.

## PESD 2.0 extension answer

A defensible answer covers retention, deletion, legal holds, key rotation, logs, replicas, exports, backups, restore-time policy replay, and resurrection prevention. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
