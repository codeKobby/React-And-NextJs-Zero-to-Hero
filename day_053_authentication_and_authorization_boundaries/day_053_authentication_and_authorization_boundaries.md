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

Start with the [course README](../README.md), [setup guide](../SETUP.md), and [day index](../DAY_INDEX.md). Choose the starter from the [examples guide](../examples/README.md). Work locally with invented data only.

Today’s steps are simple: We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: A full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection.

A building entrance may check for a badge, but each room still checks whether the visitor is allowed to open the cabinet inside.

Today we will learn **Authentication and authorization boundaries** in small steps. We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **Next.js routing, server/client boundaries, cookies, and validation**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Authentication and authorization boundaries** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **authentication and authorization boundaries** in a local protected case route with synthetic sessions, permissions, and unauthorized fixtures.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: identity and navigation checks versus server-side data and mutation authority.

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

Start with the learner's concrete question: **What is the difference between authentication and authorization**. Look at **What is the difference between authentication and authorization** in the example before learning the technical name. For **What is the difference between authentication and authorization**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is the difference between authentication and authorization**, say what goes in and what comes out.

### Where should session checks run?

Study **Where should session checks run** by looking at the value, operation, and result in the worked example. For **Where should session checks run**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Where should session checks run**, say what goes in and what comes out.

### Why is a hidden button not authorization?

Answer **Why is a hidden button not authorization** by comparing the working example with a broken or limited example. For **Why is a hidden button not authorization**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why is a hidden button not authorization?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### How do roles limit data?

To answer **How do roles limit data**, follow the operation in order and check the example. For **How do roles limit data**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do roles limit data**, change one input in the example. Write the old result and the new result for **How do roles limit data**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors.

```tsx
const session = await requireSession();
if (!session.can('case:read')) notFound();
```

**Expected result or visible behavior:**

```text
The server enforces access before returning data.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: identity and navigation checks versus server-side data and mutation authority.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const session = await requireSession();` — Waits for the async task to finish before continuing. |
| 2 | `if (!session.can('case:read')) notFound();` — Checks a condition and runs the next code only when the condition is true. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Authentication and authorization boundaries**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Hide an admin link without protecting the route and repair the server-side check.

Make the broken version in a copy. The likely mistake is: Treat a browser field, client redirect, or login flag as proof of permission and return data before the server policy runs.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **authentication and authorization boundaries** and a local protected case route with synthetic sessions, permissions, and unauthorized fixtures.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local protected case route with synthetic sessions, permissions, and unauthorized fixtures.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is identity and navigation checks versus server-side data and mutation authority.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Run the signed-out example. Write down the page or message you see.
2. Run the signed-in example. Write down what changed.
3. Change one permission. Predict whether the request should be allowed or rejected.
4. Add one invented user who is not allowed to open the record.
5. Make the client-only protection mistake from the lesson. Record what it fails to protect.
6. Fix the check on the server and run the allowed and rejected cases again.
7. Write one sentence about the cookie or secret that must stay private.
8. Write one test that proves a forbidden user cannot read or change the record.
9. Answer: why is hiding a button not enough to protect data?
10. Protect a small a local protected case route with synthetic sessions, permissions, and unauthorized fixtures with invented users and records.
11. Draw one arrow showing where the user’s request meets the server’s permission check.
12. Write two things a real deployment would still need to check.

## Finish line

You are finished when you can:

1. explain **Authentication and authorization boundaries** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **identity and navigation checks versus server-side data and mutation authority**.

Do not move on only because the code compiles. Write one limitation of this local example.

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
