# Source-pack review

Baseline: public main 9293c232ec7d8b318956df516836d7d4d4d04449.
The 44 active starter folders then contained 17 Python starters and 27 structural
placeholder roles. This follow-up reviews the assignment purpose, not only the
presence of a file. All original folder and source filenames are preserved.

## Implemented and checked in this follow-up

| Role | Packs | Evidence |
| --- | --- | --- |
| Incomplete console exercises | AM1 Mad Libs, Fictional Language Verifier, Command Assistant | Separate learner entry-point TODOs; reference input/output, rules, state, and exit regressions |
| Incomplete recursion exercises | AM5 Cascade, Palindrome, Parentheses Validator, Sum and Max, Substring Generator | Empty/boundary cases, strict bracket balance, literal comparison, contiguous/deduplicated stable output |
| Incomplete core review exercise | Check-In 1 Additional Project | Forward/reverse running sums; empty input stops; remains core |
| Supplied code to analyze | AM6 Function Analysis | Fourteen original function bodies, no complexity-answer comments; primitive-operation model and count checks |
| Mathematical worksheet | AM6 Big-O Analysis | Ten complete prompts, assumptions, blank answer spaces, and separate justified reference key; no artificial Python implementation |

Coding starters remain incomplete and initial Run gives a reminder. They do not
import references or learner answers. Analysis code is the problem input, not a
completed classification. The mathematical worksheet is readable without an IDE.

The standard-library suite checks the six previous algorithm pairs as well.
The pre-sorting milestone had 22 test methods. The reference
algorithm checks are separate from the learner starter folders. This is evidence
for these authored packs, not certification of every migrated source file.

## Sorting follow-up

Six more authored, incomplete starter packs now cover selection, insertion,
bubble, merge, quicksort, and Sorting Comparison. Original function names and
source filenames are preserved. New-list, in-place and consuming contracts are
explicit, including empty/singleton identity. References are import-safe.

Selection Comparison's incorrect minimum scan is repaired. The consuming
selection variant keeps the first equal minimum, preserving tied-record identity.
Merge uses left-side tie handling and indexed linear merging; quicksort documents
pivot values and allocating recursion. Optional shuffling documents its mutation
and randomness boundaries and handles empty input.

Sorting Comparison now uses fresh copies of shared, seeded input shapes, checks
every result, and reports only measured median timings. Generation, copying,
oracle computation, validation and printing are outside the timing boundary.
Default runs use sizes 100/300 and three repeats; explicit guards bound learner
experiments to five sizes, 2000 items each, and ten repeats. Basic bubble sort is
labeled rather than being confused with the early-exit variant.

The sorting milestone had 31 methods. Fifteen sorting variants are checked on all 364
numeric lists of length 0-5 over {-1, 0, 1}, plus former selection failures and
larger ordered cases. Tests independently check mutation/identity, stable record
labels where promised, merge/split, pivot values, shuffles, actual early-exit
comparison counts, timing boundaries, shared copies, medians, and bounds.
These tests prove the authored numeric contracts, not unbounded-input performance
or the correctness of unrelated legacy pairs.

## Migrated fundamentals follow-up

Three previously migrated pairs now have explicitly incomplete callable starters,
complete learner briefs and quiet reference imports:

| Pack | Preserved purpose and corrected contract |
| --- | --- |
| AM2 Functions Practice | Five required iterative review functions; optional factorial/Hailstone challenges remain separate from later recursion projects. Exact integer digit/Hailstone arithmetic, nonnegative exponent/factorial domains and a bounded transition cap are checked. |
| AM2 Lists Practice | Loop-generated twenty positive evens match the original task. Original two-list/nested functions remain, min/max reject empty lists, and max_list preserves its explicit empty-inner-list skip policy. |
| AM3 Fundamentals Problem Set | All sixteen original tasks and function names remain. Tied modes are ascending, case/empty/integer domains are stated, and only swap_min_max mutates its input. |

The suite now has 45 methods. Fourteen added methods verify all 32 starter
signatures/bodies and exercise reminders, independent numeric/string oracles,
all 364 small integer lists, distinct-number permutations, ordered frequencies,
fresh output identity, rejected domains and exact bounded Hailstone behavior.
The former large-integer case has 412 terms rather than the rounded result 55.
Digit counting also handles integers beyond the default string-conversion digit
limit without float arithmetic. The reference's actual large input and bounded
oracles are tested; this is not a proof of general Hailstone convergence or of
unbounded performance.

