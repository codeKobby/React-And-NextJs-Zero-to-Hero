# Day 071 solution guide: Server Actions for validated mutations

Use this guide after attempting the numbered exercises in this lesson. It reviews the decisions for **Server Actions for validated mutations**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to server actions for validated mutations rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a validated local create-case mutation with field errors and revalidation evidence.
3. The trace identifies the owner and boundary: browser intent versus server authority and data mutation.
4. The normal change isolates one input and preserves the rule for What is a Server Action?.
5. The boundary case for Where should validation and authorization happen? has deliberate behavior and an explanation.
6. The failure `Revalidate before the mutation succeeds and trust a client-provided owner ID, then repair the sequence.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A form needs to change server-owned data while preserving validation, authorization, pending state, and a useful result.
8. The quality requirement for How do we return field errors? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a validated local create-case mutation with field errors and revalidation evidence with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary browser intent versus server authority and data mutation.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
