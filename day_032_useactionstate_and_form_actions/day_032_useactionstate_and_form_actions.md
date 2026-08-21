# Day 032: useActionState and form actions

[← Previous lesson](../day_031_react_19_actions/day_031_react_19_actions.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_033_useformstatus_and_useoptimistic/day_033_useformstatus_and_useoptimistic.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does useActionState return?](#what-does-useactionstate-return)
  - [How does a form action receive FormData?](#how-does-a-form-action-receive-formdata)
  - [Where should validation happen?](#where-should-validation-happen)
  - [How do we show field errors?](#how-do-we-show-field-errors)
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

Here is the problem: The learner needs to see what useactionstate and form actions does before learning its name.

A small workshop task lets the learner change one thing and see the result.

Today we will learn **useActionState and form actions** in small steps. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **useActionState and form actions** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **useactionstate and form actions** in a small local example.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line or file that changes the result.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `useActionState` | A React Hook that connects an Action to state representing its pending and returned result. |
| `form action` | The function or URL associated with a form's submit operation. |
| `previous state` | The state value from which a functional updater computes a next value. |
| `FormData` | A browser object that collects named form controls and their submitted values. |
| `pending` | A period in which an operation has been requested but has not settled yet. |

## Topics

### What does useActionState return?

Start with the learner's concrete question: **What does useActionState return**. Look at **What does useActionState return** in the example before learning the technical name. For **What does useActionState return**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What does useActionState return**, say what goes in and what comes out.

### How does a form action receive FormData?

To answer **How does a form action receive FormData**, follow the operation in order rather than treating the result as framework magic. For **How does a form action receive FormData**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How does a form action receive FormData**, change one input in the example. Write the old result and the new result for **How does a form action receive FormData**.

### Where should validation happen?

Study **Where should validation happen** by looking at the value, operation, and result in the worked example. For **Where should validation happen**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Where should validation happen**, say what goes in and what comes out.

### How do we show field errors?

To answer **How do we show field errors**, follow the operation in order rather than treating the result as framework magic. For **How do we show field errors**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we show field errors**, change one input in the example. Write the old result and the new result for **How do we show field errors**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.

```tsx
const [state, action, pending] = useActionState(save, initialState);
```

**Expected result or visible behavior:**

```text
The form displays state and pending information.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line or file that changes the result.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const [state, action, pending] = useActionState(save, initialState);` — Stores the value on the right under the name on the left. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: The learner needs to see what useactionstate and form actions does before learning its name.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **useActionState and form actions**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Read formData.get without checking its type and repair the validation boundary.

Make the broken version in a copy. The likely mistake is: Copy the code without checking the input and the result.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **useactionstate and form actions** and a small local example.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a small local example.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the line or file that changes the result.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Run the example. Write down the number or message shown before clicking anything.
2. Click the button once, then twice. Write down the number after each click.
3. Change the starting value. Predict the first number before you run the page.
4. Add a `Reset` button. When clicked, it must show `0` or the lesson’s starting value.
5. Make the beginner mistake shown in the lesson. Write down what goes wrong.
6. Fix the mistake and run the normal example again.
7. Answer: which component stores the changing value? Point to the line where it is created.
8. Add a message that tells the user how many items are in the list.
9. Write one test for the normal case and one test for an empty list.
10. Build a small a small local example using this lesson’s state pattern.
11. Answer: what should the user see while the list is empty?
12. Write three sentences explaining the value, the button, and the screen update.

## Finish line

You are finished when you can:

1. explain **useActionState and form actions** to another beginner;
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
