# Northstar Observatory Catalog Evolution Program

This completed case demonstrates one defensible Module 14 decision on a
non-commerce system. It is not a canonical architecture. Do not transfer its
boundaries, contracts, costs, teams, thresholds, or sequence into the commerce
optional project.

## Outcome, workload, and current state

Northstar's operations registry validates observations, approves publication,
builds the public catalog, and emits subscriber bulletins. The registry owns
the authoritative accepted observation and publication decision. The catalog
and bulletins are derived.

The established workload is 18,000 catalog reads and 1,200 validated
publications per night, with a 20× clearing-sky publication burst. A good catalog
read is correct, at the declared registry version or newer, no more than two
minutes stale, and served within 600 ms.

The six-person registry team owns validation, scheduling, publication, catalog,
privacy operations, and the overnight on-call surface. A new five-person
research-access team owns researcher discovery but waits for registry releases.
Over the last twelve releases, eight catalog changes required coordination;
three waited more than ten working days. Two catalog incidents also consumed
registry capacity during active observation recovery.

## Boundary ledger and alternatives

| Driver | Evidence | Independence sought | New cost |
|---|---|---|---|
| Change | 8/12 releases coordinated; 3 delays >10 days | Research access releases catalog independently | Contract and consumer testing |
| Failure | Derived catalog incidents distract registry recovery | Catalog degrades without blocking authority | Queue, replay, projection recovery |
| Workload | Publication burst differs from registry writes | Scale projection separately | Duplicate capacity |
| Data | Publication approval must remain transactional | No new publication authority | Lag and reconciliation |
| Security | Public data is narrower than private registry | Smaller read trust surface | Event and credential controls |
| Ownership | Research access has roadmap and on-call capacity | End-to-end catalog ownership | Handoff and secondary operators |

Northstar compares:

1. **Modular monolith.** Extract a catalog module and ownership contract inside
   the registry deployment. Lowest cost and simplest consistency, but release
   coordination remains.
2. **Synchronous catalog service.** Independently deploy queries and projection,
   but a publication-time remote call risks coupling registry progress to a
   derived system.
3. **Event-driven projection.** Registry commits approval and a transactional
   outbox fact; research access builds catalog and bulletin state. Adds lag,
   replay, contract, and operational cost but preserves authority and failure
   decoupling.

Northstar first creates the modular seam. It extracts deployment only after
shadow evidence and ownership gates pass. This makes the first increment useful
even if the final extraction stops.

## Social architecture and sourcing

The teams collaborate for two increments to define the accepted-observation
contract, backfill, comparison, and incident boundaries. Collaboration expires
after compatibility, replay, rollback, and on-call exercises pass. The registry
then provides a versioned fact; research access consumes it as a service
interaction. The observatory platform group facilitates the initial event lane
and exits after the self-service runbook is proven.

Northstar compares managed messaging, self-operated messaging, database polling,
and the existing platform event lane. It selects the platform lane because it
already has staffed replay, tenant isolation, telemetry, and recovery. The
decision still records quotas, per-message cost, portable JSON contracts, a
fact export, a polling fallback, and a 90-day replacement estimate.

## Fully loaded economics

Synthetic monthly comparison inputs are:

| Cost class | Modular | Event projection | Allocation |
|---|---:|---:|---|
| Direct and shared platform | $9,000 | $15,000 | Catalog CPU/storage/message share |
| Engineering and operations | $16,000 | $24,000 | Loaded capacity assigned to catalog |
| Expected incident exposure | $5,000 | $3,000 | Frequency × bounded impact estimate |
| Transition amortized over 12 months | $0 | $12,000 | $144,000 one-time migration |
| Good catalog reads | 530,000 | 538,000 | Correct, fresh, within latency |

Current comparison cost is $30,000 / 530,000 × 1,000 = **$56.60 per 1,000
good reads**. During transition the candidate is $54,000 / 538,000 × 1,000 =
**$100.37**. The extraction is not justified as infrastructure savings. It buys
delivery independence and lower registry blast radius at a temporary premium.

