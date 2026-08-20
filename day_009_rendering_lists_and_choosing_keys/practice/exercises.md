# Day 009 practice: Rendering lists and choosing keys

Use this worksheet after reading [the lesson](../day_009_rendering_lists_and_choosing_keys.md). Start with the [course README](../../README.md), confirm the [setup guide](../../SETUP.md), and choose the local fixture from the [examples guide](../../examples/README.md). This worksheet is designed for **Rendering lists and choosing keys** and uses only local, synthetic, bounded data.

## How to submit your own evidence

For every task, record a prediction before running it, save the smallest relevant code or written artifact, copy the observed result, and explain why it happened. Do not open the solution guide until you have attempted the work.

## Exercises

1. Define **How do we render a list?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **What is a key?**, then predict before running.
5. Create a boundary case involving **Why is array index a risky key?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Use an array index as a key, reorder the data, and explain the identity bug.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply rendering lists and choosing keys to a case list with stable synthetic IDs and an explicit empty state with a local synthetic fixture.
11. Explain the owner and boundary: the data identity crossing from an array record into a rendered list item.
12. Write a review note with evidence, one limitation, and the next learning step.
