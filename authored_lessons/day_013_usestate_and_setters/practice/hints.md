# Day 013 hints: useState and setters

Use these after attempting the the numbered exercises in this lesson. Return to the [lesson](../day_013_usestate_and_setters.md) when a result surprises you.

1. One direct update from one snapshot is the easy case; record the current value before the click.
2. Both direct expressions read the same render snapshot. Write the arithmetic each expression performs.
3. A functional updater is a function that receives the latest pending value. Do not call it yourself.
4. The immediate log reads the old render's snapshot; inspect the next visible render for the requested value.
5. Copy the current object first, then overwrite only the named field.
6. Remove the spread deliberately and observe which field disappears; then restore the copy.
7. Each input reads one field and sends a new object that preserves the other field.
8. Store the initial object in one place so reset returns to a known contract.
9. For three updates, write both sequences as arithmetic from the initial snapshot and as a functional queue.
10. Your acceptance check should fail if the second field is lost.
11. A JavaScript property setter runs when a property is assigned; a React state setter requests a later render. They solve different problems.
12. The state owner coordinates the pending values. A reducer would be useful only if named transitions are becoming clearer than several setters.
