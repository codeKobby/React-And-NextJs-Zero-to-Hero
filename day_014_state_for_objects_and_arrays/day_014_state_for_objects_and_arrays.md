# Day 014: State for objects and arrays

[← Previous lesson](../day_013_usestate_and_setters/day_013_usestate_and_setters.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_015_derived_state_and_the_single_source_of_truth/day_015_derived_state_and_the_single_source_of_truth.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [Why should state updates create new references?](#why-should-state-updates-create-new-references)
  - [How do we update one object field?](#how-do-we-update-one-object-field)
  - [How do we add and remove array items?](#how-do-we-add-and-remove-array-items)
  - [What is accidental mutation?](#what-is-accidental-mutation)
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

Here is the problem: The learner needs to see what state for objects and arrays does before learning its name.

A small workshop task lets the learner change one thing and see the result.

Today we will learn **State for objects and arrays** in small steps. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **State for objects and arrays** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **state for objects and arrays** in a small local example.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line or file that changes the result.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `immutability` | Updating by creating a new value instead of changing the existing value in place. |
| `object spread` | Syntax that copies enumerable object properties into a new object, often used for immutable state updates. |
| `array spread` | Syntax that copies array items into a new array, often used to make an immutable update. |
| `update` | A request to move state, data, or configuration from its current value to a next value. |
| `reference` | A pointer or identity that lets code reach an object, DOM node, resource, or source document. |

## Topics

### Why should state updates create new references?

Answer **Why should state updates create new references** by comparing the working example with a broken or limited example. For **Why should state updates create new references**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why should state updates create new references?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### How do we update one object field?

To answer **How do we update one object field**, follow the operation in order and check the example. For **How do we update one object field**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we update one object field**, change one input in the example. Write the old result and the new result for **How do we update one object field**.

### How do we add and remove array items?

To answer **How do we add and remove array items**, follow the operation in order and check the example. For **How do we add and remove array items**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we add and remove array items**, change one input in the example. Write the old result and the new result for **How do we add and remove array items**.

### What is accidental mutation?

Start with the learner's concrete question: **What is accidental mutation**. Look at **What is accidental mutation** in the example before learning the technical name. For **What is accidental mutation**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is accidental mutation**, say what goes in and what comes out.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.

```tsx
setUser((user) => ({ ...user, name: 'Ada' }));
setItems((items) => [...items, newItem]);
```

**Expected result or visible behavior:**

```text
A new state reference is created.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line or file that changes the result.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `setUser((user) => ({ ...user, name: 'Ada' }));` — Defines a function or component that can be used later. |
| 2 | `setItems((items) => [...items, newItem]);` — Defines a function or component that can be used later. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: The learner needs to see what state for objects and arrays does before learning its name.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **State for objects and arrays**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Call user.name = ... directly and repair it with an immutable update.

Make the broken version in a copy. The likely mistake is: Copy the code without checking the input and the result.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **state for objects and arrays** and a small local example.

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

1. explain **State for objects and arrays** to another beginner;
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
