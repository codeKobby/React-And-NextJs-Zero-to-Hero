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

Start with the [course README](../README.md), [setup guide](../SETUP.md), and [day index](../DAY_INDEX.md). Choose the starter from the [examples guide](../examples/README.md). Work locally with invented data only.

Today’s steps are simple: We will distinguish rendering from synchronization, add a dependency, create cleanup, and remove an unnecessary calculation Effect. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: Rendering describes UI, but some work must synchronize with something outside React, such as a title, timer, subscription, or request.

A room display can change because the building's outside sign must also be updated; the sign is an external system with a connection and a cleanup rule.

Today we will learn **Effect dependencies and cleanup** in small steps. We will distinguish rendering from synchronization, add a dependency, create cleanup, and remove an unnecessary calculation Effect. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **state, render snapshots, functions, and browser APIs**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Effect dependencies and cleanup** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **effect dependencies and cleanup** in a local status title or synthetic subscription with setup and cleanup evidence.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line between React's render calculation and an external system's lifecycle.

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

Start with the learner's concrete question: **What is a stale closure**. Look at **What is a stale closure** in the example before learning the technical name. For **What is a stale closure**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is a stale closure**, say what goes in and what comes out.

### Why must dependencies be complete?

Answer **Why must dependencies be complete** by comparing the working example with a broken or limited example. For **Why must dependencies be complete**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why must dependencies be complete?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### How do we clean up a subscription?

To answer **How do we clean up a subscription**, follow the operation in order and check the example. For **How do we clean up a subscription**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we clean up a subscription**, change one input in the example. Write the old result and the new result for **How do we clean up a subscription**.

### How do we abort a request?

To answer **How do we abort a request**, follow the operation in order and check the example. For **How do we abort a request**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we abort a request**, change one input in the example. Write the old result and the new result for **How do we abort a request**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will distinguish rendering from synchronization, add a dependency, create cleanup, and remove an unnecessary calculation Effect.

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

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line between React's render calculation and an external system's lifecycle.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `useEffect(() => {` — Tells React to run this outside task after the screen is updated. |
| 2 | `const controller = new AbortController();` — Stores the value on the right under the name on the left. |
| 3 | `return () => controller.abort();` — Sends a value or UI tree back to the code that called this function. |
| 4 | `}, [query]);` — Runs as part of this example. After `}, [query]);`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: Rendering describes UI, but some work must synchronize with something outside React, such as a title, timer, subscription, or request.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Effect dependencies and cleanup**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Omit query from dependencies and explain the stale result.

Make the broken version in a copy. The likely mistake is: Use an Effect for a value that can be calculated during render or omit a dependency and observe stale work.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **effect dependencies and cleanup** and a local status title or synthetic subscription with setup and cleanup evidence.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local status title or synthetic subscription with setup and cleanup evidence.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the line between React's render calculation and an external system's lifecycle.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Run the example. Write down what appears before you change it.
2. Write the name of the outside thing the code talks to, such as the document title or a timer.
3. Change one dependency. Predict whether the work runs again, then check.
4. Show a loading, empty, or disconnected message that fits the example.
5. Make the Hooks mistake shown in the lesson. Write down the error or wrong result.
6. Fix the mistake and run the example again.
7. Remove the Hook when the value can be calculated during render. Explain the change in one sentence.
8. Add cleanup for the timer, subscription, request, or other outside resource.
9. Write one test or trace that shows setup and cleanup.
10. Use this behavior in a small a local status title or synthetic subscription with setup and cleanup evidence with invented data.
11. Answer: what starts the outside work, and what stops it?
12. Write two things this local example does not prove about a real application.

## Finish line

You are finished when you can:

1. explain **Effect dependencies and cleanup** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **the line between React's render calculation and an external system's lifecycle**.

Do not move on only because the code compiles. Write one limitation of this local example.

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
