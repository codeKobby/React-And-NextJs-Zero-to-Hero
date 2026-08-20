# Day 039: Next.js installation and project structure

[← Previous lesson](../day_038_testing_linting_and_project_delivery/day_038_testing_linting_and_project_delivery.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_040_root_app_versus_src_app/day_040_root_app_versus_src_app.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does create-next-app configure?](#what-does-create-next-app-configure)
  - [What belongs at the root?](#what-belongs-at-the-root)
  - [What is the App Router?](#what-is-the-app-router)
  - [What does the src choice change?](#what-does-the-src-choice-change)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: A new Next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous. A workshop needs a clear separation between tools, storage, and workbenches; two rooms claiming to be the same entrance create confusion. This lesson teaches **Next.js installation and project structure** through a connected sequence rather than a finished file dropped from the sky: We will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **React components, a terminal, Node.js, and the setup guide**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **next.js installation and project structure** to a small App Router starter whose source, configuration, and public assets have named homes. You should be able to name the owner and boundary—application source versus root configuration and the route files Next.js recognizes—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `create-next-app` | The official command-line starter that creates a Next.js project with selected options. |
| `App Router` | Next.js routing model where folders and special files define route segments and rendering boundaries. |
| `TypeScript` | A static type checker that catches many mismatches before JavaScript runs. |
| `ESLint` | A static analysis tool that reports code patterns which are incorrect, risky, or inconsistent with project rules. |
| `Tailwind` | A shorthand reference to Tailwind CSS utility classes and its design-token workflow. |
| `Turbopack` | A Next.js bundler and development engine that processes the module graph for fast feedback. |
| `src` | A conventional directory used to keep application source code separate from root configuration files. |

## Topics

### What does create-next-app configure?

Start with the learner's concrete question: **What does create-next-app configure**. The problem underneath this lesson is that a new next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous. A workshop needs a clear separation between tools, storage, and workbenches; two rooms claiming to be the same entrance create confusion. In this course's sequence, we will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout. The relevant boundary is application source versus root configuration and the route files Next.js recognizes.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### What belongs at the root?

Start with the learner's concrete question: **What belongs at the root**. The problem underneath this lesson is that a new next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous. A workshop needs a clear separation between tools, storage, and workbenches; two rooms claiming to be the same entrance create confusion. In this course's sequence, we will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout. The relevant boundary is application source versus root configuration and the route files Next.js recognizes.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### What is the App Router?

Start with the learner's concrete question: **What is the App Router**. The problem underneath this lesson is that a new next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous. A workshop needs a clear separation between tools, storage, and workbenches; two rooms claiming to be the same entrance create confusion. In this course's sequence, we will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout. The relevant boundary is application source versus root configuration and the route files Next.js recognizes.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### What does the src choice change?

Start with the learner's concrete question: **What does the src choice change**. The problem underneath this lesson is that a new next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous. A workshop needs a clear separation between tools, storage, and workbenches; two rooms claiming to be the same entrance create confusion. In this course's sequence, we will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout. The relevant boundary is application source versus root configuration and the route files Next.js recognizes.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout.

```tsx
src/app/page.tsx
src/app/layout.tsx
public/logo.svg
package.json
```

**Expected result or visible behavior:**

```text
The route code is separated from configuration.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is application source versus root configuration and the route files Next.js recognizes.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `src/app/page.tsx` — Runs inside the current example; connect its effect to application source versus root configuration and the route files Next.js recognizes. |
| 2 | `src/app/layout.tsx` — Runs inside the current example; connect its effect to application source versus root configuration and the route files Next.js recognizes. |
| 3 | `public/logo.svg` — Runs inside the current example; connect its effect to application source versus root configuration and the route files Next.js recognizes. |
| 4 | `package.json` — Runs inside the current example; connect its effect to application source versus root configuration and the route files Next.js recognizes. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A new Next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Next.js installation and project structure**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Create both app/ and src/app/ and explain which one Next.js uses.

Run the broken version in a local copy. The likely beginner mistake for this family is: Keep duplicate routers or treat generated configuration as magic that should never be inspected. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **next.js installation and project structure** to a small App Router starter whose source, configuration, and public assets have named homes. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a small App Router starter whose source, configuration, and public assets have named homes using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is application source versus root configuration and the route files Next.js recognizes. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Define **What does create-next-app configure?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **What belongs at the root?**, then predict before running.
5. Create a boundary case involving **What is the App Router?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Create both app/ and src/app/ and explain which one Next.js uses.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply next.js installation and project structure to a small App Router starter whose source, configuration, and public assets have named homes with a local synthetic fixture.
11. Explain the owner and boundary: application source versus root configuration and the route files Next.js recognizes.
12. Write a review note with evidence, one limitation, and the next learning step.

## Finish line

You are finished when you can teach **Next.js installation and project structure** to another beginner, show the normal and broken runs, explain the repair, and point to **application source versus root configuration and the route files Next.js recognizes**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
