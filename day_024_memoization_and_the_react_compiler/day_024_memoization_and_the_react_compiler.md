# Day 024: Memoization and the React Compiler

[← Previous lesson](../day_023_custom_hooks/day_023_custom_hooks.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_025_transitions_and_responsive_updates/day_025_transitions_and_responsive_updates.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is memoization?](#what-is-memoization)
  - [When can memoization help?](#when-can-memoization-help)
  - [Why can premature memoization hurt clarity?](#why-can-premature-memoization-hurt-clarity)
  - [How does the React Compiler change the decision?](#how-does-the-react-compiler-change-the-decision)
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

Today’s steps are simple: We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: The learner needs to see what memoization and the react compiler does before learning its name.

A small workshop task lets the learner change one thing and see the result.

Today we will learn **Memoization and the React Compiler** in small steps. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Memoization and the React Compiler** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **memoization and the react compiler** in a small local example.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line or file that changes the result.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `memoization` | Reusing a previous calculation or rendered result when its relevant inputs have not changed. |
| `memo` | A React optimization that can skip a component render when its props compare equal; it is not a correctness fix. |
| `useMemo` | A Hook that can reuse a calculation while its dependencies remain unchanged; it does not make stale data correct. |
| `useCallback` | A Hook that can preserve a function identity while its dependencies remain unchanged. |
| `compiler` | A tool that transforms or checks source code before a runtime executes it. |
| `purity` | The property of producing the same result from the same inputs without external mutation or side effects. |

## Topics

### What is memoization?

Start with the learner's concrete question: **What is memoization**. Look at **What is memoization** in the example before learning the technical name. For **What is memoization**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is memoization**, say what goes in and what comes out.

### When can memoization help?

Treat **When can memoization help** as a simple choice. Start with a normal example and then try an empty or bad example. For **When can memoization help**, write what the program should do in both examples.

**Try it before moving on:** For **When can memoization help?**, write one normal example and one empty or bad example. Say what each should do.

### Why can premature memoization hurt clarity?

Answer **Why can premature memoization hurt clarity** by comparing the working example with a broken or limited example. For **Why can premature memoization hurt clarity**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why can premature memoization hurt clarity?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### How does the React Compiler change the decision?

To answer **How does the React Compiler change the decision**, follow the operation in order and check the example. For **How does the React Compiler change the decision**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How does the React Compiler change the decision**, change one input in the example. Write the old result and the new result for **How does the React Compiler change the decision**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.

```tsx
const total = useMemo(() => calculateTotal(items), [items]);
```

**Expected result or visible behavior:**

```text
The calculation is reused for the same items reference.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line or file that changes the result.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const total = useMemo(() => calculateTotal(items), [items]);` — Defines a function or component that can be used later. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: The learner needs to see what memoization and the react compiler does before learning its name.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Memoization and the React Compiler**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Memoize every value, then remove the unnecessary memo and explain the simpler code.

Make the broken version in a copy. The likely mistake is: Copy the code without checking the input and the result.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **memoization and the react compiler** and a small local example.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a small local example.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the line or file that changes the result.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Answer the question **What is memoization?** in one sentence. Point to the example that helped you.
2. Run the example unchanged. Write down what appears.
3. Change one value. Predict the result, then run the code and compare.
4. Change one input in the example for **When can memoization help?**. Write down the old and new result.
5. Use an empty list, empty string, or missing value that fits **Why can premature memoization hurt clarity?**. Say what should happen.
6. Make the mistake shown in the lesson: Memoize every value, then remove the unnecessary memo and explain the simpler code.
7. Fix the mistake and run the normal example again.
8. Show the main result in the format this lesson uses: text, number, UI, or error message.
9. Write one check that fails when the important visible result disappears.
10. Build the small example from this lesson in the starter.
11. Answer: which file or function contains the important code? Give one simple reason.
12. Write four short sentences: what you built, what you saw, what you fixed, and what you did not test.

## Finish line

You are finished when you can:

1. explain **Memoization and the React Compiler** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **the line or file that changes the result**.

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
