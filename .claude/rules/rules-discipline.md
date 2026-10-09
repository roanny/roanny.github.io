---
description: Rules content discipline — what a rule may hold (invariants, constraints, patterns) and what it may not (history, status, changelog fragments)
paths: [".claude/**", "CLAUDE.md"]
---

<!-- rules-discipline:shared begin -->
A rule file is loaded when Claude reads a file its `paths:` frontmatter matches; a rule file with no `paths:` is loaded at the start of the session. Either way the whole body is then paid for in context on every turn that follows, so what is in it has to earn the place.

The drift this exists to stop is specific: after a fix, the tempting thing to write into the rule is the **history of the change** rather than the **invariant it left behind**. That turns a rule into a second changelog — duplicating what `CHANGELOG.md` and `git log` already hold, and growing with nothing pushing back.

## A rule may contain

- **Invariants** — what must always or never be true.
- **Constraints** — bounds the work has to respect, and why.
- **Patterns** — the shape a solution takes here.
- **Decisions**, so they are not re-litigated — including designs deliberately rejected, which is what stops them coming back a third time.
- **Pointers** to where the authoritative answer lives — a constant, a test module, a gate, a command that computes the list.

## A rule must not contain

- Commit SHAs, dates, or release history. That is `git log` and `CHANGELOG.md`.
- Status labels — "done", "pending", "new in the last release". A rule describes the standing state, not a moment in it.
- Changelog fragments or migration narratives.
- Enumerations that drift: test names, counts, file inventories. Name the command or the constant that produces the list instead.
- **Anything already enforced mechanically.** If a test, a schema, a gate or CI rejects it, the rule only needs to say where the enforcement lives. A rule restating a guard is a second copy free to disagree with the first, and the copy in prose is the one nobody re-runs.
- **Anything another rule already owns.** Point at the rule that owns the subject rather than repeating it here — the same discipline this file asks for.

## Self-check before adding a line

1. Will this still be true in three months without editing?
2. Does it change what someone would *do*, or is it background?
3. Is it already enforced by a test, a schema, a gate or CI?
4. Could it live closer to what it governs, as a comment where the constraint applies?

If the answers are no, no, yes, or yes — leave it out. When editing a rule after a change, write the end state and delete the narration of the journey.

## Keep the index honest

This repository's `CLAUDE.md` indexes these rules and must name every one of them; it should not restate their content. When a rule is added or changes scope, update that line rather than copying the rule into it. An index that silently omits a file teaches readers the directory is smaller than it is.
<!-- rules-discipline:shared end -->
