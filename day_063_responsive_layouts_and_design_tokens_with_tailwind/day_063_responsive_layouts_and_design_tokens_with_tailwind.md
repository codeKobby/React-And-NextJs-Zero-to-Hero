# Day 063: Responsive layouts and design tokens with Tailwind

[← Previous lesson](../day_062_tailwind_css_v4_setup_in_next_js/day_062_tailwind_css_v4_setup_in_next_js.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_064_shadcn_ui_installation_and_component_ownership/day_064_shadcn_ui_installation_and_component_ownership.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is responsive design?](#what-is-responsive-design)
  - [How do Tailwind breakpoints change a layout?](#how-do-tailwind-breakpoints-change-a-layout)
  - [What is a design token?](#what-is-a-design-token)
  - [How do dark mode and contrast affect accessibility?](#how-do-dark-mode-and-contrast-affect-accessibility)
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

This lesson is one step in a connected path. Start with the [course README](../README.md), confirm the [setup guide](../SETUP.md), and use the [day index](../DAY_INDEX.md) to see the phase. Choose the appropriate local fixture from the [examples guide](../examples/README.md). Work locally with synthetic data only. The learning loop for today is: We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive. Run the first example unchanged, write a prediction, make one purposeful change, reproduce the stated mistake, repair it, and complete only the practice that fits this concept.

## Why this lesson exists

The learner problem comes first: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. This lesson teaches **Responsive layouts and design tokens with Tailwind** through a connected sequence rather than a finished file dropped from the sky: We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **JSX, className, the Next.js starter, and basic CSS**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **responsive layouts and design tokens with tailwind** to a local dashboard shell with a readable, keyboard-usable Button and empty state. You should be able to name the owner and boundary—design-system primitives versus feature-specific data, authorization, and application behavior—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `responsive` | A layout or behavior that adapts to viewport size, input method, or device conditions. |
| `breakpoint` | A responsive layout threshold at which the design changes to fit a different viewport condition. |
| `theme variable` | A named design token used to keep visual choices consistent across themes and components. |
| `dark mode` | A visual theme that uses alternate colors and surfaces for a darker display condition. |
| `token` | A small named design value, or a security value whose trust and lifetime must be documented. |
| `contrast` | The visual difference between foreground and background needed for readable and accessible content. |

## Topics

### What is responsive design?

Start with the learner's concrete question: **What is responsive design**. The problem underneath this lesson is that a full application needs consistent visual language and accessible controls without burying every decision in ad-hoc css or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. In this course's sequence, we will style one visible element, introduce tokens and responsive states, then own and compose an accessible ui primitive. The relevant boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do Tailwind breakpoints change a layout?

To answer **How do Tailwind breakpoints change a layout**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that a full application needs consistent visual language and accessible controls without burying every decision in ad-hoc css or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. In this course's sequence, we will style one visible element, introduce tokens and responsive states, then own and compose an accessible ui primitive. The relevant boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

### What is a design token?

Start with the learner's concrete question: **What is a design token**. The problem underneath this lesson is that a full application needs consistent visual language and accessible controls without burying every decision in ad-hoc css or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. In this course's sequence, we will style one visible element, introduce tokens and responsive states, then own and compose an accessible ui primitive. The relevant boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

**Try it before moving on:** Point to the exact line or file where this idea appears, then explain its input, visible result, and owner in your own words.

### How do dark mode and contrast affect accessibility?

To answer **How do dark mode and contrast affect accessibility**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that a full application needs consistent visual language and accessible controls without burying every decision in ad-hoc css or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. In this course's sequence, we will style one visible element, introduce tokens and responsive states, then own and compose an accessible ui primitive. The relevant boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive.

```tsx
<main className="bg-background text-foreground p-4 md:p-8 dark:bg-slate-950">
  <h1 className="text-2xl md:text-4xl">Case dashboard</h1>
</main>
```

**Expected result or visible behavior:**

```text
The layout adapts at the medium breakpoint and remains readable in dark mode.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is design-system primitives versus feature-specific data, authorization, and application behavior.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `<main className="bg-background text-foreground p-4 md:p-8 dark:bg-slate-950">` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |
| 2 | `<h1 className="text-2xl md:text-4xl">Case dashboard</h1>` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |
| 3 | `</main>` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **Responsive layouts and design tokens with Tailwind**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Use arbitrary colors everywhere, create inconsistent contrast, and repair the design with named tokens and a contrast check.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy a configuration from the wrong major version, scatter arbitrary colors, or treat generated component source as a black box. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **responsive layouts and design tokens with tailwind** to a local dashboard shell with a readable, keyboard-usable Button and empty state. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local dashboard shell with a readable, keyboard-usable Button and empty state using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is design-system primitives versus feature-specific data, authorization, and application behavior. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the smallest route or structure fixture and write its URL and visible result.
2. Map each relevant folder or special file to the route or boundary it creates.
3. Change one segment or parameter and predict the URL before running it.
4. Add a normal, missing, loading, or not-found case appropriate to the route.
5. Reproduce the duplicate-router, missing-file, or parameter-timing mistake.
6. Repair the folder, file, or async boundary with the smallest change.
7. Explain which code is application source and which remains root configuration.
8. Add a semantic link, heading, or focus behavior to the route UI.
9. Add a route-level assertion or browser check for the public contract.
10. Apply the lesson to a local dashboard shell with a readable, keyboard-usable Button and empty state and document the route map.
11. Explain what crosses the design-system primitives versus feature-specific data, authorization, and application behavior and what must stay private.
12. Write a review note with the URL, file map, evidence, and one deployment limitation.

## Finish line

You are finished when you can teach **Responsive layouts and design tokens with Tailwind** to another beginner, show the normal and broken runs, explain the repair, and point to **design-system primitives versus feature-specific data, authorization, and application behavior**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
