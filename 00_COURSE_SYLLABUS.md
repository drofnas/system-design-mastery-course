---
title: "Principal Engineer and Systems Design Mastery"
subtitle: "Course Outline and Syllabus"
course_id: "PESD-72"
version: "1.0"
duration_weeks: 72
standard_hours_per_week: "10–12"
format: "Self-study, project-based"
status: "Ready to begin"
tags:
  - principal-engineering
  - system-design
  - distributed-systems
  - performance
  - architecture
  - ai-systems
---

# Principal Engineer and Systems Design Mastery

## Course Outline and Syllabus

## 1. Course purpose

This course develops the judgment expected of a Principal Software Engineer who directs architecture across stacks, explains trade-offs from first principles, and improves decisions across teams.

You will study the physical limits, correctness guarantees, failure modes, operating constraints, costs, and organizational factors behind software architecture. Each module requires you to model a system, build a working mechanism, test it under failure, and defend a decision with evidence.

The course uses implementation to expose how systems behave. It uses written decisions and design reviews to train the work that Principal Engineers perform with other teams.

Completing the course does not confer a job title. Principal-level scope also requires production ownership, sustained influence, sound decisions under uncertainty, and results that span team boundaries. The course gives you a structured way to build and demonstrate those capabilities.

## 2. Target learner

This course fits an experienced software engineer who can design and ship applications but wants stronger command of:

- System behavior under load and failure
- Database and distributed-system internals
- Performance diagnosis from application code through hardware
- Reliability, security, recovery, and cost
- Architecture across unfamiliar languages and runtimes
- Browser, frontend, CDN, and edge systems
- AI retrieval, inference, and agent architecture
- Technical strategy, migration design, and cross-team decisions

The expected starting point is senior-engineer competence in at least one production stack. You do not need prior experience implementing a database, a consensus protocol, or a model-serving system.

## 3. Graduate profile

By the end of the course, you should be able to:

1. Turn a product goal into workloads, invariants, quality-attribute scenarios, and acceptance criteria.
2. Estimate throughput, concurrency, storage, bandwidth, availability, recovery exposure, and unit cost.
3. Trace latency and resource use through CPUs, memory, operating systems, networks, storage engines, and application runtimes.
4. Select storage, replication, partitioning, indexing, and transaction strategies from workload evidence.
5. Reason about consistency and availability for each operation instead of assigning one label to an entire product.
6. Design bounded retries, deadlines, queues, concurrency, backpressure, load shedding, and idempotency.
7. Analyze safety, liveness, durability, and recovery under a stated failure model.
8. Diagnose performance and reliability problems with measurements, profiles, traces, logs, query plans, and controlled experiments.
9. Design secure trust boundaries, authorization models, tenant isolation, audit trails, and data lifecycles.
10. Compare monoliths, services, event-driven systems, managed products, and custom components using delivery and operating costs.
11. Review unfamiliar or AI-generated code through its memory, execution, concurrency, type, and failure models.
12. Design browser and edge architectures around rendering, caching, responsiveness, accessibility, and observability.
13. Evaluate vector retrieval, RAG, model serving, and agent workflows as probabilistic distributed systems.
14. Plan migrations that preserve service, data, and rollback safety.
15. Write ADRs and RFCs that make assumptions, alternatives, evidence, risks, and reversal conditions clear.
16. Lead an architecture review, resolve disagreement, and teach the reasoning to engineers outside your immediate stack.

## 4. Definition of mastery

You will demonstrate each important concept at five levels:

| Level | Capability | Evidence |
|---|---|---|
| 1. Define | Explain the mechanism and use precise terms | Concept notes and oral explanation |
| 2. Calculate | Estimate behavior, limits, probability, and cost | Capacity model or worked analysis |
| 3. Implement | Build a small version that exposes the mechanism | Source code and automated checks |
| 4. Diagnose | Find a bottleneck or correctness failure from evidence | Experiment report and telemetry |
| 5. Decide and teach | Choose an approach, defend it, and help others apply it | ADR or RFC, review, and teach-back |

Reading can establish the first level. Course completion requires evidence at the fifth level for the main architecture topics.

## 5. Course principles

### 5.1 Start with constraints

Each design begins with users, business outcomes, workloads, invariants, failure assumptions, security boundaries, and operating constraints. Technology choices follow.

### 5.2 Quantify claims

Terms such as *fast*, *scalable*, *available*, and *cost-effective* need thresholds and measurement methods. You will attach a unit, time window, percentile, workload, or budget to each claim.

### 5.3 State the failure model

A system cannot promise safety or recovery without naming the faults it covers. You will specify process crashes, restarts, network loss, partitions, stale reads, disk faults, zone loss, operator error, and dependency failures as needed.

### 5.4 Preserve invariants

