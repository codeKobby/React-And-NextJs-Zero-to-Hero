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

EXTRA_LESSONS = [
    ("Tailwind CSS v4 setup in Next.js", "Tailwind CSS, utility class, PostCSS, global stylesheet, @import, responsive", "What problem does Tailwind CSS solve?;How does Tailwind CSS v4 enter a Next.js project?;What is a utility class?;How do we verify a styled component?", "export default function Card() {\n  return <article className=\"rounded-xl border p-6 shadow-sm\">A local card</article>;\n}", "A bordered card appears with spacing and a shadow.\n", "Install a v3-style configuration in a v4 project, then repair the PostCSS plugin and global CSS import."),
    ("Responsive layouts and design tokens with Tailwind", "responsive, breakpoint, theme variable, dark mode, token, contrast", "What is responsive design?;How do Tailwind breakpoints change a layout?;What is a design token?;How do dark mode and contrast affect accessibility?", "<main className=\"bg-background text-foreground p-4 md:p-8 dark:bg-slate-950\">\n  <h1 className=\"text-2xl md:text-4xl\">Case dashboard</h1>\n</main>", "The layout adapts at the medium breakpoint and remains readable in dark mode.\n", "Use arbitrary colors everywhere, create inconsistent contrast, and repair the design with named tokens and a contrast check."),
    ("shadcn/ui installation and component ownership", "shadcn/ui, components.json, CLI, alias, generated source, composition", "What is shadcn/ui?;Why does it copy component source into the project?;What does components.json configure?;How does the @ alias work with src/?", "import { Button } from \"@/components/ui/button\";\n\nexport function SaveButton() {\n  return <Button type=\"submit\">Save case</Button>;\n}", "The project owns and composes an accessible Button component.\n", "Install a component while the alias points at the wrong directory, then repair the src-aware paths configuration."),
    ("shadcn/ui composition, theming, and accessible patterns", "Button, Dialog, Sheet, Form, Label, data table, ARIA, composition", "Why compose primitives instead of copying a screenshot?;How does a Dialog manage focus?;How do labels and errors support forms?;When should a table become a data grid?", "<Dialog>\n  <DialogTrigger asChild><Button>Review case</Button></DialogTrigger>\n  <DialogContent><DialogTitle>Case details</DialogTitle></DialogContent>\n</Dialog>", "The trigger opens a titled dialog with an explicit focus and reading boundary.\n", "Build a click-only modal without a title or escape behavior, then repair the accessible dialog contract."),
    ("The dashboard shell and feature-based boundaries", "dashboard, navigation, route group, feature boundary, layout, sidebar", "What makes a dashboard shell?;How do route groups organize features?;Where should navigation state live?;How do feature folders reduce coupling?", "src/app/(dashboard)/layout.tsx\nsrc/app/(dashboard)/cases/page.tsx\nsrc/components/cases/CaseTable.tsx\nsrc/lib/cases/queries.ts", "The shell persists while the cases route changes inside it.\n", "Put database queries, navigation, and visual components in one file, then repair the feature boundaries."),
    ("Schema validation with Zod-style boundaries", "schema, parse, safeParse, validation, coercion, trusted data", "Why validate at a boundary?;What is the difference between parse and safeParse?;How do schemas describe form data?;What must happen after validation fails?", "const CaseSchema = z.object({ title: z.string().min(1).max(120) });\nconst result = CaseSchema.safeParse({ title: formData.get('title') });\nif (!result.success) return { error: 'Enter a case title.' };", "Invalid input becomes structured form state instead of reaching the mutation.\n", "Trust formData.get('title') as a string and repair the schema boundary before calling the database."),
    ("SQL and relational data modeling", "SQL, table, row, column, primary key, foreign key, relation", "What is a table?;Why do rows need stable identifiers?;What is a foreign key?;How do we model a case and its events?", "CREATE TABLE cases (\n  id TEXT PRIMARY KEY,\n  title TEXT NOT NULL,\n  created_at TEXT NOT NULL\n);", "The schema requires an ID, title, and creation timestamp for every case.\n", "Store a user name in every event row without a foreign key, then repair the model to preserve ownership and traceability."),
    ("Drizzle ORM, SQLite, migrations, and seed data", "Drizzle ORM, SQLite, migration, schema, seed, transaction", "What does an ORM do?;Why are migrations committed?;What is seed data?;When should a transaction group changes?", "export const cases = sqliteTable('cases', {\n  id: text('id').primaryKey(),\n  title: text('title').notNull(),\n});", "The typed schema maps application data to a local SQLite table.\n", "Change the TypeScript schema without generating a migration, then repair the workflow and test a fresh database."),
    ("Repositories and server-only data access", "repository, data-access layer, server-only, query, DTO, authorization", "Why isolate database calls?;What is a repository?;What data should cross into a Client Component?;Where should authorization occur?", "import 'server-only';\n\nexport async function listCasesForUser(userId: string) {\n  return db.select().from(cases).where(eq(cases.ownerId, userId));\n}", "The server-only repository returns only records belonging to the requested user.\n", "Import the repository into a Client Component and return database rows with secrets, then repair both boundaries."),
    ("Server Actions for validated mutations", "Server Action, use server, FormData, mutation, revalidation, redirect", "What is a Server Action?;Where should validation and authorization happen?;How do we return field errors?;When should a mutation revalidate or redirect?", "'use server';\n\nexport async function createCase(formData: FormData) {\n  const input = CaseSchema.safeParse({ title: formData.get('title') });\n  if (!input.success) return { error: 'Invalid title' };\n  await requirePermission('case:create');\n  revalidatePath('/cases');\n}", "The server validates, authorizes, mutates, and refreshes the relevant route.\n", "Revalidate before the mutation succeeds and trust a client-provided owner ID, then repair the sequence."),
    ("Route Handlers, API contracts, and typed errors", "Route Handler, HTTP, GET, POST, Request, Response, status, error contract", "When should an app expose an HTTP endpoint?;How do we shape a successful response?;Which status represents invalid input?;How should clients handle typed errors?", "export async function POST(request: Request) {\n  const body = await request.json();\n  if (!body.title) return Response.json({ code: 'INVALID_TITLE' }, { status: 400 });\n  return Response.json({ ok: true }, { status: 201 });\n}", "Invalid input returns a deliberate 400 contract and valid creation returns 201.\n", "Return 200 for malformed input and leak a stack trace, then repair the status and public error shape."),
    ("Authentication providers and identity boundaries", "authentication, provider, credential, identity, callback, trust boundary", "What is authentication?;What belongs to an authentication provider?;Why is identity different from permission?;How do we keep provider code replaceable?", "const identity = await authProvider.verify(credentials);\nif (!identity) return { error: 'Invalid credentials' };\nreturn { userId: identity.id };", "The provider proves identity while the application still owns authorization decisions.\n", "Treat an email field from the browser as an authenticated identity, then repair the provider boundary."),
    ("Secure sessions and cookie policy", "session, cookie, HttpOnly, Secure, SameSite, expiry, jose, secret", "What is session management?;Why must session code be server-only?;What cookie flags reduce risk?;How do stateless sessions expire?", "const session = await createSignedSession({ userId });\n(await cookies()).set('session', session, { httpOnly: true, secure: true, sameSite: 'lax', path: '/' });", "The session is signed and stored with browser access restricted from client JavaScript.\n", "Store a raw user ID in a readable cookie without expiry, then repair signing, flags, and rotation planning."),
    ("Next.js 16 Proxy and the middleware migration", "proxy.ts, middleware.ts, matcher, redirect, rewrite, request, optimistic check", "What changed from middleware.ts to proxy.ts?;What does Proxy run before?;How does a matcher limit scope?;Why is Proxy not final authorization?", "import { NextResponse } from 'next/server';\n\nexport function proxy(request: NextRequest) {\n  if (!request.cookies.has('session')) return NextResponse.redirect(new URL('/login', request.url));\n  return NextResponse.next();\n}\n\nexport const config = { matcher: ['/dashboard/:path*'] };", "Unauthenticated dashboard requests are redirected before rendering.\n", "Protect only with a client-side redirect and call Proxy authorization complete, then repair the server data check."),
    ("Authorization, roles, ownership, and multi-tenant data", "authorization, role, permission, ownership, tenant, least privilege", "What is authorization?;How do roles differ from permissions?;Why must ownership filter the query?;What changes in a multi-tenant app?", "const actor = await requireSession();\nconst record = await getCase(caseId);\nif (record.tenantId !== actor.tenantId || !actor.permissions.includes('case:read')) notFound();", "The data access decision checks both tenant ownership and permission.\n", "Check only whether a user is logged in and return another tenant's case, then repair the query and policy."),
    ("File uploads, metadata, and storage boundaries", "upload, multipart, MIME type, size limit, object storage, metadata, download", "What is an upload boundary?;Why validate size and type on the server?;Where should file bytes live?;How should downloads be authorized?", "const MAX_BYTES = 2_000_000;\nif (file.size > MAX_BYTES || !ALLOWED_TYPES.has(file.type)) {\n  return { error: 'Unsupported file' };\n}", "Oversized or unsupported synthetic files are rejected before storage.\n", "Trust the filename extension, accept unlimited bytes, and serve a file without checking ownership, then repair all three boundaries."),
    ("Error taxonomy, logging, and instrumentation", "expected error, unexpected error, structured log, request ID, instrumentation, observability", "What is the difference between an expected and unexpected error?;What should a structured log contain?;Why use a request ID?;Where does instrumentation belong?", "logger.info({ requestId, route: '/cases', event: 'case.created', caseId });\nreturn { ok: true };", "The event can be correlated without logging a secret or raw credential.\n", "Log an entire request body and expose a stack trace to the user, then repair the event fields and public error."),
    ("Full-stack testing with Playwright and synthetic fixtures", "unit test, integration test, E2E, Playwright, fixture, accessibility, regression", "What should each test level prove?;How do we test a protected route?;What is a safe fixture?;Why test a browser journey?", "test('a learner can create a case', async ({ page }) => {\n  await page.goto('/cases');\n  await page.getByRole('button', { name: 'New case' }).click();\n  await page.getByLabel('Title').fill('Synthetic case');\n});", "The test follows a user-visible journey using invented data.\n", "Assert only that a private component function was called and skip the browser contract, then repair the test around user behavior."),
    ("Production configuration, CI, and deployment evidence", "environment variable, secret, CI, build, migration, deployment, rollback", "What belongs in an environment variable?;What should CI prove?;How do migrations run safely?;What is a rollback plan?", "pnpm lint\npnpm typecheck\npnpm test\npnpm build\npnpm db:migrate", "The delivery pipeline checks code, types, tests, build output, and schema state.\n", "Commit a secret in an env file and deploy without a migration or rollback plan, then repair the delivery checklist."),
    ("Capstone architecture, threat model, and delivery plan", "capstone, architecture decision, threat model, data model, route map, acceptance criteria", "How do we plan a full app?;What is a threat model?;How do UI, data, and policy boundaries fit together?;What evidence defines done?", "src/app/(dashboard)/cases/page.tsx\nsrc/components/ui/button.tsx\nsrc/lib/db/schema.ts\nsrc/lib/auth/require-permission.ts\nproxy.ts", "The planned structure makes UI, data, and security boundaries reviewable.\n", "Start coding without identifying actors, assets, routes, and trust boundaries, then repair the plan before implementation."),
    ("Capstone build I: design system, shell, and database-backed reads", "capstone, Tailwind, shadcn/ui, layout, loading, error, database query, DTO", "How do we turn the plan into a vertical slice?;Which UI primitives should be shared?;How do Server Components read data?;How do loading and error states complete the feature?", "export default async function CasesPage() {\n  const cases = await listCasesForUser('synthetic-user');\n  return <CaseTable rows={cases} />;\n}", "The dashboard renders a typed, user-scoped synthetic case list with explicit loading and failure boundaries.\n", "Build the entire dashboard as one client component and pass raw database objects through it, then repair the vertical slice."),
    ("Capstone build II: auth, proxy, mutations, tests, and portfolio proof", "capstone, authentication, proxy, authorization, Server Action, Playwright, evidence, residual risk", "How do we connect identity to protected mutations?;Where does Proxy help and where does it stop?;What tests prove the main journey?;How do we demonstrate residual risk honestly?", "await requirePermission('case:create');\nawait createCase(input);\nrevalidatePath('/cases');", "The protected mutation validates input, checks permission, updates data, and refreshes the visible list.\n", "Declare the capstone complete because the happy path works, then repair the demonstration with failure tests, security evidence, and explicit residual risk."),
]

