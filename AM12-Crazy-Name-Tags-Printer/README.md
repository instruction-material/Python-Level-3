# AM12 Crazy Name Tags Printer

Required single-file writing project; three separate output files are optional.
The complete learner brief and four incomplete core callables are in `starter/`.
The fifth callable is explicitly optional. `solution/` contains a separate,
import-safe reference, not learner answers to auto-import.

The original reference remains in Git at baseline
`2473272796d28401c2b8a3f50b472070d9272e3a`. Its literal character orders and extra
LF after every section, including the final section, are preserved. Validation,
UTF-8/LF output, context-managed closure and a guarded console entry point now
make the workflow deliberate and testable. Empty input is a valid three-blank-
section core output. No name trimming, case folding or Unicode normalization is
introduced.

Original `solution/output.txt`, `output1.txt`, `output2.txt` and `output3.txt` remain
unchanged. The empty historical `output.txt` is not the expected new core output;
the three optional samples show `Juni` without section separators. Generate new
files in a working copy, not over these historical samples. There are no input
assets to import.

Run `bash verify-course-source.sh` from the repository root for independent
format/domain/file/console checks. Bounded tests and preserved samples do not
certify unrelated source packs or unrestricted performance.