The stop threshold is $105 per 1,000 good reads for two consecutive monthly
windows. A 4× event-price shock crosses it unless traffic or retention changes.
If transition cost does not disappear after twelve months, the strategy returns
to review. Security, publication correctness, freshness, and availability remain
guardrails and cannot be traded away to meet cost.

## Compatibility and expand-contract

Accepted-observation v1 contains `public: boolean`. V2 adds optional
`publication_scope` while retaining `public`. New consumers accept both; old
consumers ignore the new field. Producers emit both until the inventory shows
no v1-only live, delayed, or replay consumer for one full retention window.

Contraction is a separate later release. A major version communicates the
intent to remove `public`; contract tests, consumer telemetry, stored-event
inventory, and rollback review prove whether it is safe. SemVer alone is not
evidence of runtime compatibility.

## Migration state machine

| State | Authority/read path | Exit gate | Rollback |
|---|---|---|---|
| Baseline | Registry writes and serves | Baseline frozen | None needed |
| Expand | Registry writes v1+v2/outbox | Mixed-version tests | Disable new emission |
| Backfill | Registry remains authority; candidate derived | Counts, IDs, versions, hashes reconcile | Drop candidate derived state |
| Shadow | Old catalog serves; candidate effects isolated | Segmented mismatch, SLO, cost gates | Stop shadow |
| Cutover | 5%, 25%, 50%, 100% reads to candidate | Observation window at each stage | Route only if old reader preserves new state |
| Contract | Candidate serves; old compatibility observed absent | Retention and rollback windows expire | Restore expanded form |
| Decommission | Old reads/writes/access/cost removed | Absence and recovery review | Rebuild from authoritative facts |

The outbox fact includes observation ID, registry version, contract version,
tenant/public scope, and idempotency key. Projection writes apply only when the
registry version is newer.

Backfill snapshots stable IDs and versions, processes batches of 500, and
persists the cursor only after projection effects. Restart may repeat a batch.
Idempotency and version guards make repetition safe. Reconciliation covers
count, missing/extra IDs, version lag, scoped content hashes, and bulletin
effect ledger.

## Shadow, cutover, and rollback

Northstar shadows 10% of catalog reads and 100% of accepted-observation events.
It normalizes ordering, generated request IDs, and timestamps. Promotion needs:

- zero authority, tenant, or publication-scope mismatches;
- less than 0.1% explained presentation mismatch;
- freshness within two minutes and p95 within 600 ms;
- unit cost no more than $105 per 1,000 good reads;
- primary and two secondary operators with successful replay and rollback drills.

A proposed target-only `display_alias` write makes traffic reversal lossy. The
cutover stops until the old reader can preserve that field. Northstar does not
call a routing change a rollback when state cannot return safely.

## Failure and repair summary

| Pair | Broken observation | Repair |
|---|---|---|
| F01 | v2-only event reaches v1 consumer | Backward-compatible envelope and matrix |
| F02 | `public` removed while old reader remains | Expand, observe absence, contract later |
| F03 | crash advances cursor before durable batch | Post-effect checkpoint and idempotency |
| F04 | two independent writes diverge | Registry authority plus outbox/reconciliation |
| F05 | promotion ignores segmented mismatch | Comparison gate blocks cutover |
| F06 | target-only state makes old path lossy | Tested rollback compatibility before cutover |
| F07 | 4× price spike omitted from unit cost | Complete allocation and stop threshold |
| F08 | quota/price failure has no exit | Portable contract/data and exercised fallback |
| F09 | registry experts leave | Secondary access, runbook, handoff, and exercise |

## Strategy and stopping conditions

The sequence is instrument → modularize → expand contract → backfill and shadow
→ bounded cutover → contract → decommission. Each increment can stop without
pretending the target architecture is inevitable.

The strategy stops or reverses when coordination delay does not improve,
publication authority becomes ambiguous, compatibility or reconciliation fails,
rollback is lossy, unit cost crosses its threshold, the dependency exit is not
executable, or ownership continuity fails. Alternatives remain defensible when
their evidence better fits another environment.
