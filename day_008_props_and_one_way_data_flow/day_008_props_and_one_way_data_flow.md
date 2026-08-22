# Day 008: Props and one-way data flow

[← Previous lesson](../day_007_jsx_and_the_rules_of_markup/day_007_jsx_and_the_rules_of_markup.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_009_rendering_lists_and_choosing_keys/day_009_rendering_lists_and_choosing_keys.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What are props?](#what-are-props)
  - [Why does data flow from parent to child?](#why-does-data-flow-from-parent-to-child)
  - [Why should a child not mutate props?](#why-should-a-child-not-mutate-props)
  - [How can a child request a parent change?](#how-can-a-child-request-a-parent-change)
  - [What belongs in the owner?](#what-belongs-in-the-owner)
- [Worked example](#worked-example)
  - [Example 1: hard-coded card](#example-1-hard-coded-card)
  - [Example 2: a card receives props](#example-2-a-card-receives-props)
  - [Example 3: a callback carries intent upward](#example-3-a-callback-carries-intent-upward)
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

Read the [README](../README.md), confirm [setup](../SETUP.md), and use the React playground described in the [examples guide](../examples/README.md):

```bash
cd examples/react-playground
pnpm dev
```

Open the page before editing. This lesson uses invented case records. The visible goal is simple: the parent owns the records, and a child displays one record without knowing where the record came from.

## Why this lesson exists

A component becomes useful when it can display different data without copying its markup. Imagine writing the same case card three times because one card is open, one is pending, and one is closed. The markup is the same; only the data changes. Props let the parent provide that data.

Props also solve a responsibility problem. A child should not reach into a parent's variables and quietly change them. The parent owns the decision. If a child wants something to happen, it can call a callback supplied by the parent. The callback carries intent upward; the parent decides whether that intent is valid and how state should change.

## Prerequisites

Complete Day 006 on components and Day 007 on JSX. You need function components, JSX attributes, destructuring, and browser event handlers. State is useful for Example 3, but the main idea is data flow.

## Outcomes

You should be able to define a prop, pass a string and object from parent to child, explain why props are read-only, trace data down and intent up, and choose whether a value belongs in a parent or child. You should also be able to repair a prop-mutation mistake without creating a second uncontrolled copy.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Prop** | A read-only input supplied by a parent to a child component. |
| **Parent** | The component that renders another component and supplies its props. |
| **Child** | The component that receives props from the parent. |
| **One-way data flow** | The default direction in which values move down the rendered component tree. |
| **Callback prop** | A function supplied as a prop so a child can report intent to its parent. |
| **Ownership** | The place responsible for creating, changing, and validating a value. |
| **Destructuring** | JavaScript syntax that gives properties local names, such as `{ title }`. |

## Topics

### What are props?

Props are the inputs a parent gives a child. They may be strings, numbers, objects, arrays, functions, or JSX children. A prop is not a special second state system; it is an argument to a component. When the parent renders `<CaseCard title="Review" />`, `CaseCard` receives an object containing `title`.

### Why does data flow from parent to child?

The parent knows the page context and can choose which data to provide. The child can remain focused on how one case is displayed. This one-way direction makes the source of a value easier to find. It also makes a change visible: if the parent sends a new prop, the child renders from the new input.

### Why should a child not mutate props?

Props describe the parent's input for this render. Assigning to `props.title` would not change the parent's source, and it would make the child appear to own a value it did not create. If a value must change, put the state in the owner and pass a callback or a state setter with a deliberately narrow name.

### How can a child request a parent change?

A callback prop is a message-shaped function. The child can call `onResolve(caseId)` when the user presses a button. The parent owns the callback and can update state, validate permission, or ignore the request. The child does not need to know whether the parent uses state, a Server Action, or a test spy.

### What belongs in the owner?

The owner is the smallest component that needs to coordinate the value. A card should own the markup for one card. A queue parent should own the array if several children need to see the same array. Move state upward only when a real sharing problem appears; moving everything to the top makes every child depend on unrelated data.

## Worked example

### Example 1: hard-coded card

Start with a component that can show one case:

```tsx
function CaseCard() {
  return (
    <article>
      <h2>Review access policy</h2>
      <p>Status: Open</p>
    </article>
  );
}

export default function App() {
  return <CaseCard />;
}
```

It works, but it can display only one hard-coded case. The component owns data that should belong to the page.

### Example 2: a card receives props

Move the data to the parent and pass it down:

```tsx
type CaseCardProps = {
  title: string;
  status: 'Open' | 'Pending' | 'Closed';
};

function CaseCard({ title, status }: CaseCardProps) {
  return (
    <article>
      <h2>{title}</h2>
      <p>Status: {status}</p>
    </article>
  );
}

export default function App() {
  const firstCase: CaseCardProps = {
    title: 'Review access policy',
    status: 'Open',
  };
  const secondCase: CaseCardProps = {
    title: 'Test recovery flow',
    status: 'Pending',
  };

  return (
    <main>
      <CaseCard {...firstCase} />
      <CaseCard {...secondCase} />
    </main>
  );
}
```

**Visible behavior:** the two cards use the same component but show different data. `App` owns the fixture; `CaseCard` owns the display.

### Example 3: a callback carries intent upward

Now let the user mark a case as reviewed. The parent owns the array and provides the callback:

```tsx
import { useState } from 'react';

type Case = { id: string; title: string; reviewed: boolean };

type CaseCardProps = {
  item: Case;
  onReview: (id: string) => void;
};

function CaseCard({ item, onReview }: CaseCardProps) {
  return (
    <article>
      <h2>{item.title}</h2>
      <p>{item.reviewed ? 'Reviewed' : 'Needs review'}</p>
      {!item.reviewed && (
        <button type="button" onClick={() => onReview(item.id)}>
          Mark reviewed
        </button>
      )}
    </article>
  );
}

export default function Queue() {
  const [cases, setCases] = useState<Case[]>([
    { id: 'case-001', title: 'Review access policy', reviewed: false },
  ]);

  function reviewCase(id: string) {
    setCases((current) =>
      current.map((item) =>
        item.id === id ? { ...item, reviewed: true } : item,
      ),
    );
  }

  return (
    <main>
      {cases.map((item) => (
        <CaseCard key={item.id} item={item} onReview={reviewCase} />
      ))}
    </main>
  );
}
```

The child does not call `setCases` directly. It calls `onReview` with an ID. The parent checks the ID and creates a new array. This design leaves room for a later server-authoritative mutation without changing the card's display responsibility.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `type CaseCardProps = ...` | Describes the input contract for the card. |
| `function CaseCard({ item, onReview })` | Receives the parent’s record and callback as read-only props. |
| `{item.reviewed ? ... : ...}` | Chooses the visible status from the current prop. |
| `onClick={() => onReview(item.id)}` | Sends intent upward only after the user clicks; it does not mutate the record. |
| `const [cases, setCases] = useState(...)` | The parent owns the collection because it coordinates every card. |
| `setCases((current) => current.map(...))` | Requests a new array and changes only the record with the matching ID. |
| `<CaseCard key={item.id} ... />` | The parent supplies props and a stable list identity. `key` is used by React and is not an ordinary `item` prop. |

## Execution trace

1. `Queue` renders one case with `reviewed: false`.
2. It passes the case and `reviewCase` callback to `CaseCard`.
3. `CaseCard` shows “Needs review” and a button.
4. A click calls `onReview('case-001')`.
5. The callback runs in the parent and maps the current array.
6. The matching record becomes a new object with `reviewed: true`.
7. The next render sends the updated prop, so the child shows “Reviewed” and no longer renders the button.

## Prediction experiment

Predict what happens if `Queue` passes a different `id`, if the array contains two cases, and if a reviewed case is rendered first. Then run each case. Predict whether the child can change the parent by assigning `item.reviewed = true` without a callback. Explain the result before trying the broken version.

## Broken example and repair

**Broken version:** write this inside `CaseCard`:

```tsx
item.reviewed = true;
```

The child is trying to mutate a prop. This may violate TypeScript's readonly expectations, mutate an object unexpectedly, or fail to cause the right parent render. Repair it by calling `onReview(item.id)` and letting the parent create a new array. The repair keeps ownership in the parent.

Another common mistake is `onClick={onReview(item.id)}`. That calls the callback while rendering. Use `onClick={() => onReview(item.id)}` so the callback runs after the click.

## Guided practice before independent work

First, pass a hard-coded `title` prop to `CaseCard`. Second, pass a typed object. Third, render two cards with different data. Fourth, add a callback that only logs the ID. Fifth, connect the callback to state in the parent. Keep the child unaware of how the parent stores or validates the records.

## Project application

Build a local **review queue** with a parent `Queue`, child `CaseCard`, a typed synthetic array, and a “Mark reviewed” callback. The parent must own the array. The card must receive one case and a callback. Include an empty or completed state and one accessible button name.

## Independent exercises

### Level 1 — Confidence
1. What is Props and one-way data flow? Answer in one sentence.
2. Run the hard-coded card and identify what data is trapped inside the child.
3. Move the title and status into the parent and pass them as props.
4. Render two cards from the same component with different values.
5. Draw an arrow showing the direction of each prop.

### Level 2 — Application
6. Add an `id` and `reviewed` field to a synthetic case.
7. Add an `onReview` callback and log the ID without changing state.
8. Connect the callback to a parent state update that creates a new array.
9. Add a completed or empty state for the queue.

### Level 3 — Synthesis
10. Reproduce prop mutation and immediate callback invocation, then repair both.
11. Add a test or written acceptance check proving the parent changes and the child remains reusable.
12. Explain why a callback prop is intent rather than permission or server authorization.
13. Write a review note with the owner, data direction, callback contract, visible evidence, and one limitation.

## Finish line

You are ready when you can pass new data into the same child, explain why the child cannot silently change a prop, and trace a callback from a user click to the parent-owned update.

## References

- [React Learn: Passing Props to a Component](https://react.dev/learn/passing-props-to-a-component)
- [React Learn: Sharing State Between Components](https://react.dev/learn/sharing-state-between-components)
- [React Learn: Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure)
