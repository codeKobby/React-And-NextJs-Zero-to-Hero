# Day 076 hints: Authorization, roles, ownership, and multi-tenant data

Use these after attempting the the numbered exercises in this lesson. They are specific to **Authorization, roles, ownership, and multi-tenant data** and should unblock the next thought without replacing it.

## Hints

1. Begin with the learner problem: A full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection.
2. Run the smallest example unchanged and inspect the evidence for a local protected case route with synthetic sessions, permissions, and unauthorized fixtures.
3. Trace the input, operation, output, and owner at identity and navigation checks versus server-side data and mutation authority.
4. Change exactly one input related to What is authorization?; keep the rule fixed.
5. For How do roles differ from permissions?, decide the normal and boundary behavior before coding.
6. Reproduce the likely mistake: Treat a browser field, client redirect, or login flag as proof of permission and return data before the server policy runs.
7. Repair the smallest line or boundary; do not hide the failure with a broad workaround.
8. Keep the data local and synthetic while you test Why must ownership filter the query?.
9. Assert a visible result or public contract rather than a private implementation detail.
10. Use the same fixture to apply authorization, roles, ownership, and multi-tenant data to a local protected case route with synthetic sessions, permissions, and unauthorized fixtures.
11. A passing build proves only the checked build completed; record what remains untested.
12. Your review note should name the owner, evidence, limitation, and boundary: identity and navigation checks versus server-side data and mutation authority.
