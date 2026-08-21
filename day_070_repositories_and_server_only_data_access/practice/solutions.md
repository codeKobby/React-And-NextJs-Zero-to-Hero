# Day 070 solution guide: Repositories and server-only data access

Use this guide only after attempting the numbered exercises in [the lesson](../day_070_repositories_and_server_only_data_access.md). It reviews the decisions for **Repositories and server-only data access**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to repositories and server-only data access rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a small local fixture that demonstrates repositories and server-only data access.
3. The trace identifies the owner and boundary: the code or framework boundary that owns the decision in this lesson.
4. The normal change isolates one input and preserves the rule for Why isolate database calls?.
5. The boundary case for What is a repository? has deliberate behavior and an explanation.
6. The failure `Import the repository into a Client Component and return database rows with secrets, then repair both boundaries.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: Learners need a concrete reason to study repositories and server-only data access before the terminology becomes useful.
8. The quality requirement for What data should cross into a Client Component? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a small local fixture that demonstrates repositories and server-only data access with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary the code or framework boundary that owns the decision in this lesson.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
