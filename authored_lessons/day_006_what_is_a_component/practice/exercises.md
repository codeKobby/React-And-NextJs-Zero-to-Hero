# Day 006 practice: What is a component?

Read the [lesson](../day_006_what_is_a_component.md) first. Use the React playground from the [examples guide](../../examples/README.md). Before editing, read the [README](../../README.md) and [setup guide](../../SETUP.md). Record visible behavior and your prediction before each change.

## Level 1 — Confidence

1. Run Example 1 unchanged. Write the three visible responsibilities of the page.
2. Split the page into `Header`, `Main`, and `Footer` without changing the visible result. Record the before/after output.
3. Explain why each component deserves its boundary. Do not say only “for reuse”; name the responsibility.
4. Create `StatusBadge({ label })` and render it with two different labels.

## Level 2 — Application

5. Create a `Case` array with `id`, `title`, and `status` and render one `CaseCard` per item.
6. Use the stable `id` as the key. Explain why a title or array index can be a weaker identity.
7. Add an empty-state branch for an empty array. Predict the exact sentence the user should see.
8. Add a `Summary` component that receives `count` from the parent rather than reading the array directly.

## Level 3 — Synthesis

9. Rename `CaseCard` to lowercase and reproduce the failure. Repair it and record the cause.
10. Add the `Case` type and explain one check TypeScript performs and one runtime input it cannot validate.
11. Add one accessible requirement: heading hierarchy, visible status text, or an `aria-live` summary. Explain why it belongs to this UI.
12. Write a review note with the component tree, data ownership, changed files, visible evidence, one limitation, and one next refactor.
