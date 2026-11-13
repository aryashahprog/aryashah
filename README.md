# aryashah-site

Arya Shah's personal website. A small static site: Markdown content, Jinja templates, one stylesheet, no JavaScript.

Unpublished first version. Nothing here deploys automatically.

## Editing content

All writing lives in `content/` as Markdown with a short YAML header.

- `content/home.md`: the bio on the home page.
- `content/theses/_index.md`: the intro to Working theses and the order of the four themes.
- `content/theses/<slug>.md`: one note per thesis. The file name is the URL (`/theses/<slug>/`).
  - `theme` must match one of the themes in `_index.md`; `order` sorts notes within a theme.
  - `featured: 1|2|3` puts a note on the home page in that position.
  - `updated` is the last-updated date shown on the page. Change it when you revise a note.
  - `related` lists other note slugs to link at the bottom.
  - `sources` (optional) is a list of `{title, url}`. Without it, the page says no outside evidence has been added.
- `content/building/<slug>.md`: one entry per project, with `role`, optional `status` and `links`.

Write plain text; no em dashes (the check below flags them).

## Build and preview

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
.venv/bin/python build.py          # writes dist/
.venv/bin/python serve.py          # http://127.0.0.1:8080
```

## Checks

```bash
.venv/bin/python scripts/check.py  # internal links, anchors, nav, mailto, required thesis sections, no em dashes
.venv/bin/ruff check . && .venv/bin/ruff format --check .
```

`dist/` is plain static files, so any static host (GitHub Pages, Netlify, Cloudflare Pages) can serve it later. The site sets `noindex` until it is published on purpose.

## Font

Source Serif 4 by Adobe, self-hosted under the SIL Open Font License (`static/fonts/OFL.txt`).
