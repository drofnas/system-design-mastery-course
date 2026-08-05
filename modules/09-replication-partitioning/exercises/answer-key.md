# Module 9 Explained Answer Key

Open only after freezing the matching exercise. These are reasoning boundaries,
not one required architecture.

## EX-01: Operation histories

A complete history shows enough ordering to falsify the outcome. Controller
transfer fails if two sides acknowledge different owners. Operator refresh
fails if the same session reads v2 then v1. Public browse fails only when its
declared staleness bound is exceeded. Annotation reply fails if B is visible
without causal parent A. Names alone receive little credit.

## EX-02: Weakest sufficient contract

One defensible set is linearizable authority for controller transfer,
read-your-writes plus monotonic reads for operator refresh, 30-second/two-version
bounded staleness for browse, and causal visibility for replies. Returning an
explicit error or marked-stale result must be part of the contract. Linearizing
all browse reads is likely unjustified without evidence.

## EX-03: Acknowledgement trace

The trace must keep receipt, local persistence, remote receipt, remote durable
storage, acknowledgement, and read visibility separate. "Two replicas" is
insufficient unless failure-domain independence and durability are known.

## EX-04: Topology comparison

Leader/follower reduces write conflicts but makes leader reachability and lag
material. Multi-leader supports local/disconnected writes but transfers conflict
semantics to metadata and application owners. Leaderless exposes R/W choices
and repair but requires stable membership, comparison, and convergence. A valid
answer uses the same workload and acknowledgement boundary for all three.

## EX-05: Quorum arithmetic

- `(3,2,2)`: 2+2>3 and 2×2>3; both intersections hold.
- `(5,4,2)`: 4+2>5, but 2×2 is not >5; read/write only.
- `(5,2,3)`: 2+3 is not >5, but 2×3>5; write/write only.

Equality is not intersection; the comparison is strictly greater.

## EX-06: Broken quorum assumptions

Stale maps mean sets may not share N. First-response reads do not necessarily
observe the intersection. Volatile acknowledgements do not establish durable
copies. A sloppy substitute may intersect outside the normal replica set.
Arithmetic remains true for the named sets but the claimed protocol property
does not follow.

## EX-07: Concurrent siblings

West and east v2 are concurrent siblings because both descend from v1 and
neither descends from the other. Preserve both. A merge record names both parent
identities, the authorized resolver, deterministic merged value, and resolution
version. Replaying the same merge must not create a new semantic change.

## EX-08: Repair coverage and budget

Read repair follows access and can miss cold keys; anti-entropy scans intended
ownership and costs background resources. Raw payload is 10,000 KiB. At 200
KiB/s the lower bound is 50 seconds, excluding comparison metadata, protocol
overhead, retransmission, reads, and foreground admission.

## EX-09: Placement comparison

Exact owners follow the published lab hash function, not mental arithmetic.
The evidence must include old/new node sets, all keys, moved count, and
`moved/total`. The test establishes that the fixture's consistent-hash method
moves fewer keys than modulo; it does not prove balance for every workload.

## EX-10: Reshard gate table

Every gate needs entry evidence, success threshold, stop/rollback action, and
owner. Copy is not cutover. Verification covers versions, counts/digests,
permissions, and business invariants. Decommission follows the rollback window,
not the first successful read.

## EX-11: Session lag diagnosis

Observed `[2,1]` contains one monotonic regression, and version 1 is one
read-your-writes violation relative to minimum 2. A token-aware router selects a
replica at least v2, waits inside the deadline, or returns an explicit failure.

## EX-12: Ambiguous acknowledgement

Blind retry may duplicate the logical effect. Read-back can determine whether
version/effect exists if identity and authority are queryable. An idempotency
record can return the original outcome when scope, fingerprint, atomicity,
retention, and authorization are correct. No response alone proves neither
commit nor non-commit.

## EX-13: Hot-key and tenant fairness

Max/min is `120/5 = 24`; max/mean is `120/(130/3) ≈ 2.769`. Immutable public
reads can use authorized replicas/cache with a freshness rule. Reserve private
capacity and reject excess public work at the scarce resource. Salting
controller ownership would be unsafe.

## EX-14: Partition decision matrix

The matrix must be operation-specific. Public browse may succeed on both sides
with version/staleness markers; annotation writes may accept only on an eligible
quorum or preserve siblings under an explicitly weaker contract; controller
changes fail without known authority; private data also obeys region eligibility.
Post-heal repair has an owner and convergence oracle.

## EX-15: Regional placement and cost

A credible inventory includes every durable and derived copy plus keys and
human access. Arithmetic shows units, copy count, retention, compression,
transfer, repair frequency, and sensitivity. The legal/security policy owner
approves constraints; platform owners implement and prove them.

## EX-16: ADR and defense rehearsal

Full-credit work links each choice to a history, experiment, source, cost, and
owner; compares alternatives with shared drivers; and preserves dissent.
Migration includes mixed-version compatibility and verified rollback. A
reversal threshold is measurable, such as session violations above zero for an
authoritative operation or p99 coordination exceeding its allocated budget.

## PESD 2.0 extension answer

A defensible answer covers tenant onboarding, suspension, export, offboarding, region movement, cells, control-plane/data-plane separation, tenant keys, quotas, SLOs, and cost attribution. It distinguishes the
requirement, enforcement mechanism, evidence, and owner; keeps modeled and
measured results separate; and names the failed condition that would reverse
the decision. Different architectures are acceptable when their invariants,
evidence boundaries, migration, and residual risk are explicit.
