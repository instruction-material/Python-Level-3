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
  They verify twenty-four authored coding starters remain incomplete, import quietly, run with
  exercise feedback, and match their reference function signatures. Reference
  checks cover boundaries, large integer conversion, search behavior, recursion,
  literal strings, bracket-only validation, console input/state, and AM2/AM3
  integer domains, list generation, ordered modes and mutation contracts. Separate
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
- Placeholder role folders awaiting assignment-specific material: 10
- Distinct migrated starter/reference pairs awaiting contract verification: 8
- Authored incomplete coding starter/reference pairs verified by tests: 24
- Supplied-code analysis starter/reference pairs verified by tests: 1
- Mathematical worksheet/reference pairs reviewed separately: 1
- Active source-like files excluding archive: 171

Notes: active source-like files exclude `_archived-unlinked/`. Placeholder role folders are structural markers only; they do not contain assignment source yet.

The authored material now covers the six initial algorithm packs plus AM1's
three console review projects, AM5's five recursion/string projects, the first
check-in's running-sum project, both AM6 analysis projects, and six sorting packs
from AM8 through AM11. Three previously migrated practice pairs now also have
authored callable scaffolds and checked AM2/AM3 assignment contracts. Completed
references remain separate from coding starters. Analysis inputs are supplied
code or a worksheet, not arbitrary unfinished algorithms.

The Big-O starter intentionally has no Python file: its README is the complete
mathematical task. Counting Python files alone would incorrectly label it as a
missing coding implementation. The other 10 placeholder roles still require
assignment-specific review. The remaining 8 migrated pairs have distinct content but
have not all passed these authored-pack correctness checks.

See SOURCE_PACK_REVIEW.md for evidence, role distinctions, and the open list.
