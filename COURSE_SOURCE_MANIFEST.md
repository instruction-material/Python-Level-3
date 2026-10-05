# Course Source Manifest

Canonical source repository: `Python-Level-3`

## Mapped Catalog Courses

- `python-level-3`: Python Level 3
- `java-without-graphics`: Java without Graphics
- `java-with-graphics`: Java with Graphics

## Verification Gate

- Run `./verify-course-source.sh` from this repository root before treating the source pack as ready.
- The verification gate checks for this manifest, the source backlog ledger, source-like files, removed Replit metadata, and any repo-specific readiness files.
- Project-specific unit tests or build commands should still be run inside individual project folders when a project includes its own test harness.
- The gate also runs the standard-library algorithm pack tests in `tests/`.
  They verify 42 authored coding starters remain incomplete, import quietly, run with
  exercise feedback, and match their reference function signatures. Reference
  checks cover boundaries, large integer conversion, search behavior, recursion,
  literal strings, bracket-only validation, console input/state, and AM2/AM3
  integer domains, list generation, ordered modes and mutation contracts. Five
  check-in packs add bounds-only searches, actual bubble-sort early cutoff,
  sort directions/pass traces, shared two-sort timing inputs and validated
  character-file read/write workflows. Three hybrid reviews preserve five
  supplied problem functions, checked against a frozen original-source fixture.
  Three record/file packs add stable keyed leaderboards, alternating-line
  dictionaries and the original Juni Latin character rule with optional
  punctuation. Tests preserve the original records and six input-file copies,
  check deliberate malformed-record policies and protect file aliases.
  Three interactive search packs add exact feedback/input domains, explicit
  confirmed/inferred/win/loss/cancel/error states and deterministic secret tests.
  Shared search queries, untimed warm-ups, fresh copies, measured medians and
  timing-boundary/mutation checks replace the incomparable legacy experiment.
  Separate
  analysis tests verify fourteen supplied functions without answer comments and
  a ten-prompt mathematical worksheet with a separate reference key.

## Active Catalog Targets

| Folder |
| --- |
| `AM-Check-In-1` |
| `AM-Check-In-1-Additional-Project` |
| `AM-Check-In-2` |
| `AM-Check-In-2-Additional-Project` |
| `AM-Check-In-3` |
| `AM-Check-In-3-Additional-Project` |
| `AM1-Juni-Assistant` |
| `AM1-Junian-Language-Verifier` |
| `AM1-Mad-Libs` |
| `AM10-Merge-Sort` |
| `AM11-Quicksort` |
| `AM11-Sorting-Comparison` |
| `AM12-Crazy-Name-Tags-Printer` |
| `AM12-File-IO-and-Dictionaries` |
| `AM12-Juni-Latin-with-File-IO` |
| `AM13-Conways-Game-of-Life` |
| `AM13-Two-Player-Conways` |
| `AM14-Tic-Tac-Toe-AI` |
| `AM14-Tic-Tac-Toe-AI-Test` |
| `AM14-Tic-Tac-Toe-AI-with-Forks` |
| `AM14-Tic-Tac-Toe-UI` |
| `AM2-Functions-Practice` |
| `AM2-Lists-Practice` |
| `AM3-Python-Fundamentals-Problem-Set` |
| `AM4-Binary-Converter` |
| `AM4-Fibonacci-Numbers` |
| `AM4-Recursive-Exponents` |
| `AM4-Recursive-Factorials` |
| `AM5-Parentheses-Validator` |
| `AM5-Recursive-Cascade` |
| `AM5-Recursive-Palindrome-Checker` |
| `AM5-Recursive-Sum-and-Max` |
| `AM5-Substring-Generator` |
| `AM6-Big-O-Analysis` |
| `AM6-Function-Analysis` |
| `AM6-Linear-Search` |
| `AM7-Binary-Search` |
| `AM7-Number-Guesser` |
| `AM7-Reverse-Number-Guesser` |
| `AM7-Runtime-Comparator` |
| `AM8-Insertion-Sort` |
| `AM8-Selection-Sort` |
| `AM9-Baseball-Analytics` |
| `AM9-Bubble-Sort` |

