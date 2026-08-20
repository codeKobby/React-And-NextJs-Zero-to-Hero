# Day 071: Server Actions for validated mutations

[← Previous lesson](../day_070_repositories_and_server_only_data_access/day_070_repositories_and_server_only_data_access.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_072_route_handlers_api_contracts_and_typed_errors/day_072_route_handlers_api_contracts_and_typed_errors.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a Server Action?](#what-is-a-server-action)
  - [Where should validation and authorization happen?](#where-should-validation-and-authorization-happen)
  - [How do we return field errors?](#how-do-we-return-field-errors)
  - [When should a mutation revalidate or redirect?](#when-should-a-mutation-revalidate-or-redirect)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will submit FormData, validate it on the server, check permission, mutate a local record, and revalidate the visible route. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: A form needs to change server-owned data while preserving validation, authorization, pending state, and a useful result. A signed request goes to the office that owns the records; the front desk can report pending or rejected, but it cannot approve itself. This lesson teaches **Server Actions for validated mutations** through a connected sequence rather than a finished file dropped from the sky: We will submit FormData, validate it on the server, check permission, mutate a local record, and revalidate the visible route. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **forms, async functions, validation, and Next.js Server Components**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **server actions for validated mutations** to a validated local create-case mutation with field errors and revalidation evidence. You should be able to name the owner and boundary—browser intent versus server authority and data mutation—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `Server Action` | A server-side function that a form or client interaction can invoke through a controlled framework boundary. |
| `use server` | A directive marking a module or function as server-owned for a Next.js server boundary. |
| `FormData` | A browser object that collects named form controls and their submitted values. |
| `mutation` | An operation that creates, changes, or deletes data. |
| `revalidation` | Refreshing cached or rendered data according to a route or data policy. |
| `redirect` | A response or framework operation that sends the browser to another URL. |

## Topics

### What is a Server Action?

Start with the learner's concrete question: **What is a Server Action**. The problem underneath this lesson is that a form needs to change server-owned data while preserving validation, authorization, pending state, and a useful result. A signed request goes to the office that owns the records; the front desk can report pending or rejected, but it cannot approve itself. In this course's sequence, we will submit formdata, validate it on the server, check permission, mutate a local record, and revalidate the visible route. The relevant boundary is browser intent versus server authority and data mutation.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Where should validation and authorization happen?

Study **Where should validation and authorization happen** by naming its input, operation, visible result, and owner. The problem underneath this lesson is that a form needs to change server-owned data while preserving validation, authorization, pending state, and a useful result. A signed request goes to the office that owns the records; the front desk can report pending or rejected, but it cannot approve itself. In this course's sequence, we will submit formdata, validate it on the server, check permission, mutate a local record, and revalidate the visible route. The relevant boundary is browser intent versus server authority and data mutation.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do we return field errors?

To answer **How do we return field errors**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that a form needs to change server-owned data while preserving validation, authorization, pending state, and a useful result. A signed request goes to the office that owns the records; the front desk can report pending or rejected, but it cannot approve itself. In this course's sequence, we will submit formdata, validate it on the server, check permission, mutate a local record, and revalidate the visible route. The relevant boundary is browser intent versus server authority and data mutation.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

### When should a mutation revalidate or redirect?

Treat **When should a mutation revalidate or redirect** as a decision that has a normal case, a boundary case, and a cost when chosen carelessly. The problem underneath this lesson is that a form needs to change server-owned data while preserving validation, authorization, pending state, and a useful result. A signed request goes to the office that owns the records; the front desk can report pending or rejected, but it cannot approve itself. In this course's sequence, we will submit formdata, validate it on the server, check permission, mutate a local record, and revalidate the visible route. The relevant boundary is browser intent versus server authority and data mutation.

**Try it before moving on:** Write a decision rule with one normal case and one boundary case. Include what would make the other option preferable.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will submit FormData, validate it on the server, check permission, mutate a local record, and revalidate the visible route.

```tsx
'use server';

export async function createCase(formData: FormData) {
  const input = CaseSchema.safeParse({ title: formData.get('title') });
  if (!input.success) return { error: 'Invalid title' };
  await requirePermission('case:create');
  revalidatePath('/cases');
}
```

**Expected result or visible behavior:**

```text
The server validates, authorizes, mutates, and refreshes the relevant route.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is browser intent versus server authority and data mutation.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `'use server';` — Runs inside the current example; connect its effect to browser intent versus server authority and data mutation. |
| 2 | Blank line: it separates the surrounding ideas; it has no runtime operation. |
| 3 | `export async function createCase(formData: FormData) {` — Makes this binding available to another module; the export is part of this lesson's public boundary. |
| 4 | `const input = CaseSchema.safeParse({ title: formData.get('title') });` — Creates a named value from the expression on the right; record its input, lifetime, and owner in this day's example. |
| 5 | `if (!input.success) return { error: 'Invalid title' };` — Guards the next behavior with a deliberate condition; this is where the example chooses a normal, empty, invalid, or unauthorized path. |
| 6 | `await requirePermission('case:create');` — Pauses this async operation until its promise settles; identify whether the work runs on the server and how failure is handled. |
| 7 | `revalidatePath('/cases');` — Runs inside the current example; connect its effect to browser intent versus server authority and data mutation. |
| 8 | `}` — Runs inside the current example; connect its effect to browser intent versus server authority and data mutation. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A form needs to change server-owned data while preserving validation, authorization, pending state, and a useful result.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will submit FormData, validate it on the server, check permission, mutate a local record, and revalidate the visible route.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Server Actions for validated mutations**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Revalidate before the mutation succeeds and trust a client-provided owner ID, then repair the sequence.

Run the broken version in a local copy. The likely beginner mistake for this family is: Trust a client-provided owner, validate only in the browser, or refresh the page before the mutation succeeds. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **server actions for validated mutations** to a validated local create-case mutation with field errors and revalidation evidence. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a validated local create-case mutation with field errors and revalidation evidence using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is browser intent versus server authority and data mutation. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Define **What is a Server Action?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **Where should validation and authorization happen?**, then predict before running.
5. Create a boundary case involving **How do we return field errors?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Revalidate before the mutation succeeds and trust a client-provided owner ID, then repair the sequence.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply server actions for validated mutations to a validated local create-case mutation with field errors and revalidation evidence with a local synthetic fixture.
11. Explain the owner and boundary: browser intent versus server authority and data mutation.
12. Write a review note with evidence, one limitation, and the next learning step.

## Finish line

You are finished when you can teach **Server Actions for validated mutations** to another beginner, show the normal and broken runs, explain the repair, and point to **browser intent versus server authority and data mutation**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
