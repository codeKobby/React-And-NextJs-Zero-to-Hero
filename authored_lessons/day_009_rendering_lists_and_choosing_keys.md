# Day 009: Rendering lists and choosing keys

[← Previous lesson](../day_008_props_and_one_way_data_flow/day_008_props_and_one_way_data_flow.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_010_conditional_rendering_and_empty_states/day_010_conditional_rendering_and_empty_states.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [How does one record become one list item?](#how-does-one-record-become-one-list-item)
  - [What does map return?](#what-does-map-return)
  - [What is a key?](#what-is-a-key)
  - [Why is array index a risky key?](#why-is-array-index-a-risky-key)
  - [What makes an ID stable?](#what-makes-an-id-stable)
- [Worked example](#worked-example)
  - [Example 1: render one record](#example-1-render-one-record)
  - [Example 2: map a collection](#example-2-map-a-collection)
  - [Example 3: see identity during reorder](#example-3-see-identity-during-reorder)
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

Read the [README](../README.md), confirm [setup](../SETUP.md), and run the React playground from the [examples guide](../examples/README.md):

```bash
cd examples/react-playground
pnpm dev
```

This lesson uses a local array of synthetic case records. Do not paste a public API response into the example. First understand how one record becomes one list item; then understand why React needs identity when the collection changes.

## Why this lesson exists

A real application rarely displays one record. It displays a queue, messages, tasks, alerts, or results. Writing one JSX block for every record is repetitive and makes changes expensive. JavaScript's `map` lets us transform each record into one returned element.

The second problem is less visible. React must decide which rendered item corresponds to which record when the array changes. A key is not a decorative warning suppressor. It is the identity React uses to match an item across renders. If a list is reordered while each row has its own input or state, an index key can make the wrong row appear to keep the old state.

## Prerequisites

Complete components and props. You need arrays, `map`, object properties, JSX expressions, and a basic understanding of why a parent gives a child a stable input.

## Outcomes

You should be able to map a typed array into JSX, choose a stable key from record identity, explain why an array index represents position rather than identity, and reproduce a reorder case that makes the distinction visible.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Collection** | A group of records that the UI must display. |
| **Map** | A JavaScript method that returns one new value for each item in an array. |
| **Key** | A stable identity React uses to match a list item between renders. |
| **Identity** | The fact that tells us this record is the same record after data or position changes. |
| **Index** | The current numeric position of an item in an array. |
| **Reorder** | Changing item positions without necessarily changing which records exist. |
| **Empty state** | Deliberate UI for a collection with zero records. |

## Topics

### How does one record become one list item?

Write one component for one record first. If `CaseRow` displays a title and status, its input is one case object. Once that responsibility is clear, the parent can repeat the component for an array.

### What does map return?

`map` returns a new array. In JSX, each callback return becomes one child in the rendered collection. Forgetting `return`, using braces without a return, or returning a plain object instead of JSX changes the result.

### What is a key?

A key identifies a sibling item for React's reconciliation. It should come from the record, such as `case-001`, not from a value that changes every render. The key is used by React; `CaseRow` does not receive it as `props.key`.

### Why is array index a risky key?

An index identifies a position. If a new item is inserted at the start, every later record gets a different index even though it is the same record. That can cause local input state, focus, or animation state to appear attached to the wrong row.

### What makes an ID stable?

An ID remains associated with the same record across sorting, filtering, and rerendering. A generated random ID during render is not stable. A server database ID or a deliberately created local fixture ID is stable for the lifetime of the record.

## Worked example

### Example 1: render one record

```tsx
type Case = { id: string; title: string; status: string };

function CaseRow({ item }: { item: Case }) {
  return <li>{item.title} — {item.status}</li>;
}

export default function App() {
  const item: Case = {
    id: 'case-001',
    title: 'Review access policy',
    status: 'Open',
  };
  return <CaseRow item={item} />;
}
```

The visible result is one list-row sentence. The `id` is not displayed, but it will matter when the parent renders a collection.

### Example 2: map a collection

```tsx
const cases: Case[] = [
  { id: 'case-001', title: 'Review access policy', status: 'Open' },
  { id: 'case-002', title: 'Test recovery flow', status: 'Pending' },
];

export default function App() {
  return (
    <main>
      <h1>Case queue</h1>
      <ul>
        {cases.map((item) => (
          <CaseRow key={item.id} item={item} />
        ))}
      </ul>
    </main>
  );
}
```

`map` calls the callback once per record, and the returned array contains two `CaseRow` elements. `key={item.id}` gives React the stable identity. The key does not become an ordinary prop.

### Example 3: see identity during reorder

A visible input makes identity easier to inspect:

```tsx
import { useState } from 'react';

type Case = { id: string; title: string };

export default function ReorderDemo() {
  const [items, setItems] = useState<Case[]>([
    { id: 'case-a', title: 'Access policy' },
    { id: 'case-b', title: 'Recovery flow' },
  ]);

  function moveSecondFirst() {
    setItems((current) => [current[1], current[0]]);
  }

  return (
    <main>
      <button type="button" onClick={moveSecondFirst}>Move second first</button>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            <label>
              {item.title}
              <input aria-label={`Note for ${item.title}`} />
            </label>
          </li>
        ))}
      </ul>
    </main>
  );
}
```

With stable IDs, the input associated with `Access policy` remains associated with that record after the reorder. Replace `key={item.id}` with `key={index}` after adding `index` to the callback and compare. The problem is not always visible in a static list; it appears when item-local state or focus matters.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `const cases: Case[] = [...]` | Defines a typed local collection with stable synthetic identity. |
| `{cases.map((item) => (` | Starts one transformation for every record; the callback's return is one child. |
| `<CaseRow key={item.id} item={item} />` | Supplies the record as a prop and identity as a React key. |
| `setItems((current) => [current[1], current[0]])` | Requests a new array with positions reversed without mutating the old array. |
| `key={item.id}` | Tells React which row is the same record after the array changes. |
| `aria-label={...}` | Gives each input a name that remains tied to the record's title. |

## Execution trace

1. The parent creates two records with IDs `case-a` and `case-b`.
2. `map` returns two list-item elements; React records their keys as `case-a` and `case-b`.
3. The user clicks Move second first.
4. The updater returns a new array in the order `case-b`, `case-a`.
5. React matches the new first item to key `case-b`, not merely to its former position.
6. The input state and focus associated with each record can follow the record when the key is stable.

## Prediction experiment

Predict the result of an empty array, a duplicate ID, a newly generated random key during render, and an index key after reordering. For each case, say whether the issue affects a warning, identity, state preservation, or user-visible ordering. Run one case at a time.

## Broken example and repair

**Broken version:**

```tsx
{cases.map((item, index) => (
  <CaseRow key={index} item={item} />
))}
```

This is not automatically wrong for every static list, but it is risky when records can be inserted, deleted, or reordered. Repair it with `key={item.id}` when the record has a stable identity. Do not generate `Math.random()` during render; that gives every item a new identity every time.

## Guided practice before independent work

Render one row, then two rows. Add the key after observing the warning. Give each row an input. Reorder the array using a functional updater and compare stable IDs with indexes. Finally, remove all records and write the empty state before returning to the list branch.

## Project application

Build a local **case queue** with stable IDs, a title, status, and a note input. Include a sort or reorder button, an empty state, and an explanation of why the key remains the record ID. Use invented data only.

## Independent exercises

### Level 1 — Confidence

1. Render one `CaseRow` from one object.
2. Map two records to two rows.
3. Add a stable key and explain where React uses it.
4. Render an empty-state message for an empty array.

### Level 2 — Application

5. Add a note input to each row.
6. Add a reorder button with a new array, not mutation.
7. Compare stable IDs and array indexes after reordering.
8. Add an accessible name tied to each record.

### Level 3 — Synthesis

9. Reproduce the duplicate-key and random-key mistakes and explain the evidence.
10. Add an assertion for row identity after reordering.
11. Explain why the key is not available as `props.key`.
12. Write a review note with collection shape, identity rule, empty behavior, visible evidence, and one limitation.

## Finish line

You are ready when you can explain both what `map` returns and why a stable key is an identity decision, not a way to silence a warning.

## References

- [React Learn: Rendering Lists](https://react.dev/learn/rendering-lists)
- [React Learn: Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state)
