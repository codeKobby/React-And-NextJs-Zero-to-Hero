# Day 057: Deployment and environment configuration

[← Previous lesson](../day_056_performance_and_bundle_boundaries/day_056_performance_and_bundle_boundaries.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_058_migration_from_pages_router_and_old_react/day_058_migration_from_pages_router_and_old_react.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is the production build?](#what-is-the-production-build)
  - [Which variables are public?](#which-variables-are-public)
  - [Where do secrets live?](#where-do-secrets-live)
  - [What should CI prove before deployment?](#what-should-ci-prove-before-deployment)
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

Today’s steps are simple: We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan.

A bridge is accepted with inspection records, load assumptions, emergency access, and maintenance plans, not only a photograph of one crossing.

Today we will learn **Deployment and environment configuration** in small steps. We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the preceding React/Next.js phases and a working local project**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Deployment and environment configuration** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **deployment and environment configuration** in a portfolio-ready local case-management feature with architecture and evidence notes.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: demo evidence versus production claims, operational ownership, and residual risk.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `build` | The process that checks, bundles, and prepares an application for a target environment. |
| `start` | The initial action or entry point that begins a documented learning or runtime flow. |
| `environment variable` | Configuration supplied outside source code, often used for deployment-specific values or secrets. |
| `secret` | Sensitive configuration or credential material that must not be exposed in client code or source control. |
| `runtime` | The environment and rules that execute code, such as a browser, Node.js, or the Next.js server. |
| `CI` | Continuous integration: an automated process that checks changes before they are merged or deployed. |

## Topics

### What is the production build?

Start with the learner's concrete question: **What is the production build**. Look at **What is the production build** in the example before learning the technical name. For **What is the production build**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is the production build**, say what goes in and what comes out.

### Which variables are public?

Study **Which variables are public** by looking at the value, operation, and result in the worked example. For **Which variables are public**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Which variables are public**, say what goes in and what comes out.

### Where do secrets live?

Study **Where do secrets live** by looking at the value, operation, and result in the worked example. For **Where do secrets live**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Where do secrets live**, say what goes in and what comes out.

### What should CI prove before deployment?

Start with the learner's concrete question: **What should CI prove before deployment**. Look at **What should CI prove before deployment** in the example before learning the technical name. For **What should CI prove before deployment**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What should CI prove before deployment**, say what goes in and what comes out.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly.

```tsx
npm run build
# production only
npm run start
```

**Expected result or visible behavior:**

```text
The app is built before it is started in production.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: demo evidence versus production claims, operational ownership, and residual risk.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `npm run build` — Runs as part of this example. After `npm run build`, check the next line to see the result. |
| 2 | `# production only` — Runs as part of this example. After `# production only`, check the next line to see the result. |
| 3 | `npm run start` — Runs as part of this example. After `npm run start`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Deployment and environment configuration**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Commit a secret in a local env file and repair the ignore and rotation plan.

Make the broken version in a copy. The likely mistake is: Confuse a clean build or screenshot with proof that every user, permission, failure, and deployment condition is safe.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **deployment and environment configuration** and a portfolio-ready local case-management feature with architecture and evidence notes.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a portfolio-ready local case-management feature with architecture and evidence notes.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is demo evidence versus production claims, operational ownership, and residual risk.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Answer the question **What is the production build?** in one sentence. Point to the example that helped you.
2. Run the example unchanged. Write down what appears.
3. Change one value. Predict the result, then run the code and compare.
4. Change one input in the example for **Which variables are public?**. Write down the old and new result.
5. Add one simple edge case for **Where do secrets live?**, such as an empty or invalid value.
6. Make the mistake shown in the lesson: Commit a secret in a local env file and repair the ignore and rotation plan.
7. Fix the mistake and run the normal example again.
8. Add one clear heading, label, error message, or type check that fits this lesson.
9. Write one check that fails when the important visible result disappears.
10. Build the small example from this lesson in the starter.
11. Answer: which file or function contains the important code? Give one simple reason.
12. Write four short sentences: what you built, what you saw, what you fixed, and what you did not test.

## Finish line

You are finished when you can:

1. explain **Deployment and environment configuration** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **demo evidence versus production claims, operational ownership, and residual risk**.

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
