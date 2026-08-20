# Day 078 practice: Error taxonomy, logging, and instrumentation

Use this worksheet after reading [the lesson](../day_078_error_taxonomy_logging_and_instrumentation.md). Start with the [course README](../../README.md), confirm the [setup guide](../../SETUP.md), and choose the local fixture from the [examples guide](../../examples/README.md). This worksheet is designed for **Error taxonomy, logging, and instrumentation** and uses only local, synthetic, bounded data.

## How to submit your own evidence

For every task, record a prediction before running it, save the smallest relevant code or written artifact, copy the observed result, and explain why it happened. Do not open the solution guide until you have attempted the work.

## Exercises

1. Define **What is the difference between an expected and unexpected error?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **What should a structured log contain?**, then predict before running.
5. Create a boundary case involving **Why use a request ID?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Log an entire request body and expose a stack trace to the user, then repair the event fields and public error.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply error taxonomy, logging, and instrumentation to a small local fixture that demonstrates error taxonomy, logging, and instrumentation with a local synthetic fixture.
11. Explain the owner and boundary: the code or framework boundary that owns the decision in this lesson.
12. Write a review note with evidence, one limitation, and the next learning step.
