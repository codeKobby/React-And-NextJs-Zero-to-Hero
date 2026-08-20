# Course quality standard

A lesson is accepted only when a beginner can follow the lesson's reasoning, not merely its headings. The learner should understand the problem, run a meaningful example, explain the visible result, predict a change, repair a likely mistake, and produce evidence of understanding.

## Structural requirements

The repository contains 83 sortable lessons from `day_001` through `day_083`. Each lesson has a persistent table of contents, previous and next navigation, a direct start path to the README, setup, examples, and day index, separate **Keywords and terms** and **Topics** sections, references, and a learner-facing finish line.

Each substantive lesson contains prerequisites, observable outcomes, a problem-first opening, at least one meaningful worked example or a truthful explanation of why the day is conceptual, expected output or visible behavior, a concrete line-by-line explanation for code that is present, an execution trace tied to that code, a prediction experiment, a likely beginner failure and repair, guided practice, and appropriate independent work.

## Teaching requirements

The lesson must introduce ordinary language before framework vocabulary, answer real beginner questions, and explain why the concept exists. Its examples must progress through purposeful changes rather than appearing as unrelated code blocks. Its trace must refer to actual values, events, renders, requests, outputs, or boundaries in the example. Its line-by-line explanation must not reuse generic sentences that could describe another lesson.

A lesson must distinguish JavaScript runtime behavior, React rendering behavior, and Next.js framework behavior. It must explain the ownership of values and state, the reason for a Server or Client Component boundary, and the limits of any framework shortcut. Full-stack lessons must name validation, authentication, authorization, secrets, failure behavior, and local or synthetic fixture boundaries when those concerns apply.

## Practice requirements

Practice is deliberately lesson-specific. The course must not generate twelve mechanically identical questions merely to satisfy a count. A setup or orientation lesson may have no coding exercise if it gives a better verification or installation task. A state lesson should normally progress from a small run to an interaction, boundary case, repair, and a small application. A project or capstone lesson should include milestones, acceptance criteria, tests, review evidence, and limitations.

Each lesson’s **Independent exercises** section is the canonical source for the starting point, expected behavior, acceptance criteria, and permitted concepts. `practice/hints.md` provides progressive clues without replacing the learner's attempt. `practice/solutions.md` explains decisions and review evidence rather than serving as a generic answer key. These support files must be substantive and specific to the lesson, and no redundant the lesson’s numbered exercises file is permitted.

## Human review questions

Before publication, a reviewer must be able to answer “yes” to the following questions:

| Review question | Evidence to inspect |
| --- | --- |
| Does the opening make the learner care about the concept? | Problem, analogy, broken page, or concrete motivation |
| Does the lesson build understanding through small changes? | Connected examples with visible before/after behavior |
| Does the code explanation describe real behavior? | Accurate line-specific explanation and trace |
| Does the broken example teach a likely mistake? | Reproduction, cause, minimal repair, rerun |
| Is the practice proportionate and specific? | Tasks that fit the concept, starter, and learner stage |
| Can the learner work without unexplained magic? | Boilerplate explanation, commands, outputs, and ownership |
| Does the lesson say what it does not prove? | Limitations involving security, accessibility, performance, or production readiness |

## Technical verification

Automated checks verify lesson names, required structural sections, internal anchors, navigation, substantive practice files, and Markdown links. Starter projects must also pass their documented type checks and production builds where applicable. Human review remains mandatory because a validator can count headings and words but cannot determine whether an explanation teaches state, props, composition, hooks, routing, data access, or authorization accurately.

A passing build is not proof of accessibility, security, authorization, or production readiness. Exercises use local, synthetic, bounded fixtures. Credentials, personal data, destructive payloads, and unauthorized targets do not belong in the repository.

## Completion definition

The course is complete only when its lessons, examples, practice routes, project milestones, full-stack architecture, and quality evidence form a coherent path from beginner questions to a working and explainable React/Next.js application. Coverage is valuable, but learner understanding is the acceptance criterion.
