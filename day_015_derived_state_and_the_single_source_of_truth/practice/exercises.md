# Day 015 practice: Derived state and the single source of truth

Use this worksheet after reading [the lesson](../day_015_derived_state_and_the_single_source_of_truth.md). Before you start, read the [course README](../../README.md), confirm your tools with the [setup guide](../../SETUP.md), and choose the appropriate local starter from the [examples guide](../../examples/README.md). Work only with local, synthetic data.

## How to submit your own evidence

For every exercise, save the smallest runnable code or written artifact, record your prediction before running it, copy the observed result, and explain the difference in your own words. Do not open the solution guide until you have attempted the task.

## Exercises

1. Define **What is derived state?** in two sentences for a beginner, then point to the exact line in the lesson where the idea first appears.
2. Copy the worked example unchanged into the correct starter project, run it, and record the command, expected result, and observed result.
3. Write a line-by-line execution trace for the worked example. Name the input, operation, output, and owner of each important value.
4. Replace one input with a normal alternative that still demonstrates **Why should we avoid storing what can be calculated?**. Predict the result before running it.
5. Create a boundary case involving **What is one source of truth?**. Decide whether the correct behavior is a value, an empty state, a compiler error, a loading state, or a failure message, and justify that choice.
6. Reproduce this deliberate failure: **Store completedCount separately, create a mismatch, and repair by deriving it.**. Capture the error or incorrect behavior, name the violated assumption, and repair the smallest possible change.
7. Compare **What is derived state?** and **Why should we avoid storing what can be calculated?** in a short table. Include ownership, data flow, and one situation where confusing them causes a bug.
8. Add one quality requirement to the fixture: a meaningful accessible name, a type guard, a loading state, an error state, or a server/client boundary declaration. Explain why it belongs there.
9. Add a focused test or assertion for the most important behavior. The test must fail when that behavior is removed and pass after the repair.
10. Apply the lesson to a small local feature using invented data. Write the component, route, or function boundary before writing the implementation.
11. Write a limitation statement: explain what your successful run does **not** prove about production correctness, security, performance, or accessibility.
12. Prepare a review note for a teammate. Include the changed files, evidence you collected, one remaining risk, and the next lesson you are ready to study.
