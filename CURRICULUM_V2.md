# React and Next.js Zero to Hero — Modern Curriculum Blueprint

This repository is being rebuilt as an **83-day beginner-first React and Next.js course**. It assumes no prior React, TypeScript, framework, or full-stack experience and ends with a complete application pathway. The course uses React 19.2.8 and Next.js 16.3.1 as the validation target recorded on 20 August 2026; learners should verify the latest compatible versions before starting a new project.

## Teaching contract

Every lesson contains a persistent table of contents, a **Keywords and terms** table, a separate **Topics** section, a problem-first explanation, a smallest runnable example, expected output or visible behavior, a line-by-line walkthrough, a prediction experiment, a broken example and repair, guided practice before independent work, numbered exercises, a security or reliability boundary, and a references section. The lesson must explain why code works rather than merely showing syntax.

## Course progression

| Days | Phase | Main outcomes |
| --- | --- | --- |
| 001–005 | JavaScript and web foundations | Modules, browser/runtime model, JSX prerequisites, DOM, accessibility, and tooling basics |
| 006–012 | React mental model | Components, JSX, props, composition, lists, keys, events, forms |
| 013–020 | State and interaction | `useState`, React setters, JavaScript getters and setters, derived state, controlled inputs, lifting state, reducers, context |
| 021–028 | Hooks and reusable logic | `useEffect`, dependencies, cleanup, refs, `use`, custom Hooks, memoization, transitions |
| 029–034 | Class and function components | Class lifecycle mapping, migration strategy, error boundaries, legacy API reading, testing |
| 035–040 | React 19 and production client patterns | Actions, `useActionState`, `useFormStatus`, `useOptimistic`, metadata, Suspense, React Compiler |
| 041–047 | Next.js foundations | `create-next-app`, App Router, root-level versus `src/`, aliases, layouts, pages, links, assets |
| 048–053 | Next.js routing and rendering | Dynamic routes, route groups, private folders, loading, error, not-found, metadata, images |
| 054–057 | Full-stack Next.js | Server and Client Components, data fetching, cache policy, streaming, Route Handlers, Server Actions |
| 058–061 | Professional delivery and JavaScript boundaries | Auth boundaries, security, testing, accessibility, performance, deployment, capstone architecture, getters, and setters |
| 062–066 | Styling and application shell | Tailwind CSS v4, responsive design tokens, dark mode, shadcn/ui, accessible primitives, dashboard layout, and feature boundaries |
| 067–070 | Data and mutations | Schema validation, SQL modeling, Drizzle ORM, SQLite, migrations, seed data, repositories, Server Actions, and revalidation |
| 071–074 | HTTP, identity, and authorization | Route Handler contracts, authentication providers, secure sessions, Next.js 16 `proxy.ts`, roles, permissions, ownership, and multi-tenant data |
| 075–078 | Operations and delivery | Uploads, storage boundaries, structured errors, logging, instrumentation, Playwright, CI, environment configuration, deployment, and rollback evidence |
| 079–083 | Full-stack capstone | Threat model, architecture, design system, database-backed reads, authentication, authorization, mutations, hardening, tests, deployment proof, and residual risk |

## Project sequence

The learner builds small projects before the capstone and finishes with a dedicated getter/setter and state-boundary lesson followed by a full-stack application track: an accessible React task board, a controlled form, a reducer-driven dashboard, a custom Hook data viewer, a class-to-function migration, a React 19 mutation form, a Next.js content site, a dynamic product route, a streaming dashboard, a Tailwind and shadcn dashboard shell, a validated database-backed case repository, secure sessions, a Proxy redirect, an authorization policy, a tested upload boundary, and a final full-stack case-management application.

## Project-structure decision

The course demonstrates both supported Next.js arrangements before choosing one for projects:

```text
# Root-level application code
app/
components/
lib/
public/
package.json
next.config.ts
```

and:

```text
# Application code separated under src/
src/app/
src/components/
src/lib/
public/
package.json
next.config.ts
```

Next.js supports both. The course uses `src/` in the main projects because it separates application code from root configuration, while explaining that `public/`, `package.json`, `next.config.ts`, `tsconfig.json`, and `.env.*` remain at the repository root. The course also explains that a root-level `app/` or `pages/` takes precedence over `src/app` or `src/pages`, so learners must not keep both for the same router.

## React and Next.js distinctions

React is the UI library and component model. Next.js is the full-stack framework that adds file-system routing, server rendering, data access patterns, caching, streaming, route handlers, metadata conventions, and deployment integration. A learner must understand React in isolation before the course introduces the App Router boundary.

## References

1. [React Learn](https://react.dev/learn)
2. [React Reference](https://react.dev/reference/react)
3. [React 19](https://react.dev/blog/2024/12/05/react-19)
4. [React Server Components](https://react.dev/reference/rsc/server-components)
5. [Next.js Documentation](https://nextjs.org/docs)
6. [Next.js Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
7. [Next.js `src` Folder](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)
8. [Next.js Installation](https://nextjs.org/docs/app/getting-started/installation)
9. [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
10. [Next.js Fetching Data](https://nextjs.org/docs/app/building-your-application/data-fetching)
11. [Next.js Caching](https://nextjs.org/docs/app/building-your-application/caching)
12. [Next.js Authentication](https://nextjs.org/docs/app/guides/authentication)
13. [Next.js Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
14. [Tailwind CSS Next.js guide](https://tailwindcss.com/docs/installation/framework-guides/nextjs)
15. [shadcn/ui Next.js installation](https://ui.shadcn.com/docs/installation/next)
