# Day 005: Tooling and the first component

[← Previous lesson](../day_004_typescript_foundations_for_ui_code/day_004_typescript_foundations_for_ui_code.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_006_what_is_a_component/day_006_what_is_a_component.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does a toolchain do?](#what-does-a-toolchain-do)
  - [What is a React component?](#what-is-a-react-component)
  - [How does JSX become browser output?](#how-does-jsx-become-browser-output)
  - [How do we verify a first component?](#how-do-we-verify-a-first-component)
- [Worked example](#worked-example)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: A page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate. A complete page is like a room with labeled areas: the labels help people find and change one responsibility without opening the whole building. This lesson teaches **Tooling and the first component** through a connected sequence rather than a finished file dropped from the sky: We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **JavaScript functions, JSX, and the local React playground**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **tooling and the first component** to a local case dashboard built from a shell, summary, list, and card. You should be able to name the owner and boundary—the parent-to-child data flow and the responsibility owned by each component—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `package.json` | The Node project manifest containing scripts, package metadata, and dependency declarations. |
| `bundler` | A build tool that follows module imports and produces runtime-ready output files. |
| `component` | A reusable unit of UI that receives inputs and returns a description of what should appear. |
| `JSX` | JavaScript syntax that describes UI elements using markup-like notation. |
| `render` | React evaluating component inputs and returning a description of the current UI. |
| `dev server` | A local development process that watches source files and serves the application with fast feedback. |

## Topics

### What does a toolchain do?

Start with the learner's concrete question: **What does a toolchain do**. Use the worked example to show what **What does a toolchain do** changes before introducing a framework shortcut. For **What does a toolchain do**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What does a toolchain do**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What does a toolchain do?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### What is a React component?

Start with the learner's concrete question: **What is a React component**. Use the worked example to show what **What is a React component** changes before introducing a framework shortcut. For **What is a React component**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is a React component**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is a React component?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How does JSX become browser output?

To answer **How does JSX become browser output**, follow the operation in order rather than treating the result as framework magic. For **How does JSX become browser output**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How does JSX become browser output**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How does JSX become browser output?**, change one input or boundary in the worked example. Trace the result for **How does JSX become browser output?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### How do we verify a first component?

To answer **How do we verify a first component**, follow the operation in order rather than treating the result as framework magic. For **How do we verify a first component**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we verify a first component**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we verify a first component?**, change one input or boundary in the worked example. Trace the result for **How do we verify a first component?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard.

```tsx
function Greeting() {
  return <h1>Hello, learner</h1>;
}
console.log(Greeting().type);
```

**Expected result or visible behavior:**

```text
h1
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the parent-to-child data flow and the responsibility owned by each component.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `function Greeting() {` — Declares a callable behavior or component boundary; note its inputs, owner, and when the runtime invokes it. |
| 2 | `return <h1>Hello, learner</h1>;` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |
| 3 | `}` — Runs inside the current example; connect its effect to the parent-to-child data flow and the responsibility owned by each component. |
| 4 | `console.log(Greeting().type);` — Writes an observation so the learner can compare runtime evidence with the prediction; console output is not the same as screen output. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Tooling and the first component**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Return a lowercase component name and explain why React treats it differently from a capitalized component.

Run the broken version in a local copy. The likely beginner mistake for this family is: Split every element mechanically or use a lowercase component name that JSX treats as a browser element. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **tooling and the first component** to a local case dashboard built from a shell, summary, list, and card. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local case dashboard built from a shell, summary, list, and card using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the parent-to-child data flow and the responsibility owned by each component. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the smallest page unchanged and list its visible responsibilities.
2. Split one responsibility into a named component without changing the visible result.
3. Explain why the chosen boundary earns a name.
4. Pass one prop from the parent and render two different values.
5. Compose a parent with two children and draw the data direction.
6. Reproduce the lowercase-component mistake and record the result.
7. Repair the capitalization and rerun the normal case.
8. Add a stable local fixture and an empty or fallback state.
9. Add one semantic or keyboard-accessibility improvement.
10. Add an assertion for a visible component contract.
11. Apply the boundary to a local feature and name its owner.
12. Write a review note with the component tree, evidence, and one limitation.

## Finish line

You are finished when you can teach **Tooling and the first component** to another beginner, show the normal and broken runs, explain the repair, and point to **the parent-to-child data flow and the responsibility owned by each component**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

## References

- [React Learn](https://react.dev/learn)
- [React Reference](https://react.dev/reference/react)
- [Next.js Documentation](https://nextjs.org/docs)
- [Next.js Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
- [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Next.js Authentication](https://nextjs.org/docs/app/guides/authentication)
- [Next.js Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
- [Tailwind CSS with Next.js](https://tailwindcss.com/docs/installation/framework-guides/nextjs)
- [shadcn/ui with Next.js](https://ui.shadcn.com/docs/installation/next)
