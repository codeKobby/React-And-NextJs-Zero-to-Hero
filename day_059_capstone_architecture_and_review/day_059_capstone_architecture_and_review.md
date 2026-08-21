# Day 059: Capstone architecture and review

[← Previous lesson](../day_058_migration_from_pages_router_and_old_react/day_058_migration_from_pages_router_and_old_react.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_060_final_demonstration_and_portfolio_review/day_060_final_demonstration_and_portfolio_review.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [How do we design a real app?](#how-do-we-design-a-real-app)
  - [Where do routes, components, data, and policies live?](#where-do-routes-components-data-and-policies-live)
  - [How do we document trade-offs?](#how-do-we-document-trade-offs)
  - [What evidence proves readiness?](#what-evidence-proves-readiness)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan. A bridge is accepted with inspection records, load assumptions, emergency access, and maintenance plans, not only a photograph of one crossing. This lesson teaches **Capstone architecture and review** through a connected sequence rather than a finished file dropped from the sky: We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the preceding React/Next.js phases and a working local project**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **capstone architecture and review** to a portfolio-ready local case-management feature with architecture and evidence notes. You should be able to name the owner and boundary—demo evidence versus production claims, operational ownership, and residual risk—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `architecture` | The arrangement of application boundaries, responsibilities, data flow, and deployment parts. |
| `feature boundary` | A code boundary that groups the UI, data, and policy for one user-facing capability. |
| `threat model` | A description of actors, assets, trust boundaries, threats, and mitigations for a system. |
| `test plan` | A written set of behaviors, fixtures, commands, and boundaries that testing will cover. |
| `observability` | The ability to understand system behavior through useful logs, measurements, traces, and events. |
| `trade-off` | A consequence accepted when choosing one design option over another. |

## Topics

### How do we design a real app?

To answer **How do we design a real app**, follow the operation in order rather than treating the result as framework magic. For **How do we design a real app**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we design a real app**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we design a real app?**, change one input or boundary in the worked example. Trace the result for **How do we design a real app?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### Where do routes, components, data, and policies live?

Study **Where do routes, components, data, and policies live** by naming the concrete value, operation, visible result, and owner in the worked example. For **Where do routes, components, data, and policies live**, underline the line or file where this idea becomes observable and explain what would change it. Keep the conclusion limited to the local evidence for **Where do routes, components, data, and policies live**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **Where do routes, components, data, and policies live?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do we document trade-offs?

To answer **How do we document trade-offs**, follow the operation in order rather than treating the result as framework magic. For **How do we document trade-offs**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we document trade-offs**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we document trade-offs?**, change one input or boundary in the worked example. Trace the result for **How do we document trade-offs?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### What evidence proves readiness?

Start with the learner's concrete question: **What evidence proves readiness**. Use the worked example to show what **What evidence proves readiness** changes before introducing a framework shortcut. For **What evidence proves readiness**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What evidence proves readiness**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What evidence proves readiness?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly.

```tsx
src/app/(dashboard)/cases/page.tsx
src/components/cases/CaseTable.tsx
src/lib/cases.ts
```

**Expected result or visible behavior:**

```text
The architecture makes boundaries reviewable.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is demo evidence versus production claims, operational ownership, and residual risk.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `src/app/(dashboard)/cases/page.tsx` — Runs inside the current example; connect its effect to demo evidence versus production claims, operational ownership, and residual risk. |
| 2 | `src/components/cases/CaseTable.tsx` — Runs inside the current example; connect its effect to demo evidence versus production claims, operational ownership, and residual risk. |
| 3 | `src/lib/cases.ts` — Runs inside the current example; connect its effect to demo evidence versus production claims, operational ownership, and residual risk. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Capstone architecture and review**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Add features without naming a boundary; repair by writing a one-page architecture decision.

Run the broken version in a local copy. The likely beginner mistake for this family is: Confuse a clean build or screenshot with proof that every user, permission, failure, and deployment condition is safe. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **capstone architecture and review** to a portfolio-ready local case-management feature with architecture and evidence notes. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a portfolio-ready local case-management feature with architecture and evidence notes using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is demo evidence versus production claims, operational ownership, and residual risk. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Define **How do we design a real app?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **Where do routes, components, data, and policies live?**, then predict before running.
5. Create a boundary case involving **How do we document trade-offs?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Add features without naming a boundary; repair by writing a one-page architecture decision.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply capstone architecture and review to a portfolio-ready local case-management feature with architecture and evidence notes with a local synthetic fixture.
11. Explain the owner and boundary: demo evidence versus production claims, operational ownership, and residual risk.
12. Write a review note with evidence, one limitation, and the next learning step.

## Finish line

You are finished when you can teach **Capstone architecture and review** to another beginner, show the normal and broken runs, explain the repair, and point to **demo evidence versus production claims, operational ownership, and residual risk**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
