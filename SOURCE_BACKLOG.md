# Source Backlog Ledger

Current status: no unlinked source folders remain at the active top level.

On 2026-05-14, 7 top-level folders that were not linked by the live course catalog were moved to `_archived-unlinked/`. That archive is retained for source-history review, optional-bank recovery, or future promotion, but it is not part of the active public course surface.

On 2026-06-18, `AM13-Priority-Queue` was moved to `_archived-unlinked/` because the migrated project contains a Java `PriorityQueue` reference implementation, not Python Level 3 source. It remains available for source-history review, but it should not be linked from the active Python course unless a Python-native starter and solution are authored.

Promotion rule: restore a folder from `_archived-unlinked/` only after the live course text names where it belongs, whether it is starter or solution material, and how the student or tutor verifies it. Update `COURSE_SOURCE_MANIFEST.md` and the live catalog link in the same change.

## Starter implementation backlog

On 2026-10-04, review of public revision
`d3610afbe355ce2ab3fa6747ef438bce2c83c3be` confirmed 33 of the 44 catalog-linked
starter folders contained no Python source. The first six now have distinct
incomplete exercises: AM4 Recursive Factorials, Recursive Exponents, Fibonacci
Numbers, Binary Converter, AM6 Linear Search, and AM7 Binary Search.

The accompanying reference checks preserve the one-based Fibonacci convention
and Boolean search contracts. Binary conversion now uses integer division to
avoid losing digits above floating-point precision. Reference demonstrations
run only when invoked directly, keeping imports suitable for self-checks.

The follow-up source review adds nine incomplete console/recursion starters,
the original fourteen function-analysis examples without answer comments, and
a complete ten-prompt Big-O worksheet with a separate justified reference key.

Reference corrections cover empty running sums, empty sums/maximum semantics,
consistent bracket-only validation, stable contiguous substring output, explicit
literal palindrome behavior, blank/exact assistant commands and session state,
and case-insensitive language rules with specific failure messages.

Sixteen placeholder roles remain open. Review each against its actual course
brief and separate reference. A mathematical worksheet is intentionally not a
coding starter; do not invent source only to satisfy a file-count check.
See SOURCE_PACK_REVIEW.md. These repairs do not complete the full source audit.
