# Day 043: Route groups and private folders

[← Previous lesson](../day_042_dynamic_routes_and_typed_params/day_042_dynamic_routes_and_typed_params.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_044_loading_error_and_not_found_ui/day_044_loading_error_and_not_found_ui.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a route group?](#what-is-a-route-group)
  - [Why does parentheses not change the URL?](#why-does-parentheses-not-change-the-url)
  - [What is a private folder?](#what-is-a-private-folder)
  - [What can be colocated safely?](#what-can-be-colocated-safely)
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

The learner problem comes first: Learners need a concrete reason to study route groups and private folders before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. This lesson teaches **Route groups and private folders** through a connected sequence rather than a finished file dropped from the sky: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **route groups and private folders** to a small local fixture that demonstrates route groups and private folders. You should be able to name the owner and boundary—the code or framework boundary that owns the decision in this lesson—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `route group` | A parenthesized App Router folder used for organization or layout without adding a URL segment. |
| `private folder` | A Next.js folder prefixed with an underscore that is used for colocation without becoming a route segment. |
| `colocation` | Keeping code close to the route or feature that owns it without making every file a public route. |
| `URL` | The structured address that identifies a web resource and may include path and query values. |
| `layout scope` | The set of route segments that inherit a particular shared layout. |

## Topics

### What is a route group?

Start with the learner's concrete question: **What is a route group**. Use the worked example to show what **What is a route group** changes before introducing a framework shortcut. For **What is a route group**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is a route group**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is a route group?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why does parentheses not change the URL?

The answer to **Why does parentheses not change the URL** must be earned by comparing a working case with a deliberately limited or broken case. For **Why does parentheses not change the URL**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why does parentheses not change the URL**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why does parentheses not change the URL?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a small local fixture that demonstrates route groups and private folders.

### What is a private folder?

Start with the learner's concrete question: **What is a private folder**. Use the worked example to show what **What is a private folder** changes before introducing a framework shortcut. For **What is a private folder**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is a private folder**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is a private folder?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### What can be colocated safely?

Start with the learner's concrete question: **What can be colocated safely**. Use the worked example to show what **What can be colocated safely** changes before introducing a framework shortcut. For **What can be colocated safely**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What can be colocated safely**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What can be colocated safely?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.

```tsx
app/(marketing)/about/page.tsx
app/dashboard/_components/Nav.tsx
```

**Expected result or visible behavior:**

```text
The route remains /about while the code is organized.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the code or framework boundary that owns the decision in this lesson.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `app/(marketing)/about/page.tsx` — Runs inside the current example; connect its effect to the code or framework boundary that owns the decision in this lesson. |
| 2 | `app/dashboard/_components/Nav.tsx` — Runs inside the current example; connect its effect to the code or framework boundary that owns the decision in this lesson. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Learners need a concrete reason to study route groups and private folders before the terminology becomes useful.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Route groups and private folders**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Put a route in a group and accidentally duplicate a URL; repair the folder plan.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy the syntax without identifying the input, owner, output, and boundary. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **route groups and private folders** to a small local fixture that demonstrates route groups and private folders. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a small local fixture that demonstrates route groups and private folders using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the code or framework boundary that owns the decision in this lesson. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

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
10. Apply the lesson to a small local fixture that demonstrates route groups and private folders and document the route map.
11. Explain what crosses the the code or framework boundary that owns the decision in this lesson and what must stay private.
12. Write a review note with the URL, file map, evidence, and one deployment limitation.

## Finish line

You are finished when you can teach **Route groups and private folders** to another beginner, show the normal and broken runs, explain the repair, and point to **the code or framework boundary that owns the decision in this lesson**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
