# Module 11 Glossary

- **Authoritative fact:** state whose loss or contradiction changes the
  business truth; derived state must be rebuildable from it.
- **Command:** a request to attempt a state transition; it may be rejected.
- **Event:** an immutable claim that a named fact or transition occurred under
  a stated authority and version.
- **Queue:** work distribution in which successful handling normally removes
  or hides an item from that consumer population.
- **Log:** an ordered append-only sequence retained independently of one
  consumer's progress.
- **Stream:** an unbounded sequence plus processing semantics; the word alone
  says nothing about durability, order, or delivery.
- **Consumer group:** consumers sharing partitions or work under one logical
  subscription and progress contract.
- **Partition key:** the field used to route related records to an ordering and
  scaling unit.
- **Offset:** a position in a log; it is not proof that an external effect
  succeeded.
- **At-most-once:** processing may be lost but is not retried within the stated
  boundary.
- **At-least-once:** accepted work is retried, so a consumer must tolerate
  duplicates within the stated boundary.
- **Exactly once:** one logical result inside named transactional participants;
  it is not a universal property of arbitrary external effects.
- **Transactional outbox:** business facts and event-intent rows committed in
  the same local transaction.
- **Inbox:** consumer-side durable identity record used to make local
  application idempotent.
- **Change data capture (CDC):** deriving a change stream from a database log or
  equivalent ordered commit record.
- **Replay:** reapplying retained records from a chosen position under explicit
  code, schema, effect, and ownership controls.
- **Poison record:** a record that repeatedly fails for a stable reason; it
  needs classification and ownership, not infinite retry.
- **Dead-letter store:** quarantined evidence and work; placement there is not
  resolution.
- **Saga:** a long-running workflow of local transactions with recorded forward
  progress and application-specific compensation where possible.
- **Compensation:** a new business action that addresses earlier effects; it is
  not necessarily rollback to the original state.
- **Event time:** time assigned to the domain event.
- **Processing time:** time at which a processing system observes or acts on the
  event.
- **Watermark:** an estimate or assertion about event-time completeness under a
  stated source contract.
- **Lag:** distance or age between produced and consumed positions.
- **Reconciliation:** comparing derived/effect state with authority and issuing
  audited repair work.
