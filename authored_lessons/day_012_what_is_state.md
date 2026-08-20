# Day 012: What is state?

[← Previous lesson](../day_011_events_and_event_handlers/day_011_events_and_event_handlers.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_013_usestate_and_setters/day_013_usestate_and_setters.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does state mean in ordinary life?](#what-does-state-mean-in-ordinary-life)
  - [What is state in React?](#what-is-state-in-react)
  - [Why is state different from a local variable?](#why-is-state-different-from-a-local-variable)
  - [What does a state setter request?](#what-does-a-state-setter-request)
  - [Where should state live?](#where-should-state-live)
- [Worked example](#worked-example)
  - [Example 1: a local variable that cannot update the screen](#example-1-a-local-variable-that-cannot-update-the-screen)
- [Example 2: the smallest useful useState example](#example-2-the-smallest-useful-usestate-example)
- [Example 3: name the event handler](#example-3-name-the-event-handler)
- [Example 4: state for a small case queue](#example-4-state-for-a-small-case-queue)
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

Open the local Vite URL. Run the existing page first, then make a copy of the component for each experiment. The lesson is about observing the difference between a value changing in JavaScript and React rendering a new screen.

## Why this lesson exists

Think about the state of a traffic light. At one moment it is red; after a change it is green. The important fact is not only the word “red” or “green.” The important fact is that the current condition can change over time and that people looking at the light need to see the current condition.

A user interface has the same kind of changing conditions: a menu is open or closed, a form is empty or filled, a request is loading or complete, and a case is open or resolved. A local JavaScript variable can hold a value, but changing that variable does not tell React that the screen should be calculated again. React state is the mechanism for remembering a value between renders and requesting a new render when the value changes.

We will earn that definition through a failure. First we will change a local variable and see that the screen stays the same. Then we will give React ownership of the value with `useState`. The second example is not a new spell; it is the repair for a visible problem.

## Prerequisites

You should know what a function component is, how a click event calls a handler, and how JSX places a JavaScript value inside braces. You do not need to know Effects, reducers, Context, Server Components, or Next.js yet.

## Outcomes

By the end, you should be able to explain state using an ordinary example, identify why a local variable is not enough for interactive UI, use `useState` for a small value, trace a click from event to new visible output, and choose a sensible owner for state in a simple component. You should also be able to state why state is not a general-purpose replacement for every variable.

## Keywords and terms

| Keyword or term | Meaning in this lesson |
| --- | --- |
| **State** | A value React remembers for a component between renders and uses to calculate the next UI. |
| **Render** | React evaluating a component and using its returned result to decide what the UI should show. |
| **Snapshot** | The state value visible to one particular render of a component. |
| **Setter** | The function returned by `useState` that requests the next state value. |
| **Re-render** | React evaluating a component again after an update so the visible UI can reflect new state. |
| **Event** | Information about something that happened in the browser, such as a button click. |
| **Owner** | The component whose state represents a value and whose setter is allowed to request changes. |

## Topics

### What does state mean in ordinary life?

State means the condition something is in at a particular time. A door can be open or closed. A queue can contain two cases or no cases. The condition is useful because it can change and because someone needs an accurate current view.

### What is state in React?

React state is data associated with a component's repeated renders. The first render receives the initial state. When an event calls the setter, React schedules another render with the next state value. The component function runs again; it does not continue from the old local variables as though it were one long procedure.

### Why is state different from a local variable?

A local variable belongs to one execution of the function. When React renders the component again, the function starts again and creates a new local variable. A state value is stored by React and restored for that component's next render. This is why a local variable can be useful for a calculation inside one render but is not enough for a value that the user must see change over time.

### What does a state setter request?

A setter does not mutate the current snapshot in place. It requests that React remember a next value and render the component again. The current render still sees its old snapshot after the setter call. This detail explains why a setter is not the same as assigning a normal variable, and it prepares us for functional updaters in the next lesson.

### Where should state live?

State should live in the nearest component that owns the decision and can provide the value to all components that need it. If one button and one label use a count, their shared owner can hold the count. If two sibling components need the same value, a parent may own it and pass the value down. Do not move state upward before a real sharing problem exists.

## Worked example

The following sequence is the worked example for this lesson. Each example is a repair or extension of the previous mental model.

### Example 1: a local variable that cannot update the screen

This is a useful failure. It is ordinary JavaScript and it looks plausible:

```tsx
function BrokenCounter() {
  let count = 0;

  function handleClick() {
    count += 1;
    console.log('JavaScript count:', count);
  }

  return (
    <section>
      <p>Screen count: {count}</p>
      <button type="button" onClick={handleClick}>Add one</button>
    </section>
  );
}
```

**Expected behavior:** each click prints a larger number in the console, but the visible paragraph can remain `Screen count: 0`. The local variable changed inside the event handler; nothing requested React to render the component again.

### Example 2: the smallest useful useState example

The repair gives the value to React:

```tsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <section>
      <p>Screen count: {count}</p>
      <button type="button" onClick={() => setCount(count + 1)}>
        Add one
      </button>
    </section>
  );
}
```

The array returned by `useState(0)` contains two related things: the current snapshot called `count` and the setter called `setCount`. The initial `0` is used for the first render. After a click, the setter requests the next value, and the next render reads that value in `{count}`.

**Expected behavior:** the first screen says `Screen count: 0`; after one click it says `Screen count: 1`; after a second click it says `Screen count: 2`.

### Example 3: name the event handler

The inline arrow function is short, but a named handler helps us explain what owns the action:

```tsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  function addOne() {
    setCount(count + 1);
  }

  return (
    <section>
      <p aria-live="polite">Screen count: {count}</p>
      <button type="button" onClick={addOne}>Add one</button>
    </section>
  );
}
```

`addOne` is created during a render and closes over that render's `count` snapshot. For one click, `count + 1` is the correct next value. The next lesson will explain why a functional updater is safer when several updates depend on the previous value.

### Example 4: state for a small case queue

State is more useful when it controls a small user-visible mode, not only a number:

```tsx
import { useState } from 'react';

type Case = { id: string; title: string };

function CaseQueue() {
  const [cases, setCases] = useState<Case[]>([
    { id: 'case-001', title: 'Review access policy' },
  ]);

  function clearQueue() {
    setCases([]);
  }

  return (
    <section>
      <h2>Case queue</h2>
      {cases.length === 0 ? (
        <p>No synthetic cases are waiting.</p>
      ) : (
        <ul>
          {cases.map((item) => <li key={item.id}>{item.title}</li>)}
        </ul>
      )}
      <button type="button" onClick={clearQueue}>Clear queue</button>
    </section>
  );
}
```

The state is an array, but the lesson is still the same: React remembers the current queue, `clearQueue` requests a new queue, and the next render chooses either the list or the empty state. The button does not directly edit the `<ul>`; it changes state and lets rendering describe the result.

## Line-by-line explanation

| Code line | What it does |
| --- | --- |
| `import { useState } from 'react';` | Imports the Hook that gives a function component a remembered value and an update request. |
| `const [count, setCount] = useState(0);` | Reads the current state snapshot into `count` and receives the setter that requests a next value. The first render uses `0`. |
| `function addOne() {` | Defines the event handler for one click. The handler closes over the `count` snapshot from the render that created it. |
| `setCount(count + 1);` | Calculates a next value from the current snapshot and asks React to render again. It does not change `count` in place. |
| `<p aria-live="polite">` | Gives assistive technology a meaningful place to observe the changing status without making the entire page noisy. |
| `{count}` | Reads the current render's state snapshot and places it in the visible text. |
| `onClick={addOne}` | Passes the function to React. It does not call `addOne` while rendering. |
| `const [cases, setCases] = useState<Case[]>(...)` | Gives React ownership of a list and records its TypeScript shape. |
| `setCases([])` | Requests an empty next array. The next render takes the empty-state branch. |
| `cases.length === 0 ? ... : ...` | Chooses visible UI from the current snapshot; it does not manually show and hide DOM nodes. |

## Execution trace

For the `Counter` example:

1. React renders `Counter` for the first time. `count` is `0`, so the paragraph says `Screen count: 0`.
2. The browser reports a click on the button.
3. React calls `addOne`, which reads the current render's `count` snapshot, calculates `1`, and calls `setCount(1)`.
4. React schedules a new render. The new render reads `count` as `1` and returns a paragraph with `Screen count: 1`.
5. The browser updates the relevant visible output. The old `count` variable was not mutated; a new render received a new snapshot.

For the queue example, `setCases([])` causes the next render to make `cases.length === 0` true, so the `<p>No synthetic cases are waiting.</p>` branch appears.

## Prediction experiment

Predict before running each change:

1. In `BrokenCounter`, click three times. What does the console show? What does the paragraph show?
2. In `Counter`, click three times. What does the paragraph show?
3. In `CaseQueue`, click Clear queue twice. Does the second click produce a new kind of UI or repeat the same empty state?
4. Replace the initial case with an empty array. What should the first render show?

Record the answer, run the experiment, and explain any mismatch. Restore the original fixture afterward.

## Broken example and repair

**Broken version:** change `setCount(count + 1)` to `count += 1` and leave the paragraph unchanged.

The JavaScript number can change inside the event handler, but the component has not requested a new render. The screen is still calculated from the old render. Repair the line with `setCount(count + 1)` and then verify both the first click and a three-click sequence.

Another mistake is expecting this to work:

```tsx
setCount(count + 1);
console.log(count); // still the old render's snapshot
```

The log may show the old value because the setter requests a future render; it does not rewrite the current snapshot. Use the next lesson's functional updater when several updates depend on the previous value.

## Guided practice before independent work

First, run `BrokenCounter` and write down the console and screen results. Second, replace only the local variable with `useState` and predict what changes. Third, move the click logic into a named handler. Fourth, change the state from a number to a one-item array and add an empty branch. Do not add a reducer or Effect; those are later tools for different problems.

## Project application

Build a local **case queue toggle** using invented records. The user must be able to show the queue and clear it. The component should own the queue state, show an empty state after clearing, use a stable key, and announce the number of records in a short status message. Write one paragraph explaining why the queue is state and why the static heading is not.

## Independent exercises

### Level 1 — Mechanical confidence

1. Run the local-variable failure and record console versus screen output.
2. Recreate the smallest `useState` counter and verify the first, second, and third clicks.
3. Explain the two values returned by `useState` without calling the setter a mutation.
4. Move the click logic into a named `addOne` handler.

### Level 2 — Applied practice

5. Add a `minusOne` handler and a `Reset` button. Predict the result of the sequence `+1, +1, -1, reset`.
6. Replace the number with a `Case[]` state and render a list.
7. Add a `Clear queue` button and a useful empty state.
8. Add an `aria-live` status that reports the current queue size.

### Level 3 — Synthesis

9. Reproduce the local-variable bug and explain why a console change does not prove a screen update.
10. Use an initial state function for a small local fixture and explain when lazy initialization is useful.
11. Add a test or written acceptance check for normal, empty, and repeated-clear behavior.
12. Write a review note naming the state owner, event boundary, visible evidence, one limitation, and why a reducer is not yet necessary.

## Finish line

You are ready for the next lesson when you can explain state without saying “React just remembers it,” show the failure of a local variable, trace a setter to a later render, and choose a state owner for a small queue.

## References

- [React Learn: Adding Interactivity](https://react.dev/learn/adding-interactivity)
- [React Learn: State as a Snapshot](https://react.dev/learn/state-as-a-snapshot)
- [React Learn: Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure)
- [Original 30 Days of React States lesson](https://github.com/Asabeneh/30-Days-Of-React/blob/master/08_Day_States/08_states.md)
