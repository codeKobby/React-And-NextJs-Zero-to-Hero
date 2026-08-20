# Day 061: Getters, setters, and state boundaries

[← Previous lesson](../DAY_INDEX.md) · [Day index](../DAY_INDEX.md)

## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a getter?](#what-is-a-getter)
  - [What is a setter?](#what-is-a-setter)
  - [How are property accessors different from useState setters?](#how-are-property-accessors-different-from-usestate-setters)
  - [When should a UI model expose an accessor?](#when-should-a-ui-model-expose-an-accessor)
- [Worked example](#worked-example)
- [Execution trace](#execution-trace)
- [Prediction experiment](#prediction-experiment)
- [Broken example and repair](#broken-example-and-repair)
- [Guided practice before independent work](#guided-practice-before-independent-work)
- [Project application](#project-application)
- [Independent exercises](#independent-exercises)
- [Finish line](#finish-line)
- [References](#references)

## Why this lesson exists

A learner can read a framework tutorial and still feel lost because the tutorial shows a finished file without explaining the decisions that produced it. This lesson teaches **Getters, setters, and state boundaries** as a sequence of small, testable ideas. The goal is not to memorize a recipe. The goal is to predict what the runtime will do, explain why it did it, and make a safe change without breaking the mental model.

## Prerequisites

Complete the previous lesson and make sure the repository setup works. If a command fails, stop and read the error instead of copying a random fix. You may use JavaScript, TypeScript, React, or Next.js examples depending on the phase, but every new framework word is explained before the lesson depends on it.

## Outcomes

By the end, you should be able to explain the topics in your own words, run the worked example, trace it line by line, predict one normal and one boundary result, repair the broken version, and apply the idea to a small local project. You should also be able to state one limitation: what this lesson does **not** prove about production readiness, security, performance, or correctness.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| `getter` | A term you will use in this lesson; test it in the examples before memorizing it. |
| `setter` | A term you will use in this lesson; test it in the examples before memorizing it. |
| `accessor` | A term you will use in this lesson; test it in the examples before memorizing it. |
| `property` | A term you will use in this lesson; test it in the examples before memorizing it. |
| `encapsulation` | A term you will use in this lesson; test it in the examples before memorizing it. |
| `React state setter` | A term you will use in this lesson; test it in the examples before memorizing it. |

## Topics

### What is a getter?

Start with the ordinary-language question: **What is a getter?**. In **Getters, setters, and state boundaries**, this topic is not a slogan. It is a decision you can observe in a small program. Read the next example slowly, name the input, the operation, the output, and the boundary that prevents the code from doing more than intended. Then change one value and explain which line noticed the change.

A beginner mistake is to copy the spelling without understanding the runtime. Instead, say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair.

### What is a setter?

Start with the ordinary-language question: **What is a setter?**. In **Getters, setters, and state boundaries**, this topic is not a slogan. It is a decision you can observe in a small program. Read the next example slowly, name the input, the operation, the output, and the boundary that prevents the code from doing more than intended. Then change one value and explain which line noticed the change.

A beginner mistake is to copy the spelling without understanding the runtime. Instead, say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair.

### How are property accessors different from useState setters?

Start with the ordinary-language question: **How are property accessors different from useState setters?**. In **Getters, setters, and state boundaries**, this topic is not a slogan. It is a decision you can observe in a small program. Read the next example slowly, name the input, the operation, the output, and the boundary that prevents the code from doing more than intended. Then change one value and explain which line noticed the change.

A beginner mistake is to copy the spelling without understanding the runtime. Instead, say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair.

### When should a UI model expose an accessor?

Start with the ordinary-language question: **When should a UI model expose an accessor?**. In **Getters, setters, and state boundaries**, this topic is not a slogan. It is a decision you can observe in a small program. Read the next example slowly, name the input, the operation, the output, and the boundary that prevents the code from doing more than intended. Then change one value and explain which line noticed the change.

A beginner mistake is to copy the spelling without understanding the runtime. Instead, say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair.

## Worked example

Copy this complete example into the appropriate starter file. Do not modify it before the first run.

```tsx
const account = {
  _name: 'Ada',
  get name() { return this._name; },
  set name(value) { this._name = value.trim(); },
};
account.name = ' Grace ';
console.log(account.name);
```

**Expected result or visible behavior:**

```text
Grace
```

Read the code from top to bottom. Identify the input, the named values, the operation, the output, and the line that owns the decision. If the example is JSX, distinguish JavaScript expressions inside braces from markup. If it is a Server Component or Client Component example, identify which side of the boundary each line belongs to.

## Execution trace

1. The runtime reads the declarations and creates the names used by the example.
2. The component or function receives its input and evaluates its body from top to bottom.
3. React or Next.js records the result, schedules any state update or asynchronous work, and decides what can be rendered in the current environment.
4. The visible result is evidence about this fixture. It is not proof that an untested production application is secure, accessible, or correct.

Write the trace in your own notebook. After each line, record what value exists and which component or environment owns it.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input from the worked example: use an empty value, a boundary value, a delayed promise, a missing route parameter, or a rejected action appropriate to this lesson. Predict the output, fallback, compiler error, or thrown error. Run it, record what happened, and explain the difference. Then run the original case again to prove that the repair did not remove the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** Use a setter to hide invalid data instead of validating at the boundary, then repair the model and explain why React state still needs an explicit setter call.

Run the broken version in a local copy. Capture the error or incorrect UI. Name the violated assumption in one sentence. **Repair:** change the smallest possible line or boundary, rerun the normal case, rerun the boundary case, and explain what remains untested. Do not hide the failure with a broad catch, disable a type check, or claim that a passing render proves a secure application.

## Guided practice before independent work

First, reproduce the worked example with one different value. Second, change one rule while keeping the input fixed and predict the result. Third, start a blank file and recreate the smallest version from memory. Ask yourself: what is the component boundary, what data crosses it, where does state live, and what should happen when work is loading or fails? Only after these three checkpoints should you attempt the independent exercises.

## Project application

Use a local, synthetic project fixture. Name the user-visible goal, the component or route boundary, the data shape, the loading state, the failure state, the accessibility requirement, and the test evidence. If the topic is Next.js, state whether the file is a Server Component or Client Component and why. If it uses a secret, database, cookie, or authorization decision, keep that logic server-side and test an unauthorized fixture. If the topic is React-only, use invented data and do not send it to a public service.

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
