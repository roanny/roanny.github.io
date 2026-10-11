# roanny.github.io

The operator's personal CV and portfolio, served at https://roanny.github.io/ by GitHub Pages from the root of `main`. The repository is `roanny/roanny.github.io`, under his personal GitHub account rather than the Coabana organization; it is a site, not a product, and nothing consumes it. Every push to `main` is live within minutes, so a change a visitor would see never lands without the operator's word. `googlede4b53d1c977dbfc.html` (the Search Console verification) is never renamed or removed.

## The tree

- `index.html` — the whole site: content, styles, the `i18n` dictionaries and the script. No framework, no build step.
- `404.html` — the themed not-found page, self-contained.
- `favicon.svg`, `favicon-32.png`, `og-image-2.jpg` (the 1200×630 social card), `robots.txt`, `sitemap.xml`; `.nojekyll` makes Pages serve the tree as it is.
- `.github/scripts/check_site.py`, `.github/htmlvalidate.json` — the site's own gates.

## Previewing and checking

- Preview: `python3 -m http.server 8000`, then http://localhost:8000 (`?lang=en|es` and `?theme=light|dark` force the language and the theme).
- The gates, as CI runs them: `npx --yes html-validate@11.16.0 --config .github/htmlvalidate.json index.html 404.html`, `python3 .github/scripts/check_site.py i18n`, `python3 .github/scripts/check_site.py sitemap`.
- A content change updates `lastmod` in `sitemap.xml`. A changed social card takes a new filename (`og-image-<n>.jpg`) and the three references in `index.html` (`og:image`, `twitter:image`, the JSON-LD `image`), because LinkedIn, WhatsApp and X cache a card by its URL; LinkedIn's Post Inspector refetches it once it is live.

CI (`Validate`, `.github/workflows/ci.yml`) refuses invalid HTML in either page, an `i18n` key missing from either language, a malformed sitemap, a changed shared block under `.claude/`, on pull requests a commit subject over 72 characters or with a trailing period, and a commit author other than the one below.

## Conventions

- **Language.** The content is English by default with Spanish, by audience: the text lives in the `en` and `es` dictionaries of the `i18n` object at the end of `index.html`, with the same keys, and each translatable element carries `data-i18n="<key>"`; the English default in the HTML stays aligned with `en`. The working documents — README, this file, the rules, code comments and commit subjects — are English; Spanish text quoted from the content stays Spanish.
- **Design.** The design tokens (palette, type, chips, buttons, motion) mirror `DESIGN.md` of `Coabana/coabana.github.io`, the canonical source, copied by hand into the `<style>` of `index.html`.
- **Commits.** The whole subject line at most 72 characters, no trailing period. Authored as `Roanny Lamas <roannylamaslopez@gmail.com>`, set in this checkout's local git config; the employer's address is never used here.
- **Landing.** Work on a branch, open a pull request, and land it on `main` by fast-forward (`git push origin <branch>:main`) once `Validate` is green on its head. No merge commits, no force push, no remote-ref deletion.

## Where the rules live

- `.claude/rules/git-hygiene.md` — the landing, commit, ruleset and authorization rules in full.
- `.claude/rules/markdown-docs.md` and `.claude/rules/rules-discipline.md` — the shape of the working documents and of a rule file.
- `.claude/CLAUDE.md` — the rest of the repository's instructions and their index.

As a site it carries no `docs/specs/`, no `CONTRIBUTING.md` and no release.
