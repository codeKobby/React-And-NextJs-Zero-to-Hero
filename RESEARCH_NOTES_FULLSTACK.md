# Full-stack curriculum research notes

## Next.js installation

Source: [Next.js Installation](https://nextjs.org/docs/app/getting-started/installation), accessed 20 August 2026.

The current Next.js 16.3.1 installation documentation recommends `pnpm create next-app@latest my-app --yes`, followed by `cd my-app` and `pnpm dev`. The recommended defaults enable TypeScript, Tailwind CSS, ESLint, the App Router, Turbopack, and an import alias such as `@/*`. The App Router uses React canary releases built into the framework, including stable React 19 changes and newer features being validated in frameworks. Next.js supports a root `public/` directory for static assets and has a dedicated Proxy section in the current documentation navigation.

Curriculum implication: Tailwind CSS must be taught as part of the actual starter and not merely mentioned. The course should explicitly explain the `create-next-app` defaults, the relationship between Tailwind utility classes and the component tree, and how the starter's `src/app/` structure relates to the root `public/` directory.

## shadcn/ui installation

Source: [shadcn/ui Next.js installation](https://ui.shadcn.com/docs/installation/next), accessed 20 August 2026.

The current shadcn/ui documentation says that recommended `create-next-app` defaults already cover Tailwind CSS and import aliases. For an older or custom project, Tailwind CSS should be installed first. The TypeScript alias must be configured as `@/*`; when the project uses `--src-dir`, the alias should point to `./src/*`. The current workflow offers a visual `shadcn/create` path, a CLI path, and an existing-project path, followed by adding individual components. The generated component code is intended to live in the learner's project and be customized rather than treated as a black-box package.

Curriculum implication: teach `components.json`, the `@/*` alias, `src`-aware alias configuration, component installation, composition, accessible primitives, theming, dark mode, and the distinction between copying/customizing shadcn component source and importing an opaque UI library.

## Next.js 16 Proxy and middleware migration

Sources: [Proxy file convention](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) and [Middleware-to-Proxy migration](https://nextjs.org/docs/messages/middleware-to-proxy), accessed 20 August 2026.

The current Next.js 16.3.1 documentation states that the `middleware` file convention is deprecated and has been renamed to `proxy`. A `proxy.ts` or `proxy.js` file may live at the project root or inside `src` when applicable, at the same level as `app` or `pages`. Proxy code runs on the server before routes are rendered and can rewrite, redirect, modify request or response headers, or respond directly. The official guidance emphasizes that Proxy should be invoked separately from render code and used in optimized cases such as authentication, logging, or redirects; it should not become a general-purpose data-fetching or render layer. Information is passed to the application through headers, cookies, rewrites, redirects, or the URL. The page also shows matcher configuration for limiting which paths execute.

Curriculum implication: teach both the historical `middleware.ts` name and the current Next.js 16 `proxy.ts` name, including migration language. Learners should build a small synthetic auth redirect and logging example, study matcher scope and failure behavior, and explicitly learn that Proxy is not a substitute for server-side authorization in the route, Server Action, or data layer.

## Tailwind CSS v4 with Next.js

Source: [Tailwind CSS: Install Tailwind CSS with Next.js](https://tailwindcss.com/docs/installation/framework-guides/nextjs), accessed 20 August 2026.

The current Tailwind CSS v4.3 guide installs `tailwindcss`, `@tailwindcss/postcss`, and `postcss`, configures `@tailwindcss/postcss` in `postcss.config.mjs`, imports Tailwind with `@import "tailwindcss";` in the global stylesheet, and then uses utility classes in JSX. The guide demonstrates the standard Next.js project flow and a utility-class example.

Curriculum implication: teach the actual v4 CSS import and PostCSS setup, utility-class composition, responsive states, dark mode, theme variables, accessibility, and the difference between a utility class, a component abstraction, and a design token.

## Next.js authentication architecture

Source: [Next.js Authentication Guide](https://nextjs.org/docs/app/guides/authentication), accessed 20 August 2026.

The current guide separates authentication (proving identity), session management (tracking auth state across requests), and authorization (deciding what routes and data a user may access). It recommends forms with Server Actions and `useActionState` for credential capture and server-side validation, with schema validation libraries such as Zod, Valibot, or Yup where needed. It describes server-only session logic, encrypted or signed sessions, and cookies configured with `HttpOnly`, `Secure`, `SameSite`, `Max-Age` or `Expires`, and `Path`. It also distinguishes optimistic Proxy checks from secure authorization in the data-access layer.

Curriculum implication: the capstone must include a synthetic login flow, validation, session cookie policy, Proxy redirect as an optimistic check, and authoritative authorization immediately before protected data access or mutation. Learners should understand that hiding a button or redirecting in Proxy is not the complete authorization control.
