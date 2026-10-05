# Crazy Name Tags Printer

Required AM12 project: separate a string transformation, its output format and
file writing. Complete the single-file version first. The three-file version is
an optional extension. Python 3 and its standard library are sufficient.

## Start and finish

Confirm importing this starter folder into the site's Python IDE, or work in a
copy of `starter/` locally. The import contains `main.py` and this complete brief;
no input file is needed. Initial Run prints an exercise reminder and creates no
files. Replace each required `NotImplementedError` with an implementation, test
the helpers, then replace the guarded reminder with a call to `main()`.
Run locally with `python3 main.py` from the working folder, or enter the name in
the IDE's console input when prompted. Reopen generated `output.txt`, compare
its actual contents, save/export the project and reopen the saved work.
Completed references remain separate in `solution/`.

Predict a small name before coding. Trace indexes and file closure with a course
facilitator when useful, then independently test another name. Do not copy the
reference as the attempted starter.

## Four core tasks

1. `name_variations(name)` returns a fresh tuple of three strings: the literal
   name, characters at zero-based indexes 0, 2, 4, ... and all characters in reverse
   order. Accept strings, including empty strings. Preserve case, spaces and tabs
   literally. Each Python Unicode code point counts as a character; combining
   sequences are not kept together as visual graphemes and no normalization is
   performed. Non-strings, embedded CR/LF and text that cannot encode as UTF-8
   raise `ValueError`.
2. `format_tags(name)` returns text without opening files. Use the same name
   domain. Put each character on its own line, in the three variation orders.
   Append one LF (`\n`) after every character and one additional LF after each
   section, including the last. Empty names therefore produce exactly three
   LF characters. A literal space is a space on a line, not a blank separator.
3. `write_tags(name, path="output.txt")` validates the whole name, formats the
   text and validates the destination before opening it. A destination is a
   nonempty UTF-8 encodable string or `os.PathLike` returning such text, without
   NUL; invalid destinations raise `ValueError`. Accept `pathlib.Path`. Preserve
   literal path whitespace. Open in `"w"` mode with `encoding="utf-8"` and
   `newline="\n"`, using a context manager. Valid writes deliberately overwrite
   the destination and return `None`; validation failures preserve existing
   output. Ordinary filesystem errors propagate. Parent folders are not created.
   `w+` adds unneeded reading access. An I/O failure after opening can leave a
   truncated or partial file; this task does not promise rollback.
4. `main(path="output.txt", input_fn=None, output_fn=None)` validates destination
   and callbacks before prompting. Callbacks must be callable or `None`; invalid
   configuration raises `ValueError`. Resolve `None` to built-in `input`/`print`
   at call time. Prompt once with `What is your name? ` and call `write_tags`.
   Return a fresh dictionary with exactly `status` and `path` (destination text).
   Status is `written` on successful output, `invalid` on invalid name, `failed`
   on an output `OSError`, or `cancelled` on input `EOFError`/`KeyboardInterrupt`.
   Report the corresponding outcome without claiming success on failure.
   Invalid names and input cancellation open no output. There is no reserved
   quit command: the literal name `quit` is valid. Other callback errors propagate.
   Imports must not prompt, open files, print or run the project.

## Independent checkpoints

For `Juni`, predict the three strings first. The complete core output has this
Python representation, including the final section separator:

```text
'J\nu\nn\ni\n\nJ\nn\n\ni\nn\nu\nJ\n\n'
```

Check empty input (`'\n\n\n'`), one character, an odd-length name, repeated letters,
mixed case, a literal space/tab and Unicode. Compare bytes using UTF-8, including
the final newline. With temporary files, check deliberate overwrite, invalid
name preserving prior output, invalid path, a missing parent and cancellation.
Explain why validation happens before opening and how a context manager closes
the file even if writing raises. Keep existing personal files out of experiments.

## Optional separate-file task

Only after the core works, implement
`write_separate_tags(name, paths=("output1.txt", "output2.txt", "output3.txt"))`.
Validate the complete name and all three destinations before any file is opened.
`paths` must be a list or tuple of exactly three valid destinations. Reject
identical/equivalent paths and symlink/hardlink aliases with `ValueError`, since
three different variations need three distinct files. Inspection errors propagate.
Use the core name domain and UTF-8/LF context-managed overwrite policy. Each file
contains one variation, one LF per character, without core section separators;
empty names give three empty files. Return `None`. Validation errors preserve all
outputs; later filesystem failures can leave earlier files written or a partial
file. No transactional rollback is promised. The core `main()` does not select
this extension automatically. Verify all three outputs independently.
