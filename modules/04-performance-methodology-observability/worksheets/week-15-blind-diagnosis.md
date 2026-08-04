# Week 15: Blind Diagnosis Matrix

Use only the opaque bundles produced by `blind-solo-prepare`. Do not inspect the
named guided scenario files, the local reveal envelope, or run
`blind-solo-reveal` until each diagnosis and discriminating rerun is frozen and
committed.

| Fixture | User symptom | Cited observations | Cause and mechanism | Alternatives | Discriminating rerun | Confidence | Reveal comparison |
|---|---|---|---|---|---|---|---|
| O01 | | | | | | | |
| O02 | | | | | | | |
| O03 | | | | | | | |
| O04 | | | | | | | |
| O05 | | | | | | | |
| O06 | | | | | | | |

## Evidence integrity

- Raw bundle hashes:
- Frozen diagnosis commit:
- Reveal time and source:
- Any diagnosis changed after reveal belongs only in the final column.
- Run `blind-solo-prepare`, commit this non-empty diagnosis, and then run
  `blind-solo-reveal` with the exact commit. Preserve both the
  reveal record and `.sblind` envelope, and disclose that the envelope provides
  accidental-exposure protection rather than enforced secrecy.
- An optional human reviewer may inspect the already-frozen diagnosis and reveal
  record, but is never needed to unlock or complete the exercise.