You will identify the facts that must remain true and trace each one through storage, caches, messages, retries, failover, migrations, and human operations.

### 5.5 Prefer evidence over labels

Architecture names do not settle decisions. Measurements, proof sketches, failure tests, delivery constraints, and operating experience carry more weight.

### 5.6 Include people and ownership

Deployable boundaries create ownership, coordination, and cognitive-load costs. You will name who builds, operates, secures, and changes each part of a design.

### 5.7 Design for change

You will record reversal conditions, migration paths, compatibility rules, and decommission plans. A sound decision accounts for the system you have and the next credible state.

## 6. Prerequisites

### Required experience

- Proficiency in one programming language
- Experience building or maintaining a production application
- Working knowledge of HTTP, SQL, source control, tests, and deployment
- Familiarity with logs and application metrics
- Ability to read technical documentation and source code

### Mathematics

You should know algebra, functions, exponents, logarithms, basic probability, and descriptive statistics. The course introduces the linear algebra and calculus needed for the AI modules.

### Recommended environment

- A Unix-like development environment
- Containers or virtual machines for isolated experiments
- A relational database
- A key/value or log-structured store
- A load generator
- Metrics, tracing, and profiling tools
- Network fault-injection tools
- Enough local or cloud compute for small AI retrieval and inference experiments

You may substitute tools when your environment imposes limits. Record the substitution and explain which behavior it changes.

The complete supported home-computer baseline, macOS/Linux/Windows-through-WSL2
setup, module dependency matrix, and read-only preflight are in
[`HOME_LAB_GUIDE.md`](HOME_LAB_GUIDE.md). A discrete GPU and multi-machine lab
are not required.

## 7. Time commitment and pacing

### Standard track

- Duration: 72 weeks
- Effort: 10–12 hours per week
- Total effort: about 800 hours
- Best fit: full-time engineers studying alongside work

### Accelerated track

- Duration: 48–52 weeks
- Effort: 15–18 hours per week
- Combine reading and implementation weeks, but keep the failure experiments and decision reviews.

### Extended track

- Duration: 90–104 weeks
- Effort: 6–8 hours per week
- Split builds across two weeks and preserve the assessment gates.

If work or life interrupts the schedule, pause at the end of a module. Do not skip its failure experiment or decision artifact to recover calendar time.

### Suggested weekly budget

| Activity | Hours |
|---|---:|
| Primary reading and concept notes | 2–3 |
| Implementation | 3–4 |
| Experiments and measurement | 2 |
| ADR, RFC, or technical report | 1–2 |
| Review, teach-back, and learning log | 1 |

## 8. Learning cycle

Each four-week module follows one cycle.

| Week | Focus | Required evidence |
|---:|---|---|
| 1 | Model | Vocabulary, assumptions, diagrams, estimates, and source review |
| 2 | Build | Minimal implementation or focused modification of an existing system |
| 3 | Break and measure | Load, skew, crashes, delay, loss, duplication, saturation, or misuse |
| 4 | Decide and teach | ADR or RFC, design defense, peer feedback, and revision |

You may use a production system for a module if you can experiment without putting users or company data at risk. Otherwise, build a lab system that isolates the mechanism.

## 9. Curriculum map

| Phase | Weeks | Theme | Modules |
|---|---:|---|---:|
| I | 1–16 | Engineering judgment and physical limits | 1–4 |
| II | 17–32 | Networks and persistence | 5–8 |
| III | 33–44 | Distributed systems and asynchronous correctness | 9–11 |
| IV | 45–56 | Production architecture and technical strategy | 12–14 |
| V | 57–64 | Polyglot, browser, and edge systems | 15–16 |
| VI | 65–72 | AI systems and final defense | 17–18 |

## 10. Detailed course outline

### Phase I: Engineering judgment and physical limits

#### Module 1, Weeks 1–4: Architectural judgment

**Core questions**

- Which user and business outcomes define success?
- Which facts must remain true across faults and change?
- Which quality attributes need measurable scenarios?
- Which decision would new evidence reverse?

**Topics**

- Problem framing and system context
- Functional requirements and quality attributes
- Workload dimensions and traffic shapes
- Business, data, security, and operational invariants
- Constraints, assumptions, and decision drivers
- State ownership and system boundaries
- Architecture Decision Records and Requests for Comments
- Reversibility and evidence thresholds

**Build**

Create a baseline design for a commerce platform or a system from your work. Remove vendor and framework names from the first problem statement. Define the workload, ten or more invariants, quality scenarios, failure assumptions, ownership, and cost constraints.

**Break and measure**

Review the design under a tenfold traffic burst, one slow dependency, stale data, an operator mistake, and the loss of one hosting zone. Record each unsupported claim and hidden assumption.

