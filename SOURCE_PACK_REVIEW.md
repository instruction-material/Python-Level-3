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

At the check-in milestone the suite had 63 methods. Eighteen added methods check incomplete signatures,
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

## Record/file follow-up

The last three migrated pairs now have complete learner briefs and twelve
matching incomplete callable tasks, with the punctuation helper explicitly
optional. Original filenames, ten synthetic player records, p1-p10, playerList
and compatible player_list are preserved. Six original file copies are checked
by exact SHA-256 fixtures for baseline Git LF bytes and the configured CRLF
checkout variants, retaining the unterminated final records and dictionary key
whitespace. The first Linux run exposed the Mac's core.autocrlf conversion; its
initial Mac-only fixture was corrected against the baseline Git blobs, without
normalizing arbitrary contents or changing any example/attribute file.

| Pack | Checked assignment contract |
| --- | --- |
| Baseball Analytics | Exactly Average, Home Run and RBI; validated four-field records; fresh descending names with stable input-order ties and unchanged records; adjacent bubble comparisons, quiet imports and bounded leaderboards without sleeps. Stability and nonmutation are deliberate clarified policies. |
| File IO and Dictionaries | Alternating physical keys/values, surrounding whitespace trimming, string values, valid empty values, nonblank keys, last-value-wins duplicates and line-numbered odd/delimiter errors; context-managed reading and no invented output-writing task. |
| Juni Latin with File IO | Original first-character-to-end-plus-ay rule, literal case/Unicode, explicit line/whitespace normalization and exact LF output; empty-token/file behavior, validation before output opening and path/symlink/hardlink protection. Optional edge-punctuation clusters, punctuation-only tokens and internal straight/curly apostrophes use a separately selected path. |

All 80 native methods pass. Seventeen added methods verify every new starter
signature/body, import safety, direct-run reminders, exact original assets and
guarded reference demonstrations. Independent oracles cover all 364 small keyed
rankings, duplicate-key combinations and 364 small character-rule tokens. Further
checks cover malformed records and domains, input identity, actual temporary-file
reading/writing, blank/final/CRLF records, missing/undecodable input, context-manager
closure and preservation of existing output on validation errors or input aliases.

Thirty-two authored coding/review pairs, one supplied-code analysis and one
worksheet are now checked. No distinct migrated pair remains open. Ten coding
placeholder roles remain unverified. The native gate inventories 195 source-like
files including archive, 184 excluding archive. Bounded tests do not certify
unrelated legacy references, unrestricted performance or the broader site audit.

## Interactive search follow-up

Three previously structural starters now have complete self-contained briefs
and thirteen matching incomplete callable tasks. Twelve are core tasks of their
respective assignments; the Runtime Comparator's recursive slice helper is
explicitly optional. Original project folders/filenames, original yes feedback,
1-100 interval, seven-try defaults and search function/parameter names remain.
The corrected references are separate and imports do not prompt, draw random
values, allocate workloads, print or time experiments. The original references
are retained in Git at baseline 6b7ed239bf995cc0725e71850ba6c8b83bb0629d.

| Pack | Checked assignment contract |
| --- | --- |
| Reverse Number Guesser | Required computer-led midpoint game, case/whitespace-normalized yes/above/below/quit, strict bound changes, invalid retry without consumed attempt, and distinct confirmed/inferred/contradiction/exhausted/cancelled outcomes. Inference is conditional on consistent feedback, not a false confirmation. |
| Number Guesser | Optional player-led random-secret game with signed ASCII integer/range validation, accepted-attempt counting, explicit won/lost/cancelled outcomes and deterministic secret injection. A binary strategy can find every secret within seven; arbitrary repeated guesses can lose. |
| Runtime Comparator | Required linear/iterative-binary experiment using the same multiset/targets, untimed validated warm-ups, fresh repeat copies and actual measured batch medians. Preparation, sorting, oracle, validation and printing are excluded. Original-order versus sorted hit positions are disclosed; optional sliced recursion is not benchmarked or falsely called logarithmic total work. |

Twenty-one added methods bring the native suite to 101. They verify incomplete
signatures, direct-run reminders, quiet imports without random/timing work,
all 100 default secrets and selected smaller intervals, invalid/contradictory/
cancelled/last-attempt flows, fresh outcome history and call-time callbacks.
Independent membership tests cover all 364 small lists and a virtual indexed
million-item sequence that forbids scans/slices. Injected clocks verify shared
query order, fresh copies, warm-ups, exact timer boundaries, measured medians,
mutation/wrong-result rejection, malformed configurations and finite clocks.
Real guarded default runs remain bounded; tests never assert a machine-specific
speed ratio or certify an asymptotic result from a timing sample.

Thirty-five authored coding/review pairs, one supplied-code analysis and one
worksheet are now checked. Seven coding placeholder roles remain open. The gate
inventories 199 source-like files including archive, 188 excluding archive.
The broader course, delivery-purpose and workflow audit is still incomplete.

## Crazy Name Tags follow-up

The missing AM12 starter now contains four incomplete core callables and one
explicitly optional separate-file callable. Its complete learner brief specifies
the original literal, alternate-index and reverse character orders, one LF per
character and an extra LF after each of the three core sections. Empty names
give exactly three LFs. Literal case, spaces/tabs and Unicode code points are
preserved; grapheme-aware reversal is not claimed.