## Source Inventory

- Active project folders: 44
- Active linked folders: 44
- Archived inactive/support folders: 8
- Wrapper project folders: 44
- Placeholder role folders awaiting assignment-specific material: 0
- Distinct migrated starter/reference pairs awaiting contract verification: 0
- Authored incomplete coding starter/reference pairs verified by tests: 42
- Hybrid coding reviews with preserved supplied problem functions: 3
- Supplied-code analysis starter/reference pairs verified by tests: 1
- Mathematical worksheet/reference pairs reviewed separately: 1
- Active source-like files excluding archive: 198

Notes: active source-like files exclude `_archived-unlinked/`. Placeholder role folders are structural markers only; they do not contain assignment source yet.

The authored material now covers the six initial algorithm packs plus AM1's
three console review projects, AM5's five recursion/string projects, the first
check-in's running-sum project, both AM6 analysis projects, and six sorting packs
from AM8 through AM11. Three previously migrated practice pairs now also have
authored callable scaffolds and checked AM2/AM3 assignment contracts. Five
check-in packs now have complete briefs and 27 incomplete callable exercises,
while preserving the five original tracing/optimization problem bodies.
The remaining three migrated pairs now have complete briefs and 12 incomplete
callable exercises, with the punctuation helper explicitly optional. That
milestone had 80 native methods; original synthetic player records/file bytes
remain unchanged. The interactive follow-up adds three full briefs and thirteen
matching incomplete callables, including one optional recursive-search helper.
That milestone had 101 methods; guessing outcomes and comparable measured search
batches are independently checked without claiming arbitrary guesses guarantee
a win or one benchmark proves Big-O. Crazy Name Tags adds four core incomplete
callables and one optional separate-file callable, with complete file/console
contracts. Seventeen new methods bring the native suite to 118; independent literal
character oracles, exact UTF-8/LF writes, preserved sample blobs, validation before
overwrite, quiet imports, cancellation and optional alias checks are covered.
Completed
references remain separate from coding starters. Analysis inputs are supplied
code or a worksheet, not arbitrary unfinished algorithms.

The Big-O starter intentionally has no Python file: its README is the complete
mathematical task. Counting Python files alone would incorrectly label it as a
missing coding implementation. No active linked coding placeholder remains. All 42 coding/review pairs now have
authored learner contracts and separate checked references. This does not certify
unrelated legacy files, other course packs or the broader site/course audit.

See SOURCE_PACK_REVIEW.md for evidence, role distinctions, and the open list.

## Tic Tac Toe follow-up

Four required stages now have complete learner briefs and 59 matching incomplete
callables across their self-contained packs. Learners carry forward their own
verified board/UI code; the stages add random legal play, basic tactical rules,
reproducible evaluation and fork creation/defense. Quiet imports, finite legal
selection, validation, fresh state and explicit cancellation replace unsafe
console and experiment side effects. The original default X/O roles, random
starting-order purpose and basic priority are retained. The advanced reference
repairs unconditional multiple-fork edge selection with deliberate forcing or
fork-removal defenses. Evaluation is seeded, bounded and scoped to tested policies.

All 167 native methods pass. The 23 new methods use bitmask oracles over 19,683
symbol boards, enumerate 10,956 reachable board/turn states from both starts,
check candidate/move/state mutation contracts, replay console wins/draws/cancels,
and verify counts/rates/seeded traces. All-legal-opponent game trees with every
random fallback find basic-policy losses when moving second and no losses for
the revised fork reference from an empty board, for either mark and starting
order. This result is specific to the defined reference policy and 3x3 rules,
not arbitrary positions, learner implementations or non-terminating callbacks.
The gate inventories 209 source-like files including archive, 198 active.
