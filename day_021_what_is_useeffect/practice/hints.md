# Day 021 hints: What is useEffect?

Use these after attempting the the numbered exercises in this lesson. They are specific to **What is useEffect?** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: Rendering describes UI, but some work must synchronize with something outside React, such as a title, timer, subscription, or request.
2. Run the smallest example unchanged and inspect the evidence for a local status title or synthetic subscription with setup and cleanup evidence.
3. Trace the input, operation, output, and owner at the line between React's render calculation and an external system's lifecycle.
4. Change exactly one input related to What is an Effect?; keep the rule fixed.
5. For Why is it for synchronization rather than ordinary calculations?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Use an Effect for a value that can be calculated during render or omit a dependency and observe stale work.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test What does the dependency list mean?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply what is useeffect? to a local status title or synthetic subscription with setup and cleanup evidence.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: the line between React's render calculation and an external system's lifecycle.
