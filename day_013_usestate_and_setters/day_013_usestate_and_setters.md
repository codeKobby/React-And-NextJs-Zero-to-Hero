# Day 013: useState and setters

[← Previous lesson](../day_012_what_is_state/day_012_what_is_state.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_014_state_for_objects_and_arrays/day_014_state_for_objects_and_arrays.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does useState return?](#what-does-usestate-return)
  - [Why is a setter a request instead of an assignment?](#why-is-a-setter-a-request-instead-of-an-assignment)
  - [Why can two direct updates use the same snapshot?](#why-can-two-direct-updates-use-the-same-snapshot)
  - [What is a functional updater?](#what-is-a-functional-updater)
  - [Does useState merge objects automatically?](#does-usestate-merge-objects-automatically)
  - [How should a setter be named and owned?](#how-should-a-setter-be-named-and-owned)
- [Worked example](#worked-example)
  - [Example 1: one direct update](#example-1-one-direct-update)
- [Example 2: two direct updates](#example-2-two-direct-updates)
- [Example 3: two functional updates](#example-3-two-functional-updates)
- [Example 4: object state is replaced](#example-4-object-state-is-replaced)
- [Example 5: a small controlled form state](#example-5-a-small-controlled-form-state)
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

Use the React playground from the [examples guide](../examples/README.md):

```bash
cd examples/react-playground
pnpm install
pnpm dev
```

Start with a fresh component for each example. Do not judge a setter by its name alone; record the value visible during the current render, the update request, and the value visible in the next render.

## Why this lesson exists

In the previous lesson, one click changed the count by one. That example is correct but hides an important question: what happens when several updates are requested before React renders again? Another question appears as soon as state becomes an object: does setting `{ name: 'Ada' }` keep the other fields, or replace the whole object?

The setter is where many beginners lose the mental model. It looks like an assignment, but it is a request to React. A direct value such as `setCount(count + 1)` is calculated from the current render's snapshot. A functional updater such as `setCount((current) => current + 1)` is calculated from the latest pending value. The distinction matters when updates are queued.

We will make the difference visible rather than memorizing a rule. The first example uses one update. The second asks for two direct updates. The third uses two functional updates. Then we will see that object state is replaced, not automatically merged, and use the correct spread pattern in a small form.

## Prerequisites

Complete Day 012. You should understand that state is remembered by React and that a setter requests another render. You should know basic arrow functions and object spread. You do not need reducers or Effects.

## Outcomes

By the end, you should be able to explain the array returned by `useState`, distinguish a snapshot from a setter request, predict the result of direct and functional updates, update an object without dropping fields, and place the setter behind an event boundary owned by the correct component.

## Keywords and terms

| Keyword or term | Meaning in this lesson |
| --- | --- |
| **State snapshot** | The value a particular render sees while its component function runs. |
| **Setter** | A function that requests a next state value or receives a function that calculates one. |
| **Functional updater** | A function passed to a setter that receives the latest pending state and returns the next state. |
| **Queue** | The ordered collection of state update requests React processes before a later render. |
| **Batching** | Grouping multiple updates so React can process them together before rendering. |
| **Replacement** | The fact that `useState` stores the value you provide; an object update does not automatically merge missing fields. |
| **Spread** | Syntax that copies existing object or array contents into a new value before a changed part is added. |
| **Controlled input** | An input whose displayed value is driven by React state and whose change handler requests updates. |

## Topics

### What does useState return?

`useState(initialValue)` returns a pair: the current snapshot and a setter. Array destructuring gives those two values names. The first render receives the initial value; later renders receive the value React stored after processing updates.

### Why is a setter a request instead of an assignment?

Calling a setter does not rewrite the variable from the current render. The current function has already received its snapshot. The call schedules a future render. This is why logging the state immediately after calling the setter can show the old value without indicating that the update failed.

### Why can two direct updates use the same snapshot?

Suppose one render sees `count === 0`. Both `setCount(count + 1)` expressions calculate `1` because both read that same snapshot. Asking twice for `1` is not the same as asking for “the next value, twice.” The browser result may therefore increase by only one.

### What is a functional updater?

A functional updater receives the latest pending state. React can apply two requests in order: the first receives `0` and returns `1`; the second receives `1` and returns `2`. Use this form when the next value depends on the previous value, especially for repeated updates, timers, or callbacks whose closure may be older than the state being updated.

### Does useState merge objects automatically?

No. `useState` replaces the stored value with the value provided. If the state is `{ name: 'Ada', role: 'analyst' }` and you call `setProfile({ name: 'Grace' })`, the `role` field is gone. Create a new object with the old fields copied and the changed field replaced: `setProfile((profile) => ({ ...profile, name: 'Grace' }))`.

### How should a setter be named and owned?

Name a setter for the state it changes, such as `setCount`, `setProfile`, or `setCases`. Keep the state and setter in the smallest owner that needs to coordinate the value. A child can receive a value and callback as props; it should not reach into a parent's state or create a second competing copy without a reason.

## Worked example

The following sequence is the worked example for this lesson. Each example makes one setter behavior visible.

### Example 1: one direct update

```tsx
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button type="button" onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
```

**Visible behavior:** the first click changes `Count: 0` to `Count: 1`. There is no problem yet because one update from one snapshot is enough.

### Example 2: two direct updates

```tsx
import { useState } from 'react';

export default function DoubleCounter() {
  const [count, setCount] = useState(0);

  function addTwo() {
    setCount(count + 1);
    setCount(count + 1);
  }

  return (
    <button type="button" onClick={addTwo}>
      Count: {count} — add two
    </button>
  );
}
```

**Prediction:** a learner may expect the count to become `2`. In this render, both expressions read the same `count` snapshot. Both request `1`, so the visible count can become `1`. The issue is not that React ignored the second call; the two calls asked for the same next value.

### Example 3: two functional updates

```tsx
import { useState } from 'react';

export default function DoubleCounter() {
  const [count, setCount] = useState(0);

  function addTwo() {
    setCount((current) => current + 1);
    setCount((current) => current + 1);
  }

  return (
    <button type="button" onClick={addTwo}>
      Count: {count} — add two
    </button>
  );
}
```

Now the first updater receives the pending value `0` and returns `1`. The second updater receives the result `1` and returns `2`. The visible count becomes `2`. The callback form expresses “add one to whatever the latest value is,” which is the actual requirement.

### Example 4: object state is replaced

```tsx
import { useState } from 'react';

type Profile = { name: string; role: string };

export default function ProfileEditor() {
  const [profile, setProfile] = useState<Profile>({
    name: 'Ada',
    role: 'analyst',
  });

  function rename() {
    setProfile((current) => ({ ...current, name: 'Grace' }));
  }

  return (
    <button type="button" onClick={rename}>
      {profile.name} — {profile.role}
    </button>
  );
}
```

The spread creates a new object containing both the old `name` and `role`, then the new `name` overwrites the old one. Without the spread, the role would disappear because object state is replaced.

### Example 5: a small controlled form state

```tsx
import { useState } from 'react';

type Draft = { title: string; owner: string };

export default function CaseDraft() {
  const [draft, setDraft] = useState<Draft>({ title: '', owner: '' });

  return (
    <form>
      <label>
        Title
        <input
          value={draft.title}
          onChange={(event) =>
            setDraft((current) => ({ ...current, title: event.target.value }))
          }
        />
      </label>
      <label>
        Owner
        <input
          value={draft.owner}
          onChange={(event) =>
            setDraft((current) => ({ ...current, owner: event.target.value }))
          }
        />
      </label>
      <p aria-live="polite">{draft.title || 'Untitled case'}</p>
    </form>
  );
}
```

Each input reads from state and sends the next string through the setter. The object update copies the field that the other input did not change. This is the simplest useful form of a controlled input; validation and submission belong to later lessons.

## Line-by-line explanation

| Code line | What it teaches |
| --- | --- |
| `const [count, setCount] = useState(0);` | The current render receives a snapshot and a setter request function. |
| `function addTwo() {` | The handler runs later, when the user clicks; it closes over the snapshot from the render that created it. |
| `setCount(count + 1);` | Calculates `1` twice when the current snapshot is `0`; both direct requests have the same result. |
| `setCount((current) => current + 1);` | Gives React a calculation that can receive the latest pending value. |
| `setProfile((current) => ({ ...current, name: 'Grace' }));` | Returns a new object with every old field copied and `name` replaced. |
| `value={draft.title}` | Makes the input's displayed value come from React state. |
| `onChange={(event) => ...}` | Reads the browser's new string and requests a new draft object. |
| `aria-live="polite"` | Gives the visible summary a useful announcement boundary without making keystrokes overly disruptive. |

## Execution trace

For `DoubleCounter` with direct updates:

1. The first render has `count = 0`.
2. The user clicks `addTwo`; the handler reads the snapshot `0`.
3. The first direct expression calculates `0 + 1`, so it requests `1`.
4. The second direct expression reads the same snapshot `0`, so it also requests `1`.
5. React processes the requests and the next render sees `count = 1`.

For functional updates:

1. The first updater receives `0` and returns `1`.
2. The second updater receives the latest pending value `1` and returns `2`.
3. The next render sees `count = 2`.

For the form, typing `A` into Title sends a new object `{ title: 'A', owner: '' }`. Typing `B` into Owner copies that object and returns `{ title: 'A', owner: 'B' }`; the title is not lost.

## Prediction experiment

Before running, write your predictions:

1. What does one click on Example 2 produce?
2. What does one click on Example 3 produce?
3. What does the immediate log show here: `setCount(count + 1); console.log(count);`?
4. What fields remain after `setProfile({ name: 'Grace' })`?
5. What fields remain after `setProfile((current) => ({ ...current, name: 'Grace' }))`?
6. Type a title, then an owner. Does the other field remain visible?

Run each experiment in a fresh component and restore the intended version afterward.

## Broken example and repair

**Broken version:**

```tsx
function addTwo() {
  setCount(count + 1);
  setCount(count + 1);
}
```

If the requirement is “increase by two from whatever the latest count is,” repair it with:

```tsx
function addTwo() {
  setCount((current) => current + 1);
  setCount((current) => current + 1);
}
```

A second broken version is `setProfile({ name: 'Grace' })`. It removes `role`. Repair it with the functional spread update. Do not claim that object spread performs validation; it only creates a new object with copied fields.

## Guided practice before independent work

First, run one direct update. Second, change it to two direct updates and record the result. Third, change only the updater form and predict the new result. Fourth, create a two-field object and update one field while preserving the other. Fifth, connect two controlled inputs to the object state. Do not add a reducer until the state transitions have become difficult to describe with a small number of setters.

## Project application

Build a local **case draft form** with `title`, `owner`, and `notes`. Use one state object, controlled inputs, a clear button, and a live summary. The clear button should use a deliberate initial value. Write one test or manual evidence note proving that changing `owner` does not erase `title` and that clearing returns the form to its initial state.

## Independent exercises

### Level 1 — Mechanical confidence
1. What is useState and setters? Answer in one sentence.
2. Run the one-update counter and record the first two visible results.
3. Predict and run two direct updates in one handler.
4. Replace the direct updates with functional updaters and explain the difference.
5. Log the current snapshot immediately after a setter and explain what you observe.

### Level 2 — Applied practice
6. Create a `Profile` object with two fields and update only one using spread.
7. Deliberately drop a field with a replacement object and repair it.
8. Build two controlled inputs backed by one object state.
9. Add reset behavior and a visible empty or initial-state summary.

### Level 3 — Synthesis
10. Write a sequence of three updates and predict the result for direct and functional forms.
11. Add a test or written acceptance check for preserving the untouched object field.
12. Explain why a setter is not the same as a JavaScript property setter; connect this to Day 061 later in the course.
13. Write a review note naming the snapshot, pending updates, state owner, evidence, limitation, and why a reducer is not yet necessary.

## Finish line

You are ready to move on when you can predict the result of two direct updates, explain why functional updaters differ, preserve object fields deliberately, and describe the state owner without saying that React “merges everything for you.”

## References

- [React Learn: Queueing a Series of State Updates](https://react.dev/learn/queueing-a-series-of-state-updates)
- [React Learn: Updating Objects in State](https://react.dev/learn/updating-objects-in-state)
- [React Learn: Updating Arrays in State](https://react.dev/learn/updating-arrays-in-state)
