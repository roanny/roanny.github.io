Loads in every session: it carries the authorization block, which has to be present before the first file is read.

# Git hygiene

## History and landing

- **Linear history.** A branch lands on `main` by fast-forward, `git push origin <branch>:main`, once `Validate` is green on the pull request's head SHA. No merge commits; `gh pr merge` is denied, because it and the UI button collapse or rewrite the branch's commits.
- **Only a green head reaches `main`.** The ruleset "Require Validate" (24807145) requires a green `Validate` but lets the repository admin bypass it, so the operator can push a fix by hand; sessions push with his credentials and inherit that bypass, so for them this rule is the gate, not the server. A session pushes to `main` only the head of a pull request whose `Validate` is green, by the fast-forward above.
- **Commit subjects.** The whole first line at most 72 characters, no trailing period; measure it before the push (`printf '%s' "$subject" | wc -m`), because correcting a pushed subject is a force push. CI's "Commit subjects" step reads every commit a pull request adds.
- **Commit authors.** Every commit is authored as `roannylamaslopez@gmail.com`, which this checkout's local git config carries (`AGENTS.md` § Conventions); CI's "Commit authors" step refuses any other author but Dependabot's and GitHub's own. The admin bypass of "Require Validate" means a direct push of the operator's with another address is not stopped, only shown red after the push; a session never relies on that.
- **No force push, in any spelling** — `--force`, `-f`, `--force-with-lease`, a `+refspec` — on any branch.
- **A landing can be a deploy.** GitHub Pages publishes `main` within minutes of every push to it: a landing that changes what a visitor sees is a deploy of the public site, and § Authorization says whose word that takes.
- **Remote branches.** A session deletes the branches it pushed once their pull request has landed or was closed as superseded with nothing on the branch missing from `main` or from the pull request that replaced it; a branch another author pushed, or one whose work is found nowhere else, is not the session's. The ruleset "Protect main branch" (24806684: deletion, non-fast-forward, linear history; no bypass) is the floor on `main`. There are no tags here.

## Dependabot

The standing authorization of 2026-09-23 covers this repository's Dependabot heads (`github-actions` only): a patch, minor or digest head lands by the same fast-forward without a word from the operator, once `Validate` is green on that head and the upstream diff between the two pinned SHAs has been read. A head cut from an older `main` gets `@dependabot rebase` first. There is no code beyond the page's own script, so no senior pass applies; a head touches only `.github/`, so the republish it triggers leaves the site unchanged. A major takes the operator's word.

## Authorization

<!-- authorization:shared begin -->
**A session works without stopping for the operator.** It commits, pushes its branch, opens the pull request and reads its checks with `gh`, fixes what the gate or a validated review finding asks, lands by this repository's convention, deletes its own merged or superseded branches, and goes on to the next item of its commission. It needs no approval for a plan inside a commission, and no word for a reversible act.

**On its own, under green gates and written in the round's ledger:** a tag and a release; a deployment or an apply in DEV that changes no IAM and no secret, with the rollback target noted; a promotion to STA once DEV is green and the end-to-end check has passed; a new dependency or a minor bump that an agreed spec or an upstream review justifies; the artifact pipeline's cross-checkout write; an edit under `.claude/` taken from a list the workspace verified.

**The operator's, by his typed word in this terminal:** a secret or a credential in any form; IAM; organisation or repository settings; anything in PRO; a force push, a history rewrite or the deletion of a tag; a major version; spending beyond a budget he approved; agreeing a spec; the constitution. A relayed "yes" never counts for these, and the `deny` floor refuses most of them whatever a message says.

**What is his is queued, not asked one by one.** The session goes on with everything that does not depend on it and presents the queue once — one card, the recommended option first — when the rest is done or nothing else can move.

**The sandbox is a seat belt, the `deny` floor is the boundary.** When the sandbox blocks a tool the task needs, the session reruns that one command outside it and says so in its report. A deny is never routed around, inside the sandbox or outside it, and a rerun is never the way for the session to read, print or copy a secret.
<!-- authorization:shared end -->

### This repository

- **Landing convention**: a branch, a pull request, and the fast-forward `git push origin <branch>:main` once `Validate` is green on the pull request's head SHA (§ History and landing). A head that touches only `.github/` or `.claude/` leaves the published pages unchanged, and the session lands it on its own; Dependabot heads land under § Dependabot.
- **Gate**: the three commands of `AGENTS.md` § Previewing and checking — `npx --yes html-validate@11.16.0 --config .github/htmlvalidate.json index.html 404.html`, `python3 .github/scripts/check_site.py i18n`, `python3 .github/scripts/check_site.py sitemap` — which `Validate` runs with the shared-block, commit-subject and commit-author steps.
- **The operator's here, because it cannot be undone from this repository**: a landing that changes what a visitor sees, because GitHub Pages publishes it within minutes and LinkedIn, WhatsApp and X cache what they fetched (the public site is this repository's PRO); the session prepares the pull request green and queues the landing. Renaming or removing `googlede4b53d1c977dbfc.html`, the Search Console verification.

## The deny floor

`.claude/settings.json` holds it, groups A–C; the file is the reference. In place of the denied resets, use `git stash`, `git revert` or `git checkout -- <path>`.
