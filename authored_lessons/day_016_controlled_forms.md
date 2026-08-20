# Day 016: Controlled forms

[← Previous lesson](../day_015_derived_state_and_the_single_source_of_truth/day_015_derived_state_and_the_single_source_of_truth.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_017_uncontrolled_inputs_and_refs/day_017_uncontrolled_inputs_and_refs.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What makes an input controlled?](#what-makes-an-input-controlled)
  - [Why should the value and onChange work together?](#why-should-the-value-and-onchange-work-together)
  - [When should validation run?](#when-should-validation-run)
  - [What is the difference between browser and server validation?](#what-is-the-difference-between-browser-and-server-validation)
  - [How do we submit a controlled form?](#how-do-we-submit-a-controlled-form)
- [Worked example](#worked-example)
  - [Example 1: one controlled field](#example-1-one-controlled-field)
  - [Example 2: a controlled case form](#example-2-a-controlled-case-form)
  - [Example 3: visible validation](#example-3-visible-validation)
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

Read the [README](../README.md), confirm [setup](../SETUP.md), and use the React playground in [examples](../examples/README.md). Build the form locally with synthetic data. Today the form does not contact a server; that boundary comes later.

## Why this lesson exists

A form is a conversation with a person. The person types, pauses, changes their mind, submits, and may make a mistake. If React owns the current value, the interface can show a preview, enable or disable a button, and explain an error before submission. If the DOM owns the value, the application can still read it at submit time, but it cannot use the same live state as easily.

A controlled input has two halves: `value` tells React what the input should display, and `onChange` tells React what the user just typed. Remove either half and the conversation breaks. This lesson builds one field, then a two-field case form, then a deliberate validation message.

## Prerequisites

Complete state, events, derived state, and one-way data flow. You need `useState`, `onChange`, `onSubmit`, object spread, and labels.

## Outcomes

You should be able to define a controlled input, keep a form object synchronized without dropping fields, prevent default submission intentionally, display a useful client-side message, and explain why client validation improves experience but does not replace server validation or authorization.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Controlled input** | An input whose displayed `value` comes from React state. |
| **onChange** | The handler that receives a new input value and requests state to change. |
| **Form state** | The current values and status needed to describe a form. |
| **Validation** | Checking whether an input is acceptable for the next boundary. |
| **Field error** | A message associated with one input's invalid value. |
| **Submit** | The event that represents the form's request to continue. |
| **Untrusted input** | Data that may be malformed or dishonest until a boundary validates it. |

## Topics

### What makes an input controlled?

React controls the value when the input receives `value={state}` and sends changes through `onChange`. The DOM displays the state snapshot; it is not the independent source of truth.

### Why should the value and onChange work together?

`value` without `onChange` makes an input appear locked because React keeps giving it the same value. `onChange` without `value` gives the DOM ownership. For a controlled field, the pair is deliberate.

### When should validation run?

Validation timing depends on the experience. Required fields can be checked on submit. A format hint may be checked while typing or on blur. Do not show an alarming error before the learner has had a chance to type; choose the event that matches the rule.

### What is the difference between browser and server validation?

Client validation gives immediate feedback and prevents obvious mistakes. It can be bypassed. A server or Route Handler must validate again before trusting data, and authorization must be checked separately.

### How do we submit a controlled form?

Put the behavior on the form's `onSubmit`, call `preventDefault` when this local app owns the next step, inspect the current state or `FormData`, validate, and show a deliberate result. A button click alone misses keyboard submission.

## Worked example

### Example 1: one controlled field

```tsx
import { useState } from 'react';

export default function TitleField() {
  const [title, setTitle] = useState('');

  return (
    <label>
      Case title
      <input
        value={title}
        onChange={(event) => setTitle(event.target.value)}
      />
      <span>Preview: {title || 'Untitled'}</span>
    </label>
  );
}
```

Type into the field. The preview changes because `onChange` requests a new state value and the next render sends that value back to `value`.

### Example 2: a controlled case form

```tsx
import { useState } from 'react';

type Draft = { title: string; owner: string };

export default function CaseForm() {
  const [draft, setDraft] = useState<Draft>({ title: '', owner: '' });
  const [submitted, setSubmitted] = useState<string | null>(null);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setSubmitted(`${draft.title} assigned to ${draft.owner}`);
  }

  return (
    <form onSubmit={handleSubmit}>
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
      <button type="submit">Save local draft</button>
      {submitted && <p role="status">{submitted}</p>}
    </form>
  );
}
```

The state object is updated immutably so changing `owner` preserves `title`. The local submit message is only a fixture; it is not a database write.

### Example 3: visible validation

```tsx
function CaseForm() {
  const [draft, setDraft] = useState<Draft>({ title: '', owner: '' });
  const [error, setError] = useState<string | null>(null);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!draft.title.trim()) {
      setError('Enter a case title before saving.');
      return;
    }
    setError(null);
  }

  return (
    <form onSubmit={handleSubmit} noValidate>
      <label htmlFor="title">Title</label>
      <input
        id="title"
        value={draft.title}
        onChange={(event) =>
          setDraft((current) => ({ ...current, title: event.target.value }))
        }
        aria-invalid={Boolean(error)}
      />
      {error && <p role="alert">{error}</p>}
      <button type="submit">Save</button>
    </form>
  );
}
```

The complete handler keeps the field controlled while the validation branch shows the decision boundary: validation happens before this local action claims success.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `const [draft, setDraft] = useState(...)` | React owns the current form object. |
| `value={draft.title}` | The displayed title comes from the current state snapshot. |
| `onChange={(event) => ...}` | Reads the browser's new string and creates a new draft while preserving the other field. |
| `onSubmit={handleSubmit}` | Owns both mouse and keyboard submission at the form boundary. |
| `event.preventDefault()` | Stops this local demo from navigating away. It does not validate or authorize. |
| `if (!draft.title.trim())` | Applies a client-side required-field rule before the local success path. |
| `aria-invalid={Boolean(error)}` | Communicates the error state to assistive technology. |
| `role="alert"` | Gives the error message an appropriate announcement role; the label still names the input. |

## Execution trace

1. The first render has an empty title and owner.
2. The learner types `Review` into Title.
3. The input handler receives the new string and requests a new draft with the owner preserved.
4. The next render sends `Review` back to the input and updates the preview.
5. Submit prevents navigation and checks the draft.
6. An empty title produces an error branch; a non-empty title clears the error and can show a local success message.

## Prediction experiment

Remove `value` and type. Remove `onChange` while keeping `value`. Change the title, then owner, and predict whether the other field survives. Submit an empty title and a title containing spaces. Record which behavior is client experience and which would still need server validation.

## Broken example and repair

**Broken version:**

```tsx
<input value={draft.title} />
```

The field is controlled but has no way to request a new value, so it becomes read-only. Repair it with `onChange`. Another broken version updates the object as `setDraft({ title: event.target.value })`, which drops `owner`; repair it with the functional spread update.

## Guided practice before independent work

Control one field. Add a preview. Add a second field using object spread. Submit through the form and prevent default. Add one required-field message. Finally, remove the `onChange` handler to feel the locked-input failure and repair it.

## Project application

Build a local **case draft form** with title, owner, notes, reset, empty values, and a local success message. Add labels, field error text, and an acceptance note that client validation is not server authorization.

## Independent exercises

### Level 1 — Confidence

1. Control one input with `value` and `onChange`.
2. Add a preview of the current value.
3. Add a second field while preserving the first.
4. Submit from both button click and Enter.

### Level 2 — Application

5. Add required-title validation.
6. Add a reset button and initial state.
7. Add an accessible error and status message.
8. Reproduce and repair the locked-input and dropped-field failures.

### Level 3 — Synthesis

9. Explain client validation versus server validation.
10. Add a local normal, empty, and invalid fixture.
11. Add a test or manual evidence note for submit and reset.
12. Write a review note with state shape, event boundary, evidence, limitation, and next server-side boundary.

## Finish line

You are ready when you can build a controlled form without losing fields, explain why submit belongs on the form, and state honestly why browser validation cannot authorize a real mutation.

## References

- [React Learn: Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state)
- [React Learn: Sharing State Between Components](https://react.dev/learn/sharing-state-between-components)
- [MDN: Form validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)
