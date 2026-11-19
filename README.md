# aryashah

Arya Shah's personal website. A small static site: Markdown content, Jinja templates, one stylesheet, and lightweight scripts for video playback and privacy-conscious analytics. No web fonts.

Published at https://aryashah0.com. Changes pushed to `main` deploy automatically through GitHub Pages.

## Editing content

All writing lives in `content/` as Markdown with a short YAML header.

- `content/home.md`: the bio and experience rows on the home page (the contact button is added by `templates/home.html`).
- `content/theses/_index.md`: the intro to Working theses and the order of the three themes.
- `content/theses/<slug>.md`: one note per thesis. The file name is the URL (`/theses/<slug>/`). `replaces: [old-slug, ...]` writes a redirect page at each old URL.
- `archive/theses/`: the original 12 notes before they were combined. Not built.
  - `theme` must match one of the themes in `_index.md`; `order` sorts notes within a theme.
  - `updated` is retained as content metadata but is not displayed. Change it when you revise a note. Draft status is also hidden; reading time is generated automatically.
  - `related` lists other note slugs to link at the bottom.
  - `sources` (optional) is a list of `{title, url}`, listed at the end of the note.
- `content/building/<slug>.md`: one entry per project, with `role`, optional `status` and `links`. The Building page is currently unpublished; set `SHOW_BUILDING = True` in `build.py` to restore it and its nav link.
- `content/research/<slug>.md`: a short research landing page at `/research/<slug>/` linking the `poster` PDF in `static/research/`. Not in the nav; linked from Home.
- `review/`: work held back from the site until scientific and coauthor review is done. `build.py` only copies `static/`, so nothing here is served, but the repository is public, so it is still publicly readable (and was in earlier public commits).
  - `review/papers/<slug>.md`: source for the paper PDF (figures in `review/papers/figures/`). Regenerate with `.venv/bin/python scripts/make_pdf.py` (needs Chrome or `playwright install chromium`); the PDF is written beside the source.
  - `review/research-review.md`: open questions for the authors.

Write plain text; no em dashes (the check below flags them).

## Build and preview

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
.venv/bin/python build.py          # writes dist/
.venv/bin/python serve.py          # http://127.0.0.1:8080
```

## Checks

```bash
.venv/bin/python scripts/check.py  # internal links, anchors, nav, mailto, old thesis URLs redirect to live notes, word limits, no em dashes
.venv/bin/ruff check . && .venv/bin/ruff format --check .
```

Theses default to 250–450 prose words, excluding figures and footnotes. A longer essay can set `word_limit` in its front matter while retaining the minimum length and all other checks.

`dist/` is plain static files, so any static host (GitHub Pages, Netlify, Cloudflare Pages) can serve it later. It is published to GitHub Pages at https://aryashah0.com from `main` by `.github/workflows/pages.yml`; `static/CNAME` holds the custom domain. Use `--base` only when previewing under a subdirectory. Old thesis URLs are `noindex` redirect pages.

## Type

Responsive system sans-serif typography, with a narrow reading column for theses. There are no font files to load.

## Sharing and discovery

Every published page has its own canonical URL, Open Graph and X/Twitter metadata, and a shared 1200×630 preview image in `static/social-preview.png` showing only “Arya Shah.” The homepage's sharing title and description are name-only; other pages use their page titles and descriptions. The image URL is versioned to refresh image caches when crawlers fetch the new metadata.

The build generates `sitemap.xml` from published canonical pages and `robots.txt` pointing to it. Redirects, the 404 page and unpublished Building content are excluded from the sitemap. `scripts/check.py` validates these files, social metadata, and internal-link arrows.

## Analytics

Set `GOATCOUNTER_CODE` in `build.py` to the hosted GoatCounter site code. An empty code disables analytics. The dashboard is `https://<site-code>.goatcounter.com`; filter page paths to `/theses/` to compare thesis pageviews by title. A pageview is not proof that an article was read to completion.

The integration uses GoatCounter's [documented counting endpoint](https://www.goatcounter.com/help/pixel), without loading third-party JavaScript. It sends only the page path and title, plus a random cache-buster; it omits query strings, fragments, referrers, screen dimensions, and cookies. Requests still disclose the standard network headers and IP address to GoatCounter; see its [privacy policy](https://www.goatcounter.com/help/privacy).

Only visible pages on the production HTTPS hostname (or its `www` alias) are counted. Local and hosted previews, redirects, the 404 page, embedded frames, automated browsers, Do Not Track, and Global Privacy Control are excluded. Blocked analytics never prevents reading or navigation. No cookies or browser storage are created, and no no-JavaScript tracking fallback bypasses privacy preferences.
