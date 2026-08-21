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

Start with the [course README](../README.md), [setup guide](../SETUP.md), and [day index](../DAY_INDEX.md). Choose the starter from the [examples guide](../examples/README.md). Work locally with invented data only.

Today’s steps are simple: We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive. Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package.

A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable.

Today we will learn **Responsive layouts and design tokens with Tailwind** in small steps. We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive. You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **JSX, className, the Next.js starter, and basic CSS**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **Responsive layouts and design tokens with Tailwind** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **responsive layouts and design tokens with tailwind** in a local dashboard shell with a readable, keyboard-usable Button and empty state.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: design-system primitives versus feature-specific data, authorization, and application behavior.

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

Start with the learner's concrete question: **What is responsive design**. Look at **What is responsive design** in the example before learning the technical name. For **What is responsive design**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is responsive design**, say what goes in and what comes out.

### How do Tailwind breakpoints change a layout?

To answer **How do Tailwind breakpoints change a layout**, follow the operation in order rather than treating the result as framework magic. For **How do Tailwind breakpoints change a layout**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do Tailwind breakpoints change a layout**, change one input in the example. Write the old result and the new result for **How do Tailwind breakpoints change a layout**.

### What is a design token?

Start with the learner's concrete question: **What is a design token**. Look at **What is a design token** in the example before learning the technical name. For **What is a design token**, point to the smallest value, element, function, or route that shows the answer.

**Try it before moving on:** For **What is a design token**, say what goes in and what comes out.

### How do dark mode and contrast affect accessibility?

To answer **How do dark mode and contrast affect accessibility**, follow the operation in order rather than treating the result as framework magic. For **How do dark mode and contrast affect accessibility**, write the starting value, the change you made, and the new result.

**Try it before moving on:** For **How do dark mode and contrast affect accessibility**, change one input in the example. Write the old result and the new result for **How do dark mode and contrast affect accessibility**.

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive.

```tsx
<main className="bg-background text-foreground p-4 md:p-8 dark:bg-slate-950">
  <h1 className="text-2xl md:text-4xl">Case dashboard</h1>
</main>
```

**Expected result or visible behavior:**

```text
The layout adapts at the medium breakpoint and remains readable in dark mode.
```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: design-system primitives versus feature-specific data, authorization, and application behavior.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `<main className="bg-background text-foreground p-4 md:p-8 dark:bg-slate-950">` — Creates a piece of the UI or explains the code in a comment. |
| 2 | `<h1 className="text-2xl md:text-4xl">Case dashboard</h1>` — Creates a piece of the UI or explains the code in a comment. |
| 3 | `</main>` — Creates a piece of the UI or explains the code in a comment. |

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package.
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **Responsive layouts and design tokens with Tailwind**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Use arbitrary colors everywhere, create inconsistent contrast, and repair the design with named tokens and a contrast check.

Make the broken version in a copy. The likely mistake is: Copy a configuration from the wrong major version, scatter arbitrary colors, or treat generated component source as a black box.

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **responsive layouts and design tokens with tailwind** and a local dashboard shell with a readable, keyboard-usable Button and empty state.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build a local dashboard shell with a readable, keyboard-usable Button and empty state.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is design-system primitives versus feature-specific data, authorization, and application behavior.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

1. Run the route. Write down its URL and the text you see.
2. Write the job of each special file in one short sentence.
3. Change one folder or parameter. Predict the new URL before running it.
4. Add the missing, loading, or not-found message from the lesson.
5. Make the folder or file mistake shown in the lesson. Record the error.
6. Fix the mistake and open the route again.
7. Answer: which files are application code, and which files are project settings?
8. Add one real heading, link, or keyboard-friendly control to the page.
9. Write one browser check for the route’s visible text or URL.
10. Build a small a local dashboard shell with a readable, keyboard-usable Button and empty state and list its route URLs.
11. Answer: which data should stay on the server? Give one reason.
12. Write the file tree and one sentence about what you have not tested.

## Finish line

You are finished when you can:

1. explain **Responsive layouts and design tokens with Tailwind** to another beginner;
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
