# Day 064: shadcn/ui installation and component ownership

[← Previous lesson](../day_063_responsive_layouts_and_design_tokens_with_tailwind/day_063_responsive_layouts_and_design_tokens_with_tailwind.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_065_shadcn_ui_composition_theming_and_accessible_patterns/day_065_shadcn_ui_composition_theming_and_accessible_patterns.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is shadcn/ui?](#what-is-shadcn-ui)
  - [Why does it copy component source into the project?](#why-does-it-copy-component-source-into-the-project)
  - [What does components.json configure?](#what-does-components-json-configure)
  - [How does the @ alias work with src/?](#how-does-the-alias-work-with-src)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: A page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate. A complete page is like a room with labeled areas: the labels help people find and change one responsibility without opening the whole building. This lesson teaches **shadcn/ui installation and component ownership** through a connected sequence rather than a finished file dropped from the sky: We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **JavaScript functions, JSX, and the local React playground**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **shadcn/ui installation and component ownership** to a local case dashboard built from a shell, summary, list, and card. You should be able to name the owner and boundary—the parent-to-child data flow and the responsibility owned by each component—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `shadcn/ui` | A source-owned collection of accessible UI component patterns that a project can inspect and customize. |
| `components.json` | Project configuration used by the shadcn/ui workflow to locate components, aliases, and styling conventions. |
| `CLI` | A command-line interface used to run a tool through a terminal. |
| `alias` | A shorter import name that maps to a longer filesystem or module path. |
| `generated source` | Code created by a tool from configuration or a schema, which should be understood before editing. |
| `composition` | Building a larger UI by placing smaller components together rather than inheriting from them. |

## Topics

### What is shadcn/ui?

Start with the learner's concrete question: **What is shadcn/ui**. The problem underneath this lesson is that a page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate. A complete page is like a room with labeled areas: the labels help people find and change one responsibility without opening the whole building. In this course's sequence, we will show one complete page, split it into header/main/footer, pass props to a reusable card, and compose a small dashboard. The relevant boundary is the parent-to-child data flow and the responsibility owned by each component.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### Why does it copy component source into the project?

The answer to **Why does it copy component source into the project** must be earned through a visible comparison, not memorized as a slogan. The problem underneath this lesson is that a page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate. A complete page is like a room with labeled areas: the labels help people find and change one responsibility without opening the whole building. In this course's sequence, we will show one complete page, split it into header/main/footer, pass props to a reusable card, and compose a small dashboard. The relevant boundary is the parent-to-child data flow and the responsibility owned by each component.

**Try it before moving on:** Compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a local case dashboard built from a shell, summary, list, and card.

### What does components.json configure?

Start with the learner's concrete question: **What does components.json configure**. The problem underneath this lesson is that a page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate. A complete page is like a room with labeled areas: the labels help people find and change one responsibility without opening the whole building. In this course's sequence, we will show one complete page, split it into header/main/footer, pass props to a reusable card, and compose a small dashboard. The relevant boundary is the parent-to-child data flow and the responsibility owned by each component.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How does the @ alias work with src/?

To answer **How does the @ alias work with src/**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that a page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate. A complete page is like a room with labeled areas: the labels help people find and change one responsibility without opening the whole building. In this course's sequence, we will show one complete page, split it into header/main/footer, pass props to a reusable card, and compose a small dashboard. The relevant boundary is the parent-to-child data flow and the responsibility owned by each component.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard.

```tsx
import { Button } from "@/components/ui/button";

export function SaveButton() {
  return <Button type="submit">Save case</Button>;
}
```

**Expected result or visible behavior:**

```text
The project owns and composes an accessible Button component.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is the parent-to-child data flow and the responsibility owned by each component.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `import { Button } from "@/components/ui/button";` — Imports a named dependency before the file uses it; check whether the imported API is browser-only, server-only, or shared. |
| 2 | Blank line: it separates the surrounding ideas; it has no runtime operation. |
| 3 | `export function SaveButton() {` — Makes this binding available to another module; the export is part of this lesson's public boundary. |
| 4 | `return <Button type="submit">Save case</Button>;` — Returns the value or UI tree owned by the surrounding function; the next visible result follows from this return. |
| 5 | `}` — Runs inside the current example; connect its effect to the parent-to-child data flow and the responsibility owned by each component. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **shadcn/ui installation and component ownership**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Install a component while the alias points at the wrong directory, then repair the src-aware paths configuration.

Run the broken version in a local copy. The likely beginner mistake for this family is: Split every element mechanically or use a lowercase component name that JSX treats as a browser element. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **shadcn/ui installation and component ownership** to a local case dashboard built from a shell, summary, list, and card. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local case dashboard built from a shell, summary, list, and card using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is the parent-to-child data flow and the responsibility owned by each component. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the smallest page unchanged and list its visible responsibilities.
2. Split one responsibility into a named component without changing the visible result.
3. Explain why the chosen boundary earns a name.
4. Pass one prop from the parent and render two different values.
5. Compose a parent with two children and draw the data direction.
6. Reproduce the lowercase-component mistake and record the result.
7. Repair the capitalization and rerun the normal case.
8. Add a stable local fixture and an empty or fallback state.
9. Add one semantic or keyboard-accessibility improvement.
10. Add an assertion for a visible component contract.
11. Apply the boundary to a local feature and name its owner.
12. Write a review note with the component tree, evidence, and one limitation.

## Finish line

You are finished when you can teach **shadcn/ui installation and component ownership** to another beginner, show the normal and broken runs, explain the repair, and point to **the parent-to-child data flow and the responsibility owned by each component**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
