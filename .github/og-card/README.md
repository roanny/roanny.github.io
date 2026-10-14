# The social card

`card.html` is the source of `og-image-2.jpg`, the 1200×630 card that LinkedIn, WhatsApp and X show for https://roanny.github.io/. It is a self-contained page at exactly 1200×630: the site's palette and logo written in place, and the three typefaces loaded from Google Fonts with `display=block`, so the screenshot waits for them. A new card is an edit of this file and a re-render, not a rebuild.

## Rendering

From the root of the checkout, with Google Chrome and ImageMagick installed and network access to Google Fonts:

```bash
cd .github/og-card
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --hide-scrollbars \
  --virtual-time-budget=8000 --window-size=1200,630 \
  --screenshot="$PWD/card.png" "file://$PWD/card.html"
magick card.png -quality 86 -sampling-factor 4:2:0 -strip card.jpg
magick identify card.jpg   # JPEG 1200x630
```

`card.png` and `card.jpg` are ignored by git; the card the site serves is the copy at the root. On 2026-10-14, Google Chrome 155.0.8059.41 and ImageMagick 7.1.2-33 on macOS rendered a `card.jpg` byte-identical to `og-image-2.jpg`. Another version of either, or a change to the fonts Google serves, can move pixels without changing the design.

## Publishing a new card

1. Edit `card.html`, render it, and look at `card.jpg`.
2. Copy it to the root under the next filename, `og-image-3.jpg`, and remove the old card: LinkedIn, WhatsApp and X cache a card by its URL, so a new card never reuses a filename.
3. Point the three references in `index.html` at it (`og:image`, `twitter:image`, the JSON-LD `image`), and update the filename in `AGENTS.md`, `README.md` and this file.
4. Once it is live, refetch it in LinkedIn's Post Inspector (https://www.linkedin.com/post-inspector/) with https://roanny.github.io/.

The card carries the operator's name and profile, which the root `README.md` § License leaves unlicensed, like the page itself.