**Decision artifact**

Write an RFC that compares a simple design, a moderate design, and a distributed design. Preserve the first draft for comparison at later assessment gates.

#### Module 2, Weeks 5–8: Capacity, queues, and tail latency

**Core questions**

- Where does work wait?
- Which finite resource saturates first?
- Which percentile represents the user journey?
- Which control prevents overload from spreading?

**Topics**

- Requests, events, concurrency, and data growth
- Little’s Law and queue behavior
- Service demand and utilization
- Throughput, latency, and useful throughput
- Percentiles, coordinated omission, and measurement error
- Fan-out and tail amplification
- Bounded queues and concurrency
- Admission control and load shedding
- Retry amplification and retry budgets
- Failover headroom and unit cost

**Build**

Create a capacity-planning tool and a service with configurable workers, queues, service time, and fan-out.

**Break and measure**

Sweep load from 10 percent to 150 percent of measured capacity. Add slow requests, burst traffic, queue growth, retries, and downstream limits. Compare predicted and observed saturation points.

**Decision artifact**

Publish a capacity report that sets a safe operating region, scaling signal, overload policy, failover reserve, and cost per useful request.

#### Module 3, Weeks 9–12: Computer systems and operating systems

**Core questions**

- Which hardware or operating-system limit shapes application behavior?
- Which resource does the process own, share, or borrow?
- Which work causes copying, context switches, cache misses, or page faults?
- Which benchmark result will survive a production workload?

**Topics**

- CPU pipelines, caches, locality, and branches
- Processes, threads, scheduling, and context switches
- Virtual memory, allocation, page faults, and swapping
- Locks, contention, deadlock, and false sharing
- Files, buffering, page cache, writeback, and durable writes
- Device queues and I/O latency
- Containers, quotas, throttling, and memory limits
- System calls and kernel boundaries

**Build**

Implement small programs that expose locality, allocation pressure, contention, buffered writes, durable writes, and scheduler behavior.

**Break and measure**

Apply CPU quotas, memory pressure, I/O contention, lock contention, and oversized concurrency. Measure throughput, latency, faults, context switches, allocation, and resident memory.

**Decision artifact**

Write a systems-performance report that explains one counterintuitive result through hardware or operating-system behavior.

#### Module 4, Weeks 13–16: Performance methodology and observability

**Core questions**

- Which evidence distinguishes a cause from a symptom?
- Which telemetry preserves a user journey across process boundaries?
- Which experiment can falsify the current hypothesis?
- Which optimization changes user outcomes or operating cost?

**Topics**

- Performance investigation methods
- Baselines, hypotheses, and controlled experiments
- CPU, memory, allocation, lock, and I/O profiling
- Metrics, logs, traces, and continuous profiles
- Cardinality and telemetry cost
- Context propagation and correlation
- Query plans and dependency timing
- Benchmark design and statistical interpretation
- Regression budgets and performance tests

**Build**

Instrument the saturation service from Module 2. Add request traces, resource metrics, structured logs, profiles, and a reproducible benchmark.

**Break and measure**

Introduce CPU work, allocation pressure, lock contention, slow I/O, a connection leak, and a high-cardinality label. Diagnose each fault from telemetry before inspecting the injected change.

**Decision artifact**

Create a performance review with the baseline, evidence, causal model, proposed change, validation result, and remaining uncertainty.

### Phase II: Networks and persistence

#### Module 5, Weeks 17–20: Network foundations

**Core questions**

- Which round trips sit on the critical path?
- Which layer owns congestion, reliability, encryption, and multiplexing?
- Which loss or delay pattern will break the user journey?
- Which assumption changes across regions or mobile networks?

**Topics**

- DNS, addressing, routing, and network paths
- Latency, bandwidth, jitter, loss, and reordering
- TCP connection setup, flow control, and congestion control
- TLS handshakes and certificate validation
- Connection reuse, pooling, and exhaustion
- Proxies, load balancers, NAT, and service discovery
- HTTP/1.1 and HTTP/2 behavior
- QUIC and HTTP/3 stream behavior
- Kernel and user-space network paths

**Build**

Trace one request from a client through name resolution, transport setup, encryption, proxying, application work, and a downstream dependency.

**Break and measure**

Inject delay, jitter, loss, reordering, bandwidth limits, resets, DNS failure, and slow readers. Measure connection setup, goodput, head-of-line effects, and tail latency.

**Decision artifact**

Write a protocol and topology decision for a concrete client population and failure environment.

#### Module 6, Weeks 21–24: Deadlines and resilient remote calls

**Core questions**

- Which deadline protects the user’s total time budget?
- Which retry is safe, useful, and affordable?
- Which duplicate can cause an irreversible side effect?
- Which local protection shifts failure to another component?

