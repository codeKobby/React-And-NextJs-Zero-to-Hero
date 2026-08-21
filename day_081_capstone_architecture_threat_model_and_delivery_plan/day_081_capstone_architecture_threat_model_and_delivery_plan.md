# Day 081: Capstone architecture, threat model, and delivery plan

[← Previous lesson](../day_080_production_configuration_ci_and_deployment_evidence/day_080_production_configuration_ci_and_deployment_evidence.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_082_capstone_build_i_design_system_shell_and_database_backed_reads/day_082_capstone_build_i_design_system_shell_and_database_backed_reads.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [How do we plan a full app?](#how-do-we-plan-a-full-app)
  - [What is a threat model?](#what-is-a-threat-model)
  - [How do UI, data, and policy boundaries fit together?](#how-do-ui-data-and-policy-boundaries-fit-together)
  - [What evidence defines done?](#what-evidence-defines-done)
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

The learner problem comes first: A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan. A bridge is accepted with inspection records, load assumptions, emergency access, and maintenance plans, not only a photograph of one crossing. This lesson teaches **Capstone architecture, threat model, and delivery plan** through a connected sequence rather than a finished file dropped from the sky: We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **the preceding React/Next.js phases and a working local project**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **capstone architecture, threat model, and delivery plan** to a portfolio-ready local case-management feature with architecture and evidence notes. You should be able to name the owner and boundary—demo evidence versus production claims, operational ownership, and residual risk—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `capstone` | A final integrated project that demonstrates several learned boundaries together. |
| `architecture decision` | A recorded choice about structure, trade-offs, and consequences in a system. |
| `threat model` | A description of actors, assets, trust boundaries, threats, and mitigations for a system. |
| `data model` | The structured representation of entities, fields, relationships, and constraints in an application. |
| `route map` | A written representation of URLs, route files, layouts, and boundaries in an application. |
| `acceptance criteria` | Observable statements that define what must be true before a feature is considered complete. |

## Topics

### How do we plan a full app?

To answer **How do we plan a full app**, follow the operation in order rather than treating the result as framework magic. For **How do we plan a full app**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do we plan a full app**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do we plan a full app?**, change one input or boundary in the worked example. Trace the result for **How do we plan a full app?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### What is a threat model?

Start with the learner's concrete question: **What is a threat model**. Use the worked example to show what **What is a threat model** changes before introducing a framework shortcut. For **What is a threat model**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What is a threat model**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What is a threat model?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do UI, data, and policy boundaries fit together?

To answer **How do UI, data, and policy boundaries fit together**, follow the operation in order rather than treating the result as framework magic. For **How do UI, data, and policy boundaries fit together**, write the input, the operation that changes it, the output, and the boundary that is responsible. Keep the conclusion limited to the local evidence for **How do UI, data, and policy boundaries fit together**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **How do UI, data, and policy boundaries fit together?**, change one input or boundary in the worked example. Trace the result for **How do UI, data, and policy boundaries fit together?** and identify which owner is responsible for the new behavior; record the concrete value or file that changed.

### What evidence defines done?

Start with the learner's concrete question: **What evidence defines done**. Use the worked example to show what **What evidence defines done** changes before introducing a framework shortcut. For **What evidence defines done**, point to the smallest value, element, function, route, or boundary that demonstrates the answer. Keep the conclusion limited to the local evidence for **What evidence defines done**; a small fixture cannot prove production security, accessibility, performance, or correctness.

**Try it before moving on:** For **What evidence defines done?**, point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly.

```tsx
src/app/(dashboard)/cases/page.tsx
src/components/ui/button.tsx
src/lib/db/schema.ts
src/lib/auth/require-permission.ts
proxy.ts
```

**Expected result or visible behavior:**

```text
The planned structure makes UI, data, and security boundaries reviewable.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is demo evidence versus production claims, operational ownership, and residual risk.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `src/app/(dashboard)/cases/page.tsx` — Runs inside the current example; connect its effect to demo evidence versus production claims, operational ownership, and residual risk. |
| 2 | `src/components/ui/button.tsx` — Runs inside the current example; connect its effect to demo evidence versus production claims, operational ownership, and residual risk. |
| 3 | `src/lib/db/schema.ts` — Runs inside the current example; connect its effect to demo evidence versus production claims, operational ownership, and residual risk. |
| 4 | `src/lib/auth/require-permission.ts` — Runs inside the current example; connect its effect to demo evidence versus production claims, operational ownership, and residual risk. |
| 5 | `proxy.ts` — Runs inside the current example; connect its effect to demo evidence versus production claims, operational ownership, and residual risk. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Capstone architecture, threat model, and delivery plan**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Start coding without identifying actors, assets, routes, and trust boundaries, then repair the plan before implementation.

Run the broken version in a local copy. The likely beginner mistake for this family is: Confuse a clean build or screenshot with proof that every user, permission, failure, and deployment condition is safe. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **capstone architecture, threat model, and delivery plan** to a portfolio-ready local case-management feature with architecture and evidence notes. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a portfolio-ready local case-management feature with architecture and evidence notes using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is demo evidence versus production claims, operational ownership, and residual risk. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Define **How do we plan a full app?** in your own words and point to its first concrete example.
2. Run the smallest worked example unchanged and record the expected and observed result.
3. Trace the important values, operations, output, and owner line by line.
4. Change one input while preserving the rule for **What is a threat model?**, then predict before running.
5. Create a boundary case involving **How do UI, data, and policy boundaries fit together?** and choose deliberate behavior.
6. Reproduce the deliberate failure: Start coding without identifying actors, assets, routes, and trust boundaries, then repair the plan before implementation.
7. Repair the smallest meaningful line or boundary and rerun normal and boundary cases.
8. Add one accessibility, type, loading, error, or server/client quality requirement.
9. Add a focused assertion that fails when the important behavior disappears.
10. Apply capstone architecture, threat model, and delivery plan to a portfolio-ready local case-management feature with architecture and evidence notes with a local synthetic fixture.
11. Explain the owner and boundary: demo evidence versus production claims, operational ownership, and residual risk.
12. Write a review note with evidence, one limitation, and the next learning step.

## Finish line

You are finished when you can teach **Capstone architecture, threat model, and delivery plan** to another beginner, show the normal and broken runs, explain the repair, and point to **demo evidence versus production claims, operational ownership, and residual risk**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