LESSONS.extend(EXTRA_LESSONS)


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


TERM_MEANINGS = {
    "action": "A named unit of work that can have pending, success, error, or optimistic behavior.",
    "app router": "Next.js routing model where folders and special files define route segments and rendering boundaries.",
    "browser": "The program that loads a page, provides the DOM, and runs client-side JavaScript.",
    "client component": "A component whose module begins with `use client` and may use browser-only interaction APIs.",
    "component": "A reusable unit of UI that receives inputs and returns a description of what should appear.",
    "context": "A React mechanism for making a value available to a subtree without passing it through every prop.",
    "effect": "A synchronization step that connects rendering to something outside React, such as a subscription or document title.",
    "export": "A declaration that makes a value available to another module.",
    "getter": "A JavaScript property accessor that runs when code reads a property.",
    "hook": "A React function with a call-site rule that lets a function component use React features.",
    "import": "A declaration that reads a value exported by another module.",
    "jsx": "JavaScript syntax that describes UI elements using markup-like notation.",
    "layout": "A Next.js file that wraps a route segment and can preserve shared UI while child pages change.",
    "module": "A file with its own scope that can explicitly export and import values.",
    "next.js": "A React framework that adds routing, server rendering, data boundaries, and production conventions.",
    "node.js": "A JavaScript runtime that runs outside the browser and can access server-side APIs.",
    "props": "Read-only inputs passed from a parent component to a child component.",
    "react": "A library for describing interactive user interfaces as a tree of components.",
    "ref": "A stable container or DOM reference that does not itself trigger a re-render when it changes.",
    "reducer": "A pure function that calculates the next state from the current state and a named action.",
    "route handler": "A Next.js server file that handles an HTTP method such as GET or POST.",
    "server component": "A component rendered on the server by default in the App Router and not sent as interactive client JavaScript.",
    "server action": "A server-side function that a form or client interaction can invoke through a controlled framework boundary.",
    "setter": "A function that requests a new state value; it is not the same thing as a JavaScript property setter.",
    "src": "A conventional directory used to keep application source code separate from root configuration files.",
    "state": "Data owned by a component that React remembers between renders and can use to produce new UI.",
    "typescript": "A static type checker that catches many mismatches before JavaScript runs.",
    "useeffect": "The React Hook used to synchronize with an external system after rendering.",
    "usestate": "The React Hook that returns a state snapshot and a setter for requesting the next state.",
    "validation": "A check that an input has the shape and values a boundary is prepared to handle.",
}