**Topics**

- End-to-end deadlines and timeout allocation
- Cancellation propagation
- Retry classification, backoff, and jitter
- Idempotency keys and deduplication
- Circuit breakers and their limits
- Bulkheads, pools, semaphores, and bounded fan-out
- Hedged requests and duplicate work
- Rate limits, quotas, and fairness
- Health checks and load-balancer behavior
- Partial failure and dependency budgets

**Build**

Create a fan-out service with end-to-end deadlines, cancellation, bounded concurrency, idempotency, and a retry budget.

**Break and measure**

Cause a retry storm, connection-pool exhaustion, dependency slowdown, partial response, duplicate request, and cancellation leak. Prove that the repaired service keeps work bounded.

**Decision artifact**

Produce a remote-call policy with deadline allocation, retry eligibility, idempotency rules, concurrency bounds, telemetry, and exception handling.

#### Module 7, Weeks 25–28: Data models and storage engines

**Core questions**

- Which access paths dominate the workload?
- Which amplification does the design accept?
- Which background work threatens tail latency?
- Which index supports the required query and update pattern?

**Topics**

- Relational, document, key/value, graph, time-series, and columnar models
- Logical and physical data design
- Pages, records, buffer pools, and cache behavior
- B+ trees, hash indexes, and inverted indexes
- LSM memtables, sorted tables, Bloom filters, and compaction
- Read, write, and space amplification
- Point lookups, range scans, and ordered iteration
- Tombstones and compaction debt
- Query execution, planning, and statistics
- SSD behavior and endurance

**Build**

Implement a small B+ tree and LSM-style store, or complete equivalent database-internals assignments. Include point lookup, range scan, write path, and persistence.

**Break and measure**

Compare read-heavy, write-heavy, range-heavy, skewed, and delete-heavy workloads. Measure latency distributions, bytes written, cache effects, compaction work, and storage use.

**Decision artifact**

Write a storage-engine decision that ties workload and recovery requirements to measured amplification and operating cost.

#### Module 8, Weeks 29–32: Transactions, concurrency, and recovery

**Core questions**

- Which anomaly violates a business invariant?
- Which durability claim survives a crash?
- Which transaction boundary matches the unit of correctness?
- Which recovery step has evidence from a restore test?

**Topics**

- Atomicity, consistency, isolation, and durability
- Isolation levels and serialization anomalies
- Locks, optimistic concurrency, and multiversion concurrency control
- Write-ahead logs, checkpoints, redo, and undo
- Group commit and durable acknowledgement
- Deadlocks and transaction retries
- Schema constraints as invariant enforcement
- Backups, point-in-time recovery, and restore validation
- Replicas versus backups
- Recovery time and recovery point objectives

**Build**

Create concurrent transactions around a business invariant. Implement or inspect logging and recovery behavior, then automate backup and restore validation.

**Break and measure**

Trigger lost updates, write skew, deadlocks, process termination, torn workflows, corrupted derived state, and restore failure.

**Decision artifact**

Publish a transaction and recovery design that maps each invariant to a constraint, isolation choice, retry rule, backup method, and tested recovery target.

### Phase III: Distributed systems and asynchronous correctness

#### Module 9, Weeks 33–36: Replication and partitioning

**Core questions**

- Which operation requires fresh, monotonic, causal, or linearizable data?
- Which node may accept work during a partition?
- Which key or tenant can create a hotspot?
- Which repair mechanism restores convergence?

**Topics**

- Leader/follower, multi-leader, and leaderless replication
- Synchronous and asynchronous replication
- Replication lag and session guarantees
- Quorums and their assumptions
- Read repair, anti-entropy, and conflict handling
- Hash and range partitioning
- Consistent hashing and resharding
- Hot keys, skew, and tenant isolation
- CAP and PACELC as scoped reasoning tools
- Regional placement and data residency

**Build**

Create a replicated key/value lab with selectable read and write behavior. Add partitioning, version metadata, conflict handling, and repair.

**Break and measure**

Partition replicas, stop leaders, skew traffic to one key, delay replication, lose acknowledgements, and reshard under load.

**Decision artifact**

Write a data-placement and consistency decision for each important operation. Include partition behavior, staleness limits, hotspot controls, and repair.

#### Module 10, Weeks 37–40: Time, coordination, and consensus

**Core questions**

- Which conclusion depends on an unreliable clock?
- Which property requires consensus?
- Which stale leader can still cause harm?
- Which proof or test supports safety?

**Topics**

- Physical clocks, drift, skew, and uncertainty
- Logical clocks, vector clocks, and causal order
- Safety, liveness, and failure detectors
- Leader election and replicated logs
- Raft and Paxos foundations
- Terms, epochs, quorums, and log matching
- Leases and their clock assumptions
- Fencing tokens
- Linearizable reads and membership changes
- Snapshots and log compaction

