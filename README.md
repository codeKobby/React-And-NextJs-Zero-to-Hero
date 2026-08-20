# React and Next.js Zero to Hero

A **61-day beginner-first course** for learning modern React and Next.js from the ground up. The course starts with the JavaScript and browser ideas that React relies on, teaches React in isolation, then introduces Next.js App Router and full-stack rendering one boundary at a time.

The course targets **React 19.2.8** and **Next.js 16.3.1** as the validation baseline recorded on 20 August 2026. Always check the official release notes before starting a new production project.

## Contents

| Section | Link |
| --- | --- |
| Setup | [SETUP.md](SETUP.md) |
| Modern toolchain | [MODERN_TOOLCHAIN.md](MODERN_TOOLCHAIN.md) |
| Beginner tutorial standard | [LESSON_STANDARD.md](LESSON_STANDARD.md) |
| Project structure guide | [PROJECT_STRUCTURE_GUIDE.md](PROJECT_STRUCTURE_GUIDE.md) |
| 61-day curriculum | [DAY_INDEX.md](DAY_INDEX.md) |
| Official research findings | [OFFICIAL_RESEARCH.md](OFFICIAL_RESEARCH.md) |
| Course quality checks | [COURSE_QUALITY_STANDARD.md](COURSE_QUALITY_STANDARD.md) |

## The learning loop

Read the **Keywords and terms** table first. Then follow the named **Topics** in order. Copy the complete worked example, run it unchanged, read it line by line, predict one normal and one boundary result, run the prediction experiment, repair the deliberately broken version, and complete the guided practice before attempting the numbered exercises.

A lesson is not complete because the code compiles. It is complete when you can explain what the runtime did, why the component or route owns each value, what happens while work is loading, what happens when it fails, and what the example still does not prove.

## What the course covers

The React sequence covers JSX, components, function and class components, props, composition, lists and keys, events, forms, controlled and uncontrolled inputs, state and setters, JavaScript property getters and setters, derived state, lifting state, reducers, Context, Effects, cleanup, refs, custom Hooks, memoization, transitions, Suspense, testing, accessibility, performance, security, TypeScript, React 19 Actions, `useActionState`, `useFormStatus`, `useOptimistic`, the `use` API, metadata, ref changes, and the React Compiler.

The Next.js sequence covers `create-next-app`, App Router, Pages Router history, root-level `app/` versus `src/app/`, aliases, layouts, pages, dynamic segments, route groups, private folders, loading and error boundaries, `not-found`, metadata, images, fonts, Server and Client Components, server-only boundaries, data fetching, caching, revalidation, streaming, Route Handlers, Server Actions, forms, authentication and authorization boundaries, testing, accessibility, performance, deployment, migration, and a final full-stack capstone.

## Project layout decision

The main projects use `src/` so application code is separated from root configuration:

```text
src/app/
src/components/
src/lib/
public/
package.json
next.config.ts
tsconfig.json
.env.local
```

Next.js also supports keeping `app/`, `components/`, and `lib/` at the repository root. Both choices are valid. Do not keep both a root `app/` and `src/app/` for the same router: the root-level special directory takes precedence. The course explains this decision in [PROJECT_STRUCTURE_GUIDE.md](PROJECT_STRUCTURE_GUIDE.md).

## Safety and reliability

All exercises use local or synthetic data. Never paste credentials, private logs, production tokens, or personal information into a practice project. A passing test or build is evidence about the tested fixture, not proof that a production application is secure. Every full-stack lesson names its trust boundary, validation policy, authorization rule, failure behavior, and residual risk.

## Official references

- [React Learn](https://react.dev/learn)
- [React Reference](https://react.dev/reference/react)
- [React 19](https://react.dev/blog/2024/12/05/react-19)
- [Next.js Documentation](https://nextjs.org/docs)
- [Next.js Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
- [Next.js `src` Folder](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)
- [Next.js Installation](https://nextjs.org/docs/app/getting-started/installation)
