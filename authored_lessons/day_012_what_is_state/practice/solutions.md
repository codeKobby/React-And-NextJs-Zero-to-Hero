# Day 012 solution route: What is state?

Use this route after attempting the [exercises](exercises.md). Compare the evidence and reasoning with the [lesson](../day_012_what_is_state.md), not just the final screen.

1. The broken counter's console increases while the screen can remain at zero because changing a local variable does not request a render.
2. `useState` gives React ownership; the screen reflects the current snapshot after each setter request is processed.
3. The first value is the snapshot for the current render; the second is the setter request function.
4. The named handler closes over the render's snapshot and calls the setter when the click occurs.
5. The sequence ends at zero after two increments, one decrement, and reset.
6. The queue is state because it changes over time and the screen must reflect its current records.
7. Clearing produces a meaningful empty message and does not leave a blank or stale list.
8. The status reports a concise current count and does not expose internal implementation details.
9. The explanation separates console evidence from screen evidence and names the missing render request.
10. The initializer function is justified by a real initialization cost or source, not inserted as unexplained ceremony.
11. The acceptance evidence covers normal, empty, repeated-clear, and restored paths.
12. The review note names the component owner, event path, user-visible evidence, limitation, and reason a reducer would add unnecessary complexity today.

A strong solution can explain why a state update produces a later render without claiming that state is a mutable global variable.
