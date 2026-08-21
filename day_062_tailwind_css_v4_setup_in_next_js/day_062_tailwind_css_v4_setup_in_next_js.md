# Day 062: Tailwind CSS v4 setup in Next.js

[← Previous lesson](../day_061_getters_setters_and_state_boundaries/day_061_getters_setters_and_state_boundaries.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_063_responsive_layouts_and_design_tokens_with_tailwind/day_063_responsive_layouts_and_design_tokens_with_tailwind.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What problem does Tailwind CSS solve?](#what-problem-does-tailwind-css-solve)
  - [How does Tailwind CSS v4 enter a Next.js project?](#how-does-tailwind-css-v4-enter-a-next-js-project)
  - [What is a utility class?](#what-is-a-utility-class)
  - [How do we verify a styled component?](#how-do-we-verify-a-styled-component)
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

Today we will learn **Tailwind CSS v4 setup in Next.js** in small steps. We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **JSX, className, the Next.js starter, and basic CSS**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Tailwind CSS v4 setup in Next.js** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **tailwind css v4 setup in next.js** in a local dashboard shell with a readable, keyboard-usable Button and empty state.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: design-system primitives versus feature-specific data, authorization, and application behavior.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `Tailwind CSS` | A utility-first CSS framework whose classes compose layout, spacing, color, and responsive behavior. |
| `utility class` | A small CSS class representing one visual rule that can be composed with other utilities. |
| `PostCSS` | A CSS transformation pipeline that processes styles through configured plugins. |
| `global stylesheet` | CSS loaded for the application as a whole rather than scoped to one component. |
| `@import` | A declaration that reads a value exported by another module. |
| `responsive` | A layout or behavior that adapts to viewport size, input method, or device conditions. |

## Topics

### What problem does Tailwind CSS solve?

Start with the learner's concrete question: **What problem does Tailwind CSS solve**. Look at **What problem does Tailwind CSS solve** in the example before learning the technical name. For **What problem does Tailwind CSS solve**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What problem does Tailwind CSS solve**, say what goes in and what comes out.

### How does Tailwind CSS v4 enter a Next.js project?

To answer **How does Tailwind CSS v4 enter a Next.js project**, follow the operation in order rather than treating the result as framework magic. For **How does Tailwind CSS v4 enter a Next.js project**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How does Tailwind CSS v4 enter a Next.js project**, change one input in the example. Write the old result and the new result for **How does Tailwind CSS v4 enter a Next.js project**.

### What is a utility class?

Start with the learner's concrete question: **What is a utility class**. Look at **What is a utility class** in the example before learning the technical name. For **What is a utility class**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is a utility class**, say what goes in and what comes out.

### How do we verify a styled component?

To answer **How do we verify a styled component**, follow the operation in order rather than treating the result as framework magic. For **How do we verify a styled component**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do we verify a styled component**, change one input in the example. Write the old result and the new result for **How do we verify a styled component**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive.

```tsx
export default function Card() {
  return <article className="rounded-xl border p-6 shadow-sm">A local card</article>;
}
```

**Expected result or visible behavior:**

```text
A bordered card appears with spacing and a shadow.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: design-system primitives versus feature-specific data, authorization, and application behavior.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `export default function Card() {` — Makes this value available to another file. |
| 2 | `return <article className="rounded-xl border p-6 shadow-sm">A local card</article>;` — Sends a value or UI tree back to the code that called this function. |
| 3 | `}` — Runs as part of this example. After `}`, check the next line to see the result. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Tailwind CSS v4 setup in Next.js**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Install a v3-style configuration in a v4 project, then repair the PostCSS plugin and global CSS import.

Make the broken version in a copy. The likely mistake is: Copy a configuration from the wrong major version, scatter arbitrary colors, or treat generated component source as a black box.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **tailwind css v4 setup in next.js** and a local dashboard shell with a readable, keyboard-usable Button and empty state.

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

1. explain **Tailwind CSS v4 setup in Next.js** to another beginner;
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
