# Day 069: Drizzle ORM, SQLite, migrations, and seed data

[← Previous lesson](../day_068_sql_and_relational_data_modeling/day_068_sql_and_relational_data_modeling.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_070_repositories_and_server_only_data_access/day_070_repositories_and_server_only_data_access.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does an ORM do?](#what-does-an-orm-do)
  - [Why are migrations committed?](#why-are-migrations-committed)
  - [What is seed data?](#what-is-seed-data)
  - [When should a transaction group changes?](#when-should-a-transaction-group-changes)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will model a table, create a local schema, migrate and seed it, query through a repository, and keep raw database details out of UI components. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: A growing application needs durable records and a data-access boundary that preserves ownership, migrations, and reviewability. A case archive needs labeled shelves and a catalog; writing a note on a screen is not the same as storing a record safely. This lesson teaches **Drizzle ORM, SQLite, migrations, and seed data** through a connected sequence rather than a finished file dropped from the sky: We will model a table, create a local schema, migrate and seed it, query through a repository, and keep raw database details out of UI components. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **objects, async functions, server-only modules, and the local project structure**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **drizzle orm, sqlite, migrations, and seed data** to a local synthetic case repository with typed reads and resettable seed data. You should be able to name the owner and boundary—database schema and repository versus UI data-transfer shape and authorization policy—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `Drizzle ORM` | A TypeScript-oriented database toolkit that represents SQL schemas and queries in application code. |
| `SQLite` | A file-based relational database useful for local development and bounded fixtures. |
| `migration` | A controlled change that moves an existing codebase, schema, or API to a new structure. |
| `schema` | A documented shape and set of constraints for data. |
| `seed` | Controlled initial data inserted into a local or test database so examples are repeatable. |
| `transaction` | A group of data operations that should commit together or roll back together. |

## Topics

### What does an ORM do?

Start with the learner's concrete question: **What does an ORM do**. Use the worked example to show what **What does an ORM do** changes before introducing a framework shortcut. For **What does an ORM do**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What does an ORM do**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What does an ORM do?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why are migrations committed?

The answer to **Why are migrations committed** must be earned by comparing a working case with a deliberately limited or broken case. For **Why are migrations committed**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why are migrations committed**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why are migrations committed?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a local synthetic case repository with typed reads and resettable seed data.

### What is seed data?

Start with the learner's concrete question: **What is seed data**. Use the worked example to show what **What is seed data** changes before introducing a framework shortcut. For **What is seed data**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is seed data**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is seed data?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### When should a transaction group changes?

Treat **When should a transaction group changes** as a decision with a normal case, a boundary case, and a cost when chosen carelessly. For **When should a transaction group changes**, write one rule that accepts the normal case and one rule that handles the boundary safely. Keep the conclusion limited to the local evidence for **When should a transaction group changes**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **When should a transaction group changes?**, write a decision rule with one normal case and one boundary case. Include what would make the other option preferable.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will model a table, create a local schema, migrate and seed it, query through a repository, and keep raw database details out of UI components.

```tsx
export const cases = sqliteTable('cases', {
  id: text('id').primaryKey(),
  title: text('title').notNull(),
});
```

**Expected result or visible behavior:**

```text
The typed schema maps application data to a local SQLite table.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is database schema and repository versus UI data-transfer shape and authorization policy.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `export const cases = sqliteTable('cases', {` — Makes this binding available to another module; the export is part of this lesson's public boundary. |
| 2 | `id: text('id').primaryKey(),` — Runs inside the current example; connect its effect to database schema and repository versus UI data-transfer shape and authorization policy. |
| 3 | `title: text('title').notNull(),` — Runs inside the current example; connect its effect to database schema and repository versus UI data-transfer shape and authorization policy. |
| 4 | `});` — Runs inside the current example; connect its effect to database schema and repository versus UI data-transfer shape and authorization policy. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A growing application needs durable records and a data-access boundary that preserves ownership, migrations, and reviewability.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will model a table, create a local schema, migrate and seed it, query through a repository, and keep raw database details out of UI components.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Drizzle ORM, SQLite, migrations, and seed data**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Change the TypeScript schema without generating a migration, then repair the workflow and test a fresh database.

Run the broken version in a local copy. The likely beginner mistake for this family is: Change a schema without a migration, return another user's row, or pass raw database objects and secrets into a Client Component. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **drizzle orm, sqlite, migrations, and seed data** to a local synthetic case repository with typed reads and resettable seed data. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local synthetic case repository with typed reads and resettable seed data using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is database schema and repository versus UI data-transfer shape and authorization policy. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

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
10. Apply the data boundary to a local synthetic case repository with typed reads and resettable seed data with resettable synthetic seed data.
11. Explain how authorization intersects with database schema and repository versus UI data-transfer shape and authorization policy.
12. Write a review note with schema evidence, migration state, query scope, and one limitation.

## Finish line

You are finished when you can teach **Drizzle ORM, SQLite, migrations, and seed data** to another beginner, show the normal and broken runs, explain the repair, and point to **database schema and repository versus UI data-transfer shape and authorization policy**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
