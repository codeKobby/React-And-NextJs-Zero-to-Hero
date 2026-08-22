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

Start with the [course README](../README.md), [setup guide](../SETUP.md), and [day index](../DAY_INDEX.md). Choose the starter from the [examples guide](../examples/README.md). Work locally with invented data only.

Today’s steps are simple: We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package.

A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable.

Today we will learn **shadcn/ui composition, theming, and accessible patterns** in small steps. We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **JSX, className, the Next.js starter, and basic CSS**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **shadcn/ui composition, theming, and accessible patterns** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **shadcn/ui composition, theming, and accessible patterns** in a local dashboard shell with a readable, keyboard-usable Button and empty state.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: design-system primitives versus feature-specific data, authorization, and application behavior.

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

Answer **Why compose primitives instead of copying a screenshot** by comparing the working example with a broken or limited example. For **Why compose primitives instead of copying a screenshot**, say what changed and which result is easier or safer to use.

**Try it before moving on:** For **Why compose primitives instead of copying a screenshot?**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?

### How does a Dialog manage focus?

To answer **How does a Dialog manage focus**, follow the operation in order and check the example. For **How does a Dialog manage focus**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How does a Dialog manage focus**, change one input in the example. Write the old result and the new result for **How does a Dialog manage focus**.

### How do labels and errors support forms?

To answer **How do labels and errors support forms**, follow the operation in order and check the example. For **How do labels and errors support forms**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do labels and errors support forms**, change one input in the example. Write the old result and the new result for **How do labels and errors support forms**.

### When should a table become a data grid?

Treat **When should a table become a data grid** as a simple choice. Start with a normal example and then try an empty or bad example. For **When should a table become a data grid**, write what the program should do in both examples.

**Try it before moving on:** For **When should a table become a data grid?**, write one normal example and one empty or bad example. Say what each should do.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive.

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

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: design-system primitives versus feature-specific data, authorization, and application behavior.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `<Dialog>` — Creates a piece of the UI or explains the code in a comment. |
| 2 | `<DialogTrigger asChild><Button>Review case</Button></DialogTrigger>` — Creates a piece of the UI or explains the code in a comment. |
| 3 | `<DialogContent><DialogTitle>Case details</DialogTitle></DialogContent>` — Creates a piece of the UI or explains the code in a comment. |
| 4 | `</Dialog>` — Creates a piece of the UI or explains the code in a comment. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **shadcn/ui composition, theming, and accessible patterns**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Build a click-only modal without a title or escape behavior, then repair the accessible dialog contract.

Make the broken version in a copy. The likely mistake is: Copy a configuration from the wrong major version, scatter arbitrary colors, or treat generated component source as a black box.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **shadcn/ui composition, theming, and accessible patterns** and a local dashboard shell with a readable, keyboard-usable Button and empty state.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local dashboard shell with a readable, keyboard-usable Button and empty state.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Run the starter. Write down the color, spacing, and button styles you see.
2. Style one component. Write down the visible change.
3. Make the layout change at one screen width. Check it in the browser.
4. Add a dark, empty, loading, or error message to the component.
5. Make the configuration or inaccessible-control mistake from the lesson.
6. Fix the mistake and run the page again.
7. Create one named color or spacing value and use it twice.
8. Check the button with the keyboard and check that the label is readable.
9. Write one DOM or visual check for the component.
10. Style a small a local dashboard shell with a readable, keyboard-usable Button and empty state without adding unrelated packages.
11. Answer: which styles belong to the reusable component, and which belong to this page?
12. Save one screenshot or DOM result and write one design choice you would revisit.

## Finish line

You are finished when you can:

1. explain **shadcn/ui composition, theming, and accessible patterns** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **design-system primitives versus feature-specific data, authorization, and application behavior**.

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
