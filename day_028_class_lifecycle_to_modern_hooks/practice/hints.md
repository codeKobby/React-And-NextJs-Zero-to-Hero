# Day 028 hints: Class lifecycle to modern Hooks

Use these after attempting the [exercises](exercises.md). They are specific to **Class lifecycle to modern Hooks** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: Several components need the same stateful behavior, but copying the behavior creates inconsistent fixes and unclear APIs.
2. Run the smallest example unchanged and inspect the evidence for a local toggle, data viewer, or form behavior with a named Hook API.
3. Trace the input, operation, output, and owner at the Hook owns reusable behavior while the component owns its visible composition.
4. Change exactly one input related to What did lifecycle methods do?; keep the rule fixed.
5. For How does one Effect model synchronization?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Call a Hook conditionally or hide unrelated responsibilities in a Hook with an unclear contract.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test Why is lifecycle-to-Effect translation not mechanical?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply class lifecycle to modern hooks to a local toggle, data viewer, or form behavior with a named Hook API.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: the Hook owns reusable behavior while the component owns its visible composition.
