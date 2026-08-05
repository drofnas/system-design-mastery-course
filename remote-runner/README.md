# Official Remote Container Fallback

This fallback is for a learner whose machine cannot run Docker, loopback, or
headless Chromium. It is optional and never a prerequisite for core study.

Run the `PESD remote fallback` workflow manually at the exact learner commit and
select M10, M15, M16, M17, or `all`. The workflow uses digest-pinned container
images, explicit CPU/memory/PID bounds, the same repository scenarios and
schemas, and serial execution. It uploads the raw log together with an evidence
envelope that binds:

- learner source commit;
- runner OS, architecture, and version;
- every container reference and manifest digest;
- scenario, contract, configuration, toolchain-lock, and schema hashes;
- raw-output hash, evidence mode, limits, clock, and limitations.

Download the artifact and commit it under the learner's immutable experiment
path. A remote run remains environment-bound. M16 headless output does not
replace normal-browser keyboard, reflow, JavaScript-disabled, assistive-
technology, or Windows-host callback evidence. Fixture replay never becomes
independent Build, Break, Implement, or Measure evidence.

The workflow's M16 container pins Node 24.19.0. It installs the exact
package-lock and Playwright browser revision during the run; preserve that raw
installation log. M15 uses the four image digests in its checked-in toolchain
lock and runs the full F01–F09 matrix serially.
