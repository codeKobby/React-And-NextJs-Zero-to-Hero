# Day 079: Full-stack testing with Playwright and synthetic fixtures

[← Previous lesson](../day_078_error_taxonomy_logging_and_instrumentation/day_078_error_taxonomy_logging_and_instrumentation.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_080_production_configuration_ci_and_deployment_evidence/day_080_production_configuration_ci_and_deployment_evidence.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What should each test level prove?](#what-should-each-test-level-prove)
  - [How do we test a protected route?](#how-do-we-test-a-protected-route)
  - [What is a safe fixture?](#what-is-a-safe-fixture)
  - [Why test a browser journey?](#why-test-a-browser-journey)
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

Today’s steps are simple: We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: A component can render and still be wrong for the user's actual journey, especially at empty, error, keyboard, or unauthorized boundaries.

A rehearsal checks the actions a person must take, not whether the stage lights happen to turn on once.

Today we will learn **Full-stack testing with Playwright and synthetic fixtures** in small steps. We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the component or route behavior being tested and a runnable starter**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Full-stack testing with Playwright and synthetic fixtures** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **full-stack testing with playwright and synthetic fixtures** in a local synthetic case journey with normal, invalid, empty, and failure fixtures.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the public behavior under test and the internal implementation that may change.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `unit test` | A focused test of one small function or component contract in isolation. |
| `integration test` | A test that checks a contract across more than one real application boundary. |
| `E2E` | End-to-end testing that follows a user or system journey across the running application. |
| `Playwright` | A browser automation and end-to-end testing tool for checking real user journeys. |
| `fixture` | Controlled local data or setup used to make an example or test reproducible. |
| `accessibility` | Designing and testing the interface so people using different abilities and input methods can complete tasks. |
| `regression` | A previously working behavior that breaks after a change. |

## Topics

### What should each test level prove?

Start with the learner's concrete question: **What should each test level prove**. Look at **What should each test level prove** in the example before learning the technical name. For **What should each test level prove**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What should each test level prove**, say what goes in and what comes out.

### How do we test a protected route?

To answer **How do we test a protected route**, follow the operation in order rather than treating the result as framework magic. For **How do we test a protected route**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we test a protected route**, change one input in the example. Write the old result and the new result for **How do we test a protected route**.

### What is a safe fixture?

Start with the learner's concrete question: **What is a safe fixture**. Look at **What is a safe fixture** in the example before learning the technical name. For **What is a safe fixture**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is a safe fixture**, say what goes in and what comes out.

### Why test a browser journey?

Answer **Why test a browser journey** by comparing the working example with a broken or limited example. For **Why test a browser journey**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why test a browser journey?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness.

```tsx
test('a learner can create a case', async ({ page }) => {
  await page.goto('/cases');
  await page.getByRole('button', { name: 'New case' }).click();
  await page.getByLabel('Title').fill('Synthetic case');
});
```

**Expected result or visible behavior:**

```text
The test follows a user-visible journey using invented data.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the public behavior under test and the internal implementation that may change.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `test('a learner can create a case', async ({ page }) => {` — Defines a function or component that can be used later. |
| 2 | `await page.goto('/cases');` — Waits for the async task to finish before continuing. |
| 3 | `await page.getByRole('button', { name: 'New case' }).click();` — Waits for the async task to finish before continuing. |
| 4 | `await page.getByLabel('Title').fill('Synthetic case');` — Waits for the async task to finish before continuing. |
| 5 | `});` — Runs as part of this example. After `});`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A component can render and still be wrong for the user's actual journey, especially at empty, error, keyboard, or unauthorized boundaries.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Full-stack testing with Playwright and synthetic fixtures**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Assert only that a private component function was called and skip the browser contract, then repair the test around user behavior.

Make the broken version in a copy. The likely mistake is: Assert a private implementation detail while skipping the visible contract the learner actually needs to protect.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **full-stack testing with playwright and synthetic fixtures** and a local synthetic case journey with normal, invalid, empty, and failure fixtures.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local synthetic case journey with normal, invalid, empty, and failure fixtures.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is the public behavior under test and the internal implementation that may change.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Write one sentence about the user action the test should protect.
2. Run the normal example and write down the result.
3. Add an empty, invalid, rejected, or unauthorized example.
4. Choose a unit, integration, or browser test and say what it will click or call.
5. Make the private-detail assertion mistake from the lesson.
6. Fix the test so it checks what the user can see or what the route returns.
7. Add one test for a keyboard, label, loading, or error result.
8. Remove the behavior and make sure the test fails; restore the behavior afterward.
9. Answer: what can this test not prove about a real deployment?
10. Test a small a local synthetic case journey with normal, invalid, empty, and failure fixtures with invented data.
11. Write the public button, page, or route that the test uses.
12. Write the commands, result, and one test case you would add next.

## Finish line

You are finished when you can:

1. explain **Full-stack testing with Playwright and synthetic fixtures** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **the public behavior under test and the internal implementation that may change**.

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
