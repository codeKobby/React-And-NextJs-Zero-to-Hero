# Day 006 hints: What is a component?

Use these after attempting the the numbered exercises in this lesson. If the project does not run, return to the [README](../../README.md), [setup guide](../../SETUP.md), and [examples guide](../../examples/README.md).

1. Start by preserving the visible page. A refactor can improve ownership without changing the user's result.
2. Give `Header`, `Main`, and `Footer` one responsibility each; do not split every element into a component.
3. A function component returns JSX. The function name is capitalized so JSX treats it as a user-defined component.
4. A prop is input from the parent. The child should read it, not assign to it.
5. Put the array in the parent that coordinates the page. Let the card own only one item's markup.
6. A stable key identifies a record across renders; a displayed title can change and an index can move.
7. Ask what the user should see when `cases.length === 0` before writing the conditional.
8. `Summary` needs only a count. Passing the count makes its responsibility explicit.
9. Lowercase JSX names are interpreted as intrinsic elements. Compare the generated element name with the function name.
10. Use a union for deliberate statuses, but remember that a type does not validate JSON or a server response at runtime.
11. Choose an accessibility change that improves meaning for a person using a keyboard or assistive technology, not a decorative attribute.
12. Your review note should explain the tree and data direction: parent fixture → child props → returned markup.
