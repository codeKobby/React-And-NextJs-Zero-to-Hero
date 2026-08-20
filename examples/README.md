# Runnable examples

The course uses two kinds of projects. The React-only playground isolates component and Hook behavior from framework routing. The Next.js starter is the main application-building project: it adds App Router, server/client boundaries, Tailwind CSS v4, shadcn/ui-style owned components, data access, validation, caching, streaming, authentication, Proxy, authorization, testing, and deployment concerns.

The manifests below record the modern baseline without committing a generated `node_modules` directory. The complete starter projects are already in this directory; use the [setup guide](../SETUP.md) for installation and the official CLI when creating a fresh project.

| Starter | Use it for | Location |
| --- | --- | --- |
| React playground | Days 001–038: JSX, components, props, state, Hooks, React 19 APIs, testing, accessibility, performance, and security concepts | [react-playground/](react-playground/) · [package.json](react-playground/package.json) |
| Next.js App Router starter | Days 039–061: `src/app/`, routes, layouts, Server and Client Components, data boundaries, forms, APIs, auth concepts, deployment, and project structure | [next-app/](next-app/) · [package.json](next-app/package.json) |
| Next.js full-stack pathway | Days 062–083: Tailwind CSS v4, responsive tokens, shadcn/ui, dashboard shell, schema validation, SQL/Drizzle concepts, Server Actions, sessions, `proxy.ts`, authorization, uploads, observability, Playwright, CI, deployment, and capstone delivery | [next-app/](next-app/) · [components.json](next-app/components.json) |

## Running a starter

From the repository root, change into the starter directory before running commands. Install dependencies, start the development server, and use the scripts recorded in that starter's `package.json`.

```bash
cd examples/react-playground
pnpm install
pnpm dev
```

For a Next.js lesson, use:

```bash
cd examples/next-app
pnpm install
pnpm dev
```

The Next.js starter already includes a verified Tailwind CSS v4 PostCSS setup, `components.json`, a `cn()` class-merging utility, and an owned Button primitive at `src/components/ui/button.tsx`. Study these files as source code: shadcn/ui components are copied into the project so the learner can read, test, and customize them. Days 067–083 use local or synthetic fixtures unless a lesson explicitly asks you to design a replaceable provider boundary. Do not add credentials, private logs, production tokens, or personal information to either starter.
