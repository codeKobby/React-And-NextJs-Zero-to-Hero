# Day 067: Schema validation with Zod-style boundaries

[← Previous lesson](../day_066_the_dashboard_shell_and_feature_based_boundaries/day_066_the_dashboard_shell_and_feature_based_boundaries.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_068_sql_and_relational_data_modeling/day_068_sql_and_relational_data_modeling.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [Why validate at a boundary?](#why-validate-at-a-boundary)
  - [What is the difference between parse and safeParse?](#what-is-the-difference-between-parse-and-safeparse)
  - [How do schemas describe form data?](#how-do-schemas-describe-form-data)
  - [What must happen after validation fails?](#what-must-happen-after-validation-fails)
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

Today’s steps are simple: We will inspect raw input, define a schema, compare parse and safeParse, display field errors, and keep invalid data away from the mutation. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: Form data and request bodies arrive as untrusted values, but application code needs a precise shape before it can act.

A receiving desk checks a package's label, size, and contents before sending it into the warehouse.

Today we will learn **Schema validation with Zod-style boundaries** in small steps. We will inspect raw input, define a schema, compare parse and safeParse, display field errors, and keep invalid data away from the mutation. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **forms, objects, TypeScript shapes, and server/client boundaries**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Schema validation with Zod-style boundaries** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **schema validation with zod-style boundaries** in a local case form with structured invalid-input feedback.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: untrusted input crossing into typed application logic.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `schema` | A documented shape and set of constraints for data. |
| `parse` | Reading an input representation and converting it into a structured value or a deliberate failure. |
| `safeParse` | A validation operation that returns a success or failure result without throwing for expected invalid input. |
| `validation` | A check that an input has the shape and values a boundary is prepared to handle. |
| `coercion` | An implicit or explicit conversion of a value from one JavaScript type to another. |
| `trusted data` | Data that has passed the required validation and authority checks for the current boundary. |

## Topics

### Why validate at a boundary?

Answer **Why validate at a boundary** by comparing the working example with a broken or limited example. For **Why validate at a boundary**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why validate at a boundary?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### What is the difference between parse and safeParse?

Start with the learner's concrete question: **What is the difference between parse and safeParse**. Look at **What is the difference between parse and safeParse** in the example before learning the technical name. For **What is the difference between parse and safeParse**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is the difference between parse and safeParse**, say what goes in and what comes out.

### How do schemas describe form data?

To answer **How do schemas describe form data**, follow the operation in order rather than treating the result as framework magic. For **How do schemas describe form data**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do schemas describe form data**, change one input in the example. Write the old result and the new result for **How do schemas describe form data**.

### What must happen after validation fails?

Start with the learner's concrete question: **What must happen after validation fails**. Look at **What must happen after validation fails** in the example before learning the technical name. For **What must happen after validation fails**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What must happen after validation fails**, say what goes in and what comes out.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will inspect raw input, define a schema, compare parse and safeParse, display field errors, and keep invalid data away from the mutation.

```tsx
const CaseSchema = z.object({ title: z.string().min(1).max(120) });
const result = CaseSchema.safeParse({ title: formData.get('title') });
if (!result.success) return { error: 'Enter a case title.' };
```

**Expected result or visible behavior:**

```text
Invalid input becomes structured form state instead of reaching the mutation.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: untrusted input crossing into typed application logic.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const CaseSchema = z.object({ title: z.string().min(1).max(120) });` — Stores the value on the right under the name on the left. |
| 2 | `const result = CaseSchema.safeParse({ title: formData.get('title') });` — Stores the value on the right under the name on the left. |
| 3 | `if (!result.success) return { error: 'Enter a case title.' };` — Checks a condition and runs the next code only when the condition is true. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: Form data and request bodies arrive as untrusted values, but application code needs a precise shape before it can act.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Schema validation with Zod-style boundaries**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Trust formData.get('title') as a string and repair the schema boundary before calling the database.

Make the broken version in a copy. The likely mistake is: Trust a form value because the input element looks constrained or use a type annotation as runtime validation.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **schema validation with zod-style boundaries** and a local case form with structured invalid-input feedback.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local case form with structured invalid-input feedback.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is untrusted input crossing into typed application logic.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Answer the question **Why validate at a boundary?** in one sentence. Point to the example that helped you.
2. Run the example unchanged. Write down what appears.
3. Change one value. Predict the result, then run the code and compare.
4. Change one input in the example for **What is the difference between parse and safeParse?**. Write down the old and new result.
5. Add one simple edge case for **How do schemas describe form data?**, such as an empty or invalid value.
6. Make the mistake shown in the lesson: Trust formData.get('title') as a string and repair the schema boundary before calling the database.
7. Fix the mistake and run the normal example again.
8. Add one clear heading, label, error message, or type check that fits this lesson.
9. Write one check that fails when the important visible result disappears.
10. Build the small example from this lesson in the starter.
11. Answer: which file or function contains the important code? Give one simple reason.
12. Write four short sentences: what you built, what you saw, what you fixed, and what you did not test.

## Finish line

You are finished when you can:

1. explain **Schema validation with Zod-style boundaries** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **untrusted input crossing into typed application logic**.

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
