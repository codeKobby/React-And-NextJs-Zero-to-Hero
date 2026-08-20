# Day 005: Tooling and the first component

[← Previous lesson](../day_004_typescript_foundations_for_ui_code/day_004_typescript_foundations_for_ui_code.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_006_what_is_a_component/day_006_what_is_a_component.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does a toolchain do?](#what-does-a-toolchain-do)
  - [What is a React component?](#what-is-a-react-component)
  - [How does JSX become browser output?](#how-does-jsx-become-browser-output)
  - [How do we verify a first component?](#how-do-we-verify-a-first-component)
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

This lesson belongs to the complete course, not to a disconnected collection of notes. Before coding, open the [course README](../README.md) for the learning contract, read the [setup guide](../SETUP.md) if your tools are not ready, and use the [day index](../DAY_INDEX.md) to see where this lesson fits. If you need a runnable project, open the [examples guide](../examples/README.md), choose the React playground or Next.js starter that matches this day, and work locally with synthetic data only.

The intended loop is simple: read the lesson, run the worked example unchanged, make a prediction, repair the broken version, complete the guided practice, then use the linked [practice worksheet](practice/exercises.md), [hints](practice/hints.md), and [solution guide](practice/solutions.md) only after attempting the work.

## Why this lesson exists

A learner can read a framework tutorial and still feel lost because the tutorial shows a finished file without explaining the decisions that produced it. This lesson teaches **Tooling and the first component** as a sequence of small, testable ideas. The goal is not to memorize a recipe. The goal is to predict what the runtime will do, explain why it did it, and make a safe change without breaking the mental model.

## Prerequisites

Complete the previous lesson, confirm the [setup guide](../SETUP.md), and make sure the repository setup works. If a command fails, stop and read the first error instead of copying a random fix. Use the [course README](../README.md) to understand the learning loop and the [examples guide](../examples/README.md) to choose the correct local starter. You may use JavaScript, TypeScript, React, or Next.js examples depending on the phase, but every new framework word is explained before the lesson depends on it.

## Outcomes

By the end, you should be able to explain the topics in your own words, run the worked example, trace it line by line, predict one normal and one boundary result, repair the broken version, and apply the idea to a small local project. You should also be able to state one limitation: what this lesson does **not** prove about production readiness, security, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `package.json` | A named idea in this lesson. Use the worked example to observe its input, behavior, output, and boundary before trying to define it in your own words. |
| `bundler` | A named idea in this lesson. Use the worked example to observe its input, behavior, output, and boundary before trying to define it in your own words. |
| `component` | A reusable unit of UI that receives inputs and returns a description of what should appear. |
| `JSX` | JavaScript syntax that describes UI elements using markup-like notation. |
| `render` | A named idea in this lesson. Use the worked example to observe its input, behavior, output, and boundary before trying to define it in your own words. |
| `dev server` | A named idea in this lesson. Use the worked example to observe its input, behavior, output, and boundary before trying to define it in your own words. |

## Topics

### What does a toolchain do?

Study **What does a toolchain do** by naming its input, operation, output, and owner. Change one thing at a time and keep both your prediction and the observed result so that a mismatch becomes a repairable learning signal.

A beginner mistake is to copy the spelling without understanding the runtime. Say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair.

### What is a React component?

**a React component** is the idea you must be able to point to in code. Begin with the smallest example: identify the value or boundary involved, observe what changes, and name the rule that connects the input to the result. In this lesson, the worked example gives you a controlled fixture; do not add framework complexity until you can explain the plain JavaScript or browser behavior first.

A beginner mistake is to copy the spelling without understanding the runtime. Say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair.

### How does JSX become browser output?

To answer **How does JSX become browser output**, follow a repeatable procedure. First identify the input and the owner; next make the smallest change; then predict the output, run it, and inspect the boundary behavior. If the code crosses from JavaScript into React or from a Server Component into the browser, write that boundary down explicitly.

A beginner mistake is to copy the spelling without understanding the runtime. Say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair.

### How do we verify a first component?

To answer **How do we verify a first component**, follow a repeatable procedure. First identify the input and the owner; next make the smallest change; then predict the output, run it, and inspect the boundary behavior. If the code crosses from JavaScript into React or from a Server Component into the browser, write that boundary down explicitly.

A beginner mistake is to copy the spelling without understanding the runtime. Say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair.

## Worked example

Copy this complete example into the appropriate starter file. Do not modify it before the first run.

```tsx
function Greeting() {
  return <h1>Hello, learner</h1>;
}
console.log(Greeting().type);
```

**Expected result or visible behavior:**

```text
h1
```

Read the code from top to bottom. Identify the input, the named values, the operation, the output, and the line that owns the decision. If the example is JSX, distinguish JavaScript expressions inside braces from markup. If it is a Server Component or Client Component example, identify which side of the boundary each line belongs to.

## Line-by-line explanation

| Line | What this line does |
| ---: | --- |
| 1 | `function Greeting() {` — Declares behavior; the body runs when this function or component is called or rendered. |
| 2 | `return <h1>Hello, learner</h1>;` — Returns the value or UI description that the surrounding function owns. |
| 3 | `}` — Runs as part of the surrounding expression or block; identify its input and observed effect. |
| 4 | `console.log(Greeting().type);` — Writes an observation to the console so the learner can compare it with the prediction. |

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

## Execution trace

1. The runtime reads the declarations and creates the names used by the example.
2. The component or function receives its input and evaluates its body from top to bottom.
3. React or Next.js records the result, schedules any state update or asynchronous work, and decides what can be rendered in the current environment.
4. The visible result is evidence about this fixture. It is not proof that an untested production application is secure, accessible, or correct.

Write the trace in your own notebook. After each line, record what value exists and which component or environment owns it.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input from the worked example: use an empty value, a boundary value, a delayed promise, a missing route parameter, or a rejected action appropriate to this lesson. Predict the output, fallback, compiler error, or thrown error. Run it, record what happened, and explain the difference. Then run the original case again to prove that the repair did not remove the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Return a lowercase component name and explain why React treats it differently from a capitalized component.

Run the broken version in a local copy. Capture the error or incorrect UI. Name the violated assumption in one sentence. **Repair:** change the smallest possible line or boundary, rerun the normal case, rerun the boundary case, and explain what remains untested. Do not hide the failure with a broad catch, disable a type check, or claim that a passing render proves a secure application.

## Guided practice before independent work

First, reproduce the worked example with one different value. Second, change one rule while keeping the input fixed and predict the result. Third, start a blank file and recreate the smallest version from memory. Ask yourself: what is the component boundary, what data crosses it, where does state live, and what should happen when work is loading or fails? Only after these three checkpoints should you attempt the independent exercises.

## Project application

Use a local, synthetic project fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the component or route boundary, the data shape, the loading state, the failure state, the accessibility requirement, and the test evidence. If the topic is Next.js, state whether the file is a Server Component or Client Component and why. If it uses a secret, database, cookie, or authorization decision, keep that logic server-side and test an unauthorized fixture. If the topic is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Recreate the worked example using different data.
2. Explain each keyword in the Keywords and terms table without reading the lesson.
3. Change one line and predict the new output before running it.
4. Add a normal case and a boundary case.
5. Break the example in the way described above and record the error.
6. Repair it with the smallest change.
7. Add one accessible label, keyboard behavior, or meaningful loading message.
8. Add a test or assertion for the most important behavior.
9. Explain which value is owned by which component, function, or server boundary.
10. Write one limitation that the example does not prove.
11. Apply the lesson to the current project fixture using only local or synthetic data.
12. Write a short review explaining what a teammate should inspect before merging your change.

## Finish line

You are finished when you can teach the main idea to another beginner, show the normal and broken runs, explain the repair, and point to the exact boundary where data, state, effects, or server authority changes. Do not move on because the code merely compiles.

## References

- [React Learn](https://react.dev/learn)
- [React Reference](https://react.dev/reference/react)
- [Next.js Documentation](https://nextjs.org/docs)
- [Next.js Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
- [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
