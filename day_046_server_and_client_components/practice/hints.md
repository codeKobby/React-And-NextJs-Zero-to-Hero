# Day 046 hints: Server and Client Components

Use these after attempting the [exercises](exercises.md). They are specific to **Server and Client Components** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: A page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate.
2. Run the smallest example unchanged and inspect the evidence for a local case dashboard built from a shell, summary, list, and card.
3. Trace the input, operation, output, and owner at the parent-to-child data flow and the responsibility owned by each component.
4. Change exactly one input related to Which components are Server by default?; keep the rule fixed.
5. For When is use client required?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Split every element mechanically or use a lowercase component name that JSX treats as a browser element.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test What props can cross the boundary?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply server and client components to a local case dashboard built from a shell, summary, list, and card.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: the parent-to-child data flow and the responsibility owned by each component.
