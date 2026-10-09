"""The site's own cheap gates, run by `Validate` and by hand.

    python3 .github/scripts/check_site.py i18n      # en and es carry the same keys, and every key the page uses
    python3 .github/scripts/check_site.py sitemap   # sitemap.xml is well-formed and every <loc> is on the site

Errors print as GitHub annotations; the exit code is 1 on any failure.
"""

import re
import sys
import xml.etree.ElementTree as ET

SITE = "https://roanny.github.io/"


def check_i18n() -> bool:
    html = open("index.html", encoding="utf-8").read()
    block = re.search(r"^const i18n = \{\n(.*?)^\};", html, re.S | re.M)
    if not block:
        print("::error file=index.html::no `const i18n = {` … `};` block")
        return False
    ok = True
    langs = {}
    for lang, body in re.findall(r"^  (\w+): \{\n(.*?)^  \}", block.group(1), re.S | re.M):
        # A key starts a line or follows the closing quote and comma of the previous value.
        keys = re.findall(r"(?:^|['\"],)\s*([A-Za-z_]\w*)\s*:\s*['\"]", body, re.M)
        dupes = sorted({k for k in keys if keys.count(k) > 1})
        if dupes:
            print(f"::error file=index.html::{lang} repeats keys: {dupes}")
            ok = False
        langs[lang] = set(keys)
    if sorted(langs) != ["en", "es"]:
        print(f"::error file=index.html::expected the dictionaries en and es, found {sorted(langs)}")
        return False
    # Keys the page uses: every data-i18n attribute, plus the quoted keys a script picks with a ternary
    # inside `i18n[lang][…]`.
    used = set(re.findall(r'data-i18n="([^"]+)"', html))
    for lookup in re.findall(r"i18n\[\w+\]\[([^\]]+)\]", html):
        used |= set(re.findall(r"[?:]\s*'(\w+)'", lookup))
    for a, b in (("en", "es"), ("es", "en")):
        missing = sorted(langs[a] - langs[b])
        if missing:
            print(f"::error file=index.html::keys in {a} but not in {b}: {missing}")
            ok = False
    for lang in ("en", "es"):
        missing = sorted(used - langs[lang])
        if missing:
            print(f"::error file=index.html::keys the page uses but {lang} lacks: {missing}")
            ok = False
    print(f"i18n: en {len(langs['en'])} keys, es {len(langs['es'])} keys, {len(used)} used by the page")
    return ok


def check_sitemap() -> bool:
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    try:
        root = ET.parse("sitemap.xml").getroot()
    except ET.ParseError as e:
        print(f"::error file=sitemap.xml::not well-formed: {e}")
        return False
    if root.tag != f"{ns}urlset":
        print(f"::error file=sitemap.xml::the root is {root.tag}, not a sitemaps.org urlset")
        return False
    ok = True
    urls = root.findall(f"{ns}url")
    if not urls:
        print("::error file=sitemap.xml::no <url> entries")
        ok = False
    for url in urls:
        loc = (url.findtext(f"{ns}loc") or "").strip()
        lastmod = (url.findtext(f"{ns}lastmod") or "").strip()
        if not loc.startswith(SITE):
            print(f"::error file=sitemap.xml::<loc> {loc!r} is not under {SITE}")
            ok = False
        if lastmod and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", lastmod):
            print(f"::error file=sitemap.xml::<lastmod> {lastmod!r} is not YYYY-MM-DD")
            ok = False
    print(f"sitemap: {len(urls)} url(s)")
    return ok


if __name__ == "__main__":
    checks = {"i18n": check_i18n, "sitemap": check_sitemap}
    if len(sys.argv) != 2 or sys.argv[1] not in checks:
        sys.exit(f"usage: {sys.argv[0]} {{{'|'.join(checks)}}}")
    sys.exit(0 if checks[sys.argv[1]]() else 1)
