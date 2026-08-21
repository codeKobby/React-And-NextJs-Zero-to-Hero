# Day 072: Route Handlers, API contracts, and typed errors

[← Previous lesson](../day_071_server_actions_for_validated_mutations/day_071_server_actions_for_validated_mutations.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_073_authentication_providers_and_identity_boundaries/day_073_authentication_providers_and_identity_boundaries.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [When should an app expose an HTTP endpoint?](#when-should-an-app-expose-an-http-endpoint)
  - [How do we shape a successful response?](#how-do-we-shape-a-successful-response)
  - [Which status represents invalid input?](#which-status-represents-invalid-input)
  - [How should clients handle typed errors?](#how-should-clients-handle-typed-errors)
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

Today’s steps are simple: We will read a Request, validate its body, return success and failure status codes, and test the public response contract. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: Sometimes a browser, test, webhook, or other client needs a documented HTTP boundary rather than a component-only interaction.

A service counter has a public request format, a response receipt, and a deliberate way to say no.

Today we will learn **Route Handlers, API contracts, and typed errors** in small steps. We will read a Request, validate its body, return success and failure status codes, and test the public response contract. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **async JavaScript, JSON, validation, and Next.js route files**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Route Handlers, API contracts, and typed errors** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **route handlers, api contracts, and typed errors** in a local synthetic Route Handler with typed success and error JSON.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: public HTTP contract versus private data-access and authorization decisions.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `Route Handler` | A Next.js server file that handles an HTTP method such as GET or POST. |
| `HTTP` | The request and response protocol used by browsers and web services. |
| `GET` | The HTTP method commonly used to request a representation of data without asking the server to create or change it. |
| `POST` | The HTTP method commonly used to submit data or request a server-side creation or action. |
| `Request` | An incoming HTTP message containing a method, URL, headers, cookies, and possibly a body. |
| `Response` | The HTTP result returned to a caller, including status, headers, and optional body data. |
| `status` | A named condition such as idle, loading, success, empty, or error that guides visible behavior. |
| `error contract` | A documented shape and meaning for how a boundary communicates failure. |

## Topics

### When should an app expose an HTTP endpoint?

Treat **When should an app expose an HTTP endpoint** as a simple choice. Start with a normal example and then try an empty or bad example. For **When should an app expose an HTTP endpoint**, write what the program should do in both examples.

**Try it before moving on:** For **When should an app expose an HTTP endpoint?**, write one normal example and one empty or bad example. Say what each should do.

### How do we shape a successful response?

To answer **How do we shape a successful response**, follow the operation in order rather than treating the result as framework magic. For **How do we shape a successful response**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we shape a successful response**, change one input in the example. Write the old result and the new result for **How do we shape a successful response**.

### Which status represents invalid input?

Study **Which status represents invalid input** by looking at the value, operation, and result in the worked example. For **Which status represents invalid input**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Which status represents invalid input**, say what goes in and what comes out.

### How should clients handle typed errors?

To answer **How should clients handle typed errors**, follow the operation in order rather than treating the result as framework magic. For **How should clients handle typed errors**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How should clients handle typed errors**, change one input in the example. Write the old result and the new result for **How should clients handle typed errors**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will read a Request, validate its body, return success and failure status codes, and test the public response contract.

```tsx
export async function POST(request: Request) {
  const body = await request.json();
  if (!body.title) return Response.json({ code: 'INVALID_TITLE' }, { status: 400 });
  return Response.json({ ok: true }, { status: 201 });
}
```

**Expected result or visible behavior:**

```text
Invalid input returns a deliberate 400 contract and valid creation returns 201.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: public HTTP contract versus private data-access and authorization decisions.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `export async function POST(request: Request) {` — Makes this value available to another file. |
| 2 | `const body = await request.json();` — Waits for the async task to finish before continuing. |
| 3 | `if (!body.title) return Response.json({ code: 'INVALID_TITLE' }, { status: 400 });` — Checks a condition and runs the next code only when the condition is true. |
| 4 | `return Response.json({ ok: true }, { status: 201 });` — Sends a value or UI tree back to the code that called this function. |
| 5 | `}` — Runs as part of this example. After `}`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: Sometimes a browser, test, webhook, or other client needs a documented HTTP boundary rather than a component-only interaction.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Route Handlers, API contracts, and typed errors**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Return 200 for malformed input and leak a stack trace, then repair the status and public error shape.

Make the broken version in a copy. The likely mistake is: Return 200 for invalid input, leak stack traces, or confuse an internal function result with an HTTP response.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **route handlers, api contracts, and typed errors** and a local synthetic Route Handler with typed success and error JSON.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local synthetic Route Handler with typed success and error JSON.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is public HTTP contract versus private data-access and authorization decisions.

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
10. Build a small a local synthetic Route Handler with typed success and error JSON and list its route URLs.
11. Answer: which data should stay on the server? Give one reason.
12. Write the file tree and one sentence about what you have not tested.

## Finish line

You are finished when you can:

1. explain **Route Handlers, API contracts, and typed errors** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **public HTTP contract versus private data-access and authorization decisions**.

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
