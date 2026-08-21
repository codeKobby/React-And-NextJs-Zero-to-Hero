# Code Buddy Learning Workflow

This repository is designed around a deliberate loop: read, run, predict, experiment, repair, practise, test, explain, and reflect. For the best interactive experience, install the public [code-buddy](https://github.com/codeKobby/code-buddy) Agent Skills suite in the coding agent you use.

## Install

Install all code-buddy commands:

```bash
npx skills add codeKobby/code-buddy --all
```

Install only the core learning commands:

```bash
npx skills add codeKobby/code-buddy --skill setup-learning --skill teach --skill quiz --skill exercise --skill assess --skill progress --skill next
```

Target selected coding agents when needed:

```bash
npx skills add codeKobby/code-buddy --all -a claude-code -a codex -a cline -a opencode
```

## Start in this repository

From the repository root, run `/setup-learning` once. It will inspect the 83-day course, initialize `.learning/`, and ask for your learning mission and preferences. Then use:

```text
/quiz day 1
/quiz day one
/teach day 1
/exercise day 1
/assess day-001/practice/your-answer.tsx
/progress
/next
```

`/quiz` is continuous: answer each A–D question and code-buddy will explain the result and show the next question automatically. It accepts `1`, `01`, `001`, `day one`, a lesson title, a topic, or a file path. Use `/quiz resume` to continue an unfinished session.

For this course, ask code-buddy to distinguish JavaScript, TypeScript, React, and Next.js behavior; trace state ownership and server/client boundaries; and assess loading, empty, rejected, malformed, unauthorized, and error-boundary states. A multiple-choice score is retrieval evidence; use `/exercise` and `/assess` for implementation and transfer evidence.

Code-buddy also works in unrelated repositories. When no day index exists, target a file, component, hook, route, test, bug, feature, pull request, or project milestone directly.
