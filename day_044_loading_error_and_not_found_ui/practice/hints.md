# Day 044 hints: Loading, error, and not-found UI

Use these after attempting the [exercises](exercises.md). They are specific to **Loading, error, and not-found UI** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: Learners need a concrete reason to study loading, error, and not-found ui before the terminology becomes useful.
2. Run the smallest example unchanged and inspect the evidence for a small local fixture that demonstrates loading, error, and not-found ui.
3. Trace the input, operation, output, and owner at the code or framework boundary that owns the decision in this lesson.
4. Change exactly one input related to What should users see while data loads?; keep the rule fixed.
5. For What does error.tsx catch?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Copy the syntax without identifying the input, owner, output, and boundary.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test When do we use notFound()?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply loading, error, and not-found ui to a small local fixture that demonstrates loading, error, and not-found ui.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: the code or framework boundary that owns the decision in this lesson.
