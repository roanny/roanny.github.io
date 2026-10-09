# roanny.github.io

The professional CV and portfolio of **Roanny Lamas López** (Data Engineer · Google Cloud), published with GitHub Pages at **https://roanny.github.io/**. One hand-written HTML file in plain HTML, CSS and JavaScript, with no framework and no build step. The site is in English by default, with Spanish.

[![Validate](https://github.com/roanny/roanny.github.io/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/roanny/roanny.github.io/actions/workflows/ci.yml) [![License: Apache-2.0 (code)](https://img.shields.io/badge/license-Apache--2.0%20(code)-blue.svg)](LICENSE)

## What it does

- Presents the profile, experience, certifications, skills and contact in a single page.
- Speaks English and Spanish from one set of keys, and follows the visitor's system theme (dark by default, a light "Caribbean day" variant).
- Carries the SEO a personal site needs: canonical URL, `hreflang`, Open Graph and Twitter cards, `Person` structured data, `robots.txt` and `sitemap.xml`.

## Quick start

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## The tree

```
├── index.html        # The whole site: content, styles, i18n and script
├── 404.html          # Themed not-found page, self-contained
├── favicon.svg       # Favicon (sun over waves), with favicon-32.png as fallback
├── og-image.jpg      # 1200×630 social card (LinkedIn, WhatsApp, X previews)
├── robots.txt        # Allows indexing and points at the sitemap
├── sitemap.xml       # Site map (update lastmod on content changes)
├── googlede4b53d1c977dbfc.html  # Google Search Console verification
├── .nojekyll         # Pages serves the tree as it is, without Jekyll
├── LICENSE           # Apache-2.0, for the code only (see License)
└── .github/          # Validate (ci.yml), its scripts, Dependabot
```

## Editing the text

Everything lives in `index.html`. The bilingual text is in the **`i18n`** object of the final `<script>`, in two dictionaries (`en` and `es`) with the same keys; every translatable element carries `data-i18n="key"`. Edit the value in both languages and, for a large change, update the default (English) text in the HTML as well so the two stay aligned. CI refuses a key present in one dictionary and missing from the other, and a `data-i18n` key that either one lacks.

## Language and theme

- **Language**: detected from the browser (English otherwise), forced with `?lang=en|es`, switched with the **EN/ES** button. Only a manual choice is remembered; automatic detection is not stored.
- **Theme**: starts from the system appearance (dark otherwise), forced with `?theme=light|dark`, switched with the **🌙/☀️** button, which remembers the choice. Until the visitor picks one and while no `?theme=` is in the URL, the theme follows the system live.

## Design system

The site shares its identity with [Coabana](https://coabana.github.io/): the same Caribbean-tech palette, typefaces, chips, buttons and motion. The canonical reference for tokens and components is **[`DESIGN.md` in the Coabana site's repository](https://github.com/Coabana/coabana.github.io/blob/main/DESIGN.md)**. A token changed there is copied by hand into the `<style>` of `index.html`.

## SEO

`index.html` carries the canonical URL, `hreflang` (`en`, `es` and `x-default` through `?lang=`), Open Graph and Twitter cards with `og-image.jpg`, and `Person` JSON-LD (with the Coabana affiliation). After a content change, update `lastmod` in `sitemap.xml`.

## Development

The gates CI runs, by hand:

```bash
npx --yes html-validate@11.16.0 --config .github/htmlvalidate.json index.html 404.html
python3 .github/scripts/check_site.py i18n
python3 .github/scripts/check_site.py sitemap
```

`Validate` (`.github/workflows/ci.yml`) runs on every pull request and every push to `main`: HTML validity of both pages, the `i18n` key parity, the sitemap, the fleet's shared blocks, the commit subjects (at most 72 characters, no trailing period) and the commit authors (`roannylamaslopez@gmail.com`, Dependabot and GitHub's own). Changes land on `main` by fast-forward once `Validate` is green. Two rulesets guard `main`: "Protect main branch" (no deletion, no force push, linear history; nobody bypasses it) and "Require Validate" (a green `Validate` before a push lands; the repository admin may bypass it to push a hand fix, and `Validate` still runs on that push).

## Deployment

GitHub Pages serves the root of `main`: every push to `main` is live in 1–2 minutes. There are no releases.

## Documentation

| File | What it holds |
|---|---|
| `.claude/CLAUDE.md` | How a Claude Code session works in this repository |

## The solution

This site is not part of the Looker Developer Agent and names none of its products. It belongs to the Coabana working set as a site, beside the Coabana site, whose `DESIGN.md` is the source of its design tokens.

## License

The code — the HTML structure, CSS and JavaScript of `index.html` and `404.html`, and everything under `.github/` and `.claude/` — is licensed under Apache-2.0; see [`LICENSE`](LICENSE).

The personal data and the CV's text are not licensed: the name, contact details, profile, experience, certifications and skills, in the page, in its `i18n` dictionaries, in the structured data and in `og-image.jpg`, remain the author's, all rights reserved. The Coabana name and brand, which the page cites, are not licensed either. A fork that reuses the code replaces all of them with its own.
