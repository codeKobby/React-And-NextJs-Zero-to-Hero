# Day 008 hints: Props and one-way data flow

Use these after attempting the [exercises](exercises.md). They are specific to **Props and one-way data flow** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: A child needs data from its parent and a way to request intent without reaching into the parent's private state.
2. Run the smallest example unchanged and inspect the evidence for a reusable case card and button whose parent owns the data.
3. Trace the input, operation, output, and owner at props flow down; callbacks carry intent up; the owner decides whether state changes.
4. Change exactly one input related to What are props?; keep the rule fixed.
5. For Why should a child not mutate props?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Treat read-only props as local mutable storage or create a second copy that can disagree with the owner.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test How does data move down?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply props and one-way data flow to a reusable case card and button whose parent owns the data.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: props flow down; callbacks carry intent up; the owner decides whether state changes.
