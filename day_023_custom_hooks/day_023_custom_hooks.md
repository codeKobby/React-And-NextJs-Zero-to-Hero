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

Start with the [course README](../README.md), [setup guide](../SETUP.md), and [day index](../DAY_INDEX.md). Choose the starter from the [examples guide](../examples/README.md). Work locally with invented data only.

Today’s steps are simple: We will identify repeated behavior, extract a custom Hook, enforce the Rules of Hooks, and design a small return API. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: Several components need the same stateful behavior, but copying the behavior creates inconsistent fixes and unclear APIs.

A reusable tool has a small handle and clear result; the person using it should not need to know its internal gears.

Today we will learn **Custom Hooks** in small steps. We will identify repeated behavior, extract a custom Hook, enforce the Rules of Hooks, and design a small return API. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **useState, Effects, and function component call sites**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Custom Hooks** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **custom hooks** in a local toggle, data viewer, or form behavior with a named Hook API.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the Hook owns reusable behavior while the component owns its visible composition.

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

Start with the learner's concrete question: **What is a custom Hook**. Look at **What is a custom Hook** in the example before learning the technical name. For **What is a custom Hook**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is a custom Hook**, say what goes in and what comes out.

### Which logic belongs in a Hook?

Study **Which logic belongs in a Hook** by looking at the value, operation, and result in the worked example. For **Which logic belongs in a Hook**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Which logic belongs in a Hook**, say what goes in and what comes out.

### Why must Hook names begin with use?

Answer **Why must Hook names begin with use** by comparing the working example with a broken or limited example. For **Why must Hook names begin with use**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why must Hook names begin with use?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### How do we design a small return API?

To answer **How do we design a small return API**, follow the operation in order and check the example. For **How do we design a small return API**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we design a small return API**, change one input in the example. Write the old result and the new result for **How do we design a small return API**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will identify repeated behavior, extract a custom Hook, enforce the Rules of Hooks, and design a small return API.

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

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the Hook owns reusable behavior while the component owns its visible composition.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `function useToggle(initial = false) {` — Defines a function or component that can be used later. |
| 2 | `const [value, setValue] = useState(initial);` — Gets the current value and a function that asks React for a new value. |
| 3 | `return [value, () => setValue((v) => !v)];` — Sends a value or UI tree back to the code that called this function. |
| 4 | `}` — Runs as part of this example. After `}`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: Several components need the same stateful behavior, but copying the behavior creates inconsistent fixes and unclear APIs.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Custom Hooks**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Call a Hook inside an if statement and move it to the component's top level.

Make the broken version in a copy. The likely mistake is: Call a Hook conditionally or hide unrelated responsibilities in a Hook with an unclear contract.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **custom hooks** and a local toggle, data viewer, or form behavior with a named Hook API.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local toggle, data viewer, or form behavior with a named Hook API.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the Hook owns reusable behavior while the component owns its visible composition.

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
10. Use this behavior in a small a local toggle, data viewer, or form behavior with a named Hook API with invented data.
11. Answer: what starts the outside work, and what stops it?
12. Write two things this local example does not prove about a real application.

## Finish line

You are finished when you can:

1. explain **Custom Hooks** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **the Hook owns reusable behavior while the component owns its visible composition**.

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
