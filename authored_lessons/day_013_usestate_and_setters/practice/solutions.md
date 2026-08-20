# Day 013 solution route: useState and setters

Use this route after attempting the [exercises](exercises.md). The goal is to compare state-update decisions and evidence, not to memorize a code shape.

1. One direct update changes the next render by one.
2. Two direct updates can request the same value because both read the same snapshot.
3. Two functional updates are applied in order and therefore increase the value by two.
4. The immediate log can show the old snapshot because the setter requests a later render.
5. Object spread preserves the untouched field while creating a new reference.
6. The replacement-object failure drops missing fields; the repair copies the current object first.
7. A controlled input reads from state and sends its new string through an `onChange` handler.
8. Reset returns the state object to the documented initial shape and the visible summary reflects it.
9. The direct and functional three-update predictions differ for the same reason as the two-update example.
10. The acceptance check fails when the untouched field disappears, so it protects the actual lesson concept.
11. A property setter intercepts JavaScript property assignment; a React state setter schedules a next state snapshot and render.
12. The review note names the render snapshot, pending update queue, component owner, evidence, limitation, and reason a reducer is not yet needed.

A strong solution can explain both the result and the timeline that produced it. “React batches it” is not enough; state which snapshot each update reads or receives.
