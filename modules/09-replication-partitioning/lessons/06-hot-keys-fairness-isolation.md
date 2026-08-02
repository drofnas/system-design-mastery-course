lesson_id: L06

# Hot Keys, Skew, Fairness, and Tenant Isolation

## Outcomes

- Distinguish key-count balance from request, byte, CPU, and repair balance.
- Select a hotspot response compatible with operation semantics.
- Protect tenant confidentiality, integrity, and capacity under skew.

## Prerequisites

Module 2 useful throughput/admission control, Module 6 fairness and bounded
concurrency, and Lesson 5 placement metrics.

## Mechanism and decision procedure

A partitioner balances its input metric, often key count or hash space. Workload
cost is multi-dimensional: requests, bytes, read/write ratio, fan-out, storage,
repair, compaction, and tenant priority. Measure all relevant dimensions by key,
partition, node, replica role, tenant, and operation.

Use this procedure:

1. Confirm equivalent useful work and identify the saturated resource.
2. Rank keys and tenants by request and resource share.
3. Determine whether the key can be split without breaking atomicity or order.
4. Choose among cache/replica reads, key salting, subpartitioning, aggregation,
   batching, admission control, tenant reserves, or product degradation.
5. Model write/read amplification and consistency consequences.
6. Bound mitigation state, expiry, migration, and operating ownership.

Read-heavy immutable keys may be cached or served from followers under a
freshness rule. Commutative counters may be sharded and aggregated if temporary
divergence is acceptable. Exclusive ownership cannot be salted into independent
authorities. A celebrated object's metadata may be separated from its large
append-only observation set. No generic "hot-key splitting" rule exists.

Tenant isolation has three dimensions. Confidentiality constrains where data
may be stored and who may read it. Integrity constrains who may write or merge.
Availability constrains how one tenant's load, repair, or reshard traffic can
consume shared capacity. Enforce quotas and reserves at the scarce resource,
not only at an outer API.

## Worked example

A new transient object drives 96% of Northstar public reads to one key while a
private tenant needs controller metadata. The broken design sends all reads to
the owner: n1 handles 120 units while n2/n3 handle 5 each. The repaired policy
serves public immutable metadata from three authorized replicas, reserves
private capacity, and rejects four excess public requests before private work.
The ratio improves, but Northstar records additional replica traffic and cache
invalidation obligations.

Northstar does not salt controller-window ownership because that would create
multiple writers for one invariant.

## Common expert mistakes

- **Counting keys instead of cost:** one key can dominate all useful work.
- **Adding replicas to a write-hot linearizable key:** the authority still
  serializes writes and replication may add cost.
- **Rate limiting only by tenant request count:** expensive operations remain unfair.
- **Letting background repair bypass admission:** recovery work can cause an outage.
- **Treating isolation as authentication only:** shared capacity and placement
  can leak or deny service across tenants.

## Guided practice

Given per-node load 120/5/5, calculate max/min and max/mean ratios. Propose two
repairs for an immutable read-hot key and reject one unsafe repair for exclusive
ownership. Allocate capacity among public, private, and repair traffic.
Complete EX-11 through EX-13.

## Self-check

1. Can equal key counts imply equal load?
2. When is key salting unsafe?
3. Where should a fairness control be enforced?
4. Why is repair traffic part of tenant capacity planning?

## Explained answers

1. No; frequency, bytes, and cost can be arbitrarily skewed.
2. When operations require one authoritative value, total order, or atomic
   update that independent salts cannot preserve.
3. At or before the scarce resource, with tenant/operation identity retained.
4. It consumes the same storage, network, I/O, and CPU and may be triggered by
   one tenant's placement or failure history.

## Sources and next work

Read the Meta Shard Manager case and the DynamoDB paper's traffic-imbalance and
fairness sections. Next scope partition and normal-operation trade-offs with
CAP/PACELC and regional constraints.
