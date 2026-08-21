# Day 023: Custom Hooks

[← Previous lesson](../day_022_effect_dependencies_and_cleanup/day_022_effect_dependencies_and_cleanup.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_024_memoization_and_the_react_compiler/day_024_memoization_and_the_react_compiler.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a custom Hook?](#what-is-a-custom-hook)
  - [Which logic belongs in a Hook?](#which-logic-belongs-in-a-hook)
  - [Why must Hook names begin with use?](#why-must-hook-names-begin-with-use)
  - [How do we design a small return API?](#how-do-we-design-a-small-return-api)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will identify repeated behavior, extract a custom Hook, enforce the Rules of Hooks, and design a small return API. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: Several components need the same stateful behavior, but copying the behavior creates inconsistent fixes and unclear APIs. A reusable tool has a small handle and clear result; the person using it should not need to know its internal gears. This lesson teaches **Custom Hooks** through a connected sequence rather than a finished file dropped from the sky: We will identify repeated behavior, extract a custom Hook, enforce the Rules of Hooks, and design a small return API. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **useState, Effects, and function component call sites**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **custom hooks** to a local toggle, data viewer, or form behavior with a named Hook API. You should be able to name the owner and boundary—the Hook owns reusable behavior while the component owns its visible composition—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `custom Hook` | A function that packages reusable Hook logic while following the Rules of Hooks. |
| `reuse` | Applying one tested implementation in multiple contexts without copying its knowledge. |
| `hook rules` | The rules that Hooks are called at the top level of React functions and in a stable order. |
| `composition` | Building a larger UI by placing smaller components together rather than inheriting from them. |
| `return API` | The documented values and behaviors a function or module promises to return to its caller. |

## Topics

### What is a custom Hook?

Start with the learner's concrete question: **What is a custom Hook**. Use the worked example to show what **What is a custom Hook** changes before introducing a framework shortcut. For **What is a custom Hook**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is a custom Hook**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is a custom Hook?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Which logic belongs in a Hook?

Study **Which logic belongs in a Hook** by naming the concrete value, operation, visible result, and owner in the worked example. For **Which logic belongs in a Hook**, underline the line or file where this idea becomes observable and explain what would change it. Keep the conclusion limited to the local evidence for **Which logic belongs in a Hook**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Which logic belongs in a Hook?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why must Hook names begin with use?

The answer to **Why must Hook names begin with use** must be earned by comparing a working case with a deliberately limited or broken case. For **Why must Hook names begin with use**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why must Hook names begin with use**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why must Hook names begin with use?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a local toggle, data viewer, or form behavior with a named Hook API.

### How do we design a small return API?

To answer **How do we design a small return API**, follow the operation in order rather than treating the result as framework magic. For **How do we design a small return API**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we design a small return API**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we design a small return API?**, change one input or boundary in the worked example. Trace the result for **How do we design a small return API?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will identify repeated behavior, extract a custom Hook, enforce the Rules of Hooks, and design a small return API.

```tsx
function useToggle(initial = false) {
  const [value, setValue] = useState(initial);
  return [value, () => setValue((v) => !v)];
}
```

**Expected result or visible behavior:**

```text
The Hook returns state and behavior.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the Hook owns reusable behavior while the component owns its visible composition.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `function useToggle(initial = false) {` — Declares a callable behavior or component boundary; note its inputs, owner, and when the runtime invokes it. |
| 2 | `const [value, setValue] = useState(initial);` — Asks React for a remembered value and names the current render snapshot plus the function that requests the next value. |
| 3 | `return [value, () => setValue((v) => !v)];` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |
| 4 | `}` — Runs inside the current example; connect its effect to the Hook owns reusable behavior while the component owns its visible composition. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Several components need the same stateful behavior, but copying the behavior creates inconsistent fixes and unclear APIs.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will identify repeated behavior, extract a custom Hook, enforce the Rules of Hooks, and design a small return API.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Custom Hooks**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Call a Hook inside an if statement and move it to the component's top level.

Run the broken version in a local copy. The likely beginner mistake for this family is: Call a Hook conditionally or hide unrelated responsibilities in a Hook with an unclear contract. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **custom hooks** to a local toggle, data viewer, or form behavior with a named Hook API. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local toggle, data viewer, or form behavior with a named Hook API using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the Hook owns reusable behavior while the component owns its visible composition. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the smallest Hook or synchronization example unchanged.
2. Name the external system, input, output, and cleanup responsibility.
3. Change one dependency and predict when work runs again.
4. Create a loading, empty, or disconnected boundary appropriate to the example.
5. Reproduce the likely Rules of Hooks or stale-dependency mistake.
6. Repair the mistake without silencing the lint rule or hiding the dependency.
7. Remove the Hook if the behavior can be calculated during render and explain why.
8. Add cleanup evidence for the subscription, timer, request, or resource.
9. Add a test or trace for setup and cleanup behavior.
10. Apply the behavior to a local toggle, data viewer, or form behavior with a named Hook API with a local fixture.
11. Explain the boundary between React rendering and the Hook owns reusable behavior while the component owns its visible composition.
12. Write a review note naming what remains untested in an asynchronous environment.

## Finish line

You are finished when you can teach **Custom Hooks** to another beginner, show the normal and broken runs, explain the repair, and point to **the Hook owns reusable behavior while the component owns its visible composition**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
