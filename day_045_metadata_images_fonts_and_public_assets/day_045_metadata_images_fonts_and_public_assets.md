# Day 045: Metadata, images, fonts, and public assets

[← Previous lesson](../day_044_loading_error_and_not_found_ui/day_044_loading_error_and_not_found_ui.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_046_server_and_client_components/day_046_server_and_client_components.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [Where does page metadata live?](#where-does-page-metadata-live)
  - [Why use next/image?](#why-use-next-image)
  - [What belongs in public?](#what-belongs-in-public)
  - [How do alt text and font loading affect quality?](#how-do-alt-text-and-font-loading-affect-quality)
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

Here is the problem: The learner needs to see what metadata, images, fonts, and public assets does before learning its name.

A small workshop task lets the learner change one thing and see the result.

Today we will learn **Metadata, images, fonts, and public assets** in small steps. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Metadata, images, fonts, and public assets** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **metadata, images, fonts, and public assets** in a small local example.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line or file that changes the result.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `metadata` | Information about a page, such as its title, description, or social preview fields. |
| `generateMetadata` | A Next.js function that computes route metadata from its inputs, often including dynamic params. |
| `Image` | The Next.js image component or an image asset that needs dimensions, loading, and alternative text decisions. |
| `font` | A typeface resource whose loading, fallback, and display choices affect readability and performance. |
| `public` | A route, asset, value, or boundary intentionally available without a private server check. |
| `alt text` | Text that communicates the purpose or content of an image when it cannot be perceived. |

## Topics

### Where does page metadata live?

Study **Where does page metadata live** by looking at the value, operation, and result in the worked example. For **Where does page metadata live**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Where does page metadata live**, say what goes in and what comes out.

### Why use next/image?

Answer **Why use next/image** by comparing the working example with a broken or limited example. For **Why use next/image**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why use next/image?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### What belongs in public?

Start with the learner's concrete question: **What belongs in public**. Look at **What belongs in public** in the example before learning the technical name. For **What belongs in public**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What belongs in public**, say what goes in and what comes out.

### How do alt text and font loading affect quality?

To answer **How do alt text and font loading affect quality**, follow the operation in order rather than treating the result as framework magic. For **How do alt text and font loading affect quality**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do alt text and font loading affect quality**, change one input in the example. Write the old result and the new result for **How do alt text and font loading affect quality**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.

```tsx
export const metadata = { title: 'Dashboard' };
<Image src="/avatar.png" alt="Profile" width={48} height={48} />
```

**Expected result or visible behavior:**

```text
The page has metadata and a described image.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line or file that changes the result.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `export const metadata = { title: 'Dashboard' };` — Makes this value available to another file. |
| 2 | `<Image src="/avatar.png" alt="Profile" width={48} height={48} />` — Creates a piece of the UI or explains the code in a comment. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: The learner needs to see what metadata, images, fonts, and public assets does before learning its name.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Metadata, images, fonts, and public assets**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Use an image without alt text or dimensions and repair the accessibility/performance issues.

Make the broken version in a copy. The likely mistake is: Copy the code without checking the input and the result.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **metadata, images, fonts, and public assets** and a small local example.

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

1. explain **Metadata, images, fonts, and public assets** to another beginner;
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
