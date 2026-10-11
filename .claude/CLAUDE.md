@../AGENTS.md

# roanny.github.io — Claude Code

`AGENTS.md`, imported above, says what the site is, how it is previewed and checked, and the conventions a change respects; this file adds what holds only for a Claude Code session.

## Serving and landing

Two rulesets guard `main`: "Protect main branch" (24806684: no deletion, no force push, linear history; no bypass) and "Require Validate" (24807145: `Validate` green; the repository admin bypasses it so the operator can fix by hand — a session never does, `git-hygiene.md`). There is no release and no `/release`: the fleet's `release` shared block does not apply, and a landing that changes the pages is a deploy (`git-hygiene.md`).

## The one coupling

The `DESIGN.md` that `AGENTS.md` § Conventions names is `coabana-site`'s (checkout `coabana/`), whose `CLAUDE.md` says the same from its side. Before stating what that file holds now, read it or verify it with the `contract-checker` agent.

## Index

- `.claude/rules/git-hygiene.md` — linear history, the 72-character subject, the commit author, no force push or remote-ref deletion, landing as a deploy, the two rulesets, Dependabot, the round authorization, the deny floor (every session).
- `.claude/rules/rules-discipline.md` — what a rule file may hold (fleet shared block).
- `.claude/rules/markdown-docs.md` — the shape of the Markdown working documents (fleet shared block).
- No commands and no agents: there is no release and no code to review beyond the page's script.

`.claude/settings.json` is hand-written: `allow` holds the daily work (the git and `gh` reads, the branch push, the preview server, the three gates), `deny` holds the fleet's groups A–C; there is no group D.
