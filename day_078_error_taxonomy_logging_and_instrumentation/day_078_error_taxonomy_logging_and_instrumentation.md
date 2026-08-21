# Day 078: Error taxonomy, logging, and instrumentation

[← Previous lesson](../day_077_file_uploads_metadata_and_storage_boundaries/day_077_file_uploads_metadata_and_storage_boundaries.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_079_full_stack_testing_with_playwright_and_synthetic_fixtures/day_079_full_stack_testing_with_playwright_and_synthetic_fixtures.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is the difference between an expected and unexpected error?](#what-is-the-difference-between-an-expected-and-unexpected-error)
  - [What should a structured log contain?](#what-should-a-structured-log-contain)
  - [Why use a request ID?](#why-use-a-request-id)
  - [Where does instrumentation belong?](#where-does-instrumentation-belong)
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

The learner problem comes first: Learners need a concrete reason to study error taxonomy, logging, and instrumentation before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. This lesson teaches **Error taxonomy, logging, and instrumentation** through a connected sequence rather than a finished file dropped from the sky: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **error taxonomy, logging, and instrumentation** to a small local fixture that demonstrates error taxonomy, logging, and instrumentation. You should be able to name the owner and boundary—the code or framework boundary that owns the decision in this lesson—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `expected error` | A deliberate failure outcome that the application models and handles as part of normal behavior. |
| `unexpected error` | A failure outside the documented normal input cases that requires safe logging and fallback behavior. |
| `structured log` | A machine-readable log event with consistent fields for searching and correlation. |
| `request ID` | A correlation value that lets logs and traces for one request be found across boundaries. |
| `instrumentation` | Code that records or observes runtime behavior for diagnostics, metrics, or tracing. |
| `observability` | The ability to understand system behavior through useful logs, measurements, traces, and events. |

## Topics

### What is the difference between an expected and unexpected error?

Start with the learner's concrete question: **What is the difference between an expected and unexpected error**. Use the worked example to show what **What is the difference between an expected and unexpected error** changes before introducing a framework shortcut. For **What is the difference between an expected and unexpected error**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is the difference between an expected and unexpected error**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is the difference between an expected and unexpected error?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### What should a structured log contain?

Start with the learner's concrete question: **What should a structured log contain**. Use the worked example to show what **What should a structured log contain** changes before introducing a framework shortcut. For **What should a structured log contain**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What should a structured log contain**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What should a structured log contain?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why use a request ID?

The answer to **Why use a request ID** must be earned by comparing a working case with a deliberately limited or broken case. For **Why use a request ID**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why use a request ID**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why use a request ID?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a small local fixture that demonstrates error taxonomy, logging, and instrumentation.

### Where does instrumentation belong?

Study **Where does instrumentation belong** by naming the concrete value, operation, visible result, and owner in the worked example. For **Where does instrumentation belong**, underline the line or file where this idea becomes observable and explain what would change it. Keep the conclusion limited to the local evidence for **Where does instrumentation belong**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Where does instrumentation belong?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.

```tsx
logger.info({ requestId, route: '/cases', event: 'case.created', caseId });
return { ok: true };
```

**Expected result or visible behavior:**

```text
The event can be correlated without logging a secret or raw credential.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the code or framework boundary that owns the decision in this lesson.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `logger.info({ requestId, route: '/cases', event: 'case.created', caseId });` — Runs inside the current example; connect its effect to the code or framework boundary that owns the decision in this lesson. |
| 2 | `return { ok: true };` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Learners need a concrete reason to study error taxonomy, logging, and instrumentation before the terminology becomes useful.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Error taxonomy, logging, and instrumentation**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Log an entire request body and expose a stack trace to the user, then repair the event fields and public error.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy the syntax without identifying the input, owner, output, and boundary. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **error taxonomy, logging, and instrumentation** to a small local fixture that demonstrates error taxonomy, logging, and instrumentation. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a small local fixture that demonstrates error taxonomy, logging, and instrumentation using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the code or framework boundary that owns the decision in this lesson. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Define **What is the difference between an expected and unexpected error?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **What should a structured log contain?**, then predict before running.
5. Create a boundary case involving **Why use a request ID?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Log an entire request body and expose a stack trace to the user, then repair the event fields and public error.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply error taxonomy, logging, and instrumentation to a small local fixture that demonstrates error taxonomy, logging, and instrumentation with a local synthetic fixture.
11. Explain the owner and boundary: the code or framework boundary that owns the decision in this lesson.
12. Write a review note with evidence, one limitation, and the next learning step.

## Finish line

You are finished when you can teach **Error taxonomy, logging, and instrumentation** to another beginner, show the normal and broken runs, explain the repair, and point to **the code or framework boundary that owns the decision in this lesson**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
