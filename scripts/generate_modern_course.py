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

AUTHORED_LESSONS = {
    2: ROOT / "authored_lessons/day_002_html_css_accessibility_and_the_dom.md",
    6: ROOT / "authored_lessons/day_006_what_is_a_component.md",
    7: ROOT / "authored_lessons/day_007_jsx_and_the_rules_of_markup.md",
    8: ROOT / "authored_lessons/day_008_props_and_one_way_data_flow.md",
    9: ROOT / "authored_lessons/day_009_rendering_lists_and_choosing_keys.md",
    10: ROOT / "authored_lessons/day_010_conditional_rendering_and_empty_states.md",
    11: ROOT / "authored_lessons/day_011_events_and_event_handlers.md",
    12: ROOT / "authored_lessons/day_012_what_is_state.md",
    13: ROOT / "authored_lessons/day_013_usestate_and_setters.md",
    16: ROOT / "authored_lessons/day_016_controlled_forms.md",
    21: ROOT / "authored_lessons/day_021_what_is_useeffect.md",
    27: ROOT / "authored_lessons/day_027_function_components_versus_class_components.md",
    40: ROOT / "authored_lessons/day_040_root_app_versus_src_app.md",
    46: ROOT / "authored_lessons/day_054_server_and_client_components.md",
    51: ROOT / "authored_lessons/day_059_forms_and_server_actions.md",
    61: ROOT / "authored_lessons/day_061_getters_setters_and_state_boundaries.md",
    75: ROOT / "authored_lessons/day_075_next_js_16_proxy_and_the_middleware_migration.md",
    83: ROOT / "authored_lessons/day_083_capstone_build_ii_auth_proxy_mutations_tests_and_portfolio_proof.md",
}

AUTHORED_PRACTICE = {
    2: ROOT / "authored_lessons/day_002_html_css_accessibility_and_the_dom/practice",
    6: ROOT / "authored_lessons/day_006_what_is_a_component/practice",
    12: ROOT / "authored_lessons/day_012_what_is_state/practice",
    13: ROOT / "authored_lessons/day_013_usestate_and_setters/practice",
}


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
    "accessibility": "Designing and testing an interface so people with different abilities and input methods can use it.",
    "api": "A documented boundary through which one program requests data or behavior from another.",
    "authentication": "Establishing who an actor is, usually through a provider or session.",
    "authorization": "Deciding whether an identified actor may perform a requested action or access a record.",
    "build": "The process that checks, bundles, and prepares an application for a target environment.",
    "cache": "Stored work or data reused under a freshness policy instead of being recomputed every time.",
    "ci": "Continuous integration: an automated process that checks changes before they are merged or deployed.",
    "class component": "A React component implemented as a class that extends React.Component.",
    "composition": "Building a larger UI by placing smaller components together rather than inheriting from them.",
    "database": "A system that stores structured records and provides controlled ways to query or change them.",
    "derived value": "A value calculated from existing props or state rather than stored as a second source of truth.",
    "error": "A condition in which the intended operation could not complete or the program violated an assumption.",
    "error boundary": "A React boundary that replaces a failed subtree with fallback UI and recovery options.",
    "form": "A group of controls that collects named user input for a submit action.",
    "integration test": "A test that checks a contract across more than one real application boundary.",
    "keyboard": "Input through keys and focus movement, including paths that do not require a mouse.",
    "layout": "Shared route UI that wraps child pages and can remain mounted while the child route changes.",
    "loading": "A state in which work has started but its final result is not available yet.",
    "metadata": "Information about a page, such as its title, description, or social preview fields.",
    "migration": "A controlled change that moves an existing codebase, schema, or API to a new structure.",
    "mock": "A test replacement that stands in for a dependency with deliberately controlled behavior.",
    "mutation": "An operation that creates, changes, or deletes data.",
    "observability": "The ability to understand system behavior through useful logs, measurements, traces, and events.",
    "pending": "A period in which an operation has been requested but has not settled yet.",
    "promise": "A JavaScript object representing a value that may become available or fail later.",
    "provider": "A component or service that makes a value or capability available to a defined consumer boundary.",
    "query": "A request for records or information from a data source.",
    "regression": "A previously working behavior that breaks after a change.",
    "render": "React evaluating a component and using its returned tree to describe the current UI.",
    "reset": "An intentional return to a documented initial value or state.",
    "responsive": "A layout or behavior that adapts to viewport size, input method, or device conditions.",
    "role": "A named grouping of permissions that describes a class of actor responsibilities.",
    "rollback": "A planned way to return a deployment, migration, or change to a known working state.",
    "route group": "A parenthesized App Router folder used for organization or layout without adding a URL segment.",
    "schema": "A documented shape and set of constraints for data.",
    "secret": "Sensitive configuration or credential material that must not be exposed in client code or source control.",
    "segment": "One folder-level part of a Next.js route tree.",
    "server-only": "A guard or convention that prevents a module containing server authority from entering a client graph.",
    "session": "Server-managed information that connects later requests to an authenticated actor.",
    "shadcn/ui": "A source-owned collection of accessible UI component patterns that a project can inspect and customize.",
    "streaming": "Sending parts of a rendered response as they become ready instead of waiting for the entire tree.",
    "test": "A repeatable check of a behavior or contract under controlled inputs.",
    "threat model": "A description of actors, assets, trust boundaries, threats, and mitigations for a system.",
    "transition": "A React update marked as non-urgent so more urgent interaction can remain responsive.",
    "trust boundary": "A point where data, identity, or authority crosses from one level of trust into another.",
    "unit test": "A focused test of one small function or component contract in isolation.",
    "alias": "A shorter import name that maps to a longer filesystem or module path.",
    "architecture decision": "A recorded choice about structure, trade-offs, and consequences in a system.",
    "boundary": "A point where responsibility, data, rendering, or authority changes hands.",
    "bundle": "The client or server output assembled from modules for a target runtime.",
    "callback": "A function passed to another function or system so it can be called later.",
    "capstone": "A final integrated project that demonstrates several learned boundaries together.",
    "cleanup": "Work that removes or cancels an earlier subscription, timer, request, or resource.",
    "cookie": "A browser-stored value sent with matching requests; its presence is not proof of permission.",
    "environment variable": "Configuration supplied outside source code, often used for deployment-specific values or secrets.",
    "escaping": "Rendering untrusted text safely so it is not interpreted as executable markup.",
    "expression": "JavaScript syntax that evaluates to a value and can often appear inside JSX braces.",
    "fallback": "UI shown while the intended content is unavailable, loading, or failed.",
    "feature boundary": "A code boundary that groups the UI, data, and policy for one user-facing capability.",
    "fixture": "Controlled local data or setup used to make an example or test reproducible.",
    "focus": "The current keyboard or assistive-technology interaction target in the document.",
    "immutability": "Updating by creating a new value instead of changing the existing value in place.",
    "least privilege": "Giving an actor or module only the authority required for its task.",
    "memoization": "Reusing a previous calculation or rendered result when its relevant inputs have not changed.",
    "semantic html": "HTML elements chosen for their meaning and built-in browser and accessibility behavior.",
    "status": "A named condition such as idle, loading, success, empty, or error that guides visible behavior.",
    "role": "A named grouping of permissions that describes a class of actor responsibilities.",
}