def term_meaning(term: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "", term.lower())
    for key, meaning in TERM_MEANINGS.items():
        if re.sub(r"[^a-z0-9]+", "", key) == normalized:
            return meaning
    if normalized.endswith("s"):
        singular = normalized[:-1]
        for key, meaning in TERM_MEANINGS.items():
            if re.sub(r"[^a-z0-9]+", "", key) == singular:
                return meaning
    return "A named idea in this lesson. Use the worked example to observe its input, behavior, output, and boundary before trying to define it in your own words."


def keywords_table(raw: str) -> str:
    terms = [item.strip() for item in raw.split(",")]
    rows = ["| Keyword or term | Plain-English meaning |", "| --- | --- |"]
    for term in terms:
        rows.append(f"| `{term}` | {term_meaning(term)} |")
    return "\n".join(rows)


def topic_explanation(topic: str, title: str) -> str:
    question = topic.rstrip("?")
    lower = question.lower()
    if lower.startswith("what is"):
        core = question[8:].strip()
        return f"**{core}** is the idea you must be able to point to in code. Begin with the smallest example: identify the value or boundary involved, observe what changes, and name the rule that connects the input to the result. In this lesson, the worked example gives you a controlled fixture; do not add framework complexity until you can explain the plain JavaScript or browser behavior first."
    if lower.startswith("why"):
        return f"The useful answer to **{question}** is a trade-off, not a memorized slogan. Compare the simple case with the failure case, then ask what responsibility is being protected: ownership, identity, accessibility, performance, or server authority. Record the evidence from the example before choosing a pattern."
    if lower.startswith("how"):
        return f"To answer **{question}**, follow a repeatable procedure. First identify the input and the owner; next make the smallest change; then predict the output, run it, and inspect the boundary behavior. If the code crosses from JavaScript into React or from a Server Component into the browser, write that boundary down explicitly."
    if lower.startswith("when"):
        return f"Treat **{question}** as a decision rule. List the normal case, one boundary case, and the cost of choosing the wrong option. Then use the worked example to decide which component, module, route, or server boundary should own the behavior."
    return f"Study **{question}** by naming its input, operation, output, and owner. Change one thing at a time and keep both your prediction and the observed result so that a mismatch becomes a repairable learning signal."


