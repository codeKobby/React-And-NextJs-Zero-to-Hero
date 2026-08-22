# Day 075: Next.js 16 Proxy and the middleware migration

[← Previous lesson](../day_074_secure_sessions_and_cookie_policy/day_074_secure_sessions_and_cookie_policy.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_076_authorization_roles_ownership_and_multi_tenant_data/day_076_authorization_roles_ownership_and_multi_tenant_data.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is Proxy in Next.js 16?](#what-is-proxy-in-next-js-16)
  - [Why did middleware become proxy?](#why-did-middleware-become-proxy)
  - [What does a matcher do?](#what-does-a-matcher-do)
  - [When should Proxy redirect or rewrite?](#when-should-proxy-redirect-or-rewrite)
  - [Why is Proxy not final authorization?](#why-is-proxy-not-final-authorization)
- [Worked example](#worked-example)
  - [Example 1: a narrow dashboard matcher](#example-1-a-narrow-dashboard-matcher)
  - [Example 2: an optimistic signed-out redirect](#example-2-an-optimistic-signed-out-redirect)
  - [Example 3: keep the server check authoritative](#example-3-keep-the-server-check-authoritative)
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

Use the Next.js starter from [examples](../examples/README.md). Read the [README](../README.md), [setup](../SETUP.md), and the starter's `proxy.ts`. Run the local dashboard route before changing the matcher. Use synthetic cookies and local routes; do not connect a real account.

## Why this lesson exists

A user who is clearly signed out should not wait for a protected dashboard to render before being sent to a login page. A request interception boundary can make that navigation feel immediate and can apply broad route-level rules before rendering.

Next.js 16 calls this file convention **Proxy**. Older material calls the same family of behavior **Middleware**. The rename is not permission to copy an old tutorial without checking its runtime and security assumptions. Proxy can redirect or rewrite based on request information, but the data access and mutation boundary must still perform authoritative authentication and authorization.

## Prerequisites

Complete routing, Server and Client Components, cookies and sessions, and the authentication boundary lesson. You need to read a request URL and understand that a browser cookie is input, not proof of permission.

## Outcomes

You should be able to create a narrowly matched `proxy.ts`, explain the middleware-to-Proxy terminology change, choose redirect versus rewrite, distinguish an optimistic navigation check from final authorization, and test a signed-out request without claiming that a redirect protects the data layer.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Proxy** | A Next.js request-boundary file convention that can run logic before a matched route continues. |
| **Middleware** | The older name used in earlier Next.js documentation and projects for related request interception. |
| **Matcher** | Configuration that limits which request paths invoke Proxy. |
| **Redirect** | A response that sends the browser to another URL. |
| **Rewrite** | A response that serves another route while preserving the visible URL. |
| **Optimistic check** | A fast navigation decision that improves flow but is not the final authority for protected data. |
| **Authorization** | The server-side decision about what an identified actor may read or change. |

## Topics

### What is Proxy in Next.js 16?

Proxy is a request-boundary convention. It can inspect a matched request and return a redirect, rewrite, or continuation. It is useful for broad navigation and request shaping, but it should remain small and predictable.

### Why did middleware become proxy?

The current terminology emphasizes that the file operates as a network request boundary rather than a general place to put application logic. When maintaining an older project, recognize `middleware.ts`; when teaching the current Next.js 16 convention, use `proxy.ts` and verify the version's documentation.

### What does a matcher do?

A matcher limits the paths that run the Proxy function. Narrow matching reduces unexpected work and makes the security and performance scope reviewable. A matcher is not a permission rule; it only chooses which requests reach the function.

### When should Proxy redirect or rewrite?

Redirect when the browser should move to another URL, such as sending a signed-out visitor to `/login`. Rewrite when the visible URL should remain while the server chooses another route representation. Use the smallest behavior that matches the user flow.

### Why is Proxy not final authorization?

Cookies can be missing, expired, malformed, or forged. A Proxy decision can be bypassed by another route, a direct server call, or a future code path. The protected page, repository, Server Action, or Route Handler must still identify the actor and check permission or ownership before returning or changing data.

## Worked example

### Example 1: a narrow dashboard matcher

`proxy.ts` at the project root:

```tsx
import { NextRequest, NextResponse } from 'next/server';

export function proxy(request: NextRequest) {
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*'],
};
```

The matcher means the function is relevant to dashboard paths, not every static asset or public page. Start by logging only a local synthetic path if you need to inspect it; do not log cookies.

### Example 2: an optimistic signed-out redirect

```tsx
import { NextRequest, NextResponse } from 'next/server';

export function proxy(request: NextRequest) {
  const hasSessionHint = request.cookies.has('session');

  if (!hasSessionHint) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*'],
};
```

**Visible behavior:** a request without the cookie hint is sent to `/login`, while a request with the hint continues toward the dashboard. The cookie's presence is only a hint. The dashboard page or data function must verify the session and authorization before returning records.

### Example 3: keep the server check authoritative

```tsx
// src/lib/auth/require-case-access.ts
import 'server-only';

export async function requireCaseAccess(caseId: string) {
  const actor = await requireSession();
  const record = await caseRepository.findForActor(caseId, actor.userId);

  if (!record) {
    throw new Error('Not found or not permitted');
  }

  return record;
}
```

Proxy can improve navigation; this server-only function protects the data boundary. Never remove this check because the dashboard matcher exists.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `import { NextRequest, NextResponse } ...` | Imports request and response types for the request boundary. |
| `request.cookies.has('session')` | Checks for a cookie hint; it does not verify identity or permission. |
| `NextResponse.redirect(...)` | Sends the browser to login for the optimistic signed-out flow. |
| `NextResponse.next()` | Allows the matched request to continue. |
| `matcher: ['/dashboard/:path*']` | Limits the scope to dashboard paths. |
| `import 'server-only'` | Prevents the authoritative data module from entering a client graph. |
| `findForActor(caseId, actor.userId)` | Combines the requested record with the server-derived actor scope. |
| `if (!record)` | Refuses to return data when ownership or permission is absent. |

## Execution trace

1. A browser requests `/dashboard`.
2. Next.js checks whether the path matches `/dashboard/:path*`.
3. Proxy checks for a session hint. With no hint, it redirects to `/login`.
4. With a hint, Proxy allows the request to continue.
5. The dashboard's server data function still verifies the session and queries records for the actor.
6. A missing or unauthorized record is refused at the authoritative data boundary.

## Prediction experiment

Predict what happens for `/`, `/public`, `/dashboard`, `/dashboard/settings`, and a static asset. Predict the result when a forged cookie is present. Move the server authorization check out of the repository and explain which request path could now leak data. Restore the check before considering the experiment complete.

## Broken example and repair

**Broken version:** say “the dashboard is protected because Proxy found a cookie.” Repair the claim and the code: Proxy is an optimistic navigation check; session verification and authorization remain immediately before protected reads and mutations.

Another failure is a matcher that runs on every path and performs expensive or logging-heavy work. Narrow it to the route family that actually needs the navigation decision.

## Guided practice before independent work

Run the existing starter Proxy with a public route and dashboard route. Narrow the matcher. Add a signed-out redirect. Add a signed-in continuation. Then inspect the dashboard data boundary and add a separate synthetic actor check. Do not put a database query in Proxy.

## Project application

Protect the local **dashboard route** with an optimistic redirect for a missing synthetic session cookie, then protect the case repository with an authoritative actor check. Add a test matrix for signed out, signed in, forbidden, and owned record cases.

## Independent exercises

### Level 1 — Confidence
1. What is Next.js 16 Proxy and the middleware migration? Answer in one sentence.
2. Locate the root `proxy.ts` and explain its role.
3. Add a narrow dashboard matcher.
4. Redirect a request with no session hint.
5. Let a request with a hint continue.

### Level 2 — Application
6. Test nested dashboard paths.
7. Verify public paths are not matched.
8. Add a server-only authoritative record check.
9. Document the difference between a cookie hint and verified session.

### Level 3 — Synthesis
10. Reproduce the “Proxy is authorization” mistake and repair the architecture.
11. Add signed-out, forged-cookie, forbidden, and owned-record fixtures.
12. Add a route or repository contract test.
13. Test one public path and one protected path. Write which path redirects and which path does not.

## Finish line

You are ready when you can explain the middleware-to-Proxy migration, write a narrow matcher, and defend the statement that Proxy improves navigation but never replaces the final server authorization check.

## References

- [Next.js: Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
- [Next.js: Authentication](https://nextjs.org/docs/app/guides/authentication)
- [Next.js: Middleware migration guidance](https://nextjs.org/docs/messages/middleware-to-proxy)
