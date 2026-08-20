# Day 007 hints: JSX and the rules of markup

These hints are deliberately specific enough to unblock you but not to replace the attempt. Use the [lesson](../day_007_jsx_and_the_rules_of_markup.md) and [setup guide](../../SETUP.md) first.

## Hints

1. Use the word **What is JSX?** in your definition, then connect it to an observable input and output rather than a dictionary slogan.
2. Do not change the example before the first run. If it fails, verify the current directory and the starter's package scripts.
3. Make one trace row per meaningful line. Include the value before and after a setter, render, request, or boundary decision.
4. Change exactly one input. If you change the code and the input together, you will not know what caused the result.
5. Boundary behavior is part of the feature. Decide who owns the empty, invalid, pending, or unauthorized case before coding it.
6. Start from the smallest broken line. Do not disable TypeScript, remove a dependency array, or hide an error with a broad catch.
7. **What is JSX?** and **Why must JSX have one returned root?** may be related without being interchangeable. Compare who creates the value and who is allowed to change it.
8. Prefer a small explicit boundary over a global workaround. For Next.js, state whether the code runs on the server or in the browser.
9. Assert user-visible behavior or a clear contract. A test that only checks a private implementation detail will not protect the lesson's idea.
10. Use the same local fixture throughout. Keep the feature small enough that you can explain every file in the review.
11. A build proves only that the checked build completed. It does not prove that every user path, device, permission, or failure mode works.
12. A good review note is reproducible: another learner should know what to run, what should happen, and what remains uncertain.
