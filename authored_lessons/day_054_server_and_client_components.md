# Day 046: Server and Client Components

[← Previous lesson](../day_045_metadata_images_fonts_and_public_assets/day_045_metadata_images_fonts_and_public_assets.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_047_server_only_and_client_only_boundaries/day_047_server_only_and_client_only_boundaries.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What is a Server Component?](#what-is-a-server-component)
  - [What is a Client Component?](#what-is-a-client-component)
  - [When is `use client` necessary?](#when-is-use-client-necessary)
  - [What can cross the boundary?](#what-can-cross-the-boundary)
  - [Why keep the client boundary narrow?](#why-keep-the-client-boundary-narrow)
- [Worked example](#worked-example)
  - [Example 1: a server-rendered case page](#example-1-a-server-rendered-case-page)
  - [Example 2: move only the interactive leaf](#example-2-move-only-the-interactive-leaf)
  - [Example 3: pass serializable data](#example-3-pass-serializable-data)
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

Open the Next.js starter from [examples](../examples/README.md):

```bash
cd examples/next-app
pnpm dev
```

Read the [README](../README.md) and [setup guide](../SETUP.md) first. Inspect `src/app/page.tsx`, then create a small `src/components/interactive/LikeButton.tsx`. Use only local synthetic data. The goal is not to label every file; it is to decide which side should own each responsibility.

## Why this lesson exists

The App Router gives Next.js a useful default: components are Server Components unless a module opts into the client. That means a page can read server-owned data and render HTML without sending every data-access detail and interactive dependency to the browser.

Interactivity still belongs somewhere. A button with state, an event handler, or a browser API must be a Client Component. The mistake is to make the entire page client-side because one button is interactive. We will start with a server page, move only the button across the boundary, and pass a serializable value down.

## Prerequisites

Complete routes, layouts, metadata, React state, events, and TypeScript props. You need to know that a Next.js page can be an async function and that a Client Component starts with `'use client'`.

## Outcomes

You should be able to identify Server and Client Components, justify a `use client` boundary, pass serializable props across it, keep secrets and server queries on the server, and repair the mistake of importing a browser-only or stateful module into a Server Component.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Server Component** | A component rendered by Next.js on the server and not shipped as interactive client JavaScript by default. |
| **Client Component** | A module marked with `'use client'` that can use state, event handlers, and browser APIs. |
| **Client boundary** | The point where a module graph becomes client-side and its props must cross into the browser. |
| **Serializable prop** | Data that can be represented across the server-to-client boundary, such as strings, numbers, arrays, and plain objects. |
| **Hydration** | Connecting client JavaScript to server-rendered HTML so it can become interactive. |
| **Server-only** | Code that must not enter the browser bundle because it accesses secrets, a database, or private authority. |

## Topics

### What is a Server Component?

A Server Component runs as part of the server-rendered route. It can access server-only modules and await data without turning the page into a browser bundle. It cannot use browser event handlers or state Hooks.

### What is a Client Component?

A Client Component is a module whose graph begins at `'use client'`. It can use `useState`, `onClick`, refs, and browser APIs. It is not the same as “a component that must render only in a browser”; Next.js may still use it to produce initial HTML before hydration.

### When is `use client` necessary?

Use it at the smallest module boundary that needs state, event handlers, effects, or browser-only APIs. Do not add it because a component is visually important or because a parent happens to render a button.

### What can cross the boundary?

Props crossing from Server to Client Components must be serializable. A string, number, boolean, array, or plain object can usually cross. A database connection, function closure, class instance, or secret cannot be passed as an ordinary client prop.

### Why keep the client boundary narrow?

A narrow boundary keeps server data access and client JavaScript responsibilities clear. It can reduce browser work and prevents accidentally importing server-only dependencies into the client graph. The boundary is an architecture decision, not just a compiler fix.

## Worked example

### Example 1: a server-rendered case page

`src/app/page.tsx` can remain a Server Component:

```tsx
import LikeButton from '@/components/interactive/LikeButton';

const caseRecord = {
  id: 'case-001',
  title: 'Review access policy',
  likes: 3,
};

export default function HomePage() {
  return (
    <main>
      <h1>{caseRecord.title}</h1>
      <p>Server-provided likes: {caseRecord.likes}</p>
      <LikeButton initialLikes={caseRecord.likes} />
    </main>
  );
}
```

The page owns the local server-side fixture. It does not need `use client` because it has no event handler or state.

### Example 2: move only the interactive leaf

`src/components/interactive/LikeButton.tsx`:

```tsx
'use client';

import { useState } from 'react';

export default function LikeButton({ initialLikes }: { initialLikes: number }) {
  const [likes, setLikes] = useState(initialLikes);

  return (
    <button type="button" onClick={() => setLikes((current) => current + 1)}>
      Likes: {likes}
    </button>
  );
}
```

Only the button needs client behavior. The page remains a Server Component and passes a number.

### Example 3: pass serializable data

A server component can pass a plain view model:

```tsx
type CaseSummary = { id: string; title: string; severity: 'low' | 'high' };

export default function CasePage() {
  const summary: CaseSummary = {
    id: 'case-001',
    title: 'Review access policy',
    severity: 'high',
  };

  return <CaseBadge summary={summary} />;
}
```

The client component can display the summary. It should not receive a database client, a secret, or a function that closes over server authority. If it needs a server mutation, use a documented Server Action or Route Handler boundary later in the course.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `import LikeButton ...` | The server page composes an interactive leaf without becoming interactive itself. |
| `const caseRecord = ...` | Creates a local plain-object view model; a real query would remain server-side. |
| `<LikeButton initialLikes={...} />` | Passes a serializable number across the boundary. |
| `'use client'` | Marks the module graph below this file as client-capable. |
| `useState(initialLikes)` | Gives the client leaf interactive local state initialized from the server value. |
| `onClick={...}` | Requires the client boundary because the browser must handle the event. |
| `CaseSummary` | Records a serializable shape, not a database row or connection. |

## Execution trace

1. Next.js evaluates the server page and creates the case view model on the server.
2. The page returns an `h1`, a paragraph, and a reference to `LikeButton` with the number `3`.
3. Next.js renders the page and prepares the client boundary payload.
4. The browser receives the initial output and the code needed for the interactive leaf.
5. Hydration connects the button's event handler.
6. A click updates the Client Component's local state; the server page does not rerun just because the button's local count changed.

## Prediction experiment

Add `useState` to `page.tsx` without adding `'use client'`. Put `'use client'` at the top of the entire page and compare the module boundary. Try to pass a function prop from the server page to the client button. Predict which errors or constraints appear and explain why.

## Broken example and repair

**Broken version:** import a component that uses `useState` into a Server Component without a client boundary, or pass a database client as a prop to a Client Component.

Repair the first by moving interactivity into a small `'use client'` leaf. Repair the second by passing a serializable view model and keeping the database access on the server. Do not “fix” a server/client boundary by exposing a secret or moving the database query into browser code.

## Guided practice before independent work

Start with a static Server Component. Add one Client Component button. Pass a number. Add local button state. Then attempt a function prop and observe the boundary rule. Finally, write which side owns data access and which side owns interaction.

## Project application

Add an interactive **case bookmark** button to the Next.js dashboard. Keep the case summary server-rendered and move only the bookmark interaction into a Client Component. Use a serializable synthetic summary and document the boundary in a comment or architecture note.

## Independent exercises

### Level 1 — Confidence

1. Identify which starter file is a Server Component by default.
2. Add a static case summary.
3. Create a Client Component button with local state.
4. Pass a serializable number or string.

### Level 2 — Application

5. Move only the interactive leaf across the boundary.
6. Add an accessible button name and pending or disabled behavior if needed.
7. Attempt a function prop and explain the limitation.
8. Keep a synthetic server view model separate from the client state.

### Level 3 — Synthesis

9. Reproduce the server/client import failure and repair it narrowly.
10. Add a test or manual evidence note for initial server output and client interaction.
11. Explain why a narrow client boundary helps bundle and authority reasoning.
12. Write a review note with the module graph, serializable props, server-only data, visible evidence, and limitation.

## Finish line

You are ready when you can draw the server/client boundary, justify every `use client`, pass a plain view model, and explain why an interactive button does not require the whole page to become client code.

## References

- [Next.js: Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Next.js: Composition Patterns](https://nextjs.org/docs/app/building-your-application/rendering/composition-patterns)
- [React: Server Components](https://react.dev/reference/rsc/server-components)
