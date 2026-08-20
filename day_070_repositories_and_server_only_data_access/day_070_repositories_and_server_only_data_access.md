# Day 070: Repositories and server-only data access

[← Previous lesson](../day_069_drizzle_orm_sqlite_migrations_and_seed_data/day_069_drizzle_orm_sqlite_migrations_and_seed_data.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_071_server_actions_for_validated_mutations/day_071_server_actions_for_validated_mutations.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [Why isolate database calls?](#why-isolate-database-calls)
  - [What is a repository?](#what-is-a-repository)
  - [What data should cross into a Client Component?](#what-data-should-cross-into-a-client-component)
  - [Where should authorization occur?](#where-should-authorization-occur)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: Learners need a concrete reason to study repositories and server-only data access before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. This lesson teaches **Repositories and server-only data access** through a connected sequence rather than a finished file dropped from the sky: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **repositories and server-only data access** to a small local fixture that demonstrates repositories and server-only data access. You should be able to name the owner and boundary—the code or framework boundary that owns the decision in this lesson—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `repository` | A data-access module that hides storage details behind application-specific operations. |
| `data-access layer` | A module boundary that owns queries and maps storage results into deliberate application data. |
| `server-only` | A guard or convention that prevents private server modules from entering a browser bundle. |
| `query` | A request for records or information from a data source. |
| `DTO` | A data transfer object that exposes a deliberate boundary shape instead of passing an internal database row. |
| `authorization` | Deciding whether an identified actor may perform a requested action or access a record. |

## Topics

### Why isolate database calls?

The answer to **Why isolate database calls** must be earned through a visible comparison, not memorized as a slogan. The problem underneath this lesson is that learners need a concrete reason to study repositories and server-only data access before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a small local fixture that demonstrates repositories and server-only data access.

### What is a repository?

Start with the learner's concrete question: **What is a repository**. The problem underneath this lesson is that learners need a concrete reason to study repositories and server-only data access before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### What data should cross into a Client Component?

Start with the learner's concrete question: **What data should cross into a Client Component**. The problem underneath this lesson is that learners need a concrete reason to study repositories and server-only data access before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Where should authorization occur?

Study **Where should authorization occur** by naming its input, operation, visible result, and owner. The problem underneath this lesson is that learners need a concrete reason to study repositories and server-only data access before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.

```tsx
import 'server-only';

export async function listCasesForUser(userId: string) {
  return db.select().from(cases).where(eq(cases.ownerId, userId));
}
```

**Expected result or visible behavior:**

```text
The server-only repository returns only records belonging to the requested user.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the code or framework boundary that owns the decision in this lesson.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `import 'server-only';` — Imports a named dependency before the file uses it; check whether the imported API is browser-only, server-only, or shared. |
| 2 | Blank line: it separates the surrounding ideas; it has no runtime operation. |
| 3 | `export async function listCasesForUser(userId: string) {` — Makes this binding available to another module; the export is part of this lesson's public boundary. |
| 4 | `return db.select().from(cases).where(eq(cases.ownerId, userId));` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |
| 5 | `}` — Runs inside the current example; connect its effect to the code or framework boundary that owns the decision in this lesson. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Learners need a concrete reason to study repositories and server-only data access before the terminology becomes useful.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Repositories and server-only data access**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Import the repository into a Client Component and return database rows with secrets, then repair both boundaries.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy the syntax without identifying the input, owner, output, and boundary. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **repositories and server-only data access** to a small local fixture that demonstrates repositories and server-only data access. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a small local fixture that demonstrates repositories and server-only data access using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the code or framework boundary that owns the decision in this lesson. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

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
10. Apply the data boundary to a small local fixture that demonstrates repositories and server-only data access with resettable synthetic seed data.
11. Explain how authorization intersects with the code or framework boundary that owns the decision in this lesson.
12. Write a review note with schema evidence, migration state, query scope, and one limitation.

## Finish line

You are finished when you can teach **Repositories and server-only data access** to another beginner, show the normal and broken runs, explain the repair, and point to **the code or framework boundary that owns the decision in this lesson**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
