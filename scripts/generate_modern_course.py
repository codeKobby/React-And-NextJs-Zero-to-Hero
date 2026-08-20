from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LESSONS = [
    ("JavaScript modules and the browser runtime", "JavaScript modules, browser, Node.js, strict mode, import, export", "What is a JavaScript runtime?;What is a module?;Why does the browser environment differ from Node.js?;How do we inspect a small program?", "export const lesson = 'runtime';\nconsole.log(lesson);", "runtime\n", "Use a module export but forget to import it, then repair the import path."),
    ("HTML, CSS, accessibility, and the DOM", "DOM, element, attribute, semantic HTML, accessibility, event", "What is the DOM?;Why does semantic HTML matter?;How does a browser event reach code?;What does React improve and what does it not replace?", "const button = document.querySelector('button');\nbutton?.addEventListener('click', () => console.log('clicked'));", "clicked\n", "Select a missing element and explain why optional chaining prevents a crash but does not create the element."),
    ("Modern JavaScript for React", "expression, destructuring, spread, map, promise, async, immutability", "Which JavaScript expressions appear in JSX?;Why does map return a new array?;What does immutability mean?;Which JavaScript mistakes look like React mistakes?", "const names = ['Ada', 'Lin'];\nconst labels = names.map((name) => `User: ${name}`);\nconsole.log(labels);", "[ 'User: Ada', 'User: Lin' ]\n", "Mutate the original array, observe the change, and repair the code with a copied array."),
    ("TypeScript foundations for UI code", "type, annotation, inference, union, interface, narrowing", "What problem does TypeScript solve?;What is inference?;How do unions describe real UI states?;What can TypeScript not know at runtime?", "type Status = 'idle' | 'loading' | 'success' | 'error';\nconst status: Status = 'loading';\nconsole.log(status);", "loading\n", "Assign an invalid status, read the compiler message, and repair the value rather than weakening the type."),
    ("Tooling and the first component", "package.json, bundler, component, JSX, render, dev server", "What does a toolchain do?;What is a React component?;How does JSX become browser output?;How do we verify a first component?", "function Greeting() {\n  return <h1>Hello, learner</h1>;\n}\nconsole.log(Greeting().type);", "h1\n", "Return a lowercase component name and explain why React treats it differently from a capitalized component."),
    ("What is a component?", "component, function component, props, return, composition", "What is a component?;Why are function components the modern default?;How do components compose?;What makes a component easy to review?", "function Badge({ label }) {\n  return <span>{label}</span>;\n}\nfunction App() {\n  return <Badge label=\"Ready\" />;\n}", "A Badge renders inside App.\n", "Call a component as an ordinary function and compare the result with rendering JSX."),
    ("JSX and the rules of markup", "JSX, fragment, className, expression, component name, escaping", "What is JSX?;Why must JSX have one returned root?;How do expressions enter JSX?;How do we keep markup accessible?", "const name = 'Ada';\nreturn <main><h1>Hello {name}</h1><p>Welcome.</p></main>;", "A heading and paragraph appear.\n", "Use class instead of className, read the error, and repair the JSX attribute."),
    ("Props and one-way data flow", "props, parent, child, read-only, callback prop, one-way flow", "What are props?;Why should a child not mutate props?;How does data move down?;How can a child request a parent change?", "function Button({ label, onPress }) {\n  return <button onClick={onPress}>{label}</button>;\n}", "The parent owns the data; the child receives it.\n", "Attempt to assign to a prop and replace the mutation with a callback."),
    ("Rendering lists and choosing keys", "map, key, identity, reconciliation, stable ID", "How do we render a list?;What is a key?;Why is array index a risky key?;How do stable identities prevent UI mistakes?", "const alerts = [{ id: 'a1', title: 'Review' }];\nreturn alerts.map((alert) => <li key={alert.id}>{alert.title}</li>);", "One list item renders.\n", "Use an array index as a key, reorder the data, and explain the identity bug."),
    ("Conditional rendering and empty states", "condition, ternary, logical AND, null, empty state", "How does React choose what to render?;When is a ternary clearer than &&?;What should an empty state say?;How do we avoid rendering zero accidentally?", "return items.length > 0 ? <List items={items} /> : <EmptyState />;", "The UI explains whether data is present.\n", "Render `items.length && ...` with an empty list and repair the stray zero."),
    ("Events and event handlers", "event, handler, callback, preventDefault, target, currentTarget", "What is an event handler?;Why pass a function instead of calling it?;How do we read event data?;When should we prevent default behavior?", "function SaveButton() {\n  function handleClick(event) {\n    console.log(event.currentTarget.textContent);\n  }\n  return <button onClick={handleClick}>Save</button>;\n}", "Save\n", "Write onClick={handleClick()} and repair the immediate invocation."),
    ("What is state?", "state, render, setter, snapshot, update, re-render", "What is state?;Why is state different from an ordinary variable?;What does a setter do?;Why does a state update cause another render?", "const [count, setCount] = useState(0);\nreturn <button onClick={() => setCount(count + 1)}>{count}</button>;", "The number increases after each click.\n", "Change a local variable instead of state and explain why the screen does not update."),
    ("useState and setters", "useState, setter, functional update, initial value, batching", "How does useState return a value and setter?;Why use a functional updater?;What does batching mean?;How should a setter be named?", "setCount((current) => current + 1);\nsetCount((current) => current + 1);", "The count increases twice safely.\n", "Call setCount(count + 1) twice and compare it with two functional updates."),
    ("State for objects and arrays", "immutability, object spread, array spread, update, reference", "Why should state updates create new references?;How do we update one object field?;How do we add and remove array items?;What is accidental mutation?", "setUser((user) => ({ ...user, name: 'Ada' }));\nsetItems((items) => [...items, newItem]);", "A new state reference is created.\n", "Call user.name = ... directly and repair it with an immutable update."),
    ("Derived state and the single source of truth", "derived value, source of truth, duplication, selector, invariant", "What is derived state?;Why should we avoid storing what can be calculated?;What is one source of truth?;How do selectors simplify state?", "const completed = tasks.filter((task) => task.done).length;\nreturn <p>{completed} complete</p>;", "The count is calculated from tasks.\n", "Store completedCount separately, create a mismatch, and repair by deriving it."),
    ("Controlled forms", "controlled input, value, onChange, form, validation, submit", "What makes an input controlled?;How do value and setter work together?;When should validation run?;How do we submit safely?", "const [email, setEmail] = useState('');\n<input value={email} onChange={(event) => setEmail(event.target.value)} />", "The input and state stay synchronized.\n", "Provide value without onChange, observe the locked input, and repair the pair."),
    ("Uncontrolled inputs and refs", "uncontrolled, ref, defaultValue, DOM node, useRef", "What is an uncontrolled input?;When is a ref useful?;What is the difference between value and defaultValue?;What should not be stored in refs?", "const inputRef = useRef(null);\nfunction focusInput() { inputRef.current?.focus(); }", "The input receives focus.\n", "Read ref.current during render and explain why refs are not reactive state."),
    ("Lifting state up", "lifting state, shared state, parent, callback, synchronization", "When should state move to a parent?;How do siblings share state?;What belongs in the parent?;How do callbacks move intent upward?", "<Editor value={text} onChange={setText} />\n<Preview value={text} />", "Both children show the same source.\n", "Give each sibling its own text state and repair the split-brain UI."),
    ("Reducers and dispatch", "reducer, action, dispatch, pure function, state transition", "What is a reducer?;Why name state transitions as actions?;What makes a reducer pure?;When is useReducer clearer than useState?", "function reducer(state, action) {\n  if (action.type === 'add') return [...state, action.item];\n  return state;\n}", "The reducer returns the next state.\n", "Mutate the reducer's state array and repair it with a new array."),
    ("Context and providers", "context, provider, consumer, default value, global state", "What problem does Context solve?;When is Context appropriate?;Where should a provider be placed?;Why is Context not a replacement for every state tool?", "const ThemeContext = createContext('light');\n<ThemeContext value=\"dark\"><Toolbar /></ThemeContext>", "Toolbar reads the shared theme.\n", "Put a provider too high, measure the conceptual scope, and move it closer to consumers."),
    ("What is useEffect?", "useEffect, effect, synchronization, dependency, cleanup", "What is an Effect?;Why is it for synchronization rather than ordinary calculations?;What does the dependency list mean?;When does cleanup run?", "useEffect(() => {\n  document.title = title;\n}, [title]);", "The document title follows title.\n", "Use an Effect to calculate a filtered array and replace it with a render-time calculation."),
    ("Effect dependencies and cleanup", "dependency array, stale closure, cleanup, subscription, abort", "What is a stale closure?;Why must dependencies be complete?;How do we clean up a subscription?;How do we abort a request?", "useEffect(() => {\n  const controller = new AbortController();\n  return () => controller.abort();\n}, [query]);", "Old work is cancelled when query changes.\n", "Omit query from dependencies and explain the stale result."),
    ("Custom Hooks", "custom Hook, reuse, hook rules, composition, return API", "What is a custom Hook?;Which logic belongs in a Hook?;Why must Hook names begin with use?;How do we design a small return API?", "function useToggle(initial = false) {\n  const [value, setValue] = useState(initial);\n  return [value, () => setValue((v) => !v)];\n}", "The Hook returns state and behavior.\n", "Call a Hook inside an if statement and move it to the component's top level."),
    ("Memoization and the React Compiler", "memoization, memo, useMemo, useCallback, compiler, purity", "What is memoization?;When can memoization help?;Why can premature memoization hurt clarity?;How does the React Compiler change the decision?", "const total = useMemo(() => calculateTotal(items), [items]);", "The calculation is reused for the same items reference.\n", "Memoize every value, then remove the unnecessary memo and explain the simpler code."),
    ("Transitions and responsive updates", "transition, startTransition, useTransition, deferred value, priority", "What is an urgent update?;What is a transition?;How does useTransition expose pending state?;When is useDeferredValue useful?", "const [isPending, startTransition] = useTransition();\nstartTransition(() => setQuery(nextQuery));", "The UI remains responsive while results update.\n", "Mark an input keystroke as a transition and explain why typing should remain urgent."),
    ("Suspense and the use API", "Suspense, fallback, promise, use, streaming, boundary", "What does Suspense coordinate?;What is a fallback?;How does use read a promise?;Where should a boundary live?", "<Suspense fallback={<p>Loading…</p>}><Comments promise={comments} /></Suspense>", "A loading fallback appears until data is ready.\n", "Remove the boundary around a suspending component and repair the missing fallback."),
    ("Function components versus class components", "class component, function component, render, this, lifecycle, migration", "What is a class component?;What is a function component?;How do lifecycle methods map to Hooks?;When must we read class code?", "class Counter extends React.Component {\n  state = { count: 0 };\n  render() { return <button>{this.state.count}</button>; }\n}", "The class renders its state.\n", "Use `this` inside a function component and repair the migration with useState."),
    ("Class lifecycle to modern Hooks", "componentDidMount, componentDidUpdate, componentWillUnmount, effect, cleanup", "What did lifecycle methods do?;How does one Effect model synchronization?;Why is lifecycle-to-Effect translation not mechanical?;What belongs outside Effects?", "useEffect(() => {\n  const connection = connect(roomId);\n  return () => connection.disconnect();\n}, [roomId]);", "The connection follows roomId.\n", "Copy three lifecycle methods into three Effects and consolidate the actual synchronization rule."),
    ("Error boundaries and failure UI", "error boundary, fallback, throw, recovery, reset", "What is an error boundary?;Which errors does it catch?;How should fallback UI help?;How can a user retry?", "return hasError ? <ErrorPanel onRetry={reset} /> : children;", "The UI explains failure and offers recovery.\n", "Catch an error with a broad try/catch in render and explain why a boundary is needed."),
    ("Testing components", "test, assertion, user behavior, query, mock, integration", "What should a component test prove?;Why test behavior rather than implementation?;How do we test a form?;What should remain real?", "render(<LoginForm />);\nawait user.type(screen.getByLabelText('Email'), 'a@example.com');", "The test follows a user's action.\n", "Select a private CSS class instead of an accessible label and repair the test target."),
    ("React 19 Actions", "Action, transition, pending, error, optimistic, mutation", "What is an Action?;Why do mutations need pending and error state?;How do Actions compose with transitions?;What remains application-specific?", "startTransition(async () => {\n  await saveProfile(formData);\n});", "The mutation has a pending period.\n", "Ignore a rejected promise and repair the error path."),
    ("useActionState and form actions", "useActionState, form action, previous state, FormData, pending", "What does useActionState return?;How does a form action receive FormData?;Where should validation happen?;How do we show field errors?", "const [state, action, pending] = useActionState(save, initialState);", "The form displays state and pending information.\n", "Read formData.get without checking its type and repair the validation boundary."),
    ("useFormStatus and useOptimistic", "useFormStatus, pending, optimistic update, rollback, status", "How can a child button know a form is pending?;What is an optimistic update?;When must optimistic UI roll back?;How do we communicate uncertainty?", "const { pending } = useFormStatus();\nconst [optimistic, addOptimistic] = useOptimistic(items);", "The button disables while the action runs.\n", "Show an optimistic success without handling failure and add a rollback explanation."),
    ("Metadata, refs, and modern React DOM", "metadata, title, meta, ref prop, ref cleanup, stylesheet", "How does React render metadata?;What changed for ref props?;What is ref cleanup?;How do DOM resources fit a component?", "return <><title>{title}</title><input ref={inputRef} /></>;", "The document title and input ref are managed declaratively.\n", "Return an element from a ref callback and repair the cleanup ambiguity."),
    ("React architecture and accessibility", "composition, semantic HTML, ARIA, focus, keyboard, design system", "How do we choose component boundaries?;What does semantic HTML provide?;When is ARIA needed?;How should focus move after an action?", "return <main><h1>Tasks</h1><button aria-label=\"Add task\">+</button></main>;", "The structure communicates meaning to browsers and assistive technology.\n", "Add a click-only div and repair it with a button or complete keyboard behavior."),
    ("React performance and profiling", "render, profiler, bottleneck, bundle, lazy, memoization", "What does performance mean?;How do we measure before optimizing?;What creates unnecessary renders?;When should code split?", "const Settings = lazy(() => import('./Settings'));\n<Suspense fallback={<p>Loading settings</p>}><Settings /></Suspense>", "Settings code loads when needed.\n", "Optimize a component without measuring it and replace the guess with a profiling plan."),
    ("React security and data boundaries", "XSS, escaping, dangerouslySetInnerHTML, secret, validation, trust boundary", "What does React escape?;Why is dangerouslySetInnerHTML dangerous?;Where do secrets belong?;How should user input be validated?", "return <p>{untrustedText}</p>;", "Untrusted text is rendered as text.\n", "Render raw HTML from a user field and repair it with safe text or a sanitizer policy."),
    ("Testing, linting, and project delivery", "lint, typecheck, test, build, CI, regression, review", "What does each check prove?;Why are lint and type checks different?;What belongs in CI?;How do we review a change?", "npm run lint && npm run typecheck && npm test && npm run build", "A clean pipeline gives evidence, not certainty.\n", "Skip the build because tests pass and explain the missing evidence."),
    ("Next.js installation and project structure", "create-next-app, App Router, TypeScript, ESLint, Tailwind, Turbopack, src", "What does create-next-app configure?;What belongs at the root?;What is the App Router?;What does the src choice change?", "src/app/page.tsx\nsrc/app/layout.tsx\npublic/logo.svg\npackage.json", "The route code is separated from configuration.\n", "Create both app/ and src/app/ and explain which one Next.js uses."),
    ("Root app versus src/app", "src, app, pages, precedence, configuration, alias", "Why use src?;When is root-level app simpler?;Which files stay at root?;Why must we not keep duplicate routers?", "compilerOptions: {\n  baseUrl: 'src',\n  paths: { '@/*': ['./*'] }\n}", "@/components maps inside src.\n", "Move app into src but leave an empty root app, then repair the ambiguous project."),
    ("Layouts, pages, and route segments", "page, layout, children, segment, nested layout, Link", "What makes a route public?;What does a layout preserve?;How do folders map to URLs?;How does Link navigate?", "app/layout.tsx\napp/page.tsx\napp/dashboard/page.tsx", "The files define / and /dashboard.\n", "Add a folder without page.tsx and explain why it is not public."),
    ("Dynamic routes and typed params", "dynamic segment, params, slug, catch-all, searchParams", "What is a dynamic segment?;How do params arrive?;When do we use searchParams?;What does catch-all mean?", "app/blog/[slug]/page.tsx\n\nexport default async function Page({ params }) {\n  const { slug } = await params;\n  return <h1>{slug}</h1>;\n}", "A URL slug becomes page data.\n", "Read params synchronously in a current async page signature and repair the promise handling."),
    ("Route groups and private folders", "route group, private folder, colocation, URL, layout scope", "What is a route group?;Why does parentheses not change the URL?;What is a private folder?;What can be colocated safely?", "app/(marketing)/about/page.tsx\napp/dashboard/_components/Nav.tsx", "The route remains /about while the code is organized.\n", "Put a route in a group and accidentally duplicate a URL; repair the folder plan."),
    ("Loading, error, and not-found UI", "loading, error boundary, not-found, reset, suspense, segment", "What should users see while data loads?;What does error.tsx catch?;When do we use notFound()?;How can a user retry?", "app/dashboard/loading.tsx\napp/dashboard/error.tsx\napp/dashboard/not-found.tsx", "Each boundary handles a different state.\n", "Use one generic spinner for every failure and replace it with state-specific UI."),
    ("Metadata, images, fonts, and public assets", "metadata, generateMetadata, Image, font, public, alt text", "Where does page metadata live?;Why use next/image?;What belongs in public?;How do alt text and font loading affect quality?", "export const metadata = { title: 'Dashboard' };\n<Image src=\"/avatar.png\" alt=\"Profile\" width={48} height={48} />", "The page has metadata and a described image.\n", "Use an image without alt text or dimensions and repair the accessibility/performance issues."),
    ("Server and Client Components", "Server Component, Client Component, use client, serializable props, module graph", "Which components are Server by default?;When is use client required?;What props can cross the boundary?;How do we keep the client bundle small?", "// Server Component\n<LikeButton likes={post.likes} />\n\n// Client Component\n'use client';\nconst [liked, setLiked] = useState(false);", "The server renders data and the client owns interaction.\n", "Put useState in a Server Component and move only the interactive leaf across the boundary."),
    ("Server-only and client-only boundaries", "server-only, client-only, environment poisoning, secret, NEXT_PUBLIC", "Why should secrets stay server-side?;What is environment poisoning?;How does server-only protect imports?;What belongs in NEXT_PUBLIC_?", "import 'server-only';\nexport async function getPrivateReport() { return db.report.findMany(); }", "A secret-bearing module cannot be imported into a client graph.\n", "Import a server data function into a Client Component and repair the boundary."),
    ("Fetching data in Server Components", "fetch, ORM, async component, request, authentication, authorization", "Where should a database query run?;How do we validate identity and permission?;Why can a Server Component access secrets?;What does the browser receive?", "export default async function Page() {\n  const posts = await getPosts();\n  return <PostList posts={posts} />;\n}", "The page receives server-fetched data without exposing the query client.\n", "Fetch private data without authorization and add the missing policy check."),
    ("Caching and revalidation", "cache, revalidate, tag, path, invalidation, fresh, stale", "What is a cache?;What should be cached?;When should data be revalidated?;How do tags and paths invalidate data?", "const data = await fetch(url, { next: { revalidate: 3600, tags: ['posts'] } });", "The policy states freshness and invalidation.\n", "Cache user-specific data globally and repair the scope and authorization policy."),
    ("Streaming and Suspense in Next.js", "streaming, Suspense, loading.tsx, skeleton, waterfall, boundary", "What is streaming?;Why do waterfalls happen?;Where should Suspense boundaries live?;What makes loading UI meaningful?", "<Suspense fallback={<PostSkeleton />}><SlowPostList /></Suspense>", "The page shell appears before the slow list.\n", "Place the boundary around the whole app and explain the lost progressive rendering."),
    ("Forms and Server Actions", "Server Action, use server, FormData, mutation, revalidatePath, redirect", "What is a Server Action?;How does a form call server code?;Where does validation happen?;How do we revalidate after mutation?", "'use server';\nexport async function createTask(formData: FormData) {\n  // validate, authorize, mutate\n}", "The server owns validation and mutation.\n", "Trust a FormData field as an authorized user ID and repair the authorization check."),
    ("Route Handlers and HTTP APIs", "route.ts, GET, POST, Request, Response, status, headers", "What is a Route Handler?;When do we need an HTTP endpoint?;How do we validate a request?;How should status and errors be shaped?", "export async function GET() {\n  return Response.json({ ok: true });\n}", "The endpoint returns a deliberate JSON response.\n", "Return 200 for invalid input and repair the status and error contract."),
    ("Authentication and authorization boundaries", "authentication, authorization, session, cookie, CSRF, role, least privilege", "What is the difference between authentication and authorization?;Where should session checks run?;Why is a hidden button not authorization?;How do roles limit data?", "const session = await requireSession();\nif (!session.can('case:read')) notFound();", "The server enforces access before returning data.\n", "Hide an admin link without protecting the route and repair the server-side check."),
    ("Testing Next.js applications", "unit test, integration test, E2E, route handler, fixture, mock", "What should be tested at each level?;How do we test a Server Action?;What is a safe fixture?;When is a browser test valuable?", "const response = await POST(new Request('http://test/api/tasks', { method: 'POST', body }));\nexpect(response.status).toBe(400);", "Invalid input produces a tested boundary response.\n", "Mock every internal detail and replace it with a contract-focused test."),
    ("Accessibility and resilient UI", "semantic HTML, keyboard, focus, aria, reduced motion, error message", "How does a full-stack app remain accessible?;Where do focus and errors live?;How do loading states help?;How do we test keyboard behavior?", "<label htmlFor=\"title\">Title</label>\n<input id=\"title\" aria-invalid={Boolean(error)} />", "The control has an accessible name and error signal.\n", "Use placeholder text as the only label and repair the form semantics."),
    ("Performance and bundle boundaries", "bundle, hydration, client boundary, dynamic import, image, cache", "What JavaScript reaches the browser?;Why keep client boundaries narrow?;When should we lazy-load?;How do images and fonts affect performance?", "const Chart = dynamic(() => import('@/components/Chart'), { ssr: false });", "The heavy interactive chart loads only when needed.\n", "Mark the entire page as client and compare the boundary cost."),
    ("Deployment and environment configuration", "build, start, environment variable, secret, runtime, CI", "What is the production build?;Which variables are public?;Where do secrets live?;What should CI prove before deployment?", "npm run build\n# production only\nnpm run start", "The app is built before it is started in production.\n", "Commit a secret in a local env file and repair the ignore and rotation plan."),
    ("Migration from Pages Router and old React", "Pages Router, App Router, getServerSideProps, getStaticProps, lifecycle, migration", "What is legacy?;How do Pages Router data functions map to App Router?;How do class lifecycles map to Hooks?;How do we migrate incrementally?", "pages/index.tsx -> app/page.tsx\ngetServerSideProps -> async Server Component data access", "The migration maps responsibilities, not names only.\n", "Copy getServerSideProps into app/page.tsx and explain why the model changed."),
    ("Capstone architecture and review", "architecture, feature boundary, threat model, test plan, observability, trade-off", "How do we design a real app?;Where do routes, components, data, and policies live?;How do we document trade-offs?;What evidence proves readiness?", "src/app/(dashboard)/cases/page.tsx\nsrc/components/cases/CaseTable.tsx\nsrc/lib/cases.ts", "The architecture makes boundaries reviewable.\n", "Add features without naming a boundary; repair by writing a one-page architecture decision."),
    ("Final demonstration and portfolio review", "demonstration, portfolio, README, architecture decision, evidence, residual risk", "What makes a project demonstrable?;How do we explain the architecture to another person?;What evidence belongs in a portfolio?;How do we state residual risk honestly?", "const evidence = { build: 'pass', tests: 'pass', accessibility: 'reviewed' };\nconsole.log(evidence);", "The review records evidence and remaining uncertainty.\n", "Claim that passing tests prove production readiness and repair the claim with explicit limits."),
    ("Getters, setters, and state boundaries", "getter, setter, accessor, property, encapsulation, React state setter", "What is a getter?;What is a setter?;How are property accessors different from useState setters?;When should a UI model expose an accessor?", "const account = {\n  _name: 'Ada',\n  get name() { return this._name; },\n  set name(value) { this._name = value.trim(); },\n};\naccount.name = ' Grace ';\nconsole.log(account.name);", "Grace\n", "Use a setter to hide invalid data instead of validating at the boundary, then repair the model and explain why React state still needs an explicit setter call."),
]


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def keywords_table(raw: str) -> str:
    terms = [item.strip() for item in raw.split(",")]
    rows = ["| Keyword or term | Plain-English meaning |", "| --- | --- |"]
    for term in terms:
        rows.append(f"| `{term}` | A term you will use in this lesson; test it in the examples before memorizing it. |")
    return "\n".join(rows)


