# Day 073 practice: Authentication providers and identity boundaries

Use this worksheet after reading [the lesson](../day_073_authentication_providers_and_identity_boundaries.md). Start with the [course README](../../README.md), confirm the [setup guide](../../SETUP.md), and choose the local fixture from the [examples guide](../../examples/README.md). This worksheet is designed for **Authentication providers and identity boundaries** and uses only local, synthetic, bounded data.

## How to submit your own evidence

For every task, record a prediction before running it, save the smallest relevant code or written artifact, copy the observed result, and explain why it happened. Do not open the solution guide until you have attempted the work.

## Exercises

1. Run the synthetic signed-out and signed-in fixtures and record the visible outcome.
2. Separate identity, session, navigation check, and permission in a short table.
3. Change one permission and predict which request should be allowed or rejected.
4. Add an unauthorized and an ownership-mismatch fixture.
5. Reproduce the client-only or hidden-button protection mistake.
6. Repair the authoritative server-side check before data access or mutation.
7. Inspect cookie flags, expiry, secret ownership, and environment boundaries.
8. Add a test for a forbidden actor that cannot read or mutate another record.
9. Explain why Proxy or a redirect is not final authorization.
10. Apply the policy to a local protected case route with synthetic sessions, permissions, and unauthorized fixtures with invented actors and records.
11. Document the exact trust boundary: identity and navigation checks versus server-side data and mutation authority.
12. Write residual-risk notes for session rotation, logging, and deployment configuration.
