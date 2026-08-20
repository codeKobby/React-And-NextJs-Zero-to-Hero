# Day 022 solution guide: Effect dependencies and cleanup

Use this guide after attempting [the exercises](exercises.md). It reviews the decisions for **Effect dependencies and cleanup**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to effect dependencies and cleanup rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a local status title or synthetic subscription with setup and cleanup evidence.
3. The trace identifies the owner and boundary: the line between React's render calculation and an external system's lifecycle.
4. The normal change isolates one input and preserves the rule for What is a stale closure?.
5. The boundary case for Why must dependencies be complete? has deliberate behavior and an explanation.
6. The failure `Omit query from dependencies and explain the stale result.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: Rendering describes UI, but some work must synchronize with something outside React, such as a title, timer, subscription, or request.
8. The quality requirement for How do we clean up a subscription? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a local status title or synthetic subscription with setup and cleanup evidence with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary the line between React's render calculation and an external system's lifecycle.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
