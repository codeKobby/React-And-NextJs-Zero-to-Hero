# React and Next.js lesson standard

A lesson is complete only when a beginner can explain the idea, understand why it exists, run a meaningful example, predict a change, make the change, recover from a failure, and apply the idea to an appropriately sized project. A long document, a large table of contents, or a successful type check is not evidence of teaching quality.

The course builds on the teaching rhythm demonstrated by the original [30 Days of React States lesson](https://github.com/Asabeneh/30-Days-Of-React/blob/master/08_Day_States/08_states.md) and [Introduction to React lesson](https://github.com/Asabeneh/30-Days-Of-React/blob/master/02_Day_Introduction_to_React/02_introduction_to_react.md). Modern React 19 and Next.js 16 replace obsolete APIs where necessary, but the course preserves the original strengths: motivation before terminology, small changes between examples, visible outcomes, boilerplate that the learner can inspect, and exercises that grow from mechanical confidence to synthesis.

## A lesson's teaching arc

### 1. Begin with the learner's problem

The opening must answer a real question. Why does a page need components? Why does a value need state instead of a local variable? Why does a form need controlled input? Why does Next.js distinguish Server and Client Components? Use an everyday analogy or a concrete broken page when it genuinely clarifies the problem. Do not begin with a dictionary definition or a list of APIs.

### 2. Establish prerequisites and the starting fixture

Name what the learner already needs and what they do not need. Point to the exact starter or boilerplate directory. Explain which files are scaffolding, which files the learner should edit, which command runs the example, and what the learner should see. A setup lesson may reasonably focus on installation and orientation; it must not receive an artificial coding task merely to satisfy a numeric quota.

### 3. Teach one concept through a sequence of small changes

A concept lesson should normally contain several connected examples. Start with the smallest runnable case. Show its visible result. Add one purposeful change. Explain why that change is necessary. Run the new version and compare the result with the previous version. Continue until the learner can see the concept in a meaningful mini-application.

For state, a strong sequence might move from a static value, to a local variable that fails to update the screen, to `useState`, to a named event handler, to a functional updater, and finally to a small interaction with an empty or boundary state. For components, it might move from one complete page, to a `Header`, `Main`, and `Footer`, to props, to composition, and then to a decision about ownership. The exact sequence must fit the concept.

### 4. Explain code that actually exists

Every important line must be explained according to its real behavior. Do not describe a setter as “declares behavior,” a component as merely “returns a UI description,” or an arbitrary line with a universal sentence. Explain imports, inputs, state snapshots, event handlers, closures, renders, asynchronous work, cleanup, server/client boundaries, and visible output with the vocabulary appropriate to that day.

The execution trace must follow a concrete example. It should show the initial values, the event or call, the update request, the next render or result, and the relevant ownership boundary. If a framework detail is not observable in the starter, label it as a model or inspectable fact rather than pretending the trace proved it.

### 5. Include a deliberate failure that teaches the concept

The broken example must be a likely beginner mistake, not a random syntax error. State what the learner should predict, show the failure or incorrect behavior, identify the violated assumption, and repair the smallest meaningful cause. For a state lesson, a local variable that changes without causing a render is useful. For a controlled form, an input whose value cannot change is useful. For Next.js, putting a browser-only API in a Server Component is useful.

After the repair, rerun the normal case and at least one boundary case. Explain what remains untested.

### 6. Guide before asking for independence

Guided practice should be a partial imitation of the worked sequence: change one value, then one rule, then recreate the smallest version from a blank file or a clearly bounded starter. The independent task should not introduce three new concepts at once. State the starting file, expected behavior, acceptance criteria, and the concepts the learner is allowed to use.

### 7. Match practice to the lesson

Practice is not a fixed 12-question template. The file may contain no coding task for a purely conceptual orientation day, a short set of mechanical questions for a setup day, a progressive Level 1/Level 2/Level 3 sequence for a state or component day, or a larger project checklist for a capstone day. Every task must be specific to the lesson and have a reason for being there.

When exercises are present, prefer this progression:

| Stage | Learner action | Appropriate evidence |
| --- | --- | --- |
| Confidence | Run, label, trace, or modify the smallest example | Command, output, annotated code, or prediction |
| Control | Change one value, event, prop, state rule, or boundary | Before/after behavior and explanation |
| Repair | Reproduce and fix the likely mistake | Error or incorrect result, cause, smallest repair |
| Application | Build a small feature with a named owner and boundary | Runnable local fixture, test, and visible behavior |
| Synthesis | Combine the day's ideas without hiding complexity | Short project, comparison, or design explanation |

Hints should unblock the next thought, not replace it. Solutions should show the decision and acceptance criteria, not merely repeat a generic checklist.

### 8. Use modern technology deliberately

React-only lessons use the React playground when framework behavior would obscure the concept. Next.js lessons use the App Router starter when routing, server rendering, data access, caching, streaming, styling, authentication, or deployment is itself the subject. Tailwind CSS, shadcn/ui, `src/` layout, Route Handlers, Server Actions, and `proxy.ts` must be introduced because the learner needs them for the project, not because every lesson must mention every tool.

A lesson must distinguish JavaScript runtime behavior, React rendering behavior, and Next.js server/framework behavior. It must distinguish a JavaScript property setter from a React state setter, and an optimistic Proxy redirect from authoritative server authorization.

### 9. End with evidence and a sensible finish line

The finish line must say what the learner can now explain and do, what command or visible behavior proves the local work, and what remains outside the lesson's scope. A successful build is not proof of accessibility, authorization, security, performance, or production readiness.

## Required page structure

Every substantive lesson should contain a persistent table of contents, a meaningful start-here link, prerequisites, outcomes, Keywords and terms, learner-question Topics, motivation, a runnable example or an explicit explanation of why the day is conceptual, expected output or visible behavior, a concrete line-by-line explanation when code is present, a concrete trace, a prediction experiment, a likely broken example and repair, guided practice, appropriate independent work, project application when relevant, a finish line, and references.

The validator checks the presence of navigation and sections. Human review must additionally ask whether each paragraph, code sample, exercise, and heading earns its place by helping the learner understand the day's concept.
