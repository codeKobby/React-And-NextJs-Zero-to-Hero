# Day 033: useFormStatus and useOptimistic

[← Previous lesson](../day_032_useactionstate_and_form_actions/day_032_useactionstate_and_form_actions.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_034_metadata_refs_and_modern_react_dom/day_034_metadata_refs_and_modern_react_dom.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [How can a child button know a form is pending?](#how-can-a-child-button-know-a-form-is-pending)
  - [What is an optimistic update?](#what-is-an-optimistic-update)
  - [When must optimistic UI roll back?](#when-must-optimistic-ui-roll-back)
  - [How do we communicate uncertainty?](#how-do-we-communicate-uncertainty)
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

Here is the problem: The learner needs to see what useformstatus and useoptimistic does before learning its name.

A small workshop task lets the learner change one thing and see the result.

Today we will learn **useFormStatus and useOptimistic** in small steps. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **useFormStatus and useOptimistic** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **useformstatus and useoptimistic** in a small local example.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line or file that changes the result.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `useFormStatus` | A Hook that reads pending form submission status from a descendant form boundary. |
| `pending` | A period in which an operation has been requested but has not settled yet. |
| `optimistic update` | Showing an expected result before the server confirms it, with a plan for failure or rollback. |
| `rollback` | A planned way to return a deployment, migration, or change to a known working state. |
| `status` | A named condition such as idle, loading, success, empty, or error that guides visible behavior. |

## Topics

### How can a child button know a form is pending?

To answer **How can a child button know a form is pending**, follow the operation in order rather than treating the result as framework magic. For **How can a child button know a form is pending**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How can a child button know a form is pending**, change one input in the example. Write the old result and the new result for **How can a child button know a form is pending**.

### What is an optimistic update?

Start with the learner's concrete question: **What is an optimistic update**. Look at **What is an optimistic update** in the example before learning the technical name. For **What is an optimistic update**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is an optimistic update**, say what goes in and what comes out.

### When must optimistic UI roll back?

Treat **When must optimistic UI roll back** as a simple choice. Start with a normal example and then try an empty or bad example. For **When must optimistic UI roll back**, write what the program should do in both examples.

**Try it before moving on:** For **When must optimistic UI roll back?**, write one normal example and one empty or bad example. Say what each should do.

### How do we communicate uncertainty?

To answer **How do we communicate uncertainty**, follow the operation in order rather than treating the result as framework magic. For **How do we communicate uncertainty**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we communicate uncertainty**, change one input in the example. Write the old result and the new result for **How do we communicate uncertainty**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.

```tsx
const { pending } = useFormStatus();
const [optimistic, addOptimistic] = useOptimistic(items);
```

**Expected result or visible behavior:**

```text
The button disables while the action runs.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line or file that changes the result.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const { pending } = useFormStatus();` — Stores the value on the right under the name on the left. |
| 2 | `const [optimistic, addOptimistic] = useOptimistic(items);` — Stores the value on the right under the name on the left. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: The learner needs to see what useformstatus and useoptimistic does before learning its name.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **useFormStatus and useOptimistic**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Show an optimistic success without handling failure and add a rollback explanation.

Make the broken version in a copy. The likely mistake is: Copy the code without checking the input and the result.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **useformstatus and useoptimistic** and a small local example.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a small local example.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the line or file that changes the result.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Answer the question **How can a child button know a form is pending?** in one sentence. Point to the example that helped you.
2. Run the example unchanged. Write down what appears.
3. Change one value. Predict the result, then run the code and compare.
4. Change one input in the example for **What is an optimistic update?**. Write down the old and new result.
5. Add one simple edge case for **When must optimistic UI roll back?**, such as an empty or invalid value.
6. Make the mistake shown in the lesson: Show an optimistic success without handling failure and add a rollback explanation.
7. Fix the mistake and run the normal example again.
8. Add one clear heading, label, error message, or type check that fits this lesson.
9. Write one check that fails when the important visible result disappears.
10. Build the small example from this lesson in the starter.
11. Answer: which file or function contains the important code? Give one simple reason.
12. Write four short sentences: what you built, what you saw, what you fixed, and what you did not test.

## Finish line

You are finished when you can:

1. explain **useFormStatus and useOptimistic** to another beginner;
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