def topic_sections(raw: str, title: str) -> tuple[str, str]:
    topics = [item.strip() for item in raw.split(";")]
    toc = []
    body = []
    for index, topic in enumerate(topics, 1):
        heading = f"### {topic}"
        anchor = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
        toc.append(f"  - [{topic}](#{anchor})")
        body.append(
            f"{heading}\n\n"
            f"Start with the ordinary-language question: **{topic}**. In **{title}**, this topic is not a slogan. It is a decision you can observe in a small program. Read the next example slowly, name the input, the operation, the output, and the boundary that prevents the code from doing more than intended. Then change one value and explain which line noticed the change.\n\n"
            f"A beginner mistake is to copy the spelling without understanding the runtime. Instead, say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair."
        )
    return "\n".join(toc), "\n\n".join(body)


def lesson(day: int, title: str, keywords: str, raw_topics: str, code: str, output: str, repair: str) -> str:
    topic_toc, topics = topic_sections(raw_topics, title)
    heading = f"Day {day:03d}: {title}"
    return f"""# {heading}

[← Previous lesson](../DAY_INDEX.md) · [Day index](../DAY_INDEX.md)

## Table of contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
{topic_toc}
- [Worked example](#worked-example)
- [Execution trace](#execution-trace)
- [Prediction experiment](#prediction-experiment)
- [Broken example and repair](#broken-example-and-repair)
- [Guided practice before independent work](#guided-practice-before-independent-work)
- [Project application](#project-application)
- [Independent exercises](#independent-exercises)
- [Finish line](#finish-line)
- [References](#references)

## Why this lesson exists

A learner can read a framework tutorial and still feel lost because the tutorial shows a finished file without explaining the decisions that produced it. This lesson teaches **{title}** as a sequence of small, testable ideas. The goal is not to memorize a recipe. The goal is to predict what the runtime will do, explain why it did it, and make a safe change without breaking the mental model.

## Prerequisites

Complete the previous lesson and make sure the repository setup works. If a command fails, stop and read the error instead of copying a random fix. You may use JavaScript, TypeScript, React, or Next.js examples depending on the phase, but every new framework word is explained before the lesson depends on it.

## Outcomes

By the end, you should be able to explain the topics in your own words, run the worked example, trace it line by line, predict one normal and one boundary result, repair the broken version, and apply the idea to a small local project. You should also be able to state one limitation: what this lesson does **not** prove about production readiness, security, performance, or correctness.

## Keywords and terms

{keywords_table(keywords)}

## Topics

{topics}

## Worked example

Copy this complete example into the appropriate starter file. Do not modify it before the first run.

```tsx
{code}
```

**Expected result or visible behavior:**

```text
{output}```

Read the code from top to bottom. Identify the input, the named values, the operation, the output, and the line that owns the decision. If the example is JSX, distinguish JavaScript expressions inside braces from markup. If it is a Server Component or Client Component example, identify which side of the boundary each line belongs to.

## Execution trace

1. The runtime reads the declarations and creates the names used by the example.
2. The component or function receives its input and evaluates its body from top to bottom.
3. React or Next.js records the result, schedules any state update or asynchronous work, and decides what can be rendered in the current environment.
4. The visible result is evidence about this fixture. It is not proof that an untested production application is secure, accessible, or correct.

Write the trace in your own notebook. After each line, record what value exists and which component or environment owns it.

## Prediction experiment

Before running the experiment, write your prediction. Change exactly one input from the worked example: use an empty value, a boundary value, a delayed promise, a missing route parameter, or a rejected action appropriate to this lesson. Predict the output, fallback, compiler error, or thrown error. Run it, record what happened, and explain the difference. Then run the original case again to prove that the repair did not remove the normal behavior.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** {repair}

Run the broken version in a local copy. Capture the error or incorrect UI. Name the violated assumption in one sentence. **Repair:** change the smallest possible line or boundary, rerun the normal case, rerun the boundary case, and explain what remains untested. Do not hide the failure with a broad catch, disable a type check, or claim that a passing render proves a secure application.

## Guided practice before independent work

First, reproduce the worked example with one different value. Second, change one rule while keeping the input fixed and predict the result. Third, start a blank file and recreate the smallest version from memory. Ask yourself: what is the component boundary, what data crosses it, where does state live, and what should happen when work is loading or fails? Only after these three checkpoints should you attempt the independent exercises.

## Project application

Use a local, synthetic project fixture. Name the user-visible goal, the component or route boundary, the data shape, the loading state, the failure state, the accessibility requirement, and the test evidence. If the topic is Next.js, state whether the file is a Server Component or Client Component and why. If it uses a secret, database, cookie, or authorization decision, keep that logic server-side and test an unauthorized fixture. If the topic is React-only, use invented data and do not send it to a public service.

## Independent exercises

1. Recreate the worked example using different data.
2. Explain each keyword in the Keywords and terms table without reading the lesson.
3. Change one line and predict the new output before running it.
4. Add a normal case and a boundary case.
5. Break the example in the way described above and record the error.
6. Repair it with the smallest change.
7. Add one accessible label, keyboard behavior, or meaningful loading message.
8. Add a test or assertion for the most important behavior.
9. Explain which value is owned by which component, function, or server boundary.
10. Write one limitation that the example does not prove.
11. Apply the lesson to the current project fixture using only local or synthetic data.
12. Write a short review explaining what a teammate should inspect before merging your change.

## Finish line

You are finished when you can teach the main idea to another beginner, show the normal and broken runs, explain the repair, and point to the exact boundary where data, state, effects, or server authority changes. Do not move on because the code merely compiles.

## References

- [React Learn](https://react.dev/learn)
- [React Reference](https://react.dev/reference/react)
- [Next.js Documentation](https://nextjs.org/docs)
- [Next.js Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
- [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
"""


