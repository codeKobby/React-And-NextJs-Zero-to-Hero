# Day 026: Suspense and the use API

[← Previous lesson](../day_025_transitions_and_responsive_updates/day_025_transitions_and_responsive_updates.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_027_function_components_versus_class_components/day_027_function_components_versus_class_components.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does Suspense coordinate?](#what-does-suspense-coordinate)
  - [What is a fallback?](#what-is-a-fallback)
  - [How does use read a promise?](#how-does-use-read-a-promise)
  - [Where should a boundary live?](#where-should-a-boundary-live)
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

The learner problem comes first: Sometimes a browser, test, webhook, or other client needs a documented HTTP boundary rather than a component-only interaction. A service counter has a public request format, a response receipt, and a deliberate way to say no. This lesson teaches **Suspense and the use API** through a connected sequence rather than a finished file dropped from the sky: We will read a Request, validate its body, return success and failure status codes, and test the public response contract. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **async JavaScript, JSON, validation, and Next.js route files**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **suspense and the use api** to a local synthetic Route Handler with typed success and error JSON. You should be able to name the owner and boundary—public HTTP contract versus private data-access and authorization decisions—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `Suspense` | A React boundary that coordinates fallback UI while a child is not ready to render. |
| `fallback` | UI shown while the intended content is unavailable, loading, or failed. |
| `promise` | A JavaScript object representing a value that may become available or fail later. |
| `use` | A React API for reading certain resources or context values within supported render boundaries. |
| `streaming` | Sending ready parts of a response while slower parts continue instead of waiting for the whole tree. |
| `boundary` | A point where responsibility, data, rendering, or authority changes hands. |

## Topics

### What does Suspense coordinate?

Start with the learner's concrete question: **What does Suspense coordinate**. Use the worked example to show what **What does Suspense coordinate** changes before introducing a framework shortcut. For **What does Suspense coordinate**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What does Suspense coordinate**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What does Suspense coordinate?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### What is a fallback?

Start with the learner's concrete question: **What is a fallback**. Use the worked example to show what **What is a fallback** changes before introducing a framework shortcut. For **What is a fallback**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is a fallback**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is a fallback?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How does use read a promise?

To answer **How does use read a promise**, follow the operation in order rather than treating the result as framework magic. For **How does use read a promise**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How does use read a promise**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How does use read a promise?**, change one input or boundary in the worked example. Trace the result for **How does use read a promise?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### Where should a boundary live?

Study **Where should a boundary live** by naming the concrete value, operation, visible result, and owner in the worked example. For **Where should a boundary live**, underline the line or file where this idea becomes observable and explain what would change it. Keep the conclusion limited to the local evidence for **Where should a boundary live**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Where should a boundary live?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will read a Request, validate its body, return success and failure status codes, and test the public response contract.

```tsx
<Suspense fallback={<p>Loading…</p>}><Comments promise={comments} /></Suspense>
```

**Expected result or visible behavior:**

```text
A loading fallback appears until data is ready.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is public HTTP contract versus private data-access and authorization decisions.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `<Suspense fallback={<p>Loading…</p>}><Comments promise={comments} /></Suspense>` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Sometimes a browser, test, webhook, or other client needs a documented HTTP boundary rather than a component-only interaction.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will read a Request, validate its body, return success and failure status codes, and test the public response contract.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Suspense and the use API**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Remove the boundary around a suspending component and repair the missing fallback.

Run the broken version in a local copy. The likely beginner mistake for this family is: Return 200 for invalid input, leak stack traces, or confuse an internal function result with an HTTP response. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **suspense and the use api** to a local synthetic Route Handler with typed success and error JSON. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local synthetic Route Handler with typed success and error JSON using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is public HTTP contract versus private data-access and authorization decisions. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Define **What does Suspense coordinate?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **What is a fallback?**, then predict before running.
5. Create a boundary case involving **How does use read a promise?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Remove the boundary around a suspending component and repair the missing fallback.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply suspense and the use api to a local synthetic Route Handler with typed success and error JSON with a local synthetic fixture.
11. Explain the owner and boundary: public HTTP contract versus private data-access and authorization decisions.
12. Write a review note with evidence, one limitation, and the next learning step.

## Finish line

You are finished when you can teach **Suspense and the use API** to another beginner, show the normal and broken runs, explain the repair, and point to **public HTTP contract versus private data-access and authorization decisions**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
