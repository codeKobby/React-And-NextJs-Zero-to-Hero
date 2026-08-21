# Day 075 solution guide: Next.js 16 Proxy and the middleware migration

Use this guide only after attempting the numbered exercises in [the lesson](../day_075_next_js_16_proxy_and_the_middleware_migration.md). It reviews the decisions for **Next.js 16 Proxy and the middleware migration**; it is not a copied answer key.

## Review checkpoints

1. The learner can say what problem next.js 16 proxy and the middleware migration solves in one or two simple sentences.
2. The example runs and the learner records the visible or returned result for a local protected case route with synthetic sessions, permissions, and unauthorized fixtures.
3. The learner can point to the input, the important line, and the output.
4. The learner changes one input for What changed from middleware.ts to proxy.ts? and records the old and new result.
5. The learner tries a normal and an empty or bad value for What does Proxy run before?.
6. The learner reproduces `Protect only with a client-side redirect and call Proxy authorization complete, then repair the server data check.` and writes down the error or wrong result.
7. The learner fixes the smallest line and runs the normal case again.
8. The learner uses local invented data to show How does a matcher limit scope?.
9. The test or check fails when the visible behavior is removed and passes after it is restored.
10. The learner builds a local protected case route with synthetic sessions, permissions, and unauthorized fixtures without exposing secrets or using real data.
11. The learner writes one thing the example does not prove about a real application.
12. The learner’s review note uses plain sentences and defines any technical word it needs.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
