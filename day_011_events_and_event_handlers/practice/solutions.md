# Day 011 solution guide: Events and event handlers

Use this guide only after attempting the numbered exercises in [the lesson](../day_011_events_and_event_handlers.md). It reviews the decisions for **Events and event handlers**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to events and event handlers rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a small local fixture that demonstrates events and event handlers.
3. The trace identifies the owner and boundary: the code or framework boundary that owns the decision in this lesson.
4. The normal change isolates one input and preserves the rule for What is an event handler?.
5. The boundary case for Why pass a function instead of calling it? has deliberate behavior and an explanation.
6. The failure `Write onClick={handleClick()} and repair the immediate invocation.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: Learners need a concrete reason to study events and event handlers before the terminology becomes useful.
8. The quality requirement for How do we read event data? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a small local fixture that demonstrates events and event handlers with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary the code or framework boundary that owns the decision in this lesson.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
