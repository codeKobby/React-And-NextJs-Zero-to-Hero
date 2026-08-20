# Day 074: Secure sessions and cookie policy

[← Previous lesson](../day_073_authentication_providers_and_identity_boundaries/day_073_authentication_providers_and_identity_boundaries.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_075_next_js_16_proxy_and_the_middleware_migration/day_075_next_js_16_proxy_and_the_middleware_migration.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is session management?](#what-is-session-management)
  - [Why must session code be server-only?](#why-must-session-code-be-server-only)
  - [What cookie flags reduce risk?](#what-cookie-flags-reduce-risk)
  - [How do stateless sessions expire?](#how-do-stateless-sessions-expire)
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

The learner problem comes first: A full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection. A building entrance may check for a badge, but each room still checks whether the visitor is allowed to open the cabinet inside. This lesson teaches **Secure sessions and cookie policy** through a connected sequence rather than a finished file dropped from the sky: We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **Next.js routing, server/client boundaries, cookies, and validation**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **secure sessions and cookie policy** to a local protected case route with synthetic sessions, permissions, and unauthorized fixtures. You should be able to name the owner and boundary—identity and navigation checks versus server-side data and mutation authority—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `session` | Server-managed information that connects later requests to an authenticated actor. |
| `cookie` | A browser-stored value sent with matching requests; its presence is not proof of permission. |
| `HttpOnly` | A cookie flag that prevents ordinary browser JavaScript from reading the cookie value. |
| `Secure` | A cookie flag that restricts transmission to HTTPS requests. |
| `SameSite` | A cookie policy controlling when the browser sends the cookie in cross-site contexts. |
| `expiry` | The time or condition after which a cookie, session, cache entry, or credential is no longer accepted. |
| `jose` | A JavaScript library family for working with signed or encrypted JSON-based security tokens. |
| `secret` | Sensitive configuration or credential material that must not be exposed in client code or source control. |

## Topics

### What is session management?

Start with the learner's concrete question: **What is session management**. The problem underneath this lesson is that a full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection. A building entrance may check for a badge, but each room still checks whether the visitor is allowed to open the cabinet inside. In this course's sequence, we will separate identity, session, proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors. The relevant boundary is identity and navigation checks versus server-side data and mutation authority.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why must session code be server-only?

The answer to **Why must session code be server-only** must be earned through a visible comparison, not memorized as a slogan. The problem underneath this lesson is that a full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection. A building entrance may check for a badge, but each room still checks whether the visitor is allowed to open the cabinet inside. In this course's sequence, we will separate identity, session, proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors. The relevant boundary is identity and navigation checks versus server-side data and mutation authority.

**Try it before moving on:** Compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a local protected case route with synthetic sessions, permissions, and unauthorized fixtures.

### What cookie flags reduce risk?

Start with the learner's concrete question: **What cookie flags reduce risk**. The problem underneath this lesson is that a full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection. A building entrance may check for a badge, but each room still checks whether the visitor is allowed to open the cabinet inside. In this course's sequence, we will separate identity, session, proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors. The relevant boundary is identity and navigation checks versus server-side data and mutation authority.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do stateless sessions expire?

To answer **How do stateless sessions expire**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that a full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection. A building entrance may check for a badge, but each room still checks whether the visitor is allowed to open the cabinet inside. In this course's sequence, we will separate identity, session, proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors. The relevant boundary is identity and navigation checks versus server-side data and mutation authority.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors.

```tsx
const session = await createSignedSession({ userId });
(await cookies()).set('session', session, { httpOnly: true, secure: true, sameSite: 'lax', path: '/' });
```

**Expected result or visible behavior:**

```text
The session is signed and stored with browser access restricted from client JavaScript.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is identity and navigation checks versus server-side data and mutation authority.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const session = await createSignedSession({ userId });` — Pauses this async operation until its promise settles; identify whether the work runs on the server and how failure is handled. |
| 2 | `(await cookies()).set('session', session, { httpOnly: true, secure: true, sameSite: 'lax', path: '/' });` — Pauses this async operation until its promise settles; identify whether the work runs on the server and how failure is handled. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Secure sessions and cookie policy**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Store a raw user ID in a readable cookie without expiry, then repair signing, flags, and rotation planning.

Run the broken version in a local copy. The likely beginner mistake for this family is: Treat a browser field, client redirect, or login flag as proof of permission and return data before the server policy runs. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **secure sessions and cookie policy** to a local protected case route with synthetic sessions, permissions, and unauthorized fixtures. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

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

You are finished when you can teach **Secure sessions and cookie policy** to another beginner, show the normal and broken runs, explain the repair, and point to **identity and navigation checks versus server-side data and mutation authority**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
