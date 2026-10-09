# roanny-site

The operator's personal CV and portfolio, served at https://roanny.github.io/. The repository is `roanny/roanny.github.io`, under his personal GitHub account rather than the Coabana organization. It is a site, not a product: nothing consumes it, and it names no fleet product.

## The tree

- `index.html` — the whole site: content, styles, the `i18n` dictionaries and the script. No framework, no build step.
- `404.html` — the themed not-found page, self-contained.
- `favicon.svg`, `favicon-32.png`, `og-image.jpg` (the 1200×630 social card), `robots.txt`, `sitemap.xml`, `googlede4b53d1c977dbfc.html` (Search Console verification; never removed).
- `.nojekyll` — Pages serves the tree as it is, without Jekyll.
- `.github/scripts/check_site.py`, `.github/htmlvalidate.json` — the site's own gates, run by `Validate`.

## Editing and previewing

- Text lives in the `i18n` object at the end of `index.html`: two dictionaries, `en` and `es`, with the same keys; each translatable element carries `data-i18n="<key>"`, and the English default in the HTML stays aligned with `en`.
- Preview: `python3 -m http.server 8000`, then http://localhost:8000 (`?lang=en|es` and `?theme=light|dark` force the language and the theme).
- The gates by hand, as CI runs them: `npx --yes html-validate@11.16.0 --config .github/htmlvalidate.json index.html 404.html`, `python3 .github/scripts/check_site.py i18n`, `python3 .github/scripts/check_site.py sitemap`.
- A content change updates `lastmod` in `sitemap.xml`.

## Serving

GitHub Pages serves the root of `main`; a push to `main` is live in 1–2 minutes. Two rulesets guard `main`: "Protect main branch" (24806684: no deletion, no force push, linear history; no bypass) and "Require Validate" (24807145: `Validate` green; the repository admin bypasses it so the operator can fix by hand — a session never does, `git-hygiene.md`). There is no release and no `/release`: the fleet's `release` shared block does not apply, and a landing that changes the pages is a deploy (`git-hygiene.md`).

## The one coupling

The design tokens (palette, type, chips, buttons, motion) mirror `DESIGN.md` of `coabana-site` (`Coabana/coabana.github.io`), the canonical source, copied by hand into the `<style>` of `index.html`; `coabana-site`'s `CLAUDE.md` says the same from its side. Before stating what that file holds now, read it or verify it with the `contract-checker` agent. The JSON-LD names Coabana as the affiliation, and a call to action links to https://coabana.github.io/.

## Language

The content is English by default with Spanish, by audience; the working documents — README, this file, rules, code comments and commit subjects — are English. Spanish text quoted from the content stays Spanish.

## Git identity

Commits are authored as the operator's global git config has it: `Roanny Lamas <roanny.lamaslopez@viajeseci.es>`.

## Index

- `.claude/rules/git-hygiene.md` — linear history, the 72-character subject, no force push or remote-ref deletion, landing as a deploy, Dependabot, the round authorization (every session).
- `.claude/rules/rules-discipline.md` — what a rule file may hold (fleet shared block).
- `.claude/rules/markdown-docs.md` — the shape of the Markdown working documents (fleet shared block).
- No commands and no agents: there is no release and no code to review beyond the page's script.

`.claude/settings.json` is hand-written: `allow` holds the daily work (the git and `gh` reads, the branch push, the preview server, the three gates), `deny` holds the fleet's groups A–C; there is no group D.
