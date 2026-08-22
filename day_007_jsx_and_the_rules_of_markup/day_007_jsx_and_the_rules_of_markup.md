# Day 007: JSX and the rules of markup

[← Previous lesson](../day_006_what_is_a_component/day_006_what_is_a_component.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_008_props_and_one_way_data_flow/day_008_props_and_one_way_data_flow.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is JSX?](#what-is-jsx)
  - [Why does JSX need a returned root?](#why-does-jsx-need-a-returned-root)
  - [How do JavaScript expressions enter JSX?](#how-do-javascript-expressions-enter-jsx)
  - [What changes from HTML to JSX?](#what-changes-from-html-to-jsx)
  - [How do we keep JSX accessible and safe?](#how-do-we-keep-jsx-accessible-and-safe)
- [Worked example](#worked-example)
  - [Example 1: one element](#example-1-one-element)
  - [Example 2: a page-shaped tree](#example-2-a-page-shaped-tree)
  - [Example 3: data inside JSX](#example-3-data-inside-jsx)
  - [Example 4: a reusable card](#example-4-a-reusable-card)
- [Line-by-line explanation](#line-by-line-explanation)
- [Execution trace](#execution-trace)
- [Prediction experiment](#prediction-experiment)
- [Broken example and repair](#broken-example-and-repair)
- [Guided practice before independent work](#guided-practice-before-independent-work)
- [Project application](#project-application)
- [Independent exercises](#independent-exercises)
- [Finish line](#finish-line)
- [References](#references)

## Start here

Read the [README](../README.md), confirm the [setup guide](../SETUP.md), and open the [examples guide](../examples/README.md). Use the React playground rather than adding a new dependency:

```bash
cd examples/react-playground
pnpm install
pnpm dev
```

Open the local URL printed by Vite. Run the starter unchanged first. In this lesson you will keep the same visible goal while changing one thing at a time: first one JSX element, then a page-shaped tree, then JavaScript data, then a reusable component.

## Why this lesson exists

In the browser, HTML describes a document. In React, a component returns a description of the UI tree that should appear. JSX is the readable notation that lets us write that tree beside ordinary JavaScript. It looks like HTML, but it follows JavaScript and React rules too.

The original beginner trap is to treat JSX as either “just HTML” or “magic React.” It is neither. A compiler transforms JSX syntax into JavaScript calls, and React uses the resulting element description to render the interface. You do not need to memorise the compiler output today, but you do need to know which parts are markup, which parts are JavaScript expressions, and which rules the compiler will enforce.

We will build a small **local case desk**. The content is invented and safe: a heading, a queue of review items, and a status. The page will look simple, but every change will answer a real beginner question.

## Prerequisites

You should understand JavaScript values and functions, have completed [Day 006](../day_006_what_is_a_component/day_006_what_is_a_component.md), and be able to run the React playground. You do not need state, Effects, routing, or Next.js yet.

## Outcomes

By the end you will be able to explain what JSX is, return one valid JSX tree, place JavaScript expressions inside braces, translate common HTML attributes into JSX, render a collection of synthetic records, and repair a malformed JSX example. You will also be able to explain why semantic HTML and escaped text remain important inside a React component.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| **JSX** | JavaScript syntax that describes a tree of UI elements using markup-like notation. |
| **Element** | A value describing one item in the UI tree, such as a heading or button. |
| **Expression** | JavaScript code that produces a value and can be placed inside JSX braces. |
| **Root** | The one outer JSX element or fragment returned by one expression. |
| **Fragment** | `<>...</>` grouping that returns several siblings without adding a DOM element. |
| **Prop** | A named input placed on a JSX element or component. |
| **`className`** | The JSX prop that corresponds to the HTML `class` attribute. |
| **Escaping** | Treating text as text instead of interpreting it as executable markup. |
| **Semantic HTML** | Choosing elements for their meaning and built-in browser behavior. |

## Topics

### What is JSX?

JSX is a syntax extension used in JavaScript and TypeScript files. The angle brackets describe an element tree; braces mark the places where JavaScript expressions are evaluated. JSX does not make a string of HTML. It creates a structured description that React can render.

### Why does JSX need a returned root?

A function returns one value. A JSX tree is one value too, so adjacent sibling elements need one parent or a Fragment. This rule is about the shape of the returned value, not about adding a visual wrapper for its own sake.

### How do JavaScript expressions enter JSX?

Put an expression inside `{}`. A variable, property lookup, conditional expression, or mapped array can produce a value for the UI. Statements such as `if` and `for` do not go directly inside JSX; calculate what you need before the return or use an expression with a clear result.

### What changes from HTML to JSX?

Most element names remain familiar, but JSX is checked by JavaScript tooling. Use `className` instead of `class`, close elements such as `<img />`, use camelCase props such as `tabIndex`, and pass values with braces instead of interpolating strings with a template syntax.

### How do we keep JSX accessible and safe?

JSX does not make an inaccessible element accessible. Prefer a native `<button>` for an action, a native `<a>` for navigation, headings in a meaningful order, and labels for form controls. React escapes ordinary text values, but `dangerouslySetInnerHTML` deliberately bypasses that protection and should not be used for untrusted practice data.

## Worked example

Each example below is a complete step in the same local case desk. Run the first version, record what you see, then replace it with the next version. The goal is to notice what changed and what stayed the same.

### Example 1: one element

Start with the smallest useful JSX value:

```tsx
export default function App() {
  return <h1>Local Case Desk</h1>;
}
```

**Visible behavior:** the playground displays one heading. `App` is a function component, and its returned JSX is the description of that heading.

### Example 2: a page-shaped tree

A page usually needs more than one element. Wrap related elements in one semantic parent:

```tsx
export default function App() {
  return (
    <main>
      <header>
        <h1>Local Case Desk</h1>
        <p>Review invented case records.</p>
      </header>
      <section aria-labelledby="queue-heading">
        <h2 id="queue-heading">Today's queue</h2>
        <p>No synthetic cases are waiting.</p>
      </section>
    </main>
  );
}
```

**Visible behavior:** the heading and queue message appear together. The `<main>`, `<header>`, and `<section>` elements are not decorative wrappers; they communicate structure to browsers and assistive technology.

### Example 3: data inside JSX

The markup can read ordinary JavaScript values. The braces do not print the braces; they evaluate the expression inside them:

```tsx
const learner = {
  name: 'Ada',
  completed: 3,
};

export default function App() {
  const message = `${learner.name} completed ${learner.completed} lessons.`;

  return (
    <main>
      <h1>Local Case Desk</h1>
      <p>{message}</p>
      <p aria-live="polite">
        {learner.completed >= 3 ? 'Review unlocked.' : 'Keep practising.'}
      </p>
    </main>
  );
}
```

**Visible behavior:** changing `completed` from `3` to `2` changes the second message. The conditional is JavaScript; the `<p>` elements are JSX structure.

### Example 4: a reusable card

A repeated piece of UI deserves a component boundary. The component receives data as props and returns JSX:

```tsx
type CaseCardProps = {
  title: string;
  status: 'Open' | 'Pending';
};

function CaseCard({ title, status }: CaseCardProps) {
  return (
    <li>
      <strong>{title}</strong>
      <span> — {status}</span>
    </li>
  );
}

export default function App() {
  const cases: CaseCardProps[] = [
    { title: 'Review access policy', status: 'Open' },
    { title: 'Test recovery flow', status: 'Pending' },
  ];

  return (
    <main>
      <h1>Local Case Desk</h1>
      <ul>
        {cases.map((item) => (
          <CaseCard key={item.title} title={item.title} status={item.status} />
        ))}
      </ul>
    </main>
  );
}
```

The React idea is still JavaScript: `CaseCard` receives an object and returns a UI tree. TypeScript records the allowed fields, but it does not validate data arriving from a real server at runtime. The `key` helps React identify each repeated item; it is not passed as a normal prop to `CaseCard`.

## Line-by-line explanation

Read the final example from the outside inward:

| Line or expression | What happens |
| --- | --- |
| `type CaseCardProps = ...` | TypeScript describes the fields the component expects; this disappears from the JavaScript runtime. |
| `function CaseCard({ title, status }...)` | React can render this function as a component because its capitalised name identifies it as user-defined UI. |
| `<li>` | The card uses a list item because the parent renders a list of records. |
| `{title}` | JSX evaluates the `title` expression and inserts its text value. Ordinary text is escaped rather than treated as HTML. |
| `{status}` | JSX evaluates a second prop and places it beside the title. |
| `const cases = [...]` | The parent owns the collection and chooses the records to render. |
| `cases.map(...)` | JavaScript transforms each record into one `CaseCard` element. |
| `key={item.title}` | React receives a stable identity for this local fixture; a production record should use a durable unique ID. |
| `<CaseCard title={item.title} status={item.status} />` | The parent passes two props down. The child reads them but does not mutate the parent’s collection. |
| `return (...)` | `App` returns one root `<main>` tree for React to render. |

## Execution trace

1. The playground loads `App` and React calls the component to obtain its returned element tree.
2. `App` creates the `cases` array before returning the tree.
3. `cases.map` visits the first record and creates a `CaseCard` element with `title` and `status` props.
4. React renders `CaseCard`; the expressions `{title}` and `{status}` become text inside the `<li>`.
5. React repeats the process for the second record and uses each `key` to track identity in the list.
6. The browser receives the resulting DOM structure: one heading, one list, and two list items.

The trace explains why changing a record changes the visible text, but it does not imply that React validates arbitrary external data. A server boundary still needs runtime validation later in the course.

## Prediction experiment

Before running each change, write the result you expect:

1. Replace `<main>` with `<div>`. What semantic information disappears while the visible appearance stays similar?
2. Change `completed >= 3` to `completed > 3`. Which message appears for `completed = 3`?
3. Add a third case with status `Open`. How many list items should appear?
4. Replace `key={item.title}` with `key={index}` and reorder the array. Why might index identity become unsafe when list items later hold state?

Run one change at a time, record the actual result, and explain any mismatch before continuing.

## Broken example and repair

This example contains three common beginner mistakes:

```tsx
function BrokenCard({ title }: { title: string }) {
  return (
    <div class="case-card">
      <img src="/case-icon.svg">
      <button onClick={console.log('open')}>Open case</button>
    </div>
  );
}
```

Repair it in this order:

1. Change `class` to `className`.
2. Close the image as `<img src="/case-icon.svg" alt="" />` and decide whether the image is decorative or needs meaningful alternative text.
3. Pass a function instead of calling `console.log` during render: `onClick={() => console.log('open')}`.

The first mistake is a JSX property rule, the second is an element-shape and accessibility rule, and the third is a runtime timing rule. They are different failures even though the editor may show them together.

## Guided practice before independent work

Copy Example 2 into the playground and run it unchanged. Add one `<p>` without changing the existing headings. Convert the queue message into a `CaseCard` component. Add one record to the array and predict the number of list items. Finally, deliberately make the `class` mistake, read the compiler message, repair it, and rerun the page.

## Project application

Build a small **case-desk summary** using only invented records. It must have a semantic main region, a heading, a list rendered from data, an empty-state branch, and a visible training-only notice. Keep the list data in the parent, keep the card presentational, and record one prediction, one repair, and one limitation in the project README.

## Independent exercises

### Level 1 — understand the syntax
1. What is JSX and the rules of markup? Answer in one sentence.
2. Explain JSX in two sentences and distinguish it from an HTML string.
3. Run Example 1 unchanged and record the visible result.
4. Add a paragraph beneath the heading without creating a second returned root.
5. Convert one `class` attribute in a small HTML example to the JSX equivalent.
6. Put a variable, a property lookup, and a conditional expression inside JSX braces.

### Level 2 — apply the rules
7. Rebuild Example 2 with a semantic `<header>`, `<main>`, and `<section>`.
8. Add a `CaseCard` component with typed `title` and `status` props.
9. Render three synthetic cases with `map` and stable invented IDs.
10. Create an empty-state branch for an empty array and explain why it is user-visible behavior.
11. Reproduce and repair the broken example’s three mistakes, recording each error or visible symptom.

### Level 3 — review and extend
12. Add a `priority` field and render it without changing the parent/child ownership rule.
13. Add a keyboard-accessible link to a local detail route and explain why a native link is preferable to a clickable `div`.
14. Explain what TypeScript checks in `CaseCardProps` and what it cannot prove about JSON from a server.
15. Write a review note naming the changed files, command, prediction, observed result, repair, accessibility decision, and remaining limitation.

## Finish line

You are ready for props and one-way data flow when you can read a JSX tree from the outside inward, identify which parts are JavaScript expressions, explain why one root is required, render a collection with identity, and repair the three broken examples without guessing.

## References

- [React Learn: Writing markup with JSX](https://react.dev/learn/writing-markup-with-jsx)
- [React Learn: JavaScript in JSX with curly braces](https://react.dev/learn/javascript-in-jsx-with-curly-braces)
- [React Learn: Rendering lists](https://react.dev/learn/rendering-lists)
- [React Learn: Keeping components pure](https://react.dev/learn/keeping-components-pure)
- [MDN: HTML elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
- [WAI: Web accessibility tutorials](https://www.w3.org/WAI/tutorials/)
