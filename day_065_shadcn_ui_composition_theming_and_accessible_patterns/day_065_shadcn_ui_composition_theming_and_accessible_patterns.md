# Day 065: shadcn/ui composition, theming, and accessible patterns

[← Previous lesson](../day_064_shadcn_ui_installation_and_component_ownership/day_064_shadcn_ui_installation_and_component_ownership.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_066_the_dashboard_shell_and_feature_based_boundaries/day_066_the_dashboard_shell_and_feature_based_boundaries.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [Why compose primitives instead of copying a screenshot?](#why-compose-primitives-instead-of-copying-a-screenshot)
  - [How does a Dialog manage focus?](#how-does-a-dialog-manage-focus)
  - [How do labels and errors support forms?](#how-do-labels-and-errors-support-forms)
  - [When should a table become a data grid?](#when-should-a-table-become-a-data-grid)
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

The learner problem comes first: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. This lesson teaches **shadcn/ui composition, theming, and accessible patterns** through a connected sequence rather than a finished file dropped from the sky: We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive. The goal is to explain the decision and its owner, not to memorize a spelling.

## Prerequisites

Complete the previous lesson and confirm the [setup guide](../SETUP.md). Today's minimum prerequisites are **JSX, className, the Next.js starter, and basic CSS**. If a command fails, stop at the first error and record the directory and command before changing anything. Use the [examples guide](../examples/README.md) to choose the starter; do not add a database, authentication provider, or unrelated dependency unless this lesson explicitly makes that boundary its subject.

## Outcomes

By the end, you should be able to explain the main idea in your own words, show the normal and broken behavior, trace the important values, predict a boundary result, and apply **shadcn/ui composition, theming, and accessible patterns** to a local dashboard shell with a readable, keyboard-usable Button and empty state. You should be able to name the owner and boundary—design-system primitives versus feature-specific data, authorization, and application behavior—and state what the example does not prove about production readiness, security, accessibility, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `Button` | A native interactive control that submits an action or performs a command when activated. |
| `Dialog` | A modal or non-modal surface that temporarily presents focused content and an interaction. |
| `Sheet` | A side or bottom surface used to present related controls while preserving the surrounding page context. |
| `Form` | A group of controls that collects named user input for a submit action. |
| `Label` | Visible text that names a form control and helps people understand what input it expects. |
| `data table` | A UI that presents records in rows and columns while supporting readable headers and states. |
| `ARIA` | Accessible Rich Internet Applications attributes that communicate roles, states, and relationships when native HTML is not enough. |
| `composition` | Building a larger UI by placing smaller components together rather than inheriting from them. |

## Topics

### Why compose primitives instead of copying a screenshot?

The answer to **Why compose primitives instead of copying a screenshot** must be earned through a visible comparison, not memorized as a slogan. The problem underneath this lesson is that a full application needs consistent visual language and accessible controls without burying every decision in ad-hoc css or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. In this course's sequence, we will style one visible element, introduce tokens and responsive states, then own and compose an accessible ui primitive. The relevant boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

**Try it before moving on:** Compare the smallest working case with the failure case. Record the trade-off and explain why the wrong choice would be costly for a local dashboard shell with a readable, keyboard-usable Button and empty state.

### How does a Dialog manage focus?

To answer **How does a Dialog manage focus**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that a full application needs consistent visual language and accessible controls without burying every decision in ad-hoc css or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. In this course's sequence, we will style one visible element, introduce tokens and responsive states, then own and compose an accessible ui primitive. The relevant boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

### How do labels and errors support forms?

To answer **How do labels and errors support forms**, follow the day's example one purposeful change at a time. The problem underneath this lesson is that a full application needs consistent visual language and accessible controls without burying every decision in ad-hoc css or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. In this course's sequence, we will style one visible element, introduce tokens and responsive states, then own and compose an accessible ui primitive. The relevant boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

**Try it before moving on:** Change one input or boundary in the worked example. Trace the result and identify which owner is responsible for the new behavior.

### When should a table become a data grid?

Treat **When should a table become a data grid** as a decision that has a normal case, a boundary case, and a cost when chosen carelessly. The problem underneath this lesson is that a full application needs consistent visual language and accessible controls without burying every decision in ad-hoc css or an opaque package. A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable. In this course's sequence, we will style one visible element, introduce tokens and responsive states, then own and compose an accessible ui primitive. The relevant boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

**Try it before moving on:** Write a decision rule with one normal case and one boundary case. Include what would make the other option preferable.

## Worked example

The worked example is the smallest useful fixture for this day. Copy it into the appropriate starter file, run it unchanged, and write down what you see before you improve it. The example is deliberately bounded: We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive.

```tsx
<Dialog>
  <DialogTrigger asChild><Button>Review case</Button></DialogTrigger>
  <DialogContent><DialogTitle>Case details</DialogTitle></DialogContent>
</Dialog>
```

**Expected result or visible behavior:**

```text
The trigger opens a titled dialog with an explicit focus and reading boundary.
```

Before changing the code, point to its input, operation, visible output, and owner. If the code is JSX, distinguish JavaScript expressions from markup. If it runs in Next.js, identify whether the file is a Server Component, Client Component, Route Handler, Server Action, or Proxy fixture. The exact boundary to inspect today is design-system primitives versus feature-specific data, authorization, and application behavior.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `<Dialog>` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |
| 2 | `<DialogTrigger asChild><Button>Review case</Button></DialogTrigger>` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |
| 3 | `<DialogContent><DialogTitle>Case details</DialogTitle></DialogContent>` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |
| 4 | `</Dialog>` — Declares UI structure or records an intentional comment; inspect the semantic element and the user-visible result. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. Start with the fixture's initial input: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package.
2. Follow the code until the first meaningful decision. Name the value, component, route, or server function that owns it.
3. Observe the event, render, request, update, or boundary that changes the result. This lesson's central sequence is: We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive.
4. Compare the actual output with your prediction and identify the smallest reason for any mismatch.
5. Treat the result as evidence about this local fixture, not proof that an untested production application is secure, accessible, performant, or correct.

Write the trace in your own notebook. Include the before value, the operation, the after value or response, and the boundary where authority changes.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input or boundary related to **shadcn/ui composition, theming, and accessible patterns**. Use a normal alternative first, then a boundary such as an empty value, invalid value, loading condition, missing route parameter, rejected action, unauthorized actor, or reordered record when it fits the lesson. Predict the visible output or error, run it, and explain the difference. Restore the original case to prove the repair preserved the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Build a click-only modal without a title or escape behavior, then repair the accessible dialog contract.

Run the broken version in a local copy. The likely beginner mistake for this family is: Copy a configuration from the wrong major version, scatter arbitrary colors, or treat generated component source as a black box. Capture the error or incorrect UI, name the violated assumption, and repair the smallest meaningful line or boundary. Rerun the normal case and one boundary case. Do not hide the failure with a broad catch, disable a type check, or call a passing render proof of authorization, accessibility, or security.

## Guided practice before independent work

First, reproduce the worked example unchanged. Second, change one input while keeping the rule fixed and record the visible difference. Third, reproduce the likely mistake and repair it with the smallest change. Fourth, start from the bounded local fixture and apply **shadcn/ui composition, theming, and accessible patterns** to a local dashboard shell with a readable, keyboard-usable Button and empty state. Before independent work, answer: what is the owner, what crosses the boundary, what is the normal case, and what should happen when the work is empty, invalid, loading, rejected, or unauthorized?

## Project application

Apply the lesson to a local dashboard shell with a readable, keyboard-usable Button and empty state using the local fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the owner, the data shape, the normal case, and the boundary case. The key boundary to document is design-system primitives versus feature-specific data, authorization, and application behavior. If the work touches a secret, database, cookie, authentication, or authorization decision, keep it server-side and test an unauthorized synthetic actor. If it is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Run the starter and identify the existing visual tokens or utility classes.
2. Style one component with a small, readable set of utilities and predict the visible result.
3. Add a responsive state and explain which breakpoint changes the layout.
4. Create a dark, empty, loading, or error visual state appropriate to the feature.
5. Reproduce the wrong-version configuration, alias, or inaccessible primitive mistake.
6. Repair the configuration or component while keeping the source owned by the project.
7. Add a named token or variant instead of scattering arbitrary colors.
8. Check keyboard focus, labels, contrast, and semantic elements.
9. Add a visual or DOM assertion for the component contract.
10. Apply the design boundary to a local dashboard shell with a readable, keyboard-usable Button and empty state.
11. Explain the boundary between a reusable primitive and design-system primitives versus feature-specific data, authorization, and application behavior.
12. Write a review note with screenshots or DOM evidence, trade-offs, and one limitation.

## Finish line

You are finished when you can teach **shadcn/ui composition, theming, and accessible patterns** to another beginner, show the normal and broken runs, explain the repair, and point to **design-system primitives versus feature-specific data, authorization, and application behavior**. You should be able to name one limitation and one piece of evidence that would be required before making a production claim. Do not move on because the code merely compiles.

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
