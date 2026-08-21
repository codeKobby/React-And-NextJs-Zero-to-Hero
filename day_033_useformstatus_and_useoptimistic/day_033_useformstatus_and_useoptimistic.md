# Day 033: useFormStatus and useOptimistic

[← Previous lesson](../day_032_useactionstate_and_form_actions/day_032_useactionstate_and_form_actions.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_034_metadata_refs_and_modern_react_dom/day_034_metadata_refs_and_modern_react_dom.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [How can a child button know a form is pending?](#how-can-a-child-button-know-a-form-is-pending)
  - [What is an optimistic update?](#what-is-an-optimistic-update)
  - [When must optimistic UI roll back?](#when-must-optimistic-ui-roll-back)
  - [How do we communicate uncertainty?](#how-do-we-communicate-uncertainty)
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

The learner problem comes first: Learners need a concrete reason to study useformstatus and useoptimistic before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. This lesson teaches **useFormStatus and useOptimistic** through a connected sequence rather than a finished file dropped from the sky: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **useformstatus and useoptimistic** to a small local fixture that demonstrates useformstatus and useoptimistic. You should be able to name the owner and boundary—the code or framework boundary that owns the decision in this lesson—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `useFormStatus` | A Hook that reads pending form submission status from a descendant form boundary. |
| `pending` | A period in which an operation has been requested but has not settled yet. |
| `optimistic update` | Showing an expected result before the server confirms it, with a plan for failure or rollback. |
| `rollback` | A planned way to return a deployment, migration, or change to a known working state. |
| `status` | A named condition such as idle, loading, success, empty, or error that guides visible behavior. |

## Topics

### How can a child button know a form is pending?

To answer **How can a child button know a form is pending**, follow the operation in order rather than treating the result as framework magic. For **How can a child button know a form is pending**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How can a child button know a form is pending**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How can a child button know a form is pending?**, change one input or boundary in the worked example. Trace the result for **How can a child button know a form is pending?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### What is an optimistic update?

Start with the learner's concrete question: **What is an optimistic update**. Use the worked example to show what **What is an optimistic update** changes before introducing a framework shortcut. For **What is an optimistic update**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is an optimistic update**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is an optimistic update?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### When must optimistic UI roll back?

Treat **When must optimistic UI roll back** as a decision with a normal case, a boundary case, and a cost when chosen carelessly. For **When must optimistic UI roll back**, write one rule that accepts the normal case and one rule that handles the boundary safely. Keep the conclusion limited to the local evidence for **When must optimistic UI roll back**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **When must optimistic UI roll back?**, write a decision rule with one normal case and one boundary case. Include what would make the other option preferable.

### How do we communicate uncertainty?

To answer **How do we communicate uncertainty**, follow the operation in order rather than treating the result as framework magic. For **How do we communicate uncertainty**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we communicate uncertainty**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we communicate uncertainty?**, change one input or boundary in the worked example. Trace the result for **How do we communicate uncertainty?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.

```tsx
const { pending } = useFormStatus();
const [optimistic, addOptimistic] = useOptimistic(items);
```

**Expected result or visible behavior:**

```text
The button disables while the action runs.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the code or framework boundary that owns the decision in this lesson.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const { pending } = useFormStatus();` — Creates a named value from the expression on the right; record its input, lifetime, and owner in this day's example. |
| 2 | `const [optimistic, addOptimistic] = useOptimistic(items);` — Creates a named value from the expression on the right; record its input, lifetime, and owner in this day's example. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Learners need a concrete reason to study useformstatus and useoptimistic before the terminology becomes useful.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **useFormStatus and useOptimistic**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Show an optimistic success without handling failure and add a rollback explanation.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy the syntax without identifying the input, owner, output, and boundary. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **useformstatus and useoptimistic** to a small local fixture that demonstrates useformstatus and useoptimistic. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a small local fixture that demonstrates useformstatus and useoptimistic using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the code or framework boundary that owns the decision in this lesson. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Define **How can a child button know a form is pending?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **What is an optimistic update?**, then predict before running.
5. Create a boundary case involving **When must optimistic UI roll back?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Show an optimistic success without handling failure and add a rollback explanation.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply useformstatus and useoptimistic to a small local fixture that demonstrates useformstatus and useoptimistic with a local synthetic fixture.
11. Explain the owner and boundary: the code or framework boundary that owns the decision in this lesson.
12. Write a review note with evidence, one limitation, and the next learning step.

## Finish line

You are finished when you can teach **useFormStatus and useOptimistic** to another beginner, show the normal and broken runs, explain the repair, and point to **the code or framework boundary that owns the decision in this lesson**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
