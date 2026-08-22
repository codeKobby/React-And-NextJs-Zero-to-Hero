# Day 011: Events and event handlers

[← Previous lesson](../day_010_conditional_rendering_and_empty_states/day_010_conditional_rendering_and_empty_states.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_012_what_is_state/day_012_what_is_state.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a browser event?](#what-is-a-browser-event)
  - [What is an event handler?](#what-is-an-event-handler)
  - [Why pass a function instead of calling it?](#why-pass-a-function-instead-of-calling-it)
  - [How do we read event data?](#how-do-we-read-event-data)
  - [When should we prevent default behavior?](#when-should-we-prevent-default-behavior)
- [Worked example](#worked-example)
  - [Example 1: a button handler](#example-1-a-button-handler)
  - [Example 2: read the event target](#example-2-read-the-event-target)
  - [Example 3: stop a form reload](#example-3-stop-a-form-reload)
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

Run the React playground from the [examples guide](../examples/README.md) after reading the [README](../README.md) and [setup guide](../SETUP.md). Events are browser input. State comes next; today we will log and display the event's consequences without introducing state until the final guided step.

## Why this lesson exists

A rendered button is a description. It does not perform a side effect until something happens. A click, key press, input change, and form submit are messages from the browser to the application. React lets us attach a function that responds to that message.

The most common beginner mistake is confusing a function with the result of calling a function. `onClick={handleSave}` gives React a function to call later. `onClick={handleSave()}` calls it while rendering and gives React the result instead. We will make that difference visible.

## Prerequisites

Complete JSX, components, props, and conditional rendering. You need ordinary functions, arrow functions, object properties, and basic browser form behavior.

## Outcomes

You should be able to attach a handler, pass event data to a named function, distinguish `target` from `currentTarget`, prevent a form's default navigation when the application owns submission, and explain why event handling alone is not authorization or validation.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Event** | A browser report that something happened, such as a click or input change. |
| **Handler** | A function that responds to an event. |
| **Callback** | A function supplied to another system so it can call it later. |
| **Target** | The most specific element where the event originated. |
| **Current target** | The element whose handler is currently running. |
| **preventDefault** | A request to stop a browser's default action for an event. |
| **Submit** | A form event that normally sends or navigates according to the form's action. |

## Topics

### What is a browser event?

An event is information about a browser occurrence. A click event includes the element involved and other event details. An input event includes the new value through the target element. The event is not the application's final business decision; it is an input that the handler must interpret safely.

### What is an event handler?

A handler is a function that runs because an event occurred. React receives the function reference while rendering and invokes it later. Keeping a named handler makes it easier to test, trace, and extend.

### Why pass a function instead of calling it?

Rendering should describe what to do later. `onClick={handleSave}` passes the recipe. `onClick={handleSave()}` performs the recipe now. If the call returns `undefined`, React has no handler to run on the click; if it changes state, it may cause a render loop.

### How do we read event data?

Use the event's type and target deliberately. `event.currentTarget` is the element whose handler is running. `event.target` can be a nested element that originated the event. For an input, read the input value and send it to the state owner; do not assume every event target is a text input.

### When should we prevent default behavior?

Prevent default when the browser's built-in action conflicts with the application interaction, such as a form that should submit through a controlled application path. Do not call it automatically on every event. It does not validate input, authorize a user, or make a mutation safe.

## Worked example

### Example 1: a button handler

```tsx
function SaveButton() {
  function handleClick() {
    console.log('Save requested');
  }

  return (
    <button type="button" onClick={handleClick}>
      Save case
    </button>
  );
}

export default function App() {
  return <SaveButton />;
}
```

The message appears only after a click. The handler reference is passed during render and invoked later by React.

### Example 2: read the event target

```tsx
function InspectButton() {
  function handleClick(event: React.MouseEvent<HTMLButtonElement>) {
    console.log(event.currentTarget.textContent);
  }

  return (
    <button type="button" onClick={handleClick}>
      Inspect label
    </button>
  );
}
```

`currentTarget` is the button whose handler is running. If the button contains an icon or span, `target` might be that nested element. For a button's accessible label, current target is usually the clearer boundary.

### Example 3: stop a form reload

```tsx
function CaseSearch() {
  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const form = new FormData(event.currentTarget);
    console.log('Search requested for:', form.get('query'));
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Search cases
        <input name="query" />
      </label>
      <button type="submit">Search</button>
    </form>
  );
}
```

The browser would normally navigate or reload according to the form. This handler stops that default action because the example owns the next step. It still needs validation and a server-authoritative query in a real application; `preventDefault` is only event control.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `function handleClick()` | Declares the behavior that should occur after a click. |
| `onClick={handleClick}` | Gives React the function reference; it does not execute it during render. |
| `event: React.MouseEvent...` | Records the expected mouse event and current target type for this handler. |
| `event.currentTarget.textContent` | Reads text from the element whose handler is running. |
| `onSubmit={handleSubmit}` | Gives the form a submit boundary rather than relying on a click handler alone. |
| `event.preventDefault()` | Stops the browser's default submit navigation for this local controlled example. |
| `new FormData(event.currentTarget)` | Reads the submitted form controls by their names. |
| `form.get('query')` | Retrieves untrusted input; a real mutation or query still needs validation and authorization. |

## Execution trace

1. React renders a button and stores the handler reference in the event boundary.
2. The user clicks; the browser creates a click event.
3. React invokes `handleClick`, which writes an observation.
4. For the form, the browser creates a submit event and React invokes `handleSubmit`.
5. `preventDefault()` stops navigation, then `FormData` reads the named input.
6. The logged value is evidence that the event was received; it is not evidence that the value is valid or that the caller has permission.

## Prediction experiment

Predict whether `onClick={handleClick}` and `onClick={handleClick()}` log before or after the page appears. Add a `<span>` inside the button and compare `target` with `currentTarget`. Remove `preventDefault` from the form and observe the browser behavior. Restore it and record the difference.

## Broken example and repair

**Broken version:**

```tsx
<button type="button" onClick={handleClick()}>Save</button>
```

The function is called while React is rendering. Repair it with `onClick={handleClick}`. If an argument is needed, use a wrapper: `onClick={() => handleCase(caseId)}`. Keep the wrapper small and remember that it runs later.

A second mistake is using a click handler on the submit button instead of the form's `onSubmit`. Pressing Enter may submit without clicking the button. Put submission behavior at the form boundary.

## Guided practice before independent work

First, log a button click. Second, pass the named handler directly. Third, add an argument with a wrapper. Fourth, inspect `currentTarget`. Fifth, add a form and prevent default on submit. Do not call `preventDefault` before observing the browser's default action.

## Project application

Build a local **case search form**. It should read a synthetic query on submit, prevent the page reload, show the query in a visible status area, and handle an empty query explicitly. Do not call a public API. State in a note that input validation and authorization are later boundaries.

## Independent exercises

### Level 1 — Confidence
1. What is Events and event handlers? Answer in one sentence.
2. Log a button click with a named handler.
3. Predict and compare handler reference versus handler invocation.
4. Pass one argument through a wrapper callback.
5. Inspect `currentTarget` and a nested `target`.

### Level 2 — Application
6. Build a labeled form with a submit handler.
7. Observe the default submit behavior, then prevent it intentionally.
8. Read a named field with `FormData`.
9. Add an empty-input message without pretending the input is authorized.

### Level 3 — Synthesis
10. Reproduce the immediate-invocation failure and repair it.
11. Add a visible status and a keyboard path using Enter.
12. Run the form with a normal value and an empty value. Write down what appears.
13. Write a review note describing event ownership, untrusted input, evidence, and limitations.

## Finish line

You are ready for state when you can trace a browser event into a handler, explain why a function reference is passed, and distinguish preventing a browser default from validating or authorizing an application action.

## References

- [React Learn: Responding to Events](https://react.dev/learn/responding-to-events)
- [MDN: Event](https://developer.mozilla.org/en-US/docs/Web/API/Event)
- [MDN: FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