TERM_MEANINGS.update({
    "aria": "Accessible Rich Internet Applications attributes that communicate roles, states, and relationships when native HTML is not enough.",
    "aria-label": "An accessible name supplied directly to an element when a visible label is not available.",
    "alt text": "Text that communicates the purpose or content of an image when it cannot be perceived.",
    "assertion": "A check that a value or behavior matches an expectation and should fail when the contract breaks.",
    "async": "JavaScript syntax for a function that returns a promise and can await asynchronous work.",
    "callback": "A function handed to another system so it can invoke the behavior later.",
    "client boundary": "The module edge where browser-capable React code begins and props must cross safely.",
    "client-only": "A restriction indicating that a module requires browser APIs or client execution.",
    "component name": "The identifier React uses to describe a component function or class in diagnostics and composition.",
    "custom Hook": "A function that packages reusable Hook logic while following the Rules of Hooks.",
    "DOM": "The browser's object representation of the document and its elements.",
    "DOM node": "One object in the browser document tree, such as an element, text node, or comment.",
    "event": "A browser report that an input or environmental occurrence happened.",
    "FormData": "A browser object that collects named form controls and their submitted values.",
    "fragment": "A React grouping that returns multiple children without adding an extra DOM element.",
    "hydration": "Attaching client React behavior to HTML that was already rendered so it can become interactive.",
    "hook rules": "The rules that Hooks are called at the top level of React functions and in a stable order.",
    "identity": "The property that lets an application recognize the same actor, record, or UI item over time.",
    "immutable": "Describing an update that creates a replacement value rather than changing an existing value in place.",
    "layout": "Shared route UI that wraps child pages and can persist while the child segment changes.",
    "lifecycle": "The stages of a component or resource from setup through updates to cleanup.",
    "lifting state": "Moving shared state to the nearest common owner so multiple children can use one source of truth.",
    "map": "An array method that returns one transformed value for every input item.",
    "memo": "A React optimization that can skip a component render when its props compare equal; it is not a correctness fix.",
    "object spread": "Syntax that copies enumerable object properties into a new object, often used for immutable state updates.",
    "optimistic update": "Showing an expected result before the server confirms it, with a plan for failure or rollback.",
    "parent": "A component or route that renders or owns a nested child boundary.",
    "permission": "A named capability that an identified actor may or may not exercise.",
    "previous state": "The state value from which a functional updater computes a next value.",
    "pure function": "A function whose result depends only on its inputs and which does not mutate outside state.",
    "ref": "A React escape hatch for holding a mutable value or DOM reference without causing a render when it changes.",
    "ref cleanup": "The cleanup that releases a ref-created resource or disconnects a DOM relationship.",
    "render": "React evaluating component inputs and returning a description of the current UI.",
    "selector": "A function that chooses a smaller value from a larger state or data structure.",
    "shared state": "State that multiple components need to read or change through a common owner.",
    "source of truth": "The one authoritative value from which other views or derived values should be calculated.",
    "stale closure": "A function that still reads props or state captured by an older render.",
    "state transition": "The change from one named UI or data state to another after an event or operation.",
    "strict mode": "A development-only React mode that exposes unsafe patterns and repeated setup assumptions.",
    "suspense": "A React boundary that coordinates fallback UI while a child is not ready to render.",
    "synchronization": "Keeping an external system aligned with the current React inputs after a render.",
    "transition": "A React update marked as non-urgent so urgent interaction can remain responsive.",
    "useActionState": "A React Hook that connects an Action to state representing its pending and returned result.",
    "useCallback": "A Hook that can preserve a function identity while its dependencies remain unchanged.",
    "useFormStatus": "A Hook that reads pending form submission status from a descendant form boundary.",
    "useMemo": "A Hook that can reuse a calculation while its dependencies remain unchanged; it does not make stale data correct.",
    "useRef": "A Hook that returns a stable mutable ref object whose changes do not trigger rendering.",
    "useTransition": "A Hook that marks selected updates as non-urgent and exposes pending state.",
    "use server": "A directive marking a module or function as server-owned for a Next.js server boundary.",
    "accessibility": "Designing and testing the interface so people using different abilities and input methods can complete tasks.",
    "app": "The App Router application directory where route segments, layouts, pages, and special files are defined.",
    "catch-all": "A dynamic route segment that captures one or more remaining path segments.",
    "configuration": "The explicit settings that tell a tool, framework, or deployment how to behave.",
    "create-next-app": "The official command-line starter that creates a Next.js project with selected options.",
    "dynamic segment": "A bracketed route folder whose name is filled from a URL segment at request or build time.",
    "generateMetadata": "A Next.js function that computes route metadata from its inputs, often including dynamic params.",
    "loading.tsx": "A Next.js special file that supplies a loading UI for a route segment while work is pending.",
    "nested layout": "A layout nested beneath another layout and applied to a smaller route subtree.",
    "not-found": "The deliberate route outcome used when a requested resource does not exist or is not accessible.",
    "page": "The Next.js special file that renders the UI for a route segment.",
    "params": "The dynamic route values extracted from a Next.js URL.",
    "private folder": "A Next.js folder prefixed with an underscore that is used for colocation without becoming a route segment.",
    "redirect": "A response or framework operation that sends the browser to another URL.",
    "revalidate": "A cache policy or operation that determines when previously generated data should be refreshed.",
    "revalidation": "Refreshing cached or rendered data according to a route or data policy.",
    "route.ts": "A Next.js special file that defines HTTP method handlers for a route endpoint.",
    "searchParams": "The query-string values supplied after a `?` in a URL.",
    "server-only": "A guard or convention that prevents private server modules from entering a browser bundle.",
    "server component": "A component rendered in the server environment by default in the Next.js App Router.",
    "streaming": "Sending ready parts of a response while slower parts continue instead of waiting for the whole tree.",
    "Turbopack": "A bundler used by Next.js development or build workflows to process application modules.",
    "use": "A React API for reading certain resources or context values within supported render boundaries.",
    "API": "A documented program boundary that defines how callers request data or behavior.",
    "CLI": "A command-line interface used to run a tool through a terminal.",
    "CSRF": "Cross-site request forgery, in which an unwanted request is induced from another site using a user's authority.",
    "DTO": "A data transfer object that exposes a deliberate boundary shape instead of passing an internal database row.",
    "E2E": "End-to-end testing that follows a user or system journey across the running application.",
    "HTTP": "The request and response protocol used by browsers and web services.",
    "HttpOnly": "A cookie flag that prevents ordinary browser JavaScript from reading the cookie value.",
    "MIME type": "A content-type label such as `image/png` that describes the format of uploaded or returned data.",
    "ORM": "An object-relational mapper that represents database tables and queries through application-level APIs.",
    "POST": "The HTTP method commonly used to submit data or request a server-side creation or action.",
    "SQL": "The language and query model commonly used to read and change relational database data.",
    "SQLite": "A file-based relational database useful for local development and bounded fixtures.",
    "SameSite": "A cookie policy controlling when the browser sends the cookie in cross-site contexts.",
    "Secure": "A cookie flag that restricts transmission to HTTPS requests.",
    "Tailwind CSS": "A utility-first CSS framework whose classes compose layout, spacing, color, and responsive behavior.",
    "Tailwind": "A shorthand reference to Tailwind CSS utility classes and its design-token workflow.",
    "XSS": "Cross-site scripting, in which untrusted content is interpreted as executable script in a user's context.",
    "GET": "The HTTP method commonly used to request a representation of data without asking the server to create or change it.",
    "demonstration": "A runnable or observable example used to connect an explanation to evidence.",
    "getServerSideProps": "A Pages Router data-loading API that runs on the server and is compared with App Router patterns during migration.",
    "getStaticProps": "A Pages Router build-time data-loading API that is compared with App Router generation and caching patterns during migration.",
    "reduced motion": "A user preference that asks interfaces to reduce non-essential animation and movement.",
})

