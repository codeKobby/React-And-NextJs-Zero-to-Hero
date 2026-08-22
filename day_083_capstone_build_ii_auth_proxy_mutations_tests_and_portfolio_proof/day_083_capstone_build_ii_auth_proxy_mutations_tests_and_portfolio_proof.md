# Day 083: Capstone build II — auth, Proxy, mutations, tests, and portfolio proof

[← Previous lesson](../day_082_capstone_build_i_design_system_shell_and_database_backed_reads/day_082_capstone_build_i_design_system_shell_and_database_backed_reads.md) · [README](../README.md) · [Setup](../SETUP.md) · [Day index](../DAY_INDEX.md) · [Course index →](../DAY_INDEX.md)

## Table of contents

- [Start here](#start-here)
- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [Keywords and terms](#keywords-and-terms)
- [Topics](#topics)
  - [What does a complete vertical slice contain?](#what-does-a-complete-vertical-slice-contain)
  - [How do identity and permission reach a mutation?](#how-do-identity-and-permission-reach-a-mutation)
  - [Where does Proxy help and where does it stop?](#where-does-proxy-help-and-where-does-it-stop)
  - [What tests prove the main journey?](#what-tests-prove-the-main-journey)
  - [How do we demonstrate residual risk honestly?](#how-do-we-demonstrate-residual-risk-honestly)
- [Worked example](#worked-example)
  - [Example 1: define the proof before the feature](#example-1-define-the-proof-before-the-feature)
  - [Example 2: protect and mutate a case](#example-2-protect-and-mutate-a-case)
  - [Example 3: test the user journey and the denial](#example-3-test-the-user-journey-and-the-denial)
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

Read the [README](../README.md), [setup guide](../SETUP.md), [examples guide](../examples/README.md), and [day index](../DAY_INDEX.md). Review the architecture and first vertical slice from Day 081 and Day 082. Work with synthetic actors, records, cookies, and files only.

This is not a request to create a giant application in one sitting. It is a reviewable completion of one vertical slice: a user can open a protected case page, create a permitted case, see a useful failure for invalid or forbidden input, and provide evidence for the journey.

## Why this lesson exists

The happy path is persuasive and incomplete. A screenshot of a dashboard does not show whether a second user can read the first user's case, whether a forged cookie is accepted, whether an invalid form reaches the database, whether a failed mutation leaves stale data, or whether the build can be repeated.

A full-stack engineer demonstrates boundaries. The capstone must connect design-system UI, a route, server data access, a session or synthetic identity, authorization, a mutation, Proxy navigation, tests, and a written limitation. Each piece has a job; the proof is the chain between them.

## Prerequisites

Complete the styling, data, authentication, Proxy, authorization, testing, and deployment phases. You should have a working local starter and an architecture note with actors, assets, routes, trust boundaries, and acceptance criteria.

## Outcomes

By the end, you should be able to complete and review one protected vertical slice, show normal and denied paths, explain why Proxy is not authorization, run checks from a clean checkout, and write portfolio documentation that distinguishes evidence from claims.

## Keywords and terms

| Term | Meaning |
| --- | --- |
| **Vertical slice** | A small feature that connects UI, route, data, policy, mutation, and evidence end to end. |
| **Threat model** | A structured description of actors, assets, trust boundaries, threats, and mitigations. |
| **Acceptance criterion** | A behavior that must be true for the feature to be considered complete. |
| **Regression** | A previously working behavior that breaks after a change. |
| **Proxy** | A request navigation boundary that can redirect or continue but does not replace server authorization. |
| **Residual risk** | A known uncertainty or risk that remains after the implemented controls and tests. |
| **Portfolio evidence** | Reproducible artifacts such as commands, tests, architecture notes, and screenshots that support a claim. |

## Topics

### What does a complete vertical slice contain?

It contains a visible route, owned data, a policy decision, a mutation or read, normal and boundary UI, and evidence. If a feature has only a component and a screenshot, it is not yet a full-stack slice.

### How do identity and permission reach a mutation?

The server identifies the actor from a trusted session boundary, checks permission and ownership, validates input, and only then calls the repository or mutation. The browser may request intent; it does not choose the actor or grant itself permission.

### Where does Proxy help and where does it stop?

Proxy can redirect an obviously signed-out request and reduce unnecessary rendering. It stops before final data authority. The protected page, repository, Server Action, or Route Handler must repeat the authoritative check.

### What tests prove the main journey?

A browser test can prove that a user-visible path works with a safe fixture. Integration tests can prove the mutation contract and denial response. Unit tests can prove pure validation or policy helpers. No single level proves every production property.

### How do we demonstrate residual risk honestly?

List what was tested, what was not, which assumptions were local-only, and what production controls would still be required. “All tests pass” is evidence about the tested cases, not a universal security claim.

## Worked example

### Example 1: define the proof before the feature

Write acceptance criteria before code:

```ts
const acceptance = [
  'A signed-in synthetic actor can view only their own cases.',
  'A permitted actor can create a case with a valid title.',
  'Invalid title returns field feedback and does not mutate data.',
  'A forbidden actor cannot create or read another actor’s case.',
  'The main browser journey and denial path have repeatable tests.',
];
```

The criteria name behavior rather than implementation. They are small enough to test and strong enough to reveal a missing authorization boundary.

### Example 2: protect and mutate a case

The final mutation should have an order that a reviewer can trace:

```ts
export async function createCase(formData: FormData) {
  const input = CaseSchema.safeParse({
    title: formData.get('title'),
  });
  if (!input.success) return { ok: false, code: 'INVALID_TITLE' };

  const actor = await requireSession();
  await requirePermission(actor, 'case:create');

  const record = await caseRepository.create({
    title: input.data.title,
    ownerId: actor.userId,
  });
  revalidatePath('/cases');
  return { ok: true, id: record.id };
}
```

The code does not trust a browser owner field. It validates before mutation, derives ownership from the actor, authorizes before the repository call, and refreshes only after success.

### Example 3: test the user journey and the denial

```ts
test('an actor creates a synthetic case', async ({ page }) => {
  await signInAsSyntheticActor(page, 'analyst-a');
  await page.goto('/cases');
  await page.getByRole('button', { name: 'New case' }).click();
  await page.getByLabel('Title').fill('Review recovery flow');
  await page.getByRole('button', { name: 'Save case' }).click();
  await expect(page.getByText('Review recovery flow')).toBeVisible();
});

test('a forbidden actor cannot create for another actor', async () => {
  const response = await createCaseAs('analyst-b', { title: 'Wrong owner' });
  expect(response).toMatchObject({ ok: false, code: 'FORBIDDEN' });
});
```

The first test follows the user-visible journey. The second tests the policy boundary without requiring a browser screenshot. Both use synthetic actors and data.

## Line-by-line explanation

| Line | Meaning |
| --- | --- |
| `acceptance = [...]` | Defines behavior that can be reviewed and tested before implementation. |
| `CaseSchema.safeParse(...)` | Validates untrusted form input before the server calls the repository. |
| `requireSession()` | Identifies the actor from server-controlled session state. |
| `requirePermission(...)` | Applies the authoritative policy decision. |
| `ownerId: actor.userId` | Derives ownership from the actor, not from browser input. |
| `revalidatePath('/cases')` | Requests fresh route data after a successful mutation. |
| `signInAsSyntheticActor(...)` | Sets up a bounded test identity; it is not a production credential. |
| `getByRole` and `getByLabel` | Exercise the public accessible UI contract. |
| `toMatchObject({ ok: false, code: 'FORBIDDEN' })` | Asserts a deliberate denial contract rather than a leaked implementation error. |

## Execution trace

1. The learner defines the acceptance criteria and actor matrix before implementation.
2. A signed-in synthetic actor visits `/cases`; Proxy may allow navigation, but the server route still checks the actor.
3. The form submits a title. The mutation validates it.
4. The server derives the actor and checks permission.
5. The repository creates a record owned by that actor.
6. The route is revalidated and the visible list shows the new record.
7. An invalid or forbidden request stops before the mutation and returns a deliberate result.
8. Tests record both the successful journey and the denial, while the portfolio note records what remains untested.

## Prediction experiment

Predict what happens if the hidden owner field says `analyst-a` while the session actor is `analyst-b`. Predict whether a signed-out user can pass Proxy with a forged cookie hint. Predict whether a failing mutation should revalidate the list. Run the local synthetic cases and compare them with the acceptance criteria.

## Broken example and repair

**Broken capstone:** the demo hides the Create button for a forbidden actor and declares the feature secure. Repair the feature by keeping the server-side permission check and adding a direct mutation test for the forbidden actor. UI hiding improves experience; it does not enforce authority.

Another broken capstone tests only the happy path. Add invalid, signed-out, forbidden, ownership-mismatch, empty, and failure fixtures that fit the feature.

## Guided practice before independent work

First, write the actor and acceptance matrix. Second, run the existing read-only slice. Third, add validation. Fourth, add authorization. Fifth, add the mutation and revalidation. Sixth, add a browser journey and a denial contract. Finally, run the delivery commands from a clean checkout and record their limits.

## Project application

Complete the **synthetic case-management capstone**. It should include the Tailwind/shadcn UI, dashboard route, server data boundary, session or actor fixture, authorization, validated mutation, narrow Proxy, loading/error/empty states, tests, README architecture note, and residual-risk section. Keep external credentials and personal data out of the repository.

## Independent exercises

### Level 1 — Completion evidence
1. What is Capstone build II — auth, Proxy, mutations, tests, and portfolio proof? Answer in one sentence.
2. Write the actor, asset, route, and acceptance tables.
3. Run the existing vertical slice unchanged.
4. Record normal, empty, loading, and error behavior.
5. Verify the design-system component is keyboard-usable and labeled.

### Level 2 — Security and mutation
6. Add validation before the repository call.
7. Add session and permission checks before the mutation.
8. Add a forbidden and ownership-mismatch fixture.
9. Add a narrow Proxy and document why it is not authorization.

### Level 3 — Portfolio proof
10. Add a browser test for the main journey.
11. Add a contract test for invalid and forbidden mutation.
12. Run typecheck, lint, tests, build, and migration or seed checks as applicable.
13. Write four README headings: What it does, How to run it, What you tested, and What you did not test.

## Finish line

The capstone is complete when another learner can clone it, follow the README, run the checks, observe the main journey, reproduce a denial, inspect the policy boundary, and understand exactly which claims remain outside the local evidence.

## References

- [Next.js: Authentication](https://nextjs.org/docs/app/guides/authentication)
- [Next.js: Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
- [React: Testing](https://react.dev/learn)
- [Playwright: Writing tests](https://playwright.dev/docs/writing-tests)