That milestone checked twenty-four authored coding pairs, one supplied-code
analysis and one worksheet. Eight distinct migrated pairs then awaited full
contract verification; ten genuine coding placeholder roles remain.
Source-file counts are inventory, not correctness evidence.

## Check-in follow-up

Five previously migrated pairs now have self-contained learner briefs and 27
intentionally incomplete callable exercises. Three main reviews are hybrid
analysis/coding packs: the five original strangeFunction, weirdFunction,
function1, function2 and bubbleSort bodies remain problem inputs, not answers.
A frozen fixture identifies source revision
6ed2caf76313b92163e3c450f6bd7192e518b9a5 and tests their exact syntax trees.

| Pack | Checked assignment contract |
| --- | --- |
| Check-In 1 | Middle/second strings, one-based Lucas numbers, recursive bowling pins, literal backspaces and the original random push/pop walkthrough. Small practice domains make recursion costs explicit. |
| Check-In 2 | Boolean searches use bounds rather than copying or validation scans; first-one search is logarithmic. Selection remains descending; insertion remains ascending/stable. Separate keys contain exact original expressions and corrected pass traces. |
| Check-In 2 Additional | Two ascending sorts use shared random/sorted/reversed multisets, fresh copies and measured medians. Preparation, copying, oracle, validation and printing stay outside timing; bounded small defaults remain distinct from AM11's five-sort experiment. |
| Check-In 3 | Original bubble baseline stays available; the improved sort actually stops after one no-swap pass. Indexed stable merge and ordered pivot-value partitions preserve inputs. Unicode character files retain literal spaces, deliberate record errors and separate answers. |
| Check-In 3 Additional | ASCII file sorting returns fresh lists, retains duplicates and rejects invalid records with line numbers. Validation precedes output opening; source bytes survive malformed input and path/symlink/hardlink output aliases. |

The suite now has 63 methods. Eighteen added methods check incomplete signatures,
quiet imports and direct-run reminders; all 3280 small backspace strings; all
364 small numeric lists; every binary boundary through length 128; and indexed
virtual million-item sequences that forbid scanning, copying and slicing.
Independent checks cover stable record identity, actual baseline/early-cutoff
comparison counts, pass traces, all small merge pairs, literal file bytes,
empty/malformed/missing files, alias protection, timing boundaries and medians
from injected clocks. Reference demonstrations run with bounded defaults.

Twenty-nine authored coding/review pairs, one separate supplied-code analysis
and one worksheet are checked. Three migrated pairs and ten coding placeholders
remain open. The native gate inventories 191 source-like files including archive,
180 excluding archive. These counts and bounded tests do not certify unrelated
legacy files, unrestricted performance, or the broader site/course audit.

## Open placeholder roles

The remaining 10 folders below were inspected for source shape and dependencies,
but their algorithms, instructions, asset loading, and interactive flows remain
unverified. They are not marked ready merely because a solution file exists.

| Folder | Assignment family | Next verification |
| --- | --- | --- |
| AM7-Reverse-Number-Guesser | Interactive binary-search game | Bounds, feedback validation, and termination |
| AM7-Runtime-Comparator | Search timing experiment | Comparable inputs and timing boundaries |
| AM7-Number-Guesser | Interactive guessing game | Guess limits, invalid input, and deterministic test setup |
| AM12-Crazy-Name-Tags-Printer | File I/O | File paths, output shape, independent input data |
| AM13-Conways-Game-of-Life | Console simulation | Rule oracle, board edges, local input assets, termination |
| AM13-Two-Player-Conways | Console simulation | Ownership rules, turn input, local assets, duplicate legacy files |
| AM14-Tic-Tac-Toe-UI | Console game | Input bounds, legal moves, win/draw states |
| AM14-Tic-Tac-Toe-AI | Console game | Strategy, legal moves, copied-board mutation |
| AM14-Tic-Tac-Toe-AI-Test | Strategy experiment | Deterministic adversaries and honest performance claims |
| AM14-Tic-Tac-Toe-AI-with-Forks | Console strategy game | Fork logic, legal moves, termination |

The remaining 3 distinct migrated pairs also need their own correctness review.
The broader site audit still includes other courses, supported environments,
original-source identity reconciliation, delivery-purpose distinctions, and
bridge extension language alignment. None is closed by this source-pack gate.
