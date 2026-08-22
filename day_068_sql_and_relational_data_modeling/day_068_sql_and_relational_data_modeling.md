# Day 068: SQL and relational data modeling

[← Previous lesson](../day_067_schema_validation_with_zod_style_boundaries/day_067_schema_validation_with_zod_style_boundaries.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_069_drizzle_orm_sqlite_migrations_and_seed_data/day_069_drizzle_orm_sqlite_migrations_and_seed_data.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a table?](#what-is-a-table)
  - [Why do rows need stable identifiers?](#why-do-rows-need-stable-identifiers)
  - [What is a foreign key?](#what-is-a-foreign-key)
  - [How do we model a case and its events?](#how-do-we-model-a-case-and-its-events)
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

Today’s steps are simple: We will model a table, create a local schema, migrate and seed it, query through a repository, and keep raw database details out of UI components. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: A growing application needs durable records and a data-access boundary that preserves ownership, migrations, and reviewability.

A case archive needs labeled shelves and a catalog; writing a note on a screen is not the same as storing a record safely.

Today we will learn **SQL and relational data modeling** in small steps. We will model a table, create a local schema, migrate and seed it, query through a repository, and keep raw database details out of UI components. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **objects, async functions, server-only modules, and the local project structure**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **SQL and relational data modeling** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **sql and relational data modeling** in a local synthetic case repository with typed reads and resettable seed data.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: database schema and repository versus UI data-transfer shape and authorization policy.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `SQL` | The language and query model commonly used to read and change relational database data. |
| `table` | A relational database structure containing rows with named columns. |
| `row` | One record or horizontal item in a table or data presentation. |
| `column` | One named field in a relational table, with a defined value type and constraints. |
| `primary key` | A database field or combination of fields that uniquely identifies a row. |
| `foreign key` | A database field that refers to a key in another table and represents a relationship. |
| `relation` | A connection between records or tables that describes how entities belong together. |

## Topics

### What is a table?

Start with the learner's concrete question: **What is a table**. Look at **What is a table** in the example before learning the technical name. For **What is a table**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is a table**, say what goes in and what comes out.

### Why do rows need stable identifiers?

Answer **Why do rows need stable identifiers** by comparing the working example with a broken or limited example. For **Why do rows need stable identifiers**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why do rows need stable identifiers?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### What is a foreign key?

Start with the learner's concrete question: **What is a foreign key**. Look at **What is a foreign key** in the example before learning the technical name. For **What is a foreign key**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is a foreign key**, say what goes in and what comes out.

### How do we model a case and its events?

To answer **How do we model a case and its events**, follow the operation in order and check the example. For **How do we model a case and its events**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we model a case and its events**, change one input in the example. Write the old result and the new result for **How do we model a case and its events**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will model a table, create a local schema, migrate and seed it, query through a repository, and keep raw database details out of UI components.

```tsx
CREATE TABLE cases (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  created_at TEXT NOT NULL
);
```

**Expected result or visible behavior:**

```text
The schema requires an ID, title, and creation timestamp for every case.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: database schema and repository versus UI data-transfer shape and authorization policy.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `CREATE TABLE cases (` — Runs as part of this example. After `CREATE TABLE cases (`, check the next line to see the result. |
| 2 | `id TEXT PRIMARY KEY,` — Runs as part of this example. After `id TEXT PRIMARY KEY,`, check the next line to see the result. |
| 3 | `title TEXT NOT NULL,` — Runs as part of this example. After `title TEXT NOT NULL,`, check the next line to see the result. |
| 4 | `created_at TEXT NOT NULL` — Runs as part of this example. After `created_at TEXT NOT NULL`, check the next line to see the result. |
| 5 | `);` — Runs as part of this example. After `);`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A growing application needs durable records and a data-access boundary that preserves ownership, migrations, and reviewability.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **SQL and relational data modeling**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Store a user name in every event row without a foreign key, then repair the model to preserve ownership and traceability.

Make the broken version in a copy. The likely mistake is: Change a schema without a migration, return another user's row, or pass raw database objects and secrets into a Client Component.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **sql and relational data modeling** and a local synthetic case repository with typed reads and resettable seed data.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local synthetic case repository with typed reads and resettable seed data.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is database schema and repository versus UI data-transfer shape and authorization policy.

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
10. Build a small a local synthetic case repository with typed reads and resettable seed data with resettable invented records.
11. Answer: how does the server stop one user from seeing another user’s record?
12. Write the migration command, query result, and one thing you did not test.

## Finish line

You are finished when you can:

1. explain **SQL and relational data modeling** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **database schema and repository versus UI data-transfer shape and authorization policy**.

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
