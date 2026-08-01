lesson_id: L04

# TLS Trust and Connection Establishment

## Outcomes

- Trace TLS 1.3 negotiation, key establishment, certificate authentication, and hostname validation.
- Separate encryption from peer identity and application authorization.
- Test success and rejection without committing credentials.

## Prerequisites

Lesson 3 connection establishment and basic public-key concepts.

## Mechanism and method

TLS negotiates parameters, establishes traffic keys, authenticates the server
when certificates are used, and protects records. The client must validate a
chain to a configured trust anchor and check the intended hostname. Encryption
with hostname checks disabled can create a confidential channel to the wrong peer.

TLS does not authorize an application operation. Certificate termination also
creates a plaintext/trust boundary: if the edge terminates TLS, the next hop
needs its own security decision.

Trust test procedure:

1. Generate an ephemeral key/certificate outside the repository.
2. Configure a client trust store containing only the test certificate.
3. connect with the expected hostname and record protocol/cipher/certificate result.
4. repeat without the trust anchor and with the wrong hostname; both must fail.
5. remove key material and record cleanup without logging private keys.

## Worked example

The Transit loopback server presents an ephemeral certificate for
`impact.transit.test`. The client connects to `127.0.0.1` but supplies the DNS
name for hostname verification. Trusting the generated certificate makes the
expected name pass. The default trust store rejects it. This proves the lab
trust contract, not public CA issuance or production key protection.

## Common expert mistakes

- Disabling verification to “test TLS” removes the property under test.
- Treating possession of a certificate as application authorization confuses layers.
- Committing a private key as a fixture creates avoidable secret-handling risk.
- Claiming resumption always saves one RTT ignores tickets, expiry, rejection, and replay constraints.

## Guided practice

Write four assertions for expected hostname/trusted anchor, wrong hostname,
missing anchor, and expired certificate. Name the owner and safe client behavior
for each failure.

## Self-check

1. What two checks bind a certificate to the intended server?
2. Why does TLS termination need an architecture marker?
3. What does an ephemeral self-signed certificate prove?

## Explained answers

1. Chain validation to a configured trust anchor and hostname/identity matching.
2. It identifies where confidentiality and authenticated peer identity end and where a new hop begins.
3. Correct local trust and hostname handling; it does not prove public issuance, revocation, or production key custody.

## Sources and next work

- RFC 9846, TLS 1.3: https://www.rfc-editor.org/rfc/rfc9846.html
- Continue with Lesson 5 for connection ownership beyond the TLS endpoint.
