# Day 061: Getters, setters, and state boundaries

[← Previous lesson](../day_060_final_demonstration_and_portfolio_review/day_060_final_demonstration_and_portfolio_review.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_062_tailwind_css_v4_setup_in_next_js/day_062_tailwind_css_v4_setup_in_next_js.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a JavaScript getter?](#what-is-a-javascript-getter)
  - [What is a JavaScript setter?](#what-is-a-javascript-setter)
  - [Why use an accessor boundary?](#why-use-an-accessor-boundary)
  - [How is a property setter different from a React state setter?](#how-is-a-property-setter-different-from-a-react-state-setter)
  - [Where should validation and ownership live?](#where-should-validation-and-ownership-live)
- [Worked example](#worked-example)
  - [Example 1: a getter reads a normalized model](#example-1-a-getter-reads-a-normalized-model)
  - [Example 2: a setter normalizes assignment](#example-2-a-setter-normalizes-assignment)
  - [Example 3: React state still needs an explicit request](#example-3-react-state-still-needs-an-explicit-request)
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

Read the [README](../README.md), confirm [setup](../SETUP.md), and use the local examples from [examples](../examples/README.md). This lesson is a bridge between JavaScript language behavior and React behavior. Keep the two examples in separate files so their boundaries do not blur.

## Why this lesson exists

The words getter and setter appear in two different conversations. JavaScript has property accessors: a getter runs when code reads a property, and a setter runs when code assigns to a property. React has state setters returned by `useState`: they request a new state value and a later render.

The names sound similar, but the operations are not the same. A JavaScript property setter can normalize one assignment immediately. A React state setter does not intercept ordinary property assignment; it schedules a new state snapshot. Understanding the distinction prevents a subtle category error in both everyday JavaScript and React code.

## Prerequisites

Complete JavaScript objects, classes or object literals, React state, controlled inputs, and the earlier state lessons.

## Outcomes

You should be able to define a getter and setter, trace property access and assignment, use an accessor to protect a small model boundary, explain why a React state setter is different, and choose where validation belongs in a UI or server application.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Getter** | A JavaScript accessor that runs when a property is read. |
| **Setter** | A JavaScript accessor that runs when a property is assigned. |
| **Accessor** | A getter or setter that controls property access syntax. |
| **Encapsulation** | Keeping representation details behind a smaller public boundary. |
| **Normalization** | Converting an input into a consistent form, such as trimming whitespace. |
| **React state setter** | A function that requests a next state value and a later render. |
| **Ownership** | The boundary responsible for validating and changing a value. |

## Topics

### What is a JavaScript getter?

A getter is declared with `get name()`. Code reads `object.name` as if it were a normal property, but JavaScript runs the getter. It can calculate or expose a normalized view of internal data.

### What is a JavaScript setter?

A setter is declared with `set name(value)`. Code assigns `object.name = value`, and JavaScript invokes the setter with the assigned value. The setter can normalize or reject the input before storing it.

### Why use an accessor boundary?

An accessor can protect a small model from repeated normalization code. It should remain unsurprising: if a setter trims a name, document that behavior; if it throws, callers need a deliberate error contract.

### How is a property setter different from a React state setter?

A property setter runs because JavaScript assignment syntax accesses an accessor. A React state setter is an ordinary function call returned by `useState`. It requests a next state value; it does not run because `state.name = ...` happened and it does not make direct mutation reactive.

### Where should validation and ownership live?

Normalize at the boundary that owns the model, validate again at a server trust boundary, and keep React state updates explicit. A JavaScript accessor can improve local model consistency; it cannot authorize a request or replace server validation.

## Worked example

### Example 1: a getter reads a normalized model

```ts
const account = {
  _name: 'Ada',
  get name() {
    return this._name.trim();
  },
};

console.log(account.name);
```

Reading `account.name` runs the getter and prints `Ada`.

### Example 2: a setter normalizes assignment

```ts
const account = {
  _name: 'Ada',
  get name() {
    return this._name;
  },
  set name(value: string) {
    this._name = value.trim();
  },
};

account.name = ' Grace ';
console.log(account.name);
```

Assignment runs the setter, which stores `Grace`. The syntax looks like ordinary assignment, but the accessor controls what is stored.

### Example 3: React state still needs an explicit request

```tsx
import { useState } from 'react';

type Profile = { name: string };

export default function ProfileEditor() {
  const [profile, setProfile] = useState<Profile>({ name: 'Ada' });

  function rename() {
    setProfile((current) => ({ ...current, name: 'Grace' }));
  }

  return (
    <button type="button" onClick={rename}>
      {profile.name}
    </button>
  );
}
```

`profile.name = 'Grace'` would mutate the current object and would not be the correct React update. `setProfile` is called explicitly and returns a new object so React can render the next snapshot.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `_name: 'Ada'` | Stores the internal representation used by the accessor example. The underscore is a convention, not privacy. |
| `get name()` | Defines code that runs when `account.name` is read. |
| `set name(value)` | Defines code that runs when `account.name = value` is assigned. |
| `value.trim()` | Normalizes the assigned string before storage. It is not full validation. |
| `const [profile, setProfile] = useState(...)` | Gives React a state snapshot and explicit update function. |
| `setProfile((current) => ({ ...current, name: 'Grace' }))` | Requests a new object and preserves fields that are not changing. |
| `{profile.name}` | Reads the current React snapshot during render; it does not invoke a JavaScript setter. |

## Execution trace

1. `account.name` is read, so JavaScript invokes the getter.
2. `account.name = ' Grace '` is assigned, so JavaScript invokes the setter with the string.
3. The setter trims and stores `Grace`.
4. In the React example, the first render reads `profile.name` as `Ada`.
5. A click calls `setProfile` with an updater function.
6. React processes the updater and renders a new object with `name: 'Grace'`.

## Prediction experiment

Predict whether `account._name`, `account.name`, and the visible React button change after each operation. Replace the JavaScript setter with direct `_name` mutation. Replace the React setter with `profile.name = 'Grace'`. Record which operation runs immediately and which one requests a later render.

## Broken example and repair

**Broken version:**

```tsx
profile.name = 'Grace';
```

This mutates the object held by the current React state snapshot and does not express a new state value. Repair it with `setProfile((current) => ({ ...current, name: 'Grace' }))`.

Another mistake is putting authorization in a JavaScript setter. A setter can normalize a local value; it cannot prove who is making a network request or whether that actor has permission.

## Guided practice before independent work

Run the getter. Add a setter. Trace read and assignment separately. Then create a React state object and deliberately try the direct mutation. Repair it with a new object and compare the visible result.

## Project application

Build a local **profile editor** with a plain JavaScript model that trims a display name and a React form that updates state explicitly. Add a note explaining which boundary performs normalization, which boundary performs rendering, and which server boundary would still need validation.

## Independent exercises

### Level 1 — Confidence

1. Write and read a getter.
2. Assign through a setter and log the normalized value.
3. Trace the order of getter and setter calls.
4. Explain why `_name` is only a convention.

### Level 2 — Application

5. Add a React state object.
6. Update it with a functional state setter.
7. Reproduce direct property mutation and compare visible behavior.
8. Preserve an untouched field with object spread.

### Level 3 — Synthesis

9. Compare property setter and React state setter in a table.
10. Add a test or manual evidence note for normalization and rendering.
11. Explain why neither accessor is a substitute for server authorization.
12. Write a review note with ownership, evidence, limitation, and next trust boundary.

## Finish line

You are ready when you can explain the two meanings of setter without mixing them, trace property access separately from React rendering, and choose the correct owner for normalization, state, and server validation.

## References

- [MDN: get](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
- [MDN: set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
- [React Reference: useState](https://react.dev/reference/react/useState)
