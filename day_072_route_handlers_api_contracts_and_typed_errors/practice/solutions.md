# Day 072 solution guide: Route Handlers, API contracts, and typed errors

Use this guide after attempting the numbered exercises in this lesson. It reviews the decisions for **Route Handlers, API contracts, and typed errors**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to route handlers, api contracts, and typed errors rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a local synthetic Route Handler with typed success and error JSON.
3. The trace identifies the owner and boundary: public HTTP contract versus private data-access and authorization decisions.
4. The normal change isolates one input and preserves the rule for When should an app expose an HTTP endpoint?.
5. The boundary case for How do we shape a successful response? has deliberate behavior and an explanation.
6. The failure `Return 200 for malformed input and leak a stack trace, then repair the status and public error shape.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: Sometimes a browser, test, webhook, or other client needs a documented HTTP boundary rather than a component-only interaction.
8. The quality requirement for Which status represents invalid input? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a local synthetic Route Handler with typed success and error JSON with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary public HTTP contract versus private data-access and authorization decisions.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
