# Day 067 practice: Schema validation with Zod-style boundaries

Use this worksheet after reading [the lesson](../day_067_schema_validation_with_zod_style_boundaries.md). Start with the [course README](../../README.md), confirm the [setup guide](../../SETUP.md), and choose the local fixture from the [examples guide](../../examples/README.md). This worksheet is designed for **Schema validation with Zod-style boundaries** and uses only local, synthetic, bounded data.

## How to submit your own evidence

For every task, record a prediction before running it, save the smallest relevant code or written artifact, copy the observed result, and explain why it happened. Do not open the solution guide until you have attempted the work.

## Exercises

1. Define **Why validate at a boundary?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **What is the difference between parse and safeParse?**, then predict before running.
5. Create a boundary case involving **How do schemas describe form data?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Trust formData.get('title') as a string and repair the schema boundary before calling the database.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply schema validation with zod-style boundaries to a local case form with structured invalid-input feedback with a local synthetic fixture.
11. Explain the owner and boundary: untrusted input crossing into typed application logic.
12. Write a review note with evidence, one limitation, and the next learning step.
