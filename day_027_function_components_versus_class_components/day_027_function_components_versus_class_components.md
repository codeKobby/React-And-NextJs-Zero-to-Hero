# Day 027: Function components versus class components

[← Previous lesson](../day_026_suspense_and_the_use_api/day_026_suspense_and_the_use_api.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_028_class_lifecycle_to_modern_hooks/day_028_class_lifecycle_to_modern_hooks.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a class component?](#what-is-a-class-component)
  - [What is a function component?](#what-is-a-function-component)
  - [Why are function components the modern default?](#why-are-function-components-the-modern-default)
  - [How does class state become Hook state?](#how-does-class-state-become-hook-state)
  - [When must we still read class code?](#when-must-we-still-read-class-code)
- [Worked example](#worked-example)
  - [Example 1: the legacy class](#example-1-the-legacy-class)
  - [Example 2: the function equivalent](#example-2-the-function-equivalent)
  - [Example 3: compare the responsibilities](#example-3-compare-the-responsibilities)
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

Run the React playground from [examples](../examples/README.md) after reading the [README](../README.md) and [setup](../SETUP.md). This is a reading-and-migration lesson. You may write both versions, but do not delete the class version before you understand what it does.

## Why this lesson exists

A new React learner may hear that class components are “old” and conclude that old code can be ignored. That is a practical problem: a university project, a workplace repository, or a dependency may still contain classes. A strong React engineer can read the old model, identify its responsibilities, and choose a modern model for new code.

The goal is not to hold a popularity contest. We will compare the same counter in a class and a function. The class stores state on `this`, renders from `this.state`, and calls `this.setState`. The function uses `useState`, a state snapshot, and a setter. Then we will identify what cannot be translated by replacing names mechanically.

## Prerequisites

Complete components, props, state, and basic JavaScript classes. You should know that a setter requests a new state value and that a render returns UI.

## Outcomes

You should be able to read `extends React.Component`, `this.state`, `this.setState`, and `render()`, write the function equivalent with `useState`, explain why function components are the modern default, and identify where lifecycle or error-boundary behavior requires more careful migration.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Class component** | A React component class that extends `React.Component` and usually renders from a `render()` method. |
| **Function component** | A function that returns JSX and can use Hooks for modern React features. |
| **`this`** | The class instance reference used by class methods and state. |
| **`render()`** | The class method that returns the component's UI. |
| **Lifecycle** | Stages such as mount, update, and unmount in a component's existence. |
| **Hook** | A React function with call-site rules that gives a function component access to React features. |
| **Migration** | Moving behavior to a new model while preserving requirements and visible behavior. |

## Topics

### What is a class component?

A class component is an instance of a JavaScript class that React creates and manages. It reads state through `this.state`, changes it with `this.setState`, and returns JSX from `render()`. Its methods and binding rules are part of the mental model.

### What is a function component?

A function component is a function that React renders. It receives props as arguments and uses Hooks such as `useState` for state. There is no `this` instance; ownership is visible through local names and Hook calls.

### Why are function components the modern default?

Function components work naturally with Hooks, Server Components, and the current React documentation. They usually make the data flow and synchronization rule easier to see. This does not make class code invalid; it makes functions the better default for new features in this course.

### How does class state become Hook state?

A class field such as `state = { count: 0 }` becomes `const [count, setCount] = useState(0)`. `this.setState({ count: next })` becomes a setter request. If the next value depends on the previous value, use a functional updater. Object merging also changes: Hook state replacement requires an explicit spread.

### When must we still read class code?

Read class code when maintaining a legacy application, debugging an existing dependency, understanding a lifecycle, or reviewing an error boundary. Do not migrate a line mechanically until you can state the behavior the old code was responsible for.

## Worked example

### Example 1: the legacy class

```tsx
import { Component } from 'react';

type Props = { label: string };

type State = { count: number };

export class LegacyCounter extends Component<Props, State> {
  state: State = { count: 0 };

  addOne = () => {
    this.setState((current) => ({ count: current.count + 1 }));
  };

  render() {
    return (
      <section>
        <h2>{this.props.label}</h2>
        <p>Count: {this.state.count}</p>
        <button type="button" onClick={this.addOne}>Add one</button>
      </section>
    );
  }
}
```

Identify the instance, state field, method, props, and render output before changing anything.

### Example 2: the function equivalent

```tsx
import { useState } from 'react';

type Props = { label: string };

export function Counter({ label }: Props) {
  const [count, setCount] = useState(0);

  function addOne() {
    setCount((current) => current + 1);
  }

  return (
    <section>
      <h2>{label}</h2>
      <p>Count: {count}</p>
      <button type="button" onClick={addOne}>Add one</button>
    </section>
  );
}
```

The visible behavior is the same. The function has no instance and no `this`; the Hook names the current state and the update request.

### Example 3: compare the responsibilities

| Responsibility | Class model | Function model |
| --- | --- | --- |
| Input | `this.props.label` | `label` argument |
| State | `this.state.count` | `count` from `useState` |
| Update | `this.setState(...)` | `setCount(...)` |
| UI method | `render()` | function return |
| Instance context | `this` | local variables and closures |
| Migration risk | implicit merge and binding rules | explicit replacement and Hook call rules |

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `extends Component<Props, State>` | Declares the legacy class relationship and its input/state types. |
| `state = { count: 0 }` | Creates instance state for the class. |
| `this.setState((current) => ...)` | Requests a next class state from the previous state. |
| `this.props.label` | Reads input from the class instance. |
| `const [count, setCount] = useState(0)` | Gives the function component a state snapshot and setter. |
| `setCount((current) => current + 1)` | Requests the next function-component state from the latest value. |
| `return (...)` | The function's return is its UI description; there is no separate `render()` method. |

## Execution trace

The class renders with `this.state.count = 0`. A click invokes the bound arrow method, `this.setState` requests `1`, and React renders the class again. The function renders with `count = 0`. A click invokes `addOne`, the updater receives `0`, and React renders the function again with `count = 1`. The user-visible result is the same; the ownership and API are different.

## Prediction experiment

Predict what happens if `this` is removed from the class state read, if a normal function method loses its binding, and if a function component tries to read `this.state`. Then compare the class's object state update with a Hook object update and identify the merge difference.

## Broken example and repair

**Broken migration:**

```tsx
function Counter() {
  this.setState({ count: 1 });
  return <p>{this.state.count}</p>;
}
```

A function component has no class instance. Repair it with `useState`, a named setter, and a functional updater where the next value depends on the current value. Do not repair the code by adding a fake `this` object; that hides the model difference.

## Guided practice before independent work

Read the class example and label its responsibilities. Rewrite only the state declaration. Rewrite the handler. Rewrite the render method. Run both versions and compare visible behavior. Finally, list one lifecycle or error-boundary behavior that requires a separate migration decision.

## Project application

Migrate a small legacy counter or profile card in the local playground. Keep the old version in a separate file, write the function version, and document the behavior preserved, the API changed, and the evidence collected.

## Independent exercises

### Level 1 — Confidence
1. What is Function components versus class components? Answer in one sentence.
2. Identify `this`, `state`, `setState`, props, and `render` in the class.
3. Run the class example and record the visible result.
4. Write the function state equivalent.
5. Run the function example and compare output.

### Level 2 — Application
6. Migrate an object state field with explicit spread.
7. Migrate a callback handler and preserve keyboard behavior.
8. Add a prop and explain its owner in both versions.
9. Compare the two traces.

### Level 3 — Synthesis
10. Reproduce the missing-`this` or fake-`this` failure and repair it.
11. Identify a lifecycle behavior that should not be translated mechanically.
12. Run both versions with the same input. Write down whether the visible result is the same.
13. Write a migration review with changed responsibilities, risks, and residual legacy work.

## Finish line

You are ready when you can read a class component without contempt, write the modern function equivalent, and explain the behavior that still requires a careful migration decision.

## References

- [React Learn: Your First Component](https://react.dev/learn/your-first-component)
- [React Reference: Component](https://react.dev/reference/react/Component)
- [React Reference: useState](https://react.dev/reference/react/useState)
