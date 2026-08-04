# Reliability, Incidents, and Disaster Recovery Resource Guide

Local lessons are sufficient to complete the module. External sources reinforce
the instruction and provide a checkable primary or practitioner reference; they
never replace the local explanation, practice, or answer key.

## Required authoritative spine

The required records are RES-01, RES-03, RES-06, RES-07.
Every required record is free and has a local written alternative. All other
records below are optional enrichment and do not consume required module time.

| Week | Required resources | Assigned minutes |
|---:|---|---:|
| 45 | RES-01 | 80 |
| 46 | RES-03 | 65 |
| 47 | RES-06 | 90 |
| 48 | RES-07 | 40 |

For each assigned source, preserve the requested evidence, one transfer limit,
and one observation that would falsify the claim. A required source that is
temporarily unavailable is replaced by its local alternative and the same evidence
task; record the substitution.

## Resource records

### RES-01: Implementing SLOs

- **Author/publisher:** Steven Thurgood, David Ferguson, Alex Hidalgo, Betsy Beyer; Google SRE
- **URL:** https://sre.google/workbook/implementing-slos/
- **Type/status:** practitioner book chapter; Required
- **Access:** free
- **Week/time:** Week 45; 80 minutes assigned
- **Purpose:** Derive a user-centered SLO, budget, owner, and decision policy.
- **Boundary and evidence:** Read Getting Started through Decision Making Using SLOs and Error Budgets; submit one SLI contract, budget calculation, policy action, and anti-gaming review.
- **Local alternative:** [lessons/01-user-journeys-slis-slos.md](lessons/01-user-journeys-slis-slos.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-03: Managing Load

- **Author/publisher:** Google Site Reliability Engineering
- **URL:** https://sre.google/workbook/managing-load/
- **Type/status:** practitioner book chapter; Required
- **Access:** free
- **Week/time:** Week 46; 65 minutes assigned
- **Purpose:** Reason about feedback among load controls and reserve after failure.
- **Boundary and evidence:** Read load balancing, autoscaling, shedding, combined strategies, and conclusions; draw one control interaction and calculate degraded capacity.
- **Local alternative:** [lessons/04-graceful-degradation-capacity.md](lessons/04-graceful-degradation-capacity.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-06: Contingency Planning Guide for Federal Information Systems

- **Author/publisher:** National Institute of Standards and Technology
- **URL:** https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf
- **Type/status:** standards-body guidance; Required
- **Access:** free
- **Week/time:** Week 47; 90 minutes assigned
- **Purpose:** Connect business impact, recovery order, exercises, validation, and reconstitution.
- **Boundary and evidence:** Read Sections 3.2, 3.5, 4.3, and 4.4; produce a recovery priority table, exercise charter, and reconstitution checks.
- **Local alternative:** [lessons/07-backups-restore-failover.md](lessons/07-backups-restore-failover.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-07: Preparedness and Disaster Testing

- **Author/publisher:** Google Site Reliability Engineering
- **URL:** https://sre.google/sre-book/lessons-learned/
- **Type/status:** first-person engineering experience; Required
- **Access:** free
- **Week/time:** Week 48; 40 minutes assigned
- **Purpose:** Design exercises that reveal unknown weaknesses without uncontrolled harm.
- **Boundary and evidence:** Read Preparedness and Disaster Testing and the DiRT discussion; submit a hypothesis, abort conditions, and evidence plan.
- **Local alternative:** [lessons/08-game-days-reliability-decisions.md](lessons/08-game-days-reliability-decisions.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-02: Alerting on SLOs

- **Author/publisher:** Google Site Reliability Engineering
- **URL:** https://sre.google/workbook/alerting-on-slos/
- **Type/status:** practitioner book chapter; Optional enrichment
- **Access:** free
- **Week/time:** Week 45; 70 minutes optional
- **Purpose:** Derive burn-rate windows, notification class, and reset behavior.
- **Boundary and evidence:** Read approaches 4-6 and Low-Traffic Services; recalculate one page and ticket threshold and test a low-traffic case.
- **Local alternative:** [lessons/03-burn-rates-actionable-alerting.md](lessons/03-burn-rates-actionable-alerting.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-04: Incident Response

- **Author/publisher:** Google Site Reliability Engineering
- **URL:** https://sre.google/workbook/incident-response/
- **Type/status:** first-person engineering cases; Optional enrichment
- **Access:** free
- **Week/time:** Week 47; 75 minutes optional
- **Purpose:** Separate command, operations, communications, and coordination during user impact.
- **Boundary and evidence:** Read the complete chapter and power-outage case; submit a role map, first three mitigations, and handoff contract.
- **Local alternative:** [lessons/05-incident-command-runbooks.md](lessons/05-incident-command-runbooks.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-05: Postmortem Culture: Learning from Failure

- **Author/publisher:** Daniel Rogers et al.; Google Site Reliability Engineering
- **URL:** https://sre.google/workbook/postmortem-culture/
- **Type/status:** first-person engineering case and guidance; Optional enrichment
- **Access:** free
- **Week/time:** Week 47; 70 minutes optional
- **Purpose:** Write causal, measurable, owned corrective work without blame.
- **Boundary and evidence:** Read the case comparison, action items, incentives, and tools; rewrite three weak findings and rank five actions.
- **Local alternative:** [lessons/06-postmortems-corrective-work.md](lessons/06-postmortems-corrective-work.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

### RES-08: Incident Management with Adrienne Walcer

- **Author/publisher:** Google SRE Prodcast
- **URL:** https://sre.google/prodcast/transcripts/sre-prodcast-01-08/
- **Type/status:** recorded practitioner interview with HTML transcript; Optional enrichment
- **Access:** free
- **Week/time:** Week 48; 45 minutes optional
- **Purpose:** Transfer practiced incident coordination into a runbook and defense.
- **Boundary and evidence:** Listen to the complete episode or read the transcript; record communication cadence, role boundaries, and two practice prompts.
- **Local alternative:** [lessons/05-incident-command-runbooks.md](lessons/05-incident-command-runbooks.md)
- **Verification:** verified; HTTP GET plus primary-source metadata comparison; last checked 2026-08-02
- **Reflection:** Which claim transfers to this module, which assumption limits it, and what evidence would falsify it?

Do not copy articles, chapters, slides, or transcripts into learner artifacts.
Use short attributed quotations only when necessary and otherwise paraphrase with
the source ID, exact section boundary, and stated evidence limit.
