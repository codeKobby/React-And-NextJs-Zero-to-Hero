# Day 082: Capstone build I: design system, shell, and database-backed reads

[← Previous lesson](../day_081_capstone_architecture_threat_model_and_delivery_plan/day_081_capstone_architecture_threat_model_and_delivery_plan.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_083_capstone_build_ii_auth_proxy_mutations_tests_and_portfolio_proof/day_083_capstone_build_ii_auth_proxy_mutations_tests_and_portfolio_proof.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [How do we turn the plan into a vertical slice?](#how-do-we-turn-the-plan-into-a-vertical-slice)
  - [Which UI primitives should be shared?](#which-ui-primitives-should-be-shared)
  - [How do Server Components read data?](#how-do-server-components-read-data)
  - [How do loading and error states complete the feature?](#how-do-loading-and-error-states-complete-the-feature)
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

Today we will learn **Capstone build I: design system, shell, and database-backed reads** in small steps. We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the preceding React/Next.js phases and a working local project**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Capstone build I: design system, shell, and database-backed reads** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **capstone build i: design system, shell, and database-backed reads** in a portfolio-ready local case-management feature with architecture and evidence notes.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: demo evidence versus production claims, operational ownership, and residual risk.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `capstone` | A final integrated project that demonstrates several learned boundaries together. |
| `Tailwind` | A shorthand reference to Tailwind CSS utility classes and its design-token workflow. |
| `shadcn/ui` | A source-owned collection of accessible UI component patterns that a project can inspect and customize. |
| `layout` | Shared route UI that wraps child pages and can persist while the child segment changes. |
| `loading` | A state in which work has started but its final result is not available yet. |
| `error` | A condition in which the intended operation could not complete or the program violated an assumption. |
| `database query` | A structured request that selects, inserts, updates, or deletes records in a database. |
| `DTO` | A data transfer object that exposes a deliberate boundary shape instead of passing an internal database row. |

## Topics

### How do we turn the plan into a vertical slice?

To answer **How do we turn the plan into a vertical slice**, follow the operation in order and check the example. For **How do we turn the plan into a vertical slice**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we turn the plan into a vertical slice**, change one input in the example. Write the old result and the new result for **How do we turn the plan into a vertical slice**.

### Which UI primitives should be shared?

Study **Which UI primitives should be shared** by looking at the value, operation, and result in the worked example. For **Which UI primitives should be shared**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Which UI primitives should be shared**, say what goes in and what comes out.

### How do Server Components read data?

To answer **How do Server Components read data**, follow the operation in order and check the example. For **How do Server Components read data**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do Server Components read data**, change one input in the example. Write the old result and the new result for **How do Server Components read data**.

### How do loading and error states complete the feature?

To answer **How do loading and error states complete the feature**, follow the operation in order and check the example. For **How do loading and error states complete the feature**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do loading and error states complete the feature**, change one input in the example. Write the old result and the new result for **How do loading and error states complete the feature**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly.

```tsx
export default async function CasesPage() {
  const cases = await listCasesForUser('synthetic-user');
  return <CaseTable rows={cases} />;
}
```

**Expected result or visible behavior:**

```text
The dashboard renders a typed, user-scoped synthetic case list with explicit loading and failure boundaries.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: demo evidence versus production claims, operational ownership, and residual risk.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `export default async function CasesPage() {` — Makes this value available to another file. |
| 2 | `const cases = await listCasesForUser('synthetic-user');` — Waits for the async task to finish before continuing. |
| 3 | `return <CaseTable rows={cases} />;` — Sends a value or UI tree back to the code that called this function. |
| 4 | `}` — Runs as part of this example. After `}`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Capstone build I: design system, shell, and database-backed reads**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Build the entire dashboard as one client component and pass raw database objects through it, then repair the vertical slice.

Make the broken version in a copy. The likely mistake is: Confuse a clean build or screenshot with proof that every user, permission, failure, and deployment condition is safe.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **capstone build i: design system, shell, and database-backed reads** and a portfolio-ready local case-management feature with architecture and evidence notes.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a portfolio-ready local case-management feature with architecture and evidence notes.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is demo evidence versus production claims, operational ownership, and residual risk.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Run the local database example. Write down the rows it returns.
2. Draw the tables and write one sentence about what each ID means.
3. Change one field or filter. Predict the new row before you run the query.
4. Show what the page displays when no row is found.
5. Make the missing-migration, raw-row, or wrong-user mistake from the lesson.
6. Fix the mistake and run the normal and rejected cases again.
7. Answer: which file talks to the database, and which file shows the page?
8. Add one transaction or rollback example if the lesson teaches it.
9. Write one test for the query’s normal result and one test for no result.
10. Build a small a portfolio-ready local case-management feature with architecture and evidence notes with resettable invented records.
11. Answer: how does the server stop one user from seeing another user’s record?
12. Write the migration command, query result, and one thing you did not test.

## Finish line

You are finished when you can:

1. explain **Capstone build I: design system, shell, and database-backed reads** to another beginner;
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