def main() -> None:
    for path in ROOT.glob("day_*"):
        if path.is_dir():
            import shutil
            shutil.rmtree(path)
    for day, (title, keywords, topics, code, output, repair) in enumerate(LESSONS, 1):
        folder = ROOT / f"day_{day:03d}_{slug(title)}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / f"day_{day:03d}_{slug(title)}.md").write_text(
            lesson(day, title, keywords, topics, code, output, repair), encoding="utf-8"
        )
        practice = folder / "practice"
        practice.mkdir()
        (practice / "exercises.md").write_text(
            f"# Day {day:03d} exercises\n\nUse the numbered questions in the lesson. Work without solutions first, then record your prediction, observed result, and explanation.\n",
            encoding="utf-8",
        )
        (practice / "hints.md").write_text(
            f"# Day {day:03d} hints\n\nStart with the worked example. Change one value at a time. If the failure is a boundary error, repair the input or the boundary policy rather than hiding the error.\n",
            encoding="utf-8",
        )
        (practice / "solutions.md").write_text(
            f"# Day {day:03d} solution guide\n\nA strong solution includes runnable code, expected behavior, a normal case, a boundary case, a repair, and a limitation. Compare your reasoning with the lesson rather than copying a final file.\n",
            encoding="utf-8",
        )
    print(f"Generated {len(LESSONS)} modern lessons.")


if __name__ == "__main__":
    main()