**Build**

Implement a Raft-backed key/value service or complete equivalent consensus labs. Add persistence, client deduplication, snapshotting, and membership handling.

**Break and measure**

Terminate leaders, partition the network, restart nodes, duplicate clients, delay messages, reorder messages, and interrupt snapshots.

**Decision artifact**

Create a coordination design that names the safety property, liveness assumptions, stale-owner protection, operating limits, and alternatives to consensus.

#### Module 11, Weeks 41–44: Messaging, streams, and workflows

**Core questions**

- Which database owns the business fact?
- Which delivery can repeat or arrive out of order?
- Which consumer can rebuild its state?
- Which workflow needs orchestration, compensation, or reconciliation?

**Topics**

- Queues, logs, streams, and consumer groups
- At-most-once and at-least-once delivery
- The scope of exactly-once claims
- Ordering and partition keys
- Idempotent consumers and deduplication
- Transactional outbox and inbox records
- Change data capture
- Sagas, compensation, and workflow state
- Event time, processing time, and watermarks
- Poison messages, dead letters, and replay
- Backpressure, lag, and backlog recovery
- Reconciliation and derived-state repair

**Build**

Connect an authoritative database to a transactional outbox, broker or log, idempotent consumer, derived view, and reconciliation job.

**Break and measure**

Crash each component around commit and acknowledgement boundaries. Duplicate, drop, delay, and reorder messages. Stop consumers, grow a backlog, then recover without duplicating irreversible effects.

**Decision artifact**

Write an asynchronous-workflow RFC that includes the state machine, ownership, delivery semantics, replay rules, poison-message handling, and reconciliation proof.

### Phase IV: Production architecture and technical strategy

#### Module 12, Weeks 45–48: Reliability, incidents, and disaster recovery

**Core questions**

- Which user journey defines reliability?
- Which failure consumes the error budget fastest?
- Which signal calls for mitigation rather than diagnosis?
- Which recovery claim has passed a game day?

**Topics**

- Service-level indicators, objectives, and error budgets
- Availability and latency measurement
- Multi-window burn rates
- Dependency and composite reliability
- Graceful degradation and load shedding
- Incident command, communication, and handoffs
- Postmortems and corrective actions
- Backups, restore, failover, and failback
- Zone and regional failure
- Recovery time and recovery point verification
- Capacity under degraded operation
- Chaos experiments and game days

**Build**

Add user-journey SLOs, burn-rate alerts, runbooks, degraded modes, and recovery automation to the course system.

**Break and measure**

Run a controlled incident that combines a slow dependency with load growth. Conduct a second exercise for data loss or regional unavailability. Measure detection, mitigation, recovery, and data exposure.

**Decision artifact**

Write an incident postmortem and a disaster-recovery review. Rank corrective work by risk reduction, effort, and ownership.

#### Module 13, Weeks 49–52: Security, privacy, and abuse resistance

**Core questions**

- Which actor can cross a trust boundary?
- Which authorization check protects each object and action?
- Which data must expire, disappear, or remain auditable?
- Which control detects misuse after prevention fails?

**Topics**

- Threat modeling and abuse cases
- Identity, authentication, and session security
- RBAC, ABAC, and relationship-based authorization
- Object-level authorization and tenant isolation
- Secret, certificate, and key lifecycles
- Encryption in transit and at rest
- Audit events and tamper resistance
- Data classification, retention, deletion, and residency
- Dependency and software-supply-chain controls
- Rate limits and economic abuse
- Security monitoring and incident response
- Prompt injection and tool authorization

**Build**

Create a threat model for the capstone. Implement tenant boundaries, scoped credentials, authorization tests, audit events, secret rotation, retention, and deletion verification.

**Break and measure**

Test cross-tenant access, privilege escalation, replay, expired credentials, secret exposure, dependency compromise assumptions, deletion gaps, and malicious retrieved instructions.

**Decision artifact**

Publish a security architecture that maps threats to preventive, detective, and recovery controls. Record residual risks and control owners.

#### Module 14, Weeks 53–56: Architecture evolution, economics, and organization

**Core questions**

- Which boundary reduces independent change or failure?
- Which boundary creates coordination and operating cost?
- Which migration preserves data and service through rollback?
- Which cost metric connects infrastructure to product value?

**Topics**

- Modular monoliths and service boundaries
- Event-driven boundaries and shared-data risks
- Team ownership and cognitive load
- Conway’s Law and organizational interfaces
- Managed service, open-source, and custom-build choices
- Total cost and cost per useful outcome
- Strangler migrations and branch by abstraction
- Expand-and-contract schema changes
- Backfills, shadow traffic, and parallel runs
- Dual-write hazards and verification
- Compatibility policies and versioning
- Platform capabilities, paved roads, and governance
- Technical strategy and multi-quarter sequencing

