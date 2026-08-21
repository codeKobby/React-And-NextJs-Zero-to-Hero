# Day 015: Derived state and the single source of truth

[← Previous lesson](../day_014_state_for_objects_and_arrays/day_014_state_for_objects_and_arrays.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_016_controlled_forms/day_016_controlled_forms.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is derived state?](#what-is-derived-state)
  - [Why should we avoid storing what can be calculated?](#why-should-we-avoid-storing-what-can-be-calculated)
  - [What is one source of truth?](#what-is-one-source-of-truth)
  - [How do selectors simplify state?](#how-do-selectors-simplify-state)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: Learners need a concrete reason to study derived state and the single source of truth before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. This lesson teaches **Derived state and the single source of truth** through a connected sequence rather than a finished file dropped from the sky: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **derived state and the single source of truth** to a small local fixture that demonstrates derived state and the single source of truth. You should be able to name the owner and boundary—the code or framework boundary that owns the decision in this lesson—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `derived value` | A value calculated from existing props or state rather than stored as a second source of truth. |
| `source of truth` | The one authoritative value from which other views or derived values should be calculated. |
| `duplication` | Repeated knowledge or implementation that can drift because multiple copies must be maintained. |
| `selector` | A function that chooses a smaller value from a larger state or data structure. |
| `invariant` | A condition that must remain true across all accepted states or operations. |

## Topics

### What is derived state?

Start with the learner's concrete question: **What is derived state**. Use the worked example to show what **What is derived state** changes before introducing a framework shortcut. For **What is derived state**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is derived state**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is derived state?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why should we avoid storing what can be calculated?

The answer to **Why should we avoid storing what can be calculated** must be earned by comparing a working case with a deliberately limited or broken case. For **Why should we avoid storing what can be calculated**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why should we avoid storing what can be calculated**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why should we avoid storing what can be calculated?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a small local fixture that demonstrates derived state and the single source of truth.

### What is one source of truth?

Start with the learner's concrete question: **What is one source of truth**. Use the worked example to show what **What is one source of truth** changes before introducing a framework shortcut. For **What is one source of truth**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is one source of truth**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is one source of truth?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do selectors simplify state?

To answer **How do selectors simplify state**, follow the operation in order rather than treating the result as framework magic. For **How do selectors simplify state**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do selectors simplify state**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do selectors simplify state?**, change one input or boundary in the worked example. Trace the result for **How do selectors simplify state?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.

```tsx
const completed = tasks.filter((task) => task.done).length;
return <p>{completed} complete</p>;
```

**Expected result or visible behavior:**

```text
The count is calculated from tasks.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the code or framework boundary that owns the decision in this lesson.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const completed = tasks.filter((task) => task.done).length;` — Declares a callable behavior or component boundary; note its inputs, owner, and when the runtime invokes it. |
| 2 | `return <p>{completed} complete</p>;` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Learners need a concrete reason to study derived state and the single source of truth before the terminology becomes useful.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Derived state and the single source of truth**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Store completedCount separately, create a mismatch, and repair by deriving it.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy the syntax without identifying the input, owner, output, and boundary. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **derived state and the single source of truth** to a small local fixture that demonstrates derived state and the single source of truth. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a small local fixture that demonstrates derived state and the single source of truth using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the code or framework boundary that owns the decision in this lesson. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the smallest state example and record the initial visible snapshot.
2. Trigger one update and trace event, setter or dispatch, and next render.
3. Change one input and predict the new output before running it.
4. Create a normal boundary such as empty, reset, or zero state.
5. Reproduce the likely state ownership or mutation mistake.
6. Repair it with the smallest state-structure change.
7. Compare the current state value with the source that derives it.
8. Add a user-visible status or accessible announcement for the transition.
9. Add an assertion or test for normal and boundary behavior.
10. Apply the lesson to a small local fixture that demonstrates derived state and the single source of truth using synthetic data.
11. Explain why the state belongs at the the code or framework boundary that owns the decision in this lesson.
12. Write a review note naming the next complexity that would justify a different tool.

## Finish line

You are finished when you can teach **Derived state and the single source of truth** to another beginner, show the normal and broken runs, explain the repair, and point to **the code or framework boundary that owns the decision in this lesson**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
