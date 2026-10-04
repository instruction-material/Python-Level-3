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

Twenty-seven placeholder starters remain open. Review each against its actual
course brief and separate reference; analysis-only tasks may need a worksheet
or executable analysis harness rather than an arbitrary algorithm template.
Do not treat this six-pack correction as completion of the full source audit.
