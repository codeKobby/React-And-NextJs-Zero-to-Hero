# Day 002: HTML, CSS, accessibility, and the DOM

[← Previous lesson](../day_001_javascript_modules_and_the_browser_runtime/day_001_javascript_modules_and_the_browser_runtime.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_003_modern_javascript_for_react/day_003_modern_javascript_for_react.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does a browser actually display?](#what-does-a-browser-actually-display)
  - [What is HTML responsible for?](#what-is-html-responsible-for)
  - [What is CSS responsible for?](#what-is-css-responsible-for)
  - [What is the DOM?](#what-is-the-dom)
  - [What does accessibility mean here?](#what-does-accessibility-mean-here)
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

This is a **conceptual orientation day**. It deliberately does not ask you to write a React component or complete a programming exercise. Open a browser, visit any page you are allowed to inspect, and use the browser's accessibility or element inspector. The purpose is to give names to things you can already observe before JavaScript and React add more layers.

Read the [README](../README.md), confirm the [setup guide](../SETUP.md), keep the [day index](../DAY_INDEX.md) nearby, and open the [examples guide](../examples/README.md) only when you are ready to inspect the starter. If you are completely new, it is fine to finish this lesson with notes and observations rather than a new source file.

## Why this lesson exists

A React component eventually becomes browser output. If a learner thinks React is drawing pixels directly, JSX and props feel like magic. React actually describes elements, attributes, and relationships that become part of a document. HTML gives meaning and structure. CSS controls presentation. The DOM is the browser's live object representation. Accessibility determines whether the structure communicates to people using keyboards, screen readers, zoom, or other input methods.

The best first practice is sometimes not coding. Before learning a new syntax, inspect a real page and ask what a person, browser, and assistive technology can infer from it. Later, when React produces a button or form, you will know that the element's meaning matters more than the component's name.

## Prerequisites

Day 001 setup and browser basics. No React or TypeScript knowledge is required.

## Outcomes

You should be able to describe the browser's document, separate structure from presentation, explain what the DOM represents, identify a semantic element, and name one accessibility consequence of choosing a `div` instead of a native control.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **HTML** | The markup language that describes document structure and meaning. |
| **CSS** | The language that describes presentation, layout, and visual states. |
| **DOM** | The browser's object representation of the document and its elements. |
| **Element** | A concrete item in the document tree, such as a heading, link, button, or form. |
| **Attribute** | A name-value detail attached to an element, such as `href`, `id`, or `aria-label`. |
| **Semantic HTML** | Choosing elements for their meaning and built-in browser behavior. |
| **Accessibility** | Making the interface usable and understandable across abilities and input methods. |
| **Focus** | The current keyboard or assistive-technology interaction target. |
| **CSS selector** | A pattern that chooses elements to receive style rules. |

## Topics

### What does a browser actually display?

A browser receives a response, interprets its content, builds an internal document, applies styles, and presents a result. It may also attach JavaScript behavior. The visible page is the result of several layers working together, not just the source text you first see.

### What is HTML responsible for?

HTML describes what something is and how pieces relate: a heading, paragraph, list, link, button, label, or navigation region. A semantic element carries useful default behavior and information. A heading is not merely large text; it contributes to the document outline and communicates structure.

### What is CSS responsible for?

CSS describes how the structure looks and lays out: color, spacing, size, alignment, responsive changes, and motion. CSS should not be forced to repair a missing semantic element. Making a `div` look like a button does not automatically give it button keyboard behavior.

### What is the DOM?

The DOM is a live tree of objects representing the document. Browser APIs and React can cause that tree to change. Inspecting the DOM is useful because it shows the resulting structure, not only the component source that produced it.

### What does accessibility mean here?

Accessibility means people can perceive information, operate controls, understand status, and recover from errors. A visible label, a logical heading order, keyboard focus, sufficient contrast, and a native button are practical engineering choices—not an optional decoration after the feature is finished.

## Worked example

This is a **worked observation**, not a coding exercise. Choose a page you are allowed to inspect and identify one visible card, its title, one action, and one status message. In the inspector, compare the visible appearance with the DOM element's name and role.

Write this observation table in your notes:

| Observation | Question to answer |
| --- | --- |
| A large piece of text | Is it a heading, or is it only styled to look large? |
| A clickable element | Is it a native link or button with keyboard behavior? |
| A form control | What visible or programmatic label tells a person what to enter? |
| A status message | How would a screen reader know that the status changed? |
| A repeated card | Which parent/child relationship does the DOM show? |

**Visible behavior:** when you use the browser's element inspector, the selected node is highlighted in the page and its DOM role, attributes, and computed styles can be examined separately. No React code is required to make this observation useful.

## Line-by-line explanation

There is no source-code listing to explain on purpose. Instead, trace the layers in this order:

| Step | What to inspect |
| --- | --- |
| 1 | The URL and response: what document or application did the browser request? |
| 2 | The DOM node: what element and attributes represent the visible thing? |
| 3 | The semantic role: what would a browser or assistive technology infer? |
| 4 | The CSS rules: which declarations change appearance without changing meaning? |
| 5 | The interaction: can keyboard input reach it, and does focus remain visible? |
| 6 | The React layer later: which component will own this structure when we begin coding? |

## Execution trace

1. The browser receives a document or application response.
2. It constructs a DOM tree from the document structure.
3. It applies CSS rules to determine presentation.
4. It exposes semantics, names, and relationships to accessibility APIs.
5. It accepts user input and updates the DOM or application state.
6. A future React render will describe part of this process, but it does not erase the browser's underlying responsibilities.

## Prediction experiment

Before inspecting a page, predict which element is the main heading, which control receives focus first, and whether a visual card is a link, button, or plain container. Inspect it and record one prediction that was wrong. Then turn off CSS in the inspector and describe what meaning remains visible from the HTML structure.

## Broken example and repair

**Broken design:** a clickable `div` is styled to look like a button but cannot be reached or activated with the keyboard. The repair is to start with a native `<button>` when the action performs a command, or a native `<a>` when it navigates. Add ARIA only when native semantics cannot express the real control.

## Guided practice before independent work

Choose three elements on a local or public page you are allowed to inspect. For each, record its visible appearance, DOM element, likely semantic role, accessible name, keyboard path, and one improvement. Do not write React yet. The goal is to build the observation habit.

## Project application

Create a short **accessibility observation note** for the Next.js starter: identify its main heading, navigation, button, and status area. Record what the DOM says today and one change you will verify when the component lessons begin.

## Independent exercises

This conceptual day intentionally has no coding worksheet. Complete the following observation tasks instead:
1. What is HTML, CSS, accessibility, and the DOM? Answer in one sentence.
2. Identify a heading and explain why its level matters.
3. Identify a link and a button and state the different user intents.
4. Find a form control and its label.
5. Inspect one focus state with the keyboard.
6. Turn off CSS and record what structure remains.
7. Identify one contrast or reduced-motion concern.
8. Find a repeated element and describe its DOM relationship.
9. Observe a status or error message and explain how it could be announced.
10. Replace one visual-only assumption with a semantic question.
11. Write one repair using native HTML rather than a custom ARIA imitation.
12. Apply the observation method to the local Next.js starter.
13. Write a review note with evidence, one limitation, and one question to carry into Day 003.

## Finish line

You are ready for modern JavaScript when you can explain that React eventually produces browser structure, CSS does not replace semantics, and a component's visual appearance is not the same thing as its accessible behavior.

## References

- [MDN: HTML basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [MDN: CSS first steps](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps)
- [MDN: Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WAI: Introduction to Web Accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/)
