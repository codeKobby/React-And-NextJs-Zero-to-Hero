# Day 012 practice: What is state?

Read the [lesson](../day_012_what_is_state.md) first. Use the React playground from the [examples guide](../../examples/README.md). Record a prediction before each run and keep the local fixture synthetic.

## Level 1 — Mechanical confidence

1. Run `BrokenCounter` and record the console count and visible screen count after three clicks.
2. Replace the local variable with `useState` and verify the first, second, and third visible clicks.
3. Explain the two values returned by `useState(0)` in plain language.
4. Move the click logic into a named `addOne` handler and explain what snapshot it closes over.

## Level 2 — Applied practice

5. Add `minusOne` and `Reset` buttons. Predict the sequence `+1, +1, -1, reset` before running it.
6. Replace the number with `Case[]` state and render a list with stable IDs.
7. Add `Clear queue` and a useful empty state for an empty array.
8. Add an `aria-live` summary that reports the current queue size.

## Level 3 — Synthesis

9. Reproduce the local-variable bug and explain why a console change does not prove a screen update.
10. Use an initial state function for a small local fixture and explain why lazy initialization can be useful.
11. Add a test or written acceptance check for normal, empty, repeated-clear, and restored behavior.
12. Write a review note naming the state owner, event boundary, visible evidence, one limitation, and why a reducer is not yet necessary.
