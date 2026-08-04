# Module 14 Evolution Lab

Before setup, run the repository [Home Lab Guide](../../../HOME_LAB_GUIDE.md)
preflight for `M14`.

The lab is a deterministic Python 3.11 model of compatibility, migration,
economics, dependency, and ownership decisions. It is intentionally smaller
than a production migration and uses only the standard library.

## Public interface

```bash
python3 -m evolution_lab run scenarios/f01-incompatible-deployment-broken.json
python3 -m evolution_lab run scenarios/f01-incompatible-deployment-repaired.json --output /tmp/f01-repaired.json
python3 -m unittest discover -s modules/14-architecture-evolution-economics-organization/lab/tests -v
```

Inputs conform to `schemas/evolution-scenario.schema.json`; outputs conform to
`schemas/evolution-trial.schema.json`. The runner prints canonical JSON when no
output path is supplied. It never reads a network or cloud account.

## Paired evidence contract

F01–F09 each contain broken and repaired scenarios. A pair has identical shared
inputs and differs by exactly one control. The broken output fails its declared
target invariant; the repaired output passes I01–I12. Preserve scenario and
output SHA-256 values in the independent evidence directory.

## Evidence boundary

The lab demonstrates arithmetic and decision contracts. It cannot establish
production compatibility, database atomicity, provider portability, real bills,
security isolation, human succession, or migration safety at production scale.
