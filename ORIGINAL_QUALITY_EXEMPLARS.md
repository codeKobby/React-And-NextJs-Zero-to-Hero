# Original 30 Days of React teaching exemplars

Sources reviewed on 20 August 2026:

- [Day 8: States](https://github.com/Asabeneh/30-Days-Of-React/blob/master/08_Day_States/08_states.md)
- [Day 2: Introduction to React](https://github.com/Asabeneh/30-Days-Of-React/blob/master/02_Day_Introduction_to_React/02_introduction_to_react.md#2-why-react)

## What the original States lesson does well

The Day 8 lesson is approximately 513 lines and 451 lines of lesson content. Its table of contents is intentionally small: States, What is State?, How to set a state, Resetting a state using a JavaScript method, Exercises, and three exercise levels. The lesson does not create headings for every possible teaching requirement; the headings correspond to the actual conceptual progression.

The explanation begins with the ordinary meaning of “state” and gives familiar states such as happy or sad, on or off, present or absent, and full or empty. It then connects the everyday meaning to React: state is data whose change causes a component to render again. This is a motivation-first bridge rather than a definition dropped into a vocabulary table.

The lesson builds the concept through successive runnable examples. It first shows a class component with initial state and reads `this.state.count`. It then adds one button and `this.setState`, adds a second button, refactors the handlers into named methods, and then applies the same idea to a cat/dog example. Each step is a small change from the previous one, so the learner can see the reason for each new line.

The lesson includes a boilerplate directory in the repository and points to live runnable material. It makes the reader imagine the visible result (“you will see zero”), then explains what the next change accomplishes. The code is not merely a final answer; it is a sequence of repairs and extensions.

The exercises are grouped into Levels 1, 2, and 3. The lesson does not force every day to have an identical number or type of exercise. It uses simple state changes first, then asks for small applications such as a light switch or a button that changes text, and finally asks for richer combinations such as a controlled interaction. The exercise difficulty grows with the concept.

## What the original Introduction lesson does well

The introduction lesson uses prerequisites, concrete JSX, and a plain-language explanation before discussing why React. The “Why React?” section answers a learner question: React is popular, has a growing community, and is compared with Vue using popularity evidence. Even though the historical popularity screenshots are dated, the teaching move is valuable: answer why the learner is studying the tool before asking them to memorize its vocabulary.

The introduction lesson also uses a visible component example with header, main, and footer elements. It shows a complete small composition before abstracting the idea. The learner can see what React is for, what a component looks like, and how pieces combine.

## Principles to carry into the rebuilt course

1. **Headings must follow the learner's questions and the concept's natural progression.** A large TOC is not evidence of depth.
2. **Begin with motivation and familiar experience.** Explain the problem and why the concept exists before naming APIs.
3. **Build examples incrementally.** Start with the smallest runnable case, then make one purposeful change at a time.
4. **Show the visible result.** Tell the learner what they should see and why the output changes.
5. **Use boilerplate intentionally.** A starter is useful when the lesson explains what the learner owns and what the scaffold is doing.
6. **Use exercises as a progression.** Start with mechanical confidence, move to a guided application, then offer synthesis or stretch work.
7. **Do not force irrelevant sections.** A first setup lesson may need commands and orientation but no artificial coding exercise. A state lesson needs runnable interaction and state-specific exercises.
8. **Teach fewer ideas more deeply when necessary.** Coverage is subordinate to learner understanding.
9. **Modernize the technology without copying shallow structure.** Replace obsolete APIs with React 19 and Next.js 16 equivalents while preserving the original explanatory rhythm.
10. **Review humanly.** Ask whether a beginner could teach the concept back, predict the result, change the example, and recover from an error.

## Direct comparison with the current generated course

The current Day 012 state lesson has 173 lines, but much of that length comes from navigation, generic admonitions, and repeated framework-neutral prose. Its topic sections say that state is “the idea you must be able to point to in code” and repeatedly instruct the learner to identify inputs and outputs, but they do not explain state snapshots, render timing, functional updaters, batching, or the difference between a local variable and React state in a concrete sequence.

Its worked example is only two lines: `const [count, setCount] = useState(0);` and a button with `setCount(count + 1)`. That is too small to teach the concept in context because it omits the component, import, visible layout, event timeline, and the result of multiple clicks. The execution trace is a universal four-step description that could be pasted into a lesson about data fetching, routing, or authentication.

The current Day 006 component lesson has the same pattern. It names “what is a component,” “why function components are the modern default,” composition, and reviewability, but the topic prose is generic and the example is only a `Badge` and `App` function. It does not first show the problem of a growing page, then split the page into meaningful components, then explain what changed and why. The original course's complete header/main/footer composition is a stronger starting point because it shows a visible page before and after decomposition.

The most important defect is therefore not that the current lessons have too few headings. It is that the generator's source data contains only one short code snippet, one output sentence, and one repair sentence per lesson. The renderer cannot produce original-quality teaching from that input. The redesign must store a real teaching sequence per lesson: motivation, concept explanation, incremental examples, expected visible behavior, line-specific trace, controlled failure, guided practice, and appropriately sized exercises. Uniform “12 exercises” must not be used as a substitute for deciding whether a lesson needs no coding, a short mechanical task, a guided mini-project, or a larger synthesis.
