# Day 082 solution guide: Capstone build I: design system, shell, and database-backed reads

Use this guide after attempting the numbered exercises in this lesson. It reviews the decisions for **Capstone build I: design system, shell, and database-backed reads**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to capstone build i: design system, shell, and database-backed reads rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a portfolio-ready local case-management feature with architecture and evidence notes.
3. The trace identifies the owner and boundary: demo evidence versus production claims, operational ownership, and residual risk.
4. The normal change isolates one input and preserves the rule for How do we turn the plan into a vertical slice?.
5. The boundary case for Which UI primitives should be shared? has deliberate behavior and an explanation.
6. The failure `Build the entire dashboard as one client component and pass raw database objects through it, then repair the vertical slice.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan.
8. The quality requirement for How do Server Components read data? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a portfolio-ready local case-management feature with architecture and evidence notes with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary demo evidence versus production claims, operational ownership, and residual risk.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
