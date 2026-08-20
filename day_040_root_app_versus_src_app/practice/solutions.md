# Day 040 solution guide: Root app versus src/app

Use this guide after attempting [the exercises](exercises.md). It reviews the decisions for **Root app versus src/app**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to root app versus src/app rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a small App Router starter whose source, configuration, and public assets have named homes.
3. The trace identifies the owner and boundary: application source versus root configuration and the route files Next.js recognizes.
4. The normal change isolates one input and preserves the rule for Why use src?.
5. The boundary case for When is root-level app simpler? has deliberate behavior and an explanation.
6. The failure `Move app into src but leave an empty root app, then repair the ambiguous project.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A new Next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous.
8. The quality requirement for Which files stay at root? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a small App Router starter whose source, configuration, and public assets have named homes with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary application source versus root configuration and the route files Next.js recognizes.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
