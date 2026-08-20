# Next.js project structure guide

Next.js supports storing application code directly at the repository root or under an optional `src/` folder. Both layouts use the same framework conventions; the choice is about organization, not capability.

| Choice | Example | Why choose it |
| --- | --- | --- |
| Root-level application code | `app/`, `components/`, `lib/` | Shorter paths and a small project with little configuration |
| `src/` application code | `src/app/`, `src/components/`, `src/lib/` | Separates application code from root configuration and is useful as a project grows |

The main projects in this course use `src/`. The root must still contain `public/`, `package.json`, `next.config.ts`, `tsconfig.json`, and `.env.*` files. If you use import aliases such as `@/components/Button`, configure `baseUrl` and `paths` to point into the chosen source directory.

Do not keep both `app/` and `src/app/` for the same application. A root-level `app/` or `pages/` takes precedence over the corresponding directory under `src/`, which can make a learner edit one file while Next.js renders another.

## Route files

A folder becomes a public route only when it contains `page.tsx` or `route.ts`. `layout.tsx` wraps child pages and preserves shared UI during navigation. `loading.tsx` provides a loading boundary, `error.tsx` provides an error boundary, and `not-found.tsx` describes missing resources.

```text
src/app/
├── layout.tsx                 # root layout
├── page.tsx                   # /
├── dashboard/
│   ├── layout.tsx             # shared dashboard shell
│   ├── loading.tsx            # dashboard loading UI
│   ├── page.tsx               # /dashboard
│   └── settings/page.tsx     # /dashboard/settings
├── blog/[slug]/page.tsx       # dynamic route
├── (marketing)/about/page.tsx # route group; URL remains /about
└── _components/Nav.tsx        # private, non-routable implementation file
```

Folders in `app/` map to URL segments. Square brackets create dynamic segments. Parentheses create route groups that organize files without changing the URL. An underscore-prefixed folder is a useful private implementation convention, although files can also be colocated without becoming public routes unless they are special route files.

## Design rule

Keep route files responsible for route composition and data boundaries. Keep reusable UI in components, server data access in `lib` or feature modules marked `server-only`, and interactive state in narrow Client Components. The right structure is the one that makes ownership, rendering environment, and test boundaries obvious to the next reader.

## References

- [Next.js Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
- [Next.js `src` Folder](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)
- [Next.js Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)
