# Official research used by this course

The course follows the current official React and Next.js documentation rather than the six-year-old repository defaults.

React's learning sequence introduces components, JSX, styles, displaying data, conditions, lists and keys, events, state, Hooks, and sharing data. React's reference also documents Hooks, APIs, directives, React DOM APIs, the React Compiler, Rules of React, and the Hooks lint plugin. React 19 adds Actions, `useActionState`, form Actions, `useFormStatus`, `useOptimistic`, the `use` API, Server Components, Server Actions, `ref` as a prop, context providers rendered as `<Context>`, and metadata support.

Next.js currently documents App Router and Pages Router. App Router pages and layouts are Server Components by default; Client Components are needed for state, event handlers, Effects, browser APIs, and custom Hooks. The official guidance emphasizes serializable props at the boundary, narrow `use client` boundaries, server-side secrets, `server-only`, `src/app`, route files, dynamic segments, route groups, private folders, loading/error/not-found boundaries, data fetching, streaming, caching, revalidation, Route Handlers, and Server Actions.

The official `src` guidance states that `src/app` or `src/pages` is optional, while `public`, package manifests, Next configuration, TypeScript configuration, and environment files remain at the root. A root-level `app` or `pages` takes precedence over the equivalent directory under `src`, so the course explicitly teaches learners not to maintain duplicate routers.

The recorded package baseline is React 19.2.8, React DOM 19.2.8, Next.js 16.3.1, TypeScript 7.0.2, Vite 8.2.2, and ESLint 10.8.1. These values should be refreshed against official release notes before a future cohort starts.

## References

1. [React Learn](https://react.dev/learn)
2. [React Reference Overview](https://react.dev/reference/react)
3. [React Server Components](https://react.dev/reference/rsc/server-components)
4. [React 19](https://react.dev/blog/2024/12/05/react-19)
5. [Next.js Documentation](https://nextjs.org/docs)
6. [Next.js Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
7. [Next.js `src` Folder](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)
8. [Next.js Installation](https://nextjs.org/docs/app/getting-started/installation)
9. [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
10. [Next.js Fetching Data](https://nextjs.org/docs/app/building-your-application/data-fetching)
11. [Next.js Caching](https://nextjs.org/docs/app/building-your-application/caching)
