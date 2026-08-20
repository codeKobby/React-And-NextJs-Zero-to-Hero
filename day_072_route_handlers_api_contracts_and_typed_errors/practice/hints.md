# Day 072 hints: Route Handlers, API contracts, and typed errors

Use these after attempting the the numbered exercises in this lesson. They are specific to **Route Handlers, API contracts, and typed errors** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: Sometimes a browser, test, webhook, or other client needs a documented HTTP boundary rather than a component-only interaction.
2. Run the smallest example unchanged and inspect the evidence for a local synthetic Route Handler with typed success and error JSON.
3. Trace the input, operation, output, and owner at public HTTP contract versus private data-access and authorization decisions.
4. Change exactly one input related to When should an app expose an HTTP endpoint?; keep the rule fixed.
5. For How do we shape a successful response?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Return 200 for invalid input, leak stack traces, or confuse an internal function result with an HTTP response.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test Which status represents invalid input?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply route handlers, api contracts, and typed errors to a local synthetic Route Handler with typed success and error JSON.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: public HTTP contract versus private data-access and authorization decisions.
