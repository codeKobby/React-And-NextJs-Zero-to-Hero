# Day 012 hints: What is state?

Use these after attempting the the numbered exercises in this lesson. Start with the [lesson](../day_012_what_is_state.md) and the local [React playground](../../examples/README.md).

1. Record two columns: what the console prints and what the screen displays. They are allowed to differ in the broken example.
2. `useState` needs an import, a current value, and a setter. Keep the button and paragraph unchanged while making the ownership change.
3. The first array item is the snapshot; the second is the function that requests the next value.
4. The handler is created during a render and reads that render's snapshot when it runs.
5. Write the expected state after each event before adding the buttons.
6. For a list, React needs a stable key for each record. The array itself is the state; the list markup is derived from it.
7. An empty state is a user-facing result, not an error to hide. Choose the sentence before writing the conditional.
8. `aria-live` belongs on a short status that changes meaningfully; do not announce the entire list on every change.
9. A local variable can change in an event handler without causing React to call the component again.
10. An initializer function is useful when calculating the initial value is more work than reading a literal, but do not add it only for style.
11. Test the normal list, empty list, clearing an empty list, and restoring one item separately.
12. The state owner is the component that can make the decision and provide the value to the parts that need it.
