# Day 079 solution guide: Full-stack testing with Playwright and synthetic fixtures

Use this guide after attempting [the exercises](exercises.md). It reviews the decisions for **Full-stack testing with Playwright and synthetic fixtures**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to full-stack testing with playwright and synthetic fixtures rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a local synthetic case journey with normal, invalid, empty, and failure fixtures.
3. The trace identifies the owner and boundary: the public behavior under test and the internal implementation that may change.
4. The normal change isolates one input and preserves the rule for What should each test level prove?.
5. The boundary case for How do we test a protected route? has deliberate behavior and an explanation.
6. The failure `Assert only that a private component function was called and skip the browser contract, then repair the test around user behavior.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A component can render and still be wrong for the user's actual journey, especially at empty, error, keyboard, or unauthorized boundaries.
8. The quality requirement for What is a safe fixture? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a local synthetic case journey with normal, invalid, empty, and failure fixtures with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary the public behavior under test and the internal implementation that may change.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
