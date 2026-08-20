# Runnable examples

The course uses two kinds of projects. The React-only playground isolates component and Hook behavior from framework routing. The Next.js starter adds App Router, server/client boundaries, data access, caching, streaming, and deployment concerns.

The manifests below record the modern baseline without committing a generated `node_modules` directory. The complete starter projects are already in this directory; use the [setup guide](../SETUP.md) for installation and the official CLI when creating a fresh project.

| Starter | Use it for | Location |
| --- | --- | --- |
| React playground | Days 001–038: JSX, components, props, state, Hooks, React 19 APIs, testing, accessibility, performance, and security concepts | [react-playground/](react-playground/) · [package.json](react-playground/package.json) |
| Next.js App Router starter | Days 039–061: `src/app/`, routes, layouts, Server and Client Components, data boundaries, forms, APIs, auth, deployment, and capstone work | [next-app/](next-app/) · [package.json](next-app/package.json) |

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

Keep practice data synthetic and local. Do not add credentials, private logs, production tokens, or personal information to either starter.
