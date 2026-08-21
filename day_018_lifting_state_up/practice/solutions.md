# Day 018 solution guide: Lifting state up

Use this guide only after attempting the numbered exercises in [the lesson](../day_018_lifting_state_up.md). It reviews the decisions for **Lifting state up**; it is not a copied answer key.

## Review checkpoints

1. The learner can say what problem lifting state up solves in one or two simple sentences.
2. The example runs and the learner records the visible or returned result for a small local example.
3. The learner can point to the input, the important line, and the output.
4. The learner changes one input for When should state move to a parent? and records the old and new result.
5. The learner tries a normal and an empty or bad value for How do siblings share state?.
6. The learner reproduces `Give each sibling its own text state and repair the split-brain UI.` and writes down the error or wrong result.
7. The learner fixes the smallest line and runs the normal case again.
8. The learner uses local invented data to show What belongs in the parent?.
9. The test or check fails when the visible behavior is removed and passes after it is restored.
10. The learner builds a small local example without exposing secrets or using real data.
11. The learner writes one thing the example does not prove about a real application.
12. The learner’s review note uses plain sentences and defines any technical word it needs.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
