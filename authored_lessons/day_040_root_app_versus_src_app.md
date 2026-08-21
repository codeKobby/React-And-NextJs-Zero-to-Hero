# Day 040: Root-level `app/` versus `src/app/`

[← Previous lesson](../day_039_next_js_installation_and_project_structure/day_039_next_js_installation_and_project_structure.md) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_041_layouts_pages_and_route_segments/day_041_layouts_pages_and_route_segments.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is the App Router directory?](#what-is-the-app-router-directory)
  - [What is `src/` for?](#what-is-src-for)
  - [Which files stay at the repository root?](#which-files-stay-at-the-repository-root)
  - [What happens when both routers exist?](#what-happens-when-both-routers-exist)
  - [How do aliases relate to source structure?](#how-do-aliases-relate-to-source-structure)
- [Worked example](#worked-example)
  - [Experiment 1: root-level `app/`](#experiment-1-root-level-app)
  - [Experiment 2: move to `src/app/`](#experiment-2-move-to-src-app)
  - [Experiment 3: add a source alias](#experiment-3-add-a-source-alias)
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

Read the [README](../README.md), confirm the [setup guide](../SETUP.md), and open the [examples guide](../examples/README.md). Use the local Next.js starter and make a copy before each experiment:

```bash
cd examples/next-app
pnpm install
pnpm dev
```

Open `http://localhost:3000`. Do not mix the experiments in one working tree. The point is to observe which directory Next.js recognises, not to memorise a preferred folder name.

## Why this lesson exists

A new Next.js project has application files, configuration files, public assets, dependencies, and generated build output. Beginners often move files based on visual preference and then cannot explain why a route disappeared. The framework does support two common source layouts, but the project must choose one unambiguous App Router location.

This lesson separates three questions that are easy to confuse:

1. **Which folder is the App Router?** The folder contains route segments and special files such as `page.tsx` and `layout.tsx`.
2. **Which folder contains application source?** `src/` is a conventional boundary for source code; it is not a second router.
3. **Which files stay at the root?** `package.json`, `next.config.ts`, `tsconfig.json`, `public/`, environment files, and tooling configuration remain close to the project root.

## Prerequisites

Complete Day 039, know how a Next.js project starts, and be comfortable reading a directory tree and a TypeScript function. No database, authentication, or deployment provider is needed for this lesson.

## Outcomes

By the end you will be able to create a working route in a root-level `app/`, move the same route to `src/app/`, explain why the visible URL stays the same, list the files that remain at the root, predict what happens when both router locations exist, and configure an alias that points into `src` without confusing aliases with routing.

## Keywords and terms

| Keyword or term | Plain-English meaning |
| --- | --- |
| **App Router** | Next.js routing convention where folders and special files define route segments and rendering boundaries. |
| **`app/`** | The special directory containing App Router segments when it is placed at the repository root. |
| **`src/app/`** | The same App Router convention nested inside a source directory. |
| **route segment** | A folder-level part of a URL path. |
| **`page.tsx`** | The special file that supplies the UI for one route segment. |
| **`layout.tsx`** | The special file that wraps a segment and its child segments. |
| **repository root** | The top-level project directory containing package and tool configuration. |
| **alias** | A short import path mapped to a longer filesystem path by TypeScript or the bundler. |
| **precedence** | The rule that determines which location wins when two choices overlap. |

## Topics

### What is the App Router directory?

Next.js does not treat every folder as a route. In the App Router, a folder becomes a route segment when it contains the appropriate special file. `app/page.tsx` and `src/app/page.tsx` can both represent `/`, but a project should not keep both as competing sources of truth.

### What is `src/` for?

`src/` groups application source separately from root-level project configuration. It can contain `app/`, `components/`, and `lib/`. Moving `app/` under `src/` changes the filesystem location, not the public URL: `src/app/about/page.tsx` still represents `/about`.

### Which files stay at the repository root?

The root remains the project’s control panel. Keep `package.json`, the lockfile, `next.config.ts`, `tsconfig.json`, lint and test configuration, `.env.local`, and `public/` at the root unless a tool’s documentation explicitly says otherwise. `public/` is not inside `src/` because its files are served as public assets.

### What happens when both routers exist?

Keeping both `app/` and `src/app/` creates ambiguity. The framework’s file-convention rules determine what is recognised, but a learner should not rely on an accidental precedence rule. Delete or rename the unused router, restart the dev server, and prove which folder owns the route.

### How do aliases relate to source structure?

An alias is an import convenience, not a route. This configuration makes `@/components/Notice` resolve to `src/components/Notice`:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

The alias changes how a module is imported; it does not create a URL and does not move a page into the App Router.

## Worked example

### Experiment 1: root-level `app/`

In a throwaway copy of the starter, create this tree:

```text
next-app/
├── app/
│   ├── layout.tsx
│   └── page.tsx
├── public/
├── next.config.ts
├── package.json
└── tsconfig.json
```

`app/layout.tsx`:

```tsx
import type { ReactNode } from 'react';

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

`app/page.tsx`:

```tsx
export default function HomePage() {
  return (
    <main>
      <h1>Root app route</h1>
      <p>This page is owned by app/page.tsx.</p>
    </main>
  );
}
```

Run `pnpm dev` and visit `/`. **Visible behavior:** the browser shows “Root app route.” The filename `page.tsx` is what makes this folder-backed route render.

### Experiment 2: move to `src/app/`

Stop the dev server, move the router as one unit, and leave root configuration in place:

```text
next-app/
├── src/
│   └── app/
│       ├── layout.tsx
│       └── page.tsx
├── public/
├── next.config.ts
├── package.json
└── tsconfig.json
```

Start the server again and visit `/`. Change the heading to “src app route.” **Visible behavior:** the URL is unchanged, but the page proves that `src/app/page.tsx` now owns the route.

### Experiment 3: add a source alias

Create `src/components/Notice.tsx`:

```tsx
export function Notice({ children }: { children: React.ReactNode }) {
  return <p role="status">{children}</p>;
}
```

Add the alias to `tsconfig.json`, then import it from `src/app/page.tsx`:

```tsx
import { Notice } from '@/components/Notice';

export default function HomePage() {
  return (
    <main>
      <h1>src app route</h1>
      <Notice>Training fixture only.</Notice>
    </main>
  );
}
```

**Visible behavior:** the status appears on `/`. The alias changed the import spelling, while `src/app/page.tsx` continued to own the route.

## Line-by-line explanation

| Line or file | What it does |
| --- | --- |
| `src/app/page.tsx` | The location and special filename together define the `/` route. |
| `src/app/layout.tsx` | The layout wraps the page and supplies the document shell. |
| `src/components/Notice.tsx` | This is ordinary application source; it is not itself a route because it has no App Router special filename. |
| `public/` | Holds assets that can be requested by their public URL; it is intentionally outside `src/`. |
| `package.json` | Defines scripts and dependencies and remains project configuration at the root. |
| `tsconfig.json` | Configures TypeScript and the `@/*` import mapping; it does not define a URL. |
| `paths: { "@/*": ["./src/*"] }` | Maps an import prefix to a source path. It affects module resolution, not route resolution. |
| `import { Notice } from '@/components/Notice'` | Uses the alias to import a component owned by `src/components`. |
| `export default function HomePage()` | Exports the route’s UI function from the special `page.tsx` file. |
| `<Notice>...</Notice>` | Composes the ordinary component inside the route’s returned UI tree. |

## Execution trace

1. The dev server reads the project root and its Next.js configuration.
2. Next.js scans the selected App Router location for special files.
3. `src/app/page.tsx` is associated with `/`; the folder name `src` is not added to the URL.
4. `src/app/layout.tsx` wraps the page and supplies the required document structure.
5. The TypeScript resolver reads the `@/*` mapping when the page imports `Notice`.
6. The route renders the heading and status, proving both route ownership and module ownership.
7. If the old root-level `app/` remains, remove it, restart the server, and rerun the URL check rather than guessing which file won.

## Prediction experiment

Before each change, predict the result:

1. Rename `src/app/page.tsx` to `src/app/home.tsx`. Does `/` still render?
2. Add `src/app/about/page.tsx`. Which URL should render it?
3. Move `Notice.tsx` to `src/lib/Notice.tsx` without changing the import. What error should appear?
4. Keep both `app/page.tsx` and `src/app/page.tsx` with different headings. What does the framework show, and why is that an unacceptable project design even if one heading appears?
5. Change the alias target to `./src/components/*`. Which imports should still work, and which should fail?

Run one experiment at a time and record the command, URL, visible result, and explanation.

## Broken example and repair

The broken project keeps two competing router roots:

```text
next-app/
├── app/page.tsx
└── src/app/page.tsx
```

The root page says “old route” and the source page says “new route.” Repair it by choosing one layout, deleting the unused router, restarting the dev server, and verifying `/` and one nested route. Do not hide the ambiguity with an alias or by changing the page text.

## Guided practice before independent work

Copy Experiment 1 and run it unchanged. Move it to `src/app/` and prove the URL remains `/`. Add the `Notice` component and alias. Then deliberately create both router locations, record what the dev server renders, remove the duplicate, and rerun the route checks.

## Project application

Write a short **project structure decision record** for the course’s Next.js starter. Include a file tree, the chosen App Router location, root configuration files, one alias mapping, one route URL, and one reason the unused router location must not exist. Keep the project local and do not add a database or authentication provider for this lesson.

## Independent exercises

1. Run the root-level `app/` experiment and record the URL and visible heading.
2. Draw the equivalent `src/app/` file tree and identify which files stay at the root.
3. Move the route to `src/app/` and prove the URL does not gain a `/src` segment.
4. Add `src/app/about/page.tsx` and predict its URL before running it.
5. Add `src/components/Notice.tsx` and import it through `@/components/Notice`.
6. Explain why `public/` remains outside `src/` in this project layout.
7. Rename `page.tsx` and record the resulting route failure.
8. Create both `app/` and `src/app/` with different headings, then remove the ambiguity safely.
9. Change the alias target and record which import error appears.
10. Compare a route file, a component file, and `tsconfig.json` in a three-row ownership table.
11. Add a nested route and one semantic status message without introducing client state.
12. Write a project structure decision record with the file tree, commands, URLs, evidence, and one limitation.

## Finish line

You are ready for layouts and route segments when you can explain that `app/` is a routing convention, `src/` is a source-organization choice, `public/` is a public-asset boundary, and an alias affects imports rather than URLs. You must be able to prove route ownership with a file tree and a browser result instead of relying on a memorized slogan.

## References

- [Next.js Project Organization](https://nextjs.org/docs/app/getting-started/project-structure)
- [Next.js `src` folder](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)
- [Next.js Routing Fundamentals](https://nextjs.org/docs/app/building-your-application/routing)
- [TypeScript `paths` reference](https://www.typescriptlang.org/tsconfig/#paths)