TERM_MEANINGS.update({
    "Button": "A native interactive control that submits an action or performs a command when activated.",
    "Dialog": "A modal or non-modal surface that temporarily presents focused content and an interaction.",
    "Drizzle ORM": "A TypeScript-oriented database toolkit that represents SQL schemas and queries in application code.",
    "ESLint": "A static analysis tool that reports code patterns which are incorrect, risky, or inconsistent with project rules.",
    "Image": "The Next.js image component or an image asset that needs dimensions, loading, and alternative text decisions.",
    "JavaScript modules": "Files with explicit imports and exports that form the dependency graph of an application.",
    "Label": "Visible text that names a form control and helps people understand what input it expects.",
    "Link": "A navigation control that points to another URL and should preserve ordinary keyboard and browser behavior.",
    "NEXT_PUBLIC": "A Next.js environment-variable prefix indicating that the value may be included in browser code.",
    "Pages Router": "The older Next.js routing model based on the `pages/` directory, contrasted with the App Router.",
    "Playwright": "A browser automation and end-to-end testing tool for checking real user journeys.",
    "PostCSS": "A CSS transformation pipeline that processes styles through configured plugins.",
    "README": "The repository's entry document that explains purpose, setup, workflow, and where to begin.",
    "Request": "An incoming HTTP message containing a method, URL, headers, cookies, and possibly a body.",
    "Response": "The HTTP result returned to a caller, including status, headers, and optional body data.",
    "Sheet": "A side or bottom surface used to present related controls while preserving the surrounding page context.",
    "Turbopack": "A Next.js bundler and development engine that processes the module graph for fast feedback.",
    "URL": "The structured address that identifies a web resource and may include path and query values.",
    "acceptance criteria": "Observable statements that define what must be true before a feature is considered complete.",
    "abort": "Stopping an in-flight asynchronous operation when the caller no longer owns or needs its result.",
    "annotation": "Metadata attached to code or data to clarify type, intent, or processing rules.",
    "architecture": "The arrangement of application boundaries, responsibilities, data flow, and deployment parts.",
    "array spread": "Syntax that copies array items into a new array, often used to make an immutable update.",
    "async component": "A component function that can await server-side work before returning its UI.",
    "attribute": "A name-value detail attached to an HTML or JSX element, such as `href` or `aria-label`.",
    "bottleneck": "A constrained step that limits the throughput or responsiveness of a larger operation.",
    "breakpoint": "A responsive layout threshold at which the design changes to fit a different viewport condition.",
    "bundler": "A build tool that follows module imports and produces runtime-ready output files.",
    "children": "The JSX content nested inside a component and received through its `children` prop.",
    "className": "The JSX property that assigns CSS classes to a rendered element.",
    "coercion": "An implicit or explicit conversion of a value from one JavaScript type to another.",
    "colocation": "Keeping code close to the route or feature that owns it without making every file a public route.",
    "column": "One named field in a relational table, with a defined value type and constraints.",
    "compiler": "A tool that transforms or checks source code before a runtime executes it.",
    "componentDidMount": "A legacy class lifecycle method that runs after a class component first commits.",
    "componentDidUpdate": "A legacy class lifecycle method that runs after a class component updates.",
    "componentWillUnmount": "A legacy class lifecycle method where cleanup runs before a class component is removed.",
    "components.json": "Project configuration used by the shadcn/ui workflow to locate components, aliases, and styling conventions.",
    "consumer": "The component, module, or service that reads a value supplied by another boundary.",
    "contrast": "The visual difference between foreground and background needed for readable and accessible content.",
    "credential": "Secret or identifying material used to prove access to a system; it must be handled as sensitive.",
    "dangerouslySetInnerHTML": "A React escape hatch that inserts HTML and therefore requires carefully trusted or sanitized content.",
    "dark mode": "A visual theme that uses alternate colors and surfaces for a darker display condition.",
    "dashboard": "A route or screen that summarizes important records, statuses, actions, or navigation.",
    "data model": "The structured representation of entities, fields, relationships, and constraints in an application.",
    "data table": "A UI that presents records in rows and columns while supporting readable headers and states.",
    "data-access layer": "A module boundary that owns queries and maps storage results into deliberate application data.",
    "database query": "A structured request that selects, inserts, updates, or deletes records in a database.",
    "default value": "The value used when an input is missing, empty, or has not yet received an explicit value.",
    "defaultValue": "The initial DOM value for an uncontrolled form control, unlike a continuously controlled `value`.",
    "deferred value": "A lower-priority view of a value that can keep urgent input responsive while work catches up.",
    "dependency array": "The list of reactive values that determines when a Hook's synchronization or memoized calculation changes.",
    "deployment": "Publishing a built application and its configuration into an environment where users or systems can access it.",
    "design system": "A maintained set of visual tokens, components, patterns, and usage rules shared across a product.",
    "destructuring": "JavaScript syntax that extracts named properties or positions into local variables.",
    "dev server": "A local development process that watches source files and serves the application with fast feedback.",
    "dispatch": "The operation of sending an action to a reducer or state machine for a next state decision.",
    "download": "Transferring a file or response from the application to a user's device or caller.",
    "duplication": "Repeated knowledge or implementation that can drift because multiple copies must be maintained.",
    "dynamic import": "Loading a module on demand instead of including it in the initial module path.",
    "element": "A concrete node in the rendered HTML or DOM tree, such as a button, heading, or form.",
    "environment poisoning": "Accidentally exposing server-only secrets or dependencies to a less-trusted client environment.",
    "error contract": "A documented shape and meaning for how a boundary communicates failure.",
    "error message": "Human-readable feedback that explains a failure and, where possible, the next useful action.",
    "evidence": "A reproducible observation, command, test, or artifact that supports a technical claim.",
    "expected error": "A deliberate failure outcome that the application models and handles as part of normal behavior.",
    "expiry": "The time or condition after which a cookie, session, cache entry, or credential is no longer accepted.",
    "fetch": "The browser or server API for making an HTTP request and awaiting its response.",
    "font": "A typeface resource whose loading, fallback, and display choices affect readability and performance.",
    "foreign key": "A database field that refers to a key in another table and represents a relationship.",
    "form action": "The function or URL associated with a form's submit operation.",
    "fresh": "Data that satisfies the current freshness policy and has not exceeded its allowed staleness.",
    "generated source": "Code created by a tool from configuration or a schema, which should be understood before editing.",
    "global state": "State shared across distant components through a common store or provider rather than local ownership.",
    "global stylesheet": "CSS loaded for the application as a whole rather than scoped to one component.",
    "headers": "Metadata sent with an HTTP request or response, such as content type, cache policy, or tracing IDs.",
    "inference": "A type system's deduction of a value's type from its usage and available declarations.",
    "instrumentation": "Code that records or observes runtime behavior for diagnostics, metrics, or tracing.",
    "integration": "The connection of a feature to another real boundary such as a database, provider, or browser.",
    "interface": "A declared contract describing the shape and capabilities expected at a code boundary.",
    "invalidation": "Marking cached or derived data as no longer safe to reuse without a fresh calculation.",
    "invariant": "A condition that must remain true across all accepted states or operations.",
    "jose": "A JavaScript library family for working with signed or encrypted JSON-based security tokens.",
    "layout scope": "The set of route segments that inherit a particular shared layout.",
    "lazy": "Deferring work until it is needed rather than performing it during initial loading.",
    "lint": "Automated source analysis that catches suspicious patterns and enforces project conventions.",
    "meta": "Short metadata describing a page, asset, or data object for a consumer or tool.",
    "multipart": "An HTTP body encoding that can carry multiple fields and file parts in one form submission.",
    "narrowing": "TypeScript reasoning that reduces a broad type to a safer specific type after a runtime check.",
    "navigation": "Moving from one URL or route state to another while preserving the intended user journey.",
    "object storage": "A service or boundary that stores files as objects addressed by keys rather than relational rows.",
    "optimistic": "Assuming a requested operation will succeed for responsiveness while retaining a failure path.",
    "ownership": "The actor, component, or module responsible for creating, changing, and validating a value.",
    "package.json": "The Node project manifest containing scripts, package metadata, and dependency declarations.",
    "parse": "Reading an input representation and converting it into a structured value or a deliberate failure.",
    "path": "The pathname portion of a URL or the filesystem location used to resolve a module or file.",
    "portfolio": "A public-facing record of work, decisions, evidence, and limitations that demonstrates capability.",
    "precedence": "The rule that decides which CSS, route, configuration, or operation wins when choices overlap.",
    "primary key": "A database field or combination of fields that uniquely identifies a row.",
    "priority": "The relative urgency assigned to work so an application can schedule or process it appropriately.",
    "profiler": "A tool that records render or runtime timing so expensive work can be investigated with evidence.",
    "public": "A route, asset, value, or boundary intentionally available without a private server check.",
    "purity": "The property of producing the same result from the same inputs without external mutation or side effects.",
    "recovery": "The user or system path that returns from a failure to a useful next state.",
    "ref prop": "A React 19-compatible prop boundary through which a ref can be passed without a wrapper pattern.",
    "reference": "A pointer or identity that lets code reach an object, DOM node, resource, or source document.",
    "relation": "A connection between records or tables that describes how entities belong together.",
    "repository": "A data-access module that hides storage details behind application-specific operations.",
    "request ID": "A correlation value that lets logs and traces for one request be found across boundaries.",
    "residual risk": "A known uncertainty or remaining risk after the implemented controls and tests.",
    "return API": "The documented values and behaviors a function or module promises to return to its caller.",
    "reuse": "Applying one tested implementation in multiple contexts without copying its knowledge.",
    "review": "A deliberate inspection of code, evidence, trade-offs, and remaining risks before acceptance.",
    "route map": "A written representation of URLs, route files, layouts, and boundaries in an application.",
    "row": "One record or horizontal item in a table or data presentation.",
    "runtime": "The environment and rules that execute code, such as a browser, Node.js, or the Next.js server.",
    "safeParse": "A validation operation that returns a success or failure result without throwing for expected invalid input.",
    "seed": "Controlled initial data inserted into a local or test database so examples are repeatable.",
    "searchParams": "The decoded query-string values after the pathname in a URL.",
    "sidebar": "Persistent navigation or context UI that sits beside the main content in a layout.",
    "size limit": "A maximum allowed amount of data, such as upload bytes or request body size.",
    "skeleton": "Temporary layout-shaped UI shown while content is loading.",
    "slug": "A URL-safe identifier derived from a title or record name.",
    "spread": "Syntax that copies values into a new array or object so an update can preserve existing data.",
    "stale": "No longer current under the relevant state, cache, session, or data policy.",
    "start": "The initial action or entry point that begins a documented learning or runtime flow.",
    "startTransition": "A React API that marks an update as non-urgent and exposes whether it is pending.",
    "structured log": "A machine-readable log event with consistent fields for searching and correlation.",
    "stylesheet": "A CSS resource containing rules that control the presentation of rendered elements.",
    "subscription": "A live connection that receives future events until it is explicitly removed.",
    "table": "A relational database structure containing rows with named columns.",
    "tag": "An HTML or JSX element name that describes structure or semantics.",
    "tenant": "An isolated organization or customer scope whose data must not cross into another scope.",
    "test plan": "A written set of behaviors, fixtures, commands, and boundaries that testing will cover.",
    "theme variable": "A named design token used to keep visual choices consistent across themes and components.",
    "throw": "JavaScript control flow that signals an exceptional result to the nearest handling boundary.",
    "title": "The human-readable name or page metadata that identifies a case, resource, or document.",
    "token": "A small named design value, or a security value whose trust and lifetime must be documented.",
    "trade-off": "A consequence accepted when choosing one design option over another.",
    "transaction": "A group of data operations that should commit together or roll back together.",
    "trusted data": "Data that has passed the required validation and authority checks for the current boundary.",
    "type": "A declaration or runtime category describing what values and operations are allowed.",
    "typecheck": "A static verification that source values and operations satisfy the TypeScript type contracts.",
    "uncontrolled": "A form input whose current value is owned by the DOM and read through a ref or submit boundary.",
    "unexpected error": "A failure outside the documented normal input cases that requires safe logging and fallback behavior.",
    "union": "A TypeScript type that allows one of several documented alternatives, often discriminated by a status field.",
    "update": "A request to move state, data, or configuration from its current value to a next value.",
    "upload": "Sending a file or binary content from a user or system to an application or storage boundary.",
    "user behavior": "The observable actions and decisions a person makes while using the interface.",
    "utility class": "A small CSS class representing one visual rule that can be composed with other utilities.",
    "waterfall": "A sequence in which one asynchronous operation waits for another, increasing total latency.",
})


