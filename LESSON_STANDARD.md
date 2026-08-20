# Modern lesson standard

Every lesson begins with a title, previous and next navigation, and a persistent table of contents. It then contains **Keywords and terms** in a compact table followed by a separate **Topics** sequence. A topic should be a real learner question or concept, such as **What is state?**, **What does a setter do?**, **Why are function components the modern default?**, or **When should a component be a Server Component?**

Every lesson must include a complete runnable example, expected output or visible behavior, line-by-line explanation, execution trace, prediction experiment, broken example and repair, guided practice before independent work, twelve numbered questions, a project application, a limitation statement, and references. Each lesson also includes three substantive support files: `practice/exercises.md` turns the lesson into twelve observable tasks, `practice/hints.md` provides targeted clues without giving away the work, and `practice/solutions.md` provides review checkpoints and self-assessment criteria. A file containing only a pointer back to the lesson is not acceptable.

## Teaching rules

Explain ordinary language before framework language. Distinguish JavaScript behavior from React behavior and React behavior from Next.js behavior. When a value changes, name its owner. When code crosses the server/client boundary, state what can cross and why. When using a Hook, explain its setter, dependency, cleanup, or call-site rule. When comparing class and function components, show the old API and the modern migration rather than calling the old approach useless.

Do not use a successful build as proof of security or accessibility. Test normal, empty, malformed, unauthorized, loading, rejected, and boundary cases. Keep data local and synthetic in exercises. Never put secrets in client code, never treat a hidden button as authorization, and never trust form data without validation and authorization. Start every learner from the README, setup guide, examples guide, and day index; every lesson must link back to those four entry points and provide previous/next navigation.
