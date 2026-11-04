---
description: Text or a file is searched for.
dependencies: []
---

Text is searched with ripgrep, `rg`, in the repository or flow directory the work is in: `rg -n 'text' <directory>`, with `-F` for a literal string and `-l` for file names alone. One repository answers in under 10 ms, and every repository under /git in about 20 s. The home directory holds a million and a half files and costs a minute of disk for every search.

A type filter narrows the search: `rg -t rust 'text'`, `rg -g '*.nix' 'text'`; `rg --type-list` names the types.

rg reads the ignore files: `.gitignore`, and `.ignore` for rules of its own. It skips hidden files and does not follow symlinks, so `target/`, `.git/` and `result` stay out.

Tracked files alone: `git grep -n 'text'`. A file by name: `fd -g 'name' <directory>`. Code by its structure: `ast-grep`.

A file inside a Nix input is searched at that input's own store path, taken from the flake: `nix flake metadata --json`, or `nix eval` of the input's outPath.
