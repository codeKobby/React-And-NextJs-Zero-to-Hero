# Day 008 solution guide: Props and one-way data flow

Use this guide after attempting [the exercises](exercises.md). It reviews the decisions for **Props and one-way data flow**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to props and one-way data flow rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a reusable case card and button whose parent owns the data.
3. The trace identifies the owner and boundary: props flow down; callbacks carry intent up; the owner decides whether state changes.
4. The normal change isolates one input and preserves the rule for What are props?.
5. The boundary case for Why should a child not mutate props? has deliberate behavior and an explanation.
6. The failure `Attempt to assign to a prop and replace the mutation with a callback.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A child needs data from its parent and a way to request intent without reaching into the parent's private state.
8. The quality requirement for How does data move down? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a reusable case card and button whose parent owns the data with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary props flow down; callbacks carry intent up; the owner decides whether state changes.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