def teaching_profile(title: str) -> dict[str, str]:
    lower = title.lower()
    if "what is state" in lower:
        return {"problem": "A value changes in the interface, but a local variable can change without causing the screen to update.", "analogy": "A door can be open or closed; the useful condition is the one the person looking at it can see now.", "sequence": "We will first make a local-variable counter fail, then give React ownership with useState, then apply the idea to a small queue.", "mistake": "Change a local variable and expect React to know that the screen should be calculated again.", "application": "a local case queue with a clear action and an empty state", "boundary": "the component that owns the changing value and the event that requests its next value", "prereq": "functions, JSX expressions, and browser click handlers"}
    if "usestate" in lower or "setters" in lower:
        return {"problem": "One update is easy, but repeated updates and object state reveal that a setter is a request rather than a normal assignment.", "analogy": "A queue of instructions is processed in order; two instructions that both say ‘set it to 1’ are not the same as two instructions that say ‘add one.’", "sequence": "We will compare one direct update, two direct updates, two functional updaters, object replacement, and a controlled form.", "mistake": "Read one render snapshot twice or replace an object without copying the fields that should remain.", "application": "a controlled case draft whose fields update without erasing each other", "boundary": "the render snapshot, pending update queue, and component that owns the setter", "prereq": "state snapshots, event handlers, arrow functions, and object spread"}
    if "component" in lower:
        return {"problem": "A page that starts as one function becomes hard to read, reuse, and change when several responsibilities accumulate.", "analogy": "A complete page is like a room with labeled areas: the labels help people find and change one responsibility without opening the whole building.", "sequence": "We will show one complete page, split it into Header/Main/Footer, pass props to a reusable card, and compose a small dashboard.", "mistake": "Split every element mechanically or use a lowercase component name that JSX treats as a browser element.", "application": "a local case dashboard built from a shell, summary, list, and card", "boundary": "the parent-to-child data flow and the responsibility owned by each component", "prereq": "JavaScript functions, JSX, and the local React playground"}
    if "props" in lower or "one-way" in lower:
        return {"problem": "A child needs data from its parent and a way to request intent without reaching into the parent's private state.", "analogy": "A form receives a prepared clipboard from a supervisor; it can read the fields and report a requested change, but it does not secretly edit the supervisor's records.", "sequence": "We will pass a value down, attempt an invalid prop mutation, and replace it with a callback that sends intent upward.", "mistake": "Treat read-only props as local mutable storage or create a second copy that can disagree with the owner.", "application": "a reusable case card and button whose parent owns the data", "boundary": "props flow down; callbacks carry intent up; the owner decides whether state changes", "prereq": "function components, JSX attributes, and event handlers"}
    if "list" in lower or "keys" in lower:
        return {"problem": "A collection must become repeated UI without losing the identity of one item when order or data changes.", "analogy": "A labeled case file remains the same file when it moves from one shelf position to another; position alone is not identity.", "sequence": "We will render one item, map a collection, reorder it, and compare stable IDs with array indexes as keys.", "mistake": "Use position as identity and then observe state or focus appear attached to the wrong item after reordering.", "application": "a case list with stable synthetic IDs and an explicit empty state", "boundary": "the data identity crossing from an array record into a rendered list item", "prereq": "arrays, map, JSX expressions, and component props"}
    if "effect" in lower or "cleanup" in lower:
        return {"problem": "Rendering describes UI, but some work must synchronize with something outside React, such as a title, timer, subscription, or request.", "analogy": "A room display can change because the building's outside sign must also be updated; the sign is an external system with a connection and a cleanup rule.", "sequence": "We will distinguish rendering from synchronization, add a dependency, create cleanup, and remove an unnecessary calculation Effect.", "mistake": "Use an Effect for a value that can be calculated during render or omit a dependency and observe stale work.", "application": "a local status title or synthetic subscription with setup and cleanup evidence", "boundary": "the line between React's render calculation and an external system's lifecycle", "prereq": "state, render snapshots, functions, and browser APIs"}
    if "hook" in lower:
        return {"problem": "Several components need the same stateful behavior, but copying the behavior creates inconsistent fixes and unclear APIs.", "analogy": "A reusable tool has a small handle and clear result; the person using it should not need to know its internal gears.", "sequence": "We will identify repeated behavior, extract a custom Hook, enforce the Rules of Hooks, and design a small return API.", "mistake": "Call a Hook conditionally or hide unrelated responsibilities in a Hook with an unclear contract.", "application": "a local toggle, data viewer, or form behavior with a named Hook API", "boundary": "the Hook owns reusable behavior while the component owns its visible composition", "prereq": "useState, Effects, and function component call sites"}
    if "class" in lower or "lifecycle" in lower:
        return {"problem": "A learner must be able to read existing class-based React while choosing function components for new code.", "analogy": "Learning to read an older map is different from choosing the map format for a new journey.", "sequence": "We will read the old API, trace state and lifecycle responsibilities, map them to Hooks, and identify where a mechanical translation would be wrong.", "mistake": "Declare the old API useless or translate lifecycle names one-for-one without preserving the actual synchronization rule.", "application": "a small class component migrated to a function component with equivalent visible behavior", "boundary": "legacy lifecycle responsibility versus modern state, Effect, and error boundaries", "prereq": "components, props, state, and basic JavaScript classes"}
    if "testing" in lower or "test" in lower:
        return {"problem": "A component can render and still be wrong for the user's actual journey, especially at empty, error, keyboard, or unauthorized boundaries.", "analogy": "A rehearsal checks the actions a person must take, not whether the stage lights happen to turn on once.", "sequence": "We will state a behavior claim, exercise it through the public UI or route contract, add a failure case, and distinguish test evidence from proof of production correctness.", "mistake": "Assert a private implementation detail while skipping the visible contract the learner actually needs to protect.", "application": "a local synthetic case journey with normal, invalid, empty, and failure fixtures", "boundary": "the public behavior under test and the internal implementation that may change", "prereq": "the component or route behavior being tested and a runnable starter"}
    if "next.js installation" in lower or "project structure" in lower or "root app" in lower or "src/app" in lower:
        return {"problem": "A new Next.js project contains several conventions, and an incorrect folder choice can make a route disappear or configuration ambiguous.", "analogy": "A workshop needs a clear separation between tools, storage, and workbenches; two rooms claiming to be the same entrance create confusion.", "sequence": "We will inspect the generated files, run the first route, compare root app with src/app, and choose one unambiguous project layout.", "mistake": "Keep duplicate routers or treat generated configuration as magic that should never be inspected.", "application": "a small App Router starter whose source, configuration, and public assets have named homes", "boundary": "application source versus root configuration and the route files Next.js recognizes", "prereq": "React components, a terminal, Node.js, and the setup guide"}
    if "tailwind" in lower or "shadcn" in lower:
        return {"problem": "A full application needs consistent visual language and accessible controls without burying every decision in ad-hoc CSS or an opaque package.", "analogy": "A design system is a box of labeled building pieces: the pieces are quick to use, but their source and rules must remain inspectable.", "sequence": "We will style one visible element, introduce tokens and responsive states, then own and compose an accessible UI primitive.", "mistake": "Copy a configuration from the wrong major version, scatter arbitrary colors, or treat generated component source as a black box.", "application": "a local dashboard shell with a readable, keyboard-usable Button and empty state", "boundary": "design-system primitives versus feature-specific data, authorization, and application behavior", "prereq": "JSX, className, the Next.js starter, and basic CSS"}
    if "schema validation" in lower or "validation" in lower:
        return {"problem": "Form data and request bodies arrive as untrusted values, but application code needs a precise shape before it can act.", "analogy": "A receiving desk checks a package's label, size, and contents before sending it into the warehouse.", "sequence": "We will inspect raw input, define a schema, compare parse and safeParse, display field errors, and keep invalid data away from the mutation.", "mistake": "Trust a form value because the input element looks constrained or use a type annotation as runtime validation.", "application": "a local case form with structured invalid-input feedback", "boundary": "untrusted input crossing into typed application logic", "prereq": "forms, objects, TypeScript shapes, and server/client boundaries"}
    if "sql" in lower or "drizzle" in lower or "repository" in lower:
        return {"problem": "A growing application needs durable records and a data-access boundary that preserves ownership, migrations, and reviewability.", "analogy": "A case archive needs labeled shelves and a catalog; writing a note on a screen is not the same as storing a record safely.", "sequence": "We will model a table, create a local schema, migrate and seed it, query through a repository, and keep raw database details out of UI components.", "mistake": "Change a schema without a migration, return another user's row, or pass raw database objects and secrets into a Client Component.", "application": "a local synthetic case repository with typed reads and resettable seed data", "boundary": "database schema and repository versus UI data-transfer shape and authorization policy", "prereq": "objects, async functions, server-only modules, and the local project structure"}
    if "server action" in lower or "forms and server actions" in lower:
        return {"problem": "A form needs to change server-owned data while preserving validation, authorization, pending state, and a useful result.", "analogy": "A signed request goes to the office that owns the records; the front desk can report pending or rejected, but it cannot approve itself.", "sequence": "We will submit FormData, validate it on the server, check permission, mutate a local record, and revalidate the visible route.", "mistake": "Trust a client-provided owner, validate only in the browser, or refresh the page before the mutation succeeds.", "application": "a validated local create-case mutation with field errors and revalidation evidence", "boundary": "browser intent versus server authority and data mutation", "prereq": "forms, async functions, validation, and Next.js Server Components"}
    if "route handler" in lower or "http" in lower or "api" in lower:
        return {"problem": "Sometimes a browser, test, webhook, or other client needs a documented HTTP boundary rather than a component-only interaction.", "analogy": "A service counter has a public request format, a response receipt, and a deliberate way to say no.", "sequence": "We will read a Request, validate its body, return success and failure status codes, and test the public response contract.", "mistake": "Return 200 for invalid input, leak stack traces, or confuse an internal function result with an HTTP response.", "application": "a local synthetic Route Handler with typed success and error JSON", "boundary": "public HTTP contract versus private data-access and authorization decisions", "prereq": "async JavaScript, JSON, validation, and Next.js route files"}
    if "authentication" in lower or "session" in lower or "proxy" in lower or "authorization" in lower or "tenant" in lower:
        return {"problem": "A full application must identify a caller and decide what that caller may do; a redirect or hidden link alone is not protection.", "analogy": "A building entrance may check for a badge, but each room still checks whether the visitor is allowed to open the cabinet inside.", "sequence": "We will separate identity, session, Proxy navigation, authoritative authorization, ownership, and tenant boundaries with synthetic actors.", "mistake": "Treat a browser field, client redirect, or login flag as proof of permission and return data before the server policy runs.", "application": "a local protected case route with synthetic sessions, permissions, and unauthorized fixtures", "boundary": "identity and navigation checks versus server-side data and mutation authority", "prereq": "Next.js routing, server/client boundaries, cookies, and validation"}
    if "upload" in lower or "storage" in lower:
        return {"problem": "Files are larger and more ambiguous than ordinary text fields, and a filename is not a security policy.", "analogy": "A receiving dock weighs and labels a package before storing it; a name written on the box does not prove what is inside.", "sequence": "We will bound size and type, record safe metadata, choose a storage boundary, and authorize a download.", "mistake": "Trust extensions, accept unlimited bytes, or serve a stored object without checking ownership.", "application": "a local synthetic upload validator and authorized download response", "boundary": "browser file input versus server validation, storage, and access policy", "prereq": "forms, validation, HTTP responses, and authorization"}
    if "capstone" in lower or "production" in lower or "deployment" in lower:
        return {"problem": "A project is not finished when the happy path works; other people need to understand its architecture, evidence, limitations, and recovery plan.", "analogy": "A bridge is accepted with inspection records, load assumptions, emergency access, and maintenance plans, not only a photograph of one crossing.", "sequence": "We will state the architecture, build a vertical slice, exercise failure and authorization paths, record checks, and demonstrate residual risk honestly.", "mistake": "Confuse a clean build or screenshot with proof that every user, permission, failure, and deployment condition is safe.", "application": "a portfolio-ready local case-management feature with architecture and evidence notes", "boundary": "demo evidence versus production claims, operational ownership, and residual risk", "prereq": "the preceding React/Next.js phases and a working local project"}
    return {"problem": f"The learner needs to see what {title.lower()} does before learning its name.", "analogy": "A small workshop task lets the learner change one thing and see the result.", "sequence": "We will run a small example, change one input, look at the result, make a common mistake, fix it, and try one small variation.", "mistake": "Copy the code without checking the input and the result.", "application": "a small local example", "boundary": "the line or file that changes the result", "prereq": "the previous lesson, the setup guide, and the smallest prerequisite named in the opening"}


