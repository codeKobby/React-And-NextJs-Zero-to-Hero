# Day 066: The dashboard shell and feature-based boundaries

[← Previous lesson](../day_065_shadcn_ui_composition_theming_and_accessible_patterns/day_065_shadcn_ui_composition_theming_and_accessible_patterns.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_067_schema_validation_with_zod_style_boundaries/day_067_schema_validation_with_zod_style_boundaries.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What makes a dashboard shell?](#what-makes-a-dashboard-shell)
  - [How do route groups organize features?](#how-do-route-groups-organize-features)
  - [Where should navigation state live?](#where-should-navigation-state-live)
  - [How do feature folders reduce coupling?](#how-do-feature-folders-reduce-coupling)
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

Today’s steps are simple: We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: The learner needs to see what the dashboard shell and feature-based boundaries does before learning its name.

A small workshop task lets the learner change one thing and see the result.

Today we will learn **The dashboard shell and feature-based boundaries** in small steps. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **The dashboard shell and feature-based boundaries** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **the dashboard shell and feature-based boundaries** in a small local example.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the line or file that changes the result.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `dashboard` | A route or screen that summarizes important records, statuses, actions, or navigation. |
| `navigation` | Moving from one URL or route state to another while preserving the intended user journey. |
| `route group` | A parenthesized App Router folder used for organization or layout without adding a URL segment. |
| `feature boundary` | A code boundary that groups the UI, data, and policy for one user-facing capability. |
| `layout` | Shared route UI that wraps child pages and can persist while the child segment changes. |
| `sidebar` | Persistent navigation or context UI that sits beside the main content in a layout. |

## Topics

### What makes a dashboard shell?

Start with the learner's concrete question: **What makes a dashboard shell**. Look at **What makes a dashboard shell** in the example before learning the technical name. For **What makes a dashboard shell**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What makes a dashboard shell**, say what goes in and what comes out.

### How do route groups organize features?

To answer **How do route groups organize features**, follow the operation in order rather than treating the result as framework magic. For **How do route groups organize features**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do route groups organize features**, change one input in the example. Write the old result and the new result for **How do route groups organize features**.

### Where should navigation state live?

Study **Where should navigation state live** by looking at the value, operation, and result in the worked example. For **Where should navigation state live**, point to the line that shows the idea and say what would change it.

**Try it before moving on:** For **Where should navigation state live**, say what goes in and what comes out.

### How do feature folders reduce coupling?

To answer **How do feature folders reduce coupling**, follow the operation in order rather than treating the result as framework magic. For **How do feature folders reduce coupling**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do feature folders reduce coupling**, change one input in the example. Write the old result and the new result for **How do feature folders reduce coupling**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.

```tsx
src/app/(dashboard)/layout.tsx
src/app/(dashboard)/cases/page.tsx
src/components/cases/CaseTable.tsx
src/lib/cases/queries.ts
```

**Expected result or visible behavior:**

```text
The shell persists while the cases route changes inside it.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the line or file that changes the result.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `src/app/(dashboard)/layout.tsx` — Runs as part of this example. After `src/app/(dashboard)/layout.tsx`, check the next line to see the result. |
| 2 | `src/app/(dashboard)/cases/page.tsx` — Runs as part of this example. After `src/app/(dashboard)/cases/page.tsx`, check the next line to see the result. |
| 3 | `src/components/cases/CaseTable.tsx` — Runs as part of this example. After `src/components/cases/CaseTable.tsx`, check the next line to see the result. |
| 4 | `src/lib/cases/queries.ts` — Runs as part of this example. After `src/lib/cases/queries.ts`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: The learner needs to see what the dashboard shell and feature-based boundaries does before learning its name.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **The dashboard shell and feature-based boundaries**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Put database queries, navigation, and visual components in one file, then repair the feature boundaries.

Make the broken version in a copy. The likely mistake is: Copy the code without checking the input and the result.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **the dashboard shell and feature-based boundaries** and a small local example.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a small local example.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the line or file that changes the result.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Answer the question **What makes a dashboard shell?** in one sentence. Point to the example that helped you.
2. Run the example unchanged. Write down what appears.
3. Change one value. Predict the result, then run the code and compare.
4. Change one input in the example for **How do route groups organize features?**. Write down the old and new result.
5. Add one simple edge case for **Where should navigation state live?**, such as an empty or invalid value.
6. Make the mistake shown in the lesson: Put database queries, navigation, and visual components in one file, then repair the feature boundaries.
7. Fix the mistake and run the normal example again.
8. Add one clear heading, label, error message, or type check that fits this lesson.
9. Write one check that fails when the important visible result disappears.
10. Build the small example from this lesson in the starter.
11. Answer: which file or function contains the important code? Give one simple reason.
12. Write four short sentences: what you built, what you saw, what you fixed, and what you did not test.

## Finish line

You are finished when you can:

1. explain **The dashboard shell and feature-based boundaries** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **the line or file that changes the result**.

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
