# Calibration Fixture: Pass

## Simulated structural evidence

- G01: validator passed.
- G02: baseline tag and last baseline content commit both `abc1234`; status
  frozen and dates present.
- G03–G06: complete artifact and defense bundle supplied.

## Journey, outcome, and scope

For riders planning trips during disruptions, the current approved route impact
must be visible early enough to select another route. The target is 99% of
eligible client views showing an approved version within two minutes over 28
days. Scope includes operator approval, current rider views, versioned delivery,
revocation, and audit. Predictive disruption detection is excluded.

## Workload

Normal alert views are 60/s, peak 170/s, and a five-minute citywide burst is
modeled at 800/s, projected to 1,200/s in 18 months. The top alert may receive
55% of reads. These are planning assumptions. Burst share and duration are the
highest-sensitivity inputs and require current-traffic evidence.

## Invariants and ownership

At most one version is current per route and effective interval. One approval
identity creates at most one approved version. Revoked versions are never
current for a new rider view. Only a region-authorized operator can approve.
The alert-approval responsibility owns version transitions; rider views and
channels are derived and reconcile by source version.

The proof sketch covers concurrent expected-version approval, lost response and
retry, recovery replay, and stale channel copies.

## Quality and failure model

The submission contains six-part performance, freshness, overload, availability,
recovery, and security scenarios with populations, windows, and measurement
locations.

For a 20–40 second channel slowdown plus an 800/s rider burst, it traces shared
connections as the first coupling risk, separates version safety from delivery
liveness, caps worker resources, defines full-queue behavior, and requires a
backlog-recovery test. Zone loss remains a stated pilot exclusion accepted by
the sponsor, with user consequence documented.

## Candidates, cost, and decision

Simple, moderate, and regional candidates use the same drivers. The moderate
candidate keeps one alert authority and uses a delivery worker. It wins
provisionally because channel isolation is ranked above deployment simplicity,
subject to bounded shared-resource and 30-minute recovery tests.

The pilot uses one eight-person team, sixteen weeks, existing on-call, and a
provisional unit-cost target. Reconsider the simple candidate if internal
resource isolation meets the same scenarios at lower operating cost. Regional
write authority requires residency or autonomy evidence.

## Defense and self-critique

The defense states that the worker isolates scheduling and execution, not shared
state connections. It labels backlog recovery unknown until measured and
assigns the experiment. The learner records that the initial claim “separate
worker isolates channel failure” was too broad and narrows it without editing
the frozen baseline.

