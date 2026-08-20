# Full-stack extension design

The existing 61 days establish JavaScript, TypeScript, React, and the Next.js App Router. The extension adds a second, application-building track so the learner can move from framework concepts to a complete, reviewable Next.js product.

| Days | Application capability |
| --- | --- |
| 062–063 | Tailwind CSS v4 setup, utility classes, responsive layout, theme variables, dark mode, and accessible visual states |
| 064–065 | shadcn/ui installation, `components.json`, aliases, generated component source, composition, forms, dialogs, tables, and accessible primitives |
| 066 | Dashboard shell, navigation, route groups, and feature-based folder boundaries |
| 067 | Zod-style schema validation, typed form state, and safe input boundaries |
| 068–069 | SQL mental model, SQLite/Drizzle ORM, migrations, seed data, and repository/data-access layers |
| 070 | Server Actions for mutations, optimistic UI, validation, authorization, and revalidation |
| 071–072 | HTTP API contracts, typed errors, authentication concepts, provider boundaries, and secure session cookies |
| 073 | Next.js 16 `proxy.ts`, historical `middleware.ts`, matcher scope, redirects, and the limits of optimistic checks |
| 074 | Authorization, roles, permissions, ownership, multi-tenant boundaries, and authoritative server checks |
| 075 | File uploads, metadata, size/type limits, storage boundaries, and safe download responses |
| 076 | Error taxonomy, structured logging, request IDs, instrumentation, and useful observability |
| 077 | Component, route, Server Action, and Playwright end-to-end testing with synthetic fixtures |
| 078 | Environment configuration, migrations, CI, deployment, backups, and production readiness evidence |
| 079 | Capstone architecture, threat model, data model, UI system, route map, and delivery plan |
| 080 | Capstone implementation: public shell, dashboard, design system, database-backed read paths, and loading/error states |
| 081 | Capstone implementation: auth, proxy, authorization, mutations, testing, deployment checklist, and portfolio demonstration |
| 082 | Capstone hardening: failure paths, security review, accessibility evidence, logging, and rollback rehearsal |
| 083 | Capstone presentation: portfolio README, architecture walkthrough, test/build evidence, residual risk, and next steps |

The examples remain local and synthetic. The course teaches provider and storage integration as replaceable boundaries, not as an excuse to put credentials or personal data into the repository.
