# Course quality standard

A lesson is accepted only when the learner can follow it from a clean setup, run the normal example, explain the output, predict a boundary result, repair the deliberate failure, and complete the numbered exercises without relying on unexplained magic.

The repository must contain exactly 61 zero-padded lesson directories from `day_001` through `day_061`. Each lesson must contain one Markdown lesson file with the same prefix, a persistent table of contents with working anchors, separate Keywords and Topics sections, a runnable example, an execution trace, a prediction experiment, a broken-and-repaired example, guided practice, twelve numbered exercises, a project application, and references.

React lessons must distinguish JavaScript, React, and browser behavior. Next.js lessons must distinguish Server Components, Client Components, route files, data access, caching, and deployment behavior. Full-stack examples must name authentication, authorization, validation, secrets, and failure boundaries. Exercises must use local or synthetic fixtures only.

The automated checker verifies names, counts, required sections, internal TOC anchors, practice files, and day-index completeness. Human review remains required for conceptual accuracy, accessibility, maintainability, security, and whether the explanation is genuinely understandable to a beginner.
