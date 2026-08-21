# Day 052: Route Handlers and HTTP APIs

[← Previous lesson](../day_051_forms_and_server_actions/day_051_forms_and_server_actions.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_053_authentication_and_authorization_boundaries/day_053_authentication_and_authorization_boundaries.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a Route Handler?](#what-is-a-route-handler)
  - [When do we need an HTTP endpoint?](#when-do-we-need-an-http-endpoint)
  - [How do we validate a request?](#how-do-we-validate-a-request)
  - [How should status and errors be shaped?](#how-should-status-and-errors-be-shaped)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will read a Request, validate its body, return success and failure status codes, and test the public response contract. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: Sometimes a browser, test, webhook, or other client needs a documented HTTP boundary rather than a component-only interaction. A service counter has a public request format, a response receipt, and a deliberate way to say no. This lesson teaches **Route Handlers and HTTP APIs** through a connected sequence rather than a finished file dropped from the sky: We will read a Request, validate its body, return success and failure status codes, and test the public response contract. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **async JavaScript, JSON, validation, and Next.js route files**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **route handlers and http apis** to a local synthetic Route Handler with typed success and error JSON. You should be able to name the owner and boundary—public HTTP contract versus private data-access and authorization decisions—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `route.ts` | A Next.js special file that defines HTTP method handlers for a route endpoint. |
| `GET` | The HTTP method commonly used to request a representation of data without asking the server to create or change it. |
| `POST` | The HTTP method commonly used to submit data or request a server-side creation or action. |
| `Request` | An incoming HTTP message containing a method, URL, headers, cookies, and possibly a body. |
| `Response` | The HTTP result returned to a caller, including status, headers, and optional body data. |
| `status` | A named condition such as idle, loading, success, empty, or error that guides visible behavior. |
| `headers` | Metadata sent with an HTTP request or response, such as content type, cache policy, or tracing IDs. |

## Topics

### What is a Route Handler?

Start with the learner's concrete question: **What is a Route Handler**. Use the worked example to show what **What is a Route Handler** changes before introducing a framework shortcut. For **What is a Route Handler**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is a Route Handler**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is a Route Handler?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### When do we need an HTTP endpoint?

Treat **When do we need an HTTP endpoint** as a decision with a normal case, a boundary case, and a cost when chosen carelessly. For **When do we need an HTTP endpoint**, write one rule that accepts the normal case and one rule that handles the boundary safely. Keep the conclusion limited to the local evidence for **When do we need an HTTP endpoint**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **When do we need an HTTP endpoint?**, write a decision rule with one normal case and one boundary case. Include what would make the other option preferable.

### How do we validate a request?

To answer **How do we validate a request**, follow the operation in order rather than treating the result as framework magic. For **How do we validate a request**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we validate a request**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we validate a request?**, change one input or boundary in the worked example. Trace the result for **How do we validate a request?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### How should status and errors be shaped?

To answer **How should status and errors be shaped**, follow the operation in order rather than treating the result as framework magic. For **How should status and errors be shaped**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How should status and errors be shaped**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How should status and errors be shaped?**, change one input or boundary in the worked example. Trace the result for **How should status and errors be shaped?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will read a Request, validate its body, return success and failure status codes, and test the public response contract.

```tsx
export async function GET() {
  return Response.json({ ok: true });
}
```

**Expected result or visible behavior:**

```text
The endpoint returns a deliberate JSON response.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is public HTTP contract versus private data-access and authorization decisions.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `export async function GET() {` — Makes this binding available to another module; the export is part of this lesson's public boundary. |
| 2 | `return Response.json({ ok: true });` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |
| 3 | `}` — Runs inside the current example; connect its effect to public HTTP contract versus private data-access and authorization decisions. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Sometimes a browser, test, webhook, or other client needs a documented HTTP boundary rather than a component-only interaction.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will read a Request, validate its body, return success and failure status codes, and test the public response contract.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Route Handlers and HTTP APIs**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Return 200 for invalid input and repair the status and error contract.

Run the broken version in a local copy. The likely beginner mistake for this family is: Return 200 for invalid input, leak stack traces, or confuse an internal function result with an HTTP response. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **route handlers and http apis** to a local synthetic Route Handler with typed success and error JSON. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local synthetic Route Handler with typed success and error JSON using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is public HTTP contract versus private data-access and authorization decisions. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the smallest route or structure fixture and write its URL and visible result.
2. Map each relevant folder or special file to the route or boundary it creates.
3. Change one segment or parameter and predict the URL before running it.
4. Add a normal, missing, loading, or not-found case appropriate to the route.
5. Reproduce the duplicate-router, missing-file, or parameter-timing mistake.
6. Repair the folder, file, or async boundary with the smallest change.
7. Explain which code is application source and which remains root configuration.
8. Add a semantic link, heading, or focus behavior to the route UI.
9. Add a route-level assertion or browser check for the public contract.
10. Apply the lesson to a local synthetic Route Handler with typed success and error JSON and document the route map.
11. Explain what crosses the public HTTP contract versus private data-access and authorization decisions and what must stay private.
12. Write a review note with the URL, file map, evidence, and one deployment limitation.

## Finish line

You are finished when you can teach **Route Handlers and HTTP APIs** to another beginner, show the normal and broken runs, explain the repair, and point to **public HTTP contract versus private data-access and authorization decisions**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
