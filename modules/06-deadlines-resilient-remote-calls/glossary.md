# Module 6 Glossary

- **Attempt:** one dispatch to a dependency; one logical request can create many.
- **Deadline:** the latest instant at which a result remains useful.
- **Timeout:** a duration used locally to derive or enforce a deadline.
- **Budget reserve:** time intentionally kept for response assembly and cleanup.
- **Cancellation:** a signal that the caller no longer wants work; not proof that work stopped.
- **Retry budget:** a bound on extra attempts, normally scoped by caller and time window.
- **Full jitter:** selecting a random wait from zero through the current capped backoff.
- **Ambiguous outcome:** the caller cannot know whether an effect occurred.
- **Idempotency key:** a client-stable identity for one intended operation.
- **Fingerprint:** canonical operation inputs stored to reject key reuse for different intent.
- **Bulkhead:** a resource partition that limits one workload's blast radius.
- **Hedge:** a concurrent duplicate attempt issued before the first has definitively failed.
- **Circuit breaker:** a stateful admission policy based on recent failure observations.
- **Useful-work ratio:** completed logical outcomes divided by total attempts or resource cost.
- **Retry storm:** retries become a sustaining load that impedes recovery.
- **Metastable failure:** a trigger moves a vulnerable system into a self-sustaining bad state.
