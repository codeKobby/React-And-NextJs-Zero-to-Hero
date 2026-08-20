# Day 076 solution guide: Authorization, roles, ownership, and multi-tenant data

Use this guide after attempting [the exercises](exercises.md). A solution is evidence and reasoning, not a copied file. Compare your work with the [lesson](../day_076_authorization_roles_ownership_and_multi_tenant_data.md), then improve the explanation if your code works for the wrong reason.

## Review checkpoints

1. The definition of **What is authorization?** names an observable rule and points to a concrete lesson example.
2. The unchanged worked example runs in the correct local starter and its output matches the lesson's expected result.
3. The trace identifies the order of evaluation and the owner of each important value.
4. The normal alternative changes one input and preserves the rule for **How do roles differ from permissions?**.
5. The boundary case has deliberate behavior rather than an accidental blank screen, stray value, or unhandled rejection.
6. The broken example reproduces the stated failure, and the repair is the smallest change that restores the normal case without weakening the check.
7. The comparison table distinguishes **What is authorization?** from **How do roles differ from permissions?** by responsibility, lifetime, and direction of data flow.
8. The added quality requirement is visible in the code or project structure and is explained in plain language.
9. The test or assertion fails when the important behavior is removed, then passes after the repair.
10. The local feature has a named boundary, synthetic fixture data, a normal path, and a failure or empty path appropriate to the topic.
11. The limitation statement avoids claiming that a passing build or test proves production readiness.
12. The review note names files, commands, observed evidence, one remaining risk, and the next learning step.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
