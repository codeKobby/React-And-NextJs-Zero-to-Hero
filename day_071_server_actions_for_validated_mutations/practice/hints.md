# Day 071 hints: Server Actions for validated mutations

Use these after attempting the the numbered exercises in this lesson. They are specific to **Server Actions for validated mutations** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: A form needs to change server-owned data while preserving validation, authorization, pending state, and a useful result.
2. Run the smallest example unchanged and inspect the evidence for a validated local create-case mutation with field errors and revalidation evidence.
3. Trace the input, operation, output, and owner at browser intent versus server authority and data mutation.
4. Change exactly one input related to What is a Server Action?; keep the rule fixed.
5. For Where should validation and authorization happen?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Trust a client-provided owner, validate only in the browser, or refresh the page before the mutation succeeds.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test How do we return field errors?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply server actions for validated mutations to a validated local create-case mutation with field errors and revalidation evidence.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: browser intent versus server authority and data mutation.
