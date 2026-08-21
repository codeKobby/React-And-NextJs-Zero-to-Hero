# Day 022: Effect dependencies and cleanup

[← Previous lesson](../day_021_what_is_useeffect/day_021_what_is_useeffect.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_023_custom_hooks/day_023_custom_hooks.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a stale closure?](#what-is-a-stale-closure)
  - [Why must dependencies be complete?](#why-must-dependencies-be-complete)
  - [How do we clean up a subscription?](#how-do-we-clean-up-a-subscription)
  - [How do we abort a request?](#how-do-we-abort-a-request)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will distinguish rendering from synchronization, add a dependency, create cleanup, and remove an unnecessary calculation Effect. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: Rendering describes UI, but some work must synchronize with something outside React, such as a title, timer, subscription, or request. A room display can change because the building's outside sign must also be updated; the sign is an external system with a connection and a cleanup rule. This lesson teaches **Effect dependencies and cleanup** through a connected sequence rather than a finished file dropped from the sky: We will distinguish rendering from synchronization, add a dependency, create cleanup, and remove an unnecessary calculation Effect. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **state, render snapshots, functions, and browser APIs**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **effect dependencies and cleanup** to a local status title or synthetic subscription with setup and cleanup evidence. You should be able to name the owner and boundary—the line between React's render calculation and an external system's lifecycle—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `dependency array` | The list of reactive values that determines when a Hook's synchronization or memoized calculation changes. |
| `stale closure` | A function that still reads props or state captured by an older render. |
| `cleanup` | Work that removes or cancels an earlier subscription, timer, request, or resource. |
| `subscription` | A live connection that receives future events until it is explicitly removed. |
| `abort` | Stopping an in-flight asynchronous operation when the caller no longer owns or needs its result. |

## Topics

### What is a stale closure?

Start with the learner's concrete question: **What is a stale closure**. Use the worked example to show what **What is a stale closure** changes before introducing a framework shortcut. For **What is a stale closure**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is a stale closure**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is a stale closure?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why must dependencies be complete?

The answer to **Why must dependencies be complete** must be earned by comparing a working case with a deliberately limited or broken case. For **Why must dependencies be complete**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why must dependencies be complete**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why must dependencies be complete?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a local status title or synthetic subscription with setup and cleanup evidence.

### How do we clean up a subscription?

To answer **How do we clean up a subscription**, follow the operation in order rather than treating the result as framework magic. For **How do we clean up a subscription**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we clean up a subscription**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we clean up a subscription?**, change one input or boundary in the worked example. Trace the result for **How do we clean up a subscription?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### How do we abort a request?

To answer **How do we abort a request**, follow the operation in order rather than treating the result as framework magic. For **How do we abort a request**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we abort a request**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we abort a request?**, change one input or boundary in the worked example. Trace the result for **How do we abort a request?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will distinguish rendering from synchronization, add a dependency, create cleanup, and remove an unnecessary calculation Effect.

```tsx
useEffect(() => {
  const controller = new AbortController();
  return () => controller.abort();
}, [query]);
```

**Expected result or visible behavior:**

```text
Old work is cancelled when query changes.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the line between React's render calculation and an external system's lifecycle.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `useEffect(() => {` — Declares synchronization with an external system; inspect the dependency and cleanup rules rather than treating it as a calculation. |
| 2 | `const controller = new AbortController();` — Creates a named value from the expression on the right; record its input, lifetime, and owner in this day's example. |
| 3 | `return () => controller.abort();` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |
| 4 | `}, [query]);` — Runs inside the current example; connect its effect to the line between React's render calculation and an external system's lifecycle. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Rendering describes UI, but some work must synchronize with something outside React, such as a title, timer, subscription, or request.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will distinguish rendering from synchronization, add a dependency, create cleanup, and remove an unnecessary calculation Effect.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Effect dependencies and cleanup**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Omit query from dependencies and explain the stale result.

Run the broken version in a local copy. The likely beginner mistake for this family is: Use an Effect for a value that can be calculated during render or omit a dependency and observe stale work. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **effect dependencies and cleanup** to a local status title or synthetic subscription with setup and cleanup evidence. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local status title or synthetic subscription with setup and cleanup evidence using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the line between React's render calculation and an external system's lifecycle. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

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
10. Apply the behavior to a local status title or synthetic subscription with setup and cleanup evidence with a local fixture.
11. Explain the boundary between React rendering and the line between React's render calculation and an external system's lifecycle.
12. Write a review note naming what remains untested in an asynchronous environment.

## Finish line

You are finished when you can teach **Effect dependencies and cleanup** to another beginner, show the normal and broken runs, explain the repair, and point to **the line between React's render calculation and an external system's lifecycle**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
