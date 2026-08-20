# Day 013 practice: useState and setters

Read the [lesson](../day_013_usestate_and_setters.md) first. Use the React playground from the [examples guide](../../examples/README.md). Write your prediction before each run.

## Level 1 — Mechanical confidence

1. Run the one-update counter and record the first two visible results.
2. Predict and run two direct updates in one handler.
3. Replace the direct updates with functional updaters and explain the difference.
4. Log the current snapshot immediately after a setter and explain what you observe.

## Level 2 — Applied practice

5. Create a `Profile` object with two fields and update only one using object spread.
6. Deliberately drop a field with a replacement object and repair it.
7. Build two controlled inputs backed by one object state.
8. Add reset behavior and a visible initial-state summary.

## Level 3 — Synthesis

9. Write a sequence of three updates and predict the result for direct and functional forms.
10. Add a test or written acceptance check for preserving the untouched object field.
11. Explain why a React state setter is not a JavaScript property setter; connect this to Day 061 later in the course.
12. Write a review note naming the snapshot, pending updates, state owner, evidence, limitation, and why a reducer is not yet necessary.
