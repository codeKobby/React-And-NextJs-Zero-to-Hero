# Modern toolchain

The course was checked against the following package versions on 20 August 2026:

| Tool | Version target | Role |
| --- | --- | --- |
| Node.js | 20.9+; use the current supported LTS | JavaScript runtime |
| React | 19.2.8 | UI library |
| React DOM | 19.2.8 | Browser and server DOM APIs |
| Next.js | 16.3.1 | Full-stack React framework |
| TypeScript | 7.0.2 | Static checking and editor tooling |
| Vite | 8.2.2 | Lightweight React-only playground tooling |
| ESLint | 10.8.1 | Explicit linting command |
| Tailwind CSS | 4.3.3 | Utility-first styling and design tokens |
| `@tailwindcss/postcss` | 4.3.3 | Tailwind CSS v4 PostCSS integration |
| PostCSS | 8.5.26 | CSS build pipeline |
| class-variance-authority | 0.7.1 | Variant definitions for owned UI primitives |
| clsx | 2.1.1 | Conditional class composition |
| tailwind-merge | 3.6.0 | Conflict-aware Tailwind class merging |

These versions are a recorded baseline, not a promise that future releases will keep the same numbers. Read the React and Next.js upgrade guides when starting a new project. Use the package manager lockfile for reproducibility and make upgrades in small, reviewable commits.

## React-only playgrounds

Use Vite when you want to study React without Next.js routing or server boundaries. A React-only playground is ideal for JSX, props, state, Hooks, controlled forms, reducers, Context, testing, and accessibility.

## Next.js applications

Use Next.js when the lesson needs file-system routing, server rendering, server-side data access, streaming, route handlers, metadata, styling, authentication, or deployment behavior. The App Router is the main modern path. The Pages Router is taught for reading and migration, not as the default for new projects. The full-stack starter includes Tailwind CSS v4 and a small shadcn/ui-style owned component so the learner can study the source rather than treating UI as a black box.

## Explicit checks

Use separate commands for formatting, linting, type checking, tests, and production builds. A build does not automatically prove that linting, accessibility, authorization, or edge-case behavior is correct.

## References

- [Next.js Installation](https://nextjs.org/docs/app/getting-started/installation)
- [React 19](https://react.dev/blog/2024/12/05/react-19)
- [TypeScript Releases](https://www.typescriptlang.org/docs/handbook/release-notes/overview.html)
- [Tailwind CSS Next.js guide](https://tailwindcss.com/docs/installation/framework-guides/nextjs)
- [shadcn/ui Next.js installation](https://ui.shadcn.com/docs/installation/next)
- [Next.js Authentication](https://nextjs.org/docs/app/guides/authentication)
- [Next.js Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
