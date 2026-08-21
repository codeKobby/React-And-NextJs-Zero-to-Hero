# Day 042: Dynamic routes and typed params

[← Previous lesson](../day_041_layouts_pages_and_route_segments/day_041_layouts_pages_and_route_segments.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_043_route_groups_and_private_folders/day_043_route_groups_and_private_folders.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a dynamic segment?](#what-is-a-dynamic-segment)
  - [How do params arrive?](#how-do-params-arrive)
  - [When do we use searchParams?](#when-do-we-use-searchparams)
  - [What does catch-all mean?](#what-does-catch-all-mean)
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

Here is the problem: The learner needs to see what dynamic routes and typed params does before learning its name.

A small workshop task lets the learner change one thing and see the result.

Today we will learn **Dynamic routes and typed params** in small steps. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Dynamic routes and typed params** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **dynamic routes and typed params** in a small local example.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line or file that changes the result.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `dynamic segment` | A bracketed route folder whose name is filled from a URL segment at request or build time. |
| `params` | The dynamic route values extracted from a Next.js URL. |
| `slug` | A URL-safe identifier derived from a title or record name. |
| `catch-all` | A dynamic route segment that captures one or more remaining path segments. |
| `searchParams` | The decoded query-string values after the pathname in a URL. |

## Topics

### What is a dynamic segment?

Start with the learner's concrete question: **What is a dynamic segment**. Look at **What is a dynamic segment** in the example before learning the technical name. For **What is a dynamic segment**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is a dynamic segment**, say what goes in and what comes out.

### How do params arrive?

To answer **How do params arrive**, follow the operation in order rather than treating the result as framework magic. For **How do params arrive**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do params arrive**, change one input in the example. Write the old result and the new result for **How do params arrive**.

### When do we use searchParams?

Treat **When do we use searchParams** as a simple choice. Start with a normal example and then try an empty or bad example. For **When do we use searchParams**, write what the program should do in both examples.

**Try it before moving on:** For **When do we use searchParams?**, write one normal example and one empty or bad example. Say what each should do.

### What does catch-all mean?

Start with the learner's concrete question: **What does catch-all mean**. Look at **What does catch-all mean** in the example before learning the technical name. For **What does catch-all mean**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What does catch-all mean**, say what goes in and what comes out.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.

```tsx
app/blog/[slug]/page.tsx

export default async function Page({ params }) {
  const { slug } = await params;
  return <h1>{slug}</h1>;
}
```

**Expected result or visible behavior:**

```text
A URL slug becomes page data.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line or file that changes the result.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `app/blog/[slug]/page.tsx` — Runs as part of this example. After `app/blog/[slug]/page.tsx`, check the next line to see the result. |
| 2 | Blank line: it separates the surrounding ideas; it has no runtime operation. |
| 3 | `export default async function Page({ params }) {` — Makes this value available to another file. |
| 4 | `const { slug } = await params;` — Waits for the async task to finish before continuing. |
| 5 | `return <h1>{slug}</h1>;` — Sends a value or UI tree back to the code that called this function. |
| 6 | `}` — Runs as part of this example. After `}`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: The learner needs to see what dynamic routes and typed params does before learning its name.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Dynamic routes and typed params**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Read params synchronously in a current async page signature and repair the promise handling.

Make the broken version in a copy. The likely mistake is: Copy the code without checking the input and the result.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **dynamic routes and typed params** and a small local example.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a small local example.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the line or file that changes the result.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Run the route. Write down its URL and the text you see.
2. Write the job of each special file in one short sentence.
3. Change one folder or parameter. Predict the new URL before running it.
4. Add the missing, loading, or not-found message from the lesson.
5. Make the folder or file mistake shown in the lesson. Record the error.
6. Fix the mistake and open the route again.
7. Answer: which files are application code, and which files are project settings?
8. Add one real heading, link, or keyboard-friendly control to the page.
9. Write one browser check for the route’s visible text or URL.
10. Build a small a small local example and list its route URLs.
11. Answer: which data should stay on the server? Give one reason.
12. Write the file tree and one sentence about what you have not tested.

## Finish line

You are finished when you can:

1. explain **Dynamic routes and typed params** to another beginner;
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
