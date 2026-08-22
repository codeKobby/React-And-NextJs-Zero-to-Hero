# Day 010: Conditional rendering and empty states

[← Previous lesson](../day_009_rendering_lists_and_choosing_keys/day_009_rendering_lists_and_choosing_keys.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_011_events_and_event_handlers/day_011_events_and_event_handlers.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [How does React choose what to render?](#how-does-react-choose-what-to-render)
  - [When is a ternary useful?](#when-is-a-ternary-useful)
  - [When is logical AND useful?](#when-is-logical-and-useful)
  - [What is an empty state?](#what-is-an-empty-state)
  - [How do loading and error states differ from empty?](#how-do-loading-and-error-states-differ-from-empty)
- [Worked example](#worked-example)
  - [Example 1: choose between two messages](#example-1-choose-between-two-messages)
  - [Example 2: render a list or an empty state](#example-2-render-a-list-or-an-empty-state)
  - [Example 3: model loading, success, empty, and error](#example-3-model-loading-success-empty-and-error)
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

Read the [README](../README.md), confirm [setup](../SETUP.md), and run the React playground described in [examples](../examples/README.md). Use local arrays and a local status value. An empty state is a real user experience, not a missing implementation.

## Why this lesson exists

A page is not always in its ideal state. A queue can contain records, contain no records, be waiting for data, or have failed to load. If a component only describes the success case, the user sees a blank page or a mysterious spinner when the real world produces another result.

Conditional rendering is how a component chooses one visible branch from its current inputs. The syntax is ordinary JavaScript—`if`, a ternary, or logical `&&`—but the decision has a user-facing responsibility. A good condition does not only ask “is data truthy?” It distinguishes an empty queue from loading and a server failure.

## Prerequisites

Complete components, props, and lists. You need boolean expressions, arrays, ternaries, and JSX fragments. You do not need data fetching yet; the lesson uses a hand-written status object.

## Outcomes

You should be able to choose an appropriate conditional form, create a useful empty state, distinguish loading from empty and error, and repair the common `items.length && ...` stray-zero bug.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Conditional rendering** | Choosing visible JSX from a condition. |
| **Ternary** | `condition ? whenTrue : whenFalse`, useful when both branches produce a value. |
| **Logical AND** | `condition && element`, useful when an element should appear only when a condition is true. |
| **Empty state** | Helpful UI shown when valid data contains zero records. |
| **Loading state** | UI shown while work is still in progress. |
| **Error state** | UI that explains a failed operation and offers an appropriate next step. |
| **Branch** | One possible visible path selected by a condition. |

## Topics

### How does React choose what to render?

React evaluates the JavaScript in the component and uses the returned JSX tree. If a condition is true, one branch appears; if it is false, another branch may appear. The condition should represent a meaningful UI state, not an accidental implementation detail.

### When is a ternary useful?

A ternary is useful when both outcomes are small and visible: a label can say `Open` or `Closed`, or a list can be shown instead of an empty message. If branches become large, use an `if` statement or a named component so the reader can understand each case.

### When is logical AND useful?

`condition && <Message />` is useful when the false case should render nothing. It is not a general replacement for a ternary. Be careful with numeric values: `0 && <p>...</p>` evaluates to `0`, and React may render the stray zero.

### What is an empty state?

An empty state explains what zero records means and what the user can do next. “No cases found” may be accurate but incomplete. “No cases are waiting. Create a synthetic case to begin.” gives context without pretending that empty means error.

### How do loading and error states differ from empty?

Loading means the result is not known yet. Empty means the request completed successfully and the result contains zero items. Error means the operation did not produce the expected result. A user needs different information and action for each state.

## Worked example

### Example 1: choose between two messages

```tsx
function Status({ open }: { open: boolean }) {
  return <p>{open ? 'Case is open' : 'Case is closed'}</p>;
}

export default function App() {
  return <Status open={true} />;
}
```

The prop is `true`, so the first message appears. Change it to `false` and predict the second message before running it.

### Example 2: render a list or an empty state

```tsx
type Case = { id: string; title: string };

function CaseList({ cases }: { cases: Case[] }) {
  if (cases.length === 0) {
    return <p>No synthetic cases are waiting. Create one to begin.</p>;
  }

  return (
    <ul>
      {cases.map((item) => <li key={item.id}>{item.title}</li>)}
    </ul>
  );
}

export default function App() {
  const cases: Case[] = [];
  return <CaseList cases={cases} />;
}
```

**Visible behavior:** the empty branch returns before the list branch. Change `cases` to contain one record and the list appears. The empty message is not an error; it explains a successful zero-result condition.

### Example 3: model loading, success, empty, and error

```tsx
type QueueState =
  | { status: 'loading' }
  | { status: 'success'; cases: string[] }
  | { status: 'error'; message: string };

function QueueView({ state }: { state: QueueState }) {
  if (state.status === 'loading') return <p>Loading cases…</p>;
  if (state.status === 'error') return <p role="alert">{state.message}</p>;
  if (state.cases.length === 0) {
    return <p>No cases are waiting.</p>;
  }
  return <ul>{state.cases.map((title) => <li key={title}>{title}</li>)}</ul>;
}

export default function App() {
  return <QueueView state={{ status: 'success', cases: [] }} />;
}
```

The discriminated union makes the branches explicit. The success state can still be empty. That is why empty cannot be treated as the same thing as loading or error.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `if (cases.length === 0)` | Tests the domain condition “the successful collection has zero records.” |
| `return <p>...` | Ends this branch with a meaningful user-facing result. |
| `cases.map(...)` | Runs only after the component knows the array is non-empty. |
| `state.status === 'loading'` | Narrows the union to its loading branch. |
| `state.status === 'error'` | Narrows the union and makes `message` available. |
| `state.cases.length === 0` | Distinguishes successful empty data from loading and error. |
| `role="alert"` | Marks an important error message for assistive technology; it does not make the operation retryable by itself. |

## Execution trace

For the final example, the parent passes `{ status: 'success', cases: [] }`. The loading condition is false; the error condition is false; the success array has length zero; the empty message is returned. If the parent passes `{ status: 'loading' }`, the first branch returns and the component never reads `state.cases`.

## Prediction experiment

Predict each output before running it: success with one case, success with zero cases, loading, and error. Then change a logical-AND expression from `cases.length > 0 && ...` to `cases.length && ...` with an empty array. Record whether a visible zero appears.

## Broken example and repair

**Broken version:**

```tsx
return <div>{cases.length && <CaseList cases={cases} />}</div>;
```

When `cases.length` is `0`, the expression returns `0`, so React may render a stray zero. Repair it with `cases.length > 0 && ...` or an explicit `if`/ternary. Then add a real empty-state message so the user knows what zero means.

A second mistake is showing `Loading…` forever when the request completed with an empty array. Keep status and data meaning distinct.

## Guided practice before independent work

Render the open/closed status. Replace it with a list. Add the empty branch. Add a union with loading and error. Then run the `&&` mistake with an empty array and repair it. Do not add network fetching until the local states are correct.

## Project application

Build a local **queue status panel** with four fixtures: loading, one case, zero cases, and an error message. Provide visible text for every branch and an accessible error signal. Use a button or local selector to switch fixtures so the learner can inspect each branch.

## Independent exercises

### Level 1 — Confidence
1. What is Conditional rendering and empty states? Answer in one sentence.
2. Switch a boolean status between open and closed.
3. Render one list and then an empty list.
4. Write a useful empty-state sentence.
5. Explain the difference between a false branch and an empty-data branch.

### Level 2 — Application
6. Add loading and error states with a discriminated union.
7. Add a retry or return-to-start action that is honest about what it does.
8. Reproduce the stray-zero bug with `&&`.
9. Repair it and add a test or manual check for zero records.

### Level 3 — Synthesis
10. Explain when an `if`, ternary, or `&&` is clearest.
11. Add an accessible error message and verify it is not shown for empty success.
12. Add a route or component fixture with all four states.
13. Write a review note with state meanings, branch ownership, observed output, and one limitation.

## Finish line

You are ready when you can distinguish empty, loading, error, and success, select a readable conditional form, and repair a blank or stray-zero UI without hiding the underlying state.

## References

- [React Learn: Conditional Rendering](https://react.dev/learn/conditional-rendering)
- [React Learn: Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure)
