# Day 080 solution guide: Production configuration, CI, and deployment evidence

Use this guide after attempting [the exercises](exercises.md). It reviews the decisions for **Production configuration, CI, and deployment evidence**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to production configuration, ci, and deployment evidence rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a portfolio-ready local case-management feature with architecture and evidence notes.
3. The trace identifies the owner and boundary: demo evidence versus production claims, operational ownership, and residual risk.
4. The normal change isolates one input and preserves the rule for What belongs in an environment variable?.
5. The boundary case for What should CI prove? has deliberate behavior and an explanation.
6. The failure `Commit a secret in an env file and deploy without a migration or rollback plan, then repair the delivery checklist.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan.
8. The quality requirement for How do migrations run safely? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a portfolio-ready local case-management feature with architecture and evidence notes with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary demo evidence versus production claims, operational ownership, and residual risk.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
