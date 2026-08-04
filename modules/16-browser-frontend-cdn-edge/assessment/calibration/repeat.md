# Northstar Repeat Calibration Fixture

## Missing chronology and non-equivalent evidence

Manifest `manifests/repeat.json` lacks A01, A04, A10, two learning logs, and a
baseline tag. Predictions were written after the implementation. Several
“repaired” runs use a faster device profile and smaller payload, so pair input
hashes differ and more than one control changed. Raw broken trials were replaced
by summaries.

## Unresolved safety failures

The edge caches `/staff/schedule` by pathname despite a claimed `private`
header; a two-session probe serves one staff alias to another. Browser-provided
subject and sampling fields are forwarded without validation. The public cache
omits region from its key. The critical schedule action is a clickable `div`
with no keyboard behavior, and the learner treats a clean axe scan as complete
accessibility proof. F05 and F06 repaired trials still fail their targets.

## Unsupported architecture conclusion

The RFC recommends the same client-heavy rendering and shared edge policy for
every route because one warm desktop Chromium run was fast. It omits ownership,
cost, purge failure, migration, rollback, dissent, and reversal. This fixture
fails G01, hard gates G02–G05, and has safety-critical zeros, so Repeat is required.
