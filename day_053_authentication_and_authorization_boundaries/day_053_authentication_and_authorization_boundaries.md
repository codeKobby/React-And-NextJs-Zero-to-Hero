# Day 053: Authentication and authorization boundaries

[← Previous lesson](../day_052_route_handlers_and_http_apis/day_052_route_handlers_and_http_apis.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_054_testing_next_js_applications/day_054_testing_next_js_applications.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is the difference between authentication and authorization?](#what-is-the-difference-between-authentication-and-authorization)
  - [Where should session checks run?](#where-should-session-checks-run)
  - [Why is a hidden button not authorization?](#why-is-a-hidden-button-not-authorization)
  - [How do roles limit data?](#how-do-roles-limit-data)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: A full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection. A building entrance may check for a badge, but each room still checks whether the visitor is allowed to open the cabinet inside. This lesson teaches **Authentication and authorization boundaries** through a connected sequence rather than a finished file dropped from the sky: We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **Next.js routing, server/client boundaries, cookies, and validation**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **authentication and authorization boundaries** to a local protected case route with synthetic sessions, permissions, and unauthorized fixtures. You should be able to name the owner and boundary—identity and navigation checks versus server-side data and mutation authority—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `authentication` | Establishing who an actor is, usually through a provider or session. |
| `authorization` | Deciding whether an identified actor may perform a requested action or access a record. |
| `session` | Server-managed information that connects later requests to an authenticated actor. |
| `cookie` | A browser-stored value sent with matching requests; its presence is not proof of permission. |
| `CSRF` | Cross-site request forgery, in which an unwanted request is induced from another site using a user's authority. |
| `role` | A named grouping of permissions that describes a class of actor responsibilities. |
| `least privilege` | Giving an actor or module only the authority required for its task. |

## Topics

### What is the difference between authentication and authorization?

Start with the learner's concrete question: **What is the difference between authentication and authorization**. Use the worked example to show what **What is the difference between authentication and authorization** changes before introducing a framework shortcut. For **What is the difference between authentication and authorization**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is the difference between authentication and authorization**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is the difference between authentication and authorization?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Where should session checks run?

Study **Where should session checks run** by naming the concrete value, operation, visible result, and owner in the worked example. For **Where should session checks run**, underline the line or file where this idea becomes observable and explain what would change it. Keep the conclusion limited to the local evidence for **Where should session checks run**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Where should session checks run?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why is a hidden button not authorization?

The answer to **Why is a hidden button not authorization** must be earned by comparing a working case with a deliberately limited or broken case. For **Why is a hidden button not authorization**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why is a hidden button not authorization**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why is a hidden button not authorization?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a local protected case route with synthetic sessions, permissions, and unauthorized fixtures.

### How do roles limit data?

To answer **How do roles limit data**, follow the operation in order rather than treating the result as framework magic. For **How do roles limit data**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do roles limit data**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do roles limit data?**, change one input or boundary in the worked example. Trace the result for **How do roles limit data?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors.

```tsx
const session = await requireSession();
if (!session.can('case:read')) notFound();
```

**Expected result or visible behavior:**

```text
The server enforces access before returning data.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is identity and navigation checks versus server-side data and mutation authority.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const session = await requireSession();` — Pauses this async operation until its promise settles; identify whether the work runs on the server and how failure is handled. |
| 2 | `if (!session.can('case:read')) notFound();` — Guards the next behavior with a deliberate condition; this is where the example chooses a normal, empty, invalid, or unauthorized path. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Authentication and authorization boundaries**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Hide an admin link without protecting the route and repair the server-side check.

Run the broken version in a local copy. The likely beginner mistake for this family is: Treat a browser field, client redirect, or login flag as proof of permission and return data before the server policy runs. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **authentication and authorization boundaries** to a local protected case route with synthetic sessions, permissions, and unauthorized fixtures. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local protected case route with synthetic sessions, permissions, and unauthorized fixtures using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is identity and navigation checks versus server-side data and mutation authority. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the synthetic signed-out and signed-in fixtures and record the visible outcome.
2. Separate identity, session, navigation check, and permission in a short table.
3. Change one permission and predict which request should be allowed or rejected.
4. Add an unauthorized and an ownership-mismatch fixture.
5. Reproduce the client-only or hidden-button protection mistake.
6. Repair the authoritative server-side check before data access or mutation.
7. Inspect cookie flags, expiry, secret ownership, and environment boundaries.
8. Add a test for a forbidden actor that cannot read or mutate another record.
9. Explain why Proxy or a redirect is not final authorization.
10. Apply the policy to a local protected case route with synthetic sessions, permissions, and unauthorized fixtures with invented actors and records.
11. Document the exact trust boundary: identity and navigation checks versus server-side data and mutation authority.
12. Write residual-risk notes for session rotation, logging, and deployment configuration.

## Finish line

You are finished when you can teach **Authentication and authorization boundaries** to another beginner, show the normal and broken runs, explain the repair, and point to **identity and navigation checks versus server-side data and mutation authority**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
