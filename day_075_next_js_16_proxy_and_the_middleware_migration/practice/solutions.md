# Day 075 solution guide: Next.js 16 Proxy and the middleware migration

Use this guide after attempting the numbered exercises in this lesson. It reviews the decisions for **Next.js 16 Proxy and the middleware migration**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to next.js 16 proxy and the middleware migration rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a local protected case route with synthetic sessions, permissions, and unauthorized fixtures.
3. The trace identifies the owner and boundary: identity and navigation checks versus server-side data and mutation authority.
4. The normal change isolates one input and preserves the rule for What changed from middleware.ts to proxy.ts?.
5. The boundary case for What does Proxy run before? has deliberate behavior and an explanation.
6. The failure `Protect only with a client-side redirect and call Proxy authorization complete, then repair the server data check.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection.
8. The quality requirement for How does a matcher limit scope? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a local protected case route with synthetic sessions, permissions, and unauthorized fixtures with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary identity and navigation checks versus server-side data and mutation authority.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
