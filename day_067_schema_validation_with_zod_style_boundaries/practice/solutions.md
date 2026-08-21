# Day 067 solution guide: Schema validation with Zod-style boundaries

Use this guide only after attempting the numbered exercises in [the lesson](../day_067_schema_validation_with_zod_style_boundaries.md). It reviews the decisions for **Schema validation with Zod-style boundaries**; it is not a copied answer key.

## Review checkpoints

1. The learner can say what problem schema validation with zod-style boundaries solves in one or two simple sentences.
2. The example runs and the learner records the visible or returned result for a local case form with structured invalid-input feedback.
3. The learner can point to the input, the important line, and the output.
4. The learner changes one input for Why validate at a boundary? and records the old and new result.
5. The learner tries a normal and an empty or bad value for What is the difference between parse and safeParse?.
6. The learner reproduces `Trust formData.get('title') as a string and repair the schema boundary before calling the database.` and writes down the error or wrong result.
7. The learner fixes the smallest line and runs the normal case again.
8. The learner uses local invented data to show How do schemas describe form data?.
9. The test or check fails when the visible behavior is removed and passes after it is restored.
10. The learner builds a local case form with structured invalid-input feedback without exposing secrets or using real data.
11. The learner writes one thing the example does not prove about a real application.
12. The learner’s review note uses plain sentences and defines any technical word it needs.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
