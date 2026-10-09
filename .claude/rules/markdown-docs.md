---
description: Markdown docs formatting — full-width prose and precision in references
paths: ["**/*.md"]
---

The site's content is English and Spanish by audience; this rule governs the working documents, which are English.

<!-- markdown-docs:shared begin -->
## Line width

In `.md` files, **prose and bullets go full width**: one logical line is one physical line, with no manual hard wrap at ~80 columns. The editor or viewer does the visual wrapping. Hard wrapping at ~80 columns applies **only to code files** and to code fragments embedded in the document inside a fence; documentation prose is never wrapped by hand.

**Why**: manually wrapping prose produces noisy diffs — changing one word reflows the whole paragraph — complicates merges, and produces the mix of short and long lines that reads as inconsistent. Full width keeps the diff honest, one logical line changed being one change, and delegates the wrapping to the renderer.

## What to always preserve

When reflowing or editing, never touch:

- **Code fences** (blocks delimited by triple backticks) and their contents — code does respect its language's width.
- **GFM tables** (`| … |`) — each row is one line.
- **YAML frontmatter** (the `---` … `---` block at the start of the file).
- **List structure** — one bullet (`- ` / `N. `) per logical item; an item's continuations join its bullet.
- **Blockquotes** (`>`), **headings** (`#`) and **horizontal rules** (`---`).

## Precision in references

Documentation here names exact things all the time: secrets, environment variables, service accounts, flags, roles, files. Imprecision in those references misleads, above all when one name resembles another — a secret against the environment variable it is mounted as is the usual pair. Two rules follow.

**No ad-hoc abbreviations.** Use the full, readable name, not an invented contraction: the project number is written `project_number`, **not** `projnum` nor `project-num`. Standard acronyms defined at first use (SA = service account, ADC = Application Default Credentials, OTel) are acceptable; contractions that save characters at the cost of clarity are not.

**No prefix wildcard for a finite set.** A prefix wildcard loses precision and can mislead — it is how the name of a secret gets read as the name of the variable it is mounted as. When the set is **known, finite and the exact names matter**, enumerate the names. A wildcard is for a genuinely open or extensible family, where the full list adds nothing and the immediate context defines it unambiguously; never as a shortcut for a finite, specific set.

**Why**: a reader copies and applies literally what the document says, and a wildcard sends them looking for a name that exists nowhere.
<!-- markdown-docs:shared end -->