def term_meaning(term: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "", term.lower())
    for key, meaning in TERM_MEANINGS.items():
        if re.sub(r"[^a-z0-9]+", "", key.lower()) == normalized:
            return meaning
    if normalized.endswith("s"):
        singular = normalized[:-1]
        for key, meaning in TERM_MEANINGS.items():
            if re.sub(r"[^a-z0-9]+", "", key.lower()) == singular:
                return meaning
    return f"`{term}` is a lesson-specific value, rule, or boundary. In today's example, identify what supplies it, what it changes, and what evidence would show that it is working."


def keywords_table(raw: str) -> str:
    terms = [item.strip() for item in raw.split(",")]
    rows = ["| Keyword or term | Plain-English meaning |", "| --- | --- |"]
    for term in terms:
        rows.append(f"| `{term}` | {term_meaning(term)} |")
    return "\n".join(rows)


def topic_explanation(topic: str, title: str) -> str:
    question = topic.rstrip("?")
    lower = question.lower()
    if lower.startswith("what"):
        opening = f"Start with the learner's concrete question: **{question}**. Look at **{question}** in the example before learning the technical name."
        practice = f"For **{question}**, point to the smallest value, element, function, or route that shows the answer."
    elif lower.startswith("why"):
        opening = f"Answer **{question}** by comparing the working example with a broken or limited example."
        practice = f"For **{question}**, say what changed and which result is easier or safer to use."
    elif lower.startswith("how"):
        opening = f"To answer **{question}**, follow the operation in order rather than treating the result as framework magic."
        practice = f"For **{question}**, write the starting value, the change you made, and the new result."
    elif lower.startswith("when"):
        opening = f"Treat **{question}** as a simple choice. Start with a normal example and then try an empty or bad example."
        practice = f"For **{question}**, write what the program should do in both examples."
    else:
        opening = f"Study **{question}** by looking at the value, operation, and result in the worked example."
        practice = f"For **{question}**, point to the line that shows the idea and say what would change it."
    return f"{opening} {practice}"


