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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: Learners need a concrete reason to study dynamic routes and typed params before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. This lesson teaches **Dynamic routes and typed params** through a connected sequence rather than a finished file dropped from the sky: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **dynamic routes and typed params** to a small local fixture that demonstrates dynamic routes and typed params. You should be able to name the owner and boundary—the code or framework boundary that owns the decision in this lesson—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

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

Start with the learner's concrete question: **What is a dynamic segment**. The problem underneath this lesson is that learners need a concrete reason to study dynamic routes and typed params before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do params arrive?

To answer **How do params arrive**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that learners need a concrete reason to study dynamic routes and typed params before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

### When do we use searchParams?

Treat **When do we use searchParams** as a decision that has a normal case, a boundary case, and a cost when chosen carelessly. The problem underneath this lesson is that learners need a concrete reason to study dynamic routes and typed params before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Write a decision rule with one normal case and one boundary case. Include what would make the other option preferable.

### What does catch-all mean?

Start with the learner's concrete question: **What does catch-all mean**. The problem underneath this lesson is that learners need a concrete reason to study dynamic routes and typed params before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.

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

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the code or framework boundary that owns the decision in this lesson.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `app/blog/[slug]/page.tsx` — Runs inside the current example; connect its effect to the code or framework boundary that owns the decision in this lesson. |
| 2 | Blank line: it separates the surrounding ideas; it has no runtime operation. |
| 3 | `export default async function Page({ params }) {` — Makes this binding available to another module; the export is part of this lesson's public boundary. |
| 4 | `const { slug } = await params;` — Pauses this async operation until its promise settles; identify whether the work runs on the server and how failure is handled. |
| 5 | `return <h1>{slug}</h1>;` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |
| 6 | `}` — Runs inside the current example; connect its effect to the code or framework boundary that owns the decision in this lesson. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Learners need a concrete reason to study dynamic routes and typed params before the terminology becomes useful.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Dynamic routes and typed params**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Read params synchronously in a current async page signature and repair the promise handling.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy the syntax without identifying the input, owner, output, and boundary. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **dynamic routes and typed params** to a small local fixture that demonstrates dynamic routes and typed params. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a small local fixture that demonstrates dynamic routes and typed params using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the code or framework boundary that owns the decision in this lesson. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

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
10. Apply the lesson to a small local fixture that demonstrates dynamic routes and typed params and document the route map.
11. Explain what crosses the the code or framework boundary that owns the decision in this lesson and what must stay private.
12. Write a review note with the URL, file map, evidence, and one deployment limitation.

## Finish line

You are finished when you can teach **Dynamic routes and typed params** to another beginner, show the normal and broken runs, explain the repair, and point to **the code or framework boundary that owns the decision in this lesson**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
