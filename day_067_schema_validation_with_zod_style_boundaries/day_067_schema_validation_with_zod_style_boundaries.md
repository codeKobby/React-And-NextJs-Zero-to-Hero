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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will inspect raw input, define a schema, compare parse and safeParse, display field errors, and keep invalid data away from the mutation. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: Form data and request bodies arrive as untrusted values, but application code needs a precise shape before it can act. A receiving desk checks a package's label, size, and contents before sending it into the warehouse. This lesson teaches **Schema validation with Zod-style boundaries** through a connected sequence rather than a finished file dropped from the sky: We will inspect raw input, define a schema, compare parse and safeParse, display field errors, and keep invalid data away from the mutation. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **forms, objects, TypeScript shapes, and server/client boundaries**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **schema validation with zod-style boundaries** to a local case form with structured invalid-input feedback. You should be able to name the owner and boundary—untrusted input crossing into typed application logic—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

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

The answer to **Why validate at a boundary** must be earned by comparing a working case with a deliberately limited or broken case. For **Why validate at a boundary**, name the trade-off, the owner of the decision, and the visible consequence of choosing the other option. Keep the conclusion limited to the local evidence for **Why validate at a boundary**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Why validate at a boundary?**, compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a local case form with structured invalid-input feedback.

### What is the difference between parse and safeParse?

Start with the learner's concrete question: **What is the difference between parse and safeParse**. Use the worked example to show what **What is the difference between parse and safeParse** changes before introducing a framework shortcut. For **What is the difference between parse and safeParse**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is the difference between parse and safeParse**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is the difference between parse and safeParse?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do schemas describe form data?

To answer **How do schemas describe form data**, follow the operation in order rather than treating the result as framework magic. For **How do schemas describe form data**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do schemas describe form data**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do schemas describe form data?**, change one input or boundary in the worked example. Trace the result for **How do schemas describe form data?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### What must happen after validation fails?

Start with the learner's concrete question: **What must happen after validation fails**. Use the worked example to show what **What must happen after validation fails** changes before introducing a framework shortcut. For **What must happen after validation fails**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What must happen after validation fails**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What must happen after validation fails?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will inspect raw input, define a schema, compare parse and safeParse, display field errors, and keep invalid data away from the mutation.

```tsx
const CaseSchema = z.object({ title: z.string().min(1).max(120) });
const result = CaseSchema.safeParse({ title: formData.get('title') });
if (!result.success) return { error: 'Enter a case title.' };
```

**Expected result or visible behavior:**

```text
Invalid input becomes structured form state instead of reaching the mutation.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is untrusted input crossing into typed application logic.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const CaseSchema = z.object({ title: z.string().min(1).max(120) });` — Creates a named value from the expression on the right; record its input, lifetime, and owner in this day's example. |
| 2 | `const result = CaseSchema.safeParse({ title: formData.get('title') });` — Creates a named value from the expression on the right; record its input, lifetime, and owner in this day's example. |
| 3 | `if (!result.success) return { error: 'Enter a case title.' };` — Guards the next behavior with a deliberate condition; this is where the example chooses a normal, empty, invalid, or unauthorized path. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Form data and request bodies arrive as untrusted values, but application code needs a precise shape before it can act.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will inspect raw input, define a schema, compare parse and safeParse, display field errors, and keep invalid data away from the mutation.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Schema validation with Zod-style boundaries**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Trust formData.get('title') as a string and repair the schema boundary before calling the database.

Run the broken version in a local copy. The likely beginner mistake for this family is: Trust a form value because the input element looks constrained or use a type annotation as runtime validation. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **schema validation with zod-style boundaries** to a local case form with structured invalid-input feedback. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local case form with structured invalid-input feedback using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is untrusted input crossing into typed application logic. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Define **Why validate at a boundary?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **What is the difference between parse and safeParse?**, then predict before running.
5. Create a boundary case involving **How do schemas describe form data?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Trust formData.get('title') as a string and repair the schema boundary before calling the database.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply schema validation with zod-style boundaries to a local case form with structured invalid-input feedback with a local synthetic fixture.
11. Explain the owner and boundary: untrusted input crossing into typed application logic.
12. Write a review note with evidence, one limitation, and the next learning step.

## Finish line

You are finished when you can teach **Schema validation with Zod-style boundaries** to another beginner, show the normal and broken runs, explain the repair, and point to **untrusted input crossing into typed application logic**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