def topic_sections(raw: str, title: str) -> tuple[str, str]:
    topics = [item.strip() for item in raw.split(";")]
    toc = []
    body = []
    for index, topic in enumerate(topics, 1):
        heading = f"### {topic}"
        anchor = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
        toc.append(f"  - [{topic}](#{anchor})")
        body.append(f"{heading}\n\n{topic_explanation(topic, title)}\n\nA beginner mistake is to copy the spelling without understanding the runtime. Say the rule aloud, write a prediction, run the example, and compare the result. Keep the prediction even when it is wrong; the mismatch tells you which assumption needs repair.")
    return "\n".join(toc), "\n\n".join(body)


def line_by_line(code: str) -> str:
    rows = ["| Line | What this line does |", "| ---: | --- |"]
    for number, raw_line in enumerate(code.splitlines(), 1):
        line = raw_line.strip()
        if not line:
            rows.append(f"| {number} | Blank line: it separates ideas and has no runtime operation. |")
            continue
        if line.startswith("import "):
            explanation = "Imports a binding from another module before this file uses it."
        elif line.startswith("export "):
            explanation = "Creates a module binding and makes it available to another file."
        elif "useState" in line:
            explanation = "Connects the component to React state and receives a snapshot plus a setter."
        elif "useEffect" in line:
            explanation = "Declares synchronization work that React will run after the component renders."
        elif line.startswith("return ") or line == "return":
            explanation = "Returns the value or UI description that the surrounding function owns."
        elif line.startswith("console."):
            explanation = "Writes an observation to the console so the learner can compare it with the prediction."
        elif "=>" in line or line.startswith("function ") or line.startswith("class "):
            explanation = "Declares behavior; the body runs when this function or component is called or rendered."
        elif line.startswith("<") or line.startswith("</") or line.startswith("//"):
            explanation = "Describes structure or records an intentional comment; JSX becomes part of the rendered result."
        elif "set" in line.lower() and "(" in line:
            explanation = "Requests a new value through a setter or update function rather than mutating the old value."
        elif "=" in line:
            explanation = "Creates or updates a named value; read the right-hand side to find the input and operation."
        else:
            explanation = "Runs as part of the surrounding expression or block; identify its input and observed effect."
        rows.append(f"| {number} | `{line.replace('|', '\\|')}` — {explanation} |")
    return "\n".join(rows)


