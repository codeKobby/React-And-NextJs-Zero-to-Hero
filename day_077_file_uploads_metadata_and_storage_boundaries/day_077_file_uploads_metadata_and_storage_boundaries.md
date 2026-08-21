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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will bound size and type, record safe metadata, choose a storage boundary, and authorize a download. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: Files are larger and more ambiguous than ordinary text fields, and a filename is not a security policy. A receiving dock weighs and labels a package before storing it; a name written on the box does not prove what is inside. This lesson teaches **File uploads, metadata, and storage boundaries** through a connected sequence rather than a finished file dropped from the sky: We will bound size and type, record safe metadata, choose a storage boundary, and authorize a download. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **forms, validation, HTTP responses, and authorization**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **file uploads, metadata, and storage boundaries** to a local synthetic upload validator and authorized download response. You should be able to name the owner and boundary—browser file input versus server validation, storage, and access policy—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

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

Start with the learner's concrete question: **What is an upload boundary**. Use the worked example to show what **What is an upload boundary** changes before introducing a framework shortcut. For **What is an upload boundary**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is an upload boundary**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is an upload boundary?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why validate size and type on the server?

The answer to **Why validate size and type on the server** must be earned by comparing a working case with a deliberately limited or broken case. For **Why validate size and type on the server**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why validate size and type on the server**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why validate size and type on the server?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a local synthetic upload validator and authorized download response.

### Where should file bytes live?

Study **Where should file bytes live** by naming the concrete value, operation, visible result, and owner in the worked example. For **Where should file bytes live**, underline the line or file where this idea becomes observable and explain what would change it. Keep the conclusion limited to the local evidence for **Where should file bytes live**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Where should file bytes live?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How should downloads be authorized?

To answer **How should downloads be authorized**, follow the operation in order rather than treating the result as framework magic. For **How should downloads be authorized**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How should downloads be authorized**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How should downloads be authorized?**, change one input or boundary in the worked example. Trace the result for **How should downloads be authorized?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will bound size and type, record safe metadata, choose a storage boundary, and authorize a download.

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

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is browser file input versus server validation, storage, and access policy.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const MAX_BYTES = 2_000_000;` — Creates a named value from the expression on the right; record its input, lifetime, and owner in this day's example. |
| 2 | `if (file.size > MAX_BYTES \|\| !ALLOWED_TYPES.has(file.type)) {` — Guards the next behavior with a deliberate condition; this is where the example chooses a normal, empty, invalid, or unauthorized path. |
| 3 | `return { error: 'Unsupported file' };` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |
| 4 | `}` — Runs inside the current example; connect its effect to browser file input versus server validation, storage, and access policy. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Files are larger and more ambiguous than ordinary text fields, and a filename is not a security policy.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will bound size and type, record safe metadata, choose a storage boundary, and authorize a download.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **File uploads, metadata, and storage boundaries**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Trust the filename extension, accept unlimited bytes, and serve a file without checking ownership, then repair all three boundaries.

Run the broken version in a local copy. The likely beginner mistake for this family is: Trust extensions, accept unlimited bytes, or serve a stored object without checking ownership. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **file uploads, metadata, and storage boundaries** to a local synthetic upload validator and authorized download response. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local synthetic upload validator and authorized download response using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is browser file input versus server validation, storage, and access policy. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the smallest local schema or query fixture and record the returned shape.
2. Draw the tables, identifiers, and ownership relationship before coding.
3. Change one field or query filter and predict the result.
4. Add an empty result and a malformed or missing-record case.
5. Reproduce the missing-migration, raw-row, or unscoped-query mistake.
6. Repair it with a migration, DTO, repository, or ownership filter.
7. Explain which module is server-only and why the client does not receive raw database details.
8. Add a transaction or rollback scenario where the lesson makes it relevant.
9. Add a focused test for the query or repository contract.
10. Apply the data boundary to a local synthetic upload validator and authorized download response with resettable synthetic seed data.
11. Explain how authorization intersects with browser file input versus server validation, storage, and access policy.
12. Write a review note with schema evidence, migration state, query scope, and one limitation.

## Finish line

You are finished when you can teach **File uploads, metadata, and storage boundaries** to another beginner, show the normal and broken runs, explain the repair, and point to **browser file input versus server validation, storage, and access policy**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
