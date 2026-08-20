# Day 040 hints: Root app versus src/app

Use these after attempting the [exercises](exercises.md). They are specific to **Root app versus src/app** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: A new Next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous.
2. Run the smallest example unchanged and inspect the evidence for a small App Router starter whose source, configuration, and public assets have named homes.
3. Trace the input, operation, output, and owner at application source versus root configuration and the route files Next.js recognizes.
4. Change exactly one input related to Why use src?; keep the rule fixed.
5. For When is root-level app simpler?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Keep duplicate routers or treat generated configuration as magic that should never be inspected.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test Which files stay at root?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply root app versus src/app to a small App Router starter whose source, configuration, and public assets have named homes.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: application source versus root configuration and the route files Next.js recognizes.
