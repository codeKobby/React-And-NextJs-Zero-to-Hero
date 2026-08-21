# Day 039: Next.js installation and project structure

[← Previous lesson](../day_038_testing_linting_and_project_delivery/day_038_testing_linting_and_project_delivery.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_040_root_app_versus_src_app/day_040_root_app_versus_src_app.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does create-next-app configure?](#what-does-create-next-app-configure)
  - [What belongs at the root?](#what-belongs-at-the-root)
  - [What is the App Router?](#what-is-the-app-router)
  - [What does the src choice change?](#what-does-the-src-choice-change)
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

Today’s steps are simple: We will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: A new Next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous.

A workshop needs a clear separation between tools, storage, and workbenches; two rooms claiming to be the same entrance create confusion.

Today we will learn **Next.js installation and project structure** in small steps. We will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **React components, a terminal, Node.js, and the setup guide**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Next.js installation and project structure** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **next.js installation and project structure** in a small App Router starter whose source, configuration, and public assets have named homes.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: application source versus root configuration and the route files Next.js recognizes.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `create-next-app` | The official command-line starter that creates a Next.js project with selected options. |
| `App Router` | Next.js routing model where folders and special files define route segments and rendering boundaries. |
| `TypeScript` | A static type checker that catches many mismatches before JavaScript runs. |
| `ESLint` | A static analysis tool that reports code patterns which are incorrect, risky, or inconsistent with project rules. |
| `Tailwind` | A shorthand reference to Tailwind CSS utility classes and its design-token workflow. |
| `Turbopack` | A Next.js bundler and development engine that processes the module graph for fast feedback. |
| `src` | A conventional directory used to keep application source code separate from root configuration files. |

## Topics

### What does create-next-app configure?

Start with the learner's concrete question: **What does create-next-app configure**. Look at **What does create-next-app configure** in the example before learning the technical name. For **What does create-next-app configure**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What does create-next-app configure**, say what goes in and what comes out.

### What belongs at the root?

Start with the learner's concrete question: **What belongs at the root**. Look at **What belongs at the root** in the example before learning the technical name. For **What belongs at the root**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What belongs at the root**, say what goes in and what comes out.

### What is the App Router?

Start with the learner's concrete question: **What is the App Router**. Look at **What is the App Router** in the example before learning the technical name. For **What is the App Router**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is the App Router**, say what goes in and what comes out.

### What does the src choice change?

Start with the learner's concrete question: **What does the src choice change**. Look at **What does the src choice change** in the example before learning the technical name. For **What does the src choice change**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What does the src choice change**, say what goes in and what comes out.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout.

```tsx
src/app/page.tsx
src/app/layout.tsx
public/logo.svg
package.json
```

**Expected result or visible behavior:**

```text
The route code is separated from configuration.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: application source versus root configuration and the route files Next.js recognizes.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `src/app/page.tsx` — Runs as part of this example. After `src/app/page.tsx`, check the next line to see the result. |
| 2 | `src/app/layout.tsx` — Runs as part of this example. After `src/app/layout.tsx`, check the next line to see the result. |
| 3 | `public/logo.svg` — Runs as part of this example. After `public/logo.svg`, check the next line to see the result. |
| 4 | `package.json` — Runs as part of this example. After `package.json`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A new Next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Next.js installation and project structure**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Create both app/ and src/app/ and explain which one Next.js uses.

Make the broken version in a copy. The likely mistake is: Keep duplicate routers or treat generated configuration as magic that should never be inspected.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **next.js installation and project structure** and a small App Router starter whose source, configuration, and public assets have named homes.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a small App Router starter whose source, configuration, and public assets have named homes.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is application source versus root configuration and the route files Next.js recognizes.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Answer the question **What does create-next-app configure?** in one sentence. Point to the example that helped you.
2. Run the example unchanged. Write down what appears.
3. Change one value. Predict the result, then run the code and compare.
4. Change one input in the example for **What belongs at the root?**. Write down the old and new result.
5. Add one simple edge case for **What is the App Router?**, such as an empty or invalid value.
6. Make the mistake shown in the lesson: Create both app/ and src/app/ and explain which one Next.js uses.
7. Fix the mistake and run the normal example again.
8. Add one clear heading, label, error message, or type check that fits this lesson.
9. Write one check that fails when the important visible result disappears.
10. Build the small example from this lesson in the starter.
11. Answer: which file or function contains the important code? Give one simple reason.
12. Write four short sentences: what you built, what you saw, what you fixed, and what you did not test.

## Finish line

You are finished when you can:

1. explain **Next.js installation and project structure** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **application source versus root configuration and the route files Next.js recognizes**.

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
