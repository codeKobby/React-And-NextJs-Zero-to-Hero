# Day 034: Metadata, refs, and modern React DOM

[← Previous lesson](../day_033_useformstatus_and_useoptimistic/day_033_useformstatus_and_useoptimistic.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_035_react_architecture_and_accessibility/day_035_react_architecture_and_accessibility.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [How does React render metadata?](#how-does-react-render-metadata)
  - [What changed for ref props?](#what-changed-for-ref-props)
  - [What is ref cleanup?](#what-is-ref-cleanup)
  - [How do DOM resources fit a component?](#how-do-dom-resources-fit-a-component)
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

Here is the problem: The learner needs to see what metadata, refs, and modern react dom does before learning its name.

A small workshop task lets the learner change one thing and see the result.

Today we will learn **Metadata, refs, and modern React DOM** in small steps. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Metadata, refs, and modern React DOM** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **metadata, refs, and modern react dom** in a small local example.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line or file that changes the result.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `metadata` | Information about a page, such as its title, description, or social preview fields. |
| `title` | The human-readable name or page metadata that identifies a case, resource, or document. |
| `meta` | Short metadata describing a page, asset, or data object for a consumer or tool. |
| `ref prop` | A React 19-compatible prop boundary through which a ref can be passed without a wrapper pattern. |
| `ref cleanup` | The cleanup that releases a ref-created resource or disconnects a DOM relationship. |
| `stylesheet` | A CSS resource containing rules that control the presentation of rendered elements. |

## Topics

### How does React render metadata?

To answer **How does React render metadata**, follow the operation in order and check the example. For **How does React render metadata**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How does React render metadata**, change one input in the example. Write the old result and the new result for **How does React render metadata**.

### What changed for ref props?

Start with the learner's concrete question: **What changed for ref props**. Look at **What changed for ref props** in the example before learning the technical name. For **What changed for ref props**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What changed for ref props**, say what goes in and what comes out.

### What is ref cleanup?

Start with the learner's concrete question: **What is ref cleanup**. Look at **What is ref cleanup** in the example before learning the technical name. For **What is ref cleanup**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is ref cleanup**, say what goes in and what comes out.

### How do DOM resources fit a component?

To answer **How do DOM resources fit a component**, follow the operation in order and check the example. For **How do DOM resources fit a component**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do DOM resources fit a component**, change one input in the example. Write the old result and the new result for **How do DOM resources fit a component**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.

```tsx
return <><title>{title}</title><input ref={inputRef} /></>;
```

**Expected result or visible behavior:**

```text
The document title and input ref are managed declaratively.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line or file that changes the result.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `return <><title>{title}</title><input ref={inputRef} /></>;` — Sends a value or UI tree back to the code that called this function. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: The learner needs to see what metadata, refs, and modern react dom does before learning its name.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Metadata, refs, and modern React DOM**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Return an element from a ref callback and repair the cleanup ambiguity.

Make the broken version in a copy. The likely mistake is: Copy the code without checking the input and the result.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **metadata, refs, and modern react dom** and a small local example.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a small local example.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the line or file that changes the result.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Run the local database example. Write down the rows it returns.
2. Draw the tables and write one sentence about what each ID means.
3. Change one field or filter. Predict the new row before you run the query.
4. Show what the page displays when no row is found.
5. Make the missing-migration, raw-row, or wrong-user mistake from the lesson.
6. Fix the mistake and run the normal and rejected cases again.
7. Answer: which file talks to the database, and which file shows the page?
8. Add one transaction or rollback example if the lesson teaches it.
9. Write one test for the query’s normal result and one test for no result.
10. Build a small a small local example with resettable invented records.
11. Answer: how does the server stop one user from seeing another user’s record?
12. Write the migration command, query result, and one thing you did not test.

## Finish line

You are finished when you can:

1. explain **Metadata, refs, and modern React DOM** to another beginner;
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
