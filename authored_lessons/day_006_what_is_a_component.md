# Day 006: What is a component?

[← Previous lesson](../day_005_tooling_and_the_first_component/day_005_tooling_and_the_first_component.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Next lesson →](../day_007_jsx_and_the_rules_of_markup/day_007_jsx_and_the_rules_of_markup.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What problem do components solve?](#what-problem-do-components-solve)
  - [What is a function component?](#what-is-a-function-component)
  - [Why are function components the modern default?](#why-are-function-components-the-modern-default)
  - [How do components compose?](#how-do-components-compose)
  - [How do props give a component different data?](#how-do-props-give-a-component-different-data)
- [Worked example](#worked-example)
  - [Example 1: one complete page](#example-1-one-complete-page)
- [Example 2: split the page into components](#example-2-split-the-page-into-components)
- [Example 3: make a component reusable with props](#example-3-make-a-component-reusable-with-props)
- [Example 4: compose a small dashboard](#example-4-compose-a-small-dashboard)
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

Read the [course README](../README.md), confirm the [setup guide](../SETUP.md), and open the [examples guide](../examples/README.md). This is a React-only lesson, so use the Vite playground. Run it before changing code:

```bash
cd examples/react-playground
pnpm install
pnpm dev
```

Open the local URL printed by Vite. The starter is already a working project; the point of this lesson is to change one small part at a time and observe how a page becomes a set of components.

## Why this lesson exists

A page often begins as one file because that is the easiest way to get the first result. That is a good beginning and a bad long-term plan. When the page grows, the header, navigation, main content, cards, and footer become difficult to read. Two other problems appear: the same visual idea gets copied in several places, and a change in one part accidentally affects another part.

React gives us a way to name a piece of UI and give it a boundary. That boundary is a **component**. A component is not magic markup and it is not necessarily a separate file. It is a function, class, or other React unit that describes one part of the interface and can be composed with other parts.

The best way to learn this is not to begin with a definition. We will first write a complete page, then split it, then give one component different inputs, then compose a small dashboard from the pieces. Each step answers one practical question.

## Prerequisites

You should be able to read a JavaScript function, return a value, recognize JSX elements, and run the React playground. You do not need to know state, Hooks, routing, or TypeScript yet. This lesson uses static data so that the component boundary remains visible.

## Outcomes

By the end of this lesson, you should be able to explain why a page is split into components, write a function component, pass a prop from a parent to a child, distinguish a prop from local ownership, and compose several components into a small page. You should also be able to explain why a component name begins with a capital letter and repair the common mistake of calling a component as an ordinary helper function.

## Keywords and terms

| Keyword or term | Meaning in this lesson |
| --- | --- |
| **Component** | A React unit that describes one part of a user interface and can be rendered or composed by another component. |
| **Function component** | A JavaScript function whose returned JSX describes what React should render for that component. |
| **JSX** | JavaScript syntax that lets us write a tree of UI elements using an HTML-like form. |
| **Props** | Read-only inputs supplied by a parent to a child component. |
| **Composition** | Building a larger interface by placing smaller components together. |
| **Boundary** | The named responsibility and input/output edge around a piece of UI. |
| **Children** | Content placed between an opening and closing component tag and received through the `children` prop. |

## Topics

### What problem do components solve?

A component gives a name to a part of a page. The name is useful only when it matches a real responsibility. A `Header` can own the welcome area, a `CaseCard` can own the display of one case, and a `Footer` can own the closing information. The parent page should not need to know every element inside a card to place the card on the page.

This is similar to splitting a long paragraph into sentences. The sentences are still part of the same message, but each has a smaller job. Component boundaries help a learner read, test, replace, and reuse the parts.

### What is a function component?

A function component is a function that returns JSX. The function is not called by our click handler; React calls or renders it as part of building the UI tree. Its name begins with a capital letter so JSX can distinguish a user-defined component such as `Header` from a browser element such as `header`.

A component can be completely static. It does not need state or a Hook to be a component. That matters because beginners often think a component is only an interactive widget. A static component is still valuable when it owns a coherent visual responsibility.

### Why are function components the modern default?

Function components fit ordinary JavaScript functions: they receive inputs, calculate a result, and return it. Modern React features such as Hooks are designed for function components, and function components work naturally with the Server and Client Component boundaries used by the Next.js App Router.

Class components are not useless. They remain important when reading older React code, understanding error boundaries, or migrating a legacy application. We will study the comparison later. For new code in this course, a function component is the default because it makes the data flow and modern React APIs easier to see.

### How do components compose?

Composition means a parent renders child components. The parent decides where a child belongs; the child owns the details of its own markup. The parent can compose `Header`, `Main`, and `Footer` without copying their internal elements into one giant return statement.

Composition is not the same as putting every `<div>` into its own component. A component should earn its boundary through a responsibility, reuse, independent behavior, or a meaningful test surface.

### How do props give a component different data?

Props are the parent's input to a child. If the same `StatusBadge` should display `Open` in one place and `Closed` in another, the component should receive a `label` prop instead of hard-coding one label. Props flow down. A child does not mutate its props to communicate back; later lessons will show callback props and state ownership for upward intent.

## Worked example

The following sequence is the worked example for this lesson. Each example changes one purposeful thing while preserving the visible goal.

### Example 1: one complete page

Start with one complete page. This is not bad code for a first experiment; it gives us a visible result before we introduce boundaries.

```tsx
export default function App() {
  return (
    <div>
      <header>
        <h1>Local Case Desk</h1>
        <p>Review invented case records.</p>
      </header>
      <main>
        <h2>Today's queue</h2>
        <ul>
          <li>Review access policy</li>
          <li>Test recovery flow</li>
        </ul>
      </main>
      <footer>
        <small>Training fixture only</small>
      </footer>
    </div>
  );
}
```

**Visible behavior:** the page has a heading, a queue, and a footer. Nothing is interactive yet. Notice that the page already has three responsibilities even though it is one function.

### Example 2: split the page into components

Now make one purposeful change: move each responsibility into a named component. The visible page should remain the same. That is important. We are changing the organization, not the user-facing result.

```tsx
function Header() {
  return (
    <header>
      <h1>Local Case Desk</h1>
      <p>Review invented case records.</p>
    </header>
  );
}

function Main() {
  return (
    <main>
      <h2>Today's queue</h2>
      <ul>
        <li>Review access policy</li>
        <li>Test recovery flow</li>
      </ul>
    </main>
  );
}

function Footer() {
  return (
    <footer>
      <small>Training fixture only</small>
    </footer>
  );
}

export default function App() {
  return (
    <div>
      <Header />
      <Main />
      <Footer />
    </div>
  );
}
```

**Visible behavior:** the page looks the same. The difference is in ownership: `App` composes the page, `Header` owns the welcome area, `Main` owns the queue, and `Footer` owns the training notice.

### Example 3: make a component reusable with props

The queue currently has hard-coded list items. Create a `CaseCard` that receives the title and status. The component can now be reused without copying its markup.

```tsx
type CaseCardProps = {
  title: string;
  status: 'Open' | 'Pending' | 'Closed';
};

function CaseCard({ title, status }: CaseCardProps) {
  return (
    <li>
      <strong>{title}</strong>
      <span> — {status}</span>
    </li>
  );
}

function Main() {
  const cases: CaseCardProps[] = [
    { title: 'Review access policy', status: 'Open' },
    { title: 'Test recovery flow', status: 'Pending' },
  ];

  return (
    <main>
      <h2>Today's queue</h2>
      <ul>
        {cases.map((item) => (
          <CaseCard key={item.title} title={item.title} status={item.status} />
        ))}
      </ul>
    </main>
  );
}
```

The example includes TypeScript because this repository's starter is typed. The React idea is still JavaScript: `CaseCard` receives an object and returns JSX. TypeScript additionally records the allowed fields and status values. It does not check data fetched from a server at runtime; validation remains a separate boundary.

**Visible behavior:** the same two cases appear. The new capability is not a new visual effect. It is the ability to render the same component with different data while keeping the markup in one place.

### Example 4: compose a small dashboard

Now compose the pieces into a page that has a reusable card, a summary, and an empty-state branch. This is the first example where the component boundaries help us reason about a small application.

```tsx
type Case = {
  id: string;
  title: string;
  status: 'Open' | 'Pending';
};

function Summary({ count }: { count: number }) {
  return <p aria-live="polite">{count} cases need review.</p>;
}

function CaseList({ cases }: { cases: Case[] }) {
  if (cases.length === 0) {
    return <p>No synthetic cases are waiting.</p>;
  }

  return (
    <ul>
      {cases.map((item) => (
        <li key={item.id}>
          <strong>{item.title}</strong> <span>{item.status}</span>
        </li>
      ))}
    </ul>
  );
}

export default function App() {
  const cases: Case[] = [
    { id: 'case-001', title: 'Review access policy', status: 'Open' },
    { id: 'case-002', title: 'Test recovery flow', status: 'Pending' },
  ];

  return (
    <main>
      <h1>Local Case Desk</h1>
      <Summary count={cases.length} />
      <CaseList cases={cases} />
    </main>
  );
}
```

The `Summary` component does not need to know where the count came from. `CaseList` owns the decision about the empty state because that decision belongs to rendering the list. `App` owns the fixture and composes the page. In a later lesson, a data-access boundary may provide the cases, but the UI responsibilities can remain the same.

## Line-by-line explanation

| Code line | What it teaches |
| --- | --- |
| `function CaseCard({ title, status }: CaseCardProps)` | Declares a function component and destructures its read-only props. The component's responsibility is one list item. |
| `type CaseCardProps = ...` | Names the input contract. The union means the example accepts three deliberate status values, not arbitrary text. |
| `<strong>{title}</strong>` | Inserts the prop value into JSX. Curly braces enter JavaScript expression mode; React renders the string as text. |
| `<CaseCard key={item.title} ... />` | The parent composes the child. `key` helps React identify list items; it is not passed as an ordinary prop. |
| `const cases = [...]` | `Main` owns the local fixture in this static example. Later, a server or state boundary may own the data. |
| `if (cases.length === 0)` | The list component owns the empty-state decision because it knows what “no list items” means. |
| `<Summary count={cases.length} />` | The parent calculates a value and passes it down. The child does not reach into the parent's data. |
| `<CaseList cases={cases} />` | The parent composes the list and provides its input. The data direction is parent to child. |

## Execution trace

1. React evaluates `App` and creates the local `cases` array with two objects.
2. `App` passes `cases.length`, which is `2`, to `Summary`.
3. `Summary` receives `{ count: 2 }` and returns the sentence “2 cases need review.”
4. `App` passes the same array to `CaseList`.
5. `CaseList` checks `cases.length === 0`. The condition is false, so it maps the two records.
6. Each record becomes one `<li>`. The stable `id` would be the preferred key for records whose titles may change.
7. React combines the returned trees and places the visible result in the browser.

If the array becomes empty, only the `CaseList` branch changes: the user sees “No synthetic cases are waiting.” The summary still says `0 cases need review`; that wording could be improved in a later accessibility and UX lesson.

## Prediction experiment

Before running the experiment, predict the result of changing the fixture to `const cases: Case[] = []`. Which component changes its output? Does `Summary` still render? What should a user hear if a screen reader is watching the live summary? Run the change, then restore the two-record fixture.

Next, change the title of one case but keep its `id`. Predict which visible text changes and whether the list identity should change. Keep a written answer before checking the browser.

## Broken example and repair

**Broken version:** rename `CaseCard` to `caseCard` and render `<caseCard title="Review access policy" status="Open" />`.

React treats lowercase JSX names as intrinsic browser elements. It does not look for your JavaScript function in the same way it looks for the capitalized `CaseCard` component. The repair is to use a capitalized component name and JSX tag:

```tsx
function CaseCard({ title, status }: CaseCardProps) {
  return <li><strong>{title}</strong> <span>{status}</span></li>;
}

<CaseCard title="Review access policy" status="Open" />;
```

A second likely mistake is to mutate `cases` inside `CaseList` or let a child change a prop. Props are read-only inputs. If the child needs to request a change, the parent will provide a callback; that is a later state-and-events lesson.

## Guided practice before independent work

First, copy Example 1 and run it unchanged. Second, create only `Header`, `Main`, and `Footer`, keeping the visible page the same. Third, replace one hard-coded list item with `CaseCard` and pass a different status. Fourth, empty the array and describe the empty state before running it. Only then start the independent exercises.

## Project application

Build a local **case queue card** in the React playground. It must display a title, status, owner label, and one empty state using invented data. Keep the fixture in the parent component. Make the card reusable, give the status a meaningful text label, use a stable key, and write a short note explaining why the parent owns the array while the child owns one item’s markup.

## Independent exercises

### Level 1 — Questions and first steps

1. What is a React component? Answer in one sentence.
2. How do you make a function component? Point to the function in Example 1.
3. What is the difference between a normal JavaScript function and a component function?
4. How small can a component be? Name one small part of a page.
5. Can a button or an input field be a component? Explain why.
6. Run Example 1 and write down the three visible parts of the page.

### Level 2 — Build small components

7. Make a reusable `Button` component. Render the word `Open` inside it.
8. Make a reusable `InputField` component with a label and an input.
9. Make an alert component with one parent `<div>` and one child `<p>`.
10. Split the page into `Header`, `Main`, and `Footer` without changing what the user sees.

### Level 3 — Use the components

11. Render two `CaseCard` components with different titles and statuses.
12. Show a clear message when the case list is empty. Write one sentence naming which component displays that message.

## Finish line

You are ready for the next lesson when you can draw the component tree, explain the direction of data flow, recreate the page from a blank file, repair the lowercase-component mistake, and explain why a component boundary is useful without claiming that every `<div>` deserves its own component.

## References

- [React Learn: Thinking in React](https://react.dev/learn/thinking-in-react)
- [React Learn: Passing Props to a Component](https://react.dev/learn/passing-props-to-a-component)
- [React Learn: Your First Component](https://react.dev/learn/your-first-component)
- [React Reference: JSX](https://react.dev/reference/react)