The separate reference validates name/destination before opening, writes UTF-8/LF
with context-managed closure and only prompts/writes when directly invoked.
Console outcomes distinguish writing, invalid names, cancellation and filesystem
failure. The optional extension validates all three destinations and rejects
path/symlink/hardlink aliases before any write. Ordinary later I/O errors can
leave partial output; no transactional rollback is promised. The original
reference remains in Git at 2473272796d28401c2b8a3f50b472070d9272e3a; all four
original output sample blobs remain unchanged, including the historical empty
core output that is not a new expected fixture.

Seventeen new methods bring the native suite to 118. Independent character/index
oracles check all 364 small names plus literal Unicode/space/tab cases. Tests
cover matching incomplete signatures, quiet imports, direct-run reminders,
exact baseline LF/configured CRLF sample digests, real UTF-8/LF temporary files,
overwrite, validation before opening, context closure, missing paths, callback
configuration, cancellation, fresh outcomes and honest optional partial-failure
behavior. Both console entry points are exercised in temporary workspaces.

Thirty-six authored coding/review pairs, one supplied-code analysis and one
worksheet are checked. Six coding placeholders remain. The gate inventories
201 source-like files including archive, 190 excluding archive. Bounded tests
do not certify unrelated references, unrestricted performance or the site audit.

## Conway simulation and ownership follow-up

Both required Conway packs now have full learner contracts and 24 matching
incomplete callable tasks. Boolean B3/S23 uses finite nonwrapping boundaries and
synchronous fresh generations. The owned variant retains surviving owners,
uses majority births, alternates O/X independently of counts, and validates
grow-dead/kill-opponent pairs before editing. Edits precede each generation;
initial, post-edit and post-generation extinction are checked separately.
Cancellation and turn limits never manufacture a winner. Full-board automatic
passes and bounded defaults are explicit authored policies; continuous modes
retain the original purposes without promising natural termination.

All ten original input blobs remain unchanged and are copied byte-for-byte
into learner starters. Original unsafe/conflicting references remain frozen in
Git at efd0cdfb190a9110ec1a160786e13f724a60153f. Both legacy filenames now resolve
their own sibling main.py as quiet compatibility entry points.

Twenty-six new methods bring the native suite to 144. Independent exhaustive
2-by-3 Boolean and owned-board oracles cover finite rules and ownership. Real
file/console checks cover context closure, literal original assets, domain and
mutation contracts, bounded and continuous selection, legal phase order,
invalid-pair retry, each cancellation prompt, pass/win/draw/limit outcomes,
default callbacks, quiet imports and direct compatibility entry points.

Thirty-eight authored coding/review pairs, one supplied-code analysis and one
worksheet are checked. Four coding placeholders remain. The gate inventories
204 source-like files including archive, 193 excluding archive. This bounded
evidence does not certify unrestricted game termination or other course packs.

## Tic Tac Toe follow-up

The four required AM14 stages now have complete neutral learner briefs and 59
matching deliberately incomplete callable tasks. Board helpers and candidate
evaluation leave caller state unchanged. Console games preserve human X and
computer O, optional reproducible/random starts, accepted-turn alternation,
legal moves and early win/draw termination. Quit at either prompt, EOF and
input interrupts cancel honestly. Unexpected callback errors propagate. Random
selection uses a bounded legal list and validates its result. Imports are quiet.

The basic policy retains own win, opponent block, center, original corner order
and random side priorities. Both marks are configurable for comparisons. The
fork policy counts distinct threat coordinates, excludes immediate wins from
forks and adds single/multiple-fork defenses. A compulsory blocking reply must
not itself win or fork; otherwise a candidate removing all immediate opponent
forks is considered before the stated center/corner/side fallback.

Evaluation runs fresh games with copied-board strategy callbacks and one seeded
random source. Batches validate a documented 0..10000 bound; default1000 preserves
the original experiment size. Counts/rates and a first-loss trace are returned.
A zero-game batch fabricates no outcome. Standard random-opponent performance
is reported only for that policy, starting-order and seed configuration.

Twenty-three new methods bring the full native suite to167. Independent bitmask
oracles cover all19683 symbol boards; both starts produce10956 reachable board/
turn states checked for status, legal moves, candidate threats, forks and fresh
state. Actual console traces cover wins, draws, retries, cancellation at each
prompt, call-time defaults and guarded direct runs. Experiment checks cover
seeding, counts/rates, bounded legal traces, copied callback isolation and bad
strategy results. Complete game trees include every legal opponent response and
every possible random fallback. Basic policy can lose when moving second; the
revised fork reference cannot lose from an empty board for either mark/start.
This is specific to that reference policy and finite3x3 rules, not arbitrary
positions, learner code or callback termination.

All42 coding/review pairs, one supplied-code analysis and one mathematical
worksheet now have assignment-specific material. No active linked coding
placeholder remains. The source-like inventory is209 including archive/198active.
Original AM14 snapshots remain at Git baselineefd0cdfb190a9110ec1a160786e13f724a60153f;
original public helper names and default roles are preserved. Standalone stage
files let the IDE import each starter independently. This does not close the
broader course/site audit, supported environments, original-source identity,
delivery-purpose distinctions or bridge extension language alignment.