def topic_practice_prompt(topic: str, title: str) -> str:
    lower = topic.lower()
    profile = teaching_profile(title)
    if "why" in lower:
        return f"For **{topic}**, compare the working example with the broken example. What changed? Which result is safer or easier to understand?"
    if "how" in lower:
        simple_topic = topic.rstrip("?")
        return f"For **{simple_topic}**, change one input in the example. Write the old result and the new result for **{simple_topic}**."
    if "when" in lower:
        return f"For **{topic}**, write one normal example and one empty or bad example. Say what each should do."
    simple_topic = topic.rstrip("?")
    return f"For **{simple_topic}**, say what goes in and what comes out."


def topic_sections(raw: str, title: str) -> tuple[str, str]:
    topics = [item.strip() for item in raw.split(";")]
    toc = []
    body = []
    for topic in topics:
        heading = f"### {topic}"
        anchor = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
        toc.append(f"  - [{topic}](#{anchor})")
        body.append(f"{heading}\n\n{topic_explanation(topic, title)}\n\n**Try it before moving on:** {topic_practice_prompt(topic, title)}")
    return "\n".join(toc), "\n\n".join(body)


def line_by_line(code: str, title: str = "") -> str:
    rows = ["| Line | What this line does |", "| ---: | --- |"]
    profile = teaching_profile(title) if title else None
    for number, raw_line in enumerate(code.splitlines(), 1):
        line = raw_line.strip()
        if not line:
            rows.append(f"| {number} | Blank line: it separates the surrounding ideas; it has no runtime operation. |")
            continue
        if line.startswith("import "):
            explanation = "Loads a value from another file so this file can use it."
        elif line.startswith("export "):
            explanation = "Makes this value available to another file."
        elif "useState" in line and "[" in line:
            explanation = "Gets the current value and a function that asks React for a new value."
        elif "useState" in line:
            explanation = "Creates a value that React remembers when the component renders again."
        elif "useEffect" in line:
            explanation = "Tells React to run this outside task after the screen is updated."
        elif "setCount" in line or "setState" in line or "setProfile" in line or "setCases" in line:
            explanation = "Asks React to use a new value on the next render."
        elif "onClick" in line or "onChange" in line or "onSubmit" in line:
            explanation = "Tells the browser which function to run when the user performs this action."
        elif ".map(" in line or "map((" in line:
            explanation = "Runs the function once for each item and collects the new results."
        elif "await " in line:
            explanation = "Waits for the async task to finish before continuing."
        elif line.startswith("if ") or line.startswith("if("):
            explanation = "Checks a condition and runs the next code only when the condition is true."
        elif line.startswith("return ") or line == "return":
            explanation = "Sends a value or UI tree back to the code that called this function."
        elif line.startswith("console."):
            explanation = "Prints a value so you can compare the result with your prediction."
        elif "=>" in line or line.startswith("function ") or line.startswith("class "):
            explanation = "Defines a function or component that can be used later."
        elif line.startswith("<") or line.startswith("</") or line.startswith("//"):
            explanation = "Creates a piece of the UI or explains the code in a comment."
        elif "=" in line:
            explanation = "Stores the value on the right under the name on the left."
        else:
            explanation = f"Runs as part of this example. After `{line}`, check the next line to see the result."
        escaped = line.replace("|", "\\|")
        rows.append(f"| {number} | `{escaped}` — {explanation} |")
    return "\n".join(rows)