def lesson(
    day: int,
    title: str,
    keywords: str,
    raw_topics: str,
    code: str,
    output: str,
    repair: str,
    navigation: str,
) -> str:
    topic_toc, topics = topic_sections(raw_topics, title)
    heading = f"Day {day:03d}: {title}"
    return f"""# {heading}

{navigation}

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
{topic_toc}
- [Worked example](#worked-example)
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

This lesson belongs to the complete course, not to a disconnected collection of notes. Before coding, open the [course README](../README.md) for the learning contract, read the [setup guide](../SETUP.md) if your tools are not ready, and use the [day index](../DAY_INDEX.md) to see where this lesson fits. If you need a runnable project, open the [examples guide](../examples/README.md), choose the React playground or Next.js starter that matches this day, and work locally with synthetic data only.

The intended loop is simple: read the lesson, run the worked example unchanged, make a prediction, repair the broken version, complete the guided practice, then use the linked [practice worksheet](practice/exercises.md), [hints](practice/hints.md), and [solution guide](practice/solutions.md) only after attempting the work.

## Why this lesson exists

A learner can read a framework tutorial and still feel lost because the tutorial shows a finished file without explaining the decisions that produced it. This lesson teaches **{title}** as a sequence of small, testable ideas. The goal is not to memorize a recipe. The goal is to predict what the runtime will do, explain why it did it, and make a safe change without breaking the mental model.

## Prerequisites

Complete the previous lesson, confirm the [setup guide](../SETUP.md), and make sure the repository setup works. If a command fails, stop and read the first error instead of copying a random fix. Use the [course README](../README.md) to understand the learning loop and the [examples guide](../examples/README.md) to choose the correct local starter. You may use JavaScript, TypeScript, React, or Next.js examples depending on the phase, but every new framework word is explained before the lesson depends on it.

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

## Line-by-line explanation

{line_by_line(code)}

Use the table as a starting point, not as a substitute for running the code. Add a note beside any line whose behavior differs between a browser, React, and Next.js server environment.

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

Use a local, synthetic project fixture from the [examples guide](../examples/README.md). Name the user-visible goal, the component or route boundary, the data shape, the loading state, the failure state, the accessibility requirement, and the test evidence. If the topic is Next.js, state whether the file is a Server Component or Client Component and why. If it uses a secret, database, cookie, or authorization decision, keep that logic server-side and test an unauthorized fixture. If the topic is React-only, use invented data and do not send it to a public service.

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
- [Next.js Authentication](https://nextjs.org/docs/app/guides/authentication)
- [Next.js Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
- [Tailwind CSS with Next.js](https://tailwindcss.com/docs/installation/framework-guides/nextjs)
- [shadcn/ui with Next.js](https://ui.shadcn.com/docs/installation/next)
"""


