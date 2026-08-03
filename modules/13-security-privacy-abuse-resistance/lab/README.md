# Security, Privacy, and Abuse-Resistance Lab

This Python 3.11+ standard-library lab models explicit identity, authorization,
tenant, secret, audit, deletion, dependency, abuse-budget, and tool decisions.
Its public CLI is:

```bash
python3 -m security_lab scenarios/f01-cross-tenant-access-broken.json --pretty
```

Run the checks with:

```bash
python3 -m unittest discover -s tests -v
```

The eighteen scenarios form nine same-input broken/repaired pairs. A pair changes
exactly one named control. Trial JSON conforms to
`schemas/security-trial.schema.json` and includes hashes for the full scenario,
shared adversarial input, and control configuration. Learners freeze predictions
and scenario hashes before running a trial, preserve raw output, then reproduce
the observable contract in their chosen stack or a safe operated environment.

The model does not prove production isolation, cryptographic strength, physical
deletion, provider provenance, legal compliance, or resistance to adaptive
attackers. These limits are part of every trial result.
