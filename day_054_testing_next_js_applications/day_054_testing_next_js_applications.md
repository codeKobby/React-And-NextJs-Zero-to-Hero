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

Start with the [course README](../README.md), [setup guide](../SETUP.md), and [day index](../DAY_INDEX.md). Choose the starter from the [examples guide](../examples/README.md). Work locally with invented data only.

Today’s steps are simple: We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: A component can render and still be wrong for the user's actual journey, especially at empty, error, keyboard, or unauthorized boundaries.

A rehearsal checks the actions a person must take, not whether the stage lights happen to turn on once.

Today we will learn **Testing Next.js applications** in small steps. We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **the component or route behavior being tested and a runnable starter**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Testing Next.js applications** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **testing next.js applications** in a local synthetic case journey with normal, invalid, empty, and failure fixtures.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: the public behavior under test and the internal implementation that may change.

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

Start with the learner's concrete question: **What should be tested at each level**. Look at **What should be tested at each level** in the example before learning the technical name. For **What should be tested at each level**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What should be tested at each level**, say what goes in and what comes out.

### How do we test a Server Action?

To answer **How do we test a Server Action**, follow the operation in order rather than treating the result as framework magic. For **How do we test a Server Action**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we test a Server Action**, change one input in the example. Write the old result and the new result for **How do we test a Server Action**.

### What is a safe fixture?

Start with the learner's concrete question: **What is a safe fixture**. Look at **What is a safe fixture** in the example before learning the technical name. For **What is a safe fixture**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is a safe fixture**, say what goes in and what comes out.

### When is a browser test valuable?

Treat **When is a browser test valuable** as a simple choice. Start with a normal example and then try an empty or bad example. For **When is a browser test valuable**, write what the program should do in both examples.

**Try it before moving on:** For **When is a browser test valuable?**, write one normal example and one empty or bad example. Say what each should do.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness.

```tsx
const response = await POST(new Request('http://test/api/tasks', { method: 'POST', body }));
expect(response.status).toBe(400);
```

**Expected result or visible behavior:**

```text
Invalid input produces a tested boundary response.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: the public behavior under test and the internal implementation that may change.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `const response = await POST(new Request('http://test/api/tasks', { method: 'POST', body }));` — Waits for the async task to finish before continuing. |
| 2 | `expect(response.status).toBe(400);` — Runs as part of this example. After `expect(response.status).toBe(400);`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A component can render and still be wrong for the user's actual journey, especially at empty, error, keyboard, or unauthorized boundaries.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Testing Next.js applications**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Mock every internal detail and replace it with a contract-focused test.

Make the broken version in a copy. The likely mistake is: Assert a private implementation detail while skipping the visible contract the learner actually needs to protect.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **testing next.js applications** and a local synthetic case journey with normal, invalid, empty, and failure fixtures.

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

1. explain **Testing Next.js applications** to another beginner;
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
