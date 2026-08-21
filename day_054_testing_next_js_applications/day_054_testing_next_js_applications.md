# Day 054: Testing Next.js applications

[← Previous lesson](../day_053_authentication_and_authorization_boundaries/day_053_authentication_and_authorization_boundaries.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_055_accessibility_and_resilient_ui/day_055_accessibility_and_resilient_ui.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What should be tested at each level?](#what-should-be-tested-at-each-level)
  - [How do we test a Server Action?](#how-do-we-test-a-server-action)
  - [What is a safe fixture?](#what-is-a-safe-fixture)
  - [When is a browser test valuable?](#when-is-a-browser-test-valuable)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: A component can render and still be wrong for the user's actual journey, especially at empty, error, keyboard, or unauthorized boundaries. A rehearsal checks the actions a person must take, not whether the stage lights happen to turn on once. This lesson teaches **Testing Next.js applications** through a connected sequence rather than a finished file dropped from the sky: We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the component or route behavior being tested and a runnable starter**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **testing next.js applications** to a local synthetic case journey with normal, invalid, empty, and failure fixtures. You should be able to name the owner and boundary—the public behavior under test and the internal implementation that may change—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `unit test` | A focused test of one small function or component contract in isolation. |
| `integration test` | A test that checks a contract across more than one real application boundary. |
| `E2E` | End-to-end testing that follows a user or system journey across the running application. |
| `route handler` | A Next.js server file that handles an HTTP method such as GET or POST. |
| `fixture` | Controlled local data or setup used to make an example or test reproducible. |
| `mock` | A test replacement that stands in for a dependency with deliberately controlled behavior. |

## Topics

### What should be tested at each level?

Start with the learner's concrete question: **What should be tested at each level**. Use the worked example to show what **What should be tested at each level** changes before introducing a framework shortcut. For **What should be tested at each level**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What should be tested at each level**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What should be tested at each level?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do we test a Server Action?

To answer **How do we test a Server Action**, follow the operation in order rather than treating the result as framework magic. For **How do we test a Server Action**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we test a Server Action**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we test a Server Action?**, change one input or boundary in the worked example. Trace the result for **How do we test a Server Action?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### What is a safe fixture?

Start with the learner's concrete question: **What is a safe fixture**. Use the worked example to show what **What is a safe fixture** changes before introducing a framework shortcut. For **What is a safe fixture**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is a safe fixture**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is a safe fixture?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### When is a browser test valuable?

Treat **When is a browser test valuable** as a decision with a normal case, a boundary case, and a cost when chosen carelessly. For **When is a browser test valuable**, write one rule that accepts the normal case and one rule that handles the boundary safely. Keep the conclusion limited to the local evidence for **When is a browser test valuable**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **When is a browser test valuable?**, write a decision rule with one normal case and one boundary case. Include what would make the other option preferable.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness.

```tsx
const response = await POST(new Request('http://test/api/tasks', { method: 'POST', body }));
expect(response.status).toBe(400);
```

**Expected result or visible behavior:**

```text
Invalid input produces a tested boundary response.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the public behavior under test and the internal implementation that may change.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const response = await POST(new Request('http://test/api/tasks', { method: 'POST', body }));` — Pauses this async operation until its promise settles; identify whether the work runs on the server and how failure is handled. |
| 2 | `expect(response.status).toBe(400);` — Runs inside the current example; connect its effect to the public behavior under test and the internal implementation that may change. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A component can render and still be wrong for the user's actual journey, especially at empty, error, keyboard, or unauthorized boundaries.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Testing Next.js applications**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Mock every internal detail and replace it with a contract-focused test.

Run the broken version in a local copy. The likely beginner mistake for this family is: Assert a private implementation detail while skipping the visible contract the learner actually needs to protect. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **testing next.js applications** to a local synthetic case journey with normal, invalid, empty, and failure fixtures. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local synthetic case journey with normal, invalid, empty, and failure fixtures using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the public behavior under test and the internal implementation that may change. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. State one user-visible behavior the test should protect.
2. Run the smallest normal fixture and record the public output.
3. Add an empty, invalid, rejected, or unauthorized fixture.
4. Choose unit, integration, or browser coverage and justify the level.
5. Reproduce an assertion that checks a private implementation detail.
6. Repair it around the user-visible or route contract.
7. Add a keyboard, label, loading, or error assertion where appropriate.
8. Make the test fail by removing the behavior, then restore it.
9. Explain what the test cannot prove about production.
10. Apply the test plan to a local synthetic case journey with normal, invalid, empty, and failure fixtures with local synthetic data.
11. Document the public boundary under test: the public behavior under test and the internal implementation that may change.
12. Write a review note with commands, evidence, flaky-risk considerations, and residual risk.

## Finish line

You are finished when you can teach **Testing Next.js applications** to another beginner, show the normal and broken runs, explain the repair, and point to **the public behavior under test and the internal implementation that may change**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
