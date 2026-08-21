# Day 062 solution guide: Tailwind CSS v4 setup in Next.js

Use this guide only after attempting the numbered exercises in [the lesson](../day_062_tailwind_css_v4_setup_in_next_js.md). It reviews the decisions for **Tailwind CSS v4 setup in Next.js**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to tailwind css v4 setup in next.js rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a local dashboard shell with a readable, keyboard-usable Button and empty state.
3. The trace identifies the owner and boundary: design-system primitives versus feature-specific data, authorization, and application behavior.
4. The normal change isolates one input and preserves the rule for What problem does Tailwind CSS solve?.
5. The boundary case for How does Tailwind CSS v4 enter a Next.js project? has deliberate behavior and an explanation.
6. The failure `Install a v3-style configuration in a v4 project, then repair the PostCSS plugin and global CSS import.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package.
8. The quality requirement for What is a utility class? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a local dashboard shell with a readable, keyboard-usable Button and empty state with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary design-system primitives versus feature-specific data, authorization, and application behavior.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