**Build**

Create a cost model and migration plan that moves one capstone capability from its initial architecture to a justified target state.

**Break and measure**

Simulate an incompatible deployment, partial backfill, rollback, dual-write divergence, cost spike, and loss of the team that owns a critical component.

**Decision artifact**

Write a technical strategy memo with target outcomes, sequencing, dependencies, cost, staffing assumptions, risk controls, and stopping conditions.

### Phase V: Polyglot, browser, and edge systems

#### Module 15, Weeks 57–60: Execution models across languages

**Core questions**

- Which scheduler executes this work?
- Which operation can block or grow without a bound?
- Who owns each resource, and when does it get released?
- Which guarantee disappears at a process or data boundary?

**Topics**

- Manual memory management and RAII
- Ownership and borrowing
- Tracing garbage collection
- Reference counting and cycle collection
- Stack, heap, allocation, and escape behavior
- Operating-system threads and runtime schedulers
- Event loops, worker pools, goroutines, and async tasks
- Cancellation and structured concurrency
- Memory visibility, races, and synchronization
- Static and dynamic typing
- Nominal and structural typing
- Serialization and validation boundaries

**Build**

Implement the same bounded fan-out service in Node.js with TypeScript, Go, Rust, and either Java or C#. Add Python when it helps compare reference counting or async behavior.

**Break and measure**

Cause event-loop blocking, worker exhaustion, goroutine or task leaks, allocation pressure, garbage-collection pauses, data races, missing cancellation, and resource leaks.

**Decision artifact**

Create a runtime comparison based on workload behavior, latency, memory, safety, operability, ecosystem, and team constraints.

#### Module 16, Weeks 61–64: Browser, frontend, CDN, and edge architecture

**Core questions**

- Which work blocks interaction or rendering?
- Which data can a cache reuse, and who may see it?
- Which rendering strategy fits each route?
- Which frontend boundary matches ownership without duplicating runtime cost?

**Topics**

- Browser tasks, microtasks, and the event loop
- Rendering, style, layout, paint, and compositing
- Browser memory and leak diagnosis
- Critical rendering path and resource priorities
- Core user-experience metrics
- HTTP caching, CDN caching, and invalidation
- Static, server, streaming, and client rendering
- Hydration and partial hydration
- Accessibility and resilient interaction
- Frontend observability and session context
- Design systems and component governance
- Backend-for-frontend and microfrontend trade-offs
- Third-party script governance
- Edge compute and data-consistency limits

**Build**

Create a storefront that supports route-specific rendering, measured interaction performance, safe caching, error recovery, accessibility checks, and end-to-end trace context.

**Break and measure**

Add a long main-thread task, hydration mismatch, memory leak, slow third-party script, cache-key error, stale personalized response, edge-origin failure, and poor network conditions.

**Decision artifact**

Write a frontend and edge architecture RFC with per-route rendering, cache policy, performance budgets, accessibility checks, ownership, and observability.

### Phase VI: AI systems and final defense

#### Module 17, Weeks 65–68: Model foundations and inference systems

**Core questions**

- Which operation consumes memory bandwidth or compute?
- Which model-serving choice changes latency, quality, or cost?
- Which batch and cache policy protects interactive requests?
- Which numerical shortcut changes output quality beyond tolerance?

**Topics**

- Vectors, matrices, dot products, norms, and projections
- Probability, expectation, variance, and entropy
- Derivatives, gradients, and optimization
- Tokens, embeddings, attention, and transformer blocks
- Training and inference
- GPU memory, bandwidth, and parallelism
- Batching and continuous batching
- Key/value caches
- Quantization and numerical precision
- Prefix and semantic caching
- Throughput, time to first token, and inter-token latency
- Admission control, quotas, and serving cost

**Build**

Implement core tensor operations and a small attention mechanism. Profile a small model or model server under different batch, sequence, cache, and quantization settings.

**Break and measure**

Exhaust memory, mix long and short requests, overload the queue, invalidate caches, change numerical precision, and lose an inference provider.

**Decision artifact**

Write an inference architecture and capacity model that ties quality, latency, throughput, memory, availability, and cost to a concrete use case.

#### Module 18, Weeks 69–72: Retrieval, RAG, agents, and capstone defense

**Core questions**

- Which retrieval metric predicts the product outcome?
- Which evidence version supports an answer?
- Which model action requires deterministic authorization?
- Which workflow can resume, replay, or compensate after failure?

**Topics**

