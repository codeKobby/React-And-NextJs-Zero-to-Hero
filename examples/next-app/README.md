# Next.js App Router starter

This example intentionally uses `src/app` rather than a root-level `app` directory. The root contains configuration, `public`, `components.json`, `postcss.config.mjs`, and the current Next.js 16 `proxy.ts` convention; application code lives under `src`.

```text
components.json
postcss.config.mjs
proxy.ts
src/app/layout.tsx
src/app/page.tsx
src/app/dashboard/page.tsx
src/app/globals.css
src/components/interactive/Counter.tsx
src/components/ui/button.tsx
src/lib/utils.ts
public/
package.json
next.config.ts
tsconfig.json
```

The starter is deliberately small but real. It includes Tailwind CSS v4, a `cn()` class-merging utility, and an owned Button primitive shaped like a shadcn/ui component. Read and modify the component source instead of treating it as a black box. The `/dashboard` route is matched by `proxy.ts`; it uses a synthetic cookie only for an optimistic redirect lesson, and it is not a substitute for server-side authorization.

Run `pnpm install`, then `pnpm dev`. The lessons add routes, layouts, boundaries, schema validation, data access, forms, sessions, authorization, tests, and deployment policies one step at a time. Keep all starter data local and synthetic.
