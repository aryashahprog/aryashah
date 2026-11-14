# aryashah

Arya Shah's personal website. A small static site: Markdown content, Jinja templates, one stylesheet, no JavaScript or web fonts.

Unpublished first version. Nothing here deploys automatically.

## Editing content

All writing lives in `content/` as Markdown with a short YAML header.

- `content/home.md`: the bio on the home page (the email line is added by `templates/home.html`).
- `content/theses/_index.md`: the intro to Working theses and the order of the three themes.
- `content/theses/<slug>.md`: one note per thesis. The file name is the URL (`/theses/<slug>/`). `replaces: [old-slug, ...]` writes a redirect page at each old URL.
- `archive/theses/`: the original 12 notes before they were combined. Not built.
  - `theme` must match one of the themes in `_index.md`; `order` sorts notes within a theme.
  - `updated` is the last-updated date shown on the page. Change it when you revise a note.
  - `related` lists other note slugs to link at the bottom.
  - `sources` (optional) is a list of `{title, url}`, listed at the end of the note.
- `content/building/<slug>.md`: one entry per project, with `role`, optional `status` and `links`.
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
.venv/bin/python scripts/check.py  # internal links, anchors, nav, mailto, old thesis URLs redirect to live notes, 250 to 450 words per note, no em dashes
.venv/bin/ruff check . && .venv/bin/ruff format --check .
```

`dist/` is plain static files, so any static host (GitHub Pages, Netlify, Cloudflare Pages) can serve it later. The site sets `noindex` until it is published on purpose.

## Type

The system sans-serif stack at 16px, so there are no font files to load.
