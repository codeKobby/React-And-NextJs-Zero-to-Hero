# Day 077: File uploads, metadata, and storage boundaries

[← Previous lesson](../day_076_authorization_roles_ownership_and_multi_tenant_data/day_076_authorization_roles_ownership_and_multi_tenant_data.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_078_error_taxonomy_logging_and_instrumentation/day_078_error_taxonomy_logging_and_instrumentation.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is an upload boundary?](#what-is-an-upload-boundary)
  - [Why validate size and type on the server?](#why-validate-size-and-type-on-the-server)
  - [Where should file bytes live?](#where-should-file-bytes-live)
  - [How should downloads be authorized?](#how-should-downloads-be-authorized)
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

Today’s steps are simple: We will bound size and type, record safe metadata, choose a storage boundary, and authorize a download. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: Files are larger and more ambiguous than ordinary text fields, and a filename is not a security policy.

A receiving dock weighs and labels a package before storing it; a name written on the box does not prove what is inside.

Today we will learn **File uploads, metadata, and storage boundaries** in small steps. We will bound size and type, record safe metadata, choose a storage boundary, and authorize a download. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **forms, validation, HTTP responses, and authorization**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **File uploads, metadata, and storage boundaries** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **file uploads, metadata, and storage boundaries** in a local synthetic upload validator and authorized download response.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: browser file input versus server validation, storage, and access policy.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `upload` | Sending a file or binary content from a user or system to an application or storage boundary. |
| `multipart` | An HTTP body encoding that can carry multiple fields and file parts in one form submission. |
| `MIME type` | A content-type label such as `image/png` that describes the format of uploaded or returned data. |
| `size limit` | A maximum allowed amount of data, such as upload bytes or request body size. |
| `object storage` | A service or boundary that stores files as objects addressed by keys rather than relational rows. |
| `metadata` | Information about a page, such as its title, description, or social preview fields. |
| `download` | Transferring a file or response from the application to a user's device or caller. |

## Topics

### What is an upload boundary?

Start with the learner's concrete question: **What is an upload boundary**. Look at **What is an upload boundary** in the example before learning the technical name. For **What is an upload boundary**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is an upload boundary**, say what goes in and what comes out.

### Why validate size and type on the server?

Answer **Why validate size and type on the server** by comparing the working example with a broken or limited example. For **Why validate size and type on the server**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why validate size and type on the server?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### Where should file bytes live?

Study **Where should file bytes live** by looking at the value, operation, and result in the worked example. For **Where should file bytes live**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Where should file bytes live**, say what goes in and what comes out.

### How should downloads be authorized?

To answer **How should downloads be authorized**, follow the operation in order and check the example. For **How should downloads be authorized**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How should downloads be authorized**, change one input in the example. Write the old result and the new result for **How should downloads be authorized**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will bound size and type, record safe metadata, choose a storage boundary, and authorize a download.

```tsx
const MAX_BYTES = 2_000_000;
if (file.size > MAX_BYTES || !ALLOWED_TYPES.has(file.type)) {
  return { error: 'Unsupported file' };
}
```

**Expected result or visible behavior:**

```text
Oversized or unsupported synthetic files are rejected before storage.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: browser file input versus server validation, storage, and access policy.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const MAX_BYTES = 2_000_000;` — Stores the value on the right under the name on the left. |
| 2 | `if (file.size > MAX_BYTES \|\| !ALLOWED_TYPES.has(file.type)) {` — Checks a condition and runs the next code only when the condition is true. |
| 3 | `return { error: 'Unsupported file' };` — Sends a value or UI tree back to the code that called this function. |
| 4 | `}` — Runs as part of this example. After `}`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: Files are larger and more ambiguous than ordinary text fields, and a filename is not a security policy.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **File uploads, metadata, and storage boundaries**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Trust the filename extension, accept unlimited bytes, and serve a file without checking ownership, then repair all three boundaries.

Make the broken version in a copy. The likely mistake is: Trust extensions, accept unlimited bytes, or serve a stored object without checking ownership.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **file uploads, metadata, and storage boundaries** and a local synthetic upload validator and authorized download response.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local synthetic upload validator and authorized download response.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is browser file input versus server validation, storage, and access policy.

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
10. Build a small a local synthetic upload validator and authorized download response with resettable invented records.
11. Answer: how does the server stop one user from seeing another user’s record?
12. Write the migration command, query result, and one thing you did not test.

## Finish line

You are finished when you can:

1. explain **File uploads, metadata, and storage boundaries** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **browser file input versus server validation, storage, and access policy**.

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