def practice_materials(day: int, title: str, raw_topics: str, repair: str) -> tuple[str, str, str]:
    topics = [item.strip() for item in raw_topics.split(";")]
    first, second, third, fourth = topics[:4]
    lesson_slug = f"day_{day:03d}_{slug(title)}"
    exercises = f"""# Day {day:03d} practice: {title}

Use this worksheet after reading [the lesson](../{lesson_slug}.md). Before you start, read the [course README](../../README.md), confirm your tools with the [setup guide](../../SETUP.md), and choose the appropriate local starter from the [examples guide](../../examples/README.md). Work only with local, synthetic data.

## How to submit your own evidence

For every exercise, save the smallest runnable code or written artifact, record your prediction before running it, copy the observed result, and explain the difference in your own words. Do not open the solution guide until you have attempted the task.

## Exercises

1. Define **{first}** in two sentences for a beginner, then point to the exact line in the lesson where the idea first appears.
2. Copy the worked example unchanged into the correct starter project, run it, and record the command, expected result, and observed result.
3. Write a line-by-line execution trace for the worked example. Name the input, operation, output, and owner of each important value.
4. Replace one input with a normal alternative that still demonstrates **{second}**. Predict the result before running it.
5. Create a boundary case involving **{third}**. Decide whether the correct behavior is a value, an empty state, a compiler error, a loading state, or a failure message, and justify that choice.
6. Reproduce this deliberate failure: **{repair}**. Capture the error or incorrect behavior, name the violated assumption, and repair the smallest possible change.
7. Compare **{first}** and **{second}** in a short table. Include ownership, data flow, and one situation where confusing them causes a bug.
8. Add one quality requirement to the fixture: a meaningful accessible name, a type guard, a loading state, an error state, or a server/client boundary declaration. Explain why it belongs there.
9. Add a focused test or assertion for the most important behavior. The test must fail when that behavior is removed and pass after the repair.
10. Apply the lesson to a small local feature using invented data. Write the component, route, or function boundary before writing the implementation.
11. Write a limitation statement: explain what your successful run does **not** prove about production correctness, security, performance, or accessibility.
12. Prepare a review note for a teammate. Include the changed files, evidence you collected, one remaining risk, and the next lesson you are ready to study.
"""
    hints = f"""# Day {day:03d} hints: {title}

These hints are deliberately specific enough to unblock you but not to replace the attempt. Use the [lesson](../{lesson_slug}.md) and [setup guide](../../SETUP.md) first.

## Hints

1. Use the word **{first}** in your definition, then connect it to an observable input and output rather than a dictionary slogan.
2. Do not change the example before the first run. If it fails, verify the current directory and the starter's package scripts.
3. Make one trace row per meaningful line. Include the value before and after a setter, render, request, or boundary decision.
4. Change exactly one input. If you change the code and the input together, you will not know what caused the result.
5. Boundary behavior is part of the feature. Decide who owns the empty, invalid, pending, or unauthorized case before coding it.
6. Start from the smallest broken line. Do not disable TypeScript, remove a dependency array, or hide an error with a broad catch.
7. **{first}** and **{second}** may be related without being interchangeable. Compare who creates the value and who is allowed to change it.
8. Prefer a small explicit boundary over a global workaround. For Next.js, state whether the code runs on the server or in the browser.
9. Assert user-visible behavior or a clear contract. A test that only checks a private implementation detail will not protect the lesson's idea.
10. Use the same local fixture throughout. Keep the feature small enough that you can explain every file in the review.
11. A build proves only that the checked build completed. It does not prove that every user path, device, permission, or failure mode works.
12. A good review note is reproducible: another learner should know what to run, what should happen, and what remains uncertain.
"""
    solutions = f"""# Day {day:03d} solution guide: {title}

Use this guide after attempting [the exercises](exercises.md). A solution is evidence and reasoning, not a copied file. Compare your work with the [lesson](../{lesson_slug}.md), then improve the explanation if your code works for the wrong reason.

## Review checkpoints

1. The definition of **{first}** names an observable rule and points to a concrete lesson example.
2. The unchanged worked example runs in the correct local starter and its output matches the lesson's expected result.
3. The trace identifies the order of evaluation and the owner of each important value.
4. The normal alternative changes one input and preserves the rule for **{second}**.
5. The boundary case has deliberate behavior rather than an accidental blank screen, stray value, or unhandled rejection.
6. The broken example reproduces the stated failure, and the repair is the smallest change that restores the normal case without weakening the check.
7. The comparison table distinguishes **{first}** from **{second}** by responsibility, lifetime, and direction of data flow.
8. The added quality requirement is visible in the code or project structure and is explained in plain language.
9. The test or assertion fails when the important behavior is removed, then passes after the repair.
10. The local feature has a named boundary, synthetic fixture data, a normal path, and a failure or empty path appropriate to the topic.
11. The limitation statement avoids claiming that a passing build or test proves production readiness.
12. The review note names files, commands, observed evidence, one remaining risk, and the next learning step.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
"""
    return exercises, hints, solutions


