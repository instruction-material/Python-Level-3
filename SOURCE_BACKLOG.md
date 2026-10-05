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

The sorting follow-up adds six incomplete starter packs for AM8-AM11 and checks
fifteen sorting variants, explicit mutation/identity/stability contracts, merge
costs, optional shuffle boundaries, and import-safe references. Sorting Comparison
now reports only checked, measured medians over fresh copies of shared input data;
it no longer prints historical guesses as results.

The fundamentals follow-up replaces three migrated comment-only starters with
32 matching, deliberately incomplete callable exercises. References repair exact
Hailstone arithmetic, twenty positive even numbers and deterministic ascending
tied modes. All sixteen fundamentals questions are present in the learner brief.
Integer domains, a practical Hailstone transition cap, empty-list policies and
mutation/case contracts are tested. Five function-review tasks remain required;
factorial and Hailstone remain optional iterative challenges before AM4 recursion.
The next check-in follow-up verifies five of the eight other migrated pairs.

The three main check-ins retain five supplied functions for tracing, complexity
analysis and optimization. Their complete briefs and two additional core review
projects now have 27 incomplete callable exercises. Reference corrections add
the missing logarithmic first-one search, remove recursive binary-search slicing,
repair the descending selection trace, implement the requested bubble early
cutoff, and distinguish readlines from word splitting. The two-sort experiment
uses all three shared input shapes and measured medians with fresh copies.
Character-file contracts preserve meaningful spaces, reject malformed records
deliberately, validate before overwriting, and protect input/output aliases.
All 63 native test methods pass, including original-body preservation, independent
bounded oracles, mutation/identity and exact file-byte regressions.

Three migrated pairs still need assignment-specific verification:
AM9-Baseball-Analytics, AM12-File-IO-and-Dictionaries and
AM12-Juni-Latin-with-File-IO. These, plus ten coding placeholders, remain open.

Ten placeholder roles remain open. Review each against its actual course
brief and separate reference. A mathematical worksheet is intentionally not a
coding starter; do not invent source only to satisfy a file-count check.
See SOURCE_PACK_REVIEW.md. These repairs do not complete the full source audit.
