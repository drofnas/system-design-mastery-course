# Module 12 Glossary

Use this reference after studying the mechanisms.

| Term | Operational meaning |
|---|---|
| valid event | An event included in an SLI denominator under explicit population and exclusion rules. |
| good event | A valid event satisfying every success condition for the measured journey. |
| SLI | A measured ratio or distribution describing one user-visible behavior. |
| SLO | A target for an SLI over a stated window and population. |
| error budget | The allowed bad-event fraction or count implied by an SLO. |
| burn rate | Error-budget consumption rate divided by the sustainable rate for the objective window. |
| multi-window alert | An alert requiring long- and short-window evidence so it detects material active burn. |
| composite reliability | Reliability of a journey derived from its actual dependency graph and failure correlation. |
| shared fate | A common cause that can fail supposedly redundant paths together. |
| graceful degradation | A declared reduced service mode that preserves priority journeys and invariants. |
| load shedding | Rejecting or deferring work before overload destroys more useful work. |
| mitigation | An action intended to reduce current user impact before full causal diagnosis. |
| incident commander | The person accountable for priorities, coordination, and declared incident state. |
| operations lead | The person coordinating technical mitigations under incident command. |
| communications lead | The person maintaining accurate stakeholder and user updates. |
| handoff | Explicit transfer of role, state, active hypotheses, actions, risks, and next update time. |
| postmortem | Evidence-based record of impact, timeline, contributing conditions, recovery, and corrective work. |
| corrective action | Owned work with a verifiable completion condition tied to a named risk. |
| RPO | Maximum acceptable authoritative-data loss measured backward from disruption. |
| RTO | Maximum acceptable time to restore the declared minimum service from disruption. |
| failover | Transfer of service or authority to an alternate failure domain. |
| failback | Controlled return from the alternate domain after verification and reconciliation. |
| fencing | Rejecting work from stale owners using epochs, leases with valid assumptions, or equivalent authority tokens. |
| reconstitution | Validation that recovered service, data, controls, and users can return to normal operation. |
| game day | A controlled exercise with hypothesis, scope, roles, abort conditions, evidence, and follow-up. |
| blast radius | The users, data, components, regions, and time exposed to an action or failure. |
| break-glass access | Exceptional access that is time-bounded, approved, audited, and reviewed. |
