# Day 054 hints: Testing Next.js applications

Use these only after attempting the numbered exercises in [the lesson](../day_054_testing_next_js_applications.md). They are specific to **Testing Next.js applications** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: A component can render and still be wrong for the user's actual journey, especially at empty, error, keyboard, or unauthorized boundaries.
2. Run the smallest example unchanged and inspect the evidence for a local synthetic case journey with normal, invalid, empty, and failure fixtures.
3. Trace the input, operation, output, and owner at the public behavior under test and the internal implementation that may change.
4. Change exactly one input related to What should be tested at each level?; keep the rule fixed.
5. For How do we test a Server Action?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Assert a private implementation detail while skipping the visible contract the learner actually needs to protect.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test What is a safe fixture?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply testing next.js applications to a local synthetic case journey with normal, invalid, empty, and failure fixtures.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: the public behavior under test and the internal implementation that may change.
