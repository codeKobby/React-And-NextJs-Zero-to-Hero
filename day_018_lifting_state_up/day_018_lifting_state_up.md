# Day 018: Lifting state up

[← Previous lesson](../day_017_uncontrolled_inputs_and_refs/day_017_uncontrolled_inputs_and_refs.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_019_reducers_and_dispatch/day_019_reducers_and_dispatch.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [When should state move to a parent?](#when-should-state-move-to-a-parent)
  - [How do siblings share state?](#how-do-siblings-share-state)
  - [What belongs in the parent?](#what-belongs-in-the-parent)
  - [How do callbacks move intent upward?](#how-do-callbacks-move-intent-upward)
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

Here is the problem: The learner needs to see what lifting state up does before learning its name.

A small workshop task lets the learner change one thing and see the result.

Today we will learn **Lifting state up** in small steps. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Lifting state up** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **lifting state up** in a small local example.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line or file that changes the result.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `lifting state` | Moving shared state to the nearest common owner so multiple children can use one source of truth. |
| `shared state` | State that multiple components need to read or change through a common owner. |
| `parent` | A component or route that renders or owns a nested child boundary. |
| `callback` | A function handed to another system so it can invoke the behavior later. |
| `synchronization` | Keeping an external system aligned with the current React inputs after a render. |

## Topics

### When should state move to a parent?

Treat **When should state move to a parent** as a simple choice. Start with a normal example and then try an empty or bad example. For **When should state move to a parent**, write what the program should do in both examples.

**Try it before moving on:** For **When should state move to a parent?**, write one normal example and one empty or bad example. Say what each should do.

### How do siblings share state?

To answer **How do siblings share state**, follow the operation in order and check the example. For **How do siblings share state**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do siblings share state**, change one input in the example. Write the old result and the new result for **How do siblings share state**.

### What belongs in the parent?

Start with the learner's concrete question: **What belongs in the parent**. Look at **What belongs in the parent** in the example before learning the technical name. For **What belongs in the parent**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What belongs in the parent**, say what goes in and what comes out.

### How do callbacks move intent upward?

To answer **How do callbacks move intent upward**, follow the operation in order and check the example. For **How do callbacks move intent upward**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do callbacks move intent upward**, change one input in the example. Write the old result and the new result for **How do callbacks move intent upward**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.

```tsx
<Editor value={text} onChange={setText} />
<Preview value={text} />
```

**Expected result or visible behavior:**

```text
Both children show the same source.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line or file that changes the result.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `<Editor value={text} onChange={setText} />` — Tells the browser which function to run when the user performs this action. |
| 2 | `<Preview value={text} />` — Creates a piece of the UI or explains the code in a comment. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: The learner needs to see what lifting state up does before learning its name.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Lifting state up**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Give each sibling its own text state and repair the split-brain UI.

Make the broken version in a copy. The likely mistake is: Copy the code without checking the input and the result.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **lifting state up** and a small local example.

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

1. explain **Lifting state up** to another beginner;
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
