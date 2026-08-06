---
lesson_id: L02
title: "Identity, authentication, recovery, and sessions"
---

# Identity, authentication, recovery, and sessions

## Outcomes

- Separate identity proofing, authentication, authorization, and session continuity.
- Derive authenticator and recovery requirements from impact and assurance needs.
- Test expiry, replay, revocation, reauthentication, logout, and recovery paths.

## Prerequisites

Threat actors and boundaries from L01; deadline, retry, and replay reasoning from Module 6.

## Mechanism and repeatable method

Authentication establishes evidence that a claimant controls one or more
authenticators. A session carries bounded continuity from that event. Neither
answers whether a subject may perform a particular action.

Model the lifecycle as states and transitions:

`unverified -> authenticated -> active session -> reauthenticated or expired -> revoked`

Account recovery and authenticator replacement are privileged transitions, not
support conveniences. They need at least as much scrutiny as login because an
attacker can bypass a strong authenticator through a weak recovery channel.

For each journey, derive:

1. subject and authenticator identities;
2. required assurance and phishing/replay resistance;
3. session binding, audience, scope, inactivity and overall lifetime;
4. reauthentication triggers for sensitive actions;
5. logout, compromise, revocation, and propagation targets;
6. recovery proof, notification, delay, and audit evidence;
7. negative tests for stolen, expired, replayed, downgraded, and replaced credentials.

Do not infer user presence from a long-lived access token. A token may remain
valid after the interactive session ends. Record which component is authoritative
for session and credential status and how quickly revocation propagates.

## Worked example

Northstar researchers use a 60-minute session for viewing private observations.
Changing publication status requires a fresh authentication event no more than
five minutes old. A session secret is opaque, bound to the intended host, and
never contains observation data. Logout invalidates the server-side session;
credential-compromise response revokes all sessions for that authenticator.

An operator recovery request requires an already registered second channel,
notifies the current account contact, delays privilege restoration, invalidates
old recovery material, and produces an audit event. F03 replays a revoked
90-minute session. The repaired system denies it before object authorization and
records the status source and policy version.

## Common expert mistakes

- **Equating authentication with authorization:** a valid identity can still be
  forbidden from an object or action.
- **Designing login but not recovery:** the weakest identity transition becomes
  the attacker's preferred path.
- **Embedding claims forever:** stale roles or tenant membership in long-lived
  tokens outlive policy changes.
- **Client-only expiry:** a server that accepts an expired credential still has a vulnerability.
- **Global logout claims without evidence:** revocation must be measured across
  caches, services, and federated sessions.

## Guided practice

Create a Northstar state machine for researcher login, session refresh,
publication approval, logout, authenticator loss, and compromise. For every
transition, name input evidence, authoritative state, maximum age, denied
conditions, audit event, and recovery action. Add tests for replay after logout,
role removal during a session, and recovery-channel replacement.

## Self-check

1. Why does a valid access token not prove user presence?
2. What makes recovery security-critical?
3. Where should session expiry be enforced?
4. What evidence supports a revocation target?

## Explained answers

1. Tokens can outlive the interactive authentication session and may be copied.
2. Recovery can replace authenticators and restore privilege, bypassing the normal login path.
3. At the server-side trust boundary before protected work, regardless of client behavior.
4. Timed negative tests across every accepting component, including caches and federated boundaries.

## Sources and next work

- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html)

Complete EX-03 and EX-04 and add session/recovery abuse cases to the frozen model.
