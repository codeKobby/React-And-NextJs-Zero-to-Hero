# Day 027 solution guide: Function components versus class components

Use this guide after attempting the numbered exercises in this lesson. It reviews the decisions for **Function components versus class components**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to function components versus class components rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a local case dashboard built from a shell, summary, list, and card.
3. The trace identifies the owner and boundary: the parent-to-child data flow and the responsibility owned by each component.
4. The normal change isolates one input and preserves the rule for What is a class component?.
5. The boundary case for What is a function component? has deliberate behavior and an explanation.
6. The failure `Use `this` inside a function component and repair the migration with useState.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate.
8. The quality requirement for How do lifecycle methods map to Hooks? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a local case dashboard built from a shell, summary, list, and card with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary the parent-to-child data flow and the responsibility owned by each component.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
