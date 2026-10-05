# Conway's Game of Life

This required core project has a complete learner contract in
[starter/README.md](starter/README.md). Import the incomplete [starter](starter)
after confirmation. The separate [solution](solution) is an import-safe reference
for review after an attempt. Both roles contain the unchanged original patterns.

The first Conway project teaches a finite synchronous Boolean automaton. The
two-player project builds on it with retained ownership, paired legal edits,
alternating turns and explicit extinction/cancellation outcomes. They are
distinct required capstones rather than optional duplicates.

Original material is frozen in Git at
`efd0cdfb190a9110ec1a160786e13f724a60153f`:
`AM13-Conways-Game-of-Life/solution/main.py` and
`AM13-Conways-Game-of-Life/solution/AM13-Conways-Game-of-Life.py`.
The legacy-named file is now a quiet compatibility entry point to sibling
`main.py`, so there is one active reference behavior. It resolves its own sibling,
not an unrelated globally imported `main`.

The supplied files remain byte-for-byte original in Git. This revision authors
the previously missing scaffold and clarifies contracts. It repairs import-time
execution, hardcoded next-grid dimensions and ambiguous run termination.
Default five-update execution is an explicit bounded inspection mode; the original
continuous purpose remains selectable with generations=None and a chosen delay.

Run `PYTHONDONTWRITEBYTECODE=1 bash verify-course-source.sh` from the repository
root. Bounded independent rule oracles and real file/console tests verify these
packs; they do not prove unrestricted game termination or the broader site audit.
