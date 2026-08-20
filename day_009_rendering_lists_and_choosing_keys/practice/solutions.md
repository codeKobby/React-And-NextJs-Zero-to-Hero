# Day 009 solution guide: Rendering lists and choosing keys

Use this guide after attempting [the exercises](exercises.md). It reviews the decisions for **Rendering lists and choosing keys**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to rendering lists and choosing keys rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a case list with stable synthetic IDs and an explicit empty state.
3. The trace identifies the owner and boundary: the data identity crossing from an array record into a rendered list item.
4. The normal change isolates one input and preserves the rule for How do we render a list?.
5. The boundary case for What is a key? has deliberate behavior and an explanation.
6. The failure `Use an array index as a key, reorder the data, and explain the identity bug.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A collection must become repeated UI without losing the identity of one item when order or data changes.
8. The quality requirement for Why is array index a risky key? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a case list with stable synthetic IDs and an explicit empty state with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary the data identity crossing from an array record into a rendered list item.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