def independent_exercises(title: str, raw_topics: str, repair: str) -> str:
    lower = title.lower()
    profile = teaching_profile(title)
    if "component" in lower and "class" not in lower:
        items = [
            "Run the page unchanged. Write down the three parts you can see.",
            "Write a `Header` component and move the heading into it.",
            "Write one sentence: what does the `Header` component do?",
            "Pass a `title` prop to a component and display two different titles.",
            "Put a parent component and two child components on the page.",
            "Change a component name to lowercase. Read the error or wrong result.",
            "Change the name back to a capital letter and run the page again.",
            "Show a clear message when the list has no items.",
            "Add a real heading, button, or link that a keyboard user can use.",
            "Write one check that fails if the component’s visible text disappears.",
            f"Build a small {profile['application']} with the components from this lesson.",
            "Answer: which component owns each piece of data? Use one short sentence per piece.",
        ]
    elif "state" in lower or "usestate" in lower or "reducer" in lower or "context" in lower:
        items = [
            "Run the example. Write down the number or message shown before clicking anything.",
            "Click the button once, then twice. Write down the number after each click.",
            "Change the starting value. Predict the first number before you run the page.",
            "Add a `Reset` button. When clicked, it must show `0` or the lesson’s starting value.",
            "Make the beginner mistake shown in the lesson. Write down what goes wrong.",
            "Fix the mistake and run the normal example again.",
            "Answer: which component stores the changing value? Point to the line where it is created.",
            "Add a message that tells the user how many items are in the list.",
            "Write one test for the normal case and one test for an empty list.",
            f"Build a small {profile['application']} using this lesson’s state pattern.",
            "Answer: what should the user see while the list is empty?",
            "Write three sentences explaining the value, the button, and the screen update.",
        ]
    elif "effect" in lower or "hook" in lower:
        items = [
            "Run the example. Write down what appears before you change it.",
            "Write the name of the outside thing the code talks to, such as the document title or a timer.",
            "Change one dependency. Predict whether the work runs again, then check.",
            "Show a loading, empty, or disconnected message that fits the example.",
            "Make the Hooks mistake shown in the lesson. Write down the error or wrong result.",
            "Fix the mistake and run the example again.",
            "Remove the Hook when the value can be calculated during render. Explain the change in one sentence.",
            "Add cleanup for the timer, subscription, request, or other outside resource.",
            "Write one test or trace that shows setup and cleanup.",
            f"Use this behavior in a small {profile['application']} with invented data.",
            "Answer: what starts the outside work, and what stops it?",
            "Write two things this local example does not prove about a real application.",
        ]
    elif "route" in lower or "layout" in lower or "app router" in lower or "dynamic" in lower or "src" in lower:
        items = [
            "Run the route. Write down its URL and the text you see.",
            "Write the job of each special file in one short sentence.",
            "Change one folder or parameter. Predict the new URL before running it.",
            "Add the missing, loading, or not-found message from the lesson.",
            "Make the folder or file mistake shown in the lesson. Record the error.",
            "Fix the mistake and open the route again.",
            "Answer: which files are application code, and which files are project settings?",
            "Add one real heading, link, or keyboard-friendly control to the page.",
            "Write one browser check for the route’s visible text or URL.",
            f"Build a small {profile['application']} and list its route URLs.",
            "Answer: which data should stay on the server? Give one reason.",
            "Write the file tree and one sentence about what you have not tested.",
        ]
    elif "authentication" in lower or "session" in lower or "authorization" in lower or "proxy" in lower or "tenant" in lower:
        items = [
            "Run the signed-out example. Write down the page or message you see.",
            "Run the signed-in example. Write down what changed.",
            "Change one permission. Predict whether the request should be allowed or rejected.",
            "Add one invented user who is not allowed to open the record.",
            "Make the client-only protection mistake from the lesson. Record what it fails to protect.",
            "Fix the check on the server and run the allowed and rejected cases again.",
            "Write one sentence about the cookie or secret that must stay private.",
            "Write one test that proves a forbidden user cannot read or change the record.",
            "Answer: why is hiding a button not enough to protect data?",
            f"Protect a small {profile['application']} with invented users and records.",
            "Draw one arrow showing where the user’s request meets the server’s permission check.",
            "Write two things a real deployment would still need to check.",
        ]
    elif "sql" in lower or "drizzle" in lower or "repository" in lower or "data" in lower:
        items = [
            "Run the local database example. Write down the rows it returns.",
            "Draw the tables and write one sentence about what each ID means.",
            "Change one field or filter. Predict the new row before you run the query.",
            "Show what the page displays when no row is found.",
            "Make the missing-migration, raw-row, or wrong-user mistake from the lesson.",
            "Fix the mistake and run the normal and rejected cases again.",
            "Answer: which file talks to the database, and which file shows the page?",
            "Add one transaction or rollback example if the lesson teaches it.",
            "Write one test for the query’s normal result and one test for no result.",
            f"Build a small {profile['application']} with resettable invented records.",
            "Answer: how does the server stop one user from seeing another user’s record?",
            "Write the migration command, query result, and one thing you did not test.",
        ]
    elif "tailwind" in lower or "shadcn" in lower or "design" in lower:
        items = [
            "Run the starter. Write down the color, spacing, and button styles you see.",
            "Style one component. Write down the visible change.",
            "Make the layout change at one screen width. Check it in the browser.",
            "Add a dark, empty, loading, or error message to the component.",
            "Make the configuration or inaccessible-control mistake from the lesson.",
            "Fix the mistake and run the page again.",
            "Create one named color or spacing value and use it twice.",
            "Check the button with the keyboard and check that the label is readable.",
            "Write one DOM or visual check for the component.",
            f"Style a small {profile['application']} without adding unrelated packages.",
            "Answer: which styles belong to the reusable component, and which belong to this page?",
            "Save one screenshot or DOM result and write one design choice you would revisit.",
        ]
    elif "test" in lower or "testing" in lower:
        items = [
            "Write one sentence about the user action the test should protect.",
            "Run the normal example and write down the result.",
            "Add an empty, invalid, rejected, or unauthorized example.",
            "Choose a unit, integration, or browser test and say what it will click or call.",
            "Make the private-detail assertion mistake from the lesson.",
            "Fix the test so it checks what the user can see or what the route returns.",
            "Add one test for a keyboard, label, loading, or error result.",
            "Remove the behavior and make sure the test fails; restore the behavior afterward.",
            "Answer: what can this test not prove about a real deployment?",
            f"Test a small {profile['application']} with invented data.",
            "Write the public button, page, or route that the test uses.",
            "Write the commands, result, and one test case you would add next.",
        ]
    else:
        topics = [item.strip() for item in raw_topics.split(";")]
        first, second, third = topics[:3]
        items = [
            f"Answer the question **{first}** in one sentence. Point to the example that helped you.",
            "Run the example unchanged. Write down what appears.",
            "Change one value. Predict the result, then run the code and compare.",
            f"Change one input in the example for **{second}**. Write down the old and new result.",
            f"Add one simple edge case for **{third}**, such as an empty or invalid value.",
            f"Make the mistake shown in the lesson: {repair}",
            "Fix the mistake and run the normal example again.",
            "Add one clear heading, label, error message, or type check that fits this lesson.",
            "Write one check that fails when the important visible result disappears.",
            "Build the small example from this lesson in the starter.",
            "Answer: which file or function contains the important code? Give one simple reason.",
            "Write four short sentences: what you built, what you saw, what you fixed, and what you did not test.",
        ]
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, 1))


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
    profile = teaching_profile(title)
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

Start with the [course README](../README.md), [setup guide](../SETUP.md), and [day index](../DAY_INDEX.md). Choose the starter from the [examples guide](../examples/README.md). Work locally with invented data only.

Today’s steps are simple: {profile['sequence']} Run the first example. Write what you expect. Change one thing. Make the stated mistake. Fix it. Then do the numbered exercises.

