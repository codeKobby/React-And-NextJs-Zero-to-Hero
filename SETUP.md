# Setup

This course is written for a learner who may be new to React tooling. Install Node.js 20.9 or newer, then verify it:

```bash
node --version
npm --version
```

Create a current Next.js project with the official CLI when you reach the Next.js phase:

```bash
pnpm create next-app@latest modern-case-app
cd modern-case-app
pnpm dev
```

The current recommended defaults include TypeScript, ESLint, Tailwind CSS, App Router, Turbopack, and an import alias such as `@/*`. If the CLI asks whether to use a `src/` directory, choose **Yes** for the main projects in this course. The course still teaches the root-level alternative so you can read either layout confidently.

Install VS Code if you do not already have it. Useful extensions include the official ESLint extension, the official TypeScript and JavaScript language features, a formatter such as Prettier, and a browser development tools extension. Extensions improve feedback; they do not replace running the project checks.

## Daily verification

Run the development server while editing:

```bash
pnpm dev
```

Run the explicit checks before committing:

```bash
pnpm lint
pnpm typecheck
pnpm test
pnpm build
```

In Next.js 16, linting is not automatically performed by `next build`, so the course keeps linting as a separate explicit command. Do not treat a successful build as a substitute for tests, accessibility review, or security review.

## First troubleshooting steps

When something fails, read the first error line, confirm the current directory, check the installed Node version, and rerun the smallest command that reproduces the failure. Do not delete the lockfile or install global packages as a first response. Record the command, the expected result, the observed result, and the smallest repair.

## References

- [Next.js Installation](https://nextjs.org/docs/app/getting-started/installation)
- [Next.js TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript)
- [Next.js ESLint](https://nextjs.org/docs/app/api-reference/config/eslint)
