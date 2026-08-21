# Day 077 solution guide: File uploads, metadata, and storage boundaries

Use this guide only after attempting the numbered exercises in [the lesson](../day_077_file_uploads_metadata_and_storage_boundaries.md). It reviews the decisions for **File uploads, metadata, and storage boundaries**; it is not a copied answer key.

## Review checkpoints

1. The submission states the problem and connects it to file uploads, metadata, and storage boundaries rather than offering only a definition.
2. The unchanged example runs and its visible or returned result is recorded for a local synthetic upload validator and authorized download response.
3. The trace identifies the owner and boundary: browser file input versus server validation, storage, and access policy.
4. The normal change isolates one input and preserves the rule for What is an upload boundary?.
5. The boundary case for Why validate size and type on the server? has deliberate behavior and an explanation.
6. The failure `Trust the filename extension, accept unlimited bytes, and serve a file without checking ownership, then repair all three boundaries.` is reproduced, diagnosed, and repaired with the smallest meaningful change.
7. The repair keeps the responsibility that the lesson owns: Files are larger and more ambiguous than ordinary text fields, and a filename is not a security policy.
8. The quality requirement for Where should file bytes live? is visible in code or project structure.
9. The assertion or test fails when the important behavior is removed and passes after the repair.
10. The local application demonstrates a local synthetic upload validator and authorized download response with synthetic data and a named owner.
11. The limitation avoids claiming that a build, screenshot, or one passing test proves production readiness.
12. The review note is reproducible and records evidence, residual risk, and the boundary browser file input versus server validation, storage, and access policy.

## Self-assessment

Mark the work **ready** only when you can explain why the implementation works, reproduce the result from a clean checkout, and describe what it still does not cover. If your answer is “the framework does it,” return to the execution trace and identify the actual boundary where the behavior is decided.
