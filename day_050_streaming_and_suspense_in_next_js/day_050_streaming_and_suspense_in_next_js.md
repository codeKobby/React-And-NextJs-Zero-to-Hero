# Day 050: Streaming and Suspense in Next.js

[← Previous lesson](../day_049_caching_and_revalidation/day_049_caching_and_revalidation.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_051_forms_and_server_actions/day_051_forms_and_server_actions.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is streaming?](#what-is-streaming)
  - [Why do waterfalls happen?](#why-do-waterfalls-happen)
  - [Where should Suspense boundaries live?](#where-should-suspense-boundaries-live)
  - [What makes loading UI meaningful?](#what-makes-loading-ui-meaningful)
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

The learner problem comes first: Learners need a concrete reason to study streaming and suspense in next.js before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. This lesson teaches **Streaming and Suspense in Next.js** through a connected sequence rather than a finished file dropped from the sky: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **streaming and suspense in next.js** to a small local fixture that demonstrates streaming and suspense in next.js. You should be able to name the owner and boundary—the code or framework boundary that owns the decision in this lesson—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `streaming` | Sending ready parts of a response while slower parts continue instead of waiting for the whole tree. |
| `Suspense` | A React boundary that coordinates fallback UI while a child is not ready to render. |
| `loading.tsx` | A Next.js special file that supplies a loading UI for a route segment while work is pending. |
| `skeleton` | Temporary layout-shaped UI shown while content is loading. |
| `waterfall` | A sequence in which one asynchronous operation waits for another, increasing total latency. |
| `boundary` | A point where responsibility, data, rendering, or authority changes hands. |

## Topics

### What is streaming?

Start with the learner's concrete question: **What is streaming**. Use the worked example to show what **What is streaming** changes before introducing a framework shortcut. For **What is streaming**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is streaming**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is streaming?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why do waterfalls happen?

The answer to **Why do waterfalls happen** must be earned by comparing a working case with a deliberately limited or broken case. For **Why do waterfalls happen**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why do waterfalls happen**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why do waterfalls happen?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a small local fixture that demonstrates streaming and suspense in next.js.

### Where should Suspense boundaries live?

Study **Where should Suspense boundaries live** by naming the concrete value, operation, visible result, and owner in the worked example. For **Where should Suspense boundaries live**, underline the line or file where this idea becomes observable and explain what would change it. Keep the conclusion limited to the local evidence for **Where should Suspense boundaries live**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Where should Suspense boundaries live?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### What makes loading UI meaningful?

Start with the learner's concrete question: **What makes loading UI meaningful**. Use the worked example to show what **What makes loading UI meaningful** changes before introducing a framework shortcut. For **What makes loading UI meaningful**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What makes loading UI meaningful**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What makes loading UI meaningful?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.

```tsx
<Suspense fallback={<PostSkeleton />}><SlowPostList /></Suspense>
```

**Expected result or visible behavior:**

```text
The page shell appears before the slow list.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the code or framework boundary that owns the decision in this lesson.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `<Suspense fallback={<PostSkeleton />}><SlowPostList /></Suspense>` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Learners need a concrete reason to study streaming and suspense in next.js before the terminology becomes useful.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Streaming and Suspense in Next.js**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Place the boundary around the whole app and explain the lost progressive rendering.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy the syntax without identifying the input, owner, output, and boundary. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **streaming and suspense in next.js** to a small local fixture that demonstrates streaming and suspense in next.js. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a small local fixture that demonstrates streaming and suspense in next.js using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the code or framework boundary that owns the decision in this lesson. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Define **What is streaming?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **Why do waterfalls happen?**, then predict before running.
5. Create a boundary case involving **Where should Suspense boundaries live?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Place the boundary around the whole app and explain the lost progressive rendering.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply streaming and suspense in next.js to a small local fixture that demonstrates streaming and suspense in next.js with a local synthetic fixture.
11. Explain the owner and boundary: the code or framework boundary that owns the decision in this lesson.
12. Write a review note with evidence, one limitation, and the next learning step.

## Finish line

You are finished when you can teach **Streaming and Suspense in Next.js** to another beginner, show the normal and broken runs, explain the repair, and point to **the code or framework boundary that owns the decision in this lesson**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
