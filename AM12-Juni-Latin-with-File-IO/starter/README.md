# Juni Latin: a staged text-file translator

This core project combines reading, a character rule and writing. Keep the original
input_no_punctuation.txt and input_punctuation.txt. The latter is for the optional
extension. This is the supplied Juni Latin rule, not general Pig Latin or a
dictionary-based translator: there are no known/unknown-word lookups.

## Core assignment

Implement the five core TODO helpers; translate_punctuation is optional. Initial
Run gives a reminder. Imports must not open files, print or run translation.

1. translate(word) receives a whitespace-free string. For a nonempty token, move
   its first character to the end and append ay. An empty token returns the empty
   string. Preserve the characters' original case; do not capitalize the new
   first character or lowercase the moved one. Unicode characters work too.
   Non-string or whitespace-containing input raises ValueError. The helper treats
   all token characters literally; use the punctuation-free file for core work.
2. read_lines(path="input_no_punctuation.txt") reads UTF-8 with a context manager.
   Return a list of physical lines without their CR/LF delimiters. Accept LF/CRLF
   and an unterminated final line; retain blank lines. Empty files give [].
   Propagate normal file/decoding errors; do not modify the input.
3. translate_lines(lines, punctuation=False) receives a list of delimiter-free
   strings. Split each line into whitespace-separated tokens, translate each,
   then join them with single spaces. Deliberately remove leading/trailing space
   and normalize repeated spaces/tabs, but keep one output line per input line,
   including blank lines. Return a fresh list without changing lines. Invalid
   containers, non-string records or CR/LF inside a record raise ValueError;
   delimiter errors identify the line number. punctuation must be a Boolean.
4. write_lines(lines, path="output.txt") validates the entire list using those
   same record rules before opening output. Write UTF-8, one LF newline after
   every record, without trailing token spaces; [] produces an empty file.
   Return None. Valid runs deliberately overwrite output; invalid records must
   leave an existing output unchanged.
5. translate_file(input_path="input_no_punctuation.txt", output_path="output.txt",
   punctuation=False) rejects input/output aliases with ValueError, including
   identical paths, equivalent paths, symlinks and hardlinks. Read and translate
   the whole source before opening output; retain the input bytes. Missing,
   undecodable or invalid input must leave an existing output unchanged. Return
   the translated list. Ordinary output I/O failures still propagate.
6. After completing core TODOs, call translate_file() under the direct-run guard
   in place of the reminder. Run from starter with Python 3, or confirm importing
   main.py and the original files into the site's Python IDE. Reopen output.txt,
   check the line/token policy and save/export the workspace.

## Optional punctuation extension

Implement translate_punctuation(word), then select it only when punctuation=True.
Preserve the leading and trailing punctuation clusters around a translated body.
Supported edge characters are Python's string.punctuation plus the curly quotes
“ ” ‘ ’ and ellipsis …. A punctuation-only or empty token remains unchanged.
Characters inside the body, including straight or curly internal apostrophes,
remain in the body and follow the same first-character rotation. This does not
promise language-aware contraction handling or preservation of arbitrary internal
punctuation at its old numeric character index.

Run the extension separately with input_punctuation.txt and output_punctuation.txt,
passing punctuation=True. Read that input anew; do not reuse the core file's lines
or a closed output handle. Core completion does not require the extension.

## Work and check

Predict a small token and a two-line fixture before execution. Discuss one trace
with a course facilitator, then independently check empty/single-character words,
case, Unicode, blank lines, repeated whitespace and absent final newline. Optional
checks add clustered edge punctuation, punctuation-only tokens and the supplied
curly apostrophe in wasn’t. Explain intentional whitespace changes. Test malformed
data and aliases in temporary directories, not by overwriting the supplied files
or existing personal output. Completed reference code remains separate in solution.