- Exact and approximate nearest-neighbor search
- HNSW structure and tuning
- Lexical, vector, and hybrid retrieval
- Chunking, metadata filters, and reranking
- Recall, ranking quality, latency, and index cost
- Retrieval freshness and evidence provenance
- Grounded-answer and unsupported-answer evaluation
- Structured tool contracts
- Durable agent state and checkpoints
- Idempotency, replay, cancellation, and budgets
- Human approval for high-risk actions
- Prompt injection, data exfiltration, and tool abuse
- Evaluation datasets and release gates

**Build**

Complete the Global Commerce Platform with an AI Shopping Assistant. Add hybrid retrieval, answer evidence, evaluation, a bounded tool workflow, durable state, scoped credentials, approvals, audit history, and cost controls.

**Break and measure**

Test a stale or missing index, revoked evidence, adversarial documents, provider timeout, low-quality retrieval, duplicate tool results, workflow restart, budget exhaustion, and an unauthorized irreversible action.

**Decision artifact**

Defend the complete architecture before an adversarial review panel. Submit the final RFC, operational evidence, threat model, cost model, migration path, incident record, and a revision log that explains how your judgment changed since Week 1.

## 11. Principal capstone

### System

Build a Global Commerce Platform with an AI Shopping Assistant. A modular monolith with independently scalable workers provides a sound starting point. Add deployable boundaries only when a workload, failure, ownership, security, or delivery constraint supports them.

### Required capabilities

- Product catalog and merchant ingestion
- Search and product discovery
- Inventory reservation
- Checkout and payment
- Order workflow and notifications
- Tenant isolation
- Browser storefront and edge delivery
- Retrieval-based product research
- Versioned evidence and citations
- Bounded assistant tools and approvals
- Observability, recovery, and cost reporting

### Required invariants

1. Confirmed inventory cannot exceed sellable stock.
2. One payment attempt cannot cause two successful captures.
3. Order transitions must follow the documented state machine.
4. One tenant cannot read or mutate another tenant’s private data.
5. Each generated answer must retain the evidence versions used to produce it.
6. Revoked or deleted evidence must disappear within the stated service objective.
7. Event replay cannot duplicate an irreversible side effect.
8. An assistant cannot perform an irreversible action without authorization and an idempotency record.
9. A failed migration must preserve a tested rollback or roll-forward path.
10. The team must be able to restore authoritative data within the declared recovery targets.

### Required failure experiments

- Downstream packet loss and a dependency slowdown
- Database-primary loss and connection-pool exhaustion
- Hot-product traffic skew
- Broker outage and backlog recovery
- Duplicate and out-of-order events
- Disk or memory pressure
- Expired credentials
- Incompatible schema deployment
- Missing or stale retrieval index
- AI-provider timeout
- Malicious instructions in retrieved content
- Duplicate delivery of an assistant tool result
- Regional unavailability
- Operator error during recovery

## 12. Assessment gates

Each gate reviews the previous 12 weeks. A gate contains a written examination, a practical exercise, an architecture defense, and a portfolio review.

| Gate | Week | Focus | Required defense |
|---:|---:|---|---|
| 1 | 12 | Judgment, capacity, and computer systems | Explain a saturation curve and revise the baseline design |
| 2 | 24 | Performance, networks, and remote calls | Diagnose a hidden fault and defend deadline and retry policy |
| 3 | 36 | Storage, transactions, replication, and partitioning | Preserve an invariant through concurrency and partition tests |
| 4 | 48 | Consensus, messaging, reliability, and recovery | Recover a failed workflow and defend system safety |
| 5 | 60 | Security, evolution, economics, and runtimes | Present a threat model, migration, cost model, and runtime choice |
| 6 | 72 | Browser, edge, AI systems, and capstone | Defend the system under technical, product, security, and operating review |

### Gate result

Use three result bands:

- **Pass:** Evidence supports the decision, and you can answer follow-up questions without changing the failure model.
- **Revise:** The design may work, but missing evidence, unclear semantics, or weak experiments prevent a defensible decision.
- **Repeat:** A safety property fails, the recovery claim lacks a test, or the explanation depends on incorrect system behavior.

Revise or repeat the weak component before starting the next phase. You do not need to repeat work that already meets the standard.

## 13. Grading rubric

Score each major artifact from 0 to 4 in each category.

| Category | 0 | 2 | 4 |
|---|---|---|---|
| Conceptual accuracy | Major errors | Correct terms with gaps | Precise model and scoped claims |
| Quantification | No estimates | Basic estimates | Validated model with sensitivity analysis |
| Implementation | Missing | Happy path works | Mechanism exposed with tests and instrumentation |
| Failure testing | None | A few injected faults | Systematic fault matrix with observed outcomes |
| Diagnosis | Guesswork | Evidence identifies symptoms | Causal explanation with falsification |
| Decision quality | Preference | Trade-offs listed | Choice follows drivers and includes reversal evidence |
| Operations | Ignored | Basic monitoring | SLOs, runbooks, overload, recovery, and ownership |
| Security | Ignored | Common controls | Threat-driven controls and residual risk |
| Communication | Unclear | Understandable | Review-ready, concise, and teachable |
| Leadership | Individual view | Feedback collected | Conflict resolved and others enabled |