def main() -> None:
    for path in ROOT.glob("day_*"):
        if path.is_dir():
            import shutil
            shutil.rmtree(path)
    lesson_paths = [ROOT / f"day_{day:03d}_{slug(item[0])}" for day, item in enumerate(LESSONS, 1)]
    for day, (title, keywords, topics, code, output, repair) in enumerate(LESSONS, 1):
        folder = lesson_paths[day - 1]
        folder.mkdir(parents=True, exist_ok=True)
        previous = "../DAY_INDEX.md" if day == 1 else f"../{lesson_paths[day - 2].name}/{lesson_paths[day - 2].name}.md"
        next_link = "../DAY_INDEX.md" if day == len(LESSONS) else f"../{lesson_paths[day].name}/{lesson_paths[day].name}.md"
        previous_label = "← Course overview" if day == 1 else "← Previous lesson"
        next_label = "Course index →" if day == len(LESSONS) else "Next lesson →"
        navigation = f"[{previous_label}]({previous}) · [Start here](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [{next_label}]({next_link})"
        (folder / f"{folder.name}.md").write_text(
            lesson(day, title, keywords, topics, code, output, repair, navigation), encoding="utf-8"
        )
        practice = folder / "practice"
        practice.mkdir()
        exercises, hints, solutions = practice_materials(day, title, topics, repair)
        (practice / "exercises.md").write_text(exercises, encoding="utf-8")
        (practice / "hints.md").write_text(hints, encoding="utf-8")
        (practice / "solutions.md").write_text(solutions, encoding="utf-8")
    print(f"Generated {len(LESSONS)} modern lessons with learner-specific practice materials.")


if __name__ == "__main__":
    main()
