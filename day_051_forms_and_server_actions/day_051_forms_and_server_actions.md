# Day 051: Forms and Server Actions

[← Previous lesson](../day_050_streaming_and_suspense_in_next_js/day_050_streaming_and_suspense_in_next_js.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_052_route_handlers_and_http_apis/day_052_route_handlers_and_http_apis.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a Server Action?](#what-is-a-server-action)
  - [How does a form call server code?](#how-does-a-form-call-server-code)
  - [Where should validation happen?](#where-should-validation-happen)
  - [Where should authorization happen?](#where-should-authorization-happen)
  - [When should we revalidate or redirect?](#when-should-we-revalidate-or-redirect)
- [Worked example](#worked-example)
  - [Example 1: a server-owned function](#example-1-a-server-owned-function)
  - [Example 2: validate before mutation](#example-2-validate-before-mutation)
  - [Example 3: return a useful form result](#example-3-return-a-useful-form-result)
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

Use the Next.js starter from [examples](../examples/README.md) after reading the [README](../README.md) and [setup](../SETUP.md). Use a local synthetic case fixture. This lesson explains the architecture and can be completed with an in-memory function before adding a database.

## Why this lesson exists

A form is often the first place a full-stack app crosses from browser intent into server authority. A button click is not permission to write a record. The server must receive the form data, validate it, identify the caller, check permission, perform the mutation, and then tell the UI what happened.

A Server Action is a server-side function that a form or controlled interaction can invoke through a framework boundary. It is convenient, but it is not a magic security wrapper. The function still needs validation, authentication, authorization, deliberate error handling, and a sensible revalidation or redirect policy.

## Prerequisites

Complete forms, Server and Client Components, validation, and server-only data boundaries. You should know that browser input is untrusted and that a client button cannot authorize itself.

## Outcomes

You should be able to write a small Server Action, read `FormData`, validate before mutation, derive ownership from the server-side session rather than a hidden field, return field errors, and revalidate the route only after a successful mutation.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Server Action** | A server-side function exposed through a controlled framework form or interaction boundary. |
| **FormData** | A browser representation of named form fields and submitted values. |
| **Mutation** | An operation that creates, changes, or deletes data. |
| **Validation** | Checking that untrusted input has the required shape and values. |
| **Authorization** | Deciding whether the identified actor may perform the operation. |
| **Revalidation** | Telling the framework that previously rendered data should be refreshed. |
| **Redirect** | Sending the user to another route after a deliberate result. |
| **Field error** | A user-facing explanation tied to invalid form input. |

## Topics

### What is a Server Action?

A Server Action is a server function that can be connected to a form action. It reduces the amount of manual client request code, but it does not remove the need to treat the input as untrusted.

### How does a form call server code?

A form submits named controls. The Action receives `FormData` and returns a result or performs a deliberate navigation. The browser does not become the authority merely because it sent the request.

### Where should validation happen?

Validate on the server immediately after reading the input and before calling a repository or database. Client validation can improve feedback but is bypassable. Keep the validation schema close to the server boundary.

### Where should authorization happen?

Authorize on the server after identifying the actor and before reading protected data or mutating it. Do not accept `ownerId` from a hidden input as proof of ownership. Derive the actor from the session and check permission or ownership against authoritative data.

### When should we revalidate or redirect?

Revalidate after a successful mutation so the next render sees fresh data. Redirect only after the result and destination are deliberate. Do not refresh a route before a mutation succeeds; that can hide failure and leave stale assumptions.

## Worked example

### Example 1: a server-owned function

```tsx
// src/app/cases/actions.ts
'use server';

export async function createCase(formData: FormData) {
  const title = formData.get('title');
  if (typeof title !== 'string' || title.trim() === '') {
    return { ok: false, error: 'Enter a case title.' };
  }

  return { ok: true, title: title.trim() };
}
```

The example validates and returns a local result. It does not yet write to a database.

### Example 2: validate before mutation

```tsx
'use server';

import { revalidatePath } from 'next/cache';

export async function createCase(formData: FormData) {
  const title = formData.get('title');
  if (typeof title !== 'string' || title.trim().length < 3) {
    return { ok: false, error: 'Use at least three characters.' };
  }

  const actor = await requireSession();
  if (!actor.permissions.includes('case:create')) {
    return { ok: false, error: 'You cannot create a case.' };
  }

  await caseRepository.create({
    title: title.trim(),
    ownerId: actor.userId,
  });
  revalidatePath('/cases');
  return { ok: true };
}
```

The ordering matters. Invalid input never reaches the repository. The owner comes from the server actor, not from a hidden form field. Revalidation happens after the mutation succeeds.

### Example 3: return a useful form result

A form can show the Action's result through a later React 19 form-state lesson. Even before that, design a result with stable fields:

```ts
return { ok: false, field: 'title', error: 'Enter a case title.' };
```

A stable result is easier for a client form to display and easier for a test to assert than a raw thrown stack trace.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `'use server'` | Marks this module or function as server-owned; it is not permission by itself. |
| `formData.get('title')` | Reads untrusted submitted data; the result may not be a string. |
| `typeof title !== 'string'` | Checks the runtime type before string methods. |
| `title.trim().length < 3` | Applies a domain validation rule before mutation. |
| `requireSession()` | Identifies the actor from server-side session state. |
| `actor.permissions.includes(...)` | Applies authorization; a logged-in actor is not automatically allowed. |
| `ownerId: actor.userId` | Derives ownership from authority, not a browser-controlled field. |
| `revalidatePath('/cases')` | Requests fresh route data after the successful mutation. |

## Execution trace

1. The browser submits a form containing a title.
2. The Action reads the field as `FormData` and checks its runtime type.
3. Invalid or too-short input returns a structured error and stops.
4. Valid input identifies the actor on the server.
5. Missing permission returns an authorization result and stops.
6. Authorized input reaches the repository with a server-derived owner.
7. After success, the cases path is revalidated and the form can show success or navigate.

## Prediction experiment

Predict the result of a missing title, a numeric-like value, a two-character title, a signed-out actor, and an actor without `case:create`. Move `revalidatePath` before the repository call and explain what evidence becomes misleading. Add a hidden `ownerId` field and predict whether it should affect the server's owner decision.

## Broken example and repair

**Broken version:** trust `formData.get('ownerId')` as the record owner and call `revalidatePath` before the mutation. Repair by deriving `ownerId` from the server-side actor, authorizing before the repository call, and revalidating only after success.

Do not repair it by hiding the owner input with CSS or disabling the submit button. Those are browser presentation choices, not authority.

## Guided practice before independent work

Start with an in-memory Action that returns an error for an empty title. Add type checking. Add a synthetic actor. Add permission. Add a repository stub. Add revalidation after success. At every step write what is trusted and what is not.

## Project application

Add a local **create-case Server Action** to the dashboard. It must validate title and severity, derive the owner from a synthetic server session, reject an unauthorized actor, mutate a local repository or fixture, and return a structured result. Record the normal and failure evidence.

## Independent exercises

### Level 1 — Confidence
1. What is Forms and Server Actions? Answer in one sentence.
2. Read a title from `FormData`.
3. Reject missing and non-string values.
4. Return a structured field error.
5. Return success for a valid synthetic title.

### Level 2 — Application
6. Add a synthetic actor and permission.
7. Derive ownership from the actor, not a hidden field.
8. Add a repository stub and mutation call.
9. Revalidate only after success.

### Level 3 — Synthesis
10. Reproduce the client-provided-owner failure and repair it.
11. Add normal, invalid, signed-out, and forbidden fixtures.
12. Submit the form once with a good value and once with a bad value. Write down both messages.
13. Write a review note with validation order, authority boundary, revalidation point, evidence, and limitation.

## Finish line

You are ready when you can explain why a Server Action is a server boundary but not an automatic authorization system, and you can show the exact order of validation, identity, permission, mutation, and refresh.

## References

- [Next.js: Updating Data](https://nextjs.org/docs/app/getting-started/updating-data)
- [Next.js: Forms](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)
- [Next.js: Authentication](https://nextjs.org/docs/app/guides/authentication)
