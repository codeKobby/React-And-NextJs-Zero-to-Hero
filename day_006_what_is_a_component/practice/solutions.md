# Day 006 solution route: What is a component?

Compare your work with the [lesson](../day_006_what_is_a_component.md) after attempting the the numbered exercises in this lesson. The goal is to explain decisions, not copy a page.

1. The original page has welcome, queue, and closing responsibilities.
2. The split page keeps the same visible output while giving each responsibility a named owner.
3. A component boundary is justified by responsibility, composition, reuse, independent behavior, or a meaningful test—not by a fixed size rule.
4. `StatusBadge` receives a label and renders it; the parent decides which label to provide.
5. Each `CaseCard` receives one record and returns one list item.
6. The stable ID represents record identity even if the title changes; the array index represents position, not identity.
7. The empty branch explains that no synthetic cases are waiting rather than rendering a blank list.
8. `Summary` receives a count because the parent owns the array and the summary needs only the derived value.
9. Lowercase JSX is interpreted as a browser element; capitalization tells React to use the user-defined function.
10. TypeScript checks fields and allowed status values at compile time, but runtime data still needs validation.
11. The accessibility addition has visible or announced meaning and is paired with appropriate semantic HTML.
12. The review note includes the component tree, parent-to-child data flow, commands, visible result, limitation, and next refactor.

A strong submission can recreate the smallest page from an empty file and explain why the parent owns the fixture while the child owns one item's markup.