## Why this lesson exists

Here is the problem: {profile['problem']}

{profile['analogy']}

Today we will learn **{title}** in small steps. {profile['sequence']} You are learning what the code does, not just memorising a word.

## Prerequisites

Complete the previous lesson and read the [setup guide](../SETUP.md). You need **{profile['prereq']}**.

Use the [examples guide](../examples/README.md) to choose the starter. If a command fails, stop. Write down the folder and command before trying again. Do not add a database, login provider, or unrelated package unless this lesson teaches it.

## Outcomes

By the end, you should be able to:

- explain **{title}** in your own words;
- run the normal example;
- show the broken example and fix it;
- change one input and predict the result; and
- use **{title.lower()}** in {profile['application']}.

This local example does not prove that a real application is secure, accessible, fast, or ready for production. We will name the important boundary later: {profile['boundary']}.

## Keywords and terms

{keywords_table(keywords)}

## Topics

{topics}

## Worked example

Start with this small example. Copy it into the starter file and run it without changing it. Write down what you see. We will then change one thing at a time. {profile['sequence']}

```tsx
{code}
```

**Expected result or visible behavior:**

```text
{output}```

Before changing the code, answer four simple questions: What goes in? What does the code do? What comes out? Which file contains the decision?

If the code is JSX, mark the JavaScript parts and the markup parts. If it runs in Next.js, say whether it is a Server Component, Client Component, Route Handler, Server Action, or Proxy file. Today’s important boundary is: {profile['boundary']}.

## Line-by-line explanation

{line_by_line(code, title)}

Use the table while you run the code. Do not only read it. If the same line behaves differently in the browser, React, and Next.js, write one short note.

## Execution trace

1. Write down the starting value: {profile['problem']}
2. Follow the code one line at a time until the result changes.
3. Write down the action, the new value, and what appears on the screen or in the terminal.
4. Compare what happened with your prediction. Say one reason if they differ.
5. Remember that this result belongs to this small local example. It is not proof that a real application is secure, accessible, fast, or correct.

Write four things in your notebook: the value before, the action, the value after, and the file or system that made the decision.

## Prediction experiment

Write your prediction before you run the experiment. Change one input related to **{title}**. Start with a normal value. Then try one useful edge case, such as an empty value, bad value, loading state, missing route, rejected action, or unauthorized user. Write what you expected. Run it. Write what actually happened. Put the normal example back when you finish.

## Broken example and repair

A deliberate failure is part of the lesson. **Broken version:** {repair}

Make the broken version in a copy. The likely mistake is: {profile['mistake']}

Run it and write down the error or wrong screen. Say what assumption was wrong. Change the smallest line that fixes the problem. Run the normal example and one edge case again. Do not hide the error with a broad catch or a disabled type check. A passing render is not proof of authorization, accessibility, or security.

## Guided practice before independent work

Do these steps in order:

1. Run the worked example unchanged.
2. Change one input and write down the new result.
3. Make the likely mistake and fix it.
4. Use the same starter for **{title.lower()}** and {profile['application']}.

Before the independent exercises, answer: What should happen for a normal value? What should happen for an empty or bad value?

## Project application

Use the local starter from the [examples guide](../examples/README.md) to build {profile['application']}.

Write down the goal and the data you will use. Show the normal case and one edge case. The important boundary is {profile['boundary']}.

Keep secrets, databases, cookies, login checks, and permission checks on the server. Use an invented user who should be rejected when the lesson involves authorization. For React-only work, use invented data and do not send it to a public service.

## Independent exercises

{independent_exercises(title, raw_topics, repair)}

## Finish line

You are finished when you can:

1. explain **{title}** to another beginner;
2. show the normal result;
3. show the broken result and the repair;
4. explain one edge case; and
5. point to **{profile['boundary']}**.

Do not move on only because the code compiles. Write one limitation of this local example.

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


def practice_hints(title: str, raw_topics: str, repair: str) -> str:
    topics = [item.strip() for item in raw_topics.split(";")]
    first, second, third = topics[:3]
    profile = teaching_profile(title)
    items = [
        f"Read the short problem statement for {title.lower()} and say what the page or program should do.",
        f"Run the example without changes. If it works, write down what you see for {profile['application']}.",
        "Point to the input and the line that changes the output. Do not try to explain the whole application at once.",
        f"Change one input for {first}. Keep every other line the same.",
        f"For {second}, try the normal case first. Then try one empty or bad value.",
        f"Make this mistake in a copy: {profile['mistake']}",
        "Read the error or wrong result. Fix one line. Run the example again.",
        f"Use invented local data while you try {third}.",
        "Check the text, number, URL, or DOM element that the learner can actually see.",
        f"Use the same starter to build {profile['application']}. Do not add a new package.",
        "A passing check only proves that check passed. Write one thing you did not test.",
        "If a technical word is confusing, define it in your own simple sentence before using it.",
    ]
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, 1))


def practice_solutions(title: str, raw_topics: str, repair: str) -> str:
    topics = [item.strip() for item in raw_topics.split(";")]
    first, second, third = topics[:3]
    profile = teaching_profile(title)
    items = [
        f"The learner can say what problem {title.lower()} solves in one or two simple sentences.",
        f"The example runs and the learner records the visible or returned result for {profile['application']}.",
        "The learner can point to the input, the important line, and the output.",
        f"The learner changes one input for {first} and records the old and new result.",
        f"The learner tries a normal and an empty or bad value for {second}.",
        f"The learner reproduces `{repair}` and writes down the error or wrong result.",
        "The learner fixes the smallest line and runs the normal case again.",
        f"The learner uses local invented data to show {third}.",
        "The test or check fails when the visible behavior is removed and passes after it is restored.",
        f"The learner builds {profile['application']} without exposing secrets or using real data.",
        "The learner writes one thing the example does not prove about a real application.",
        "The learner’s review note uses plain sentences and defines any technical word it needs.",
    ]
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, 1))


def practice_materials(day: int, title: str, raw_topics: str, repair: str) -> tuple[str, str]:
    hints = f"""# Day {day:03d} hints: {title}

Use these only after attempting the numbered exercises in [the lesson](../day_{day:03d}_{slug(title)}.md). They are specific to **{title}** and should unblock the next thought without replacing it.

## Hints

{practice_hints(title, raw_topics, repair)}
"""
    solutions = f"""# Day {day:03d} solution guide: {title}

Use this guide only after attempting the numbered exercises in [the lesson](../day_{day:03d}_{slug(title)}.md). It reviews the decisions for **{title}**; it is not a copied answer key.

## Review checkpoints

{practice_solutions(title, raw_topics, repair)}

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
"""
    return hints, solutions


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
        authored_lesson = AUTHORED_LESSONS.get(day)
        if authored_lesson and authored_lesson.exists():
            (folder / f"{folder.name}.md").write_text(authored_lesson.read_text(encoding="utf-8"), encoding="utf-8")
        else:
            (folder / f"{folder.name}.md").write_text(
                lesson(day, title, keywords, topics, code, output, repair, navigation), encoding="utf-8"
            )
        practice = folder / "practice"
        practice.mkdir()
        authored_practice = AUTHORED_PRACTICE.get(day)
        if authored_practice and authored_practice.exists():
            for source in authored_practice.glob("*.md"):
                (practice / source.name).write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
        else:
            hints, solutions = practice_materials(day, title, topics, repair)
            (practice / "exercises.md").unlink(missing_ok=True)
            (practice / "hints.md").write_text(hints, encoding="utf-8")
            (practice / "solutions.md").write_text(solutions, encoding="utf-8")
    print(f"Generated {len(LESSONS)} modern lessons with learner-specific practice materials.")


if __name__ == "__main__":
    main()
