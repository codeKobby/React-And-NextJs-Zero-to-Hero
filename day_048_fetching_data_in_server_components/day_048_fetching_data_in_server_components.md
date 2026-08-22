# Day 048: Fetching data in Server Components

[← Previous lesson](../day_047_server_only_and_client_only_boundaries/day_047_server_only_and_client_only_boundaries.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_049_caching_and_revalidation/day_049_caching_and_revalidation.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [Where should a database query run?](#where-should-a-database-query-run)
  - [How do we validate identity and permission?](#how-do-we-validate-identity-and-permission)
  - [Why can a Server Component access secrets?](#why-can-a-server-component-access-secrets)
  - [What does the browser receive?](#what-does-the-browser-receive)
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

Today’s steps are simple: We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: A page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate.

A complete page is like a room with labeled areas: the labels help people find and change one responsibility without opening the whole building.

Today we will learn **Fetching data in Server Components** in small steps. We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **JavaScript functions, JSX, and the local React playground**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Fetching data in Server Components** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **fetching data in server components** in a local case dashboard built from a shell, summary, list, and card.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the parent-to-child data flow and the responsibility owned by each component.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `fetch` | The browser or server API for making an HTTP request and awaiting its response. |
| `ORM` | An object-relational mapper that represents database tables and queries through application-level APIs. |
| `async component` | A component function that can await server-side work before returning its UI. |
| `request` | An incoming HTTP message containing a method, URL, headers, cookies, and possibly a body. |
| `authentication` | Establishing who an actor is, usually through a provider or session. |
| `authorization` | Deciding whether an identified actor may perform a requested action or access a record. |

## Topics

### Where should a database query run?

Study **Where should a database query run** by looking at the value, operation, and result in the worked example. For **Where should a database query run**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Where should a database query run**, say what goes in and what comes out.

### How do we validate identity and permission?

To answer **How do we validate identity and permission**, follow the operation in order and check the example. For **How do we validate identity and permission**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we validate identity and permission**, change one input in the example. Write the old result and the new result for **How do we validate identity and permission**.

### Why can a Server Component access secrets?

Answer **Why can a Server Component access secrets** by comparing the working example with a broken or limited example. For **Why can a Server Component access secrets**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why can a Server Component access secrets?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### What does the browser receive?

Start with the learner's concrete question: **What does the browser receive**. Look at **What does the browser receive** in the example before learning the technical name. For **What does the browser receive**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What does the browser receive**, say what goes in and what comes out.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard.

```tsx
export default async function Page() {
  const posts = await getPosts();
  return <PostList posts={posts} />;
}
```

**Expected result or visible behavior:**

```text
The page receives server-fetched data without exposing the query client.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the parent-to-child data flow and the responsibility owned by each component.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `export default async function Page() {` — Makes this value available to another file. |
| 2 | `const posts = await getPosts();` — Waits for the async task to finish before continuing. |
| 3 | `return <PostList posts={posts} />;` — Sends a value or UI tree back to the code that called this function. |
| 4 | `}` — Runs as part of this example. After `}`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Fetching data in Server Components**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Fetch private data without authorization and add the missing policy check.

Make the broken version in a copy. The likely mistake is: Split every element mechanically or use a lowercase component name that JSX treats as a browser element.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **fetching data in server components** and a local case dashboard built from a shell, summary, list, and card.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local case dashboard built from a shell, summary, list, and card.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the parent-to-child data flow and the responsibility owned by each component.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Run the page unchanged. Write down the three parts you can see.
2. Write a `Header` component and move the heading into it.
3. Write one sentence: what does the `Header` component do?
4. Pass a `title` prop to a component and display two different titles.
5. Put a parent component and two child components on the page.
6. Change a component name to lowercase. Read the error or wrong result.
7. Change the name back to a capital letter and run the page again.
8. Show a clear message when the list has no items.
9. Add a real heading, button, or link that a keyboard user can use.
10. Write one check that fails if the component’s visible text disappears.
11. Build a small a local case dashboard built from a shell, summary, list, and card with the components from this lesson.
12. Answer: which component owns each piece of data? Use one short sentence per piece.

## Finish line

You are finished when you can:

1. explain **Fetching data in Server Components** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **the parent-to-child data flow and the responsibility owned by each component**.

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