### Passing standard

- No category may score 0 on a safety-critical artifact.
- Each assessment gate requires an average of 3.
- The final capstone requires an average of 3.5.
- You must repair any failed invariant before completion.

The scores guide revision. The evidence and your ability to defend it matter more than arithmetic.

## 14. Required portfolio

By Week 72, your portfolio should contain:

| Artifact | Minimum |
|---|---:|
| Architecture Decision Records | 12 |
| Substantial RFCs | 6 |
| Capacity and cost models | 3 |
| Performance investigation reports | 6 |
| Controlled-incident postmortems | 4 |
| Failure matrices | 6 |
| Source-code internals reviews | 3 |
| Runtime comparison reports | 2 |
| Security threat models | 1 major model |
| Disaster-recovery exercise reports | 2 |
| Migration plans | 2 |
| Recorded teach-backs or review sessions | 6 |
| Complete capstone | 1 |

Sanitize company information before placing work-derived material in a personal portfolio. Replace customer data, credentials, internal URLs, proprietary code, and confidential scale figures with safe equivalents.

## 15. Core resource spine

Use a small set of substantial sources as the course spine:

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Brendan Gregg, *Systems Performance*
- A database-internals course such as CMU 15-445/645
- A distributed-systems course such as MIT 6.5840
- Google’s Site Reliability Engineering books and workbook
- OWASP ASVS and threat-modeling guidance
- MDN and web performance curricula for browser systems
- A build-from-first-principles language-model course such as Stanford CS336

Supplement these with standards, source code, and foundational papers. A separate reading and paper guide will map each source to the relevant week, set reading boundaries, and define a review template.

## 16. Use of AI tools

AI tools can accelerate implementation, explain unfamiliar syntax, generate test cases, and challenge a design. You remain responsible for each claim and artifact.

Follow these rules:

1. State where you used AI assistance on graded artifacts.
2. Verify generated claims against primary sources, code, or experiments.
3. Read and explain generated code before including it.
4. Test failure paths instead of accepting a generated happy path.
5. Keep secrets, private data, and proprietary material out of unapproved tools.
6. Preserve your own first design before asking AI to critique it.
7. Record prompts or review notes when they influenced a major decision.
8. Reject citations that you cannot inspect.

During an architecture defense, you must explain the work without relying on an AI tool to answer for you.

## 17. Study records

Maintain one course repository or notebook with:

```text
principal-engineer-course/
├── notes/
├── labs/
├── experiments/
├── adr/
├── rfc/
├── reports/
├── reviews/
├── capstone/
└── learning-log/
```

Each weekly learning-log entry should record:

- Claims you can now support
- Predictions that measurements disproved
- Decisions made and evidence used
- Open questions
- Risks or gaps to revisit
- One concept you taught to someone else

## 18. Review standard for architecture decisions

Before accepting a design, confirm that it answers:

1. Which user or business outcome does the design serve?
2. Which workload and growth assumptions drive it?
3. Which invariants does it preserve?
4. Which consistency and transaction semantics apply to each operation?
5. Which failure model and overload behavior does it cover?
6. Which capacity, latency, recovery, and cost targets can you measure?
7. Which security and privacy boundaries does it enforce?
8. Who owns each component in development and production?
9. Which migration path avoids unsafe state or irreversible coupling?
10. Which evidence would trigger a different decision?

If the design cannot answer one of these questions, record the gap as a risk, an experiment, or a prerequisite decision.

## 19. Completion criteria

You complete the course when:

- All six assessment gates pass.
- The required portfolio meets the artifact standard.
- Capstone experiments preserve the stated invariants.
- Recovery exercises meet the declared targets.
- The final defense answers technical, product, security, cost, and ownership challenges.
- The Week 72 revision identifies specific changes from the untouched Week 1 baseline.
- You publish a next-year practice plan tied to production scope and cross-team influence.

## 20. First action

Begin with the Week 1 baseline before reading architecture recommendations.

Choose the capstone or a familiar production problem. Write:

- The user journey and business outcome
- Normal, peak, burst, and projected workloads
- Ten or more invariants
- Five measurable quality-attribute scenarios
- The failure and overload model
- A context diagram and state owners
- The simplest design you believe will work
- Your strongest reasons for and against that design

Date the document and preserve it without later edits. Create revised copies at Weeks 24, 48, and 72 so that the course produces evidence of how your judgment changed.
