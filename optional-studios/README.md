# PESD 2.0 Optional Studios

These flex-week side quests are substantial, ungraded, and never affect course
completion. Each studio preserves the same evidence boundaries as core work.
Do not replace a required local mechanism with a studio or turn a cloud, device,
accelerator, Kubernetes, or second-machine dependency into a hidden prerequisite.

## Device and fleet edge

Anchor the study in [NIST SP 1800-36](https://csrc.nist.gov/pubs/sp/1800/36/final).
Model a synthetic fleet with trusted onboarding, rotating device identity,
intermittent operation, signed OTA rollout, staged rollback, fleet observability,
quarantine, and end-of-life. Implement a local device simulator and signed
manifest verifier. Break expired identity, partial rollout, rollback denial,
offline queue growth, telemetry loss, and retirement. Decide who may enroll,
update, quarantine, export, and retire a device. Modeled fleet results must not
be presented as physical-device measurements.

## TLA+, PlusCal, or equivalent model checking

Translate one course invariant into a small executable state model. Start with
a bounded state space and explicit safety and liveness properties. Produce a
counterexample for a deliberately broken transition, repair the model, and map
each abstract action to learner code or an operational control. State what the
finite model does not prove. Strong candidates are M08 recovery, M10 joint
membership, M11 replay, and M18 approval plus deduplication.

## PQC and hybrid-handshake benchmarking

Inventory the local TLS/crypto boundary, select a hybrid or post-quantum test
implementation, and freeze size, latency, CPU, memory, compatibility, downgrade,
rotation, and rollback predictions. Run only loopback or isolated-container
experiments with pinned versions. Separate algorithm behavior from library and
hardware behavior. Decide a staged crypto-agility migration; do not assert
production security or universal compliance from the benchmark.

## Kubernetes or cloud-backed platform implementation

Extend M14's local platform product into an optional cluster or cloud account.
Implement a catalog entry, self-service interface, golden path, policy guardrail,
exception workflow, ownership metadata, platform SLO, allocation/showback, and
exit plan. Measure adoption friction and support work as product signals. Inject
control-plane loss, policy drift, tenant quota exhaustion, provider outage, and
export failure. Preserve a complete local alternative.

## Accelerator-specific inference profiling

Run M17's actual tiny transformer on an explicitly recorded GPU, MPS, or other
accelerator. Profile prefill, decode, KV extension, transfer, allocation, queue,
precision, and useful-output cost. Record warm-up, repetitions, device/runtime,
power or energy measurement method, profiler overhead, and thermal limitations.
Do not extrapolate tiny-model results to a different model or accelerator.

## Multi-agent and interoperability experiments

Build two bounded agents or services with distinct authorities and a versioned,
typed exchange contract. Test identity propagation, capability negotiation,
schema evolution, provenance, policy drift, partial failure, replay,
human-approval effectiveness, cost budgets, audit, rollback, and retirement.
The model may propose an action but cannot mint authority. Compare direct tools,
workflow orchestration, and an interoperability protocol using the same frozen
workload and safety invariants.

## Studio completion record

For any studio, preserve:

- Question, useful outcome, invariant, and prohibited conclusion
- Source commit and scenario/input/configuration hashes
- Evidence mode, runtime, resource and clock boundary
- Prediction, raw outcomes, analysis, and limitations
- Security, governance, cost, recovery, ownership, migration, and exit decision
- A five-minute teach-back that clearly labels the work optional
