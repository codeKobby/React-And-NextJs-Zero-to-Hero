# Day 009 hints: Rendering lists and choosing keys

Use these only after attempting the numbered exercises in [the lesson](../day_009_rendering_lists_and_choosing_keys.md). They are specific to **Rendering lists and choosing keys** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: A collection must become repeated UI without losing the identity of one item when order or data changes.
2. Run the smallest example unchanged and inspect the evidence for a case list with stable synthetic IDs and an explicit empty state.
3. Trace the input, operation, output, and owner at the data identity crossing from an array record into a rendered list item.
4. Change exactly one input related to How do we render a list?; keep the rule fixed.
5. For What is a key?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Use position as identity and then observe state or focus appear attached to the wrong item after reordering.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test Why is array index a risky key?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply rendering lists and choosing keys to a case list with stable synthetic IDs and an explicit empty state.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: the data identity crossing from an array record into a rendered list item.
