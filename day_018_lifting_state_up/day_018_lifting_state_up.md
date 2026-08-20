# Day 018: Lifting state up

[← Previous lesson](../day_017_uncontrolled_inputs_and_refs/day_017_uncontrolled_inputs_and_refs.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_019_reducers_and_dispatch/day_019_reducers_and_dispatch.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [When should state move to a parent?](#when-should-state-move-to-a-parent)
  - [How do siblings share state?](#how-do-siblings-share-state)
  - [What belongs in the parent?](#what-belongs-in-the-parent)
  - [How do callbacks move intent upward?](#how-do-callbacks-move-intent-upward)
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

The learner problem comes first: Learners need a concrete reason to study lifting state up before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. This lesson teaches **Lifting state up** through a connected sequence rather than a finished file dropped from the sky: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the previous lesson, the setup guide, and the smallest prerequisite named in the opening**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **lifting state up** to a small local fixture that demonstrates lifting state up. You should be able to name the owner and boundary—the code or framework boundary that owns the decision in this lesson—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `lifting state` | Moving shared state to the nearest common owner so multiple children can use one source of truth. |
| `shared state` | State that multiple components need to read or change through a common owner. |
| `parent` | A component or route that renders or owns a nested child boundary. |
| `callback` | A function handed to another system so it can invoke the behavior later. |
| `synchronization` | Keeping an external system aligned with the current React inputs after a render. |

## Topics

### When should state move to a parent?

Treat **When should state move to a parent** as a decision that has a normal case, a boundary case, and a cost when chosen carelessly. The problem underneath this lesson is that learners need a concrete reason to study lifting state up before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Write a decision rule with one normal case and one boundary case. Include what would make the other option preferable.

### How do siblings share state?

To answer **How do siblings share state**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that learners need a concrete reason to study lifting state up before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

### What belongs in the parent?

Start with the learner's concrete question: **What belongs in the parent**. The problem underneath this lesson is that learners need a concrete reason to study lifting state up before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do callbacks move intent upward?

To answer **How do callbacks move intent upward**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that learners need a concrete reason to study lifting state up before the terminology becomes useful. A small workshop task gives the learner something visible to change before the tool's name matters. In this course's sequence, we will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture. The relevant boundary is the code or framework boundary that owns the decision in this lesson.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.

```tsx
<Editor value={text} onChange={setText} />
<Preview value={text} />
```

**Expected result or visible behavior:**

```text
Both children show the same source.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the code or framework boundary that owns the decision in this lesson.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `<Editor value={text} onChange={setText} />` — Connects a browser event to a handler without calling the handler during render; the event supplies the later input. |
| 2 | `<Preview value={text} />` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: Learners need a concrete reason to study lifting state up before the terminology becomes useful.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will run a smallest example, change one input, inspect the result, reproduce a likely mistake, and apply the idea to a local fixture.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Lifting state up**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Give each sibling its own text state and repair the split-brain UI.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy the syntax without identifying the input, owner, output, and boundary. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **lifting state up** to a small local fixture that demonstrates lifting state up. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a small local fixture that demonstrates lifting state up using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the code or framework boundary that owns the decision in this lesson. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the smallest state example and record the initial visible snapshot.
2. Trigger one update and trace event, setter or dispatch, and next render.
3. Change one input and predict the new output before running it.
4. Create a normal boundary such as empty, reset, or zero state.
5. Reproduce the likely state ownership or mutation mistake.
6. Repair it with the smallest state-structure change.
7. Compare the current state value with the source that derives it.
8. Add a user-visible status or accessible announcement for the transition.
9. Add an assertion or test for normal and boundary behavior.
10. Apply the lesson to a small local fixture that demonstrates lifting state up using synthetic data.
11. Explain why the state belongs at the the code or framework boundary that owns the decision in this lesson.
12. Write a review note naming the next complexity that would justify a different tool.

## Finish line

You are finished when you can teach **Lifting state up** to another beginner, show the normal and broken runs, explain the repair, and point to **the code or framework boundary that owns the decision in this lesson**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
