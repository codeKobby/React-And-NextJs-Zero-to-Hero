# Day 021: What is useEffect?

[← Previous lesson](../day_020_context_and_providers/day_020_context_and_providers.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_022_effect_dependencies_and_cleanup/day_022_effect_dependencies_and_cleanup.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is an external system?](#what-is-an-external-system)
  - [What is an Effect?](#what-is-an-effect)
  - [Why is an Effect synchronization rather than a calculation?](#why-is-an-effect-synchronization-rather-than-a-calculation)
  - [When does an Effect run?](#when-does-an-effect-run)
  - [What is cleanup?](#what-is-cleanup)
- [Worked example](#worked-example)
  - [Example 1: synchronize the document title](#example-1-synchronize-the-document-title)
  - [Example 2: synchronize a timer](#example-2-synchronize-a-timer)
  - [Example 3: remove an unnecessary Effect](#example-3-remove-an-unnecessary-effect)
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

Read the [README](../README.md), confirm [setup](../SETUP.md), and use the React playground from [examples](../examples/README.md). This lesson uses browser APIs only. Do not add a data fetch just to make an Effect look impressive.

## Why this lesson exists

Most component code is a calculation: given props and state, return JSX. Some work is different because it talks to something outside React. Changing `document.title`, starting a timer, subscribing to a browser event, connecting to a chat room, or synchronizing a non-React widget are external-system work.

`useEffect` is a tool for synchronizing after React renders. It is not a place to put every piece of code that feels important. If a value can be calculated from props and state during render, an Effect adds a second state transition and more chances for stale data. We will first synchronize a title, then create a timer with cleanup, then remove an unnecessary derived-data Effect.

## Prerequisites

Complete state, events, controlled forms, and basic browser APIs. You need dependency arrays, functions, and cleanup callbacks. You do not need data fetching; the browser title and timer are enough to see the lifecycle.

## Outcomes

You should be able to identify an external system, write a minimal Effect with a complete dependency list, return cleanup for a timer or subscription, distinguish synchronization from a render-time calculation, and explain what happens when the dependency changes.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Effect** | Code that synchronizes a component with an external system after rendering. |
| **External system** | Something outside React that the component must coordinate with. |
| **Dependency** | A prop, state value, or function value that can change the synchronization input. |
| **Cleanup** | The function that disconnects, cancels, or reverses an earlier external setup. |
| **Subscription** | A connection that receives future events until it is removed. |
| **Stale closure** | A function that still reads values from an older render. |
| **Render-time calculation** | A value derived directly from current props and state without external synchronization. |

## Topics

### What is an external system?

An external system is not controlled by React's returned JSX: the browser document, a timer, a WebSocket, a media player, or a third-party widget. If no outside system exists, first ask whether ordinary rendering is enough.

### What is an Effect?

An Effect is a post-render synchronization step. React runs the setup after committing the UI, and the setup may return cleanup. The component describes the relationship between its current inputs and the external system.

### Why is an Effect synchronization rather than a calculation?

A filtered array, formatted label, or derived count is a calculation and can normally be created during render. An Effect for it causes a render, then an extra state update, and can briefly show stale output. Effects are for keeping something outside React in step.

### When does an Effect run?

The dependency list describes which values the synchronization uses. With `[title]`, the title synchronization runs after the first commit and when title changes. With no list, it runs after every render. An empty list means the setup does not depend on changing reactive values; it is not a general “run once” escape hatch.

### What is cleanup?

Cleanup runs before a changed Effect's next setup and when the component leaves the tree. It should remove an event listener, clear a timer, disconnect a subscription, or abort work started by the setup. Cleanup prevents old external work from continuing after the component's responsibility changes.

## Worked example

### Example 1: synchronize the document title

```tsx
import { useEffect, useState } from 'react';

export default function TitleDemo() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Cases: ${count}`;
  }, [count]);

  return (
    <button type="button" onClick={() => setCount((current) => current + 1)}>
      Cases: {count}
    </button>
  );
}
```

The button is rendered first. After the commit, the Effect updates the browser tab title. Clicking changes state, React renders the new count, and the Effect synchronizes the title again.

### Example 2: synchronize a timer

```tsx
import { useEffect, useState } from 'react';

export default function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const id = window.setInterval(() => {
      setSeconds((current) => current + 1);
    }, 1000);

    return () => window.clearInterval(id);
  }, []);

  return <p aria-live="polite">Seconds: {seconds}</p>;
}
```

The timer is outside React. The state is inside React. The interval callback uses a functional updater because it runs later. Cleanup clears the interval when the component leaves the page.

### Example 3: remove an unnecessary Effect

This is a common overuse:

```tsx
const [completed, setCompleted] = useState(0);

useEffect(() => {
  setCompleted(tasks.filter((task) => task.done).length);
}, [tasks]);
```

The completed count is derived from `tasks`; no external system is involved. The simpler version is:

```tsx
const completed = tasks.filter((task) => task.done).length;
```

This calculation is available during the same render and does not need a second state value or Effect.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `useEffect(() => {` | Schedules synchronization work after React commits the render. |
| `document.title = ...` | Changes a browser-owned external system; this is why an Effect is relevant. |
| `[count]` | Declares that the synchronization depends on the current count. |
| `window.setInterval(...)` | Starts external timer work and returns an identifier. |
| `setSeconds((current) => current + 1)` | Requests the next state from the latest timer value rather than a stale closure snapshot. |
| `return () => window.clearInterval(id)` | Cleans up the timer when the Effect is replaced or removed. |
| `tasks.filter(...)` | Calculates derived data during render; it does not need an Effect. |

## Execution trace

For the title example:

1. The first render shows `Cases: 0`.
2. React commits the button.
3. The Effect runs and assigns `document.title = 'Cases: 0'`.
4. A click requests count `1`.
5. React renders `Cases: 1` and commits it.
6. The dependency changed, so React runs the Effect again and assigns `Cases: 1` to the title.

For the timer, cleanup runs before a replacement setup or when the component leaves. Without cleanup, old intervals continue to update state after the component no longer owns the page.

## Prediction experiment

Predict the browser title after the first render and after two clicks. Predict how many intervals exist after mounting and after unmounting. Remove cleanup temporarily and describe the risk. Replace the derived-count Effect with an ordinary calculation and compare the number of renders and states you need to reason about.

## Broken example and repair

**Broken version:** calculate completed tasks in an Effect and store it in state. The UI can briefly show an old count and the code has two sources of truth. Repair it with a render-time calculation.

Another broken version omits `count` from the title dependency list. The title can remain stale after the button changes. Repair the dependency list and ask whether the Effect is actually needed for the browser title.

## Guided practice before independent work

First, synchronize a title. Second, add one dependency. Third, add a timer and return cleanup. Fourth, remove an Effect that only derives a value. Fifth, inspect the result after unmounting the timer component. Do not use an empty dependency list to silence a warning without explaining why the setup has no changing reactive input.

## Project application

Build a local **case review timer** that shows a selected case title in the browser tab while counting seconds spent on the fixture. Start the timer when the component is present and clear it when it is removed. Explain why the title and timer are Effects but a completed-count calculation is not.

## Independent exercises

### Level 1 — Confidence
1. What is What is useEffect?? Answer in one sentence.
2. Synchronize `document.title` with a local value.
3. Change the value and predict the title.
4. Add a timer with cleanup.
5. Trace setup and cleanup in writing.

### Level 2 — Application
6. Add a dependency and observe reruns.
7. Remove an unnecessary derived-data Effect.
8. Add a local empty or paused timer state.
9. Use a functional updater inside delayed work.

### Level 3 — Synthesis
10. Reproduce a stale dependency and repair it.
11. Reproduce a missing-cleanup risk and repair it.
12. Run the example, then remove the component. Write down what runs before and after removal.
13. Write a review note naming the external system, dependency, cleanup, evidence, and limitation.

## Finish line

You are ready when you can explain what is outside React, why an Effect synchronizes it, how cleanup protects ownership, and why a derived value usually belongs in render rather than state plus Effect.

## References

- [React Learn: Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects)
- [React Learn: You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect)
- [React Reference: useEffect](https://react.dev/reference/react/useEffect)
